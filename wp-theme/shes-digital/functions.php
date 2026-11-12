<?php
if ( ! defined( 'ABSPATH' ) ) exit;

/* -------------------------------------------------------
 * Configuración básica del tema
 * ----------------------------------------------------- */
function sd_theme_setup(): void {
    add_theme_support( 'title-tag' );
    add_theme_support( 'post-thumbnails' );
    register_nav_menus( [
        'primary' => 'Menú principal',
        'footer'  => 'Menú pie de página',
    ] );
}
add_action( 'after_setup_theme', 'sd_theme_setup' );

/* -------------------------------------------------------
 * Limpiar <head> de salidas innecesarias de WordPress
 * ----------------------------------------------------- */
remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
remove_action( 'admin_print_scripts', 'print_emoji_detection_script' );
remove_action( 'wp_print_styles', 'print_emoji_styles' );
remove_action( 'admin_print_styles', 'print_emoji_styles' );
remove_action( 'wp_head', 'wp_generator' );
remove_action( 'wp_head', 'wlwmanifest_link' );
remove_action( 'wp_head', 'rsd_link' );
remove_action( 'wp_head', 'wp_shortlink_wp_head' );

// Fuentes locales en /assets/fonts/ — no se necesitan hints a Google Fonts
add_filter( 'wp_resource_hints', 'sd_remove_gfonts_hints', 10, 2 );
function sd_remove_gfonts_hints( array $hints, string $type ): array {
    if ( in_array( $type, [ 'preconnect', 'dns-prefetch' ], true ) ) {
        return array_filter( $hints, static function ( $h ) {
            $url = is_array( $h ) ? ( $h['href'] ?? '' ) : $h;
            return ! str_contains( $url, 'fonts.gstatic.com' )
                && ! str_contains( $url, 'fonts.googleapis.com' );
        } );
    }
    return $hints;
}

/* -------------------------------------------------------
 * Meta SEO personalizados (_shes_meta_title / _shes_meta_desc)
 * Visibles en el editor REST (panel de bloque lateral)
 * ----------------------------------------------------- */
function sd_register_meta(): void {
    $opts = [
        'show_in_rest'  => true,
        'single'        => true,
        'type'          => 'string',
        'auth_callback' => static fn() => current_user_can( 'edit_posts' ),
    ];
    register_post_meta( 'page', '_shes_meta_title', $opts );
    register_post_meta( 'page', '_shes_meta_desc',  $opts );
}
add_action( 'init', 'sd_register_meta' );

/* -------------------------------------------------------
 * Scripts para la plantilla "Página con bloques" (page-bloques.php)
 * Se cargan SOLO cuando esa plantilla está activa.
 * Los archivos viven en /assets/ en la raíz del dominio,
 * fuera del directorio del tema, igual que en la web estática.
 * ----------------------------------------------------- */
function sd_enqueue_bloques(): void {
    if ( ! is_page_template( 'page-bloques.php' ) ) {
        return;
    }

    $home = home_url( '/' );
    $v    = '20261109';

    wp_enqueue_style( 'sd-v2', $home . 'assets/css/v2.css', [], $v );
    wp_enqueue_style( 'sd-blocks', get_stylesheet_directory_uri() . '/blocks.css', [ 'sd-v2' ], '1.0.0' );

    // GSAP + Lenis (encadenados por dependencias)
    $prev = [];
    foreach ( [ 'sd-gsap' => 'gsap.min.js', 'sd-scrolltrigger' => 'ScrollTrigger.min.js', 'sd-lenis' => 'lenis.min.js' ] as $handle => $file ) {
        wp_enqueue_script( $handle, $home . 'assets/js/' . $file, $prev, $v, [ 'strategy' => 'defer', 'in_footer' => true ] );
        $prev = [ $handle ];
    }

    // bloques-attrs.js — inyecta data-* antes de que main.js los lea
    wp_enqueue_script(
        'sd-bloques-attrs',
        get_stylesheet_directory_uri() . '/assets/js/bloques-attrs.js',
        $prev,
        '1.0.0',
        [ 'strategy' => 'defer', 'in_footer' => true ]
    );
    $prev = [ 'sd-bloques-attrs' ];

    // main.js y cookies.js dependen de sd-bloques-attrs
    foreach ( [ 'sd-main' => 'main.js', 'sd-cookies' => 'cookies.js' ] as $handle => $file ) {
        wp_enqueue_script( $handle, $home . 'assets/js/' . $file, $prev, $v, [ 'strategy' => 'defer', 'in_footer' => true ] );
        $prev = [ $handle ];
    }
}
add_action( 'wp_enqueue_scripts', 'sd_enqueue_bloques' );

require_once get_template_directory() . '/inc/textos-panel.php';

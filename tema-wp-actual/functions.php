<?php
if ( ! defined( 'ABSPATH' ) ) exit;

/**
 * She's Digital — Divi Child Theme
 * Carga los estilos del parent (Divi) + los estilos de marca
 */
function sd_divi_child_enqueue() {

    // 1. Parent theme styles (Divi)
    wp_enqueue_style(
        'divi-parent-style',
        get_template_directory_uri() . '/style.css'
    );

    // 2. Google Fonts — Funnel Display + DM Sans
    wp_enqueue_style(
        'sd-fonts',
        'https://fonts.googleapis.com/css2?family=Funnel+Display:wght@300;400;500;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap',
        [],
        null
    );

    // 3. Child theme styles (style.css — cargado después de Divi)
    wp_enqueue_style(
        'sd-child-style',
        get_stylesheet_uri(),
        [ 'divi-parent-style', 'sd-fonts' ],
        '1.0.0'
    );

    // 4. JS de animaciones
    wp_enqueue_script(
        'sd-animations',
        get_stylesheet_directory_uri() . '/assets/js/animations.js',
        [],
        '1.0.0',
        true
    );
}
add_action( 'wp_enqueue_scripts', 'sd_divi_child_enqueue' );

/**
 * Registra las fuentes en el editor visual de Divi
 * para que aparezcan en el selector de tipografía
 */
function sd_divi_custom_fonts( $fonts ) {
    $fonts['Funnel Display'] = [
        'styles'  => '300,400,500,600,700,800',
        'subset'  => 'latin,latin-ext',
    ];
    $fonts['DM Sans'] = [
        'styles'  => '300,400,500',
        'subset'  => 'latin',
    ];
    return $fonts;
}
add_filter( 'et_google_fonts', 'sd_divi_custom_fonts' );

/**
 * Colores de marca en la paleta de colores de Divi Builder
 */
function sd_divi_color_palette() {
    return [
        '#1E2420', // dark
        '#7CBCAD', // mint-deep
        '#C8E8E0', // mint
        '#F0D4D4', // rose
        '#F8EEBB', // butter
        '#EDE0CC', // beige-warm
        '#4A5045', // text-mid
        '#FAFAF6', // background
    ];
}
add_filter( 'et_pb_color_palette', 'sd_divi_color_palette' );

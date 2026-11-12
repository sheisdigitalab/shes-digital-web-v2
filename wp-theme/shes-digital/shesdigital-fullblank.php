<?php
/**
 * Template Name: shesdigital-fullblank
 *
 * Plantilla para las 49 páginas estáticas migradas desde la web de She is Digital Lab.
 * El post_content de cada página contiene el HTML completo (nav, main, footer incluidos),
 * tal como lo generó el script de migración. Esta plantilla se limita a envolverlo
 * en un documento HTML válido con los meta SEO correctos.
 */
if ( ! defined( 'ABSPATH' ) ) exit;

$pid   = get_the_ID();
$title = get_post_meta( $pid, '_shes_meta_title', true ) ?: get_the_title();
$desc  = get_post_meta( $pid, '_shes_meta_desc',  true ) ?: '';
$url   = get_permalink( $pid );
$home  = home_url( '/' );
?><!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title><?= esc_html( $title ) ?></title>
<?php if ( $desc ) : ?>
<meta name="description" content="<?= esc_attr( $desc ) ?>">
<?php endif; ?>
<link rel="canonical" href="<?= esc_url( $url ) ?>">
<meta property="og:url"   content="<?= esc_url( $url ) ?>">
<meta property="og:title" content="<?= esc_attr( $title ) ?>">
<?php if ( $desc ) : ?>
<meta property="og:description" content="<?= esc_attr( $desc ) ?>">
<?php endif; ?>
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<?php
// Desactivar wpautop y wptexturize para preservar el HTML estático tal cual.
remove_filter( 'the_content', 'wpautop',     10 );
remove_filter( 'the_content', 'wptexturize', 10 );

if ( have_posts() ) :
    while ( have_posts() ) :
        the_post();
        the_content();
    endwhile;
endif;
?>
<?php wp_footer(); ?>
</body>
</html>

<?php
/**
 * Panel «Textos de la web» — Settings API
 * Incluido desde functions.php con require_once.
 */
if ( ! defined( 'ABSPATH' ) ) exit;

/* -------------------------------------------------------
 * Campos que admiten HTML (se sanitizan con wp_kses_post)
 * ----------------------------------------------------- */
define( 'SD_TEXTOS_HTML_FIELDS', [
    'hero_lead',
    'serv_title',
    'work_title',
    'reviews_title',
    'about_title',
    'about_p2',
    'process_title',
    'faq_title',
    'contact_title',
    'faq_a_1',  'faq_a_2',  'faq_a_3',  'faq_a_4',  'faq_a_5',
    'faq_a_6',  'faq_a_7',  'faq_a_8',  'faq_a_9',  'faq_a_10',
    'faq_a_11', 'faq_a_12', 'faq_a_13',
] );

/* -------------------------------------------------------
 * Valores por defecto (reflejan index.html tal cual)
 * ----------------------------------------------------- */
function sd_textos_defaults(): array {
    return [
        // SEO
        'meta_title'            => "She's Digital · Diseño web para negocios en Barcelona",
        'meta_desc'             => 'Diseño web para negocios en Barcelona. Webs que te traen clientes, para pymes y negocios locales. Precio cerrado desde 450 €.',
        'contact_phone_intl'    => '+34637889942',

        // Hero
        'hero_eyebrow'          => 'Disponible para nuevos proyectos',
        'hero_h1_sronly'        => 'Tu web a medida: que vende, destaca y convierte.',
        'hero_rotor_1'          => 'que vende.',
        'hero_rotor_2'          => 'que destaca.',
        'hero_rotor_3'          => 'que convierte.',
        'hero_rotor_4'          => 'a medida.',
        'hero_lead'             => 'Webs que te traen clientes, para <strong>negocios locales y pymes</strong>. Lista desde <strong>1 semana</strong> y con precio cerrado desde <strong>450 €</strong>.',
        'hero_btn1_text'        => 'Pide tu presupuesto gratis',
        'hero_btn1_href'        => '#contacto',
        'hero_btn2_text'        => 'Ver proyectos',
        'hero_btn2_href'        => '#proyectos',
        'hero_sub'              => 'Te respondo en menos de 24 h',
        'hero_founder'          => 'Llevo tu proyecto de principio a fin y soy tu único contacto. Cuando el proyecto lo pide, me apoyo en profesionales de confianza en SEO, redes y diseño.',

        // Servicios
        'serv_eyebrow'          => '01 — Servicios',
        'serv_title'            => 'Todo lo que tu negocio necesita online, <em>con precio cerrado y trato directo.</em>',
        'precio_landing'        => '450 €',
        'precio_web_completa'   => '790 €',
        'precio_ecommerce'      => '1.190 €',
        'precio_seo'            => '190 €',
        'precio_branding'       => '490 €',
        'precio_redes'          => '250 €',

        // Proyectos
        'work_eyebrow'          => '02 — Proyectos',
        'work_title'            => 'Webs para negocios <em>de verdad.</em>',
        'work_lead'             => '¿Qué tipo de negocio tienes? Elige tu sector y mira cómo podría quedar tu web.',

        // Reseñas
        'reviews_eyebrow'       => '03 — Reseñas',
        'reviews_title'         => 'Lo que dicen <br><em>mis clientes.</em>',

        // Sobre mí
        'about_eyebrow'         => '04 — Sobre mí',
        'about_title'           => 'Hola, soy Jenifer. <br><em>Diseño y código con criterio.</em>',
        'about_p1'              => 'Llevo cada proyecto de principio a fin y soy tu contacto en todo momento: te escucho, te propongo y desarrollo tu web.',
        'about_p2'              => 'Cuando el proyecto lo pide, me apoyo en profesionales de confianza en <strong>SEO, redes y diseño</strong>. Tú tienes el trato directo de trabajar con una persona, sin intermediarios ni pasos de mano en mano.',
        'about_p3'              => 'Sin intermediarios, sin pasar de mano en mano, y sin sorpresas en el precio.',

        // Proceso
        'process_eyebrow'       => '05 — Proceso',
        'process_title'         => 'Un proceso claro, <br><em>sin sorpresas.</em>',

        // FAQ
        'faq_eyebrow'           => '06 — FAQ',
        'faq_title'             => 'Las preguntas <br><em>más frecuentes.</em>',
        'faq_q_1'               => '¿Qué incluye el precio? ¿El dominio y el hosting van aparte?',
        'faq_a_1'               => 'El precio incluye el diseño, el desarrollo, los textos ajustados para Google y la puesta en marcha. El dominio y el hosting van aparte y quedan a tu nombre; te ayudo a contratarlos. Antes de empezar te paso un presupuesto cerrado con todo detallado.',
        'faq_q_2'               => '¿Tendré que pagar algo cada mes?',
        'faq_a_2'               => 'Solo si quieres. La web es tuya y puede funcionar sin cuotas. El mantenimiento es opcional, a medida y sin permanencia.',
        'faq_q_3'               => '¿Cuánto tarda en estar lista mi web?',
        'faq_a_3'               => 'La landing básica está lista en <strong>1 semana</strong>. Una web de varias páginas con branding ronda las <strong>3-5 semanas</strong>. Te doy fechas exactas en el presupuesto, sin promesas vacías.',
        'faq_q_4'               => '¿Lo haces todo tú?',
        'faq_a_4'               => 'Yo llevo y desarrollo cada proyecto, y soy tu contacto principal. Para el diseño, el SEO y las redes sociales cuento con profesionales senior de confianza, así que cada parte la hace quien mejor la sabe hacer.',
        'faq_q_5'               => '¿Trabajas con clientes fuera de Barcelona?',
        'faq_a_5'               => 'Sí, trabajo en remoto para toda España. Hacemos videollamadas siempre que haga falta: el trato directo no cambia con la distancia.',
        'faq_q_6'               => '¿Qué pasa si no me gusta el diseño?',
        'faq_a_6'               => 'Validamos el diseño antes de programar nada, con <strong>2 rondas de cambios</strong> incluidas para ajustarlo. Si después necesitas más, te las presupuesto aparte, sin sorpresas.',
        'faq_q_7'               => '¿Podré editar la web después?',
        'faq_a_7'               => 'Por supuesto. Con WordPress podrás cambiar textos e imágenes con facilidad, y te dejo un vídeo tutorial personalizado para tu web. Si va sin CMS, los cambios te los hago yo.',
        'faq_q_8'               => '¿Qué pasa después del lanzamiento?',
        'faq_a_8'               => 'Después del lanzamiento sigo contigo. Te enseño a usarla en una videollamada y durante el primer mes te resuelvo dudas y arreglo cualquier error sin coste. Después, si quieres despreocuparte, te preparo un plan de mantenimiento a medida, sin permanencia.',
        'faq_q_9'               => '¿WordPress o web a medida? ¿Qué me conviene?',
        'faq_a_9'               => 'Depende de cómo vayas a usarla. WordPress te deja cambiar textos e imágenes desde un panel. Una web sin CMS es más rápida y segura, y los cambios me los pides a mí. Te lo explico con calma en este artículo: <a href="/blog/wordpress-o-web-a-medida/">¿WordPress o web a medida?</a>',
        'faq_q_10'              => '¿De quién es la web cuando termines?',
        'faq_a_10'              => 'Tuya al <strong>100 %</strong>: dominio a tu nombre, hosting en tu cuenta y el código es de tu propiedad. Sin permanencias ni dependencias raras.',
        'faq_q_11'              => '¿Cómo se paga?',
        'faq_a_11'              => '50 % al firmar el presupuesto y 50 % al lanzar. Acepto transferencia, Bizum o tarjeta.',
        'faq_q_12'              => '',
        'faq_a_12'              => '',
        'faq_q_13'              => '',
        'faq_a_13'              => '',

        // Contacto
        'contact_eyebrow'       => '07 — Contacto',
        'contact_title'         => 'Cuéntame <br><em>tu proyecto.</em>',
        'contact_lead'          => 'Escríbeme por el formulario o directamente. Te respondo en menos de 24 h.',
        'wa_number'             => '34637889942',
        'contact_phone_display' => '+34 637 889 942',
        'contact_email'         => 'hola@sheisdigitalab.com',
        'contact_location'      => 'Barcelona · en remoto a todas partes',
    ];
}

/* -------------------------------------------------------
 * Sanitización
 * ----------------------------------------------------- */
function sd_sanitize_textos( $input ): array {
    $defaults = sd_textos_defaults();
    $output   = [];

    foreach ( $defaults as $key => $default_val ) {
        $raw = isset( $input[ $key ] ) ? (string) $input[ $key ] : '';
        if ( '' === trim( $raw ) ) {
            $output[ $key ] = $default_val;
            continue;
        }
        $output[ $key ] = in_array( $key, SD_TEXTOS_HTML_FIELDS, true )
            ? wp_kses_post( $raw )
            : sanitize_text_field( $raw );
    }

    return $output;
}

/* -------------------------------------------------------
 * Registro Settings API
 * ----------------------------------------------------- */
add_action( 'admin_init', function () {
    register_setting( 'sd_textos', 'sd_textos', [
        'sanitize_callback' => 'sd_sanitize_textos',
        'default'           => sd_textos_defaults(),
    ] );
} );

/* -------------------------------------------------------
 * Menú de administración
 * ----------------------------------------------------- */
add_action( 'admin_menu', function () {
    add_menu_page(
        'Textos de la web',
        'Textos de la web',
        'manage_options',
        'sd-textos',
        'sd_textos_page',
        'dashicons-edit-page',
        30
    );
} );

/* -------------------------------------------------------
 * Render del panel
 * ----------------------------------------------------- */
function sd_textos_page(): void {
    if ( ! current_user_can( 'manage_options' ) ) return;

    $opts = wp_parse_args( (array) get_option( 'sd_textos', [] ), sd_textos_defaults() );
    ?>
    <div class="wrap">
    <h1>Textos de la web</h1>
    <form method="post" action="options.php">
    <?php settings_fields( 'sd_textos' ); ?>

    <h2>SEO</h2>
    <table class="form-table"><tbody>
      <tr><th><label for="sd_meta_title">Title de la página</label></th>
        <td><input type="text" name="sd_textos[meta_title]" id="sd_meta_title"
            value="<?= esc_attr( $opts['meta_title'] ) ?>" class="large-text">
          <p class="description">Recomendado: 50-60 caracteres. Aparece en Google y en la pestaña.</p></td></tr>
      <tr><th><label for="sd_meta_desc">Meta descripción</label></th>
        <td><textarea name="sd_textos[meta_desc]" id="sd_meta_desc" rows="2" class="large-text"><?= esc_textarea( $opts['meta_desc'] ) ?></textarea>
          <p class="description">Recomendado: 150-160 caracteres.</p></td></tr>
      <tr><th><label for="sd_contact_phone_intl">Teléfono en JSON-LD (tel: href)</label></th>
        <td><input type="text" name="sd_textos[contact_phone_intl]" id="sd_contact_phone_intl"
            value="<?= esc_attr( $opts['contact_phone_intl'] ) ?>" class="regular-text">
          <p class="description">Con + y sin espacios. Ej: +34637889942</p></td></tr>
    </tbody></table>

    <h2>Hero</h2>
    <table class="form-table"><tbody>
      <tr><th><label for="sd_hero_eyebrow">Etiqueta superior</label></th>
        <td><input type="text" name="sd_textos[hero_eyebrow]" id="sd_hero_eyebrow"
            value="<?= esc_attr( $opts['hero_eyebrow'] ) ?>" class="large-text"></td></tr>
      <tr><th><label for="sd_hero_h1_sronly">H1 accesible (solo lectores de pantalla)</label></th>
        <td><input type="text" name="sd_textos[hero_h1_sronly]" id="sd_hero_h1_sronly"
            value="<?= esc_attr( $opts['hero_h1_sronly'] ) ?>" class="large-text">
          <p class="description">No se ve visualmente. Versión completa del H1 animado.</p></td></tr>
      <tr><th>Palabras del rotor</th>
        <td>
          <?php foreach ( range( 1, 4 ) as $i ) : $k = "hero_rotor_{$i}"; ?>
          <input type="text" name="sd_textos[<?= $k ?>]" placeholder="Palabra <?= $i ?>"
            value="<?= esc_attr( $opts[ $k ] ) ?>" style="display:block;margin-bottom:4px;width:28ch">
          <?php endforeach; ?>
          <p class="description">Las 4 palabras que rotan bajo "Tu web".</p>
        </td></tr>
      <tr><th><label for="sd_hero_lead">Párrafo lead</label></th>
        <td><textarea name="sd_textos[hero_lead]" id="sd_hero_lead" rows="3" class="large-text"><?= esc_textarea( $opts['hero_lead'] ) ?></textarea>
          <p class="description">Permite &lt;strong&gt;.</p></td></tr>
      <tr><th>Botón principal</th>
        <td>
          <input type="text" name="sd_textos[hero_btn1_text]" placeholder="Texto"
            value="<?= esc_attr( $opts['hero_btn1_text'] ) ?>" style="width:30ch;display:block;margin-bottom:4px">
          <input type="text" name="sd_textos[hero_btn1_href]" placeholder="Enlace"
            value="<?= esc_attr( $opts['hero_btn1_href'] ) ?>" style="width:20ch">
        </td></tr>
      <tr><th>Botón secundario</th>
        <td>
          <input type="text" name="sd_textos[hero_btn2_text]" placeholder="Texto"
            value="<?= esc_attr( $opts['hero_btn2_text'] ) ?>" style="width:30ch;display:block;margin-bottom:4px">
          <input type="text" name="sd_textos[hero_btn2_href]" placeholder="Enlace"
            value="<?= esc_attr( $opts['hero_btn2_href'] ) ?>" style="width:20ch">
        </td></tr>
      <tr><th><label for="sd_hero_sub">Texto bajo los botones</label></th>
        <td><input type="text" name="sd_textos[hero_sub]" id="sd_hero_sub"
            value="<?= esc_attr( $opts['hero_sub'] ) ?>" class="large-text"></td></tr>
      <tr><th><label for="sd_hero_founder">Texto fundadora</label></th>
        <td><textarea name="sd_textos[hero_founder]" id="sd_hero_founder" rows="3" class="large-text"><?= esc_textarea( $opts['hero_founder'] ) ?></textarea></td></tr>
    </tbody></table>

    <h2>Servicios</h2>
    <table class="form-table"><tbody>
      <tr><th><label for="sd_serv_eyebrow">Etiqueta sección</label></th>
        <td><input type="text" name="sd_textos[serv_eyebrow]" id="sd_serv_eyebrow"
            value="<?= esc_attr( $opts['serv_eyebrow'] ) ?>" class="regular-text"></td></tr>
      <tr><th><label for="sd_serv_title">Título sección</label></th>
        <td><textarea name="sd_textos[serv_title]" id="sd_serv_title" rows="2" class="large-text"><?= esc_textarea( $opts['serv_title'] ) ?></textarea>
          <p class="description">Permite &lt;em&gt;.</p></td></tr>
      <tr><th>Precios «desde»</th>
        <td>
          <?php
          $precios = [
              'precio_landing'      => 'Landing page',
              'precio_web_completa' => 'Web completa',
              'precio_ecommerce'    => 'Tienda online',
              'precio_seo'          => 'SEO /mes',
              'precio_branding'     => 'Branding',
              'precio_redes'        => 'Redes /mes',
          ];
          foreach ( $precios as $pk => $plabel ) : ?>
          <span style="display:inline-flex;align-items:center;gap:6px;margin:0 16px 6px 0">
            <label for="sd_<?= $pk ?>" style="min-width:14ch"><?= esc_html( $plabel ) ?></label>
            <input type="text" name="sd_textos[<?= $pk ?>]" id="sd_<?= $pk ?>"
              value="<?= esc_attr( $opts[ $pk ] ) ?>" style="width:10ch">
          </span>
          <?php endforeach; ?>
        </td></tr>
    </tbody></table>

    <h2>Proyectos</h2>
    <table class="form-table"><tbody>
      <tr><th><label for="sd_work_eyebrow">Etiqueta sección</label></th>
        <td><input type="text" name="sd_textos[work_eyebrow]" id="sd_work_eyebrow"
            value="<?= esc_attr( $opts['work_eyebrow'] ) ?>" class="regular-text"></td></tr>
      <tr><th><label for="sd_work_title">Título sección</label></th>
        <td><textarea name="sd_textos[work_title]" id="sd_work_title" rows="2" class="large-text"><?= esc_textarea( $opts['work_title'] ) ?></textarea>
          <p class="description">Permite &lt;em&gt;.</p></td></tr>
      <tr><th><label for="sd_work_lead">Párrafo intro</label></th>
        <td><textarea name="sd_textos[work_lead]" id="sd_work_lead" rows="2" class="large-text"><?= esc_textarea( $opts['work_lead'] ) ?></textarea></td></tr>
    </tbody></table>

    <h2>Reseñas</h2>
    <table class="form-table"><tbody>
      <tr><th><label for="sd_reviews_eyebrow">Etiqueta sección</label></th>
        <td><input type="text" name="sd_textos[reviews_eyebrow]" id="sd_reviews_eyebrow"
            value="<?= esc_attr( $opts['reviews_eyebrow'] ) ?>" class="regular-text"></td></tr>
      <tr><th><label for="sd_reviews_title">Título sección</label></th>
        <td><textarea name="sd_textos[reviews_title]" id="sd_reviews_title" rows="2" class="large-text"><?= esc_textarea( $opts['reviews_title'] ) ?></textarea>
          <p class="description">Permite &lt;br&gt; y &lt;em&gt;.</p></td></tr>
    </tbody></table>

    <h2>Sobre mí</h2>
    <table class="form-table"><tbody>
      <tr><th><label for="sd_about_eyebrow">Etiqueta sección</label></th>
        <td><input type="text" name="sd_textos[about_eyebrow]" id="sd_about_eyebrow"
            value="<?= esc_attr( $opts['about_eyebrow'] ) ?>" class="regular-text"></td></tr>
      <tr><th><label for="sd_about_title">Título sección</label></th>
        <td><textarea name="sd_textos[about_title]" id="sd_about_title" rows="2" class="large-text"><?= esc_textarea( $opts['about_title'] ) ?></textarea>
          <p class="description">Permite &lt;br&gt; y &lt;em&gt;.</p></td></tr>
      <tr><th><label for="sd_about_p1">Párrafo 1</label></th>
        <td><textarea name="sd_textos[about_p1]" id="sd_about_p1" rows="2" class="large-text"><?= esc_textarea( $opts['about_p1'] ) ?></textarea></td></tr>
      <tr><th><label for="sd_about_p2">Párrafo 2</label></th>
        <td><textarea name="sd_textos[about_p2]" id="sd_about_p2" rows="3" class="large-text"><?= esc_textarea( $opts['about_p2'] ) ?></textarea>
          <p class="description">Permite &lt;strong&gt;.</p></td></tr>
      <tr><th><label for="sd_about_p3">Párrafo 3</label></th>
        <td><textarea name="sd_textos[about_p3]" id="sd_about_p3" rows="2" class="large-text"><?= esc_textarea( $opts['about_p3'] ) ?></textarea></td></tr>
    </tbody></table>

    <h2>Proceso</h2>
    <table class="form-table"><tbody>
      <tr><th><label for="sd_process_eyebrow">Etiqueta sección</label></th>
        <td><input type="text" name="sd_textos[process_eyebrow]" id="sd_process_eyebrow"
            value="<?= esc_attr( $opts['process_eyebrow'] ) ?>" class="regular-text"></td></tr>
      <tr><th><label for="sd_process_title">Título sección</label></th>
        <td><textarea name="sd_textos[process_title]" id="sd_process_title" rows="2" class="large-text"><?= esc_textarea( $opts['process_title'] ) ?></textarea>
          <p class="description">Permite &lt;br&gt; y &lt;em&gt;.</p></td></tr>
    </tbody></table>

    <h2>FAQ</h2>
    <table class="form-table"><tbody>
      <tr><th><label for="sd_faq_eyebrow">Etiqueta sección</label></th>
        <td><input type="text" name="sd_textos[faq_eyebrow]" id="sd_faq_eyebrow"
            value="<?= esc_attr( $opts['faq_eyebrow'] ) ?>" class="regular-text"></td></tr>
      <tr><th><label for="sd_faq_title">Título sección</label></th>
        <td><textarea name="sd_textos[faq_title]" id="sd_faq_title" rows="2" class="large-text"><?= esc_textarea( $opts['faq_title'] ) ?></textarea>
          <p class="description">Permite &lt;br&gt; y &lt;em&gt;.</p></td></tr>
    </tbody></table>

    <?php for ( $i = 1; $i <= 13; $i++ ) :
        $qk       = "faq_q_{$i}";
        $ak       = "faq_a_{$i}";
        $opcional = ( $i > 11 );
    ?>
    <h3><?= $opcional ? "Pregunta {$i} (opcional)" : "Pregunta {$i}" ?></h3>
    <table class="form-table"><tbody>
      <tr><th><label for="sd_<?= $qk ?>">Pregunta</label></th>
        <td><input type="text" name="sd_textos[<?= $qk ?>]" id="sd_<?= $qk ?>"
            value="<?= esc_attr( $opts[ $qk ] ) ?>" class="large-text"
            placeholder="<?= $opcional ? 'Deja vacío para no mostrar este bloque' : '' ?>"></td></tr>
      <tr><th><label for="sd_<?= $ak ?>">Respuesta</label></th>
        <td><textarea name="sd_textos[<?= $ak ?>]" id="sd_<?= $ak ?>" rows="3" class="large-text"
            placeholder="<?= $opcional ? 'Deja vacío para no mostrar este bloque' : '' ?>"><?= esc_textarea( $opts[ $ak ] ) ?></textarea>
          <p class="description">Permite &lt;strong&gt;, &lt;em&gt; y &lt;a&gt;.</p></td></tr>
    </tbody></table>
    <?php endfor; ?>

    <h2>Contacto</h2>
    <table class="form-table"><tbody>
      <tr><th><label for="sd_contact_eyebrow">Etiqueta sección</label></th>
        <td><input type="text" name="sd_textos[contact_eyebrow]" id="sd_contact_eyebrow"
            value="<?= esc_attr( $opts['contact_eyebrow'] ) ?>" class="regular-text"></td></tr>
      <tr><th><label for="sd_contact_title">Título sección</label></th>
        <td><textarea name="sd_textos[contact_title]" id="sd_contact_title" rows="2" class="large-text"><?= esc_textarea( $opts['contact_title'] ) ?></textarea>
          <p class="description">Permite &lt;br&gt; y &lt;em&gt;.</p></td></tr>
      <tr><th><label for="sd_contact_lead">Párrafo intro</label></th>
        <td><input type="text" name="sd_textos[contact_lead]" id="sd_contact_lead"
            value="<?= esc_attr( $opts['contact_lead'] ) ?>" class="large-text"></td></tr>
      <tr><th><label for="sd_wa_number">Número WhatsApp (wa.me)</label></th>
        <td><input type="text" name="sd_textos[wa_number]" id="sd_wa_number"
            value="<?= esc_attr( $opts['wa_number'] ) ?>" class="regular-text">
          <p class="description">Solo dígitos, sin +. Ej: 34637889942</p></td></tr>
      <tr><th><label for="sd_contact_phone_display">Teléfono visible</label></th>
        <td><input type="text" name="sd_textos[contact_phone_display]" id="sd_contact_phone_display"
            value="<?= esc_attr( $opts['contact_phone_display'] ) ?>" class="regular-text"></td></tr>
      <tr><th><label for="sd_contact_email">Email</label></th>
        <td><input type="text" name="sd_textos[contact_email]" id="sd_contact_email"
            value="<?= esc_attr( $opts['contact_email'] ) ?>" class="regular-text"></td></tr>
      <tr><th><label for="sd_contact_location">Ubicación</label></th>
        <td><input type="text" name="sd_textos[contact_location]" id="sd_contact_location"
            value="<?= esc_attr( $opts['contact_location'] ) ?>" class="large-text"></td></tr>
    </tbody></table>

    <?php submit_button( 'Guardar textos' ); ?>
    </form>
    </div>
    <?php
}

/* -------------------------------------------------------
 * Filtro the_content — reemplaza {{sd:key}} en la portada
 * Solo actúa en la página con ID 400.
 * ----------------------------------------------------- */
add_filter( 'the_content', function ( $content ) {
    if ( ! is_singular() || get_the_ID() !== 400 ) {
        return $content;
    }

    $defaults = sd_textos_defaults();
    $opts     = wp_parse_args( (array) get_option( 'sd_textos', [] ), $defaults );

    // Bloques opcionales FAQ 12 y 13 — eliminar el bloque si la pregunta está vacía
    foreach ( [ 12, 13 ] as $n ) {
        $q = trim( $opts[ "faq_q_{$n}" ] ?? '' );
        if ( '' === $q ) {
            $content = preg_replace(
                '/\{\{sd:faq_block_' . $n . '_start\}\}.*?\{\{sd:faq_block_' . $n . '_end\}\}/s',
                '',
                $content
            );
        } else {
            $content = str_replace( "{{sd:faq_block_{$n}_start}}", '', $content );
            $content = str_replace( "{{sd:faq_block_{$n}_end}}",   '', $content );
        }
    }

    // Reemplazar marcadores normales
    foreach ( $opts as $key => $val ) {
        $val     = ( '' !== trim( (string) $val ) ) ? $val : ( $defaults[ $key ] ?? '' );
        $escaped = in_array( $key, SD_TEXTOS_HTML_FIELDS, true )
            ? wp_kses_post( (string) $val )
            : esc_html( (string) $val );
        $content = str_replace( '{{sd:' . $key . '}}', $escaped, $content );
    }

    // Marcadores JSON-LD: texto plano sin HTML para el schema FAQPage
    foreach ( range( 1, 11 ) as $n ) {
        foreach ( [ 'q', 'a' ] as $t ) {
            $key   = "faq_{$t}_{$n}";
            $val   = $opts[ $key ] ?? $defaults[ $key ] ?? '';
            $plain = esc_js( wp_strip_all_tags( wp_kses_post( (string) $val ) ) );
            $content = str_replace( "{{sd:json_faq_{$t}_{$n}}}", $plain, $content );
        }
    }

    return $content;
}, 10 );

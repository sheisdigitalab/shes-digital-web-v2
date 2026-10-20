"""Genera las páginas de sectores en v2."""
import os, textwrap

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# ---------------------------------------------------------------------------
# Datos por sector
# ---------------------------------------------------------------------------
SECTORES = [
    {
        "slug": "autonomos",
        "title": "Diseño web para autónomos · Desde 450 € | She's Digital",
        "description": "Web profesional para coaches, consultores, abogados y terapeutas. Lista en 1 semana desde 450 €. Precio cerrado, sin sorpresas.",
        "og_title": "She's Digital · Web para autónomos",
        "crumb": "Autónomos",
        "eyebrow": "Sectores · Autónomos &amp; Profesionales liberales",
        "h1_line1": "Tu web profesional,",
        "h1_mark": "desde 450 €.",
        "lead": "Coaches, consultores, abogados, terapeutas. Una web que vende por ti, lista en 1 semana. Sin letra pequeña, sin tecnicismos.",
        "meta_desde": "450 € + IVA",
        "meta_entrega": "1 semana",
        "meta_k3": "EDITABLE",
        "meta_v3": "✓ Sí",
        "meta_k4": "PAGOS",
        "meta_v4": "50/50",
        "s1_eyebrow": "01",
        "s1_title": "Una web hecha para autónomos como tú.",
        "s1_body": """<p>No necesitas una agencia de 50 personas ni un proyecto de 10.000 €. Necesitas una web que te represente, que cargue rápido y que convierta visitas en llamadas. Eso es lo que hago.</p>
        <p>Trabajo en directo contigo, sin intermediarios. Una llamada de 30 min, un presupuesto cerrado y una web lista en 1 semana. Sin sorpresas en la factura.</p>""",
        "s2_eyebrow": "02",
        "s2_title": "Qué incluye la web.",
        "s2_items": [
            ("Diseño a medida", "Sin plantillas recicladas. Mockup en Figma con tus colores, tipografía y fotos antes de programar nada."),
            ("Web one-page con hasta 6 secciones", "Hero · sobre ti · servicios · proceso · testimonios · contacto. Justo lo necesario para vender."),
            ("Formulario y WhatsApp directo", "Formulario anti-spam + botón flotante de WhatsApp con tu número. Cero fricción para que te escriban."),
            ("SEO básico incluido", "Meta tags, schema Person + LocalBusiness, sitemap XML, Open Graph. Sin extras a posteriori."),
            ("Editable por ti", "Cambios de textos y fotos sin tocar código. Mini-vídeo personalizado de cómo editar tu web tras la entrega."),
            ("Mobile-first", "Tu cliente te busca desde el móvil. La diseño primero para móvil y la adapto a desktop. No al revés."),
        ],
        "s3_eyebrow": "03",
        "s3_title": "Trabajamos contigo si eres…",
        "s3_body": """<ul class="sv-fits">
          <li>Coach o terapeuta que quiere consultas online o presenciales</li>
          <li>Consultor/a independiente con servicios B2B definidos</li>
          <li>Abogado/a, gestor/a o asesor/a fiscal de zona</li>
          <li>Diseñador/a, fotógrafa, copywriter, traductora… cualquier oficio creativo</li>
          <li>Profesional liberal de cualquier sector que vende su tiempo y conocimiento</li>
        </ul>""",
        "cta_title": "¿Lista para tener tu mejor escaparate?",
        "cta_lead": "Tu web profesional puede estar lista en 7 días. Cuéntame qué necesitas.",
    },
    {
        "slug": "clinicas-y-salud",
        "title": "Diseño web para clínicas y salud · Desde 450 € | She's Digital",
        "description": "Webs para clínicas, fisios, dentistas y psicólogos en Barcelona. Reservas online, LOPD y SEO médico. Desde 450 €.",
        "og_title": "She's Digital · Web para clínicas y salud",
        "crumb": "Clínicas y Salud",
        "eyebrow": "Sectores · Clínicas, Fisios &amp; Salud",
        "h1_line1": "Webs para profesionales",
        "h1_mark": "de la salud.",
        "lead": "Clínicas, fisios, dentistas, osteópatas y psicólogos. Reservas online, blog SEO médico y cumplimiento LOPD. Desde 450 €.",
        "meta_desde": "450 € + IVA",
        "meta_entrega": "2-4 semanas",
        "meta_k3": "LOPD",
        "meta_v3": "✓ Cumple",
        "meta_k4": "CASO REAL",
        "meta_v4": "+120 leads B2B",
        "s1_eyebrow": "01",
        "s1_title": "Por qué tu consulta necesita web seria.",
        "s1_body": """<p>En salud, la confianza es todo. Tu web es la primera consulta, antes incluso de la videollamada o la primera visita. Si la web no transmite seriedad, no llegan al paso siguiente.</p>
        <p>Diseño webs sanitarias que cumplen LOPD desde el primer día, con páginas por especialidad, blog para captar pacientes vía Google («osteopatía cerca de mí», «fisio Barcelona») y reservas online integradas.</p>""",
        "s2_eyebrow": "02",
        "s2_title": "Qué incluye la web.",
        "s2_items": [
            ("Página por especialidad", "Una landing optimizada por cada servicio con SEO local específico."),
            ("Reservas online", "Integración con Doctoralia, Cita Previa, Reservi o sistema propio con confirmación email + recordatorio SMS."),
            ("Blog SEO médico", "Estructura para artículos divulgativos que rankean en Google. Atrae pacientes que buscan información sobre dolencias."),
            ("Cumplimiento LOPD", "Aviso legal médico, política de privacidad RGPD, gestión de consentimientos y formularios con cifrado."),
            ("Schema MedicalBusiness", "Datos estructurados Schema.org/MedicalClinic para que Google entienda que ofreces servicios sanitarios."),
            ("Diseño que transmite confianza", "Tipografía clara, fotos profesionales del equipo, testimonios reales y certificaciones visibles."),
        ],
        "s3_eyebrow": "03",
        "s3_title": "Caso real: Olia Workplace.",
        "s3_body": """<p>Olia es una osteópata que ofrece servicios B2B (osteopatía corporativa). Lanzó su web en 3 semanas y captó +120 leads B2B en 3 meses.</p>
        <p>Web bilingüe ES/CA con landing por servicio, formulario de propuesta para empresas y blog con artículos sobre ergonomía laboral.</p>
        <a href="../../proyectos/olia-workplace/" class="btn btn--line">Ver caso completo →</a>""",
        "cta_title": "¿Llenamos tu agenda de pacientes?",
        "cta_lead": "Cuéntame tu especialidad y te paso propuesta a medida en 24 h.",
    },
    {
        "slug": "restaurantes",
        "title": "Diseño web para restaurantes · Desde 450 € | She's Digital",
        "description": "Web profesional para restaurantes en Barcelona: menú online, reservas, SEO local y Google Maps. Desde 450 €.",
        "og_title": "She's Digital · Web para restaurantes",
        "crumb": "Restaurantes",
        "eyebrow": "Sectores · Restaurantes &amp; Hostelería",
        "h1_line1": "Webs para restaurantes",
        "h1_mark": "que llenan mesas.",
        "lead": "Web profesional + menú online + reservas + SEO local. Que te encuentren en Google Maps cuando alguien busca «restaurante cerca de mí». Desde 450 €.",
        "meta_desde": "450 € + IVA",
        "meta_entrega": "1-3 semanas",
        "meta_k3": "IDIOMAS",
        "meta_v3": "ES · CA · EN",
        "meta_k4": "RESERVAS",
        "meta_v4": "TheFork o propias",
        "s1_eyebrow": "01",
        "s1_title": "Por qué tu restaurante necesita web.",
        "s1_body": """<p>El 81 % de los comensales investiga online antes de elegir restaurante. Si tu web no carga rápido, no tiene menú visible o no enseña fotos reales, pierdes mesas antes incluso de que entren por la puerta.</p>
        <p>Google premia los restaurantes con web propia, schema markup específico (Restaurant + Menu) y reseñas gestionadas. Eso es lo que hago.</p>""",
        "s2_eyebrow": "02",
        "s2_title": "Qué incluye la web.",
        "s2_items": [
            ("Menú online editable", "Cambias platos, precios y disponibilidad desde el móvil. Sin llamarme cada vez que hay un cambio."),
            ("Reservas integradas", "Integración con TheFork, Mr. Booking, OpenTable, ResOS o sistema propio con calendario. Tú decides."),
            ("SEO local + Google Maps", "Schema Restaurant + Menu + LocalBusiness, Google Business Profile y citaciones para aparecer en el pack local."),
            ("Galería de fotos profesional", "Optimización de imágenes y lazy load para que la web cargue rápida incluso con muchas fotos."),
            ("Multiidioma", "ES + CA + EN si trabajas con turismo. WordPress con WPML o Polylang. Bien hecho desde el primer día."),
            ("Gestión de reseñas Google", "Sistema para responder reseñas en tu tono, automatizado pero personalizable."),
        ],
        "s3_eyebrow": "03",
        "s3_title": "Esta web encaja si tu restaurante es…",
        "s3_body": """<ul class="sv-fits">
          <li>Restaurante de barrio que quiere modernizar su presencia digital</li>
          <li>Bar de tapas, brunch o cafetería en zonas turísticas</li>
          <li>Cocina creativa, gastrobar o casa de comidas con identidad propia</li>
          <li>Negocio familiar con segunda generación que toma el relevo digital</li>
          <li>Grupo de restauración con varios locales que necesita web central</li>
        </ul>""",
        "cta_title": "¿Listo para llenar tu restaurante?",
        "cta_lead": "Cuéntame qué tipo de restaurante tienes y te paso presupuesto cerrado en 24 h.",
    },
    {
        "slug": "servicios-locales",
        "title": "Diseño web para negocios locales · SEO local | She's Digital",
        "description": "Web + SEO local para fontaneros, electricistas, taxis, cerrajeros y reformas. Aparece en Google Maps. Desde 450 €.",
        "og_title": "She's Digital · Web para servicios locales",
        "crumb": "Servicios Locales",
        "eyebrow": "Sectores · Servicios de Proximidad",
        "h1_line1": "Que te encuentren",
        "h1_mark": "cuando te buscan.",
        "lead": "Web + SEO local para fontaneros, electricistas, taxis, cerrajeros y reformas. Tu negocio en el pack local de Google. Desde 450 €.",
        "meta_desde": "450 € + IVA",
        "meta_entrega": "1-2 semanas",
        "meta_k3": "SEO LOCAL",
        "meta_v3": "✓ Incluido",
        "meta_k4": "CASO REAL",
        "meta_v4": "+248 % tráfico",
        "s1_eyebrow": "01",
        "s1_title": "El cliente busca «cerca de mí».",
        "s1_body": """<p>Cuando alguien tiene una fuga, necesita un taxi YA o quiere arreglar una persiana, no busca en redes sociales. Busca en Google: «fontanero cerca de mí», «taxi Lliçà», «reformas Barcelona». Si tu negocio no aparece, no existes.</p>
        <p>Diseño webs para servicios locales con SEO/GEO desde el día uno: Google Business Profile optimizado, schema LocalBusiness, citaciones, reseñas y contenido por zona.</p>""",
        "s2_eyebrow": "02",
        "s2_title": "Qué incluye la web.",
        "s2_items": [
            ("Web simple y directa", "Tu cliente necesita llamarte rápido. CTA claro: teléfono visible en todas las pantallas."),
            ("Google Business Profile", "Optimización completa de tu ficha en Google Maps. Categorías, atributos, fotos, horarios, servicios."),
            ("Páginas por zona", "Una landing por ciudad o barrio donde operes. Ranking long-tail para cada zona."),
            ("Estrategia de reseñas", "Sistema para captar reseñas reales de clientes satisfechos. Respuesta automática + personalizable."),
            ("WhatsApp / llamada directa", "Botón flotante de WhatsApp y teléfono click-to-call. Cero fricción para emergencias."),
            ("Schema LocalBusiness", "Datos estructurados que Google entiende: dirección, teléfono, horarios, zona de servicio."),
        ],
        "s3_eyebrow": "03",
        "s3_title": "Caso real: Taxi Santa Susanna.",
        "s3_body": """<p>Servicio de taxi local que pasó de invisible online a posicionarse #1 en «taxi Santa Susanna» con +248 % tráfico orgánico en 6 meses.</p>
        <p>Web con reservas online, tarifas transparentes, integración con Maps y SEO local agresivo. Hoy reciben llamadas directas desde Google Maps cada día.</p>
        <a href="../../proyectos/taxi-santa-susanna/" class="btn btn--line">Ver caso completo →</a>""",
        "cta_title": "Tu próximo cliente te está buscando ahora.",
        "cta_lead": "Cuéntame tu servicio y zona. Te paso presupuesto cerrado en 24 h.",
    },
]

# ---------------------------------------------------------------------------
# Template del sector (profundidad ../../)
# ---------------------------------------------------------------------------
SECTOR_TPL = """\
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <link rel="canonical" href="https://sheisdigitalab.com/sectores/{slug}/" />
  <meta property="og:title" content="{og_title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="../../assets/img/og-cover.jpg" />
  <meta property="og:type" content="website" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="theme-color" content="#FAF8F4" />
  <link rel="icon" href="../../assets/img/favicon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="/assets/fonts/fonts.css" />
  <link rel="stylesheet" href="../../assets/css/v2.css?v=17" />
  <link rel="stylesheet" href="../../assets/css/service.css" />
  <script>
    (function (d) {{
      var r = d.documentElement; r.classList.add('js');
      var manual = false;
      try {{ manual = localStorage.getItem('sd-motion') === 'reduce'; }} catch (e) {{}}
      if (manual) r.classList.add('reduce-motion');
      if (!manual && !matchMedia('(prefers-reduced-motion: reduce)').matches) {{
        r.classList.add('is-anim');
        setTimeout(function () {{ if (!window.gsap) r.classList.remove('is-anim'); }}, 3000);
      }}
    }})(document);
  </script>
</head>
<body class="service-page">
  <a class="skip" href="#main">Saltar al contenido</a>

  <header class="nav" data-nav>
    <div class="nav__inner wrap">
      <a href="../../" class="nav__logo" aria-label="She's Digital, inicio">
        <img src="../../assets/img/logo-stacked.svg" alt="" width="112" height="63" />
      </a>
      <nav class="nav__links" id="nav-menu" aria-label="Principal">
        <a href="../../#servicios">Servicios y precios</a>
        <a href="../../#proyectos">Proyectos</a>
        <a href="../../#proceso">Proceso</a>
        <a href="../../#sobre-mi">Sobre mí</a>
        <a href="../../#faq">FAQ</a>
        <a href="#contacto" class="btn btn--dark nav__cta-mobile">Pide tu presupuesto gratis <span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span></a>
      </nav>
      <a href="#contacto" class="btn btn--dark nav__cta">Pide tu presupuesto gratis <span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span></a>
      <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="nav-menu">
        <span class="sr-only">Abrir menú</span>
        <span class="nav__bars" aria-hidden="true"><i></i><i></i></span>
      </button>
    </div>
  </header>

  <main id="main">

    <section class="cs-hero sv-hero" id="top" aria-labelledby="sv-title">
      <div class="wrap">
        <nav class="sv-crumbs" aria-label="Ruta" data-hero="fade">
          <ol>
            <li><a href="../../">Inicio</a></li>
            <li><a href="../../sectores/">Sectores</a></li>
            <li aria-current="page">{crumb}</li>
          </ol>
        </nav>

        <p class="eyebrow" data-hero="fade">{eyebrow}</p>
        <h1 class="sv-title" id="sv-title">
          <span class="hero__line"><span class="hero__line-in" data-hero="line">{h1_line1}</span></span>
          <span class="hero__line"><span class="hero__line-in" data-hero="line"><span class="sv-mark">{h1_mark}</span></span></span>
        </h1>

        <div class="cs-hero__grid sv-hero__grid">
          <div>
            <p class="cs-hero__lead" data-hero="fade">{lead}</p>
            <div class="sv-actions" data-hero="fade">
              <a href="#contacto" class="btn btn--dark btn--magnetic">Pide tu presupuesto gratis <span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span></a>
              <a href="#incluye" class="btn btn--line">Ver qué incluye</a>
            </div>
          </div>

          <dl class="cs-meta" data-hero="fade">
            <div><dt>Desde</dt><dd>{meta_desde}</dd></div>
            <div><dt>Entrega</dt><dd>{meta_entrega}</dd></div>
            <div><dt>{meta_k3}</dt><dd>{meta_v3}</dd></div>
            <div><dt>{meta_k4}</dt><dd>{meta_v4}</dd></div>
          </dl>
        </div>
      </div>
    </section>

    <section class="section sv-section" id="por-que" aria-labelledby="porq-title" data-reveal>
      <div class="wrap sv-section__grid">
        <header>
          <p class="eyebrow">{s1_eyebrow}</p>
          <h2 class="h2" id="porq-title">{s1_title}</h2>
        </header>
        <div class="sv-prose">
          {s1_body}
        </div>
      </div>
    </section>

    <section class="section sv-section sv-section--alt" id="incluye" aria-labelledby="incl-title" data-reveal>
      <div class="wrap">
        <header class="sv-section__head">
          <p class="eyebrow">{s2_eyebrow}</p>
          <h2 class="h2" id="incl-title">{s2_title}</h2>
        </header>
        <ul class="sv-features">
          {s2_items_html}
        </ul>
      </div>
    </section>

    <section class="section sv-section" id="para-quien" aria-labelledby="paraq-title" data-reveal>
      <div class="wrap sv-section__grid">
        <header>
          <p class="eyebrow">{s3_eyebrow}</p>
          <h2 class="h2" id="paraq-title">{s3_title}</h2>
        </header>
        <div class="sv-prose">
          {s3_body}
        </div>
      </div>
    </section>

    <section class="section sv-cta" id="cta-mid" data-reveal>
      <div class="wrap sv-cta__inner">
        <h2 class="h2">{cta_title}</h2>
        <p>{cta_lead}</p>
        <a href="#contacto" class="btn btn--dark btn--magnetic">Pide tu presupuesto gratis <span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span></a>
      </div>
    </section>

    <section class="section contact" id="contacto" aria-labelledby="contact-title">
      <div class="wrap contact__grid">
        <div class="contact__intro">
          <p class="eyebrow" data-reveal>Contacto</p>
          <h2 class="h2" id="contact-title" data-split>Cuéntame<br /><em>tu proyecto.</em></h2>
          <p class="contact__lead" data-reveal>Escríbeme por el formulario o directamente. Te respondo el mismo día.</p>
          <ul class="contact__direct" data-reveal>
            <li><span>WhatsApp</span><a href="https://wa.me/34637889942">+34 637 889 942</a></li>
            <li><span>Email</span><a href="mailto:hola@sheisdigitalab.com">hola@sheisdigitalab.com</a></li>
            <li><span>Ubicación</span><p>Barcelona · en remoto a todas partes</p></li>
          </ul>
        </div>
        <form class="form" id="contact-form" method="post" novalidate data-reveal>
          <p class="form__note" id="form-note">Todos los campos son obligatorios.</p>
          <div class="field">
            <label for="f-name">¿Cómo te llamas?</label>
            <input id="f-name" name="name" type="text" autocomplete="name" required aria-describedby="f-name-err" />
            <p class="field__err" id="f-name-err" aria-live="polite"></p>
          </div>
          <div class="field">
            <label for="f-msg">Cuéntame tu proyecto</label>
            <textarea id="f-msg" name="message" rows="4" required aria-describedby="f-msg-err"></textarea>
            <p class="field__err" id="f-msg-err" aria-live="polite"></p>
          </div>
          <div class="field field--check">
            <input id="f-privacy" name="privacy" type="checkbox" required aria-describedby="f-privacy-err" />
            <label for="f-privacy">He leído y acepto la <a href="https://sheisdigitalab.com/legal/privacidad/">política de privacidad</a>.</label>
            <p class="field__err" id="f-privacy-err" aria-live="polite"></p>
          </div>
          <button type="submit" class="btn btn--dark btn--block">
            <span data-btn-label>Enviar por WhatsApp</span>
            <span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span>
          </button>
          <p class="form__wa-note">Se abrirá WhatsApp con tu mensaje listo para enviar.</p>
          <p class="form__status" role="status" aria-live="polite"></p>
        </form>
      </div>
    </section>

  </main>

  <footer class="footer">
    <div class="wrap">
      <div class="footer__cols">
        <div>
          <img src="../../assets/img/logo-stacked-light.svg" alt="She's Digital" width="150" height="84" loading="lazy" />
          <p>Diseño web, marca y marketing digital en Barcelona.<br />Web · Ecommerce · SEO · Branding · Redes · IA y apps a medida.</p>
        </div>
        <nav aria-label="Pie: servicios">
          <h3>Servicios</h3>
          <ul>
            <li><a href="../../servicios/branding/">Branding</a></li>
            <li><a href="../../servicios/diseno-web/">Diseño web</a></li>
            <li><a href="../../servicios/ecommerce/">Ecommerce</a></li>
            <li><a href="../../servicios/seo/seo-local/">SEO local</a></li>
            <li><a href="../../servicios/redes-sociales/">Redes sociales</a></li>
          </ul>
        </nav>
        <nav aria-label="Pie: sectores">
          <h3>Sectores</h3>
          <ul>
            <li><a href="../../sectores/autonomos/">Autónomos</a></li>
            <li><a href="../../sectores/clinicas-y-salud/">Clínicas y salud</a></li>
            <li><a href="../../sectores/restaurantes/">Restaurantes</a></li>
            <li><a href="../../sectores/servicios-locales/">Servicios locales</a></li>
          </ul>
        </nav>
        <div>
          <h3>Contacto</h3>
          <ul>
            <li><a href="mailto:hola@sheisdigitalab.com">hola@sheisdigitalab.com</a></li>
            <li><a href="tel:+34637889942">+34 637 889 942</a></li>
            <li>Barcelona</li>
          </ul>
        </div>
        <nav aria-label="Pie: legal">
          <h3>Legal</h3>
          <ul>
            <li><a href="https://sheisdigitalab.com/legal/aviso-legal/">Aviso legal</a></li>
            <li><a href="https://sheisdigitalab.com/legal/privacidad/">Privacidad</a></li>
            <li><a href="https://sheisdigitalab.com/legal/cookies/">Cookies</a></li>
          </ul>
        </nav>
      </div>
      <div class="footer__bottom">
        <p>© 2026 She's Digital · She is Digital Lab</p>
        <button class="motion-toggle" type="button" aria-pressed="false" data-motion-toggle>Reducir animaciones</button>
        <p>Hecho a mano en Barcelona ✦</p>
      </div>
    </div>
  </footer>

  <div class="cursor-badge" data-cursor aria-hidden="true"></div>

  <a class="wa-fab" href="https://wa.me/34637889942?text=Hola%20Jenifer%2C%20quiero%20pedir%20presupuesto%20para%20mi%20web" target="_blank" rel="noopener noreferrer" aria-label="Escríbenos por WhatsApp">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2l-.5-.3Z"/></svg>
  </a>

  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/lenis@1.3.4/dist/lenis.min.js" defer></script>
  <script src="../../assets/js/main.js" defer></script>
  <script src="../../assets/js/service.js" defer></script>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# Template del índice de sectores (profundidad ../)
# ---------------------------------------------------------------------------
INDEX_TPL = """\
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>She&#x27;s Digital · Sectores que atendemos</title>
  <meta name="description" content="Diseño web especializado para autónomos, clínicas, restaurantes y negocios locales en Barcelona. Webs a medida desde 450 €." />
  <link rel="canonical" href="https://sheisdigitalab.com/sectores/" />
  <meta property="og:title" content="She&#x27;s Digital · Sectores que atendemos" />
  <meta property="og:image" content="../assets/img/og-cover.jpg" />
  <meta name="theme-color" content="#FAF8F4" />
  <link rel="icon" href="../assets/img/favicon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="/assets/fonts/fonts.css" />
  <link rel="stylesheet" href="../assets/css/v2.css?v=17" />
  <link rel="stylesheet" href="../assets/css/service.css" />
  <script>
    (function (d) {
      var r = d.documentElement; r.classList.add('js');
      var manual = false;
      try { manual = localStorage.getItem('sd-motion') === 'reduce'; } catch (e) {}
      if (manual) r.classList.add('reduce-motion');
      if (!manual && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
        r.classList.add('is-anim');
        setTimeout(function () { if (!window.gsap) r.classList.remove('is-anim'); }, 3000);
      }
    })(document);
  </script>
</head>
<body class="service-page">
  <a class="skip" href="#main">Saltar al contenido</a>

  <header class="nav" data-nav>
    <div class="nav__inner wrap">
      <a href="../" class="nav__logo" aria-label="She's Digital, inicio">
        <img src="../assets/img/logo-stacked.svg" alt="" width="112" height="63" />
      </a>
      <nav class="nav__links" id="nav-menu" aria-label="Principal">
        <a href="../#servicios">Servicios y precios</a>
        <a href="../#proyectos">Proyectos</a>
        <a href="../#proceso">Proceso</a>
        <a href="../#sobre-mi">Sobre mí</a>
        <a href="../#faq">FAQ</a>
        <a href="#contacto" class="btn btn--dark nav__cta-mobile">Pide tu presupuesto gratis <span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span></a>
      </nav>
      <a href="#contacto" class="btn btn--dark nav__cta">Pide tu presupuesto gratis <span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span></a>
      <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="nav-menu">
        <span class="sr-only">Abrir menú</span>
        <span class="nav__bars" aria-hidden="true"><i></i><i></i></span>
      </button>
    </div>
  </header>

  <main id="main">

    <section class="cs-hero sv-hero sv-hero--index" id="top" aria-labelledby="sv-title">
      <div class="wrap">
        <nav class="sv-crumbs" aria-label="Ruta" data-hero="fade">
          <ol>
            <li><a href="../">Inicio</a></li>
            <li aria-current="page">Sectores</li>
          </ol>
        </nav>
        <h1 class="sv-title" id="sv-title">
          <span class="hero__line"><span class="hero__line-in" data-hero="line">Webs a medida</span></span>
          <span class="hero__line"><span class="hero__line-in" data-hero="line"><span class="sv-mark">para tu sector.</span></span></span>
        </h1>
        <div class="cs-hero__grid sv-hero__grid sv-hero__grid--slim">
          <div>
            <p class="cs-hero__lead" data-hero="fade">Cada sector tiene sus propias necesidades digitales. Diseño webs especializadas para que tu negocio destaque online y capte clientes. Desde 450 €.</p>
            <div class="sv-actions" data-hero="fade">
              <a href="#contacto" class="btn btn--dark btn--magnetic">Pide tu presupuesto gratis <span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span></a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="sectores-lista" aria-labelledby="sect-title">
      <div class="wrap">
        <header class="v3-head">
          <p class="eyebrow">Sectores</p>
          <h2 class="h2" id="sect-title">¿A qué se dedica <em>tu negocio?</em></h2>
        </header>
        <ul class="sv-sectors">
          <li>
            <a href="autonomos/" class="sv-sector-card">
              <div class="sv-sector-card__body">
                <h3>Autónomos y profesionales</h3>
                <p>Coaches, consultores, abogados, terapeutas. Una web que vende por ti, lista en 1 semana.</p>
                <span class="sv-sector-card__price">Desde 450 €</span>
              </div>
              <span class="sv-sector-card__arrow" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M7 17 17 7M8 7h9v9"/></svg></span>
            </a>
          </li>
          <li>
            <a href="clinicas-y-salud/" class="sv-sector-card">
              <div class="sv-sector-card__body">
                <h3>Clínicas y salud</h3>
                <p>Clínicas, fisios, dentistas y psicólogos. Reservas online, LOPD y SEO médico.</p>
                <span class="sv-sector-card__price">Desde 450 €</span>
              </div>
              <span class="sv-sector-card__arrow" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M7 17 17 7M8 7h9v9"/></svg></span>
            </a>
          </li>
          <li>
            <a href="restaurantes/" class="sv-sector-card">
              <div class="sv-sector-card__body">
                <h3>Restaurantes y hostelería</h3>
                <p>Menú online, reservas, SEO local y Google Maps. Para llenar mesas.</p>
                <span class="sv-sector-card__price">Desde 450 €</span>
              </div>
              <span class="sv-sector-card__arrow" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M7 17 17 7M8 7h9v9"/></svg></span>
            </a>
          </li>
          <li>
            <a href="servicios-locales/" class="sv-sector-card">
              <div class="sv-sector-card__body">
                <h3>Servicios locales</h3>
                <p>Fontaneros, electricistas, taxis, reformas. Tu negocio en el pack local de Google.</p>
                <span class="sv-sector-card__price">Desde 450 €</span>
              </div>
              <span class="sv-sector-card__arrow" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M7 17 17 7M8 7h9v9"/></svg></span>
            </a>
          </li>
        </ul>
      </div>
    </section>

    <section class="section contact" id="contacto" aria-labelledby="contact-title">
      <div class="wrap contact__grid">
        <div class="contact__intro">
          <p class="eyebrow" data-reveal>Contacto</p>
          <h2 class="h2" id="contact-title" data-split>Cuéntame<br /><em>tu proyecto.</em></h2>
          <p class="contact__lead" data-reveal>Escríbeme por el formulario o directamente. Te respondo el mismo día.</p>
          <ul class="contact__direct" data-reveal>
            <li><span>WhatsApp</span><a href="https://wa.me/34637889942">+34 637 889 942</a></li>
            <li><span>Email</span><a href="mailto:hola@sheisdigitalab.com">hola@sheisdigitalab.com</a></li>
            <li><span>Ubicación</span><p>Barcelona · en remoto a todas partes</p></li>
          </ul>
        </div>
        <form class="form" id="contact-form" method="post" novalidate data-reveal>
          <p class="form__note" id="form-note">Todos los campos son obligatorios.</p>
          <div class="field">
            <label for="f-name">¿Cómo te llamas?</label>
            <input id="f-name" name="name" type="text" autocomplete="name" required aria-describedby="f-name-err" />
            <p class="field__err" id="f-name-err" aria-live="polite"></p>
          </div>
          <div class="field">
            <label for="f-msg">Cuéntame tu proyecto</label>
            <textarea id="f-msg" name="message" rows="4" required aria-describedby="f-msg-err"></textarea>
            <p class="field__err" id="f-msg-err" aria-live="polite"></p>
          </div>
          <div class="field field--check">
            <input id="f-privacy" name="privacy" type="checkbox" required aria-describedby="f-privacy-err" />
            <label for="f-privacy">He leído y acepto la <a href="https://sheisdigitalab.com/legal/privacidad/">política de privacidad</a>.</label>
            <p class="field__err" id="f-privacy-err" aria-live="polite"></p>
          </div>
          <button type="submit" class="btn btn--dark btn--block">
            <span data-btn-label>Enviar por WhatsApp</span>
            <span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span>
          </button>
          <p class="form__wa-note">Se abrirá WhatsApp con tu mensaje listo para enviar.</p>
          <p class="form__status" role="status" aria-live="polite"></p>
        </form>
      </div>
    </section>

  </main>

  <footer class="footer">
    <div class="wrap">
      <div class="footer__cols">
        <div>
          <img src="../assets/img/logo-stacked-light.svg" alt="She's Digital" width="150" height="84" loading="lazy" />
          <p>Diseño web, marca y marketing digital en Barcelona.<br />Web · Ecommerce · SEO · Branding · Redes · IA y apps a medida.</p>
        </div>
        <nav aria-label="Pie: servicios">
          <h3>Servicios</h3>
          <ul>
            <li><a href="../servicios/branding/">Branding</a></li>
            <li><a href="../servicios/diseno-web/">Diseño web</a></li>
            <li><a href="../servicios/ecommerce/">Ecommerce</a></li>
            <li><a href="../servicios/seo/seo-local/">SEO local</a></li>
            <li><a href="../servicios/redes-sociales/">Redes sociales</a></li>
          </ul>
        </nav>
        <nav aria-label="Pie: sectores">
          <h3>Sectores</h3>
          <ul>
            <li><a href="autonomos/" aria-current="page">Autónomos</a></li>
            <li><a href="clinicas-y-salud/">Clínicas y salud</a></li>
            <li><a href="restaurantes/">Restaurantes</a></li>
            <li><a href="servicios-locales/">Servicios locales</a></li>
          </ul>
        </nav>
        <div>
          <h3>Contacto</h3>
          <ul>
            <li><a href="mailto:hola@sheisdigitalab.com">hola@sheisdigitalab.com</a></li>
            <li><a href="tel:+34637889942">+34 637 889 942</a></li>
            <li>Barcelona</li>
          </ul>
        </div>
        <nav aria-label="Pie: legal">
          <h3>Legal</h3>
          <ul>
            <li><a href="https://sheisdigitalab.com/legal/aviso-legal/">Aviso legal</a></li>
            <li><a href="https://sheisdigitalab.com/legal/privacidad/">Privacidad</a></li>
            <li><a href="https://sheisdigitalab.com/legal/cookies/">Cookies</a></li>
          </ul>
        </nav>
      </div>
      <div class="footer__bottom">
        <p>© 2026 She's Digital · She is Digital Lab</p>
        <button class="motion-toggle" type="button" aria-pressed="false" data-motion-toggle>Reducir animaciones</button>
        <p>Hecho a mano en Barcelona ✦</p>
      </div>
    </div>
  </footer>

  <div class="cursor-badge" data-cursor aria-hidden="true"></div>

  <a class="wa-fab" href="https://wa.me/34637889942?text=Hola%20Jenifer%2C%20quiero%20pedir%20presupuesto%20para%20mi%20web" target="_blank" rel="noopener noreferrer" aria-label="Escríbenos por WhatsApp">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2l-.5-.3Z"/></svg>
  </a>

  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/lenis@1.3.4/dist/lenis.min.js" defer></script>
  <script src="../assets/js/main.js" defer></script>
  <script src="../assets/js/service.js" defer></script>
</body>
</html>
"""


def make_features_html(items):
    rows = []
    for name, desc in items:
        rows.append(f"          <li><strong>{name}</strong><span>{desc}</span></li>")
    return "\n".join(rows)


def build_sector(data):
    out_dir = os.path.join(ROOT, "sectores", data["slug"])
    os.makedirs(out_dir, exist_ok=True)
    html = SECTOR_TPL.format(
        s2_items_html=make_features_html(data["s2_items"]),
        **{k: v for k, v in data.items() if k != "s2_items"},
    )
    path = os.path.join(out_dir, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"ok sectores/{data['slug']}/index.html")


def build_index():
    out_dir = os.path.join(ROOT, "sectores")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(INDEX_TPL)
    print("ok sectores/index.html")


if __name__ == "__main__":
    build_index()
    for s in SECTORES:
        build_sector(s)

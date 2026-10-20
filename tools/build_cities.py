#!/usr/bin/env python3
"""Genera las 6 páginas de ciudad en la raíz del proyecto."""

import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

CITIES = [
    {
        "slug": "diseno-web-barcelona",
        "city": "Barcelona",
        "city_acc": "Barcelona",
        "title": "Diseño Web Barcelona · Páginas web profesionales | She's Digital",
        "description": "Diseño web profesional en Barcelona para pequeños negocios y autónomos. Webs a medida desde 450 €. Presupuesto cerrado en 24 h, lista en 1-5 semanas.",
        "eyebrow": "Diseño web · Barcelona",
        "h1": "Diseño web profesional<br />en Barcelona.",
        "lead": "Webs a medida, rápidas y pensadas para convertir, con trato directo y presencial. Desde 450&nbsp;€ en una semana.",
        "s01_title": "Tu web en Barcelona.",
        "s01_body": "<p>Barcelona es una de las ciudades más competitivas de España en negocios online. Destacar no va de tener “una web”, sino de tener una que cargue rápido, se vea perfecta en el móvil y convierta visitas en clientes. Si la tuya no cumple, la competencia te adelanta en Google y se lleva a tus clientes.</p>",
        "s02_title": "Cerca de ti, en persona si quieres.",
        "s02_body": "<p>Estoy en Barcelona: podemos vernos, conozco el mercado y entiendo a tu cliente local. Trato directo conmigo, sin intermediarios ni agencias impersonales. La cercanía también se nota en el resultado.</p>",
        "s03_title": "Negocios de Barcelona con los que trabajo.",
        "s03_items": ["Comercio y retail", "Restauración y hostelería", "Clínicas y centros de salud", "Startups y empresas"],
        "cta_city": "Barcelona",
        "canonical_city": "barcelona",
    },
    {
        "slug": "diseno-web-granollers",
        "city": "Granollers",
        "city_acc": "Granollers",
        "title": "Diseño Web Granollers · Páginas web profesionales | She's Digital",
        "description": "Diseño web profesional en Granollers y el Vallès Oriental para negocios locales. Webs a medida desde 450 €. Presupuesto en 24 h.",
        "eyebrow": "Diseño web · Granollers",
        "h1": "Diseño web profesional<br />en Granollers.",
        "lead": "Webs a medida para negocios, comercios y empresas de la comarca. Cercanía y resultados.",
        "s01_title": "Tu web en Granollers.",
        "s01_body": "<p>Granollers es el corazón del Vallès Oriental, con un comercio local y un tejido de pymes muy activos. Muchos negocios todavía tienen webs anticuadas o ninguna. Aparecer bien en Google cuando alguien busca tu servicio en la zona marca la diferencia entre captar a ese cliente o perderlo frente a la competencia.</p>",
        "s02_title": "Cerca, en el Vallès Oriental.",
        "s02_body": "<p>Estoy en el área de Barcelona y Granollers está a un paso. Trato directo, reuniones presenciales si lo prefieres, y alguien que entiende el mercado local y a tu cliente de la comarca.</p>",
        "s03_title": "Negocios de Granollers con los que trabajo.",
        "s03_items": ["Comercio local y tiendas", "Pymes y empresas", "Hostelería y restauración", "Autónomos y gremios"],
        "cta_city": "Granollers",
        "canonical_city": "granollers",
    },
    {
        "slug": "diseno-web-sabadell",
        "city": "Sabadell",
        "city_acc": "Sabadell",
        "title": "Diseño Web Sabadell · Páginas web profesionales | She's Digital",
        "description": "Diseño web profesional en Sabadell y el Vallès para empresas, comercios y profesionales. Webs a medida desde 450 €. Presupuesto en 24 h.",
        "eyebrow": "Diseño web · Sabadell",
        "h1": "Diseño web profesional<br />en Sabadell.",
        "lead": "Webs a medida para empresas, comercios y profesionales de la zona. Cercanía, rapidez y resultados.",
        "s01_title": "Tu web en Sabadell.",
        "s01_body": "<p>Sabadell tiene uno de los tejidos empresariales y comerciales más fuertes de Cataluña. Empresas, despachos y comercios que necesitan una presencia online a la altura. Una web profesional no es un gasto: es la herramienta que trabaja por ti las 24 horas, captando clientes mientras tú te dedicas a lo tuyo.</p>",
        "s02_title": "Del Vallès, con trato cercano.",
        "s02_body": "<p>Trabajo con negocios de Sabadell y todo el Vallès con la cercanía de alguien de la zona. Reuniones presenciales si te van mejor, comunicación directa y un proceso ágil. Conozco el mercado local y a quién te diriges.</p>",
        "s03_title": "Negocios de Sabadell con los que trabajo.",
        "s03_items": ["Empresas y B2B", "Despachos y profesionales", "Comercio y retail", "Servicios locales"],
        "cta_city": "Sabadell",
        "canonical_city": "sabadell",
    },
    {
        "slug": "diseno-web-terrassa",
        "city": "Terrassa",
        "city_acc": "Terrassa",
        "title": "Diseño Web Terrassa · Páginas web profesionales | She's Digital",
        "description": "Diseño web profesional en Terrassa y el Vallès Occidental para empresas, comercios y profesionales. Webs a medida desde 450 €. Presupuesto en 24 h.",
        "eyebrow": "Diseño web · Terrassa",
        "h1": "Diseño web profesional<br />en Terrassa.",
        "lead": "Webs a medida para empresas, comercios y profesionales de la zona. Cercanía y resultados.",
        "s01_title": "Tu web en Terrassa.",
        "s01_body": "<p>Terrassa tiene un tejido industrial y comercial potente, con muchas empresas y negocios familiares que aún no aprovechan internet para captar clientes. Una web profesional, bien posicionada en Google, te pone por delante de la competencia local que todavía depende solo del boca a boca.</p>",
        "s02_title": "Cerca de ti, en el Vallès.",
        "s02_body": "<p>Estoy en el área de Barcelona y Terrassa la tengo al lado. Podemos vernos en persona, conozco la zona y a tu cliente. Trato cercano de verdad, no un número de teléfono lejano.</p>",
        "s03_title": "Negocios de Terrassa con los que trabajo.",
        "s03_items": ["Industria y empresas", "Comercio y retail", "Despachos y profesionales", "Hostelería y servicios"],
        "cta_city": "Terrassa",
        "canonical_city": "terrassa",
    },
    {
        "slug": "diseno-web-mataro",
        "city": "Mataró",
        "city_acc": "Mataró",
        "title": "Diseño Web Mataró · Páginas web profesionales | She's Digital",
        "description": "Diseño web profesional para negocios de Mataró y el Maresme. Webs a medida desde 450 €. Presupuesto en 24 h, lista en 1-5 semanas.",
        "eyebrow": "Diseño web · Mataró",
        "h1": "Diseño web profesional<br />en Mataró.",
        "lead": "Webs a medida, rápidas y pensadas para convertir, con trato directo y personal. Desde 450&nbsp;€ en una semana.",
        "s01_title": "Tu web en Mataró.",
        "s01_body": "<p>Mataró és la capital del Maresme i un centre econòmic amb molta activitat comercial i industrial. Els negocis amb presència web professional aquí destaquen davant dels competidors que no han digitalitzat.</p>",
        "s02_title": "Trabajo en remoto para toda España.",
        "s02_body": "<p>Trabajo con negocios de toda España en remoto, con la misma atención personalizada que si estuviéramos en la misma calle. Trato directo conmigo por WhatsApp o videollamada, sin intermediarios ni agencias impersonales.</p>",
        "s03_title": "Negocios de Mataró con los que trabajo.",
        "s03_items": ["Comercio y retail", "Restauración y hostelería", "Clínicas y centros de salud", "Autónomos y freelances", "Startups y empresas"],
        "cta_city": "Mataró",
        "canonical_city": "mataro",
    },
    {
        "slug": "diseno-web-sant-cugat",
        "city": "Sant Cugat del Vallès",
        "city_acc": "Sant Cugat",
        "title": "Diseño Web Sant Cugat del Vallès | She's Digital",
        "description": "Diseño web profesional para negocios de Sant Cugat del Vallès. Webs a medida desde 450 €. Presupuesto en 24 h, lista en 1-5 semanas.",
        "eyebrow": "Diseño web · Sant Cugat del Vallès",
        "h1": "Diseño web profesional<br />en Sant Cugat del Vallès.",
        "lead": "Webs a medida, rápidas y pensadas para convertir, con trato directo y personal. Desde 450&nbsp;€ en una semana.",
        "s01_title": "Tu web en Sant Cugat del Vallès.",
        "s01_body": "<p>Sant Cugat del Vallès és un dels municipis amb renda més alta de Catalunya. Els seus residents i empreses esperen una imatge digital impecable: una web professional aquí és una inversió que es nota.</p>",
        "s02_title": "Trabajo en remoto para toda España.",
        "s02_body": "<p>Trabajo con negocios de toda España en remoto, con la misma atención personalizada que si estuviéramos en la misma calle. Trato directo conmigo por WhatsApp o videollamada, sin intermediarios ni agencias impersonales.</p>",
        "s03_title": "Negocios de Sant Cugat del Vallès con los que trabajo.",
        "s03_items": ["Comercio y retail", "Restauración y hostelería", "Clínicas y centros de salud", "Autónomos y freelances", "Startups y empresas"],
        "cta_city": "Sant Cugat del Vallès",
        "canonical_city": "sant-cugat",
    },
]


def render_city(c):
    s03_items_html = "\n".join(f"          <li>{item}</li>" for item in c["s03_items"])
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{c['title']}</title>
  <meta name="description" content="{c['description']}" />
  <link rel="canonical" href="https://sheisdigitalab.com/diseno-web-{c['canonical_city']}/" />
  <meta property="og:title" content="{c['title']}" />
  <meta property="og:description" content="{c['description']}" />
  <meta property="og:image" content="../assets/img/og-cover.jpg" />
  <meta property="og:type" content="website" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="theme-color" content="#FAF8F4" />
  <link rel="icon" href="../assets/img/favicon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="/assets/fonts/fonts.css" />
  <link rel="stylesheet" href="../assets/css/v2.css?v=17" />
  <link rel="stylesheet" href="../assets/css/service.css" />
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
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "She's Digital",
    "description": "{c['description']}",
    "url": "https://sheisdigitalab.com",
    "address": {{"@type": "PostalAddress", "addressLocality": "{c['city']}", "addressCountry": "ES"}},
    "telephone": "+34637889942"
  }}
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

    <section class="cs-hero sv-hero sv-hero--index" id="top" aria-labelledby="city-title">
      <div class="wrap">
        <nav class="sv-crumbs" aria-label="Ruta" data-hero="fade">
          <ol>
            <li><a href="../">Inicio</a></li>
            <li aria-current="page">Diseño web {c['city']}</li>
          </ol>
        </nav>

        <p class="eyebrow" data-hero="fade">{c['eyebrow']}</p>
        <h1 class="sv-title" id="city-title">
          <span class="hero__line"><span class="hero__line-in" data-hero="line">Diseño web profesional</span></span>
          <span class="hero__line"><span class="hero__line-in" data-hero="line"><span class="sv-mark">en {c['city']}.</span></span></span>
        </h1>

        <div class="cs-hero__grid sv-hero__grid sv-hero__grid--slim">
          <div>
            <p class="cs-hero__lead" data-hero="fade">{c['lead']}</p>
            <div class="sv-actions" data-hero="fade">
              <a href="#contacto" class="btn btn--dark btn--magnetic">Pedir presupuesto <span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span></a>
              <a href="../#proyectos" class="btn btn--line">Ver proyectos</a>
            </div>
            <ul class="city-checks" data-hero="fade">
              <li>✓ Presupuesto en 24&nbsp;h</li>
              <li>✓ Lista en 1-5 semanas</li>
              <li>✓ SEO incluido</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="section sv-section" id="s01" aria-labelledby="s01-title" data-reveal>
      <div class="wrap sv-section__grid">
        <header>
          <p class="eyebrow">01</p>
          <h2 class="h2" id="s01-title">{c['s01_title']}</h2>
        </header>
        <div class="sv-prose">
          {c['s01_body']}
        </div>
      </div>
    </section>

    <section class="section sv-section sv-section--alt" id="s02" aria-labelledby="s02-title" data-reveal>
      <div class="wrap sv-section__grid">
        <header>
          <p class="eyebrow">02</p>
          <h2 class="h2" id="s02-title">{c['s02_title']}</h2>
        </header>
        <div class="sv-prose">
          {c['s02_body']}
        </div>
      </div>
    </section>

    <section class="section sv-section" id="s03" aria-labelledby="s03-title" data-reveal>
      <div class="wrap sv-section__grid">
        <header>
          <p class="eyebrow">03</p>
          <h2 class="h2" id="s03-title">{c['s03_title']}</h2>
        </header>
        <div class="sv-prose">
          <ul class="sv-fits">
{s03_items_html}
          </ul>
          <p style="margin-top:16px">¿No ves el tuyo? Da igual: si tienes un negocio y quieres que te encuentren online, te ayudo igual.</p>
        </div>
      </div>
    </section>

    <section class="section" id="contacto" aria-labelledby="contacto-title" data-reveal>
      <div class="wrap wrap--narrow">
        <header class="section__head">
          <p class="eyebrow">Contacto</p>
          <h2 class="h2" id="contacto-title">¿Hablamos de tu web en {c['cta_city']}?</h2>
          <p class="section__lead">Cuéntame qué necesitas y te envío un presupuesto cerrado en 24&nbsp;h. Sin compromiso.</p>
        </header>
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
        <p class="city-tel">O llámanos: <a href="tel:+34637889942">+34 637 889 942</a></p>
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
            <li><a href="../sectores/autonomos/">Autónomos</a></li>
            <li><a href="../sectores/clinicas-y-salud/">Clínicas y salud</a></li>
            <li><a href="../sectores/restaurantes/">Restaurantes</a></li>
            <li><a href="../sectores/servicios-locales/">Servicios locales</a></li>
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


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  OK  {os.path.relpath(path, ROOT)}")


if __name__ == "__main__":
    print("=== build_cities.py ===")
    for city in CITIES:
        path = os.path.join(ROOT, city["slug"], "index.html")
        write(path, render_city(city))
    print(f"\nGeneradas: {len(CITIES)} páginas de ciudad")

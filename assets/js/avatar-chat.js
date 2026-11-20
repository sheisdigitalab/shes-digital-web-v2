/* She's Digital · Avatar del hero
   - Chat con respuestas preparadas (sin servidor ni coste). Los datos salen de
     los precios y plazos publicados en la propia web. Para conectar una IA más
     adelante, solo hay que sustituir la función reply().
   - Las respuestas aparecen en el bocadillo del avatar, con puntos de
     "escribiendo" y efecto de escritura.
   - Giro de cabeza hacia el cursor (solo punteros finos y sin movimiento reducido). */
(function () {
  'use strict';

  var root = document.getElementById('avatar');
  if (!root) return;

  var bubble = root.querySelector('#avatar-bubble');
  var live = root.querySelector('#avatar-live');
  var ghost = root.querySelector('[data-avatar-ghost]');
  var typed = root.querySelector('[data-avatar-typed]');
  var dots = root.querySelector('[data-avatar-dots]');
  var actions = root.querySelector('[data-avatar-actions]');
  var form = root.querySelector('#avatar-form');
  var input = root.querySelector('#avatar-q');
  var chips = root.querySelector('[data-avatar-chips]');
  var nextBtn = root.querySelector('[data-avatar-next]');
  var frame = root.querySelector('[data-avatar-tilt]');

  var reduce = document.documentElement.classList.contains('reduce-motion') ||
    (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  var finePointer = window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  var GREETING = '¡Hola! Soy Jenifer. Cuéntame qué necesita tu negocio y te oriento.';
  var ANSWERS = {
    precio: 'Una landing page desde 450 €, una web completa de hasta 5 páginas desde 790 € y una tienda online desde 1.190 €. El precio es cerrado antes de empezar y no incluye IVA.',
    plazo: 'Desde 1 semana. Antes de publicar, ves tu web en un enlace de prueba y la revisamos juntos.',
    tienda: 'Sí. Una tienda online con pagos y envíos listos, de hasta 20 productos, desde 1.190 €.',
    seo: 'Hago SEO local, técnico y de contenidos para que te encuentren en Google y en Maps, desde 190 € al mes.',
    pago: 'El pago es en 2 plazos: 50 % al inicio y 50 % al lanzamiento. Sin permanencias ni cuotas ocultas.',
    incluye: 'Textos legales y aviso de cookies, un enlace de prueba para ver tu web antes de publicarla, formación para usarla y 1 mes de soporte.',
    proceso: 'Te escucho, preparo el plan y el diseño y lo validamos juntos antes de programar. Después desarrollo tu web, la publicamos y seguimos mejorándola.',
    branding: 'Sí. Diseño tu logo, tus colores y tu tipografía con personalidad propia, desde 490 €, para que tu marca se recuerde.',
    redes: 'Sí. Llevo tus redes con contenido constante y con tu voz, cada mes, desde 250 € al mes.',
    ia: 'Sí. Creo agentes de IA que contestan, reservan y venden por WhatsApp, 24 horas al día. El presupuesto es a medida y gratis.',
    apps: 'Sí. Desarrollo CRM, áreas de cliente o herramientas de gestión interna a medida. Cuéntame tu caso y te preparo presupuesto gratis.',
    otro: 'Gracias por preguntar. Cuéntame tu caso por WhatsApp o pide tu presupuesto gratis: te respondo en menos de 24 h.'
  };

  // A qué parte de la web lleva cada respuesta (botón principal del bocadillo)
  var LINKS = {
    precio:   { href: '#servicios', label: 'Ver precios' },
    plazo:    { href: '#proceso', label: 'Ver el proceso' },
    tienda:   { href: '/servicios/ecommerce/', label: 'Ver tiendas online' },
    seo:      { href: '/servicios/seo/seo-local/', label: 'Ver SEO local' },
    pago:     { href: '#faq', label: 'Ver preguntas' },
    incluye:  { href: '/servicios/diseno-web/', label: 'Ver diseño web' },
    proceso:  { href: '#proceso', label: 'Ver el proceso' },
    branding: { href: '/servicios/branding/', label: 'Ver branding' },
    redes:    { href: '/servicios/redes-sociales/', label: 'Ver redes sociales' },
    ia:       { href: '/servicios/agentes-ia/', label: 'Ver agentes de IA' },
    apps:     { href: '/servicios/apps-a-medida/', label: 'Ver apps a medida' },
    otro:     { href: '#contacto', label: 'Presupuesto gratis' }
  };
  var primary = root.querySelector('[data-avatar-primary]');

  function track(name, detail) {
    // gtag solo existe si la persona ha aceptado las cookies de analítica
    if (typeof window.gtag === 'function') {
      window.gtag('event', name, { event_category: 'avatar', event_label: detail || '' });
    }
  }

  /* ---------- Bocadillo: puntos + escritura ---------- */
  var timer = 0;
  var token = 0;

  var skipTyping = null;

  function speak(text, withActions) {
    var my = ++token;
    clearTimeout(timer);
    // El texto completo reserva el tamaño del bocadillo: no salta mientras se escribe
    ghost.textContent = text;
    typed.textContent = '';
    bubble.classList.toggle('has-actions', !!withActions);
    bubble.classList.remove('is-done');
    if (!reduce) { bubble.classList.remove('is-pop'); void bubble.offsetWidth; bubble.classList.add('is-pop'); }
    if (actions) actions.setAttribute('aria-hidden', 'true');

    function finish() {
      if (my !== token) return;
      typed.textContent = text;
      dots.classList.remove('is-on');
      live.textContent = text;
      bubble.classList.add('is-done');
      if (actions) actions.removeAttribute('aria-hidden');
    }

    skipTyping = finish;
    if (reduce) { finish(); return; }

    dots.classList.add('is-on');
    timer = setTimeout(function () {
      if (my !== token) return;
      dots.classList.remove('is-on');
      var i = 0;
      (function tick() {
        if (my !== token) return;
        if (i <= text.length) {
          typed.textContent = text.slice(0, i++);
          timer = setTimeout(tick, 14);
        } else {
          finish();
        }
      })();
    }, 650);
  }

  function reply(key, label) {
    var L = LINKS[key] || LINKS.otro;
    if (primary) { primary.textContent = L.label; primary.setAttribute('href', L.href); primary.setAttribute('data-avatar-detail', key); }
    speak(ANSWERS[key] || ANSWERS.otro, true);
    track('avatar_pregunta', label || key);
  }

  function clearAsked() {
    if (!chips) return;
    [].forEach.call(chips.querySelectorAll('.avatar__chip'), function (c) { c.classList.remove('is-asked'); c.removeAttribute('aria-pressed'); });
  }

  /* ---------- Preguntas sugeridas ---------- */
  root.addEventListener('click', function (e) {
    var chip = e.target.closest('.avatar__chip');
    if (chip) {
      [].forEach.call(chips.querySelectorAll('.avatar__chip'), function (c) { c.classList.remove('is-asked'); c.removeAttribute('aria-pressed'); });
      chip.classList.add('is-asked'); chip.setAttribute('aria-pressed', 'true');
      reply(chip.getAttribute('data-q'), chip.textContent.trim()); return;
    }
    if (e.target.closest('#avatar-bubble') && !e.target.closest('a, button') && skipTyping && !bubble.classList.contains('is-done')) { skipTyping(); return; }
    var cta = e.target.closest('[data-avatar-event]');
    if (cta) { track('avatar_' + cta.getAttribute('data-avatar-event'), cta.getAttribute('data-avatar-detail') || ''); return; }
    if (e.target.closest('[data-avatar-close]')) { clearAsked(); speak(GREETING, false); }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && bubble.classList.contains('has-actions')) { clearAsked(); speak(GREETING, false); }
  });

  var prevBtn = root.querySelector('[data-avatar-prev]');
  if (chips && nextBtn) {
    var syncNext = function () {
      var max = chips.scrollWidth - chips.clientWidth - 2;
      var overflow = max > 0;
      var hasL = overflow && chips.scrollLeft > 2;
      var hasR = overflow && chips.scrollLeft < max;
      nextBtn.hidden = !hasR;
      if (prevBtn) prevBtn.hidden = !hasL;
      chips.classList.toggle('has-l', hasL);
      chips.classList.toggle('has-r', hasR);
    };
    var scrollStep = function (dir) {
      chips.scrollBy({ left: dir * Math.max(180, chips.clientWidth * 0.7), behavior: reduce ? 'auto' : 'smooth' });
    };
    nextBtn.addEventListener('click', function () { scrollStep(1); });
    if (prevBtn) prevBtn.addEventListener('click', function () { scrollStep(-1); });
    chips.addEventListener('scroll', syncNext, { passive: true });
    window.addEventListener('resize', syncNext);
    syncNext();
    setTimeout(syncNext, 400);
  }

  /* Arrastrar la fila de preguntas con el ratón (en táctil y trackpad ya se desliza sola) */
  if (chips) {
    var dragX = 0, startLeft = 0, dragging = false, moved = false;
    chips.addEventListener('pointerdown', function (e) {
      if (e.pointerType !== 'mouse' || e.button !== 0) return;
      dragging = true; moved = false; dragX = e.clientX; startLeft = chips.scrollLeft;
    });
    window.addEventListener('pointermove', function (e) {
      if (!dragging) return;
      var dx = e.clientX - dragX;
      if (!moved && Math.abs(dx) > 4) { moved = true; chips.classList.add('is-drag'); }
      if (moved) chips.scrollLeft = startLeft - dx;
    });
    window.addEventListener('pointerup', function () {
      if (!dragging) return;
      dragging = false;
      setTimeout(function () { chips.classList.remove('is-drag'); }, 0);
    });
  }

  /* ---------- Texto libre ---------- */
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var v = input.value.trim();
    if (!v) { input.focus(); return; }
    var l = v.toLowerCase();
    var key = 'otro';
    // primero el tema concreto (servicio) y después las preguntas generales (precio, plazo...)
    if (/(logo|logotipo|marca|branding|identidad)/.test(l)) key = 'branding';
    else if (/(redes|instagram|facebook|tiktok|social)/.test(l)) key = 'redes';
    else if (/(tienda|ecommerce|e-commerce|vender online|productos|shopify|woocommerce)/.test(l)) key = 'tienda';
    else if (/(seo|google|posicion|maps)/.test(l)) key = 'seo';
    else if (/(agente|asistente|chatbot|inteligencia|\bia\b|\bbot\b|whatsapp)/.test(l)) key = 'ia';
    else if (/(\bapp\b|\bapps\b|aplicaci|crm|gesti[oó]n interna|[aá]rea de clientes)/.test(l)) key = 'apps';
    else if (/(cuesta|precio|tarifa|cu[aá]nto vale|presupuesto|€)/.test(l)) key = 'precio';
    else if (/(tard|plazo|cu[aá]ndo|semana|r[aá]pid)/.test(l)) key = 'plazo';
    else if (/(pag[ao]r?|cobr|plazos|factura)/.test(l)) key = 'pago';
    else if (/(incluye|incluido|soporte|formaci[oó]n|legal|cookies)/.test(l)) key = 'incluye';
    else if (/(proceso|c[oó]mo trabajas|pasos|metodolog)/.test(l)) key = 'proceso';
    else if (/(web|p[aá]gina|dise[nñ]o)/.test(l)) key = 'precio';
    reply(key, 'texto_libre');
    input.value = '';
  });

  /* ---------- Saludo inicial ---------- */
  speak(GREETING, false);

  /* ---------- Giro de cabeza hacia el cursor ---------- */
  // 13 fotogramas (de -6 a +6). La posición avanza con inercia y se mezclan solo dos fotogramas vecinos.
  // Rendimiento: solo los dos fotogramas activos se pintan (el resto va con visibility:hidden, sin capa de GPU),
  // y solo se escribe en el DOM lo que cambia.
  var posesBox = root.querySelector('[data-avatar-poses]');
  if (posesBox && finePointer && !reduce) {
    var frames = [].slice.call(posesBox.querySelectorAll('[data-f]'))
      .sort(function (a, b) { return a.getAttribute('data-f') - b.getAttribute('data-f'); });
    var N = frames.length, MID = (N - 1) / 2;
    var op = [], vis = [];
    frames.forEach(function (im, i) {
      im.style.zIndex = i + 1;
      op[i] = (i === MID) ? 1 : 0; vis[i] = (i === MID);
      if (i !== MID) im.style.visibility = 'hidden';
    });

    // Carga escalonada, del centro hacia fuera, cuando el navegador está libre: no compite con la carga de la página
    var loadOrder = frames.map(function (im, i) { return i; }).filter(function (i) { return i !== MID; })
      .sort(function (a, b) { return Math.abs(a - MID) - Math.abs(b - MID); });
    var ready = {};
    function loadNext() {
      var i = loadOrder.shift();
      if (i === undefined) return;
      var im = frames[i];
      im.srcset = im.dataset.srcset; im.src = im.dataset.src;
      var done = function () { ready[i] = true; setTimeout(loadNext, 90); };
      if (im.decode) im.decode().then(done, done); else im.onload = done;
    }
    function startLoading() { setTimeout(loadNext, 500); }
    if (document.readyState === 'complete') startLoading(); else window.addEventListener('load', startLoading, { once: true });

    var pos = MID, target = MID, last = 0, raf = 0;
    function setFrame(k, o) {
      var v = o > 0;
      if (v !== vis[k]) { frames[k].style.visibility = v ? 'visible' : 'hidden'; frames[k].style.willChange = v ? 'opacity' : ''; vis[k] = v; }
      if (o !== op[k]) { frames[k].style.opacity = o; op[k] = o; }
    }
    function render() {
      var i = Math.max(0, Math.min(N - 2, Math.floor(pos)));
      // si el fotograma todavía no ha cargado, se usa el cargado más cercano hacia el centro
      var i0 = i, i1 = i + 1;
      while (i0 !== MID && !ready[i0]) i0 += (i0 < MID ? 1 : -1);
      while (i1 !== MID && !ready[i1]) i1 += (i1 < MID ? 1 : -1);
      var f = pos - i;
      var w = Math.max(0, Math.min(1, (f - 0.3) / 0.4));
      w = w * w * (3 - 2 * w);
      if (i0 === i1) w = 0;
      for (var k = 0; k < N; k++) {
        var o = 0;
        if (k === i0) o = 1;
        else if (k === i1) o = w;
        setFrame(k, o);
      }
    }
    function tick(t) {
      var dt = last ? Math.min(0.05, (t - last) / 1000) : 0.016; last = t;
      pos += (target - pos) * (1 - Math.exp(-dt * 7.5));        // inercia: arranque y frenada suaves
      if (Math.abs(target - pos) < 0.004) { pos = target; raf = 0; last = 0; render(); return; }
      render();
      raf = requestAnimationFrame(tick);
    }
    function go(t) { target = t; if (!raf) raf = requestAnimationFrame(tick); }
    render();

    // Posición del avatar en pantalla: se mide una vez y se actualiza al hacer scroll o cambiar de tamaño
    var cx = 0, onScreen = true;
    function measure() {
      var r = (frame || posesBox).getBoundingClientRect();
      cx = r.left + r.width / 2; onScreen = !(r.bottom < 0 || r.top > window.innerHeight);
    }
    measure();
    window.addEventListener('resize', measure);
    window.addEventListener('scroll', measure, { passive: true });

    // El avatar reacciona al cursor en toda la ventana, no solo cuando está encima
    window.addEventListener('pointermove', function (e) {
      if (!onScreen || (e.pointerType && e.pointerType !== 'mouse' && e.pointerType !== 'pen')) return;
      var nx = Math.max(-1, Math.min(1, (e.clientX - cx) / (window.innerWidth * 0.5)));
      go(MID + Math.max(-MID, Math.min(MID, nx * 10)));          // giro completo a ~60 % del recorrido
    }, { passive: true });

    document.documentElement.addEventListener('pointerleave', function () { go(MID); });
  }
})();

/* She's Digital · Home v2 — interacción y movimiento
   GSAP + ScrollTrigger + Lenis (único motor de scroll suave) */
(function () {
  'use strict';

  const root = document.documentElement;
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  const hasGsap = typeof window.gsap !== 'undefined' && typeof window.ScrollTrigger !== 'undefined';
  const animate = hasGsap && !reduced;

  if (!animate) root.classList.remove('is-anim');

  /* ---------- Navegación ---------- */
  const nav = document.querySelector('[data-nav]');
  const toggle = nav.querySelector('.nav__toggle');
  const menu = document.getElementById('nav-menu');

  function setMenu(open) {
    toggle.setAttribute('aria-expanded', String(open));
    toggle.querySelector('.sr-only').textContent = open ? 'Cerrar menú' : 'Abrir menú';
    menu.classList.toggle('is-open', open);
  }
  toggle.addEventListener('click', () => setMenu(toggle.getAttribute('aria-expanded') !== 'true'));
  menu.addEventListener('click', (e) => { if (e.target.closest('a')) setMenu(false); });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && menu.classList.contains('is-open')) { setMenu(false); toggle.focus(); }
  });

  let lastY = window.scrollY;
  function onScrollNav(y) {
    nav.classList.toggle('is-scrolled', y > 24);
    const goingDown = y > lastY && y > 400;
    nav.classList.toggle('is-hidden', goingDown && !menu.classList.contains('is-open') && !nav.contains(document.activeElement));
    lastY = y;
  }

  /* ---------- Formulario → WhatsApp ---------- */
  const form = document.getElementById('contact-form');
  if (form) {
    const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const rules = {
      'f-name': (el) => el.value.trim() ? '' : 'Escribe tu nombre.',
      'f-email': (el) => !el.value.trim() ? 'El email es obligatorio.' : (emailRe.test(el.value.trim()) ? '' : 'Ese email no parece válido.'),
      'f-msg': (el) => el.value.trim() ? '' : 'Cuéntame algo de tu proyecto.',
      'f-privacy': (el) => el.checked ? '' : 'Acepta la política de privacidad para continuar.'
    };
    const check = (id) => {
      const el = document.getElementById(id);
      const msg = rules[id](el);
      document.getElementById(id + '-err').textContent = msg;
      el.setAttribute('aria-invalid', msg ? 'true' : 'false');
      return !msg;
    };
    Object.keys(rules).forEach((id) => {
      const el = document.getElementById(id);
      el.addEventListener('blur', () => { if (el.value || el.type === 'checkbox') check(id); });
      el.addEventListener('input', () => { if (el.getAttribute('aria-invalid') === 'true') check(id); });
      el.addEventListener('change', () => { if (el.getAttribute('aria-invalid') === 'true') check(id); });
    });
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const ok = Object.keys(rules).map(check).every(Boolean);
      const status = form.querySelector('.form__status');
      if (!ok) { form.querySelector('[aria-invalid="true"]').focus(); return; }
      const name = form.elements.name.value.trim();
      const email = form.elements.email.value.trim();
      const message = form.elements.message.value.trim();
      const text = 'Hola Jenifer, soy ' + name + ' (' + email + ').\n\n' + message;
      window.open('https://wa.me/34637889942?text=' + encodeURIComponent(text), '_blank', 'noopener');
      status.textContent = 'Te abro WhatsApp con tu mensaje. Si no se abre, escríbeme a hola@sheisdigitalab.com.';
      form.reset();
    });
  }

  /* ---------- Rotador del titular (una sola vuelta, menos de 5 s) ---------- */
  const rotorEl = document.querySelector('[data-rotor]');
  const fitRotor = (word) => {
    if (!rotorEl || !word) return;
    const range = document.createRange();
    range.selectNodeContents(word);
    rotorEl.style.setProperty('--w', range.getBoundingClientRect().width + 'px');
  };
  const fitActive = () => fitRotor(rotorEl && rotorEl.querySelector('.is-active'));
  fitActive();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitActive);
  window.addEventListener('resize', fitActive);

  function runRotor() {
    const rotor = rotorEl;
    if (!rotor) return;
    const words = Array.from(rotor.children);
    const order = [1, 2, 3, 0];
    let step = 0;
    const next = () => {
      const current = words.find((w) => w.classList.contains('is-active'));
      const incoming = words[order[step]];
      gsap.to(current, { yPercent: -100, opacity: 0, duration: .45, ease: 'power3.in', onComplete: () => {
        current.classList.remove('is-active');
        gsap.set(current, { clearProps: 'all' });
      } });
      incoming.classList.add('is-active');
      fitRotor(incoming);
      gsap.fromTo(incoming, { yPercent: 100, opacity: 0 }, { yPercent: 0, opacity: 1, duration: .6, ease: 'power3.out', delay: .3 });
      step += 1;
      if (step < order.length) gsap.delayedCall(1.05, next);
    };
    gsap.delayedCall(1.2, next);
  }

  if (!animate) {
    window.addEventListener('scroll', () => onScrollNav(window.scrollY), { passive: true });
    return;
  }

  /* =========================================================
     A partir de aquí, solo con movimiento permitido
     ========================================================= */
  gsap.registerPlugin(ScrollTrigger);

  /* ---------- Lenis ---------- */
  let lenis = null;
  if (typeof window.Lenis !== 'undefined') {
    lenis = new Lenis({ lerp: 0.1, wheelMultiplier: 1 });
    lenis.on('scroll', (e) => { ScrollTrigger.update(); onScrollNav(e.scroll); });
    gsap.ticker.add((t) => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
  } else {
    window.addEventListener('scroll', () => onScrollNav(window.scrollY), { passive: true });
  }

  // Anclas internas con el mismo desplazamiento suave y foco accesible
  document.addEventListener('click', (e) => {
    const a = e.target.closest('a[href^="#"]');
    if (!a) return;
    const id = a.getAttribute('href');
    const target = id === '#' ? null : document.querySelector(id);
    if (!target) return;
    e.preventDefault();
    const focusTarget = () => {
      if (!target.hasAttribute('tabindex')) target.setAttribute('tabindex', '-1');
      target.focus({ preventScroll: true });
    };
    if (lenis) lenis.scrollTo(target, { offset: id === '#top' ? 0 : -72, duration: 1.4, onComplete: focusTarget });
    else { target.scrollIntoView({ behavior: 'smooth' }); focusTarget(); }
    history.replaceState(null, '', id);
  });

  /* ---------- Proyectos: carril horizontal en escritorio ---------- */
  const mm = gsap.matchMedia();
  mm.add('(min-width: 1024px)', () => {
    const section = document.querySelector('[data-work]');
    const rail = section.querySelector('[data-work-track]');
    const count = section.querySelector('[data-work-count]');
    const bar = section.querySelector('[data-work-progress]');
    const total = rail.children.length - 1;
    section.classList.add('is-horizontal');
    const distance = () => rail.scrollWidth - window.innerWidth;

    const tween = gsap.to(rail, {
      x: () => -distance(),
      ease: 'none',
      scrollTrigger: {
        trigger: section,
        start: 'top top',
        end: () => '+=' + distance(),
        pin: true,
        scrub: 1,
        invalidateOnRefresh: true,
        onUpdate: (self) => {
          gsap.set(bar, { scaleX: self.progress });
          const n = Math.min(total, Math.round(self.progress * (total - 1)) + 1);
          count.textContent = String(n).padStart(2, '0');
        }
      }
    });

    // Ligero desplazamiento interno de cada captura mientras pasa
    rail.querySelectorAll('.case__media img').forEach((img) => {
      gsap.fromTo(img, { xPercent: -4 }, {
        xPercent: 4, ease: 'none',
        scrollTrigger: { trigger: img.closest('.case'), containerAnimation: tween, start: 'left right', end: 'right left', scrub: true }
      });
    });

    // Con teclado: llevar a la vista la tarjeta que recibe el foco
    const onFocus = (e) => {
      const card = e.target.closest('.case');
      if (!card) return;
      const st = tween.scrollTrigger;
      const pad = parseFloat(getComputedStyle(rail).paddingLeft) || 0;
      const p = gsap.utils.clamp(0, 1, (card.offsetLeft - pad) / distance());
      const y = st.start + p * (st.end - st.start);
      if (lenis) lenis.scrollTo(y, { immediate: true }); else window.scrollTo(0, y);
      // El navegador desplaza el contenedor recortado para mostrar el foco: lo deshacemos
      [section, section.querySelector('.work__pin')].forEach((el) => { el.scrollLeft = 0; });
      requestAnimationFrame(() => { section.scrollLeft = 0; });
    };
    rail.addEventListener('focusin', onFocus);

    return () => {
      rail.removeEventListener('focusin', onFocus);
      section.classList.remove('is-horizontal');
    };
  });

  /* ---------- Partir titulares en palabras ---------- */
  function splitWords(el) {
    const plain = el.cloneNode(true);
    plain.querySelectorAll('br').forEach((br) => br.replaceWith(' '));
    const label = plain.textContent.replace(/\s+/g, ' ').trim();
    const visual = document.createElement('span');
    visual.setAttribute('aria-hidden', 'true');
    const build = (source, target) => {
      source.childNodes.forEach((node) => {
        if (node.nodeType === 3) {
          node.textContent.split(/(\s+)/).forEach((part) => {
            if (!part) return;
            if (/^\s+$/.test(part)) { target.appendChild(document.createTextNode(' ')); return; }
            const outer = document.createElement('span');
            outer.className = 'split-word';
            const inner = document.createElement('span');
            inner.textContent = part;
            outer.appendChild(inner);
            target.appendChild(outer);
          });
        } else if (node.nodeType === 1) {
          const clone = node.cloneNode(false);
          target.appendChild(clone);
          build(node, clone);
        }
      });
    };
    build(el, visual);
    const sr = document.createElement('span');
    sr.className = 'sr-only';
    sr.textContent = label;
    el.replaceChildren(sr, visual);
    return visual;
  }

  document.querySelectorAll('[data-split]').forEach((el) => {
    const visual = splitWords(el);
    const words = visual.querySelectorAll('.split-word > span');
    const marks = visual.querySelectorAll('em');
    gsap.set(words, { yPercent: 110 });
    gsap.set(marks, { backgroundSize: '0% 100%' });
    const tl = gsap.timeline({ scrollTrigger: { trigger: el, start: 'top 86%', once: true } });
    tl.to(words, { yPercent: 0, duration: 1.05, ease: 'expo.out', stagger: 0.045 })
      .to(marks, { backgroundSize: '100% 100%', duration: .9, ease: 'expo.inOut' }, '-=.7');
  });

  /* ---------- Revelados generales ---------- */
  ScrollTrigger.batch('[data-reveal]', {
    start: 'top 90%',
    once: true,
    onEnter: (batch) => gsap.to(batch, { opacity: 1, y: 0, duration: 1, ease: 'expo.out', stagger: 0.08, overwrite: true })
  });

  /* ---------- Hero: intro + abanico ---------- */
  const cards = gsap.utils.toArray('.deck__card');
  const base = cards.map((_, i) => ({ xPercent: i * 5, yPercent: i * -8, rotation: (i - 1.5) * 5 }));
  cards.forEach((c, i) => gsap.set(c, { x: 0, y: 0, ...base[i] }));

  const intro = gsap.timeline({ defaults: { ease: 'expo.out' }, onComplete: runRotor });
  intro
    .to('[data-hero="line"]', { y: 0, duration: 1.2, stagger: 0.12 }, 0.1)
    .to('[data-hero="fade"]', { opacity: 1, y: 0, duration: 1, stagger: 0.08 }, 0.35)
    .fromTo(cards,
      { opacity: 0, yPercent: 60, rotation: 0, xPercent: 0 },
      { opacity: 1, duration: 1.4, stagger: 0.1, yPercent: (i) => base[i].yPercent, rotation: (i) => base[i].rotation, xPercent: (i) => base[i].xPercent },
      0.25)
    .from('.deck__tag', { opacity: 0, scale: .8, duration: .8 }, 1.1);

  const stage = document.querySelector('[data-stage]');
  if (stage && finePointer) {
    const rot = cards.map((c) => gsap.quickTo(c, 'rotation', { duration: .8, ease: 'power3.out' }));
    const xs = cards.map((c) => gsap.quickTo(c, 'x', { duration: .8, ease: 'power3.out' }));
    const ys = cards.map((c) => gsap.quickTo(c, 'y', { duration: .8, ease: 'power3.out' }));
    let raf = 0;
    stage.addEventListener('pointermove', (e) => {
      if (raf || intro.isActive()) return;
      raf = requestAnimationFrame(() => {
        raf = 0;
        const r = stage.getBoundingClientRect();
        const px = (e.clientX - r.left) / r.width - 0.5;
        const py = (e.clientY - r.top) / r.height - 0.5;
        cards.forEach((_, i) => {
          const k = i - 1.5;
          rot[i](base[i].rotation + k * px * 7);
          xs[i](k * px * 46);
          ys[i](py * -12 * (i + 1));
        });
      });
    });
    const reset = () => cards.forEach((_, i) => { rot[i](base[i].rotation); xs[i](0); ys[i](0); });
    stage.addEventListener('pointerleave', reset);
    window.addEventListener('blur', reset);
  }

  // El abanico se abre un poco al hacer scroll fuera del hero
  gsap.to(cards, {
    yPercent: (i) => base[i].yPercent - 6 * (i + 1),
    ease: 'none',
    scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true }
  });

  /* ---------- Cinta: velocidad según el scroll ---------- */
  const track = document.querySelector('[data-marquee]');
  if (track) {
    const loop = gsap.to(track, { xPercent: -50, duration: 38, ease: 'none', repeat: -1 });
    ScrollTrigger.create({
      trigger: '.ribbon', start: 'top bottom', end: 'bottom top',
      onToggle: (self) => (self.isActive ? loop.play() : loop.pause()),
      onUpdate: (self) => {
        const v = Math.min(Math.abs(self.getVelocity()) / 400, 4);
        gsap.to(loop, { timeScale: (self.direction < 0 ? -1 : 1) * (1 + v), duration: .3, overwrite: true });
        gsap.to(loop, { timeScale: self.direction < 0 ? -1 : 1, duration: 1, delay: .3 });
      }
    });
  }

  /* ---------- Proceso: línea de progreso ---------- */
  gsap.to('[data-process-line]', {
    scaleX: 1, ease: 'none',
    scrollTrigger: { trigger: '.process', start: 'top 70%', end: 'bottom 70%', scrub: true }
  });

  /* ---------- Sobre mí: párrafo que se ilumina palabra a palabra ---------- */
  document.querySelectorAll('[data-words]').forEach((p) => {
    const words = p.textContent.trim().split(/\s+/);
    p.replaceChildren(...words.flatMap((w, i) => {
      const s = document.createElement('span');
      s.className = 'word';
      s.textContent = w;
      return i < words.length - 1 ? [s, document.createTextNode(' ')] : [s];
    }));
    gsap.fromTo(p.querySelectorAll('.word'), { opacity: .18 }, {
      opacity: 1, ease: 'none', stagger: .1,
      scrollTrigger: { trigger: p, start: 'top 80%', end: 'bottom 45%', scrub: true }
    });
  });

  const about = document.querySelector('[data-parallax] img');
  if (about) {
    gsap.fromTo(about, { yPercent: -8 }, {
      yPercent: 0, ease: 'none',
      scrollTrigger: { trigger: '[data-parallax]', start: 'top bottom', end: 'bottom top', scrub: true }
    });
  }

  /* ---------- Precio: contador ---------- */
  document.querySelectorAll('[data-count]').forEach((el) => {
    const end = Number(el.dataset.count);
    const obj = { v: 0 };
    gsap.to(obj, {
      v: end, duration: 1.6, ease: 'expo.out',
      scrollTrigger: { trigger: el, start: 'top 85%', once: true },
      onUpdate: () => { el.textContent = Math.round(obj.v); }
    });
  });

  /* ---------- Botones magnéticos ---------- */
  if (finePointer) {
    document.querySelectorAll('.btn--magnetic').forEach((btn) => {
      const qx = gsap.quickTo(btn, 'x', { duration: .5, ease: 'power3.out' });
      const qy = gsap.quickTo(btn, 'y', { duration: .5, ease: 'power3.out' });
      btn.addEventListener('pointermove', (e) => {
        const r = btn.getBoundingClientRect();
        qx((e.clientX - r.left - r.width / 2) * 0.25);
        qy((e.clientY - r.top - r.height / 2) * 0.35);
      });
      btn.addEventListener('pointerleave', () => { qx(0); qy(0); });
    });
  }

  ScrollTrigger.sort();

  /* ---------- Medidas tras cargar fuentes e imágenes ---------- */
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => ScrollTrigger.refresh());
  window.addEventListener('load', () => ScrollTrigger.refresh());

  /* ---------- Limpieza ---------- */
  window.addEventListener('pagehide', () => {
    mm.revert();
    ScrollTrigger.getAll().forEach((t) => t.kill());
    if (lenis) lenis.destroy();
  });
})();

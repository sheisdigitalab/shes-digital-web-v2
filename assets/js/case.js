/* She's Digital · Caso de estudio — movimiento propio de la página
   Se apoya en main.js (GSAP, ScrollTrigger y Lenis ya iniciados) */
(function () {
  'use strict';
  if (typeof window.gsap === 'undefined' || typeof window.ScrollTrigger === 'undefined') return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const mm = gsap.matchMedia();

  /* ---------- Portada: de tarjeta a sangre completa ---------- */
  const cover = document.querySelector('[data-cover]');
  if (cover) {
    const gutter = parseFloat(getComputedStyle(document.querySelector('.wrap')).paddingLeft) || 16;
    gsap.fromTo(cover,
      { clipPath: `inset(0px ${gutter}px 0px ${gutter}px round 20px)` },
      { clipPath: 'inset(0px 0px 0px 0px round 0px)', ease: 'none',
        scrollTrigger: { trigger: cover, start: 'top 80%', end: 'top 10%', scrub: true } });
    gsap.fromTo(cover.querySelector('img'), { yPercent: 0, scale: 1.06 }, {
      yPercent: 8, scale: 1, ease: 'none',
      scrollTrigger: { trigger: cover, start: 'top 80%', end: 'bottom top', scrub: true }
    });
  }

  /* ---------- Recorrido: la captura completa avanza con el scroll ---------- */
  const tour = document.querySelector('[data-tour]');
  if (tour) {
    const screen = tour.querySelector('[data-tour-screen]');
    const img = tour.querySelector('[data-tour-img]');
    const steps = Array.from(tour.querySelectorAll('[data-tour-steps] li'));
    const travel = () => Math.max(0, img.offsetHeight - screen.clientHeight);
    const mark = (p) => {
      const i = Math.min(steps.length - 1, Math.floor(p * steps.length));
      steps.forEach((s, k) => s.classList.toggle('is-active', k === i));
    };
    // La imagen es lazy: hay que medir cuando ya tiene altura real
    img.loading = 'eager';

    mm.add('(min-width: 1024px)', () => {
      gsap.to(img, {
        y: () => -travel(), ease: 'none',
        scrollTrigger: {
          trigger: tour, start: 'top top', end: () => '+=' + Math.round(travel() * 0.55),
          pin: true, scrub: 1, invalidateOnRefresh: true,
          onUpdate: (self) => mark(self.progress)
        }
      });
    });
    mm.add('(max-width: 1023px)', () => {
      gsap.to(img, {
        y: () => -travel(), ease: 'none',
        scrollTrigger: {
          trigger: screen, start: 'top 75%', end: 'bottom 25%', scrub: 1, invalidateOnRefresh: true,
          onUpdate: (self) => mark(self.progress)
        }
      });
    });
    if (img.complete) ScrollTrigger.refresh(); else img.addEventListener('load', () => ScrollTrigger.refresh(), { once: true });
  }

  /* ---------- Imágenes que se acercan al entrar ---------- */
  document.querySelectorAll('[data-zoom] img').forEach((el) => {
    gsap.fromTo(el, { scale: 1.12 }, {
      scale: 1, ease: 'none',
      scrollTrigger: { trigger: el.parentElement, start: 'top bottom', end: 'center center', scrub: true }
    });
  });

  /* ---------- Móviles a distintas velocidades ---------- */
  mm.add('(min-width: 768px)', () => {
    const speeds = [-10, 8, -6, 12];
    document.querySelectorAll('[data-phone]').forEach((el) => {
      gsap.fromTo(el, { yPercent: 0 }, {
        yPercent: speeds[Number(el.dataset.phone)] || 0, ease: 'none',
        scrollTrigger: { trigger: '.cs-phones', start: 'top bottom', end: 'bottom top', scrub: true }
      });
    });
  });

  ScrollTrigger.sort();
  ScrollTrigger.refresh();
})();

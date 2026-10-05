/* She's Digital · Páginas de servicio — movimiento propio
   Se apoya en main.js (GSAP, ScrollTrigger y Lenis ya iniciados) */
(function () {
  'use strict';
  if (typeof window.gsap === 'undefined' || typeof window.ScrollTrigger === 'undefined') return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (document.documentElement.classList.contains('reduce-motion')) return;

  /* Tira de proyectos: avanza con el scroll, nunca sola */
  const strip = document.querySelector('[data-strip]');
  if (strip) {
    gsap.to(strip, {
      x: () => -Math.max(0, strip.scrollWidth - window.innerWidth),
      ease: 'none',
      scrollTrigger: { trigger: strip, start: 'top bottom', end: 'bottom top', scrub: true, invalidateOnRefresh: true }
    });
    // Con teclado, el enlace enfocado tiene que quedar a la vista
    strip.addEventListener('focusin', (e) => {
      const li = e.target.closest('li');
      if (!li) return;
      const r = li.getBoundingClientRect();
      if (r.left < 0 || r.right > window.innerWidth) {
        gsap.set(strip, { x: Math.min(0, -(li.offsetLeft - 24)) });
      }
      strip.parentElement.scrollLeft = 0;
    });
  }

  ScrollTrigger.sort();
  ScrollTrigger.refresh();
})();

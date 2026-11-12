(function () {
  'use strict';

  /* 1 · data-nav en el header de navegación */
  document.querySelectorAll('.nav').forEach(function (el) {
    if (!el.hasAttribute('data-nav')) el.setAttribute('data-nav', '');
  });

  /* 2 · data-reveal en elementos con entrada por scroll */
  document.querySelectorAll(
    '.eyebrow, .hero__lead, .hero__actions, .hero__sub, .hero__founder,' +
    '.trust, .v3-title, .v3-guar,' +
    '.ps-lead, .ps-panels,' +
    '.reviews__rating, .reviews__grid, .reviews__cta-wrap,' +
    '.about__copy p,' +
    '.process__steps .step,' +
    '.faq__list .qa,' +
    '.contact__lead, .contact__direct, .form'
  ).forEach(function (el) {
    if (!el.hasAttribute('data-reveal')) el.setAttribute('data-reveal', '');
  });

  /* 3 · data-hero en el copy del hero */
  document.querySelectorAll(
    '.hero__status, .hero__lead, .hero__actions, .hero__sub, .hero__founder'
  ).forEach(function (el) {
    if (!el.hasAttribute('data-hero')) el.setAttribute('data-hero', 'fade');
  });

  /* 4 · data-split en headings animados (excluye el H1 que ya lo tiene en su HTML) */
  document.querySelectorAll(
    '.v3-title, .about__copy .h2, .contact__intro .h2, ' +
    '.reviews .h2, .process .h2, .faq .h2, .work .h2'
  ).forEach(function (el) {
    if (!el.hasAttribute('data-split')) el.setAttribute('data-split', '');
  });

  /* 5 · data-parallax en la foto del about */
  document.querySelectorAll('.about__media').forEach(function (el) {
    if (!el.hasAttribute('data-parallax')) el.setAttribute('data-parallax', '');
  });

  /* 6 · data-process-line */
  document.querySelectorAll('.process__line span').forEach(function (el) {
    if (!el.hasAttribute('data-process-line')) el.setAttribute('data-process-line', '');
  });

  /* 7 · .qa__icon inyectado en cada <summary> del FAQ */
  document.querySelectorAll('.qa summary').forEach(function (s) {
    if (!s.querySelector('.qa__icon')) {
      var icon = document.createElement('span');
      icon.className = 'qa__icon';
      icon.setAttribute('aria-hidden', 'true');
      s.appendChild(icon);
    }
  });

  /* 8 · aria-label en la barra de confianza */
  document.querySelectorAll('.trust').forEach(function (el) {
    if (!el.getAttribute('aria-label')) {
      el.setAttribute('aria-label', 'Por qué trabajar con She’s Digital');
    }
  });

  /* 9 · aria-labelledby en secciones principales */
  var sectionMap = {
    'servicios': 'services-title',
    'proyectos': 'work-title',
    'resenas':   'reviews-title',
    'sobre-mi':  'about-title',
    'proceso':   'process-title',
    'faq':       'faq-title',
    'contacto':  'contact-title'
  };
  Object.keys(sectionMap).forEach(function (id) {
    var sec = document.getElementById(id);
    if (sec && !sec.getAttribute('aria-labelledby')) {
      sec.setAttribute('aria-labelledby', sectionMap[id]);
    }
  });

  /* 10 · data-cursor en el badge magnético del cursor */
  document.querySelectorAll('.cursor-badge').forEach(function (el) {
    if (!el.hasAttribute('data-cursor')) el.setAttribute('data-cursor', '');
  });

})();

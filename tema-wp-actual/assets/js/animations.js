document.addEventListener('DOMContentLoaded', function () {

  // ── Scroll reveal para elementos con clase .sd-reveal ──
  const reveals = document.querySelectorAll('.sd-reveal');
  if ( reveals.length ) {
    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if ( entry.isIntersecting ) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    reveals.forEach(function (el) { observer.observe(el); });
  }

  // ── Smooth scroll para links internos ──
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if ( target ) {
        e.preventDefault();
        const offset = document.querySelector('#main-header')
          ? document.querySelector('#main-header').offsetHeight
          : 80;
        window.scrollTo({
          top: target.getBoundingClientRect().top + window.scrollY - offset,
          behavior: 'smooth'
        });
      }
    });
  });

  // ── Nav sombra al hacer scroll ──
  const header = document.querySelector('#main-header');
  if ( header ) {
    window.addEventListener('scroll', function () {
      if ( window.scrollY > 20 ) {
        header.style.boxShadow = '0 2px 20px rgba(30,36,32,0.08)';
      } else {
        header.style.boxShadow = 'none';
      }
    });
  }

});

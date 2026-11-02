/* ============================================================
   She's Digital · service-v3.js
   Animaciones para páginas de servicio v3
   ============================================================ */

/* ---- Tabs: agentes-ia (WhatsApp) ---- */
(function () {
  var chat = document.getElementById('sv3-chat');
  if (!chat) return;

  var D = {
    pelu: {av:'P', biz:'Peluquería · Asistente', m:[
      ['sv3-msg-in','Hola! Tenéis hueco mañana para corte?','22:47'],
      ['sv3-msg-out','¡Hola! Mañana tengo libre a las 10:30 y a las 17:00. ¿Cuál te va mejor?','22:47',true],
      ['sv3-msg-in','A las 17 perfecto','22:48'],
      ['sv3-msg-out','Reservado: mañana a las 17:00 ✓ Te escribo por la mañana para recordártelo.','22:48']]},
    taller: {av:'T', biz:'Taller · Asistente', m:[
      ['sv3-msg-in','Hola, el coche hace un ruido raro al frenar','22:47'],
      ['sv3-msg-out','Hola. Mejor que lo vea un mecánico. ¿Te va bien traerlo el jueves a las 9:00?','22:47',true],
      ['sv3-msg-in','Sí, el jueves','22:48'],
      ['sv3-msg-out','Apuntado: jueves a las 9:00 ✓ Si me dices modelo y matrícula, lo dejo anotado.','22:48']]},
    clinica: {av:'C', biz:'Clínica · Asistente', m:[
      ['sv3-msg-in','¿Hacéis primera visita de fisio esta semana?','22:47'],
      ['sv3-msg-out','Sí. Tengo el miércoles a las 18:30 o el viernes a las 10:00. ¿Cuál prefieres?','22:47',true],
      ['sv3-msg-in','Miércoles','22:48'],
      ['sv3-msg-out','Reservado: miércoles a las 18:30 ✓ Te envío la dirección y cómo llegar.','22:48']]},
    taxi: {av:'T', biz:'Taxi · Asistente', m:[
      ['sv3-msg-in','Hola, necesito un taxi mañana a las 6 para ir al aeropuerto','22:47'],
      ['sv3-msg-out','¡Hola! Sí, hay disponibilidad. ¿Desde qué dirección te recogemos y cuántas personas sois?','22:47',true],
      ['sv3-msg-in','Calle Mayor 12. Somos 2, con maletas','22:48'],
      ['sv3-msg-out','Reservado: mañana a las 6:00 en Calle Mayor 12, para 2 con maletas ✓ Antes de salir te enviamos el nombre del conductor y la matrícula.','22:48']]},
    resto: {av:'R', biz:'Restaurante · Asistente', m:[
      ['sv3-msg-in','Mesa para 4 el sábado por la noche?','22:47'],
      ['sv3-msg-out','Hay mesa a las 21:00 o a las 22:00. ¿Cuál os va mejor?','22:47',true],
      ['sv3-msg-in','21:00','22:48'],
      ['sv3-msg-out','Reservado: sábado a las 21:00 para 4 ✓ Si alguien tiene alergias, dímelo y lo anoto.','22:48']]}
  };

  function esc(t) { return t.replace(/[&<>]/g, function(c){ return({'&':'&amp;','<':'&lt;','>':'&gt;'})[c]; }); }

  function show(k) {
    var d = D[k]; if (!d) return;
    document.getElementById('sv3-av').textContent = d.av;
    document.getElementById('sv3-biz').textContent = d.biz;
    var a=d.m[0],b=d.m[1],c=d.m[2],e=d.m[3];
    chat.innerHTML =
      '<span class="sv3-day">Hoy</span>' +
      '<div class="sv3-msg sv3-msg-in s1">' + esc(a[1]) + '<time>' + a[2] + '</time></div>' +
      '<div class="sv3-typing t1"><i></i><i></i><i></i></div>' +
      '<div class="sv3-msg sv3-msg-out s2"><span class="sv3-tag">Asistente automático</span>' + esc(b[1]) + '<time>' + b[2] + '</time></div>' +
      '<div class="sv3-msg sv3-msg-in s3">' + esc(c[1]) + '<time>' + c[2] + '</time></div>' +
      '<div class="sv3-typing t2"><i></i><i></i><i></i></div>' +
      '<div class="sv3-msg sv3-msg-out s4">' + esc(e[1]) + '<time>' + e[2] + '</time></div>';
  }

  document.querySelectorAll('.sv3-tabs--ia button').forEach(function(btn) {
    btn.addEventListener('click', function() {
      document.querySelectorAll('.sv3-tabs--ia button').forEach(function(x) {
        x.setAttribute('aria-selected', x === btn ? 'true' : 'false');
      });
      show(btn.dataset.k);
    });
  });
})();

/* ---- Tabs: apps-a-medida (CRM) ---- */
(function () {
  var appRows = document.getElementById('sv3-app-rows');
  if (!appRows) return;

  var D = {
    taxi: {t:'Reservas de hoy', q:'Buscar reserva…', f:['Hoy 14','Pendientes 3','Asignadas 9'], r:[
      ['06:00','Aeropuerto BCN','2 personas · maletas','Asignada','c',true],
      ['09:30','Hotel → Estación','1 persona','Pendiente','p',false],
      ['13:15','Aeropuerto GRO','4 personas · silla bebé','Asignada','c',false],
      ['18:40','Restaurante → Hotel','3 personas','Pagada','d',false]]},
    reformas: {t:'Clientes', q:'Buscar cliente…', f:['Todos 24','Presupuesto 5','En curso 8'], r:[
      ['MG','Marta Gil','Reforma cocina','Presupuesto','p',false],
      ['CP','Comunidad Prats','Fachada y portal','En curso','c',false],
      ['JR','Jordi Ruiz','Baño completo','Cerrado','d',false],
      ['LC','Laura Costa','Llamar el lunes','Presupuesto','p',false]]}
  };

  function show(k) {
    var d = D[k]; if (!d) return;
    document.getElementById('sv3-app-title').textContent = d.t;
    document.getElementById('sv3-app-search').textContent = d.q;
    document.getElementById('sv3-app-filters').innerHTML = d.f.map(function(x,i){
      return '<span' + (i===0?' class="sv3-on"':'') + '>' + x + '</span>';
    }).join('');
    appRows.innerHTML = d.r.map(function(x,i){
      return '<li class="r' + (i+1) + '">' +
        '<i' + (k==='taxi'?' class="sv3-hr"':'') + '>' + x[0] + '</i>' +
        '<div><b>' + x[1] + '</b><small>' + x[2] + '</small></div>' +
        '<span class="sv3-st sv3-st--' + x[4] + '">' + x[3] + '</span></li>';
    }).join('');
  }

  document.querySelectorAll('.sv3-tabs--apps button').forEach(function(btn) {
    btn.addEventListener('click', function() {
      document.querySelectorAll('.sv3-tabs--apps button').forEach(function(x) {
        x.setAttribute('aria-selected', x === btn ? 'true' : 'false');
      });
      show(btn.dataset.k);
    });
  });

  show('taxi');
})();

/* ---- Project window carousel (diseno-web) ---- */
(function () {
  var images = [].slice.call(document.querySelectorAll('.sv3-cyc'));
  if (images.length < 2) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) { if(images[0]) images[0].classList.add('sv3-on'); return; }

  var dots = [].slice.call(document.querySelectorAll('.sv3-cyc-dots span'));
  var urlEl = document.getElementById('sv3-cyc-url');
  var tagEl = document.getElementById('sv3-cyc-tag');
  var i = 0;

  images[0].classList.add('sv3-on');
  if (dots[0]) dots[0].classList.add('sv3-on');

  setInterval(function() {
    images[i].classList.remove('sv3-on');
    if (dots[i]) dots[i].classList.remove('sv3-on');
    i = (i + 1) % images.length;
    images[i].classList.add('sv3-on');
    if (dots[i]) dots[i].classList.add('sv3-on');
    if (urlEl) { urlEl.style.opacity = '0'; setTimeout(function(){ urlEl.textContent = images[i].dataset.url || ''; urlEl.style.opacity = '1'; }, 250); }
    if (tagEl) tagEl.textContent = images[i].dataset.tag || '';
  }, 3000);
})();

/* ---- Steps scroll animation ---- */
(function () {
  var rm = matchMedia('(prefers-reduced-motion: reduce)').matches;

  function apply(el, p) {
    el.style.setProperty('--p', p.toFixed(3));
    var steps = el.querySelectorAll('.sv3-step'), n = steps.length;
    steps.forEach(function(s, i) {
      var on = p >= (n > 1 ? i / (n - 1) * 0.97 : 0) + 0.001;
      s.classList.toggle('sv3-on', on);
      s.classList.toggle('sv3-done', on && i === n - 1 && p >= 0.99);
    });
  }

  function go() {
    var all = [].slice.call(document.querySelectorAll('.sv3-steps'));

    function fit() {
      all.forEach(function(el) {
        var bs = el.querySelectorAll('.sv3-step b');
        if (!bs.length) return;
        var r = el.getBoundingClientRect(), l = bs[bs.length - 1].getBoundingClientRect();
        el.style.setProperty('--end', Math.max(0, r.right - (l.left + l.width / 2)) + 'px');
      });
    }

    all.forEach(function(el) {
      if (!el.querySelector('.sv3-fill')) {
        var f = document.createElement('span');
        f.className = 'sv3-fill';
        f.setAttribute('aria-hidden', 'true');
        el.prepend(f);
      }
      if (rm || !('IntersectionObserver' in window)) { apply(el, 1); return; }

      var s = document.createElement('span');
      s.setAttribute('aria-hidden', 'true');
      s.style.cssText = 'position:absolute;left:0;width:1px;top:0;height:max(480px,100%);pointer-events:none;visibility:hidden';
      el.appendChild(s);

      var th = [];
      for (var k = 0; k <= 100; k++) th.push(k / 100);
      apply(el, 0);

      new IntersectionObserver(function(es) {
        es.forEach(function(e) {
          var leavingTop = e.intersectionRect.top > e.boundingClientRect.top + 2 && e.isIntersecting;
          var p = leavingTop ? 1 : Math.min(1, e.intersectionRatio / 0.96);
          if (!e.isIntersecting) p = e.boundingClientRect.top < 0 ? 1 : 0;
          apply(el, p);
        });
      }, {threshold: th}).observe(s);
    });

    fit();
    addEventListener('resize', fit);
  }

  if (document.readyState !== 'loading') go();
  else document.addEventListener('DOMContentLoaded', go);
})();

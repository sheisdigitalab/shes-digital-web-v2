/* COOKIE BANNER — RGPD */
(function () {
  'use strict';
  const STORAGE_KEY = 'shesdigital_cookie_consent';
  const banner = document.getElementById('cookieBanner');
  const reopenBtn = document.querySelector('.cookie-reopen');
  if (!banner) return;

  function getConsent() {
    try { const raw = localStorage.getItem(STORAGE_KEY); return raw ? JSON.parse(raw) : null; } catch (e) { return null; }
  }
  function saveConsent(state) {
    const data = { ...state, ts: Date.now(), version: 1 };
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(data)); } catch (e) {}
    applyConsent(data);
  }

  const GA_ID = 'G-KREXLL4QX2';
  let gaLoaded = false;
  function loadGA() {
    if (gaLoaded) return; gaLoaded = true;
    const s = document.createElement('script'); s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date()); window.gtag('config', GA_ID);
  }
  function applyConsent(state) {
    window.__cookieConsent = { analytics: !!state.analytics };
    if (state.analytics) loadGA();
  }
  function showBanner() {
    banner.hidden = false;
    requestAnimationFrame(() => banner.classList.add('is-visible'));
    if (reopenBtn) reopenBtn.hidden = true;
  }
  function hideBanner() {
    banner.classList.remove('is-visible');
    setTimeout(() => { banner.hidden = true; if (reopenBtn) reopenBtn.hidden = false; }, 300);
  }
  function handleAction(action) {
    if (action === 'accept') { saveConsent({ necessary: true, analytics: true }); hideBanner(); }
    else if (action === 'reject') { saveConsent({ necessary: true, analytics: false }); hideBanner(); }
    else if (action === 'config') { window.location.href = 'https://sheisdigitalab.com/legal/cookies/'; }
    else if (action === 'reopen') { showBanner(); }
  }
  document.querySelectorAll('[data-cookie-action]').forEach((el) => {
    el.addEventListener('click', () => handleAction(el.dataset.cookieAction));
  });
  const consent = getConsent();
  if (!consent) { setTimeout(showBanner, 800); }
  else { applyConsent(consent); if (reopenBtn) reopenBtn.hidden = false; }
})();

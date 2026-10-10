/* Reserve the real bar height, including safe areas and enlarged text. No cart requests. */
(() => {
  if (window.gujjuMobileBottomBarLoaded) return;
  window.gujjuMobileBottomBarLoaded = true;
  const instances = new Map();
  function sync() {
    document.body.classList.toggle('has-mobile-bottom-bar', instances.size > 0);
    const height = Math.max(0, ...[...instances.keys()].map(bar => bar.getBoundingClientRect().height));
    if (instances.size) document.body.style.setProperty('--mobile-bottom-bar-height', `${Math.ceil(height)}px`);
    else document.body.style.removeProperty('--mobile-bottom-bar-height');
  }
  function init() {
    document.querySelectorAll('[data-mobile-bottom-bar]').forEach(bar => {
      if (instances.has(bar)) return;
      const observer = typeof ResizeObserver === 'function' ? new ResizeObserver(sync) : null;
      instances.set(bar, observer);
      observer?.observe(bar);
    });
    sync();
  }
  document.addEventListener('shopify:section:load', init);
  document.addEventListener('shopify:section:unload', event => {
    instances.forEach((observer, bar) => {
      if (!event.target.contains(bar)) return;
      observer?.disconnect();
      instances.delete(bar);
    });
    sync();
  });
  window.addEventListener('resize', sync, { passive: true });
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();

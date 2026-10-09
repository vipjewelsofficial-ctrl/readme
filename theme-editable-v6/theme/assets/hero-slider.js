/* Scoped carousel; its settings are supplied by Shopify. No cart/checkout hooks. */
(() => {
  if (window.gujjuHeroSliderLoaded) return;
  window.gujjuHeroSliderLoaded = true;
  const instances = new WeakMap();
  function init(scope = document) {
    const roots = [...(scope.matches?.('[data-hero-slider]') ? [scope] : []), ...scope.querySelectorAll('[data-hero-slider]')];
    roots.forEach(root => {
      if (instances.has(root)) return;
      const slides = [...root.querySelectorAll('[data-hero-slide]')];
      if (slides.length < 2) return;
      const dots = [...root.querySelectorAll('[data-slide-index]')];
      const pauseButton = root.querySelector('[data-slider-pause]');
      const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
      const controller = new AbortController();
      const opts = { signal: controller.signal };
      let index = 0, timer, hovered = false, touch;
      let paused = motion.matches;
      function schedule() {
        clearInterval(timer);
        if (root.dataset.autoplay === 'true' && !paused && !hovered && !document.hidden && !root.contains(document.activeElement) && !window.Shopify?.designMode) {
          timer = setInterval(() => show(index + 1), Number(root.dataset.interval || 5000));
        }
        if (pauseButton) {
          pauseButton.setAttribute('aria-pressed', String(paused));
          pauseButton.textContent = paused ? root.dataset.playLabel : root.dataset.pauseLabel;
        }
      }
      function show(next) {
        index = (next + slides.length) % slides.length;
        slides.forEach((slide, i) => { slide.hidden = i !== index; });
        dots.forEach((dot, i) => dot.setAttribute('aria-current', String(i === index)));
        const status = root.querySelector('[data-slider-status]');
        if (status) status.textContent = `${index + 1} / ${slides.length}`;
        schedule();
      }
      root.querySelector('[data-slider-prev]')?.addEventListener('click', () => show(index - 1), opts);
      root.querySelector('[data-slider-next]')?.addEventListener('click', () => show(index + 1), opts);
      dots.forEach(dot => dot.addEventListener('click', () => show(Number(dot.dataset.slideIndex)), opts));
      pauseButton?.addEventListener('click', () => { paused = !paused; schedule(); }, opts);
      root.addEventListener('mouseenter', () => { hovered = true; schedule(); }, opts);
      root.addEventListener('mouseleave', () => { hovered = false; schedule(); }, opts);
      root.addEventListener('focusin', schedule, opts);
      root.addEventListener('focusout', () => setTimeout(schedule, 0), opts);
      root.addEventListener('keydown', event => {
        if (event.target.matches('input,textarea,select')) return;
        if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
          event.preventDefault(); show(index + (event.key === 'ArrowRight' ? 1 : -1));
        }
      }, opts);
      root.addEventListener('touchstart', event => { touch = event.touches[0]; }, { ...opts, passive: true });
      root.addEventListener('touchend', event => {
        if (!touch) return;
        const end = event.changedTouches[0], dx = end.clientX - touch.clientX, dy = end.clientY - touch.clientY;
        if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy)) show(index + (dx < 0 ? 1 : -1));
        touch = null;
      }, { ...opts, passive: true });
      document.addEventListener('visibilitychange', schedule, opts);
      motion.addEventListener('change', () => { if (motion.matches) paused = true; schedule(); }, opts);
      document.addEventListener('shopify:block:select', event => {
        const selected = slides.findIndex(slide => slide.dataset.blockId === event.detail.blockId);
        if (selected >= 0) { paused = true; show(selected); }
      }, opts);
      const destroy = () => { clearInterval(timer); controller.abort(); instances.delete(root); };
      document.addEventListener('shopify:section:unload', event => { if (event.target.contains(root)) destroy(); }, opts);
      instances.set(root, { destroy });
      show(0);
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', () => init());
  else init();
  document.addEventListener('shopify:section:load', event => init(event.target));
})();

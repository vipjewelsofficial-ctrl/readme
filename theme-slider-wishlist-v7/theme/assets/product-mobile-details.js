/* Progressive mobile product enhancements. Cart submission stays on Shopify's native form. */
(() => {
  if (window.gujjuMobileProductInitialized) return;
  window.gujjuMobileProductInitialized = true;

  function initStickyCart(scope = document) {
    scope.querySelectorAll('[data-mobile-sticky-cart]').forEach(bar => {
      if (bar.dataset.initialized === 'true') return;
      const form = document.getElementById(bar.dataset.productFormId);
      const primary = form?.querySelector('[data-product-submit]');
      const sticky = bar.querySelector('button');
      if (!primary || !sticky) return;
      bar.dataset.initialized = 'true';
      const mobile = window.matchMedia('(max-width: 989px)');
      let frame;

      const syncButton = () => {
        sticky.textContent = primary.textContent.trim();
        sticky.disabled = primary.disabled;
        sticky.setAttribute('aria-disabled', String(primary.disabled));
      };
      const updateVisibility = () => {
        bar.hidden = !mobile.matches || primary.getBoundingClientRect().bottom >= 0;
      };
      const onScroll = () => {
        if (frame) return;
        frame = requestAnimationFrame(() => { frame = null; updateVisibility(); });
      };
      const observer = new MutationObserver(syncButton);
      observer.observe(primary, { attributes: true, attributeFilter: ['disabled'], childList: true, subtree: true, characterData: true });
      window.addEventListener('scroll', onScroll, { passive: true });
      window.addEventListener('resize', onScroll, { passive: true });
      mobile.addEventListener('change', updateVisibility);
      syncButton();
      updateVisibility();

      const onUnload = event => {
        if (!event.target.contains(bar)) return;
        observer.disconnect();
        window.removeEventListener('scroll', onScroll);
        window.removeEventListener('resize', onScroll);
        mobile.removeEventListener('change', updateVisibility);
        if (frame) cancelAnimationFrame(frame);
        document.removeEventListener('shopify:section:unload', onUnload);
      };
      document.addEventListener('shopify:section:unload', onUnload);
    });
  }

  function initRecommendations(scope = document) {
    scope.querySelectorAll('[data-mobile-product-recommendations]').forEach(container => {
      if (container.dataset.initialized === 'true') return;
      container.dataset.initialized = 'true';
      if (container.dataset.mode === 'manual') return;
      let requested = false;
      const load = async () => {
        if (requested) return;
        requested = true;
        try {
          const response = await fetch(container.dataset.url);
          if (!response.ok) throw new Error('Recommendations unavailable');
          const html = new DOMParser().parseFromString(await response.text(), 'text/html');
          const content = html.querySelector('[data-recommendation-content]');
          if (container.isConnected && content) container.replaceChildren(content);
        } catch (error) {
          // Keep the server-rendered same-collection fallback; cart access is unaffected.
          if (window.Shopify?.designMode) console.warn('Product recommendations:', error);
        }
      };
      const onUnload = event => {
        if (!event.target.contains(container)) return;
        document.removeEventListener('shopify:section:unload', onUnload);
      };
      document.addEventListener('shopify:section:unload', onUnload);
      load();
    });
  }

  function initFooter(scope = document) {
    if (!document.body.classList.contains('template-product')) return;
    scope.querySelectorAll('.site-footer .footer-top').forEach(footer => {
      if (footer.closest('.site-footer')?.dataset.productAccordion === 'false') return;
      const initiallyOpen = footer.closest('.site-footer')?.dataset.accordionOpen === 'true';
      if (footer.dataset.productDisclosureInitialized === 'true') return;
      footer.dataset.productDisclosureInitialized = 'true';
      const mobile = window.matchMedia('(max-width: 989px)');
      const disclosures = [];
      footer.querySelectorAll('.footer-nav').forEach(column => {
        const details = document.createElement('details');
        details.className = 'product-footer-disclosure';
        const summary = document.createElement('summary');
        summary.className = 'product-footer-disclosure__summary';
        summary.textContent = column.querySelector('.footer-nav__title')?.textContent || 'About Gujju Jewels';
        const content = document.createElement('div');
        content.className = 'product-footer-disclosure__content';
        column.replaceWith(details);
        content.append(column);
        details.append(summary, content);
        details.open = !mobile.matches || initiallyOpen;
        disclosures.push(details);
      });
      const onChange = () => disclosures.forEach(details => { details.open = !mobile.matches || initiallyOpen; });
      const onUnload = event => {
        if (!event.target.contains(footer)) return;
        mobile.removeEventListener('change', onChange);
        document.removeEventListener('shopify:section:unload', onUnload);
      };
      mobile.addEventListener('change', onChange);
      document.addEventListener('shopify:section:unload', onUnload);
    });
  }

  function init(scope = document) {
    initStickyCart(scope);
    initRecommendations(scope);
    initFooter(scope);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', () => init());
  else init();
  document.addEventListener('shopify:section:load', event => init(event.target));
})();

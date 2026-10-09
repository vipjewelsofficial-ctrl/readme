/* Save cart quantities through Shopify and use server-rendered prices/discounts. */
(() => {
  if (window.vipCartQuantityInitialized) return;
  window.vipCartQuantityInitialized = true;
  const states = new WeakMap();

  function properties(value) {
    const pairs = Array.isArray(value) ? value : Object.entries(value || {});
    return pairs.map(([key, item]) => [String(key), String(item)]).sort((a, b) => a[0].localeCompare(b[0]));
  }
  function identity(variant, props, plan) {
    return JSON.stringify([String(variant), properties(props), String(plan || '')]);
  }
  function rowIdentity(row) {
    return identity(row.dataset.cartVariantId, JSON.parse(row.dataset.cartProperties || '{}'), row.dataset.cartSellingPlan);
  }
  function itemIdentity(item) {
    return identity(item.variant_id, item.properties, item.selling_plan_allocation?.selling_plan?.id);
  }
  function enhance(scope = document) {
    scope.querySelectorAll('[data-cart-section]').forEach(root => {
      if (!states.has(root)) states.set(root, { pending: new Map(), timer: null, running: false, checkout: false });
      root.querySelectorAll('.cart-quantity__buttons').forEach(buttons => {
        buttons.hidden = false;
        buttons.parentElement.classList.add('cart-quantity-control--enhanced');
      });
    });
  }
  function message(root, text, visible = false) {
    const status = root.querySelector('[data-cart-status]');
    if (!status) return;
    status.hidden = !text;
    status.classList.toggle('visually-hidden', !visible);
    status.textContent = text;
  }
  function busy(root, active) {
    root.querySelector('.cart-form')?.setAttribute('aria-busy', String(active));
    root.querySelectorAll('[data-cart-quantity], [data-cart-delta], [name="checkout"]').forEach(control => { control.disabled = active; });
    root.querySelectorAll('.cart-line__remove').forEach(link => {
      if (active) link.setAttribute('aria-disabled', 'true');
      else link.removeAttribute('aria-disabled');
    });
  }
  function restoreInputs(root) {
    root.querySelectorAll('[data-cart-quantity]').forEach(input => { input.value = input.dataset.savedQuantity; });
  }
  function quantity(input) {
    return /^\d+$/.test(input.value) && Number.isSafeInteger(Number(input.value)) ? Number(input.value) : null;
  }
  function queue(input, delay) {
    const root = input.closest('[data-cart-section]');
    const state = states.get(root);
    if (!state || state.running) return;
    const row = input.closest('[data-cart-line]');
    const id = row.dataset.cartKey;
    const value = quantity(input);
    if (value === null) {
      state.pending.delete(id);
      clearTimeout(state.timer);
      state.timer = state.pending.size ? setTimeout(() => flush(root, state), delay) : null;
      return;
    }
    input.removeAttribute('data-invalid-quantity');
    message(root, '');
    if (value === Number(input.dataset.savedQuantity)) state.pending.delete(id);
    else state.pending.set(id, { key: id, identity: rowIdentity(row), quantity: value });
    clearTimeout(state.timer);
    state.timer = state.pending.size ? setTimeout(() => flush(root, state), delay) : null;
  }
  function render(root, html) {
    const next = new DOMParser().parseFromString(html, 'text/html').querySelector('[data-cart-section]');
    if (!next) throw new Error((window.cartStrings?.refreshError || 'Cart display could not be refreshed.'));
    root.innerHTML = next.innerHTML;
    root.querySelectorAll('.cart-quantity__buttons').forEach(buttons => {
      buttons.hidden = false;
      buttons.parentElement.classList.add('cart-quantity-control--enhanced');
    });
  }
  async function sectionHTML(root, cart) {
    const sectionId = root.dataset.sectionId;
    const valid = html => html && new DOMParser().parseFromString(html, 'text/html').querySelector('[data-cart-section]');
    if (valid(cart.sections?.[sectionId])) return cart.sections[sectionId];
    const url = new URL(root.querySelector('.cart-form')?.action || window.location.href);
    url.searchParams.set('sections', sectionId);
    const response = await fetch(url, { headers: { Accept: 'application/json' }, cache: 'no-store' });
    if (!response.ok) throw new Error((window.cartStrings?.refreshError || 'Cart display could not be refreshed.'));
    const sections = await response.json();
    if (!valid(sections[sectionId])) throw new Error((window.cartStrings?.refreshError || 'Cart display could not be refreshed.'));
    return sections[sectionId];
  }
  async function flush(root, state) {
    clearTimeout(state.timer);
    state.timer = null;
    if (state.running || !state.pending.size) return;
    state.running = true;
    busy(root, true);
    message(root, (window.cartStrings?.updating || 'Updating cart…'));
    const focused = document.activeElement;
    const focusRow = focused?.closest('[data-cart-line]');
    const focusIdentity = focusRow ? rowIdentity(focusRow) : null;
    const focusDelta = focused?.dataset.cartDelta;
    let latestCart, latestHTML, errorText = '', success = false;
    try {
      while (state.pending.size) {
        const [pendingKey, change] = state.pending.entries().next().value;
        state.pending.delete(pendingKey);
        if (latestCart) {
          const match = latestCart.items.find(item => item.key === change.key);
          const candidates = match ? [match] : latestCart.items.filter(item => itemIdentity(item) === change.identity);
          if (candidates.length !== 1) throw new Error((window.cartStrings?.changed || 'The cart changed. Please retry this quantity.'));
          change.key = candidates[0].key;
        }
        const response = await fetch(root.dataset.cartChangeUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify({ id: change.key, quantity: change.quantity, sections: [root.dataset.sectionId], sections_url: new URL(root.querySelector('.cart-form').action).pathname })
        });
        const data = await response.json();
        if (!response.ok || data.status >= 400) throw new Error(data.description || data.message || (window.cartStrings?.saveError || 'This quantity could not be saved. Please try again.'));
        latestCart = data;
        latestHTML = null;
        latestHTML = await sectionHTML(root, data);
        const updatedItem = data.items.find(item => item.key === change.key) || data.items.find(item => itemIdentity(item) === change.identity);
        if (change.quantity > 0 && (!updatedItem || updatedItem.quantity !== change.quantity)) errorText = (window.cartStrings?.limited || 'The requested quantity is not available. Your cart shows the available quantity.');
      }
      success = true;
    } catch (error) {
      errorText = error instanceof TypeError ? (window.cartStrings?.connectionError || 'Your quantity change could not be confirmed. Check your connection and try again.') : error.message || (window.cartStrings?.saveError || 'Your quantity change could not be saved. Please try again.');
      state.pending.clear();
      state.checkout = false;
    } finally {
      if (root.isConnected) {
        if (latestCart && !latestHTML) {
          // A saved quantity with an unavailable section must not leave stale totals.
          window.location.reload();
        } else {
          if (latestHTML) render(root, latestHTML);
          else restoreInputs(root);
          busy(root, false);
          message(root, errorText || (window.cartStrings?.updated || 'Cart updated.'), Boolean(errorText));
          if (latestCart) document.querySelectorAll('.header-cart-count').forEach(badge => {
            badge.textContent = latestCart.item_count;
            badge.hidden = latestCart.item_count === 0;
          });
          if (focusIdentity) {
            const row = [...root.querySelectorAll('[data-cart-line]')].find(item => rowIdentity(item) === focusIdentity);
            const target = row?.querySelector(focusDelta ? `[data-cart-delta="${focusDelta}"]` : '[data-cart-quantity]') || root.querySelector('[data-cart-quantity], [name="checkout"]');
            target?.focus({ preventScroll: true });
          }
        }
      }
      if (errorText) state.checkout = false;
      state.running = false;
    }
    if (success && !errorText && state.checkout && root.isConnected) {
      state.checkout = false;
      const checkout = root.querySelector('[name="checkout"]');
      if (checkout) checkout.form.requestSubmit(checkout);
    }
  }

  document.addEventListener('click', event => {
    const arrow = event.target.closest('[data-cart-delta]');
    if (arrow) {
      const input = arrow.closest('.cart-quantity-control').querySelector('[data-cart-quantity]');
      if (input.disabled) return;
      input.value = Math.max(0, (quantity(input) ?? Number(input.dataset.savedQuantity)) + Number(arrow.dataset.cartDelta));
      queue(input, 180);
    }
    const remove = event.target.closest('.main-cart-section .cart-line__remove');
    if (remove) {
      const state = states.get(remove.closest('[data-cart-section]'));
      if (state?.running || state?.pending.size) event.preventDefault();
    }
  });
  document.addEventListener('input', event => {
    if (event.target.matches('[data-cart-quantity]')) queue(event.target, 350);
  });
  document.addEventListener('change', event => {
    if (!event.target.matches('[data-cart-quantity]')) return;
    if (quantity(event.target) === null) {
      event.target.value = event.target.dataset.savedQuantity;
      event.target.dataset.invalidQuantity = 'true';
      message(event.target.closest('[data-cart-section]'), (window.cartStrings?.invalidQuantity || 'Enter a whole-number quantity of zero or more.'), true);
    } else queue(event.target, 100);
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Enter' && event.target.matches('[data-cart-quantity]')) {
      event.preventDefault();
      queue(event.target, 0);
    }
  });
  document.addEventListener('submit', event => {
    const root = event.target.closest('[data-cart-section]');
    const state = root && states.get(root);
    if (state && [...root.querySelectorAll('[data-cart-quantity]')].some(input => quantity(input) === null || input.dataset.invalidQuantity === 'true')) {
      event.preventDefault();
      message(root, (window.cartStrings?.invalidQuantity || 'Enter a whole-number quantity of zero or more.'), true);
      return;
    }
    if (state && (state.running || state.pending.size)) {
      event.preventDefault();
      if (event.submitter?.name === 'checkout') state.checkout = true;
      flush(root, state);
    }
  });
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', () => enhance());
  else enhance();
  document.addEventListener('shopify:section:load', event => enhance(event.target));
})();

/* Browser-saved product wishlist. Independent of Shopify cart and checkout. */
(() => {
  if (window.gujjuWishlistLoaded) return;
  window.gujjuWishlistLoaded = true;
  const init = () => {
    const dialog = document.querySelector('[data-wishlist-dialog]');
    if (!dialog || typeof dialog.showModal !== 'function') return;
    const list = dialog.querySelector('[data-wishlist-list]');
    const empty = dialog.querySelector('[data-wishlist-empty]');
    const key = 'gujju-jewels:wishlist:v1';
    let opener, entries = [], scrollStyle;
    function productURL(value) {
      try {
        const url = new URL(value, location.origin);
        if (url.origin === location.origin && /\/products\/[^/]+\/?$/.test(url.pathname)) {
          // A saved product must not depend on a collection still existing.
          return url.pathname.replace(/\/collections\/[^/]+(?=\/products\/)/, '') + url.search;
        }
      } catch (_) { /* Ignore invalid stored data. */ }
      return '';
    }
    function imageURL(value) {
      if (!value) return '';
      try { const url = new URL(value, location.origin); if (['https:', 'http:'].includes(url.protocol)) return url.href; } catch (_) { /* Ignore invalid images. */ }
      return '';
    }
    function read() {
      try {
        const saved = JSON.parse(localStorage.getItem(key) || '[]');
        if (!Array.isArray(saved)) return [];
        const seen = new Set();
        return saved.slice(0, 200).filter(item => {
          if (!item || typeof item !== 'object' || !/^\d+$/.test(String(item.id)) || !productURL(item.url) || typeof item.title !== 'string' || seen.has(String(item.id))) return false;
          seen.add(String(item.id)); return true;
        }).map(item => ({ id: String(item.id), url: productURL(item.url), title: item.title.slice(0, 300), image: imageURL(item.image) }));
      } catch (_) { return []; }
    }
    function announce(text) { document.querySelectorAll('[data-wishlist-message]').forEach(el => { el.textContent = text; }); }
    function sync() {
      let refreshed = false;
      document.querySelectorAll('[data-wishlist-product]').forEach(button => {
        const item = entries.find(item => item.id === button.dataset.productId);
        const saved = Boolean(item);
        // Shopify's current product data takes precedence over browser-saved links.
        const url = productURL(button.dataset.productUrl);
        if (item && url) {
          const title = (button.dataset.productTitle || item.title).slice(0, 300);
          const image = imageURL(button.dataset.productImage);
          if (item.url !== url || item.title !== title || item.image !== image) {
            Object.assign(item, { url, title, image });
            refreshed = true;
          }
        }
        button.hidden = false;
        button.setAttribute('aria-pressed', String(saved));
        button.setAttribute('aria-label', saved ? button.dataset.removeLabel : button.dataset.addLabel);
        const label = button.querySelector('[data-wishlist-toggle-label]');
        const text = saved ? dialog.dataset.savedText : dialog.dataset.addText;
        if (label && label.textContent !== text) label.textContent = text;
      });
      document.querySelectorAll('[data-wishlist-open]').forEach(button => {
        button.hidden = false;
        button.setAttribute('aria-label', dialog.dataset.countLabel.replace('[count]', String(entries.length)));
        const count = button.querySelector('[data-wishlist-count]');
        if (count) { count.textContent = entries.length; count.hidden = entries.length === 0; }
      });
      if (refreshed) {
        try { localStorage.setItem(key, JSON.stringify(entries)); }
        catch (_) { announce(dialog.dataset.errorMessage); }
        render();
      }
    }
    function render() {
      const active = document.activeElement;
      const activeId = active?.dataset.wishlistRemove;
      const activeIndex = [...list.querySelectorAll('[data-wishlist-remove]')].indexOf(active);
      list.replaceChildren();
      empty.hidden = entries.length !== 0;
      entries.forEach(item => {
        const row = document.createElement('li'); row.className = 'wishlist-dialog__item';
        const imageLink = document.createElement('a'); imageLink.href = item.url; imageLink.tabIndex = -1; imageLink.setAttribute('aria-hidden', 'true');
        const photo = document.createElement(item.image ? 'img' : 'span'); photo.className = 'wishlist-dialog__image';
        if (item.image) { photo.src = item.image; photo.alt = ''; photo.loading = 'lazy'; photo.width = 90; photo.height = 110; }
        imageLink.append(photo);
        const content = document.createElement('div');
        const title = document.createElement('a'); title.className = 'wishlist-dialog__title'; title.href = item.url; title.textContent = item.title;
        const actions = document.createElement('div'); actions.className = 'wishlist-dialog__actions';
        const view = document.createElement('a'); view.href = item.url; view.textContent = dialog.dataset.viewLabel;
        const remove = document.createElement('button'); remove.type = 'button'; remove.dataset.wishlistRemove = item.id; remove.textContent = dialog.dataset.removeLabel; remove.setAttribute('aria-label', `${dialog.dataset.removeLabel}: ${item.title}`);
        actions.append(view, remove); content.append(title, actions); row.append(imageLink, content); list.append(row);
      });
      if (activeId && dialog.open) {
        const buttons = [...list.querySelectorAll('[data-wishlist-remove]')];
        (buttons.find(b => b.dataset.wishlistRemove === activeId) || buttons[Math.min(activeIndex, buttons.length - 1)] || dialog.querySelector('[data-wishlist-close]')).focus();
      }
    }
    function save(next, message) {
      try { localStorage.setItem(key, JSON.stringify(next)); }
      catch (_) { announce(dialog.dataset.errorMessage); return; }
      entries = next; sync(); render(); announce(message);
    }
    document.addEventListener('click', event => {
      const toggle = event.target.closest('[data-wishlist-product]');
      if (toggle) {
        const id = toggle.dataset.productId;
        const existing = entries.some(item => item.id === id);
        if (existing) save(entries.filter(item => item.id !== id), dialog.dataset.removedMessage);
        else {
          if (entries.length >= 200) { announce(dialog.dataset.limitMessage); return; }
          const url = productURL(toggle.dataset.productUrl);
          if (!/^\d+$/.test(id) || !url) return;
          save([...entries, { id, url, title: (toggle.dataset.productTitle || '').slice(0, 300), image: imageURL(toggle.dataset.productImage) }], dialog.dataset.savedMessage);
        }
        return;
      }
      const open = event.target.closest('[data-wishlist-open]');
      if (open) { opener = open; sync(); render(); dialog.showModal(); scrollStyle = document.body.style.overflow; document.body.style.overflow = 'hidden'; dialog.querySelector('[data-wishlist-close]').focus(); }
      if (event.target.closest('[data-wishlist-close]')) dialog.close();
      const remove = event.target.closest('[data-wishlist-remove]');
      if (remove) save(entries.filter(item => item.id !== remove.dataset.wishlistRemove), dialog.dataset.removedMessage);
    });
    dialog.addEventListener('click', event => { if (event.target === dialog) { const box = dialog.getBoundingClientRect(); if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) dialog.close(); } });
    dialog.addEventListener('close', () => { document.body.style.overflow = scrollStyle || ''; if (opener?.isConnected) opener.focus(); });
    window.addEventListener('storage', event => { if (event.key === key || event.key === null) { entries = read(); sync(); render(); } });
    document.addEventListener('shopify:section:load', sync);
    new MutationObserver(records => {
      if (records.some(record => [...record.addedNodes].some(node => node.nodeType === 1 && (node.matches('[data-wishlist-product],[data-wishlist-open]') || node.querySelector('[data-wishlist-product],[data-wishlist-open]'))))) sync();
    }).observe(document.body, { childList: true, subtree: true });
    entries = read(); sync(); render();
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();

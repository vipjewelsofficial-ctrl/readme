/**
 * theme.js — Lightweight Vanilla JS for Modern Shopify Online Store 2.0
 * Handles Mobile Menu, Search Drawer, Sticky Header, and Quick Add
 */

function initTheme() {
  initStickyHeader();
  initMobileMenu();
  initSearchDrawer();
  initQuickAdd();
  initProductMedia();
  initProductVariants();
  initCollectionFilters();
}

document.addEventListener('DOMContentLoaded', initTheme);
document.addEventListener('shopify:section:load', initTheme);

/* 1. Sticky Header scroll effect */
function initStickyHeader() {
  const header = document.getElementById('site-header');
  if (!header || header.dataset.stickyInitialized === 'true') return;
  header.dataset.stickyInitialized = 'true';

  window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
      header.classList.add('is-scrolled');
    } else {
      header.classList.remove('is-scrolled');
    }
  }, { passive: true });
}

/* 2. Mobile Hamburger Menu Toggle */
function initMobileMenu() {
  const menuToggle = document.getElementById('mobile-menu-toggle');
  const menuClose = document.getElementById('mobile-menu-close');
  const mobileMenu = document.getElementById('mobile-menu');
  const overlay = document.getElementById('header-overlay');
  const headerSection = mobileMenu ? mobileMenu.closest('.header-section') : null;

  if (!menuToggle || !mobileMenu || menuToggle.dataset.mobileMenuInitialized === 'true') return;
  menuToggle.dataset.mobileMenuInitialized = 'true';

  let previouslyFocusedElement = null;

  function openMenu() {
    previouslyFocusedElement = document.activeElement;
    mobileMenu.removeAttribute('hidden');
    menuToggle.setAttribute('aria-expanded', 'true');
    if (headerSection) headerSection.classList.add('is-menu-open');
    if (overlay) overlay.classList.add('is-active');
    document.body.style.overflow = 'hidden';
    if (menuClose) menuClose.focus();
  }

  function closeMenu() {
    mobileMenu.setAttribute('hidden', '');
    menuToggle.setAttribute('aria-expanded', 'false');
    if (headerSection) headerSection.classList.remove('is-menu-open');
    if (overlay) overlay.classList.remove('is-active');
    document.body.style.overflow = '';
    if (previouslyFocusedElement instanceof HTMLElement) previouslyFocusedElement.focus();
  }

  menuToggle.addEventListener('click', openMenu);
  if (menuClose) menuClose.addEventListener('click', closeMenu);
  if (overlay) overlay.addEventListener('click', closeMenu);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !mobileMenu.hasAttribute('hidden')) {
      closeMenu();
    }
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 989 && !mobileMenu.hasAttribute('hidden')) {
      closeMenu();
    }
  }, { passive: true });
}

/* 3. Search Drawer Toggle */
function initSearchDrawer() {
  const searchBtn = document.getElementById('search-toggle-btn');
  const searchClose = document.getElementById('search-close-btn');
  const searchDrawer = document.getElementById('search-drawer');
  const searchInput = document.getElementById('search-input');

  if (!searchBtn || !searchDrawer || searchBtn.dataset.searchInitialized === 'true') return;
  searchBtn.dataset.searchInitialized = 'true';

  let previouslyFocusedElement = null;

  function openSearch() {
    previouslyFocusedElement = document.activeElement;
    searchDrawer.removeAttribute('hidden');
    searchBtn.setAttribute('aria-expanded', 'true');
    if (searchInput) searchInput.focus();
  }

  function closeSearch() {
    searchDrawer.setAttribute('hidden', '');
    searchBtn.setAttribute('aria-expanded', 'false');
    if (previouslyFocusedElement instanceof HTMLElement) previouslyFocusedElement.focus();
  }

  searchBtn.addEventListener('click', () => {
    const isHidden = searchDrawer.hasAttribute('hidden');
    if (isHidden) openSearch();
    else closeSearch();
  });

  if (searchClose) searchClose.addEventListener('click', closeSearch);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !searchDrawer.hasAttribute('hidden')) {
      closeSearch();
    }
  });
}

/* 4. AJAX Quick Add to Cart */
function initQuickAdd() {
  if (document.documentElement.dataset.quickAddInitialized === 'true') return;
  document.documentElement.dataset.quickAddInitialized = 'true';

  document.addEventListener('submit', async (e) => {
    const form = e.target;
    if (!form.matches('.product-card__quick-add-form')) return;

    e.preventDefault();
    const btn = form.querySelector('[data-quick-add]');
    const label = btn ? btn.querySelector('.product-card__action-label') : null;
    const originalText = label ? label.textContent : (btn ? btn.textContent : '');

    if (btn) {
      btn.disabled = true;
      btn.classList.add('is-loading');
      if (label) label.textContent = (window.themeStrings?.adding || 'Adding…');
    }

    try {
      const response = await fetch(window.routes.cart_add_url + '.js', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'X-Requested-With': 'XMLHttpRequest'
        },
        body: new URLSearchParams(new FormData(form))
      });

      if (response.ok) {
        if (btn) {
          btn.classList.remove('is-loading');
          btn.classList.add('is-added');
          if (label) label.textContent = (window.themeStrings?.added || 'Added ✓');
        }
        updateCartCount();
        setTimeout(() => {
          if (btn) {
            btn.disabled = false;
            btn.classList.remove('is-added');
            if (label) label.textContent = originalText;
          }
        }, 2000);
      } else {
        throw new Error((window.themeStrings?.addError || 'Add to cart failed'));
      }
    } catch (err) {
      console.error('Cart error:', err);
      if (btn) {
        btn.classList.remove('is-loading');
        if (label) label.textContent = (window.themeStrings?.tryAgain || 'Try again');
        setTimeout(() => {
          btn.disabled = false;
          if (label) label.textContent = originalText;
        }, 2000);
      }
    }
  });
}

/* Update header cart count badge */
async function updateCartCount() {
  try {
    const res = await fetch(window.routes.cart_url + '.js');
    if (res.ok) {
      const cart = await res.json();
      const cartBadges = document.querySelectorAll('.header-cart-count');
      cartBadges.forEach(badge => {
        badge.textContent = cart.item_count;
        badge.hidden = cart.item_count === 0;
      });
    }
  } catch (e) {
    console.error('Failed to fetch cart:', e);
  }
}

/* 5. Product gallery thumbnails */
function initProductMedia() {
  const mainImage = document.getElementById('ProductMainImage');
  const thumbnails = document.querySelectorAll('[data-product-thumbnail]');
  if (!mainImage || thumbnails.length === 0) return;

  thumbnails.forEach(thumbnail => {
    if (thumbnail.dataset.mediaInitialized === 'true') return;
    thumbnail.dataset.mediaInitialized = 'true';

    thumbnail.addEventListener('click', () => {
      const source = thumbnail.dataset.fullSrc;
      if (!source) return;

      mainImage.removeAttribute('srcset');
      mainImage.removeAttribute('sizes');
      mainImage.src = source;
      mainImage.alt = thumbnail.dataset.alt || mainImage.alt;

      thumbnails.forEach(item => {
        const isActive = item === thumbnail;
        item.classList.toggle('is-active', isActive);
        item.setAttribute('aria-pressed', String(isActive));
      });
    });
  });
}

/* 6. Product variant availability and price */
function initProductVariants() {
  document.querySelectorAll('[data-variant-select]').forEach(select => {
    if (select.dataset.variantInitialized === 'true') return;
    select.dataset.variantInitialized = 'true';

    const productInfo = select.closest('.product-info-wrap');
    const form = select.closest('form');
    if (!productInfo || !form) return;

    const priceAmount = productInfo.querySelector('.price__amount');
    const comparePrice = productInfo.querySelector('.price__compare');
    const savingsBadge = productInfo.querySelector('.price__savings');
    const submitButton = form.querySelector('[data-product-submit]');
    const mainImage = document.getElementById('ProductMainImage');

    select.addEventListener('change', () => {
      const option = select.selectedOptions[0];
      if (!option) return;

      const available = option.dataset.available === 'true';
      const comparePriceText = option.dataset.comparePrice || '';
      const savings = option.dataset.savings || '';

      if (priceAmount) priceAmount.textContent = option.dataset.price || '';

      if (comparePrice) {
        comparePrice.textContent = comparePriceText;
        comparePrice.hidden = comparePriceText === '';
        if (comparePriceText) comparePrice.setAttribute('aria-label', (window.themeStrings?.regularPrice || 'Regular price [price]').replace('[price]', comparePriceText));
      }

      if (savingsBadge) {
        savingsBadge.textContent = savings ? `-${savings}%` : '';
        savingsBadge.hidden = !savings || savings === '0';
        if (savings && savings !== '0') savingsBadge.setAttribute('aria-label', (window.themeStrings?.percentOff || '[percent]% off').replace('[percent]', savings));
      }

      if (submitButton) {
        submitButton.disabled = !available;
        submitButton.setAttribute('aria-disabled', String(!available));
        submitButton.textContent = available
          ? window.variantStrings.addToCart
          : window.variantStrings.soldOut;
      }

      const variantImage = option.dataset.imageSrc;
      if (mainImage && variantImage) {
        mainImage.removeAttribute('srcset');
        mainImage.removeAttribute('sizes');
        mainImage.src = variantImage;
      }

      const url = new URL(window.location.href);
      url.searchParams.set('variant', option.value);
      window.history.replaceState({}, '', url.toString());
    });
  });
}

/* 7. Responsive collection filter drawer */
function initCollectionFilters() {
  document.querySelectorAll('[data-collection-filters]').forEach(drawer => {
    if (drawer.dataset.collectionFiltersInitialized === 'true') return;
    drawer.dataset.collectionFiltersInitialized = 'true';

    let desktopMode = window.innerWidth > 989;
    drawer.open = desktopMode;

    window.addEventListener('resize', () => {
      const nextDesktopMode = window.innerWidth > 989;
      if (nextDesktopMode === desktopMode) return;
      desktopMode = nextDesktopMode;
      drawer.open = desktopMode;
    }, { passive: true });
  });
}

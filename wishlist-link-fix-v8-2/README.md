# Wishlist product-link fix — v8.2

This update fixes two reproducible wishlist URL problems: browser-saved links are never refreshed when the same product appears with a new URL, and collection-scoped links can depend on a collection that has since been removed.

Only **assets/wishlist.js** changed from the delivered v8.1 theme. The other **103 theme files are byte-for-byte identical**. Existing wishlist storage uses the same key and product IDs; saved items are retained. Header, bottom navigation, slider, images, settings, cart and checkout code are unchanged.

## Install on your existing theme

Shopify Admin → Online Store → Themes → Edit code → **assets/wishlist.js**. Replace that file's contents with the file in this folder and save. This is the preferred method if you have changed any images or settings in Shopify since v8.1.

Reload the storefront, visit the collection or homepage showing the affected product, then open Wishlist and select View product. Showing the current product lets the theme refresh its saved URL using the stable product ID. No need to clear browser storage or delete the wishlist.

Alternatively, upload the complete `downloads/Gujju-Jewels-Wishlist-Link-Fix-v8.2.zip` through Online Store → Themes → Add theme → Upload ZIP file. It contains the v8.1 theme settings snapshot, rather than later changes made in Shopify.

## Behaviour and limits

- Current product buttons refresh matching saved URLs, titles and images on page load, drawer opening, Shopify section insertion and cross-tab storage updates.
- Collection prefixes are removed from product links while locale prefixes and query strings are retained. Image, title and View product links all use the same corrected URL.
- The theme cannot discover a renamed product's new handle by ID unless its current product data is on the page. It cannot restore a deleted product or publish a product to the Online Store channel.
- The merchant's exact failing URL was requested but was unavailable at release. Live-store access from the test environment is blocked. These changes fix demonstrated code defects; they do not establish the cause of every possible live Shopify 404.

## Verification

The original script reproduced a 404 for a saved old handle on a controlled HTTP route. The corrected script passed **14 targeted browser checks**, including actual View product navigation on mobile and desktop, title/image navigation, collection-independent paths, locale/variant query preservation, dynamic Shopify sections, cross-tab updates, removal, focus restoration and invalid stored data guards.

**21 broader local browser checks** passed for responsive navigation, wishlist counts, card size/spacing, slider autoplay, product variants, sticky buttons, cart quantity autosave and checkout form submission. Cart and account responses were simulated, not live orders or logins.

JSON, Liquid section schemas, local references, CSS and JavaScript syntax passed. Shopify Theme Check reports zero errors and the same two existing warnings: 41 product-section settings and an unused product-image snippet. ZIP integrity and all 104 packaged files were verified.

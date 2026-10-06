# Version 4 — automatic cart quantity controls

This version changes only three files compared with Version 3:

- `sections/main-cart.liquid`
- `assets/cart-quantity.css` (new)
- `assets/cart-quantity.js` (new)

The Update Cart button is removed. Each cart item has up/down quantity arrows on mobile, tablet and desktop. Typing a quantity also updates automatically after a short pause. Shopify's Ajax cart API saves the quantity; its server-rendered cart section supplies the final item prices, totals and subtotal, including discounts. The header count updates to match the returned cart.

Zero quantity removes that line, as permitted by the original quantity field. The existing Remove links and Secure Checkout form are retained. Checkout waits for pending quantity saves; a failed update does not silently proceed to checkout. Unavailable quantities show Shopify's error or accepted quantity. Cart controls are temporarily disabled during requests, and rapid clicks before a request are combined.

Line-item properties and selling plans are preserved. If Shopify changes line keys after discounts, pending updates are matched to the corresponding item. The script avoids using product IDs alone because the same variant may have different custom properties.

The VIP JEWELS footer, colours, product pages, offers, benefits, related products, FAQ, header, shared product cards and existing cart/payment configuration are byte-for-byte unchanged from the Version 3 ZIP. Product reviews remain removed.

## Apply to Shopify

Upload `Gujju-Jewels-Product-Updates-v4.zip` as an unpublished theme and preview before publishing.

If you have customized your current theme after installing Version 3, use `Gujju-Jewels-Cart-Only-v4.zip` instead: in **Online Store → Themes → Edit code**, add its two asset files and replace `sections/main-cart.liquid`. This avoids overwriting later editor settings or other code customizations. The three source files are also available in the repository under `cart-update-v4`.

Preview: increase/decrease a line, type a quantity, check the subtotal, remove a line and check checkout. For example, ₹249 × 1 plus ₹199 × 2 should total ₹647, before any discount. Perform a real Shopify cart test with your stock limits and installed checkout apps before publishing.

## Validation

Local Chromium tests pass at 320, 360, 390, 430, 768, 990 and 1440px. They cover up/down and typed quantities, line totals/subtotal/header count, no horizontal overflow, rapid clicks, Enter saving without checkout, checkout waiting, multiple changed lines, changing cart keys, distinct properties on the same variant, partial batch errors, stock errors, network errors, inventory clamping, discounted server prices, missing-section fallback and quantity zero/empty cart. The existing product-page regression checks also pass.

The tests simulate Shopify responses and checkout submission; they do not place orders or replace a live Shopify test. Screenshots use sample products and prices. JavaScript syntax and new CSS parse checks pass. Shopify Theme Check retains the same original 11 findings, including its parser-blocking script error; no new findings were introduced. The inherited malformed final global CSS patch is unchanged.

Earlier downloads are preserved. No live Shopify theme, app, payment setting or order was changed from this environment.

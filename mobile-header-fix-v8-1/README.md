# Centered mobile header — v8.1

Full theme download: `downloads/Gujju-Jewels-Centered-Mobile-Header-v8.1.zip`.

Based on the complete Gujju Jewels Mobile Navigation v8 package. Only `sections/header.liquid` and `assets/wishlist.css` changed; the remaining **102 files are byte-for-byte identical to v8**.

## Result

- Below 990px, the top header contains a smaller hamburger, the Gujju Jewels logo centered on the viewport, Search and Cart.
- Mobile header Wishlist and Account icons are hidden. Both remain available through the existing bottom bar; desktop header icons are unchanged.
- Equal 88px side columns prevent the two right-side buttons from pushing the logo to the left.
- Hamburger graphic is 22px wide with 2px strokes and a 44px tap area. Search is 20px and Cart is 22px. Header is 64px tall for the default logo, which is capped at 56px high without distorting its proportions.
- The current image/text logo modes, selected logo assets, mobile logo width, search/cart visibility and desktop alignment controls remain available. The requested simple mobile header takes precedence over the retained mobile-account flag.
- Removed the earlier wishlist stylesheet's competing mobile-header grid and narrow-screen second-row rules. Wishlist dialog and product-heart styling are preserved.

The bottom bar, cart autosave, wishlist storage, product sticky button, slider settings/scripts, homepage spacing, images, menus, customer-account routes, footer and all global settings are unchanged from v8.

## Install

Upload the complete ZIP through Shopify Admin → Online Store → Themes → Add theme → Upload ZIP file, then Preview before publishing.

If you already installed v8 and subsequently edited settings or images in Shopify, you can instead replace **only the two files provided in this folder** using Edit code on that theme. This applies the same header fix while keeping those later Shopify edits. Do not upload this two-file folder as a complete theme.

## Verification

- 31 local browser checks passed.
- Tested 280, 320, 360, 390, 430, 768, 989, 990, 1440 and 1920px.
- Verified logo center position, compact hamburger strokes, 44px touch targets, only Search/Cart visible in mobile header, no horizontal overflow and working menu/search drawers.
- Wishlist remains accessible from the bottom bar and cart counters still update after quick add.
- Native image/text logo modes, custom logo images, left desktop alignment, mobile-account flag and disabled wishlist configurations checked across mobile/tablet widths.
- Desktop header element geometry exactly matches v8 at 990, 1440 and 1920px. Mobile/desktop resizing restores the appropriate icons.
- Shopify Theme Check: zero errors; the same two pre-existing warnings remain (41 product-section settings and an unused `product-image` snippet).
- ZIP integrity and every packaged file verified.

Tests used a local browser and simulated Shopify cart data. No live-store changes, login sessions, orders or payments were performed.

![Local mobile header preview](previews/header-only-390.png)

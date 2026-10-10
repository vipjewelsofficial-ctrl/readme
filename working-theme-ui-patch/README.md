# Apply the requested interface updates to the existing working theme

This is a **10-file patch**, not a complete Shopify theme. Apply it to a duplicate of the theme whose product pages work in Shopify. Do not upload this patch ZIP through Add theme.

The patch keeps the centered compact mobile header, smaller wishlist hearts, tighter Category/New Arrivals spacing, mobile bottom navigation and the existing wishlist URL refresh. It changes seven existing files and adds three navigation files. It does not include or replace global configuration or product-page files.

## Why this patch exists

The newly uploaded `theme_export__gujjujewels-com-gujju-jewels-slider-wishlist-v7__10OCT2026-0115pm.zip` is byte-identical to the earlier uploaded v7 backup. It contains 98 files, an empty `config/settings_schema.json`, no `config/settings_data.json`, no `templates/product.json` and no `sections/main-product.liquid`.

The user reports that the earlier Shopify theme's product pages worked. This archive therefore does not provide the actual product-page implementation needed to preserve that working behaviour exactly. Absence from this archive does not prove those files are absent from the running theme.

The delivered v8.2 ZIP contains 104 files: 90 unchanged, eight existing files changed and six files added. Besides the requested interface changes, it restores global configuration and product-page files from an earlier complete version. The user's live 404 cause has not been established. The restore must not be described as a confirmed cause or this patch as a confirmed live fix.

Product cards, the wishlist Liquid button, the base layout, the main JavaScript and cart quantity script are identical between the uploaded v7 archive and v8.2. Product cards and wishlist buttons use Shopify's `product.url`; there is no hardcoded `traditional-gold-tone-floral-necklace-set` link in either source.

## Apply

1. In Shopify → Online Store → Themes, locate the original working theme in the theme library. Preview it and open the affected product to confirm it still works.
2. Duplicate that working theme. Use Edit code on the duplicate and apply the files in this folder's `files` directory, preserving their exact folder names. Replace seven existing files and add the three `mobile-bottom-bar` files.
3. Keep the duplicate's `config` files, product templates, main product section and other code intact.
4. Preview the duplicate and check product-card image navigation, Wishlist → View product, cart and the mobile interface before publishing.

The supplied homepage/footer JSON derives from the user's uploaded backup. Its only semantic changes are category bottom spacing, New Arrivals mobile top spacing and adding the mobile navigation section. If the original working theme has later homepage/footer edits, merge those three changes rather than replacing its JSON wholesale.

To produce a complete ZIP while retaining the exact working product code and settings, export the working Shopify theme through its menu → Download theme. The supplied incomplete backup cannot establish those missing files' contents.

## Verification

ZIP integrity and all ten patch contents were verified against the tested v8.2 source. The patch excludes all configuration files, product templates and the main product section. See `manifest.json` and `v7-v8.2-comparison.json` for exact scope.

The v8.2 source passed 39 local browser checks, including product-template rendering and product image/wishlist navigation. Shopify catalog routing, publication and cart responses were simulated; these checks do not verify the merchant's live 404 or this patch installed on the working theme. Live store access from the execution environment is blocked.

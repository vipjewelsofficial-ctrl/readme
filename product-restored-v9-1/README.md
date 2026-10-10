# Gujju Jewels v9.1: product template restoration

The v9 archive had no default product template or main product section. This package restores `templates/product.json` and `sections/main-product.liquid` byte-for-byte from the earlier complete v7 source retained in this repository. Shopify uses the singular filename `product.json`, not `products.json`.

It also restores the global settings schema and adds global settings data. Saved values use the existing v9 layout colour/size fallbacks, Inter/Cormorant Garamond font selections, and the original control defaults. No older homepage, header, footer, image or app settings are copied into the configuration. The favicon image was absent from the uploaded export; select it through Theme settings if required.

Compared with v9: 100 existing files are byte-identical, `config/settings_schema.json` changes, and three files are added (`templates/product.json`, `sections/main-product.liquid`, `config/settings_data.json`). No file is removed. The current hero slides, product card links, collection links, cart scripts, header, spacing fixes, wishlist scripts, bottom bar, and homepage/footer section settings remain byte-identical to v9.

## Validation

79 local browser checks passed using simulated Shopify data/routes: product template rendering, product card image/title and wishlist navigation, thumbnail images, available/sold-out variants, quantity submission, single-variant products, mobile sticky product cart positioning, mobile/desktop header, slideshow autoplay, spacing, wishlist, cart updates, bottom navigation options, and section lifecycle.

Theme Check: zero errors, two advisory warnings inherited from the restored source (41 main-product settings; unused product-image snippet). JSON, section schema defaults, asset/snippet/section references, JavaScript and CSS syntax passed. The final ZIP has 104 files, passes CRC integrity checks, and every packaged file matches the tested source.

Local browser tests are not a test of live Shopify routing, product publication, payments, accounts or orders. Live product URL success has not been confirmed from this environment.

## Install

In Shopify, open Online Store > Themes > Add theme > Upload ZIP file and upload the full v9.1 archive as an unpublished theme. Open Preview and check an actual product from both its image/title and wishlist, its images, options and cart flow. The default product template is now present. Publish after the merchant preview succeeds.

If applying repairs directly to an existing theme, duplicate it first. The two product files are available under `restored-files`. Preserve any existing global settings data in Shopify; do not overwrite a working theme's saved global values with the defaults in this package. Merge schema controls only if needed.

The restored product template includes its earlier offer/benefit blocks; review those messages in the product template editor against the actual store policies. This code does not configure promotions, payment gateways, COD apps or customer-account authentication.

# Complete Gujju Jewels category theme — v10.1

Download `Gujju-Jewels-Complete-Category-Theme-v10.1.zip`. This is the full 104-file Shopify theme, not the earlier single-file homepage patch. Assets, config, layout, locales, sections, snippets and templates are at the ZIP root.

## Included changes

- Shop by Category now has Necklaces, Jewellery Sets, Gold Tone Jewellery, Oxidised Silver Jewellery and Mangalsutra, in that order. Five columns on desktop and the existing mobile swipe row/spacing are retained.
- Each category uses a corresponding product-photo reference from the merchant's previously uploaded product export, plus native image and collection selectors in Customize.
- `config/settings_schema.json` was empty and `config/settings_data.json` absent in the 20 October export. Both are restored from the last complete delivered v10 source. Version metadata is 10.1.0. All 39 referenced global settings are now defined, including typography, colours, favicon and wishlist options; saved font and wishlist heading/empty-state values are restored. These are the last known v10 saved globals, not a recovery of any later unsupplied settings.

Compared with the supplied 103-file export: 101 existing files are byte-identical; templates/index.json and config/settings_schema.json change; config/settings_data.json is added. The only homepage configuration change is inside Shop by Category. Every other section's saved content and relative order is preserved. Header/menu, product pages, cart, footer, wishlist and slider source files are unchanged. Other findings in the separate full audit remain separate from this narrowly scoped release.

## Upload and preview

1. Shopify → Online Store → Themes → Import / Add theme → Upload ZIP. Select this complete ZIP.
2. Open Customize on the uploaded theme. It includes the working default product template and main-product section.
3. Home page → Shop by Category → open each card and confirm its Image and Collection. All five remain editable.
4. Preview the homepage, a product and the cart; publish the uploaded theme after confirming the native Shopify preview.

| Category | Product photo reference | Collection handle preselected |
|---|---|---|
| Necklaces | Gold-tone temple necklace | necklaces |
| Jewellery Sets | Gold-tone choker necklace set | necklace-sets |
| Gold Tone Jewellery | Gold-tone temple necklace set | gold-tone-jewellery |
| Oxidised Silver Jewellery | Oxidised pearl-layered necklace set | oxidised-jewellery |
| Mangalsutra | Black-bead mangalsutra with a gold-tone temple pendant | mangalsutras |

Photo references point to existing Shopify Files using shopify://shop_images/. The live store and CDN cannot be accessed from the execution environment, so native image/collection availability needs preview confirmation. If an image is unavailable, select the matching product photo in the card's Image picker. If a handle differs, choose the correct collection. Unassigned collections use the existing Shop All fallback. This theme ZIP does not create collections or assign their products.

The top navigation menu is preserved. To change its source to Shopify Content → Menus, use the existing Header switch for built-in navigation; this package does not change that switch.

## Verification

- 34 local regression checks passed: nine category layout widths, 13 product-page checks and 12 cart/navigation/sticky-control checks. Catalogue, image resolution, cart responses and form submissions are local fixtures; no real order was created.
- Shopify Theme Check: zero errors, two existing advisory warnings (41 product settings and an unused product-image snippet).
- JSON, references, schema defaults, JavaScript and CSS checks passed across 28 section schemas. All referenced global setting IDs are defined.
- All 104 ZIP members round-trip against tested source; CRC checks pass. Required product.json, main-product.liquid and both global configuration files are present.

See review/package-report.json for the archive SHA-256 and review/scope-check.json for exact preservation evidence.

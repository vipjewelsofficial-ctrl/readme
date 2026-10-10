# Best Sellers and Shopify homepage controls — v10

Adds Best Sellers immediately after New Arrivals. All original homepage sections and their relative order, saved settings and blocks are retained. You can drag the sections into your preferred order in Shopify. The existing compact homepage spacing is retained.

## Recommended: update the existing working theme

Use Edit code in a duplicate of your current working theme. Replace each of these section files completely and save them before replacing templates/index.json:

1. sections/new-arrivals.liquid
2. sections/featured-products.liquid
3. sections/collection-card-grid.liquid
4. templates/index.json

The four-file ZIP is for manual code updates, not a complete theme to upload through Add theme. Product-page files, globals, header, footer, cart, wishlist and slider files are not replaced by this patch. The homepage template comes from the retained latest configuration; if you changed homepage blocks or settings since that backup, preserve those edits and add an instance of Featured Products through Customize instead, naming it Best Sellers and setting its section ID to best-sellers.

## Alternative: complete theme ZIP

Gujju-Jewels-Best-Sellers-Shopify-Controls-v10.zip contains all 104 theme files, including templates/product.json and the working sections/main-product.liquid with the shortened valid details block label. Upload through Online Store → Themes → Import / Add theme → Upload ZIP. Customize and preview before publishing. This package reflects the retained theme backup, not any later unsupplied admin edits. Global theme metadata is version 10.0.0.

## Choose products and arrange sections

Online Store → Themes → Customize → Home page:

- New Arrivals, Best Sellers, Trending Picks: open the section, use Products to select and arrange up to 16 products. Choose Products to show (2–16) and Product order → Keep selected product / collection order. Each section has independent selections. Individual selections take priority over the collection.
- If no individual products are chosen, a selected Collection supplies the products. Optional all-products fallback remains available. Best Sellers has fallback disabled by default so it displays only products you choose; its empty setup state is shown in the editor and hidden on the live storefront.
- View All: enable the button and select its link when using manual products. A selected collection can supply the button destination. The button stays hidden when no destination is configured. The label prefix and section heading remain editable; the heading is appended to the prefix as before.
- Shop by Style: open a Style card. Select a Collection or Featured product, plus an optional custom image, title and custom link. Product links take priority over collections; a custom link takes priority over both. Custom image takes priority over product image. Existing demo style images remain available, with a new setting to disable them.
- Shop with Confidence: edit/add/remove benefit blocks and their titles, descriptions and icons.
- FAQ: edit/add/remove FAQ Item blocks and questions/answers.
- Footer: select Footer in its section group to edit links, text, newsletter settings and images.
- Drag any homepage section to change its position. The theme does not force a page order through JavaScript.

## Validation

Shopify Theme Check: 0 errors, two existing advisory warnings (product section settings count and an unused product-image snippet). Native section/block/preset names checked against Shopify’s 25-character limit. All selected padding values, section references and block types validated. JSON, Liquid references, CSS and JavaScript syntax checked.

24 homepage selection/rendering checks, including nine screen widths; 13 existing product-page regression checks. Browser routes, catalogue and cart APIs use local fixtures, so these do not establish live Shopify rendering or real order placement. Product-template files remain byte-identical to the working repair. The full ZIP round-trips against all 104 source files and includes all product dependencies.

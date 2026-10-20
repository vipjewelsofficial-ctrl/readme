# Shop by Category — five-category update

This is a single homepage-template update for the v10 theme export supplied on 20 October 2026. Only the `categories` section configuration inside `templates/index.json` changes. No Liquid/CSS/JavaScript, product-page, cart, wishlist, slider, footer or global configuration file is replaced. All other homepage sections, settings and their order are preserved.

## Apply to the existing working theme

In Shopify → Online Store → Themes → Edit code, open `templates/index.json`, replace its entire contents with the supplied file, and Save. This JSON is not a complete theme ZIP. It is based on the uploaded 20 October backup. If you have edited other homepage content since that export, copy only the `categories` object from the new JSON into your existing template instead of replacing the entire template.

Then open Customize → Home page → Shop by Category and inspect each card. All labels, images and Collection selections remain editable. Desktop uses five columns; the existing circular styling and mobile swipe row are retained, including the previous spacing values.

| Category | Chosen product photo from the merchant product export | Preselected collection handle |
|---|---|---|
| Necklaces | Gold-tone temple necklace with statement pendant | necklaces |
| Jewellery Sets | Gold-tone choker set with red/green stones and pearl drops | necklace-sets |
| Gold Tone Jewellery | Gold-tone temple necklace set with green/pink stones | gold-tone-jewellery |
| Oxidised Silver Jewellery | Oxidised silver pearl-layered necklace set | oxidised-jewellery |
| Mangalsutra | Black-bead mangalsutra with a gold-tone temple pendant | mangalsutras |

Photo selections use `shopify://shop_images/` references derived from the Image Src fields in the product CSV previously uploaded by the merchant. They refer to existing Shopify Files, not newly generated jewellery photographs. Live Shopify/CDN access is blocked by the execution environment, so the image files and collection handles could not be verified against the current store. If a selected image is unavailable, use Image → Select to choose the corresponding stored product photo. If a collection is unassigned or the handle differs, choose the correct Collection. The existing section safely falls back to Shop All when a collection cannot resolve; no new guessed direct collection URL is hardcoded.

The source CSV and image mapping are recorded in review/category-mapping.json. Browser layout checks substitute local fixture images; they cannot establish that those stored photos still exist in Shopify.

The global settings issues found during the separate full-theme audit are not modified by this narrowly scoped patch. The uploaded theme files themselves remain unchanged.

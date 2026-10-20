# Gujju Jewels Accessories category update — v10.2

Download `Gujju-Jewels-Accessories-Category-Update-v10.2.zip`. This is the complete 104-file theme based on the last complete v10.1 package, with all working product and global settings files included.

## Requested changes

- Removed the Shop by Style section from the homepage. The section type remains available in the theme editor if you want to add it again later; its prior configuration is archived in review/removed-style-section.json.
- Removed Necklaces and Jewellery Sets from the Shop by Category row.
- Added one Accessories category card in their place. The category order is Accessories → Gold Tone Jewellery → Oxidised Silver Jewellery → Mangalsutra.
- Accessories uses the existing top-menu destination `/collections/accessories`. The supplied header uses built-in navigation with no custom Accessories URL override; the category matches that supplied configuration.
- Accessories uses its selected collection's featured image if available, or the bundled kada/bracelet photo as a fallback. You can select a custom image in Customize. The other three category image references are preserved.
- Desktop category columns change from five to four. Mobile swipe behavior and spacing are preserved.

The user explicitly asked to ignore Wall Cladding. Footer files, menus and saved footer settings are byte-identical to v10.1; no Wall Cladding filter was introduced. The header and top-menu files are also byte-identical.

All other homepage sections, content and relative order are retained. Product-page, cart, wishlist, slider and saved global settings files are unchanged. Of 104 files, 101 are byte-identical. Only templates/index.json, sections/category-directory.liquid and version/documentation metadata in config/settings_schema.json change. No CSS or JavaScript changes.

## Upload

Shopify → Online Store → Themes → Import / Add theme → Upload ZIP. Open Customize and preview the uploaded theme before publishing.

Home page → Shop by Category → Accessories lets you edit its collection, image, title and link. The theme does not create the Accessories collection or assign products; it points to the destination already used by your menu. Live collection availability is not verified from this execution environment. The other three images continue to use the same existing Shopify Files references as v10.1, so confirm those in the native preview.

For manual updates to an existing theme, replace sections/category-directory.liquid first and templates/index.json second with the two repair-files provided. This homepage template is based on the retained v10.1 configuration; preserve any newer unsupplied homepage edits if you use this manual route.

## Verification

16 targeted checks passed, including four-category rendering at nine widths from 320px to 1920px, matching menu/category URLs, fallback/collection/custom image priorities, absence of Shop by Style and unchanged footer menu behavior. Browser catalogue/image objects are fixtures; native Shopify data and collection availability are outside those checks.

Shopify Theme Check: zero errors, two existing advisory warnings (product settings count and unused product-image snippet). All JSON, section references, asset/snippet references, schema defaults, JavaScript and CSS checks pass; section/block/preset names are within the 25-character save limit. The ZIP has 104 files, passes CRC and round-trips against tested source, including the product template and section.

See review/scope-check.json and review/package-report.json for preservation and archive evidence.

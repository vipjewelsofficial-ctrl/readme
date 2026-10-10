# Gujju Jewels v9.2: repair the missing default product template

The merchant tested the same necklace URL in Dawn, where it opened, and switched back to the custom theme, where it returned the designed 404 page. Its public product data identifies product 8810893803716, confirms the handle, and shows an empty template_suffix (Default product).

The subsequently uploaded published-theme export, named v9.1, contains 101 files. It is missing templates/product.json, sections/main-product.liquid and config/settings_data.json, and its config/settings_schema.json is an empty array. All 101 file contents match the earlier v9 UI-only archive, rather than the 104-file v9.1 package delivered. This establishes the source mismatch and missing product-page files; it does not establish whether a different ZIP was uploaded or how those contents reached the published theme. A theme name is an editable label, not proof of the files installed.

The full v9.2 ZIP repairs this exact export. It adds the two product files and saved global settings, and replaces the empty settings schema with the original controls and explicit theme version 9.2.0. The product template and main section match the retained earlier complete v7 implementation. The global saved values match the v9 fallback colours and layout sizes; previous homepage/header/footer settings are not imported. The other 100 existing files are byte-identical, including the current header, menu, hero slideshow, category/arrival spacing, wishlist, cart scripts, footer and section-group settings.

## Full theme installation

Download Gujju-Jewels-Product-Template-Repair-v9.2.zip (the 104-file full theme). In Shopify open Online Store > Themes > Add theme > Upload ZIP file. Keep the newly uploaded theme unpublished while checking it.

Open Edit code on that newly uploaded theme and verify:

1. config/settings_schema.json starts with theme_info and theme_version 9.2.0, rather than an empty array.
2. sections/main-product.liquid exists and contains the product gallery, product form and Main Product schema.
3. templates/product.json exists (singular product) and its main section has type main-product.
4. config/settings_data.json exists and contains current global values.

Use that theme's Preview, preserving its preview context, to open the actual necklace from a product image/title and from Wishlist > View product. Verify images, quantity and cart submission. Publish after that real Shopify preview succeeds. Local test success is not a claim that the repaired package has already been uploaded or rendered on the merchant store.

## Targeted repair through Edit code

If the imported files are missing again, the two page files can be saved directly in a duplicate of the current theme, avoiding another full theme import. Under repair-files/sections, open main-product.liquid, copy the entire raw file, create sections/main-product.liquid in Shopify and Save. Then copy repair-files/templates/product.json, create templates/product.json and Save. Save the section before the template so its referenced section exists. Do not use the plural name products.json.

The small Gujju-Jewels-Product-Files-Only-v9.2.zip contains only those two source files for Edit code. It is NOT a complete theme and must not be uploaded through Add theme. The four repair source files are also available individually in this directory.

Global control repairs are available under repair-files/config. Apply the schema and saved data to this export if absent. Preserve or merge any existing saved global values rather than overwriting them if the installed theme has newer settings. This export did not contain a favicon selection; that can be selected in Theme settings once the controls are restored.

If Shopify shows an error while saving either product file, capture the exact error text before proceeding; it identifies a native import/save constraint that local checks cannot reproduce. No product handle, product assignment, sales-channel settings, payment gateway or app configuration needs to be changed to apply this code repair.

## Verification

79 local browser checks passed: product rendering and product-card/wishlist navigation, image thumbnails, single/multiple variants, sold-out behaviour, quantity submission, sticky product cart placement, desktop/mobile header, autoplay, spacing, wishlist counts, cart quantity/removal and native checkout submit, bottom bar controls and editor lifecycle. Shopify responses, order/account behaviour and product catalogue are simulated in those tests.

Theme Check reported zero errors and two existing advisory warnings (main-product settings count; unused product-image snippet). JSON, section schema defaults and block references, asset/snippet references, CSS and JS syntax passed. The missing-file check fails on the provided published export and passes on the repaired source. Both ZIPs pass CRC checks; every file in the 104-file theme ZIP matches the tested source. Live access to the storefront remains blocked from this environment.

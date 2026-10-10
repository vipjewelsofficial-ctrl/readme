# Gujju Jewels — compact mobile Shop by Category row

This update changes only **Shop Categories**: one replacement Liquid section and one new CSS asset. It preserves saved category titles, images, blocks, destination collections/links, shapes, descriptions, optional buttons and counts. Saved theme settings/templates and other sections are not replaced.

## Apply to your current theme

1. Download and extract **Gujju-Jewels-Mobile-Category-Row-Fix.zip**.
2. Shopify Admin → Online Store → Themes → your current theme → … → **Edit code**.
3. Under **Assets**, create **category-mobile-row.css**, paste the entire contents of the ZIP's matching CSS file, and save.
4. Keep a copy of **Sections → category-directory.liquid**. Replace its entire contents with the ZIP's `sections/category-directory.liquid`, then save. The replacement section loads the stylesheet automatically; no layout file edits are required.
5. **Customize → Home page → Shop Categories**. Under **Compact row on phones and tablets**, use **Single swipeable row**. It is the new default. The row applies below 990px; desktop retains the selected desktop columns.
6. Adjust category size, gap, heading visibility/size and top/bottom spacing in the new controls. Defaults: 92px cards, 12px gap, 24px heading, 16px top and 20px bottom spacing. Hide the heading if you want the photo shortcuts directly below the hero.
7. Preview on a phone and desktop. Swipe horizontally or use Tab/arrow keys to reach the remaining categories. Selecting **Original grid** restores the former layout; existing mobile/tablet columns and image-size controls continue to apply to that option.

This ZIP is a section/asset patch, not a complete theme. Apply the two files through Edit code to preserve the images and settings you have recently added. No Shopify Admin changes were performed from this workspace.

## Hero banner

The existing hero supports separate desktop/mobile images. The wide desktop artwork can scale to mobile without cropping, but text already baked into that image gets small when the full artwork is shrunk. Upload a mobile-specific design through **Hero Image Slider → each Slide → Mobile image** to improve text readability. Keep the jewellery and shopping text readable at actual phone width, and use a moderate banner height so category shortcuts remain close below it.

This patch preserves your current hero. The earlier [responsive header/slider correction](../responsive-header-slider-fix/README.md) supplies the separate autoplay and dots-only fixes: dots sit below mobile artwork, arrows/Pause are hidden, and rotation resumes after editor slide deselection. If already installed, leave those files in place.

## Validation

Local Chromium tests cover 320, 360, 390, 430, 768, 989, 990, 1440 and 1920px. They verify single-row categories, exact desktop geometry against the earlier section, correct collection links, real image loading, native touch swiping, keyboard scrolling/focus, eight categories with a long name, empty/single cases, original-grid restoration, editor controls and image shapes. Combined checks verify the adjacent hero retains its artwork ratio, autoplay and dots; wishlist controls still open/save correctly.

Preview images use local sample artwork and products. They demonstrate layout and are not screenshots of your live store. Live collection contents, customer checkout and payments need checking in your Shopify draft preview.

All existing block setting IDs and existing section setting IDs are retained. Hero, header, footer, product/cart JavaScript, customer accounts, wishlist storage, templates and saved settings are not edited by this category-only patch. See `validation.json`, `theme-check.json`, `package-validation.json` and `previews`.

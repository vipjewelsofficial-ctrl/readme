# Gujju Jewels — Slider and Wishlist Theme v7

Complete Shopify theme based on the delivered v6 package. All 100 theme files are included. Changes from v6: 11 existing files modified, 4 files added, 85 files identical. Settings data, all image assets and homepage/product section order are preserved. Existing native cart/checkout routes and automatic quantity updates remain in place.

## Upload

Shopify Admin → Online Store → Themes → Add theme / Import theme → Upload ZIP. Upload `Gujju-Jewels-Slider-Wishlist-v7.zip` as a draft, then open Customize and preview before publishing. The live store was not changed from this workspace.

## Set up your hero slideshow

1. Customize → Home page → **Hero Image Slider**.
2. Open the first **Slide** block. Your existing `Jewellery_for_Every_Celebration.png` artwork is already there. Set its destination link and optional separate mobile image.
3. Choose **Add block → Slide**, select another desktop image and, if desired, a separate mobile image. Add up to 8 Slide blocks.
4. Select **Image only** for artwork that already contains its text; select **Overlay text** for photos needing an editable heading, description and buttons.
5. Set autoplay, interval, arrows/dots, fixed/adapt height and image fit in the section settings. Autoplay is enabled for the imported slider but starts only when at least two slides exist. Pause/play, keyboard navigation, swipe and reduced-motion support are included.

The ZIP intentionally retains your single existing artwork. A second image must be selected in Shopify before the storefront can cycle between images. No extra promotional image was invented or inserted. The old section-level artwork fields remain under **Legacy original slide** for compatibility; normally edit the Slide blocks.

## Wishlist

**Theme settings → Wishlist** controls enabling the feature, header entry point, hearts on cards, panel heading and empty-state text. **Products → Default product → Main Product → Wishlist button** controls the product-page button placement. Interface wording is available under **Edit default theme content → General → Wishlist**.

Customers can save/remove products using heart buttons on cards or product pages, open the wishlist from the header, and follow **View product** for current prices, available variants and purchasing. No stale snapshot price is shown in the wishlist. The panel uses your theme colour and font variables and is responsive. Keyboard focus, Escape, scroll locking, focus restoration, item counts and dynamically loaded recommendation cards are supported.

This is a free browser-storage wishlist. No app, subscription or customer login is required. Items remain after refresh and synchronize between tabs in the same browser. They do not synchronize across devices or appear in Shopify Admin; clearing browser data removes them. Server/account synchronization would require an app or backend. If storage is blocked/full, saving reports a failure without displaying a false saved state. The maximum is 200 saved products.

## Four editor fixes

| Fix | Where to edit |
|---|---|
| Built-in desktop logo follows the width setting; the old fixed height cap is removed | Header → Logo width |
| Section heading size now affects mobile text | Theme settings → Layout & typography → Section heading size |
| Collection Banner caption, button and mobile-panel colours/opacity are configurable | Home page → Collection Banner → Text and mobile panel colours |
| Removing all product information blocks leaves the information area empty | Main Product → Use product information blocks; enabled in the imported default product template |

Disable **Use product information blocks** only when you want the legacy layout and no component blocks are present. Gallery content is separate from the information blocks. Product form quantity/options stay together in the Buy buttons block so native submission is preserved.

## Validation

Local slider, editor, product, wishlist and cart checks passed. Product/cart/wishlist layouts were checked at 320, 360, 390, 430, 768, 990 and 1440px. Cart checks include 13 stock/network/concurrency/quantity cases. Wishlist checks include persistence, card/product synchronization, removal, tab synchronization, keyboard focus, invalid stored data, blocked storage, unsafe URLs and dynamically added cards. A repeat regression run passed. Combined cart/wishlist checks at 320, 390, 768 and 1440px confirmed separate counters, no cart mutations from wishlist actions, quick add, and checkout waiting for pending quantity updates. Core cart scripts and routes remain unchanged. The original hero artwork is preserved in the first slide. JavaScript and CSS syntax checks passed, and the ZIP was validated against every packaged source file.

Shopify Theme Check reports zero errors and two nonblocking warnings: the preserved unused product-image snippet, and Main Product’s 41 editor fields exceeding the checker’s recommended threshold of 40. All section JSON and saved block references are valid. Compatible app blocks still need their corresponding installed app.

These checks used local product data and mocked Shopify responses. Real checkout, orders, payments, customer account behavior and installed apps need a draft preview in your Shopify store. Preview screenshots show test products rather than your live store.

See [file-manifest.csv](file-manifest.csv), [package-validation.json](package-validation.json), [validation](validation) and [previews](previews). All v6 features and editing locations remain documented in the [v6 guide](../theme-editable-v6/README.md).

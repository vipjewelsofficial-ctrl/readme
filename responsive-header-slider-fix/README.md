# Gujju Jewels — responsive header, wishlist and slider correction

This patch applies to the delivered v7 theme. It replaces only three existing assets. It preserves your currently saved hero images, Slide blocks, colour/font settings, menus, product data, cart and wishlist data. Shopify Admin and the live theme were not edited from this workspace.

## Apply to your current theme

1. Download and extract `Gujju-Jewels-Responsive-Header-Slider-Fix.zip`.
2. Shopify Admin → Online Store → Themes → your current theme → … → Edit code.
3. Keep copies of the current three files for rollback. Replace the entire contents of each file with its counterpart in the ZIP's `assets` folder, then save:
   - **Assets → wishlist.css**
   - **Assets → hero-slider.css**
   - **Assets → hero-slider.js**
4. Customize → Home page → Hero Image Slider. Keep **Show slide dots ON**, **Auto-rotate slides ON**, and at least two Slide blocks. Use your preferred interval (for example 5 seconds). **Show previous / next arrows** can remain OFF. The replacement CSS hides arrows and Pause on all screen sizes.
5. Open a fresh storefront preview tab and refresh. In Customize, leave an individual Slide's settings to see rotation resume.

This is an asset patch, not a complete theme. Apply the three existing files through Edit code so the banner images/settings you added recently remain in place.

## What changes

- On mobile/tablet, the header logo uses its own grid column. The wishlist heart, search and cart icons stay together without crossing the logo. Icons and hamburger have 44px touch targets. Desktop header layout is preserved.
- The optional mobile account icon is preserved. On phones below 375px, if that extra icon is enabled, actions use a second row so all four controls remain usable.
- Only the slider dots remain visible. On phones they sit below the artwork, protecting its text and shopping link. Desktop dots remain in their existing bottom position.
- Mobile wishlist title wrapping, item columns and safe-area padding fit narrow screens and long product names. Save/remove, persistent browser storage, badges, Escape, keyboard focus and scroll restoration retain the existing wishlist JavaScript.
- Includes the earlier autoplay JavaScript correction: rotation works in Customize, continues while a pointer is over the artwork or after clicking dots, and resumes after deselecting an editor Slide block. Keyboard focus, hidden tabs and reduced-motion preferences still pause appropriately. OFF intentionally means manual navigation.

The artwork stays intact: no images are replaced, cropped or redrawn by this patch. For a portrait mobile banner, select a separate mobile image within each Slide block; otherwise the theme adapts the desktop artwork to fit.

## Validation

Local Chromium checks cover seven viewport widths: 320, 360, 390, 430, 768, 990 and 1440px. Header geometry and menu/search/cart controls were checked in 42 configurations (three logo modes and mobile account on/off at each width). Wishlist persistence, long titles, remove, keyboard focus, Escape and autoplay with only dots were checked at 320, 390, 768 and 1440px. All eight supported slide dots also fit without horizontal scrolling at those widths. The script also retains the previously tested 18 autoplay cases.

No logo/icon overlap, horizontal page overflow or JavaScript exceptions were found in these checks. CSS and JavaScript syntax checks passed. Preview images are local fixtures with sample artwork/products, not screenshots of your live store. See `validation.json` and `previews`.

No Liquid/template files or wishlist/cart JavaScript is changed. The ZIP contains exact copies of the three supplied replacement assets. Live Shopify checkout and payment processing were not tested by this layout patch.

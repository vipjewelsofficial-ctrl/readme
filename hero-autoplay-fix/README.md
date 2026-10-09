# Hero autoplay correction for Gujju Jewels v7

This is a one-file JavaScript replacement for the delivered v7 theme. It preserves your currently saved Slide blocks, images, theme settings, dots, wishlist, cart and checkout. The live Shopify theme was not edited from this workspace.

## Apply to your current theme

1. Open `hero-slider.js` in this directory and copy its entire contents.
2. Shopify Admin → Online Store → Themes → your current theme → … → Edit code.
3. Open **Assets → hero-slider.js**. Keep a copy of the existing file for rollback, replace its contents with the corrected script, and save.
4. Customize → Home page → Hero Image Slider. Keep **Auto-rotate slides ON**, set **Seconds between slides** (for example 5), and ensure at least two Slide blocks are present. Keep **Show slide dots ON** and **Show previous / next arrows OFF**.
5. Leave the existing custom CSS hiding `[data-slider-pause]` in place if you want only dots. This JavaScript also works when arrow and pause buttons are absent.
6. Open the storefront preview in a new tab and refresh it. In Customize, leave the individual Slide block to see it rotate. OFF intentionally keeps the slideshow manual.

Do not replace your current theme with the older full v7 ZIP to apply this fix: your recently added images and settings are preserved by replacing the one asset directly.

## Correction

The earlier script unconditionally blocked autoplay while Shopify.designMode was true, paused when the pointer hovered anywhere over the artwork, and never resumed on editor block deselection. The correction permits editor autoplay, keeps rotating while the pointer is over the artwork and after mouse clicks on dots, and pauses only while an individual editor slide is selected, resuming when it is deselected.

Keyboard focus still pauses rotation so links and dots remain usable without changing under focus. Hidden tabs pause and resume when visible. Reduced-motion preferences are respected and recover when the preference changes; an explicit Play action may opt in. Manual Pause remains independent of reduced-motion changes. Editor unload/reload removes old timers/listeners.

## Validation

18 local Chromium browser checks passed: dots-only autoplay at 320, 390, 768 and 1440px in both storefront and simulated Shopify editor; pointer hover and dot clicks; autoplay OFF; a single slide; editor selection/deselection; keyboard focus and arrows; reduced motion; manual pause/play; tab visibility; editor reload and setting changes; swipe. No horizontal overflow or JavaScript exceptions in these checks. JavaScript syntax validation also passed.

Only the replacement slider JavaScript changes. No theme Liquid, image, settings, cart, product, wishlist, menu or footer files were changed. These were local tests with rendered Shopify-like fixtures and simulated editor events, not a live Shopify Admin session. See `validation.json` for the individual checks.

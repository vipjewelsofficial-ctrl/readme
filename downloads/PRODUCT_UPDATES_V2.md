# Gujju Jewels product updates — version 2

This version extends the verified first theme download. The first ZIP is retained in the GitHub repository for rollback. Nothing has been installed or published to the live Shopify store.

## 1. Choose how many related products appear

Open **Online Store → Themes → Customize → Products → Default product → Related products**.

- **Products to show** now accepts every number from **1 to 10**. This is the total card count. Mobile/tablet still uses two columns; desktop uses four.
- **Fallback collection** lets you select a collection to fill spaces when Shopify returns fewer recommendations. Leave it blank to use the current product's first collection. An empty or missing collection falls back to All products.
- Shopify's recommendations appear first, then available fallback products. The current product and duplicates are excluded. A small catalog can still produce fewer cards than requested.
- Turn **Show related products** off to hide the section completely.

## 2. Enable real product review submissions, sorting and admin management

The new **Product reviews** section appears below the main product information and before related products. It styles Judge.me's actual widget in the theme's burgundy, ivory and gold palette. It supports the app's summary, rating histogram, Write a Review button, sort selector, entries, form fields and pagination. The app supplies the review data, form behaviour and verified-purchase status. The ZIP contains no sample reviews or ratings.

**A theme cannot store or moderate reviews on its own. A connected reviews app is required. This update does not install an app or create a review backend.**

Recommended setup:

1. Install **Judge.me Product Reviews** from the Shopify App Store, or use it if already installed.
2. Open the uploaded theme's **Customize → App embeds** and enable Judge.me's embed if the app provides/requires it for your installation.
3. Open **Products → Default product → Product reviews → Add block → Apps**, then add Judge.me's **Review Widget** block. Set **Reviews integration** to **Use an added reviews app block**. This uses the app's native Shopify block and is the preferred setup.
4. Alternatively, leave **Reviews integration** as **Judge.me (app required)** for an installation whose app embed loads the legacy Judge.me product widget. The section uses `product.metafields.judgeme.widget` and the current product ID. An added app block takes precedence, so the theme renders one widget instead of two.
5. In **Shopify Admin → Apps → Judge.me → Reviews**, manage published/pending reviews, filter by product/rating/status, and choose your moderation settings. These controls live in the app, not Shopify's native product editor. Configure the available storefront sorting options in the app's widget settings.
6. In the Shopify theme preview, submit a test review on one product, verify that it appears for that product in Judge.me admin, check moderation/publication, and try the storefront sorting options. This live app check is still required.

Without an app widget, the section shows an honest unavailable state or existing standard Shopify rating/count metafields. It does not present a form that pretends to save reviews.

Other reviews apps can be added through the same app-block slot. Their own widget settings may also be needed to match the palette; the detailed widget CSS in this update targets Judge.me. Previously supported Main Product app blocks are retained. The default template turns off the old compact review summary to avoid a second review area.

Products assigned to custom product templates need the Product reviews section added to those templates as well. The updated export supplies it in `templates/product.json`.

## 3. Adjust the footer logo

Open **Customize → Footer**.

- The logo stays visible on mobile product pages. Only Shop and Help & Support navigation remains collapsible.
- The default asset uses its correct intrinsic dimensions (924 × 670) and is displayed without cropping, stretching or an added light background.
- **Desktop logo width** defaults to 240px. **Mobile and tablet logo width** defaults to 200px. Both can be adjusted; the logo is clamped to its available column width.
- **Footer logo (optional replacement)** accepts an uploaded logo. Leave it blank to use the existing Gujju Jewels asset.
- The sizing rules apply on home, product and other page templates. The brand text, links, social links, newsletter and policy links are retained.

## Validation and limits

The three changes were made sequentially, with the existing product checks run after each. Final local Chromium checks passed at **320, 360, 390, 430, 768, 990 and 1440px**.

Checked: count settings from 1–10; recommendation/fallback merging; duplicate/current-product exclusion; empty and limited collections; accordion mouse/keyboard interactions; variant sold-out synchronization; native sticky cart form binding; simulated quick-add; breakpoint resizing; footer image loading, visibility and proportions; review product IDs; honest unconnected review state; representative widget styling and unobstructed native controls. No horizontal overflow or browser errors were observed. Section JSON schemas, template JSON, new CSS and JavaScript syntax checks pass.

Shopify Theme Check still reports the original **11 findings**, including its existing parser-blocking script error, and no new findings. The inherited malformed final global CSS patch remains outside these changes.

The review screenshots are clearly labelled **design previews with sample app markup**. They are not screenshots of a connected Judge.me installation. Review submission, moderation, real app sorting, live Shopify recommendations/cart and physical-device Safari have not been verified from this environment.

Upload the version 2 ZIP as an unpublished theme and check it in Shopify before publishing. The advertised shipping/discount/gift terms still require separate Shopify promotion configuration.

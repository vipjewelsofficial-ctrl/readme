# Version 3 — VIP JEWELS footer, product reviews removed

The product review integration is removed for now. The default product template has no Customer Reviews section, unavailable message, compact rating area or Judge.me widget. Its added review section and stylesheet were removed. No review app/backend is included. Original homepage testimonial content is separate from that product review integration and is retained.

The footer now displays **VIP JEWELS** as text instead of an image. Its brand description and copyright use the same footer name. The default palette is deep burgundy (#5C1828), a darker wine gradient end (#35101B), warm ivory text (#FFF9EE) and gold headings/buttons (#ECD39A). Its former forced black background is overridden by footer-scoped styles so its settings now work.

## Shopify controls

Upload `Gujju-Jewels-Product-Updates-v3.zip` as an unpublished theme, then open **Customize → Footer**. You can edit:

- Footer brand name and description.
- Footer background and text colour.
- Brand and heading colour.
- Footer accent/button colour.
- Use gradient background, and Gradient end colour. Turn the gradient off for a solid footer.

Other palettes that suit the ivory/gold styling:

| Palette | Background | Gradient end |
| --- | --- | --- |
| Deep burgundy (default) | #5C1828 | #35101B |
| Forest green | #123D35 | #082720 |
| Midnight blue | #172D40 | #0C1926 |

The footer name is always visible on mobile. Product-page Shop and Help & Support menus remain expandable on mobile and open on desktop. Navigation, policy links, social links, newsletter and payment content are retained. Related-product counts from 1–10, offers, benefits, FAQ accordions and native/sticky Add to Cart are retained.

If you pause reviews on an existing theme instead of uploading this export, remove its review widget blocks and disable its Judge.me app embed in that theme's editor. This workspace cannot uninstall or change settings in the live Shopify app. No stored customer reviews were deleted.

## Checks

Local Chromium checks pass at 320, 360, 390, 430, 768, 990 and 1440px: no horizontal overflow or page errors; reviews absent; footer text present with no logo image; burgundy/gradient styles override the old black background; responsive navigation; variant sold-out synchronization; sticky form binding; simulated quick-add; FAQ/detail mouse/keyboard interactions; related-product counts 1–10 and deduplication.

JSON, section schemas, new CSS and JavaScript syntax checks pass. Shopify Theme Check still has the original 11 findings (one parser-blocking script error and ten warnings), with no new findings. The original malformed final global CSS patch remains outside this footer change.

Screenshots are local previews using sample product data. Live checkout, real Shopify recommendation results and physical-device Safari have not been verified. Nothing has been published to the live store. Preview the uploaded theme before publishing. Earlier ZIPs are preserved in the repository for rollback.

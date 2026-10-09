# Gujju Jewels — basic SEO audit

Audit date: 9 October 2026 (India). Source: `theme_export__gujjujewels-com-gujju-jewels-menu-theme-v5__09OCT2026-0135pm.zip`, 91 files. Product-data evidence is from the previously uploaded `products_export_1.csv`, not a fresh 9 October export. This is an audit only: no theme, product, navigation, checkout or store setting has been changed.

The uploaded theme provides a workable SEO foundation. The main work is connecting the actual catalogue to coherent collection landing pages, completing product metadata and image descriptions, adding validated product structured data, and checking indexing in Google Search Console. You do not need a paid SEO app to complete these basics. No ranking, traffic or conversion guarantee is implied.

## Scope and confidence

- **Confirmed in the backup:** theme code, homepage settings, asset sizes and configured links.
- **Confirmed in an older CSV:** product metadata, saved image alt fields, prices, vendors, types and taxonomy at that export date. Recheck before editing because the live catalogue may have changed.
- **Not verified live:** page status codes, collection contents, current metadata, robots.txt, sitemap.xml, Google indexing, installed-app schema, Search Console, Google Analytics, Merchant Center or actual Core Web Vitals.

Requests to the homepage, robots.txt, sitemap.xml and the oxidised collection were rejected by this execution environment's network proxy with CONNECT 403. This is **not evidence that your store returns 403 or blocks Google**. I cannot certify that the uploaded ZIP exactly matches the currently published theme or that Google can crawl the store.

## What is already present

| Foundation | Evidence | Assessment |
| --- | --- | --- |
| Dynamic page title | layout/theme.liquid:13–18 | Shopify `page_title` and shop name are supported. Long default product titles still need editorial work. |
| Meta description support | layout/theme.liquid:20–22 | Outputs Shopify `page_description` when provided. Missing custom SEO fields do not prove the live description is absent; Shopify can derive defaults. |
| Canonical link | snippets/meta-tags.liquid:35 | Present and based on `canonical_url`. Do not add a second canonical tag. Live targets still need checking. |
| Open Graph/social tags | snippets/meta-tags.liquid:14–34 | Title, description, URL, type and conditional share image supported. |
| Main headings | hero.liquid:79, main-product.liquid:75, main-collection.liquid:21, main-page.liquid:4, main-article.liquid:1 | The principal templates have an H1; supporting homepage sections use H2/H3. Product descriptions in the older CSV do not add extra heading tags. |
| Crawlable links | header.liquid, gujju-built-in-menu.liquid, product-card.liquid:91–93, pagination.liquid | Native HTML anchors for navigation, products and pagination. A JavaScript-only navigation rebuild is unnecessary. |
| Product descriptions | main-product.liquid:81–84 and product-mobile-details.liquid:43 | Rendered server-side, including the accordion. The older CSV has descriptions for all 21 products. Collapsing a description in an accessible accordion does not automatically prevent indexing. |
| Image alt fallback | main-product.liquid:20; product-card.liquid:27–28 | Uses saved alt text or product title. Improve the saved values, rather than assuming every image has no alt attribute. |
| Responsive image delivery | main-product.liquid:24–32; hero.liquid:24–67 | Shopify image resizing/srcset on selected uploads; eager/high-priority main images and lazy-loading secondary content. |
| Language and viewport | layout/theme.liquid:2,6 | Locale language and mobile viewport are present. Multi-market hreflang still requires a live check if you use multiple languages/markets. |
| Useful policy links | footer.liquid:81–85,125–138 | Links render if policies exist in Shopify. Actual policy content and contact/about pages are separate store data. |

## Priority 1 — collection landing pages and relevant internal links

### 1. Verify the five collection URLs first — required store check

The included menu targets these URLs:

| Landing page | Handle | Expected older-catalogue count |
| --- | --- | ---: |
| Necklace Sets | necklace-sets | 15 |
| Oxidised Jewellery | oxidised-jewellery | 8 |
| Gold-Tone Jewellery | gold-tone-jewellery | 13 |
| Mangalsutras | mangalsutras | 3 |
| Accessories | accessories | 2 |

Check that each returns a real collection page, contains the appropriate products and is available to Online Store. Counts overlap intentionally. The backup does not contain collections or membership, so I cannot say these are currently missing. Never treat installing the menu as creating the collections.

**Shopify action:** Products → Collections. Assign products, publish to Online Store, verify URL handles, and preview each collection. Use the earlier collection-memberships.csv reference. If an existing collection uses a different handle, either link to it through the custom Shopify menu or change the handle with a redirect.

**Verification:** open each URL logged out on mobile and desktop; test representative product links; use Search Console URL Inspection for availability/canonical/indexing.

### 2. Fix homepage category and style links — confirmed in this backup

`templates/index.json` still displays Earrings, Necklaces, Bangles & Bracelets, Rings, Jewellery Sets and Hair Accessories. None has a selected collection. Four explicit links point to `/collections/all`; the other two fall back to it in `category-directory.liquid:39–43`. All six category tiles therefore target Shop All.

The four Shop by Style cards—Oxidised, Traditional, Statement and Everyday—also have no selected collection or URL. `collection-card-grid.liquid:37–42` sends each to Shop All.

This is not a proven crawl failure, but it weakens the relationship between link labels and destination pages and makes navigation less useful. Your older catalogue has no standalone rings/bangles/earrings range; matching earrings inside necklace sets should not be presented as a standalone earrings catalogue.

**Shopify action:** Customize → Home page → Shop by Category / Shop by Style. Select relevant collections and align the category labels with the real range: Necklace Sets, Oxidised Jewellery, Gold-Tone Jewellery, Mangalsutras and Accessories. No new layout or checkout feature is required.

The Hero's Shop Now and New Arrivals button links are both blank. Both fall back to Shop All in `hero.liquid:87,92`. Shop Now can reasonably remain Shop All; New Arrivals should link to a real new-arrivals collection or the existing `/#new-arrivals` section. The footer already links to that section.

### 3. Add collection content and unique metadata — not verifiable from a theme export

Each collection needs a descriptive title, an original helpful introduction, relevant products, and distinct SEO title/description. Explain the actual designs and included pieces rather than repeating a generic paragraph on every collection. There is no compulsory word count. A concise useful introduction is enough; avoid filler and keyword stuffing.

The theme already renders `collection.description` when enabled (`main-collection.liquid:22–23`). Actual collection descriptions and SEO fields are stored in Shopify, not in the ZIP.

**Shopify action:** Products → Collections → collection → Description and Search engine listing → Edit. See `homepage-collection-seo-proposals.csv` for suggested metadata. These are drafts, not an automatic importer or a ranking promise.

## Priority 2 — product metadata, imagery and catalogue trust

### 4. Complete custom product SEO fields — evidence from the older CSV

| Field | Completed | Remaining to review |
| --- | ---: | ---: |
| Custom SEO title | 4 / 21 | 17 |
| Custom SEO description | 3 / 21 | 18 |
| Product description | 21 / 21 | Review accuracy/detail, not blank fields |
| Image alt text saved in export | 0 / 81 image rows | 81 image descriptions |

19 of the 21 product titles are longer than 70 characters; the range is 43–144 characters. Long titles are not a Google penalty, and character limits are not fixed ranking rules, but the default search title may become difficult to scan or be truncated. Write concise distinctive SEO titles without changing existing product handles. Existing good custom titles can be retained.

**Example product SEO title:** `Oxidised Mirror Work Necklace Set | Gujju Jewels`.

**Shopify action:** Products → product → Search engine listing → Edit. Prioritise the best-selling necklace sets, then the remaining products. Google may rewrite titles/descriptions; meta descriptions mainly help communicate the result and earn relevant clicks, rather than acting as a direct ranking factor.

`product-seo-proposals.csv` provides drafts for all 21 older-export products. It is a reference sheet, not a Shopify import CSV. Confirm each product's current stock/content before saving.

### 5. Describe images accurately — confirmed older CSV gap, not absent rendered attributes

The theme fills blank image alt values with the product title. That is a useful fallback, but every image then gets essentially the same text.

Use image-specific descriptions, for example:

- Oxidised mirror-work necklace set with matching earrings — front view.
- Floral pendant detail on a gold-tone pearl necklace set.
- Back clasp and adjustment chain on the necklace.

Describe the actual image; do not apply 'front view' to every photo or stuff city names/keywords. Decorative images may correctly have empty alt text. A model photo's alt should describe the model wearing the relevant jewellery, rather than repeat a marketing headline. The Hero currently uses its heading as alt text (`hero.liquid:52,63`); a separate descriptive image-alt option would improve this.

**Shopify action:** open product media → Edit alt text. Use your actual product photographs for the banner, category tiles and social imagery where possible. The backup has no custom Hero images selected, so it uses its bundled demo images.

### 6. Align the headline, material claims and brand information

The homepage H1 remains **Statement Silver, Crafted with Soul**. This focuses the site on silver despite an older catalogue containing 13 gold-tone and 8 oxidised products. It can also blur the distinction between silver-tone fashion jewellery and sterling silver.

Suggested H1: **Traditional Necklace Sets & Oxidised Jewellery**. Suggested supporting copy: **Discover gold-tone and oxidised designs for festive and everyday styling.** Confirm material claims from suppliers; do not add 925/sterling, nickel-free or hypoallergenic claims without support.

The current footer settings correctly say **Gujju Jewels**; this backup no longer uses VIP JEWELS as its saved footer wordmark. However, the older product CSV has Vendor **My Store** on 19 products and **GujjuJewels** on 2. The main product template visibly renders Vendor (`main-product.liquid:71–72`). If still current, standardise it to the appropriate actual brand. Changing Vendor is a catalogue-cleanup action, not a magical ranking factor.

### 7. Recheck the ₹0 product and product classification — older CSV only

`traditional-gold-tone-chandbali-necklace-set` had a variant price of ₹0. Verify it is intentional or correct it before merchant listings and structured offers use the live price. Do not copy an invented price into schema.

Only 2 products have Type, 2 have Tags, and one choker was Uncategorized. Consistent classification helps collection rules, feeds and catalogue management; Type/Tags are not direct SEO scores. The CSV has no GTIN values; do not invent barcodes. Assign real manufacturer identifiers only when available and use appropriate identifier handling for unbranded/custom products.

## Priority 3 — structured data and technical validation

### 8. Add or verify Product structured data — absent from theme files

There are no `application/ld+json`, `schema.org` or `product | structured_data` calls in the uploaded theme. Open Graph product price tags are social metadata; they do not replace Product JSON-LD.

This is a gap in the theme, not proof that the live page has no structured data: installed apps or Shopify's runtime header could inject it. Test representative live product URLs in Google's Rich Results Test first.

If absent, use Shopify's built-in product `structured_data` filter or carefully implemented Product JSON-LD based on actual product/variant data. Include appropriate product identity, canonical URL, images and offers with real currency, price and availability. Review shipping/returns data for merchant-listing enhancements where applicable. Ensure there are no conflicting duplicate offers after adding it.

Product structured data supports Google's understanding and rich-result eligibility; it is not required simply to get indexed and does not guarantee enhanced results. Do not add fabricated ratings/reviews. The previously removed review system does not need to be reinstated for basic SEO.

Organization data with the actual Gujju Jewels identity/logo, and useful breadcrumb navigation/BreadcrumbList are secondary improvements. This theme has no explicit breadcrumb component or organization JSON-LD. Use a stable hierarchy for products that belong to overlapping collections. FAQ schema is not a priority for a jewellery store; Google generally limits FAQ rich results to authoritative government/health sites.

### 9. Confirm indexing and crawl controls in Shopify / Google — currently unverified

- Verify the domain in Google Search Console and submit `https://gujjujewels.com/sitemap.xml`.
- Inspect Home, the five collection pages and representative products. Check Google's selected canonical and any exclusion reason.
- Ensure the storefront is publicly accessible without a password and Online Store publication is correct.
- Confirm the primary HTTPS domain and intended redirects from www/other domains. Do not infer redirect behaviour from this ZIP.
- Check `/robots.txt` and `/sitemap.xml` live. Shopify normally generates them; their absence from the theme archive is not an SEO defect.
- Review indexing of internal search, cart/account and filter/sort URLs. Preserve useful product/collection pages. Do not blanket-block `/collections`, assets or scripts.
- If URLs were renamed, add proper redirects from old URLs to relevant new destinations. A 404 template existing is normal; dead links pointing to it need attention.
- If using multiple markets/languages, inspect live hreflang and canonicals before adding manual tags. `content_for_header` is retained; do not remove it.

Search Console records impressions, clicks, queries and indexing. A `site:` search alone cannot prove complete indexing. Google Analytics 4 is useful for measurement/conversions, but installing it is not a ranking requirement. Neither Search Console nor analytics configuration can be inferred from this backup because integrations may live outside theme files.

## Priority 4 — performance and remaining polish

### 10. Optimise the header logos before blaming the banner

The bundled desktop logo is 600,058 bytes and mobile logo 371,013 bytes. Both are eager `<img>` elements in the header, with CSS deciding which is visible. They use the original asset URLs rather than Shopify-resized CDN image URLs. In a local Chromium fixture of this backup at both 390 and 1440px, both logo files were requested, totalling 971,071 bytes before any browser cache. This is a request/asset observation, not a measurement of live transfer time or Core Web Vitals.

The desktop banner is about 186 KB and the mobile banner about 95 KB; these are smaller than the header logo files. Optimise logos to suitable dimensions and formats while checking quality/transparency. Prefer responsive `<picture>` delivery or resized Shopify images to avoid downloading both versions. Reduce competition between logo requests and the actual largest-content image.

The theme loads approximately 100 KB of uncompressed global CSS across three stylesheets. This is not automatically excessive; measure actual transfer/cache/compression and unused styles before consolidation. `theme.js` uses a parser-blocking `script_tag` at layout/theme.liquid:107; assess a deferred script with functional regression testing. External Google Fonts already have preconnect/async stylesheet loading; avoid redesigning fonts without measurement.

Use PageSpeed Insights and Search Console Core Web Vitals for live evidence. Useful good thresholds at the 75th percentile are LCP ≤2.5 s, INP ≤200 ms and CLS ≤0.1. These are targets, not measured results from this audit. A local preview is not a live performance score or field-data measurement.

### 11. Repair the inherited CSS syntax separately from SEO content work

`assets/homepage.css:3214` contains literal escaped `\n` sequences in its final patch. This can make selectors in that block parse incorrectly. It does not prove that Google cannot index the store, but a tidy-up should be tested for category/footer styling regressions. No CSS has been changed in this audit.

Shopify Theme Check reports 11 findings: one ParserBlockingScript error and ten warnings (four RemoteAsset, one AssetPreload, one OrphanedSnippet, four UnusedAssign). These are code-quality/performance findings, not 11 confirmed SEO failures. Unused assignments and an orphan snippet are low priority for search visibility.

### 12. Finish social previews, favicon and trust pages

- No custom favicon is saved in this backup. Add a legible square brand favicon in Theme settings; useful for recognition, not a direct ranking boost.
- Set/verify a homepage social-sharing image under Shopify Preferences/available theme settings, commonly 1200×630. Current OG image output depends on `page_image`; a banner upload does not prove a homepage sharing image has been set.
- Meta-tags has no explicit twitter:image; platforms may fall back to OG imagery. Its OG dimensions use original image dimensions while requesting a resized width; these are minor sharing improvements.
- Product OG prices use locale-formatted `money_without_currency`; check large prices for comma separators and use an appropriate machine-readable decimal if needed.
- Confirm an informative About page, working contact details, shipping, returns/refund, privacy and terms content. Policies need truthful details matching checkout. Templates alone do not establish that those pages exist.
- The footer social account URLs are blank in the backup. Add genuine official profiles if you have them; a social profile link is not a guaranteed ranking signal.
- Product reviews can remain removed as requested. Never add invented aggregate ratings to satisfy an SEO checklist.

## Suggested metadata to start with

**Home SEO title:** Traditional Necklace Sets & Oxidised Jewellery | Gujju Jewels

**Home meta description:** Shop traditional necklace sets, oxidised jewellery, gold-tone designs and mangalsutras at Gujju Jewels. Discover jewellery for festive and everyday styling.

**Oxidised collection title:** Oxidised Jewellery & Necklace Sets | Gujju Jewels

**Oxidised collection description:** Discover oxidised necklace sets and maang tikka designs at Gujju Jewels, featuring floral, mirror-work, pearl-style and traditional pendant details.

Save homepage metadata under Online Store → Preferences (or the current equivalent in Shopify admin), and collection/product metadata under the individual resource's Search engine listing. Character lengths are editorial guides, not hard SEO rules; check how actual titles read on mobile.

## Recommended implementation order

1. Verify working populated collections, Online Store availability and public crawl access.
2. Correct homepage category/style destinations and align the Hero copy with the real catalogue.
3. Save homepage/collection metadata; complete missing custom product SEO fields and image alt descriptions.
4. Validate and implement product structured data if the live pages currently lack it.
5. Resolve the older ₹0 price/vendor/classification findings if they are still current.
6. Verify Search Console and sitemap, then monitor index coverage and search queries.
7. Optimise logo delivery and resolve the script/CSS issues with cart/product/checkout regression checks.
8. Complete social preview/favicon/trust content; add relevant advice articles later if useful.

Useful future content includes choosing a necklace set for an outfit, caring for oxidised fashion jewellery, and styling mangalsutras. Blog articles and link-building campaigns are secondary to fixing the catalogue/landing-page basics. Avoid bulk AI pages, fabricated reviews, irrelevant keyword pages or unnecessary paid SEO tools.

## Verification evidence and scope

The archive is intact and all 91 extracted files remain byte-for-byte equal to its entries. Shopify Theme Check ran on this backup. Local Liquid/browser checks verify canonical/social output, a single Hero H1 and no horizontal overflow in the reviewed header/hero at 390 and 1440px; Shopify objects/requests are adapted for the local fixture. These checks do not establish live indexing, crawlability or field performance.

Included files: `seo-checklist.csv`, `product-seo-proposals.csv`, `homepage-collection-seo-proposals.csv`, `catalogue-evidence.json`, `theme-evidence.json`, and `review/theme-check.json`. No modified theme ZIP is provided because no changes were requested.


## Reference guidance

- Google Search Central: SEO Starter Guide — https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Product structured data — https://developers.google.com/search/docs/appearance/structured-data/product
- Image SEO — https://developers.google.com/search/docs/appearance/google-images
- Title links — https://developers.google.com/search/docs/appearance/title-link
- Snippets/meta descriptions — https://developers.google.com/search/docs/appearance/snippet
- Canonical URLs — https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- Rich Results Test — https://search.google.com/test/rich-results
- PageSpeed Insights — https://pagespeed.web.dev/

These are reference links for applying the recommendations; this session did not retrieve their current contents.

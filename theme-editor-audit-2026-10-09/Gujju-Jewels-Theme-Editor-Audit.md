# Gujju Jewels — Shopify theme editor audit

Source: `theme_export__gujjujewels-com-gujju-jewels-menu-theme-v5__09OCT2026-0705pm.zip`.
Audit date: 9 October 2026. Scope: uploaded theme code and saved configuration, not the live Shopify admin.

**The theme is partially configurable, rather than entirely hardcoded.** Many homepage features already have Shopify controls. The clearest defects are settings that appear in the editor but are never used or are overridden by later CSS. The slideshow and image-only hero mode are absent features. This audit changes no theme files and introduces no functionality.

## Coverage and verification

- Inventoried all 91 files: 36 Liquid, 14 JSON, 6 CSS, 3 JavaScript and 32 static image assets. Static images were inventoried as assets; they are not executable code.
- Mapped all 27 section schemas plus global settings: 279 declared input definitions, including block field definitions. This is not 279 different features or necessarily 279 controls on a particular screen.
- Checked settings references, dynamic offer/benefit keys, schema blocks, template usage, locale coverage, JavaScript behaviours and the final CSS cascade.
- Ran local Liquid fixtures and Chromium checks at mobile 390×900 and desktop 1440×900 for the consequential ignored controls. These fixtures use synthetic products/menus and local assets, not authenticated Shopify data.
- Confirmed every extracted theme file still matches the upload byte for byte. No theme changes, Shopify admin changes, publication or purchases were performed.
- Theme Check reported 11 findings: one parser-blocking script error-level finding and ten warnings (four remote assets, four unused assignments, one stylesheet-preload warning and one unused snippet). These are existing issues; the theme should not be described as error-free. The final homepage CSS also contains literal escaped newline sequences in a legacy patch; this is a separate cleanup item, not an editor feature.

## Controls that already exist

| Feature | Where to edit | Available control |
|---|---|---|
| Featured Products | Customize → Home page → Featured Products | Collection, product count 2–16, desktop columns 2–5, headings, colours, spacing and View All visibility. Use a manually ordered collection to choose/order products. |
| New Arrivals | Customize → Home page → New Arrivals | Same count/collection/layout fields. A selected collection supplies its product order; the unselected all-products fallback is sorted by publication date. |
| Related products | Customize → Products → Default product → You may also like / recommendations | Enable, title, subtitle, product count 1–10 and fallback collection. Requested count is an upper limit, not a guarantee that enough eligible products exist. |
| Shop Categories | Customize → Home page → Shop Categories → Category group | Upload image, select collection, title, description, badge, fallback link and up to four subcategory collections/labels. Base content is editable. |
| Collection Card Grid | Customize → Home page → Collection Card Grid | Add/edit collection-card blocks, images, links, titles and descriptions. |
| Offers and product benefits | Customize → Products → Default product → Product Information | Four offer texts; three benefit title/subtext pairs; description-open and sticky-cart options. Text fields work, but slot counts/icons are fixed. |
| FAQs | Customize → FAQ sections → question blocks | Add, remove, reorder and edit questions/answers. |
| Benefits | Customize → Benefits / Why Choose Us → benefit blocks | Select from existing icons and edit title/description. |
| Testimonials | Customize → Reviews / Testimonials → review blocks | Manually enter real customer text/rating/name. This does not collect customer submissions. |
| Footer branding | Customize → Footer | VIP JEWELS wordmark, description, colours/gradient, social links and newsletter copy. Footer Menu 2/3 do not work. |
| Favicon | Customize → Theme settings → favicon field | Already connected and configured to `website-favicon.png` in this backup. |
| Colour palette and sizes | Customize → Theme settings | Global palette, font sizes, widths, spacing and radius controls; documented component-specific constraints still apply. Font families are not selectable. |
| Collection page | Customize → Collections → Default collection | Description/count visibility, filter/sort switches, desktop columns 3/4 and products per page 12–36 in steps of 4. |
| Main menu | Shopify Content → Menus; then Customize → Header | Disable Use built-in menu and choose the native menu. Built-in mode bypasses the selected native menu. |

Homepage sections in the JSON template can be reordered, hidden and removed. Main Product's internal elements cannot be dragged independently because they are not blocks. Section names may vary slightly with Shopify's editor display.

## Detailed limitations and possible later changes

Priority reflects this store's stated needs. A missing optional control is not automatically a bug. “High” items are candidates for the first implementation pass, not changes made by this audit.

| ID | Priority | Feature | Classification | Finding | Source evidence | Possible later action |
|---|---|---|---|---|---|---|
| 01 | High | Hero slider | Missing feature | One hero image pair; no slide blocks, navigation, swipe or autoplay controls. | sections/hero.liquid:109; assets/theme.js:6 | Add a slideshow section or extend Hero with editable slide blocks; retain the current single-image option. |
| 02 | High | Hero image-only mode | Missing control | The content panel always has markup, even when its text and buttons are cleared. No show/hide panel setting exists. This causes duplicated content over an already designed banner. | sections/hero.liquid:82 | Add an image-only/content-overlay switch; preserve accessible text and real clickable links. |
| 03 | High | Hero height | Ignored setting | Minimum height is set inline but !important CSS replaces it: 300px and 800px selections both computed to 648px at 1440×900 and 680px at 390×900. | sections/hero.liquid:19; assets/homepage.css:3137; assets/homepage.css:3153 | Connect desktop/mobile height controls to the final responsive CSS. |
| 04 | High | Hero mobile panel | Partly ignored settings | On mobile, panel colour/opacity, content width and text alignment are constrained by fixed CSS. Opacity 0 and 100 both computed to the same 92% ivory background at 390px. Desktop opacity worked. At widths ≤380px the heading-size choices are also overridden by a fixed 31px font size. | assets/simple-theme.css:306; assets/simple-theme.css:316 | Respect the existing settings or expose separate mobile panel controls. |
| 05 | Medium | Hero mobile image alone | Conditional limitation | The mobile image is used only inside the desktop-image branch. Selecting only a mobile image still displays demo images. The current export has a desktop image selected and no separate mobile image. | sections/hero.liquid:23 | Allow a mobile-only selection with a defined desktop fallback. |
| 06 | Medium | Banner fit, position and link | Missing controls | Hero has no whole-image destination, image-only link, fit-to-image mode or crop-mode selector. Collection Banner has no separate mobile image. A button painted into an image is not an actual link. | sections/hero.liquid:82; sections/collection-banner.liquid:18 | Add the required image/link/fit controls when implementing the slideshow. |
| 07 | High | Header menu source | Available but bypassed | Built-in navigation has seven fixed titles and handles. With Use built-in menu enabled, the selected native Shopify Menu is ignored by design. This export has built-in mode enabled. | sections/header.liquid:2; snippets/gujju-built-in-menu.liquid:6 | Already editable: disable Use built-in menu in Header, then select the menu managed in Shopify Content → Menus. |
| 08 | Medium | Header text logo fallback | Unused setting | Text logo fallback is assigned to logo_text but never displayed. A built-in Gujju Jewels image is displayed instead when no logo is selected. | sections/header.liquid:11; sections/header.liquid:43 | Render the text setting as a selectable fallback; retain image upload options. |
| 09 | High | Header background and divider | Ignored settings | Desktop/mobile background and divider fields generate variables, but later CSS uses global palette variables. Red/green backgrounds and a blue divider were not reflected at either tested width. | sections/header.liquid:20; assets/simple-theme.css:37 | Use the header-specific variables in the final style rules. |
| 10 | Medium | Built-in logo sizing | Partly ignored setting | The mobile built-in image has a fixed responsive clamp instead of mobile_logo_width. Uploaded logos have width controls; the desktop built-in image is height-constrained. | sections/header.liquid:238; sections/header.liquid:248 | Make the built-in sizing policy explicit or connect it to the existing width fields. |
| 11 | Medium | Header layout and mobile account icon | Fixed design | No logo-alignment or search/cart visibility controls. The account icon is hidden in the mobile header by CSS even if Show account is enabled; the account link is available in the mobile menu when accounts are enabled. | assets/homepage.css:502; sections/header.liquid:23 | Add layout controls only if desired; account authentication remains Shopify-managed. |
| 12 | High | Footer Menu 2 and Menu 3 | Unused settings | Both fields appear in the editor and are assigned, but neither is rendered. Synthetic menu links for these two fields never appeared in the output. | sections/footer.liquid:3; sections/footer.liquid:4 | Render the selected menus and their headings. |
| 13 | High | Footer navigation | Hardcoded content | Shop and Help & Support headings and the base links are fixed. Menu 1 only appends up to four links and excludes a link titled Search. New Arrivals and Trending Picks target fixed homepage anchors. | sections/footer.liquid:63; sections/footer.liquid:69; sections/footer.liquid:82 | Use editable menu columns and heading settings while preserving dynamic Shopify policy links. |
| 14 | Medium | Footer newsletter and legal labels | Missing controls/hardcoded text | Heading and description are editable, but there is no newsletter visibility toggle. Subscribe, success text and the copyright suffix are literal strings. Clearing the heading does not remove the form. | sections/footer.liquid:98; sections/footer.liquid:120; sections/footer.liquid:134 | Add a visibility field and use locale keys or appropriate text settings. |
| 15 | Low | Product-page mobile footer accordion | Fixed behaviour | JavaScript transforms footer navigation into closed disclosures on product pages at widths ≤989px. No accordion toggle, breakpoint or default-open control exists. | assets/product-mobile-details.js:78 | Expose a control if this behaviour needs merchant configuration; preserve the current default. |
| 16 | Medium | Category button label | Setting hidden by CSS | The category-level Button label is rendered but the shop-link element is hidden on every viewport. Image/title links still function; the section-level bottom button is separate. | sections/category-directory.liquid; assets/simple-theme.css:267 | Add a show-category-button control or make the existing label visible. |
| 17 | Medium | Category shape and responsive columns | Fixed design | Category media is forced circular with a fixed size cap; no circle/square/aspect-ratio setting. Desktop columns are configurable; mobile/tablet grid changes are prescribed by CSS. | assets/simple-theme.css:264; assets/simple-theme.css:304; assets/homepage.css:1027 | Expose shape and mobile-column options only if required. |
| 18 | Medium | Social gallery empty state | Hardcoded fallback | No post blocks means six built-in demo photos are shown on the storefront. There is no show-demo switch. The gallery is manual content, not a connected Instagram feed. | sections/social-gallery.liquid:45 | Add an empty-state/demo toggle; actual images/captions/links are already editable post blocks. |
| 19 | High | Collection Banner overlay | Ignored setting | Changing overlay opacity from 10 to 80 still yields a transparent overlay because its background is forced transparent. | sections/collection-banner.liquid:42; assets/simple-theme.css:274 | Restore an actual overlay colour and respect opacity. |
| 20 | Medium | Product-page component order | Fixed layout | Main Product has settings but no component blocks. Gallery/vendor/title/price/quantity/options/cart/details order cannot be rearranged individually; no @app block support in Main Product. Separate template sections can be managed in the editor. | sections/main-product.liquid:16; sections/main-product.liquid:160 | Convert only the required product components into editable blocks; preserve product-form logic. |
| 21 | Medium | Product offer count and icons | Fixed slots | Four offer texts are editable, but the maximum count and percentage icon are fixed. Clearing a text hides that offer; no Add offer block supports a fifth. | snippets/product-mobile-details.liquid:8; sections/main-product.liquid:172 | Use offer blocks if flexible count/icons are needed. These messages do not create discounts or gifts. |
| 22 | Medium | Product benefit count and icons | Fixed slots | Three benefit titles/subtexts are editable. The maximum count and return/shipping/COD icon assignments are fixed. | snippets/product-mobile-details.liquid:68; sections/main-product.liquid:180 | Use benefit blocks if flexible count/icons are needed. |
| 23 | Low | Product trust fallback | Hardcoded text | Disabling the expanded product details shows three fixed strings: Secure checkout, Carefully packed and Customer support. | sections/main-product.liquid:150 | Expose text fields only if retaining this fallback. |
| 24 | Low | Product accordion defaults | Partial control | Description open/closed is configurable; Shipping & Returns and product FAQ default-open behaviour is fixed. Policy content is drawn from Shopify policies or the shipping text setting. | snippets/product-mobile-details.liquid:38; sections/mobile-product-faq.liquid | Add default-open controls if desired; policy content does not need hardcoding. |
| 25 | Medium | Product cards | Missing display controls | No editor switches for second-image hover, quick add, Sale/Sold Out badges or savings display. Card wording is mostly literal English. Product titles/photos/prices/availability themselves come from Shopify products. | snippets/product-card.liquid:26; snippets/product-card.liquid:88; snippets/price.liquid | Add product-card switches and locale keys while keeping native product/variant data. |
| 26 | Low | Product-card Boolean parameters | Code defect; no UI currently | show_quick_add:false and lazy_load:false are overridden by Liquid default:true. Local rendering confirmed quick add and lazy loading remained enabled. Current callers use the defaults, so this is a latent configuration defect. | snippets/product-card.liquid:11 | Preserve explicit false values before exposing these options. |
| 27 | Medium | Related-product display | Partial control | Enable, heading, subheading, fallback collection and count are editable. Count is 1–10. Responsive columns and recommendation-loading behaviour are fixed; no theme product-list picker for individual related products. | sections/mobile-product-recommendations.liquid:40; assets/product-mobile-details.js:50 | No count change needed. Add layout/product-selection controls only if requested; Shopify supplies recommendation results. |
| 28 | Low | Featured/New Arrivals product selection | Partial control | Collection and product count are editable (2–16), as are desktop columns (2–5). No direct product_list picker or section sort-mode field. New Arrivals sorts all-product fallback by publication date only when no collection is selected; a selected collection uses its order. View All wording has a fixed prefix. | sections/featured-products.liquid:3; sections/new-arrivals.liquid:14 | Use an ordered Shopify collection now; add individual selection/sort/text controls only if required. |
| 29 | Medium | Font family selection | Hardcoded design | Inter and Cormorant Garamond are loaded explicitly; there is no font_picker setting. Font-size settings already exist. | layout/theme.liquid:34; assets/theme.css:51; config/settings_schema.json | Add body/heading font pickers and connect loading/CSS to them. |
| 30 | Low | Spacing and radius limits | Partially constrained controls | Section-specific spacing overrides global spacing. Some mobile section padding is capped at 72px. Category circles and product panels override radius defaults; product panels have a minimum 12px radius. | assets/simple-theme.css:148; assets/simple-theme.css:232; assets/product-mobile-details.css:8 | Document intended overrides or add separate mobile/component controls. |
| 31 | Medium | Cart labels and layout | No section settings | Main Cart has an empty settings array. Headings, labels, empty-state text, arrow arrangement and checkout wording are code-defined. Quantity arrows and autosave exist; no Update Cart button is rendered. | sections/main-cart.liquid:97; assets/cart-quantity.js | Expose labels/layout only if desired; preserve existing quantity/checkout behaviour. |
| 32 | Medium | Search page | No section settings | Fixed headings/placeholders, product-only search, 24 results per page and four-column desktop grid. No merchant controls for these choices. | sections/main-search.liquid:1; sections/main-search.liquid:19; sections/main-search.liquid:25 | Add appropriate text, result-count and layout settings; broader search requires matching result rendering. |
| 33 | Low | Blog listing and article layout | No section settings | Blog listing uses 12 articles per page, three columns, a 180-character excerpt and literal Read more. Blog/article content is editable in Shopify; template layout is fixed. | sections/main-blog.liquid:1; sections/main-article.liquid | Add layout/display controls only when needed. |
| 34 | Low | Contact form | No section settings | Name/Email/Phone/Message fields, required email/message, Send message and success wording are fixed. Page title/body remain editable Shopify page content. | sections/main-contact.liquid:1 | Add configurable field/label options while preserving Shopify contact form processing. |
| 35 | Low | 404, pagination and general labels | Hardcoded text | 404 content, Previous/Next, collection toolbar labels, price accessibility text and quick-add status messages are largely literal strings rather than locale keys. Editing default theme content cannot change literals. | sections/main-404.liquid; snippets/pagination.liquid; snippets/price.liquid; assets/theme.js:144 | Move customer-facing strings into locales; use section text settings where appropriate. |
| 36 | Low | Header/footer section placement | Fixed layout structure | Announcement, header and footer are static section calls in the layout rather than section groups. Homepage template sections can be reordered; the header/footer areas cannot be freely composed into groups. | layout/theme.liquid:76; layout/theme.liquid:83 | Use section groups only if flexible header/footer composition is required. |
| 37 | Low | Legacy duplicate Footer section | Inactive component | custom-footer.liquid is a separate older Footer with different controls/fallback imagery. The active layout uses footer.liquid. Editing or adding the legacy section will not control the live static footer. | sections/custom-footer.liquid; layout/theme.liquid:83 | Keep this distinction visible; consolidate only in a later explicitly scoped change. |
| 38 | Low | Media and runtime policies | Normal code-driven behaviour | Product image swapping, variant price/availability sync, cart request handling, mobile drawers, breakpoint thresholds and retry timings are implemented in JavaScript/CSS without merchant fields. No slideshow, predictive-search interface or review submission backend is present. | assets/theme.js; assets/cart-quantity.js; assets/product-mobile-details.js | These are implementation details, not automatically missing Shopify features. Expose only the behaviours the merchant needs to configure. |

## Saved configuration matters

The latest export selects `Jewellery_for_Every_Celebration.png` for the desktop hero, while the old overlay heading/subtext/buttons remain configured. Therefore the duplicated panel is explained by two layers of content, rather than an inability to upload an image. There is no separate mobile hero image selected.

Featured Products and New Arrivals have blank collection selections with all-products fallback enabled. Several homepage category blocks also have no collection selection and default/fallback destinations. Assigning the intended collections is Shopify configuration work; it does not require building new collection pickers. A URL or label does not create a collection or assign products to it.

The Social Styling Gallery has no configured post blocks, so its six demo images are shown. Add real posts or hide/remove this section now; the proposed empty-state control is a later code improvement. Empty testimonial blocks are hidden from normal storefront output, while the theme editor can show an explanatory empty state. No customer review submission system was found in the uploaded product template; restoring one would be a separate task.

`list-collections.json` uses the manual Shop Categories section with no blocks. It is not an automatic directory of all Shopify collections. Add category-group blocks and select collections in that template to populate it.

## Shopify admin data versus theme code

| Item | Managed in Shopify / external service | What theme code can do |
|---|---|---|
| Product titles, descriptions, photos, image alt text, prices, variants, vendor and inventory | Products | Display the stored data; editing the display is different from changing the catalogue. |
| Collection names, handles, products, images, descriptions and order | Products → Collections | Render assigned collections; a theme ZIP cannot create their records. |
| Native menus and dropdown hierarchy | Content → Menus | Select/render the menu; menu records are not imported with the theme ZIP. |
| Policy contents | Settings → Policies | Show policy content and dynamic URLs. Some surrounding labels are hardcoded. |
| Collection filter definitions | Shopify Search & Discovery | Render configured filters when enabled. |
| Customer accounts/login/sign-up | Shopify customer account settings | Link to accounts; the screenshot's mobile-OTP checkout needs an actual checkout provider/integration. |
| Native COD, online gateway, settlements and KYC | Settings → Payments / chosen provider | Direct customers to Shopify checkout. No dedicated Releasit/Shiprocket COD integration was found in the uploaded source. Installed app injections cannot be audited from this ZIP alone. |
| Real discounts, gifts and shipping thresholds | Discounts / shipping settings / relevant app | Offer text is promotional display only; changing it does not enforce the offer. |
| Homepage SEO title/description and store name | Shopify preferences / store settings | Render platform values and document-title rules. These are not missing homepage visual-editor fields. |
| Real customer review storage/moderation | Review app or a backend integration | Style/render a widget; theme-only Liquid/JavaScript does not supply an admin-managed review database. |

## Complete section inventory

| Section file | Editor name | Input definitions | Block types | Current configuration access |
|---|---|---|---|---|
| announcement-bar.liquid | Announcement Bar | 5 | None | Text, destination, marquee switch and colours are exposed. |
| benefits.liquid | Benefits / Why Choose Us | 7 | benefit | Heading, palette, spacing and benefit blocks with icon/title/description are exposed. |
| category-directory.liquid | Shop Categories | 16 | category_group | Category/subcategory blocks, images, collections, links, text, desktop columns, counts and palette are exposed; category button hidden and circle shape fixed. |
| collection-banner.liquid | Collection Banner | 7 | None | Image/text/link/position exposed; opacity overridden; separate mobile image absent. |
| collection-card-grid.liquid | Collection Card Grid | 16 | collection_card | Collection-card blocks with image/title/link/badge/description and section controls are exposed. |
| custom-footer.liquid | Footer | 11 | None | Older alternative Footer, not the footer used by the layout; do not confuse with active Footer. |
| custom-liquid.liquid | Custom Liquid | 1 | None | Liquid text input is exposed; advanced code entry, not merchant controls for existing components. |
| faq.liquid | FAQ | 7 | faq_item | Questions/answers, heading, palette and spacing exposed; native accordion defaults fixed. |
| featured-products.liquid | Featured Products | 13 | None | Collection, 2–16 products, 2–5 desktop columns, headings, View All visibility, palette, spacing and anchor exposed. |
| footer.liquid | Footer | 18 | None | Wordmark, description, colours/gradient, socials, newsletter copy and payment-icon visibility exposed; Menu 2/3 unused, base links fixed. |
| header.liquid | Header | 17 | None | Native menu available with built-in mode disabled; uploaded logos/account/badge controls exposed; text fallback unused, backgrounds/divider overridden. |
| hero.liquid | Hero Banner | 20 | None | Desktop/mobile image, headings, CTA labels/links, colour and position controls exist; no slideshow or image-only mode; height/mobile panel controls overridden. |
| main-404.liquid | Main 404 | 0 | None | No section settings; error-page text and layout literal. |
| main-article.liquid | Article | 0 | None | No section settings; article content comes from Shopify. |
| main-blog.liquid | Blog | 0 | None | No section settings; Shopify supplies blog/article content; listing layout fixed. |
| main-cart.liquid | Main Cart | 0 | None | No section settings; Shopify supplies cart contents; existing arrow/autosave behaviour is code-driven. |
| main-collection.liquid | Main Collection | 7 | None | Description/count/filter/sort switches, 3–4 desktop columns and 12–36 products per page (steps of 4) exposed. |
| main-contact.liquid | Contact page | 0 | None | No section settings; page title/content from Shopify, form fields fixed. |
| main-page.liquid | Main Page | 0 | None | No section settings; page title/content from Shopify Pages. |
| main-product.liquid | Main Product | 17 | None | 17 settings including details visibility, four offer texts, three benefit title/text pairs and sticky-cart visibility; main component order fixed. |
| main-search.liquid | Main Search | 0 | None | No section settings; search text, result type/count and layout fixed. |
| mobile-product-faq.liquid | Product FAQs | 2 | question | Enable, heading and question/answer blocks exposed; also appears on larger screens despite its internal filename. |
| mobile-product-recommendations.liquid | Related products | 5 | None | Enable, heading/subheading, 1–10 related products and fallback collection exposed; responsive layout fixed. |
| new-arrivals.liquid | New Arrivals | 13 | None | Collection, 2–16 products, 2–5 desktop columns, headings, View All visibility, palette, spacing and anchor exposed. |
| reviews.liquid | Reviews / Testimonials | 7 | review | Manual testimonial blocks with rating/text/customer/location/product and palette/spacing exposed; not customer-submitted product reviews. |
| shop-by-price.liquid | Shop by Price | 9 | price_card | Price-card blocks with labels/description/collection/link/colours exposed; labels do not generate real price-filter rules. |
| social-gallery.liquid | Social Styling Gallery | 12 | post | Manual post blocks and section controls exposed; empty blocks trigger six demo images; not a live Instagram feed. |

## Recommended sequence after this audit

1. Agree the scope for Hero: slideshow blocks, separate desktop/mobile images, image-only or overlay mode, real links and reliable responsive sizing. Keep the current single-banner behaviour as a supported option.
2. Repair ignored editor controls in Hero, Header, Collection Banner and Footer without altering cart/checkout logic.
3. Only then add requested optional controls such as fonts, product-card switches, flexible product-detail blocks and mobile layout options.

Do not rebuild Featured Products, New Arrivals, related-product count, FAQ content or the favicon picker merely to make them editable: controls already exist. Do not reintroduce reviews, alter COD/checkout or change branding during these fixes without a new instruction.

Supporting files: `findings.csv` (38 grouped findings), `section-accessibility.csv` (all 27 sections), `editor-settings-inventory.csv` (279 schema inputs), `javascript-functions.csv` (named functions/helpers), `file-coverage.csv` (91 source hashes), `schema-map.json`, `control-verification.json` and `theme-check.json`.

The static direct-unused candidates in schema-map are investigative hints, not final findings: dynamic setting keys can be functional. The final report and render checks resolve those cases. Live account, payment, review-app and catalogue state were not verified against authenticated Shopify.

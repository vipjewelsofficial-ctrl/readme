# Gujju Jewels — Shopify Editable Theme v6

Complete theme based on the latest 09 Oct 2026, 07:05pm v5 export. All original files remain included. This changes theme-editor accessibility and adds a hero slideshow; it does not install an app, create collections, change product prices or activate a payment gateway.

## Upload the theme

Shopify Admin → Online Store → Themes → Add theme / Import theme → Upload ZIP. Select `Gujju-Jewels-Shopify-Editable-v6.zip`. The ZIP contains the Shopify theme folders at its root; the source directory and this guide are for reference only.

Open Customize on the uploaded draft. Preview your actual products, menus and chosen images before publishing. The live theme was not modified by this work.

## Where to make changes

| Area | Shopify editor location | Controls |
|---|---|---|
| Hero slideshow | Home page → Hero Banner | Add Slide blocks (up to 8 additional slides); keep or hide original slide; per-slide images, text, buttons and destination; autoplay, interval, arrows and dots |
| Designed banner artwork | Hero Banner → Content display | Image only shows embedded artwork without another text panel. Overlay text uses editable heading/copy/buttons. The existing first hero is set to Image only and Adapt to image. Original heading and button values are retained. |
| Hero responsiveness | Hero Banner | Separate desktop/mobile images, desktop/mobile height, adapt/fixed mode, cover/contain fit, panel width/colour/opacity/alignment; mobile-only selection supported |
| Header / announcement | Header group | Existing colour, logo and menu settings work; choose image/text logo, alignment, search/cart icon visibility and mobile account icon |
| Navigation | Header → Use built-in menu | Keep enabled to edit the seven included menu titles/URLs. Disable to select a native Shopify menu, managed under Content → Menus. The existing included menu selection is preserved. |
| Footer | Footer group → Footer | Three menu pickers, column headings, base-link visibility, link limit, newsletter/policy visibility, contact destination, brand text/sizes/alignment, colours/gradient and product-page accordion defaults |
| Product information | Products → Default product → Main Product | Reorder/remove/add Vendor, Title, Price, Description, Buy buttons, Details and Trust blocks; add custom text or compatible app blocks; gallery placement, quantity visibility, description presentation and shipping disclosure default |
| Offers / benefits | Main Product → Offer / Benefit blocks | Add/delete/reorder rows and choose their icons/text. Current content was migrated into blocks. Keep the Details block to display offers, accordions and benefits. Legacy fields remain for old/custom templates and are used only when their block switches are off. |
| Product cards | Theme settings → Product cards | Quick add, second-image hover, Sale/Sold out badges, compare price and savings switches |
| Featured / New Arrivals | Home page → relevant section | Collection or individually selected products, count, collection/newest/price/title ordering, desktop/mobile columns and View All wording |
| Related products | Products → Related products | Count 1–10, automatic recommendations or chosen products, fallback collection, desktop/mobile columns, colours and spacing. Unique products determine the actual maximum shown. |
| Categories | Home page → Shop Categories | Editable category blocks, show category buttons, circle/square/portrait images, image size, tablet/mobile columns and spacing |
| Collection banner | Home page → Collection Banner | Separate mobile image, overlay colour/opacity, editable text/button or whole-image destination, fixed/adapt height and image fit |
| Social gallery | Home page → Social Styling Gallery | Manual image/caption/link blocks, demo fallback visibility, link target and mobile columns. It is a manual gallery, not an Instagram API connection. |
| Fonts / global appearance | Theme settings → Layout & typography / Colours | Native Shopify body/heading font pickers, sizes, colours and existing shape/layout controls |
| FAQ | Home page or product FAQ → Question blocks | Question/answer content and each question’s default-open state |
| Cart | Cart template → Main Cart | Headings, labels, empty state, checkout wording, quantity control size/radius/colour and section colours/spacing. Always-visible arrows and automatic saves are retained. |
| Search | Search template → Main Search | Headings/placeholders, product-only or products/pages/articles, result count, columns, empty-state text and colours/spacing |
| Contact / pages / blog / article / 404 | Select corresponding template → main section | Field/label/display options, listing counts/columns/excerpts, article image/date/author/back link, page title/layout, 404 text/destination and colours/spacing |
| Shared interface wording | Themes → … → Edit default theme content | Pagination, collection filters/sorting, product-card and cart status messages, review-free product detail labels, slider accessibility and footer/legal wording |
| Header/footer composition | Customize → Header / Footer groups | Reorder supported group sections or add compatible sections. The original header/announcement/footer settings are copied to the group JSON files. |

The old duplicate Footer section is now labelled **Legacy Footer** to distinguish it from the active Footer. It remains in the package for compatibility.

## Store-managed data and behaviour

Products, collections, inventory, prices, native menus, policies, customer accounts, shipping, normal COD and payment gateway settings are edited in Shopify Admin. A ZIP cannot create those records or change checkout authentication. Text about free shipping/gifts/discounts does not create shipping rules, gifts or discount codes. Compatible app blocks require the corresponding app.

No customer review system or third-party COD app code was introduced. Normal checkout and existing cart behavior remain in place. JavaScript request handling and breakpoints remain implementation details; merchant-facing display choices are exposed in settings.

## Preservation and validation

44 original files modified, 5 new files, 47 original files byte-for-byte unchanged; 96 files in the ZIP. No original file was deleted. All original image assets and settings_data.json are unchanged. Original homepage/product section ordering is retained.

Shopify Theme Check: zero errors; one existing warning for the unused product-image snippet retained for compatibility. All theme JavaScript passed syntax checks and CSS has no top-level parser errors. Editor controls, slideshow navigation/swipe/autoplay/reduced motion/reloading, variant availability/prices, quick add, sticky native product form, footer responsiveness and cart controls were checked locally. Product/cart layouts passed at 320, 360, 390, 430, 768, 990 and 1440px; cart checks also covered 13 error/concurrency edge cases. Theme schema defaults/ranges, saved block references, section groups and archive integrity were validated.

Local test products and mocked Shopify responses were used; real order/payment/contact processing and installed apps require a draft preview in your store. Preview images in this folder show fixture content, not your live storefront. Source asset handles and the existing brand text from your uploaded theme are retained.

See [file-manifest.csv](file-manifest.csv), [editor-settings.csv](editor-settings.csv), [package-validation.json](package-validation.json) and [validation](validation) for detailed evidence.

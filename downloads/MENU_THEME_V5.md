# Complete theme with included Gujju Jewels menu — Version 5

Upload `Gujju-Jewels-Menu-Theme-v5.zip` in Shopify → Online Store → Themes → Add theme → Upload ZIP. Preview the new theme before publishing. This is a complete Shopify theme ZIP, unlike the earlier menu setup reference package.

The desktop navigation and mobile hamburger automatically show:

Home → Necklace Sets → Oxidised Jewellery → Gold-Tone Jewellery → Mangalsutras → Accessories → Shop All

Only the existing `sections/header.liquid` changes, and one new snippet `snippets/gujju-built-in-menu.liquid` is added. All other 89 files from the uploaded Version 4 export are preserved byte-for-byte, including cart quantity arrows/autoupdate, native checkout, footer, colours, offers, related products, product pages, FAQs and homepage configuration. The archive contains 91 theme files. The header logo is retained.

## Collection destinations

The included menu makes the requested links appear immediately without needing a Shopify navigation menu. It does NOT create Shopify store collections. If missing, create these manual collections under Products → Collections and make them available to Online Store:

| Collection | URL handle | Expected products |
| --- | --- | ---: |
| Necklace Sets | necklace-sets | 15 |
| Oxidised Jewellery | oxidised-jewellery | 8 |
| Gold-Tone Jewellery | gold-tone-jewellery | 13 |
| Mangalsutras | mangalsutras | 3 |
| Accessories | accessories | 2 |

Use the collection-memberships.csv reference from the earlier menu setup package to assign products. Existing collections with these handles are reused automatically. If a collection is missing, its menu link points to its expected URL and will not work until the collection is created. Home and Shop All use Shopify's native routes. Prices, product types, tags, inventory and collection membership were not modified.

## Use a custom Shopify menu later

Online Store → Themes → Customize → Header: switch off **Use included Gujju Jewels menu**, then choose your Shopify menu using the existing **Menu** picker. Nested links up to three levels and the existing configurable sale badge continue to work. Keeping the included menu switched on displays the fixed requested seven-item launch structure. To rename or restructure it through Shopify menus, switch this option off and select your custom menu.

## Checks and limits

Local Chromium previews pass at 320, 390, 768, 990, 1024 and 1440px, with the exact seven labels and no horizontal overflow or JavaScript page errors. Mobile menu open/Escape-close works. Native custom-menu markup with three levels and sale badge is identical to the original when the included menu is disabled. Localized fallback collection paths, collection URL resolution, current-page highlighting and default activation without an existing saved setting are checked.

Shopify Theme Check reports the same 11 inherited findings as Version 4, with no new check types or issues in the added snippet. Existing global styles and their known malformed final CSS patch were left unchanged as requested. Preview checks do not confirm live collection existence or replace testing the uploaded theme in Shopify. No theme was published to the live store from this workspace.

# Gujju Jewels — requested Shopify menu

The uploaded theme already supports editable Shopify menus on desktop and mobile, with nesting up to three levels. The Header Menu setting uses `main-menu`. No theme code needs changing to use the requested navigation.

Shopify menus and collection membership are store data; they are not included in theme exports and cannot be installed by uploading a theme ZIP. No Shopify admin connection is available in this session, so the menu and collections have NOT been uploaded to your live store.

## 1. Create five manual collections

In Shopify admin → Products → Collections → Create collection, choose Manual and use these titles/URL handles:

| Collection title | URL handle | Products |
| --- | --- | ---: |
| Necklace Sets | necklace-sets | 15 |
| Oxidised Jewellery | oxidised-jewellery | 8 |
| Gold-Tone Jewellery | gold-tone-jewellery | 13 |
| Mangalsutras | mangalsutras | 3 |
| Accessories | accessories | 2 |

If these collections already exist, reuse them. Make them available to the Online Store sales channel. Use `collection-memberships.csv` to select the exact products for each collection. It is a reference sheet, not a Shopify product-import file. Membership overlaps intentionally. Accessories includes the maang tikka and bracelet watch. The standalone temple necklace belongs to Gold-Tone Jewellery. All 21 products remain in Shop All.

Manual collections avoid changing your product types, tags, prices, categories or other product data. No CSV re-import is needed.

## 2. Set the requested menu

Shopify admin → Content → Menus → Main menu (older admin: Online Store → Navigation).

Use these seven items, in this order:

| Label | Link |
| --- | --- |
| Home | Home page |
| Necklace Sets | Collections → Necklace Sets |
| Oxidised Jewellery | Collections → Oxidised Jewellery |
| Gold-Tone Jewellery | Collections → Gold-Tone Jewellery |
| Mangalsutras | Collections → Mangalsutras |
| Accessories | Collections → Accessories |
| Shop All | All products (/collections/all) |

Save. Keep GUJJU JEWELS as the existing brand/logo, not an eighth menu link. The requested launch list contains no named submenu items, so do not invent dropdown entries. The existing theme supports adding nested links later when you decide what they should be.

If you prefer to preserve Main menu, create a separate menu with these items, then Online Store → Themes → Customize → Header → Menu and select it. This changes only the menu selection.

## 3. Verify in the theme preview

Open desktop and mobile previews. Check all seven labels and links. Open/close the mobile hamburger. Visit each collection to confirm the counts and products. Menus link to existing collections; do not save placeholder links before creating their destinations. Link targets in this setup pack assume the URL handles listed above; select the actual collection resource in Shopify when setting each link.

The local header preview checks the requested seven labels and mobile menu controls at 320, 390, 768, 990, 1024 and 1440px. This does not verify that the collections exist on the live store.

## Product export findings

81 CSV rows contain 21 distinct products, all active: 15 necklace sets, 3 mangalsutras, 1 standalone necklace, 1 maang tikka and 1 bracelet watch. Styles: 8 oxidised and 13 gold-tone. The floral pearl necklace set's description explicitly confirms gold-tone accents.

Only 2 products have Type and 2 have Tags. One choker is Uncategorized. The Chandbali Necklace Set has a ₹0 variant price; review its price in Shopify before selling it. No product data or prices have been changed by this setup pack.

## Scope

All 90 uploaded theme files remain unchanged. Header logo, footer, colours, homepage sections, offers, related products, FAQs, Add to Cart, automatic cart quantity arrows, Remove and native checkout are untouched. No COD app, product review feature, extra menu entry or homepage reordering is added.

`menu-definition.json`, `menu-links.csv` and `collection-memberships.csv` are setup references. Shopify has no built-in menu import for these files. They are not a substitute for creating the menu in Shopify admin or through an authorized Admin API connection.

# Shopify product section save repair

Shopify rejected the prior main-product.liquid section with:
`FileSaveError: Invalid block details: name is too long (max 25 characters)`.

The details block label is shortened from `Offers, details & benefits` (26 characters) to `Offers & benefits` (17 characters). No block IDs, settings, product logic, layout or styles change. The product.json template is unchanged.

In the theme you are testing, save all of sections/main-product.liquid first, then all of templates/product.json. The template filename is product.json, singular. Existing files should have their complete contents replaced; do not append these files. Do not upload this two-file ZIP as a complete Shopify theme.

Validation: all section, block and preset names in the source theme checked against the 25-character limit; only this label exceeded it. JSON parses, referenced sections exist, block types/order resolve, and the ZIP round-trips. Native Shopify saving and product URL rendering still require merchant verification.

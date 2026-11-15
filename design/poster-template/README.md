# Seamens product poster template

Owner-approved design (Nov 15, 2026): `base.jpg` is the approved EcoShort-GS-777 poster.

## What the script changes on the base
- a bigger Seamens logo card (top left) and a bigger logo on the drum label
- on the drum label, the IPO mark is replaced by the Industrial Grade mark
- a bigger CONAIR-PAK tick badge in the side panel
- NET WEIGHT per pack size
- a QR code to the product's own page

## Make posters for a product
1. Copy `products/ecoshort-gs-777.json` to `products/<slug>.json` and edit:
   - name, subtitle, form, headline, benefits (8 × [title, line])
   - packs
   - folder (`eco-series` / `water-safe`)
   - version
   - `"redraw": true`
2. Run `python3 design/poster-template/poster.py <slug>` from the repo root.
3. Output:
   - `images/products/<slug>-<kg>kg-v<version>.webp`, `-sm.webp`, `-full.webp`, `.jpg`, `-sm.jpg` (website)
   - `images/products/posters/<Name>-<kg>KG-v<version>.jpg` (3200px original for the owner)
4. Check every word against the site, then put the files on the product page (the pack-size slider is in `design/page-generator/cat_orig.html`).

Changing an image means bumping `version` (images are cached for 1 year).

This folder is excluded from deploy (`.vercelignore`).

# CLAUDE.md: Seamens Enterprises Website

Read this first in every session. The full content rules are in `SEAMENS-BLOG-KNOWLEDGE-BASE.md` (757 lines, excluded from deploy via `.vercelignore`). This file covers **how we work** and the **latest owner decisions, which override the knowledge base wherever the two conflict**.

## 1. Working workflow (owner: Usman, works from mobile)

1. Usman gives a task in chat, in Urdu/Hindi/English. Reply in simple Roman Urdu with English technical terms.
2. Do the work on the session's `claude/...` feature branch. **Never push straight to `main`.**
3. Run the checks (Section 5), commit, and push the branch.
4. Open a **draft PR** to `main`, or reuse the open PR for the branch.
5. Vercel creates a **Preview deployment** automatically for every pushed branch. Get the preview URL from the commit status (`gh api repos/aitsaamali/seamens-enterprises-website/commits/<sha>/statuses`, context `Vercel`) or from the PR checks, and send Usman:
   - the PR link
   - the Vercel preview link
   - the exact pages to check on the phone
6. **Wait for Usman's explicit "live karo" or "approve".** Only then mark the PR ready and merge it into `main`. A push to `main` triggers the Vercel **Production** deploy to https://www.seamensenterprises.com.
7. After the merge, confirm the production deployment succeeded and send the live link.

Vercel project: `aitsaamalis-projects/seamens-enterprises-website`. Production deploys come only from `main`.

## 2. Company facts (never alter)

- **Seamens Enterprises**, est. **1997**, Lahore, Pakistan
- Address: Plot No. 51, Street No. 1, Awal Khair Stop, Al-Saeed Chowk, Main Sharqpur Road, Lahore
- Phone: **+92-302-6686354** · WhatsApp: **+92-305-4444125** (`https://wa.me/923054444125`)
- Domain: https://www.seamensenterprises.com
- Certifications: ISO 9001:2015, ISO 45001, IPO Pakistan registered, FBR NTN and Sales Tax registered. Never invent more.
- CONAIR / Luwa-Nederman: Seamens' water treatment chemicals are **certified by** them for use in their equipment. Never write "authorised agent", "distributor" or "partner".

## 3. Latest owner decisions (override the knowledge base)

From commits `378eb74`, `3b2088b` and `7eafc7d` (Oct 2026):

- **German based technology (updated Nov 14, 2026):** describe the chemicals only as "German based organic chemical technology" (or "German based technology"), with the SVG German flag. **Never write "Made in Germany"** anywhere (owner instruction). Never use the Pakistani flag or the phrase "Made/manufactured in Pakistan". The knowledge base's "never say Germany" rule is outdated. Spare parts may still be described as sourced from Germany, Italy and China.
- "Locally manufactured" is now worded as **locally stocked / supplied**.
- **No personal author bylines** and no "Head of Digital Presence" byline anywhere. The homepage "in numbers" facts section was removed on owner request. Schema `author` is the Organization.
- **ECO-Series has 19 products.** EcoSil-SS was replaced by **Eco-SilSoftner Glazer / Hydrophobic / Hydrophilic**.
- **Water Safe series** includes FC-30B and FC-7090 (FC-70/90). The product names on the live `index.html` are the single source of truth for spelling.
- Product detail tables (EcoSize-CXW-111, EcoShort-GS-777, EcoAcryllic-ACL-55, D-11) come from the owner's sheets. Don't change figures unless the owner sends new ones.
- **All blog posts share one stylesheet:** `assets/blog.v1.css`. Don't add per-post CSS.

Still valid from the knowledge base:

- Never disclose formulation details.
- Stay positive and never disparage competitors.
- Every product claim must match the catalog. Example: EcoFix-FB is formaldehyde-based.
- End each post with a WhatsApp CTA. **Never offer free samples or free trials** (owner decision, Nov 14, 2026: people asked for free samples and did not order). Use wording like "Contact us for more details" and "Product details, pricing and trial terms are shared on request". Free water analysis offers on Water Safe pages are still live (not yet decided).

## 4. Open decisions (ask Usman before acting)

- **"X vs Y" posts.** 13 published comparison posts in `/blog/*-vs-*` conflict with the "one product per post, no comparisons" rule. Keep, rewrite or rename? Not yet decided.
- **Updating the knowledge base.** The knowledge base still contains the old Pakistan-manufacturing rule and the 17-SKU list. Should it be updated to match Section 3?
- **Image optimisation.** 119 images, mostly JPEG, with "WhatsApp Image ..." filenames. Convert to WebP and rename? That would need every reference updated.

## 5. Technical conventions and checks

- Static HTML/CSS/JS with no build step, deployed on Vercel. Config is in `vercel.json`: headers, CSP, redirects and rewrites.
- Blog file: `/blog/{slug}.html`. Public URL: `/{slug}` (clean). Every new post needs:
  - a `vercel.json` redirect `/blog/{slug}.html` → `/{slug}` and a rewrite `/{slug}` → `/blog/{slug}.html`
  - a `sitemap.xml` entry
  - a blog card on `blog/index.html` and the homepage where relevant
  - an `llms.txt` / `llms-full.txt` update
- **Images, CSS and JS are cached for 1 year (`immutable`).** Never change a file's content under the same name: give it a new versioned name (e.g. `-v5` → `-v6`) and update every reference, or returning visitors (and Usman's phone) keep seeing the old file.
- The CSP allows scripts only from self and cdnjs, and fonts from Google. Don't add other CDNs without updating the CSP.
- Before every push:
  - check internal links (no broken `href`/`src`)
  - validate JSON-LD (it must parse)
  - make sure `vercel.json` is valid JSON
  - check the layout at 375px mobile width with Playwright
- Never commit secrets. The quote form has no backend: `request-quote.html` sends the enquiry to WhatsApp.

## 6. Dedicated product pages and posters

- Every branded product has its own page (added Nov 2026):
  - 19 ECO-Series pages at `/products/eco-series/{slug}`, files in `products/eco-series/`
  - 12 Water Safe pages at `/products/water-safe/{slug}`, files in `products/water-safe/`
  - Each new page needs a `vercel.json` rewrite (clean URL to `.html`), a `.html` to clean URL redirect and a `sitemap.xml` entry.
- Each page has:
  - unique copy
  - a key-facts card
  - benefits and applications
  - technical tables from the owner sheets, where they exist
  - FAQ
  - related products and guides
  - Product, BreadcrumbList and FAQPage JSON-LD
  - shared styles from `assets/product-page.v1.css`
- Never duplicate a product's full details on the category pages. Category pages link to the product pages.
- Also on request (Nov 2026):
  - 14 cleaning chemical pages at `/products/cleaning/{slug}` (Product schema)
  - 15 engineering service pages at `/products/services/{slug}` (Service schema): boilers, humidification, cooling towers, chillers, RO plants, erection, parts, maintenance and fabrication
  - The site now has 60 item pages in total. Keep every page's copy unique: pairwise 5-gram Jaccard is currently at most 0.15.
  - Since Nov 14, every item page has at least 1,000 words of main content (owner rule: no thin pages). Sections: how it works, benefits in detail, problems it solves, how to measure results, where it delivers the most value, buyer's guide, Pakistan context, practical tips, FAQ (6-8), and references and standards (WebPage `citation` schema). Item pages use `assets/product-page.v3.css`.
  - **Reading layer (Nov 14):** all blog posts and item pages load `assets/reading.v1.css` and `assets/reading.v1.js`. These add an "On this page" TOC, a FAQ accordion, phone card layout for tables, a reading progress bar and a mobile WhatsApp/Call bar. New posts must include both files.
  - **Cleaning chemical pack sizes:** not yet supplied by the owner. Pages show "Confirmed with your quote". When Usman sends the sizes, fill `CL_PACK` in the generator's `cl_pack.py` and regenerate.
  - **Comparison ("X vs Y") posts:** owner said don't write new ones for now (Nov 14).
  - `llms-full.txt` has a section for each of the 60 pages, and blog posts link to product pages at the first mention of each product name.
- **Navigation and interlinking (Nov 14):** every page's nav has a Products mega menu listing all 6 groups and all 60 item pages (desktop hover/click; on mobile, an accordion inside the hamburger menu). It uses `assets/megamenu.v1.css` and `.js`. The homepage has a "Find any product or service in one tap" directory (`#all-products`), a "View all" link under each product tab, and clickable industry badges. `/products` has the same directory. The menu HTML is generated by the scratchpad generator's `menu.py` and inserted by `navpatch.py`; run it after `gen.py` / `gen2.py`, and add any new item to the menu.
- **Adding a product poster:**
  1. Save it as `images/products/{slug}-v1.webp` (about 1080px wide) plus a 720px `-sm` version.
  2. In the product page hero, replace the `<figure class="pp-media">` block with a `<figure class="pshow">` block. Copy the one in `products/eco-series/ecoshort-gs-777.html`.
  3. Link `assets/product-showcase.v1.css` and `.js` on that page.
  4. Set the Product JSON-LD `image` to the poster.
  5. Check the poster's facts against the site.
- **Poster v2 (approved by Usman, Nov 14, 2026):** `images/products/ecoshort-gs-777-v2.webp` (1080), `-v2-sm` (720) and `-v2-full` (2048, opened by the zoom link; its QR scans). Design: the owner's reference poster, enhanced with the Canva AI image tool, then corrected in code:
  - real Seamens logo and real certification marks
  - textile-accurate benefit lines
  - "Office & Warehouse" address heading
  - no 24/7 badge
  - NET WEIGHT box and certification strip wrapped around the drum
  - QR card linking to the product page
  A 125 KG version is live as `ecoshort-gs-777-125kg-v1(-sm|-full).webp`. The page shows a **pack-size switcher**: CSS-only radio tabs from `assets/pack-switch.v1.css`, up to 4 sizes, with one image per pack size; markup lives in the generator's `cat_orig.html` poster block. Use the same switcher for the next products. Next products follow the same recipe, one product at a time, each reviewed by Usman. Always check AI text for spelling, invented badges and wrong-industry wording before use.

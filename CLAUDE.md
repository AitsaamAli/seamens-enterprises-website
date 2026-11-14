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

- **Made in Germany:** the site now says "German based organic chemical technology, made in Germany" and uses an SVG German flag. Never use the Pakistani flag or the phrase "Made/manufactured in Pakistan". The knowledge base's "never say Germany" rule is **outdated**.
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
- End each post with a WhatsApp CTA that makes a specific free offer.

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
  - Since Nov 14, every item page has at least 1,000 words of main content (owner rule: no thin pages). Sections: how it works, benefits in detail, problems it solves, how to measure results, where it delivers the most value, buyer's guide, Pakistan context, practical tips, FAQ (6-8), and references and standards (WebPage `citation` schema). Item pages use `assets/product-page.v2.css`.
  - `llms-full.txt` has a section for each of the 60 pages, and blog posts link to product pages at the first mention of each product name.
- **Adding a product poster:**
  1. Save it as `images/products/{slug}-v1.webp` (about 1080px wide) plus a 720px `-sm` version.
  2. In the product page hero, replace the `<figure class="pp-media">` block with a `<figure class="pshow">` block. Copy the one in `products/eco-series/ecoshort-gs-777.html`.
  3. Link `assets/product-showcase.v1.css` and `.js` on that page.
  4. Set the Product JSON-LD `image` to the poster.
  5. Check the poster's facts against the site. GS-777's poster says 250 KG; the site says 125–240 KG (open question for Usman).

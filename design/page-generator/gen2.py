import extra, json, html, urllib.parse, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from cl_data import CL, CL_PARENT
from cl_pack import CL_PACK
from sv_data import SV
ROOT = '/home/user/seamens-enterprises-website'
SITE = 'https://www.seamensenterprises.com'
cat = open(os.path.join(os.path.dirname(__file__), 'cat_orig.html'), encoding='utf-8').read()
STYLE = cat[cat.index('<style>'):cat.index('</style>') + 8]
NAV = cat[cat.index('<nav>'):cat.index('</nav>') + 6]
TAIL = cat[cat.index('<a href="https://wa.me/923054444125" target="_blank" rel="noopener" class="wa-float"'):cat.index('</footer>') + 9]
esc = lambda s: html.escape(s, quote=True)
js = lambda d: '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False, separators=(',', ':')) + '</script>'

def build(p, kind):
    cl = kind == 'cl'
    folder = 'cleaning' if cl else 'services'
    url = f'{SITE}/products/{folder}/{p["slug"]}'
    parent = CL_PARENT if cl else p['parent']
    label = 'Industrial Cleaning' if cl else 'Engineering Services'
    img = '/images/hero/industrial-cleaning-v5-sm.webp' if p['img'] == 'industrial-cleaning' else f'/images/cards/{p["img"]}.webp'
    wa_txt = (f'Assalam o Alaikum, please share the price and usage advice for {p["name"]}.' if cl
              else f'Assalam o Alaikum, I would like to discuss {p["name"]} for our plant. Please arrange a call or site visit.')
    wa = 'https://wa.me/923054444125?text=' + urllib.parse.quote(wa_txt)
    og = {'/products/industrial-cleaning-chemicals': 'industrial-cleaning-v5.jpg', '/products/boiler-water-treatment-humidification': 'steam-boilers-v5.jpg',
          '/products/cooling-tower-chiller-ro': 'cooling-tower-v5.jpg', '/products/plant-erection-machinery-parts': 'industrial-exhaust-fan-v5.jpg'}[parent[0]]
    og_img = f'{SITE}/images/og/{og}'
    if cl:
        facts = [('Product', p['name']), ('Application', p['app']), ('Department', p['dept']), ('Form', p['form']), ('Pack sizes', CL_PACK.get(p['slug']) or 'Confirmed with your quote')]
    else:
        facts = [('Service', p['name']), ('Category', parent[1])] + [('Scope', x) for x in p['scope']]
    facts_html = ''.join(f'<div class="pp-fact"><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>' for k, v in facts)
    body_html = ''.join(f'<h2>{esc(h)}</h2>' + ''.join(f'<p>{esc(x)}</p>' for x in paras) for h, paras in p['body'])
    two = ('<div class="pp-two"><div class="pp-box"><h2>Key benefits</h2><ul>' + ''.join(f'<li>{esc(b)}</li>' for b in p['benefits']) +
           f'</ul></div><div class="pp-box"><h2>{"Where it is used" if cl else "Who it is for"}</h2><ul>' + ''.join(f'<li>{esc(a)}</li>' for a in p['apps']) + '</ul></div></div>')
    steps = (['Tell us the surface, soiling and area you need to clean.', 'Seamens recommends the product, dilution and routine.', 'Try it on site; we adjust the dilution if needed.', 'Agree regular supply for your housekeeping or maintenance team.'] if cl else
             ['Share your requirement, drawings or the problem you want solved.', 'Seamens visits the site and assesses the scope.', 'You receive a written proposal with scope and timeline.', 'Seamens executes, tests and hands over, with support afterwards.'])
    steps_html = f'<h2>{"How to get started" if cl else "How a project starts"}</h2><ol class="pp-steps">' + ''.join(f'<li>{esc(s)}</li>' for s in steps) + '</ol>'
    allp = {x['slug']: x for x in (CL if cl else SV)}
    rel_html = f'<h2>Related {"products" if cl else "services"}</h2><div class="pp-rel">' + ''.join(
        f'<a href="/products/{folder}/{r}"><b>{esc(allp[r]["name"])}</b><span>{esc(allp[r]["dept"] if cl else allp[r]["parent"][1])}</span></a>' for r in p['related']) + '</div>'
    KIND = kind
    ALLFAQ = extra.faqs(KIND, p['slug'], p['faqs'])
    EX = extra.sections(KIND, p['slug'], p['name'])
    REFH, RKEYS = extra.refs_html(KIND, p['slug'])
    faq_html = '<div class="faq"><h2>Frequently Asked Questions</h2>' + ''.join(f'<div class="faq-q">{esc(q)}</div><div class="faq-a">{esc(a)}</div>' for q, a in ALLFAQ) + '</div>'
    cta = (f'<div class="cta-box"><h3>{"Get the right " + esc(p["name"]) + " for your site" if cl else "Discuss " + esc(p["name"]) + " for your plant"}</h3><p>{"Tell us what you need to clean, and we will recommend the product, dilution and routine." if cl else "Tell us your requirement, and we will arrange a call or a site visit."}</p>'
           f'<a href="{wa}" target="_blank" rel="noopener" class="cta-btn">WhatsApp +92-305-4444125</a></div>')
    guides_html = '<div class="related"><h3>Related Guides</h3><div class="related-grid">' + ''.join(
        f'<a href="{u}" class="related-card"><div class="rc-cat">{label}</div><div class="rc-title">{esc(t)}</div></a>' for u, t in p['guides']) + f'<a href="{parent[0]}" class="related-card"><div class="rc-cat">Products</div><div class="rc-title">All {esc(parent[1])}</div></a></div></div>'
    schema_bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE},
        {"@type": "ListItem", "position": 2, "name": "Products", "item": f"{SITE}/products"},
        {"@type": "ListItem", "position": 3, "name": parent[1], "item": SITE + parent[0]},
        {"@type": "ListItem", "position": 4, "name": p['name'], "item": url}]}
    if cl:
        main = {"@context": "https://schema.org", "@type": "Product", "@id": url + "#product", "name": p['name'], "description": p['lead'],
                "brand": {"@type": "Brand", "name": "Seamens Enterprises"}, "manufacturer": {"@id": f"{SITE}/#organization"},
                "category": "Industrial cleaning chemicals", "url": url, "image": SITE + img,
                "additionalProperty": [{"@type": "PropertyValue", "name": k, "value": v} for k, v in facts[1:] if not v.startswith('Confirmed with')]}
    else:
        main = {"@context": "https://schema.org", "@type": "Service", "@id": url + "#service", "name": p['name'], "description": p['lead'],
                "serviceType": p['name'], "provider": {"@id": f"{SITE}/#organization"}, "areaServed": {"@type": "Country", "name": "Pakistan"},
                "url": url, "image": SITE + img,
                "hasOfferCatalog": {"@type": "OfferCatalog", "name": p['name'], "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": x}} for x in p['scope']]}}
    schema_f = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in ALLFAQ]}
    schema_w = {"@context": "https://schema.org", "@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p['title'], "inLanguage": "en-PK", "datePublished": "2026-11-13", "dateModified": "2026-11-14", "isPartOf": {"@id": SITE + "/#website"}, "publisher": {"@id": SITE + "/#organization"}, "citation": extra.citations(RKEYS)}
    out = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(p["title"])}</title>
<meta name="description" content="{esc(p["meta"])}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<link rel="canonical" href="{url}">
<link rel="icon" type="image/png" href="/images/seamens-logo-transparent.png">
<link rel="apple-touch-icon" href="/images/seamens-logo-transparent.png">
<meta property="og:type" content="{"product" if cl else "website"}">
<meta property="og:title" content="{esc(p["h1"])}">
<meta property="og:description" content="{esc(p["meta"])}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Seamens Enterprises">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_PK">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(p["title"])}">
<meta name="twitter:description" content="{esc(p["meta"])}">
<meta name="twitter:image" content="{og_img}">
{js(schema_bc)}
{js(main)}
{js(schema_f)}
{js(schema_w)}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Barlow:wght@300;400;500;600&family=Barlow+Condensed:wght@500;700&display=swap" rel="stylesheet">
{STYLE}
<link rel="stylesheet" href="/assets/product-page.v3.css">
<link rel="stylesheet" href="/assets/reading.v1.css">
</head>
<body>
{NAV}

<header class="pp-hero">
  <div class="pp-crumb" role="navigation" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><a href="/products">Products</a><span aria-hidden="true">/</span><a href="{parent[0]}">{esc(parent[1])}</a><span aria-hidden="true">/</span><span>{esc(p["name"])}</span></div>
  <div class="pp-hero-in">
    <div>
      <div class="pp-series">{label}</div>
      <h1>{esc(p["h1"])}</h1>
      <p class="pp-lead">{esc(p["lead"])}</p>
      <div class="pp-btns"><a class="pp-btn wa" href="{wa}" target="_blank" rel="noopener">{"Get price &amp; advice" if cl else "Discuss your project"}</a><a class="pp-btn ghost" href="/request-quote">Request a quote</a></div>
    </div>
    <figure class="pp-media"><img src="{img}" width="800" height="420" alt="{esc(p["imgalt"])}" fetchpriority="high" decoding="async"><figcaption>{esc(("Department: " + p["dept"]) if cl else parent[1])}</figcaption></figure>
  </div>
</header>

<main>
<article class="blog-content">
<dl class="pp-facts">{facts_html}</dl>
{body_html}
{EX}
{two}
{steps_html}
{rel_html}
{REFH}
<p style="font-size:.85rem;opacity:.75">Seamens Enterprises, Lahore. Updated November 2026. {"Dilution and use are confirmed with the Seamens team for your site." if cl else "Scope, timeline and specification are confirmed after a site assessment."}</p>
</article>
{faq_html}
<article class="blog-content" style="padding-top:0">{cta}</article>
{guides_html}
</main>

{TAIL}
<script src="/assets/reading.v1.js" defer></script>
</body>
</html>
'''
    os.makedirs(f'{ROOT}/products/{folder}', exist_ok=True)
    open(f'{ROOT}/products/{folder}/{p["slug"]}.html', 'w', encoding='utf-8').write(out)
    if len(p['title']) > 62 or len(p['meta']) > 160:
        print('LEN', p['slug'], len(p['title']), len(p['meta']))

for p in CL: build(p, 'cl')
for p in SV: build(p, 'sv')
print('done', len(CL), len(SV))

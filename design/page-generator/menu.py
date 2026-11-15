import html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from eco_data import ECO
from ws_data import WS
from cl_data import CL
from sv_data import SV
esc = lambda s: html.escape(s, quote=True)
def sv_of(path): return [(p['name'], f'/products/services/{p["slug"]}') for p in SV if p['parent'][0] == path]
GROUPS = [
 ('Textile Auxiliaries', 'ECO-Series textile chemicals', '/products/textile-auxiliaries', [(p['name'], f'/products/eco-series/{p["slug"]}') for p in ECO]),
 ('Water Safe Chemicals', 'Boiler, cooling, chiller and RO treatment', None, [(p['name'], f'/products/water-safe/{p["slug"]}') for p in WS]),
 ('Industrial Cleaning', 'Cleaning and maintenance chemicals', '/products/industrial-cleaning-chemicals', [(p['name'], f'/products/cleaning/{p["slug"]}') for p in CL]),
 ('Boilers & Humidification', 'Supply, erection and support', '/products/boiler-water-treatment-humidification', sv_of('/products/boiler-water-treatment-humidification')),
 ('Cooling, Chillers & RO', 'Towers, chillers and RO plants', '/products/cooling-tower-chiller-ro', sv_of('/products/cooling-tower-chiller-ro')),
 ('Plant Erection & Parts', 'Erection, parts and maintenance', '/products/plant-erection-machinery-parts', sv_of('/products/plant-erection-machinery-parts')),
]
def mega():
    cols = ''
    for i, (t, sub, url, its) in enumerate(GROUPS):
        lis = ''.join(f'<li><a href="{u}">{esc(n)}</a></li>' for n, u in its)
        more = f'<li class="mm-all"><a href="{url}">View all {esc(t)} &rarr;</a></li>' if url else ''
        cols += (f'<details class="mm-col{" mm-wide" if i == 0 else ""}"><summary><span class="mm-ct">{esc(t)}</span><span class="mm-cs">{esc(sub)} &middot; {len(its)}</span></summary>'
                 f'<ul>{lis}{more}</ul></details>')
    return ('<li class="mm-li"><a href="/products" class="mm-top">Products</a>'
            '<button type="button" class="mm-tog" aria-expanded="false" aria-controls="mm-panel" aria-label="Show all products"><span aria-hidden="true"></span></button>'
            f'<div class="mm" id="mm-panel"><div class="mm-in">{cols}</div>'
            '<div class="mm-foot"><a href="/products">All products and services</a><a href="/request-quote">Request a quote</a><a href="https://wa.me/923054444125" target="_blank" rel="noopener">WhatsApp +92-305-4444125</a></div></div></li>')
def directory(hid='all-products', title='Browse every product and service', lead=''):
    cards = ''
    for t, sub, url, its in GROUPS:
        lis = ''.join(f'<li><a href="{u}">{esc(n)}</a></li>' for n, u in its)
        head = f'<a href="{url}">{esc(t)}</a>' if url else esc(t)
        cards += (f'<div class="pdir-card"><h3>{head}</h3><p>{esc(sub)} &middot; {len(its)} pages</p><ul>{lis}</ul>'
                  + (f'<a class="pdir-all" href="{url}">Open category &rarr;</a>' if url else '') + '</div>')
    return (f'<section class="pdir" id="{hid}" aria-labelledby="{hid}-h"><div class="pdir-in"><div class="pdir-label">Quick access</div><h2 id="{hid}-h">{esc(title)}</h2>'
            + (f'<p class="pdir-lead">{esc(lead)}</p>' if lead else '') + f'<div class="pdir-grid">{cards}</div></div></section>')

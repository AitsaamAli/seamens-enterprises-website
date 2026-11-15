import html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from refs import REFS
from x_eco import X as XE
from x_ws import X as XW
from x_cl import X as XC
from x_sv import X as XS
from y_eco import Y as YE
from s_eco import S as SE
from y_ws import Y as YW, S as SW
from y_cl import Y as YC, S as SC
from y_sv import Y as YS, S as SS
import importlib
from h_all import H
from z_all import Z
from q_all import Q
for _k,_v in Q.items(): Z.setdefault(_k,[]).append(_v)
for _k,_v in Z.items(): H.setdefault(_k,[]).extend(_v)
GG={}
for _m in ('g_eco','g_ws','g_cl','g_sv'):
    try: GG[_m[2:]]=importlib.import_module(_m).G
    except ModuleNotFoundError: GG[_m[2:]]={}
for _X,_Y,_S in ((XE,YE,SE),(XW,YW,SW),(XC,YC,SC),(XS,YS,SS)):
    for _k in _X:
        _X[_k].update(_Y[_k]); _X[_k]['scen']=_S[_k]
ALL = {'eco': XE, 'ws': XW, 'cl': XC, 'sv': XS}
esc = lambda s: html.escape(s, quote=True)

def get(kind, slug):
    x = ALL[kind].get(slug)
    if not x:
        raise KeyError(f'missing expansion {kind}/{slug}')
    return x

def sections(kind, slug, name):
    x = get(kind, slug)
    g = GG[kind].get(slug, []) + H.get(slug, [])
    h = f'<h2>How {esc(name)} works</h2><div class="pp-how">' + ''.join(f'<p>{esc(p)}</p>' for p in x['how']) + '</div>'
    h += f'<h2>Benefits of {esc(name)} in detail</h2><div class="pp-bens">' + ''.join(
        f'<div class="pp-ben"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t, d in x['bens']) + '</div>'
    h += ('<h2>Problems it helps solve</h2><div style="overflow-x:auto"><table class="product-table"><thead><tr><th>Problem you see</th><th>Usual cause</th><th>How it helps</th></tr></thead><tbody>' +
          ''.join(f'<tr><td><strong>{esc(a)}</strong></td><td>{esc(b)}</td><td>{esc(c)}</td></tr>' for a, b, c in x['probs']) + '</tbody></table></div>')
    h += ('<h2>How to measure the results</h2><p>Results are confirmed with recognised test methods, so improvements are measured rather than assumed.</p><div style="overflow-x:auto"><table class="product-table"><thead><tr><th>What to check</th><th>How it is measured</th><th>Reference</th></tr></thead><tbody>' +
          ''.join(f'<tr><td><strong>{esc(a)}</strong></td><td>{esc(b)}</td><td>{esc(REFS[r][0].split(":")[0])}</td></tr>' for a, b, r in x['checks']) + '</tbody></table></div>')
    h += f'<h2>Where {esc(name)} delivers the most value</h2><div class="pp-cards">' + ''.join(f'<div class="pp-card"><h3>{esc(t)}</h3><p>{esc(p)}</p></div>' for t, p in x['scen']) + '</div>'
    if g: h += f'<h2>Buyer\'s guide to {esc(name)}</h2><div class="pp-guide">' + ''.join(f'<div class="pp-gi"><h3>{esc(t)}</h3><p>{esc(p)}</p></div>' for t, p in g) + '</div>'
    h += f'<h2>Why it matters for plants in Pakistan</h2><aside class="pp-callout"><b>Local context</b><p>{esc(x["pk"])}</p></aside>'
    h += f'<h2>Practical tips for the best results</h2><ul class="pp-tips">' + ''.join(f'<li>{esc(t)}</li>' for t in x['tips']) + '</ul>'
    return h

def refs_html(kind, slug):
    x = get(kind, slug)
    keys = list(dict.fromkeys(x['refs'] + [c[2] for c in x['checks']]))
    items = ''.join(f'<li><a href="{REFS[k][2]}" target="_blank" rel="noopener nofollow">{esc(REFS[k][0])}</a> &middot; {esc(REFS[k][1])}</li>' for k in keys)
    return (f'<section class="pp-refs"><h2>References and standards</h2><p>The standards and guidance below are the recognised methods used to specify and test results in this application. Seamens Enterprises works to ISO 9001:2015 and ISO 45001.</p><ol>{items}</ol></section>', keys)

def citations(keys):
    return [{"@type": "CreativeWork", "name": REFS[k][0], "publisher": {"@type": "Organization", "name": REFS[k][1]}, "url": REFS[k][2]} for k in keys]

def faqs(kind, slug, base):
    return list(base) + list(get(kind, slug)['faq2']) + list(get(kind, slug)['faq3'])

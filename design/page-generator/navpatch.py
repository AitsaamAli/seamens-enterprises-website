# Idempotent: inserts the Products mega menu and its assets into every page. Run after gen.py / gen2.py.
import re, glob, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import menu
ROOT = '/home/user/seamens-enterprises-website'
MEGA = menu.mega()
CSS = '<link rel="stylesheet" href="/assets/megamenu.v1.css">'
JS = '<script src="/assets/megamenu.v1.js" defer></script>'
pat_old = re.compile(r'<li><a href="/products">Products</a></li>')
pat_new = re.compile(r'<li class="mm-li">.*?</div></div></li>', re.S)
n = 0
for f in glob.glob(ROOT + '/*.html') + glob.glob(ROOT + '/blog/*.html') + glob.glob(ROOT + '/products/**/*.html', recursive=True):
    s = open(f, encoding='utf-8').read(); o = s
    if 'id="navLinks"' not in s: continue
    if pat_new.search(s): s = pat_new.sub(lambda m: MEGA, s, count=1)
    else: s = pat_old.sub(lambda m: MEGA, s, count=1)
    if CSS not in s: s = s.replace('</head>', CSS + '\n</head>', 1)
    if JS not in s: s = s.replace('</body>', JS + '\n</body>', 1)
    if 'class="mm-li"' not in s: print('NO NAV MATCH', f)
    if s != o: open(f, 'w', encoding='utf-8').write(s); n += 1
print('patched', n)

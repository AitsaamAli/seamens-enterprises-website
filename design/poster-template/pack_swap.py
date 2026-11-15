"""Swap the centre package of an approved product poster for a 25 KG bag or a 1000 KG IBC tank.
Left and right panels come unchanged from the product's own drum poster; only the centre package changes.
Usage: python3 design/poster-template/pack_swap.py <slug> bag|ibc
base-bag.png / base-ibc.png are Canva renders (1600x1066) of the same layout with the package in the centre."""
import sys, os, json, re
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
IMG = ROOT + '/images/'; F = '/usr/share/fonts/opentype/inter/Inter-%s.otf'; S = 2
slug, kind = sys.argv[1], sys.argv[2]
cfg = json.load(open(f'{HERE}/products/{slug}.json'))
NAVY = (24, 44, 92)
def font(w, px): return ImageFont.truetype(F % w, int(px * S))
def B(*v): return [int(round(x * S)) for x in v]

# 1. Left/right from the product's own drum poster (3200 wide), centre from the package render (upscaled)
src = f"{IMG}products/posters/{re.sub(r'[^A-Za-z0-9-]+', '', cfg['name'].replace(' ', '-').replace('+', '-'))}-{cfg['packs'][0]}KG-v{cfg['version']}.jpg"
side = Image.open(src).convert('RGB')
pk = Image.open(f'{HERE}/base-{kind}.png').convert('RGB').resize(side.size, Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 55, 2))
if cfg.get('bg') == 'wave':      # Water Safe: put the package on the same ocean scene as the drum posters
    import poster
    scene, _ = poster.wave_scene(side.width, side.height)
    tm = np.zeros((side.height, side.width), np.float32)
    if kind == 'ibc': cv2.rectangle(tm, tuple(B(499, 60)), tuple(B(1088, 997)), 1, -1)
    else: cv2.ellipse(tm, tuple(B(805, 560)), tuple(B(250, 420)), 0, 0, 360, 1, -1)
    tm = cv2.GaussianBlur(tm, (0, 0), 1.2 * S)[..., None]
    pk = Image.fromarray((np.array(pk).astype(np.float32) * tm + scene * (1 - tm)).clip(0, 255).astype(np.uint8))
m = np.zeros((side.height, side.width), np.float32); m[:, B(522)[0]:B(1100)[0]] = 1
m = cv2.GaussianBlur(m, (0, 0), 8 * S)[..., None]
im = Image.fromarray((np.array(side) * (1 - m) + np.array(pk) * m).astype(np.uint8))

def patch(rect, ref_rows):
    """Repaint rect with the per-column colour of nearby clean rows (label paper)."""
    global im
    a = np.array(im).astype(np.float32); x0, y0, x1, y1 = B(*rect); r0, r1 = B(*ref_rows)
    col = cv2.GaussianBlur(np.median(a[r0:r1, x0:x1], axis=0)[None], (0, 0), 3 * S)[0]
    a[y0:y1, x0:x1] = col[None]; im = Image.fromarray(a.clip(0, 255).astype(np.uint8))
def erase(rect, grow=4):
    """Inpaint dark or coloured marks (old text/logo) inside rect on light label paper."""
    global im
    a = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR); x0, y0, x1, y1 = B(*rect)
    sub = a[y0:y1, x0:x1]; hsv = cv2.cvtColor(sub, cv2.COLOR_BGR2HSV)
    mk = ((sub.mean(axis=2) < 205) | (hsv[..., 1] > 55)).astype(np.uint8) * 255
    m = np.zeros(a.shape[:2], np.uint8); m[y0:y1, x0:x1] = cv2.dilate(mk, np.ones((grow * S, grow * S), np.uint8))
    a = cv2.inpaint(a, m, 6 * S, cv2.INPAINT_TELEA); im = Image.fromarray(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))
def text(xy, s, f, col, anchor='mm'):
    ImageDraw.Draw(im).text((xy[0] * S, xy[1] * S), s, font=f, fill=col, anchor=anchor)
def fit(w, size, s, maxw):
    while size > 8 and font(w, size).getlength(s) / S > maxw: size -= 0.5
    return font(w, size)
def logo(cx, cy, width):
    lg = Image.open(IMG + 'seamens-logo-transparent.png').convert('RGBA')
    lg = lg.resize(B(width, width * lg.height / lg.width), Image.LANCZOS)
    im.paste(lg, (B(cx)[0] - lg.width // 2, B(cy)[0] - lg.height // 2), lg)

if kind == 'bag':
    erase((640, 238, 975, 312)); logo(805, 274, 300)                 # real logo
    patch((610, 764, 1000, 789), (791, 795))                                    # contact line (+92)
    text((805, 776.5), '+92-305-4444125  ·  www.seamensenterprises.com', font('SemiBold', 15), (235, 238, 245))
    lab = dict(name=(805, 390, 430, 46), sub=(805, 450), form=(805, 485), nw=(670, 605, 140), nwrect=(593, 582, 747, 630))
else:
    erase((700, 288, 905, 352)); logo(805, 320, 210)
    lab = dict(name=(805, 394, 400, 40), sub=(805, 443), form=(805, 473), nw=(674, 563, 145), nwrect=(593, 543, 754, 585))

# Industrial Grade mini badge (the render's own one has garbled text)
igb = Image.open(f'{HERE}/base.jpg').convert('RGB').crop((1340 - 43, 413 - 43, 1340 + 43, 413 + 43))
def ig(cx, cy, r):
    c = igb.resize(B(2 * r, 2 * r), Image.LANCZOS); mk = Image.new('L', c.size, 0)
    ImageDraw.Draw(mk).ellipse([0, 0, c.width - 1, c.height - 1], fill=255)
    im.paste(c, (B(cx)[0] - c.width // 2, B(cy)[0] - c.height // 2), mk.filter(ImageFilter.GaussianBlur(S)))
if kind == 'bag': ig(967.5, 600, 25.5)
else: ig(970, 557.5, 24)

# 2. Product wording on the package label (the render shows CXW-111; redraw for this product)
if cfg['slug'] != 'ecosize-cxw-111' or True:
    a = np.array(im); cx, ny, mw, fs = lab['name']
    x0, x1 = cx - mw / 2 - 20, cx + mw / 2 + 20
    y0, y1 = ny - fs * 0.75, lab['form'][1] + 14
    band = a[B(y0)[0]:B(y1)[0], B(x0)[0]:B(x1)[0]]
    navy = tuple(int(v) for v in np.median(band.reshape(-1, 3)[band.reshape(-1, 3).sum(1) < 200], axis=0))
    ImageDraw.Draw(im).rectangle(B(x0, y0, x1, y1), fill=navy)
    text((cx, ny), cfg['name'], fit('ExtraBold', fs, cfg['name'], mw), (255, 255, 255))
    text(lab['sub'], cfg['subtitle'], fit('Medium', 17, cfg['subtitle'], mw), (232, 238, 248))
    text(lab['form'], cfg['form'], fit('SemiBold', 14, cfg['form'], mw), (150, 210, 90))
    net = '25 KG' if kind == 'bag' else '1000 KG'
    r = lab['nwrect']; erase(r)
    text((lab['nw'][0], lab['nw'][1]), net, fit('ExtraBold', 40, net, lab['nw'][2]), NAVY)

kg = '25' if kind == 'bag' else '1000'; v = cfg['version']
base = f"{IMG}products/{cfg['slug']}-{kg}kg-v{v}"
for suf, w, q in [('-sm', 720, 78), ('', 1080, 80), ('-full', 1600, 80)]:
    rr = im.resize((w, round(w * im.height / im.width)), Image.LANCZOS)
    rr.save(base + suf + '.webp', quality=q, method=6)
    if suf != '-full': rr.save(base + suf + '.jpg', quality=82, optimize=True, progressive=True)
out = src.replace(f"-{cfg['packs'][0]}KG-", f"-{kg}KG-"); im.save(out, quality=90, optimize=True, progressive=True)
print('saved', out)

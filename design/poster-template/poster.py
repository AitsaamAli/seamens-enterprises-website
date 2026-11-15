"""Seamens product poster template (owner-approved design, Nov 2026).

Usage:  python3 design/poster-template/poster.py ecoshort-gs-777
Reads products/<slug>.json, draws one poster per pack size on top of base.jpg and writes:
  images/products/<slug>-<kg>kg-v<version>.webp / -sm.webp / -full.webp / .jpg / -sm.jpg   (website)
  images/products/posters/<Name>-<kg>KG-v<version>.jpg                                    (3200px original)
base.jpg is the approved EcoShort-GS-777 poster. For another product set "redraw": true in its JSON:
the GS-777 wording (headline, benefits, label name/subtitle/form) is wiped and redrawn from the JSON.
"""
import sys, os, io, json, math
import numpy as np, cv2, segno
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
IMG = os.path.join(ROOT, 'images') + '/'
F = '/usr/share/fonts/opentype/inter/Inter-%s.otf'
S = 2                                   # work at 2x of the 1600x1066 base
NAVY, MID, WHITE = (24, 44, 92), (52, 82, 140), (255, 255, 255)
CX, RAD, ARC = 805, 270, 20             # drum axis x, drum radius, vertical arc of label text (base px)

cfg = json.load(open(os.path.join(HERE, 'products', sys.argv[1] + '.json')))
URL = f"https://www.seamensenterprises.com/products/{cfg['folder']}/{cfg['slug']}"

def font(w, px): return ImageFont.truetype(F % w, int(px * S))
def B(*v): return [int(round(x * S)) for x in v]

def load_base():
    src = Image.open(os.path.join(HERE, 'base.jpg')).convert('RGB')
    im = src.resize((src.width * S, src.height * S), Image.LANCZOS)
    return im.filter(ImageFilter.UnsharpMask(radius=2, percent=55, threshold=2))

def wipe(im, rect, thr=150, grow=3):
    """Inpaint bright text inside rect (text on a dark background)."""
    a = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR); x0, y0, x1, y1 = B(*rect)
    sub = a[y0:y1, x0:x1]; m = np.zeros(a.shape[:2], np.uint8)
    hsv = cv2.cvtColor(sub, cv2.COLOR_BGR2HSV)
    mm = ((sub.max(axis=2) > thr) | ((hsv[..., 1] > 90) & (hsv[..., 2] > 110))).astype(np.uint8) * 255
    m[y0:y1, x0:x1] = cv2.dilate(mm, np.ones((grow * S, grow * S), np.uint8))
    a = cv2.inpaint(a, m, 5 * S, cv2.INPAINT_TELEA)
    return Image.fromarray(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))

def wipe_dark(im, rect, thr=175, grow=3):
    """Inpaint dark text inside rect (text on light paper)."""
    a = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR); x0, y0, x1, y1 = B(*rect)
    m = np.zeros(a.shape[:2], np.uint8)
    m[y0:y1, x0:x1] = cv2.dilate((a[y0:y1, x0:x1].mean(axis=2) < thr).astype(np.uint8) * 255, np.ones((grow * S, grow * S), np.uint8))
    a = cv2.inpaint(a, m, 4 * S, cv2.INPAINT_TELEA)
    return Image.fromarray(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))

def col_fill(im, rect, ref, mode='bright', keep=0.4):
    """Repaint rect with a per-column colour taken from the ref rows (keeps the drum's left-right shading)."""
    a = np.array(im).astype(np.float32); x0, y0, x1, y1 = B(*rect); r0, r1 = B(ref[0], ref[1])
    reg = a[r0:r1, x0:x1]; lum = reg.mean(axis=2); n = reg.shape[0]
    k = np.argsort(lum, axis=0); k = k[int(n * (1 - keep)):] if mode == 'bright' else k[:int(n * 0.5)]
    col = np.take_along_axis(reg, k[..., None].repeat(3, axis=2), axis=0).mean(axis=0)
    col = cv2.GaussianBlur(col[None], (0, 0), 3 * S)[0]
    a[y0:y1, x0:x1] = col[None]
    return Image.fromarray(a.clip(0, 255).astype(np.uint8)), col

def text(im, xy, s, f, color, anchor='la', spacing=0.0, angle=0.0):
    if not spacing and not angle:
        ImageDraw.Draw(im).text((xy[0] * S, xy[1] * S), s, font=f, fill=color, anchor=anchor); return
    w = int(sum(f.getlength(c) + spacing * S for c in s) + 20 * S); h = int(f.size * 1.8)
    L = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(L); x = 10 * S
    for c in s: d.text((x, h / 2), c, font=f, fill=color, anchor='lm'); x += f.getlength(c) + spacing * S
    L = L.crop((0, 0, int(x + 10 * S), h))
    if angle: L = L.rotate(angle, resample=Image.BICUBIC, expand=True)
    ox = {'l': 10 * S, 'm': L.width / 2, 'r': L.width - 10 * S}[anchor[0]]
    im.paste(L, (int(xy[0] * S - ox), int(xy[1] * S - L.height / 2)), L)

def warp_paste(im, flat, by0, bx=(548, 1062)):
    """flat: RGBA layer drawn in arc-length coords (width 560 base px, centred on the drum axis), top at base y=by0."""
    FW = flat.width / S; H = flat.height
    xs = np.arange(B(bx[0])[0], B(bx[1])[0]) / S; ys = np.arange(H) / S + by0
    XX, YY = np.meshgrid(xs, ys); th = np.arcsin(np.clip((XX - CX) / RAD, -.999, .999))
    mx = ((RAD * th + FW / 2) * S).astype(np.float32); my = ((YY + ARC * (1 - np.cos(th)) - by0) * S).astype(np.float32)
    w = cv2.remap(np.array(flat), mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0)).astype(np.float32)
    w[..., :3] *= (0.9 + 0.1 * np.cos(th))[..., None]       # slight shading towards the drum edges
    a = np.array(im).astype(np.float32); y0 = B(by0)[0]; x0 = B(bx[0])[0]
    reg = a[y0:y0 + H, x0:x0 + w.shape[1]]; al = w[..., 3:4] / 255
    reg[:] = reg * (1 - al) + w[..., :3] * al
    return Image.fromarray(a.clip(0, 255).astype(np.uint8))

def flat_layer(h):
    L = Image.new('RGBA', (560 * S, int(h * S)), (0, 0, 0, 0)); return L, ImageDraw.Draw(L)

def ftext(d, u, y, s, f, col, spacing=0.0):
    w = sum(f.getlength(c) / S + spacing for c in s) - spacing; x = u - w / 2
    for c in s: d.text(((x + 280) * S, y * S), c, font=f, fill=col, anchor='lm'); x += f.getlength(c) / S + spacing

def fit(weight, size, s, maxw, spacing=0.0):
    while size > 8 and sum(font(weight, size).getlength(c) / S + spacing for c in s) > maxw: size -= 0.5
    return font(weight, size)

def logo():
    return Image.open(IMG + 'seamens-logo-transparent.png').convert('RGBA')

def badge_cut(im, cx, cy, r):
    """Cut a round badge (with its gold ring) out of the poster as RGBA."""
    x0, y0, x1, y1 = B(cx - r, cy - r, cx + r, cy + r)
    c = im.crop((x0, y0, x1, y1)).convert('RGBA')
    m = Image.new('L', c.size, 0); ImageDraw.Draw(m).ellipse([0, 0, c.width - 1, c.height - 1], fill=255)
    c.putalpha(m.filter(ImageFilter.GaussianBlur(0.6 * S))); return c

def build(net):
    im = load_base()

    # 1. Bigger Seamens logo card (top left)
    lg = logo(); lw = 342; lh = lw * lg.height / lg.width
    card = Image.new('RGBA', B(lw + 40, lh + 28), (0, 0, 0, 0))
    ImageDraw.Draw(card).rounded_rectangle([0, 0, card.width - 1, card.height - 1], radius=18 * S, fill=(255, 255, 255, 255))
    card.alpha_composite(lg.resize(B(lw, lh), Image.LANCZOS), tuple(B(20, 14)))
    sh = Image.new('RGBA', (card.width + 80 * S, card.height + 80 * S), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([40 * S, 48 * S, 40 * S + card.width, 48 * S + card.height], radius=18 * S, fill=(0, 0, 0, 130))
    sh = sh.filter(ImageFilter.GaussianBlur(16 * S))
    im.paste(sh, tuple(B(40 - 40, 40 - 40)), sh); im.paste(card, tuple(B(40, 40)), card)

    # 2. Taller label strip with a bigger Seamens logo on the drum
    im, paper = col_fill(im, (556, 273, 1051, 333), (274, 310), 'bright', keep=0.2)
    a = np.array(im); a[B(333)[0]:B(337)[0], B(556)[0]:B(1051)[0]] = np.array([60, 160, 70])[None, None]
    im = Image.fromarray(a)
    im, _ = col_fill(im, (556, 337, 1051, 346), (340, 346), 'dark')
    L, d = flat_layer(70); lgw = 218; lgh = lgw * lg.height / lg.width
    L.alpha_composite(lg.resize(B(lgw, lgh), Image.LANCZOS), (int((280 - lgw / 2) * S), int((302.5 - 273 - lgh / 2) * S)))
    im = warp_paste(im, L, 273)

    if cfg.get('redraw'):
        im = redraw_product(im)

    # 3. NET WEIGHT: repaint the number inside the box
    if net != '240' or cfg.get('redraw'):
        im = wipe_dark(im, (597, 519, 760, 578), thr=205, grow=5)
        im = wipe_dark(im, (597, 519, 760, 578), thr=215, grow=3)
        L, d = flat_layer(70)
        ftext(d, -131, 548 - 520, f'{net} KG', fit('ExtraBold', 44, f'{net} KG', 150), NAVY, 0.3)
        im = warp_paste(im, L, 520)

    # 4. Label: IPO mini badge -> Industrial Grade (taken from the panel art)
    ig = badge_cut(im, 1340, 413, 43)
    ig = ig.resize(B(41, 52), Image.LANCZOS)
    im.paste(ig, (B(970)[0] - ig.width // 2, B(540)[0] - ig.height // 2), ig)
    im = wipe_dark(im, (936, 566, 1012, 586))
    text(im, (971, 573), 'INDUSTRIAL', font('Bold', 8.2), NAVY, 'mm', 0.2, angle=3.5)
    text(im, (971.5, 582), 'GRADE', font('Bold', 8.2), NAVY, 'mm', 0.2, angle=3.5)

    # 5. Bigger CONAIR-PAK tick badge in the side panel
    cb = badge_cut(im, 1506, 271, 44); cb = cb.resize((int(cb.width * 1.16), int(cb.height * 1.16)), Image.LANCZOS)
    im.paste(cb, (B(1506)[0] - cb.width // 2, B(267)[0] - cb.height // 2), cb)

    # 6. QR card always points at this product's page
    q = segno.make(URL, error='m'); buf = io.BytesIO()
    q.save(buf, kind='png', scale=20, border=2, dark='#0e2250', light='#ffffff')
    qi = Image.open(io.BytesIO(buf.getvalue())).convert('RGB').resize(B(100, 100), Image.NEAREST)
    im.paste(qi, tuple(B(1137, 950)))
    return im

def redraw_product(im):
    """Wipe GS-777 wording and draw this product's wording (other products)."""
    for r in [(36, 194, 200, 216), (34, 222, 465, 378), (96, 452, 420, 896)]:
        im = wipe(im, r)
    text(im, (40, 205), cfg['series'], font('Bold', 17), (110, 190, 60), 'lm', 3.2)
    hl = cfg['headline']; y = 248
    for line in hl:
        text(im, (37, y), line, fit('ExtraBold', 46, line, 420), WHITE, 'lm'); y += 47
    text(im, (37, y + 2), cfg['headline_accent'], fit('ExtraBold', 46, cfg['headline_accent'], 420), (122, 200, 30), 'lm')
    ys = [466, 522, 580, 635, 693, 750, 809, 865]
    for (t, s), y in zip(cfg['benefits'], ys):
        text(im, (100, y), t, font('SemiBold', 21), WHITE, 'lm')
        text(im, (100, y + 21), s, font('Regular', 15), (200, 210, 226), 'lm')
    im, _ = col_fill(im, (566, 346, 1046, 470), (349, 352), 'dark')
    L, d = flat_layer(130)
    ftext(d, 0, 376 - 346, cfg['name'], fit('ExtraBold', 54, cfg['name'], 430), WHITE, -0.4)
    ftext(d, 0, 428 - 346, cfg['subtitle'], fit('Medium', 17, cfg['subtitle'], 400), (232, 238, 248))
    ftext(d, 0, 457 - 346, cfg['form'], font('SemiBold', 14.5), (150, 210, 90), 2.2)
    return warp_paste(im, L, 346)

def save(im, net):
    v = cfg['version']; base = f"{IMG}products/{cfg['slug']}-{net}kg-v{v}"
    for suf, w, q in [('-sm', 720, 78), ('', 1080, 80), ('-full', 1600, 80)]:
        r = im.resize((w, round(w * im.height / im.width)), Image.LANCZOS).convert('RGB')
        r.save(base + suf + '.webp', quality=q, method=6)
        if suf != '-full': r.save(base + suf + '.jpg', quality=82, optimize=True, progressive=True)
    os.makedirs(IMG + 'products/posters', exist_ok=True)
    im.convert('RGB').save(f"{IMG}products/posters/{cfg["name"]}-{net}KG-v{v}.jpg", quality=90, optimize=True, progressive=True)
    print('saved', base)

if __name__ == '__main__':
    for net in cfg['packs']:
        save(build(net), net)

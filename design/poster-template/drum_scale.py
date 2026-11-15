"""Make the drum smaller for smaller packs (60 L / 150 L) in an existing poster; everything else stays identical.
Usage: python3 design/poster-template/drum_scale.py <slug> <kg> <scale>   e.g. ecoacryllic-acl-55 60 0.66
Reads images/products/posters/<Name>-<kg>KG-v<N>.jpg (made by poster.py, NET WEIGHT already correct),
writes the same files with suffix -s (scaled drum)."""
import sys, os, json, re
import numpy as np, cv2
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..')); IMG = ROOT + '/images/'
slug, kg, k = sys.argv[1], sys.argv[2], float(sys.argv[3])
cfg = json.load(open(f'{HERE}/products/{slug}.json'))
nm = re.sub(r'[^A-Za-z0-9-]+', '', cfg['name'].replace(' ', '-').replace('+', '-'))
src = f"{IMG}products/posters/{nm}-{kg}KG-v{cfg['version']}.jpg"
im = np.array(Image.open(src).convert('RGB')).astype(np.float32); H, W = im.shape[:2]; s = W / 1600
X0, X1, Y0, Y1 = int(528 * s), int(1092 * s), int(40 * s), int(1010 * s)   # drum zone (base px * s)
FLOOR = int(908 * s)                                                       # drum bottom contact line
# drum mask: bright/saturated pixels in the zone, largest blob, holes filled, cut at the floor
reg = im[Y0:Y1, X0:X1].astype(np.uint8); hsv = cv2.cvtColor(reg, cv2.COLOR_RGB2HSV)
m = ((hsv[..., 2] > 70) & ((hsv[..., 1] > 90) | (hsv[..., 2] > 150))).astype(np.uint8)
m[FLOOR - Y0:] = 0
m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((int(25 * s),) * 2, np.uint8))
n, lab, st, _ = cv2.connectedComponentsWithStats(m); big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA]); m = (lab == big).astype(np.uint8)
cnt, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE); m = np.zeros_like(m); cv2.drawContours(m, cnt, -1, 1, -1)
m = cv2.dilate(m, np.ones((int(5 * s),) * 2, np.uint8))
x, y, w, h = cv2.boundingRect(m)
drum = reg[y:y + h, x:x + w]; dm = m[y:y + h, x:x + w].astype(np.float32)
# background: per-row blend between the clean columns either side of the zone, plus the original glow kept outside the drum
bg = im.copy(); L = im[Y0:Y1, X0 - int(6 * s):X0].mean(axis=1); R = im[Y0:Y1, X1:X1 + int(6 * s)].mean(axis=1)
t = np.linspace(0, 1, X1 - X0)[None, :, None]; fill = L[:, None] * (1 - t) + R[:, None] * t
# keep the centre glow: brighten the middle a little, as in the original backdrop
glow = np.exp(-((np.linspace(-1, 1, X1 - X0)) ** 2) / 0.35)[None, :, None] * np.array([6, 14, 34])[None, None]
fill = fill + glow * np.linspace(0.6, 1, Y1 - Y0)[:, None, None]
full = np.zeros((Y1 - Y0, X1 - X0), np.float32); full[y:y + h, x:x + w] = dm
full = cv2.GaussianBlur(cv2.dilate(full, np.ones((int(9 * s),) * 2, np.uint8)), (0, 0), 3 * s)[..., None]
bg[Y0:Y1, X0:X1] = im[Y0:Y1, X0:X1] * (1 - full) + fill * full
# scaled drum, centred on the same axis, standing on the same floor line
nw, nh = int(w * k), int(h * k)
d2 = cv2.resize(drum, (nw, nh), interpolation=cv2.INTER_AREA).astype(np.float32)
m2 = cv2.GaussianBlur(cv2.resize(dm, (nw, nh), interpolation=cv2.INTER_AREA), (0, 0), 0.8 * s)[..., None]
cx = X0 + x + w // 2; px, py = cx - nw // 2, (Y0 + y + h) - nh
# contact shadow
sh = np.zeros(bg.shape[:2], np.float32); cv2.ellipse(sh, (cx, py + nh - int(2 * s)), (int(nw * 0.52), int(16 * s * k)), 0, 0, 360, 1, -1)
sh = cv2.GaussianBlur(sh, (0, 0), 10 * s)[..., None]; bg = bg * (1 - 0.55 * sh)
# soft floor reflection
rh = min(int(nh * 0.22), bg.shape[0] - (py + nh))
ref = d2[::-1][:rh] * np.linspace(0.22, 0, rh)[:, None, None]
rm = m2[::-1][:rh]; ry = py + nh
bg[ry:ry + ref.shape[0], px:px + nw] = bg[ry:ry + ref.shape[0], px:px + nw] * (1 - rm * 0.22) + ref * rm / max(1e-3, 1)
bg[py:py + nh, px:px + nw] = bg[py:py + nh, px:px + nw] * (1 - m2) + d2 * m2
out = Image.fromarray(bg.clip(0, 255).astype(np.uint8))
o = src.replace('.jpg', '-s.jpg'); out.save(o, quality=90, optimize=True, progressive=True); print('saved', o)

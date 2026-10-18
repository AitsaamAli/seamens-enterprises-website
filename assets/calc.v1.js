(function () {
'use strict';
var WA = '923054444125';
function el(t, a, h) { var e = document.createElement(t); for (var k in a || {}) e.setAttribute(k, a[k]); if (h != null) e.innerHTML = h; return e; }
function fmt(n, d) { if (!isFinite(n)) return '-'; return n.toLocaleString('en-US', { maximumFractionDigits: d == null ? 1 : d }); }
function field(id, label, val, step, min) {
  return '<div><label for="' + id + '">' + label + '</label><input id="' + id + '" type="number" inputmode="decimal" value="' + val + '" step="' + (step || 'any') + '" min="' + (min == null ? 0 : min) + '"></div>';
}
function res(label, val) { return '<div class="calc-res"><b>' + val + '</b><span>' + label + '</span></div>'; }
function num(id) { var v = parseFloat(document.getElementById(id).value); return isFinite(v) ? v : NaN; }
function wa(text) { return 'https://wa.me/' + WA + '?text=' + encodeURIComponent(text); }

var CALCS = {
  blowdown: {
    title: 'Boiler Blowdown Calculator',
    sub: 'Mass-balance method. Use feed water TDS measured after softener/RO, not raw borewell TDS.',
    html: function (p) { return '<div class="calc-grid">' + field(p + 's', 'Steam output (kg/h)', 5000) + field(p + 'f', 'Feed water TDS (ppm)', 300) + field(p + 'b', 'Max boiler water TDS (ppm)', 3000) + '</div>'; },
    run: function (p) {
      var S = num(p + 's'), F = num(p + 'f'), B = num(p + 'b');
      if (!(S > 0 && F >= 0 && B > 0)) return { err: 'Enter positive values.' };
      if (B <= F) return { err: 'Max boiler TDS must be higher than feed water TDS. Improve feed water quality (softening/RO) or confirm the boiler limit.' };
      var bd = S * F / (B - F), feed = S + bd;
      return {
        out: res('Cycles of concentration', fmt(B / F, 1)) + res('Blowdown, % of steam', fmt(F / (B - F) * 100, 1) + '%') + res('Blowdown, % of feed water', fmt(F / B * 100, 1) + '%') + res('Blowdown flow', fmt(bd, 0) + ' kg/h') + res('Feed water needed', fmt(feed, 0) + ' kg/h'),
        note: 'Formulas: blowdown (kg/h) = steam x F / (B - F); % of feed water = F / B. Assumes no TDS in returned condensate and no carryover. Confirm the boiler TDS limit with the manufacturer.',
        msg: 'Boiler blowdown calculation: steam ' + S + ' kg/h, feed TDS ' + F + ' ppm, max boiler TDS ' + B + ' ppm, blowdown ' + fmt(bd, 0) + ' kg/h. Please advise on a treatment programme.'
      };
    }
  },
  cooling: {
    title: 'Cooling Tower Makeup Water Calculator',
    sub: 'Evaporation + drift + blowdown water balance for a recirculating cooling tower.',
    html: function (p) { return '<div class="calc-grid">' + field(p + 'q', 'Circulation rate (m3/h)', 500) + field(p + 't', 'Cooling range, hot - cold (C)', 5.5) + field(p + 'c', 'Cycles of concentration', 4, 0.1, 1.1) + field(p + 'd', 'Drift loss (% of circulation)', 0.02, 0.01) + '</div>'; },
    run: function (p) {
      var Q = num(p + 'q'), T = num(p + 't'), C = num(p + 'c'), D = num(p + 'd');
      if (!(Q > 0 && T > 0 && C > 1 && D >= 0)) return { err: 'Enter positive values; cycles must be above 1.' };
      var E = 0.00153 * T * Q, Dr = Q * D / 100, B = Math.max(E / (C - 1) - Dr, 0), M = E + Dr + B;
      return {
        out: res('Evaporation', fmt(E, 2) + ' m3/h') + res('Drift', fmt(Dr, 2) + ' m3/h') + res('Blowdown', fmt(B, 2) + ' m3/h') + res('Makeup water', fmt(M, 2) + ' m3/h') + res('Makeup per day (24 h)', fmt(M * 24, 0) + ' m3') + res('Makeup, % of circulation', fmt(M / Q * 100, 2) + '%'),
        note: 'Formulas: evaporation is approx. 0.00153 x range(C) x circulation (common engineering approximation; actual value varies with load and weather). Blowdown = E / (cycles - 1) - drift. Makeup = E + drift + blowdown. Use metered data for budgeting.',
        msg: 'Cooling tower water balance: circulation ' + Q + ' m3/h, range ' + T + ' C, cycles ' + C + ', makeup ' + fmt(M, 2) + ' m3/h. Please advise on treatment.'
      };
    }
  },
  ro: {
    title: 'RO Antiscalant Dosing Calculator',
    sub: 'Convert a target ppm dose and feed flow into hourly, daily and monthly antiscalant consumption.',
    html: function (p) { return '<div class="calc-grid">' + field(p + 'f', 'Feed flow (m3/h)', 10) + field(p + 'p', 'Target dose (ppm = mg/L)', 4, 0.1) + field(p + 'd', 'Product density (kg/L)', 1.1, 0.01) + '</div>'; },
    run: function (p) {
      var F = num(p + 'f'), P = num(p + 'p'), Dn = num(p + 'd');
      if (!(F > 0 && P > 0 && Dn > 0)) return { err: 'Enter positive values.' };
      var gh = F * P, kgd = gh * 24 / 1000;
      return {
        out: res('Antiscalant per hour', fmt(gh, 1) + ' g/h') + res('Per day', fmt(kgd, 2) + ' kg') + res('Per day (volume)', fmt(kgd / Dn, 2) + ' L') + res('Per 30 days', fmt(kgd * 30, 1) + ' kg') + res('Dosing pump rate', fmt(gh / Dn, 1) + ' mL/h'),
        note: '1 mg/L x 1 m3/h = 1 g/h. Typical antiscalant doses are about 2-5 ppm, but the right dose depends on feed analysis, recovery and the product; confirm with the manufacturer\'s projection and scaling indices. Check density on the product datasheet.',
        msg: 'RO antiscalant dosing: feed ' + F + ' m3/h, dose ' + P + ' ppm, ' + fmt(kgd, 2) + ' kg/day. Please advise on product and dose.'
      };
    }
  },
  textilecost: {
    title: 'Textile Chemical Cost-in-Use Calculator',
    sub: 'Compare two chemical quotes as cost per kg of fabric, using price, dose (g/L) and liquor ratio.',
    html: function (p) { return '<div class="calc-grid">' + field(p + 'w', 'Batch fabric weight (kg)', 500) + field(p + 'r', 'Liquor ratio (1 : x)', 10, 0.5, 1) + field(p + 'a', 'Quote A: price (Rs/kg)', 500) + field(p + 'x', 'Quote A: dose (g/L)', 2, 0.01) + field(p + 'b', 'Quote B: price (Rs/kg)', 650) + field(p + 'y', 'Quote B: dose (g/L)', 1.2, 0.01) + '</div>'; },
    run: function (p) {
      var W = num(p + 'w'), R = num(p + 'r'), A = num(p + 'a'), X = num(p + 'x'), B = num(p + 'b'), Y = num(p + 'y');
      if (!(W > 0 && R > 0 && A > 0 && X > 0 && B > 0 && Y > 0)) return { err: 'Enter positive values in every field.' };
      var ga = X * R, gb = Y * R, ca = A / 1000 * ga, cb = B / 1000 * gb, ba = ca * W, bb = cb * W;
      var cheaper = ca <= cb ? 'Quote A' : 'Quote B', diff = Math.abs(ba - bb), pct = Math.abs(ca - cb) / Math.max(ca, cb) * 100;
      return {
        out: res('Quote A: chemical per kg fabric', fmt(ga, 1) + ' g') + res('Quote A: cost per kg fabric', 'Rs ' + fmt(ca, 2)) + res('Quote A: cost per batch', 'Rs ' + fmt(ba, 0)) + res('Quote B: chemical per kg fabric', fmt(gb, 1) + ' g') + res('Quote B: cost per kg fabric', 'Rs ' + fmt(cb, 2)) + res('Quote B: cost per batch', 'Rs ' + fmt(bb, 0)) + res('Lower cost-in-use', cheaper) + res('Difference per batch', 'Rs ' + fmt(diff, 0) + ' (' + fmt(pct, 0) + '%)'),
        note: 'Formulas: grams per kg fabric = dose (g/L) x liquor ratio; cost per kg fabric = price per kg / 1000 x grams per kg fabric. Doses must come from your own trial. Prices here are your inputs, not Seamens prices.',
        msg: 'Textile chemical cost-in-use: ' + W + ' kg batch at 1:' + R + '. Quote A Rs ' + fmt(ca, 2) + '/kg fabric, Quote B Rs ' + fmt(cb, 2) + '/kg fabric. Please advise on products and a trial.'
      };
    }
  },
  steamcost: {
    title: 'Boiler Chemical Cost per Tonne of Steam Calculator',
    sub: 'Convert daily chemical use, price and steam output into Rs per tonne of steam, with testing and service cost included.',
    html: function (p) { return '<div class="calc-grid">' + field(p + 'k', 'Chemical used per day (kg)', 12, 0.1) + field(p + 'p', 'Price (Rs/kg)', 400) + field(p + 's', 'Steam output (tonne/h)', 5, 0.1) + field(p + 'h', 'Operating hours per day', 20, 1) + field(p + 'm', 'Service and testing cost per month (Rs)', 30000, 100, 0) + '</div>'; },
    run: function (p) {
      var K = num(p + 'k'), P = num(p + 'p'), S = num(p + 's'), H = num(p + 'h'), M = num(p + 'm');
      if (!(K >= 0 && P > 0 && S > 0 && H > 0 && M >= 0)) return { err: 'Enter positive values (service cost may be zero).' };
      var steam = S * H, daily = K * P, perT = daily / steam, svcT = M / (steam * 30), total = perT + svcT;
      return {
        out: res('Steam per day', fmt(steam, 1) + ' tonne') + res('Chemical cost per day', 'Rs ' + fmt(daily, 0)) + res('Chemical cost per tonne of steam', 'Rs ' + fmt(perT, 2)) + res('Service and testing per tonne', 'Rs ' + fmt(svcT, 2)) + res('Total per tonne of steam', 'Rs ' + fmt(total, 2)) + res('Chemical cost per 30 days', 'Rs ' + fmt(daily * 30, 0)),
        note: 'Formulas: steam per day = tonne/h x hours; chemical cost per tonne = (kg per day x price) / steam per day; service per tonne = monthly cost / (steam per day x 30). Compare programmes on the total, and include blowdown losses separately. Prices are your inputs, not Seamens prices.',
        msg: 'Boiler chemical cost: ' + fmt(steam, 1) + ' t steam/day, total Rs ' + fmt(total, 2) + ' per tonne. Please advise on a treatment programme.'
      };
    }
  },
  recipe: {
    title: 'Textile Chemical Dosing Calculator (g/L and % owf)',
    sub: 'Fabric weight x liquor ratio = liquor volume; liquor volume x g/L = grams of chemical.',
    html: function (p) { return '<div class="calc-grid">' + field(p + 'w', 'Fabric weight (kg)', 500) + field(p + 'r', 'Liquor ratio (1 : x)', 10, 0.5, 1) + '</div><div class="calc-rows" id="' + p + 'rows"></div><button type="button" class="calc-btn alt" id="' + p + 'add">+ Add chemical</button>'; },
    init: function (p, upd) {
      var rows = document.getElementById(p + 'rows'), n = 0;
      function add(name, dose) {
        n++;
        var r = el('div', { 'class': 'row' });
        r.innerHTML = '<div><label for="' + p + 'n' + n + '">Chemical</label><input id="' + p + 'n' + n + '" type="text" value="' + name + '"></div><div><label for="' + p + 'g' + n + '">Dose (g/L)</label><input id="' + p + 'g' + n + '" type="number" inputmode="decimal" step="any" min="0" value="' + dose + '"></div><div><label for="' + p + 'o' + n + '">or % owf</label><input id="' + p + 'o' + n + '" type="number" inputmode="decimal" step="any" min="0" value=""></div>';
        rows.appendChild(r);
      }
      add('Levelling agent', 1.5); add('Softener', 20);
      document.getElementById(p + 'add').addEventListener('click', function () { add('Chemical ' + (n + 1), 1); upd(); });
    },
    run: function (p) {
      var W = num(p + 'w'), R = num(p + 'r');
      if (!(W > 0 && R > 0)) return { err: 'Enter fabric weight and liquor ratio.' };
      var L = W * R, out = res('Liquor volume', fmt(L, 0) + ' L'), lines = [], i = 1;
      while (document.getElementById(p + 'n' + i)) {
        var nm = document.getElementById(p + 'n' + i).value || 'Chemical', g = num(p + 'g' + i), o = num(p + 'o' + i), gr = NaN;
        nm = nm.replace(/[<>&]/g, '');
        if (isFinite(o) && o > 0) gr = o / 100 * W * 1000; else if (isFinite(g)) gr = g * L;
        if (isFinite(gr)) { out += res(nm, fmt(gr / 1000, 2) + ' kg'); lines.push(nm + ': ' + fmt(gr / 1000, 2) + ' kg'); }
        i++;
      }
      return {
        out: out,
        note: '% owf = percent on weight of fabric (grams = % / 100 x fabric kg x 1000). If a % owf value is entered it overrides g/L for that row. Always confirm the liquor ratio of the specific machine; keep g/L constant when scaling from lab-dip to bulk.',
        msg: 'Textile dosing: ' + W + ' kg fabric at 1:' + R + ' (' + fmt(L, 0) + ' L liquor). ' + lines.join('; ') + '. Please advise on recipe/products.'
      };
    }
  }
};

function mount(host, idx) {
  var key = host.getAttribute('data-calc'), c = CALCS[key];
  if (!c) return;
  var p = 'c' + idx + key.charAt(0);
  host.innerHTML = '<h2>' + c.title + '</h2><p class="calc-sub">' + c.sub + '</p>' + c.html(p) + '<div id="' + p + 'o"></div><p class="calc-note" id="' + p + 'n"></p><a class="calc-btn" id="' + p + 'w" target="_blank" rel="noopener" href="#">Send this to Seamens on WhatsApp</a>';
  function upd() {
    var r = c.run(p), o = document.getElementById(p + 'o');
    if (r.err) { o.innerHTML = '<p class="calc-err" role="alert">' + r.err + '</p>'; document.getElementById(p + 'n').textContent = ''; return; }
    o.innerHTML = '<div class="calc-out" aria-live="polite">' + r.out + '</div>';
    document.getElementById(p + 'n').textContent = r.note;
    document.getElementById(p + 'w').href = wa(r.msg);
  }
  if (c.init) c.init(p, upd);
  host.addEventListener('input', upd);
  upd();
}
function go() { var h = document.querySelectorAll('[data-calc]'); for (var i = 0; i < h.length; i++) mount(h[i], i); }
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', go); else go();
})();

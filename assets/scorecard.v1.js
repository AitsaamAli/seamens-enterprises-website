(function () {
'use strict';
var ITEMS = [
  ['ISO 9001 certificate verified on the IAF CertSearch database', 'Search the certificate holder name at iafcertsearch.org'],
  ['Company and tax registration confirmed (NTN / sales tax, SECP where applicable)', 'Ask for registration numbers and verify them'],
  ['Technical data sheet and safety data sheet supplied for every product', 'Check active content, pH, handling and storage details'],
  ['Batch consistency evidence (certificate of analysis or test report)', 'Ask what is tested on each batch and how it is recorded'],
  ['Free trial or sample evaluated on your own equipment', 'Trial on your machine, boiler, tower or surface, not only in a lab'],
  ['References from similar plants you can actually call', 'Ask for at least three, in your industry and region'],
  ['Written technical support scope and response time', 'Who attends, how fast, and what is included'],
  ['Local stock and a stated lead time', 'Ask how many days from order to your gate'],
  ['Quote shown as cost-in-use, not only price per kg or litre', 'Dose, dilution or yield must be part of the quote'],
  ['Supplier open to a plant or facility visit', 'See storage, labelling, packing and quality records']
];
function mount(host) {
  var html = '<h2>Chemical Supplier Scorecard</h2><p class="calc-sub">Rate any supplier, including us, on ten verifiable points. 2 = verified, 1 = partly, 0 = not yet.</p><div class="calc-grid">';
  for (var i = 0; i < ITEMS.length; i++) {
    html += '<div><label for="sc' + i + '">' + (i + 1) + '. ' + ITEMS[i][0] + '</label><select id="sc' + i + '" aria-describedby="sch' + i + '"><option value="0">0 - Not yet</option><option value="1">1 - Partly</option><option value="2">2 - Verified</option></select><p class="calc-note" id="sch' + i + '" style="margin-top:.3rem">' + ITEMS[i][1] + '</p></div>';
  }
  html += '</div><div id="scout"></div><p class="calc-note">This scorecard is a self-assessment aid. It does not certify or rank any company. Verify every answer with documents.</p>';
  host.innerHTML = html;
  function upd() {
    var t = 0;
    for (var i = 0; i < ITEMS.length; i++) t += parseInt(document.getElementById('sc' + i).value, 10) || 0;
    var pct = Math.round(t / 20 * 100), v;
    if (pct >= 80) v = 'Strong evidence. Move to a trial and a written quote.';
    else if (pct >= 50) v = 'Some gaps. Ask the supplier to close the open points before ordering.';
    else v = 'Limited evidence so far. Request documents and references before any purchase.';
    document.getElementById('scout').innerHTML = '<div class="calc-out" aria-live="polite"><div class="calc-res"><b>' + t + ' / 20</b><span>Score</span></div><div class="calc-res"><b>' + pct + '%</b><span>Evidence level</span></div><div class="calc-res" style="grid-column:1/-1"><b style="font-size:1rem">' + v + '</b><span>Suggested next step</span></div></div>';
  }
  host.addEventListener('change', upd);
  upd();
}
function go() { var h = document.querySelectorAll('[data-scorecard]'); for (var i = 0; i < h.length; i++) mount(h[i]); }
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', go); else go();
})();

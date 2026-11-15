/* Product directory: every category open on desktop; on phones an accordion where opening one closes the others */
(function () {
  var cards = [].slice.call(document.querySelectorAll('.pdir-card')); if (!cards.length) return;
  var mq = window.matchMedia('(min-width: 901px)');
  function apply() { cards.forEach(function (d, i) { d.open = mq.matches ? true : i === 0; }); }
  cards.forEach(function (d) { d.addEventListener('toggle', function () {
    if (!mq.matches && d.open) cards.forEach(function (o) { if (o !== d) o.open = false; });
  }); });
  apply(); (mq.addEventListener ? mq.addEventListener('change', apply) : mq.addListener(apply));
})();

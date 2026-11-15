/* Homepage ECO showcase: tapping a product in the list swaps the poster and details (links still work without JS) */
(function () {
  var box = document.querySelector('.eco-show'); if (!box) return;
  var imgA = box.querySelector('.es-img'), img = imgA.querySelector('img'), src = imgA.querySelector('source');
  var nameEl = box.querySelector('.es-name'), stageEl = box.querySelector('.es-stage'), descEl = box.querySelector('.es-desc'),
      packsEl = box.querySelector('.es-packs'), cta = box.querySelector('.es-cta');
  var items = [].slice.call(box.querySelectorAll('.es-item'));
  function show(a) {
    if (a.classList.contains('on')) return;
    items.forEach(function (x) { x.classList.toggle('on', x === a); });
    var b = a.getAttribute('data-img'), pre = new Image();
    imgA.classList.add('fade');
    pre.onload = pre.onerror = function () {
      src.srcset = b + '-sm.webp 720w, ' + b + '.webp 1080w'; img.src = b + '-sm.jpg';
      img.alt = a.querySelector('b').textContent + ' poster by Seamens Enterprises';
      setTimeout(function () { imgA.classList.remove('fade'); }, 30);
    };
    pre.src = b + (window.innerWidth > 900 ? '.webp' : '-sm.webp');
    nameEl.textContent = a.querySelector('b').textContent; stageEl.textContent = a.getAttribute('data-stage');
    descEl.textContent = a.getAttribute('data-desc'); packsEl.innerHTML = a.getAttribute('data-packs');
    imgA.href = cta.href = a.getAttribute('href');
    if (window.innerWidth <= 900) a.scrollIntoView({ block: 'nearest', inline: 'center', behavior: 'smooth' });
  }
  items.forEach(function (a) {
    a.addEventListener('click', function (e) { e.preventDefault(); show(a); });
    a.addEventListener('mouseenter', function () { new Image().src = a.getAttribute('data-img') + '-sm.webp'; });
  });
})();

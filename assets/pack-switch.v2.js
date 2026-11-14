/* Pack-size slider: tabs and arrows scroll the track, the active tab follows swipes, gentle autoplay until the visitor interacts */
(function () {
  document.querySelectorAll('.pk-car').forEach(function (car) {
    var track = car.querySelector('.pk-track');
    var slides = [].slice.call(track.querySelectorAll('.pk-slide'));
    var tabs = [].slice.call(car.querySelectorAll('.pk-tabs button'));
    var prev = car.querySelector('.pk-nav.prev'), next = car.querySelector('.pk-nav.next');
    if (slides.length < 2) return;
    var cur = 0, timer = null, touched = false;
    function go(i) {
      cur = (i + slides.length) % slides.length;
      var s = slides[cur];
      track.scrollTo({ left: s.offsetLeft - (track.clientWidth - s.clientWidth) / 2, behavior: 'smooth' });
      mark(cur);
    }
    function mark(i) {
      tabs.forEach(function (t, k) { t.setAttribute('aria-pressed', k === i ? 'true' : 'false'); });
      if (prev) prev.disabled = i === 0;
      if (next) next.disabled = i === slides.length - 1;
    }
    function stop() { touched = true; if (timer) { clearInterval(timer); timer = null; } }
    tabs.forEach(function (t, k) { t.addEventListener('click', function () { stop(); go(k); }); });
    if (prev) prev.addEventListener('click', function () { stop(); go(cur - 1); });
    if (next) next.addEventListener('click', function () { stop(); go(cur + 1); });
    ['pointerdown', 'touchstart', 'wheel', 'keydown'].forEach(function (ev) { track.addEventListener(ev, stop, { passive: true }); });
    var raf = null;
    track.addEventListener('scroll', function () {
      if (raf) return;
      raf = requestAnimationFrame(function () {
        raf = null;
        var mid = track.scrollLeft + track.clientWidth / 2, best = 0, bd = 1e9;
        slides.forEach(function (s, k) { var d = Math.abs(s.offsetLeft + s.clientWidth / 2 - mid); if (d < bd) { bd = d; best = k; } });
        cur = best; mark(best);
      });
    }, { passive: true });
    mark(0);
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      timer = setInterval(function () { if (!touched && !document.hidden) go(cur + 1); }, 3500);
    }
  });
})();

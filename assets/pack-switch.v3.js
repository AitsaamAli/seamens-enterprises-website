/* Pack-size slider v3: auto-rotates every 4 s in a loop, pauses while touched, hovered, off-screen or the tab is hidden,
   resumes after the visitor stops interacting; tabs, arrows and swipes keep the active tab in sync */
(function () {
  var DUR = 4000, IDLE = 6000;
  document.querySelectorAll('.pk-car').forEach(function (car) {
    var track = car.querySelector('.pk-track');
    var slides = [].slice.call(track.querySelectorAll('.pk-slide'));
    var tabs = [].slice.call(car.querySelectorAll('.pk-seg button'));
    var prev = car.querySelector('.pk-nav.prev'), next = car.querySelector('.pk-nav.next');
    if (slides.length < 2) return;
    car.style.setProperty('--pk-dur', DUR + 'ms');
    var cur = 0, timer = null, idle = null, visible = true, hover = false, busy = false, held = false;
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function mark(i) {
      tabs.forEach(function (t, k) { t.setAttribute('aria-pressed', k === i ? 'true' : 'false'); });
      restartBar();
    }
    function restartBar() {
      var t = tabs[cur]; if (!t) return;
      var bar = t.querySelector('i'); if (!bar) return;
      var c = bar.cloneNode(true); bar.parentNode.replaceChild(c, bar);
    }
    function go(i) {
      cur = (i + slides.length) % slides.length;
      var s = slides[cur];
      busy = true;
      track.scrollTo({ left: s.offsetLeft - (track.clientWidth - s.clientWidth) / 2, behavior: reduce ? 'auto' : 'smooth' });
      setTimeout(function () { busy = false; }, 700);
      mark(cur);
    }
    function canPlay() { return !reduce && visible && !hover && !held && !document.hidden; }
    function play() {
      stop();
      if (!canPlay()) { car.classList.remove('pk-play'); return; }
      car.classList.add('pk-play'); car.classList.remove('pk-paused'); restartBar();
      timer = setInterval(function () { if (canPlay()) go(cur + 1); }, DUR);
    }
    function stop() { if (timer) { clearInterval(timer); timer = null; } }
    function interact() {
      stop(); car.classList.remove('pk-play'); held = true;
      clearTimeout(idle); idle = setTimeout(function () { held = false; play(); }, IDLE);
    }
    tabs.forEach(function (t, k) { t.addEventListener('click', function () { interact(); go(k); }); });
    if (prev) prev.addEventListener('click', function () { interact(); go(cur - 1); });
    if (next) next.addEventListener('click', function () { interact(); go(cur + 1); });
    ['pointerdown', 'touchstart', 'wheel', 'keydown'].forEach(function (ev) { track.addEventListener(ev, interact, { passive: true }); });
    car.addEventListener('pointerenter', function (e) { if (e.pointerType !== 'mouse') return; hover = true; stop(); car.classList.add('pk-paused'); });
    car.addEventListener('pointerleave', function (e) { if (e.pointerType !== 'mouse') return; hover = false; car.classList.remove('pk-paused'); play(); });
    var raf = null;
    track.addEventListener('scroll', function () {
      if (busy || raf) return;
      raf = requestAnimationFrame(function () {
        raf = null;
        var mid = track.scrollLeft + track.clientWidth / 2, best = 0, bd = 1e9;
        slides.forEach(function (s, k) { var d = Math.abs(s.offsetLeft + s.clientWidth / 2 - mid); if (d < bd) { bd = d; best = k; } });
        if (best !== cur) { cur = best; mark(best); }
      });
    }, { passive: true });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) { visible = es[0].isIntersecting; if (visible) play(); else { stop(); car.classList.remove('pk-play'); } }, { threshold: 0.35 }).observe(car);
    }
    document.addEventListener('visibilitychange', function () { if (document.hidden) stop(); else play(); });
    mark(0); play();
  });
})();

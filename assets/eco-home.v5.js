/* Coverflow with a timer bar on the active dot (any number of .eco-cf on a page): centre slide full size, neighbours scaled and faded; auto-advance 3.5 s, pauses on touch, hover or off-screen */
(function () {
  [].forEach.call(document.querySelectorAll('.eco-cf'), init);
  function init(box) {
  var track = box.querySelector('.cf-track'), slides = [].slice.call(track.querySelectorAll('.cf-slide'));
  var dotsBox = box.querySelector('.cf-dots'), cur = 0, timer = null, held = false, idle = null, vis = true, hover = false;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  slides.forEach(function () { dotsBox.appendChild(document.createElement('i')); });
  var dots = [].slice.call(dotsBox.children);
  function paint() {
    var mid = track.scrollLeft + track.clientWidth / 2, best = 0, bd = 1e9;
    slides.forEach(function (s, k) {
      var c = s.offsetLeft + s.offsetWidth / 2, d = Math.abs(c - mid) / s.offsetWidth;
      if (Math.abs(c - mid) < bd) { bd = Math.abs(c - mid); best = k; }
      var t = Math.min(d, 1);
      s.style.setProperty('--s', (1 - 0.18 * t).toFixed(3));
      s.style.setProperty('--o', (1 - 0.55 * t).toFixed(3));
    });
    if (best !== cur || !slides[best].classList.contains('on')) {
      cur = best;
      slides.forEach(function (s, k) { s.classList.toggle('on', k === cur); s.setAttribute('tabindex', k === cur ? '0' : '-1'); });
      dots.forEach(function (d, k) { d.classList.toggle('on', k === cur); });
    }
  }
  function go(i) {
    cur = (i + slides.length) % slides.length; var s = slides[cur];
    track.scrollTo({ left: s.offsetLeft - (track.clientWidth - s.offsetWidth) / 2, behavior: reduce ? 'auto' : 'smooth' });
  }
  function can() { return !reduce && vis && !hover && !held && !document.hidden && track.clientWidth > 0; }
  // timer: elapsed time only grows while the carousel may play; the active dot fills as a progress bar
  var DUR = 3500, el = 0, last = null, shown = -1;
  function tick(ts) {
    var dt = last == null ? 0 : Math.min(ts - last, 100); last = ts;
    if (cur !== shown) { el = 0; dots.forEach(function (d) { d.style.removeProperty('--p'); }); shown = cur; }
    if (can()) { el += dt; if (el >= DUR) { el = 0; go(cur + 1); } }
    if (dots[cur]) dots[cur].style.setProperty('--p', Math.min(el / DUR, 1).toFixed(3));
    requestAnimationFrame(tick);
  }
  function play() { if (!reduce) requestAnimationFrame(tick); }
  function interact() { el = 0; held = true; clearTimeout(idle); idle = setTimeout(function () { held = false; }, 7000); }
  var raf = null;
  track.addEventListener('scroll', function () { if (!raf) raf = requestAnimationFrame(function () { raf = null; paint(); }); }, { passive: true });
  ['pointerdown', 'touchstart', 'wheel', 'keydown'].forEach(function (ev) { track.addEventListener(ev, interact, { passive: true }); });
  box.querySelector('.cf-nav.prev').addEventListener('click', function () { interact(); go(cur - 1); });
  box.querySelector('.cf-nav.next').addEventListener('click', function () { interact(); go(cur + 1); });
  slides.forEach(function (s, k) { s.addEventListener('click', function (e) { if (k !== cur) { e.preventDefault(); interact(); go(k); } }); });
  box.addEventListener('pointerenter', function (e) { if (e.pointerType === 'mouse') hover = true; });
  box.addEventListener('pointerleave', function (e) { if (e.pointerType === 'mouse') hover = false; });
  if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { vis = es[0].isIntersecting; }, { threshold: 0.3 }).observe(box);
  window.addEventListener('resize', paint);
  // carousels inside hidden tabs: re-centre when they become visible
  var w0 = track.clientWidth;
  if ('ResizeObserver' in window) new ResizeObserver(function () { var w = track.clientWidth; if (w && !w0) { var s = slides[cur]; track.scrollLeft = s.offsetLeft - (w - s.offsetWidth) / 2; } w0 = w; paint(); }).observe(track);
  paint(); go(0); play();
  }
})();

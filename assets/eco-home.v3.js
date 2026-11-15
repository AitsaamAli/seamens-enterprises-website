/* Coverflow: centre slide full size, neighbours scaled and faded; auto-advance 3.5 s, pauses on touch, hover or off-screen */
(function () {
  var box = document.querySelector('.eco-cf'); if (!box) return;
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
  function can() { return !reduce && vis && !hover && !held && !document.hidden; }
  function play() { stop(); timer = setInterval(function () { if (can()) go(cur + 1); }, 3500); }
  function stop() { if (timer) { clearInterval(timer); timer = null; } }
  function interact() { held = true; clearTimeout(idle); idle = setTimeout(function () { held = false; }, 7000); }
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
  paint(); go(0); play();
})();

/* Products mega menu: desktop hover/click, mobile accordion inside the hamburger menu */
(function () {
  var li = document.querySelector('.mm-li');
  if (!li) return;
  var tog = li.querySelector('.mm-tog');
  var cols = li.querySelectorAll('.mm-col');
  var ham = document.getElementById('hamburger');
  var root = document.documentElement;
  var mobile = null;

  function isMobile() {
    return ham ? getComputedStyle(ham).display !== 'none' : window.innerWidth <= 900;
  }
  function apply() {
    var m = isMobile();
    if (m === mobile) return;
    mobile = m;
    root.classList.toggle('mm-mobile', m);
    cols.forEach(function (d) { if (m) d.removeAttribute('open'); else d.setAttribute('open', ''); });
    setOpen(false);
  }
  function setOpen(o) {
    li.classList.toggle('open', o);
    tog.setAttribute('aria-expanded', o ? 'true' : 'false');
  }
  tog.addEventListener('click', function (e) {
    e.stopPropagation();
    setOpen(!li.classList.contains('open'));
  });
  // On desktop the column headings are not toggles
  cols.forEach(function (d) {
    d.querySelector('summary').addEventListener('click', function (e) { if (!mobile) e.preventDefault(); });
  });
  document.addEventListener('click', function (e) { if (!mobile && !li.contains(e.target)) setOpen(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { setOpen(false); tog.focus(); } });
  // Close the hamburger menu when a product link is tapped
  li.querySelectorAll('.mm a').forEach(function (a) {
    a.addEventListener('click', function () {
      var nl = document.getElementById('navLinks');
      if (nl) nl.classList.remove('open');
      setOpen(false);
    });
  });
  apply();
  window.addEventListener('resize', apply);
})();

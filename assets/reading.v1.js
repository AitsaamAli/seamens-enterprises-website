/* Shared reading layer: progress bar, "On this page", table cards, FAQ accordion, mobile action bar */
(function () {
  var art = document.querySelector('article.blog-content');
  if (!art) return;

  // Reading progress
  var bar = document.createElement('div');
  bar.className = 'rd-progress';
  bar.setAttribute('aria-hidden', 'true');
  document.body.appendChild(bar);
  var ticking = false;
  function prog() {
    var h = document.documentElement;
    var max = h.scrollHeight - h.clientHeight;
    bar.style.width = (max > 0 ? Math.min(100, (h.scrollTop || document.body.scrollTop) / max * 100) : 0) + '%';
    ticking = false;
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(prog); } }, { passive: true });

  // On this page
  var hs = art.querySelectorAll('h2');
  if (hs.length >= 4) {
    var used = {};
    var nav = document.createElement('div');
    nav.setAttribute('role', 'navigation');
    nav.className = 'rd-toc';
    nav.setAttribute('aria-label', 'On this page');
    var ol = document.createElement('ol');
    ol.className = 'rd-toc-l';
    hs.forEach(function (h) {
      if (!h.id) {
        var id = h.textContent.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 60) || 'section';
        while (used[id] || document.getElementById(id)) id += '-2';
        h.id = id;
      }
      used[h.id] = 1;
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.textContent = h.textContent;
      li.appendChild(a);
      ol.appendChild(li);
    });
    var t = document.createElement('div');
    t.className = 'rd-toc-t';
    t.textContent = 'On this page';
    nav.appendChild(t);
    nav.appendChild(ol);
    if (hs.length > 7) {
      nav.classList.add('rd-collapsed');
      var more = document.createElement('button');
      more.type = 'button';
      more.className = 'rd-toc-more';
      more.textContent = 'Show all ' + hs.length + ' sections';
      more.addEventListener('click', function () {
        var c = nav.classList.toggle('rd-collapsed');
        more.textContent = c ? 'Show all ' + hs.length + ' sections' : 'Show fewer';
      });
      nav.appendChild(more);
    }
    var anchor = art.querySelector('.tldr, .pp-facts');
    if (anchor && anchor.parentNode === art) anchor.after(nav);
    else art.insertBefore(nav, art.firstChild);
  }

  // Tables: label cells for the phone card layout, wrap for horizontal scroll
  document.querySelectorAll('.blog-content table').forEach(function (tb) {
    var heads = Array.prototype.map.call(tb.querySelectorAll('thead th'), function (th) { return th.textContent.trim(); });
    if (heads.length >= 2) {
      tb.classList.add('rd-cards');
      tb.querySelectorAll('tbody tr').forEach(function (tr) {
        Array.prototype.forEach.call(tr.children, function (td, i) { if (heads[i]) td.setAttribute('data-label', heads[i]); });
      });
    }
    var p = tb.parentNode;
    if (!(p.classList.contains('rd-tw')) && !(p.style && p.style.overflowX)) {
      var w = document.createElement('div');
      w.className = 'rd-tw';
      p.insertBefore(w, tb);
      w.appendChild(tb);
    } else if (p.style && p.style.overflowX) {
      p.classList.add('rd-tw');
    }
  });

  // FAQ accordion (content stays in the DOM for search engines)
  document.querySelectorAll('.faq .faq-q').forEach(function (q, i) {
    var a = q.nextElementSibling;
    if (!a || !a.classList.contains('faq-a')) return;
    var id = 'faq-a-' + i;
    var inner = document.createElement('div');
    while (a.firstChild) inner.appendChild(a.firstChild);
    a.appendChild(inner);
    a.id = id;
    a.classList.add('rd-a');
    q.classList.add('rd-q');
    q.setAttribute('role', 'button');
    q.setAttribute('tabindex', '0');
    q.setAttribute('aria-controls', id);
    function set(open) { q.setAttribute('aria-expanded', open ? 'true' : 'false'); a.classList.toggle('open', open); }
    set(i === 0);
    function toggle() { set(q.getAttribute('aria-expanded') !== 'true'); }
    q.addEventListener('click', toggle);
    q.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); } });
  });

  // Mobile action bar
  var waEl = document.querySelector('.pp-btn.wa, .cta-box a[href*="wa.me"], .wa-float');
  var wa = waEl ? waEl.getAttribute('href') : 'https://wa.me/923054444125';
  var ab = document.createElement('div');
  ab.className = 'rd-bar';
  ab.innerHTML = '<a class="wa" target="_blank" rel="noopener" href="' + wa.replace(/"/g, '&quot;') + '"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.2c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.5-3.9-4.7-4.1-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.4 0 .5l-.3.5-.4.5c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l2 .9c.3.2.5.2.5.4.1.1.1.7-.1 1.3z"/></svg>WhatsApp</a>' +
    '<a class="call" href="tel:+923026686354"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>Call</a>';
  document.body.appendChild(ab);
  document.body.classList.add('rd-has-bar');
})();

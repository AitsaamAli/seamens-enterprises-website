/* Opens a .pshow poster full screen in a <dialog>; falls back to the link (new tab) without dialog support */
(function(){if(typeof HTMLDialogElement!=='function')return;var d=document.createElement('dialog');d.className='pshow-dlg';d.innerHTML='<button class="pshow-close" aria-label="Close">&times;</button><img alt="">';document.body.appendChild(d);var im=d.querySelector('img');
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('.pshow-zoom');if(!a)return;e.preventDefault();var s=a.querySelector('img');im.src=a.getAttribute('href');im.alt=s?s.alt:'';d.showModal()});
d.addEventListener('click',function(e){if(e.target===d||e.target.classList.contains('pshow-close'))d.close()});})();

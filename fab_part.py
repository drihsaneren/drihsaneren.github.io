# -*- coding: utf-8 -*-
# Mobilde alttan yüzen küçük "WhatsApp'tan seans planla" + ara çubuğu
FAB_CSS = '''  /* mobil yüzen iletişim çubuğu */
  .fab{position:fixed;left:50%;bottom:calc(14px + env(safe-area-inset-bottom,0px));z-index:45;display:flex;gap:8px;align-items:center;
    transform:translate(-50%,24px);opacity:0;visibility:hidden;transition:transform .35s ease,opacity .35s ease,visibility 0s linear .35s}
  .fab.on{transform:translate(-50%,0);opacity:1;visibility:visible;transition:transform .35s ease,opacity .35s ease,visibility 0s}
  .fab a{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:44px;border-radius:999px;text-decoration:none;font-family:var(--body);font-weight:600;font-size:14px;white-space:nowrap;
    box-shadow:0 8px 22px rgba(0,0,0,.38),0 0 0 1px rgba(236,229,207,.10)}
  .fab .wa{padding:0 18px 0 14px;background:var(--foil);color:var(--ground)}
  .fab .wa:active{background:var(--gold)}
  .fab svg{width:18px;height:18px;flex:none}
  .fab a:focus-visible{outline:2px solid var(--gold);outline-offset:3px}
  @media (min-width:761px){.fab{display:none}}
  @media (prefers-reduced-motion:reduce){.fab,.fab.on{transition:none}}
  /* masaüstü: sağ altta telefondakiyle aynı altın renkli buton; üzerine gelince yazı açılır */
  .fab-d{display:none}
  @media (min-width:761px){
    .fab-d{position:fixed;right:24px;bottom:24px;z-index:45;height:52px;min-width:52px;padding:0 16px;border-radius:999px;display:inline-flex;align-items:center;justify-content:center;gap:0;
      background:var(--foil);color:var(--ground);text-decoration:none;font-family:var(--body);font-weight:600;font-size:14px;white-space:nowrap;
      box-shadow:0 8px 22px rgba(0,0,0,.38),0 0 0 1px rgba(236,229,207,.10);transition:gap .25s ease,background .2s ease}
    .fab-d svg{width:20px;height:20px;flex:none}
    .fab-d .lbl{max-width:0;overflow:hidden;opacity:0;transition:max-width .3s ease,opacity .2s ease}
    .fab-d:hover,.fab-d:focus-visible{gap:8px;background:var(--gold)}
    .fab-d:hover .lbl,.fab-d:focus-visible .lbl{max-width:240px;opacity:1}
    .fab-d:focus-visible{outline:2px solid var(--gold);outline-offset:3px}
  }
  @media (min-width:761px) and (max-width:1199px){.fab-d{right:14px;bottom:14px;height:48px;min-width:48px;padding:0 14px}}
  @media (min-width:761px) and (max-width:1199px){:root{--gut:72px}}
  @media (prefers-reduced-motion:reduce){.fab-d,.fab-d .lbl{transition:none}}
'''
def fab_html(wa):
    return f'''<a class="fab-d" href="{wa}" target="_blank" rel="noopener" aria-label="WhatsApp'tan seans planla (yeni sekmede açılır)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2.1-5.4A8.4 8.4 0 1 1 21 11.5z"/></svg><span class="lbl">WhatsApp'tan seans planla</span></a>
<div class="fab" id="fab" aria-hidden="true">
  <a class="wa" href="{wa}" target="_blank" rel="noopener" tabindex="-1"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2.1-5.4A8.4 8.4 0 1 1 21 11.5z"/></svg>WhatsApp'tan seans planla</a>
</div>
<script>
(function(){{
  var f = document.getElementById('fab'); if (!f) return;
  var stop = document.getElementById('iletisim') || document.querySelector('footer');
  var links = f.querySelectorAll('a'), on = null;
  function upd(){{
    var show = (window.scrollY || window.pageYOffset || 0) > window.innerHeight * 0.7;
    if (show && stop && stop.getBoundingClientRect().top < window.innerHeight - 60) show = false;
    if (show === on) return; on = show;
    f.classList.toggle('on', show); f.setAttribute('aria-hidden', show ? 'false' : 'true');
    for (var i = 0; i < links.length; i++) links[i].tabIndex = show ? 0 : -1;
  }}
  window.addEventListener('scroll', upd, {{passive: true}}); window.addEventListener('resize', upd); upd();
}})();
</script>
'''

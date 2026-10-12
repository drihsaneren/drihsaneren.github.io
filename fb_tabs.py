# -*- coding: utf-8 -*-
# Ana sayfa: hero altındaki 5 düğmeyi belirgin sekmelere çevirir (12 Ekim 2026).
# Hizmetler · Hızlı test · Longevity analizi · Kişiye özel egzersiz · Uygulama kareleri · Logonun anlamı
# Yalnızca seçili bölüm görünür; aşağı inince ince bir sekme çubuğu başlığın altına yapışır.
# Bilgi köşesindeki uzun konu listeleri her ekranda "Tüm konuları göster" ile katlanır.
# publish.sh içinde splice_home.py'den sonra çalışır (bilgi bölümü o adımda eklenir).
import re
p = "site/index.html"
s = open(p, encoding="utf-8").read()
if 'id="kesfet"' in s:
    print("fb_tabs: zaten uygulanmış"); raise SystemExit

def rep(old, new, cnt=1):
    global s
    assert s.count(old) == cnt, (old[:70], s.count(old)); s = s.replace(old, new)

# 1) hero'daki küçük düğmeler kalkıyor (yerlerini sekmeler alıyor)
m = re.search(r'\n    <ul class="nav">\n(      <li><a href="#[^"]+">[^<]+</a></li>\n){5}    </ul>\n', s)
assert m, "hero nav bulunamadı"
s = s[:m.start()] + "\n" + s[m.end():]

# 2) hızlı test kendi bölümüne taşınıyor
a = s.index('      <div class="qt" id="hizli-test">')
b = s.index('\n    </div>\n  </section>\n\n  <section id="ornek-plan">', a)
qt = s[a:b]
s = s[:a].rstrip() + s[b:]
rep('<p class="lx-foot"><a href="#hizli-test">2 dakikalık hızlı testi deneyin ↓</a>',
    '<p class="lx-foot"><a href="#hizli-test">2 dakikalık hızlı testi deneyin →</a>')

ICON = {
 "hizmetler": '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M12 17.2s-3-1.9-3-4a1.6 1.6 0 0 1 3-.8 1.6 1.6 0 0 1 3 .8c0 2.1-3 4-3 4z"/>',
 "test": '<circle cx="12" cy="13.5" r="7.5"/><path d="M12 9.5v4l2.6 2.4M10 2.5h4M12 2.5V6M18.5 6.5l1.6-1.6"/>',
 "analiz": '<path d="M4 17.5a8 8 0 1 1 16 0"/><path d="M12 17.5l4.2-5.2"/><circle cx="12" cy="17.5" r="1.4"/><path d="M6.6 12.2l1.2.8M12 9.4v1.4M17.4 12.2l-1.2.8"/>',
 "ornek-plan": '<path d="M6.5 6.5v11M17.5 6.5v11M3.5 9.5v5M20.5 9.5v5M6.5 12h11"/>',
 "kareler": '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="10" r="1.8"/><path d="M21 16l-5-5-8 8"/>',
 "logo": '<circle cx="12" cy="12" r="9.5"/><path d="M12 20V12M12 12L7 6.5M12 12l5-5.5"/>',
}
TABS = [("hizmetler", "Hizmetler", ""), ("test", "Hızlı test", "2 dk"), ("analiz", "Longevity analizi", ""),
        ("ornek-plan", "Kişiye özel egzersiz", ""), ("kareler", "Uygulama kareleri", ""), ("logo", "Logonun anlamı", "")]
btns = []
for i, (pid, lab, badge) in enumerate(TABS):
    bd = f'<em class="new">{badge}</em>' if badge else ""
    btns.append(f'        <button type="button" role="tab" id="kt-{pid}" aria-controls="{pid}" aria-selected="{"true" if i == 0 else "false"}">'
                f'<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">{ICON[pid]}</svg><span>{lab}</span>{bd}</button>')
KESFET = ('  <section id="kesfet" class="kt">\n    <div class="wrap">\n'
          '      <div class="sec-head"><p class="eyebrow">Keşfedin</p><h2>Neyi merak ediyorsunuz?</h2></div>\n'
          '      <div class="kt-tabs" role="tablist" aria-label="Bölümler">\n' + "\n".join(btns) + '\n      </div>\n    </div>\n  </section>\n\n')

# 3) bölümler sekme paneli oluyor
for pid, _, _ in TABS:
    if pid == "test": continue
    rep(f'  <section id="{pid}">', f'  <section id="{pid}" class="kt-p" role="tabpanel" aria-labelledby="kt-{pid}">')
TEST = ('  <section id="test" class="kt-p" role="tabpanel" aria-labelledby="kt-test">\n    <div class="wrap">\n'
        + qt + '\n    </div>\n  </section>\n\n')
rep('<main>\n  <section id="hizmetler"', '<main>\n' + KESFET + '  <section id="hizmetler"')
rep('  <section id="analiz" class="kt-p"', TEST + '  <section id="analiz" class="kt-p"')

# 4) bilgi köşesi: uzun konu listeleri her ekranda katlı başlar
a = s.index('      <div class="kose-idx">')
endm = '<a class="all" href="bilgi.html">Tüm konular →</a>\n      </div>'
b = s.index(endm, a) + len(endm)
idx = s[a:b]
total = sum(int(x) for x in re.findall(r'<small>(\d+)</small>', idx))
s = (s[:a] + f'      <details class="kt-idx" id="kt-idx"><summary><span>Tüm konuları göster</span><small data-n="{total}"><span>başlık</span></small></summary>\n'
     + idx + '\n      </details>' + s[b:])

CSS = """
  /* keşfet sekmeleri */
  .kt{padding-block:clamp(30px,6vw,52px) clamp(8px,2vw,16px)}
  .kt .sec-head{margin-bottom:16px}
  .kt-tabs{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px}
  @media (max-width:860px){.kt-tabs{grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}}
  .kt-tabs button{all:unset;box-sizing:border-box;cursor:pointer;position:relative;display:grid;justify-items:center;align-content:center;gap:8px;min-height:98px;padding:14px 8px 12px;
    border:1px solid var(--line);border-radius:16px;text-align:center;color:var(--ink-soft);font-size:14.5px;font-weight:600;line-height:1.25;
    background:radial-gradient(120% 100% at 50% 0%,rgba(226,171,71,.07),transparent 65%),var(--ground-2);transition:border-color .2s ease,color .2s ease,transform .2s ease,box-shadow .2s ease}
  .kt-tabs button svg{width:30px;height:30px;fill:none;stroke:var(--sage);stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;transition:stroke .2s ease}
  .kt-tabs button:hover{border-color:var(--line-strong);color:var(--ink);transform:translateY(-2px)}
  .kt-tabs button[aria-selected="true"]{border-color:var(--foil);color:var(--ink);box-shadow:0 12px 30px rgba(0,0,0,.28),inset 0 0 0 1px rgba(216,178,94,.35);
    background:radial-gradient(120% 100% at 50% 0%,rgba(226,171,71,.26),rgba(226,171,71,.05) 70%),var(--ground-2)}
  .kt-tabs button[aria-selected="true"] svg{stroke:var(--gold)}
  .kt-tabs button:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .kt-tabs .new{position:absolute;top:8px;right:8px;font-style:normal;font-size:10.5px;letter-spacing:.04em;font-weight:700;color:var(--ground);background:var(--gold);border-radius:999px;padding:2px 7px;line-height:1.4}
  @media (max-width:420px){.kt-tabs button{min-height:88px;font-size:13px;padding:12px 6px 10px;gap:6px}.kt-tabs button svg{width:26px;height:26px}.kt-tabs .new{top:6px;right:6px}}
  .kt-on section.kt-p{border-top:0;padding-top:clamp(22px,4vw,40px)}
  .kt-on section.kt-p[hidden]{display:none}
  .kt-on #test{padding-bottom:clamp(30px,6vw,56px)}
  #test .qt{margin-top:0}
  .kt-on section.kt-p.kt-in{animation:kt-in .35s ease both}
  @keyframes kt-in{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
  .kt-mini{position:fixed;left:0;right:0;top:var(--kt-top,57px);z-index:39;background:rgba(28,40,25,.95);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
    border-bottom:1px solid var(--line);transform:translateY(-120%);opacity:0;visibility:hidden;transition:transform .25s ease,opacity .25s ease,visibility 0s linear .25s}
  .kt-mini.show{transform:none;opacity:1;visibility:visible;transition:transform .25s ease,opacity .25s ease}
  .kt-mini .wrap{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;padding-block:8px}
  .kt-mini .wrap::-webkit-scrollbar{display:none}
  .kt-mini button{all:unset;box-sizing:border-box;cursor:pointer;flex:none;padding:7px 14px;border-radius:999px;border:1px solid var(--line);font-size:13.5px;color:var(--ink-soft);white-space:nowrap}
  .kt-mini button[aria-pressed="true"]{background:var(--foil);border-color:var(--foil);color:var(--ground);font-weight:600}
  .kt-mini button:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .kt-idx{margin-top:20px}
  .kt-idx > summary{list-style:none;cursor:pointer;display:flex;align-items:center;justify-content:space-between;gap:12px;padding:14px 18px;border:1px solid var(--line-strong);border-radius:14px;
    background:var(--ground-2);color:var(--ink);font-weight:600}
  .kt-idx > summary::-webkit-details-marker{display:none}
  .kt-idx > summary small{color:var(--muted);font-weight:400;font-size:14px;display:flex;align-items:center;gap:10px}
  .kt-idx > summary small::before{content:attr(data-n);color:var(--foil);font-weight:600;margin-right:-5px}
  .kt-idx > summary small::after{content:"";width:9px;height:9px;border-right:2px solid var(--foil);border-bottom:2px solid var(--foil);transform:rotate(45deg) translateY(-3px);transition:transform .2s ease}
  .kt-idx[open] > summary small::after{transform:rotate(-135deg) translateY(-3px)}
  .kt-idx[open] > summary{border-color:var(--line)}
  .kt-idx > summary:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  @media (prefers-reduced-motion:reduce){.kt-mini,.kt-tabs button,.kt-idx > summary small::after{transition:none}.kt-on section.kt-p.kt-in{animation:none}}
"""
rep("  section + section{border-top:1px solid var(--line)}", "  section + section{border-top:1px solid var(--line)}" + CSS)

JS = r"""<script>
(function(){
  var sec = document.getElementById('kesfet'); if (!sec) return;
  var tabs = [].slice.call(sec.querySelectorAll('[role="tab"]'));
  var panels = tabs.map(function(t){ return document.getElementById(t.getAttribute('aria-controls')); });
  if (!panels.every(Boolean)) return;
  document.documentElement.classList.add('kt-on');
  var bar = document.querySelector('.bar'), list = sec.querySelector('.kt-tabs'), cur = 0;
  function off(){ return bar ? bar.getBoundingClientRect().height : 0; }
  var mini = document.createElement('nav'); mini.className = 'kt-mini'; mini.setAttribute('aria-label', list.getAttribute('aria-label'));
  var mw = document.createElement('div'); mw.className = 'wrap'; mini.appendChild(mw);
  var mb = tabs.map(function(t, i){
    var b = document.createElement('button'); b.type = 'button'; b.textContent = t.querySelector('span').textContent;
    b.addEventListener('click', function(){ pick(i); toPanel(i, true); }); mw.appendChild(b); return b;
  });
  document.body.appendChild(mini);
  function pick(i, quiet){
    cur = i;
    tabs.forEach(function(t, k){ var on = k === i;
      t.setAttribute('aria-selected', on ? 'true' : 'false'); t.tabIndex = on ? 0 : -1;
      if (panels[k].hidden !== !on) { panels[k].hidden = !on; if (on && !quiet) { panels[k].classList.remove('kt-in'); void panels[k].offsetWidth; panels[k].classList.add('kt-in'); } }
      mb[k].setAttribute('aria-pressed', on ? 'true' : 'false'); });
    var b = mb[i]; mw.scrollLeft = Math.max(0, b.offsetLeft - (mw.clientWidth - b.offsetWidth) / 2);
    try { window.dispatchEvent(new Event('resize')); } catch (e) {}
    upd();
  }
  function scrollToY(y, smooth){ window.scrollTo({top: Math.max(0, y), behavior: smooth ? 'smooth' : 'auto'}); }
  function toPanel(i, smooth){ var r = panels[i].getBoundingClientRect(); scrollToY(r.top + window.scrollY - off() - 52, smooth); }
  tabs.forEach(function(t, i){
    t.addEventListener('click', function(){ pick(i);
      var r = panels[i].getBoundingClientRect(); if (r.top > window.innerHeight * .72) scrollToY(sec.getBoundingClientRect().top + window.scrollY - off(), true); });
    t.addEventListener('keydown', function(e){
      var k = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0; if (!k && e.key !== 'Home' && e.key !== 'End') return;
      e.preventDefault(); var n = e.key === 'Home' ? 0 : e.key === 'End' ? tabs.length - 1 : (i + k + tabs.length) % tabs.length; pick(n); tabs[n].focus(); });
  });
  function panelOf(el){ for (var k = 0; k < panels.length; k++) if (panels[k] === el || panels[k].contains(el)) return k; return -1; }
  function go(hash, smooth){
    var id = ''; try { id = decodeURIComponent((hash || '').slice(1)); } catch (e) { return false; }
    var el = id && document.getElementById(id); if (!el) return false;
    var k = panelOf(el); if (k < 0) return false;
    pick(k, !smooth);
    requestAnimationFrame(function(){
      if (el === panels[k]) scrollToY(sec.getBoundingClientRect().top + window.scrollY - off(), smooth);
      else scrollToY(el.getBoundingClientRect().top + window.scrollY - off() - 60, smooth);
    });
    return true;
  }
  document.addEventListener('click', function(e){
    var a = e.target.closest ? e.target.closest('a[href^="#"]') : null; if (!a) return;
    var h = a.getAttribute('href'); if (h.length > 1 && go(h, true)) { e.preventDefault(); try { history.pushState(null, '', h); } catch (x) {} }
  });
  window.addEventListener('hashchange', function(){ go(location.hash, true); });
  var tick = false;
  function upd(){
    tick = false; var o = off(), tb = list.getBoundingClientRect(), pb = panels[cur].getBoundingClientRect();
    var show = tb.bottom < o && pb.bottom > o + 90;
    mini.style.setProperty('--kt-top', o + 'px'); mini.classList.toggle('show', show);
    if ('inert' in mini) mini.inert = !show;
  }
  window.addEventListener('scroll', function(){ if (!tick) { tick = true; requestAnimationFrame(upd); } }, {passive: true});
  window.addEventListener('resize', function(){ if (!tick) { tick = true; requestAnimationFrame(upd); } });
  if (!go(location.hash, false)) pick(0, true);
})();
</script>
"""
s = s.rstrip("\n") + "\n" + JS
open(p, "w", encoding="utf-8").write(s)
print("fb_tabs: sekmeler eklendi;", total, "başlık katlandı")

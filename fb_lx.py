# -*- coding: utf-8 -*-
# Longevity bölüm başı: "iğne yok, tahlil yok, genetik test yok" vurgusu + büyük çalışmalardan
# sayarak gelen, ışıklı rakamlar + umut veren kapanış.
p = "site/index.html"
s = open(p, encoding="utf-8").read()


def rep(old, new, cnt=1):
    global s
    assert s.count(old) == cnt, (old[:80], s.count(old))
    s = s.replace(old, new)


LEAF = '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 15V7.2M8 8.4C8 5.6 6.2 3.8 3.4 3.6c.1 2.7 1.9 4.6 4.6 4.8Zm0 0c0-2.8 1.8-4.6 4.6-4.8-.1 2.7-1.9 4.6-4.6 4.8Z" stroke="currentColor" stroke-width="1.1" fill="none" stroke-linecap="round"/></svg>'
IC = {
    "grip": '<path d="M7 11V6.5a1.5 1.5 0 0 1 3 0V11M10 10V5a1.5 1.5 0 0 1 3 0v5M13 10V6a1.5 1.5 0 0 1 3 0v6c0 4.5-2.5 8-6.5 8-2.5 0-4-1.4-5.5-4l-1.3-2.4a1.4 1.4 0 0 1 2.4-1.4L7 14"/>',
    "walk": '<circle cx="13" cy="4.5" r="1.8"/><path d="M11 21l2-6 3 3v3M13 15l-1-5 3-2 2 3 3 1M10 10l-3 1-1 3"/>',
    "bal": '<circle cx="12" cy="4.5" r="1.8"/><path d="M12 7v7l-1 7M12 9.5l-5 1.5M12 9.5l5 1.5M12 14l4 1.5-1 3"/>',
    "floor": '<path d="M3 20h18M6 20l2-5h4l3-3M12 12l-1-4M11 8a1.8 1.8 0 1 0 0-.1M15 12l3 2"/>',
}
ST = [
    ("grip", "%16", "Kavrama gücü", "Her 5 kg düşüşte ölüm riskindeki artış. Tansiyondan daha güçlü bir gösterge.",
     "https://doi.org/10.1016/S0140-6736(14)62000-6", "Lancet 2015 · 139.691 kişi"),
    ("walk", "%12", "Yürüme hızı", "Her 0,1 m/sn daha hızlı yürüyüşte ölüm riskindeki azalma.",
     "https://jamanetwork.com/journals/jama/fullarticle/644554", "JAMA 2011 · 34.485 kişi"),
    ("bal", "%84", "Tek ayak dengesi", "10 saniye tek ayakta duramayanlarda ölüm riskindeki artış.",
     "https://doi.org/10.1136/bjsports-2021-105360", "BJSM 2022 · 1.702 kişi"),
    ("floor", "6 kat", "Yerden kalkma", "Yerde oturup kalkma testinde düşük puanda kalp-damar kaynaklı ölüm riski.",
     "https://academic.oup.com/eurjpc/article/33/12/2170/8163161", "Eur J Prev Cardiol 2026 · 4.282 kişi"),
]
tiles = "\n".join(f'''          <li style="--i:{i}"><svg class="lx-ic" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{IC[ic]}</svg><b class="lx-n">{n}</b><span class="lx-l">{l}</span><p>{t}</p><a class="lx-src" href="{h}" target="_blank" rel="noopener">{src}</a></li>'''
                  for i, (ic, n, l, t, h, src) in enumerate(ST))

old_head = '''      <div class="sec-head">
        <p class="eyebrow">Longevity projesi</p>
        <h2>Analiz ve karşılığında egzersiz reçetesi</h2>
        <p class="intro">Önce fonksiyonel analiz yapıyoruz: kuvvet, güç, denge, yürüyüş ve esneklik ölçülür, kişinin fonksiyonel yaşı çıkarılır. Sonuca göre ona özel, animasyonlu bir egzersiz reçetesi veriyoruz. <a href="#hizli-test">2 dakikalık hızlı testi deneyin ↓</a></p>
      </div>'''
new_head = f'''      <div class="lx" id="lx">
        <p class="eyebrow">Longevity analizi</p>
        <h2 class="lx-h"><span class="lx-h1">İğne yok, tahlil yok, genetik test yok.</span><span class="lx-h2">Nasıl hareket ettiğiniz, ne kadar uzun ve sağlıklı yaşayacağınıza dair çok şey söyler.</span></h2>
        <p class="intro">Kavrama gücü, yürüme hızı, denge ve yerden kalkabilmek; büyük bilimsel çalışmalarda uzun yaşamla en güçlü ilişkili göstergeler arasında. Bunları evinizde ölçüyor, fonksiyonel yaşınızı çıkarıyor ve size özel bir egzersiz reçetesine dönüştürüyorum.</p>
        <ul class="lx-stats">
{tiles}
        </ul>
        <p class="lx-proof"><b>Tahmin değil, ölçüm.</b> Her göstergenin arkasında yayımlanmış bir çalışma var; sonuçlarınız yazılı bir raporla sizde kalır.</p>
        <p class="lx-hope">{LEAF}<span><b>İyi haber:</b> Genlerinizi değiştiremezsiniz; kas gücünüzü, dengenizi ve yürüyüşünüzü ise her yaşta geliştirebilirsiniz.</span></p>
        <p class="lx-foot"><a href="#hizli-test">2 dakikalık hızlı testi deneyin ↓</a><span>Tahlillerin yerini tutmaz, onları tamamlar.</span></p>
      </div>'''
rep(old_head, new_head)

CSS = r'''  /* longevity bölüm başı */
  #analiz{position:relative;overflow:hidden;isolation:isolate}
  #analiz::before{content:"";position:absolute;left:50%;top:-260px;width:min(1200px,160vw);height:760px;translate:-50% 0;z-index:-1;pointer-events:none;
    background:radial-gradient(closest-side,rgba(226,171,71,.14),rgba(143,164,118,.06) 55%,transparent);animation:aura 10s ease-in-out infinite}
  .lx{display:grid;gap:14px;margin-bottom:clamp(36px,6vw,56px)}
  .lx-h{display:grid;gap:10px;max-width:none}
  .lx-h1{font-size:clamp(32px,6.4vw,54px);line-height:1.12;padding:.06em 0 .14em;margin-bottom:-.12em;color:var(--foil)}
  @supports ((-webkit-background-clip:text) or (background-clip:text)){
    .lx-h1{background:linear-gradient(100deg,var(--foil) 0 40%,#fff3cf 50%,var(--foil) 60% 100%) 100% 0/260% 100% no-repeat;-webkit-background-clip:text;background-clip:text;color:transparent}
    .lx.seen .lx-h1{animation:shimmer 2.2s ease-in-out .3s both}
  }
  .lx-h2{font-size:clamp(21px,3vw,28px);line-height:1.3;color:var(--ink);max-width:36ch}
  .lx .intro{margin:0;color:var(--ink-soft);max-width:62ch}
  .lx-stats{list-style:none;margin:10px 0 0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
  @media (min-width:1000px){.lx-stats{grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}}
  .lx-stats li{position:relative;display:grid;align-content:start;gap:4px;padding:16px 16px 14px;border:1px solid var(--line);border-radius:16px;overflow:hidden;
    background:radial-gradient(120% 90% at 0% 0%,rgba(226,171,71,.10),transparent 60%),var(--ground-2)}
  .lx-stats li::after{content:"";position:absolute;inset:0;pointer-events:none;background:linear-gradient(115deg,transparent 30%,rgba(255,236,190,.10) 48%,transparent 66%);translate:-120% 0}
  .lx.seen .lx-stats li::after{animation:lx-sweep 1.6s ease-out both;animation-delay:calc(.5s + var(--i)*.18s)}
  @keyframes lx-sweep{to{translate:120% 0}}
  .lx.js:not(.seen) .lx-stats li{opacity:0}
  .lx.seen .lx-stats li{animation:rise .8s cubic-bezier(.2,.7,.2,1) both;animation-delay:calc(var(--i)*.12s)}
  .lx-ic{width:30px;height:30px;fill:none;stroke:var(--sage);stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;margin-bottom:4px}
  .lx-n{font-family:var(--display);font-weight:400;font-size:clamp(36px,5vw,48px);line-height:1;color:var(--gold);font-variant-numeric:tabular-nums;text-shadow:0 0 22px rgba(226,171,71,.45);white-space:nowrap}
  .lx-l{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink);font-weight:600;margin-top:4px}
  .lx-stats p{margin:0;font-size:14px;line-height:1.45;color:var(--ink-soft)}
  .lx-src{margin-top:6px;font-size:12px;color:var(--muted);text-decoration:none}
  .lx-src:hover{color:var(--foil);text-decoration:underline}
  .lx-proof{margin:4px 0 0;padding-left:14px;border-left:2px solid var(--gold);color:var(--ink-soft);max-width:62ch}
  .lx-proof b{color:var(--ink);font-weight:600}
  .lx-hope{margin:6px 0 0;display:flex;align-items:flex-start;gap:12px;font-family:var(--display);font-size:clamp(19px,2.4vw,23px);line-height:1.4;color:var(--ink);max-width:52ch}
  .lx-hope b{font-weight:400;color:var(--gold)}
  .lx-hope svg{flex:none;width:24px;height:24px;margin-top:3px;color:var(--gold);filter:drop-shadow(0 0 6px rgba(226,171,71,.7))}
  .lx-foot{margin:0;display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 18px;font-size:14px}
  .lx-foot a{font-weight:600}
  .lx-foot span{color:var(--muted);font-size:13px}
  @media (prefers-reduced-motion:reduce){#analiz::before{animation:none}}
'''
rep("  /* analiz raporu: slayt gösterisi */", CSS + "  /* analiz raporu: slayt gösterisi */")

JS = r'''<script>
(function(){
  var box = document.getElementById('lx'); if (!box) return;
  box.classList.add('js');
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function run(){
    box.classList.add('seen');
    if (reduce) return;
    [].forEach.call(box.querySelectorAll('.lx-n'), function(el, i){
      var fin = el.textContent, m = fin.match(/^([^\d]*)(\d+)(.*)$/); if (!m) return;
      var to = +m[2], st = null, dur = 1400, delay = 300 + i * 180;
      el.textContent = m[1] + '0' + m[3];
      function step(ts){
        if (st === null) st = ts;
        var t = Math.min(1, Math.max(0, (ts - st - delay) / dur)), e = 1 - Math.pow(1 - t, 3);
        el.textContent = m[1] + Math.round(to * e) + m[3];
        if (t < 1) requestAnimationFrame(step); else el.textContent = fin;
      }
      requestAnimationFrame(step);
    });
  }
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(es){ if (es[0].isIntersecting) { io.disconnect(); run(); } }, {threshold: .3});
    io.observe(box.querySelector('.lx-stats'));
  } else run();
})();
</script>
'''
anchor = "<script>\n(function(){\n  var box = document.getElementById('rapor'); if (!box) return;"
assert s.count(anchor) == 1
s = s.replace(anchor, JS + anchor, 1)
open(p, "w", encoding="utf-8").write(s)
print("ok")

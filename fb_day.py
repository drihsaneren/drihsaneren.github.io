# -*- coding: utf-8 -*-
# "Günlük Hareket Skalası": sabahtan geceye 9 kısa soru, her ekranda tek soru.
# Yaş grubuna göre puanlanır; sonuç yeşil / sarı / turuncu / kırmızı bölge olarak gösterilir.
# Sonuç ve en çok zorlanılan anlar ücretsiz ön görüşme mesajına eklenir.
p = "site/index.html"
s = open(p, encoding="utf-8").read()


def rep(old, new, cnt=1):
    global s
    assert s.count(old) == cnt, (old[:80], s.count(old))
    s = s.replace(old, new)


IC = {
    "sun": '<path d="M3 18h18M6.5 18a5.5 5.5 0 0 1 11 0M12 5.5V3M5.3 9.3 3.9 7.9M18.7 9.3l1.4-1.4"/>',
    "sink": '<path d="M3.5 11h17a8.5 7 0 0 1-17 0zM12 11V6.5a2 2 0 0 1 4 0V7M9 21h6"/>',
    "foot": '<path d="M9 3v9.5c0 1.5-.8 2.6-2.2 3.4C5.3 16.8 5 18 5.6 19.2c.6 1.1 1.8 1.6 3.2 1.6h7.4c1.4 0 2.3-1.2 1.8-2.4-.5-1.3-2-2-3.9-2.4L13.5 15V3"/><path d="M17 6.5c1.2-.8 2.6-.8 3.5 0M17.5 9.5c1-.6 2-.6 2.8 0"/>',
    "shoe": '<path d="M3 16.5V10l3.5-1 2 2.5 4-2 1.5 2.5c3.5.7 6.5 1.8 7 4.5v2H3z"/><path d="M8.5 11.5l1.5 2M11.5 10.5l1.5 2M3 16.5h19"/>',
    "stairs": '<path d="M3 20h5v-4h4v-4h4V8h5M16 4l2-1.5"/>',
    "desk": '<path d="M5 5.5h14v9H5zM3 18.5h18M10 14.5v4M14 14.5v4"/>',
    "chair": '<path d="M7 3v18M7 12.5h10V21M17 12.5V9"/>',
    "walk": '<circle cx="13" cy="4.5" r="1.8"/><path d="M11 21l2-6 3 3v3M13 15l-1-5 3-2 2 3 3 1M10 10l-3 1-1 3"/>',
    "moon": '<path d="M19.5 14.5A8 8 0 1 1 9.5 4.5a6.5 6.5 0 0 0 10 10z"/>',
}
# (saat, an, ikon, soru, seçenekler, yaş ayarı: bu yaş grubundan itibaren 1 puan indirilir, rehber, kısa ad)
Q = [
    ("07:00", "Uyanış", "sun", "Yataktan doğrulurken ağrı hissediyor musunuz?",
     ["Hayır", "Hafif", "Belirgin", "Çok, zorlukla kalkıyorum"], None, "bel-agrisi.html", "yataktan doğrulurken ağrı"),
    ("07:10", "Lavabo", "sink", "Yüzünüzü yıkarken lavaboya eğilmek nasıl?",
     ["Rahat", "Biraz zorlanıyorum", "Tutunarak eğiliyorum", "Çok ağrılı ve zor"], None, "bel-fitigi.html", "lavaboya eğilirken zorlanma"),
    ("07:15", "Ayak yıkama", "foot", "Ayağınızı yıkamak için lavaboya kaldırabiliyor musunuz?",
     ["Rahatça", "Zorlanarak", "Tutunarak, güçlükle", "Yapamıyorum"], 4, "dusme-onleme.html", "ayağı lavaboya kaldırmakta güçlük"),
    ("07:30", "Giyinme", "shoe", "Ayakkabı bağcığınızı kendiniz bağlayabiliyor musunuz?",
     ["Rahatça", "Zorlanarak", "Oturup uzun uğraşla", "Yardım gerekiyor"], None, "kalca-kireclenmesi.html", "ayakkabı bağlarken zorlanma"),
    ("08:30", "Merdiven", "stairs", "Bir kat merdiveni nasıl çıkıyorsunuz?",
     ["Rahatça", "Nefes nefese ya da ağrıyla", "Tutunarak, dinlenerek", "Çıkamıyorum"], 4, "diz-kireclenmesi.html", "merdivende zorlanma"),
    ("11:00", "Masa başında", "desk", "Otururken ağrı hissediyor musunuz?",
     ["Hayır", "Uzun oturunca", "Kısa sürede", "Sürekli"], None, "masa-basi.html", "otururken ağrı"),
    ("15:00", "Kalkarken", "chair", "Sandalyeden kalkarken ellerinizden destek alıyor musunuz?",
     ["Hayır", "Bazen", "Her zaman", "Ancak yardımla kalkabiliyorum"], None, "otur-kalk-testi.html", "sandalyeden kalkarken destek alma"),
    ("18:00", "Yürüyüş", "walk", "Buradan yürümeye başlasanız, durmadan kaç dakika yürürsünüz?",
     ["30 dakikadan fazla", "15–30 dakika", "5–15 dakika", "5 dakikadan az"], 3, "hareket.html", "kısa yürüme süresi"),
    ("23:00", "Gece", "moon", "Ağrı uykunuzu bölüyor mu?",
     ["Hayır", "Ara sıra", "Haftada birkaç gece", "Her gece"], None, "uyku.html", "ağrının uykuyu bölmesi"),
]
N = len(Q)
MAX = 3 * N
AGES = ["18–39", "40–54", "55–64", "65–74", "75+"]
ages = "".join(f'<button type="button" class="gh-o" data-v="{i}">{a}</button>' for i, a in enumerate(AGES))
steps = []
for i, (t, nm, ic, q, opts, adj, href, short) in enumerate(Q):
    ob = "".join(f'<button type="button" class="gh-o" data-v="{k}">{o}</button>' for k, o in enumerate(opts))
    steps.append(f'''          <div class="gh-step" data-s="{i}"{f' data-adj="{adj}"' if adj is not None else ''} data-href="{href}">
            <div class="dm-h"><svg class="dm-ic" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{IC[ic]}</svg><b class="dm-t">{t}</b><span class="dm-w">{nm}</span></div>
            <p class="gh-q" id="ghq{i}">{q}</p>
            <div class="gh-opts" role="group" aria-labelledby="ghq{i}">{ob}</div>
            <span class="dm-s" hidden>{short}</span>
          </div>''')
dots = "".join(f'<i style="--i:{i}"></i>' for i in range(N))
SUN = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6"/></svg>'
MOON = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M19.5 14.5A8 8 0 1 1 9.5 4.5a6.5 6.5 0 0 0 10 10z"/></svg>'
BACK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 6-6 6 6 6"/></svg>'
BANDS = [
    ("g", "Yeşil", "Gününüz rahat akıyor",
     'Yaşınıza göre günlük hareketleriniz çok iyi. Korumak için <a href="bilgi.html#kendine-iyi-bak">Kendine iyi bak</a> bölümüne göz atabilirsiniz.'),
    ("y", "Sarı", "İlk sinyaller var",
     "Bazı anlar zorlamaya başlamış. Bu evrede başlanan birkaç haftalık düzenli egzersiz genellikle belirgin fark yaratır."),
    ("o", "Turuncu", "Günlük hayatınız kısıtlanıyor",
     "Ağrı ve zorlanma günlük işlerinizi etkiliyor. Kapsamlı bir değerlendirme ve size özel bir program zamanı."),
    ("r", "Kırmızı", "Destek alma zamanı",
     "Günün birçok anında belirgin zorlanıyorsunuz. Bununla yaşamak zorunda değilsiniz: önce bir hekim değerlendirmesi, ardından evde düzenli rehabilitasyon öneririm."),
]
zones = "".join(f'<span class="z {b}">{nm}</span>' for b, nm, _, _ in BANDS)
heads = "\n".join(f'            <h3 class="gh-title" data-b="{b}" hidden><span class="gh-band {b}">{nm} bölge</span>{t}</h3>' for b, nm, t, _ in BANDS)
msgs = "\n".join(f'            <p class="gh-msg" data-b="{b}" hidden>{m}</p>' for b, _, _, m in BANDS)

SEC = f'''  <section id="bir-gun" class="day-sec">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Günlük Hareket Skalası</p>
        <h2>Bir gününüz nasıl geçiyor?</h2>
        <p class="intro">Sabahtan geceye {N} kısa soru. Yaşınıza göre değerlendirilir, sonucunuz renkle gösterilir.</p>
      </div>
      <div class="gh" id="gh">
        <div class="dm-bar" aria-hidden="true">{SUN}<span class="dm-line">{dots}</span>{MOON}</div>
        <div class="gh-card">
          <div class="gh-step on" data-s="age">
            <div class="dm-h"><span class="dm-w">Başlarken</span></div>
            <p class="gh-q" id="ghqa">Yaş grubunuz?</p>
            <div class="gh-opts gh-age" role="group" aria-labelledby="ghqa">{ages}</div>
          </div>
{chr(10).join(steps)}
          <div class="gh-step gh-res" data-s="res" tabindex="-1">
            <p class="gh-k">Ön değerlendirme</p>
            <div class="gh-scale" aria-hidden="true"><div class="gh-bar">{zones}</div><i class="gh-pin" id="gh-pin"></i></div>
{heads}
{msgs}
            <p class="gh-flag" id="gh-flag" hidden>Her gece uykunuzu bölen ağrıyı ayrıca bir hekime göstermenizi öneririm.</p>
            <div class="gh-top" id="gh-topw" hidden><p class="gh-k">En çok zorlandığınız anlar</p><ul id="gh-top"></ul></div>
            <p class="gh-meta">Puan <b id="gh-score">0</b> / {MAX} · <span id="gh-agel"></span> yaş grubu</p>
            <div class="gh-acts"><a class="cta" href="#tanisma">Sonucumu birlikte yorumlayalım</a><button type="button" class="cta ghost" id="gh-again">Yeniden başla</button></div>
          </div>
          <div class="gh-nav"><button type="button" class="gh-back" id="gh-back" hidden>{BACK}Geri</button><span class="gh-n" id="gh-n" aria-hidden="true"></span></div>
        </div>
      </div>
      <p class="dm-safe">WOMAC ve Oswestry gibi bilimsel ölçeklerden esinlenerek hazırladığım bir ön değerlendirmedir; tanı koymaz. Şiddetli ya da giderek artan ağrı, ateş, açıklanamayan kilo kaybı, bacaklarda güçsüzlük ya da idrar veya bağırsak kontrolünde değişiklik varsa önce bir hekime başvurun.</p>
    </div>
  </section>

'''
rep('  <section id="tanisma" class="book-sec">', SEC + '  <section id="tanisma" class="book-sec">')

CSS = r'''  /* günlük hareket skalası */
  .day-sec{background:linear-gradient(180deg,rgba(226,171,71,.05),transparent 35%,transparent 65%,rgba(143,164,118,.05)),var(--ground)}
  .gh{max-width:760px}
  @media (min-width:1000px){
    .day-sec .wrap{display:grid;grid-template-columns:minmax(0,.78fr) minmax(0,1.22fr);grid-template-areas:"head gh" "safe gh";column-gap:52px;align-items:start}
    .day-sec .sec-head{grid-area:head;margin-bottom:0;padding-top:34px}
    .day-sec .gh{grid-area:gh;max-width:none}
    .day-sec .dm-safe{grid-area:safe;align-self:end;margin:18px 0 0}
  }
  .dm-bar{display:flex;align-items:center;gap:12px;margin:0 0 16px}
  .dm-bar > svg{flex:none;width:24px;height:24px;fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
  .dm-bar > svg:first-child{stroke:var(--gold);filter:drop-shadow(0 0 6px rgba(226,171,71,.6))}
  .dm-bar > svg:last-child{stroke:var(--sage)}
  .dm-line{position:relative;flex:1;height:14px;display:flex;justify-content:space-between;align-items:center}
  .dm-line::before{content:"";position:absolute;left:0;right:0;top:50%;height:2px;translate:0 -50%;border-radius:2px;background:linear-gradient(90deg,var(--gold),var(--foil) 30%,var(--sage) 70%,#4c5d45);opacity:.6}
  .dm-line i{position:relative;width:12px;height:12px;border-radius:50%;background:var(--ground);border:2px solid rgba(236,229,207,.28);transition:background .4s,border-color .4s,box-shadow .4s,transform .4s}
  .dm-line i.cur{border-color:var(--ink);transform:scale(1.25)}
  .dm-line i.s0{background:#8fa476;border-color:#a9bf8c}
  .dm-line i.s1{background:#e2c35a;border-color:#efd27a}
  .dm-line i.s2{background:#e08c3c;border-color:#f0a45a;box-shadow:0 0 10px rgba(224,140,60,.6)}
  .dm-line i.s3{background:#cf5f4b;border-color:#e57b66;box-shadow:0 0 12px rgba(207,95,75,.7)}
  .gh-card{position:relative;border:1px solid var(--line-strong);border-radius:18px;padding:clamp(18px,3.6vw,28px);
    background:radial-gradient(110% 80% at 0% 0%,rgba(226,171,71,.09),transparent 60%),var(--ground-2);box-shadow:0 18px 50px rgba(0,0,0,.26)}
  .gh-step{display:none}
  .gh-step.on{display:grid;gap:14px;animation:gh-in .45s cubic-bezier(.2,.7,.2,1)}
  @keyframes gh-in{from{opacity:0;transform:translateX(14px)}}
  .gh-step:focus{outline:none}
  .dm-h{display:flex;align-items:center;gap:10px}
  .dm-ic{flex:none;width:36px;height:36px;padding:7px;border-radius:50%;background:rgba(226,171,71,.12);fill:none;stroke:var(--foil);stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
  .dm-t{font-family:var(--display);font-weight:400;font-size:20px;color:var(--gold);font-variant-numeric:tabular-nums}
  .dm-w{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);font-weight:600}
  .gh-q{margin:0;font-family:var(--display);font-size:clamp(23px,3.6vw,30px);line-height:1.25;color:var(--ink);text-wrap:balance}
  .gh-opts{display:grid;grid-template-columns:minmax(0,1fr);gap:8px}
  @media (min-width:560px){.gh-opts{grid-template-columns:repeat(2,minmax(0,1fr))}}
  .gh-age{grid-template-columns:repeat(auto-fill,minmax(92px,1fr))!important}
  .gh-o{all:unset;box-sizing:border-box;cursor:pointer;padding:13px 16px;border-radius:12px;border:1px solid var(--line);background:rgba(236,229,207,.03);color:var(--ink);font-size:15.5px;line-height:1.3;text-align:left;transition:border-color .2s,background .2s,box-shadow .25s,transform .15s}
  .gh-age .gh-o{text-align:center;font-variant-numeric:tabular-nums}
  .gh-o:hover{border-color:var(--line-strong);background:rgba(216,178,94,.06)}
  .gh-o:active{transform:scale(.98)}
  .gh-o:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .gh-o[aria-pressed="true"]{border-color:var(--foil);background:rgba(216,178,94,.14);box-shadow:0 0 0 1px var(--foil),0 0 18px rgba(226,171,71,.2)}
  .gh-nav{display:flex;align-items:center;justify-content:space-between;margin-top:16px;min-height:36px}
  .gh-back[hidden]{display:none!important}
  .gh-back{all:unset;cursor:pointer;display:inline-flex;align-items:center;gap:6px;color:var(--muted);font-size:14px;padding:6px 10px 6px 4px;border-radius:8px}
  .gh-back:hover{color:var(--foil)} .gh-back:focus-visible{outline:2px solid var(--gold)}
  .gh-back svg{width:16px;height:16px}
  .gh-n{margin-left:auto;font-size:13px;color:var(--muted);font-variant-numeric:tabular-nums}
  .gh .gh-k{margin:0;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--foil);font-weight:600}
  .gh-scale{position:relative;padding-top:14px}
  .gh-bar{display:grid;grid-template-columns:repeat(4,1fr);gap:3px}
  .gh-bar .z{display:block;padding:9px 0 0;border-top:8px solid;font-size:12px;letter-spacing:.08em;text-transform:uppercase;font-weight:600;text-align:center;color:var(--muted)}
  .gh-bar .z.g{border-color:#8fa476;border-radius:4px 0 0 4px} .gh-bar .z.y{border-color:#e2c35a} .gh-bar .z.o{border-color:#e08c3c} .gh-bar .z.r{border-color:#cf5f4b;border-radius:0 4px 4px 0}
  .gh-pin{position:absolute;top:0;left:0;width:18px;height:18px;margin-left:-9px;border-radius:50%;background:#fff6dc;border:3px solid var(--ground);box-shadow:0 0 0 2px var(--gold),0 0 16px rgba(255,220,140,.9);transition:left 1.2s cubic-bezier(.3,.8,.2,1)}
  .gh-title{margin:6px 0 0;font-size:clamp(24px,3.8vw,32px);line-height:1.2;color:var(--ink)}
  .gh-band{display:block;font-family:var(--body);font-size:13px;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin-bottom:4px}
  .gh-band.g{color:#a9bf8c} .gh-band.y{color:#efd27a} .gh-band.o{color:#f0a45a} .gh-band.r{color:#ef8a73}
  .gh-msg{margin:0;color:var(--ink-soft);max-width:60ch}
  .gh-flag{margin:0;padding:10px 12px;border-radius:10px;border:1px solid rgba(207,95,75,.6);background:rgba(207,95,75,.08);color:var(--ink);font-size:14.5px}
  .gh-top ul{list-style:none;margin:8px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:8px}
  .gh-top a{display:inline-flex;align-items:center;padding:7px 13px;border-radius:999px;border:1px solid var(--line-strong);color:var(--ink);text-decoration:none;font-size:14px}
  .gh-top a:hover{border-color:var(--foil);color:var(--foil)}
  .gh-top a::before{content:"";width:8px;height:8px;border-radius:50%;margin-right:8px;background:var(--c,#e08c3c)}
  .gh-meta{margin:0;font-size:13px;color:var(--muted)}
  .gh-meta b{color:var(--gold);font-weight:600}
  .gh-acts{display:flex;flex-wrap:wrap;gap:10px}
  .gh-acts button.cta{font:inherit;font-weight:600;font-size:15px;cursor:pointer}
  .dm-safe{margin:14px 0 0;font-size:13px;color:var(--muted);max-width:80ch}
  #bir-gun:not(.js) .gh{display:none}
'''
rep("  /* tanışma görüşmesi */", CSS + "  /* tanışma görüşmesi */")

JS = r'''<script>
(function(){
  var sec = document.getElementById('bir-gun'); if (!sec) return;
  sec.classList.add('js');
  var steps = [].slice.call(sec.querySelectorAll('.gh-step')), qs = steps.filter(function(x){ return /^\d+$/.test(x.getAttribute('data-s')); });
  var dots = [].slice.call(sec.querySelectorAll('.dm-line i')), N = qs.length, MAX = N * 3;
  var back = document.getElementById('gh-back'), num = document.getElementById('gh-n'), res = steps[steps.length - 1];
  // yaş grubuna göre bölge sınırları (yeşil / sarı / turuncu üst sınırları)
  var TH = [[2, 6, 11], [3, 7, 12], [4, 9, 14], [5, 10, 15], [6, 11, 16]];
  var age = null, ans = [], cur = 0;
  function score(i){
    var v = ans[i]; if (v == null) return null;
    var adj = qs[i].getAttribute('data-adj');
    return (adj !== null && age >= +adj) ? Math.max(0, v - 1) : v;
  }
  function paint(){
    dots.forEach(function(d, i){ var sc = score(i); d.className = (sc == null ? '' : 's' + sc) + (cur === i + 1 ? ' cur' : ''); });
  }
  function show(k, init){  // k: 0 = yaş, 1..N = sorular, N+1 = sonuç
    cur = k;
    steps.forEach(function(st, i){ st.classList.toggle('on', i === k); });
    back.hidden = k === 0;
    num.textContent = k >= 1 && k <= N ? k + ' / ' + N : '';
    paint();
    var box = sec.querySelector('.gh-card').getBoundingClientRect();
    if (!init && box.top < 0) sec.querySelector('.gh').scrollIntoView({behavior: 'smooth', block: 'start'});
    if (k === N + 1) { result(); res.focus({preventScroll: true}); }
    else { var b = steps[k].querySelector('.gh-o[aria-pressed="true"]') || steps[k].querySelector('.gh-o'); if (k > 0 || age !== null) b.focus({preventScroll: true}); }
  }
  steps.forEach(function(st, k){
    [].forEach.call(st.querySelectorAll('.gh-o'), function(b){
      b.setAttribute('aria-pressed', 'false');
      b.addEventListener('click', function(){
        [].forEach.call(st.querySelectorAll('.gh-o'), function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        var v = +b.getAttribute('data-v');
        if (k === 0) age = v; else ans[k - 1] = v;
        paint();
        setTimeout(function(){ show(k + 1); }, 260);
      });
    });
  });
  back.addEventListener('click', function(){ if (cur > 0) show(cur - 1); });
  document.getElementById('gh-again').addEventListener('click', function(){
    age = null; ans = [];
    [].forEach.call(sec.querySelectorAll('.gh-o'), function(x){ x.setAttribute('aria-pressed', 'false'); });
    window.drSkala = null; try { document.dispatchEvent(new CustomEvent('dr-skala')); } catch (e) {}
    show(0); steps[0].querySelector('.gh-o').focus({preventScroll: true});
  });
  function result(){
    var tot = 0, n3 = 0, items = [];
    for (var i = 0; i < N; i++) { var sc = score(i) || 0; tot += sc; if (ans[i] === 3) n3++; if (sc >= 2) items.push([sc, i]); }
    var t = TH[age || 0], band = tot <= t[0] ? 0 : tot <= t[1] ? 1 : tot <= t[2] ? 2 : 3;
    if (n3 >= 1 && band < 1) band = 1;
    if (n3 >= 2 && band < 2) band = 2;
    var B = ['g', 'y', 'o', 'r'], lo = [0, t[0], t[1], t[2]], hi = [t[0], t[1], t[2], MAX];
    var f = band === 0 ? (t[0] ? tot / t[0] : 0) : (tot - lo[band]) / Math.max(1, hi[band] - lo[band]);
    f = Math.max(.08, Math.min(.92, f));
    var pin = document.getElementById('gh-pin'); pin.style.left = '0%';
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ pin.style.left = ((band + f) * 25) + '%'; }); });
    [].forEach.call(res.querySelectorAll('[data-b]'), function(el){ el.hidden = el.getAttribute('data-b') !== B[band]; });
    document.getElementById('gh-flag').hidden = ans[N - 1] !== 3;
    document.getElementById('gh-score').textContent = tot;
    document.getElementById('gh-agel').textContent = steps[0].querySelectorAll('.gh-o')[age || 0].textContent;
    items.sort(function(a, b){ return b[0] - a[0] || a[1] - b[1]; });
    var top = items.slice(0, 3), ul = document.getElementById('gh-top'), C = ['', '', '#e08c3c', '#cf5f4b'], names = [];
    ul.innerHTML = '';
    top.forEach(function(x){
      var q = qs[x[1]], li = document.createElement('li'), a = document.createElement('a');
      a.href = q.getAttribute('data-href'); a.textContent = q.querySelector('.dm-s').textContent.trim(); a.style.setProperty('--c', C[x[0]]);
      names.push(a.textContent); li.appendChild(a); ul.appendChild(li);
    });
    document.getElementById('gh-topw').hidden = !top.length;
    var zones = sec.querySelectorAll('.gh-bar .z');
    window.drSkala = {band: zones[band].textContent.trim(), score: tot, max: MAX, top: names};
    try { document.dispatchEvent(new CustomEvent('dr-skala')); } catch (e) {}
  }
  show(0, true);
})();
</script>
'''
anchor = "<script>\n(function(){\n  var card = document.getElementById('book'); if (!card) return;"
assert s.count(anchor) == 1
s = s.replace(anchor, JS + anchor, 1)
open(p, "w", encoding="utf-8").write(s)
print("ok")

# -*- coding: utf-8 -*-
# Kendine iyi bak, 6. tur: yürüme hızı testi, ağrı günlüğü. self5_part.py'den sonra exec edilir
# (SELF5_CSS, WAKE_JS, cs_sts, cs_heel hazır).

SELF6_CSS = SELF5_CSS + """
  /* yürüme hızı */
  .yh-time{text-align:center;margin:6px 0 0}
  .yh-time b{display:block;font-family:var(--display);font-weight:400;font-size:clamp(64px,13vw,96px);line-height:1;color:var(--ink);font-variant-numeric:tabular-nums}
  .yh-time span{font-size:13px;color:var(--ink-soft)}
  .yh-big{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;margin:4px 0 2px}
  .yh-big b{font-family:var(--display);font-weight:400;font-size:clamp(36px,6vw,48px);color:var(--foil);line-height:1}
  .yh-big span{font-size:14px;color:var(--ink-soft)}
  /* ağrı günlüğü */
  .ag{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:clamp(16px,3vw,32px);align-items:start}
  @media (max-width:820px){.ag{grid-template-columns:1fr}}
  .ag-form label.lbl{display:block}
  .ag-date{all:unset;box-sizing:border-box;padding:9px 14px;border-radius:12px;border:1px solid var(--line-strong);font-size:16px;color:var(--ink);background:rgba(236,229,207,.04);color-scheme:dark}
  .ag-pain{display:flex;align-items:center;gap:14px;margin:6px 0 2px}
  .ag-pain output{flex:none;width:58px;height:58px;border-radius:50%;display:grid;place-content:center;font-family:var(--display);font-size:30px;color:var(--ground);background:var(--sage)}
  .ag-pain input{flex:1;accent-color:var(--foil);height:34px}
  .ag-scale{display:flex;justify-content:space-between;font-size:12px;color:var(--muted);margin:0 0 4px 72px}
  .ag-note{all:unset;box-sizing:border-box;width:100%;padding:10px 14px;border-radius:12px;border:1px solid var(--line-strong);font-size:15px;color:var(--ink);background:rgba(236,229,207,.04)}
  .ag-note:focus-visible,.ag-date:focus-visible{outline:2px solid var(--foil);outline-offset:2px}
  .ag-saved{font-size:14px;color:var(--sage);min-height:1.4em;margin-top:8px}
  .ag-sum{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-bottom:14px}
  .ag-sum div{border:1px solid var(--line);border-radius:12px;padding:10px 8px;text-align:center;font-size:12.5px;color:var(--muted)}
  .ag-sum b{display:block;font-family:var(--display);font-weight:400;font-size:26px;color:var(--ink);font-variant-numeric:tabular-nums}
  .ag-chart{width:100%;height:auto;display:block;border:1px solid var(--line);border-radius:14px;background:rgba(236,229,207,.03)}
  .ag-chart .gl{stroke:rgba(236,229,207,.08);stroke-width:1}
  .ag-chart .ln{fill:none;stroke:var(--foil);stroke-width:2.5;stroke-linejoin:round;stroke-linecap:round}
  .ag-chart .dt{fill:var(--foil)}
  .ag-chart text{fill:var(--muted);font-size:11px;font-family:inherit}
  .ag-insight{font-size:14.5px;color:var(--ink-soft);margin:12px 0 0;line-height:1.55}
  .ag-list{list-style:none;padding:0;margin:14px 0 0;display:grid;gap:6px}
  .ag-list li{display:grid;grid-template-columns:auto 1fr auto;gap:10px;align-items:center;border-bottom:1px solid var(--line);padding:6px 0;font-size:14px;color:var(--ink-soft)}
  .ag-list li b{width:30px;height:30px;border-radius:50%;display:grid;place-content:center;color:var(--ground);font-weight:700;font-size:14px}
  .ag-list li button{all:unset;cursor:pointer;font-size:12.5px;color:var(--muted);padding:4px 8px;border-radius:8px}
  .ag-list li button:hover,.ag-list li button:focus-visible{color:var(--ink);outline:1px solid var(--line-strong)}
  .ag-empty{font-size:14.5px;color:var(--muted);margin:10px 0}
"""

# ------------------------------------------------------------------ 1 · YÜRÜME HIZI TESTİ
# Bohannon ve Andrews 2011, ortalama yürüme hızı (m/sn): [erkek, kadın]
YH_NORM = [("20–29", 1.36, 1.34), ("30–39", 1.43, 1.34), ("40–49", 1.43, 1.39), ("50–59", 1.43, 1.31), ("60–69", 1.34, 1.24), ("70–79", 1.26, 1.13), ("80–99", 0.97, 0.94)]
YH_ROWS = "\n".join(f'<tr data-i="{i}"><td>{a}</td><td>{str(w).replace(".", ",")}</td><td>{str(m).replace(".", ",")}</td></tr>' for i, (a, m, w) in enumerate(YH_NORM))

YH_FAQ = [
 ("Neden yürüme hızı önemli?", "Yürümek; kaslarınızı, eklemlerinizi, dengenizi, kalbinizi, akciğerlerinizi ve sinir sisteminizi birlikte kullanmayı gerektirir. Bu yüzden yürüme hızı, yaşlılarda genel sağlığın basit bir göstergesi olarak kullanılıyor. 65 yaş üstü 34.485 kişinin izlendiği dokuz çalışmanın birleştirildiği analizde, daha hızlı yürüyenlerin daha uzun yaşadığı görüldü. Bu bir ilişkidir; test tek başına bir hastalığı göstermez."),
 ("Hızlı mı yürümeliyim?", "Hayır. Testte her zamanki, rahat temponuzla yürüyün. Amaç günlük yürüyüşünüzü ölçmektir; yarışmayın."),
 ("Baston ya da yürüteçle yapabilir miyim?", "Evet. Günlük hayatta kullandığınız baston ya da yürüme yardımcısıyla yapabilirsiniz. Karşılaştırma için her seferinde aynı şekilde yapmanız yeterli."),
 ("Hızım düşük çıktı, ne yapmalıyım?", "Bu bir tanı değildir. Bacak gücü, denge ve düzenli yürüyüş yürüme hızını destekler; aşağıdaki egzersizlerle başlayabilirsiniz. Son zamanlarda yürüyüşünüz belirgin yavaşladıysa, sık düşüyorsanız ya da nefes darlığı ve göğüs ağrısı gibi yakınmalarınız varsa bir hekime görünün."),
]

YH_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Yürüme hızı testi</h1>
    <p class="lede">Her zamanki temponuzla 4 metreyi kaç saniyede yürüyorsunuz? Yürüme hızı, yaşlılarda genel sağlığın basit bir göstergesi olarak kullanılıyor: 65 yaş üstü 34.485 kişinin verilerinin birleştirildiği bir analizde, daha hızlı yürüyenlerin daha uzun yaşadığı görüldü. Bu bir tanı değil, ama izlemeye değer bir ölçü. Aşağıdaki süreölçerle ölçün ve yaşınızdaki ortalamayla karşılaştırın.</p>
    <p class="meta">Son güncelleme: 16 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>4 metre</b><span>Testin mesafesi; yeriniz darsa 3 metre de kullanılabilir</span></div>
        <div class="stat"><b>%12</b><span>Her 0,1 m/sn daha hızlı yürüyüşle ilişkili ölüm riski azalması (65 yaş üstü)</span></div>
        <div class="stat"><b>1,0 m/sn</b><span>Bu hız ve üzeri, beklenenden daha uzun yaşamla ilişkiliydi</span></div>
        <div class="stat"><b>0,8 m/sn</b><span>Yaklaşık olarak ortalama yaşam beklentisine karşılık gelen hız</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Kendinizi ölçün</p>
      <h2>Süreölçerle ölçün</h2>
      <p class="soft">Yerde başlangıç ve bitiş çizgilerini işaretleyin. Süreyi yanınızdaki biri tutsun: “Başla” dediği anda süreölçeri başlatsın, bir ayağınız bitiş çizgisini tamamen geçince durdursun. İki deneme yapın; hızlı olanı sonucunuzdur.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <p class="lbl">Mesafe</p>
            <div class="seg" role="group" aria-label="Mesafe" id="yh-dist">
              <button type="button" data-v="3" aria-pressed="false">3 metre</button>
              <button type="button" data-v="4" aria-pressed="true">4 metre</button>
              <button type="button" data-v="5" aria-pressed="false">5 metre</button>
            </div>
            <p class="lbl">Cinsiyet</p>
            <div class="seg" role="group" aria-label="Cinsiyet" id="yh-sex">
              <button type="button" data-v="f" aria-pressed="true">Kadın</button>
              <button type="button" data-v="m" aria-pressed="false">Erkek</button>
            </div>
            <p class="lbl"><label for="yh-age">Yaşınız</label></p>
            <input class="cs-age" id="yh-age" type="number" inputmode="numeric" min="18" max="110" placeholder="ör. 70">
          </div>
          <div class="bt-out">
            <div class="trials" id="yh-trials" style="grid-template-columns:repeat(2,minmax(0,1fr))"><div><span>1. deneme</span><b>–</b></div><div><span>2. deneme</span><b>–</b></div></div>
            <div class="res" id="yh-res" hidden>
              <p class="lab" id="yh-lab"></p>
              <div class="yh-big"><b id="yh-speed"></b><span id="yh-kmh"></span></div>
              <p id="yh-txt"></p>
              <span class="bt-badge" id="yh-badge"></span>
              <div class="cs-acts"><a class="cta" id="yh-wa" href="#" target="_blank" rel="noopener">Sonucumu WhatsApp’tan gönder</a></div>
            </div>
            <div id="yh-histw" style="margin-top:20px" hidden>
              <p class="lbl">Önceki sonuçlarınız (bu cihazda)</p>
              <ul class="cs-hist" id="yh-hist"></ul>
            </div>
          </div>
          <div class="bt-run">
            <div class="yh-time"><b id="yh-sec">0,00</b><span>saniye</span></div>
            <p class="bt-phase" id="yh-phase" aria-live="polite">Hazır</p>
            <p class="bt-cue" id="yh-cue">Kişi iki ayağı başlangıç çizgisinde dursun. “Başla” derken süreölçeri başlatın.</p>
            <button type="button" class="bt-tap" id="yh-go">Başla</button>
            <div class="controls" style="margin-top:10px;justify-content:center">
              <button type="button" class="cta ghost" id="yh-reset">Denemeleri sıfırla</button>
            </div>
          </div>
        </div>
        <div class="yh-strings" hidden>
          <span data-k="ready">Hazır</span>
          <span data-k="readyc">Kişi iki ayağı başlangıç çizgisinde dursun. “Başla” derken süreölçeri başlatın.</span>
          <span data-k="run">Yürüyor</span>
          <span data-k="runc">Bir ayak bitiş çizgisini tamamen geçince durdurun.</span>
          <span data-k="start">Başla</span>
          <span data-k="stop">Bitti</span>
          <span data-k="next">2. denemeyi başlat</span>
          <span data-k="saved">1. deneme kaydedildi</span>
          <span data-k="savedc">Başlangıç çizgisine dönün; hazır olunca ikinci denemeyi başlatın.</span>
          <span data-k="done">İki deneme tamamlandı</span>
          <span data-k="donec">Hızlı olan deneme sonucunuzdur; hızınız ve karşılaştırma hazır.</span>
          <span data-k="lab">En iyi süreniz: {{s}} saniye ({{d}} metre)</span>
          <span data-k="kmh">yaklaşık {{k}} km/sa</span>
          <span data-k="ms">m/sn</span>
          <span data-k="noage">Karşılaştırma için yaşınızı girin.</span>
          <span data-k="outage">Bu yaş için güvenilir bir karşılaştırma değeri yok.</span>
          <span data-k="avg">Yaş grubunuzun ortalaması {{m}} m/sn.</span>
          <span data-k="hi">1,0 m/sn ve üzeri, 65 yaş üstü kişilerde beklenenden daha uzun yaşamla ilişkiliydi.</span>
          <span data-k="mid">0,8 m/sn civarı, 65 yaş üstü kişilerde yaklaşık ortalama yaşam beklentisine karşılık geliyordu; 1,0 m/sn ve üzeri daha uzun yaşamla ilişkiliydi.</span>
          <span data-k="lo">0,8 m/sn’nin altındaki hızlar, 65 yaş üstü kişilerde daha kısa yaşam beklentisiyle ilişkiliydi. Bu bir tanı değildir; güç, denge ve yürüyüş çalışmalarıyla başlayabilir, bir hekim ya da fizyoterapistle konuşabilirsiniz.</span>
          <span data-k="bok">Ortalamanın üzerinde ya da yakınında</span>
          <span data-k="blow">Ortalamanın altında</span>
          <span data-k="wa">Merhaba, drihsaneren.com’daki yürüme hızı testini yaptım: {{v}} m/sn ({{d}} metre, {{s}} saniye). Değerlendirme hakkında bilgi almak istiyorum.</span>
          <span data-k="sec">saniye</span>
        </div>
      </div>
      <p class="count">Sonuçlarınız yalnızca bu cihazda saklanır; hiçbir yere gönderilmez.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nasıl yapılır?</h2>
        <ol class="steps">
          <li><span>Düz ve boş bir zeminde <strong>4 metreyi</strong> (yer darsa 3 metreyi) ölçün; başlangıç ve bitiş çizgilerini bantla işaretleyin.</span></li>
          <li><span>Kişi <strong>iki ayağı başlangıç çizgisinde</strong> dursun. Bitiş çizgisinden sonra da birkaç adım yürüyebileceği boş alan olsun.</span></li>
          <li><span>“Başla” deyin ve süreölçeri başlatın. Kişi <strong>her zamanki temposuyla</strong> bitiş çizgisini geçene kadar yürüsün.</span></li>
          <li><span>Bir ayak bitiş çizgisini <strong>tamamen geçtiği anda</strong> durdurun. İki deneme yapın; hızlı olanı sayılır.</span></li>
        </ol>
      </div>
      <div>
        <h2>Güvenle yapmak için</h2>
        <ul class="dots">
          <li>Halı kenarı, kablo gibi takılabileceğiniz şeyleri yoldan kaldırın; rahat ve kaymayan ayakkabı giyin.</li>
          <li>Günlük hayatta baston ya da yürüteç kullanıyorsanız testi onunla yapın.</li>
          <li>Dengeniz zayıfsa ya da yakın zamanda düştüyseniz yanınızda biri yürüsün.</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="normlar">
    <div class="wrap">
      <p class="eyebrow">Karşılaştırma</p>
      <h2>Yaşa göre ortalama yürüme hızı</h2>
      <p class="soft">Sağlıklı yetişkinlerde yapılan çalışmaların birleştirildiği bir analizden ortalama değerler (metre/saniye). Yaş grubunuz yukarıdaki yaşa göre işaretlenir.</p>
      <table class="nt" id="yh-nt">
        <thead><tr><th>Yaş</th><th>Kadın</th><th>Erkek</th></tr></thead>
        <tbody>
{YH_ROWS}
        </tbody>
      </table>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Yürüyüşünüzü destekleyin</p>
      <h2>Evde dört egzersiz</h2>
      <p class="soft">Güçlü bacaklar ve iyi bir denge, rahat ve güvenli yürüyüşün temelidir. Bacak gücünüz için <a href="sandalye-testi.html">30 saniye sandalye testine</a>, dengeniz için <a href="denge-testi.html">10 saniye denge testine</a> de bakabilirsiniz.</p>
      {ex_grid(["walk", "cs_sts", "cs_heel", "tandem"], "ex four")}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(YH_FAQ)}
      {CTA_CARD("Yürüyüşünüz ve dengeniz", "yürüme ve denge değerlendirmesi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Studenski S, Perera S, Patel K, et al. " + ext("https://immattersacp.org/weekly/archives/2011/01/11/4.htm", "Gait speed and survival in older adults") + ". JAMA. 2011;305:50–58.",
        "Bohannon RW, Andrews AW. " + ext("https://www.physicaltherapy.utoronto.ca/sites/default/files/assets/files/11walking-speed-age-and-sex-specific-normative-values-final.pdf", "Normal walking speed: a descriptive meta-analysis") + ". Physiotherapy. 2011;97:182–189.",
        "Harvard eFrailty. " + ext("https://efrailty.hsl.harvard.edu/ToolSPPB.html", "Short Physical Performance Battery (SPPB)") + ": gait speed test instructions.",
      ])}
    </div>
  </section>
</main>'''

YH_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.yh-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var EN = document.documentElement.lang === 'en';
  var $ = function(id){ return document.getElementById(id); };
  var NORM = [[1.36, 1.34], [1.43, 1.34], [1.43, 1.39], [1.43, 1.31], [1.34, 1.24], [1.26, 1.13], [0.97, 0.94]];
  var KEY = 'drihsaneren.yuruyus.v1', WA = 'https://wa.me/905538815568?text=';
  var dist = 4, sex = 'f', trials = [], phase = 'idle', t0 = 0, iv = null, snd = null, ctx = null, lock = null;
''' + WAKE_JS + '''
  function fmt(x, d){ var s = x.toFixed(d); return EN ? s : s.replace('.', ','); }
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function age(){ var a = parseInt($('yh-age').value, 10); return isNaN(a) ? null : a; }
  function band(a){ if (a == null || a < 20) return -1; if (a >= 80) return a <= 99 ? 6 : -1; return Math.floor(a / 10) - 2; }
  function store(){ try { return JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { return []; } }
  function save(l){ try { localStorage.setItem(KEY, JSON.stringify(l.slice(-10))); } catch (e) {} }
  function paintNorm(){ var b = band(age()); $('yh-nt').querySelectorAll('tbody tr').forEach(function(r){ r.classList.toggle('me', +r.getAttribute('data-i') === b); }); }
  function paintTrials(){
    var best = trials.length ? Math.min.apply(null, trials) : null;
    $('yh-trials').querySelectorAll('div').forEach(function(d, j){
      d.querySelector('b').textContent = j < trials.length ? fmt(trials[j], 2) : '–';
      d.classList.toggle('best', j < trials.length && trials[j] === best);
    });
    var res = $('yh-res'); if (best == null){ res.hidden = true; return; }
    res.hidden = false;
    var v = dist / best, a = age(), b = band(a);
    $('yh-lab').textContent = fill(S.lab, {s: fmt(best, 2), d: dist});
    $('yh-speed').textContent = fmt(v, 2) + ' ' + S.ms;
    $('yh-kmh').textContent = fill(S.kmh, {k: fmt(v * 3.6, 1)});
    var txt = '', badge = $('yh-badge');
    if (a == null){ txt = S.noage; badge.hidden = true; }
    else if (b < 0){ txt = S.outage; badge.hidden = true; }
    else {
      var m = NORM[b][sex === 'm' ? 0 : 1], ok = v >= m * 0.9;
      txt = fill(S.avg, {m: fmt(m, 2)});
      badge.hidden = false; badge.textContent = ok ? S.bok : S.blow; badge.classList.toggle('no', !ok);
    }
    if (a != null && a >= 65) txt += ' ' + (v >= 1.0 ? S.hi : v >= 0.8 ? S.mid : S.lo);
    $('yh-txt').textContent = txt;
    $('yh-wa').href = WA + encodeURIComponent(fill(S.wa, {v: fmt(v, 2), d: dist, s: fmt(best, 2)}));
  }
  function paintHist(){
    var h = store(), ul = $('yh-hist'); $('yh-histw').hidden = !h.length; ul.innerHTML = '';
    h.slice().reverse().forEach(function(r){
      var li = document.createElement('li'), sp = document.createElement('span'), bb = document.createElement('b');
      sp.textContent = new Date(r.t).toLocaleDateString(EN ? 'en-GB' : 'tr-TR', {day: 'numeric', month: 'short', year: 'numeric'}) + ' · ' + r.d + ' m';
      bb.textContent = fmt(r.v, 2) + ' ' + S.ms; li.appendChild(sp); li.appendChild(bb); ul.appendChild(li);
    });
  }
  function idle(p, c){
    phase = 'idle'; clearInterval(iv); iv = null; wake(false);
    $('yh-go').textContent = trials.length === 1 ? S.next : S.start; $('yh-go').classList.remove('stop');
    $('yh-phase').textContent = p || S.ready; $('yh-cue').textContent = c || S.readyc;
  }
  function start(){
    if (trials.length >= 2){ trials = []; paintTrials(); }
    phase = 'run'; t0 = performance.now(); wake(true);
    $('yh-go').textContent = S.stop; $('yh-go').classList.add('stop');
    $('yh-phase').textContent = S.run; $('yh-cue').textContent = S.runc;
    clearInterval(iv); iv = setInterval(function(){ $('yh-sec').textContent = fmt((performance.now() - t0) / 1000, 2); }, 31);
  }
  function stop(){
    var x = (performance.now() - t0) / 1000; clearInterval(iv); iv = null;
    if (x < 0.8){ $('yh-sec').textContent = fmt(0, 2); idle(); return; }
    trials.push(Math.round(x * 100) / 100); $('yh-sec').textContent = fmt(x, 2); paintTrials();
    if (trials.length >= 2){
      var best = Math.min.apply(null, trials), h = store(); h.push({t: new Date().toISOString(), v: dist / best, d: dist}); save(h); paintHist();
      idle(S.done, S.donec);
    } else idle(S.saved, S.savedc);
  }
  function press(){ if (phase === 'idle') start(); else stop(); }
  $('yh-go').addEventListener('click', press);
  document.addEventListener('keydown', function(e){ if (phase === 'run' && (e.code === 'Space' || e.key === ' ')){ e.preventDefault(); stop(); } });
  $('yh-reset').addEventListener('click', function(){ trials = []; paintTrials(); $('yh-sec').textContent = fmt(0, 2); idle(); });
  function seg(id, fn){ $(id).addEventListener('click', function(e){ var b = e.target.closest('button'); if (!b) return; this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); fn(b.getAttribute('data-v')); }); }
  seg('yh-dist', function(v){ dist = +v; if (phase !== 'idle') idle(); trials = []; paintTrials(); $('yh-sec').textContent = fmt(0, 2); });
  seg('yh-sex', function(v){ sex = v; paintTrials(); });
  $('yh-age').addEventListener('input', function(){ paintNorm(); paintTrials(); });
  if (EN) $('yh-nt').querySelectorAll('td').forEach(function(td){ td.textContent = td.textContent.replace(/(\\d),(\\d)/g, '$1.$2'); });
  $('yh-sec').textContent = fmt(0, 2); paintNorm(); paintHist(); idle();
})();
</script>
'''

page("yurume-hizi-testi.html", "Yürüme Hızı Testi",
     "Her zamanki temponuzla 4 metreyi kaç saniyede yürüyorsunuz? Süreölçerle yürüme hızınızı ölçün, yaşınızdaki ortalamayla karşılaştırın ve yürüyüşünüzü destekleyen dört egzersizi öğrenin.",
     "yurume-hizi-testi.html", SELF6_CSS, YH_BODY, YH_JS,
     seo_title="Yürüme Hızı Testi: 4 Metre Süreölçer ve Yaşa Göre Ortalamalar | İhsan Eren",
     about={"@type": "MedicalTest", "name": "Yürüme hızı testi"},
     faq_items=YH_FAQ)

# ------------------------------------------------------------------ 2 · AĞRI GÜNLÜĞÜ
AG_PLACES = ["Bel", "Boyun", "Omuz", "Diz", "Kalça", "Baş", "Diğer"]
AG_PLACEH = "".join(f'<button type="button" data-v="{i}" aria-pressed="false">{p}</button>' for i, p in enumerate(AG_PLACES))

AG_FAQ = [
 ("Günlüğü ne sıklıkla doldurmalıyım?", "Günde bir kez, her gün yaklaşık aynı saatte doldurmanız karşılaştırmayı kolaylaştırır. Bir günü atlamanız sorun değil; aynı güne yeniden kayıt yaparsanız o günün kaydı güncellenir."),
 ("Verilerim nerede saklanıyor?", "Yalnızca bu cihazda, tarayıcınızın içinde saklanır; hiçbir sunucuya gönderilmez. Tarayıcı verilerini silerseniz ya da başka bir cihaz kullanırsanız kayıtlar görünmez. Kayıtlarınızı CSV dosyası olarak indirip saklayabilirsiniz."),
 ("Ağrım ne kadar azalırsa anlamlı bir iyileşmedir?", "Uzun süreli ağrısı olan 2.724 kişinin verileriyle yapılan bir çalışmada, 0–10 ölçeğinde ortalama 2 puanlık ya da yaklaşık %30’luk bir azalma, kişilerin kendilerini anlamlı ölçüde daha iyi hissetmelerine karşılık geliyordu. Bu bir ortalama; sizin için önemli olan, günlük hayatınızda neyin değiştiğidir."),
 ("Ağrım artarsa ne yapmalıyım?", "Ağrınız yeni başladıysa, giderek kötüleşiyorsa ya da başka yakınmalar eşlik ediyorsa bir hekime görünün. Bilgi köşesindeki rehberlerde her durum için ne zaman beklemeden başvurmanız gerektiğini bulabilirsiniz."),
]

AG_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Ağrı günlüğü</h1>
    <p class="lede">Ağrınız iyi günlerde ve kötü günlerde nasıl değişiyor? Her gün bir dakikanızı ayırıp ağrınızı, uykunuzu ve ne kadar hareket ettiğinizi kaydedin. Haftalar içinde ağrınızın seyrini bir grafikte görür, hekiminiz ya da fizyoterapistinizle konuşurken somut bir tabloya sahip olursunuz.</p>
    <p class="meta">Son güncelleme: 16 Ekim 2026</p>
  </div>
</header>

<main>
  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Günlüğünüz</p>
      <h2>Bugünü kaydedin</h2>
      <div class="tool">
        <div class="ag">
          <div class="ag-form">
            <label class="lbl" for="ag-date">Tarih</label>
            <input class="ag-date" type="date" id="ag-date">
            <p class="lbl">Ağrınızın şiddeti (0 = ağrı yok, 10 = düşünebileceğiniz en kötü ağrı)</p>
            <div class="ag-pain"><output id="ag-out" for="ag-pain">0</output><input type="range" id="ag-pain" min="0" max="10" step="1" value="0" aria-label="Ağrı şiddeti, 0–10"></div>
            <div class="ag-scale"><span>0</span><span>5</span><span>10</span></div>
            <p class="lbl">Nerede?</p>
            <div class="seg" role="group" aria-label="Ağrının yeri" id="ag-place">{AG_PLACEH}</div>
            <p class="lbl">Dün gece uykunuz</p>
            <div class="seg" role="group" aria-label="Uyku" id="ag-sleep">
              <button type="button" data-v="2" aria-pressed="false">İyi</button>
              <button type="button" data-v="1" aria-pressed="false">Orta</button>
              <button type="button" data-v="0" aria-pressed="false">Kötü</button>
            </div>
            <p class="lbl">Bugün ne kadar hareket ettiniz?</p>
            <div class="seg" role="group" aria-label="Hareket" id="ag-move">
              <button type="button" data-v="0" aria-pressed="false">Az</button>
              <button type="button" data-v="1" aria-pressed="false">Orta</button>
              <button type="button" data-v="2" aria-pressed="false">Çok</button>
            </div>
            <label class="lbl" for="ag-note">Not (isteğe bağlı)</label>
            <input class="ag-note" id="ag-note" maxlength="120" placeholder="ör. uzun süre oturdum, egzersiz yaptım">
            <div class="controls" style="margin-top:14px"><button type="button" class="cta" id="ag-save">Kaydet</button></div>
            <p class="ag-saved" id="ag-saved" aria-live="polite"></p>
          </div>
          <div class="ag-view">
            <div class="ag-sum">
              <div><b id="ag-n">0</b>kayıt</div>
              <div><b id="ag-a7">–</b>son 7 gün ortalaması</div>
              <div><b id="ag-d7">–</b>önceki 7 güne göre</div>
            </div>
            <svg class="ag-chart" id="ag-chart" viewBox="0 0 360 180" role="img" aria-label="Son 30 günün ağrı grafiği"></svg>
            <p class="ag-insight" id="ag-ins"></p>
            <p class="ag-empty" id="ag-empty">Henüz kayıt yok. İlk kaydınızı formdan ekleyin.</p>
            <ul class="ag-list" id="ag-list"></ul>
            <div class="cs-acts">
              <a class="cta" id="ag-wa" href="#" target="_blank" rel="noopener">Özeti WhatsApp’tan gönder</a>
              <button type="button" class="cta ghost" id="ag-csv">CSV olarak indir</button>
              <button type="button" class="cta ghost" id="ag-clear">Tümünü sil</button>
            </div>
          </div>
        </div>
        <div class="ag-strings" hidden>
          <span data-k="saved">Kaydedildi</span>
          <span data-k="updated">Bu günün kaydı güncellendi</span>
          <span data-k="del">Sil</span>
          <span data-k="confirm">Tüm kayıtlar bu cihazdan silinsin mi?</span>
          <span data-k="s0">kötü uyku</span>
          <span data-k="s1">orta uyku</span>
          <span data-k="s2">iyi uyku</span>
          <span data-k="m0">az hareket</span>
          <span data-k="m1">orta hareket</span>
          <span data-k="m2">çok hareket</span>
          <span data-k="sleepins">İyi uyuduğunuz günlerde ağrınız ortalama {{g}}, kötü uyuduğunuz günlerde {{b}} olmuş.</span>
          <span data-k="moveins">Çok hareket ettiğiniz günlerde ağrınız ortalama {{h}}, az hareket ettiğiniz günlerde {{l}} olmuş.</span>
          <span data-k="few">Grafik ve örüntüler, birkaç günlük kayıttan sonra anlam kazanır.</span>
          <span data-k="caution">Bunlar yalnızca sizin kayıtlarınızdan çıkan gözlemler; neden-sonuç ilişkisi göstermez.</span>
          <span data-k="wa">Merhaba, ağrı günlüğümün özeti ({{f}} – {{t}}): {{n}} kayıt, ortalama ağrı {{a}}/10, en düşük {{lo}}, en yüksek {{hi}}. Değerlendirme hakkında bilgi almak istiyorum.</span>
          <span data-k="csvh">tarih;ağrı;yer;uyku;hareket;not</span>
          <span data-k="csvname">agri-gunlugu</span>
        </div>
      </div>
      <p class="count">Kayıtlarınız yalnızca bu cihazda saklanır; hiçbir yere gönderilmez.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Neden günlük tutmalı?</h2>
        <ul class="dots">
          <li>Ağrı gün içinde ve günden güne değişir; hafıza ise çoğu zaman en kötü günleri hatırlar. Kayıtlar size daha dengeli bir tablo gösterir.</li>
          <li>Uykunuz, hareketiniz ve ağrınız arasında size özgü örüntüleri fark etmenizi kolaylaştırır.</li>
          <li>Tedavinizin ya da egzersiz programınızın işe yarayıp yaramadığını konuşurken somut bir dayanak olur.</li>
        </ul>
      </div>
      <div>
        <h2>0–10 ölçeği nasıl kullanılır?</h2>
        <ul class="dots">
          <li>0 hiç ağrı olmadığı, 10 düşünebileceğiniz en kötü ağrı anlamına gelir.</li>
          <li>Günün genel ağrısını düşünün; tek bir anı değil.</li>
          <li>Her gün aynı ölçütü kullanın; sayıların kendisinden çok değişim önemlidir.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(AG_FAQ)}
      <p class="soft" style="margin-top:18px">Ağrının nasıl oluştuğunu <a href="agriyi-anlamak.html">ağrıyı anlamak</a> sayfasında, egzersiz sırasındaki ağrıyı <a href="egzersizde-agri.html">egzersizde ağrı trafik ışığında</a> okuyabilirsiniz.</p>
      {CTA_CARD("Süregelen ağrınız", "ağrı günlüğüm ve ağrı değerlendirmesi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Farrar JT, Young JP Jr, LaMoreaux L, Werth JL, Poole RM. " + ext("https://chiro.org/LINKS/ABSTRACTS/Clinical_Importance_of_Changes.shtml", "Clinical importance of changes in chronic pain intensity measured on an 11-point numerical pain rating scale") + ". Pain. 2001;94(2):149–158.",
      ])}
    </div>
  </section>
</main>'''

AG_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.ag-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var EN = document.documentElement.lang === 'en';
  var $ = function(id){ return document.getElementById(id); };
  var KEY = 'drihsaneren.agri.v1', WA = 'https://wa.me/905538815568?text=';
  var PL = []; $('ag-place').querySelectorAll('button').forEach(function(b){ PL.push(b.textContent); });
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function f1(x){ var s = (Math.round(x * 10) / 10).toFixed(1); return EN ? s : s.replace('.', ','); }
  function load(){ try { var l = JSON.parse(localStorage.getItem(KEY) || '[]'); return Array.isArray(l) ? l : []; } catch (e) { return []; } }
  function store(l){ try { localStorage.setItem(KEY, JSON.stringify(l)); } catch (e) {} }
  function iso(d){ return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2); }
  function dayN(s){ var p = s.split('-'); return Date.UTC(+p[0], +p[1] - 1, +p[2]) / 864e5; }
  function nice(s){ var p = s.split('-'); return new Date(+p[0], +p[1] - 1, +p[2]).toLocaleDateString(EN ? 'en-GB' : 'tr-TR', {day: 'numeric', month: 'short'}); }
  function col(v){ return v <= 3 ? 'var(--sage)' : v <= 6 ? '#e2ab47' : '#c9694f'; }
  function single(id){ $(id).addEventListener('click', function(e){ var b = e.target.closest('button'); if (!b) return; var on = b.getAttribute('aria-pressed') !== 'true'; this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', 'false'); }); b.setAttribute('aria-pressed', on ? 'true' : 'false'); }); }
  function val(id){ var b = $(id).querySelector('[aria-pressed=true]'); return b ? +b.getAttribute('data-v') : null; }
  function setVal(id, v){ $(id).querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', +x.getAttribute('data-v') === v ? 'true' : 'false'); }); }
  single('ag-sleep'); single('ag-move');
  $('ag-place').addEventListener('click', function(e){ var b = e.target.closest('button'); if (b) b.setAttribute('aria-pressed', b.getAttribute('aria-pressed') === 'true' ? 'false' : 'true'); });
  var range = $('ag-pain'), out = $('ag-out');
  function paintOut(){ out.textContent = range.value; out.style.background = col(+range.value); }
  range.addEventListener('input', paintOut);
  function fillForm(d){
    var e = load().filter(function(x){ return x.d === d; })[0];
    range.value = e ? e.p : 0; paintOut();
    $('ag-place').querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', e && e.w && e.w.indexOf(+x.getAttribute('data-v')) >= 0 ? 'true' : 'false'); });
    setVal('ag-sleep', e ? e.s : -1); setVal('ag-move', e ? e.m : -1); $('ag-note').value = e && e.n ? e.n : '';
  }
  $('ag-date').value = iso(new Date()); $('ag-date').max = iso(new Date());
  $('ag-date').addEventListener('change', function(){ if (this.value) fillForm(this.value); $('ag-saved').textContent = ''; });
  $('ag-save').addEventListener('click', function(){
    var d = $('ag-date').value || iso(new Date()), l = load(), had = l.some(function(x){ return x.d === d; });
    var w = []; $('ag-place').querySelectorAll('[aria-pressed=true]').forEach(function(x){ w.push(+x.getAttribute('data-v')); });
    l = l.filter(function(x){ return x.d !== d; });
    l.push({d: d, p: +range.value, w: w, s: val('ag-sleep'), m: val('ag-move'), n: $('ag-note').value.trim().slice(0, 120)});
    l.sort(function(a, b){ return a.d < b.d ? -1 : 1; }); if (l.length > 400) l = l.slice(-400);
    store(l); $('ag-saved').textContent = had ? S.updated : S.saved; paint();
  });
  function avg(a){ return a.length ? a.reduce(function(s, x){ return s + x.p; }, 0) / a.length : null; }
  function chart(l){
    var svg = $('ag-chart'), W = 360, H = 180, L = 26, R = 10, T = 12, B = 26, today = dayN(iso(new Date())), s = '';
    for (var g = 0; g <= 10; g += 5){ var y = T + (H - T - B) * (1 - g / 10); s += '<line class="gl" x1="' + L + '" x2="' + (W - R) + '" y1="' + y + '" y2="' + y + '"/><text x="' + (L - 6) + '" y="' + (y + 4) + '" text-anchor="end">' + g + '</text>'; }
    var pts = l.filter(function(x){ return today - dayN(x.d) < 30 && today - dayN(x.d) >= 0; }).map(function(x){
      var X = L + (W - L - R) * (1 - (today - dayN(x.d)) / 29), Y = T + (H - T - B) * (1 - x.p / 10); return [X, Y, x];
    });
    if (pts.length > 1) s += '<path class="ln" d="M' + pts.map(function(p){ return p[0].toFixed(1) + ' ' + p[1].toFixed(1); }).join(' L') + '"/>';
    pts.forEach(function(p){ s += '<circle class="dt" cx="' + p[0].toFixed(1) + '" cy="' + p[1].toFixed(1) + '" r="3.6" style="fill:' + col(p[2].p) + '"/>'; });
    var d0 = new Date(); d0.setDate(d0.getDate() - 29);
    s += '<text x="' + L + '" y="' + (H - 8) + '">' + nice(iso(d0)) + '</text><text x="' + (W - R) + '" y="' + (H - 8) + '" text-anchor="end">' + nice(iso(new Date())) + '</text>';
    svg.innerHTML = s;
  }
  function paint(){
    var l = load(), today = dayN(iso(new Date()));
    $('ag-n').textContent = String(l.length);
    var w1 = l.filter(function(x){ var k = today - dayN(x.d); return k >= 0 && k < 7; }), w0 = l.filter(function(x){ var k = today - dayN(x.d); return k >= 7 && k < 14; });
    var a1 = avg(w1), a0 = avg(w0);
    $('ag-a7').textContent = a1 == null ? '–' : f1(a1);
    $('ag-d7').textContent = (a1 == null || a0 == null) ? '–' : ((a1 - a0 > 0 ? '+' : '') + f1(a1 - a0));
    chart(l);
    var ins = [];
    if (l.length < 5) ins.push(S.few);
    else {
      var g = l.filter(function(x){ return x.s === 2; }), b = l.filter(function(x){ return x.s === 0; });
      if (g.length >= 3 && b.length >= 3) ins.push(fill(S.sleepins, {g: f1(avg(g)), b: f1(avg(b))}));
      var hm = l.filter(function(x){ return x.m === 2; }), lm = l.filter(function(x){ return x.m === 0; });
      if (hm.length >= 3 && lm.length >= 3) ins.push(fill(S.moveins, {h: f1(avg(hm)), l: f1(avg(lm))}));
      if (ins.length) ins.push(S.caution);
    }
    $('ag-ins').textContent = ins.join(' ');
    var ul = $('ag-list'); ul.innerHTML = ''; $('ag-empty').hidden = l.length > 0;
    l.slice(-14).reverse().forEach(function(x){
      var li = document.createElement('li'), b = document.createElement('b'), sp = document.createElement('span'), del = document.createElement('button');
      b.textContent = String(x.p); b.style.background = col(x.p);
      var bits = [nice(x.d)];
      if (x.w && x.w.length) bits.push(x.w.map(function(i){ return PL[i]; }).join(', '));
      if (x.s != null && x.s >= 0) bits.push(S['s' + x.s]); if (x.m != null && x.m >= 0) bits.push(S['m' + x.m]);
      if (x.n) bits.push('“' + x.n + '”');
      sp.textContent = bits.join(' · ');
      del.type = 'button'; del.textContent = S.del; del.addEventListener('click', function(){ store(load().filter(function(y){ return y.d !== x.d; })); paint(); fillForm($('ag-date').value); });
      li.appendChild(b); li.appendChild(sp); li.appendChild(del); ul.appendChild(li);
    });
    var last = l.filter(function(x){ var k = today - dayN(x.d); return k >= 0 && k < 14; });
    var wa = $('ag-wa');
    if (last.length){
      var ps = last.map(function(x){ return x.p; });
      wa.href = WA + encodeURIComponent(fill(S.wa, {f: nice(last[0].d), t: nice(last[last.length - 1].d), n: last.length, a: f1(avg(last)), lo: Math.min.apply(null, ps), hi: Math.max.apply(null, ps)}));
      wa.removeAttribute('aria-disabled'); wa.style.opacity = '';
    } else { wa.href = '#'; wa.setAttribute('aria-disabled', 'true'); wa.style.opacity = '.5'; }
  }
  $('ag-wa').addEventListener('click', function(e){ if (this.getAttribute('aria-disabled') === 'true') e.preventDefault(); });
  $('ag-csv').addEventListener('click', function(){
    var l = load(), rows = [S.csvh];
    l.forEach(function(x){ rows.push([x.d, x.p, (x.w || []).map(function(i){ return PL[i]; }).join(', '), x.s != null && x.s >= 0 ? S['s' + x.s] : '', x.m != null && x.m >= 0 ? S['m' + x.m] : '', '"' + (x.n || '').replace(/"/g, '""') + '"'].join(';')); });
    var blob = new Blob(['\\ufeff' + rows.join('\\n')], {type: 'text/csv;charset=utf-8'}), a = document.createElement('a');
    a.href = URL.createObjectURL(blob); a.download = S.csvname + '-' + iso(new Date()) + '.csv'; document.body.appendChild(a); a.click();
    setTimeout(function(){ URL.revokeObjectURL(a.href); a.remove(); }, 500);
  });
  $('ag-clear').addEventListener('click', function(){ if (load().length && window.confirm(S.confirm)){ store([]); paint(); fillForm($('ag-date').value); $('ag-saved').textContent = ''; } });
  fillForm($('ag-date').value); paint();
})();
</script>
'''

page("agri-gunlugu.html", "Ağrı Günlüğü",
     "Ağrınızı, uykunuzu ve hareketinizi her gün bir dakikada kaydedin; ağrınızın seyrini grafikte görün, özeti hekiminiz ya da fizyoterapistinizle paylaşın. Kayıtlar yalnızca cihazınızda kalır.",
     "agri-gunlugu.html", SELF6_CSS, AG_BODY, AG_JS,
     seo_title="Ağrı Günlüğü: Günlük Ağrı, Uyku ve Hareket Kaydı | İhsan Eren",
     faq_items=AG_FAQ)

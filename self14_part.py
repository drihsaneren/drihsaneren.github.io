# -*- coding: utf-8 -*-
# Kendine iyi bak, 14. tur: ev tansiyon günlüğü ve 6 dakika yürüme testi. self13_part.py'den sonra exec edilir (SELF13_CSS, WAKE_JS hazır).
# Kaynaklar (23 Ekim 2026'da okundu): NICE NG136 ev ölçümü (GPnotebook özeti), NHS 111 Wales yüksek tansiyon (4 Ara 2024), UHB PI25/3366/06 (Eki 2025), Blood Pressure UK,
# ESC 2024 (ACC özeti), nidirect (26 Şub 2026); Holland 2014 ERS/ATS teknik standardı (tam metin), Enright & Sherrill 1998 (özet), ATS hasta bilgisi (2021),
# CUH 6 dakika yürüme testi (Şub 2025), Polkey 2013 ECLIPSE (RBHT özeti).

SELF14_CSS = SELF13_CSS + """
  .tg-in{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-top:6px}
  .tg-in label{display:block;font-size:12.5px;color:var(--muted);margin-bottom:4px}
  .tg-in input{width:100%;box-sizing:border-box;padding:10px 10px;border-radius:12px;border:1px solid var(--line-strong);background:rgba(236,229,207,.04);color:var(--ink);font:inherit;font-size:16px}
  .tg-msg{font-size:14px;line-height:1.5;margin:10px 0 0;color:var(--ink-soft)}
  .tg-msg.warn{color:#f0c7a6}
  .tg-avg{font-family:var(--display);font-size:clamp(40px,7vw,56px);line-height:1;color:var(--ink);font-variant-numeric:tabular-nums;margin:6px 0 0}
  .tg-avg small{font-family:var(--body,inherit);font-size:14px;color:var(--muted);margin-left:6px}
  .tg-tools{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
  .aw-dist{text-align:center;font-family:var(--display);font-size:clamp(40px,7vw,56px);line-height:1;color:var(--ink);font-variant-numeric:tabular-nums;margin:6px 0 0}
  .aw-distl{text-align:center;margin:0;font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
  .aw-row{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin-top:10px}
  .aw-row label{display:block;font-size:12.5px;color:var(--muted);margin-bottom:4px}
  .aw-row input{width:100%;box-sizing:border-box;padding:10px 10px;border-radius:12px;border:1px solid var(--line-strong);background:rgba(236,229,207,.04);color:var(--ink);font:inherit;font-size:16px}
"""

# ------------------------------------------------------------------ 1 · EV TANSİYON GÜNLÜĞÜ
TG_FAQ = [
 ("Neden iki ölçüm yapıyorum?", "İlk ölçüm çoğu zaman biraz yüksek çıkar. İngiltere’nin kılavuzu (NICE) her seferde 1 dakika arayla iki ölçüm yapılmasını öneriyor. Blood Pressure UK da ilk ölçüm diğerinden belirgin yüksekse onu atıp bir ölçüm daha yapmayı öneriyor."),
 ("Neden ilk günün ölçümleri sayılmıyor?", "Ev ölçümüne yeni başlayanlarda ilk günün değerleri, alışma ve heyecan nedeniyle daha yüksek olabilir. NICE, tanı için 4–7 gün boyunca ölçüm yapılmasını, ilk günün ölçümlerinin atılıp kalanların ortalamasının alınmasını öneriyor. Bu günlük de ortalamayı aynı şekilde hesaplar."),
 ("Ortalamam 135/85’in üzerinde çıktı, ne yapmalıyım?", "Bu bir tanı değildir, ama ölçümlerinizi hekiminizle paylaşmanız gerekir. Evde ölçülen ortalamanın 135/85 ya da üzerinde olması (80 yaş ve üzerinde 145/85 ya da üzerinde) yüksek tansiyonu düşündürür. Tanıyı ve tedaviyi hekiminiz muayene ölçümleriyle birlikte değerlendirerek koyar. Tek tek ölçümlere bakarak ilacınızı değiştirmeyin."),
 ("Hangi cihazı kullanmalıyım?", "Üst koldan ölçen, doğruluğu klinik olarak test edilmiş bir cihaz kullanın; bilekten ya da parmaktan ölçen cihazlar önerilmiyor. Manşon kolunuzun çevresine uygun olmalı ve cihaz en az 2 yılda bir kalibre edilmeli. Cihazınızı bir muayeneye götürüp doğru ölçtüğünü kontrol ettirebilirsiniz."),
 ("Ev ölçümü neden önemli?", "Bazı kişilerde tansiyon yalnızca muayenehanede yüksek çıkar, bazılarında ise muayenede normal görünürken gün içinde yüksektir. Avrupa Kardiyoloji Derneği tanı için muayene dışı ölçümleri öneriyor ve kendi tansiyonunu ölçmenin tedaviye uyumu da desteklediğini belirtiyor."),
]

TG_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Ev tansiyon günlüğü</h1>
    <p class="lede">Hekiminiz evde tansiyon ölçmenizi istediyse, ya da kendi değerlerinizi düzenli izlemek istiyorsanız bu günlük işinizi kolaylaştırır. Ölçümden önceki 5 dakikalık dinlenmeyi ve iki ölçüm arasındaki 1 dakikayı sayar, ölçümlerinizi kaydeder, İngiltere kılavuzunun yöntemiyle ortalamanızı hesaplar ve hekiminize götürebileceğiniz bir dosya hazırlar.</p>
    <p class="meta">Son güncelleme: 23 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>2 × 2</b><span>Sabah ve akşam, 1 dakika arayla ikişer ölçüm</span></div>
        <div class="stat"><b>4–7 gün</b><span>Tanı için önerilen ölçüm süresi; ilk günün ölçümleri ortalamaya katılmaz</span></div>
        <div class="stat"><b>135/85</b><span>Evde ölçülen ortalamada yüksek tansiyonu düşündüren sınır; 80 yaş ve üzerinde 145/85</span></div>
        <div class="stat"><b>5 dakika</b><span>Ölçümden önce sessizce oturup dinlenme süresi</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Kendinizi ölçün</p>
      <h2>Ölçün ve kaydedin</h2>
      <p class="soft">Sırtınız destekli, bacaklarınız çapraz olmadan oturun; kolunuzu kalp hizasında bir masaya koyun. Dinlenmeyi başlatın, 5 dakika dolunca ilk ölçümü yapıp değerleri girin. Sayfa 1 dakika sayar; ardından ikinci ölçümü yapıp onu da girin. Nabız alanını boş bırakabilirsiniz.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <p class="lbl">Ölçüm zamanı</p>
            <div class="seg" role="group" aria-label="Ölçüm zamanı" id="tg-z">
              <button type="button" data-v="s" aria-pressed="true">Sabah</button>
              <button type="button" data-v="a" aria-pressed="false">Akşam</button>
            </div>
            <div class="tg-in">
              <div><label for="tg-s">Büyük</label><input id="tg-s" type="number" inputmode="numeric" min="60" max="260" placeholder="ör. 128"></div>
              <div><label for="tg-d">Küçük</label><input id="tg-d" type="number" inputmode="numeric" min="30" max="160" placeholder="ör. 82"></div>
              <div><label for="tg-p">Nabız</label><input id="tg-p" type="number" inputmode="numeric" min="30" max="220" placeholder="ör. 72"></div>
            </div>
            <label class="mz-chk"><input type="checkbox" id="tg-80"> 80 yaş ve üzerindeyim</label>
            <label class="mz-chk"><input type="checkbox" id="tg-sound" checked> Sesli uyarı</label>
            <div class="controls" style="margin-top:12px"><button type="button" class="cta" id="tg-add">Ölçümü ekle</button></div>
            <p class="tg-msg" id="tg-msg" aria-live="polite"></p>
          </div>
          <div class="bt-out">
            <div class="res" id="tg-res">
              <p class="lab" id="tg-lab"></p>
              <p class="tg-avg" id="tg-avg" hidden></p>
              <p id="tg-txt"></p>
              <span class="bt-badge" id="tg-badge" hidden></span>
            </div>
            <div id="tg-histw" style="margin-top:20px" hidden>
              <p class="lbl">Son ölçümleriniz (bu cihazda)</p>
              <ul class="cs-hist" id="tg-hist"></ul>
              <div class="tg-tools">
                <button type="button" class="cta ghost" id="tg-csv">CSV indir</button>
                <button type="button" class="cta ghost" id="tg-undo">Son ölçümü sil</button>
                <button type="button" class="cta ghost" id="tg-clear">Tümünü sil</button>
              </div>
            </div>
          </div>
          <div class="bt-run">
            <div class="yh-time"><b id="tg-sec">5:00</b><span id="tg-unit">dinlenme</span></div>
            <p class="bt-phase" id="tg-phase" aria-live="polite">Hazır</p>
            <p class="bt-cue" id="tg-cue">Oturun, kolunuzu masaya koyun ve dinlenmeyi başlatın.</p>
            <button type="button" class="bt-tap" id="tg-go">Dinlenmeyi başlat</button>
            <div class="controls" style="margin-top:10px;justify-content:center">
              <button type="button" class="cta ghost" id="tg-reset">Sıfırla</button>
            </div>
          </div>
        </div>
        <div class="tg-strings" hidden>
          <span data-k="ready">Hazır</span>
          <span data-k="readyc">Oturun, kolunuzu masaya koyun ve dinlenmeyi başlatın.</span>
          <span data-k="start">Dinlenmeyi başlat</span>
          <span data-k="stop">Durdur</span>
          <span data-k="rest">Sessizce dinlenin</span>
          <span data-k="restc">Konuşmayın, bacaklarınızı çaprazlamayın.</span>
          <span data-k="m1">1. ölçümü yapın</span>
          <span data-k="m1c">Değerleri girip Ölçümü ekle’ye basın.</span>
          <span data-k="wait">1 dakika bekleyin</span>
          <span data-k="waitc">Kolunuzu masada tutun, sakin kalın.</span>
          <span data-k="m2">2. ölçümü yapın</span>
          <span data-k="m2c">Değerleri girip Ölçümü ekle’ye basın.</span>
          <span data-k="done">Bu oturum tamam</span>
          <span data-k="donec">Bir sonraki ölçüm zamanında yeniden başlayın.</span>
          <span data-k="restu">dinlenme</span>
          <span data-k="waitu">bekleme</span>
          <span data-k="bad">Değerleri kontrol edin: büyük tansiyon 60–260, küçük tansiyon 30–160 arasında olmalı ve büyük tansiyon küçükten yüksek olmalı.</span>
          <span data-k="badp">Nabız 30–220 arasında olmalı ya da boş bırakılmalı.</span>
          <span data-k="ok">Kaydedildi: {{s}}/{{d}}</span>
          <span data-k="high">Bu ölçüm çok yüksek ({{s}}/{{d}}). 5 dakika dinlenip yeniden ölçün; yine bu düzeydeyse aynı gün hekiminize başvurun. Göğüs ağrısı, nefes darlığı, yüzde kayma, kolda güçsüzlük ya da konuşma bozukluğu varsa 112’yi arayın.</span>
          <span data-k="low">Bu ölçüm düşük ({{s}}/{{d}}). Baş dönmesi, bayılma ya da halsizlik varsa hekiminize danışın.</span>
          <span data-k="none">Henüz ölçüm yok. İlk ölçümünüzü ekleyin.</span>
          <span data-k="few">Son 7 günde {{n}} gün ölçüm var. Güvenilir bir ortalama için en az 4 gün ölçün; ilk günün ölçümleri ortalamaya katılmaz.</span>
          <span data-k="lab">Son 7 gün: {{n}} gün, {{m}} ölçüm</span>
          <span data-k="avgu">ortalama, ilk gün hariç</span>
          <span data-k="under">Ev ölçümü ortalamanız {{c}}’in altında; ev ölçümleri için normal kabul edilen aralıkta.</span>
          <span data-k="over">Ev ölçümü ortalamanız {{c}} ya da üzerinde. Bu yüksek tansiyonu düşündürebilir; ölçümlerinizi hekiminizle paylaşın.</span>
          <span data-k="bok">Normal aralıkta</span>
          <span data-k="bno">Hekiminizle paylaşın</span>
          <span data-k="zs">Sabah</span>
          <span data-k="za">Akşam</span>
          <span data-k="sure">Emin misiniz? Silmek için yeniden basın</span>
          <span data-k="clear">Tümünü sil</span>
          <span data-k="csvh">Tarih;Saat;Zaman;Büyük;Küçük;Nabız</span>
        </div>
      </div>
      <p class="count">Ölçümleriniz yalnızca bu cihazda saklanır; hiçbir yere gönderilmez. CSV dosyasını hekiminizle paylaşabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Doğru ölçüm için</h2>
        <ol class="steps">
          <li><span>Üst koldan ölçen, doğruluğu test edilmiş bir cihaz ve kolunuza uygun manşon kullanın.</span></li>
          <li><span>Ölçümden önceki 30 dakika yemek yemeyin, sigara, kahve ve egzersizden kaçının; tuvalete gidin.</span></li>
          <li><span>Sırtınız destekli, bacaklarınız çapraz olmadan oturun; kolunuzu kalp hizasında masaya koyun ve manşonu çıplak kola, dirseğin yaklaşık 2 cm üzerine takın.</span></li>
          <li><span>5 dakika sessizce dinlenin, ölçüm sırasında konuşmayın. Sabah (ilaçlardan önce) ve akşam, 1 dakika arayla ikişer ölçüm yapın.</span></li>
          <li><span>Her ölçümü, yüksek çıkanlar dahil, olduğu gibi kaydedin; her seferinde aynı kolu kullanın.</span></li>
        </ol>
      </div>
      <div>
        <h2>Sonuç ne anlama gelir?</h2>
        <p class="soft">Tek tek ölçümlere değil, ortalamaya bakılır. Evde ölçülen ortalamanın 135/85’in altında olması normal kabul ediliyor; 135/85 ya da üzeri (80 yaş ve üzerinde 145/85 ya da üzeri) yüksek tansiyonu düşündürür. Ev ölçümü tek başına tanı koydurmaz; hekiminiz muayene ölçümleriyle birlikte değerlendirir.</p>
        <div class="callout">
          <p>Tek tek ölçümlere bakarak ilacınızı değiştirmeyin ya da bırakmayın. Ölçümlerinizi hekiminizle paylaşın.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(TG_FAQ)}
      <p class="soft" style="margin-top:18px">Tansiyonu düşürmek için egzersiz ve yaşam tarzı önerileri <a href="yuksek-tansiyon.html">yüksek tansiyonda egzersiz</a> rehberinde; izometrik egzersiz için <a href="duvar-oturusu.html">duvar oturuşu zamanlayıcısına</a> bakabilirsiniz.</p>
      {CTA_CARD("Tansiyonunuz ve egzersiz programınız", "yüksek tansiyonda egzersiz programı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "National Institute for Health and Care Excellence. Hypertension in adults: diagnosis and management. NICE guideline NG136. Ev ölçümü özeti: " + ext("https://gpnotebook.com/pages/cardiovascular-medicine/home-self-blood-pressure-monitoring", "GPnotebook") + ".",
        "NHS 111 Wales. " + ext("https://111.wales.nhs.uk/Bloodpressure(high)", "Blood pressure (high)") + ". Last updated 4 December 2024.",
        "University Hospitals Birmingham NHS Foundation Trust. " + ext("https://www.uhb.nhs.uk/media/cdkdecer/pi-renal-blood-pressure-self-monitoring.pdf", "Self-blood pressure monitoring: key points") + ". PI25/3366/06, October 2025.",
        "Blood Pressure UK. " + ext("https://www.bloodpressureuk.org/BloodPressureandyou/Homemonitoring/Howtomeasure", "How to measure your blood pressure at home") + ".",
        "McEvoy JW, McCarthy CP, Bruno RM, et al. 2024 ESC Guidelines for the management of elevated blood pressure and hypertension. Eur Heart J. 2024;45(38):3912–4018. Özet: " + ext("https://www.acc.org/Latest-in-Cardiology/ten-points-to-remember/2024/09/05/14/11/2024-esc-guidelines-for-bp-esc-2024", "American College of Cardiology") + ".",
        "nidirect (Northern Ireland). " + ext("https://www.nidirect.gov.uk/articles/high-blood-pressure-hypertension", "High blood pressure (hypertension)") + ". Last updated 26 February 2026.",
      ])}
    </div>
  </section>
</main>'''

TG_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.tg-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var EN = document.documentElement.lang === 'en';
  var $ = function(id){ return document.getElementById(id); }, KEY = 'drihsaneren.tansiyon.v1';
  var lock = null, ctx = null, snd = $('tg-sound');
''' + WAKE_JS + '''
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function mmss(s){ s = Math.max(0, Math.ceil(s)); var m = Math.floor(s / 60), r = s % 60; return m + ':' + (r < 10 ? '0' : '') + r; }
  function zone(){ return $('tg-z').querySelector('[aria-pressed="true"]').getAttribute('data-v'); }
  function pickZ(v){ $('tg-z').querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x.getAttribute('data-v') === v ? 'true' : 'false'); }); }
  function load(){ try { return JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { return []; } }
  function save(l){ try { localStorage.setItem(KEY, JSON.stringify(l.slice(-200))); } catch (e) {} }
  function dkey(d){ return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2); }
  function cut(){ return $('tg-80').checked ? [145, 85] : [135, 85]; }
  function summary(){
    var l = load(), now = new Date(), from = dkey(new Date(now.getFullYear(), now.getMonth(), now.getDate() - 6));
    var w = l.filter(function(r){ return dkey(new Date(r.t)) >= from; });
    var days = {}; w.forEach(function(r){ var k = dkey(new Date(r.t)); (days[k] = days[k] || []).push(r); });
    var ks = Object.keys(days).sort(), use = [];
    ks.slice(1).forEach(function(k){ use = use.concat(days[k]); });
    var avg = null;
    if (use.length){ var s = 0, d = 0; use.forEach(function(r){ s += r.s; d += r.d; }); avg = [Math.round(s / use.length), Math.round(d / use.length)]; }
    return {days: ks.length, n: w.length, avg: avg, all: l};
  }
  function paint(){
    var r = summary(), c = cut(), badge = $('tg-badge'), av = $('tg-avg');
    $('tg-lab').textContent = r.n ? fill(S.lab, {n: r.days, m: r.n}) : '';
    if (!r.n){ $('tg-txt').textContent = S.none; av.hidden = badge.hidden = true; }
    else if (r.days < 4){ $('tg-txt').textContent = fill(S.few, {n: r.days}); av.hidden = badge.hidden = true; }
    else {
      av.hidden = false; av.innerHTML = r.avg[0] + '/' + r.avg[1] + '<small></small>'; av.querySelector('small').textContent = S.avgu;
      var hi = r.avg[0] >= c[0] || r.avg[1] >= c[1];
      $('tg-txt').textContent = fill(hi ? S.over : S.under, {c: c[0] + '/' + c[1]});
      badge.hidden = false; badge.textContent = hi ? S.bno : S.bok; badge.classList.toggle('no', hi);
    }
    var ul = $('tg-hist'); ul.innerHTML = ''; $('tg-histw').hidden = !r.all.length;
    r.all.slice(-14).reverse().forEach(function(x){
      var li = document.createElement('li'), sp = document.createElement('span'), b = document.createElement('b'), d = new Date(x.t);
      sp.textContent = d.toLocaleDateString(EN ? 'en-GB' : 'tr-TR', {day: 'numeric', month: 'short'}) + ' · ' + d.toLocaleTimeString(EN ? 'en-GB' : 'tr-TR', {hour: '2-digit', minute: '2-digit'}) + ' · ' + S['z' + x.z];
      b.textContent = x.s + '/' + x.d + (x.p ? ' · ' + x.p : '');
      li.appendChild(sp); li.appendChild(b); ul.appendChild(li);
    });
  }
  var phase = 'idle', left = 300, t0 = 0, iv = null, run = false, inSession = 0;
  function setPhase(p, c, u){ $('tg-phase').textContent = p; $('tg-cue').textContent = c; if (u) $('tg-unit').textContent = u; }
  function tick(){
    var rem = left - (performance.now() - t0) / 1000; $('tg-sec').textContent = mmss(rem);
    if (rem > 0) return;
    clearInterval(iv); iv = null; run = false; wake(false);
    beep(660, .2, .18); setTimeout(function(){ beep(880, .3, .18); }, 240);
    $('tg-go').textContent = S.start; $('tg-go').classList.remove('stop');
    if (phase === 'rest'){ phase = 'm1'; setPhase(S.m1, S.m1c); $('tg-s').focus(); }
    else if (phase === 'wait'){ phase = 'm2'; setPhase(S.m2, S.m2c); $('tg-s').focus(); }
  }
  function startTimer(p, sec){
    phase = p; left = sec; t0 = performance.now(); run = true; wake(true);
    try { ctx = ctx || new (window.AudioContext || window.webkitAudioContext)(); if (ctx.resume) ctx.resume(); } catch (e) {}
    if (p === 'rest') setPhase(S.rest, S.restc, S.restu); else setPhase(S.wait, S.waitc, S.waitu);
    $('tg-go').textContent = S.stop; $('tg-go').classList.add('stop');
    clearInterval(iv); iv = setInterval(tick, 250); tick();
  }
  function reset(){
    clearInterval(iv); iv = null; run = false; wake(false); phase = 'idle'; inSession = 0; left = 300;
    $('tg-sec').textContent = mmss(300); setPhase(S.ready, S.readyc, S.restu);
    $('tg-go').textContent = S.start; $('tg-go').classList.remove('stop');
  }
  $('tg-go').addEventListener('click', function(){
    if (run){ reset(); return; }
    inSession = 0; startTimer('rest', 300);
  });
  $('tg-reset').addEventListener('click', reset);
  $('tg-z').addEventListener('click', function(e){ var b = e.target.closest('button'); if (b) pickZ(b.getAttribute('data-v')); });
  $('tg-80').addEventListener('change', paint);
  $('tg-add').addEventListener('click', function(){
    var s = parseInt($('tg-s').value, 10), d = parseInt($('tg-d').value, 10), p = $('tg-p').value === '' ? null : parseInt($('tg-p').value, 10), msg = $('tg-msg');
    msg.classList.remove('warn');
    if (isNaN(s) || isNaN(d) || s < 60 || s > 260 || d < 30 || d > 160 || s <= d){ msg.textContent = S.bad; msg.classList.add('warn'); return; }
    if (p != null && (isNaN(p) || p < 30 || p > 220)){ msg.textContent = S.badp; msg.classList.add('warn'); return; }
    var l = load(); l.push({t: new Date().toISOString(), s: s, d: d, p: p, z: zone()}); save(l);
    $('tg-s').value = ''; $('tg-d').value = ''; $('tg-p').value = '';
    if (s >= 180 || d >= 110){ msg.textContent = fill(S.high, {s: s, d: d}); msg.classList.add('warn'); }
    else if (s <= 90 || d <= 60){ msg.textContent = fill(S.low, {s: s, d: d}); msg.classList.add('warn'); }
    else msg.textContent = fill(S.ok, {s: s, d: d});
    paint();
    if (phase === 'm1' || (phase === 'idle' && inSession === 0)){ inSession = 1; startTimer('wait', 60); }
    else if (phase === 'm2'){ inSession = 2; phase = 'idle'; setPhase(S.done, S.donec); }
  });
  $('tg-undo').addEventListener('click', function(){ var l = load(); l.pop(); save(l); paint(); });
  var armed = false;
  $('tg-clear').addEventListener('click', function(){
    if (!armed){ armed = true; this.textContent = S.sure; var b = this; setTimeout(function(){ armed = false; b.textContent = S.clear; }, 4000); return; }
    save([]); armed = false; this.textContent = S.clear; paint();
  });
  $('tg-csv').addEventListener('click', function(){
    var rows = [S.csvh];
    load().forEach(function(r){ var d = new Date(r.t); rows.push([dkey(d), d.toTimeString().slice(0, 5), S['z' + r.z], r.s, r.d, r.p == null ? '' : r.p].join(';')); });
    try {
      var blob = new Blob(['\\ufeff' + rows.join('\\n')], {type: 'text/csv;charset=utf-8'}), a = document.createElement('a');
      a.href = URL.createObjectURL(blob); a.download = (EN ? 'blood-pressure-diary' : 'tansiyon-gunlugu') + '.csv';
      document.body.appendChild(a); a.click(); setTimeout(function(){ URL.revokeObjectURL(a.href); a.remove(); }, 500);
    } catch (e) {}
  });
  pickZ(new Date().getHours() < 15 ? 's' : 'a'); reset(); paint();
  window.__tg = {st: function(){ var r = summary(); return [phase, r.n, r.days, r.avg]; }, ff: function(s){ t0 -= s * 1000; }};
})();
</script>
'''

page("tansiyon-gunlugu.html", "Ev Tansiyon Günlüğü",
     "Evde tansiyon ölçümü için günlük: 5 dakika dinlenme ve 1 dakika ara zamanlayıcısı, sabah-akşam ikişer ölçüm, ilk gün hariç ortalama, 135/85 sınırı ve hekiminize götürebileceğiniz CSV dosyası.",
     "tansiyon-gunlugu.html", SELF14_CSS, TG_BODY, TG_JS,
     seo_title="Ev Tansiyon Günlüğü: Doğru Ölçüm, Ortalama ve 135/85 Sınırı | İhsan Eren",
     about={"@type": "MedicalTest", "name": "Evde tansiyon ölçümü"},
     faq_items=TG_FAQ)

# ------------------------------------------------------------------ 2 · 6 DAKİKA YÜRÜME TESTİ
AW_FAQ = [
 ("Evde yapabilir miyim?", "Yapabilirsiniz, ama sonucu kendi ilerlemenizi izlemek için kullanın. Uluslararası standart, en az 30 metrelik düz bir koridor öneriyor; yaşa ve boya göre beklenen değerler de bu koşullarda elde edildi. Parkur kısaldıkça sonuç değişebilir: bir çalışmada 30 metrelik parkurda 10 metrelik parkura göre yaklaşık 50 metre daha fazla yüründü. Her seferinde aynı parkuru kullanın."),
 ("Neden iki kez yapmam öneriliyor?", "İnsanlar ikinci denemede genellikle daha uzağa yürür: akciğer hastalarında ikinci test ortalama 26 metre daha uzun çıkıyor. Bu yüzden ilk kez yapıyorsanız tam dinlendikten sonra testi tekrarlayıp daha iyi sonucu kaydedebilirsiniz."),
 ("Ne kadarlık değişim anlamlı?", "Kronik akciğer hastalıklarında anlamlı kabul edilen değişim yaklaşık 30 metre (25–33 metre). Bu değer çoğunlukla grup ortalamalarından hesaplandı; kişisel sonuçlarınızı yorumlarken hekiminiz ya da fizyoterapistinizle konuşun."),
 ("Mesafem düştü, ne anlama gelir?", "Bir yıl boyunca 2.112 KOAH hastasının izlendiği bir çalışmada, 6 dakika yürüme mesafesinde 30 metre ya da daha fazla düşüş, ölüm riskinde artışla ilişkiliydi. Sonucunuz belirgin düştüyse ya da nefes darlığınız arttıysa hekiminize danışın; bu tek başına bir tanı değildir."),
 ("Test sırasında durabilir miyim?", "Evet. Yavaşlayabilir, durup dinlenebilir ve kendinizi hazır hissettiğinizde yürümeye devam edebilirsiniz; süre işlemeye devam eder. Amaç 6 dakikada kendi temponuzla olabildiğince uzağa yürümektir; koşmayın."),
]

AW_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>6 dakika yürüme testi</h1>
    <p class="lede">6 dakika yürüme testi, kalp ve akciğer hastalıklarında ve rehabilitasyonda günlük hayattaki kondisyonu ölçmek için en sık kullanılan testlerden biridir: 6 dakikada kendi temponuzla ne kadar uzağa yürüdüğünüze bakılır. Bu sayfa süreyi tutar, her dakika standart cümlelerle sizi yönlendirir, parkur dönüşlerini sayarak mesafenizi hesaplar ve sonuçlarınızı kaydeder.</p>
    <p class="meta">Son güncelleme: 23 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>6 dakika</b><span>Kendi temponuzla, gerekirse durup dinlenerek yürünen süre</span></div>
        <div class="stat"><b>30 m</b><span>Uluslararası standartta önerilen düz parkur uzunluğu</span></div>
        <div class="stat"><b>~30 m</b><span>Kronik akciğer hastalıklarında anlamlı kabul edilen değişim</span></div>
        <div class="stat"><b>+26 m</b><span>İkinci denemede ortalama daha uzun yürünen mesafe</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Kendinizi ölçün</p>
      <h2>Testi yapın</h2>
      <p class="soft">Düz bir koridorda iki nokta işaretleyin ve aralarındaki mesafeyi girin. Başla’ya basıp iki işaret arasında gidip gelin; her işarete ulaştığınızda büyük düğmeye dokunun ya da yanınızdaki kişi dokunsun. Süre bitince son yarım kalan parkuru da ekleyip kaydedin.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <div class="aw-row">
              <div><label for="aw-l">Parkur uzunluğu (m)</label><input id="aw-l" type="number" inputmode="decimal" min="3" max="60" value="10"></div>
              <div><label for="aw-age">Yaşınız</label><input id="aw-age" type="number" inputmode="numeric" min="18" max="100" placeholder="ör. 62"></div>
              <div><label for="aw-h">Boy (cm)</label><input id="aw-h" type="number" inputmode="numeric" min="120" max="220" placeholder="ör. 168"></div>
              <div><label for="aw-w">Kilo (kg)</label><input id="aw-w" type="number" inputmode="numeric" min="30" max="250" placeholder="ör. 74"></div>
            </div>
            <p class="lbl" style="margin-top:12px">Cinsiyet</p>
            <div class="seg" role="group" aria-label="Cinsiyet" id="aw-sex">
              <button type="button" data-v="f" aria-pressed="true">Kadın</button>
              <button type="button" data-v="m" aria-pressed="false">Erkek</button>
            </div>
            <label class="mz-chk"><input type="checkbox" id="aw-sound" checked> Sesli uyarı</label>
            <div class="ad-man">
              <div><p class="lbl"><label for="aw-man">Toplam mesafe (m)</label></p><input id="aw-man" type="number" inputmode="numeric" min="0" max="1200" placeholder="ör. 420"></div>
              <button type="button" class="cta" id="aw-save">Kaydet</button>
            </div>
          </div>
          <div class="bt-out">
            <div class="res" id="aw-res" hidden>
              <p class="lab" id="aw-lab"></p>
              <p id="aw-txt"></p>
            </div>
            <div id="aw-histw" style="margin-top:20px" hidden>
              <p class="lbl">Önceki sonuçlarınız (bu cihazda)</p>
              <ul class="cs-hist" id="aw-hist"></ul>
            </div>
          </div>
          <div class="bt-run">
            <div class="yh-time"><b id="aw-sec">6:00</b><span>kalan süre</span></div>
            <p class="aw-dist" id="aw-dist">0</p><p class="aw-distl" id="aw-distl">metre · 0 parkur</p>
            <p class="bt-phase" id="aw-phase" aria-live="polite">Hazır</p>
            <p class="bt-cue" id="aw-cue">Başlangıç işaretinde durun ve Başla’ya basın.</p>
            <button type="button" class="bt-tap" id="aw-go">Başla</button>
            <div class="controls" style="margin-top:10px;justify-content:center">
              <button type="button" class="cta ghost" id="aw-reset">Sıfırla</button>
            </div>
          </div>
        </div>
        <div class="aw-strings" hidden>
          <span data-k="ready">Hazır</span>
          <span data-k="readyc">Başlangıç işaretinde durun ve Başla’ya basın.</span>
          <span data-k="start">Başla</span>
          <span data-k="tap">Dönüş: +1 parkur</span>
          <span data-k="get">Hazır olun</span>
          <span data-k="getc">Birazdan başlıyor.</span>
          <span data-k="run">Yürüyün</span>
          <span data-k="runc">Kendi temponuzla, olabildiğince uzağa yürüyün; koşmayın.</span>
          <span data-k="e1">İyi gidiyorsunuz. 5 dakikanız kaldı.</span>
          <span data-k="e2">Böyle devam edin. 4 dakikanız kaldı.</span>
          <span data-k="e3">İyi gidiyorsunuz. Yarıya geldiniz.</span>
          <span data-k="e4">Böyle devam edin. Yalnızca 2 dakikanız kaldı.</span>
          <span data-k="e5">İyi gidiyorsunuz. Yalnızca 1 dakikanız kaldı.</span>
          <span data-k="done">Durun</span>
          <span data-k="donec">Yarım kalan parkuru mesafeye ekleyip Kaydet’e basın.</span>
          <span data-k="distl">metre · {{n}} parkur</span>
          <span data-k="saved">Sonuç kaydedildi</span>
          <span data-k="savedc">Birkaç hafta sonra testi aynı parkurda tekrarlayabilirsiniz.</span>
          <span data-k="lab">Sonucunuz: {{m}} metre</span>
          <span data-k="pred">Yaşınız, boyunuz ve kilonuza göre sağlıklı yetişkinlerde beklenen yaklaşık {{p}} metre; sonucunuz bunun %{{r}}’i.</span>
          <span data-k="short">Beklenen değerle karşılaştırma için en az 30 metrelik düz bir parkur gerekir. Bu sonucu, aynı parkurda kendi ilerlemenizi izlemek için kullanın.</span>
          <span data-k="noinfo">Beklenen değeri görmek için yaşınızı (40–80), boyunuzu ve kilonuzu girin.</span>
          <span data-k="diff">Önceki teste göre {{d}} metre.</span>
          <span data-k="big">Bu, anlamlı kabul edilen yaklaşık 30 metrelik değişimden büyük.</span>
          <span data-k="lenx">Önceki test farklı uzunlukta bir parkurda yapıldı; sonuçlar doğrudan karşılaştırılamaz.</span>
          <span data-k="m">m</span>
          <span data-k="course">parkur {{l}} m</span>
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
          <li><span>Rahat giysiler ve yürüyüş ayakkabısı giyin, ilaçlarınızı ve inhalerlerinizi her zamanki gibi kullanın. Testten önceki 2 saat ağır egzersiz yapmayın; isterseniz 1–2 saat önce hafif bir şey yiyin.</span></li>
          <li><span>Düz, engelsiz bir koridorda iki nokta işaretleyin. Kullandığınız baston ya da yürüteci yanınıza alın; yanınızda biri olsun.</span></li>
          <li><span>Başlamadan önce yaklaşık 10 dakika oturup dinlenin.</span></li>
          <li><span>Başla’ya basın ve 6 dakika boyunca iki işaret arasında, kendi temponuzla olabildiğince uzağa yürüyün. Gerekirse durup dinlenin; süre işlemeye devam eder.</span></li>
          <li><span>Süre bitince olduğunuz yerde durun, yarım kalan parkuru ekleyip sonucu kaydedin.</span></li>
        </ol>
      </div>
      <div>
        <h2>Güvenlik</h2>
        <ul class="dots">
          <li>Son bir ay içinde kalp krizi geçirdiyseniz ya da göğüs ağrınız son zamanlarda değiştiyse testi yapmayın.</li>
          <li>Dinlenirken nabzınız dakikada 120’nin, tansiyonunuz 180/100’ün üzerindeyse önce hekiminize danışın.</li>
          <li>Göğüs ağrısı, dayanılmaz nefes darlığı, bacak krampları, sendeleme, aşırı terleme ya da solukluk olursa hemen durun.</li>
          <li>Oksijen kullanıyorsanız test sırasında da hekiminizin önerdiği şekilde kullanın.</li>
        </ul>
        <div class="callout">
          <p>Bu sayfa kendi ilerlemenizi izlemeniz içindir; hastanede yapılan, oksijen ve nabız ölçümüyle izlenen testin yerini tutmaz.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(AW_FAQ)}
      <p class="soft" style="margin-top:18px">Dar bir alanda kondisyonunuzu ölçmek için <a href="iki-dakika-adim-testi.html">2 dakika adım testine</a>, ilgili rehberler için <a href="koah.html">KOAH</a> ve <a href="kalp-yetmezligi.html">kalp yetmezliğinde egzersiz</a> sayfalarına bakabilirsiniz.</p>
      {CTA_CARD("Kondisyonunuz ve rehabilitasyon programınız", "6 dakika yürüme testi ve kondisyon değerlendirmesi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Holland AE, Spruit MA, Troosters T, et al. " + ext("https://documentserver.uhasselt.be/bitstream/1942/17964/1/1428.full.pdf", "An official European Respiratory Society/American Thoracic Society technical standard: field walking tests in chronic respiratory disease") + ". Eur Respir J. 2014;44(6):1428–1446.",
        "Enright PL, Sherrill DL. " + ext("https://experts.arizona.edu/en/publications/reference-equations-for-the-six-minute-walk-in-healthy-adults/", "Reference equations for the six-minute walk in healthy adults") + ". Am J Respir Crit Care Med. 1998;158(5 Pt 1):1384–1387.",
        "American Thoracic Society. " + ext("https://THORACIC.ORG/patients/patient-resources/resources/six-minute-walk-test.pdf", "Six-minute walk test (6MWT)") + ". Patient Education Series, 2021.",
        "Cambridge University Hospitals NHS Foundation Trust. " + ext("https://cuh.nhs.uk/patient-information/six-minute-walk-test", "Six minute walk test") + ". Version 2, February 2025.",
        "Polkey MI, Spruit MA, Edwards LD, et al. Six-minute-walk test in chronic obstructive pulmonary disease: minimal clinically important difference for death or hospitalization. Am J Respir Crit Care Med. 2013;187(4):382–386. Özet: " + ext("https://www.rbht.nhs.uk/node/878", "Royal Brompton & Harefield") + ".",
      ])}
    </div>
  </section>
</main>'''

AW_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.aw-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var EN = document.documentElement.lang === 'en';
  var $ = function(id){ return document.getElementById(id); }, KEY = 'drihsaneren.yurume6.v1', DUR = 360;
  var lock = null, ctx = null, snd = $('aw-sound');
''' + WAKE_JS + '''
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function mmss(s){ s = Math.max(0, Math.ceil(s)); var m = Math.floor(s / 60), r = s % 60; return m + ':' + (r < 10 ? '0' : '') + r; }
  function num(id){ var v = parseFloat(String($(id).value).replace(',', '.')); return isNaN(v) ? null : v; }
  function sex(){ return $('aw-sex').querySelector('[aria-pressed="true"]').getAttribute('data-v'); }
  function L(){ var v = num('aw-l'); return v && v >= 3 && v <= 60 ? v : null; }
  function store(){ try { return JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { return []; } }
  function keep(l){ try { localStorage.setItem(KEY, JSON.stringify(l.slice(-10))); } catch (e) {} }
  function predicted(){
    var a = num('aw-age'), h = num('aw-h'), w = num('aw-w');
    if (a == null || h == null || w == null || a < 40 || a > 80) return null;
    return sex() === 'm' ? 7.57 * h - 5.02 * a - 1.76 * w - 309 : 2.11 * h - 2.29 * w - 5.78 * a + 667;
  }
  var phase = 'idle', t0 = 0, iv = null, laps = 0, said = {}, endT = 0, last = null;
  function setLaps(n){ laps = n; var l = L() || 0; $('aw-dist').textContent = String(Math.round(n * l)); $('aw-distl').textContent = fill(S.distl, {n: n}); }
  function idle(p, c){
    phase = 'idle'; clearInterval(iv); iv = null; wake(false);
    $('aw-go').textContent = S.start; $('aw-go').classList.remove('stop');
    $('aw-phase').textContent = p || S.ready; $('aw-cue').textContent = c || S.readyc;
  }
  function tick(){
    var el = (performance.now() - t0) / 1000;
    if (phase === 'get'){
      $('aw-sec').textContent = mmss(DUR);
      if (el >= 3){ phase = 'run'; t0 = performance.now(); beep(880, .5, .22); $('aw-phase').textContent = S.run; $('aw-cue').textContent = S.runc; $('aw-go').textContent = S.tap; $('aw-go').classList.add('stop'); }
      return;
    }
    var rem = DUR - el; $('aw-sec').textContent = mmss(rem);
    var m = Math.floor(el / 60);
    if (m >= 1 && m <= 5 && !said[m]){ said[m] = 1; beep(660, .25, .18); $('aw-cue').textContent = S['e' + m]; }
    if (rem <= 0) end();
  }
  function end(){
    clearInterval(iv); iv = null; wake(false); phase = 'end'; endT = performance.now(); $('aw-sec').textContent = mmss(0);
    beep(660, .2, .18); setTimeout(function(){ beep(880, .2, .18); }, 220); setTimeout(function(){ beep(1100, .35, .18); }, 440);
    $('aw-man').value = Math.round(laps * (L() || 0)); $('aw-go').textContent = S.start; $('aw-go').classList.remove('stop');
    $('aw-phase').textContent = S.done; $('aw-cue').textContent = S.donec; $('aw-man').focus();
  }
  function start(){
    if (!L()){ $('aw-l').focus(); return; }
    setLaps(0); said = {}; phase = 'get'; t0 = performance.now(); wake(true);
    try { ctx = ctx || new (window.AudioContext || window.webkitAudioContext)(); if (ctx.resume) ctx.resume(); } catch (e) {}
    beep(520, .15, .16); $('aw-phase').textContent = S.get; $('aw-cue').textContent = S.getc;
    clearInterval(iv); iv = setInterval(tick, 100); tick();
  }
  function tap(){ if (phase !== 'run') return; setLaps(laps + 1); beep(990, .05, .08); }
  function paintRes(){
    var res = $('aw-res'); if (last == null){ res.hidden = true; return; }
    res.hidden = false; $('aw-lab').textContent = fill(S.lab, {m: last.m});
    var parts = [], p = predicted();
    if (last.l < 30) parts.push(S.short);
    else if (p == null) parts.push(S.noinfo);
    else parts.push(fill(S.pred, {p: Math.round(p), r: Math.round(last.m / p * 100)}));
    var h = store(), prev = h.length > 1 ? h[h.length - 2] : null;
    if (prev){
      if (prev.l !== last.l) parts.push(S.lenx);
      else { var d = last.m - prev.m; parts.push(fill(S.diff, {d: (d > 0 ? '+' : '') + d})); if (Math.abs(d) >= 30) parts.push(S.big); }
    }
    $('aw-txt').textContent = parts.join(' ');
  }
  function paintHist(){
    var h = store(), ul = $('aw-hist'); $('aw-histw').hidden = !h.length; ul.innerHTML = '';
    h.slice().reverse().forEach(function(r){
      var li = document.createElement('li'), sp = document.createElement('span'), bb = document.createElement('b');
      sp.textContent = new Date(r.t).toLocaleDateString(EN ? 'en-GB' : 'tr-TR', {day: 'numeric', month: 'short', year: 'numeric'}) + ' · ' + fill(S.course, {l: r.l});
      bb.textContent = r.m + ' ' + S.m; li.appendChild(sp); li.appendChild(bb); ul.appendChild(li);
    });
  }
  $('aw-go').addEventListener('click', function(){ if (phase === 'run') tap(); else if (phase === 'end' && performance.now() - endT < 2500) return; else if (phase !== 'get') start(); });
  document.addEventListener('keydown', function(e){ if (phase === 'run' && (e.code === 'Space' || e.key === ' ')){ e.preventDefault(); tap(); } });
  $('aw-save').addEventListener('click', function(){
    var m = parseInt($('aw-man').value, 10), l = L();
    if (isNaN(m) || m < 0 || m > 1200){ $('aw-man').focus(); return; }
    if (!l){ $('aw-l').focus(); return; }
    if (phase === 'run' || phase === 'get') return;
    last = {t: new Date().toISOString(), m: m, l: l}; var h = store(); h.push(last); keep(h);
    paintHist(); paintRes(); idle(S.saved, S.savedc);
  });
  $('aw-reset').addEventListener('click', function(){ clearInterval(iv); iv = null; setLaps(0); $('aw-sec').textContent = mmss(DUR); idle(); });
  $('aw-sex').addEventListener('click', function(e){
    var b = e.target.closest('button'); if (!b) return;
    this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); paintRes();
  });
  ['aw-age', 'aw-h', 'aw-w'].forEach(function(id){ $(id).addEventListener('input', paintRes); });
  $('aw-l').addEventListener('input', function(){ setLaps(laps); });
  var h0 = store(); if (h0.length) last = h0[h0.length - 1];
  $('aw-sec').textContent = mmss(DUR); setLaps(0); paintHist(); paintRes(); idle();
  window.__aw = {st: function(){ return [phase, laps, last && last.m]; }, ff: function(s){ t0 -= s * 1000; }};
})();
</script>
'''

page("alti-dakika-yurume-testi.html", "6 Dakika Yürüme Testi",
     "6 dakika yürüme testi: standart yönlendirme cümleleriyle süreölçer, parkur dönüş sayacı, mesafe hesabı, 30 m parkurda yaşa ve boya göre beklenen değer ve sonuç kaydı.",
     "alti-dakika-yurume-testi.html", SELF14_CSS, AW_BODY, AW_JS,
     seo_title="6 Dakika Yürüme Testi: Süreölçer, Tur Sayacı ve Beklenen Mesafe | İhsan Eren",
     about={"@type": "MedicalTest", "name": "6 dakika yürüme testi"},
     faq_items=AW_FAQ)

# -*- coding: utf-8 -*-
# Kendine iyi bak, 12. tur: evde güç devresi (haftada 2 gün kas güçlendirme zamanlayıcısı) ve 2 dakika adım testi.
# self11_part.py'den sonra exec edilir (SELF11_CSS, WAKE_JS, .gu-step, .days7 hazır).
# Kaynaklar (22 Ekim 2026'da okundu): DSÖ "Be healthy" önerileri, Momma 2022 (BJSM özeti), Currier 2023 (BJSM tam metin PDF'inin özeti),
# Penn State ve Penn State Health haberleri (FAST-2, PLOS One 2026), NHS Strength exercises (28 Şubat 2024); Shirley Ryan AbilityLab 2 Minute Step Test
# (Rikli & Jones 1999b yüzdelikleri, 2013 bağımsızlık eşikleri), Rikli & Jones 2013 Gerontologist özeti, Human Kinetics kitap alıntısı.

SELF12_CSS = SELF11_CSS + """
  .gd-stage{border:1px solid var(--line);border-radius:18px;padding:clamp(14px,2.4vw,22px);background:rgba(18,26,16,.35)}
  .gd-ex[hidden]{display:none}
  .gd-next{font-size:14px;color:var(--muted);margin:12px 0 0}
  .gd-total{font-size:14.5px;color:var(--ink-soft);margin:12px 0 0}
  .gd-total b{color:var(--ink);font-variant-numeric:tabular-nums}
  .bt-run.rest .yh-time b{color:var(--foil)}
  .gd-week{font-size:14.5px;color:var(--ink-soft);margin:14px 0 0}
  .gd-week.ok{color:#cfe0b6}
  .ad-cnt{text-align:center;font-family:var(--display);font-size:clamp(52px,9vw,76px);line-height:1;color:var(--ink);font-variant-numeric:tabular-nums;margin:2px 0 0}
  .ad-cntl{text-align:center;margin:0;font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
  .ad-man{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:10px;align-items:end;margin-top:14px}
  .ad-man input{width:100%;box-sizing:border-box;padding:10px 12px;border-radius:12px;border:1px solid var(--line-strong);background:rgba(236,229,207,.04);color:var(--ink);font:inherit;font-size:16px}
  .ad-bar{position:relative;height:14px;border-radius:999px;background:rgba(236,229,207,.08);margin:18px 0 26px}
  .ad-bar .mid{position:absolute;top:0;bottom:0;border-radius:999px;background:rgba(143,164,118,.45)}
  .ad-bar .cut{position:absolute;top:-5px;bottom:-5px;width:2px;background:var(--foil)}
  .ad-bar .me{position:absolute;top:50%;width:16px;height:16px;margin:-8px 0 0 -8px;border-radius:50%;background:#ece5cf;box-shadow:0 0 0 3px rgba(216,178,94,.55)}
  @media (max-width:520px){#ad-nt{font-size:14px}#ad-nt th{font-size:10.5px;letter-spacing:.03em}#ad-nt th,#ad-nt td{padding:8px 4px}}
  .ad-leg{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:12.5px;color:var(--muted);margin:-14px 0 6px}
  .ad-leg i{display:inline-block;width:12px;height:8px;border-radius:4px;margin-right:6px;vertical-align:middle}
"""

# ------------------------------------------------------------------ 1 · EVDE GÜÇ DEVRESİ
_ex2("gd_sts", "sts", "Sandalyeden kalkıp oturma", "Kolsuz, sağlam bir sandalyenin önüne oturun. Ellerinizi kullanmadan ayağa kalkın, yavaşça oturun. Zor gelirse ellerinizi dizlerinize koyarak destek alın.", "")
_ex2("gd_push", "sk_push", "Duvar şınavı", "Ellerinizi göğüs hizasında duvara koyun. Dirseklerinizi gövdenize yakın tutarak bükün, göğsünüzü duvara yaklaştırın ve itin. Kolaylaşınca tezgâha, daha sonra alçak bir masaya geçebilirsiniz.", "")
_ex2("gd_row", "row", "Lastik bantla kürek çekme", "Bandı bir kapı koluna ya da ayaklarınızın altına sabitleyin. Dirseklerinizi gövdenize yakın tutarak bandı kendinize doğru çekin, kürek kemiklerinizi birbirine yaklaştırın, yavaşça bırakın. Bandınız yoksa kürek kemiklerinizi sıkıştırıp birkaç saniye tutun.", "")
_ex2("gd_step", "sn_stair", "Basamak çıkma", "Tırabzana tutunarak merdivenin ilk basamağına ya da sağlam, alçak bir basamağa sırayla bir ayağınızla çıkın ve inin. Yarıda ayağınızı değiştirin.", "")
_ex2("gd_bridge", "bridge", "Köprü", "Sırtüstü uzanın, dizleriniz bükülü, ayaklarınız yerde olsun. Kalçanızı sıkıp yerden kaldırın; omuzlarınızdan dizlerinize düz bir çizgi oluşsun. Yavaşça indirin.", "")
_ex2("gd_heel", "heel2", "Topuk yükseltme", "Bir tezgâha ya da sandalye arkalığına hafifçe tutunun. İki topuğunuzu birlikte kaldırıp parmak uçlarınızda yükselin, yavaşça inin. Kolaylaşınca tutunmadan deneyin.", "")
GD_KEYS = ["gd_sts", "gd_push", "gd_row", "gd_step", "gd_bridge", "gd_heel"]
GD_STAGE = "\n".join(
    f'''            <div class="gd-ex gu-step" data-i="{i}"{" hidden" if i else ""}>
              {SV[k]}
              <div><h3>{EXT[k][0]}</h3><p>{EXT[k][1]}</p></div>
            </div>''' for i, k in enumerate(GD_KEYS))

GD_FAQ = [
 ("Neden haftada 2 gün?", "Dünya Sağlık Örgütü, 18 yaş üstü herkese haftada en az 150 dakika orta yoğunlukta hareketin yanında, haftanın en az 2 günü büyük kas gruplarını çalıştıran güçlendirme egzersizleri öneriyor. Bu devre bacak, kalça, göğüs, kol ve sırt kaslarını bir arada çalıştırır."),
 ("Ne kadar yeterli?", "16 gözlemsel çalışmayı birleştiren bir meta-analizde, kas güçlendirme egzersizi yapanlarda ölüm, kalp-damar hastalığı, kanser, diyabet ve akciğer kanseri riski %10–17 daha düşüktü. Ölüm, kalp-damar hastalığı ve kanserde en büyük azalma haftada yaklaşık 30–60 dakikada görüldü; bundan çok daha fazlasında ek yarar belirgin değildi. Güçlendirmeyi aerobik egzersizle birleştirenlerde ölüm riski %40 daha düşüktü. Bunlar ilişki gösteren çalışmalardır; neden-sonuç kanıtlamaz."),
 ("Kısa seanslar işe yarar mı?", "ABD’de Penn State Üniversitesi’nde 65 yaş üstü 97 kişiyle yapılan ve 2026’da PLOS One’da yayımlanan bir randomize çalışmada, katılımcılar her gün yaklaşık 4 dakika süren bir program yaptı: şınav, sandalyeden kalkma, lastik bantla kürek çekme ve basamak çıkma; her hareket 30 saniye, ardından 30 saniye dinlenme. Program, egzersiz yapmayan gruba göre 30 saniyede sandalyeden kalkma sayısını 4,2 tekrar, tek ayak üstünde durma süresini 3,6 saniye artırdı. Katılımcılar programı günlerin %81’inde yaptı."),
 ("Ağırlık kullanmam gerekir mi?", "Başlamak için gerekmez. 178 çalışmayı birleştiren 2023 tarihli bir analizde, incelenen bütün direnç egzersizi biçimleri hiç egzersiz yapmamaya göre kas gücünü ve kas kütlesini artırdı. Kas gücündeki en büyük artış ise daha ağır yüklerle ve birden fazla setle elde edildi. Vücut ağırlığınız ve bir lastik bantla başlayıp hareketler kolaylaştıkça zorlaştırabilirsiniz."),
 ("Ne zaman zorlaştırmalıyım?", "Çalışma süresinin sonunda hâlâ birkaç tekrar daha yapabilecek gibi hissediyorsanız hareketi zorlaştırabilirsiniz: duvar yerine tezgâhta şınav, daha sert bir bant, tutunmadan topuk yükseltme ya da tek bacakla köprü gibi. Tekrar sayısını yavaş yavaş artırmak da bir yoldur."),
 ("Kimler dikkatli olmalı?", "Kalp hastalığınız, kontrolsüz yüksek tansiyonunuz varsa, yakın zamanda ameliyat olduysanız ya da hekiminiz egzersizi kısıtladıysa önce danışın. Egzersiz sırasında nefesinizi tutmayın; göğüs ağrısı, baş dönmesi ya da keskin bir eklem ağrısı olursa durun."),
]

GD_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Evde güç devresi</h1>
    <p class="lede">Kaslarınızı güçlendirmek için spor salonuna gitmeniz gerekmiyor. Bu zamanlayıcı sizi evde, vücut ağırlığınız ve bir lastik bantla yapılan dört ya da altı hareketlik bir devreden geçirir: her hareket için çalışma ve dinlenme süresini sayar, sıradaki hareketi gösterir. Dünya Sağlık Örgütü kas güçlendirme egzersizlerini haftada en az 2 gün öneriyor; zamanlayıcı bu haftaki günlerinizi de sayar.</p>
    <p class="meta">Son güncelleme: 22 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>Haftada 2 gün</b><span>Büyük kas gruplarını çalıştıran güçlendirme egzersizi önerisi (DSÖ)</span></div>
        <div class="stat"><b>30–60 dk</b><span>Haftalık güçlendirmede ölüm ve kalp-damar riskindeki en büyük azalmanın görüldüğü süre (gözlemsel)</span></div>
        <div class="stat"><b>4 dakika</b><span>65 yaş üstünde günde 4 dakikalık programla sandalyeden kalkma sayısı arttı (randomize çalışma)</span></div>
        <div class="stat"><b>178 çalışma</b><span>İncelenen bütün direnç egzersizi biçimleri kas gücünü artırdı</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Zamanlayıcıyla birlikte yapın</p>
      <h2>Devrenizi seçin ve başlayın</h2>
      <p class="soft">Hareket sayısını, çalışma süresini ve tur sayısını seçin. Çalışma süresi boyunca hareketi kontrollü bir tempoda tekrarlayın, dinlenme süresinde sıradaki harekete hazırlanın. Sesi açarsanız geçişlerde bip sesi duyarsınız; isterseniz hareketlerin adı da sesli okunur.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <p class="lbl">Hareket sayısı</p>
            <div class="seg" role="group" aria-label="Hareket sayısı" id="gd-n">
              <button type="button" data-v="4" aria-pressed="true">4 hareket</button>
              <button type="button" data-v="6" aria-pressed="false">6 hareket</button>
            </div>
            <p class="lbl" style="margin-top:12px">Çalışma ve dinlenme</p>
            <div class="seg" role="group" aria-label="Çalışma ve dinlenme" id="gd-w">
              <button type="button" data-v="30" aria-pressed="true">30 sn + 30 sn</button>
              <button type="button" data-v="40" aria-pressed="false">40 sn + 20 sn</button>
            </div>
            <p class="lbl" style="margin-top:12px">Tur</p>
            <div class="seg" role="group" aria-label="Tur" id="gd-r">
              <button type="button" data-v="1" aria-pressed="true">1</button>
              <button type="button" data-v="2" aria-pressed="false">2</button>
              <button type="button" data-v="3" aria-pressed="false">3</button>
            </div>
            <p class="gd-total" id="gd-total"></p>
            <label class="mz-chk"><input type="checkbox" id="gd-sound" checked> Sesli uyarı</label>
            <label class="mz-chk"><input type="checkbox" id="gd-say"> Hareketin adını sesli oku</label>
          </div>
          <div class="bt-out">
            <div class="gd-stage" id="gd-stage">
{GD_STAGE}
            </div>
            <div class="gu-dots" id="gd-dots" aria-hidden="true"></div>
            <p class="gd-next" id="gd-next"></p>
            <p class="gd-week" id="gd-week"></p>
            <div class="days7" id="gd-days" aria-label="Son 7 gün"></div>
          </div>
          <div class="bt-run" id="gd-run">
            <div class="yh-time"><b id="gd-sec">–</b><span>saniye</span></div>
            <p class="bt-phase" id="gd-phase" aria-live="polite">Hazır</p>
            <p class="bt-cue" id="gd-cue">Hareketleri bir kez gözden geçirin, sonra Başla’ya basın.</p>
            <button type="button" class="bt-tap" id="gd-go">Başla</button>
            <div class="controls" style="margin-top:10px;justify-content:center">
              <button type="button" class="cta ghost" id="gd-skip">Sonraki</button>
              <button type="button" class="cta ghost" id="gd-reset">Sıfırla</button>
            </div>
          </div>
        </div>
        <div class="gd-strings" hidden>
          <span data-k="ready">Hazır</span>
          <span data-k="readyc">Hareketleri bir kez gözden geçirin, sonra Başla’ya basın.</span>
          <span data-k="start">Başla</span>
          <span data-k="stop">Durdur</span>
          <span data-k="get">Hazırlanın</span>
          <span data-k="getc">İlk hareket birazdan başlıyor.</span>
          <span data-k="work">Çalışın</span>
          <span data-k="workc">Kontrollü bir tempoyla tekrarlayın; nefesinizi tutmayın.</span>
          <span data-k="rest">Dinlenin</span>
          <span data-k="restc">Nefeslenin ve sıradaki harekete hazırlanın.</span>
          <span data-k="done">Devre tamam</span>
          <span data-k="donec">Bugünkü güçlendirmenizi yaptınız. Haftada en az 2 günü hedefleyin.</span>
          <span data-k="paused">Durduruldu</span>
          <span data-k="pausedc">Kaldığınız yerden devam etmek için Başla’ya basın.</span>
          <span data-k="next">Sıradaki: {{x}}</span>
          <span data-k="pos">Hareket {{i}} / {{n}} · Tur {{r}} / {{t}}</span>
          <span data-k="total">Toplam süre: yaklaşık <b>{{m}} dakika</b></span>
          <span data-k="week">Bu hafta güçlendirme yaptığınız gün: {{n}} · hedef en az 2</span>
          <span data-k="weekok">Bu hafta {{n}} gün güçlendirme yaptınız; haftalık hedefe ulaştınız.</span>
          <span data-k="sgo">Başlayın</span>
          <span data-k="snext">Sıradaki hareket</span>
          <span data-k="sdone">Devre tamam. Tebrikler.</span>
          <span data-k="d0">Pzt</span><span data-k="d1">Sal</span><span data-k="d2">Çar</span><span data-k="d3">Per</span><span data-k="d4">Cum</span><span data-k="d5">Cmt</span><span data-k="d6">Paz</span>
        </div>
      </div>
      <p class="count">Hangi günlerde devre yaptığınız yalnızca bu cihazda saklanır; hiçbir yere gönderilmez.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Başlamadan önce</h2>
        <ul class="dots">
          <li>Kolsuz, tekerleksiz ve kaymayan sağlam bir sandalye kullanın.</li>
          <li>Rahat giysiler giyin, yanınızda su bulundurun.</li>
          <li>Birkaç dakika yerinde yürüyerek ya da kollarınızı sallayarak ısının.</li>
          <li>İlk haftalarda 4 hareket ve 1 turla başlayın, kademeli artırın.</li>
        </ul>
      </div>
      <div>
        <h2>Doğru yapmak için</h2>
        <ul class="dots">
          <li>Hızdan çok kontrol: her tekrarı yavaş ve tam yapın.</li>
          <li>Zorlandığınız kısımda nefes verin, nefesinizi tutmayın.</li>
          <li>Çömelme ve şınavda sırtınızı düz tutun; kalkarken kollarınızla değil bacaklarınızla itin.</li>
          <li>Hafif bir kas yorgunluğu normaldir; keskin eklem ağrısı olursa o hareketi atlayın.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(GD_FAQ)}
      <p class="soft" style="margin-top:18px">Bacak gücünüzü ölçmek için <a href="sandalye-testi.html">30 saniye sandalye testine</a>, gün içine yayılan kısa hareketler için <a href="hareket-atistirmaliklari.html">hareket atıştırmalıklarına</a>, haftalık hareket hedefiniz için <a href="hareket.html">ne kadar hareket yeterli</a> sayfasına bakabilirsiniz.</p>
      {CTA_CARD("Size özel bir güçlendirme programı", "kişiye özel güçlendirme programı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "World Health Organization. " + ext("https://who.int/initiatives/behealthy/physical-activity", "Physical activity: recommendations for adults and older adults") + ".",
        "Bull FC, Al-Ansari SS, Biddle S, et al. " + ext("https://bjsm.bmj.com/content/54/24/1451", "World Health Organization 2020 guidelines on physical activity and sedentary behaviour") + ". Br J Sports Med. 2020;54(24):1451–1462.",
        "Momma H, Kawakami R, Honda T, Sawada SS. " + ext("https://bjsm.bmj.com/content/56/13/755", "Muscle-strengthening activities are associated with lower risk and mortality in major non-communicable diseases: a systematic review and meta-analysis of cohort studies") + ". Br J Sports Med. 2022;56(13):755–763.",
        "Currier BS, Mcleod JC, Banfield L, et al. " + ext("https://bjsm.bmj.com/content/bjsports/57/18/1211.full.pdf", "Resistance training prescription for muscle strength and hypertrophy in healthy adults: a systematic review and Bayesian network meta-analysis") + ". Br J Sports Med. 2023;57:1211–1220.",
        "Sciamanna C, et al. FAST-2 randomised controlled trial. PLOS One. 2026. " + ext("https://doi.org/10.1371/journal.pone.0336748", "doi:10.1371/journal.pone.0336748") + ". Haber: " + ext("https://www.psu.edu/news/research/story/four-minute-daily-workout-improves-strength-balance-older-adults", "Penn State News, 9 June 2026") + ".",
        "NHS. " + ext("https://www.nhs.uk/live-well/exercise/strength-exercises", "Strength exercises") + ". Page last reviewed 28 February 2024.",
      ])}
    </div>
  </section>
</main>'''

GD_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.gd-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var EN = document.documentElement.lang === 'en', LANG = EN ? 'en-GB' : 'tr-TR';
  var $ = function(id){ return document.getElementById(id); }, KEY = 'drihsaneren.guc.v1';
  var lock = null, ctx = null, snd = $('gd-sound'), sayBox = $('gd-say');
''' + WAKE_JS + '''
  var EX = [].slice.call(root.querySelectorAll('.gd-ex')), NAMES = EX.map(function(e){ return e.querySelector('h3').textContent; });
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function seg(id){ return +$(id).querySelector('[aria-pressed="true"]').getAttribute('data-v'); }
  function say(t){ if (!sayBox.checked || !('speechSynthesis' in window)) return; try { speechSynthesis.cancel(); var u = new SpeechSynthesisUtterance(t); u.lang = LANG; u.rate = .95; speechSynthesis.speak(u); } catch (e) {} }
  function load(){ try { return JSON.parse(localStorage.getItem(KEY)) || {d: {}}; } catch (e) { return {d: {}}; } }
  function save(o){ try { localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {} }
  function dkey(d){ return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2); }
  function paintDays(){
    var o = load(), box = $('gd-days'), now = new Date(); box.innerHTML = '';
    for (var i = 6; i >= 0; i--){
      var d = new Date(now.getFullYear(), now.getMonth(), now.getDate() - i), n = o.d[dkey(d)] || 0, el = document.createElement('div');
      el.innerHTML = '<b>' + n + '</b>' + S['d' + ((d.getDay() + 6) % 7)];
      if (n) el.classList.add('on'); if (!i) el.classList.add('now');
      box.appendChild(el);
    }
    var mon = new Date(now.getFullYear(), now.getMonth(), now.getDate() - ((now.getDay() + 6) % 7)), wk = 0;
    for (var j = 0; j < 7; j++){ var dd = new Date(mon.getFullYear(), mon.getMonth(), mon.getDate() + j); if (o.d[dkey(dd)]) wk++; }
    var w = $('gd-week'); w.textContent = fill(wk >= 2 ? S.weekok : S.week, {n: wk}); w.classList.toggle('ok', wk >= 2);
  }
  function order(){ var n = seg('gd-n'), a = []; for (var i = 0; i < n; i++) a.push(i); return a; }
  function build(){
    var w = seg('gd-w'), rest = 60 - w, rounds = seg('gd-r'), o = order(), p = [['get', 5, o[0], 1, 1]];
    for (var r = 1; r <= rounds; r++) o.forEach(function(ex, i){
      p.push(['work', w, ex, r, i + 1]);
      var last = r === rounds && i === o.length - 1;
      if (!last) p.push(['rest', rest, i + 1 < o.length ? o[i + 1] : o[0], i + 1 < o.length ? r : r + 1, i + 1 < o.length ? i + 2 : 1]);
    });
    return p;
  }
  function total(){ var w = seg('gd-w'), n = seg('gd-n'), r = seg('gd-r'); return Math.round((5 + n * r * 60 - (60 - w)) / 60); }
  function paintTotal(){ $('gd-total').innerHTML = fill(S.total, {m: total()}); }
  function showEx(i){ EX.forEach(function(e, j){ e.hidden = j !== i; }); }
  function dots(cur){
    var o = order(), box = $('gd-dots'); box.innerHTML = '';
    o.forEach(function(ex, i){ var d = document.createElement('i'); if (i < cur) d.className = 'on'; box.appendChild(d); });
  }
  var plan = [], idx = 0, t0 = 0, left = 0, run = false, iv = null, lastBeep = -1;
  function show(st){
    var k = st[0], o = order();
    $('gd-phase').textContent = S[k]; $('gd-cue').textContent = S[k + 'c'];
    $('gd-run').classList.toggle('rest', k === 'rest' || k === 'get');
    showEx(st[2]);
    $('gd-next').textContent = (k === 'work' ? fill(S.pos, {i: st[4], n: o.length, r: st[3], t: seg('gd-r')}) : fill(S.next, {x: NAMES[st[2]]}));
    dots(k === 'work' ? st[4] : st[4] - 1);
    if (k === 'work'){ beep(880, .45, .22); say(S.sgo + '. ' + NAMES[st[2]]); }
    if (k === 'rest'){ beep(520, .3, .18); say(S.snext + ': ' + NAMES[st[2]]); }
    if (k === 'get') say(NAMES[st[2]]);
    lastBeep = -1;
  }
  function enter(i){ idx = i; left = plan[i][1]; t0 = performance.now(); show(plan[i]); }
  function tick(){
    var rem = left - (performance.now() - t0) / 1000, c = Math.ceil(rem);
    $('gd-sec').textContent = String(Math.max(0, c));
    if (c <= 3 && c >= 1 && c !== lastBeep){ lastBeep = c; beep(660, .12, .14); }
    if (rem > 0) return;
    if (idx + 1 < plan.length) enter(idx + 1); else finish();
  }
  function finish(){
    clearInterval(iv); iv = null; run = false; wake(false); $('gd-run').classList.remove('rest');
    beep(660, .2, .18); setTimeout(function(){ beep(880, .2, .18); }, 220); setTimeout(function(){ beep(1100, .35, .18); }, 440); say(S.sdone);
    var o = load(), k = dkey(new Date()); o.d[k] = (o.d[k] || 0) + 1;
    var ks = Object.keys(o.d).sort(); while (ks.length > 120) delete o.d[ks.shift()];
    save(o); paintDays(); dots(order().length);
    $('gd-phase').textContent = S.done; $('gd-cue').textContent = S.donec; $('gd-sec').textContent = '✓'; $('gd-next').textContent = '';
    $('gd-go').textContent = S.start; $('gd-go').classList.remove('stop'); plan = [];
  }
  ['gd-n', 'gd-w', 'gd-r'].forEach(function(id){
    $(id).addEventListener('click', function(e){
      var b = e.target.closest('button'); if (!b || run || plan.length) return;
      this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      paintTotal(); dots(0);
    });
  });
  $('gd-go').addEventListener('click', function(){
    if (run){
      clearInterval(iv); iv = null; run = false; wake(false); left = Math.max(0, left - (performance.now() - t0) / 1000);
      $('gd-phase').textContent = S.paused; $('gd-cue').textContent = S.pausedc;
      this.textContent = S.start; this.classList.remove('stop'); return;
    }
    run = true; wake(true); this.textContent = S.stop; this.classList.add('stop');
    try { ctx = ctx || new (window.AudioContext || window.webkitAudioContext)(); if (ctx.resume) ctx.resume(); } catch (e) {}
    if (!plan.length){ plan = build(); enter(0); } else { t0 = performance.now(); show(plan[idx]); }
    clearInterval(iv); iv = setInterval(tick, 100); tick();
  });
  $('gd-skip').addEventListener('click', function(){ if (!plan.length) return; if (idx + 1 < plan.length){ var r = run; enter(idx + 1); if (!r) { $('gd-phase').textContent = S.paused; $('gd-cue').textContent = S.pausedc; } } else finish(); });
  $('gd-reset').addEventListener('click', function(){
    clearInterval(iv); iv = null; run = false; wake(false); plan = []; $('gd-run').classList.remove('rest');
    try { speechSynthesis.cancel(); } catch (e) {}
    $('gd-sec').textContent = '–'; $('gd-phase').textContent = S.ready; $('gd-cue').textContent = S.readyc; $('gd-next').textContent = '';
    $('gd-go').textContent = S.start; $('gd-go').classList.remove('stop'); showEx(0); dots(0);
  });
  paintTotal(); paintDays(); dots(0);
  window.__gd = {st: function(){ return [run, idx, plan.length, plan[idx] && plan[idx][0], plan[idx] && plan[idx][2]]; }, skip: function(){ left = 0; t0 = performance.now(); }};
})();
</script>
'''

page("guc-devresi.html", "Evde Güç Devresi",
     "Haftada 2 gün kas güçlendirme: vücut ağırlığı ve lastik bantla 4 ya da 6 hareketlik ev devresi, sesli çalışma-dinlenme zamanlayıcısı, haftalık takip ve araştırmaların söyledikleri.",
     "guc-devresi.html", SELF12_CSS, GD_BODY, GD_JS,
     seo_title="Evde Güç Devresi: Haftada 2 Gün Kas Güçlendirme Zamanlayıcısı | İhsan Eren",
     about={"@type": "ExercisePlan", "name": "Evde kas güçlendirme devresi"},
     faq_items=GD_FAQ)

# ------------------------------------------------------------------ 2 · 2 DAKİKA ADIM TESTİ
# Rikli & Jones 1999b yüzdelikleri (10., 25., 50., 75., 90.) ve 2013 bağımsızlık eşikleri; Shirley Ryan AbilityLab'dan.
AD_AGES = ["60–64", "65–69", "70–74", "75–79", "80–84", "85–89", "90–94"]
AD_M = [[74, 87, 101, 115, 128], [72, 86, 101, 116, 130], [66, 80, 95, 110, 125], [56, 73, 91, 109, 125], [56, 71, 87, 103, 118], [44, 59, 75, 91, 106], [36, 52, 69, 86, 102]]
AD_F = [[60, 75, 91, 107, 122], [57, 73, 90, 107, 123], [53, 68, 84, 101, 116], [52, 68, 84, 100, 115], [46, 60, 75, 91, 104], [42, 55, 70, 85, 98], [31, 44, 58, 72, 85]]
AD_CUT_M = [106, 101, 95, 88, 80, 71, 60]
AD_CUT_F = [97, 93, 89, 84, 78, 70, 60]
AD_ROWS = "\n".join(f'<tr data-i="{i}"><td>{a}</td><td>{f[1]}–{f[3]}</td><td>{AD_CUT_F[i]}</td><td>{m[1]}–{m[3]}</td><td>{AD_CUT_M[i]}</td></tr>'
                    for i, (a, f, m) in enumerate(zip(AD_AGES, AD_F, AD_M)))

AD_FAQ = [
 ("Bu test neyi ölçer?", "Aerobik dayanıklılığınızı, yani yürümek, merdiven çıkmak ve günlük işleri yorulmadan sürdürebilmek için gereken kondisyonu. 60 yaş üstü kişiler için geliştirilen Kıdemli Fitness Testi’nin bir parçasıdır; uzun bir yürüme alanı gerektirmediği için evde de yapılabilir. Küçük çalışmalarda sonuçları, 1 mil (yaklaşık 1,6 km) yürüme süresiyle ve koşu bandı testiyle iyi uyum gösterdi."),
 ("Dizimi ne kadar kaldırmalıyım?", "Diz kapağınızın ortası ile kalça kemiğinizin en üst noktası (leğen kemiği kenarı) arasındaki mesafenin yarısına kadar. Bu yüksekliği ayakta dururken bir mezurayla bulun ve yanınızdaki duvara bir bantla işaretleyin. Yalnızca sağ dizinizin bu işarete ulaştığı adımlar sayılır."),
 ("Tutunabilir miyim?", "Evet. Dengeniz iyi değilse bir duvara, masaya ya da sandalye arkalığına tutunarak yapabilirsiniz. Güvenlik için yanınızda biri bulunsun; adımları o da sayabilir."),
 ("Değerler neye göre?", "Tablodaki aralıklar, ABD’de 60–94 yaş arası 7.183 kişiden elde edilen değerlerde yaşıtların ortadaki yarısını (25. ile 75. yüzdelik) gösterir. Bağımsızlık eşikleri ise aynı araştırmacıların 2013’te yayımladığı ve 90’lı yaşlara kadar kendi başına yaşamayı sürdürmek için gereken kondisyonu hedefleyen değerlerdir. Bu eşikler, ileride beklenen düşüş hesaba katılarak belirlendiği için genç yaş gruplarında ortalamanın biraz üstündedir."),
 ("60 yaşından gencim, sonucum neyi gösterir?", "Bu testin karşılaştırma değerleri 60–94 yaş için. Daha genç yaştaysanız sonucunuzu kaydedip birkaç haftada bir tekrarlayarak kendi gidişatınızı izleyebilirsiniz."),
 ("Sonucumu nasıl iyileştiririm?", "Düzenli aerobik hareketle: Dünya Sağlık Örgütü haftada en az 150 dakika orta yoğunlukta hareket öneriyor; tempolu yürüyüş bunun en kolay yolu. Bacak kaslarını güçlendirmek de yardımcı olur. Testi birkaç haftada bir aynı koşullarda tekrarlayın; tek seferlik küçük farklar ölçüm hatası olabilir, eğilime bakın."),
]

AD_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>2 dakika adım testi</h1>
    <p class="lede">Kondisyonunuzu ölçmek için koşu bandına ya da uzun bir koridora gerek yok. 2 dakika boyunca yerinde adım atıp sağ dizinizin belirli bir yüksekliğe kaç kez ulaştığını sayarsınız. Bu sayfa süreyi tutar, adımları saymanıza yardım eder ve 60–94 yaş için sonucunuzu yaşıtlarınızla ve ileri yaşlarda bağımsızlıkla ilişkilendirilen eşikle karşılaştırır.</p>
    <p class="meta">Son güncelleme: 22 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>2 dakika</b><span>Yerinde adım atma süresi; sağ dizin hedef yüksekliğe ulaştığı adımlar sayılır</span></div>
        <div class="stat"><b>7.183 kişi</b><span>Yaşa ve cinsiyete göre karşılaştırma değerlerinin elde edildiği 60–94 yaş arası yetişkinler</span></div>
        <div class="stat"><b>0,90</b><span>Testin tekrarlandığında tutarlılığı (ICC; 1 en yüksek)</span></div>
        <div class="stat"><b>60–106</b><span>Yaşa ve cinsiyete göre bağımsızlık eşikleri (adım)</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Kendinizi ölçün</p>
      <h2>Testi yapın</h2>
      <p class="soft">Duvara diz yüksekliğini işaretleyin, yaşınızı ve cinsiyetinizi seçin, Başla’ya basın. 3 saniyelik hazırlıktan sonra 2 dakika boyunca yerinde adım atın. Yanınızdaki kişi sağ diziniz işarete her ulaştığında büyük düğmeye dokunsun; yalnızsanız sesli sayın ve sonunda sayıyı yazın.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <p class="lbl"><label for="ad-age">Yaşınız</label></p>
            <input class="cs-age" id="ad-age" type="number" inputmode="numeric" min="18" max="110" placeholder="ör. 70">
            <p class="lbl" style="margin-top:12px">Cinsiyet</p>
            <div class="seg" role="group" aria-label="Cinsiyet" id="ad-sex">
              <button type="button" data-v="f" aria-pressed="true">Kadın</button>
              <button type="button" data-v="m" aria-pressed="false">Erkek</button>
            </div>
            <label class="mz-chk"><input type="checkbox" id="ad-sound" checked> Sesli uyarı</label>
            <div class="ad-man">
              <div><p class="lbl"><label for="ad-man">Adım sayısı</label></p><input id="ad-man" type="number" inputmode="numeric" min="0" max="250" placeholder="ör. 85"></div>
              <button type="button" class="cta" id="ad-save">Kaydet</button>
            </div>
          </div>
          <div class="bt-out">
            <div class="res" id="ad-res" hidden>
              <p class="lab" id="ad-lab"></p>
              <div class="ad-bar" id="ad-bar" hidden><i class="mid" id="ad-mid"></i><i class="cut" id="ad-cut"></i><i class="me" id="ad-me"></i></div>
              <p class="ad-leg" id="ad-leg" hidden><span><i style="background:rgba(143,164,118,.6)"></i>Yaşıtlarınızın ortadaki yarısı</span><span><i style="background:#d8b25e;width:3px"></i>Bağımsızlık eşiği</span></p>
              <p id="ad-txt"></p>
              <span class="bt-badge" id="ad-badge" hidden></span>
            </div>
            <div id="ad-histw" style="margin-top:20px" hidden>
              <p class="lbl">Önceki sonuçlarınız (bu cihazda)</p>
              <ul class="cs-hist" id="ad-hist"></ul>
            </div>
          </div>
          <div class="bt-run">
            <div class="yh-time"><b id="ad-sec">2:00</b><span>kalan süre</span></div>
            <p class="ad-cnt" id="ad-cnt">0</p><p class="ad-cntl">adım</p>
            <p class="bt-phase" id="ad-phase" aria-live="polite">Hazır</p>
            <p class="bt-cue" id="ad-cue">İşaretin önünde durun ve Başla’ya basın.</p>
            <button type="button" class="bt-tap" id="ad-go">Başla</button>
            <div class="controls" style="margin-top:10px;justify-content:center">
              <button type="button" class="cta ghost" id="ad-reset">Sıfırla</button>
            </div>
          </div>
        </div>
        <div class="ad-strings" hidden>
          <span data-k="ready">Hazır</span>
          <span data-k="readyc">İşaretin önünde durun ve Başla’ya basın.</span>
          <span data-k="start">Başla</span>
          <span data-k="get">Hazır olun</span>
          <span data-k="getc">Birazdan başlıyor.</span>
          <span data-k="run">Yerinde adım atın</span>
          <span data-k="runc">Sağ diz işarete her ulaştığında dokunun.</span>
          <span data-k="tap">+1 adım</span>
          <span data-k="half">1 dakika kaldı</span>
          <span data-k="last">Son 30 saniye</span>
          <span data-k="done">Süre doldu</span>
          <span data-k="donec">Sayıyı kontrol edin, gerekirse düzeltip Kaydet’e basın.</span>
          <span data-k="saved">Sonuç kaydedildi</span>
          <span data-k="savedc">Birkaç hafta sonra testi aynı koşullarda tekrarlayabilirsiniz.</span>
          <span data-k="lab">Sonucunuz: {{n}} adım</span>
          <span data-k="noage">Yaşıtlarınızla karşılaştırmak için yaşınızı girin.</span>
          <span data-k="young">Karşılaştırma değerleri 60–94 yaş için. Sonucunuzu kaydedip kendi gidişatınızı izleyebilirsiniz.</span>
          <span data-k="mid">Yaşıtlarınızın ortadaki yarısı {{a}}–{{b}} adım.</span>
          <span data-k="p0">Sonucunuz yaşıtlarınızın en düşük %10’luk dilimi içinde.</span>
          <span data-k="p1">Sonucunuz yaşıtlarınızın ortalamasının altında.</span>
          <span data-k="p2">Sonucunuz yaşıtlarınızın ortalama aralığında.</span>
          <span data-k="p3">Sonucunuz yaşıtlarınızın ortalamasının üstünde.</span>
          <span data-k="p4">Sonucunuz yaşıtlarınızın en yüksek %10’luk dilimi içinde.</span>
          <span data-k="cutok">Yaşınız ve cinsiyetiniz için önerilen bağımsızlık eşiği ({{c}} adım) düzeyinde ya da üstündesiniz.</span>
          <span data-k="cutno">Yaşınız ve cinsiyetiniz için önerilen bağımsızlık eşiğinin ({{c}} adım) altındasınız. Bu bir tanı değildir; düzenli yürüyüş ve güçlendirmeyle kondisyonunuzu artırabilir, bir fizyoterapistle konuşabilirsiniz.</span>
          <span data-k="bok">Eşikte ya da üstünde</span>
          <span data-k="bno">Eşiğin altında</span>
          <span data-k="steps">adım</span>
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
          <li><span>Ayakta durun. Diz kapağınızın ortası ile kalça kemiğinizin en üst noktası arasındaki mesafeyi ölçün; <strong>yarısını</strong> bulun.</span></li>
          <li><span>Bu yüksekliği yanınızdaki duvara bir bantla işaretleyin. Gerekirse duvara ya da sandalye arkalığına tutunabilirsiniz.</span></li>
          <li><span>Başla’ya basın ve <strong>2 dakika</strong> boyunca yerinde, dizlerinizi işarete kadar kaldırarak adım atın.</span></li>
          <li><span>Yalnızca <strong>sağ dizinizin</strong> işarete ulaştığı adımlar sayılır. Durmanız gerekirse durun; süre işlemeye devam eder.</span></li>
        </ol>
        <div class="callout">
          <p>Göğüs ağrısı, baş dönmesi, belirgin nefes darlığı ya da bacaklarda ağrı olursa testi bırakın. Kalp hastalığınız varsa ya da hekiminiz egzersizi kısıtladıysa önce danışın.</p>
        </div>
      </div>
      <div>
        <h2>Yaşa göre değerler</h2>
        <p class="soft">Yaşıtların ortadaki yarısı (25.–75. yüzdelik) ve ileri yaşlarda bağımsızlıkla ilişkilendirilen eşik, adım sayısı olarak.</p>
        <table class="nt" id="ad-nt">
          <thead><tr><th>Yaş</th><th>Kadın</th><th>Eşik</th><th>Erkek</th><th>Eşik</th></tr></thead>
          <tbody>
{AD_ROWS}
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(AD_FAQ)}
      <p class="soft" style="margin-top:18px">Bacak gücünüz için <a href="sandalye-testi.html">30 saniye sandalye testine</a>, yürüyüşünüz için <a href="yurume-hizi-testi.html">yürüme hızı testine</a>, kondisyonunuzu artırmak için <a href="tempolu-yuruyus.html">tempolu yürüyüş metronomuna</a> bakabilirsiniz.</p>
      {CTA_CARD("Kondisyonunuz ve egzersiz programınız", "2 dakika adım testi ve kondisyon değerlendirmesi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Shirley Ryan AbilityLab. " + ext("https://www.sralab.org/rehabilitation-measures/2-minute-step-test", "2 Minute Step Test") + ". Rehabilitation Measures Database. Last updated 1 August 2021.",
        "Rikli RE, Jones CJ. Development and validation of a functional fitness test for community-residing older adults. J Aging Phys Act. 1999;7(2):129–161.",
        "Rikli RE, Jones CJ. Functional fitness normative scores for community-residing older adults, ages 60–94. J Aging Phys Act. 1999;7(2):162–181.",
        "Rikli RE, Jones CJ. " + ext("https://academic.oup.com/gerontologist/article/53/2/255/560735", "Development and validation of criterion-referenced clinically relevant fitness standards for maintaining physical independence in later years") + ". Gerontologist. 2013;53(2):255–267.",
        "Human Kinetics. " + ext("https://us.humankinetics.com/blogs/excerpt/identifying-the-recommended-senior-fitness-standards", "Identifying the recommended senior fitness standards") + ". Excerpt from Rikli RE, Jones CJ. Senior Fitness Test Manual. 2nd ed.",
        "World Health Organization. " + ext("https://who.int/initiatives/behealthy/physical-activity", "Physical activity: recommendations for adults and older adults") + ".",
      ])}
    </div>
  </section>
</main>'''

AD_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.ad-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var EN = document.documentElement.lang === 'en';
  var $ = function(id){ return document.getElementById(id); }, KEY = 'drihsaneren.adim2.v1';
  var P = {m: ''' + str(AD_M) + ''', f: ''' + str(AD_F) + '''}, CUT = {m: ''' + str(AD_CUT_M) + ''', f: ''' + str(AD_CUT_F) + '''};
  var lock = null, ctx = null, snd = $('ad-sound');
''' + WAKE_JS + '''
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function sex(){ return $('ad-sex').querySelector('[aria-pressed="true"]').getAttribute('data-v'); }
  function age(){ var a = parseInt($('ad-age').value, 10); return isNaN(a) ? null : a; }
  function band(a){ if (a == null || a < 60 || a > 94) return -1; return Math.min(6, Math.floor((a - 60) / 5)); }
  function store(){ try { return JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { return []; } }
  function keep(l){ try { localStorage.setItem(KEY, JSON.stringify(l.slice(-10))); } catch (e) {} }
  var phase = 'idle', t0 = 0, iv = null, cnt = 0, last = null, cues = {}, endT = 0;
  function mmss(s){ s = Math.max(0, Math.ceil(s)); var m = Math.floor(s / 60), r = s % 60; return m + ':' + (r < 10 ? '0' : '') + r; }
  function paintNorm(){ var b = band(age()); $('ad-nt').querySelectorAll('tbody tr').forEach(function(r){ r.classList.toggle('me', +r.getAttribute('data-i') === b); }); }
  function paintRes(){
    var res = $('ad-res'); if (last == null){ res.hidden = true; return; }
    res.hidden = false; $('ad-lab').textContent = fill(S.lab, {n: last});
    var a = age(), b = band(a), badge = $('ad-badge'), bar = $('ad-bar'), leg = $('ad-leg'), txt;
    if (a == null || b < 0){ txt = a == null ? S.noage : S.young; bar.hidden = leg.hidden = badge.hidden = true; $('ad-txt').textContent = txt; return; }
    var p = P[sex()][b], c = CUT[sex()][b], i = last < p[0] ? 0 : last < p[1] ? 1 : last <= p[3] ? 2 : last <= p[4] ? 3 : 4;
    txt = fill(S.mid, {a: p[1], b: p[3]}) + ' ' + S['p' + i] + ' ' + fill(last >= c ? S.cutok : S.cutno, {c: c});
    $('ad-txt').textContent = txt;
    var lo = 20, hi = 160, pos = function(x){ return Math.max(0, Math.min(100, (x - lo) / (hi - lo) * 100)) + '%'; };
    $('ad-mid').style.left = pos(p[1]); $('ad-mid').style.width = ((p[3] - p[1]) / (hi - lo) * 100) + '%';
    $('ad-cut').style.left = pos(c); $('ad-me').style.left = pos(last); bar.hidden = leg.hidden = false;
    badge.hidden = false; badge.textContent = last >= c ? S.bok : S.bno; badge.classList.toggle('no', last < c);
  }
  function paintHist(){
    var h = store(), ul = $('ad-hist'); $('ad-histw').hidden = !h.length; ul.innerHTML = '';
    h.slice().reverse().forEach(function(r){
      var li = document.createElement('li'), sp = document.createElement('span'), bb = document.createElement('b');
      sp.textContent = new Date(r.t).toLocaleDateString(EN ? 'en-GB' : 'tr-TR', {day: 'numeric', month: 'short', year: 'numeric'});
      bb.textContent = r.n + ' ' + S.steps; li.appendChild(sp); li.appendChild(bb); ul.appendChild(li);
    });
  }
  function setCnt(n){ cnt = n; $('ad-cnt').textContent = String(n); }
  function idle(p, c){
    phase = 'idle'; clearInterval(iv); iv = null; wake(false);
    $('ad-go').textContent = S.start; $('ad-go').classList.remove('stop');
    $('ad-phase').textContent = p || S.ready; $('ad-cue').textContent = c || S.readyc;
  }
  function tick(){
    var el = (performance.now() - t0) / 1000;
    if (phase === 'get'){
      $('ad-sec').textContent = mmss(120);
      if (el >= 3){ phase = 'run'; t0 = performance.now(); beep(880, .5, .22); $('ad-phase').textContent = S.run; $('ad-cue').textContent = S.runc; $('ad-go').textContent = S.tap; $('ad-go').classList.add('stop'); }
      return;
    }
    var rem = 120 - el; $('ad-sec').textContent = mmss(rem);
    if (rem <= 60 && !cues.h){ cues.h = 1; beep(660, .25, .18); $('ad-phase').textContent = S.half; }
    if (rem <= 30 && !cues.l){ cues.l = 1; beep(660, .25, .18); setTimeout(function(){ beep(660, .25, .18); }, 300); $('ad-phase').textContent = S.last; }
    if (rem <= 0) end();
  }
  function end(){
    clearInterval(iv); iv = null; wake(false); phase = 'end'; endT = performance.now(); $('ad-sec').textContent = mmss(0);
    beep(660, .2, .18); setTimeout(function(){ beep(880, .2, .18); }, 220); setTimeout(function(){ beep(1100, .35, .18); }, 440);
    $('ad-man').value = cnt; $('ad-go').textContent = S.start; $('ad-go').classList.remove('stop');
    $('ad-phase').textContent = S.done; $('ad-cue').textContent = S.donec; $('ad-man').focus();
  }
  function start(){
    setCnt(0); cues = {}; phase = 'get'; t0 = performance.now(); wake(true);
    try { ctx = ctx || new (window.AudioContext || window.webkitAudioContext)(); if (ctx.resume) ctx.resume(); } catch (e) {}
    beep(520, .15, .16); $('ad-phase').textContent = S.get; $('ad-cue').textContent = S.getc;
    clearInterval(iv); iv = setInterval(tick, 100); tick();
  }
  function tap(){ if (phase !== 'run') return; setCnt(cnt + 1); beep(990, .05, .08); }
  $('ad-go').addEventListener('click', function(){ if (phase === 'run') tap(); else if (phase === 'end' && performance.now() - endT < 2500) return; else if (phase !== 'get') start(); });
  document.addEventListener('keydown', function(e){ if (phase === 'run' && (e.code === 'Space' || e.key === ' ')){ e.preventDefault(); tap(); } });
  $('ad-save').addEventListener('click', function(){
    var n = parseInt($('ad-man').value, 10); if (isNaN(n) || n < 0 || n > 250){ $('ad-man').focus(); return; }
    if (phase === 'run' || phase === 'get') return;
    last = n; setCnt(n); var h = store(); h.push({t: new Date().toISOString(), n: n}); keep(h);
    paintHist(); paintRes(); idle(S.saved, S.savedc); phase = 'idle';
  });
  $('ad-reset').addEventListener('click', function(){ clearInterval(iv); iv = null; setCnt(0); $('ad-sec').textContent = mmss(120); idle(); });
  $('ad-sex').addEventListener('click', function(e){
    var b = e.target.closest('button'); if (!b) return;
    this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); paintRes();
  });
  $('ad-age').addEventListener('input', function(){ paintNorm(); paintRes(); });
  $('ad-sec').textContent = mmss(120); paintNorm(); paintHist(); idle();
  window.__ad = {st: function(){ return [phase, cnt, last]; }, ff: function(s){ t0 -= s * 1000; }};
})();
</script>
'''

page("iki-dakika-adim-testi.html", "2 Dakika Adım Testi",
     "Yerinde 2 dakika adım atarak kondisyonunuzu ölçün: süreölçer ve adım sayacı, 60–94 yaş için yaşa ve cinsiyete göre değerler, bağımsızlık eşiği ve sonuç kaydı.",
     "iki-dakika-adim-testi.html", SELF12_CSS, AD_BODY, AD_JS,
     seo_title="2 Dakika Adım Testi: Yerinde Adım Sayacı ve Yaşa Göre Değerler | İhsan Eren",
     about={"@type": "MedicalTest", "name": "2 dakika adım testi"},
     faq_items=AD_FAQ)

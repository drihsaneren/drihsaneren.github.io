# -*- coding: utf-8 -*-
# Kendine iyi bak, 10. tur: pelvik taban egzersiz zamanlayıcısı, tempolu yürüyüş metronomu.
# self9_part.py'den sonra exec edilir (SELF9_CSS, WAKE_JS hazır).

SELF10_CSS = SELF9_CSS + """
  .pf-orb{width:150px;height:150px;margin:6px auto 4px;position:relative;display:grid;place-items:center}
  .pf-orb i{position:absolute;inset:0;border-radius:50%;border:2px solid rgba(236,229,207,.22)}
  .pf-orb b{width:92px;height:92px;border-radius:50%;background:radial-gradient(circle at 50% 35%,#d8b25e,#8a6a2a);box-shadow:0 0 0 0 rgba(216,178,94,.0);
    transform:translateY(18px) scale(.82);transition:transform .9s cubic-bezier(.3,.7,.3,1),box-shadow .9s ease}
  .pf-orb.up b{transform:translateY(-10px) scale(1);box-shadow:0 0 0 10px rgba(216,178,94,.12)}
  .pf-orb.fast b{transition-duration:.35s}
  .days7{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:6px;margin-top:10px}
  .days7 div{border:1px solid var(--line);border-radius:10px;padding:7px 2px;text-align:center;font-size:11.5px;color:var(--muted)}
  .days7 div b{display:block;font-family:var(--display);font-weight:400;font-size:19px;color:var(--ink);font-variant-numeric:tabular-nums}
  .days7 div.on{border-color:rgba(216,178,94,.6);background:rgba(216,178,94,.1)}
  .days7 div.now{outline:1px dashed rgba(236,229,207,.35);outline-offset:2px}
  .tp-beat{width:120px;height:120px;margin:4px auto 0;border-radius:50%;border:2px solid rgba(236,229,207,.25);display:grid;place-items:center}
  .tp-beat span{width:34px;height:34px;border-radius:50%;background:#8fa476;transition:transform .12s ease,background .12s ease}
  .tp-beat.on span{transform:scale(1.9);background:#d8b25e}
  .wkbar{height:12px;border-radius:999px;background:rgba(236,229,207,.08);overflow:hidden;margin-top:8px}
  .wkbar i{display:block;height:100%;width:0;background:linear-gradient(90deg,#8fa476,#d8b25e);border-radius:999px;transition:width .4s ease}
  .tp-chk{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:10px;align-items:end;margin-top:12px}
  .tp-chk input{width:100%;box-sizing:border-box;padding:10px 12px;border-radius:12px;border:1px solid var(--line-strong);background:rgba(236,229,207,.04);color:var(--ink);font:inherit;font-size:16px}
  .tp-res{margin-top:10px;font-size:15px;color:var(--ink-soft)}
  .tp-res b{color:var(--ink)}
"""

# ------------------------------------------------------------------ 1 · PELVİK TABAN ZAMANLAYICISI
PF_FAQ = [
 ("Pelvik taban egzersizleri kimler için?", "Kadınlar ve erkekler için. Öksürürken, hapşırırken ya da gülerken idrar kaçırma, sık ve ani tuvalete gitme isteği, doğum sonrası dönem ve prostat ameliyatı sonrası bu egzersizlerin en sık önerildiği durumlardır. Bir ameliyat, doğum ya da tedavi geçirdiyseniz ekibinizin size özel önerileri olabilir; önce onlara uyun."),
 ("İşe yarıyor mu?", "Evet. 31 randomize çalışmayı ve 1.817 kadını kapsayan bir Cochrane derlemesinde, öksürük ve zorlanmayla idrar kaçırma yaşayan kadınlarda pelvik taban egzersizi yapanların %56’sı iyileştiğini bildirdi; egzersiz yapmayanlarda bu oran %6’ydı. İyileşme ya da belirgin düzelme bildirenlerin oranı ise %74’e karşı %11’di. Derleme yalnızca kadınlarda yapıldı ve çoğu çalışmanın izlem süresi bir yıldan kısaydı."),
 ("Ne zaman fark ederim?", "Kasların güçlenmesi zaman alır: en az 3 ay düzenli çalışın. Başta yalnızca birkaç saniye tutabiliyor ya da birkaç tekrar yapabiliyorsanız sorun değil; devam edin ve kademeli artırın."),
 ("Kasları doğru çalıştırdığımı nasıl anlarım?", "Bir elinizi anüs ile cinsel organlar arasındaki bölgeye (perine) koyun: kasları sıktığınızda bu bölge elinizden uzaklaşacak şekilde yukarı kalkmalı. Kalçanızı, uyluklarınızı ya da çenenizi sıkmayın, nefesinizi tutmayın ve karnınızı içeri çekmeyin."),
]

PF_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Pelvik taban egzersiz zamanlayıcısı</h1>
    <p class="lede">Pelvik taban kasları mesaneyi ve bağırsağı destekler; güçlü olduklarında öksürürken, hapşırırken ya da bir şey kaldırırken idrar kaçırma azalır. Bu egzersizler kadınlar ve erkekler için. Zamanlayıcı size ne zaman sıkıp ne zaman gevşeyeceğinizi sesle ve görüntüyle söyler; günde 3–4 seansı birkaç dakikada tamamlarsınız.</p>
    <p class="meta">Son güncelleme: 19 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>10 × 10 sn</b><span>Hedef: 10 saniyelik 10 yavaş sıkma</span></div>
        <div class="stat"><b>10 hızlı</b><span>Ardından 10 kısa ve hızlı sıkma</span></div>
        <div class="stat"><b>Günde 3–4 kez</b><span>Kaslar yorulana kadar çalışın</span></div>
        <div class="stat"><b>En az 3 ay</b><span>Kasların güçlenmesi için gereken düzenli çalışma süresi</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Zamanlayıcıyla birlikte yapın</p>
      <h2>Sıkın, tutun, gevşeyin</h2>
      <p class="soft">Oturun ya da dizleriniz bükülü uzanın. Tutma sürenizi ve tekrar sayısını seçin, sonra Başla’ya basın. Altın daire yükseldiğinde sıkın ve yukarı çekin, indiğinde tamamen gevşeyin.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <p class="lbl">Yavaş sıkmada tutma süresi</p>
            <div class="seg" role="group" aria-label="Tutma süresi" id="pf-hold">
              <button type="button" data-v="3" aria-pressed="false">3 sn</button>
              <button type="button" data-v="5" aria-pressed="true">5 sn</button>
              <button type="button" data-v="8" aria-pressed="false">8 sn</button>
              <button type="button" data-v="10" aria-pressed="false">10 sn</button>
            </div>
            <p class="lbl" style="margin-top:12px">Yavaş sıkma sayısı</p>
            <div class="seg" role="group" aria-label="Yavaş sıkma sayısı" id="pf-slow">
              <button type="button" data-v="5" aria-pressed="false">5</button>
              <button type="button" data-v="8" aria-pressed="false">8</button>
              <button type="button" data-v="10" aria-pressed="true">10</button>
            </div>
            <p class="lbl" style="margin-top:12px">Hızlı sıkma sayısı</p>
            <div class="seg" role="group" aria-label="Hızlı sıkma sayısı" id="pf-fast">
              <button type="button" data-v="5" aria-pressed="false">5</button>
              <button type="button" data-v="10" aria-pressed="true">10</button>
            </div>
            <label class="mz-chk"><input type="checkbox" id="pf-sound" checked> Sesli uyarı</label>
          </div>
          <div class="bt-out">
            <div class="pf-orb" id="pf-orb" aria-hidden="true"><i></i><b></b></div>
            <div class="trials" style="grid-template-columns:repeat(2,minmax(0,1fr))">
              <div><span>Yavaş</span><b id="pf-ns">0 / 10</b></div>
              <div><span>Hızlı</span><b id="pf-nf">0 / 10</b></div>
            </div>
            <p class="mz-today" id="pf-today"></p>
            <div class="days7" id="pf-days" aria-label="Son 7 gün"></div>
          </div>
          <div class="bt-run">
            <div class="yh-time"><b id="pf-sec">–</b><span>saniye</span></div>
            <p class="bt-phase" id="pf-phase" aria-live="polite">Hazır</p>
            <p class="bt-cue" id="pf-cue">Rahat bir pozisyon alın ve Başla’ya basın.</p>
            <button type="button" class="bt-tap" id="pf-go">Başla</button>
            <div class="controls" style="margin-top:10px;justify-content:center">
              <button type="button" class="cta ghost" id="pf-reset">Sıfırla</button>
            </div>
          </div>
        </div>
        <div class="pf-strings" hidden>
          <span data-k="ready">Hazır</span>
          <span data-k="readyc">Rahat bir pozisyon alın ve Başla’ya basın.</span>
          <span data-k="start">Başla</span>
          <span data-k="stop">Durdur</span>
          <span data-k="get">Hazırlanın</span>
          <span data-k="getc">İlk sıkma birazdan başlıyor.</span>
          <span data-k="sq">Sıkın ve yukarı çekin</span>
          <span data-k="sqc">Gaz ve idrarı aynı anda tutar gibi. Nefesinizi tutmayın.</span>
          <span data-k="rl">Tamamen gevşeyin</span>
          <span data-k="rlc">Kasları bırakın, normal nefes alın.</span>
          <span data-k="fprep">Şimdi hızlı sıkmalar</span>
          <span data-k="fprepc">Her uyarıda hızlıca sıkın ve hemen bırakın.</span>
          <span data-k="fsq">Sık</span>
          <span data-k="frl">Bırak</span>
          <span data-k="done">Seans tamam</span>
          <span data-k="donec">Günde 3–4 seansı hedefleyin.</span>
          <span data-k="paused">Durduruldu</span>
          <span data-k="pausedc">Kaldığınız yerden devam etmek için Başla’ya basın.</span>
          <span data-k="today">Bugün: {{n}} seans · hedef günde 3–4</span>
          <span data-k="d0">Pzt</span><span data-k="d1">Sal</span><span data-k="d2">Çar</span><span data-k="d3">Per</span><span data-k="d4">Cum</span><span data-k="d5">Cmt</span><span data-k="d6">Paz</span>
        </div>
      </div>
      <p class="count">Seans sayınız yalnızca bu cihazda saklanır; hiçbir yere gönderilmez.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Kasları bulun</h2>
        <ol class="steps">
          <li><span>Oturun ya da dizleriniz bükülü uzanın.</span></li>
          <li><span>Gaz çıkarmayı ve idrarı aynı anda tutmaya çalışıyormuş gibi yapın.</span></li>
          <li><span>Bunun yerine cinsel organlarınızı yukarı kaldırdığınızı ya da kuyruk sokumunuzu karnınıza doğru çektiğinizi de düşünebilirsiniz.</span></li>
          <li><span>Doğru yaptığınızda anüs ile cinsel organlar arasındaki bölge yukarı kalkar.</span></li>
        </ol>
      </div>
      <div>
        <h2>Sık yapılan hatalar</h2>
        <ul class="dots">
          <li>Kalçayı, uylukları ya da çeneyi sıkmak.</li>
          <li>Nefesi tutmak.</li>
          <li>Karın kaslarını içeri çekmek.</li>
          <li>Sıkmalar arasında tam gevşememek.</li>
        </ul>
        <h2 style="margin-top:22px">Püf noktası</h2>
        <p class="soft">Öksürmeden, hapşırmadan, gülmeden ya da ağır bir şey kaldırmadan hemen önce ve o sırada pelvik taban kaslarınızı sıkın. Bu alışkanlık kaçırmayı azaltmaya ya da önlemeye yardım eder. 10 saniyelik 10 sıkmayı rahatça yapabildiğinizde egzersizleri ayakta, çömelirken ya da bir adım öne çıkarken de deneyin.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(PF_FAQ)}
      <p class="soft" style="margin-top:18px">İdrar kaçırmanın türleri ve tedavisi için <a href="idrar-kacirma.html">idrar kaçırma</a>, doğum sonrası karın kasları için <a href="karin-kasi-ayrilmasi.html">karın kası ayrılması</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman bir uzmana başvurmalı?</h2>
      <ul class="dots redflags">
        <li>8–12 hafta düzenli çalıştığınız hâlde belirtilerinizde değişiklik yoksa</li>
        <li>Kasların sıkıştığını ya da yukarı kalktığını hissedemiyorsanız</li>
        <li>Egzersizleri yaparken belirtileriniz artıyorsa</li>
      </ul>
      <p class="soft">Bu durumlarda hekiminizle konuşabilir ve pelvik sağlık alanında çalışan bir fizyoterapistten değerlendirme isteyebilirsiniz.</p>
      {CTA_CARD("Pelvik taban kaslarınız", "pelvik taban egzersizleri ve değerlendirme")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "St George’s University Hospitals NHS Foundation Trust, Physiotherapy. " + ext("https://www.stgeorges.nhs.uk/wp-content/uploads/2026/05/PHY_PFEA_01.pdf", "Pelvic floor exercises for all") + ". PHY_PFEA_01, May 2026.",
        "Dumoulin C, Cacciari LP, Hay-Smith EJC. Pelvic floor muscle training versus no treatment, or inactive control treatments, for urinary incontinence in women. Cochrane Database Syst Rev. 2018;(10):CD005654. Özet: " + ext("https://evidence.nihr.ac.uk/alert/pelvic-floor-muscle-training-can-improve-symptoms-of-urinary-incontinence/", "NIHR Evidence, 2 January 2019") + ".",
      ])}
    </div>
  </section>
</main>'''

PF_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.pf-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var $ = function(id){ return document.getElementById(id); }, KEY = 'drihsaneren.pelvik.v1';
  var lock = null, ctx = null, snd = $('pf-sound');
''' + WAKE_JS + '''
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function seg(id){ var b = $(id).querySelector('[aria-pressed="true"]'); return +b.getAttribute('data-v'); }
  ['pf-hold', 'pf-slow', 'pf-fast'].forEach(function(id){
    $(id).addEventListener('click', function(e){
      var b = e.target.closest('button'); if (!b || run) return;
      this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      counts(0, 0);
    });
  });
  function load(){ try { return JSON.parse(localStorage.getItem(KEY)) || {d: {}}; } catch (e) { return {d: {}}; } }
  function save(o){ try { localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {} }
  function dkey(d){ return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2); }
  function paintDays(){
    var o = load(), box = $('pf-days'), now = new Date(); box.innerHTML = '';
    for (var i = 6; i >= 0; i--){
      var d = new Date(now.getFullYear(), now.getMonth(), now.getDate() - i), n = o.d[dkey(d)] || 0, el = document.createElement('div');
      el.innerHTML = '<b>' + n + '</b>' + S['d' + ((d.getDay() + 6) % 7)];
      if (n) el.classList.add('on'); if (!i) el.classList.add('now');
      box.appendChild(el);
    }
    $('pf-today').textContent = fill(S.today, {n: o.d[dkey(now)] || 0});
  }
  function counts(a, b){ $('pf-ns').textContent = a + ' / ' + seg('pf-slow'); $('pf-nf').textContent = b + ' / ' + seg('pf-fast'); }
  var plan = [], idx = 0, t0 = 0, left = 0, run = false, iv = null, orb = $('pf-orb');
  function build(){
    var h = seg('pf-hold'), ns = seg('pf-slow'), nf = seg('pf-fast'), p = [['get', 3]];
    for (var i = 1; i <= ns; i++){ p.push(['sq', h, i]); p.push(['rl', Math.max(4, h), i]); }
    p.push(['fprep', 4]);
    for (var j = 1; j <= nf; j++){ p.push(['fsq', 1, j]); p.push(['frl', 1.5, j]); }
    return p;
  }
  function show(st){
    var k = st[0];
    $('pf-phase').textContent = S[k] || '';
    $('pf-cue').textContent = S[k + 'c'] || (k === 'fsq' || k === 'frl' ? S.fprepc : '');
    orb.classList.toggle('up', k === 'sq' || k === 'fsq'); orb.classList.toggle('fast', k === 'fsq' || k === 'frl');
    if (k === 'sq') { beep(880, .25, .2); counts(st[2], 0); }
    if (k === 'rl') beep(440, .3, .16);
    if (k === 'fprep') counts(seg('pf-slow'), 0);
    if (k === 'fsq') { beep(990, .12, .2); counts(seg('pf-slow'), st[2]); }
  }
  function enter(i){ idx = i; left = plan[i][1]; t0 = performance.now(); show(plan[i]); }
  function tick(){
    var el = (performance.now() - t0) / 1000, rem = left - el;
    $('pf-sec').textContent = String(Math.max(0, Math.ceil(rem)));
    if (rem > 0) return;
    if (idx + 1 < plan.length) enter(idx + 1); else finish();
  }
  function finish(){
    clearInterval(iv); iv = null; run = false; wake(false); orb.classList.remove('up');
    beep(660, .2, .18); setTimeout(function(){ beep(880, .2, .18); }, 220); setTimeout(function(){ beep(1100, .35, .18); }, 440);
    var o = load(), k = dkey(new Date()); o.d[k] = (o.d[k] || 0) + 1;
    var ks = Object.keys(o.d).sort(); while (ks.length > 120) delete o.d[ks.shift()];
    save(o); paintDays();
    $('pf-phase').textContent = S.done; $('pf-cue').textContent = S.donec; $('pf-sec').textContent = '✓';
    $('pf-go').textContent = S.start; $('pf-go').classList.remove('stop'); plan = [];
  }
  $('pf-go').addEventListener('click', function(){
    if (run){
      clearInterval(iv); iv = null; run = false; wake(false); left = Math.max(0, left - (performance.now() - t0) / 1000);
      orb.classList.remove('up'); $('pf-phase').textContent = S.paused; $('pf-cue').textContent = S.pausedc;
      this.textContent = S.start; this.classList.remove('stop'); return;
    }
    run = true; wake(true); this.textContent = S.stop; this.classList.add('stop');
    if (!plan.length){ plan = build(); enter(0); } else { t0 = performance.now(); show(plan[idx]); }
    clearInterval(iv); iv = setInterval(tick, 100); tick();
  });
  $('pf-reset').addEventListener('click', function(){
    clearInterval(iv); iv = null; run = false; wake(false); plan = []; orb.classList.remove('up', 'fast');
    $('pf-sec').textContent = '–'; $('pf-phase').textContent = S.ready; $('pf-cue').textContent = S.readyc;
    $('pf-go').textContent = S.start; $('pf-go').classList.remove('stop'); counts(0, 0);
  });
  counts(0, 0); paintDays();
  window.__pf = {st: function(){ return [run, idx, plan.length, plan[idx] && plan[idx][0]]; }, skip: function(){ left = 0; }};
})();
</script>
'''

page("pelvik-taban-zamanlayicisi.html", "Pelvik Taban Egzersiz Zamanlayıcısı",
     "Kadınlar ve erkekler için pelvik taban (Kegel) egzersizleri: kasları nasıl bulursunuz, kaç saniye tutarsınız? Sesli ve görsel uyarılı zamanlayıcı, günlük seans takibi.",
     "pelvik-taban-zamanlayicisi.html", SELF10_CSS, PF_BODY, PF_JS,
     seo_title="Pelvik Taban (Kegel) Egzersiz Zamanlayıcısı: Sesli Rehber | İhsan Eren",
     about={"@type": "ExercisePlan", "name": "Pelvik taban kası egzersizleri"},
     faq_items=PF_FAQ)

# ------------------------------------------------------------------ 2 · TEMPOLU YÜRÜYÜŞ METRONOMU
TP_FAQ = [
 ("Neden dakikada 100 adım?", "ABD’de laboratuvarda yapılan iki çalışmada (21–40 ve 41–60 yaş arası yetişkinler), dakikada yaklaşık 100 adımlık yürüyüşün orta yoğunluğa (3 MET), yaklaşık 130 adımın ise yüksek yoğunluğa (6 MET) karşılık geldiği görüldü. Her 10 adımlık artış yaklaşık 1 MET daha fazla eforu gösterir. Adım sayarak yürüyüşünüzün “tempolu” olup olmadığını pratik olarak anlayabilirsiniz."),
 ("Bu tempo herkes için aynı mı?", "Hayır. Bu değerler sağlıklı yetişkinlerin ortalamasıdır ve kişiden kişiye değişir. Kondisyonu düşük, yaşı ileri ya da kilosu fazla biri için dakikada 100 adım daha zorlayıcı olabilir. Rahat ettiğiniz bir tempoyla başlayın ve kademeli artırın. Kalp hastalığınız varsa ya da yürürken göğüs ağrısı, baş dönmesi veya konuşmanızı engelleyen nefes darlığı olursa durun ve hekiminize danışın."),
 ("Telefon cebimdeyken çalışır mı?", "Sayfa açıkken ekran kapanmasın diye ekran kilidi engellenir; sesler de bu sayede devam eder. Bazı telefonlarda ekran kilitlenirse ya da başka bir uygulamaya geçerseniz ses duraksayabilir. En iyisi ses açıkken ekranı açık bırakıp telefonu cebinizde taşımaktır."),
 ("Haftada ne kadar yürümeliyim?", "Dünya Sağlık Örgütü yetişkinlere haftada en az 150–300 dakika orta yoğunlukta ya da 75–150 dakika yüksek yoğunlukta aerobik aktivite öneriyor. Bu, haftada 5 gün günde 30 dakikalık tempolu yürüyüşle karşılanabilir; daha kısa yürüyüşler de sayılır."),
]

TP_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Tempolu yürüyüş metronomu</h1>
    <p class="lede">Yürüyüşünüz gerçekten “tempolu” mu? Araştırmalar, dakikada yaklaşık 100 adımın orta yoğunlukta egzersize karşılık geldiğini gösteriyor. Bu metronom seçtiğiniz tempoda her adımınız için bir ses çalar; siz de adımlarınızı sese uydurursunuz. Önce 15 saniyede kaç adım attığınızı sayarak bugünkü temponuzu ölçebilirsiniz.</p>
    <p class="meta">Son güncelleme: 19 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>100 adım/dk</b><span>Orta yoğunluğun yaklaşık eşiği (3 MET)</span></div>
        <div class="stat"><b>130 adım/dk</b><span>Yüksek yoğunluğun yaklaşık eşiği (6 MET)</span></div>
        <div class="stat"><b>+10 adım</b><span>Dakikadaki her 10 adım, yaklaşık 1 MET daha fazla efor</span></div>
        <div class="stat"><b>150 dk</b><span>Haftalık en az orta yoğunlukta aktivite önerisi</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Zamanlayıcıyla birlikte yapın</p>
      <h2>Adımlarınızı sese uydurun</h2>
      <p class="soft">Tempoyu ve süreyi seçin, Başla’ya basın ve her seste bir adım atın. Sesi açın; ekran açık kalır.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <p class="lbl">Tempo (adım/dakika)</p>
            <div class="seg" role="group" aria-label="Tempo" id="tp-cad">
              <button type="button" data-v="100" aria-pressed="true">100</button>
              <button type="button" data-v="110" aria-pressed="false">110</button>
              <button type="button" data-v="120" aria-pressed="false">120</button>
              <button type="button" data-v="130" aria-pressed="false">130</button>
            </div>
            <p class="soft" id="tp-band" style="margin:8px 0 0;font-size:14px"></p>
            <p class="lbl" style="margin-top:12px">Süre</p>
            <div class="seg" role="group" aria-label="Süre" id="tp-dur">
              <button type="button" data-v="10" aria-pressed="true">10 dk</button>
              <button type="button" data-v="20" aria-pressed="false">20 dk</button>
              <button type="button" data-v="30" aria-pressed="false">30 dk</button>
            </div>
            <label class="mz-chk"><input type="checkbox" id="tp-sound" checked> Adım sesi</label>
          </div>
          <div class="bt-out">
            <div class="tp-beat" id="tp-beat" aria-hidden="true"><span></span></div>
            <div class="trials" style="grid-template-columns:repeat(2,minmax(0,1fr))">
              <div><span>Geçen süre</span><b id="tp-el">0:00</b></div>
              <div><span>Adım</span><b id="tp-steps">0</b></div>
            </div>
            <p class="mz-today" id="tp-week"></p>
            <div class="wkbar" aria-hidden="true"><i id="tp-wbar"></i></div>
          </div>
          <div class="bt-run">
            <div class="yh-time"><b id="tp-left">10:00</b><span>kalan</span></div>
            <p class="bt-phase" id="tp-phase" aria-live="polite">Hazır</p>
            <p class="bt-cue" id="tp-cue">Başla’ya basın ve her seste bir adım atın.</p>
            <button type="button" class="bt-tap" id="tp-go">Başla</button>
            <div class="controls" style="margin-top:10px;justify-content:center">
              <button type="button" class="cta ghost" id="tp-reset">Sıfırla</button>
            </div>
          </div>
        </div>
        <div class="tp-strings" hidden>
          <span data-k="b100">Orta yoğunluk (yaklaşık 3 MET): tempolu yürüyüş.</span>
          <span data-k="b110">Orta yoğunluk (yaklaşık 4 MET).</span>
          <span data-k="b120">Orta-yüksek yoğunluk (yaklaşık 5 MET).</span>
          <span data-k="b130">Yüksek yoğunluk (yaklaşık 6 MET): çok hızlı yürüyüş.</span>
          <span data-k="ready">Hazır</span>
          <span data-k="readyc">Başla’ya basın ve her seste bir adım atın.</span>
          <span data-k="start">Başla</span>
          <span data-k="stop">Durdur</span>
          <span data-k="run">Yürüyün</span>
          <span data-k="runc">Her seste bir adım. Dik durun, kollarınızı sallayın.</span>
          <span data-k="paused">Durduruldu</span>
          <span data-k="pausedc">Devam etmek için Başla’ya basın.</span>
          <span data-k="done">Yürüyüş tamam</span>
          <span data-k="donec">Birkaç dakika yavaş yürüyerek soğuyun.</span>
          <span data-k="week">Son 7 günde metronomla: {{m}} dakika / 150</span>
        </div>
      </div>

      <div class="tool" style="margin-top:18px">
        <div class="bt" style="display:block">
          <p class="lbl">Temponuzu ölçün</p>
          <p class="soft" style="margin-top:4px">Her zamanki tempolu yürüyüşünüzle yürürken Başla’ya basın ve 15 saniye boyunca attığınız adımları sayın. Bitiş sesinden sonra sayıyı yazın.</p>
          <div class="controls" style="margin-top:8px">
            <button type="button" class="cta" id="tc-go">15 saniyeyi başlat</button>
            <span class="yh-time" style="display:inline-flex;align-items:baseline;gap:6px"><b id="tc-sec" style="font-size:34px">15</b><span>sn</span></span>
          </div>
          <div class="tp-chk">
            <label><span class="lbl">15 saniyedeki adım sayınız</span><input type="number" inputmode="numeric" min="5" max="60" id="tc-n" placeholder="ör. 27"></label>
            <button type="button" class="cta ghost" id="tc-calc">Hesapla</button>
          </div>
          <p class="tp-res" id="tc-res" aria-live="polite"></p>
          <div class="tc-strings" hidden>
            <span data-k="res">Temponuz: <b>{{c}} adım/dakika</b>. {{t}}</span>
            <span data-k="lo">Bu tempo orta yoğunluğun altında; dakikada 100 adıma doğru yavaş yavaş hızlanmayı deneyebilirsiniz.</span>
            <span data-k="mid">Orta yoğunluktasınız: bu bir tempolu yürüyüş.</span>
            <span data-k="hi">Yüksek yoğunluğa yakın ya da üstündesiniz.</span>
            <span data-k="bad">Lütfen 5 ile 60 arasında bir sayı yazın.</span>
          </div>
        </div>
      </div>
      <p class="count">Yürüyüş süreleriniz yalnızca bu cihazda saklanır; hiçbir yere gönderilmez.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nasıl yürümeli?</h2>
        <ul class="dots">
          <li>İlk 2–3 dakikayı rahat bir tempoyla yürüyerek ısının, sonra metronoma geçin.</li>
          <li>Adımlarınızı uzatmaya çalışmayın; temponuzu artırmak için adım sıklığınızı artırın.</li>
          <li>Dik durun, kollarınızı dirsekten bükerek doğal sallayın.</li>
          <li>Rahat ayakkabı giyin ve düz, güvenli bir yol seçin.</li>
        </ul>
      </div>
      <div>
        <h2>Bir de ölçerek bakın</h2>
        <ul class="dots">
          <li><a href="yurume-hizi-testi.html">Yürüme hızı testi</a>: her zamanki temponuzla 4 metreyi kaç saniyede yürüdüğünüzü ölçün.</li>
          <li><a href="hareket.html">Ne kadar hareket?</a>: haftalık hareketinizi önerilerle karşılaştırın.</li>
          <li><a href="hareket-atistirmaliklari.html">Hareket atıştırmalıkları</a>: gün içine serpiştirilmiş kısa hareket molaları.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(TP_FAQ)}
      {CTA_CARD("Size uygun bir yürüyüş programı", "kişiye özel yürüyüş ve egzersiz programı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Tudor-Locke C, Aguiar EJ, Han H, et al. " + ext("https://ijbnpa.biomedcentral.com/track/pdf/10.1186/s12966-019-0769-6", "Walking cadence (steps/min) and intensity in 21–40 year olds: CADENCE-adults") + ". Int J Behav Nutr Phys Act. 2019;16:8.",
        "Tudor-Locke C, Ducharme SW, Aguiar EJ, et al. " + ext("https://doi.org/10.1186/s12966-020-01045-z", "Walking cadence (steps/min) and intensity in 41 to 60-year-old adults: the CADENCE-adults study") + ". Int J Behav Nutr Phys Act. 2020;17.",
        "World Health Organization. " + ext("https://www.who.int/publications/i/item/9789240015128", "WHO guidelines on physical activity and sedentary behaviour") + ". 2020.",
      ])}
    </div>
  </section>
</main>'''

TP_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.tp-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var T = {}; root.querySelectorAll('.tc-strings [data-k]').forEach(function(e){ T[e.getAttribute('data-k')] = e.innerHTML; });
  var $ = function(id){ return document.getElementById(id); }, KEY = 'drihsaneren.tempo.v1';
  var lock = null, ctx = null, snd = $('tp-sound');
''' + WAKE_JS + '''
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function seg(id){ return +$(id).querySelector('[aria-pressed="true"]').getAttribute('data-v'); }
  function mmss(s){ s = Math.max(0, Math.round(s)); return Math.floor(s / 60) + ':' + ('0' + s % 60).slice(-2); }
  function band(){ $('tp-band').textContent = S['b' + seg('tp-cad')]; }
  ['tp-cad', 'tp-dur'].forEach(function(id){
    $(id).addEventListener('click', function(e){
      var b = e.target.closest('button'); if (!b || run) return;
      this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      band(); if (!el) $('tp-left').textContent = mmss(seg('tp-dur') * 60);
    });
  });
  function load(){ try { return JSON.parse(localStorage.getItem(KEY)) || {d: {}}; } catch (e) { return {d: {}}; } }
  function dkey(d){ return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2); }
  function week(){
    var o = load(), now = new Date(), m = 0;
    for (var i = 0; i < 7; i++) m += o.d[dkey(new Date(now.getFullYear(), now.getMonth(), now.getDate() - i))] || 0;
    $('tp-week').textContent = fill(S.week, {m: m}); $('tp-wbar').style.width = Math.min(100, m / 150 * 100) + '%';
  }
  function record(upto){
    var mins = Math.floor((upto - recorded) / 60); if (mins < 1) return;
    recorded += mins * 60;
    var o = load(), k = dkey(new Date()); o.d[k] = (o.d[k] || 0) + mins;
    var ks = Object.keys(o.d).sort(); while (ks.length > 120) delete o.d[ks.shift()];
    try { localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {}
    week();
  }
  // metronom: Web Audio ile ileriye zamanlanmış tıklar; ekran kapalıyken de akması için arka planda daha uzun ileriye bakar
  var run = false, el = 0, t0 = 0, cad = 100, next = 0, steps = 0, sched = null, iv = null, beat = $('tp-beat'), recorded = 0;
  function click(at){
    try {
      var o = ctx.createOscillator(), g = ctx.createGain();
      o.frequency.value = 1050; g.gain.setValueAtTime(0.0001, at);
      g.gain.exponentialRampToValueAtTime(snd.checked ? 0.25 : 0.0001, at + 0.005); g.gain.exponentialRampToValueAtTime(0.0001, at + 0.06);
      o.connect(g); g.connect(ctx.destination); o.start(at); o.stop(at + 0.08);
    } catch (e) {}
    var ms = Math.max(0, (at - ctx.currentTime) * 1000);
    setTimeout(function(){ if (!run) return; steps++; $('tp-steps').textContent = String(steps); beat.classList.add('on'); setTimeout(function(){ beat.classList.remove('on'); }, 110); }, ms);
  }
  function schedule(){
    var ahead = document.hidden ? 1.6 : 0.15;
    while (next < ctx.currentTime + ahead){ click(next); next += 60 / cad; }
  }
  function tick(){
    var total = seg('tp-dur') * 60, now = el + (performance.now() - t0) / 1000;
    $('tp-el').textContent = mmss(now); $('tp-left').textContent = mmss(total - now);
    if (now >= total) finish(total);
  }
  function stopTimers(){ clearInterval(sched); clearInterval(iv); sched = iv = null; wake(false); }
  function finish(total){
    stopTimers(); run = false; record(total); recorded = 0; el = 0;
    var bk = snd.checked; snd.checked = true; beep(660, .2, .2); setTimeout(function(){ beep(880, .2, .2); }, 230); setTimeout(function(){ beep(1100, .4, .2); snd.checked = bk; }, 460);
    $('tp-phase').textContent = S.done; $('tp-cue').textContent = S.donec; $('tp-left').textContent = '0:00';
    $('tp-go').textContent = S.start; $('tp-go').classList.remove('stop');
  }
  $('tp-go').addEventListener('click', function(){
    if (run){
      el += (performance.now() - t0) / 1000; stopTimers(); run = false;
      record(el);
      $('tp-phase').textContent = S.paused; $('tp-cue').textContent = S.pausedc; this.textContent = S.start; this.classList.remove('stop'); return;
    }
    try { ctx = ctx || new (window.AudioContext || window.webkitAudioContext)(); if (ctx.resume) ctx.resume(); } catch (e) {}
    if (!ctx) return;
    cad = seg('tp-cad'); run = true; t0 = performance.now(); next = ctx.currentTime + 0.1; wake(true);
    if (!el) { steps = 0; $('tp-steps').textContent = '0'; }
    this.textContent = S.stop; this.classList.add('stop'); $('tp-phase').textContent = S.run; $('tp-cue').textContent = S.runc;
    schedule(); sched = setInterval(schedule, 25); iv = setInterval(tick, 250); tick();
  });
  $('tp-reset').addEventListener('click', function(){
    if (run){ el += (performance.now() - t0) / 1000; record(el); }
    stopTimers(); run = false; el = 0; recorded = 0; steps = 0;
    $('tp-steps').textContent = '0'; $('tp-el').textContent = '0:00'; $('tp-left').textContent = mmss(seg('tp-dur') * 60);
    $('tp-phase').textContent = S.ready; $('tp-cue').textContent = S.readyc; $('tp-go').textContent = S.start; $('tp-go').classList.remove('stop');
  });
  document.addEventListener('visibilitychange', function(){ if (run && ctx) { clearInterval(sched); sched = setInterval(schedule, document.hidden ? 400 : 25); schedule(); } });
  // 15 saniyelik adım sayımı
  var civ = null;
  $('tc-go').addEventListener('click', function(){
    clearInterval(civ); var s0 = performance.now(), b = this; b.disabled = true;
    var bk = snd.checked; snd.checked = true; beep(880, .2, .2); snd.checked = bk;
    civ = setInterval(function(){
      var r = 15 - (performance.now() - s0) / 1000; $('tc-sec').textContent = String(Math.max(0, Math.ceil(r)));
      if (r <= 0){ clearInterval(civ); b.disabled = false; var k = snd.checked; snd.checked = true; beep(660, .5, .22); snd.checked = k; $('tc-n').focus(); }
    }, 100);
  });
  $('tc-calc').addEventListener('click', function(){
    var n = parseInt($('tc-n').value, 10), out = $('tc-res');
    if (!(n >= 5 && n <= 60)) { out.innerHTML = T.bad; return; }
    var c = n * 4;
    out.innerHTML = fill(T.res, {c: c, t: c < 100 ? T.lo : c < 130 ? T.mid : T.hi});
  });
  band(); week(); $('tp-left').textContent = mmss(seg('tp-dur') * 60);
  window.__tp = {st: function(){ return [run, steps, el, cad]; }};
})();
</script>
'''

page("tempolu-yuruyus.html", "Tempolu Yürüyüş Metronomu",
     "Yürüyüşünüz gerçekten tempolu mu? Dakikada 100 adım orta yoğunluğun eşiği. Seçtiğiniz tempoda adım sesi çalan metronom, 15 saniyelik tempo ölçümü ve haftalık takip.",
     "tempolu-yuruyus.html", SELF10_CSS, TP_BODY, TP_JS,
     seo_title="Tempolu Yürüyüş Metronomu: Dakikada 100 Adım | İhsan Eren",
     about={"@type": "ExercisePlan", "name": "Tempolu yürüyüş"},
     faq_items=TP_FAQ)

# -*- coding: utf-8 -*-
# Kendine iyi bak, 13. tur: yemek sonrası yürüyüş zamanlayıcısı ve denge antrenmanı (Otago programından uyarlanmış ev programı).
# self12_part.py'den sonra exec edilir (SELF12_CSS, WAKE_JS, .gu-step, .gu-dots, .days7 hazır).
# Kaynaklar (22 Ekim 2026'da okundu): Reynolds 2016 (PEDro künyesi + HCPLive haberi), Buffey 2022 (MDedge haberi), Colberg 2016 ADA (AJMC haberi + ACU künyesi), DSÖ;
# Sherrington 2019 Cochrane (MDedge haberi), Thomas 2010 (Age Ageing özeti), Dünya Düşme Kılavuzu 2022 (RoSPA sunumu), Royal Orthopaedic Hospital Otago sayfası.

SELF13_CSS = SELF12_CSS + """
  .yy-meals{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-top:12px}
  .yy-meals div{border:1px solid var(--line);border-radius:12px;padding:9px 6px;text-align:center;font-size:13px;color:var(--muted)}
  .yy-meals div b{display:block;font-size:20px;line-height:1.2;color:var(--ink-soft)}
  .yy-meals div.on{border-color:rgba(216,178,94,.6);background:rgba(216,178,94,.1);color:var(--ink)}
  .yy-meals div.on b{color:var(--foil)}
  .db-ex[hidden]{display:none}
  .db-sup{font-size:14px;color:var(--foil);margin:12px 0 0;line-height:1.5}
  .db-weeks{font-size:14.5px;color:var(--ink-soft);margin:8px 0 0}
"""

# ------------------------------------------------------------------ 1 · YEMEK SONRASI YÜRÜYÜŞ
YY_FAQ = [
 ("Kimler için?", "En güçlü veri tip 2 diyabeti olanlardan geliyor: Yeni Zelanda’da tip 2 diyabetli 41 yetişkinle yapılan bir çalışmada, her ana öğünden sonra 10 dakika yürümek, aynı toplam süreyi günde bir kez 30 dakika yürümeye göre yemek sonrası kan şekerini ortalama %12, akşam yemeğinden sonra ise %22 daha çok düşürdü. Yedi çalışmayı birleştiren bir analizde, çoğu diyabeti olmayan kişilerde bile yemekten sonraki birkaç dakikalık hafif yürüyüş kan şekerini ve insülini düşürdü."),
 ("Yemekten ne kadar sonra yürümeliyim?", "Yemeği bitirdikten kısa süre sonra başlamak iyi bir alışkanlık. Analizin yazarlarına göre kan şekeri genellikle yemekten 60–90 dakika sonra zirveye çıkıyor; bu zirveden önce yapılan hareket en iyi sonucu veriyor."),
 ("Ne kadar yürümek yeterli?", "Çalışmada her öğünden sonra 10 dakika yürüyüş kullanıldı. Yemekten sonraki 2–5 dakikalık kısa ve hafif yürüyüşlerin de kan şekerini düşürdüğü görüldü; ayakta durmak da oturmaktan iyiydi ama yürümek kadar etkili değildi. Zamanınız azsa kısa bir yürüyüş bile hiç yürümemekten iyidir."),
 ("Günlük egzersizimin yerine geçer mi?", "Tek başına yetmez, ama ona katkı sağlar. Dünya Sağlık Örgütü yetişkinlere haftada en az 150 dakika orta yoğunlukta hareket ve haftada en az 2 gün kas güçlendirme öneriyor ve her hareketin sayıldığını vurguluyor. Amerikan Diyabet Derneği de diyabeti olanlara düzenli egzersizin yanında, uzun oturmanın her 30 dakikada bir birkaç dakikalık hafif hareketle bölünmesini öneriyor."),
 ("İnsülin ya da şeker ilacı kullanıyorsam?", "İnsülin ya da bazı şeker düşürücü ilaçları kullanıyorsanız egzersiz sırasında ve sonrasında şekeriniz düşebilir. Yürüyüş planınızı hekiminizle konuşun, şekerinizi ölçüyorsanız yürüyüşten önce ve sonra bakın, titreme, terleme, baş dönmesi gibi düşük şeker belirtilerinde durun ve yanınızda hızlı etkili bir şeker bulundurun."),
]

YY_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Yemek sonrası yürüyüş</h1>
    <p class="lede">Yemekten sonra kısa bir yürüyüş, kan şekerinin yükselmesini yumuşatır. Tip 2 diyabetli kişilerle yapılan bir çalışmada, her öğünden sonra 10 dakika yürümek, aynı süreyi günde bir kez yürümekten daha etkili oldu. Bu zamanlayıcı öğününüzü ve süreyi seçmenizi, yürüyüşünüzü saymayı ve gün içinde hangi öğünlerden sonra yürüdüğünüzü işaretlemeyi sağlar.</p>
    <p class="meta">Son güncelleme: 23 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%12</b><span>Her öğünden sonra 10 dakika yürüyüşle yemek sonrası kan şekerinde ek düşüş (tip 2 diyabet, 41 kişi)</span></div>
        <div class="stat"><b>%22</b><span>Akşam yemeğinden sonra görülen ek düşüş</span></div>
        <div class="stat"><b>2–5 dk</b><span>Yemekten sonraki kısa, hafif yürüyüş bile kan şekerini ve insülini düşürdü (7 çalışma)</span></div>
        <div class="stat"><b>30 dk</b><span>Uzun oturmayı her 30 dakikada bir birkaç dakikalık hafif hareketle bölme önerisi (Amerikan Diyabet Derneği)</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Zamanlayıcıyla birlikte yapın</p>
      <h2>Yemeği bitirdiniz mi? Yürüyüşe çıkın</h2>
      <p class="soft">Öğünü ve süreyi seçip Başla’ya basın. Rahat, konuşabildiğiniz bir tempoda yürüyün; dışarı çıkamıyorsanız evin içinde ya da yerinde yürümek de olur. Her dakika kısa bir bip sesi duyarsınız.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <p class="lbl">Öğün</p>
            <div class="seg" role="group" aria-label="Öğün" id="yy-meal">
              <button type="button" data-v="k" aria-pressed="false">Kahvaltı</button>
              <button type="button" data-v="o" aria-pressed="true">Öğle</button>
              <button type="button" data-v="a" aria-pressed="false">Akşam</button>
            </div>
            <p class="lbl" style="margin-top:12px">Süre</p>
            <div class="seg" role="group" aria-label="Süre" id="yy-min">
              <button type="button" data-v="3" aria-pressed="false">3 dk</button>
              <button type="button" data-v="10" aria-pressed="true">10 dk</button>
              <button type="button" data-v="15" aria-pressed="false">15 dk</button>
            </div>
            <label class="mz-chk"><input type="checkbox" id="yy-sound" checked> Sesli uyarı</label>
          </div>
          <div class="bt-out">
            <p class="lbl">Bugün</p>
            <div class="yy-meals" id="yy-today">
              <div data-m="k"><b>–</b>Kahvaltı</div>
              <div data-m="o"><b>–</b>Öğle</div>
              <div data-m="a"><b>–</b>Akşam</div>
            </div>
            <p class="mz-today" id="yy-sum"></p>
            <div class="days7" id="yy-days" aria-label="Son 7 gün"></div>
          </div>
          <div class="bt-run">
            <div class="yh-time"><b id="yy-sec">10:00</b><span>kalan süre</span></div>
            <p class="bt-phase" id="yy-phase" aria-live="polite">Hazır</p>
            <p class="bt-cue" id="yy-cue">Yemeği bitirince Başla’ya basın.</p>
            <button type="button" class="bt-tap" id="yy-go">Başla</button>
            <div class="controls" style="margin-top:10px;justify-content:center">
              <button type="button" class="cta ghost" id="yy-reset">Sıfırla</button>
            </div>
          </div>
        </div>
        <div class="yy-strings" hidden>
          <span data-k="ready">Hazır</span>
          <span data-k="readyc">Yemeği bitirince Başla’ya basın.</span>
          <span data-k="start">Başla</span>
          <span data-k="stop">Durdur</span>
          <span data-k="run">Yürüyün</span>
          <span data-k="runc">Rahat, konuşabildiğiniz bir tempoda.</span>
          <span data-k="half">Yarısı tamam</span>
          <span data-k="done">Yürüyüş tamam</span>
          <span data-k="donec">Bu öğünü işaretledik. Bir sonraki öğünden sonra görüşmek üzere.</span>
          <span data-k="paused">Durduruldu</span>
          <span data-k="pausedc">Kaldığınız yerden devam etmek için Başla’ya basın.</span>
          <span data-k="sum">Bugün {{n}} öğünden sonra yürüdünüz · hedef 3</span>
          <span data-k="d0">Pzt</span><span data-k="d1">Sal</span><span data-k="d2">Çar</span><span data-k="d3">Per</span><span data-k="d4">Cum</span><span data-k="d5">Cmt</span><span data-k="d6">Paz</span>
        </div>
      </div>
      <p class="count">Hangi öğünlerden sonra yürüdüğünüz yalnızca bu cihazda saklanır; hiçbir yere gönderilmez.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Neden işe yarıyor?</h2>
        <p class="soft">Yemekten sonra kan şekeri yükselir. Çalışan kaslar kandaki şekeri kullandığı için, bu sırada yapılan kısa bir yürüyüş yükselişi azaltır ve şekerin daha yavaş inip çıkmasını sağlar. Yedi çalışmanın birleştirildiği analizde ayakta durmak da oturmaktan iyiydi, ama yalnızca hafif yürüyüş hem kan şekerini hem insülini düşürdü.</p>
      </div>
      <div>
        <h2>Alışkanlık hâline getirmek için</h2>
        <ul class="dots">
          <li>Yürüyüşü bir öğüne bağlayın: önce akşam yemeğinden sonra başlayın.</li>
          <li>Bir yakınınızla birlikte yürüyün; sohbet süreyi kısaltır.</li>
          <li>Hava kötüyse evin içinde, koridorda ya da yerinde yürüyün.</li>
          <li>Telefonunuzdaki bu sayfayı yemek masasının yanında açık tutun.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(YY_FAQ)}
      <p class="soft" style="margin-top:18px">Adımlarınızı bir tempoya oturtmak için <a href="tempolu-yuruyus.html">tempolu yürüyüş metronomunu</a>, gün içinde oturma sürenizi görmek için <a href="oturma-suresi.html">oturma süresi hesaplayıcısını</a>, kas güçlendirme için <a href="guc-devresi.html">evde güç devresini</a> kullanabilirsiniz.</p>
      {CTA_CARD("Diyabette size uygun bir egzersiz programı", "diyabette egzersiz programı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Reynolds AN, Mann JI, Williams S, Venn BJ. " + ext("https://doi.org/10.1007/s00125-016-4085-2", "Advice to walk after meals is more effective for lowering postprandial glycaemia in type 2 diabetes mellitus than advice that does not specify timing: a randomised crossover study") + ". Diabetologia. 2016;59(12):2572–2578. Haber: " + ext("https://hcplive.com/view/type-2-diabetes-exercise-time-matters", "HCPLive") + ".",
        "Buffey AJ, Herring MP, Langley CK, et al. The acute effects of interrupting prolonged sitting time in adults with standing and light-intensity walking on biomarkers of cardiometabolic health: a systematic review and meta-analysis. Sports Med. 2022;52:1765–1787. Haber: " + ext("https://mdedge.com/fedprac/article/256982/diabetes/short-walks-after-meals-can-cut-diabetes-risk", "MDedge, 11 August 2022") + ".",
        "Colberg SR, Sigal RJ, Yardley JE, et al. " + ext("https://doi.org/10.2337/dc16-1728", "Physical activity/exercise and diabetes: a position statement of the American Diabetes Association") + ". Diabetes Care. 2016;39(11):2065–2079. Haber: " + ext("https://www.ajmc.com/view/american-diabetes-association-issues-recommendations-for-physical-activity-exercise", "AJMC") + ".",
        "Bull FC, Al-Ansari SS, Biddle S, et al. " + ext("https://bjsm.bmj.com/content/54/24/1451", "World Health Organization 2020 guidelines on physical activity and sedentary behaviour") + ". Br J Sports Med. 2020;54(24):1451–1462.",
      ])}
    </div>
  </section>
</main>'''

YY_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.yy-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var $ = function(id){ return document.getElementById(id); }, KEY = 'drihsaneren.yemekyuruyus.v1';
  var lock = null, ctx = null, snd = $('yy-sound');
''' + WAKE_JS + '''
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function seg(id){ return $(id).querySelector('[aria-pressed="true"]').getAttribute('data-v'); }
  function pick(id, v){ $(id).querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x.getAttribute('data-v') === v ? 'true' : 'false'); }); }
  function mmss(s){ s = Math.max(0, Math.ceil(s)); var m = Math.floor(s / 60), r = s % 60; return m + ':' + (r < 10 ? '0' : '') + r; }
  function load(){ try { return JSON.parse(localStorage.getItem(KEY)) || {d: {}}; } catch (e) { return {d: {}}; } }
  function save(o){ try { localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {} }
  function dkey(d){ return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2); }
  function paint(){
    var o = load(), now = new Date(), t = o.d[dkey(now)] || {}, n = 0;
    $('yy-today').querySelectorAll('[data-m]').forEach(function(el){ var on = !!t[el.getAttribute('data-m')]; el.classList.toggle('on', on); el.querySelector('b').textContent = on ? '✓' : '–'; if (on) n++; });
    $('yy-sum').textContent = fill(S.sum, {n: n});
    var box = $('yy-days'); box.innerHTML = '';
    for (var i = 6; i >= 0; i--){
      var d = new Date(now.getFullYear(), now.getMonth(), now.getDate() - i), r = o.d[dkey(d)] || {}, c = Object.keys(r).length, el = document.createElement('div');
      el.innerHTML = '<b>' + c + '</b>' + S['d' + ((d.getDay() + 6) % 7)];
      if (c) el.classList.add('on'); if (!i) el.classList.add('now');
      box.appendChild(el);
    }
  }
  var total = 600, left = 600, t0 = 0, run = false, iv = null, lastMin = -1, halfDone = false;
  function setTotal(){ total = left = (+seg('yy-min')) * 60; $('yy-sec').textContent = mmss(left); halfDone = false; lastMin = -1; }
  function tick(){
    var rem = left - (performance.now() - t0) / 1000;
    $('yy-sec').textContent = mmss(rem);
    var m = Math.ceil(rem / 60);
    if (m !== lastMin && rem < total - 1 && rem > 1){ if (lastMin !== -1) beep(660, .12, .12); lastMin = m; }
    if (!halfDone && rem <= total / 2){ halfDone = true; $('yy-phase').textContent = S.half; beep(880, .2, .16); }
    if (rem <= 0) finish();
  }
  function finish(){
    clearInterval(iv); iv = null; run = false; wake(false);
    beep(660, .2, .18); setTimeout(function(){ beep(880, .2, .18); }, 220); setTimeout(function(){ beep(1100, .35, .18); }, 440);
    var o = load(), k = dkey(new Date()); o.d[k] = o.d[k] || {}; o.d[k][seg('yy-meal')] = 1;
    var ks = Object.keys(o.d).sort(); while (ks.length > 120) delete o.d[ks.shift()];
    save(o); paint();
    $('yy-phase').textContent = S.done; $('yy-cue').textContent = S.donec; $('yy-sec').textContent = '✓';
    $('yy-go').textContent = S.start; $('yy-go').classList.remove('stop'); left = 0;
  }
  ['yy-meal', 'yy-min'].forEach(function(id){
    $(id).addEventListener('click', function(e){
      var b = e.target.closest('button'); if (!b || run) return;
      pick(id, b.getAttribute('data-v')); if (id === 'yy-min' || left <= 0 || left === total) setTotal();
    });
  });
  $('yy-go').addEventListener('click', function(){
    if (run){
      clearInterval(iv); iv = null; run = false; wake(false); left = Math.max(0, left - (performance.now() - t0) / 1000);
      $('yy-phase').textContent = S.paused; $('yy-cue').textContent = S.pausedc; this.textContent = S.start; this.classList.remove('stop'); return;
    }
    if (left <= 0) setTotal();
    try { ctx = ctx || new (window.AudioContext || window.webkitAudioContext)(); if (ctx.resume) ctx.resume(); } catch (e) {}
    run = true; wake(true); t0 = performance.now(); this.textContent = S.stop; this.classList.add('stop');
    $('yy-phase').textContent = halfDone ? S.half : S.run; $('yy-cue').textContent = S.runc; beep(880, .3, .2);
    clearInterval(iv); iv = setInterval(tick, 250); tick();
  });
  $('yy-reset').addEventListener('click', function(){
    clearInterval(iv); iv = null; run = false; wake(false); setTotal();
    $('yy-phase').textContent = S.ready; $('yy-cue').textContent = S.readyc; $('yy-go').textContent = S.start; $('yy-go').classList.remove('stop');
  });
  var h = new Date().getHours(); pick('yy-meal', h < 11 ? 'k' : h < 16 ? 'o' : 'a');
  setTotal(); paint();
  window.__yy = {st: function(){ return [run, Math.round(left), seg('yy-meal')]; }, ff: function(s){ t0 -= s * 1000; }};
})();
</script>
'''

page("yemek-sonrasi-yuruyus.html", "Yemek Sonrası Yürüyüş",
     "Yemekten sonra kısa bir yürüyüş kan şekerinin yükselmesini yumuşatır. Öğün ve süre seçin, zamanlayıcıyla yürüyün, gün içinde hangi öğünlerden sonra yürüdüğünüzü işaretleyin.",
     "yemek-sonrasi-yuruyus.html", SELF13_CSS, YY_BODY, YY_JS,
     seo_title="Yemek Sonrası Yürüyüş: Kan Şekeri İçin 10 Dakikalık Zamanlayıcı | İhsan Eren",
     about={"@type": "ExercisePlan", "name": "Yemek sonrası yürüyüş"},
     faq_items=YY_FAQ)

# ------------------------------------------------------------------ 2 · DENGE ANTRENMANI (Otago'dan uyarlanmış)
_ex2("db_tstand", "tandem", "Topuk-burun duruş", "Bir ayağınızı diğerinin tam önüne, topuğunuz arkadaki ayağın parmak ucuna değecek şekilde koyun ve öyle durun. Sonra ayaklarınızın yerini değiştirin.", "")
_ex2("db_sls", "sls", "Tek ayak üstünde durma", "Bir ayağınızı yerden hafifçe kaldırın ve diğer ayağınızın üstünde durun. Sonra diğer ayağınıza geçin.", "")
_ex2("db_twalk", "tandem", "Topuk-burun yürüyüş", "Düz bir çizgi boyunca, her adımda topuğunuzu öndeki ayağın parmak ucuna değdirerek 20 adım yürüyün; dönün ve tekrarlayın.", "")
_ex2("db_side", "sidestep", "Yana yürüme", "Ellerinizi belinize koyun. Sağa doğru 10 yan adım, sonra sola doğru 10 yan adım atın. Ayaklarınızı çarpmadan, yere iyi basarak ilerleyin.", "")
_ex2("db_toe", "heel2", "Parmak ucunda yürüme", "Topuklarınızı kaldırıp parmak uçlarınızda 10 adım yürüyün; dönün ve tekrarlayın.", "")
_ex2("db_sts", "sts", "Sandalyeden kalkıp oturma", "Çok alçak olmayan, sağlam bir sandalyeye oturun. Öne eğilip ayağa kalkın, yavaşça oturun. Başta ellerinizden destek alın; kolaylaştıkça destekten vazgeçin.", "")
DB_KEYS = [("db_tstand", "hold"), ("db_sls", "hold"), ("db_twalk", "reps"), ("db_side", "reps"), ("db_toe", "reps"), ("db_sts", "reps")]
DB_STAGE = "\n".join(
    f'''            <div class="db-ex gu-step" data-i="{i}" data-mode="{mode}"{" hidden" if i else ""}>
              {SV[k]}
              <div><h3>{EXT[k][0]}</h3><p>{EXT[k][1]}</p></div>
            </div>''' for i, (k, mode) in enumerate(DB_KEYS))

DB_FAQ = [
 ("Denge egzersizi düşmeleri gerçekten azaltır mı?", "Evet. 108 rastgele kontrollü çalışmayı ve 23.407 kişiyi kapsayan Cochrane derlemesinde egzersiz, toplumda yaşayan yaşlılarda düşme sıklığını %23, düşen kişi sayısını %15 azalttı (kanıt düzeyi yüksek). Denge ve işlevsel egzersizler düşme sıklığını %24, düşen kişi sayısını %13 azalttı; çoğunlukla denge ve güçlendirmeyi birleştiren programlarda azalma %34 ve %22 idi (kanıt düzeyi orta). Bu sayfanın temel aldığı Otago programına ilişkin 7 çalışmanın analizinde (1.503 kişi, yaş ortalaması 81,6) düşmeler %32 azaldı."),
 ("Neden sandalyeye değil de tezgâha tutunmalıyım?", "Sandalye gibi kayabilecek ya da devrilebilecek bir şeye tutunmayın. Mutfak tezgâhı ya da ağır bir masa gibi sabit bir yüzeyin yanında çalışın. Seviye ilerledikçe tutunmayı azaltın, ama sabit yüzey her zaman elinizin yetişeceği yerde olsun."),
 ("Ne kadar sürede fark ederim?", "Dünya Düşme Kılavuzu, düşmeleri önlemek için haftada en az 3 kez yapılan, en az 12 hafta süren, kişiye göre ayarlanmış ve kademeli ilerleyen bir denge ve işlevsel egzersiz programı öneriyor; daha uzun sürdürmek daha çok yarar sağlıyor. Bu sayfa, haftada 3 seans hedefine ulaştığınız haftaları sayar."),
 ("Yürüyüş yeterli değil mi?", "Yürüyüş kalp ve genel sağlık için çok değerli. Ancak Cochrane derlemesinde, yalnızca yürüyüş programlarının düşmeler üzerindeki etkisini belirlemeye yetecek kanıt bulunamadı; düşmeleri önlemede dengeyi zorlayan ve bacakları güçlendiren egzersizler öne çıkıyor. Tai chi de bir seçenek: aynı derlemede düşme sıklığını %19 azalttı (kanıt düzeyi düşük)."),
 ("Hangi seviyeden başlamalıyım?", "Emin değilseniz 1. seviyeden, iki elle tutunarak başlayın. Bir hareketi birkaç seans boyunca rahatça ve güvenle yapabildiğinizde bir sonraki seviyeye geçin. Hareketler sizi biraz zorlamalı, ama düşme riski yaratmamalı. Düşme riskinizi ölçmek için 4 aşamalı denge testine bakabilirsiniz."),
 ("Ne zaman egzersizi bırakmalıyım?", "Egzersiz sırasında baş dönmesi, göğüs ağrısı ya da nefes darlığı olursa durun ve hekiminize başvurun. Bir hastalık nedeniyle programa ara verdiyseniz, yeniden başlamadan önce sizi yönlendiren fizyoterapistle konuşun."),
]

DB_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Denge antrenmanı</h1>
    <p class="lede">Yaşlılarda düşmeleri önlemenin en iyi kanıtlanmış yollarından biri, dengeyi zorlayan ve bacakları güçlendiren egzersizlerdir. Bu sayfa, Yeni Zelanda’da geliştirilen ve düşmeleri azalttığı gösterilen Otago programındaki altı denge hareketini üç destek seviyesiyle sunar: sizi hareket hareket yönlendirir, duruş sürelerini sayar, haftalık seanslarınızı ve hedefe ulaştığınız haftaları kaydeder.</p>
    <p class="meta">Son güncelleme: 23 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%24</b><span>Denge ve işlevsel egzersizlerle düşme sıklığındaki azalma (Cochrane, 108 çalışma, 23.407 kişi)</span></div>
        <div class="stat"><b>%32</b><span>Otago programıyla düşmelerde azalma (7 çalışma, 1.503 kişi)</span></div>
        <div class="stat"><b>Haftada 3</b><span>Önerilen seans sayısı</span></div>
        <div class="stat"><b>En az 12 hafta</b><span>Düşmeleri azaltmak için önerilen program süresi (Dünya Düşme Kılavuzu)</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Zamanlayıcıyla birlikte yapın</p>
      <h2>Seviyenizi seçin ve başlayın</h2>
      <p class="soft">Mutfak tezgâhı gibi sabit bir yüzeyin yanında durun; mümkünse yakınınızda biri olsun. Duruş hareketlerinde zamanlayıcı her ayak için 10 saniye sayar; yürüyüş hareketlerinde adımları tamamlayınca İleri’ye basın.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <p class="lbl">Destek seviyesi</p>
            <div class="seg" role="group" aria-label="Destek seviyesi" id="db-lv">
              <button type="button" data-v="1" aria-pressed="true">1. seviye</button>
              <button type="button" data-v="2" aria-pressed="false">2. seviye</button>
              <button type="button" data-v="3" aria-pressed="false">3. seviye</button>
            </div>
            <p class="db-sup" id="db-sup"></p>
            <label class="mz-chk"><input type="checkbox" id="db-sound" checked> Sesli uyarı</label>
            <p class="gd-week" id="db-week"></p>
            <p class="db-weeks" id="db-weeks"></p>
            <div class="days7" id="db-days" aria-label="Son 7 gün"></div>
          </div>
          <div class="bt-out">
            <div class="gd-stage">
{DB_STAGE}
            </div>
            <div class="gu-dots" id="db-dots" aria-hidden="true"></div>
          </div>
          <div class="bt-run" id="db-run">
            <div class="yh-time"><b id="db-sec">–</b><span id="db-unit">saniye</span></div>
            <p class="bt-phase" id="db-phase" aria-live="polite">Hazır</p>
            <p class="bt-cue" id="db-cue">Sabit bir yüzeyin yanında durun ve Başla’ya basın.</p>
            <button type="button" class="bt-tap" id="db-go">Başla</button>
            <div class="controls" style="margin-top:10px;justify-content:center">
              <button type="button" class="cta ghost" id="db-prev">Geri</button>
              <button type="button" class="cta ghost" id="db-reset">Sıfırla</button>
            </div>
          </div>
        </div>
        <div class="db-strings" hidden>
          <span data-k="l1">İki elinizle tezgâha tutunun.</span>
          <span data-k="l2">Tek elinizle tezgâha hafifçe tutunun.</span>
          <span data-k="l3">Tutunmadan yapın; tezgâh elinizin yetişeceği yerde olsun.</span>
          <span data-k="ready">Hazır</span>
          <span data-k="readyc">Sabit bir yüzeyin yanında durun ve Başla’ya basın.</span>
          <span data-k="start">Başla</span>
          <span data-k="next">İleri</span>
          <span data-k="pause">Durdur</span>
          <span data-k="get">Hazırlanın</span>
          <span data-k="side1">Birinci ayak</span>
          <span data-k="sw">Ayak değiştirin</span>
          <span data-k="side2">İkinci ayak</span>
          <span data-k="holdc">Dik durun, karşıya bakın, nefesinizi tutmayın.</span>
          <span data-k="reps">Adımları tamamlayın</span>
          <span data-k="repsc">Bitince İleri’ye basın.</span>
          <span data-k="paused">Durduruldu</span>
          <span data-k="pausedc">Devam etmek için Başla’ya basın.</span>
          <span data-k="done">Seans tamam</span>
          <span data-k="donec">Haftada 3 seansı hedefleyin; hareketler kolaylaşınca bir üst seviyeye geçin.</span>
          <span data-k="sec">saniye</span>
          <span data-k="step">hareket</span>
          <span data-k="week">Bu hafta: {{n}} seans · hedef 3</span>
          <span data-k="weekok">Bu hafta {{n}} seans yaptınız; haftalık hedefe ulaştınız.</span>
          <span data-k="weeks">Hedefe ulaşılan hafta: {{n}} · hedef en az 12</span>
          <span data-k="d0">Pzt</span><span data-k="d1">Sal</span><span data-k="d2">Çar</span><span data-k="d3">Per</span><span data-k="d4">Cum</span><span data-k="d5">Cmt</span><span data-k="d6">Paz</span>
        </div>
      </div>
      <p class="count">Seanslarınız yalnızca bu cihazda saklanır; hiçbir yere gönderilmez.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Üç seviye</h2>
        <ul class="tx">
          <li><b>1. seviye</b><span>İki elle sabit bir yüzeye tutunarak.</span></li>
          <li><b>2. seviye</b><span>Tek elle hafifçe tutunarak.</span></li>
          <li><b>3. seviye</b><span>Tutunmadan; sabit yüzey yine elinizin yetişeceği yerde.</span></li>
        </ul>
        <p class="soft" style="margin-top:12px">Otago programında destek, kişinin dengesine ve güvenine göre ayarlanır. Buradaki üç seviye bu ilkenin basitleştirilmiş bir uyarlamasıdır; size özel ilerlemeyi bir fizyoterapist belirleyebilir.</p>
      </div>
      <div>
        <h2>Güvenlik</h2>
        <ul class="dots">
          <li>Sandalye gibi kayabilecek bir şeye değil, tezgâh ya da ağır bir masa gibi sabit bir yüzeye tutunun.</li>
          <li>Kaymayan bir zeminde, düz tabanlı ayakkabıyla çalışın; mümkünse yakınınızda biri olsun.</li>
          <li>Hareketler sizi zorlamalı ama düşme riski yaratmamalı.</li>
          <li>Nefesinizi tutmayın.</li>
          <li>Baş dönmesi, göğüs ağrısı ya da nefes darlığı olursa durun.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(DB_FAQ)}
      <p class="soft" style="margin-top:18px">Dengenizi ölçmek için <a href="dort-asamali-denge-testi.html">4 aşamalı denge testine</a> ve <a href="denge-testi.html">10 saniye denge testine</a>, bacak gücünüz için <a href="guc-devresi.html">evde güç devresine</a>, ayrıntılı bilgi için <a href="dusme-onleme.html">düşmeleri önleme</a> rehberine bakabilirsiniz.</p>
      {CTA_CARD("Dengeniz ve düşme riskiniz", "denge antrenmanı ve düşme riski değerlendirmesi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Sherrington C, Fairhall NJ, Wallbank GK, et al. " + ext("https://doi.org/10.1002/14651858.CD012424.pub2", "Exercise for preventing falls in older people living in the community") + ". Cochrane Database Syst Rev. 2019;(1):CD012424. Haber: " + ext("https://mdedge.com/content/exercise-type-matters-fall-prevention-among-elderly", "MDedge") + ".",
        "Thomas S, Mackintosh S, Halbert J. " + ext("https://academic.oup.com/ageing/article/39/6/681/9467", "Does the ‘Otago exercise programme’ reduce mortality and falls in older adults? A systematic review and meta-analysis") + ". Age Ageing. 2010;39(6):681–687.",
        "Montero-Odasso M, van der Velde N, Martin FC, et al. " + ext("https://doi.org/10.1093/ageing/afac205", "World guidelines for falls prevention and management for older adults: a global initiative") + ". Age Ageing. 2022;51(9):afac205. Özet: " + ext("https://www.rospa.com/getattachment/aed8d4ea-ae48-4456-8893-e925a46c4dc6/World-Falls-Guidelines.pdf?lang=en-US", "RoSPA") + ".",
        "Royal Orthopaedic Hospital NHS Foundation Trust. " + ext("https://roh.nhs.uk/services-information/therapy/otago-strength-and-balance-exercises", "Otago strength and balance exercises") + ".",
      ])}
    </div>
  </section>
</main>'''

DB_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.db-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var $ = function(id){ return document.getElementById(id); }, KEY = 'drihsaneren.denge.v1';
  var lock = null, ctx = null, snd = $('db-sound');
''' + WAKE_JS + '''
  var EX = [].slice.call(root.querySelectorAll('.db-ex')), HOLD = 10;
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function lv(){ return $('db-lv').querySelector('[aria-pressed="true"]').getAttribute('data-v'); }
  function load(){ try { return JSON.parse(localStorage.getItem(KEY)) || {d: {}}; } catch (e) { return {d: {}}; } }
  function save(o){ try { localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {} }
  function dkey(d){ return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2); }
  function monday(d){ return new Date(d.getFullYear(), d.getMonth(), d.getDate() - ((d.getDay() + 6) % 7)); }
  function paintDays(){
    var o = load(), box = $('db-days'), now = new Date(); box.innerHTML = '';
    for (var i = 6; i >= 0; i--){
      var d = new Date(now.getFullYear(), now.getMonth(), now.getDate() - i), n = o.d[dkey(d)] || 0, el = document.createElement('div');
      el.innerHTML = '<b>' + n + '</b>' + S['d' + ((d.getDay() + 6) % 7)];
      if (n) el.classList.add('on'); if (!i) el.classList.add('now');
      box.appendChild(el);
    }
    var wk = {}, cur = dkey(monday(now));
    Object.keys(o.d).forEach(function(k){ var p = k.split('-'), m = dkey(monday(new Date(+p[0], +p[1] - 1, +p[2]))); wk[m] = (wk[m] || 0) + o.d[k]; });
    var thisW = wk[cur] || 0, ok = Object.keys(wk).filter(function(k){ return wk[k] >= 3; }).length;
    var w = $('db-week'); w.textContent = fill(thisW >= 3 ? S.weekok : S.week, {n: thisW}); w.classList.toggle('ok', thisW >= 3);
    $('db-weeks').textContent = fill(S.weeks, {n: ok});
  }
  function sup(){ $('db-sup').textContent = S['l' + lv()]; }
  function dots(cur){ var box = $('db-dots'); box.innerHTML = ''; EX.forEach(function(e, i){ var d = document.createElement('i'); if (i < cur) d.className = 'on'; box.appendChild(d); }); }
  function show(i){ EX.forEach(function(e, j){ e.hidden = j !== i; }); dots(i); }
  var idx = 0, stage = 'idle', left = 0, t0 = 0, iv = null, run = false, lastBeep = -1;
  function mode(i){ return EX[i].getAttribute('data-mode'); }
  function setTime(v, unit){ $('db-sec').textContent = v; $('db-unit').textContent = unit; }
  function enterEx(i){
    idx = i; show(i); clearInterval(iv); iv = null;
    if (mode(i) === 'hold'){ stage = 'get'; left = 3; t0 = performance.now(); $('db-phase').textContent = S.get; $('db-cue').textContent = S['l' + lv()]; run = true; iv = setInterval(tick, 100); tick(); $('db-go').textContent = S.pause; }
    else { stage = 'reps'; run = false; setTime((i + 1) + '/' + EX.length, S.step); $('db-phase').textContent = S.reps; $('db-cue').textContent = S.repsc; $('db-go').textContent = S.next; beep(880, .25, .18); }
  }
  function tick(){
    var rem = left - (performance.now() - t0) / 1000, c = Math.ceil(rem);
    setTime(String(Math.max(0, c)), S.sec);
    if ((stage === 's1' || stage === 's2') && c <= 3 && c >= 1 && c !== lastBeep){ lastBeep = c; beep(660, .1, .12); }
    if (rem > 0) return;
    if (stage === 'get'){ stage = 's1'; left = HOLD; t0 = performance.now(); lastBeep = -1; $('db-phase').textContent = S.side1; $('db-cue').textContent = S.holdc; beep(880, .35, .2); return; }
    if (stage === 's1'){ stage = 'sw'; left = 3; t0 = performance.now(); $('db-phase').textContent = S.sw; beep(520, .3, .18); return; }
    if (stage === 'sw'){ stage = 's2'; left = HOLD; t0 = performance.now(); lastBeep = -1; $('db-phase').textContent = S.side2; beep(880, .35, .2); return; }
    next();
  }
  function next(){ if (idx + 1 < EX.length) enterEx(idx + 1); else finish(); }
  function finish(){
    clearInterval(iv); iv = null; run = false; stage = 'idle'; wake(false); dots(EX.length);
    beep(660, .2, .18); setTimeout(function(){ beep(880, .2, .18); }, 220); setTimeout(function(){ beep(1100, .35, .18); }, 440);
    var o = load(), k = dkey(new Date()); o.d[k] = (o.d[k] || 0) + 1;
    var ks = Object.keys(o.d).sort(); while (ks.length > 400) delete o.d[ks.shift()];
    save(o); paintDays();
    $('db-phase').textContent = S.done; $('db-cue').textContent = S.donec; setTime('✓', ''); $('db-go').textContent = S.start; idx = 0;
  }
  $('db-go').addEventListener('click', function(){
    try { ctx = ctx || new (window.AudioContext || window.webkitAudioContext)(); if (ctx.resume) ctx.resume(); } catch (e) {}
    if (stage === 'idle'){ wake(true); enterEx(0); return; }
    if (stage === 'reps'){ next(); return; }
    if (run){ clearInterval(iv); iv = null; run = false; left = Math.max(0, left - (performance.now() - t0) / 1000); $('db-phase').textContent = S.paused; $('db-cue').textContent = S.pausedc; this.textContent = S.start; return; }
    run = true; t0 = performance.now(); this.textContent = S.pause; iv = setInterval(tick, 100); tick();
  });
  $('db-prev').addEventListener('click', function(){ if (stage === 'idle' || idx === 0) return; enterEx(idx - 1); });
  $('db-reset').addEventListener('click', function(){
    clearInterval(iv); iv = null; run = false; stage = 'idle'; idx = 0; wake(false); show(0);
    setTime('–', S.sec); $('db-phase').textContent = S.ready; $('db-cue').textContent = S.readyc; $('db-go').textContent = S.start;
  });
  $('db-lv').addEventListener('click', function(e){
    var b = e.target.closest('button'); if (!b) return;
    this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); sup();
  });
  sup(); show(0); paintDays();
  window.__db = {st: function(){ return [stage, idx, run]; }, skip: function(){ left = 0; t0 = performance.now(); }};
})();
</script>
'''

page("denge-antrenmani.html", "Denge Antrenmanı",
     "Düşmeleri önlemek için Otago programından uyarlanmış altı denge hareketi: üç destek seviyesi, duruş zamanlayıcısı, haftada 3 seans ve 12 haftalık hedef takibi.",
     "denge-antrenmani.html", SELF13_CSS, DB_BODY, DB_JS,
     seo_title="Denge Antrenmanı: Düşmeleri Önlemek İçin Otago Tarzı Ev Programı | İhsan Eren",
     about={"@type": "ExercisePlan", "name": "Denge antrenmanı (Otago programından uyarlanmış)"},
     faq_items=DB_FAQ)

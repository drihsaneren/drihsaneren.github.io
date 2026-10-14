# -*- coding: utf-8 -*-
# Kendine iyi bak, 4. tur: 10 saniye denge testi (sonra: hareket atıştırmalıkları, ağrıyı anlamak,
# egzersizde ağrı trafik ışığı). kapi_part.py'den sonra exec edilir (SELF2_CSS, WAKE_JS, _n hazır).

SELF4_CSS = SELF2_CSS + """
  /* denge testi */
  .bt{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);grid-template-areas:"opt run" "out run";gap:clamp(14px,3vw,24px) clamp(18px,4vw,40px);align-items:start}
  .bt-opt{grid-area:opt}.bt-run{grid-area:run}.bt-out{grid-area:out}
  @media (max-width:820px){.bt{grid-template-columns:1fr;grid-template-areas:"opt" "run" "out"}}
  .bt-ring{position:relative;width:min(240px,64vw);aspect-ratio:1;margin:6px auto 0}
  .bt-ring svg{width:100%;height:100%;transform:rotate(-90deg)}
  .bt-ring circle{fill:none;stroke-width:8}
  .bt-ring .bg{stroke:rgba(236,229,207,.12)}
  .bt-ring .fg{stroke:var(--foil);stroke-linecap:round}
  .bt-ring .ten{stroke:var(--sage);stroke-width:14;stroke-dasharray:3 362}
  .bt-ring.ok .fg{stroke:var(--sage)}
  .bt-ring .c{position:absolute;inset:0;display:grid;place-content:center;text-align:center}
  .bt-ring .c b{font-family:var(--display);font-weight:400;font-size:clamp(44px,8vw,58px);color:var(--ink);font-variant-numeric:tabular-nums;line-height:1}
  .bt-ring .c span{font-size:13px;color:var(--ink-soft);margin-top:6px;min-height:1em}
  .bt-phase{font-family:var(--display);font-size:clamp(22px,3vw,27px);color:var(--ink);text-align:center;margin:14px 0 4px;min-height:1.3em}
  .bt-cue{text-align:center;color:var(--ink-soft);font-size:15px;margin:0 0 12px;min-height:3em}
  .bt-tap{all:unset;box-sizing:border-box;display:block;width:100%;cursor:pointer;text-align:center;padding:20px 16px;border-radius:16px;
    font-family:var(--display);font-size:clamp(22px,3vw,26px);background:var(--foil);color:var(--ground)}
  .bt-tap.stop{background:#c9694f;color:#fff}
  .bt-tap:focus-visible{outline:3px solid var(--ink);outline-offset:3px}
  .trials{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin:14px 0 6px}
  .trials div{border:1px solid var(--line);border-radius:10px;padding:8px 6px;text-align:center;font-size:13px;color:var(--muted)}
  .trials div b{display:block;font-family:var(--display);font-weight:400;font-size:22px;color:var(--ink);font-variant-numeric:tabular-nums}
  .trials div.best{border-color:var(--foil);background:rgba(216,178,94,.10)}
  .bt-badge{display:inline-block;margin-top:10px;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;padding:4px 10px;border-radius:999px;background:var(--sage);color:var(--ground)}
  .bt-badge.no{background:rgba(236,229,207,.14);color:var(--ink)}
  .lbl{font-size:13px;color:var(--muted);margin:10px 0 0}
  .lbl:first-child{margin-top:0}
  .cmp .row em.you{font-style:normal}
"""

# Springer ve ark. 2007, üç denemenin en iyisi (sn)
BT_NORM = [("18–39", 44.7, 15.2), ("40–49", 41.9, 12.7), ("50–59", 41.2, 8.3), ("60–69", 32.1, 4.4), ("70–79", 21.5, 3.1), ("80+", 9.4, 1.9)]
BT_ROWS = "\n".join(
    f'<div class="row" data-o="{o}" data-c="{c}"><span>{a}<em class="you">siz</em></span><span class="bar"><i style="width:{o / 45 * 100:.1f}%"></i></span><b>{str(o).replace(".", ",")}</b></div>'
    for a, o, c in BT_NORM)

BT_FAQ = [
 ("10 saniye duramazsam erken ölüm riskim mi yüksek?", "Bu bir tanı değildir. Araştırma, testi yapamayanlarda sonraki yıllarda ölüm oranının daha yüksek olduğunu gösteriyor; ama bu bir ilişkidir, testin kendisi bir hastalığı göstermez. Araştırmacılar yakın zamanda geçirilen düşmeler ve fiziksel aktivite gibi etkenleri hesaba katamadıklarını belirtiyor. Testi bir uyarı ışığı gibi düşünüp dengenizi çalıştırmaya başlayabilir, kaygınız varsa hekiminizle konuşabilirsiniz."),
 ("Hangi ayakla yapmalıyım?", "Yaş ortalamalarının çıkarıldığı çalışmada katılımcılar ayağı kendileri seçti. İsterseniz iki ayağınızı ayrı ayrı deneyip karşılaştırabilirsiniz."),
 ("Gözler kapalıyken neden bu kadar zor?", "Dengeyi korurken gözlerden, iç kulaktan ve ayak tabanı ile eklemlerdeki duyulardan gelen bilgiyi birlikte kullanırız. Gözleri kapatınca bu bilgilerden biri ortadan kalkar. Ortalamalarda da fark büyük: 18–39 yaşta gözler açıkken 44,7 saniye, kapalıyken 15,2 saniye."),
 ("Dengemi geliştirebilir miyim?", "Evet. Toplumda yaşayan yaşlılarla yapılan çalışmaların Cochrane derlemesinde, denge ve günlük hareketleri çalıştıran egzersizler düşme sayısını %24 azalttı. Yukarıdaki egzersizlerle başlayabilir, düşmeleri önleme rehberine de bakabilirsiniz."),
]

BT_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>10 saniye denge testi</h1>
    <p class="lede">Bir ayağınızın üzerinde 10 saniye durabiliyor musunuz? 51–75 yaş arası 1.702 kişinin yaklaşık 7 yıl izlendiği bir araştırmada, her beş kişiden biri bunu yapamadı ve bu kişilerde izlem süresince ölüm oranı belirgin şekilde daha yüksekti. Bu basit test bir tanı değil, ama dengenize dair değerli bir ipucu. Aşağıdaki süreölçerle deneyin ve yaşınızdaki ortalamayla karşılaştırın.</p>
    <p class="meta">Son güncelleme: 14 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>5’te 1</b><span>51–75 yaş arası katılımcılardan 10 saniye tek ayak üzerinde duramayanların oranı</span></div>
        <div class="stat"><b>%17,5 / %4,6</b><span>Yaklaşık 7 yıllık izlemde ölüm oranı: testi yapamayanlar / yapabilenler</span></div>
        <div class="stat"><b>1,84 kat</b><span>Yaş, cinsiyet, kilo ve hastalıklar hesaba katıldıktan sonra yapamayanlardaki ölüm riski</span></div>
        <div class="stat"><b>%24</b><span>Denge ve günlük hareket egzersizleriyle yaşlılarda düşme sayısındaki azalma</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Kendinizi ölçün</p>
      <h2>Süreölçerle deneyin</h2>
      <p class="soft">Bir duvarın ya da sağlam bir tezgâhın yanında, çıplak ayakla durun. Telefonu kolayca dokunabileceğiniz bir yere koyun ya da birinden süreyi tutmasını isteyin. Üç deneme yapın; en iyisi sonucunuzdur.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <p class="lbl">Gözler</p>
            <div class="seg" role="group" aria-label="Gözler" id="bt-eye">
              <button type="button" data-v="o" aria-pressed="true">Açık</button>
              <button type="button" data-v="c" aria-pressed="false">Kapalı</button>
            </div>
            <p class="lbl">Yaşınız</p>
            <div class="seg" role="group" aria-label="Yaş grubu" id="bt-age">
              <button type="button" data-v="0" aria-pressed="false">18–39</button>
              <button type="button" data-v="1" aria-pressed="false">40–49</button>
              <button type="button" data-v="2" aria-pressed="true">50–59</button>
              <button type="button" data-v="3" aria-pressed="false">60–69</button>
              <button type="button" data-v="4" aria-pressed="false">70–79</button>
              <button type="button" data-v="5" aria-pressed="false">80+</button>
            </div>
          </div>
          <div class="bt-out">
            <div class="trials" id="bt-trials"><div><span>1. deneme</span><b>–</b></div><div><span>2. deneme</span><b>–</b></div><div><span>3. deneme</span><b>–</b></div></div>
            <div class="res" id="bt-res" hidden>
              <p class="lab" id="bt-lab"></p>
              <p id="bt-txt"></p>
              <span class="bt-badge" id="bt-badge"></span>
            </div>
          </div>
          <div class="bt-run">
            <div class="bt-ring" id="bt-ring"><svg viewBox="0 0 132 132" aria-hidden="true"><circle class="bg" cx="66" cy="66" r="58"/><circle class="ten" cx="66" cy="66" r="58" stroke-dashoffset="-79.5"/><circle class="fg" id="bt-arc" cx="66" cy="66" r="58" stroke-dasharray="364.4" stroke-dashoffset="364.4"/></svg>
              <div class="c"><b id="bt-sec">0,0</b><span id="bt-unit">saniye</span></div></div>
            <p class="bt-phase" id="bt-phase" aria-live="polite">Hazır</p>
            <p class="bt-cue" id="bt-cue">Başlat’a basınca 5 saniyelik hazırlanma süresi başlar.</p>
            <button type="button" class="bt-tap" id="bt-go">Başlat</button>
            <div class="controls" style="margin-top:10px;justify-content:center">
              <button type="button" class="cta ghost" id="bt-reset">Denemeleri sıfırla</button>
            </div>
            <label class="snd"><input type="checkbox" id="bt-sound" checked> Sesli uyarı</label>
          </div>
        </div>
        <div class="bt-strings" hidden>
          <span data-k="ready">Hazır</span>
          <span data-k="readyc">Başlat’a basınca 5 saniyelik hazırlanma süresi başlar.</span>
          <span data-k="prep">Hazırlanın</span>
          <span data-k="prepc">Kollarınızı göğsünüzde çapraz yapın, karşıda bir noktaya bakın. Sinyalle birlikte bir ayağınızı kaldırın.</span>
          <span data-k="prepcc">Kollarınızı göğsünüzde çapraz yapın. Sinyalle birlikte gözlerinizi kapatıp bir ayağınızı kaldırın.</span>
          <span data-k="go">Ayağınızı kaldırın</span>
          <span data-k="goc">Ayağınız yere değince ya da kollarınızı açınca ekrana dokunun.</span>
          <span data-k="ten">10 saniye! Devam edebildiğiniz kadar durun.</span>
          <span data-k="stop">Durdur</span>
          <span data-k="start">Başlat</span>
          <span data-k="next">Sonraki deneme</span>
          <span data-k="saved">{{n}}. deneme kaydedildi</span>
          <span data-k="savedc">Kısa bir dinlenmeden sonra bir sonraki denemeye geçin.</span>
          <span data-k="max">45 saniye: testin üst sınırına ulaştınız</span>
          <span data-k="done">Üç deneme tamamlandı</span>
          <span data-k="donec">En iyi süreniz ve karşılaştırma, deneme kutularının altında. Diğer göz koşulunu da deneyebilirsiniz.</span>
          <span data-k="sec">saniye</span>
          <span data-k="lab">En iyi süreniz: {{s}} saniye</span>
          <span data-k="cmp">Yaş grubunuzun ortalaması (gözler {{e}}): {{m}} saniye.</span>
          <span data-k="eo">açık</span>
          <span data-k="ec">kapalı</span>
          <span data-k="above">Ortalamanın üzerinde ya da yakınındasınız.</span>
          <span data-k="below">Ortalamanın altındasınız; denge egzersizleriyle geliştirebilirsiniz.</span>
          <span data-k="yes">10 saniyeyi geçtiniz</span>
          <span data-k="no">10 saniyenin altında</span>
          <span data-k="nonote">Bu bir tanı değildir. Denge egzersizlerine başlayabilir, kaygınız varsa hekiminiz ya da fizyoterapistinizle konuşabilirsiniz.</span>
        </div>
      </div>
      <p class="count">Sonuçlarınız yalnızca bu sayfada kalır; hiçbir yere gönderilmez.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nasıl yapılır?</h2>
        <ol class="steps">
          <li><span><strong>Çıplak ayakla</strong>, tutunabileceğiniz bir duvarın ya da tezgâhın yanında durun.</span></li>
          <li><span>Kollarınızı göğsünüzde <strong>çapraz</strong> yapın, karşınızda göz hizasındaki bir noktaya bakın.</span></li>
          <li><span>Bir ayağınızı kaldırın; kaldırdığınız ayak diğer ayak bileğinize <strong>yakın ama değmeden</strong> dursun. Süre, ayağınız yerden kalkınca başlar.</span></li>
          <li><span>Kollarınızı açarsanız, kaldırdığınız ayak yere ya da diğer bacağınıza değerse, duran ayağınız kayar ya da dönerse, gözler kapalı denemede gözünüzü açarsanız <strong>süre durur</strong>. Üst sınır 45 saniyedir.</span></li>
        </ol>
      </div>
      <div>
        <h2>Güvenle yapmak için</h2>
        <ul class="dots">
          <li>Dengeniz bozulursa hemen tutunabileceğiniz bir yerin yanında yapın.</li>
          <li>Son zamanlarda düştüyseniz, baş dönmeniz ya da belirgin bir denge sorununuz varsa testi yanınızda biri varken yapın; gözler kapalı denemeyi atlayın.</li>
          <li>Baş dönmesi, ağrı ya da fenalık hissederseniz durun.</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="normlar">
    <div class="wrap">
      <p class="eyebrow">Karşılaştırma</p>
      <h2>Yaşa göre ortalama süreler</h2>
      <p class="soft">Denge sorunu olmayan 549 sağlıklı yetişkinde, üç denemenin en iyisi (saniye; üst sınır 45). Gözler kapalıyken süreler belirgin şekilde kısalır. Yaş grubunuz yukarıdaki seçime göre işaretlenir.</p>
      <div class="seg" role="group" aria-label="Gözler" id="bt-neye">
        <button type="button" data-v="o" aria-pressed="true">Gözler açık</button>
        <button type="button" data-v="c" aria-pressed="false">Gözler kapalı</button>
      </div>
      <div class="cmp" id="bt-cmp">
{BT_ROWS}
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Dengenizi geliştirin</p>
      <h2>Evde dört denge egzersizi</h2>
      <p class="soft">Bir tezgâhın önünde, gerektiğinde tutunarak yapın. Kolaylaştıkça tutunmayı azaltın. Daha fazlası için <a href="dusme-onleme.html">düşmeleri önleme ve denge</a> rehberine bakabilirsiniz.</p>
      {ex_grid(["sls", "tandem", "sidestep", "heel2"], "ex four")}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(BT_FAQ)}
      {CTA_CARD("Dengeniz ve düşme riskiniz", "denge değerlendirmesi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Araujo CG, de Souza e Silva CG, Laukkanen JA, et al. " + ext("https://bjsm.bmj.com/content/56/17/975", "Successful 10-second one-legged stance performance predicts survival in middle-aged and older individuals") + ". Br J Sports Med. 2022;56(17):975.",
        "Springer BA, Marin R, Cyhan T, Roberts H, Gill NW. " + ext("https://geriatrictoolkit.missouri.edu/balance/Normative_Values_for_the_Unipedal_Stance_Test_Springer-JGPT.pdf", "Normative values for the unipedal stance test with eyes open and closed") + ". J Geriatr Phys Ther. 2007;30(1).",
        "Sherrington C, Fairhall NJ, Wallbank GK, et al. " + ext("https://www.cochrane.org/evidence/CD012424_exercise-preventing-falls-older-people-living-community", "Exercise for preventing falls in older people living in the community") + ". Cochrane Database Syst Rev. 2019;1:CD012424.",
      ])}
    </div>
  </section>
</main>'''

BT_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.bt-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var EN = document.documentElement.lang === 'en';
  var $ = function(id){ return document.getElementById(id); };
  var NORM = [[44.7, 15.2], [41.9, 12.7], [41.2, 8.3], [32.1, 4.4], [21.5, 3.1], [9.4, 1.9]];
  var go = $('bt-go'), secEl = $('bt-sec'), unit = $('bt-unit'), arc = $('bt-arc'), ring = $('bt-ring'), phaseEl = $('bt-phase'), cue = $('bt-cue'), snd = $('bt-sound');
  var C = 364.4, MAX = 45, PREP = 5, eye = 'o', age = 2, trials = [], phase = 'idle', t0 = 0, iv = null, tenDone = false, ctx = null, lock = null;
''' + WAKE_JS + '''
  function fmt(x){ var s = x.toFixed(1); return EN ? s : s.replace('.', ','); }
  function paintRing(x){ arc.style.strokeDashoffset = (C * (1 - Math.min(x, MAX) / MAX)).toFixed(1); ring.classList.toggle('ok', x >= 10); }
  function paintTrials(){
    var best = trials.length ? Math.max.apply(null, trials) : -1;
    $('bt-trials').querySelectorAll('div').forEach(function(d, j){
      d.querySelector('b').textContent = j < trials.length ? fmt(trials[j]) : '–';
      d.classList.toggle('best', j < trials.length && trials[j] === best);
    });
    var res = $('bt-res');
    if (!trials.length){ res.hidden = true; return; }
    res.hidden = false;
    var m = NORM[age][eye === 'o' ? 0 : 1];
    $('bt-lab').textContent = S.lab.replace('{s}', fmt(best));
    var txt = S.cmp.replace('{e}', eye === 'o' ? S.eo : S.ec).replace('{m}', fmt(m)) + ' ' + (best >= m * 0.85 ? S.above : S.below);
    var badge = $('bt-badge');
    if (eye === 'o'){ badge.hidden = false; badge.textContent = best >= 10 ? S.yes : S.no; badge.classList.toggle('no', best < 10); if (best < 10) txt += ' ' + S.nonote; }
    else badge.hidden = true;
    $('bt-txt').textContent = txt;
  }
  function stopTimer(){ clearInterval(iv); iv = null; }
  function idle(msg, c){
    phase = 'idle'; stopTimer(); wake(false);
    go.textContent = (trials.length && trials.length < 3) ? S.next : S.start; go.classList.remove('stop');
    phaseEl.textContent = msg || S.ready; cue.textContent = c || S.readyc;
  }
  function record(x, hitMax){
    stopTimer(); x = Math.min(x, MAX);
    trials.push(Math.round(x * 10) / 10); paintTrials();
    secEl.textContent = fmt(x); paintRing(x);
    beep(660, 0.15); setTimeout(function(){ beep(880, 0.3); }, 180);
    if (trials.length >= 3) idle(S.done, S.donec);
    else idle(hitMax ? S.max : S.saved.replace('{n}', trials.length), S.savedc);
  }
  function startPrep(){
    if (trials.length >= 3){ trials = []; paintTrials(); }
    phase = 'prep'; t0 = performance.now(); tenDone = false; wake(true);
    phaseEl.textContent = S.prep; cue.textContent = eye === 'o' ? S.prepc : S.prepcc;
    go.textContent = S.stop; go.classList.add('stop');
    secEl.textContent = String(PREP); unit.textContent = ''; paintRing(0);
    var lastS = PREP; beep(520, 0.08);
    stopTimer();
    iv = setInterval(function(){
      var el = (performance.now() - t0) / 1000;
      if (phase === 'prep'){
        var s = Math.ceil(PREP - el);
        if (s !== lastS && s > 0){ lastS = s; beep(520, 0.08); }
        secEl.textContent = String(Math.max(1, s));
        if (el >= PREP){ phase = 'run'; t0 = performance.now(); beep(880, 0.35); phaseEl.textContent = S.go; cue.textContent = S.goc; unit.textContent = S.sec; }
        return;
      }
      if (el >= MAX){ record(MAX, true); return; }
      if (!tenDone && el >= 10){ tenDone = true; cue.textContent = S.ten; beep(990, 0.2); }
      secEl.textContent = fmt(el); paintRing(el);
    }, 50);
  }
  function press(){
    if (phase === 'idle') startPrep();
    else if (phase === 'prep'){ secEl.textContent = fmt(0); unit.textContent = S.sec; idle(); }
    else if (phase === 'run') record((performance.now() - t0) / 1000, false);
  }
  go.addEventListener('click', press);
  document.addEventListener('keydown', function(e){ if (phase === 'run' && (e.code === 'Space' || e.key === ' ')){ e.preventDefault(); press(); } });
  root.querySelector('.bt').addEventListener('pointerdown', function(e){ if (phase === 'run' && !e.target.closest('button,input,label')) press(); });
  $('bt-reset').addEventListener('click', function(){ trials = []; paintTrials(); secEl.textContent = fmt(0); unit.textContent = S.sec; paintRing(0); idle(); });
  function seg(id, fn){ $(id).addEventListener('click', function(e){ var b = e.target.closest('button'); if (!b) return; this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); fn(b.getAttribute('data-v')); }); }
  var cmp = $('bt-cmp'), neye = 'o';
  function paintCmp(){
    var mx = neye === 'o' ? 45 : 16;
    cmp.querySelectorAll('.row').forEach(function(r, j){
      var n = +r.getAttribute(neye === 'o' ? 'data-o' : 'data-c');
      r.querySelector('i').style.width = (n / mx * 100).toFixed(1) + '%';
      r.querySelector('b').textContent = fmt(n);
      r.classList.toggle('me', j === age);
    });
  }
  seg('bt-eye', function(v){ eye = v; if (phase !== 'idle') idle(); trials = []; paintTrials(); secEl.textContent = fmt(0); unit.textContent = S.sec; paintRing(0); });
  seg('bt-age', function(v){ age = +v; paintTrials(); paintCmp(); });
  seg('bt-neye', function(v){ neye = v; paintCmp(); });
  document.addEventListener('visibilitychange', function(){ if (!document.hidden && phase !== 'idle') wake(true); });
  secEl.textContent = fmt(0); paintCmp(); idle();
})();
</script>
'''

page("denge-testi.html", "10 Saniye Denge Testi",
     "Bir ayağınızın üzerinde 10 saniye durabiliyor musunuz? Süreölçerle deneyin, yaşınızdaki ortalamayla karşılaştırın ve dengenizi geliştiren dört egzersizi öğrenin.",
     "denge-testi.html", SELF4_CSS, BT_BODY, BT_JS,
     seo_title="10 Saniye Denge Testi: Tek Ayak Üzerinde Durma Süreölçeri ve Yaş Ortalamaları | İhsan Eren",
     about={"@type": "MedicalTest", "name": "Tek ayak üzerinde durma testi"},
     faq_items=BT_FAQ)

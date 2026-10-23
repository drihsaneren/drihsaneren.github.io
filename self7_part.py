# -*- coding: utf-8 -*-
# Kendine iyi bak, 7. tur: nabız ölçer ve hedef nabız, bel–boy oranı. self6_part.py'den sonra exec edilir
# (SELF6_CSS, WAKE_JS hazır).

SELF7_CSS = SELF6_CSS + """
  /* nabız */
  .nb-z{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin:10px 0 4px}
  .nb-z div{border:1px solid var(--line);border-radius:12px;padding:10px 8px;text-align:center;font-size:12.5px;color:var(--muted)}
  .nb-z b{display:block;font-family:var(--display);font-weight:400;font-size:22px;color:var(--ink);font-variant-numeric:tabular-nums}
  .nb-z div.on{border-color:var(--foil);background:rgba(216,178,94,.1)}
  .nb-max{font-size:14px;color:var(--ink-soft);margin:4px 0 0}
  .nb-row{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:6px 0 2px}
  /* bel–boy oranı */
  .bb-in{display:flex;gap:18px;flex-wrap:wrap}
  .bb-in div{display:grid;gap:6px}
  .bb-big{font-family:var(--display);font-weight:400;font-size:clamp(56px,11vw,84px);line-height:1;color:var(--ink);text-align:center;font-variant-numeric:tabular-nums;margin:6px 0 2px}
  .bb-cap{text-align:center;font-size:14px;color:var(--ink-soft);margin:0 0 18px}
  .bb-g{position:relative;height:14px;border-radius:999px;background:linear-gradient(90deg,rgba(236,229,207,.16) 0 12.5%,var(--sage) 12.5% 37.5%,var(--foil) 37.5% 62.5%,#c9694f 62.5% 100%)}
  .bb-m{position:absolute;top:-7px;width:5px;height:28px;border-radius:3px;background:var(--ink);box-shadow:0 0 0 2px var(--ground);transform:translateX(-50%);transition:left .3s}
  .bb-t{position:relative;height:20px;font-size:12px;color:var(--muted);margin-top:6px}
  .bb-t span{position:absolute;transform:translateX(-50%)}
  .bb-k{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:12.5px;color:var(--muted);margin-top:8px}
  .bb-k i{display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:6px;vertical-align:-1px}
"""

# ------------------------------------------------------------------ 1 · NABIZ ÖLÇER VE HEDEF NABIZ
NB_FAQ = [
 ("Ne zaman ölçmeliyim?", "Amerikan Kalp Derneği, dinlenme nabzını sabah iyi bir uykudan sonra, yataktan kalkmadan ve kahve içmeden ölçmeyi öneriyor. İngiltere Kalp Vakfı da doğru bir sonuç için her gün aynı saatte ölçmenizi öneriyor. Ölçümden önce 5 dakika oturun ya da uzanın; öncesinde sigara ve kafeinden uzak durun."),
 ("Egzersize yeni başlıyorum, hangi aralıkta çalışmalıyım?", "Hedef aralığın alt ucuyla, en yüksek nabzınızın yaklaşık %50’siyle başlayıp yavaş yavaş artırabilirsiniz. Zamanla en yüksek nabzınızın %85’ine kadar rahatça çalışabilirsiniz."),
 ("220 eksi yaş formülü herkes için doğru mu?", "Hayır, kaba bir tahmindir. Bazı ilaçlar nabzı düşürür; bu durumda en yüksek nabzınız ve hedef aralığınız da daha düşük olabilir. Kalp hastalığınız varsa ya da düzenli ilaç kullanıyorsanız hedef nabzınızı hekiminize sorun. 18.712 kişiyi kapsayan bir meta-analize göre bu formül 40 yaş altında en yüksek nabzı biraz fazla, 40 yaşından sonra giderek daha az tahmin ediyor; aynı çalışmada önerilen formül 208 − 0,7 × yaş. 70 yaşında iki formül arasındaki fark dakikada yaklaşık 10 vuru."),
 ("Nabzım düzensizse ne yapmalıyım?", "İngiltere’nin ulusal sağlık kılavuzu NICE, nefes darlığı, çarpıntı, baş dönmesi ya da bayılma, göğüste rahatsızlık gibi yakınmaları olanlarda nabzın elle kontrol edilmesini, nabız düzensizse atriyal fibrilasyon için 12 derivasyonlu EKG çekilmesini öneriyor. Nabzınız düzensizse hekiminize başvurabilirsiniz; göğüs ağrısı, ciddi nefes darlığı ya da bayılma varsa 112’yi arayın."),
 ("Akıllı saatimle ölçebilir miyim?", "Egzersiz sırasında nabzınızı izlemek için giyilebilir bir cihaz da kullanabilirsiniz. Elle saymak, cihazınızın gösterdiği değeri ara sıra kontrol etmenin basit bir yoludur."),
]

NB_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Nabız ölçer ve hedef nabız</h1>
    <p class="lede">Nabzınızı elle saymayı biliyor musunuz? Dinlenme nabzınız ve ritminin düzenli olup olmadığı, kalbinizle ilgili basit ama değerli bilgiler verir. Egzersiz sırasında saydığınız nabız da ne kadar yoğun çalıştığınızı gösterir. Aşağıdaki süreölçerle sayın, sonucunuzu yaşınıza göre hedef aralıkla karşılaştırın.</p>
    <p class="meta">Son güncelleme: 16 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>60–100</b><span>Yetişkinlerde olağan dinlenme nabzı (atım/dakika)</span></div>
        <div class="stat"><b>220 − yaş</b><span>En yüksek nabzın kaba tahmini</span></div>
        <div class="stat"><b>%50–70</b><span>Orta yoğunlukta egzersizde hedef nabız aralığı</span></div>
        <div class="stat"><b>%70–85</b><span>Yüksek yoğunlukta egzersizde hedef nabız aralığı</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Kendinizi ölçün</p>
      <h2>Nabzınızı sayın</h2>
      <p class="soft">İşaret ve orta parmağınızı bileğinizin iç yüzüne, başparmak tarafına koyun. Süreölçeri başlatın ve süre bitene kadar hissettiğiniz atımları sayın. Ritim düzensiz geliyorsa tam 60 saniye sayın.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <p class="lbl"><label for="nb-age">Yaşınız</label></p>
            <input class="cs-age" id="nb-age" type="number" inputmode="numeric" min="15" max="100" placeholder="ör. 50">
            <div id="nb-zw" hidden>
              <div class="nb-z" id="nb-z">
                <div data-z="0"><b id="nb-z0"></b>Hafif</div>
                <div data-z="1"><b id="nb-z1"></b>Orta</div>
                <div data-z="2"><b id="nb-z2"></b>Yüksek</div>
              </div>
              <p class="nb-max" id="nb-max"></p>
            </div>
            <p class="lbl">Ne zaman ölçüyorsunuz?</p>
            <div class="seg" role="group" aria-label="Ölçüm zamanı" id="nb-ctx">
              <button type="button" data-v="rest" aria-pressed="true">Dinlenirken</button>
              <button type="button" data-v="ex" aria-pressed="false">Egzersizde</button>
            </div>
            <p class="lbl">Sayma süresi</p>
            <div class="seg" role="group" aria-label="Sayma süresi" id="nb-dur">
              <button type="button" data-v="30" aria-pressed="true">30 saniye</button>
              <button type="button" data-v="60" aria-pressed="false">60 saniye</button>
            </div>
          </div>
          <div class="bt-out">
            <p class="lbl"><label for="nb-beats">Kaç atım saydınız?</label></p>
            <div class="nb-row">
              <input class="cs-age" id="nb-beats" type="number" inputmode="numeric" min="5" max="150" placeholder="ör. 36">
              <button type="button" class="cta" id="nb-calc">Hesapla</button>
            </div>
            <p class="lbl">Ritim nasıldı?</p>
            <div class="seg" role="group" aria-label="Ritim" id="nb-rh">
              <button type="button" data-v="reg" aria-pressed="true">Düzenli</button>
              <button type="button" data-v="irr" aria-pressed="false">Düzensiz</button>
              <button type="button" data-v="uns" aria-pressed="false">Emin değilim</button>
            </div>
            <div class="res" id="nb-res" hidden>
              <p class="lab" id="nb-lab"></p>
              <p id="nb-txt"></p>
              <span class="bt-badge" id="nb-badge"></span>
              <div class="cs-acts"><a class="cta" id="nb-wa" href="#" target="_blank" rel="noopener">Sonucumu WhatsApp’tan gönder</a></div>
            </div>
            <div id="nb-histw" style="margin-top:20px" hidden>
              <p class="lbl">Önceki ölçümleriniz (bu cihazda)</p>
              <ul class="cs-hist" id="nb-hist"></ul>
            </div>
          </div>
          <div class="bt-run">
            <div class="yh-time"><b id="nb-sec">30</b><span>saniye</span></div>
            <p class="bt-phase" id="nb-phase" aria-live="polite">Hazır</p>
            <p class="bt-cue" id="nb-cue">Parmaklarınızı bileğinize yerleştirin, atımı hissedince başlatın.</p>
            <button type="button" class="bt-tap" id="nb-go">Başla</button>
            <label class="snd"><input type="checkbox" id="nb-sound" checked> Sesli uyarı</label>
          </div>
        </div>
        <div class="nb-strings" hidden>
          <span data-k="ready">Hazır</span>
          <span data-k="readyc">Parmaklarınızı bileğinize yerleştirin, atımı hissedince başlatın.</span>
          <span data-k="run">Sayın</span>
          <span data-k="runc">Her atımı içinizden sayın; süre bitince sesli uyarı gelir.</span>
          <span data-k="done">Süre doldu</span>
          <span data-k="donec">Saydığınız atım sayısını aşağıya yazın.</span>
          <span data-k="start">Başla</span>
          <span data-k="stop">Durdur</span>
          <span data-k="sec">saniye</span>
          <span data-k="zone">{{a}}–{{b}}</span>
          <span data-k="max">Tahmini en yüksek nabzınız: {{m}} atım/dakika</span>
          <span data-k="lab">Nabzınız: {{v}} atım/dakika</span>
          <span data-k="rlow40">Dinlenme nabzınız 40’ın altında. Sporcu ya da çok aktif kişilerde 40’a kadar inebilir. Baygınlık hissi, bayılma, aşırı yorgunluk ya da baş dönmesi varsa hekiminize görünün.</span>
          <span data-k="rlow">60’ın altındaki dinlenme nabzı çok formda ya da sporcu kişilerde, uykuda ve beta bloker kullananlarda olağan olabilir. Baygınlık hissi, bayılma, aşırı yorgunluk ya da baş dönmesi varsa hekiminize görünün.</span>
          <span data-k="rok">Yetişkinlerde dinlenme nabzı için olağan aralık 60–100 atım/dakikadır.</span>
          <span data-k="rhigh">Dinlenirken nabzınız 100’ün üzerinde. 5 dakika oturup dinlendikten sonra, kafein ve sigaradan uzakken yeniden ölçün. Belirgin bir neden yokken dinlenme nabzınız hızlıysa hekiminize görünün.</span>
          <span data-k="irr">Ritminiz düzensiz geldi. Düzensiz nabız, atriyal fibrilasyon gibi bir ritim bozukluğunun işareti olabilir; 65 yaş üstünde bu daha olasıdır. Arada bir atlayan atım genellikle sorun değildir. Düzensizlik sürüyorsa ya da emin değilseniz hekiminize görünün.</span>
          <span data-k="irr30">Düzensiz ritimde tam 60 saniye saymak daha doğru sonuç verir.</span>
          <span data-k="noage">Egzersiz yoğunluğunu karşılaştırmak için yaşınızı girin.</span>
          <span data-k="e0">Hafif yoğunluk: en yüksek nabzınızın %{{p}}’i. Orta yoğunluğa çıkmak için temponuzu biraz artırabilirsiniz.</span>
          <span data-k="e1">Orta yoğunluk: en yüksek nabzınızın %{{p}}’i.</span>
          <span data-k="e2">Yüksek yoğunluk: en yüksek nabzınızın %{{p}}’i.</span>
          <span data-k="e3">En yüksek nabzınızın %{{p}}’i: hedef aralığın (%85’e kadar) üzerindesiniz. Temponuzu düşürebilirsiniz.</span>
          <span data-k="bok">Olağan aralıkta</span>
          <span data-k="bno">Aralığın dışında</span>
          <span data-k="bl">Hafif</span>
          <span data-k="bm">Orta yoğunluk</span>
          <span data-k="bv">Yüksek yoğunluk</span>
          <span data-k="bx">Hedefin üzerinde</span>
          <span data-k="birr">Ritim düzensiz</span>
          <span data-k="hrest">dinlenirken</span>
          <span data-k="hex">egzersizde</span>
          <span data-k="hirr">düzensiz</span>
          <span data-k="bpm">atım/dk</span>
          <span data-k="wa">Merhaba, drihsaneren.com’daki nabız ölçerle nabzımı ölçtüm: {{v}} atım/dakika ({{c}}). Bilgi almak istiyorum.</span>
        </div>
      </div>
      <p class="count">Sonuçlarınız yalnızca bu cihazda saklanır; hiçbir yere gönderilmez.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nabız nasıl sayılır?</h2>
        <ol class="steps">
          <li><span>Ölçümden önce <strong>5 dakika</strong> oturun ya da uzanın; sigara ve kafeinden uzak durun.</span></li>
          <li><span>Avucunuz yukarı bakacak, dirseğiniz hafif bükük olsun. <strong>İşaret ve orta parmağınızı</strong> öbür bileğinizin iç yüzüne, başparmak tarafına koyun. Başparmağınızla saymayın.</span></li>
          <li><span>Atımı hissedemiyorsanız biraz daha bastırın ya da parmaklarınızı kaydırın. Bileğinizde bulamazsanız boynunuzda, çenenizin hemen altında, nefes borusunun yanında da sayabilirsiniz; hafifçe bastırın.</span></li>
          <li><span><strong>30 saniye</strong> sayıp ikiyle çarpın ya da <strong>60 saniye</strong> sayın. Ritim düzensizse her zaman 60 saniye sayın.</span></li>
        </ol>
      </div>
      <div>
        <h2>Ne zaman hemen yardım almalı?</h2>
        <ul class="dots redflags">
          <li>Çarpıntınız geçmiyorsa</li>
          <li>Çarpıntıyla birlikte göğüs ağrısı varsa</li>
          <li>Nefes darlığı varsa</li>
          <li>Baygınlık hissi ya da bayılma varsa</li>
        </ul>
        <p class="soft">Bu durumlarda 112’yi arayın; kendiniz araç kullanmayın. Bu belirtiler olup geçtiyse de aynı gün bir hekime başvurun. Çarpıntılar tekrarlıyor, sıklaşıyor ya da birkaç dakikadan uzun sürüyorsa hekiminize görünün.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(NB_FAQ)}
      <p class="soft" style="margin-top:18px">Haftada ne kadar hareket etmeniz gerektiğini <a href="hareket.html">Ne kadar hareket yeterli?</a> sayfasında hesaplayabilirsiniz.</p>
      {CTA_CARD("Egzersiz programınız ve güvenli yoğunluk", "nabız ve egzersiz yoğunluğu")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "British Heart Foundation. " + ext("https://www.bhf.org.uk/informationsupport/tests/checking-your-pulse", "Checking your pulse") + ". Published 18 October 2024.",
        "American Heart Association. " + ext("https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates", "Target heart rates chart") + ". Last reviewed 12 August 2024.",
        "NHS. " + ext("https://www.nhs.uk/symptoms/heart-palpitations/", "Heart palpitations") + ". Page last reviewed: 17 March 2026.",
        "NICE. " + ext("https://www.nice.org.uk/guidance/ng196", "Atrial fibrillation: diagnosis and management") + ". NICE guideline NG196, 2021",
        "Tanaka H, Monahan KD, Seals DR. " + ext("https://webs.um.es/jlyuste/documts/tanaka.pdf", "Age-predicted maximal heart rate revisited") + ". J Am Coll Cardiol. 2001;37(1):153–156.",
      ])}
    </div>
  </section>
</main>'''

NB_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.nb-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var EN = document.documentElement.lang === 'en';
  var $ = function(id){ return document.getElementById(id); };
  var KEY = 'drihsaneren.nabiz.v1', WA = 'https://wa.me/905538815568?text=';
  var ctxv = 'rest', dur = 30, rh = 'reg', phase = 'idle', t0 = 0, iv = null, lock = null, ctx = null, snd = $('nb-sound');
''' + WAKE_JS + '''
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function age(){ var a = parseInt($('nb-age').value, 10); return (isNaN(a) || a < 15 || a > 100) ? null : a; }
  function store(){ try { return JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { return []; } }
  function save(l){ try { localStorage.setItem(KEY, JSON.stringify(l.slice(-10))); } catch (e) {} }
  function zone(p){ return p < 50 ? 0 : p < 70 ? 1 : p <= 85 ? 2 : 3; }
  function paintZones(v){
    var a = age(); $('nb-zw').hidden = a == null; if (a == null) return;
    var m = 220 - a, r = function(x){ return Math.round(m * x); };
    $('nb-z0').textContent = '< ' + r(0.5);
    $('nb-z1').textContent = fill(S.zone, {a: r(0.5), b: r(0.7)});
    $('nb-z2').textContent = fill(S.zone, {a: r(0.7), b: r(0.85)});
    $('nb-max').textContent = fill(S.max, {m: m});
    var z = (v != null && ctxv === 'ex') ? zone(v / m * 100) : -1;
    $('nb-z').querySelectorAll('div').forEach(function(d){ d.classList.toggle('on', +d.getAttribute('data-z') === z); });
  }
  function paintHist(){
    var h = store(), ul = $('nb-hist'); $('nb-histw').hidden = !h.length; ul.innerHTML = '';
    h.slice().reverse().forEach(function(r){
      var li = document.createElement('li'), sp = document.createElement('span'), bb = document.createElement('b');
      sp.textContent = new Date(r.t).toLocaleDateString(EN ? 'en-GB' : 'tr-TR', {day: 'numeric', month: 'short', year: 'numeric'}) + ' · ' + (r.c === 'ex' ? S.hex : S.hrest) + (r.r === 'irr' ? ' · ' + S.hirr : '');
      bb.textContent = r.v + ' ' + S.bpm; li.appendChild(sp); li.appendChild(bb); ul.appendChild(li);
    });
  }
  var last = null;
  function result(store1){
    var n = parseInt($('nb-beats').value, 10);
    if (isNaN(n) || n < 5 || n > 150){ $('nb-res').hidden = true; last = null; paintZones(null); return; }
    var v = Math.round(n * 60 / dur), a = age(), txt = '', badge = $('nb-badge'), ok = true, lab = '';
    last = v; $('nb-res').hidden = false;
    $('nb-lab').textContent = fill(S.lab, {v: v});
    if (ctxv === 'rest'){
      if (v < 40){ txt = S.rlow40; ok = false; } else if (v < 60){ txt = S.rlow; ok = false; } else if (v <= 100){ txt = S.rok; } else { txt = S.rhigh; ok = false; }
      lab = ok ? S.bok : S.bno;
    } else if (a == null){ txt = S.noage; lab = ''; }
    else {
      var p = Math.round(v / (220 - a) * 100), z = zone(p);
      txt = fill(S['e' + z], {p: p}); lab = [S.bl, S.bm, S.bv, S.bx][z]; ok = z === 1 || z === 2;
    }
    if (rh === 'irr'){ txt += ' ' + S.irr + (dur === 30 ? ' ' + S.irr30 : ''); ok = false; lab = S.birr; }
    else if (rh === 'uns' && dur === 30) txt += ' ' + S.irr30;
    $('nb-txt').textContent = txt;
    badge.hidden = !lab; badge.textContent = lab; badge.classList.toggle('no', !ok);
    $('nb-wa').href = WA + encodeURIComponent(fill(S.wa, {v: v, c: (ctxv === 'ex' ? S.hex : S.hrest) + (rh === 'irr' ? ', ' + S.hirr : '')}));
    paintZones(v);
    if (store1){ var h = store(); h.push({t: new Date().toISOString(), v: v, c: ctxv, r: rh}); save(h); paintHist(); }
  }
  function idle(p, c){
    phase = 'idle'; clearInterval(iv); iv = null; wake(false);
    $('nb-go').textContent = S.start; $('nb-go').classList.remove('stop');
    $('nb-phase').textContent = p || S.ready; $('nb-cue').textContent = c || S.readyc;
  }
  function tick(){
    var left = Math.max(0, dur - (performance.now() - t0) / 1000);
    $('nb-sec').textContent = Math.ceil(left);
    if (left <= 0){
      beep(880, 0.6, 0.25); try { navigator.vibrate && navigator.vibrate(300); } catch (e) {}
      idle(S.done, S.donec); $('nb-sec').textContent = 0;
      setTimeout(function(){ $('nb-beats').focus(); }, 50);
    }
  }
  function start(){
    phase = 'run'; t0 = performance.now(); wake(true); beep(660, 0.25, 0.2);
    $('nb-go').textContent = S.stop; $('nb-go').classList.add('stop');
    $('nb-phase').textContent = S.run; $('nb-cue').textContent = S.runc;
    clearInterval(iv); iv = setInterval(tick, 100); tick();
  }
  $('nb-go').addEventListener('click', function(){ if (phase === 'idle') start(); else { idle(); $('nb-sec').textContent = dur; } });
  $('nb-calc').addEventListener('click', function(){ result(true); });
  $('nb-beats').addEventListener('keydown', function(e){ if (e.key === 'Enter'){ e.preventDefault(); result(true); } });
  document.addEventListener('visibilitychange', function(){ if (document.hidden && phase === 'run'){ idle(); $('nb-sec').textContent = dur; } });
  function seg(id, fn){ $(id).addEventListener('click', function(e){ var b = e.target.closest('button'); if (!b) return; this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); fn(b.getAttribute('data-v')); }); }
  seg('nb-ctx', function(v){ ctxv = v; if (last != null) result(false); else paintZones(null); });
  seg('nb-dur', function(v){ dur = +v; if (phase === 'idle') $('nb-sec').textContent = dur; if (last != null) result(false); });
  seg('nb-rh', function(v){ rh = v; if (last != null) result(false); });
  $('nb-age').addEventListener('input', function(){ if (last != null) result(false); else paintZones(null); });
  $('nb-sec').textContent = dur; paintHist(); idle();
})();
</script>
'''

page("nabiz-olcer.html", "Nabız Ölçer ve Hedef Nabız",
     "Nabzınızı elle nasıl sayarsınız? Süreölçerle dinlenme nabzınızı ölçün, ritmin düzenini kontrol edin ve yaşınıza göre egzersizde hedef nabız aralığınızı öğrenin.",
     "nabiz-olcer.html", SELF7_CSS, NB_BODY, NB_JS,
     seo_title="Nabız Ölçer: Dinlenme Nabzı ve Yaşa Göre Hedef Nabız Aralığı | İhsan Eren",
     about={"@type": "MedicalTest", "name": "Nabız ölçümü"},
     faq_items=NB_FAQ)

# ------------------------------------------------------------------ 2 · BEL–BOY ORANI
BB_FAQ = [
 ("Kimler için uygun?", "NICE bu oranı beden kitle indeksi (BKİ) 35’in altında olan yetişkinler için öneriyor. Aynı sınırlar kadın ve erkekte, her etnik kökende kullanılabilir. 5 yaş ve üzeri çocuklarda ve gençlerde de aynı sınırlar geçerlidir."),
 ("BKİ’m normal, yine de ölçmeli miyim?", "Evet. BKİ fazla kiloyu gösterir ama yağın nerede toplandığını göstermez. Bel–boy oranı, göbek çevresindeki yağlanmanın pratik bir tahminidir. Çalışmaları birleştiren 2012 tarihli bir meta-analizde bel–boy oranı, yetişkinlerde kalp-damar ve metabolik risk etkenlerini taramada bel çevresinden ve BKİ’den daha başarılıydı. Bazı etnik kökenlerden insanlar karın çevresinde yağlanmaya daha yatkındır ve kiloyla ilişkili hastalıkların riski onlarda daha düşük BKİ’de artar. İngiltere’de yapılan bir analizde, BKİ ve bel çevresine dayalı değerlendirmenin sorunsuz saydığı yetişkinlerin %35’i bel–boy oranına göre daha yüksek risk grubundaydı."),
 ("Oranım 0,5’in üzerinde çıktı, ne yapmalıyım?", "Bu bir tanı değildir, ama sağlık riskinizin arttığını gösterir. Hedef, belinizi boyunuzun yarısının altında tutmaktır. Düzenli hareket ve beslenme alışkanlıklarınız üzerine bir hekim ya da diyetisyenle konuşabilir, tansiyon, kan şekeri ve kolesterol gibi değerlerinizi kontrol ettirebilirsiniz."),
]

BB_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Bel–boy oranı</h1>
    <p class="lede">Bel çevreniz boyunuzun yarısından az mı? Bu basit oran, yağın göbek çevrenizde toplanıp toplanmadığını gösterir. İngiltere’nin ulusal sağlık kılavuzu NICE, beden kitle indeksi 35’in altında olan yetişkinlere belini boyunun yarısının altında tutmayı öneriyor. Bir mezura yeter: ölçün ve aşağıda hesaplayın.</p>
    <p class="meta">Son güncelleme: 16 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>0,4–0,49</b><span>Sağlıklı aralık: artmış sağlık riski yok</span></div>
        <div class="stat"><b>0,5–0,59</b><span>Artmış merkezi yağlanma: sağlık riski artmış</span></div>
        <div class="stat"><b>0,6 ve üzeri</b><span>Yüksek merkezi yağlanma: sağlık riski daha da artmış</span></div>
        <div class="stat"><b>5 yaş</b><span>Aynı sınırlar 5 yaş ve üzeri çocuklarda da kullanılabilir</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Kendinizi ölçün</p>
      <h2>Oranınızı hesaplayın</h2>
      <p class="soft">Boyunuzu ve bel çevrenizi santimetre olarak girin. Belinizi nasıl ölçeceğinizi aşağıda bulabilirsiniz.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <div class="bb-in">
              <div><label class="lbl" for="bb-h">Boyunuz (cm)</label><input class="cs-age" id="bb-h" type="number" inputmode="decimal" min="100" max="230" step="0.5" placeholder="ör. 170"></div>
              <div><label class="lbl" for="bb-w">Bel çevreniz (cm)</label><input class="cs-age" id="bb-w" type="number" inputmode="decimal" min="40" max="200" step="0.5" placeholder="ör. 82"></div>
            </div>
          </div>
          <div class="bt-run">
            <p class="bb-big" id="bb-r">–</p>
            <p class="bb-cap" id="bb-cap">Bel–boy oranı</p>
            <div class="bb-g" aria-hidden="true"><span class="bb-m" id="bb-m" hidden></span></div>
            <div class="bb-t" aria-hidden="true"><span style="left:12.5%">0,4</span><span style="left:37.5%">0,5</span><span style="left:62.5%">0,6</span></div>
            <div class="bb-k"><span><i style="background:var(--sage)"></i>Sağlıklı</span><span><i style="background:var(--foil)"></i>Artmış</span><span><i style="background:#c9694f"></i>Yüksek</span></div>
          </div>
          <div class="bt-out">
            <div class="res" id="bb-res" hidden>
              <p class="lab" id="bb-lab"></p>
              <p id="bb-txt"></p>
              <span class="bt-badge" id="bb-badge"></span>
              <div class="cs-acts">
                <button type="button" class="cta" id="bb-save">Sonucu kaydet</button>
                <a class="cta ghost" id="bb-wa" href="#" target="_blank" rel="noopener">WhatsApp’tan gönder</a>
              </div>
              <p class="ag-saved" id="bb-saved" aria-live="polite"></p>
            </div>
            <div id="bb-histw" style="margin-top:20px" hidden>
              <p class="lbl">Önceki sonuçlarınız (bu cihazda)</p>
              <ul class="cs-hist" id="bb-hist"></ul>
            </div>
          </div>
        </div>
        <div class="bb-strings" hidden>
          <span data-k="cap">Bel–boy oranı</span>
          <span data-k="bad">Boyunuzu (100–230 cm) ve bel çevrenizi (40–200 cm) girin.</span>
          <span data-k="lab0">Bu aralık için bir sınıflama yok</span>
          <span data-k="lab1">Sağlıklı aralık</span>
          <span data-k="lab2">Artmış merkezi yağlanma</span>
          <span data-k="lab3">Yüksek merkezi yağlanma</span>
          <span data-k="t0">NICE sınıflaması 0,4’ten başlıyor. Ölçümünüzü bir kez daha kontrol edin: mezura kaburgalarınızın altı ile kalça kemiğinizin üstünün tam ortasından geçmeli.</span>
          <span data-k="t1">Göbek çevresindeki yağlanma sağlıklı aralıkta; artmış sağlık riski göstermiyor.</span>
          <span data-k="t2">Göbek çevresindeki yağlanma artmış; bu, artmış sağlık riskine işaret ediyor.</span>
          <span data-k="t3">Göbek çevresindeki yağlanma yüksek; bu, daha da artmış sağlık riskine işaret ediyor. Bir hekimle konuşmanız iyi olur.</span>
          <span data-k="goal">Boyunuza göre hedef: bel çevreniz {{g}} cm’nin altında olsun.</span>
          <span data-k="bok">Hedefin altında</span>
          <span data-k="bno">Hedefin üzerinde</span>
          <span data-k="saved">Kaydedildi.</span>
          <span data-k="cm">cm</span>
          <span data-k="wa">Merhaba, drihsaneren.com’da bel–boy oranımı hesapladım: {{r}} (boy {{h}} cm, bel {{w}} cm). Bilgi almak istiyorum.</span>
        </div>
      </div>
      <p class="count">Sonuçlarınız yalnızca bu cihazda saklanır; hiçbir yere gönderilmez.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belinizi nasıl ölçersiniz?</h2>
        <ol class="steps">
          <li><span><strong>Kaburgalarınızın en alt noktasını</strong> ve <strong>kalça kemiğinizin en üst noktasını</strong> bulun.</span></li>
          <li><span>Mezurayı bu iki noktanın <strong>tam ortasından</strong> belinize sarın; bu nokta çoğu kişide göbeğin hemen üstüdür.</span></li>
          <li><span><strong>Doğal bir şekilde nefes verin</strong> ve ölçümü o anda okuyun.</span></li>
        </ol>
      </div>
      <div>
        <h2>Neden önemli?</h2>
        <ul class="dots">
          <li>Beden kitle indeksi fazla kiloyu gösterir, ama yağın nerede toplandığını göstermez.</li>
          <li>Bel–boy oranı, göbek çevresindeki yağlanmanın pratik bir tahminidir.</li>
          <li>Bazı etnik kökenlerden insanlar karın çevresinde yağlanmaya daha yatkındır; kiloyla ilişkili hastalıkların riski onlarda daha düşük BKİ’de artar.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(BB_FAQ)}
      <p class="soft" style="margin-top:18px">Hareketinizi artırmak için <a href="hareket.html">Ne kadar hareket yeterli?</a> ve <a href="hareket-atistirmaliklari.html">hareket atıştırmalıkları</a> sayfalarına bakabilirsiniz.</p>
      {CTA_CARD("Hareket ve egzersiz planınız", "bel–boy oranı ve hareket planı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "NICE. " + ext("https://www.nice.org.uk/guidance/ng246/chapter/Identifying-and-assessing-overweight-obesity-and-central-adiposity", "Overweight and obesity management: identifying and assessing overweight, obesity and central adiposity") + ". NICE guideline NG246.",
        "NICE. " + ext("https://www.nice.org.uk/guidance/cg189/chapter/3-Other-information", "Obesity: identification, assessment and management (CG189): other information") + ".",
        "Ashwell M, Gunn P, Gibson S. " + ext("https://doi.org/10.1111/j.1467-789X.2011.00952.x", "Waist-to-height ratio is a better screening tool than waist circumference and BMI for adult cardiometabolic risk factors: systematic review and meta-analysis") + ". Obes Rev. 2012;13(3):275–286.",
        "Browning LM, Hsieh SD, Ashwell M. " + ext("https://doi.org/10.1017/S0954422410000144", "A systematic review of waist-to-height ratio as a screening tool for the prediction of cardiovascular disease and diabetes: 0·5 could be a suitable global boundary value") + ". Nutr Res Rev. 2010;23(2):247–269",
        "Ashwell M, Gibson S. " + ext("https://pmc.ncbi.nlm.nih.gov/articles/PMC4800150/", "Waist-to-height ratio as an indicator of ‘early health risk’: simpler and more predictive than using a ‘matrix’ based on BMI and waist circumference") + ". BMJ Open. 2016;6(3):e010159.",
      ])}
    </div>
  </section>
</main>'''

BB_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.bb-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var EN = document.documentElement.lang === 'en';
  var $ = function(id){ return document.getElementById(id); };
  var KEY = 'drihsaneren.belboy.v1', WA = 'https://wa.me/905538815568?text=';
  function fmt(x, d){ var s = x.toFixed(d); return EN ? s : s.replace('.', ','); }
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function num(id){ var v = parseFloat(String($(id).value).replace(',', '.')); return isNaN(v) ? null : v; }
  function store(){ try { return JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { return []; } }
  function save(l){ try { localStorage.setItem(KEY, JSON.stringify(l.slice(-10))); } catch (e) {} }
  var cur = null;
  function paint(){
    var h = num('bb-h'), w = num('bb-w'), ok = h != null && w != null && h >= 100 && h <= 230 && w >= 40 && w <= 200;
    $('bb-saved').textContent = '';
    if (!ok){
      cur = null; $('bb-r').textContent = '–'; $('bb-m').hidden = true; $('bb-res').hidden = (h == null && w == null);
      $('bb-lab').textContent = ''; $('bb-txt').textContent = S.bad; $('bb-badge').hidden = true; $('bb-save').hidden = true; $('bb-wa').hidden = true;
      return;
    }
    var r = Math.round(w / h * 100) / 100, c = r < 0.4 ? 0 : r < 0.5 ? 1 : r < 0.6 ? 2 : 3;
    cur = {h: h, w: w, r: r};
    $('bb-r').textContent = fmt(r, 2);
    var m = $('bb-m'); m.hidden = false; m.style.left = (Math.max(0, Math.min(1, (r - 0.35) / 0.4)) * 100) + '%';
    $('bb-res').hidden = false; $('bb-save').hidden = false; $('bb-wa').hidden = false;
    $('bb-lab').textContent = S['lab' + c];
    $('bb-txt').textContent = S['t' + c] + ' ' + fill(S.goal, {g: fmt(h / 2, (h / 2) % 1 ? 1 : 0)});
    var b = $('bb-badge'); b.hidden = false; b.textContent = r < 0.5 ? S.bok : S.bno; b.classList.toggle('no', r >= 0.5);
    $('bb-wa').href = WA + encodeURIComponent(fill(S.wa, {r: fmt(r, 2), h: fmt(h, h % 1 ? 1 : 0), w: fmt(w, w % 1 ? 1 : 0)}));
  }
  function paintHist(){
    var hs = store(), ul = $('bb-hist'); $('bb-histw').hidden = !hs.length; ul.innerHTML = '';
    hs.slice().reverse().forEach(function(x){
      var li = document.createElement('li'), sp = document.createElement('span'), bb = document.createElement('b');
      sp.textContent = new Date(x.t).toLocaleDateString(EN ? 'en-GB' : 'tr-TR', {day: 'numeric', month: 'short', year: 'numeric'}) + ' · ' + fmt(x.w, x.w % 1 ? 1 : 0) + ' ' + S.cm;
      bb.textContent = fmt(x.r, 2); li.appendChild(sp); li.appendChild(bb); ul.appendChild(li);
    });
  }
  $('bb-save').addEventListener('click', function(){
    if (!cur) return; var hs = store(); hs.push({t: new Date().toISOString(), h: cur.h, w: cur.w, r: cur.r}); save(hs); paintHist();
    $('bb-saved').textContent = S.saved;
    try { localStorage.setItem(KEY + '.h', String(cur.h)); } catch (e) {}
  });
  $('bb-h').addEventListener('input', paint); $('bb-w').addEventListener('input', paint);
  try { var hh = localStorage.getItem(KEY + '.h'); if (hh) $('bb-h').value = hh; } catch (e) {}
  paintHist(); if (num('bb-h') != null) paint();
})();
</script>
'''

page("bel-boy-orani.html", "Bel–Boy Oranı",
     "Bel çevreniz boyunuzun yarısından az mı? Bel–boy oranınızı hesaplayın, NICE sınırlarıyla karşılaştırın ve belinizi doğru ölçmeyi öğrenin.",
     "bel-boy-orani.html", SELF7_CSS, BB_BODY, BB_JS,
     seo_title="Bel–Boy Oranı Hesaplama: Belinizi Boyunuzun Yarısının Altında Tutun | İhsan Eren",
     about={"@type": "MedicalTest", "name": "Bel–boy oranı"},
     faq_items=BB_FAQ)

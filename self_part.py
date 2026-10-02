# -*- coding: utf-8 -*-
# Kendine iyi bak: sabah rutini, hareket, uyku. ankle_part.py'den sonra exec edilir.

SELF_CSS = NECK_CSS + """
  [hidden]{display:none!important}
  .controls{display:flex;flex-wrap:wrap;gap:10px;margin-top:6px}
  button.cta{font:inherit;font-weight:600;font-size:15px;cursor:pointer}
  .count{font-size:14px;color:var(--muted);margin-top:10px}
  .hint{font-size:14px;color:var(--muted);margin:2px 0 0}
  .days{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0 4px}
  .days button{all:unset;cursor:pointer;min-width:40px;height:40px;padding:0 10px;box-sizing:border-box;text-align:center;border-radius:999px;border:1px solid var(--line-strong);font-size:14px;color:var(--ink-soft);display:inline-grid;place-items:center;font-variant-numeric:tabular-nums}
  .days button:hover{border-color:var(--foil);color:var(--ink)}
  .days button[aria-pressed="true"]{background:var(--foil);border-color:var(--foil);color:var(--ground);font-weight:600}
  .days button:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .tool{border:1px solid var(--line-strong);border-radius:16px;padding:clamp(16px,3vw,26px);
    background:radial-gradient(120% 120% at 0% 0%, rgba(226,171,71,.10), transparent 60%),var(--ground-2)}
  .q{font-weight:600;color:var(--ink);margin:18px 0 0;font-size:16px}
  .q:first-child{margin-top:0}
  .q output{color:var(--foil);font-variant-numeric:tabular-nums}
  input[type=range]{width:100%;accent-color:var(--foil);margin:10px 0 0;height:28px}
  .chk{display:inline-flex;align-items:center;gap:10px;margin-top:18px;cursor:pointer;color:var(--ink)}
  .chk input{width:20px;height:20px;accent-color:var(--foil);margin:0}

  /* sabah rutini oynatıcı */
  .mr{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);gap:clamp(18px,3vw,34px);align-items:center}
  @media (max-width:760px){.mr{grid-template-columns:1fr}}
  .mr-stage{border-radius:14px;overflow:hidden;background:var(--paper);display:grid;place-items:center;min-height:240px}
  .mr-fig{display:none;width:100%}
  .mr-fig.on{display:block}
  .mr-fig .an{padding:18px 10px 12px}
  .mr-fig .an svg{max-width:300px}
  @media (max-width:760px){.mr-fig .an svg{max-width:220px}}
  .mr-top{display:flex;align-items:center;justify-content:space-between;gap:12px}
  .mr-top .eyebrow{color:var(--foil)}
  .mr-phase{font-size:14px;color:var(--ink-soft);font-weight:600}
  .mr-cue{display:none}
  .mr-cue.on{display:block}
  .mr-cue h3{font-size:clamp(24px,3.4vw,30px);margin:8px 0 6px}
  .mr-cue p{color:var(--ink-soft);margin:0}
  .mr-mid{display:flex;align-items:center;gap:18px;margin:16px 0 12px}
  .mr-ring{position:relative;width:92px;height:92px;flex:none}
  .mr-ring svg{width:92px;height:92px;transform:rotate(-90deg)}
  .mr-ring circle{fill:none;stroke-width:7}
  .mr-ring .bg{stroke:rgba(236,229,207,.12)}
  .mr-ring .fg{stroke:var(--foil);stroke-linecap:round;transition:stroke-dashoffset .12s linear}
  .mr-ring b{position:absolute;inset:0;display:grid;place-items:center;font-family:var(--display);font-weight:400;font-size:30px;color:var(--ink);font-variant-numeric:tabular-nums}
  .mr-bar{display:grid;grid-auto-flow:column;grid-auto-columns:1fr;gap:4px;flex:1}
  .mr-bar i{height:6px;border-radius:3px;background:rgba(236,229,207,.12)}
  .mr-bar i.done{background:var(--sage)}
  .mr-bar i.cur{background:var(--foil)}
  .snd{display:inline-flex;align-items:center;gap:8px;font-size:14px;color:var(--ink-soft);margin-top:12px;cursor:pointer}
  .snd input{width:18px;height:18px;accent-color:var(--foil);margin:0}

  /* hareket ölçer */
  .meter{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:clamp(18px,4vw,40px);align-items:center}
  @media (max-width:820px){.meter{grid-template-columns:1fr}}
  .gauge{position:relative;width:min(240px,70vw);margin:0 auto}
  .gauge svg{width:100%;height:auto;display:block;transform:rotate(-90deg)}
  .gauge circle{fill:none;stroke-width:12}
  .gauge .bg{stroke:rgba(236,229,207,.10)}
  .gauge .fg{stroke:var(--foil);stroke-linecap:round;transition:stroke-dashoffset .35s ease}
  .gauge .t150{stroke:var(--sage);stroke-width:3}
  .gauge .c{position:absolute;inset:0;display:grid;place-content:center;text-align:center}
  .gauge .c b{font-family:var(--display);font-weight:400;font-size:clamp(34px,5vw,44px);color:var(--ink);line-height:1;font-variant-numeric:tabular-nums}
  .gauge .c span{font-size:13px;color:var(--muted);max-width:140px;margin:6px auto 0}
  .res-list{list-style:none;margin:18px 0 0;padding:0;display:grid;gap:10px}
  .res-list li{display:grid;grid-template-columns:14px minmax(0,1fr);gap:12px;align-items:start;font-size:15px;color:var(--ink-soft)}
  .res-list i{width:12px;height:12px;border-radius:50%;margin-top:5px;background:rgba(236,229,207,.25)}
  .res-list li.ok i{background:var(--sage)}
  .res-list li.low i{background:var(--gold)}

  /* uyku planlayıcı */
  .planner{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:clamp(18px,4vw,40px);align-items:start}
  @media (max-width:820px){.planner{grid-template-columns:1fr}}
  .planner input[type=time]{font:inherit;font-size:22px;color:var(--ink);background:var(--ground);border:1px solid var(--line-strong);border-radius:10px;padding:8px 12px;margin-top:10px;color-scheme:dark;font-variant-numeric:tabular-nums}
  .p-out{list-style:none;margin:0;padding:0;display:grid;gap:10px}
  .p-out li{display:grid;grid-template-columns:auto minmax(0,1fr);gap:16px;align-items:center;padding:14px 16px;border:1px solid var(--line);border-radius:12px;background:var(--ground)}
  .p-out b{font-family:var(--display);font-weight:400;font-size:30px;color:var(--foil);font-variant-numeric:tabular-nums;min-width:86px}
  .p-out span{font-size:15px;color:var(--ink-soft)}
  .p-out li.main{border-color:var(--line-strong)}
  .p-out li.main b{font-size:38px;color:var(--ink)}
"""

# ------------------------------------------------------------------ SABAH RUTİNİ
# (anahtar, süre sn, iki taraflı mı, başlık, kısa yönerge, ayrıntılı yönerge)
MR_STEPS = [
 ("k2c", 30, True, "Dizi göğse çekme", "Yatakta sırtüstü. Bir dizinizi iki elinizle göğsünüze doğru çekin; yarı sürede diğer bacağa geçin.",
  "Yatakta sırtüstü uzanın. Bir dizinizi iki elinizle tutup göğsünüze doğru yavaşça çekin, belinizde hafif bir gerilme hissedin. Nefesinizi tutmayın. Yarı sürede diğer bacağa geçin."),
 ("bridge", 30, False, "Köprü", "Dizler bükülü, ayaklar yatakta. Kalçanızı yavaşça kaldırıp indirin.",
  "Sırtüstü, dizleriniz bükülü ve ayaklarınız yatakta olsun. Kalçanızı sıkarak yavaşça kaldırın, 2–3 saniye bekleyip indirin. Belinizi aşırı çukurlaştırmadan, rahat bir yükseklikte kalın."),
 ("cat", 30, False, "Kedi-deve", "Eller ve dizler üzerinde. Sırtınızı yavaşça yuvarlayıp çukurlaştırın.",
  "Ellerinizin ve dizlerinizin üzerine gelin. Nefes verirken sırtınızı kedi gibi yukarı yuvarlayın, nefes alırken belinizi hafifçe çukurlaştırıp başınızı kaldırın. Acele etmeden, rahat aralıkta hareket edin."),
 ("sts", 30, False, "Sandalyeden kalkıp oturma", "Hafifçe öne eğilip kalkın, kontrollü şekilde oturun.",
  "Sağlam bir sandalyenin önüne oturun, ayaklarınız yere tam bassın. Hafifçe öne eğilerek ayağa kalkın, tamamen doğrulun, sonra kontrollü şekilde oturun. Gerekirse ellerinizden destek alın."),
 ("bext", 30, False, "Ayakta arkaya esneme", "Eller belde. Kalçayı hafifçe öne itip rahat ettiğiniz kadar geriye esneyin.",
  "Ayaklarınız omuz genişliğinde açık dururken ellerinizi belinizin arkasına koyun. Kalçanızı hafifçe öne iterek gövdenizi rahat ettiğiniz kadar geriye esnetin, sonra doğrulun. Başınızın dönmemesi için yavaş yapın."),
 ("scap", 30, False, "Kürek kemiği sıkıştırma", "Omuzları kaldırmadan kürek kemiklerini geriye ve aşağıya yaklaştırın.",
  "Dik durun. Omuzlarınızı kulaklarınıza kaldırmadan kürek kemiklerinizi geriye ve biraz aşağıya doğru birbirine yaklaştırın, 3 saniye tutup bırakın."),
 ("rot", 30, False, "Boyun döndürme", "Başınızı yavaşça bir sağa bir sola çevirin.",
  "Omuzlarınızı sabit tutun. Başınızı yavaşça sağa çevirin, rahat olan son noktada kısa bir süre bekleyin, sonra sola çevirin. Baş dönmesi olursa yavaşlayın ya da bırakın."),
 ("heel2", 30, False, "Tezgâha tutunarak topuk yükseltme", "Bir yere hafifçe tutunun. Parmak uçlarına yükselip yavaşça inin.",
  "Mutfak tezgâhına ya da sağlam bir sandalyenin arkasına hafifçe tutunun. Parmak uçlarınıza yükselin, bir an bekleyip yavaşça inin. Baldır kaslarını ısıtır, dengeye yardım eder."),
 ("sls", 30, True, "Tek ayak üzerinde durma", "Tutunarak bir ayağınızı kaldırın; yarı sürede ayak değiştirin.",
  "Tezgâhın önünde dik durun, bir ya da iki elinizle hafifçe tutunun. Bir ayağınızı yerden kaldırıp dengede kalın; yarı sürede diğer ayağa geçin. Kolaylaştıkça tek elle, sonra parmak ucuyla tutunun."),
]
for _k, _t, _s, _h, _c, _d in MR_STEPS:
    EXT["mr_" + _k] = (_h, _d, "Her iki tarafa 15'er saniye" if _s else f"{_t} saniye")
    SV["mr_" + _k] = SV[_k]

MR_FIGS = "\n".join(f'<div class="mr-fig{" on" if i == 0 else ""}" data-i="{i}">{SV[k]}</div>' for i, (k, *_r) in enumerate(MR_STEPS))
SIDE_ATTR = ' data-side="1"'
MR_CUES = "\n".join(
    f'<div class="mr-cue{" on" if i == 0 else ""}" data-t="{t}"{SIDE_ATTR if s else ""}><h3>{h}</h3><p>{c}</p></div>'
    for i, (k, t, s, h, c, d) in enumerate(MR_STEPS))
MR_BAR = "".join("<i></i>" for _ in MR_STEPS)

MORNING_FAQ = [
 ("Sabah mı egzersiz yapmalıyım, akşam mı?", "Herkes için tek bir en iyi saat yok. En iyi zaman, düzenli olarak yapabildiğiniz zamandır. Sabah yapılan kısa bir rutin güne hareketle başlamayı kolaylaştırır; akşam yapmayı tercih ediyorsanız bu da işe yarar."),
 ("Her gün yapabilir miyim?", "Evet. Bu rutindeki hareketler hafif ve kontrollüdür; her gün yapılabilir. Hareketleri rahat olduğunuz aralıkta yapın. Bir hareket ağrınızı belirgin şekilde artırıyorsa onu atlayın."),
 ("Sabahları çok tutuk kalkıyorum, bu normal mi?", "Uyandıktan sonra kısa süren tutukluk, özellikle kireçlenmede sık görülür ve hareket ettikçe açılır. Tutukluk yarım saatten uzun sürüyorsa, eklemlerde şişlik ve kızarıklık varsa ya da gece ağrısıyla uyanıyorsanız iltihaplı bir romatizmal hastalık açısından hekime başvurun."),
 ("Bu rutin spor yerine geçer mi?", "Hayır, bu rutin bir ısınma ve hareketlenme alışkanlığıdır. Dünya Sağlık Örgütü yetişkinler için haftada 150–300 dakika orta yoğunlukta hareket ve en az 2 gün kas güçlendirme öneriyor. Ayrıntılar için Ne kadar hareket yeterli? sayfasına bakabilirsiniz."),
]

MORNING_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Güne 5 dakikayla başlayın</h1>
    <p class="lede">Yatakta başlayıp ayakta biten dokuz hareket. Her hareket 30 saniye; ekrandaki zamanlayıcı sizi hareketten harekete götürür. Sabah tutukluğunu açmak ve güne hareketle başlamak için kısa, sade bir rutin.</p>
    <p class="meta">Son güncelleme: 29 Eylül 2026</p>
  </div>
</header>

<main>
  <section id="rutin">
    <div class="wrap">
      <div class="tool">
        <div class="mr">
          <div class="mr-stage" aria-hidden="true">
{MR_FIGS}
          </div>
          <div class="mr-panel">
            <div class="mr-top"><p class="eyebrow" id="mr-step">1 / {len(MR_STEPS)}</p><span class="mr-phase" id="mr-phase" aria-live="polite">Hazır</span></div>
            <div class="mr-cues">
{MR_CUES}
            </div>
            <div class="mr-mid">
              <div class="mr-ring"><svg viewBox="0 0 92 92" aria-hidden="true"><circle class="bg" cx="46" cy="46" r="40"/><circle class="fg" id="mr-arc" cx="46" cy="46" r="40" stroke-dasharray="251.3" stroke-dashoffset="0"/></svg><b id="mr-sec">30</b></div>
              <div class="mr-bar" aria-hidden="true">{MR_BAR}</div>
            </div>
            <div class="controls">
              <button type="button" class="cta" id="mr-go">Başlat</button>
              <button type="button" class="cta ghost" id="mr-prev">Önceki</button>
              <button type="button" class="cta ghost" id="mr-next">Sonraki</button>
            </div>
            <label class="snd"><input type="checkbox" id="mr-sound" checked> Sesli uyarı</label>
            <p class="count" id="mr-msg" aria-live="polite">Toplam yaklaşık 5 dakika. Her hareketten önce 5 saniyelik hazırlanma süresi var.</p>
          </div>
        </div>
        <div class="mr-strings" hidden>
          <span data-k="ready">Hazırlanın</span>
          <span data-k="next">Sıradaki hareket</span>
          <span data-k="work">Hareket</span>
          <span data-k="side">Diğer tarafa geçin</span>
          <span data-k="paused">Duraklatıldı</span>
          <span data-k="done">Tamamlandı</span>
          <span data-k="donemsg">Harika, bugünkü rutininizi tamamladınız. Yarın aynı saatte tekrar etmeye ne dersiniz?</span>
          <span data-k="start">Başlat</span>
          <span data-k="pause">Duraklat</span>
          <span data-k="resume">Devam et</span>
          <span data-k="again">Baştan başla</span>
        </div>
      </div>
      <p class="count">Ekran, rutin sürerken kapanmayacak şekilde ayarlanır (tarayıcınız destekliyorsa). Ses uyarısı her hareketin başında ve iki taraflı hareketlerde yarı sürede çalar.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Güvenle yapmak için</h2>
        <p class="soft">Hareketleri acele etmeden, rahat olduğunuz aralıkta yapın. Amaç zorlamak değil, bedeni uyandırmak.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Yataktan kalkarken önce yan dönüp oturun, birkaç saniye bekleyin, sonra ayağa kalkın.</li>
        <li>Ayakta yapılan hareketlerde bir tezgâha ya da sağlam bir sandalyeye yakın durun.</li>
        <li>Bir hareket ağrınızı belirgin şekilde artırıyorsa onu atlayın.</li>
        <li>Baş dönmesi, göğüs ağrısı ya da nefes darlığı olursa durun.</li>
        <li>Kemik erimesi tanınız varsa öne eğilme içeren hareketler (dizi göğse çekme, kedi-deve) için önce fizyoterapistinize danışın.</li>
      </ul>
    </div>
  </section>

  <section id="hareketler">
    <div class="wrap">
      <p class="eyebrow">Rutindeki hareketler</p>
      <h2>Dokuz hareket, adım adım</h2>
      <p class="soft">Zamanlayıcıyı kullanmadan da yapabilirsiniz. Sıra, yatakta başlayıp ayakta bitecek şekilde düzenlendi.</p>
      {ex_grid(["mr_" + s[0] for s in MR_STEPS])}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Sabah için hareket videoları</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("ERFjHlWN28k", "Uyanma ve duruş rutini videosunu oynat", "The Best Stimulating Wake-Up and Posture Daily Routine 2-3 Minutes")}
          <h3>2–3 dakikalık uyanma ve duruş rutini</h3>
          <p>Bir havlu ya da sopa yardımıyla omuzları ve sırtı açan kısa bir sabah rutini.</p>
        </div>
        <div class="vid">
          {vbox("L2OoV9-A50s", "5 dakikalık günlük germe videosunu oynat", "Bob &amp; Brad's 5 Minute Daily Stretch Challenge (30 Day)")}
          <h3>Her gün 5 dakika germe</h3>
          <p>30 günlük bir alışkanlık olarak hazırlanmış, her gün yapılabilecek kısa bir germe programı.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(MORNING_FAQ)}
      {CTA_CARD("Sabah tutukluğunuz ya da ağrınız", "sabah tutukluğu ve ağrı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(["Bull FC, Al-Ansari SS, Biddle S, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/33239350/", "World Health Organization 2020 guidelines on physical activity and sedentary behaviour") + ". Br J Sports Med. 2020;54(24):1451-1462."])}
    </div>
  </section>
</main>'''

MORNING_JS = '''<script>
(function(){
  var root = document.getElementById('rutin'); if (!root) return;
  var S = {}; root.querySelectorAll('.mr-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var figs = root.querySelectorAll('.mr-fig'), cues = root.querySelectorAll('.mr-cue'), bars = root.querySelectorAll('.mr-bar i');
  var $ = function(id){ return document.getElementById(id); };
  var go = $('mr-go'), prevB = $('mr-prev'), nextB = $('mr-next'), secEl = $('mr-sec'), stepEl = $('mr-step'),
      phaseEl = $('mr-phase'), msg = $('mr-msg'), arc = $('mr-arc'), snd = $('mr-sound');
  var C = 251.3, PREP = 5, N = cues.length, i = 0, phase = 'idle', left = 0, running = false, t = null, last = 0, half = false, ctx = null, lock = null;
  var introMsg = msg.textContent;
  function dur(k){ return +cues[k].getAttribute('data-t'); }
  function show(k){
    for (var j = 0; j < N; j++){
      figs[j].classList.toggle('on', j === k); cues[j].classList.toggle('on', j === k);
      bars[j].className = j < k ? 'done' : (j === k ? 'cur' : '');
    }
    stepEl.textContent = (k + 1) + ' / ' + N;
  }
  function beep(f, d){
    if (!snd.checked) return;
    try {
      ctx = ctx || new (window.AudioContext || window.webkitAudioContext)();
      var o = ctx.createOscillator(), g = ctx.createGain(), n = ctx.currentTime;
      o.frequency.value = f; g.gain.setValueAtTime(0.0001, n);
      g.gain.exponentialRampToValueAtTime(0.2, n + 0.02); g.gain.exponentialRampToValueAtTime(0.0001, n + d);
      o.connect(g); g.connect(ctx.destination); o.start(n); o.stop(n + d + 0.05);
    } catch (e) {}
  }
  function render(){
    var tot = phase === 'prep' ? PREP : dur(i);
    secEl.textContent = phase === 'done' ? '✓' : (phase === 'idle' ? dur(i) : Math.max(0, Math.ceil(left)));
    arc.style.strokeDashoffset = (phase === 'prep' || phase === 'work') ? (C * (1 - left / tot)).toFixed(1) : (phase === 'done' ? 0 : C);
  }
  function enter(p, k){
    phase = p; i = k; half = false; show(k);
    if (p === 'prep'){ left = PREP; phaseEl.textContent = k === 0 ? S.ready : S.next; }
    else { left = dur(k); phaseEl.textContent = S.work; beep(880, 0.25); }
    render();
  }
  function wake(on){
    try {
      if (on && navigator.wakeLock && !lock) navigator.wakeLock.request('screen').then(function(l){ lock = l; }).catch(function(){});
      if (!on && lock){ lock.release(); lock = null; }
    } catch (e) {}
  }
  function tick(){
    var now = performance.now(), dt = (now - last) / 1000; last = now;
    var before = Math.ceil(left); left -= dt;
    if (phase === 'work' && cues[i].hasAttribute('data-side') && !half && left <= dur(i) / 2){ half = true; phaseEl.textContent = S.side; beep(660, 0.2); }
    if (left <= 0){
      if (phase === 'prep') enter('work', i);
      else if (i < N - 1) enter('prep', i + 1);
      else finish();
      return;
    }
    if (phase === 'prep' && left <= 3 && Math.ceil(left) !== before) beep(520, 0.08);
    render();
  }
  function run(){ running = true; last = performance.now(); clearInterval(t); t = setInterval(tick, 100); go.textContent = S.pause; wake(true); }
  function pause(){ running = false; clearInterval(t); go.textContent = S.resume; phaseEl.textContent = S.paused; wake(false); }
  function finish(){
    running = false; clearInterval(t); phase = 'done'; show(N - 1);
    for (var j = 0; j < N; j++) bars[j].className = 'done';
    phaseEl.textContent = S.done; msg.textContent = S.donemsg; go.textContent = S.again; render(); wake(false);
    beep(660, 0.15); setTimeout(function(){ beep(880, 0.3); }, 180);
  }
  go.addEventListener('click', function(){
    if (phase === 'idle' || phase === 'done'){ msg.textContent = introMsg; enter('prep', 0); run(); }
    else if (running) pause();
    else { phaseEl.textContent = phase === 'prep' ? (i === 0 ? S.ready : S.next) : S.work; run(); }
  });
  function jump(k){
    if (k < 0 || k >= N) return;
    if (phase === 'idle' || phase === 'done'){ phase = 'idle'; i = k; show(k); render(); return; }
    enter('prep', k); if (!running) phaseEl.textContent = S.paused;
  }
  prevB.addEventListener('click', function(){ jump(i - 1); });
  nextB.addEventListener('click', function(){ jump(i + 1); });
  document.addEventListener('visibilitychange', function(){ if (!document.hidden && running) wake(true); });
  render();
})();
</script>
'''

page("sabah-rutini.html", "Sabah Rutini",
     "Yatakta başlayıp ayakta biten dokuz hareketlik, yaklaşık 5 dakikalık sabah rutini. Ekrandaki zamanlayıcıyla birlikte yapın; sabah tutukluğunu açın, güne hareketle başlayın.",
     "sabah-rutini.html", SELF_CSS, MORNING_BODY, MORNING_JS + YT_JS,
     seo_title="Güne 5 Dakikayla Başlayın: Sabah Hareket Rutini | İhsan Eren",
     about={"@type": "Thing", "name": "Sabah hareket rutini"},
     faq_items=pick(MORNING_FAQ, 0, 1, 2))

# ------------------------------------------------------------------ NE KADAR HAREKET YETERLİ?
def DAYS(name, sel):
    return (f'<div class="days" role="group" data-for="{name}">' +
            "".join(f'<button type="button" data-v="{d}" aria-pressed="{"true" if d == sel else "false"}">{d}</button>' for d in range(8)) +
            '</div>')

MOVE_FAQ = [
 ("Günde 10.000 adım atmak şart mı?", "Hayır. 57 çalışmayı bir araya getiren 2025 tarihli bir derlemede günde 7.000 adım atanlarda ölüm riski, 2.000 adım atanlara göre %47 daha düşüktü ve bu fayda 10.000 adımdakine çok yakındı. Bazı sonuçlarda 7.000 adımdan sonra fayda düzleşiyor. Az adım atıyorsanız her artış değerlidir."),
 ("Ev işleri ve merdiven çıkmak sayılır mı?", "Evet. Dünya Sağlık Örgütü her hareketin sayıldığını vurguluyor. Egzersiz yapmayan 25 binden fazla kişinin izlendiği bir çalışmada, günde 1–2 dakikalık üç kısa ve tempolu hareket (merdiven çıkmak, çok hızlı yürümek gibi) yapanlarda ölüm riski belirgin şekilde daha düşük bulundu."),
 ("Kas güçlendirme için spor salonu gerekir mi?", "Hayır. Sandalyeden kalkıp oturma, duvar şınavı, lastik bantla egzersizler ya da ağır alışveriş torbalarını taşımak da kaslarınızı çalıştırır. Önemli olan, tüm büyük kas gruplarını haftada en az 2 gün yormaktır."),
 ("Hiç hareket etmiyorum, nereden başlamalıyım?", "Az da olsa hareket, hiç hareket etmemekten iyidir. Küçük başlayın ve süreyi, sıklığı ve yoğunluğu zamanla artırın; örneğin günlük kısa bir yürüyüşle başlayıp her hafta birkaç dakika ekleyebilirsiniz. Kalp hastalığınız ya da yeni başlayan bir şikâyetiniz varsa önce hekiminize danışın."),
]

MOVE_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Ne kadar hareket yeterli?</h1>
    <p class="lede">Hareketin faydasını görmek için spor salonuna gitmek şart değil. Dünya Sağlık Örgütü'nün önerileri, günlük adım sayısı ve gün içine serpiştirilen kısa hareketler hakkındaki güncel bulgular. Kendi haftanızı da aşağıdaki ölçerle hesaplayın.</p>
    <p class="meta">Son güncelleme: 29 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>150–300 dk</b><span>Yetişkinler için önerilen haftalık orta yoğunlukta hareket</span></div>
        <div class="stat"><b>2 gün</b><span>Haftada en az kas güçlendirme egzersizi yapılması önerilen gün sayısı</span></div>
        <div class="stat"><b>%47</b><span>Günde 7.000 adım atanlarda, 2.000 adım atanlara göre daha düşük ölüm riski</span></div>
        <div class="stat"><b>3 × 1–2 dk</b><span>Gün içine yayılan kısa ve tempolu hareket: egzersiz yapmayanlarda daha düşük ölüm riskiyle ilişkili</span></div>
      </div>
    </div>
  </section>

  <section id="olcer">
    <div class="wrap">
      <p class="eyebrow">Hemen hesaplayın</p>
      <h2>Haftalık hareket ölçer</h2>
      <p class="soft">Sıradan bir haftanızı düşünün. Dünya Sağlık Örgütü'ne göre 1 dakika yüksek yoğunlukta hareket, 2 dakika orta yoğunlukta harekete denk sayılır.</p>
      <div class="tool">
        <div class="meter">
          <div>
            <p class="q">Orta yoğunlukta hareket: <output id="m-mod-v">60</output> dk / hafta</p>
            <input type="range" id="m-mod" min="0" max="600" step="10" value="60" aria-label="Haftalık orta yoğunlukta hareket (dakika)">
            <p class="hint">Tempolu yürüyüş, bisiklet, dans, bahçe işleri. Konuşabilirsiniz ama şarkı söyleyemezsiniz.</p>
            <p class="q">Yüksek yoğunlukta hareket: <output id="m-vig-v">0</output> dk / hafta</p>
            <input type="range" id="m-vig" min="0" max="300" step="5" value="0" aria-label="Haftalık yüksek yoğunlukta hareket (dakika)">
            <p class="hint">Koşu, yokuş yukarı hızlı yürüyüş, tempolu yüzme. Nefes nefese kalır, ancak birkaç kelime söyleyebilirsiniz.</p>
            <p class="q">Kas güçlendirme: haftada kaç gün?</p>
            {DAYS("str", 0)}
            <label class="chk"><input type="checkbox" id="m-65"> 65 yaş ve üstündeyim</label>
            <div id="m-bal-wrap" hidden>
              <p class="q">Denge ve kuvvet çalışması: haftada kaç gün?</p>
              {DAYS("bal", 0)}
            </div>
          </div>
          <div>
            <div class="gauge">
              <svg viewBox="0 0 240 240" aria-hidden="true"><circle class="bg" cx="120" cy="120" r="100"/><circle class="fg" id="m-arc" cx="120" cy="120" r="100" stroke-dasharray="628.3" stroke-dashoffset="628.3"/><line class="t150" x1="220" y1="120" x2="232" y2="120" transform="rotate(180 120 120)"/></svg>
              <div class="c"><b id="m-eq">60</b><span>dakika / hafta, orta yoğunluk eşdeğeri</span></div>
            </div>
            <ul class="res-list" aria-live="polite">
              <li id="m-r1"><i></i><span></span></li>
              <li id="m-r2"><i></i><span></span></li>
              <li id="m-r3" hidden><i></i><span></span></li>
            </ul>
          </div>
        </div>
        <div class="m-strings" hidden>
          <span data-k="aer_low">Temel hedefe {{n}} dakika kaldı. Her dakika sayılır; haftaya 10–15 dakika ekleyerek başlayabilirsiniz.</span>
          <span data-k="aer_ok">Temel hedefe ulaştınız: haftada en az 150 dakika.</span>
          <span data-k="aer_hi">Ek fayda aralığındasınız: haftada 300 dakika ve üstü.</span>
          <span data-k="str_low">Kas güçlendirme: haftada en az 2 gün önerilir; {{n}} gün daha ekleyin.</span>
          <span data-k="str_ok">Kas güçlendirme hedefi tamam: haftada 2 gün ve üstü.</span>
          <span data-k="bal_low">Denge ve kuvvet: 65 yaş ve üstünde haftada en az 3 gün önerilir; {{n}} gün daha ekleyin.</span>
          <span data-k="bal_ok">Denge ve kuvvet hedefi tamam: haftada 3 gün ve üstü.</span>
        </div>
      </div>
      <p class="count">Halkadaki ince yeşil çizgi 150 dakikayı, halkanın tamamı 300 dakikayı gösterir. Bu ölçer bilgilendirme amaçlıdır; kişisel bir egzersiz reçetesi değildir.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Dünya Sağlık Örgütü ne öneriyor?</h2>
        <p class="soft">2020'de güncellenen öneriler, hareketin her yaşta ve her miktarda fayda sağladığını vurguluyor: az da olsa hareket, hiç hareket etmemekten iyidir.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li><strong>Yetişkinler:</strong> haftada 150–300 dakika orta yoğunlukta ya da 75–150 dakika yüksek yoğunlukta hareket veya ikisinin eşdeğer bir karışımı.</li>
        <li><strong>Kas güçlendirme:</strong> tüm büyük kas gruplarını çalıştıran egzersizler, haftada en az 2 gün.</li>
        <li><strong>65 yaş ve üstü:</strong> bunlara ek olarak, düşmeleri önlemek için denge ve kuvveti birlikte çalıştıran hareketler, haftada en az 3 gün.</li>
        <li><strong>Oturma süresi:</strong> uzun oturmaları sınırlayıp yerine her yoğunlukta hareket koymak.</li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Adım sayısı: 10.000 sihirli bir sayı değil</h2>
      <p class="soft">57 çalışmayı bir araya getiren ve 2025'te <em>The Lancet Public Health</em>'te yayımlanan bir derlemede, günde 7.000 adım atanlar 2.000 adım atanlarla karşılaştırıldı:</p>
      <div class="stats">
        <div class="stat"><b>%47</b><span>Daha düşük ölüm riski</span></div>
        <div class="stat"><b>%47</b><span>Daha düşük kalp-damar hastalığından ölüm riski</span></div>
        <div class="stat"><b>%25</b><span>Daha düşük kalp-damar hastalığı riski</span></div>
        <div class="stat"><b>%38</b><span>Daha düşük demans riski</span></div>
      </div>
      <p class="soft" style="margin-top:14px">Ölüm riskindeki azalma, günde 10.000 adım atanlardakine çok yakındı; bazı sonuçlarda 7.000 adımdan sonra fayda düzleşiyor. Bu bulgular gözlem çalışmalarına dayanır, yani ilişki gösterir; yine de az adım atan biri için her artış anlamlıdır.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Hareket atıştırmalıkları</h2>
        <p class="soft">Egzersiz yapmayan ve ortalama 62 yaşındaki 25.241 kişinin bileklerine takılan cihazlarla ölçülen bir çalışmada, günlük hayatın içindeki kısa ve tempolu hareket patlamaları incelendi. Ortalama 7 yıllık izlemde, günde 1–2 dakikalık 3 kısa hareket yapanlarda hiç yapmayanlara göre genel ve kanser kaynaklı ölüm riski %38–40, kalp-damar kaynaklı ölüm riski %48–49 daha düşüktü.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Merdivenleri tempolu çıkın.</li>
        <li>Otobüse ya da işe giderken birkaç dakika çok hızlı yürüyün.</li>
        <li>Alışveriş torbalarını taşıyın, çocuklarla ya da torunlarla hareketli oyunlar oynayın.</li>
        <li>Bu bir gözlem çalışmasıdır; neden-sonuç ilişkisini kanıtlamaz, ama egzersize vakit bulamayanlar için umut verici bir başlangıç noktasıdır.</li>
      </ul>
    </div>
  </section>

  <section id="video">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Günün 23,5 saati</h2>
      <p class="soft">Kanadalı aile hekimi Mike Evans'ın çizimlerle anlattığı, çok izlenen kısa videosu: günün yalnızca yarım saatini harekete ayırmak sağlığımızı nasıl etkiler? Video İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("aUaInS6HIGo", "23,5 saat videosunu oynat", "23 and 1/2 hours: What is the single best thing we can do for our health?")}
          <h3>23,5 saat: sağlığımız için yapabileceğimiz en iyi şey</h3>
          <p>Hareketin kalp, eklem, ruh sağlığı ve uzun yaşam üzerindeki etkilerini araştırmalarla anlatıyor.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(MOVE_FAQ)}
      <div class="note warn" style="margin-top:22px"><strong>Dikkat:</strong> Hareket sırasında göğüs ağrısı, alışılmadık nefes darlığı, baş dönmesi ya da çarpıntı olursa durun ve bir hekime başvurun. Kalp hastalığınız varsa yeni bir programa başlamadan önce hekiminize danışın.</div>
      {CTA_CARD("Size uygun bir hareket programı", "kişiye özel egzersiz programı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Bull FC, Al-Ansari SS, Biddle S, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/33239350/", "World Health Organization 2020 guidelines on physical activity and sedentary behaviour") + ". Br J Sports Med. 2020;54(24):1451-1462.",
        "Ding D, et al. " + ext("https://www.thelancet.com/journals/lanpub/article/PIIS2468-2667(25)00164-1/fulltext", "Daily steps and health outcomes in adults: a systematic review and dose-response meta-analysis") + ". Lancet Public Health. 2025.",
        "Stamatakis E, Ahmadi MN, Gill JMR, et al. " + ext("https://www.nature.com/articles/s41591-022-02100-x", "Association of wearable device-measured vigorous intermittent lifestyle physical activity with mortality") + ". Nat Med. 2022;28:2521-2529.",
      ])}
    </div>
  </section>
</main>'''

MOVE_JS = '''<script>
(function(){
  var root = document.getElementById('olcer'); if (!root) return;
  var S = {}; root.querySelectorAll('.m-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var $ = function(id){ return document.getElementById(id); };
  var mod = $('m-mod'), vig = $('m-vig'), old = $('m-65'), arc = $('m-arc'), C = 628.3;
  var val = { str: 0, bal: 0 };
  root.querySelectorAll('.days').forEach(function(g){
    g.addEventListener('click', function(e){
      var b = e.target.closest('button'); if (!b) return;
      g.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      val[g.getAttribute('data-for')] = +b.getAttribute('data-v'); upd();
    });
  });
  function row(id, ok, txt){ var li = $(id); li.className = ok ? 'ok' : 'low'; li.querySelector('span').textContent = txt; }
  function upd(){
    var m = +mod.value, v = +vig.value, eq = m + 2 * v;
    $('m-mod-v').textContent = m; $('m-vig-v').textContent = v; $('m-eq').textContent = eq;
    arc.style.strokeDashoffset = (C * (1 - Math.min(eq, 300) / 300)).toFixed(1);
    if (eq < 150) row('m-r1', false, S.aer_low.replace('{n}', 150 - eq));
    else row('m-r1', true, eq >= 300 ? S.aer_hi : S.aer_ok);
    row('m-r2', val.str >= 2, val.str >= 2 ? S.str_ok : S.str_low.replace('{n}', 2 - val.str));
    $('m-bal-wrap').hidden = !old.checked; $('m-r3').hidden = !old.checked;
    if (old.checked) row('m-r3', val.bal >= 3, val.bal >= 3 ? S.bal_ok : S.bal_low.replace('{n}', 3 - val.bal));
  }
  mod.addEventListener('input', upd); vig.addEventListener('input', upd); old.addEventListener('change', upd);
  upd();
})();
</script>
'''

page("hareket.html", "Ne Kadar Hareket Yeterli?",
     "Dünya Sağlık Örgütü önerilerine göre haftada ne kadar hareket etmelisiniz? Haftalık hareket ölçer, günde kaç adım gerektiği ve gün içine yayılan kısa hareketler hakkında güncel bulgular.",
     "hareket.html", SELF_CSS, MOVE_BODY, MOVE_JS + YT_JS,
     seo_title="Ne Kadar Hareket Yeterli? Haftalık Hareket Ölçer ve Adım Sayısı | İhsan Eren",
     about={"@type": "Thing", "name": "Fiziksel aktivite"},
     faq_items=pick(MOVE_FAQ, 0, 1, 2, 3))

# ------------------------------------------------------------------ İYİ UYKU
NEEDS = [(7, "7 saat"), (7.5, "7,5 saat"), (8, "8 saat"), (8.5, "8,5 saat"), (9, "9 saat")]
NEED_BTNS = "".join(f'<button type="button" data-v="{v}" aria-pressed="{"true" if v == 8 else "false"}">{t}</button>' for v, t in NEEDS)

SLEEP_FAQ = [
 ("Yetişkinler kaç saat uyumalı?", "Amerikan Uyku Tıbbı Akademisi ile Uyku Araştırmaları Derneği'nin ortak önerisine göre 18–60 yaş arasındaki yetişkinler düzenli olarak gecede 7 saat ya da daha fazla uyumalı. Gecede 9 saatten uzun uykunun sağlık riskiyle ilişkili olup olmadığı ise belirsiz."),
 ("Öğleden sonra içtiğim kahve uykumu etkiler mi?", "Etkileyebilir. Bir çalışmada yatmadan 6 saat önce alınan 400 mg kafein (yaklaşık 2–3 fincan kahve), ölçülen uyku süresini bir saatten fazla kısalttı. Uyku sorununuz varsa kahve ve çayı öğleden sonranın erken saatlerinde bırakmayı deneyin."),
 ("Kronik uykusuzlukta ilk tercih tedavi nedir?", "Amerikan Hekimler Koleji (ACP), kronik uykusuzlukta ilk tedavi olarak uykusuzluğa yönelik bilişsel davranışçı terapiyi öneriyor. Bu tedavi uyku düzenini, yatakla uyku arasındaki bağı ve uykuyla ilgili kaygıları ele alır. Uyku ilacı kullanıp kullanmamaya hekiminizle birlikte karar verin."),
 ("Horlamak önemli mi?", "Tek başına horlama her zaman bir hastalık işareti değildir. Yüksek sesli horlamaya uykuda nefes durmaları, boğulur gibi uyanma ya da gündüz aşırı uyku hali eşlik ediyorsa uyku apnesi açısından bir hekime başvurun."),
]

SLEEP_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>İyi uyku için</h1>
    <p class="lede">Uyku, iyileşmenin en az konuşulan parçası. Kaç saat uyumalı, kahve uykuyu nasıl etkiler, uyku ile ağrı arasında nasıl bir ilişki var? Aşağıdaki planlayıcıyla kendi yatma saatinizi de hesaplayın.</p>
    <p class="meta">Son güncelleme: 29 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>7+ saat</b><span>Yetişkinler için önerilen gecelik uyku süresi</span></div>
        <div class="stat"><b>1 saatten fazla</b><span>Yatmadan 6 saat önce alınan yüksek doz kafeinin kısalttığı uyku süresi</span></div>
        <div class="stat"><b>İki yönlü</b><span>Uyku ile ağrı arasındaki ilişki: biri bozulunca diğeri de etkilenir</span></div>
        <div class="stat"><b>İlk tercih</b><span>Kronik uykusuzlukta ilaçtan önce önerilen bilişsel davranışçı terapi</span></div>
      </div>
    </div>
  </section>

  <section id="planlayici">
    <div class="wrap">
      <p class="eyebrow">Hemen hesaplayın</p>
      <h2>Yatma saati planlayıcı</h2>
      <p class="soft">Sabah kalkmanız gereken saati ve hedeflediğiniz uyku süresini seçin. Planlayıcı, uykuya dalmak için yaklaşık 15 dakikalık bir pay bırakır.</p>
      <div class="tool">
        <div class="planner">
          <div>
            <label class="q" for="p-wake">Kalkış saatiniz</label><br>
            <input type="time" id="p-wake" value="07:00" step="300">
            <p class="q">Hedeflediğiniz uyku süresi</p>
            <div class="days" role="group" id="p-need">{NEED_BTNS}</div>
            <p class="hint">Yetişkinler için önerilen süre gecede 7 saat ve üstüdür.</p>
          </div>
          <ul class="p-out" aria-live="polite">
            <li class="main"><b id="p-bed">22:45</b><span>Yatağa girme saati</span></li>
            <li><b id="p-wind">21:45</b><span>Işıkları azaltıp ekranları bırakma: yatmadan yaklaşık 1 saat önce</span></li>
            <li><b id="p-caf">16:45</b><span>Son kahve ya da çay: yatmadan en az 6 saat önce</span></li>
          </ul>
        </div>
      </div>
      <p class="count">Hafta sonu dahil her gün aynı saatte kalkmak, uyku düzenini oturtmanın en etkili yollarından biridir.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Uyku ve ağrı</h2>
        <p class="soft">Uyku ile ağrı birbirini besler: ağrı uykuyu böler, kötü uyku da ağrıya duyarlılığı artırır. Sağlıklı gönüllülerde tek bir gece uykusuz kalmanın bile ağrıya duyarlılığı artırdığı gösterildi. Bu yüzden bel, boyun ya da eklem ağrısıyla yaşayan biri için uykuyu iyileştirmek, tedavinin bir parçasıdır.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Yan yatıyorsanız dizlerinizin arasına bir yastık koymak bel ve kalçayı rahatlatabilir.</li>
        <li>Sırtüstü yatıyorsanız dizlerinizin altına bir yastık koymak belinizi rahatlatabilir.</li>
        <li>Başınızı omuz hizasında tutan bir yastık yüksekliği seçin; ayrıntılar <a href="boyun-agrisi.html">boyun ağrısı</a> rehberinde.</li>
        <li>Ağrı sizi her gece uyandırıyorsa ya da dinlenmekle geçmiyorsa bir hekime başvurun.</li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>İyi uyku için alışkanlıklar</h2>
      <p class="soft">Bu alışkanlıklar tek başına kronik uykusuzluğu her zaman çözmez, ama iyi bir temel oluşturur.</p>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Aynı saatte kalkın</h3><p>Hafta sonu da dahil her gün aynı saatte kalkın. Sabah gün ışığına çıkmak iç saatinizi ayarlar.</p></div>
        <div class="kind"><span class="n">2</span><h3>Yatak uyku içindir</h3><p>Yaklaşık 20 dakikada uyuyamazsanız kalkın, loş ışıkta sakin bir şeyle uğraşın; uykunuz gelince dönün.</p></div>
        <div class="kind"><span class="n">3</span><h3>Kafeini erken bırakın</h3><p>Kahve ve çayı öğleden sonranın erken saatlerinde bırakın; kafein saatlerce etkisini sürdürür.</p></div>
        <div class="kind"><span class="n">4</span><h3>Gün içinde hareket edin</h3><p>Düzenli hareket, gün ışığı ve kısa tutulan öğle uykuları gece uykusunu destekler. <a href="sabah-rutini.html">Sabah rutini</a> iyi bir başlangıç olabilir.</p></div>
      </div>
      <p class="soft" style="margin-top:18px">Yatmadan önce zihniniz meşgulse <a href="stres.html">nefes egzersizleri</a> yardımcı olabilir.</p>
    </div>
  </section>

  <section id="video">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Uyku neden bu kadar önemli?</h2>
      <p class="soft">Uyku bilimci Matt Walker'ın, uykunun öğrenme, bağışıklık ve kalp sağlığındaki rolünü anlattığı çok izlenen TED konuşması. Konuşma İngilizcedir; oynatıcının altyazı ayarlarından Türkçe altyazı seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("5MuIMqhT8DM", "Uyku TED konuşmasını oynat", "Sleep Is Your Superpower | Matt Walker | TED")}
          <h3>Uyku sizin süper gücünüz</h3>
          <p>Konuşmadaki bazı çarpıcı ifadeler bilim insanları arasında tartışılıyor; temel mesajı olan düzenli ve yeterli uykunun önemi ise geniş kabul görüyor.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(SLEEP_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman bir hekime başvurmalı?</h2>
      <p class="soft">Ara sıra kötü uyumak normaldir. Şu durumlarda ise bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Haftalardır çoğu gece uykuya dalmakta ya da uykuyu sürdürmekte zorlanıyor, gündüz bunun etkisini hissediyorsanız</li>
        <li>Yüksek sesli horlamaya uykuda nefes durmaları ya da boğulur gibi uyanma eşlik ediyorsa</li>
        <li>Gündüz aşırı uyku hali varsa, özellikle araç kullanırken uyuklama oluyorsa</li>
        <li>Akşamları bacaklarda hareket ettirme isteğiyle birlikte rahatsız edici bir his uykuya dalmayı engelliyorsa</li>
        <li>Uykusuzluğa belirgin bir çökkünlük ya da kaygı eşlik ediyorsa</li>
      </ul>
      {CTA_CARD("Ağrı nedeniyle bozulan uykunuz", "ağrı nedeniyle bozulan uyku")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Watson NF, Badr MS, Belenky G, et al. " + ext("https://jcsm.aasm.org/doi/10.5664/jcsm.4758", "Recommended amount of sleep for a healthy adult: a joint consensus statement of the American Academy of Sleep Medicine and Sleep Research Society") + ". J Clin Sleep Med. 2015;11(6):591-592.",
        "Drake C, Roehrs T, Shambroom J, Roth T. " + ext("https://jcsm.aasm.org/doi/10.5664/jcsm.3170", "Caffeine effects on sleep taken 0, 3, or 6 hours before going to bed") + ". J Clin Sleep Med. 2013;9(11):1195-1200.",
        "Qaseem A, Kansagara D, Forciea MA, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/27136449/", "Management of chronic insomnia disorder in adults: a clinical practice guideline from the American College of Physicians") + ". Ann Intern Med. 2016;165(2):125-133.",
        "Krause AJ, Prather AA, Wager TD, Lindquist MA, Walker MP. " + ext("https://www.jneurosci.org/content/39/12/2291", "The pain of sleep loss: a brain characterization in humans") + ". J Neurosci. 2019;39(12):2291-2300.",
        "Staffe AT, Bech MW, Clemmensen SLK, et al. " + ext("https://pmc.ncbi.nlm.nih.gov/articles/PMC6892491/", "Total sleep deprivation increases pain sensitivity, impairs conditioned pain modulation and facilitates temporal summation of pain in healthy participants") + ". PLoS One. 2019.",
      ])}
    </div>
  </section>
</main>'''

SLEEP_JS = '''<script>
(function(){
  var root = document.getElementById('planlayici'); if (!root) return;
  var $ = function(id){ return document.getElementById(id); };
  var wake = $('p-wake'), need = 8;
  function fmt(m){ m = ((m % 1440) + 1440) % 1440; var h = Math.floor(m / 60), n = Math.round(m % 60); return (h < 10 ? '0' : '') + h + ':' + (n < 10 ? '0' : '') + n; }
  function upd(){
    var p = (wake.value || '07:00').split(':'), w = (+p[0]) * 60 + (+p[1]);
    var bed = w - need * 60 - 15;
    $('p-bed').textContent = fmt(bed); $('p-wind').textContent = fmt(bed - 60); $('p-caf').textContent = fmt(bed - 360);
  }
  $('p-need').addEventListener('click', function(e){
    var b = e.target.closest('button'); if (!b) return;
    this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
    need = +b.getAttribute('data-v'); upd();
  });
  wake.addEventListener('input', upd); wake.addEventListener('change', upd);
  upd();
})();
</script>
'''

page("uyku.html", "İyi Uyku İçin",
     "Yetişkinler kaç saat uyumalı, kahve uykuyu nasıl etkiler, uyku ile ağrı arasında nasıl bir ilişki var? Kronik uykusuzlukta ilk tercih tedavi, iyi uyku alışkanlıkları ve yatma saati planlayıcı.",
     "uyku.html", SELF_CSS, SLEEP_BODY, SLEEP_JS + YT_JS,
     seo_title="İyi Uyku İçin: Uyku Süresi, Kafein, Ağrı ve Yatma Saati Planlayıcı | İhsan Eren",
     about=[{"@type": "Thing", "name": "Uyku sağlığı"}, cond("Uykusuzluk")],
     faq_items=pick(SLEEP_FAQ, 0, 1, 2, 3))

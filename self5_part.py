# -*- coding: utf-8 -*-
# Kendine iyi bak, 5. tur: 30 saniye sandalye testi (kameralı sayaç). self4_part.py'den sonra exec edilir
# (SELF4_CSS, WAKE_JS, _ex2, ex_grid hazır). Kamera modu: MediaPipe Pose Landmarker (assets/mp/, 0.10.35),
# görüntü cihazda işlenir; model dosyası ilk açılışta Google'ın sunucusundan indirilir.

CS_MODEL = "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/1/pose_landmarker_lite.task"

SELF5_CSS = SELF4_CSS + """
  /* sandalye testi */
  .cs-stage{position:relative;width:100%;margin:0 auto 12px;background:#0d1712;border-radius:16px;overflow:hidden;border:1px solid var(--line);aspect-ratio:4/3}
  .cs-stage video,.cs-stage canvas{position:absolute;inset:0;width:100%;height:100%;object-fit:contain}
  .cs-stage.mir video,.cs-stage.mir canvas{transform:scaleX(-1)}
  .cs-hud{position:absolute;left:0;right:0;top:0;display:flex;justify-content:space-between;align-items:flex-start;padding:10px 14px;pointer-events:none;
    background:linear-gradient(rgba(0,0,0,.55),rgba(0,0,0,0))}
  .cs-hud b{font-family:var(--display);font-weight:400;font-size:clamp(48px,11vw,84px);line-height:1;color:#fff;font-variant-numeric:tabular-nums;text-shadow:0 2px 8px rgba(0,0,0,.6)}
  .cs-hud span{font-family:var(--display);font-size:clamp(22px,5vw,34px);color:var(--foil);font-variant-numeric:tabular-nums;text-shadow:0 2px 8px rgba(0,0,0,.6)}
  .cs-msg{position:absolute;inset:0;display:grid;place-content:center;text-align:center;padding:20px;color:var(--ink-soft);font-size:15px}
  .cs-chips{position:absolute;left:8px;right:8px;bottom:8px;display:flex;flex-wrap:wrap;gap:6px;pointer-events:none}
  .cs-chips i{font-style:normal;font-size:12.5px;padding:4px 10px;border-radius:999px;background:rgba(13,23,18,.78);color:#ece5cf;border:1px solid rgba(236,229,207,.25)}
  .cs-chips i.ok{border-color:var(--sage);color:#dfe9d3}
  .cs-chips i.ok::before{content:"✓ ";color:var(--sage)}
  .cs-chips i.no::before{content:"• ";color:#e2ab47}
  .cs-big{all:unset;box-sizing:border-box;display:block;width:100%;cursor:pointer;text-align:center;padding:30px 16px;border-radius:16px;margin-top:10px;
    font-family:var(--display);font-size:clamp(26px,4vw,32px);background:rgba(216,178,94,.16);color:var(--ink);border:2px dashed var(--foil);touch-action:manipulation}
  .cs-big:active{background:rgba(216,178,94,.32)}
  .cs-big:focus-visible{outline:3px solid var(--ink);outline-offset:3px}
  .cs-age{all:unset;box-sizing:border-box;width:110px;padding:9px 14px;border-radius:12px;border:1px solid var(--line-strong);font-size:16px;color:var(--ink);background:rgba(236,229,207,.04)}
  .cs-age:focus-visible{outline:2px solid var(--foil);outline-offset:2px}
  .cs-adj{display:flex;align-items:center;gap:10px;margin:12px 0 4px;font-size:14px;color:var(--ink-soft);flex-wrap:wrap}
  .cs-adj button{all:unset;cursor:pointer;width:38px;height:38px;border-radius:50%;border:1px solid var(--line-strong);text-align:center;line-height:38px;font-size:20px;color:var(--ink)}
  .cs-adj button:hover{border-color:var(--foil)}
  .cs-num{width:76px;text-align:center;padding:7px 8px}
  .cs-adj button:focus-visible{outline:2px solid var(--foil);outline-offset:2px}
  .cs-hist{list-style:none;margin:12px 0 0;padding:0;display:grid;gap:6px;font-size:14px;color:var(--ink-soft)}
  .cs-hist li{display:flex;justify-content:space-between;gap:10px;border-bottom:1px solid var(--line);padding:4px 0}
  .cs-hist li b{color:var(--ink);font-variant-numeric:tabular-nums}
  .cs-acts{display:flex;flex-wrap:wrap;gap:10px;margin-top:14px}
  .nt{width:100%;max-width:640px;border-collapse:collapse;margin-top:12px;font-size:15px}
  .nt th,.nt td{text-align:left;padding:9px 10px;border-bottom:1px solid var(--line)}
  .nt th{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:600}
  .nt td{color:var(--ink-soft);font-variant-numeric:tabular-nums}
  .nt td:first-child{color:var(--ink)}
  .nt tr.me td{background:rgba(216,178,94,.12)}
  .nt tr.me td:first-child{box-shadow:inset 3px 0 0 var(--foil)}
"""

# Rikli & Jones 1999 (60–94 yaş, n=7183): yaşıtların ortadaki yarısı (%25–75), [kadın, erkek]
CS_RJ = [("60–64", (12, 17), (14, 19)), ("65–69", (11, 16), (12, 18)), ("70–74", (10, 15), (12, 17)), ("75–79", (10, 15), (11, 17)),
         ("80–84", (9, 14), (10, 15)), ("85–89", (8, 13), (8, 14)), ("90–94", (4, 11), (7, 12))]
CS_ROWS = ('<tr data-a="20-59"><td>20–59</td><td>22,6 ± 6,2</td><td>24,2 ± 6,3</td></tr>\n' +
           "\n".join(f'<tr data-a="{a.replace("–", "-")}"><td>{a}</td><td>{w[0]}–{w[1]}</td><td>{m[0]}–{m[1]}</td></tr>' for a, w, m in CS_RJ))

_ex2("cs_sts", "sts", "Sandalyeden kalkıp oturma", "Testin kendisi en iyi egzersizidir. Sağlam, kolsuz bir sandalyede kollarınız göğsünüzde çapraz, kontrollü bir hızla kalkın ve oturun. Zor geliyorsa önce kollarınızdan destek alarak ya da daha yüksek bir sandalyeyle başlayın.", "8–12 tekrar, 2–3 set, haftada 2–3 gün")
_ex2("cs_wall", "wallsit", "Duvarda oturma", "Sırtınızı duvara dayayın, ayaklarınızı biraz öne alın ve dizlerinizi rahat edebildiğiniz kadar bükerek kayın. Dizleriniz ayak bileklerinizin üzerinde kalsın; nefesinizi tutmayın.", "20–30 saniye, 3–4 kez")
_ex2("cs_bridge", "bridge", "Köprü", "Sırtüstü yatın, dizleriniz bükülü ve ayaklarınız yerde olsun. Kalçanızı sıkarak yerden kaldırın, omuzlarınızdan dizlerinize düz bir çizgi oluşsun; yavaşça indirin.", "10–12 tekrar, 2–3 set")
_ex2("cs_heel", "heel2", "Topuk yükseltme", "Bir tezgâha hafifçe tutunarak dik durun. Topuklarınızı kaldırıp parmak uçlarınızda yükselin, yavaşça inin. Kolaylaşınca tek ayakla deneyin.", "10–15 tekrar, 2–3 set")

CS_FAQ = [
 ("Kamera görüntüm bir yere gönderiliyor mu?", "Hayır. Görüntü yalnızca sizin cihazınızda, tarayıcınızın içinde işlenir; kaydedilmez ve hiçbir sunucuya gönderilmez. Kamerayı ilk açtığınızda hareket algılama programı (Google’ın açık kaynaklı MediaPipe modeli, toplam yaklaşık 17 MB) cihazınıza indirilir; sayma işi tamamen cihazınızda yapılır. Sonuçlarınız da yalnızca bu cihazda saklanır."),
 ("Kamera yanlış sayarsa ne olur?", "Kamera sayacı bir yardımcıdır, kusursuz değildir. Bol kıyafet, kötü ışık ya da bacaklarınızın görüntüden çıkması sayımı bozabilir. Test bitince sayıyı kendiniz düzeltebilirsiniz. En güvenilir yol, yanınızdaki birinin de saymasıdır."),
 ("Kollarımı kullanmadan kalkamıyorsam?", "CDC’nin STEADI protokolüne göre kalkmak için kollarınızı kullanmanız gerekiyorsa test durdurulur ve sonuç 0 kaydedilir. Bu, bacak gücünüzün desteğe ihtiyacı olduğunu gösterir; bir fizyoterapist ya da hekimle değerlendirme yaptırmanız iyi olur."),
 ("Bu test düşüp düşmeyeceğimi kesin olarak söyler mi?", "Hayır. İngiltere’nin ulusal sağlık kılavuzu NICE (2025), düşme riskini tahmin etmek için tek başına bir test ya da puanlama aracı kullanılmamasını öneriyor; bu tür testler yürüme ve denge sorunlarını fark etmeye yardım eder. Bu yüzden son bir yılda düştüyseniz, sonucunuz ne olursa olsun bunu hekiminize söyleyin. Birden fazla kez düştüyseniz, düşmede yaralandıysanız, bilincinizi kaybettiyseniz ya da yerden yardımsız kalkamadıysanız kapsamlı bir düşme değerlendirmesi isteyebilirsiniz."),
 ("Sonucumu geliştirebilir miyim?", "Evet. Bacak gücü her yaşta egzersizle gelişebilir. Aşağıdaki egzersizlerle başlayabilir, testi birkaç haftada bir tekrarlayarak ilerlemenizi izleyebilirsiniz. Kalça kireçlenmesi olanlarda yapılan bir çalışmada 2 tekrarlık artış anlamlı bir iyileşme olarak kabul edildi."),
]

CS_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>30 saniye sandalye testi</h1>
    <p class="lede">30 saniyede bir sandalyeden kaç kez kalkabiliyorsunuz? Bu basit test bacaklarınızın gücünü ve dayanıklılığını ölçer. ABD Hastalık Kontrol ve Önleme Merkezi (CDC), yaşlılarda düşme riskini değerlendirirken bu testi kullanıyor. Telefonunuzun kamerası tekrarlarınızı sizin yerinize sayabilir; görüntünüz cihazınızdan dışarı çıkmaz.</p>
    <p class="meta">Son güncelleme: 15 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>30 saniye</b><span>Testin süresi; kollar göğüste çapraz, kalkışlar sayılır</span></div>
        <div class="stat"><b>43 cm</b><span>Önerilen sandalye yüksekliği (yaklaşık); kolçaksız, sırtı düz</span></div>
        <div class="stat"><b>7.183 kişi</b><span>60–94 yaş için karşılaştırma değerlerinin dayandığı araştırmadaki katılımcı sayısı</span></div>
        <div class="stat"><b>2 tekrar</b><span>Kalça kireçlenmesinde anlamlı kabul edilen en küçük iyileşme</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Kendinizi ölçün</p>
      <h2>Kamerayla ya da kamerasız deneyin</h2>
      <p class="soft">Kamerayla: telefonu 2–3 metre uzağa, bel hizasında bir yere koyun; sizi yandan, başınızdan ayaklarınıza kadar görsün. Kamerasız: yanınızdaki biri her kalkışınızda ekrana dokunsun; yalnızsanız kalkışlarınızı kendiniz sayın ve süre bitince sonucu girin.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <p class="lbl">Yöntem</p>
            <div class="seg" role="group" aria-label="Yöntem" id="cs-mode">
              <button type="button" data-v="cam" aria-pressed="true">Kamerayla</button>
              <button type="button" data-v="tap" aria-pressed="false">Kamerasız</button>
            </div>
            <p class="lbl">Cinsiyet</p>
            <div class="seg" role="group" aria-label="Cinsiyet" id="cs-sex">
              <button type="button" data-v="f" aria-pressed="true">Kadın</button>
              <button type="button" data-v="m" aria-pressed="false">Erkek</button>
            </div>
            <p class="lbl"><label for="cs-age">Yaşınız</label></p>
            <input class="cs-age" id="cs-age" type="number" inputmode="numeric" min="18" max="110" placeholder="ör. 65">
          </div>
          <div class="bt-out">
            <div class="res" id="cs-res" hidden>
              <p class="lab" id="cs-lab"></p>
              <p id="cs-txt"></p>
              <span class="bt-badge" id="cs-badge"></span>
              <div class="cs-adj"><label for="cs-num">Sayımı düzeltin:</label><button type="button" id="cs-minus" aria-label="Bir eksilt">−</button><input class="cs-age cs-num" id="cs-num" type="number" inputmode="numeric" min="0" max="60"><button type="button" id="cs-plus" aria-label="Bir artır">+</button></div>
              <div class="cs-acts"><a class="cta" id="cs-wa" href="#" target="_blank" rel="noopener">Sonucumu WhatsApp’tan gönder</a></div>
            </div>
            <div id="cs-histw" style="margin-top:20px" hidden>
              <p class="lbl">Önceki sonuçlarınız (bu cihazda)</p>
              <ul class="cs-hist" id="cs-hist"></ul>
            </div>
          </div>
          <div class="bt-run">
            <div class="cs-stage" id="cs-stage">
              <video id="cs-video" playsinline muted></video>
              <canvas id="cs-canvas"></canvas>
              <div class="cs-hud" id="cs-hud" hidden><b id="cs-hn">0</b><span id="cs-ht">30</span></div>
              <div class="cs-chips" id="cs-chips" hidden><i id="cs-c1">Baştan ayağa görünün</i><i id="cs-c2">Oturun</i></div>
              <div class="cs-msg" id="cs-msg">Kamerayı açınca görüntünüz burada görünür. Görüntü cihazınızdan çıkmaz.</div>
            </div>
            <div class="bt-ring" id="cs-ring" hidden><svg viewBox="0 0 132 132" aria-hidden="true"><circle class="bg" cx="66" cy="66" r="58"/><circle class="fg" id="cs-arc" cx="66" cy="66" r="58" stroke-dasharray="364.4" stroke-dashoffset="364.4"/></svg>
              <div class="c"><b id="cs-n">0</b><span id="cs-unit">tekrar</span></div></div>
            <p class="bt-phase" id="cs-phase" aria-live="polite">Hazır</p>
            <p class="bt-cue" id="cs-cue">Kamerayı açın, sandalyenizi ve telefonu yerleştirin.</p>
            <button type="button" class="bt-tap" id="cs-cam">Kamerayı aç</button>
            <button type="button" class="bt-tap" id="cs-go" hidden>Başlat</button>
            <button type="button" class="cs-big" id="cs-tap" hidden>Kalktı · +1</button>
            <div class="controls" style="margin-top:10px;justify-content:center">
              <button type="button" class="cta ghost" id="cs-flip" hidden>Kamerayı çevir</button>
              <button type="button" class="cta ghost" id="cs-off" hidden>Kamerayı kapat</button>
            </div>
            <label class="snd"><input type="checkbox" id="cs-sound" checked> Sesli uyarı</label>
          </div>
        </div>
        <div class="cs-strings" hidden>
          <span data-k="ready">Hazır</span>
          <span data-k="readycam">Kamerayı açın, sandalyenizi ve telefonu yerleştirin.</span>
          <span data-k="readytap">Başlat’a basınca 5 saniyelik hazırlanma süresi başlar.</span>
          <span data-k="cam">Kamerayı aç</span>
          <span data-k="loading">Hareket algılama yükleniyor (ilk seferde yaklaşık 17 MB)…</span>
          <span data-k="asking">Kamera izni bekleniyor…</span>
          <span data-k="denied">Kamera açılamadı. Tarayıcı ayarlarından kamera izni verebilir ya da kamerasız yöntemi kullanabilirsiniz.</span>
          <span data-k="failed">Hareket algılama bu cihazda yüklenemedi. Kamerasız yöntemi kullanabilirsiniz.</span>
          <span data-k="idlemsg">Kamerayı açınca görüntünüz burada görünür. Görüntü cihazınızdan çıkmaz.</span>
          <span data-k="camready">Kamera hazır</span>
          <span data-k="camreadyc">Sandalyeye oturun ve baştan ayağa göründüğünüzden emin olun. Hazır olunca Başlat’a basın; 10 saniye sonra test başlar.</span>
          <span data-k="c1ok">Baştan ayağa görünüyorsunuz</span>
          <span data-k="c1no">Baştan ayağa görünün</span>
          <span data-k="c2sit">Oturuyorsunuz</span>
          <span data-k="c2up">Ayaktasınız</span>
          <span data-k="c2no">Oturun</span>
          <span data-k="prep">Hazırlanın</span>
          <span data-k="prepcam">Sandalyenize oturun, kollarınızı göğsünüzde çapraz yapın. Sinyalle birlikte kalkıp oturmaya başlayın.</span>
          <span data-k="preptap">Kollarınızı göğsünüzde çapraz yapın. Sinyalle birlikte kalkıp oturmaya başlayın.</span>
          <span data-k="go">Kalkın ve oturun</span>
          <span data-k="gocam">Tam ayağa kalkın, sonra tekrar oturun. Her kalkışta bip sesi duyacaksınız.</span>
          <span data-k="gotap">Her tam kalkışta büyük düğmeye dokunun.</span>
          <span data-k="lost">Bacaklarınız görüntüden çıktı</span>
          <span data-k="broke">Test yarıda kaldı</span>
          <span data-k="brokec">Ekran kapandığı ya da başka bir uygulamaya geçildiği için süre doğru ölçülemedi; sonuç kaydedilmedi. Kamerayı yeniden açıp tekrar deneyebilirsiniz.</span>
          <span data-k="start">Başlat</span>
          <span data-k="stop">Durdur</span>
          <span data-k="again">Yeniden dene</span>
          <span data-k="done">Süre doldu</span>
          <span data-k="donec">Sonucunuz ve yaşınıza göre karşılaştırma hazır. Sayım yanlışsa düzeltebilirsiniz.</span>
          <span data-k="half">Süre biterken yarıdan fazla doğrulmuştunuz; kurala göre bu da sayıldı.</span>
          <span data-k="rep">tekrar</span>
          <span data-k="lab">Sonucunuz: {{n}} tekrar</span>
          <span data-k="noage">Karşılaştırma için yaşınızı girin.</span>
          <span data-k="outage">Bu yaş için güvenilir bir karşılaştırma değeri yok; sonucunuzu zaman içinde kendinizle karşılaştırabilirsiniz.</span>
          <span data-k="rjlow">Yaşıtlarınızın ortadaki yarısı {{lo}}–{{hi}} tekrar yapıyor; siz bunun altındasınız. CDC’nin STEADI aracına göre bu, ortalamanın altı demek ve düşme riskine işaret eder.</span>
          <span data-k="rjmid">Yaşıtlarınızın ortadaki yarısıyla aynı aralıktasınız ({{lo}}–{{hi}} tekrar).</span>
          <span data-k="rjhigh">Yaşıtlarınızın ortadaki yarısı {{lo}}–{{hi}} tekrar yapıyor; siz üst çeyrektesiniz.</span>
          <span data-k="mklow">Yaş grubunuzda ortalama {{m}} tekrar; çoğu kişi {{a}}–{{b}} arasında. Siz bu aralığın altındasınız.</span>
          <span data-k="mkmid">Yaş grubunuzda ortalama {{m}} tekrar; çoğu kişi {{a}}–{{b}} arasında. Siz bu aralıktasınız.</span>
          <span data-k="mkhigh">Yaş grubunuzda ortalama {{m}} tekrar; çoğu kişi {{a}}–{{b}} arasında. Siz bu aralığın üzerindesiniz.</span>
          <span data-k="blow">Ortalamanın altında</span>
          <span data-k="bmid">Ortalama aralıkta</span>
          <span data-k="bhigh">Ortalamanın üzerinde</span>
          <span data-k="lownote">Bu bir tanı değildir. Bacak gücü egzersizle gelişir; aşağıdaki egzersizlerle başlayabilir, düşme kaygınız varsa hekiminiz ya da fizyoterapistinizle konuşabilirsiniz.</span>
          <span data-k="zero">Kalkmak için kollarınızı kullanmanız gerektiyse sonuç 0 kaydedilir. Bir fizyoterapist ya da hekimle değerlendirme yaptırmanız iyi olur.</span>
          <span data-k="delta">Önceki sonucunuza göre {{d}}</span>
          <span data-k="wa">Merhaba, drihsaneren.com’daki 30 saniye sandalye testini yaptım: {{n}} tekrar ({{s}}, {{a}} yaş). Değerlendirme hakkında bilgi almak istiyorum.</span>
          <span data-k="wanoage">Merhaba, drihsaneren.com’daki 30 saniye sandalye testini yaptım: {{n}} tekrar. Değerlendirme hakkında bilgi almak istiyorum.</span>
          <span data-k="sf">kadın</span>
          <span data-k="sm">erkek</span>
          <span data-k="cammode">Kameralı sayım</span>
          <span data-k="tapmode">Elle sayım</span>
        </div>
      </div>
      <p class="count">Kamera görüntünüz yalnızca bu cihazda işlenir; kaydedilmez, hiçbir yere gönderilmez. Sonuçlarınız yalnızca bu cihazda saklanır.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nasıl yapılır?</h2>
        <ol class="steps">
          <li><span>Kolçaksız, sırtı düz, <strong>sağlam bir sandalyeyi</strong> kaymaması için duvara dayayın (oturak yüksekliği yaklaşık 43 cm).</span></li>
          <li><span>Sandalyenin ortasına oturun, ayaklarınız yere düz bassın. Kollarınızı <strong>göğsünüzde çapraz</strong> yapın, elleriniz karşı omuzlarınızda dursun.</span></li>
          <li><span>Sinyalle birlikte <strong>tam ayağa kalkın</strong>, sonra tekrar oturun. 30 saniye boyunca tekrarlayın.</span></li>
          <li><span>Yalnızca tam kalkışlar sayılır. Süre bittiğinde <strong>yarıdan fazla doğrulmuşsanız</strong> o kalkış da sayılır. Kalkmak için kollarınızı kullanmanız gerekirse test durur ve sonuç 0 olur.</span></li>
        </ol>
      </div>
      <div>
        <h2>Güvenle yapmak için</h2>
        <ul class="dots">
          <li>CDC, test sırasında yanınızda birinin durmasını öneriyor. Yakın zamanda düştüyseniz, baş dönmeniz ya da denge sorununuz varsa testi yalnız yapmayın.</li>
          <li>Göğüs ağrısı, nefes darlığı, baş dönmesi ya da belirgin diz veya kalça ağrısı olursa hemen durun.</li>
          <li>Kamera için arkanızda parlak bir pencere olmasın; bol kıyafet kalça ve dizlerinizi gizleyebilir.</li>
          <li>Yarışmayın: hızlı ama kontrollü kalkıp oturun, sandalyeye kendinizi bırakmayın.</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="normlar">
    <div class="wrap">
      <p class="eyebrow">Karşılaştırma</p>
      <h2>Yaşa göre tekrar sayıları</h2>
      <p class="soft">60–94 yaş: 7.183 kişilik bir araştırmada yaşıtların ortadaki yarısının (%25–75) yaptığı tekrar aralığı. Bu aralığın altı, CDC’nin STEADI aracında “ortalamanın altı” kabul edilir ve düşme riskine işaret eder. 20–59 yaş: 400 sağlıklı yetişkinde ortalama ± standart sapma. Yaş grubunuz yukarıdaki yaşa göre işaretlenir.</p>
      <table class="nt" id="cs-nt">
        <thead><tr><th>Yaş</th><th>Kadın</th><th>Erkek</th></tr></thead>
        <tbody>
{CS_ROWS}
        </tbody>
      </table>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Bacaklarınızı güçlendirin</p>
      <h2>Evde dört egzersiz</h2>
      <p class="soft">Haftada 2–3 gün, ağrısız bir aralıkta yapın. Birkaç hafta sonra testi tekrarlayıp ilerlemenizi görebilirsiniz. Denge için <a href="denge-testi.html">10 saniye denge testine</a>, düşme riskiniz için <a href="dusme-onleme.html">düşmeleri önleme</a> rehberine bakabilirsiniz.</p>
      {ex_grid(["cs_sts", "cs_wall", "cs_bridge", "cs_heel"], "ex four")}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(CS_FAQ)}
      {CTA_CARD("Bacak gücünüz ve düşme riskiniz", "bacak gücü ve denge değerlendirmesi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Centers for Disease Control and Prevention. " + ext("https://www.cdc.gov/steadi/media/pdfs/STEADI-Assessment-30Sec-508.pdf", "STEADI Assessment: 30-Second Chair Stand") + ". 2017.",
        "Rikli RE, Jones CJ. Functional fitness normative scores for community-residing older adults, ages 60–94. J Aging Phys Act. 1999;7:162–181.",
        "McKay MJ, Baldwin JN, Ferreira P, et al. Reference values for developing responsive functional outcome measures across the lifespan. Neurology. 2017;88:1512–1519.",
        "Wright AA, Cook CE, et al. A comparison of 3 methodological approaches to defining major clinically important improvement of 4 performance measures in patients with hip osteoarthritis. J Orthop Sports Phys Ther. 2011;41(5):319–327.",
        "Shirley Ryan AbilityLab. " + ext("https://www.sralab.org/rehabilitation-measures/30-second-sit-stand-test", "30 Second Sit to Stand Test") + ". Rehabilitation Measures Database.",
        "NICE. " + ext("https://www.nice.org.uk/guidance/ng249", "Falls: assessment and prevention in older people and in people 50 and over at higher risk") + ". NICE guideline NG249, 29 April 2025",
        "Montero-Odasso M, van der Velde N, Martin FC, et al. " + ext("https://doi.org/10.1093/ageing/afac205", "World guidelines for falls prevention and management for older adults: a global initiative") + ". Age Ageing. 2022;51(9):afac205",
      ])}
    </div>
  </section>
</main>'''

CS_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.cs-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var EN = document.documentElement.lang === 'en';
  var $ = function(id){ return document.getElementById(id); };
  var MODEL = "''' + CS_MODEL + '''", MP = '/assets/mp/';
  var RJ = {60: [[12, 17], [14, 19]], 65: [[11, 16], [12, 18]], 70: [[10, 15], [12, 17]], 75: [[10, 15], [11, 17]], 80: [[9, 14], [10, 15]], 85: [[8, 13], [8, 14]], 90: [[4, 11], [7, 12]]};
  var MK = [[22.6, 6.2], [24.2, 6.3]];
  var KEY = 'drihsaneren.sandalye.v1', WA = 'https://wa.me/905538815568?text=';
  var C = 364.4, DUR = 30, snd = $('cs-sound'), ctx = null, lock = null;
  var mode = 'cam', sex = 'f', phase = 'idle', n = 0, t0 = 0, iv = null, last = null, halfAdded = false;
  var video = $('cs-video'), canvas = $('cs-canvas'), cx = canvas.getContext('2d'), stage = $('cs-stage');
  var pl = null, mod = null, deleg = 'GPU', dly = [], stream = null, facing = 'user', raf = 0, lastTs = 0, fr = 0, tr = [], seen = 0, nsv = null, broke = false, lockP = false;
''' + WAKE_JS + '''
  function fmt(x){ var s = String(x); return EN ? s : s.replace('.', ','); }
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function age(){ var a = parseInt($('cs-age').value, 10); return isNaN(a) ? null : a; }
  function store(){ try { return JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { return []; } }
  function save(list){ try { localStorage.setItem(KEY, JSON.stringify(list.slice(-10))); } catch (e) {} }
  // ---------- karşılaştırma
  function verdict(x){
    var a = age(); if (a == null) return {t: S.noage};
    var si = sex === 'm' ? 1 : 0;
    if (a >= 60 && a <= 94){
      var r = RJ[Math.min(90, Math.floor(a / 5) * 5)][si], o = {lo: r[0], hi: r[1]};
      if (x < r[0]) return {t: fill(S.rjlow, o), b: S.blow, low: true};
      if (x > r[1]) return {t: fill(S.rjhigh, o), b: S.bhigh};
      return {t: fill(S.rjmid, o), b: S.bmid};
    }
    if (a >= 20 && a <= 59){
      var m = MK[si], o2 = {m: fmt(m[0]), a: Math.round(m[0] - m[1]), b: Math.round(m[0] + m[1])};
      if (x < m[0] - m[1]) return {t: fill(S.mklow, o2), b: S.blow, low: true};
      if (x > m[0] + m[1]) return {t: fill(S.mkhigh, o2), b: S.bhigh};
      return {t: fill(S.mkmid, o2), b: S.bmid};
    }
    return {t: S.outage};
  }
  function paintNorm(){
    var a = age(), key = null;
    if (a != null){ if (a >= 20 && a <= 59) key = '20-59'; else if (a >= 60 && a <= 94){ var b = Math.min(90, Math.floor(a / 5) * 5); key = b + '-' + (b + 4); } }
    $('cs-nt').querySelectorAll('tbody tr').forEach(function(r){ r.classList.toggle('me', r.getAttribute('data-a') === key); });
  }
  function paintRes(){
    var res = $('cs-res'); if (last == null){ res.hidden = true; return; }
    res.hidden = false;
    $('cs-lab').textContent = fill(S.lab, {n: last});
    if (document.activeElement !== $('cs-num')) $('cs-num').value = last;
    var v = verdict(last), txt = v.t, badge = $('cs-badge');
    if (last === 0) txt += ' ' + S.zero; else if (v.low) txt += ' ' + S.lownote;
    if (halfAdded) txt = S.half + ' ' + txt;
    var h = store(); if (h.length > 1){ var d = last - h[h.length - 2].n; txt += ' ' + fill(S.delta, {d: (d > 0 ? '+' : '') + d}) + '.'; }
    $('cs-txt').textContent = txt;
    badge.hidden = !v.b; if (v.b){ badge.textContent = v.b; badge.classList.toggle('no', !!v.low); }
    var a = age(), msg = a == null ? fill(S.wanoage, {n: last}) : fill(S.wa, {n: last, a: a, s: sex === 'm' ? S.sm : S.sf});
    $('cs-wa').href = WA + encodeURIComponent(msg);
    paintHist();
  }
  function paintHist(){
    var h = store(), ul = $('cs-hist'); $('cs-histw').hidden = !h.length; ul.innerHTML = '';
    h.slice().reverse().forEach(function(r){
      var li = document.createElement('li'), d = new Date(r.t), sp = document.createElement('span'), b = document.createElement('b');
      sp.textContent = d.toLocaleDateString(EN ? 'en-GB' : 'tr-TR', {day: 'numeric', month: 'short', year: 'numeric'}) + ' · ' + (r.m === 'cam' ? S.cammode : S.tapmode);
      b.textContent = r.n + ' ' + S.rep; li.appendChild(sp); li.appendChild(b); ul.appendChild(li);
    });
  }
  function setLast(v){
    if (last == null || isNaN(v)) return; last = Math.max(0, Math.min(60, v)); halfAdded = false; n = last; paintCount();
    var h = store(); if (h.length){ h[h.length - 1].n = last; save(h); }
    paintRes();
  }
  // ---------- sayaç görünümü
  function paintCount(){ $('cs-n').textContent = String(n); $('cs-hn').textContent = String(n); }
  function paintTime(el){
    var left = Math.max(0, DUR - el);
    $('cs-arc').style.strokeDashoffset = (C * (1 - Math.min(el, DUR) / DUR)).toFixed(1);
    $('cs-ht').textContent = String(Math.ceil(left));
  }
  function vid(on){
    if (on){
      if (!nsv){ nsv = document.createElement('video'); nsv.setAttribute('playsinline', ''); nsv.setAttribute('muted', ''); nsv.muted = true; nsv.loop = true;
        nsv.src = MP + 'awake.mp4'; nsv.style.cssText = 'position:fixed;left:0;top:0;width:1px;height:1px;opacity:0;pointer-events:none'; document.body.appendChild(nsv); }
      var pp = nsv.play(); if (pp && pp.catch) pp.catch(function(){});
    } else if (nsv) nsv.pause();
  }
  function awake(on){
    if (on){
      if (navigator.wakeLock){ if (!lock && !lockP){ lockP = true; navigator.wakeLock.request('screen').then(function(l){ lockP = false; lock = l; l.addEventListener('release', function(){ if (lock === l) lock = null; }); }).catch(function(){ lockP = false; vid(true); }); } }
      else vid(true);
    } else { if (lock){ try { lock.release(); } catch (e) {} lock = null; } vid(false); }
  }
  function setPhase(p, c){ $('cs-phase').textContent = p; $('cs-cue').textContent = c; }
  function buttons(){
    var cam = mode === 'cam', on = !!stream;
    $('cs-cam').hidden = !cam || on || phase !== 'idle';
    $('cs-go').hidden = (cam && !on) || (phase === 'run' && !cam);
    $('cs-go').textContent = phase === 'idle' ? (last == null ? S.start : S.again) : S.stop;
    $('cs-go').classList.toggle('stop', phase !== 'idle');
    $('cs-tap').hidden = cam || phase !== 'run';
    $('cs-flip').hidden = !cam || !on || phase !== 'idle';
    $('cs-off').hidden = !cam || !on || phase !== 'idle';
    stage.hidden = !cam; $('cs-ring').hidden = cam;
    $('cs-hud').hidden = !cam || !on;
    $('cs-chips').hidden = !cam || !on;
  }
  function idle(){
    phase = 'idle'; clearInterval(iv); iv = null; awake(!!stream);
    if (mode === 'cam') stream ? setPhase(S.camready, S.camreadyc) : setPhase(S.ready, S.readycam);
    else setPhase(S.ready, S.readytap);
    buttons();
  }
  function finish(){
    clearInterval(iv); iv = null; halfAdded = false;
    if (mode === 'cam' && CT.state === 'down' && CT.sm != null && CT.sm > 0.5 && CT.prev != null && CT.sm >= CT.prev){ n++; halfAdded = true; paintCount(); }
    last = n; var h = store(); h.push({t: new Date().toISOString(), n: n, m: mode}); save(h);
    beep(660, 0.2); setTimeout(function(){ beep(880, 0.5); }, 220);
    phase = 'idle'; awake(!!stream); paintRes(); setPhase(S.done, S.donec); buttons();
    if (window.innerWidth <= 820) $('cs-res').scrollIntoView({behavior: 'smooth', block: 'center'});
  }
  function start(){
    var prep = mode === 'cam' ? 10 : 5;
    n = 0; paintCount(); paintTime(0); halfAdded = false;
    phase = 'prep'; t0 = performance.now(); awake(true);
    setPhase(S.prep, mode === 'cam' ? S.prepcam : S.preptap); buttons();
    var lastS = prep; $('cs-ht').textContent = String(prep); if (mode === 'tap') $('cs-n').textContent = String(prep);
    beep(520, 0.08);
    clearInterval(iv);
    iv = setInterval(function(){
      var el = (performance.now() - t0) / 1000;
      if (phase === 'prep'){
        var s = Math.ceil(prep - el);
        if (s !== lastS && s > 0){ lastS = s; if (s <= 3) beep(520, 0.1); }
        $('cs-ht').textContent = String(Math.max(1, s)); if (mode === 'tap') $('cs-n').textContent = String(Math.max(1, s));
        if (el >= prep){
          phase = 'run'; t0 = performance.now(); CT.reset();
          paintCount(); beep(880, 0.4); setPhase(S.go, mode === 'cam' ? S.gocam : S.gotap); buttons();
        }
        return;
      }
      if (el >= DUR){ paintTime(DUR); finish(); return; }
      paintTime(el);
    }, 50);
  }
  function count(){ if (phase !== 'run') return; n++; paintCount(); beep(990, 0.12, 0.25); }
  // ---------- kamera ve hareket algılama
  // Sayaç: son 5 ölçümün medyanı (anlık sıçramaları siler) + yumuşatma; eşiğin ötesinde en az 120–150 ms kalmalı.
  // Kısa süren 'oturma'lar (takılma) sayılmaz. 0 ≈ oturuyor, 1 ≈ ayakta.
  function mkCounter(onUp){
    var UP = 0.75, DOWN = 0.40, buf = [], sm = null, prev = null, st = null, cand = null, candT = 0, lastUp = -1e9, downAt = -1e9;
    function med(a){ var b = a.slice().sort(function(x, y){ return x - y; }); return b[b.length >> 1]; }
    return {
      feed: function(r, t){
        buf.push(r); if (buf.length > 5) buf.shift();
        var m = med(buf); prev = sm; sm = sm == null ? m : sm * 0.4 + m * 0.6;
        if (st == null){ st = sm > 0.6 ? 'up' : 'down'; return; }
        var want = st === 'down' ? (sm > UP ? 'up' : null) : (sm < DOWN ? 'down' : null);
        if (!want){ cand = null; return; }
        if (cand !== want){ cand = want; candT = t; return; }
        if (t - candT < (want === 'up' ? 120 : 150)) return;
        if (want === 'up'){
          // Oturma 200 ms'den kısa sürdüyse ya da son sayımdan beri 500 ms geçmediyse bu bir takılmadır: sayma
          var real = (candT - downAt) >= 200 && (t - lastUp) >= 500;
          st = 'up'; cand = null; if (real){ lastUp = t; onUp(); }
        } else { st = 'down'; downAt = candT; cand = null; }
      },
      reset: function(){ st = sm == null ? null : (sm > 0.6 ? 'up' : 'down'); cand = null; },
      clear: function(){ buf = []; sm = null; prev = null; st = null; cand = null; },
      get state(){ return st; }, get sm(){ return sm; }, get prev(){ return prev; }
    };
  }
  var CT = mkCounter(function(){ count(); });
  function sideMetric(L, w, h){
    var sides = [];
    [[23, 25, 27], [24, 26, 28]].forEach(function(s){
      var a = L[s[0]], k = L[s[1]], f = L[s[2]];
      var v = Math.min(a.visibility || 0, k.visibility || 0, f.visibility || 0);
      var shin = Math.hypot((k.x - f.x) * w, (k.y - f.y) * h);
      if (v < 0.15 || shin < 4) return;
      // diz–kalça ve ayak bileği–kalça yüksekliklerinin ortalaması (baldır boyuna oranla)
      var r = 0.5 * ((k.y - a.y) * h / shin) + 0.5 * ((f.y - a.y) * h / shin - 1);
      sides.push({r: r, v: v});
    });
    if (!sides.length) return null;
    sides.sort(function(x, y){ return y.v - x.v; });
    if (sides.length > 1 && sides[1].v > 0.6) return {r: (sides[0].r * sides[0].v + sides[1].r * sides[1].v) / (sides[0].v + sides[1].v), q: sides[0].v};
    return {r: sides[0].r, q: sides[0].v};
  }
  var BONES = [[11, 12], [11, 23], [12, 24], [23, 24], [23, 25], [25, 27], [24, 26], [26, 28], [27, 31], [28, 32], [11, 13], [13, 15], [12, 14], [14, 16]];
  function draw(L){
    var w = canvas.width, h = canvas.height; cx.clearRect(0, 0, w, h); if (!L) return;
    cx.lineWidth = Math.max(3, w / 160); cx.lineCap = 'round'; cx.strokeStyle = 'rgba(216,178,94,.9)';
    BONES.forEach(function(b){ var p = L[b[0]], q = L[b[1]]; if ((p.visibility || 0) < 0.3 || (q.visibility || 0) < 0.3) return;
      cx.beginPath(); cx.moveTo(p.x * w, p.y * h); cx.lineTo(q.x * w, q.y * h); cx.stroke(); });
    cx.fillStyle = '#8fa476';
    [23, 24, 25, 26, 27, 28].forEach(function(i){ var p = L[i]; if ((p.visibility || 0) < 0.3) return; cx.beginPath(); cx.arc(p.x * w, p.y * h, Math.max(5, w / 90), 0, 7); cx.fill(); });
  }
  function chips(full, r){
    var c1 = $('cs-c1'), c2 = $('cs-c2');
    c1.textContent = full ? S.c1ok : S.c1no; c1.className = full ? 'ok' : 'no';
    if (r == null){ c2.textContent = S.c2no; c2.className = 'no'; }
    else if (r < 0.5){ c2.textContent = S.c2sit; c2.className = 'ok'; }
    else { c2.textContent = S.c2up; c2.className = 'no'; }
  }
  function loop(){
    raf = requestAnimationFrame(loop);
    if (!pl || !stream || video.readyState < 2) return;
    var now = performance.now(); if (now - lastTs < 45) return; lastTs = now;
    if (canvas.width !== video.videoWidth){ canvas.width = video.videoWidth; canvas.height = video.videoHeight; stage.style.aspectRatio = video.videoWidth + ' / ' + video.videoHeight; }
    var res, t1 = performance.now(); try { res = pl.detectForVideo(video, now); fr++; } catch (e) { return; }
    if (deleg === 'GPU' && fr > 1){ dly.push(performance.now() - t1); if (dly.length >= 3){ var avg = (dly[0] + dly[1] + dly[2]) / 3; dly = []; if (avg > 150) toCPU(); else deleg = 'GPU+'; } }
    var L = res && res.landmarks && res.landmarks[0];
    draw(L);
    if (!L){ chips(false, null); lost(now); return; }
    var m = sideMetric(L, video.videoWidth, video.videoHeight);
    var inF = function(i){ return L[i].y > -0.02 && L[i].y < 1.02 && (L[i].visibility || 0) > 0.15; };
    var full = !!m && inF(0) && (inF(27) || inF(28)) && (inF(23) || inF(24));
    if (!m){ chips(false, null); lost(now); return; }
    seen = now; CT.feed(m.r, now); chips(full, CT.sm == null ? m.r : CT.sm);
    if (tr.length < 600) tr.push([Math.round(now), +m.r.toFixed(2), +CT.sm.toFixed(2)]);
  }
  function lost(now){ if (phase === 'run' && now - seen > 800) $('cs-cue').textContent = S.lost; }
  var FS = {wasmLoaderPath: MP + 'vision_wasm_internal.js', wasmBinaryPath: MP + 'vision_wasm_internal.wasm'};
  function opt(d){ return {baseOptions: {modelAssetPath: MODEL, delegate: d}, runningMode: 'VIDEO', numPoses: 1}; }
  function loadModel(){
    if (pl) return Promise.resolve(pl);
    return import(MP + 'vision_bundle.js').then(function(m){
      mod = m;
      return m.PoseLandmarker.createFromOptions(FS, opt('GPU')).catch(function(){ deleg = 'CPU'; return m.PoseLandmarker.createFromOptions(FS, opt('CPU')); });
    }).then(function(p){ pl = p; return p; });
  }
  // Grafik işlemci yavaşsa (bazı cihazlarda) işlemciye geç
  function toCPU(){
    var old = pl; pl = null; deleg = 'CPU';
    mod.PoseLandmarker.createFromOptions(FS, opt('CPU')).then(function(p){ pl = p; try { old.close(); } catch (e) {} }, function(){ pl = old; });
  }
  function msg(t){ var e = $('cs-msg'); e.hidden = !t; e.textContent = t || ''; }
  function openCam(){
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia){ msg(S.denied); return; }
    $('cs-cam').disabled = true; msg(S.loading); setPhase(S.ready, S.loading);
    loadModel().then(function(){
      msg(S.asking);
      return navigator.mediaDevices.getUserMedia({video: {facingMode: facing, width: {ideal: 640}, height: {ideal: 480}}, audio: false}).then(function(s){
        stream = s; video.srcObject = s; stage.classList.toggle('mir', facing === 'user');
        return video.play();
      }).then(function(){
        msg(''); CT.clear(); idle();
        cancelAnimationFrame(raf); raf = requestAnimationFrame(loop);
      }).catch(function(){ closeCam(); msg(S.denied); setPhase(S.ready, S.denied); });
    }, function(){ msg(S.failed); setPhase(S.ready, S.failed); })
    .then(function(){ $('cs-cam').disabled = false; buttons(); });
  }
  function closeCam(){
    cancelAnimationFrame(raf); raf = 0;
    if (stream){ stream.getTracks().forEach(function(t){ t.stop(); }); stream = null; }
    video.srcObject = null; cx.clearRect(0, 0, canvas.width, canvas.height); msg(S.idlemsg);
    if (phase !== 'idle'){ clearInterval(iv); }
    idle();
  }
  // ---------- olaylar
  function seg(id, fn){ $(id).addEventListener('click', function(e){ var b = e.target.closest('button'); if (!b) return; this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); fn(b.getAttribute('data-v')); }); }
  seg('cs-mode', function(v){ if (phase !== 'idle'){ clearInterval(iv); } mode = v; if (v === 'tap' && stream) closeCam(); paintCount(); paintTime(0); idle(); });
  seg('cs-sex', function(v){ sex = v; paintRes(); });
  $('cs-age').addEventListener('input', function(){ paintNorm(); paintRes(); });
  $('cs-cam').addEventListener('click', openCam);
  $('cs-off').addEventListener('click', closeCam);
  $('cs-flip').addEventListener('click', function(){ facing = facing === 'user' ? 'environment' : 'user'; if (stream){ stream.getTracks().forEach(function(t){ t.stop(); }); stream = null; } openCam(); });
  $('cs-go').addEventListener('click', function(){ if (phase === 'idle') start(); else { clearInterval(iv); paintTime(0); n = 0; paintCount(); idle(); } });
  $('cs-tap').addEventListener('pointerdown', function(e){ e.preventDefault(); count(); });
  $('cs-tap').addEventListener('keydown', function(e){ if (e.key === 'Enter' || e.key === ' '){ e.preventDefault(); count(); } });
  $('cs-minus').addEventListener('click', function(){ setLast(last - 1); });
  $('cs-plus').addEventListener('click', function(){ setLast(last + 1); });
  $('cs-num').addEventListener('input', function(){ var v = parseInt(this.value, 10); if (!isNaN(v)) setLast(v); });
  document.addEventListener('visibilitychange', function(){
    if (document.hidden){
      if (phase !== 'idle'){ clearInterval(iv); iv = null; phase = 'idle'; n = 0; paintCount(); paintTime(0); broke = true; }
      if (stream) closeCam();
      awake(false);
    } else if (broke){ broke = false; setPhase(S.broke, S.brokec); buttons(); }
  });
  window.addEventListener('pagehide', function(){ if (stream) stream.getTracks().forEach(function(t){ t.stop(); }); });
  window.__cs = {mk: mkCounter, get n(){ return n; }, get state(){ return CT.state; }, get phase(){ return phase; }, get fr(){ return fr; }, get deleg(){ return deleg; }, get tr(){ return tr; }};
  if (EN) $('cs-nt').querySelectorAll('td').forEach(function(td){ td.textContent = td.textContent.replace(/(\\d),(\\d)/g, '$1.$2'); });
  paintCount(); paintTime(0); paintNorm(); paintHist(); idle();
})();
</script>
'''

page("sandalye-testi.html", "30 Saniye Sandalye Testi",
     "30 saniyede bir sandalyeden kaç kez kalkabiliyorsunuz? Telefonunuzun kamerası tekrarları sizin yerinize saysın; sonucunuzu yaşınızdaki değerlerle karşılaştırın ve bacaklarınızı güçlendiren dört egzersizi öğrenin.",
     "sandalye-testi.html", SELF5_CSS, CS_BODY, CS_JS,
     seo_title="30 Saniye Sandalye Testi: Kameralı Otur-Kalk Sayacı ve Yaşa Göre Değerler | İhsan Eren",
     about={"@type": "MedicalTest", "name": "30 saniye sandalyeden kalkma testi"},
     faq_items=CS_FAQ)

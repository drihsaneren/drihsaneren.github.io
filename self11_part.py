# -*- coding: utf-8 -*-
# Kendine iyi bak, 11. tur: düştükten sonra yerden kalkma rehberi, günlük oturma süresi hesaplayıcısı.
# self10_part.py'den sonra exec edilir (SELF10_CSS hazır).
import json

SELF11_CSS = SELF10_CSS + """
  .gu{border:1px solid var(--line);border-radius:22px;padding:clamp(18px,3vw,30px);background:rgba(18,26,16,.45)}
  .gu-q{font-family:var(--display);font-size:clamp(22px,2.6vw,28px);line-height:1.3;margin:6px 0 14px;color:var(--ink)}
  .gu-acts{display:flex;flex-wrap:wrap;gap:10px;margin-top:14px}
  .gu-step{display:grid;grid-template-columns:minmax(0,220px) minmax(0,1fr);gap:clamp(16px,3vw,32px);align-items:center}
  .gu-step figure{margin:0}.gu-step figure svg{max-width:220px}
  .gu-step h3{font-family:var(--display);font-weight:400;font-size:clamp(22px,2.4vw,27px);margin:4px 0 8px;color:var(--ink)}
  .gu-step p{margin:0;font-size:16.5px;line-height:1.55;color:var(--ink-soft)}
  @media (max-width:640px){.gu-step{grid-template-columns:1fr}.gu-step figure svg{max-width:180px;margin:0 auto}}
  .gu-dots{display:flex;gap:6px;margin:14px 0 0}
  .gu-dots i{flex:1;height:5px;border-radius:999px;background:rgba(236,229,207,.12)}
  .gu-dots i.on{background:var(--foil)}
  .gu ol.steps{margin-top:6px}
  .gu .lbl{margin:0}
  .st-row{margin-top:14px}
  .st-row .lbl{display:flex;justify-content:space-between;align-items:baseline;gap:10px}
  .st-row .lbl b{font-family:var(--display);font-weight:400;font-size:24px;color:var(--ink);font-variant-numeric:tabular-nums}
  .st-row input[type=range]{width:100%;accent-color:var(--foil);margin:8px 0 0;height:28px}
  .st-tab{width:100%;border-collapse:separate;border-spacing:4px;margin-top:8px;font-size:13px}
  .st-tab th{font-weight:500;color:var(--muted);text-align:center;padding:4px 2px}
  .st-tab th[scope=row]{text-align:left;white-space:nowrap}
  .st-tab td{text-align:center;border-radius:8px;padding:9px 2px;font-variant-numeric:tabular-nums;color:var(--ink);background:rgba(236,229,207,.05)}
  .st-tab td.h1{background:rgba(216,178,94,.14)}.st-tab td.h2{background:rgba(226,171,71,.26)}.st-tab td.h3{background:rgba(201,107,90,.38)}
  .st-tab td.me{outline:2px solid var(--foil);outline-offset:1px;font-weight:700}
  .st-big{font-family:var(--display);font-size:clamp(46px,6vw,64px);line-height:1;color:var(--ink);font-variant-numeric:tabular-nums}
  .st-big small{font-size:18px;color:var(--muted)}
"""

# ------------------------------------------------------------------ 1 · DÜŞTÜKTEN SONRA KALKMA
_CH = '<path class="obj" d="M78 78 H110 M80 78 V112 M108 78 V112 M108 78 V46"/>'
GU_FIGS = [
 fig(GRD + '<circle class="hd" cx="16" cy="98" r="7"/><path class="fig" d="M24 102 L62 104"/><path class="fig hl" d="M62 104 L80 94 L96 108"/>'
     '<path class="fig" d="M30 102 L44 96"/><path d="M40 82 A16 16 0 0 1 64 84" fill="none" stroke="#C8963E" stroke-width="2.5" stroke-dasharray="3 4" stroke-linecap="round"/>', "Yana dönme"),
 fig(GRD + '<circle class="hd" cx="28" cy="62" r="7"/><path class="fig hl" d="M36 66 L74 70"/><path class="fig" d="M40 68 L40 110 M74 70 L74 110 L98 110"/>', "Eller ve dizler"),
 fig(GRD + _CH + f'<g>{anim_t("-20 0;6 0;-20 0", dur="4s")}<circle class="hd" cx="28" cy="62" r="7"/><path class="fig hl" d="M36 66 L66 70"/><path class="fig" d="M40 68 L40 110 M66 70 L66 110 L86 110"/></g>', "Mobilyaya emekleme"),
 fig(GRD + _CH + '<circle class="hd" cx="64" cy="40" r="7"/><path class="fig" d="M62 48 L56 80 L56 110 L32 110"/><path class="fig hl" d="M60 56 L86 76"/>', "Elleri mobilyaya koyma"),
 fig(GRD + _CH + '<circle class="hd" cx="66" cy="40" r="7"/><path class="fig" d="M64 48 L54 80 L46 110 L26 110"/><path class="fig hl" d="M54 80 L74 86 L74 112"/><path class="fig" d="M62 56 L88 76"/>', "Güçlü bacağı öne alma"),
 fig(GRD + _CH + '<circle class="hd" cx="64" cy="20" r="7"/><path class="fig" d="M64 28 L62 70"/><path class="fig hl" d="M62 70 L58 112 M62 70 L68 112"/><path class="fig" d="M64 38 L86 60 L104 56"/>', "İterek doğrulma"),
 fig(GRD + CHAIR_L + '<path class="fig" d="M46 74 H80 V112"/><path class="fig hl" d="M46 74 L48 42"/><circle class="hd" cx="50" cy="33" r="8"/><path class="fig" d="M48 50 L62 64 L72 70"/>', "Dönüp oturma"),
 fig(GRD + CHAIR_L + '<path class="fig" d="M46 74 H80 V112"/><path class="fig" d="M46 74 L48 42"/><circle class="hd" cx="50" cy="33" r="8"/><path class="fig" d="M48 50 L60 44 L62 34"/><rect x="58" y="22" width="9" height="14" rx="2" fill="#C8963E"/>', "Dinlenip haber verme"),
]
GU_STEPS = [
 ("Yana dönün", "Acele etmeyin. Kendinizi hazır hissettiğinizde yan tarafınıza dönün."),
 ("Ellerinizin ve dizlerinizin üzerine gelin", "Kollarınızla iterek ellerinizin ve dizlerinizin üzerine yükselin."),
 ("Sağlam bir mobilyaya emekleyin", "Yakınınızda değilse sağlam bir sandalyeye, kanepeye, yatağa ya da merdivenin alt basamağına doğru emekleyin. Yorulursanız durup dinlenin."),
 ("Ellerinizi mobilyaya koyun", "İki elinizi mobilyanın oturma yerine ya da basamağa koyun ve destek alın."),
 ("Güçlü bacağınızı öne alın", "Daha güçlü bacağınızın dizini bükerek öne alın ve ayağınızı yere düz basın."),
 ("İterek doğrulun", "Öne eğilin, kollarınız ve bacaklarınızla iterek yavaşça ayağa kalkın; diğer ayağınızı da yanına getirin."),
 ("Yavaşça dönüp oturun", "Mobilyaya tutunarak yavaşça dönün ve oturun."),
 ("Dinlenin ve haber verin", "Bir süre oturup dinlenin. Sonra birine düştüğünüzü ve nasıl hissettiğinizi söyleyin."),
]
GU_STEP_HTML = "\n".join(
    f'''        <div class="gu-step" data-i="{i}"{"" if i == 0 else " hidden"}>
          {f}
          <div><p class="lbl gu-n"></p><h3>{t}</h3><p>{d}</p></div>
        </div>''' for i, (f, (t, d)) in enumerate(zip(GU_FIGS, GU_STEPS)))

GU_FAQ = [
 ("Düştükten sonra 112’yi aramak doğru mu?", "Evet. Başınızı, boynunuzu, sırtınızı ya da kalçanızı incitmiş olabileceğinizi düşünüyorsanız ya da kalkamıyorsanız 112’yi arayın. Düştükten sonra yardım istemekte bir sakınca yoktur."),
 ("Neden hemen kalkmamalıyım?", "Düşmenin şokuyla hızla kalkmaya çalışmak yeniden düşmenize ya da bir yaralanmanın kötüleşmesine yol açabilir. Önce sakin kalın, birkaç dakika olduğunuz yerde durun, bir yerinizin ağrıyıp ağrımadığını kontrol edin ve kalkıp kalkamayacağınızı düşünün."),
 ("Kalkamıyorsam neden hareket etmeliyim?", "Yandan yana yuvarlanmak, kollarınızı ve bacaklarınızı oynatmak sizi sıcak tutar, dolaşımı destekler, tutulmayı ve uzun süre aynı pozisyonda kalmaya bağlı bası yarası riskini azaltır."),
 ("Kalkmayı neden önceden öğrenmeliyim?", "İngiltere’nin ulusal sağlık kılavuzu NICE (2025), düşme riski olan kişilerle düştükten sonra ne yapacaklarının ve yerden nasıl kalkacaklarının konuşulmasını öneriyor. Adımları önceden, yanınızda biri varken denemek, gerçek bir düşmede ne yapacağınızı bilmenizi kolaylaştırır."),
 ("Kalktım ve iyiyim, yine de hekime gitmeli miyim?", "Evet, hekiminize düştüğünüzü söyleyin. Düşme değerlendirmesinde denge testleri yapılabilir, ilaçlarınız gözden geçirilebilir, göz muayenesi, kalp ritmi kaydı (EKG) ve yatarken ve ayaktayken tansiyon ölçümü istenebilir. Evinizdeki tehlikeler için bir sağlık profesyonelinin ziyareti ve kuvvet ve denge egzersizleri de önerilebilir."),
]

GU_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Düştükten sonra yerden kalkma</h1>
    <p class="lede">Düştüğünüzde ilk iş acele etmemek. Yaralanmadıysanız ve kendinizi hazır hissediyorsanız, kalkmanın güvenli bir yolu var; incindiyseniz ya da kalkamıyorsanız da yardım gelene kadar yapabilecekleriniz var. Bu rehber, NHS’in önerdiği adımları size soru sorarak ve resimlerle tek tek gösterir. Düşmeden önce bir kez okumanız, gerektiğinde ne yapacağınızı bilmenizi kolaylaştırır.</p>
    <p class="meta">Son güncelleme: 19 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>Önce durun</b><span>Sakin kalın, bir yerinizin incinip incinmediğini kontrol edin</span></div>
        <div class="stat"><b>8 adım</b><span>Yardımsız ve güvenle yerden kalkmanın adımları</span></div>
        <div class="stat"><b>112</b><span>Baş, boyun, sırt ya da kalçanızı incittiyseniz ya da kalkamıyorsanız</span></div>
        <div class="stat"><b>Sıcak tutun</b><span>Yardım beklerken üzerinizi örtün ve hareket edin</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Adım adım</p>
      <h2>Düştünüz: şimdi ne yapmalı?</h2>
      <div class="gu" id="gu">
        <div id="gu-start">
          <p class="lbl">Önce</p>
          <p class="gu-q">Acele etmeyin. Birkaç dakika olduğunuz yerde kalın, nefesinizi düzenleyin ve bir yerinizde ağrı olup olmadığını kontrol edin.</p>
          <p class="soft">Başınızı, boynunuzu, sırtınızı ya da kalçanızı incitmiş olabilir misiniz, ya da kalkamayacağınızı mı düşünüyorsunuz?</p>
          <div class="gu-acts">
            <button type="button" class="cta" data-go="help">Evet ya da emin değilim</button>
            <button type="button" class="cta ghost" data-go="up">Hayır, kalkabilecek gibiyim</button>
          </div>
        </div>
        <div id="gu-help" hidden>
          <p class="lbl">Kalkmaya çalışmayın</p>
          <p class="gu-q">Yardım çağırın ve sıcak kalın</p>
          <ol class="steps">
            <li><span><strong>Yardım çağırın:</strong> Evde biri varsa seslenin. Telefonunuz ya da acil durum alarmınız yakınınızdaysa kullanın; yoksa duvara, yere ya da kalorifere vurarak dikkat çekin.</span></li>
            <li><span><strong>112’yi arayın:</strong> Başınızı, boynunuzu, sırtınızı ya da kalçanızı incitmiş olabilirseniz ya da kalkamıyorsanız.</span></li>
            <li><span><strong>Sıcak kalın:</strong> Üzerinizi bir battaniye, havlu ya da sabahlıkla örtün, başınızın altına bir yastık koyun. Sert bir zemindeyseniz yapabiliyorsanız halıya geçin, cereyandan uzaklaşın.</span></li>
            <li><span><strong>Hareket edin:</strong> Yapabildiğiniz ölçüde yandan yana yuvarlanın, kollarınızı ve bacaklarınızı oynatın.</span></li>
            <li><span><strong>Su için:</strong> Yakınınızda bir içecek varsa yudumlayın.</span></li>
            <li><span><strong>Gerekirse tuvalet:</strong> Tuvaletiniz gelirse yapın, sonra ıslak yerden uzağa yuvarlanın.</span></li>
          </ol>
          <div class="gu-acts"><button type="button" class="cta ghost" data-go="start">Başa dön</button></div>
        </div>
        <div id="gu-up" hidden>
{GU_STEP_HTML}
          <div class="gu-dots" aria-hidden="true">{"".join("<i></i>" for _ in GU_STEPS)}</div>
          <div class="gu-acts">
            <button type="button" class="cta ghost" id="gu-prev">Geri</button>
            <button type="button" class="cta" id="gu-next">Sonraki adım</button>
            <button type="button" class="cta ghost" data-go="help">Bu adımda zorlanıyorum</button>
          </div>
        </div>
        <div id="gu-done" hidden>
          <p class="lbl">Kalktınız</p>
          <p class="gu-q">Bir süre dinlenin ve düştüğünüzü hekiminize söyleyin</p>
          <p class="soft">Kendinizi iyi hissetseniz bile bir düşme değerlendirmesi, yeni düşmeleri önlemenize yardım eder. Düşme riskinizi şimdi <a href="dusme-riski-testi.html">12 soruluk düşme riski testiyle</a> değerlendirebilirsiniz.</p>
          <div class="gu-acts"><button type="button" class="cta ghost" data-go="start">Başa dön</button></div>
        </div>
        <div class="gu-strings" hidden><span data-k="n">{{n}}. adım / {len(GU_STEPS)}</span><span data-k="next">Sonraki adım</span><span data-k="fin">Bitir</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Önceden hazırlanın</h2>
        <ul class="dots">
          <li>Evde yalnız yaşıyorsanız telefonunuzu ya da acil durum alarmınızı yanınızda taşıyın.</li>
          <li>Bu adımları sağlıklıyken, yanınızda biri varken ve tercihen bir fizyoterapistle birlikte deneyin.</li>
          <li>Bacak gücünüzü ve dengenizi korumak, hem düşmeleri önler hem de yerden kalkmayı kolaylaştırır.</li>
        </ul>
      </div>
      <div>
        <h2>Bir de ölçerek bakın</h2>
        <ul class="dots">
          <li><a href="otur-kalk-testi.html">Yere oturup kalkabiliyor musunuz?</a>: yerden kalkma becerinizi sınayın.</li>
          <li><a href="dort-asamali-denge-testi.html">4 aşamalı denge testi</a>: duruş dengenizi ölçün.</li>
          <li><a href="dusme-onleme.html">Düşmeleri önleme ve denge</a>: altı denge egzersizi ve ev güvenliği.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(GU_FAQ)}
      {CTA_CARD("Yerden kalkma, denge ve düşme riskiniz", "yerden kalkma ve düşme önleme çalışması")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Guy’s and St Thomas’ NHS Foundation Trust. " + ext("https://guysandstthomas.nhs.uk/health-information/falls/what-do-if-you-fall", "What to do if you fall") + ". Resource 5320/VER2, last reviewed July 2026.",
        "nidirect (Northern Ireland). " + ext("https://www.nidirect.gov.uk/conditions/falls", "Falls") + ". Last modified 3 March 2026.",
        "Torbay and South Devon NHS Foundation Trust. " + ext("https://www.torbayandsouthdevon.nhs.uk/services/falls-fracture-prevention-bone-health/what-to-do-if-a-fall-occurs", "What to do if a fall occurs") + ".",
        "NICE. " + ext("https://www.nice.org.uk/guidance/ng249", "Falls: assessment and prevention in older people and in people 50 and over at higher risk") + ". NICE guideline NG249, 29 April 2025.",
      ])}
    </div>
  </section>
</main>'''

GU_JS = '''<script>
(function(){
  var g = document.getElementById('gu'); if (!g) return;
  var S = {}; g.querySelectorAll('.gu-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var $ = function(id){ return document.getElementById(id); }, steps = [].slice.call(g.querySelectorAll('.gu-step')), dots = [].slice.call(g.querySelectorAll('.gu-dots i')), i = 0;
  function view(v){ ['start', 'help', 'up', 'done'].forEach(function(k){ $('gu-' + k).hidden = k !== v; }); if (v === 'up') { i = 0; step(); } g.scrollIntoView({block: 'start', behavior: 'smooth'}); }
  function step(){
    steps.forEach(function(s, k){ s.hidden = k !== i; s.querySelector('.gu-n').textContent = S.n.replace('{n}', k + 1); });
    dots.forEach(function(d, k){ d.classList.toggle('on', k <= i); });
    $('gu-prev').disabled = i === 0; $('gu-next').textContent = i === steps.length - 1 ? S.fin : S.next;
  }
  g.addEventListener('click', function(e){ var b = e.target.closest('[data-go]'); if (b) view(b.getAttribute('data-go')); });
  $('gu-next').addEventListener('click', function(){ if (i < steps.length - 1) { i++; step(); } else view('done'); });
  $('gu-prev').addEventListener('click', function(){ if (i > 0) { i--; step(); } });
  window.__gu = {st: function(){ return [['start', 'help', 'up', 'done'].filter(function(k){ return !$('gu-' + k).hidden; })[0], i]; }};
})();
</script>
'''

page("dustukten-sonra-kalkma.html", "Düştükten Sonra Yerden Kalkma",
     "Düştüğünüzde ne yapmalısınız? İncindiyseniz ya da kalkamıyorsanız yardım beklerken yapılacaklar, yaralanmadıysanız 8 adımda güvenle yerden kalkma. Resimli, adım adım rehber.",
     "dustukten-sonra-kalkma.html", SELF11_CSS, GU_BODY, GU_JS,
     seo_title="Düştükten Sonra Yerden Nasıl Kalkılır? Adım Adım Rehber | İhsan Eren",
     about={"@type": "HowTo", "name": "Düştükten sonra yerden kalkma"},
     faq_items=GU_FAQ)

# ------------------------------------------------------------------ 2 · OTURMA SÜRESİ HESAPLAYICISI
# Ekelund ve ark. Lancet 2016, Tablo 2 (oturma) ve Tablo 3 (TV): her hareket grubunda, en az oturanlara göre tehlike oranı
ST_SIT = {"q1": [1, 1.08, 1.09, 1.27], "q2": [1, 1.04, 1.06, 1.12], "q3": [1, 1.05, 1.03, 1.10], "q4": [1, 1.00, 1.01, 1.04]}
ST_SIG = {"q1": [0, 1, 1, 1], "q2": [0, 0, 1, 1], "q3": [0, 1, 0, 1], "q4": [0, 0, 0, 0]}
ST_TV = {"q1": [1, 1.00, 1.10, 1.44], "q2": [1, 1.00, 1.08, 1.29], "q3": [1, 1.08, 1.17, 1.41], "q4": [1, 0.96, None, 1.15]}
ST_TVSIG = {"q1": [0, 0, 1, 1], "q2": [0, 0, 1, 1], "q3": [0, 0, 1, 1], "q4": [0, 0, 0, 1]}
ST_Q = [("q4", "Günde 60–75 dk ve üzeri"), ("q3", "Günde yaklaşık 50–65 dk"), ("q2", "Günde yaklaşık 25–35 dk"), ("q1", "Günde yaklaşık 5 dk")]
ST_COLS = ["4 saatten az", "4–6 saat", "6–8 saat", "8 saatten fazla"]
def _st_cell(v, sig):
    pct = round((v - 1) * 100)
    cls = "" if not sig else ("h1" if pct < 8 else "h2" if pct < 15 else "h3")
    return cls, pct
ST_ROWS = "\n".join(
    f'<tr data-q="{q}"><th scope="row">{lab}</th>' + "".join(
        (lambda c, t: f'<td data-c="{k}" data-p="{t}" class="{c}"></td>')(*_st_cell(ST_SIT[q][k], ST_SIG[q][k])) for k in range(4)) + "</tr>"
    for q, lab in ST_Q)

ST_FAQ = [
 ("Bu sonuçlar ne kadar güvenilir?", "Hesaplayıcı, 16 çalışmadan bir milyondan fazla yetişkinin verisini aynı yöntemle yeniden analiz eden ve The Lancet’te yayımlanan bir meta-analize dayanıyor. Ancak bunlar gözlem çalışmaları: oturmanın ya da hareketsizliğin ölüme yol açtığını kanıtlamıyor. Oturma ve hareket süreleri çoğunlukla kişilerin kendi beyanıyla ölçüldü; katılımcıların çoğu 45 yaş üzerindeydi ve Batı Avrupa, ABD ya da Avustralya’da yaşıyordu. Sonuçları kişisel bir risk hesabı olarak değil, genel bir yol gösterici olarak okuyun."),
 ("Orta tempolu hareket ne demek?", "Araştırmada orta yoğunluk, örneğin saatte yaklaşık 5,6 km hızla tempolu yürümek ya da saatte 16 km hızla bisiklet sürmek gibi etkinliklerdi. Dakikada yaklaşık 100 adımlık bir yürüyüş de orta yoğunluğa karşılık gelir."),
 ("Neden televizyon ayrıca soruluyor?", "Aynı araştırmada televizyon izleme süresi ayrıca incelendi. Günde 3 saat ve üzeri televizyon izlemek, en hareketli grup dışında daha yüksek riskle ilişkiliydi; günde 5 saat ve üzeri izlemek ise en hareketli grupta bile riskte artışla ilişkiliydi."),
 ("Hareket ölçerle yapılan araştırmalar ne gösteriyor?", "Hareket ölçer takan 44.000’den fazla orta yaşlı ve yaşlı yetişkinin verisini birleştiren 2020 tarihli bir meta-analizde, günde yaklaşık 30–40 dakika orta ya da yüksek yoğunlukta hareket, uzun oturmayla ilişkili ölüm riskindeki artışı azaltıyordu; bu süre, kişilerin kendi beyanına dayanan önceki tahminlerden kısaydı. Dünya Sağlık Örgütü de 2020 kılavuzunda oturma süresini azaltmayı ve yerine hangi yoğunlukta olursa olsun hareket koymayı öneriyor; çok oturanların önerilen hareket miktarının üzerine çıkmaya çalışmasını tavsiye ediyor."),
 ("Günde 60 dakikaya nasıl ulaşırım?", "Bu hareketin tek seferde yapılması gerekmez. Örneğin işe giderken 20 dakika tempolu yürüyüş, öğle arasında 15 dakika ve akşam 25 dakika yürüyüş ya da bisiklet. Uzun oturmaları sık sık bölmek de önerilir; mola zamanlayıcısı ve tempolu yürüyüş metronomu yardımcı olabilir."),
]

ST_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Günlük oturma süresi hesaplayıcısı</h1>
    <p class="lede">Günde kaç saat oturuyorsunuz? Bir milyondan fazla kişinin verisini inceleyen büyük bir araştırma, uzun oturmanın sağlık üzerindeki olumsuz etkisinin, ne kadar hareket ettiğinize göre çok değiştiğini gösterdi: günde 60–75 dakika orta tempolu hareket edenlerde, günde 8 saatten fazla oturmak bile ölüm riskinde belirgin bir artışla ilişkili değildi. Oturma ve hareket sürelerinizi girin, araştırmada sizinkine benzer gruptaki kişilerde ne bulunduğunu görün.</p>
    <p class="meta">Son güncelleme: 19 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>1 milyon</b><span>16 çalışmada incelenen yetişkin sayısı</span></div>
        <div class="stat"><b>60–75 dk</b><span>Bu kadar orta tempolu hareket edenlerde uzun oturma, ölüm riskinde belirgin bir artışla ilişkili değildi</span></div>
        <div class="stat"><b>%59</b><span>En az hareket edip günde 8 saatten fazla oturanlarda, en hareketli ve en az oturanlara göre ölüm riski artışı</span></div>
        <div class="stat"><b>4’te 3</b><span>Katılımcılardan günde 60–75 dakikaya ulaşamayanların oranı</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Kendinizi ölçün</p>
      <h2>Oturma ve hareket dengeniz</h2>
      <p class="soft">İş, yolculuk, yemek ve ekran başında geçen tüm oturma sürenizi düşünün. Hareket için yalnızca nefesinizi hızlandıran tempolu yürüyüş, bisiklet gibi etkinlikleri sayın.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <div class="st-row"><p class="lbl"><span>Günde oturarak geçen süre</span><b><span id="st-sv">8</span> sa</b></p>
              <input type="range" id="st-sit" min="0" max="16" step="0.5" value="8" aria-label="Günde oturarak geçen süre (saat)"></div>
            <div class="st-row"><p class="lbl"><span>Günde orta tempolu hareket</span><b><span id="st-mv">20</span> dk</b></p>
              <input type="range" id="st-mov" min="0" max="120" step="5" value="20" aria-label="Günde orta tempolu hareket (dakika)"></div>
            <p class="lbl" style="margin-top:16px">Günde televizyon izleme</p>
            <div class="seg" role="group" aria-label="Günde televizyon izleme" id="st-tv">
              <button type="button" data-v="0" aria-pressed="true">1 saatten az</button>
              <button type="button" data-v="1" aria-pressed="false">1–2 saat</button>
              <button type="button" data-v="2" aria-pressed="false">3–4 saat</button>
              <button type="button" data-v="3" aria-pressed="false">5 saat ve üzeri</button>
            </div>
          </div>
          <div class="bt-out">
            <p class="lbl">Araştırmada, aynı hareket grubunda en az oturanlara (4 saatten az) göre ölüm riskindeki fark</p>
            <table class="st-tab" id="st-tab">
              <thead><tr><th scope="col"></th>{"".join(f'<th scope="col">{c}</th>' for c in ST_COLS)}</tr></thead>
              <tbody>
{ST_ROWS}
              </tbody>
            </table>
            <p class="count" style="margin-top:8px">Renkli kutular istatistiksel olarak anlamlı farkları gösterir. Çerçeveli kutu sizin grubunuz. Girdiğiniz hareket süresi, araştırmadaki dört gruptan size en yakın olanla yaklaşık olarak eşleştirilir.</p>
          </div>
          <div class="bt-run">
            <p class="lbl" id="st-grp"></p>
            <p class="st-big" id="st-big">–</p>
            <p class="bt-cue" id="st-txt"></p>
            <p class="bt-cue" id="st-tvtxt"></p>
            <p class="bt-cue" id="st-gap"></p>
          </div>
        </div>
        <div class="st-strings" hidden>
          <span data-k="q1">Hareket grubunuz: en az hareket edenler (günde yaklaşık 5 dakika)</span>
          <span data-k="q2">Hareket grubunuz: günde yaklaşık 25–35 dakika</span>
          <span data-k="q3">Hareket grubunuz: günde yaklaşık 50–65 dakika</span>
          <span data-k="q4">Hareket grubunuz: en hareketliler (günde 60–75 dakika ve üzeri)</span>
          <span data-k="ref">Bu grupta en az oturanlarla aynı düzeydesiniz.</span>
          <span data-k="sig">Sizinkine benzer hareket düzeyindeki kişilerde bu kadar oturmak, 4 saatten az oturmaya göre ölüm riskinde yaklaşık %{{p}} artışla ilişkiliydi.</span>
          <span data-k="ns">Sizinkine benzer hareket düzeyindeki kişilerde bu kadar oturmak, ölüm riskinde istatistiksel olarak anlamlı bir artışla ilişkili değildi.</span>
          <span data-k="tv0">Günde 1 saatten az televizyon izlemek, karşılaştırmanın temel alındığı gruptur.</span>
          <span data-k="tvs">Televizyon: aynı hareket grubunda günde 1 saatten az izleyenlere göre ölüm riskinde yaklaşık %{{p}} artış.</span>
          <span data-k="tvn">Televizyon: aynı hareket grubunda belirgin bir fark görülmedi.</span>
          <span data-k="gap">Günde 60 dakikaya ulaşmak için {{m}} dakika daha orta tempolu hareket gerekiyor.</span>
          <span data-k="ok">Günlük hareket süreniz, uzun oturmanın etkisini dengeleyen düzeyde.</span>
          <span data-k="none">Fark yok</span>
        </div>
      </div>
      <p class="count">Girdiğiniz değerler hiçbir yere gönderilmez ve kaydedilmez.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Oturmayı nasıl azaltırım?</h2>
        <ul class="dots">
          <li>Uzun oturmaları sık sık bölün: her yarım saatte birkaç dakika kalkıp yürüyün.</li>
          <li>Telefonla konuşurken ayağa kalkın ya da yürüyün.</li>
          <li>Kısa mesafeleri yürüyerek ya da bisikletle gidin.</li>
          <li>Televizyon izlerken reklam aralarında kalkın.</li>
        </ul>
      </div>
      <div>
        <h2>Yardımcı araçlar</h2>
        <ul class="dots">
          <li><a href="mola-zamanlayicisi.html">Masa başı mola zamanlayıcısı</a>: oturma molalarınızı hatırlatır.</li>
          <li><a href="tempolu-yuruyus.html">Tempolu yürüyüş metronomu</a>: yürüyüşünüzü orta tempoya taşır.</li>
          <li><a href="hareket.html">Ne kadar hareket?</a>: haftalık hareketinizi önerilerle karşılaştırın.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(ST_FAQ)}
      {CTA_CARD("Daha hareketli bir gün planı", "oturma süremi azaltma ve kişiye özel hareket programı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Ekelund U, Steene-Johannessen J, Brown WJ, et al. " + ext("https://doi.org/10.1016/S0140-6736(16)30370-1", "Does physical activity attenuate, or even eliminate, the detrimental association of sitting time with mortality? A harmonised meta-analysis of data from more than 1 million men and women") + ". Lancet. 2016;388(10051):1302–1310.",
        "Ekelund U, Tarp J, Fagerland MW, et al. " + ext("https://bjsm.bmj.com/content/54/24/1499", "Joint associations of accelerometer-measured physical activity and sedentary time with all-cause mortality: a harmonised meta-analysis in more than 44 000 middle-aged and older individuals") + ". Br J Sports Med. 2020;54(24):1499–1506.",
        "Bull FC, Al-Ansari SS, Biddle S, et al. " + ext("https://bjsm.bmj.com/content/54/24/1451", "World Health Organization 2020 guidelines on physical activity and sedentary behaviour") + ". Br J Sports Med. 2020;54(24):1451–1462.",
        "MRC Epidemiology Unit, University of Cambridge. " + ext("https://www.epi.ims.cam.ac.uk/blog/2016/07/28/hour-moderate-exercise-day-enough-counter-health-risks-prolonged-sitting/", "An hour of moderate exercise a day enough to counter health risks from prolonged sitting") + ". 28 July 2016.",
      ])}
    </div>
  </section>
</main>'''

ST_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.st-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var $ = function(id){ return document.getElementById(id); }, EN = document.documentElement.lang === 'en';
  var SIT = ''' + json.dumps(ST_SIT) + ''', SIG = ''' + json.dumps(ST_SIG) + ''', TV = ''' + json.dumps(ST_TV) + ''', TVS = ''' + json.dumps(ST_TVSIG) + ''';
  function fmt(x){ var s = String(x); return EN ? s : s.replace('.', ','); }
  function pc(p){ return p === 0 ? '–' : (p > 0 ? '+' : '−') + (EN ? Math.abs(p) + '%' : '%' + Math.abs(p)); }
  $('st-tab').querySelectorAll('td').forEach(function(td){ td.textContent = pc(+td.getAttribute('data-p')); });
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function paint(){
    var h = +$('st-sit').value, m = +$('st-mov').value, tv = +$('st-tv').querySelector('[aria-pressed="true"]').getAttribute('data-v');
    $('st-sv').textContent = fmt(h); $('st-mv').textContent = String(m);
    var q = m < 15 ? 'q1' : m < 45 ? 'q2' : m < 60 ? 'q3' : 'q4', c = h < 4 ? 0 : h < 6 ? 1 : h <= 8 ? 2 : 3;
    $('st-tab').querySelectorAll('td').forEach(function(td){ td.classList.toggle('me', td.parentNode.getAttribute('data-q') === q && +td.getAttribute('data-c') === c); });
    var v = SIT[q][c], p = Math.round((v - 1) * 100);
    $('st-grp').textContent = S[q];
    $('st-big').textContent = c === 0 ? '–' : SIG[q][c] ? pc(p) : S.none;
    $('st-txt').textContent = c === 0 ? S.ref : SIG[q][c] ? fill(S.sig, {p: p}) : S.ns;
    var t = TV[q][tv];
    $('st-tvtxt').textContent = tv === 0 ? S.tv0 : TVS[q][tv] ? fill(S.tvs, {p: Math.round((t - 1) * 100)}) : S.tvn;
    $('st-gap').textContent = m >= 60 ? S.ok : fill(S.gap, {m: 60 - m});
  }
  $('st-sit').addEventListener('input', paint); $('st-mov').addEventListener('input', paint);
  $('st-tv').addEventListener('click', function(e){
    var b = e.target.closest('button'); if (!b) return;
    this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); paint();
  });
  paint();
})();
</script>
'''

page("oturma-suresi.html", "Günlük Oturma Süresi Hesaplayıcısı",
     "Günde kaç saat oturuyorsunuz, ne kadar hareket ediyorsunuz? Bir milyondan fazla kişiyi inceleyen araştırmaya göre oturma ve hareket dengenizi görün; günde 60–75 dakikanın önemi.",
     "oturma-suresi.html", SELF11_CSS, ST_BODY, ST_JS,
     seo_title="Oturma Süresi Hesaplayıcısı: Günde Kaç Saat Oturuyorsunuz? | İhsan Eren",
     about={"@type": "MedicalRiskCalculator", "name": "Oturma süresi ve hareket dengesi"},
     faq_items=ST_FAQ)

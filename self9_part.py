# -*- coding: utf-8 -*-
# Kendine iyi bak, 9. tur: düşme riski öz değerlendirmesi (CDC STEADI "Stay Independent"), 4 aşamalı denge testi (CDC STEADI).
# self8_part.py'den sonra exec edilir (SELF8_CSS, WAKE_JS, cs_sts, cs_heel hazır).

SELF9_CSS = SELF8_CSS + """
  .fq{display:grid;gap:10px;margin:6px 0 0;padding:0}
  .fq li{list-style:none;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:12px;align-items:center;padding:12px 14px;border:1px solid var(--line);border-radius:14px;background:rgba(236,229,207,.03)}
  .fq li p{margin:0;font-size:15.5px;line-height:1.45;color:var(--ink)}
  .fq li p small{display:block;font-size:12.5px;color:var(--muted);margin-top:3px}
  .fq li .seg{margin:0;flex-wrap:nowrap}
  .fq li.y{border-color:rgba(216,178,94,.55);background:rgba(216,178,94,.08)}
  @media (max-width:560px){.fq li{grid-template-columns:1fr}}
  .fr-sum{position:sticky;top:76px;padding:18px;border:1px solid var(--line);border-radius:18px;background:rgba(18,26,16,.6)}
  .fr-sc{font-family:var(--display);font-size:64px;line-height:1;color:var(--ink);font-variant-numeric:tabular-nums}
  .fr-sc span{font-size:22px;color:var(--muted)}
  .fr-why{margin:10px 0 0;padding-left:18px;font-size:14px;line-height:1.5;color:var(--ink-soft)}
  .fr-why li{margin:4px 0}
  .fr-grid{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr);gap:clamp(16px,3vw,32px);align-items:start}
  @media (max-width:860px){.fr-grid{grid-template-columns:1fr}.fr-sum{position:static}}
  .ft{width:150px;height:150px;display:block;margin:0 auto 6px}
  .ft .fo{fill:#8fa476}.ft .fo.g{fill:none;stroke:rgba(236,229,207,.35);stroke-width:2;stroke-dasharray:5 4}
  .st4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;margin:12px 0 0}
  .st4 div{border:1px solid var(--line);border-radius:12px;padding:10px 6px;text-align:center;font-size:12px;color:var(--muted)}
  .st4 b{display:block;font-family:var(--display);font-weight:400;font-size:22px;color:var(--ink);font-variant-numeric:tabular-nums}
  .st4 div.on{border-color:var(--foil);background:rgba(216,178,94,.1)}
  .st4 div.ok b{color:var(--sage)}.st4 div.no b{color:#e07a5f}
"""

# ------------------------------------------------------------------ 1 · DÜŞME RİSKİ ÖZ DEĞERLENDİRMESİ
FR_Q = [
 (2, "Son bir yıl içinde düştüm.", "Bir kez düşen kişilerin yeniden düşme olasılığı yüksektir."),
 (2, "Güvenle dolaşabilmek için baston ya da yürüteç kullanıyorum ya da kullanmam önerildi.", "Baston ya da yürüteç kullanması önerilen kişilerin düşme olasılığı zaten daha yüksek olabilir."),
 (1, "Yürürken bazen dengemi kaybedecek gibi oluyorum.", "Yürürken sendeleme ya da desteğe ihtiyaç duyma, zayıf dengenin işaretidir."),
 (1, "Evde yürürken eşyalara tutunarak dengemi sağlıyorum.", "Bu da zayıf dengenin bir işaretidir."),
 (1, "Düşmekten endişe ediyorum.", "Düşmekten endişe eden kişilerin düşme olasılığı daha yüksektir."),
 (1, "Sandalyeden kalkmak için ellerimle itmem gerekiyor.", "Bacak kaslarının zayıfladığını gösterir; bu, düşmelerin başlıca nedenlerinden biridir."),
 (1, "Kaldırıma çıkmakta biraz zorlanıyorum.", "Bu da bacak kaslarının zayıflığının bir işaretidir."),
 (1, "Sık sık tuvalete yetişmek için acele etmem gerekiyor.", "Özellikle gece tuvalete acele etmek düşme olasılığını artırır."),
 (1, "Ayaklarımda his kaybı var.", "Ayaklardaki uyuşukluk tökezlemeye ve düşmelere yol açabilir."),
 (1, "Bazen başımı döndüren ya da beni olağandan yorgun hissettiren bir ilaç kullanıyorum.", "İlaçların yan etkileri bazen düşme olasılığını artırabilir."),
 (1, "Uykuma ya da ruh hâlime yardımcı olan bir ilaç kullanıyorum.", "Bu ilaçlar bazen düşme olasılığını artırabilir."),
 (1, "Sık sık kendimi üzgün ya da çökkün hissediyorum.", "Halsizlik ya da yavaşlamış hissetme gibi depresyon belirtileri düşmelerle ilişkilidir."),
]
FR_LIST = "\n".join(
    f'''            <li data-p="{p}"><p>{q}<small>{p} puan</small></p><div class="seg" role="group" aria-label="{q}"><button type="button" data-v="1" aria-pressed="false">Evet</button><button type="button" data-v="0" aria-pressed="false">Hayır</button></div><span class="why" hidden>{w}</span></li>'''
    for p, q, w in FR_Q)

FR_FAQ = [
 ("Bu test ne kadar güvenilir?", "Bu soru listesi ABD’de bir gaziler hastanesinin yaşlı sağlığı merkezinde geliştirildi ve yaşlılarda düşme riskini öz değerlendirme için doğrulandı. ABD Hastalık Kontrol ve Önleme Merkezleri (CDC), bu listeyi düşmeleri önleme programında kullanıyor. Bir tanı aracı değildir; sonucunuzu hekiminizle konuşmanız için bir başlangıç noktasıdır."),
 ("Bu liste düşüp düşmeyeceğimi kesin olarak söyler mi?", "Hayır. İngiltere’nin ulusal sağlık kılavuzu NICE (2025), düşme riskini tahmin etmek için tek başına bir soru listesi ya da puanlama aracı kullanılmamasını öneriyor; 2022 tarihli Dünya Düşme Kılavuzu da değerlendirmeye son 12 ayda düşüp düşmediğinizi sorarak başlıyor. Bu yüzden son bir yılda düştüyseniz, puanınız ne olursa olsun bunu hekiminize söyleyin. Birden fazla kez düştüyseniz, düşmede yaralandıysanız, bilincinizi kaybettiyseniz ya da yerden yardımsız kalkamadıysanız kapsamlı bir düşme değerlendirmesi isteyebilirsiniz."),
 ("Puanım 4’ün altında, içim rahat olabilir mi?", "Düşük puan düşme riskinizin hiç olmadığı anlamına gelmez. Bacak gücünüzü ve dengenizi korumak için hareketli kalmanız ve bu soruları yılda bir yeniden yanıtlamanız iyi olur."),
 ("Puanım yüksek çıktı, ne yapabilirim?", "Sonucunuzu hekiminizle konuşun; kullandığınız ilaçları, görmenizi ve ayaklarınızı gözden geçirmek isteyebilir. Güç ve denge egzersizleri düşmeleri önlemenin en etkili yollarından biridir. Bir fizyoterapist size özel bir program hazırlayabilir. 108 çalışmayı kapsayan Cochrane derlemesinde egzersiz, toplumda yaşayan yaşlılarda düşme sıklığını %23 azalttı. ABD'de 22 aile hekimliği muayenehanesinde düşme riski taşıyan yaklaşık 12 bin yaşlıyla yapılan 2026 tarihli bir çalışmada, elektronik hasta kaydı üzerinden önerilen kısa ev egzersizleri kayıtlara geçen düşmeleri %9 azalttı."),
]

FR_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Düşme riskinizi değerlendirin</h1>
    <p class="lede">On iki kısa soruya “evet” ya da “hayır” deyin, düşme riskinizi bir dakikada öğrenin. Bu soru listesini ABD Hastalık Kontrol ve Önleme Merkezleri (CDC) yaşlılarda düşmeleri önleme programında kullanıyor. 4 puan ve üzeri, düşme riskiniz olabileceğini gösterir. Sonucunuzu hekiminizle ya da fizyoterapistinizle paylaşabilirsiniz.</p>
    <p class="meta">Son güncelleme: 24 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>12 soru</b><span>Her biri düşmelerle ilişkili bir etkeni yokluyor</span></div>
        <div class="stat"><b>4 puan</b><span>Bu puan ve üzeri, düşme riski olabileceğini gösterir</span></div>
        <div class="stat"><b>2 puan</b><span>Son bir yılda düşmüş olmak ve baston ya da yürüteç kullanmak</span></div>
        <div class="stat"><b>1 dakika</b><span>Soruları yanıtlamak için gereken yaklaşık süre</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Kendinizi ölçün</p>
      <h2>Soruları yanıtlayın</h2>
      <p class="soft">Her cümle için size uyuyorsa “Evet”, uymuyorsa “Hayır”ı seçin.</p>
      <div class="fr-grid">
        <ol class="fq" id="fq">
{FR_LIST}
        </ol>
        <div class="fr-sum">
          <p class="lbl">Puanınız</p>
          <p class="fr-sc"><b id="fr-n">0</b><span> / 14</span></p>
          <p class="nb-max" id="fr-left"></p>
          <div class="res" id="fr-res" hidden>
            <p class="lab" id="fr-lab"></p>
            <p id="fr-txt"></p>
            <ul class="fr-why" id="fr-why"></ul>
            <span class="bt-badge" id="fr-badge"></span>
            <div class="cs-acts"><a class="cta" id="fr-wa" href="#" target="_blank" rel="noopener">Sonucumu WhatsApp’tan gönder</a></div>
          </div>
        </div>
      </div>
      <div class="fr-strings" hidden>
        <span data-k="left">Yanıtlanmayan soru: {{n}}</span>
        <span data-k="done">Tüm soruları yanıtladınız.</span>
        <span data-k="hi">Düşme riskiniz olabilir</span>
        <span data-k="lo">4 puanın altındasınız</span>
        <span data-k="hit">4 puan ve üzeri, düşme riskiniz olabileceğini gösterir. Sonucunuzu hekiminizle konuşun. “Evet” dediğiniz maddelerin neden önemli olduğu:</span>
        <span data-k="lot">Bu, düşme riskinizin hiç olmadığı anlamına gelmez. Hareketli kalın, bacak gücünüzü ve dengenizi koruyun.</span>
        <span data-k="bhi">Hekiminizle konuşun</span>
        <span data-k="blo">4 puanın altında</span>
        <span data-k="wa">Merhaba, drihsaneren.com’daki düşme riski öz değerlendirmesinde {{s}} puan aldım. Değerlendirme hakkında bilgi almak istiyorum.</span>
      </div>
      <p class="count">Yanıtlarınız hiçbir yere gönderilmez ve kaydedilmez.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Düşmeleri önlemek için</h2>
        <ul class="dots">
          <li>Bacak gücü ve denge egzersizlerini düzenli yapın.</li>
          <li>Kullandığınız ilaçları hekiminizle gözden geçirin.</li>
          <li>Gözlerinizi düzenli muayene ettirin, ayaklarınıza ve ayakkabılarınıza dikkat edin.</li>
          <li>Evinizdeki tehlikeleri azaltın: takılabileceğiniz halılar, kablolar, karanlık koridorlar.</li>
        </ul>
        <p class="soft">Ayrıntılar için <a href="dusme-onleme.html">düşmeleri önleme</a> rehberine bakabilirsiniz.</p>
      </div>
      <div>
        <h2>Bir de ölçerek bakın</h2>
        <ul class="dots">
          <li><a href="dort-asamali-denge-testi.html">4 aşamalı denge testi</a>: duruş dengenizi dört adımda ölçün.</li>
          <li><a href="kalk-yuru-testi.html">Kalk ve yürü testi</a>: kalkma, yürüme ve dönme sürenizi ölçün.</li>
          <li><a href="sandalye-testi.html">30 saniye sandalye testi</a>: bacak gücünüzü ölçün.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(FR_FAQ)}
      {CTA_CARD("Düşme riskiniz, dengeniz ve bacak gücünüz", "düşme riski ve denge değerlendirmesi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Centers for Disease Control and Prevention (STEADI). " + ext("https://www.cdc.gov/steadi/pdf/steadi-brochure-stayindependent-508.pdf", "Stay Independent: check your risk for falling") + ". 2023. Türkçe çeviri sitemize aittir.",
        "eSTEPS: JAMA Netw Open. 2026. doi:10.1001/jamanetworkopen.2026.39240. Özet: " + ext("https://www.utmb.edu/scoa/news-and-events/archive/2026/10/19/study-finds-electronic-health-record-tool-can-help-reduce-falls-among-older-adults", "UTMB, 19 October 2026") + ".",
        "Sherrington C, Fairhall NJ, Wallbank GK, et al. " + ext("https://www.cochrane.org/evidence/CD012424", "Exercise for preventing falls in older people living in the community") + ". Cochrane Database Syst Rev. 2019;(1):CD012424.",
        "Rubenstein LZ, Vivrette R, Harker JO, Stevens JA, Kramer BJ. Validating an evidence-based, self-rated fall risk questionnaire (FRQ) for older adults. J Safety Res. 2011;42(6):493–499.",
        "NICE. " + ext("https://www.nice.org.uk/guidance/ng249", "Falls: assessment and prevention in older people and in people 50 and over at higher risk") + ". NICE guideline NG249, 29 April 2025.",
        "Montero-Odasso M, van der Velde N, Martin FC, et al. " + ext("https://doi.org/10.1093/ageing/afac205", "World guidelines for falls prevention and management for older adults: a global initiative") + ". Age Ageing. 2022;51(9):afac205.",
      ])}
    </div>
  </section>
</main>'''

FR_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.fr-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var $ = function(id){ return document.getElementById(id); }, WA = 'https://wa.me/905538815568?text=';
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  var items = [].slice.call(root.querySelectorAll('#fq li'));
  function paint(){
    var sc = 0, left = 0, why = [];
    items.forEach(function(li){
      var v = li.getAttribute('data-a');
      if (v === null) left++;
      else if (v === '1'){ sc += +li.getAttribute('data-p'); why.push(li.querySelector('.why').textContent); }
      li.classList.toggle('y', v === '1');
    });
    $('fr-n').textContent = String(sc);
    $('fr-left').textContent = left ? fill(S.left, {n: left}) : S.done;
    var res = $('fr-res'), hi = sc >= 4;
    res.hidden = left > 0 && !hi;
    if (res.hidden) return;
    $('fr-lab').textContent = hi ? S.hi : S.lo;
    $('fr-txt').textContent = hi ? S.hit : S.lot;
    var ul = $('fr-why'); ul.innerHTML = '';
    if (hi) why.forEach(function(w){ var li = document.createElement('li'); li.textContent = w; ul.appendChild(li); });
    var b = $('fr-badge'); b.textContent = hi ? S.bhi : S.blo; b.classList.toggle('no', hi);
    $('fr-wa').href = WA + encodeURIComponent(fill(S.wa, {s: sc}));
  }
  items.forEach(function(li){
    li.querySelector('.seg').addEventListener('click', function(e){
      var b = e.target.closest('button'); if (!b) return;
      this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      li.setAttribute('data-a', b.getAttribute('data-v')); paint();
    });
  });
  paint();
})();
</script>
'''

page("dusme-riski-testi.html", "Düşme Riskinizi Değerlendirin",
     "On iki soruya evet ya da hayır deyin, düşme riskinizi bir dakikada öğrenin. CDC’nin yaşlılarda kullandığı öz değerlendirme listesi, puanlama ve düşmeleri önleme önerileri.",
     "dusme-riski-testi.html", SELF9_CSS, FR_BODY, FR_JS,
     seo_title="Düşme Riski Testi: 12 Soruluk Öz Değerlendirme (CDC) | İhsan Eren",
     about={"@type": "MedicalTest", "name": "Düşme riski öz değerlendirmesi"},
     faq_items=FR_FAQ)

# ------------------------------------------------------------------ 2 · 4 AŞAMALI DENGE TESTİ
def _foot(x, y, ghost=False):
    c = "fo g" if ghost else "fo"
    return (f'<path class="{c}" d="M{x} {y + 12} q0 -12 10 -12 q10 0 10 14 q0 18 -4 30 q-3 10 -6 10 q-6 0 -8 -10 q-3 -14 -2 -32 z"/>'
            + ("" if ghost else f'<circle class="fo" cx="{x + 3}" cy="{y - 4}" r="2.6"/><circle class="fo" cx="{x + 9}" cy="{y - 6}" r="2.6"/><circle class="fo" cx="{x + 15}" cy="{y - 4}" r="2.4"/>'))
B4_FEET = [
    _foot(52, 52) + _foot(78, 52),
    _foot(60, 70) + _foot(78, 32),
    _foot(65, 92) + _foot(65, 32),
    _foot(65, 52) + _foot(92, 40, True),
]
B4_SVG = "".join(f'<svg class="ft" viewBox="0 0 150 150" data-s="{i}" aria-hidden="true"{"" if i == 0 else " hidden"}>{f}</svg>' for i, f in enumerate(B4_FEET))
B4_NAMES = ["Ayaklar yan yana", "Yarı tandem", "Tandem duruş", "Tek ayak"]
B4_DESC = ["İki ayağınızı yan yana, birbirine değecek şekilde koyun.",
           "Bir ayağınızın iç kenarını, öbür ayağınızın başparmağına değecek şekilde biraz öne alın.",
           "Bir ayağınızı tam öbürünün önüne koyun; öndeki ayağın topuğu arkadakinin parmaklarına değsin.",
           "Bir ayağınızın üzerinde durun."]

B4_FAQ = [
 ("Neden tandem duruş bu kadar önemli?", "ABD Hastalık Kontrol ve Önleme Merkezleri (CDC), tandem duruşu (bir ayak tam öbürünün önünde) en az 10 saniye koruyamayan yaşlıların düşme riskinin arttığını belirtiyor. Bu durumda denge ve yürüyüş egzersizleri için bir fizyoterapiste ya da tai chi gibi kanıtlanmış bir düşme önleme programına yönlendirme öneriliyor. Dengeniz zayıf çıktıysa, bu testteki duruşları da içeren Otago gibi ev programları düşmeleri azaltabiliyor: 7 çalışmanın analizinde düşmeler %32 azaldı."),
 ("Bu test düşüp düşmeyeceğimi kesin olarak söyler mi?", "Hayır. İngiltere’nin ulusal sağlık kılavuzu NICE (2025), düşme riskini tahmin etmek için tek başına bir test ya da puanlama aracı kullanılmamasını öneriyor; bu tür testler yürüme ve denge sorunlarını fark etmeye yardım eder. Bu yüzden son bir yılda düştüyseniz, sonucunuz ne olursa olsun bunu hekiminize söyleyin. Birden fazla kez düştüyseniz, düşmede yaralandıysanız, bilincinizi kaybettiyseniz ya da yerden yardımsız kalkamadıysanız kapsamlı bir düşme değerlendirmesi isteyebilirsiniz."),
 ("Ayaklarımı oynatırsam ne olur?", "Ayaklarınız yer değiştirirse ya da bir yere tutunmak zorunda kalırsanız o aşamada süre durur ve test biter. Kollarınızı açabilir, gövdenizi oynatabilirsiniz; yalnızca ayaklarınız yerinde kalmalı."),
 ("Tek ayak aşamasını geçemedim, sorun mu?", "Tek ayak üzerinde durmak dördünün en zorudur. Yaşınıza göre karşılaştırma için <a href=\"denge-testi.html\">10 saniye denge testi</a> sayfamıza bakabilirsiniz."),
]

B4_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>4 aşamalı denge testi</h1>
    <p class="lede">Ayakta dururken dengeniz ne kadar sağlam? Bu testte giderek zorlaşan dört duruşta 10’ar saniye kalmaya çalışırsınız. ABD Hastalık Kontrol ve Önleme Merkezleri (CDC), yaşlılarda düşme riskini değerlendirirken bu testi kullanıyor: üçüncü aşamadaki tandem duruşu 10 saniye koruyamamak, düşme riskinin arttığını gösteriyor. Yanınızda biriyle, aşağıdaki süreölçerle deneyin.</p>
    <p class="meta">Son güncelleme: 18 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>4 duruş</b><span>Her biri öncekinden daha zor</span></div>
        <div class="stat"><b>10 saniye</b><span>Her duruşta kalınması gereken süre</span></div>
        <div class="stat"><b>3. aşama</b><span>Tandem duruşu 10 saniye koruyamamak, düşme riski işareti</span></div>
        <div class="stat"><b>Gözler açık</b><span>Baston ya da yürüteç kullanmadan</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Kendinizi ölçün</p>
      <h2>Süreölçerle deneyin</h2>
      <p class="soft">Bir duvarın ya da tezgâhın yanında durun, yanınızdaki kişi gerektiğinde sizi tutabilecek mesafede olsun. Pozisyona yerleşip dengenizi bulunca süreyi başlatın.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <p class="lbl" id="b4-step">1. aşama</p>
            {B4_SVG}
            <p class="lab" id="b4-name" style="text-align:center;margin:0">{B4_NAMES[0]}</p>
            <p class="soft" id="b4-desc" style="text-align:center;margin-top:6px">{B4_DESC[0]}</p>
          </div>
          <div class="bt-out">
            <div class="st4" id="b4-st">{"".join(f'<div data-i="{i}"{" class=on" if i == 0 else ""}><b>–</b>{n}</div>' for i, n in enumerate(B4_NAMES))}</div>
            <div class="res" id="b4-res" hidden>
              <p class="lab" id="b4-lab"></p>
              <p id="b4-txt"></p>
              <span class="bt-badge" id="b4-badge"></span>
              <div class="cs-acts"><a class="cta" id="b4-wa" href="#" target="_blank" rel="noopener">Sonucumu WhatsApp’tan gönder</a></div>
            </div>
          </div>
          <div class="bt-run">
            <div class="yh-time"><b id="b4-sec">0,0</b><span>saniye</span></div>
            <p class="bt-phase" id="b4-phase" aria-live="polite">Hazır</p>
            <p class="bt-cue" id="b4-cue">Pozisyona yerleşin, dengenizi bulunca başlatın.</p>
            <button type="button" class="bt-tap" id="b4-go">Başla</button>
            <div class="controls" style="margin-top:10px;justify-content:center">
              <button type="button" class="cta ghost" id="b4-reset">Baştan başla</button>
            </div>
            <label class="mz-chk" style="justify-content:center"><input type="checkbox" id="b4-sound" checked> Sesli uyarı</label>
          </div>
        </div>
        <div class="b4-strings" hidden>
          {"".join(f'<span data-k="n{i}">{n}</span><span data-k="d{i}">{d}</span>' for i, (n, d) in enumerate(zip(B4_NAMES, B4_DESC)))}
          <span data-k="step">{{n}}. aşama</span>
          <span data-k="ready">Hazır</span>
          <span data-k="readyc">Pozisyona yerleşin, dengenizi bulunca başlatın.</span>
          <span data-k="run">Dengede kalın</span>
          <span data-k="runc">Ayaklarınız oynarsa ya da tutunursanız hemen “Ayak oynadı”ya basın.</span>
          <span data-k="start">Başla</span>
          <span data-k="stop">Ayak oynadı</span>
          <span data-k="pass">Aşama tamam</span>
          <span data-k="passc">Bir sonraki duruşa geçin; hazır olunca başlatın.</span>
          <span data-k="end">Test bitti</span>
          <span data-k="endc">Sonucunuz aşağıda.</span>
          <span data-k="lall">Dört aşamayı da tamamladınız</span>
          <span data-k="lt">Tandem duruşu 10 saniye korudunuz</span>
          <span data-k="lrisk">Tandem duruşu 10 saniye koruyamadınız</span>
          <span data-k="tall">Dengeniz bu testte iyi görünüyor. Dengenizi korumak için hareketli kalın.</span>
          <span data-k="tt">Tandem duruşu 10 saniye korumanız, bu testin düşme riski eşiğini geçtiğiniz anlamına gelir. Tek ayak üzerinde denge çalışmasına devam edebilirsiniz.</span>
          <span data-k="trisk">CDC’ye göre tandem duruşu en az 10 saniye koruyamayan yaşlıların düşme riski artmıştır. Bu bir tanı değildir; denge ve yürüyüş egzersizleri için bir fizyoterapistle konuşabilirsiniz.</span>
          <span data-k="bok">Düşme riski eşiğinin üzerinde</span>
          <span data-k="bno">Değerlendirme önerilir</span>
          <span data-k="wa">Merhaba, drihsaneren.com’daki 4 aşamalı denge testini yaptım: {{r}}. Değerlendirme hakkında bilgi almak istiyorum.</span>
          <span data-k="sec">sn</span>
        </div>
      </div>
      <p class="count">Sonuçlarınız hiçbir yere gönderilmez.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nasıl yapılır?</h2>
        <ol class="steps">
          {"".join(f'<li><span><strong>{n}:</strong> {d}</span></li>' for n, d in zip(B4_NAMES, B4_DESC))}
        </ol>
        <p class="soft">Her duruşta 10 saniye kalabildiyseniz bir sonrakine geçin; kalamadıysanız test orada biter.</p>
      </div>
      <div>
        <h2>Güvenle yapmak için</h2>
        <ul class="dots">
          <li>Yanınızda biri dursun; ilk anda kolunuzdan tutup pozisyona yerleşmenize yardım edebilir.</li>
          <li>Baston ya da yürüteç kullanmayın, gözleriniz açık olsun.</li>
          <li>Kollarınızı açabilir, gövdenizi oynatabilirsiniz; ayaklarınızı oynatmayın.</li>
          <li>Bir duvarın ya da tezgâhın yanında yapın; başınız dönerse hemen tutunun.</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Dengenizi geliştirin</p>
      <h2>Evde dört egzersiz</h2>
      <p class="soft">Ayrıntılı öneriler için <a href="dusme-onleme.html">düşmeleri önleme</a> rehberine, düşme riskinizi soru listesiyle değerlendirmek için <a href="dusme-riski-testi.html">düşme riski testine</a> bakabilirsiniz.</p>
      {ex_grid(["tandem", "sls", "cs_heel", "cs_sts"], "ex four")}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(B4_FAQ)}
      {CTA_CARD("Dengeniz ve düşme riskiniz", "4 aşamalı denge testi ve denge değerlendirmesi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Centers for Disease Control and Prevention (STEADI). " + ext("https://www.cdc.gov/steadi/media/pdfs/STEADI-Assessment-4Stage-508.pdf", "Assessment: The 4-Stage Balance Test") + ". 2017.",
        "NICE. " + ext("https://www.nice.org.uk/guidance/ng249", "Falls: assessment and prevention in older people and in people 50 and over at higher risk") + ". NICE guideline NG249, 29 April 2025.",
        "Montero-Odasso M, van der Velde N, Martin FC, et al. " + ext("https://doi.org/10.1093/ageing/afac205", "World guidelines for falls prevention and management for older adults: a global initiative") + ". Age Ageing. 2022;51(9):afac205.",
        "Sherrington C, Fairhall NJ, Wallbank GK, et al. " + ext("https://www.cochrane.org/evidence/CD012424_exercise-preventing-falls-older-people-living-community", "Exercise for preventing falls in older people living in the community") + ". Cochrane Database Syst Rev. 2019;1:CD012424.",
        "Thomas S, Mackintosh S, Halbert J. " + ext("https://academic.oup.com/ageing/article/39/6/681/9467", "Does the ‘Otago exercise programme’ reduce mortality and falls in older adults? A systematic review and meta-analysis") + ". Age Ageing. 2010;39(6):681–687.",
      ])}
    </div>
  </section>
</main>'''

B4_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.b4-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var EN = document.documentElement.lang === 'en';
  var $ = function(id){ return document.getElementById(id); }, WA = 'https://wa.me/905538815568?text=';
  var stage = 0, times = [null, null, null, null], phase = 'idle', t0 = 0, iv = null, lock = null, ctx = null, snd = $('b4-sound');
''' + WAKE_JS + '''
  function fmt(x){ var s = x.toFixed(1); return EN ? s : s.replace('.', ','); }
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function paintStage(){
    root.querySelectorAll('svg.ft').forEach(function(s){ s.toggleAttribute('hidden', +s.getAttribute('data-s') !== stage); });
    $('b4-step').textContent = fill(S.step, {n: stage + 1});
    $('b4-name').textContent = S['n' + stage]; $('b4-desc').textContent = S['d' + stage];
    $('b4-st').querySelectorAll('div').forEach(function(d, i){
      var t = times[i]; d.querySelector('b').textContent = t == null ? '–' : fmt(t);
      d.classList.toggle('on', i === stage && phase !== 'end'); d.classList.toggle('ok', t != null && t >= 10); d.classList.toggle('no', t != null && t < 10);
    });
  }
  function result(){
    var res = $('b4-res'); res.hidden = false;
    var t3 = times[2], all = times[3] != null && times[3] >= 10, risk = t3 == null || t3 < 10;
    $('b4-lab').textContent = all ? S.lall : risk ? S.lrisk : S.lt;
    $('b4-txt').textContent = all ? S.tall : risk ? S.trisk : S.tt;
    var b = $('b4-badge'); b.textContent = risk ? S.bno : S.bok; b.classList.toggle('no', risk);
    var r = times.map(function(t, i){ return t == null ? null : S['n' + i] + ' ' + fmt(t) + ' ' + S.sec; }).filter(Boolean).join(', ');
    $('b4-wa').href = WA + encodeURIComponent(fill(S.wa, {r: r}));
  }
  function idle(p, c, label){
    clearInterval(iv); iv = null; wake(false);
    $('b4-go').textContent = label || S.start; $('b4-go').classList.remove('stop'); $('b4-go').hidden = phase === 'end';
    $('b4-phase').textContent = p || S.ready; $('b4-cue').textContent = c || S.readyc;
  }
  function finish(t){
    times[stage] = Math.min(10, Math.round(t * 10) / 10);
    $('b4-sec').textContent = fmt(times[stage]);
    if (times[stage] >= 10 && stage < 3){ beep(880, .35, .2); stage++; phase = 'idle'; paintStage(); idle(S.pass, S.passc); }
    else { beep(times[stage] >= 10 ? 880 : 440, .45, .2); phase = 'end'; paintStage(); idle(S.end, S.endc); result(); }
  }
  function tick(){
    var t = (performance.now() - t0) / 1000;
    if (t >= 10){ clearInterval(iv); iv = null; finish(10); return; }
    $('b4-sec').textContent = fmt(t);
  }
  $('b4-go').addEventListener('click', function(){
    if (phase === 'end') return;
    if (phase === 'idle'){
      phase = 'run'; t0 = performance.now(); $('b4-sec').textContent = fmt(0); wake(true); beep(660, .2, .18);
      $('b4-go').textContent = S.stop; $('b4-go').classList.add('stop');
      $('b4-phase').textContent = S.run; $('b4-cue').textContent = S.runc;
      clearInterval(iv); iv = setInterval(tick, 50);
    } else { clearInterval(iv); iv = null; finish((performance.now() - t0) / 1000); }
  });
  $('b4-reset').addEventListener('click', function(){
    clearInterval(iv); iv = null; stage = 0; times = [null, null, null, null]; phase = 'idle';
    $('b4-res').hidden = true; $('b4-sec').textContent = fmt(0); paintStage(); idle();
  });
  document.addEventListener('visibilitychange', function(){ if (document.hidden && phase === 'run'){ clearInterval(iv); iv = null; phase = 'idle'; $('b4-sec').textContent = fmt(0); idle(); } });
  $('b4-sec').textContent = fmt(0); paintStage(); idle();
  window.__b4 = {st: function(){ return [phase, stage, times.slice()]; }};
})();
</script>
'''

page("dort-asamali-denge-testi.html", "4 Aşamalı Denge Testi",
     "Giderek zorlaşan dört duruşta 10’ar saniye kalabiliyor musunuz? CDC’nin düşme riskini değerlendirmek için kullandığı 4 aşamalı denge testini süreölçerle yapın.",
     "dort-asamali-denge-testi.html", SELF9_CSS, B4_BODY, B4_JS,
     seo_title="4 Aşamalı Denge Testi: Süreölçer ve Düşme Riski Eşiği (CDC) | İhsan Eren",
     about={"@type": "MedicalTest", "name": "4 aşamalı denge testi"},
     faq_items=B4_FAQ)

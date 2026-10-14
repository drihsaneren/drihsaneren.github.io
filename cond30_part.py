# -*- coding: utf-8 -*-
# Yeni rehber (30): Kürek kemiği arası ağrı (sırt ağrısı). cond29_part.py'den sonra exec edilir. Video yok.
# İki yeni çizim: oturarak gövde döndürme ve duvarda yana eğilme; diğerleri hazır anahtarlar.

SV["ub_trot"] = fig(GRD +
    '<path class="obj" d="M40 84 H80 M42 84 V112 M78 84 V112"/>'
    '<path class="fig" d="M60 40 V82 M52 84 L50 112 M68 84 L70 112 M60 32 V40"/>'
    f'<path class="fig hl" d="M44 40 H76 M44 40 L56 56 L72 44 M76 40 L64 56 L48 44">'
    f'{anim_d("M44 40 H76 M44 40 L56 56 L72 44 M76 40 L64 56 L48 44;M50 40 H72 M50 40 L59 56 L70 44 M72 40 L63 56 L52 44;M44 40 H76 M44 40 L56 56 L72 44 M76 40 L64 56 L48 44;M48 40 H70 M48 40 L57 56 L68 44 M70 40 L61 56 L50 44;M44 40 H76 M44 40 L56 56 L72 44 M76 40 L64 56 L48 44", dur="4.8s", kt="0;0.25;0.5;0.75;1")}</path>'
    '<circle class="hd" cx="60" cy="22" r="9"/>'
    f'<g>{anim_t("0 0;-4 0;0 0;4 0;0 0", dur="4.8s", kt="0;0.25;0.5;0.75;1")}'
    '<circle cx="56" cy="20" r="1.5" fill="#efe9d6"/><circle cx="64" cy="20" r="1.5" fill="#efe9d6"/></g>'
    '<path d="M36 64 Q60 76 84 64 M40 61 L36 64 L40 68 M80 61 L84 64 L80 68" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "Oturarak gövde döndürme")

SV["ub_sbend"] = fig(GRD +
    '<rect x="30" y="4" width="60" height="108" rx="3" fill="rgba(185,203,198,.28)"/>'
    f'<path class="fig" d="{LEGS_F}"/>'
    f'<g>{anim_t("0 60 80;-18 60 80;0 60 80;18 60 80;0 60 80", dur="5.6s", kt="0;0.25;0.5;0.75;1", typ="rotate")}'
    '<path class="fig hl" d="M60 80 V40"/><path class="fig" d="M46 40 H74 M46 40 L42 62 L44 78 M74 40 L78 62 L76 78 M60 32 V40"/>'
    '<circle class="hd" cx="60" cy="23" r="8"/></g>',
    "Duvarda yana eğilme")

EXT["ub_trot"] = ("Oturarak gövde döndürme", "Sandalyeye dik oturun, ayaklarınız yere bassın, kollarınızı göğsünüzde çapraz yapın. Kalçanızı oynatmadan gövdenizi yavaşça sağa çevirin, rahat olan son noktada 2–3 saniye bekleyin, sonra aynı şekilde sola çevirin.", "Her yöne 10–20 tekrar, günde 2–3 kez")
EXT["ub_sbend"] = ("Duvarda yana eğilme", "Sırtınızı duvara verin, ayaklarınız kalça genişliğinde açık olsun. Sırtınızı duvardan ayırmadan gövdenizi yavaşça yana eğin; eliniz bacağınızın yanından aşağı kaysın. Gövdenizin yanında hafif bir gerginlik hissedin, doğrulup öbür yana geçin.", "Her yana 10 tekrar, günde 2–3 kez")

UB_FAQ = [
 ("Kürek kemiklerimin arasındaki ağrı kalpten olabilir mi?", "Nadiren olabilir. Kalp krizinde ağrı genellikle göğüste sıkışma ya da baskı şeklindedir; kola, boyuna ve çeneye yayılabilir, nefes darlığı, terleme ve bulantı eşlik edebilir. Aniden başlayan, yırtılır gibi çok şiddetli göğüs ya da sırt ağrısı ise ana atardamarın (aort) yırtılmasının belirtisi olabilir. Bu belirtilerde beklemeden 112’yi arayın. Hareketle ve pozisyonla değişen ağrı daha çok kas ve eklemlerden kaynaklanır, ama bu tek başına kalbi dışlamaz."),
 ("Ağrı boyundan gelebilir mi?", "Evet. Boyundaki bir sinir kökü sıkıştığında kürek kemiği bölgesinde ağrı sık görülür ve bazen kol ağrısından haftalar önce başlayabilir. Kola yayılan ağrı, uyuşma ya da güçsüzlük varsa boyun fıtığı rehberine bakabilir, bir hekime ya da fizyoterapiste başvurabilirsiniz."),
 ("Ne kadar sürer?", "Göğüs omurgası güçlü bir yapıdır ve çoğu kişi basit önlemlerle iyileşir. Şikâyetler birkaç hafta, bazen birkaç ay sürebilir. Hareketli kalmak ve egzersizleri düzenli yapmak iyileşmeyi destekler."),
 ("Çocuğumun sırtı ağrıyor, çantadan mı?", "Olabilir, ama tek neden olmayabilir. Araştırmalarda sırt ağrısı çocuk ve gençlerde, özellikle kızlarda, yetişkinlerden daha sık bildirilmiş; sırt çantası kullanımı ilişkili bulunan etkenlerden biri. Stres, uyku ve hareket alışkanlıkları gibi etkenlere de bakmak gerekir. Ağrı geçmiyorsa ya da uyarı işaretleri varsa çocuğunuzu bir hekime gösterebilirsiniz."),
]

UB_SRC = [
 "Berkshire Healthcare NHS Foundation Trust. " + ext("https://www.berkshirehealthcare.nhs.uk/advice/mid-back-pain", "Mid-back pain") + ". Self-care advice, version 1, February 2026.",
 "Briggs AM, Smith AJ, Straker LM, Bragge P. " + ext("https://doaj.org/article/e56a433d4c66476f902b286d1093b8d4", "Thoracic spine pain in the general population: prevalence, incidence and associated factors in children, adolescents and adults. A systematic review") + ". BMC Musculoskeletal Disorders. 2009;10:77.",
 "Carmichael J, Weber KA, Rubinstein S, Svoboda E, Bade M. " + ext("https://pure.amsterdamumc.nl/en/publications/scapular-pain-in-cervical-radiculopathy-a-scoping-review/", "Scapular pain in cervical radiculopathy: a scoping review") + ". North American Spine Society Journal. 2025;23:100619.",
 "NHS. " + ext("https://www.nhs.uk/conditions/heart-attack/symptoms/", "Symptoms of a heart attack") + ". Page last reviewed 31 March 2026.",
 "HSE. " + ext("https://www.hse.ie/conditions/aortic-dissection/symptoms-of-aortic-dissection", "Symptoms of aortic dissection") + ".",
]

UB_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Kürek kemiği arası ağrı (sırt ağrısı)</h1>
    <p class="lede">Kürek kemiklerinin arasında ya da sırtın ortasında hissedilen sızı, yanma ya da batma çok sık görülür. Göğüs omurgası güçlü bir yapıdır ve çoğu kişi basit önlemler ve düzenli hareketle iyileşir. Yine de bu bölgeye boyundan ve nadiren kalp gibi iç organlardan ağrı yansıyabildiği için, hangi belirtilerde beklememek gerektiğini bilmek önemlidir.</p>
    <p class="meta">Son güncelleme: 14 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%16–20</b><span>Yetişkinlerde yaşam boyu görülme oranı; çalışmalar arasında farklar büyük</span></div>
        <div class="stat"><b>Gençlerde daha sık</b><span>Çocuk ve gençlerde, özellikle kızlarda, yetişkinlerden daha sık bildirilmiş</span></div>
        <div class="stat"><b>Haftalar – aylar</b><span>Şikâyetlerin sürebileceği zaman; çoğu kişi basit önlemlerle iyileşir</span></div>
        <div class="stat"><b>Günde 2–3 kez</b><span>Önerilen egzersiz sıklığı, her harekette 10–20 tekrar</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Kürek kemiklerinin arasında sızı ya da batma.</li>
          <li>Dönerken ya da sabah uyandığınızda tutukluk.</li>
          <li>Sırt kaslarında gerginlik ya da kasılma.</li>
          <li>Bir şey kaldırırken, uzanırken ya da uzun süre otururken artan ağrı.</li>
          <li>Kaburgalara ya da göğüs duvarına yayılan ağrı.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li><b>Kaslar ve eklemler:</b> En sık neden budur. Ağrı hareketle, dönmekle ve pozisyonla değişir.</li>
          <li><b>Boyun:</b> Boyundaki bir sinir kökü sıkıştığında ağrı kürek kemiği bölgesine yansıyabilir.</li>
          <li><b>İlişkili etkenler:</b> Araştırmalarda başka kas ve eklem ağrıları, sırt çantası, duruş, stres ve yaşam tarzı ilişkili bulunmuş; ama bunların hepsi kesin neden değildir.</li>
          <li><b>Nadiren iç organlar:</b> Kalp ve ana atardamar (aort) gibi organlardan da bu bölgeye ağrı yansıyabilir.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Hareketli kalın</h3><p>Göğüs omurgası güçlüdür. Ağrının izin verdiği ölçüde günlük işlerinize devam etmek iyileşmeyi destekler.</p></div>
        <div class="kind"><span class="n">2</span><h3>Pozisyon değiştirin</h3><p>Uzun süre oturmak ağrıyı artırabilir. Masa başında sık sık kalkıp birkaç adım atabilir, omuzlarınızı gevşetebilirsiniz.</p></div>
        <div class="kind"><span class="n">3</span><h3>Düzenli egzersiz</h3><p>Aşağıdaki hareketleri 10–20 tekrar, günde 2–3 kez yapabilirsiniz. Hafif bir gerginlik normaldir, ağrıyı zorlamayın.</p></div>
        <div class="kind"><span class="n">4</span><h3>Nefes ve gevşeme</h3><p>Stres sırt kaslarını gerebilir. Yavaş nefes ve gevşeme için <a href="uc-kapi.html">Üç Kapı</a> ya da <a href="kas-gevsetme.html">kas gevşetme</a> sayfasını deneyebilirsiniz.</p></div>
      </div>
      <p class="soft" style="margin-top:18px">Masa başında çalışıyorsanız <a href="masa-basi.html">masa başı rehberine</a>, duruşunuz öne doğruysa <a href="kambur-durus.html">kambur duruş rehberine</a> de bakabilirsiniz.</p>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Sırtı açan altı egzersiz</h2>
      <p class="soft">Hareketleri yavaş ve kontrollü, ağrısız bir aralıkta yapın. Göğüste sıkışma, nefes darlığı ya da yeni bir uyuşma olursa egzersizi bırakın.</p>
      {ex_grid(["cat", "ub_trot", "thor", "ub_sbend", "scap", "row"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(UB_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Acil: göğüste sıkışma ya da baskı, kola, boyuna ya da çeneye yayılan ağrı, nefes darlığı, terleme ya da bulantı varsa hemen 112’yi arayın</li>
        <li>Acil: aniden başlayan, yırtılır gibi çok şiddetli göğüs ya da sırt ağrısında hemen 112’yi arayın</li>
        <li>Acil: iki bacakta güçsüzlük, uyuşma ya da karıncalanma, yürümede zorluk, apış arasında uyuşma, idrar ya da dışkı kontrolünde sorun varsa</li>
        <li>Açıklanamayan kilo kaybı, geçmeyen şiddetli ağrı, gece ağrısı ya da kendinizi hasta hissediyorsanız</li>
        <li>Kola yayılan ağrı, uyuşma ya da güçsüzlük varsa (<a href="boyun-fitigi.html">boyun fıtığı</a> rehberine bakabilirsiniz)</li>
      </ul>
      {CTA_CARD("Sırt ağrınız", "kürek kemiği arası ağrı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(UB_SRC)}
    </div>
  </section>
</main>'''

page("kurek-kemigi-arasi-agri.html", "Kürek Kemiği Arası Ağrı",
     "Kürek kemiklerinin arasında ağrı neden olur, ne zaman tehlikelidir? Boyundan ve kalpten gelen ağrıyı ayırmaya yardımcı uyarı işaretleri, iyi gelenler ve evde altı egzersiz.",
     "kurek-kemigi-arasi-agri.html", NECK_CSS, UB_BODY, "",
     seo_title="Kürek Kemiği Arası Ağrı (Sırt Ağrısı): Nedenleri, Uyarı İşaretleri ve Egzersizler | İhsan Eren",
     condition="Kürek kemiği arası ağrı (torakal sırt ağrısı)", faq_items=UB_FAQ)

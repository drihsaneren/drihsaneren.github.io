# -*- coding: utf-8 -*-
# Yeni rehber (41): El ve parmak kireçlenmesi (el osteoartriti). cond40_part.py'den sonra exec edilir. Video yok.
# Egzersizler NHS el terapisi broşürlerindeki hareketlere göre, hazır çizimlerle.

_ex2("ho_fist", "tglide", "Yumruk yapıp açma", "Parmaklarınızı nazikçe tamamen düzeltip açın, sonra yavaşça yumruk yapın. Yumruğu sıkmanız gerekmez; amaç parmak eklemlerini tüm açıklığında hareket ettirmektir.", "5–10 tekrar, günde 2–3 kez")
_ex2("ho_opp", "thumb", "Başparmakla parmak uçlarına dokunma", "Başparmağınızın ucuyla sırayla her parmağınızın ucuna dokunun, sonra elinizi açıp başparmağınızı olabildiğince dışarı açın. Hareket başparmağın bilek tarafındaki kökünden gelsin.", "5–10 tur, günde 2–3 kez")
_ex2("ho_web", "thumb", "Başparmak arasını esnetme", "Elinizi önce ısıtın. Diğer elinizle başparmak ile işaret parmağı arasındaki kası nazikçe ovun; yapabiliyorsanız bu sırada başparmağınızı işaret parmağından uzaklaştırın.", "30 saniye, 2–3 kez")
_ex2("ho_grip", "grip", "Topu hafifçe sıkma", "Bir tenis topunu ya da yumuşak bir topu başparmağınız ve parmaklarınızla hafifçe kavrayın. Nazikçe sıkın, sonra gevşetin. Ağrı artıyorsa daha yumuşak bir nesne seçin.", "10 tekrar, günde 1–2 kez")
_ex2("ho_wrist", "dq_wrist", "Bileği aşağı yukarı hareket ettirme", "Ön kolunuzu masaya koyun, eliniz masanın kenarından taşsın. Bileğinizi rahatça yapabildiğiniz kadar yukarı kaldırın, sonra aşağı indirin.", "10 tekrar, günde 2–3 kez")
_ex2("ho_rot", "ge_rot", "Ön kolu çevirme", "Ön kolunuz masada dursun. Avucunuzu yukarı, sonra aşağı bakacak şekilde yavaşça çevirin.", "10 tekrar, günde 2–3 kez")

HO_FAQ = [
 ("Parmaklarımdaki sert şişlikler nedir?", "Parmak ucuna yakın eklemlerdeki sert, boğumlu şişliklere Heberden nodülü, orta eklemlerdekilere Bouchard nodülü denir. El kireçlenmesinin tipik bulgularıdır."),
 ("Egzersiz gerçekten işe yarar mı?", "Bir Cochrane derlemesine göre egzersiz el ağrısını, işlevini ve parmak tutukluğunu biraz iyileştirir; 0–10 ölçekte ağrıda ortalama yarım puanlık bir azalma. Etki küçük ve kanıtların kalitesi düşük, ama yan etkiler az ve hafif. Düzenli yapıldığında elinizi hareketli tutmanın güvenli bir yoludur."),
 ("Sıcak mı soğuk mu?", "Elleriniz tutuk ya da sızlıyorsa sıcak, bir eklem şiş ya da sıcaksa soğuk uygulama önerilir. Egzersizden önce elinizi birkaç dakika ılık suda ya da sıcak torbayla ısıtmak hareketi kolaylaştırabilir."),
 ("Romatizmadan nasıl ayırt edilir?", "El kireçlenmesinde ağrı genellikle hareketle artar ve sabah tutukluğu en fazla yarım saat sürer; 45 yaş ve üzerinde bu tablo çoğu zaman tetkik gerekmeden tanı koymaya yeter. Eklemlerde yumuşak, sıcak ve kabarık şişlik ise romatoid artrit gibi iltihaplı bir romatizmayı düşündürür ve romatoloji değerlendirmesi gerektirir."),
]

HO_SRC = [
 "NHS Dumfries & Galloway, Right Decisions. " + ext("https://rightdecisions.scot.nhs.uk/nhs-dumfries-galloway-refhelp/musculoskeletal-system/hand/hand-osteoarthritis", "Hand osteoarthritis") + ". Last reviewed 12 December 2025.",
 "St George’s University Hospitals NHS Foundation Trust. " + ext("https://www.stgeorges.nhs.uk/wp-content/uploads/2025/05/HAN_ESTO.pdf", "Exercises and strengthening for thumb osteoarthritis") + ". May 2025.",
 "Østerås N, Kjeken I, Smedslund G, et al. " + ext("https://search.pedro.org.au/search-results/record-detail/48861", "Exercise for hand osteoarthritis") + ". Cochrane Database of Systematic Reviews. 2017;(1):CD010388.",
]

HO_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>El ve parmak kireçlenmesi</h1>
    <p class="lede">Parmak eklemlerinizde sert boğumlar mı belirdi, kavanoz açmak, düğme iliklemek ya da küçük bir şeyi tutmak eskisi kadar kolay değil mi? El kireçlenmesi, özellikle 50 yaşından sonra sık görülen, uzun süreli bir eklem sorunudur. Tamamen geçmez, ama elinizi doğru kullanmak, ısı ve düzenli hareketle ağrı ve tutukluk çoğu zaman kontrol altında tutulabilir.</p>
    <p class="meta">Son güncelleme: 14 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>50 yaş üstü</b><span>Daha sık görüldüğü dönem</span></div>
        <div class="stat"><b>30 dakika</b><span>Sabah tutukluğu genellikle bundan kısa sürer; daha uzunsa başka bir romatizmayı düşündürebilir</span></div>
        <div class="stat"><b>5 dakika</b><span>Egzersizden önce elinizi ısıtmanız önerilen süre</span></div>
        <div class="stat"><b>Yarım puan</b><span>Egzersizle 0–10 ölçekte ağrıdaki ortalama azalma: küçük ama güvenli bir yarar</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Hareketle artan eklem ağrısı ve kısa süren sabah tutukluğu.</li>
          <li>Parmak eklemlerinde sert, boğumlu şişlikler (Heberden ve Bouchard nodülleri).</li>
          <li>Başparmak kökünde şişlik, hassasiyet, bazen kemikte küçük bir “basamak”.</li>
          <li>Tutma, sıkıştırma ve küçük nesneleri alma zorluğu; çarpınca artan ağrı.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Eklem yüzeyleri zamanla zarar görür ve eskisi kadar pürüzsüz hareket etmez.</li>
          <li>Yaş, cinsiyet, daha önceki eklem yaralanmaları ve eklem yapısındaki farklılıklar riski artırır.</li>
          <li>En sık parmak uçlarına yakın eklemler, orta eklemler ve başparmak kökü etkilenir.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Hareketli tutun</h3><p>Uzun süreli bir durum olduğu için elinizin hareketini ve gücünü korumak önemlidir; eklemleri gereksiz zorlamadan düzenli hareket edin.</p></div>
        <div class="kind"><span class="n">2</span><h3>Isı ve soğuk</h3><p>Elleriniz tutuk ya da sızlıyorsa ılık su veya sıcak torba; bir eklem şiş ve sıcaksa soğuk uygulayabilirsiniz.</p></div>
        <div class="kind"><span class="n">3</span><h3>Molalar verin</h3><p>Örgü, bilgisayar, bahçe işi gibi uzun süreli el işlerine kısa molalar koyarak yükü azaltabilirsiniz.</p></div>
        <div class="kind"><span class="n">4</span><h3>Başparmağa destek</h3><p>Ağırlıklı olarak başparmak kökü sorunlarında ya da ağrı ve işlev kaybı yapan şekil bozukluklarında bir el terapistine yönlendirilmek yararlı olabilir.</p></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Elleri açan altı egzersiz</h2>
      <p class="soft">Başlamadan önce elinizi birkaç dakika ılık suyla ya da sıcak torbayla ısıtın. Hareketleri yavaş ve ağrısız bir aralıkta yapın; parmak eklemlerinde şişlik ya da ağrı artarsa miktarı azaltın.</p>
      {ex_grid(["ho_fist", "ho_opp", "ho_web", "ho_grip", "ho_wrist", "ho_rot"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(HO_FAQ)}
      <p class="soft" style="margin-top:18px">Başparmak kökündeki ağrının başka bir nedeni için <a href="de-quervain.html">De Quervain</a>, iltihaplı eklem hastalığı için <a href="romatoid-artrit.html">romatoid artrit</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Bir el ekleminde yumuşak, kabarık ve sıcak şişlik varsa (iltihaplı bir romatizma olabilir)</li>
        <li>Sabah tutukluğu yarım saatten uzun sürüyorsa</li>
        <li>Ağrı ve şekil bozukluğu elinizi kullanmanızı belirgin kısıtlıyorsa</li>
        <li>Kendi önlemlerinize rağmen belirtiler yönetilemez hale geldiyse</li>
      </ul>
      {CTA_CARD("El ağrınız", "el ve parmak kireçlenmesi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(HO_SRC)}
    </div>
  </section>
</main>'''

page("el-kireclenmesi.html", "El ve Parmak Kireçlenmesi",
     "Parmak eklemlerinizde sert boğumlar ve tutukluk mu var? El kireçlenmesi nedir, romatizmadan nasıl ayrılır, egzersiz işe yarar mı? Uyarı işaretleri ve evde altı egzersiz.",
     "el-kireclenmesi.html", NECK_CSS, HO_BODY, "",
     seo_title="El ve Parmak Kireçlenmesi (El Osteoartriti): Belirtiler, Tedavi ve Egzersizler | İhsan Eren",
     condition="El osteoartriti", faq_items=HO_FAQ)

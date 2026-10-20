# -*- coding: utf-8 -*-
# Yeni rehber (36): Sakroiliak eklem ağrısı (SİE). cond35_part.py'den sonra exec edilir. Video yok.
# Egzersizler bel rehberindeki hazır çizimlerle; leğen kemiğini dengeleyen kaslara odaklı.

_ex2("si_abd", "abd", "Yan yatarak bacak kaldırma", "Yan yatın, alttaki dizinizi hafifçe bükün. Üstteki bacağınızı dizi düz, ayak ucu öne bakacak şekilde yukarı kaldırın; kalçanız geriye devrilmesin. Kalçanın yan kasları leğen kemiğini dengede tutmaya yardım eder.", "Her iki yana 10–15 tekrar")
_ex2("si_walk", "walk", "Yürüyüş", "Rahat ayakkabılarla, ağrının izin verdiği bir tempoda ve sürede yürüyün. Uzun süre oturmak ağrıyı artırıyorsa, gün içine kısa yürüyüşler serpiştirin.", "5–10 dakikayla başlayın, her hafta birkaç dakika artırın")

SI_FAQ = [
 ("Sakroiliak eklem nerede?", "Omurganın en alt kısmındaki üçgen kemik (sakrum) ile leğen kemiğinin arasında, belin iki yanında, kalçanın üst-arka kısmındaki iki küçük çukurun hemen altındadır. Gövdenin yükünü bacaklara aktarır ve çok az hareket eder."),
 ("Ağrının bu eklemden geldiği nasıl anlaşılır?", "Kolay değildir. Ağrı belden, kalçadan ya da siyatik sinirden gelen ağrılara çok benzer. Tek bir muayene testi ya da görüntüleme kesin sonuç vermez; hekimler birkaç ağrı tetikleme testini birlikte değerlendirir. En güvenilir yöntem genellikle ekleme uyuşturucu iğne yapıp ağrının geçip geçmediğine bakmaktır."),
 ("Kemer işe yarar mı?", "Sakroiliak kemerler egzersiz, fizyoterapi ve iğne tedavileriyle birlikte kullanılan seçenekler arasında; ama sonuçlar kişiden kişiye değişiyor. Kemerin işinize yarayıp yaramadığını bir fizyoterapistle birlikte değerlendirebilirsiniz."),
 ("Ameliyat gerekir mi?", "Çok az kişide. Eklemi dondurma (füzyon) ameliyatı, en az 6 ay süren ameliyatsız tedaviye rağmen geçmeyen, testlerle ve tanısal iğneyle eklemden kaynaklandığı gösterilmiş ağrıda düşünülür. Bazı kişilerde sinir uçlarını ısıyla etkisizleştiren radyofrekans tedavisi 6–12 ay süren rahatlama sağlayabilir."),
]

SI_SRC = [
 "Barros G, McGrath L, Gelfenbeyn M. " + ext("https://community.the-hospitalist.org/content/sacroiliac-joint-dysfunction-patients-low-back-pain", "Sacroiliac joint dysfunction in patients with low back pain") + ". Federal Practitioner. 2019;36(8):370–375.",
 "HCA Healthcare UK. " + ext("https://www.hcahealthcare.co.uk/conditions/sacroiliac-joint-pain", "Sacroiliac (SI) joint pain") + ".",
 "Szadek KM, van der Wurff P, van Tulder MW, Zuurmond WWA, Perez RSGM. " + ext("https://doi.org/10.1016/j.jpain.2008.09.014", "Diagnostic validity of criteria for sacroiliac joint pain: a systematic review") + ". J Pain. 2009;10(4):354–368",
 SRC_NICE59,
]

SI_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Sakroiliak eklem ağrısı</h1>
    <p class="lede">Belinizin en alt kısmında, bir yanda, kalçanın üst-arka kısmında saplanan bir ağrı mı var? Oturduğunuz yerden kalkarken ya da uzun süre oturunca mı artıyor? Bu ağrı, omurganın alt ucunu leğen kemiğine bağlayan sakroiliak eklemden kaynaklanıyor olabilir. Bel ağrılarının yaklaşık yüzde 15 ile 30’unda bu eklemin payı olduğu tahmin ediliyor. Tanısı zordur, ama çoğu kişi egzersiz ve fizyoterapiyle rahatlar.</p>
    <p class="meta">Son güncelleme: 14 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%15–30</b><span>Bel ağrısı vakalarında sakroiliak eklemin kaynak olduğu tahmin edilen oran</span></div>
        <div class="stat"><b>3 × 10 cm</b><span>Ağrının genellikle toplandığı alan: kalçanın üst-arka çıkıntısının hemen altı</span></div>
        <div class="stat"><b>Belin en altı</b><span>Bu eklemden kaynaklanan ağrı genellikle son bel omurunun hizasından yukarı çıkmaz</span></div>
        <div class="stat"><b>Birkaç test</b><span>Tanı tek bir testle değil, birkaç muayene testinin birlikte değerlendirilmesiyle konur</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Belin en alt kısmında, genellikle bir yanda, kalçanın üst-arka kısmında ağrı.</li>
          <li>Kalçaya, kasığa, uyluğun arkasına, hatta bacağa yayılabilen ağrı; siyatiğe benzeyebilir.</li>
          <li>Oturduğunuz yerden kalkarken ya da uzun süre oturduktan sonra artan ağrı.</li>
          <li>Bazen bacağın boşalacakmış gibi olması ya da karıncalanma.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Kalçanın üstüne sert bir düşüş ya da tekrarlayan zorlanma.</li>
          <li>Gebelik; eklem bağlarının gevşemesiyle. <a href="gebelikte-bel-agrisi.html">Gebelikte bel ve leğen ağrısı</a> rehberine bakabilirsiniz.</li>
          <li>Bacak boyu farkı, yürüme bozuklukları, skolyoz ve uzun süreli yoğun spor.</li>
          <li>Daha önce belden füzyon ameliyatı olmak.</li>
          <li><a href="ankilozan-spondilit.html">Ankilozan spondilit</a> gibi eklemde iltihap yapan romatizmal hastalıklar.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Evde neler yapabilirim?</h2>
        <ul class="dots">
          <li>Hareketli kalmaya ve günlük işlerinize elden geldiğince devam etmeye çalışın.</li>
          <li>Uzun süre oturmaktan kaçınıp sık sık kalkabilir, kısa yürüyüşler yapabilirsiniz.</li>
          <li>Buz ya da ağrı kesici rahatlatabilir; ilaç kullanmadan önce hekiminize ya da eczacınıza danışabilirsiniz.</li>
          <li>Aşağıdaki egzersizlerle leğen kemiğini dengeleyen kasları güçlendirebilirsiniz.</li>
        </ul>
      </div>
      <div>
        <h2>Tedavi seçenekleri</h2>
        <ul class="dots">
          <li><b>Egzersiz ve fizyoterapi:</b> Leğen kemiğini dengeleyen egzersizler ilk basamaktır.</li>
          <li><b>Kemer:</b> Bazı kişilerde destek sağlar; sonuçlar değişkendir.</li>
          <li><b>İğne tedavileri:</b> Ekleme ya da çevresine yapılan iğneler hem tanıya hem tedaviye yardım edebilir.</li>
          <li><b>Radyofrekans ve ameliyat:</b> Diğer tedavilere uzun süre yanıt vermeyen seçilmiş kişilerde düşünülür.</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Leğen kemiğini dengeleyen altı egzersiz</h2>
      <p class="soft">Hareketleri yavaş ve kontrollü, ağrısız bir aralıkta yapın. Bir hareket eklem bölgesindeki ağrıyı belirgin artırıyorsa onu bir süre atlayıp diğerlerine devam edebilirsiniz.</p>
      {ex_grid(["ptilt", "bridge", "birddog", "si_abd", "k2c", "si_walk"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(SI_FAQ)}
      <p class="soft" style="margin-top:18px">Benzer ağrılar için <a href="bel-agrisi.html">bel ağrısı</a> ve <a href="piriformis-sendromu.html">piriformis sendromu</a> rehberlerine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Ağrı birkaç haftada azalmıyor ya da giderek artıyorsa</li>
        <li>Genç yaşta başlayan, sabahları uzun süren tutuklukla birlikte olan ve hareketle azalan bel-kalça ağrısı varsa (romatizmal bir hastalık olabilir)</li>
        <li>Düşme ya da darbeden sonra başladıysa</li>
        <li>Ateş, nedensiz kilo kaybı ya da kanser öyküsüyle birlikteyse</li>
        <li>Acil: iki bacakta güçsüzlük ya da uyuşma, kasık ve makat çevresinde uyuşma, idrar ya da dışkı kontrolünde sorun varsa</li>
      </ul>
      {CTA_CARD("Sakroiliak eklem ağrınız", "sakroiliak eklem ağrısı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(SI_SRC)}
    </div>
  </section>
</main>'''

page("sakroiliak-eklem-agrisi.html", "Sakroiliak Eklem Ağrısı",
     "Belin en altında, bir yanda saplanan ağrı sakroiliak eklemden mi geliyor? Belirtiler, nedenler, tanının neden zor olduğu, tedavi seçenekleri ve evde altı egzersiz.",
     "sakroiliak-eklem-agrisi.html", NECK_CSS, SI_BODY, "",
     seo_title="Sakroiliak Eklem Ağrısı (SİE): Belirtiler, Tedavi ve Egzersizler | İhsan Eren",
     condition="Sakroiliak eklem ağrısı", faq_items=SI_FAQ)

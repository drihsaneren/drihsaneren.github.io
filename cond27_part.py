# -*- coding: utf-8 -*-
# Yeni rehber (27): piriformis sendromu. cond26_part.py'den sonra exec edilir. Video yok.
# slump, bridge, abd, sideplank, hext mevcut anahtarlar (çevirileri hazır); piriformis germe bu sayfaya özel.

_ex2("pi_str", "k2c", "Piriformis germe", "Sırtüstü yatın, dizleriniz bükülü olsun. Ağrılı tarafınızın ayak bileğini diğer dizinizin üzerine koyun (4 rakamı gibi). Alttaki uyluğunuzu iki elinizle tutup göğsünüze doğru yavaşça çekin; ağrılı kalçanızın arkasında hafif bir gerilme hissedin. Uyuşma ya da karıncalanma artarsa bırakın.", "30 saniye tutun, 3 tekrar")

PI_FAQ = [
 ("Siyatik ile piriformis sendromu aynı şey mi?", "Hayır. Siyatik, siyatik sinir boyunca bacağa yayılan ağrının adıdır ve en sık nedeni bel fıtığıdır. Piriformis sendromunda ise sinirin kalçadaki piriformis kası tarafından sıkıştırıldığı düşünülür; ortopedi pratiğinde siyatik ağrılarının yaklaşık %1’i ya da daha azının bu nedenle olduğu tahmin ediliyor. Bel fıtığı için bel fıtığı rehberimize bakabilirsiniz."),
 ("Uzun oturmak kötüleştirir mi?", "Oturunca, özellikle sert bir sandalyede artan ağrı bu sendromun tipik özelliklerindendir. Uzun süre oturmanız gerekiyorsa sık sık kalkıp hareket edebilir, sert yüzeyler yerine daha yumuşak bir yüzeyde oturmayı deneyebilirsiniz."),
 ("Hangi test tanı koydurur?", "Tek başına tanı koyduran bir test yok. Muayenede kullanılan pek çok test tanımlanmış, ancak doğrulukları henüz bilinmiyor. Tanı, belirtiler ve muayene bulguları birlikte değerlendirilerek ve bel kaynaklı nedenler de düşünülerek konur."),
 ("İğne ya da ameliyat gerekir mi?", "Çoğu zaman egzersiz ve etkinliği düzenlemekle başlanır. Bazı durumlarda kortizon iğnesi yardımcı olabilir; ameliyat ise çok nadiren gerekir."),
]

PI_SRC = [
 "Hopayian K, Song F, Riera R, Sambandan S. The clinical features of the piriformis syndrome: a systematic review. Eur Spine J. 2010;19(12):2095–2109. " + ext("https://ueaeprints.uea.ac.uk/id/eprint/34961/", "ueaeprints.uea.ac.uk") + ".",
 "Hopayian K, Danielyan A. Four symptoms define the piriformis syndrome: an updated systematic review of its clinical features. Eur J Orthop Surg Traumatol. 2018;28(2):155–164. " + ext("https://ueaeprints.uea.ac.uk/id/eprint/92822", "ueaeprints.uea.ac.uk") + ".",
 "NHS Lothian. " + ext("https://policyonline.nhslothian.scot/wp-content/uploads/2025/02/Piriformis-Syndrome.pdf", "Piriformis syndrome") + ". January 2025.",
 "NHS. " + ext("https://www.nhs.uk/conditions/sciatica/", "Sciatica") + ". Page last reviewed 3 December 2024.",
]

PI_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Piriformis sendromu</h1>
    <p class="lede">Piriformis, kalçanın derininde, bacağı dışa döndüren bir kastır; siyatik sinir bu kasın yakınından, bazen de içinden geçer. Piriformis sendromunda sinirin bu kas tarafından sıkıştırıldığı düşünülür. Kalçada, oturunca artan ve bacağın arkasına yayılabilen bir ağrıya yol açar. Tartışmalı bir tanıdır: siyatik ağrısının çok daha sık nedeni bel fıtığıdır.</p>
    <p class="meta">Son güncelleme: 11 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>≤ %1</b><span>Ortopedi pratiğinde siyatik ağrıları içinde piriformis sendromunun tahmini payı</span></div>
        <div class="stat"><b>4 bulgu</b><span>Tanıyı en çok destekleyenler: kalça ağrısı, oturunca artma, kalçada basınca hassasiyet, kası geren hareketlerle ağrı</span></div>
        <div class="stat"><b>55 çalışma</b><span>2010’daki sistematik derlemede incelendi; kanıtların çoğu olgu sunumu</span></div>
        <div class="stat"><b>30 saniye</b><span>Germe egzersizlerinde önerilen bekleme süresi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Kalçada ağrı ve basınca hassasiyet.</li>
          <li>Oturunca, özellikle sert sandalyede artan ağrı.</li>
          <li>Uyluğun arkasında karıncalanma, uyuşma ya da yanma; bazen ayağa kadar.</li>
          <li>Kalçada, kasıkta ya da uyluğun arkasında künt ya da yanıcı ağrı.</li>
          <li>Bacakta ağırlık ya da yorgunluk hissi.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Siyatik sinirin piriformis kası tarafından sıkıştırılması.</li>
          <li>Etkinliğin miktarında ya da şiddetinde ani artış.</li>
          <li>Bacaktaki başka bir yaralanmayı telafi etmeye çalışmak.</li>
          <li>Koşu ve sıçrama sporları, uzun yürüyüş, merdiven ya da yokuş çıkmak.</li>
          <li>Kas gücünün ya da esnekliğin yetersiz olması.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Tanı neden zor?</h2>
        <p class="soft">2010’da 55 çalışmayı inceleyen sistematik derlemede kanıtların çoğu olgu sunumları ve derlemelerden oluşuyordu. En sık bildirilen dört bulgu kalça ağrısı, kalçada siyatik çentik üzerinde basınca hassasiyet, oturunca artan ağrı ve piriformis kasını geren hareketlerle ortaya çıkan ağrıydı.</p>
        <p class="soft">2018’deki güncel derlemeye göre muayene testlerinin doğruluğu henüz bilinmiyor; düz bacak kaldırma testinin normal çıkması bu tanıyı dışlamıyor.</p>
      </div>
      <div>
        <h2>Ne kadar sık?</h2>
        <p class="soft">Ortopedi pratiğinde siyatik ağrıları içinde piriformis sendromunun payı %1 ya da daha az olarak tahmin ediliyor. Siyatik ağrısının en sık nedeni bel fıtığıdır; dar kanal ve bel kayması da siyatik yapabilir. Bu yüzden belden kaynaklanan nedenler de düşünülmelidir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Etkinliği düzenleyin</h3><p>Belirtileri artıran etkinliğe bir süre ara verebilirsiniz. Uzun süre oturuyorsanız sık sık kalkıp hareket etmek rahatlatabilir.</p></div>
        <div class="kind"><span class="n">2</span><h3>Germe ve güçlendirme</h3><p>Kalçayı geren egzersizlerde her pozisyonu 30 saniye tutabilirsiniz. Güçlendirme egzersizleri kalçanın yükü daha iyi taşımasına yardım eder.</p></div>
        <div class="kind"><span class="n">3</span><h3>Tenis topuyla masaj</h3><p>Duvara yaslanarak ya da yerde, kalçanızın altına bir tenis topu koyup hassas bölgeye hafifçe masaj yapabilirsiniz.</p></div>
        <div class="kind"><span class="n">4</span><h3>Buz, sıcak, ağrı kesici</h3><p>20 dakikalık buz uygulaması ağrıyı, sıcak uygulama esnekliği destekleyebilir. Parasetamol ya da ibuprofen gibi bir ilacı prospektüse uygun şekilde kullanabilirsiniz.</p></div>
      </div>
      <p class="soft" style="margin-top:18px">Belden bacağa yayılan ağrı için <a href="bel-fitigi.html">bel fıtığı</a>, kalçanın dış yanındaki ağrı için <a href="kalca-yan-agrisi.html">kalça yan ağrısı</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Kalçayı rahatlatan altı egzersiz</h2>
      <p class="soft">Hareketleri yavaş ve kontrollü yapın. Bacaktaki uyuşma ya da karıncalanma artarsa o hareketi bırakabilir, bir hekime ya da fizyoterapiste danışabilirsiniz.</p>
      {ex_grid(["pi_str", "slump", "bridge", "abd", "sideplank", "hext"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(PI_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Ağrı birkaç haftada düzelmiyor, kötüleşiyor ya da günlük işlerinizi engelliyorsa</li>
        <li>Acil: siyatik ağrısı iki bacakta birden varsa</li>
        <li>Acil: iki bacakta ciddi ya da giderek artan güçsüzlük veya uyuşma varsa</li>
        <li>Acil: cinsel organların ya da makatın çevresinde uyuşma varsa</li>
        <li>Acil: idrar ya da dışkı kontrolünde yeni bir sorun varsa</li>
      </ul>
      {CTA_CARD("Kalça ve bacak ağrınız", "piriformis sendromu")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(PI_SRC)}
    </div>
  </section>
</main>'''

page("piriformis-sendromu.html", "Piriformis Sendromu",
     "Kalçada oturunca artan, bacağın arkasına yayılan ağrı piriformis sendromu mu? Belirtiler, tanının neden zor olduğu, siyatikten farkı, öneriler ve evde altı egzersiz.",
     "piriformis-sendromu.html", NECK_CSS, PI_BODY, "",
     seo_title="Piriformis Sendromu: Belirtiler, Egzersiz ve Siyatikten Farkı | İhsan Eren",
     condition="Piriformis sendromu", faq_items=PI_FAQ)

# -*- coding: utf-8 -*-
# Masa başı çalışanlar için rehber. protez_part.py'den sonra exec edilir.

# Ayakta arkaya esneme (yandan): eller belde, gövde kalçadan geriye esner.
SV["bext"] = fig(GRD +
    '<path class="fig" d="M58 72 L54 112 M58 72 L62 112"/>'
    f'<g>{anim_t("0 58 72;-22 58 72;0 58 72", typ="rotate")}'
    '<path class="fig hl" d="M58 72 L58 34"/><circle class="hd" cx="59" cy="24" r="7"/><path d="M65 22 L70 25 L65 27 Z" fill="#2A6F6B"/>'
    '<path class="fig" d="M58 40 L48 54 L56 66"/></g>',
    "Ayakta arkaya esneme")

EXT["bext"] = ("Ayakta arkaya esneme", "Ayağa kalkın, ayaklarınız omuz genişliğinde açık olsun. Ellerinizi belinizin arkasına koyun ve kalçanızı hafifçe öne iterek gövdenizi rahat ettiğiniz kadar geriye esnetin, sonra doğrulun. Uzun oturduktan sonra iyi gelir.", "5–10 tekrar, her molada")

DESK_FAQ = [
 ("Dik oturmak zorunda mıyım?", "Hayır. Tek bir ideal duruşun var olduğunu ya da 'yanlış' duruşlardan kaçınmanın bel ağrısını önlediğini gösteren güçlü bir kanıt yok. Omurga sağlam bir yapıdır; farklı pozisyonlarda rahatça oturabilirsiniz. Önemli olan uzun süre aynı pozisyonda kalmamak ve sık sık hareket etmektir."),
 ("Ayakta çalışma masası işe yarar mı?", "Oturma süresini azaltmaya yardım eder. İngiltere'de yapılan bir çalışmada ayarlanabilir masa ve destek programı, 12. ayda iş gününde oturma süresini yaklaşık 82 dakika azalttı; kas-iskelet şikâyetlerine etkisi ise tutarlı değildi. Uzun süre ayakta durmak da yorucudur; amaç oturma ve ayakta durma arasında dönüşümlü çalışmaktır."),
 ("Spor yapıyorum, uzun süre oturmak yine de zararlı mı?", "Günde 8 saatten fazla oturan kişilerde günde 60–75 dakika orta yoğunlukta hareket, uzun oturmayla ilişkili artmış ölüm riskini ortadan kaldırıyor. Dünya Sağlık Örgütü de oturma süresini sınırlamayı ve bu süreyi her yoğunlukta hareketle değiştirmeyi öneriyor."),
 ("Ne sıklıkla mola vermeliyim?", "Kesin bir süre için güçlü bir kanıt yok. Pratikte yarım saatte bir, en azından saatte bir kalkıp birkaç dakika hareket etmek iyi bir hedeftir. Telefonla konuşurken ayağa kalkmak, su almaya yürümek gibi küçük alışkanlıklar da sayılır."),
 ("Boynum ya da belim ağrıyorsa ne yapmalıyım?", "Çoğu boyun ve bel ağrısı ciddi bir nedene bağlı değildir ve hareketle azalır. <a href=\"boyun-agrisi.html\">Boyun ağrısı</a> ve <a href=\"bel-agrisi.html\">bel ağrısı</a> rehberlerindeki egzersizleri deneyebilirsiniz. Ağrı birkaç haftada düzelmiyorsa bir fizyoterapiste başvurun."),
]

DESK_SRC = [
 "Bull FC, Al-Ansari SS, Biddle S, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/33239350/", "World Health Organization 2020 guidelines on physical activity and sedentary behaviour") + ". Br J Sports Med. 2020;54(24):1451-1462.",
 "Ekelund U, Steene-Johannessen J, Brown WJ, et al. " + ext("https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(16)30370-1/abstract", "Does physical activity attenuate, or even eliminate, the detrimental association of sitting time with mortality? A harmonised meta-analysis of data from more than 1 million men and women") + ". Lancet. 2016;388(10051):1302-1310.",
 "NIHR Evidence. " + ext("https://evidence.nihr.ac.uk/alert/standing-desks-with-a-support-package-reduce-time-sitting-at-work", "Standing desks with a support package reduce time sitting at work") + ".",
 "Slater D, et al. " + ext("https://www.jospt.org/doi/10.2519/jospt.2019.0610", "\"Sit up straight\": time to re-evaluate") + ". J Orthop Sports Phys Ther. 2019.",
 "The Rotherham NHS Foundation Trust. " + ext("https://www.therotherhamft.nhs.uk/patients-and-visitors/patient-information/posture", "Posture") + ".",
]

DESK_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Masa başında çalışanlar için</h1>
    <p class="lede">Birçoğumuz günün büyük kısmını bilgisayar başında, oturarak geçiriyor. Boyun ve bel sağlığı için "mükemmel duruş"tan daha önemli olan şey sık sık hareket etmek, pozisyon değiştirmek ve gün içinde kısa hareket molaları vermek.</p>
    <p class="meta">Son güncelleme: {UPDATED}</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>150–300 dk</b><span>Dünya Sağlık Örgütü'nün yetişkinler için önerdiği haftalık orta yoğunlukta hareket</span></div>
        <div class="stat"><b>2 gün</b><span>Haftada en az kas güçlendirme egzersizi yapılması önerilen gün sayısı</span></div>
        <div class="stat"><b>60–75 dk</b><span>Günde 8 saatten fazla oturanlarda artan ölüm riskini ortadan kaldıran günlük hareket</span></div>
        <div class="stat"><b>82 dk</b><span>Ayarlanabilir masa ve destek programıyla iş gününde azalan oturma süresi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Doğru duruş diye bir şey var mı?</h2>
      <p class="soft">Yıllarca "dik otur" diye öğütlendik. Oysa tek bir ideal duruşun var olduğunu ya da "yanlış" duruşlardan kaçınmanın bel ağrısını önlediğini gösteren güçlü bir kanıt yok. Omurganın hiçbir eğrilik biçimi ağrıyla güçlü şekilde ilişkili bulunmamıştır; omurga, farklı pozisyonları güvenle taşıyabilen sağlam bir yapıdır.</p>
      <div class="callout">
        <p>Fizyoterapistlerin sık kullandığı bir söz vardır: En iyi duruş, bir sonraki duruştur. Rahat ettiğiniz pozisyonlarda oturun ama uzun süre aynı pozisyonda kalmayın; pozisyon değiştirmek ve hareket etmek hem sırtınıza hem genel sağlığınıza iyi gelir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Rahat bir çalışma düzeni</h2>
        <p class="soft">Bunlar kesin kurallar değil, rahat çalışmanıza yardım edebilecek önerilerdir. Size iyi gelen düzeni deneyerek bulun.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Ekranı yaklaşık bir kol boyu uzağa, üst kenarı göz hizasında ya da biraz altında olacak şekilde yerleştirin.</li>
        <li>Dizüstü bilgisayarla uzun çalışıyorsanız ekranı yükseltip ayrı klavye ve fare kullanın.</li>
        <li>Klavye ve fareyi gövdenize yakın tutun; omuzlarınız rahat, bilekleriniz düz kalsın.</li>
        <li>Ayaklarınız yere ya da bir ayak desteğine rahatça bassın.</li>
        <li>Telefona uzun süre bakacaksanız başınızı eğmek yerine telefonu biraz yukarı kaldırın.</li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Gün içine hareket serpiştirin</h2>
        <p class="soft">Dünya Sağlık Örgütü oturma süresini sınırlamayı ve bu süreyi her yoğunlukta hareketle değiştirmeyi öneriyor. Küçük alışkanlıklar gün sonunda büyük fark yaratır.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Yarım saatte bir, en azından saatte bir kalkıp birkaç dakika hareket edin.</li>
        <li>Telefonla konuşurken ayağa kalkın ya da yürüyün.</li>
        <li>Su şişenizi küçük seçin; doldurmak için sık sık kalkın.</li>
        <li>Asansör yerine merdiveni, kısa mesafelerde yürümeyi tercih edin.</li>
        <li>Mümkünse bazı toplantıları ayakta ya da yürüyerek yapın.</li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Masa başı egzersizleri</p>
      <h2>Mola için altı hareket</h2>
      <p class="soft">Bu hareketleri gün içinde, molalarda birkaç tanesini seçerek yapabilirsiniz. Hepsi masanızın yanında, özel ekipman olmadan yapılır. Hareketler ağrıyı belirgin şekilde artırıyorsa zorlamayın.</p>
      {ex_grid(["chin", "scap", "thor", "side", "bext", "wflex"])}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Masa başı çalışanlar için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("TjwKe_YLLEM", "Sırt germe videosunu oynat", "The One Stretch EVERYONE Should Do!")}
          <h3>Herkesin yapması gereken sırt germe</h3>
          <p>Uzun oturmanın ardından sırtın orta bölümünü açan germe hareketi.</p>
        </div>
        <div class="vid">
          {vbox("Wsb78V2UYVA", "Temel boyun egzersizi videosunu oynat", "The One Exercise Everyone Should Do For Neck Pain")}
          <h3>Herkesin yapması gereken tek boyun egzersizi</h3>
          <p>Ekran başında uzun süre kalan boyun için temel egzersiz.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(DESK_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman bir uzmana başvurmalı?</h2>
      <p class="soft">Masa başı çalışanlarda boyun, sırt ve bel ağrıları çoğunlukla zararsızdır ve hareketle azalır. Şu durumlarda ise beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Kola ya da bacağa yayılan ağrıyla birlikte uyuşma, karıncalanma ya da güç kaybı</li>
        <li>Elde sürekli uyuşma, özellikle geceleri artan (<a href="karpal-tunel-sendromu.html">karpal tünel sendromu</a> olabilir)</li>
        <li>Dinlenmekle geçmeyen gece ağrısı, ateş ya da nedensiz kilo kaybı</li>
        <li>Ani başlayan çok şiddetli baş ağrısı, görme bozukluğu ya da konuşma güçlüğü (<strong>112</strong>'yi arayın)</li>
      </ul>
      {CTA_CARD("Boyun, sırt ve bel şikâyetleriniz", "masa başı çalışmaya bağlı boyun ve bel ağrısı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(DESK_SRC)}
    </div>
  </section>
</main>'''

page("masa-basi.html", "Masa Başında Çalışanlar İçin",
     "Masa başında çalışanlar için boyun ve bel sağlığı: doğru duruş diye bir şey var mı, ne sıklıkla mola verilmeli, ayakta çalışma masası işe yarar mı? Mola için altı egzersiz, rahat çalışma düzeni ve videolar.",
     "masa-basi.html", NECK_CSS, DESK_BODY, YT_JS,
     seo_title="Masa Başı Çalışanlar İçin Duruş, Mola ve Egzersiz Rehberi | İhsan Eren",
     about={"@type": "Thing", "name": "Masa başı çalışmada kas-iskelet sağlığı"},
     faq_items=pick(DESK_FAQ, 0, 1, 2, 3))

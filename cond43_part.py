# -*- coding: utf-8 -*-
# Yeni rehber (43): Omuzda kireç birikmesi (kalsifik tendinit). cond42_part.py'den sonra exec edilir. Video yok.
# Egzersizler Doncaster ve Bassetlaw NHS broşüründeki evrelere göre; sarkaç ve sopa çizimleri donuk omuz rehberinden (EX).

_EXF = {e[0]: e[3] for e in EX}
SV["cf_pendf"] = _EXF["Sarkaç"]
SV["cf_stickf"] = _EXF["Sopa ile dışa döndürme"]
_ex2("cf_pend", "cf_pendf", "Sarkaç", "Sağlam elinizle bir masaya dayanıp öne eğilin. Ağrılı kolunuzu gevşekçe sarkıtın ve gövdenizi hafifçe sallayarak kolunuza küçük daireler çizdirin. Kolu kaslarınızla zorlamayın.", "Toplam 1–2 dakika, günde 4–5 kez")
_ex2("cf_post", "scap", "Dik duruş", "Dik oturun ya da durun. Omuzlarınızı kaldırmadan geriye ve hafifçe aşağıya alın, göğsünüz açılsın.", "20–30 saniye tutun, 5 tekrar")
_ex2("cf_elbow", "ly_arm", "Dirseği bükme ve açma", "Kolunuz rahatça yanınızda dursun. Dirseğinizi ağrısız bir aralıkta tam bükün, sonra tam açın. Hafif bir gerilme yeterli; ağrıya doğru zorlamayın.", "10–15 tekrar, günde 4–5 kez")
_ex2("cf_wall", "wslide", "Duvarda kolu kaydırma", "Yüzünüz duvara dönük durun, ağrılı kolunuzun ön kolunu duvara yaslayın. Kolunuzu duvarda ağrısız bir aralıkta yukarı kaydırın, sonra yavaşça indirin.", "10 tekrar, günde 4–5 kez (ilk 2–3 hafta geçtikten sonra)")
_ex2("cf_stick", "cf_stickf", "Sopa ile dışa döndürme", "Ağrılı kolunuzun dirseği gövdenize yapışık ve 90 derece bükülü olsun. Bir sopayı iki elinizle tutun; sağlam kolunuzla iterek ağrılı kolunuzun ön kolunu yavaşça dışarı doğru açın.", "5 saniye tutun, 10 tekrar (ilk 2–3 hafta geçtikten sonra)")
_ex2("cf_iso", "isoer", "Kapı pervazında dışa itme", "Dirseğiniz 90 derece bükülü, gövdenize yakın olsun. Elinizin dış yüzünü bir kapı pervazına yaslayın ve kolunuzu hareket ettirmeden dışarı doğru hafifçe itin.", "5 saniye, 10 tekrar (ağrı azaldıktan sonra)")

CF_FAQ = [
 ("Röntgende kireç çıktı; ağrımın nedeni bu mu?", "Her zaman değil. Belirtisi olmayan yetişkinlerin yaklaşık %8’inde de omuz tendonlarında kireç birikimi görülebiliyor. Bu yüzden röntgendeki kireç tek başına ağrının nedenini göstermez; muayeneyle birlikte değerlendirilmesi gerekir."),
 ("Kireç kendiliğinden kaybolur mu?", "Çoğu kireç birikimi zamanla kendiliğinden kaybolur. Şiddetli ağrı çoğu zaman birkaç hafta içinde yatışır, ama kirecin tamamen erimesi 9 ay ya da daha uzun sürebilir; bu sürede daha hafif bir ağrı devam edebilir."),
 ("Ağrı neden birdenbire bu kadar şiddetlendi?", "Ani ve çok şiddetli ağrı çoğu zaman vücudun kireci emmeye başladığı dönemde ortaya çıkar. Yani bu evre ne kadar zorlu olsa da çoğu zaman iyileşmenin bir parçasıdır."),
 ("Hangi tedaviler var?", "İlk adım ağrı kontrolü ve kolu ağrının izin verdiği kadar hareketli tutmaktır. Ağrı yatışmazsa hekiminiz kortizon iğnesi, ultrason eşliğinde kirecin iğneyle parçalanıp yıkanması (lavaj) ya da şok dalga tedavisi önerebilir. Bir derlemede lavajın şok dalgaya ve tek başına kortizona göre daha etkili olabileceği bulundu, ancak kanıtların kalitesi düşük. Ameliyat, başka yöntemlerle kontrol edilemeyen ağrının olduğu nadir durumlara ayrılır. Diğer tedavilere rağmen ağrısı süren 48 hastayla yapılan randomize bir çalışmada, lavaja ek olarak kortizon iğnesi yapılanlar 1 yılın sonunda yalnızca kortizon iğnesi yapılanlardan daha fazla iyileşti ve komplikasyon riski düşüktü."),
 ("Askı kullanmalı mıyım?", "Askıyı yalnızca rahatlamak için kısa süre kullanın ve mümkün olan en kısa sürede bırakın. Omzunuzu ağrıyı artırmadan hareket ettirmek tutukluğu önler. Uyurken yastıklarla desteklenmiş yarı oturur bir pozisyon daha rahat olabilir."),
]

CF_SRC = [
 "NHS Lothian. " + ext("https://policyonline.nhslothian.scot/Policies/PatientInformation/Calcific_Tendinopathy.pdf", "Calcific tendinopathy") + ". Patient information, July 2020.",
 "Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust. " + ext("https://www.dbth.nhs.uk/wp-content/uploads/2023/08/WPR45490-Shoulder-Calcific-Tendonitus.pdf", "Shoulder calcific tendonitis") + ". WPR45490, 2017.",
 "Whittington Health NHS Trust. " + ext("https://www.whittington.nhs.uk/mini-apps/leaflet/?id=501", "Calcific tendinopathy") + ". 2025.",
 "Lafrance S, Doiron-Cadrin P, Saulnier M, et al. " + ext("https://pmc.ncbi.nlm.nih.gov/articles/PMC6539165", "Is ultrasound-guided lavage an effective intervention for rotator cuff calcific tendinopathy? A systematic review with a meta-analysis of randomised controlled trials") + ". BMJ Open Sport Exerc Med. 2019;5(1):e000506.",
 "de Witte PB, Selten JW, Navas A, et al. " + ext("https://doi.org/10.1177/0363546513487066", "Calcific tendinitis of the rotator cuff: a randomized controlled trial of ultrasound-guided needling and lavage versus subacromial corticosteroids") + ". Am J Sports Med. 2013;41(7):1665–1673.",
 "NHS. " + ext("https://www.nhs.uk/conditions/shoulder-pain/", "Shoulder pain") + ".",
]

CF_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Omuzda kireç birikmesi (kalsifik tendinit)</h1>
    <p class="lede">Omzunuzda birdenbire başlayan, geceleri uyutmayan şiddetli bir ağrı mı var, röntgende “kireç” mi görüldü? Omzu çevreleyen tendonlarda kalsiyum birikmesine kalsifik tendinit denir. Ağrı çok yoğun olabilir, ama ciddi ya da zararlı bir durum değildir; çoğu kireç birikimi zamanla kendiliğinden kaybolur.</p>
    <p class="meta">Son güncelleme: 24 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>30–60 yaş</b><span>En sık görüldüğü dönem; kadınlarda biraz daha sık</span></div>
        <div class="stat"><b>Birkaç hafta</b><span>Şiddetli ağrının çoğu zaman yatıştığı süre</span></div>
        <div class="stat"><b>9 ay</b><span>Kirecin tamamen erimesi bu kadar ya da daha uzun sürebilir</span></div>
        <div class="stat"><b>%8</b><span>Belirtisi olmayan yetişkinlerde de görülen kireç birikimi oranı (yaklaşık)</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Birdenbire başlayan omuz ağrısı ve tutukluk.</li>
          <li>Kolu hareket ettirince artan yoğun ağrı.</li>
          <li>Uykuyu bölen şiddetli ağrı.</li>
          <li>Omuz hareketlerinde kısıtlılık, omuz tendonlarında hassasiyet.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Omzu çevreleyen tendonlarda (rotator manşet) kalsiyum birikir ve tendonu tahriş eder.</li>
          <li>En şiddetli ağrı çoğu zaman vücudun bu kireci emmeye başladığı dönemde görülür.</li>
          <li>Kireç her zaman ağrı yapmaz; röntgende görülen kirecin ağrıyla ilişkisini muayene belirler.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Ağrıyı kontrol edin</h3><p>Hekiminize danışarak ağrı kesici ya da iltihap giderici ilaç kullanabilirsiniz. Buz uygulaması da ağrıyı hafifletebilir.</p></div>
        <div class="kind"><span class="n">2</span><h3>Yükü azaltın</h3><p>İlk birkaç hafta işleri biraz hafifletin, ağrıyı artıran hareketleri değiştirin.</p></div>
        <div class="kind"><span class="n">3</span><h3>Kolu hareketli tutun</h3><p>Omzunuzu ağrının izin verdiği kadar hareket ettirin; bu tutukluğu önler. Askıyı yalnızca kısa süre, rahatlamak için kullanın.</p></div>
        <div class="kind"><span class="n">4</span><h3>Adım adım güçlenin</h3><p>Şiddetli ağrı yatıştıktan sonra esneme ve güçlendirme egzersizlerine geçin. Belirtiler sürerse fizyoterapi destek olabilir.</p></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Omzu adım adım açan altı egzersiz</h2>
      <p class="soft">İlk üç egzersizle başlayın. Ağrı azalmaya başlayınca, genellikle 2–3 hafta sonra, diğerlerini ekleyin. Hareketleri doğal aralığınızda yapın, zorlamayın; egzersizler belirtilerinizi artırmamalı.</p>
      {ex_grid(["cf_pend", "cf_post", "cf_elbow", "cf_wall", "cf_stick", "cf_iso"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(CF_FAQ)}
      <p class="soft" style="margin-top:18px">Kolu yana kaldırırken artan ağrı için <a href="omuz-sikismasi.html">omuz sıkışması</a>, giderek artan tutukluk için <a href="donuk-omuz.html">donuk omuz</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Ani ya da çok şiddetli omuz ağrısı varsa, kolunuzu hiç hareket ettiremiyorsanız</li>
        <li>Ağrı bir yaralanma ya da düşmeden sonra başladıysa</li>
        <li>Omzunuzun şekli değiştiyse ya da belirgin şişlik varsa</li>
        <li>Kolunuzda geçmeyen karıncalanma ya da his kaybı varsa</li>
        <li>Omzunuz dokunulduğunda sıcak ya da soğuksa, ateşiniz ya da halsizliğiniz varsa</li>
        <li>Ağrı kötüleşiyor ya da 2 hafta içinde düzelmiyorsa</li>
      </ul>
      {CTA_CARD("Omuz ağrınız", "omuzda kireç birikmesi (kalsifik tendinit)")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(CF_SRC)}
    </div>
  </section>
</main>'''

page("omuzda-kirec-birikmesi.html", "Omuzda Kireç Birikmesi (Kalsifik Tendinit)",
     "Omzunuzda birdenbire başlayan şiddetli ağrı ve röntgende kireç mi var? Kalsifik tendinit nedir, kendiliğinden geçer mi, hangi tedaviler var? Uyarı işaretleri ve evde altı egzersiz.",
     "omuzda-kirec-birikmesi.html", NECK_CSS, CF_BODY, "",
     seo_title="Omuzda Kireç Birikmesi (Kalsifik Tendinit): Belirtiler, Tedavi ve Egzersizler | İhsan Eren",
     condition="Kalsifik tendinit", faq_items=CF_FAQ)

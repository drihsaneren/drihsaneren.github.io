# -*- coding: utf-8 -*-
# Yeni rehber (71): Uzun COVID'de hareket ve nefes. cond70_part.py'den sonra exec edilir. Video yok.
# Kaynaklar (24 Ekim 2026'da okundu): DSÖ post COVID-19 condition sayfası (2023 yaşayan kılavuzun 24. bölüm önerileri), NICE NG188 (25 Oca 2024),
# World Physiotherapy Briefing Paper 9 (Haz 2021, tam metin), Berry 2025 JAMA Netw Open (tam metin özeti), Glasgow Üniv. (10 Kas 2025), McGregor 2024 BMJ REGAIN (Hospital Healthcare Europe),
# DSÖ Avrupa kendi kendine rehabilitasyon broşürü (27 Eyl 2021, yalnızca tanıtım sayfası).

_ex2("lc_breath", "kb_breath", "Yavaş ve derin nefes", "Rahatça oturun, omuzlarınızı gevşetin, bir elinizi karnınıza koyun. Burnunuzdan yavaşça nefes alırken karnınızın şiştiğini hissedin, sonra ağzınızdan yavaşça verin. Nefesinizi zorlamayın.", "Birkaç dakika, gün içinde birkaç kez")
_ex2("lc_plb", "plb", "Büzük dudak nefesi", "Burnunuzdan nefes alın, sonra dudaklarınızı ıslık çalar gibi büzerek nefesinizi yavaşça, alıştan yaklaşık iki kat uzun sürede verin. Nefes darlığı sırasında ya da merdiven çıkarken kullanabilirsiniz.", "Nefes darlığı hissettiğinizde")
_ex2("lc_lean", "fwdlean", "Öne eğilerek toparlanma", "Nefesiniz daraldığında oturup öne eğilin, dirseklerinizi dizlerinize ya da bir masaya dayayın. Omuzlarınızı gevşetip yavaş nefes alıp verin; nefesiniz düzelince devam edin.", "Gerektiğinde")
_ex2("lc_sts", "sts", "Sandalyeden kalkıp oturma", "Sağlam bir sandalyeden kalkıp kontrollü şekilde oturun. Yalnızca egzersiz sonrası belirgin kötüleşme yaşamıyorsanız yapın; sayıyı o günkü enerjinize göre ayarlayın.", "Ertesi gün kötüleşme olmayacak kadar; örneğin 5 tekrarla başlayın")
_ex2("lc_push", "sk_push", "Duvar şınavı", "Ellerinizi göğüs hizasında duvara koyun, dirseklerinizi bükerek göğsünüzü duvara yaklaştırın ve geri itin. Oturarak ya da yatarak da kol egzersizleriyle başlanabilir.", "Belirtilerinize göre; az tekrarla başlayın")
_ex2("lc_walk", "walk", "Kısa yürüyüşler", "Ev içinde ya da yakın çevrede kısa yürüyüşler yapın. Belirtileriniz ertesi gün kötüleşmiyorsa süreyi çok az artırın; kötü günlerde azaltın.", "Belirtilere göre ayarlanan, kısa bölümler")

LC_FAQ = [
 ("Egzersiz beni kötüleştirir mi?", "Bazı kişilerde evet. Uzun COVID'li kişilerin bir kısmında bedensel, zihinsel ya da sosyal bir çabadan sonra, çoğu zaman 12 saat ya da daha geç, belirtiler belirgin kötüleşir; buna egzersiz sonrası belirti alevlenmesi denir. Dünya Fizyoterapi Konfederasyonu egzersiz önermeden önce bu durumun sorgulanmasını öneriyor. Sizde varsa egzersizi zorlamak yerine enerjinizi planlamak öncelikli olmalıdır."),
 ("Enerjiyi planlamak (pacing) ne demek?", "Etkinliklerinizi, belirtilerinizi alevlendirmeyecek bir sınırın içinde tutacak şekilde planlamaktır. Bu, hareketten kaçınmak değil; iyi günlerde de aşırıya kaçmadan, gün içine dinlenme araları koyarak ilerlemektir. Belirtiler artmaya başladığında durun, dinlenin ve planınızı yeniden düzenleyin. Bir günlük ya da uygulama, sınırınızı fark etmenize yardımcı olabilir."),
 ("Kademeli egzersiz tedavisi uygun mu?", "Egzersiz sonrası belirti alevlenmesi olan kişilerde önerilmiyor. Dünya Fizyoterapi Konfederasyonu, belirtilerden bağımsız olarak süre ya da yükü önceden belirlenmiş aralıklarla artıran programların uzun COVID'de kullanılmamasını, belirtilere göre sürekli ayarlanan hareketin tercih edilmesini öneriyor."),
 ("Egzersize başlamadan önce neler kontrol edilmeli?", "Dünya Sağlık Örgütü, egzersiz programına başlamadan önce çabayla oksijen düşmesinin ve kalp sorunlarının araştırılıp tedavi edilmesini güçlü şekilde öneriyor. Ayağa kalkınca baş dönmesi, çarpıntı ya da bayılma hissi varsa bu da değerlendirilmeli; bu durumda yatarak ya da oturarak yapılan egzersizlerle başlamak gerekebilir."),
 ("Egzersizin yararı gösterildi mi?", "Bazı gruplarda evet. İskoçya'da 233 kişiyle yapılan bir çalışmada 3 ay boyunca her gün yapılan kişiye özel direnç egzersizleri yürüme mesafesini olağan bakıma göre ortalama 36,5 metre artırdı, el kavrama gücünü, yaşam kalitesini, kaygı ve depresyon belirtilerini iyileştirdi; ancak yorgunluk ölçümlerinde fark yoktu. COVID nedeniyle hastanede yatmış 585 kişiyle yapılan başka bir çalışmada 8 haftalık çevrim içi grup egzersizi ve psikolojik destek, yaşam kalitesini bir yıl boyunca iyileştirdi."),
 ("Ne kadar sürer?", "Kişiden kişiye çok değişir. Dünya Sağlık Örgütü'nün aktardığı tahminlere göre 2021 sonuna kadar enfeksiyon geçirenlerin yaklaşık %3,7'sinde uzun COVID gelişti ve bunların %15'inde belirtiler 12 ay sonra hâlâ sürüyordu. Çoğu kişi zamanla düzelir; belirtilerin iniş çıkışlı olması olağandır."),
]

LC_SRC = [
 "World Health Organization. " + ext("https://www.who.int/teams/health-care-readiness/post-covid-19-condition", "Post COVID-19 condition") + ". Clinical management of COVID-19: living guideline (2023), bölüm 24: rehabilitasyon önerileri.",
 "National Institute for Health and Care Excellence. " + ext("https://nice.org.uk/guidance/ng188/resources/covid19-rapid-guideline-managing-thelongterm-effects-of-covid19-pdf-66142028400325", "COVID-19 rapid guideline: managing the long-term effects of COVID-19") + ". NICE guideline NG188. Last updated 25 January 2024.",
 "World Physiotherapy. " + ext("https://world.physio/sites/default/files/2021-07/Briefing-Paper-9-Long-Covid-FINAL-English-202107.pdf", "Safe rehabilitation approaches for people living with Long COVID: physical activity and exercise") + ". Briefing paper 9, June 2021.",
 "Berry C, McKinley G, Bayes HK, et al. " + ext("https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2841264", "Resistance exercise therapy after COVID-19 infection: a randomized clinical trial") + ". JAMA Netw Open. 2025;8(11):e2534304.",
 "University of Glasgow. " + ext("https://www.gla.ac.uk/news/headline_1224102_en.html", "Resistance exercise can improve physical and mental symptoms of Long Covid") + ". 10 November 2025.",
 "McGregor G, Sandhu H, Bruce J, et al. Clinical effectiveness of an online supervised group physical and mental health rehabilitation programme for adults with post-covid-19 condition (REGAIN study). BMJ. 2024;384:e076506. Özet: " + ext("https://hospitalhealthcare.com/clinical/respiratory/long-covid-quality-of-life-improved-via-online-group-rehab-research-suggests/", "Hospital Healthcare Europe, 12 February 2024") + ".",
 "WHO Regional Office for Europe. " + ext("https://www.who.int/europe/publications/i/item/WHO-EURO-2021-855-40590-59892", "Support for rehabilitation: self-management after COVID-19-related illness, second edition") + ". 27 September 2021.",
]

LC_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>Uzun COVID'de hareket ve nefes</h1>
    <p class="lede">COVID-19'dan sonra aylarca süren yorgunluk, nefes darlığı ve düşünmede güçlük yaşayan kişilerde hareket, iyileşmenin önemli bir parçası olabilir; ama yanlış dozda yapılırsa belirtileri alevlendirebilir. Bu rehber uzun COVID'in ne olduğunu, egzersize başlamadan önce nelere dikkat etmeniz gerektiğini, enerjinizi nasıl planlayacağınızı ve evde yapabileceğiniz hafif hareketleri anlatıyor.</p>
    <p class="meta">Son güncelleme: 24 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%3,7</b><span>2021 sonuna kadar COVID-19 geçirenlerde tahmini uzun COVID oranı (yaklaşık 145 milyon kişi)</span></div>
        <div class="stat"><b>%15</b><span>Bu kişilerden belirtileri 12 ay sonra hâlâ süren oran</span></div>
        <div class="stat"><b>+36,5 m</b><span>3 aylık kişiye özel direnç egzersiziyle yürüme testinde olağan bakıma göre ek artış</span></div>
        <div class="stat"><b>%17 / %8</b><span>8 haftalık çevrim içi grup programından 3 ay sonra sağlığını “çok daha iyi” bulanlar, karşılaştırma grubuna göre</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Uzun COVID nedir?</h2>
        <p class="soft">Dünya Sağlık Örgütü'nün tanımına göre uzun COVID (COVID-19 sonrası durum), enfeksiyonun başlamasından genellikle 3 ay sonra görülen, en az 2 ay süren ve başka bir hastalıkla açıklanamayan belirtilerdir. Belirtiler yeni ortaya çıkabilir ya da hastalıktan beri sürebilir; iniş çıkışlar ve yeniden alevlenmeler olağandır. İngiltere'nin kılavuzu (NICE) 4–12 hafta süren belirtileri “süregelen belirtili COVID-19”, 12 haftadan uzun sürenleri “COVID-19 sonrası sendrom” olarak adlandırıyor.</p>
        <p class="soft">En sık belirtiler yorgunluk, nefes darlığı ve dikkat ile hafızada güçlüktür; bunlar günlük hayatı belirgin şekilde etkileyebilir.</p>
      </div>
      <div>
        <h2>Egzersizden önce</h2>
        <p class="soft">Dünya Sağlık Örgütü ve Dünya Fizyoterapi Konfederasyonu, egzersize başlamadan önce şunların değerlendirilmesini öneriyor:</p>
        <ul class="dots">
          <li><b>Egzersiz sonrası belirti alevlenmesi:</b> Bedensel, zihinsel ya da sosyal bir çabadan sonra, çoğu zaman 12 saat ya da daha geç ortaya çıkan belirgin kötüleşme.</li>
          <li><b>Çabayla oksijen düşmesi:</b> Hafif bir çaba sırasında ya da sonrasında oksijen değerinin 3 puan ya da daha fazla düşmesi araştırılmalıdır.</li>
          <li><b>Kalp sorunları:</b> Göğüs ağrısı, çarpıntı ya da açıklanamayan nefes darlığı varsa önce kalp değerlendirmesi gerekir.</li>
          <li><b>Ayağa kalkınca baş dönmesi:</b> Çarpıntı, baş dönmesi ya da bayılma hissi varsa yatarak ya da oturarak yapılan egzersizlerle başlamak gerekebilir.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Enerjinizi planlayın</h2>
      <p class="soft">Egzersiz sonrası belirti alevlenmesi yaşayan kişilerde Dünya Sağlık Örgütü, enerjiyi koruma ve etkinlikleri planlama (pacing) eğitimini öneriyor; egzersizi bu kişilerde zorlamıyor. Yorgunluk için ise enerji planlamasıyla birlikte, belirtilere göre ayarlanan dikkatli bir egzersize dönüş öneriliyor.</p>
      <ul class="tx">
        <li><b>Dur</b><span>Belirtileriniz artmaya başladığında etkinliğe ara verin; sona kadar zorlamayın.</span></li>
        <li><b>Dinlen</b><span>Gün içine düzenli dinlenme araları koyun; yalnızca yorulduğunuzda değil, yorulmadan önce de dinlenin.</span></li>
        <li><b>Planla</b><span>Ağır işleri güne ve haftaya yayın, iyi günlerde de aşırıya kaçmayın. Bir günlükle hangi etkinliğin ertesi gün belirtileri artırdığını izleyin.</span></li>
      </ul>
      <div class="callout">
        <p>Dünya Fizyoterapi Konfederasyonu, uzun COVID'de belirtilerden bağımsız olarak süre ya da yükü düzenli aralıklarla artıran kademeli egzersiz programlarının kullanılmamasını, hareketin her gün belirtilere göre ayarlanmasını öneriyor.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Araştırmalar ne gösteriyor?</h2>
      <p class="soft">İskoçya'da en az 4 haftadır belirtileri süren 233 kişiyle yapılan randomize çalışmada, 3 ay boyunca her gün evde yapılan kişiye özel direnç egzersizleri (yatağa bağlı olanlar için yatarak, diğerleri için oturarak ya da ayakta; önce kol, üçüncü haftadan sonra bacak egzersizleri) yürüme testindeki mesafeyi olağan bakıma göre ortalama 36,5 metre artırdı. El kavrama gücü, yaşam kalitesi, kaygı ve depresyon belirtileri de iyileşti; yorgunluk ve nefes darlığı ölçümlerinde ise fark görülmedi.</p>
      <p class="soft">COVID-19 nedeniyle hastanede yatmış ve 3 aydan uzun süredir yakınmaları olan 585 kişiyle yapılan REGAIN çalışmasında, 8 hafta süren çevrim içi, denetimli grup egzersizi ve psikolojik destek programı yaşam kalitesini bir yıl boyunca iyileştirdi; 3. ayda sağlığını “çok daha iyi” bulanların oranı %17'ye karşı %8'di ve programın zarar verdiğine dair bir işaret görülmedi. Bu sonuçların hastanede yatmamış ve egzersiz sonrası belirgin alevlenme yaşayan kişilere ne ölçüde uyduğu bilinmiyor.</p>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Uzun COVID için altı hafif hareket</h2>
      <p class="soft">İlk üç hareket nefes darlığını yönetmeye, son üçü güç ve dayanıklılığı yavaşça geri kazanmaya yöneliktir. Son üç hareketi yalnızca egzersiz sonrası belirti alevlenmesi yaşamıyorsanız ya da sağlık ekibiniz uygun gördüyse yapın. Dozu her gün belirtilerinize göre ayarlayın: ertesi gün belirtileriniz artıyorsa bir sonraki sefer azaltın.</p>
      {ex_grid(["lc_breath", "lc_plb", "lc_lean", "lc_sts", "lc_push", "lc_walk"])}
      <p class="soft" style="margin-top:14px">Rahatlamak için <a href="ic-cekis.html">iç çekiş nefesine</a>, belirtilerinizi izlemek için <a href="agri-gunlugu.html">ağrı günlüğüne</a> bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(LC_FAQ)}
      <p class="soft" style="margin-top:18px">Yoğun bakımda yatmış olanlar için <a href="yogun-bakim-sonrasi.html">yoğun bakım sonrası iyileşme</a>, nefes darlığı için <a href="koah.html">akciğer rehabilitasyonu</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">“Acil” yazan durumlarda 112'yi arayın:</p>
      <ul class="dots redflags">
        <li>Göğüs ağrısı, ani ya da giderek artan nefes darlığı (acil)</li>
        <li>Bayılma ya da bilinç bulanıklığı (acil)</li>
        <li>Kendinize zarar verme ya da yaşamınıza son verme düşünceleri (acil)</li>
        <li>Hafif bir çabayla oksijen değerinin belirgin düşmesi, çarpıntı ya da ayağa kalkınca bayılacak gibi olma: hekiminize</li>
      </ul>
      {CTA_CARD("Uzun COVID'de hareket ve nefes", "uzun COVID'de rehabilitasyon")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(LC_SRC)}
    </div>
  </section>
</main>'''

page("uzun-covid.html", "Uzun COVID'de Hareket ve Nefes",
     "Uzun COVID'de hareket ve nefes: egzersiz sonrası belirti alevlenmesi, egzersizden önce kontrol edilmesi gerekenler, enerji planlaması, araştırmalar ve evde altı hafif hareket.",
     "uzun-covid.html", NECK_CSS, LC_BODY, "",
     seo_title="Uzun COVID'de Hareket ve Nefes: Güvenli Egzersiz ve Enerji Planlaması | İhsan Eren",
     condition="Uzun COVID (COVID-19 sonrası durum)", faq_items=LC_FAQ)

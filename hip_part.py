# -*- coding: utf-8 -*-
# Kalça kireçlenmesi sayfası. desk_part.py'den sonra exec edilir.

# Tezgâha tutunarak kalçayı arkaya açma (yandan)
SV["hext"] = fig(GRD + COUNTER_R +
    '<circle class="hd" cx="50" cy="20" r="7"/><path d="M56 18 L61 21 L56 23 Z" fill="#2A6F6B"/>'
    '<path class="fig" d="M50 28 L50 70 M50 38 L68 50 L84 60"/>'
    '<path class="fig" d="M50 70 L50 108 L60 110"/>'
    f'<path class="fig hl" d="M50 70 L50 108 L58 110">{anim_d("M50 70 L50 108 L58 110;M50 70 L36 104 L42 110;M50 70 L50 108 L58 110")}</path>',
    "Kalçayı arkaya açma")

# Tezgâha tutunarak kalçayı yana açma (önden)
SV["sabd"] = fig(GRD +
    '<path class="obj" d="M12 64 H108"/>'
    '<circle class="hd" cx="60" cy="20" r="8"/><path class="fig" d="M44 38 H76 M60 30 V78 M44 38 L40 64 M76 38 L80 64"/>'
    '<path class="fig" d="M60 78 L54 112"/>'
    f'<path class="fig hl" d="M60 78 L66 112">{anim_d("M60 78 L66 112;M60 78 L84 106;M60 78 L66 112")}</path>',
    "Kalçayı yana açma")

EXT.update({
 "hext": ("Kalçayı arkaya açma", "Tezgâha tutunarak dik durun. Dizinizi düz tutarak bir bacağınızı yavaşça geriye doğru uzatın; belinizi çukurlaştırmadan kalçanızı sıkın. Yavaşça başlangıca dönün.", "Her bacakla 10 tekrar"),
 "sabd": ("Kalçayı yana açma", "Tezgâha önden tutunun. Gövdenizi dik tutarak bir bacağınızı ayak ucunuz öne bakacak şekilde yana doğru açın, yavaşça geri getirin. Kalçanın yan kasları yürürken dengeyi sağlar.", "Her bacakla 10–15 tekrar"),
})
SV["bridge3"] = SV["bridge"]; EXT["bridge3"] = ("Köprü", "Sırtüstü yatın, dizleriniz bükülü, ayaklarınız yerde olsun. Kalçanızı sıkarak yerden kaldırın; omuzlarınızdan dizlerinize kadar düz bir çizgi oluşsun. 3–5 saniye bekleyip yavaşça inin.", "10–15 tekrar, günde 1–2 kez")
SV["abd2"] = SV["abd"]; EXT["abd2"] = EXT["abd"]
SV["sts5"] = SV["sts"]; EXT["sts5"] = EXT["sts"]
SV["k2c2"] = SV["k2c"]; EXT["k2c2"] = ("Dizi göğse çekme", "Sırtüstü yatın. Bir dizinizi iki elinizle tutup ağrısız aralıkta göğsünüze doğru yavaşça çekin, kalçanızda hafif bir gerilme hissedin. Sonra diğer bacakla tekrarlayın. Kalça protezi olanlar bu hareketi cerrahına danışmadan yapmamalıdır.", "20–30 saniye, her bacakla 3 kez")

KALCA_FAQ = [
 ("Kalça kireçlenmesinde yürümek zararlı mı?", "Hayır. Egzersiz ve düzenli hareket kireçlenmede tedavinin temelidir. Ağrıyı belirgin artırmayacak bir mesafe ve tempoyla yürüyün; ağrılı dönemlerde süreyi kısaltıp sıklığı artırın. Bisiklet ve suda egzersiz de eklemi daha az yükleyen iyi seçeneklerdir."),
 ("Egzersiz gerçekten işe yarıyor mu?", "2026'da güncellenen Cochrane derlemesine (18 çalışma, 1.368 kişi) göre egzersiz kalça kireçlenmesinde ağrıyı, tedavi almayanlara ya da olağan bakıma göre 100 üzerinden yaklaşık 7 puan azaltıyor; bu, günlük hayatta fark edilebilir kabul edilen 12 puanın altında. İşlevde de benzer küçük bir iyileşme görülüyor. Buna rağmen yan etkisi az ve genel sağlığa pek çok faydası olduğu için Amerikan Romatoloji Koleji egzersizi güçlü şekilde öneriyor. Egzersiz; kilo kontrolü, baston ve hastalığı doğru anlamakla birlikte bir tedavi paketinin parçasıdır. İngiltere’nin 2022 kılavuzu (NICE) da herkese kişiye göre ayarlanmış egzersiz, fazla kilosu olanlara kilo vermeyi (az miktarda kilo kaybı bile yararlı) ve gerekirse baston öneriyor; tanı için genellikle görüntüleme gerekmediğini, glukozamin ve güçlü opioidlerin önerilmediğini belirtiyor. 2026'da yayımlanan ve 5 sistematik derleme ile 28 randomize çalışmayı bir araya getiren bir şemsiye derlemede de egzersizin kalça ağrısına etkisi ihmal edilebilir düzeyde bulundu; yazarlar egzersizin genel sağlığa yararlarını ve hastaların tercihini göz ardı etmeden ortak karar verilmesini öneriyor."),
 ("Glukozamin ya da eklem iğneleri işe yarar mı?", "Amerikan Romatoloji Koleji'nin kılavuzu kalça kireçlenmesinde glukozamin, kondroitin, hyaluronik asit iğnesi, PRP ve kök hücre iğnelerine karşı güçlü öneride bulunuyor. Ultrason eşliğinde yapılan kortizon iğnesi ise kısa süreli rahatlama için önerilen seçeneklerden biridir."),
 ("Baston hangi elde tutulur?", "Ağrılı kalçanın karşı tarafındaki elde. Baston ağrılı bacakla aynı anda yere basar ve kalçanın taşıdığı yükü azaltır. Boyunun doğru ayarlanması önemlidir."),
 ("Kalça protezi ne zaman gerekir?", "Egzersiz, kilo kontrolü ve ilaç tedavisine rağmen ağrı ve kısıtlılık günlük yaşamı ciddi şekilde bozuyorsa ortopedi değerlendirmesi gerekir. Karar yalnızca röntgene göre değil, yaşam kalitenize göre verilir. NICE kılavuzuna göre protez için sevk kararında yaş, cinsiyet, sigara, eşlik eden hastalıklar ya da fazla kilo tek başına engel sayılmamalıdır."),
 ("Kalça protezi ne kadar dayanır?", "Avustralya ve Finlandiya ulusal kayıtlarını inceleyen bir analizde kalça protezlerinin %89'u 15 yıl boyunca yenilenmeden dayandı; 25 yıllık veriler yalnızca Finlandiya kaydından geldi ve bu kayda göre protezlerin yaklaşık %58'i 25 yıl dayandı. Bu protezlerin bir kısmı bugün kullanılan modellerden farklıdır."),
 ("Röntgenim temiz ama kalçam ağrıyor; kireçlenme olabilir mi?", "Olabilir. ABD'deki iki büyük toplum çalışmasında sık ağrıyan kalçaların yalnızca %9–16'sında röntgende kireçlenme görüldü; röntgende kireçlenmesi olan kalçaların da yalnızca %21–24'ü sık ağrıyordu. Araştırmacılar yalnızca röntgene bakılırsa kalça kireçlenmesinin gözden kaçabileceğini belirtiyor. Bu yüzden tanıda öykü ve muayene önemlidir."),
]

KALCA_SRC = [
 "Altman R, et al. " + ext("https://www.qxmd.com/r/2025304", "The American College of Rheumatology criteria for the classification and reporting of osteoarthritis of the hip") + ". Arthritis Rheum. 1991.",
 "Evans JT, Evans JP, Walker R, et al. " + ext("https://read.qxmd.com/read/30782340/how-long-does-a-hip-replacement-last-a-systematic-review-and-meta-analysis-of-case-series-and-national-registry-reports-with-more-than-15-years-of-follow-up", "How long does a hip replacement last? A systematic review and meta-analysis of case series and national registry reports with more than 15 years of follow-up") + ". Lancet. 2019;393:647-654. Özet: " + ext("https://evidence.nihr.ac.uk/alert/more-than-50-of-hip-replacements-appear-to-last-25-years/", "NIHR Evidence") + ".",
 "GBD 2021 Osteoarthritis Collaborators. " + ext("https://openaccess.sgul.ac.uk/id/eprint/115643", "Global, regional, and national burden of osteoarthritis, 1990–2020 and projections to 2050: a systematic analysis for the Global Burden of Disease Study 2021") + ". Lancet Rheumatol. 2023;5(9):e508-e522.",
 "Kim C, Nevitt MC, Niu J, et al. " + ext("https://escholarship.org/uc/item/3mh786tk", "Association of hip pain with radiographic evidence of hip osteoarthritis: diagnostic test study") + ". BMJ. 2015;351:h5983.",
 "Learmonth ID, Young C, Rorabeck C. " + ext("https://ouci.dntb.gov.ua/works/4EoJXwx9", "The operation of the century: total hip replacement") + ". Lancet. 2007:1508-1519.",
 "Skou ST, Roos EM. " + ext("https://link.springer.com/article/10.1186/s12891-017-1439-y", "Good Life with osteoArthritis in Denmark (GLA:D™): evidence-based education and supervised neuromuscular exercise delivered by certified physiotherapists nationwide") + ". BMC Musculoskelet Disord. 2017;18:72.",
 "Wrightington, Wigan and Leigh Teaching Hospitals NHS Foundation Trust. " + ext("https://www.wwl.nhs.uk/pioneer-of-hip-replacement-surgery", "Pioneer of hip replacement surgery: Sir John Charnley") + ".",
 "Hall M, Lawford BJ, et al. " + ext("https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD007912.pub3/full", "Exercise for osteoarthritis of the hip") + ". Cochrane Database Syst Rev. 2026;CD007912. Özet: " + ext("https://canada.cochrane.org/news/exercise-helps-hip-arthritis-pain-perhaps-less-we-thought", "Cochrane Canada, 23 July 2026") + ".",
 "Kolasinski SL, Neogi T, Hochberg MC, et al. " + ext("https://acrjournals.onlinelibrary.wiley.com/doi/10.1002/acr.24131", "2019 American College of Rheumatology/Arthritis Foundation guideline for the management of osteoarthritis of the hand, hip, and knee") + ". Arthritis Care Res (Hoboken). 2020;72(2):149-162. Özetler: " + ext("https://www.aafp.org/pubs/afp/issues/2021/0115/p120.html", "American Family Physician, 2021") + "; " + ext("https://rheumnow.com/content/acr-arthritis-foundation-treatment-guidelines-osteoarthritis", "RheumNow") + ".",
 ext("https://www.arthroplastytoday.org/article/S2352-3441(17)30073-0/fulltext", "Don't forget the hip! Hip arthritis masquerading as knee pain") + ". Arthroplasty Today. 2017.",
 "Physiopedia. " + ext("https://www.physio-pedia.com/Hip_Osteoarthritis", "Hip Osteoarthritis") + ".",
 "National Institute for Health and Care Excellence. " + ext("https://www.nice.org.uk/guidance/ng226/chapter/Recommendations", "Osteoarthritis in over 16s: diagnosis and management") + ". NICE guideline NG226, 19 October 2022.",
 "Schleimer T, Teichert F, Henriksen M, et al. Effectiveness of exercise therapy for osteoarthritis: an overview of systematic reviews and randomised controlled trials. RMD Open. 2026;12(1):e006275. Özet: " + ext("https://bmjgroup.com/effectiveness-of-exercise-to-ease-osteoarthritis-symptoms-likely-minimal-and-transient/", "BMJ Group, 17 February 2026") + ".",
]

KALCA_TL = [
 ("1962", "İngiltere'de cerrah John Charnley, Wrightington Hastanesi'nde geliştirdiği total kalça protezi ameliyatını uygulamaya koydu. Yöntemi bir yıl önce The Lancet'te \"yeni bir ameliyat\" olarak tanıtmıştı."),
 ("1991", "Amerikan Romatoloji Koleji, kalça ağrısı olan 201 hastanın verisine dayanarak kalça kireçlenmesi için sınıflandırma ölçütlerini yayımladı: kalça ağrısıyla birlikte kalçanın içe dönüş açısı, içe dönerken ağrı, sabah tutukluğunun 1 saati geçmemesi ve 50 yaş üstü gibi bulgular birlikte değerlendirildi."),
 ("2007", "The Lancet'te yayımlanan bir derleme, total kalça protezini \"yüzyılın ameliyatı\" olarak tanımladı."),
 ("2015", "ABD'deki iki büyük toplum çalışmasında kalça ağrısı ile röntgendeki kireçlenme arasında zayıf bir uyum bulundu: sık ağrıyan kalçaların çoğunda röntgende kireçlenme yoktu."),
 ("2017", "Danimarka'daki GLA:D programında (bilgilendirme ve fizyoterapist eşliğinde egzersiz) kalça kireçlenmesi olanların ağrısı 3. ayda 100 üzerinden ortalama 11 puan azaldı; karşılaştırma grubu olmayan bir çalışmaydı."),
 ("2019", "Avustralya ve Finlandiya ulusal kayıtlarını inceleyen bir analizde kalça protezlerinin %89'u 15 yıl, Finlandiya kaydına göre yaklaşık %58'i 25 yıl yenilenmeden dayandı."),
 ("2020", "Amerikan Romatoloji Koleji ve Artrit Vakfı'nın 2019 kılavuzu yayımlandı: egzersiz, fazla kilolularda kilo verme, tai chi ve baston güçlü şekilde önerildi; kalçaya hyaluronik asit, PRP ve kök hücre iğnelerine ve TENS'e karşı güçlü öneri yapıldı."),
 ("2022", "İngiltere'nin NICE kılavuzu güncellendi: kişiye göre ayarlanmış egzersiz herkese öneriliyor, tanı genellikle görüntüleme gerekmeden konuyor ve protez sevkinde yaş ya da kilo tek başına engel sayılmıyor."),
 ("2026", "Kalça kireçlenmesinde egzersizi inceleyen Cochrane derlemesi güncellendi (18 çalışma, 1.368 kişi): ağrıdaki azalma, tedavi almayanlara ya da olağan bakıma göre 100 üzerinden yaklaşık 7 puandı. Yazarlar, yararın beklenenden küçük olabileceğini ama egzersizin düşük maliyetli ve düşük riskli bir seçenek olarak kaldığını belirtiyor."),
]

KALCA_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Kalça kireçlenmesi (koksartroz)</h1>
    <p class="lede">Kalça eklemindeki kıkırdağın zamanla incelmesiyle ortaya çıkar. Ağrı çoğunlukla kasıkta hissedilir; çorap giymek, ayakkabı bağlamak ve arabaya binmek zorlaşabilir. Egzersiz, fazla kiloluysanız kilo vermek ve gerektiğinde baston gibi yardımcılar günlük hayatı kolaylaştırabilir; ağrı ve kısıtlılık çok belirginse kalça protezi bir seçenektir.</p>
    <p class="meta">Son güncelleme: 31 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>Kasık</b><span>Ağrının en sık hissedildiği bölge; uyluğa, kalçanın arkasına ve dize yayılabilir</span></div>
        <div class="stat"><b>%78,6</b><span>2020–2050 arasında dünyada kalça kireçlenmesi vakalarında beklenen artış</span></div>
        <div class="stat"><b>Güçlü öneri</b><span>Egzersiz, kilo verme, Tai Chi ve gerektiğinde baston (Amerikan Romatoloji Koleji)</span></div>
        <div class="stat"><b>Karşı öneri</b><span>Glukozamin, hyaluronik asit, PRP ve kök hücre iğneleri</span></div>
      </div>
      {g_toc([("nedir", "Nedir?"), ("tani", "Tanı ve röntgen"), ("diz", "Ağrı dizde olabilir"), ("tarihce", "Geçmişten bugüne"), ("tedavi", "Tedavi seçenekleri"), ("egzersizler", "Egzersizler"), ("gunluk", "Günlük hayatta"), ("videolar", "Videolar"), ("sss", "Sık sorulan sorular"), ("uyari", "Uyarı işaretleri")])}
    </div>
  </section>

  <section id="nedir">
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Kalça, uyluk kemiğinin başı ile leğen kemiğindeki çukurun oluşturduğu bir top-yuva eklemidir. Kireçlenmede eklem yüzeylerini kaplayan kıkırdak incelir, eklem kenarlarında kemik çıkıntıları oluşur ve eklemin hareketi, özellikle içe dönüşü, kısıtlanır.</p>
        <p class="soft">Tanı çoğu zaman öykü ve muayeneyle konur; görüntüleme her zaman gerekmez. Ayrıntılar aşağıdaki "Tanı ve röntgen" bölümünde. Kasık ağrısının başka nedenleri de olabilir; örneğin: <a href="kalca-sikismasi.html">Kalça sıkışması →</a></p>
      </div>
      <div>
        <h2>Belirtiler ve risk etkenleri</h2>
        <ul class="dots">
          <li>Kasıkta, uyluğun önünde ya da kalçanın dış yanında hareketle artan ağrı</li>
          <li>Sabah ya da uzun oturduktan sonra kısa süren tutukluk</li>
          <li>Çorap giyme, ayakkabı bağlama, arabaya binip inmede zorlanma</li>
          <li>Topallama, yürüme mesafesinde azalma</li>
          <li>Risk etkenleri: ileri yaş, fazla kilo, ailede kireçlenme, önceki kalça yaralanması, doğuştan kalça çıkığı (displazi) ya da kalça sıkışması</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="tani">
    <div class="wrap">
      <h2>Tanı nasıl konur? Röntgen ne anlatır?</h2>
      <p class="soft">İngiltere'nin NICE kılavuzuna göre 45 yaş ve üstünde, hareketle artan eklem ağrısı olan ve sabah tutukluğu hiç olmayan ya da 30 dakikayı geçmeyen kişilerde kireçlenme tanısı görüntüleme gerekmeden konabilir. Görüntüleme, belirtiler alışılmışın dışındaysa ya da başka bir neden düşünülüyorsa istenir. Muayenede kalçanın içe dönüşündeki kısıtlılık ve bu hareketle ortaya çıkan ağrı tanıya yardımcı olur.</p>
      <div class="stats" style="margin-top:14px">
        <div class="stat"><b>%9–16</b><span>Sık ağrıyan kalçalar içinde röntgende kireçlenme görülenler</span></div>
        <div class="stat"><b>%21–24</b><span>Röntgende kireçlenme görülen kalçalar içinde sık ağrıyanlar</span></div>
      </div>
      <div class="callout">
        <p>Bu sayılar ABD'de iki büyük toplum çalışmasından (Framingham ve Osteoarthritis Initiative; 946 ve 4.366 kişi) geliyor. Kalça ağrısı ile röntgendeki görüntü çoğu zaman örtüşmüyor: araştırmacılar yalnızca röntgene bakılırsa kalça kireçlenmesinin gözden kaçabileceğini belirtiyor. Tersine, röntgende kireçlenme görülmesi de ağrının tek açıklaması olmayabilir.</p>
      </div>
    </div>
  </section>

  <section id="diz">
    <div class="wrap">
      <h2>Ağrı dizde, sorun kalçada olabilir</h2>
      <p class="soft">Kalça kireçlenmesinin ağrısı yalnızca kasıkta hissedilmez; uyluk boyunca dize yayılabilir. Bazı hastalar yalnızca diz ağrısı tarif eder ve sorun kalçada olduğu hâlde dizi araştırılır.</p>
      <div class="callout">
        <p>Dizinizde ağrı var ama diz muayenesi ve görüntülemesi ağrıyı açıklamıyorsa, kalçanın da değerlendirilmesi gerekir. Fizyoterapi değerlendirmesinde kalçanın hareket açıklığına mutlaka bakılır.</p>
      </div>
    </div>
  </section>

  <section id="tarihce">
    <div class="wrap">
      <p class="eyebrow">Geçmişten bugüne</p>
      <h2>Kalça kireçlenmesinin kısa tarihi</h2>
      <p class="soft">1960'larda yaygınlaşan kalça protezi ileri kireçlenmede yaşamı değiştiren bir tedavi oldu. Son yıllarda araştırmalar, ameliyattan önceki dönemde egzersizin ve hastalığı doğru anlamanın yerini ve sınırlarını daha net ortaya koydu.</p>
      {g_tl(KALCA_TL)}
    </div>
  </section>

  <section id="tedavi">
    <div class="wrap">
      <h2>Tedavi</h2>
      <p class="soft">Amerikan Romatoloji Koleji'nin kılavuzu tedavinin merkezine egzersizi, kilo kontrolünü ve hastalığın kişi tarafından yönetilmesini koyuyor.</p>
      <ul class="tx">
        <li><b>Egzersiz</b><span>Güçlü şekilde önerilir. 2026'da güncellenen Cochrane derlemesine göre ağrı ve işlevdeki ortalama iyileşme küçük olsa da (ağrıda tedavi almayanlara göre 100 üzerinden yaklaşık 7 puan), egzersiz yan etkisi az ve genel sağlığa pek çok faydası olan bir tedavidir. Kalça çevresi kaslarını güçlendiren ve hareket açıklığını koruyan bir program önerilir.</span></li>
        <li><b>Kilo kontrolü</b><span>Fazla kilolu kişilerde kilo vermek güçlü şekilde önerilir. %5'lik bir kilo kaybı bile kalça ağrısında fark yaratabilir; NICE'a göre %10 kilo kaybı %5'ten muhtemelen daha yararlıdır.</span></li>
        <li><b>Tai Chi ve öz yönetim</b><span>Tai Chi ve hastalığı tanıyıp kendi kendine yönetmeyi öğreten programlar kılavuzda güçlü şekilde önerilen yöntemler arasındadır.</span></li>
        <li><b>Baston</b><span>Kireçlenme yürümeyi, eklem dengesini ya da ağrıyı belirgin etkiliyorsa baston güçlü şekilde önerilir.</span></li>
        <li><b>İlaçlar ve iğne</b><span>Hekiminizin önerdiği ağız yoluyla alınan iltihap giderici ağrı kesiciler ve ultrason eşliğinde yapılan kortizon iğnesi kılavuzda yer alır.</span></li>
        <li><b>Protez ameliyatı</b><span>Ameliyatsız tedaviye rağmen ağrı ve kısıtlılık yaşam kalitesini ciddi şekilde bozuyorsa düşünülür. <a href="protez-sonrasi.html">Protez sonrası rehbere göz atın →</a></span></li>
      </ul>
      <div class="callout">
        <p><strong>Amerikan kılavuzunda karşı öneri yapılanlar:</strong> glukozamin ve kondroitin takviyeleri, kalçaya hyaluronik asit, PRP ya da kök hücre iğneleri ve TENS.</p>
      </div>
      <h3 class="g-h3">Tedavi seçenekleri: kılavuzlar ne diyor?</h3>
      <p class="soft">Amerikan Romatoloji Koleji ve Artrit Vakfı'nın (ACR, 2019) kılavuzu ile İngiltere'nin NICE kılavuzunun (2022) kalça kireçlenmesi için önerileri yan yana. ACR önerilerinde "güçlü" ve "koşullu" ayrımı yapıyor; NICE ise "önerilir", "düşünülebilir" ve "önerilmez" ifadelerini kullanıyor. Kılavuzlar her konuda aynı fikirde değil; tedavi kişiye göre seçilir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Egzersiz</h3><dl><dt>ACR</dt><dd>Güçlü öneri; tai chi de güçlü, denge egzersizleri koşullu öneriliyor.</dd><dt>NICE</dt><dd>Herkese kişiye göre ayarlanmış egzersiz; düzenli egzersizin başta ağrı ya da rahatsızlık yapsa bile eklemlere yararlı olacağı anlatılmalı.</dd><dt>Kanıt</dt><dd>Ağrıda 100 üzerinden yaklaşık 7 puanlık azalma (Cochrane, 2026); fark edilebilir kabul edilen sınırın altında.</dd></dl></div>
        <div class="kind"><h3>Kilo verme</h3><dl><dt>ACR</dt><dd>Fazla kilolu ya da obez kişilerde güçlü öneri.</dd><dt>NICE</dt><dd>Kilo vermenin yaşam kalitesini ve işlevi iyileştireceği, ağrıyı azaltacağı anlatılmalı; %10 kilo kaybı muhtemelen %5'ten daha iyi.</dd></dl></div>
        <div class="kind"><h3>Baston ve destekler</h3><dl><dt>ACR</dt><dd>Baston güçlü öneriliyor.</dd><dt>NICE</dt><dd>Baston gibi yürüme yardımcıları düşünülebilir. Tabanlık, destek, bant ve ateller, eklemde dengesizlik gibi özel bir durum yoksa rutin olarak önerilmiyor.</dd></dl></div>
        <div class="kind"><h3>Manuel terapi</h3><dl><dt>ACR</dt><dd>Kalça ve diz kireçlenmesinde karşı koşullu öneri.</dd><dt>NICE</dt><dd>Yalnızca egzersizle birlikte düşünülebilir; tek başına kullanımını destekleyen yeterli kanıt yok.</dd></dl></div>
        <div class="kind"><h3>Akupunktur</h3><dl><dt>ACR</dt><dd>Koşullu öneri.</dd><dt>NICE</dt><dd>Akupunktur ve kuru iğneleme önerilmiyor.</dd><dt>Not</dt><dd>Türkiye'de yalnızca yetkili hekimler uygulayabilir.</dd></dl></div>
        <div class="kind"><h3>Elektroterapi</h3><dl><dt>ACR</dt><dd>Kalça ve dizde TENS'e karşı güçlü öneri.</dd><dt>NICE</dt><dd>Yararına dair yeterli kanıt olmadığı için elektroterapi tedavileri önerilmiyor.</dd></dl></div>
        <div class="kind"><h3>Eklem içi iğneler</h3><dl><dt>ACR</dt><dd>Kalçaya kortizon iğnesi güçlü öneri; hyaluronik asit, PRP ve kök hücre iğnelerine karşı güçlü öneri.</dd><dt>NICE</dt><dd>Kortizon iğnesi diğer tedaviler etkisiz ya da uygun değilse düşünülebilir; yalnızca kısa süreli (2–10 hafta) rahatlama sağlar. Hyaluronik asit iğnesi önerilmiyor.</dd></dl></div>
        <div class="kind"><h3>Protez ameliyatı</h3><dl><dt>NICE</dt><dd>Sevk kararı puanlama sistemleriyle değil klinik değerlendirmeyle verilmeli; yaş, cinsiyet, sigara, eşlik eden hastalıklar ya da fazla kilo tek başına engel sayılmamalı.</dd></dl></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Kalça için altı egzersiz</h2>
      <p class="soft">Egzersiz sırasında hafif bir ağrı olabilir; ağrı ertesi gün artmıyorsa devam etmek güvenlidir. Ertesi gün belirgin artış olursa tekrar sayısını azaltın. Ayakta yapılan hareketlerde sağlam bir yere tutunun.</p>
      {ex_grid(["bridge3", "abd2", "sts5", "k2c2", "hext", "sabd"])}
    </div>
  </section>

  <section id="gunluk">
    <div class="wrap two">
      <div>
        <h2>Günlük hayatta kalçanız için</h2>
        <p class="soft">Kalçayı korumak, onu hareketsiz bırakmak değil, yükünü akıllıca dağıtmaktır.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Haftanın çoğu günü yürüyün; bisiklet ve suda egzersiz iyi alternatiflerdir.</li>
        <li>Alçak koltuklar yerine yüksek ve kollu sandalyeler tercih edin.</li>
        <li>Uzun saplı ayakkabı çekeceği ve çorap giyme aparatı eğilmeyi azaltır.</li>
        <li>Arabaya binerken önce oturup sonra iki bacağınızı birlikte içeri alın.</li>
        <li>Uzun süre aynı pozisyonda oturmayın; kısa aralarla kalkıp yürüyün.</li>
      </ul>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Kalça kireçlenmesi için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("7HRV0y7pRUY", "Kalça kireçlenmesi tedavileri videosunu oynat", "Hip Pain/Arthritis? 8 Strongly Recommended Treatments by Experts")}
          <h3>Kalça kireçlenmesinde önerilen sekiz tedavi</h3>
          <p>Amerikan Romatoloji Koleji kılavuzundaki güçlü önerilerin anlatımı.</p>
        </div>
        <div class="vid">
          {vbox("eV-GtsPkgFk", "Kalça ağrısı programı videosunu oynat", "Introduction to the Complete Program for Treatment of Hip Pain")}
          <h3>Kalça ağrısı için egzersiz programı</h3>
          <p>Kalça ağrısında evde uygulanabilecek bir programa giriş.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section id="sss">
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(KALCA_FAQ)}
    </div>
  </section>

  <section id="uyari">
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlar kireçlenme dışında bir soruna işaret edebilir. Beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Düşme sonrası kalça ağrısı ve bacağa yük verememe (kalça kırığı olabilir)</li>
        <li>Kalçada ani başlayan şiddetli ağrıyla birlikte ateş, titreme</li>
        <li>Uzun süre kortizon kullanımı ya da yoğun alkol kullanımı olan genç bir kişide yeni başlayan kalça ağrısı (kemik dolaşım bozukluğu olabilir)</li>
        <li>Dinlenmekle geçmeyen gece ağrısı, nedensiz kilo kaybı ya da kanser öyküsü</li>
        <li>Bacağa yayılan ağrıyla birlikte uyuşma ya da güç kaybı (bel kaynaklı olabilir)</li>
      </ul>
      {CTA_CARD("Kalça ağrınız ve kireçlenmeniz", "kalça kireçlenmesi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(KALCA_SRC)}
    </div>
  </section>
</main>'''

page("kalca-kireclenmesi.html", "Kalça Kireçlenmesi",
     "Kalça kireçlenmesi (koksartroz) nedir, tanı nasıl konur, röntgen ağrıyı açıklar mı, ağrı neden dize vurur? Egzersizin gerçek etkisi, ACR ve NICE kılavuzlarının karşılaştırması, kısa tarihçe, evde altı egzersiz ve uyarı işaretleri.",
     "kalca-kireclenmesi.html", NECK_CSS, KALCA_BODY, YT_JS,
     seo_title="Kalça Kireçlenmesi (Koksartroz): Belirtiler, Egzersizler ve Tedavi | İhsan Eren",
     condition="Kalça kireçlenmesi (koksartroz)", about=cond("Kalça kireçlenmesi (koksartroz)"),
     faq_items=pick(KALCA_FAQ, 0, 1, 2, 3))

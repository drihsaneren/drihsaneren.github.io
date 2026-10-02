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
 ("Egzersiz gerçekten işe yarıyor mu?", "2026'da güncellenen Cochrane derlemesine göre egzersiz kalça kireçlenmesinde ağrıyı ve işlevi hafifçe iyileştiriyor; ortalama etki küçük. Buna rağmen yan etkisi az ve genel sağlığa pek çok faydası olduğu için Amerikan Romatoloji Koleji egzersizi güçlü şekilde öneriyor. Egzersiz; kilo kontrolü, baston ve hastalığı doğru anlamakla birlikte bir tedavi paketinin parçasıdır."),
 ("Glukozamin ya da eklem iğneleri işe yarar mı?", "Amerikan Romatoloji Koleji'nin kılavuzu kalça kireçlenmesinde glukozamin, kondroitin, hyaluronik asit iğnesi, PRP ve kök hücre iğnelerine karşı güçlü öneride bulunuyor. Ultrason eşliğinde yapılan kortizon iğnesi ise kısa süreli rahatlama için önerilen seçeneklerden biridir."),
 ("Baston hangi elde tutulur?", "Ağrılı kalçanın karşı tarafındaki elde. Baston ağrılı bacakla aynı anda yere basar ve kalçanın taşıdığı yükü azaltır. Boyunun doğru ayarlanması önemlidir."),
 ("Kalça protezi ne zaman gerekir?", "Egzersiz, kilo kontrolü ve ilaç tedavisine rağmen ağrı ve kısıtlılık günlük yaşamı ciddi şekilde bozuyorsa ortopedi değerlendirmesi gerekir. Karar yalnızca röntgene göre değil, yaşam kalitenize göre verilir."),
]

KALCA_SRC = [
 "Hall M, et al. " + ext("https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD007912.pub3/full", "Exercise for osteoarthritis of the hip") + ". Cochrane Database Syst Rev. 2026;CD007912.",
 "Kolasinski SL, Neogi T, Hochberg MC, et al. " + ext("https://acrjournals.onlinelibrary.wiley.com/doi/10.1002/acr.24131", "2019 American College of Rheumatology/Arthritis Foundation guideline for the management of osteoarthritis of the hand, hip, and knee") + ". Arthritis Care Res (Hoboken). 2020;72(2):149-162.",
 ext("https://www.arthroplastytoday.org/article/S2352-3441(17)30073-0/fulltext", "Don't forget the hip! Hip arthritis masquerading as knee pain") + ". Arthroplasty Today. 2017.",
 "Physiopedia. " + ext("https://www.physio-pedia.com/Hip_Osteoarthritis", "Hip Osteoarthritis") + ".",
]

KALCA_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Kalça kireçlenmesi (koksartroz)</h1>
    <p class="lede">Kalça eklemindeki kıkırdağın zamanla incelmesiyle ortaya çıkar. Ağrı çoğunlukla kasıkta hissedilir; çorap giymek, ayakkabı bağlamak ve arabaya binmek zorlaşabilir. Egzersiz, kilo kontrolü ve doğru yardımcılarla birçok kişi uzun yıllar aktif kalabilir.</p>
    <p class="meta">Son güncelleme: {UPDATED}</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>Kasık</b><span>Ağrının en sık hissedildiği bölge; uyluğa, kalçanın arkasına ve dize yayılabilir</span></div>
        <div class="stat"><b>1 saatten kısa</b><span>Tanı ölçütlerinden biri olan sabah tutukluğu süresi</span></div>
        <div class="stat"><b>Güçlü öneri</b><span>Egzersiz, kilo verme, Tai Chi ve gerektiğinde baston (Amerikan Romatoloji Koleji)</span></div>
        <div class="stat"><b>Karşı öneri</b><span>Glukozamin, hyaluronik asit, PRP ve kök hücre iğneleri</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Kalça, uyluk kemiğinin başı ile leğen kemiğindeki çukurun oluşturduğu bir top-yuva eklemidir. Kireçlenmede eklem yüzeylerini kaplayan kıkırdak incelir, eklem kenarlarında kemik çıkıntıları oluşur ve eklemin hareketi, özellikle içe dönüşü, kısıtlanır.</p>
        <p class="soft">50 yaş üstünde yük vermekle artan kalça ağrısı, bir saatten kısa süren sabah tutukluğu ve kalçanın içe dönüşündeki kısıtlılık varsa tanı çoğu zaman muayeneyle konur.</p>
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

  <section>
    <div class="wrap">
      <h2>Ağrı dizde, sorun kalçada olabilir</h2>
      <p class="soft">Kalça kireçlenmesinin ağrısı yalnızca kasıkta hissedilmez; uyluk boyunca dize yayılabilir. Bazı hastalar yalnızca diz ağrısı tarif eder ve sorun kalçada olduğu hâlde dizi araştırılır.</p>
      <div class="callout">
        <p>Dizinizde ağrı var ama diz muayenesi ve görüntülemesi ağrıyı açıklamıyorsa, kalçanın da değerlendirilmesi gerekir. Fizyoterapi değerlendirmesinde kalçanın hareket açıklığına mutlaka bakılır.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <p class="soft">Amerikan Romatoloji Koleji'nin kılavuzu tedavinin merkezine egzersizi, kilo kontrolünü ve hastalığın kişi tarafından yönetilmesini koyuyor.</p>
      <ul class="tx">
        <li><b>Egzersiz</b><span>Güçlü şekilde önerilir. 2026'da güncellenen Cochrane derlemesine göre ağrı ve işlevdeki ortalama iyileşme küçük olsa da, egzersiz yan etkisi az ve genel sağlığa pek çok faydası olan bir tedavidir. Kalça çevresi kaslarını güçlendiren ve hareket açıklığını koruyan bir program önerilir.</span></li>
        <li><b>Kilo kontrolü</b><span>Fazla kilolu kişilerde kilo vermek güçlü şekilde önerilir; vücut ağırlığının en az %5'ini vermek hedeflenir.</span></li>
        <li><b>Tai Chi ve öz yönetim</b><span>Tai Chi ve hastalığı tanıyıp kendi kendine yönetmeyi öğreten programlar kılavuzda güçlü şekilde önerilen yöntemler arasındadır.</span></li>
        <li><b>Baston</b><span>Kireçlenme yürümeyi, eklem dengesini ya da ağrıyı belirgin etkiliyorsa baston güçlü şekilde önerilir.</span></li>
        <li><b>İlaçlar ve iğne</b><span>Hekiminizin önerdiği ağız yoluyla alınan iltihap giderici ağrı kesiciler ve ultrason eşliğinde yapılan kortizon iğnesi kılavuzda yer alır.</span></li>
        <li><b>Protez ameliyatı</b><span>Ameliyatsız tedaviye rağmen ağrı ve kısıtlılık yaşam kalitesini ciddi şekilde bozuyorsa düşünülür. <a href="protez-sonrasi.html">Protez sonrası rehbere göz atın →</a></span></li>
      </ul>
      <div class="callout">
        <p><strong>Kılavuzda karşı güçlü öneri yapılanlar:</strong> glukozamin ve kondroitin takviyeleri, kalçaya hyaluronik asit, PRP ya da kök hücre iğneleri ve TENS.</p>
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

  <section>
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

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(KALCA_FAQ)}
    </div>
  </section>

  <section>
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
     "Kalça kireçlenmesi (koksartroz) nedir, ağrı neden dize vurur, egzersiz ve kilo kontrolü ne kadar işe yarar, hangi tedaviler önerilmez? Evde altı egzersiz, günlük hayat önerileri, videolar ve uyarı işaretleri.",
     "kalca-kireclenmesi.html", NECK_CSS, KALCA_BODY, YT_JS,
     seo_title="Kalça Kireçlenmesi (Koksartroz): Belirtiler, Egzersizler ve Tedavi | İhsan Eren",
     condition="Kalça kireçlenmesi (koksartroz)", about=cond("Kalça kireçlenmesi (koksartroz)"),
     faq_items=pick(KALCA_FAQ, 0, 1, 2, 3))

# -*- coding: utf-8 -*-
# Yeni rehberler (14): De Quervain (başparmak tarafında bilek ağrısı) ve diyabetik nöropati.
# cond14_part.py'den sonra exec edilir. Videolar: Mayo Clinic, Doctor O'Donovan, Diabetes UK (oEmbed ile doğrulandı).

# ---- yeni çizimler
# Çekiç hareketi: ön kol masada, yumruk masanın kenarından taşar; el başparmak yukarıda, aşağı iner ve geri kalkar.
SV["dq_hammer"] = fig(TABLE +
    '<path class="fig" d="M14 64 H62"/>'
    f'<g>{anim_t("-14 62 64;26 62 64;-14 62 64", dur="4s", kt="0;0.6;1", typ="rotate")}'
    '<path class="fig hl" d="M62 64 H76"/><path d="M77 80 V42" stroke="#C8963E" stroke-width="4.5" stroke-linecap="round"/><rect x="70" y="34" width="14" height="9" rx="2.5" fill="#C8963E"/></g>',
    "Çekiç hareketi")
# Lastikle başparmağı açma: el dik, başparmak lastiğe karşı yana açılır.
SV["dq_band"] = fig(
    '<path class="fig" d="M60 112 L60 84"/>'
    '<rect x="46" y="48" width="28" height="38" rx="8" fill="#2A6F6B"/>'
    '<path class="fig" d="M50 48 V24 M57 48 V18 M64 48 V20 M71 48 V28"/>'
    f'<g>{anim_t("0 48 76;-34 48 76;0 48 76", typ="rotate")}<path class="fig hl" d="M48 76 L36 62 L32 50"/></g>'
    '<ellipse cx="52" cy="56" rx="25" ry="6.5" fill="none" stroke="#C8963E" stroke-width="3" transform="rotate(-12 52 56)"/>',
    "Lastikle başparmak açma")

_ex2("dq_thenar", "thumb", "Başparmak kökünü germe", "Diğer elinizle başparmağınızı tutun ve başparmak kökünü nazikçe dışa doğru gerin. Ağrı değil, hafif bir gerilme hissetmelisiniz.", "15–20 saniye tutun, 8–10 tekrar")
SV["dq_wrist"] = fig(TABLE +
    '<path class="fig" d="M14 64 H62"/>'
    f'<g>{anim_t("-35 62 64;35 62 64;-35 62 64", dur="4s", kt="0;0.5;1", typ="rotate")}<path class="fig hl" d="M62 64 H84"/></g>',
    "Bilek hareketi")
EXT["dq_wrist"] = ("Bileği aşağı yukarı hareket ettirme", "Ön kolunuzu masaya koyun, eliniz masanın kenarından taşsın. Elinizde ağırlık olmadan bileğinizi yapabildiğiniz kadar yukarı kaldırın, sonra aşağı indirin. Ön kolunuz masadan kalkmasın.", "Her yöne 8–10 tekrar")
_ex2("dq_opp", "tglide", "Başparmağı serçe parmağa götürme", "Ön kolunuzu masaya koyun, başparmağınız rahat bir konumda olsun. Başparmağınızı avucunuzun içinden serçe parmağınızın köküne doğru götürün; gerekirse diğer elinizle yardım edin. Sonra başlangıca dönün.", "12 tekrar, 3 set, her gün")
_ex2("dq_grip", "grip", "Top sıkma", "Ağrı yatıştıktan sonra, yumuşak bir topu ya da top yapılmış bir çift çorabı avucunuzda sıkın ve bırakın. Kavrama gücünü geri kazandırır.", "10–15 tekrar, günde 4 kez")
EXT["dq_hammer"] = ("Çekiç hareketi", "Ön kolunuzu masaya koyun; başparmağınız yukarı bakacak şekilde yumruk yapın, eliniz masanın kenarından taşsın. Bileğinizi yere doğru yavaşça indirin, sonra başlangıca getirin. Önce ağırlıksız; kolaylaşınca elinize hafif bir ağırlık alın.", "10–15 tekrar, günde 4 kez")
EXT["dq_band"] = ("Lastikle başparmağı açma", "Parmaklarınızın ve başparmağınızın çevresine bir paket lastiği ya da saç lastiği geçirin. Ön kolunuz masadayken başparmağınızı lastiğe karşı işaret parmağınızdan uzaklaştırın, sonra yavaşça geri getirin.", "10–15 tekrar, günde 4 kez")

_ex2("dn_wshift", "wshift2", "Ağırlık aktarma", "Tezgâha tutunarak ayaklarınız kalça genişliğinde açık durun. Ağırlığınızı yavaşça bir ayağınıza, sonra diğerine verin; ayak tabanlarınızdaki basıncın değiştiğini izleyin. Ayaklarınızdaki his azaldıysa gözlerinizle de kontrol edin.", "Her yana 10 kez")
_ex2("dn_sls", "sls", "Tek ayak üzerinde durma", "Tezgâhın önünde dik durun, bir ya da iki elinizle hafifçe tutunun. Bir ayağınızı yerden kaldırın ve dengede kalın. Kolaylaştıkça tek elle, sonra parmak ucuyla tutunun.", "10–15 saniye, her ayakla 3–5 kez")
_ex2("dn_tandem", "tandem", "Topuk-parmak yürüyüşü", "Tezgâh ya da duvar boyunca, bir elinizi dayanak için hazır tutarak yürüyün. Her adımda öndeki ayağınızın topuğunu arkadaki ayağınızın parmak uçlarının hemen önüne koyun.", "10 adım, 3 tur")
_ex2("dn_heel", "heel2", "Tezgâha tutunarak topuk yükseltme", "Tezgâha tutunarak dik durun. İki topuğunuzu birlikte kaldırıp parmak uçlarınızda yükselin, 2 saniye bekleyip yavaşça inin. Baldır kasları yürürken dengeyi toparlamak için önemlidir.", "10–15 tekrar")
_ex2("dn_sts", "sts", "Sandalyeden kalkıp oturma", "Sağlam bir sandalyenin ön kısmına oturun, ayaklarınız yere tam bassın. Öne eğilip ellerinizden mümkün olduğunca az destek alarak ayağa kalkın, sonra yavaşça oturun. Bacak gücü dengenin temelidir.", "8–10 tekrar, 2 set")
_ex2("dn_walk", "walk", "Yürüyüş", "Ayağınıza iyi oturan, içi pürüzsüz bir ayakkabı ve dikişsiz çorapla yürüyün. Kısa mesafeyle başlayıp azar azar artırın. Yürüyüşten sonra ayaklarınızı kızarıklık, su toplaması ya da yara açısından kontrol edin.", "Haftanın çoğu günü, azar azar artırarak")

# ============================================================== DE QUERVAIN
DQ_FAQ = [
 ("De Quervain kendiliğinden geçer mi?", "Çoğu kişide şikâyetler dinlendirme, atel ve etkinlikleri uyarlamayla zamanla yatışır; ameliyat nadiren gerekir. Dört hafta içinde düzelme olmazsa bir fizyoterapiste ya da hekime başvurun."),
 ("Atel ne kadar süre takılır?", "Hem bileği hem başparmağı saran bir atel kullanılır. İngiltere'deki hastane broşürleri 3–8 hafta arasında süreler veriyor; biri altı hafta boyunca gece gündüz kullanımı, ardından 2–4 haftada kademeli bırakmayı öneriyor. Süreyi ve tipi el terapistiniz ya da hekiminiz belirler."),
 ("Kortizon iğnesi işe yarar mı?", "İğne yaygın olarak kullanılıyor ama kanıt zayıf. Cochrane derlemesi yalnızca 18 kişilik tek bir küçük çalışma bulabildi: İğne yapılan dokuz kadının hepsinde ağrı geçti, yalnızca atel takan dokuz kadının hiçbirinde geçmedi. Çalışma küçük ve kalitesi düşük olduğu için sonuç kesin sayılmıyor. İğne genellikle atel ve egzersiz yetmediğinde düşünülür."),
 ("Egzersize ne zaman başlanır?", "Önce bilek ve başparmak dinlendirilir. Ağrı yatışınca nazik germe ve hareketlerle başlanır, ardından lastik ve hafif ağırlıkla güçlendirmeye geçilir. Egzersizden sonraki rahatsızlık birkaç saatten uzun sürüyorsa tekrar sayısını azaltın."),
]

DQ_SRC = [
 "Dorset County Hospital NHS Foundation Trust. " + ext("https://dchft.nhs.uk/wp-content/uploads/2025/04/De-Quervains-Tenosynovitis-PIL.pdf", "De Quervain's tenosynovitis") + ". Hand Therapy patient leaflet. April 2025.",
 "Gloucestershire Hospitals NHS Foundation Trust. " + ext("https://gloshospitals.nhs.uk/documents/21449/De_Quervains_syndrome_of_the_wrist_GHPI1134_07_24.pdf", "De Quervain's syndrome of the wrist") + ". GHPI1134_07_24. July 2024.",
 "Leicestershire Partnership NHS Trust. " + ext("https://www.leicspart.nhs.uk/wp-content/uploads/2021/08/595-De-Quervains.pdf", "De Quervain's") + ". Leaflet 595. July 2021.",
 "Peters-Veluthamaningal C, van der Windt DAWM, Winters JC, Meyboom-de Jong B. " + ext("https://www.cochrane.org/CD005616/MUSKEL_corticosteroid-injection-for-de-quervains-tenosynovitis", "Corticosteroid injection for de Quervain's tenosynovitis") + ". Cochrane Database Syst Rev. 2009;(3):CD005616.",
 "Sherwood Forest Hospitals NHS Foundation Trust. " + ext("https://www.sfh-tr.nhs.uk/media/ky2f0s0t/pil202601-02-dqt-hand-therapy-de-quervains-tenosynovitis.pdf", "De Quervain's tenosynovitis") + ". Hand Therapy leaflet PIL202601-02-DQT. January 2026.",
 "University Hospitals Plymouth NHS Trust. " + ext("https://www.plymouthhospitals.nhs.uk/display-pil/pil-dequervains-tenosynovitis-6904", "DeQuervain's tenosynovitis") + ". Patient information leaflet C-325. December 2023.",
]

DQ_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>De Quervain: başparmak tarafında bilek ağrısı</h1>
    <p class="lede">De Quervain, başparmağı hareket ettiren kirişlerin bileğin başparmak tarafındaki tünelde tahriş olmasıdır. Kavanoz açarken, çaydanlıktan su dökerken ya da bebeği kucağa alırken ağrır; kadınlarda ve özellikle yeni annelerde sık görülür. Çoğu kişide dinlendirme, atel ve aşamalı egzersizle yatışır.</p>
    <p class="meta">Son güncelleme: 8 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>3 kat</b><span>Kadınlarda erkeklere göre daha sık; özellikle küçük bebeği olanlarda</span></div>
        <div class="stat"><b>30–55 yaş</b><span>En sık görüldüğü yaş aralığı; her yaşta ortaya çıkabilir</span></div>
        <div class="stat"><b>3–8 hafta</b><span>Bileği ve başparmağı saran atel için hastane broşürlerinde verilen süre</span></div>
        <div class="stat"><b>18 kişi</b><span>Kortizon iğnesini atelle karşılaştıran tek çalışmanın büyüklüğü; kanıt zayıf</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Başparmağı hareket ettiren kirişler, bileğin başparmak tarafında tünel gibi bir kılıfın içinden geçer. Bu kılıf kalınlaşıp iltihaplandığında kirişler rahat kayamaz; el kullanıldıkça ağrı ortaya çıkar.</p>
        <p class="soft">Çoğu zaman belirgin bir neden bulunmaz. Bilek öne ya da yana bükülüyken uzun süre kavrama, başparmağın ve bileğin hızlı ve tekrarlı hareketleri, alışık olunmayan bir işe birden başlamak (bahçe, boya, yeni bir spor) ya da bileğin dış yanına alınan bir darbe tetikleyebilir.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Başparmak kökünde ve bileğin yanında ağrı; ön kola yayılabilir</li>
          <li>Kavrarken, sıkıştırırken, bir şeyi burarken artan ağrı</li>
          <li>Çaydanlıktan su dökmek, kavanoz açmak gibi işlerde zorlanma</li>
          <li>Ağrılı noktada şişlik ya da sert bir kabarıklık</li>
          <li>Başparmak hareketlerinde takılma ya da sürtünme hissi</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Yeni annelerde neden sık?</h2>
      <p class="soft">De Quervain en çok küçük bebeği olan kadınlarda görülür. Nedeni tam bilinmiyor: Gebelik ve doğum sonrasındaki hormon değişiklikleri de, bebeği tekrar tekrar kaldırmak, taşımak ve beslemek de rol oynuyor olabilir.</p>
      <p class="soft">En çok ağrıtan hareket, bileğin yana doğru bükülmesidir. Bu yüzden ağrıyan işlerde elinizin ve bileğinizin konumunu değiştirmek, kavrama gerektiren işlerde sık sık ara vermek ve bileği yana büken hareketlerden kaçınmak önerilir. Bebeğinizi kucağınıza alırken bileklerinizi düz tutmaya ve yükü ön kollarınıza yaymaya çalışın.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>İlk adım: dinlendirme ve atel</h2>
      <p class="soft">Tedavinin ilk basamağı kirişleri dinlendirmektir. Bunun için hem bileği hem başparmağı saran bir atel kullanılır. İngiltere'deki hastane broşürleri 3–8 hafta arasında süreler veriyor; bir broşür altı hafta boyunca gece gündüz takmayı, ağrı azalırsa ateli 2–4 haftada kademeli olarak bırakmayı öneriyor. Atel yalnızca duş ve bilek hareketleri için çıkarılır.</p>
      <p class="soft">Bölgeyi günde üç kez, 20 dakika soğutmak ağrıyı azaltabilir. Ağrı kesici ya da iltihap giderici ilaç ve jeller için eczacınıza ya da hekiminize danışın.</p>
      <div class="callout">
        <p>Atel ve egzersiz yetmezse kılıfın içine kortizon iğnesi düşünülebilir; bazı kişilerde birden fazla iğne gerekir. İğneyi sınayan araştırma çok az: Cochrane derlemesi 18 kişilik tek bir çalışma bulabildi ve kanıtın kesinliğini çok düşük olarak değerlendirdi. Ameliyat nadiren gerekir; günübirlik bir işlemle kılıf açılarak kirişlere yer açılır.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <ul class="tx">
        <li><b>Dinlendirme</b><span>Ağrıyı artıran işleri azaltmak ve el-bilek konumunu değiştirmek.</span></li>
        <li><b>Atel</b><span>Bileği ve başparmağı birlikte saran atel; süre ve tipini el terapisti belirler.</span></li>
        <li><b>Soğuk ve ilaç</b><span>Günde üç kez 20 dakika soğuk; ilaç ve jeller için eczacıya ya da hekime danışılır.</span></li>
        <li><b>Egzersiz</b><span>Ağrı yatışınca nazik hareketlerle başlar, kademeli olarak güçlendirmeye geçer.</span></li>
        <li><b>Kortizon iğnesi</b><span>Diğer yöntemler yetmediğinde; kanıtı sınırlı.</span></li>
        <li><b>Ameliyat</b><span>Nadiren; kılıfı gevşeten küçük bir işlem.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>De Quervain için altı egzersiz</h2>
      <p class="soft">İlk üçü ağrı yatışmaya başladığında yapılan nazik hareketlerdir. Son üçü güçlendirme içindir; ağrı belirgin biçimde azaldıktan sonra eklenir. Başta biraz rahatsızlık olabilir ama birkaç saatten uzun sürmemelidir; sürüyorsa tekrar sayısını azaltın.</p>
      {ex_grid(["dq_thenar", "dq_wrist", "dq_opp", "dq_hammer", "dq_band", "dq_grip"])}
      <div class="callout">
        <p>Atel kullanıyorsanız egzersizleri ne zaman ve ne sıklıkta yapacağınızı el terapistinize sorun. Dört hafta sonra hâlâ zorlanıyorsanız bir fizyoterapiste ya da hekime başvurun.</p>
      </div>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>De Quervain için videolar</h2>
      <p class="soft">ABD'deki Mayo Clinic'in ve İngiltere'de hekim olan Dr. James O'Donovan'ın YouTube kanallarından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("o0KSfDuy3i0", "De Quervain tanıtım videosunu oynat", "Mayo Clinic Minute: Is your thumb pain de Quervain's tenosynovitis?")}
          <h3>Başparmak ağrınız De Quervain mi?</h3>
          <p>Hastalığı kısaca tanıtan bir dakikalık video.</p>
        </div>
        <div class="vid">
          {vbox("RdtJdUSIaVQ", "De Quervain egzersizleri videosunu oynat", "De Quervain's Tenosynovitis Relief Exercises | Doctor and Physio led")}
          <h3>Rahatlatan egzersizler</h3>
          <p>Bir hekim ve fizyoterapistin anlattığı egzersiz videosu.</p>
        </div>
      </div>
      <p class="meta">Videolar Mayo Clinic ve Doctor O'Donovan kanallarına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(DQ_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Düşme ya da darbeden sonra bilekte şişlik ve şiddetli ağrı</li>
        <li>Bilekte kızarıklık ve sıcaklıkla birlikte ateş</li>
        <li>Elde geçmeyen uyuşma ya da karıncalanma</li>
        <li>Başparmağı hiç hareket ettirememe</li>
        <li>Dört haftalık dinlendirme ve atele rağmen düzelmeyen ağrı</li>
      </ul>
      {CTA_CARD("De Quervain'e bağlı bilek ağrınız", "De Quervain (bilek ağrısı)")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(DQ_SRC)}
    </div>
  </section>
</main>'''

page("de-quervain.html", "De Quervain: Başparmak Tarafında Bilek Ağrısı",
     "De Quervain nedir, yeni annelerde neden sık görülür? Atel ne kadar takılır, kortizon iğnesi işe yarar mı, egzersize ne zaman başlanır? Evde altı egzersiz ve videolar.",
     "de-quervain.html", NECK_CSS, DQ_BODY, YT_JS,
     seo_title="De Quervain Tendiniti: Bilek Ağrısı, Atel ve Egzersiz | İhsan Eren",
     condition="De Quervain tenosinoviti", faq_items=DQ_FAQ)

# ============================================================== DİYABETİK NÖROPATİ
DN_FAQ = [
 ("Diyabetik nöropati geçer mi?", "Sinirde oluşan hasar geri döndürülemez; ilaçlar ağrıyı azaltır ama siniri onarmaz. Buna karşılık kan şekerini, tansiyonu ve kolesterolü hedef değerlere yakın tutmak hasarın ilerlemesini önlemeye yardım eder. Bu yüzden erken fark etmek ve ayakları korumak önemlidir."),
 ("Ayaklarım uyuşukken egzersiz yapmak güvenli mi?", "Evet, birkaç önlemle. Sekiz çalışmayı (457 kişi) inceleyen derlemede denge ve kuvvet egzersizleri dengeyi ve düşme korkusunu bir miktar iyileştirdi. Ayağınıza iyi oturan ayakkabı giyin, egzersizden sonra ayaklarınızı kontrol edin ve tutunabileceğiniz bir yerin yanında çalışın. Ayağınızda açık yara varsa önce hekiminize danışın."),
 ("Yanan ayaklarım için sıcak su torbası kullanabilir miyim?", "Hayır. Sıcağı ve ağrıyı hissetme azaldığı için cildiniz fark etmeden yanabilir. Ayaklarınızı sıcak su torbasından, ısıtıcıdan ve açık ateşten uzak tutun; banyo suyunu dirseğinizle ya da termometreyle kontrol edin. Ayaklarınız üşüyorsa yatakta çorap giyin."),
 ("Uyuşmanın nedeni B12 eksikliği olabilir mi?", "Olabilir; bu yüzden hekimler nöropatiyi araştırırken tiroid ve böbrek sorunlarıyla birlikte B12 düzeyine de bakar. Metformin B12 düşüklüğünün nedenleri arasındadır; böyle bir durumda ilaç B12 takviyesiyle sürdürülebilir. Kararı hekiminiz verir; ilacınızı kendiniz kesmeyin."),
]

DN_SRC = [
 "De Oliveira Lima RA, Piemonte GA, Nogueira CR, Nunes-Nogueira VS. " + ext("https://www.scielo.br/j/aem/a/bNMqwKs5nh4WWkwp3wpVqXP/?lang=en", "Efficacy of exercise on balance, fear of falling, and risk of falls in patients with diabetic peripheral neuropathy: a systematic review and meta-analysis") + ". Arch Endocrinol Metab. 2021;65(2):198-211.",
 "National Institute of Diabetes and Digestive and Kidney Diseases. " + ext("https://www.niddk.nih.gov/health-information/diabetes/overview/preventing-problems/nerve-damage-diabetic-neuropathies/peripheral-neuropathy", "Peripheral neuropathy") + ". Last reviewed February 2018.",
 "National Institute of Diabetes and Digestive and Kidney Diseases. " + ext("https://www.niddk.nih.gov/health-information/diabetes/overview/preventing-problems/foot-problems", "Diabetes and foot problems") + ". Last reviewed January 2017.",
 "Wang D, Pang X, Shen P, Mao D, Song Q. " + ext("https://search.pedro.org.au/search-results/record-detail/84239", "Effectiveness of various exercise types in reducing fall risk among older adults with diabetic peripheral neuropathy: a systematic review and meta-analysis") + ". J Exerc Sci Fit. 2025;23(3):157-166.",
]

DN_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Diyabetik nöropati: ayaklarda uyuşma ve yanma</h1>
    <p class="lede">Diyabetik nöropati, uzun süre yüksek seyreden kan şekerinin sinirlere zarar vermesidir; en çok ayaklarda yanma, karıncalanma ve uyuşma yapar. Diyabeti olanların yarıya yakınında görülür. Hasar geri döndürülemese de ilerlemesi yavaşlatılabilir. Her gün yapılan ayak kontrolü yaraları erken yakalamaya, denge ve kuvvet egzersizleri de daha güvenli yürümeye yardım eder.</p>
    <p class="meta">Son güncelleme: 8 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>2'de 1</b><span>Diyabeti olanların yarıya kadarında sinir hasarı görülüyor (NIDDK)</span></div>
        <div class="stat"><b>Her akşam</b><span>Ayakların, parmak araları dahil, kontrol edilmesi önerilen sıklık</span></div>
        <div class="stat"><b>Yılda 1</b><span>En az bu sıklıkla ayrıntılı ayak ve bacak muayenesi</span></div>
        <div class="stat"><b>457 kişi</b><span>Egzersizin dengeyi ve düşme korkusunu iyileştirdiği sekiz çalışma</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Uzun süre yüksek kalan kan şekeri ve kan yağları, sinirlere ve onları besleyen küçük damarlara zarar verir. Hasar çoğunlukla en uzun sinirlerin ucundan, yani ayaklardan başlar; zamanla bacaklara, bazen ellere ve kollara ilerler.</p>
        <p class="soft">Asıl tehlike ağrının kendisi değil, hissin azalmasıdır: Ayağındaki yarayı, su toplamasını ya da ayakkabıya giren taşı hissetmeyen kişi onu fark etmez. Diyabette yaralar geç iyileşir ve kolay enfekte olur.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Ayaklarda ve bacaklarda yanma, karıncalanma, iğnelenme</li>
          <li>Uyuşma; ağrıyı, sıcağı ve soğuğu daha az hissetme</li>
          <li>Hafif bir dokunuşla bile şiddetli ağrı</li>
          <li>Güçsüzlük, yürüyüşte değişiklik, denge kaybı ve düşmeler</li>
          <li>Belirtilerin geceleri artması</li>
          <li>Çoğunlukla iki tarafta birden görülmesi</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi: üç hedef</h2>
      <p class="soft"><strong>İlerlemeyi durdurmak.</strong> Kan şekerini, tansiyonu ve kolesterolü hedef değerlere yakın tutmak sinir hasarının kötüleşmesini önlemeye yardım eder. Bu, tedavinin temelidir.</p>
      <p class="soft"><strong>Ağrıyı azaltmak.</strong> Sinir ağrısında alışılmış ağrı kesiciler çoğu zaman yeterince işe yaramaz. Hekimler bunun yerine bazı antidepresanları (duloksetin, amitriptilin gibi), bazı sara ilaçlarını (pregabalin, gabapentin) ya da cilde sürülen lidokaini reçete edebilir. Bu ilaçlar ağrıyı azaltır ama sinir hasarını geri çevirmez; biri işe yaramazsa başka biri denenebilir.</p>
      <p class="soft"><strong>Ayakları ve dengeyi korumak.</strong> Günlük ayak bakımı ile kuvvet ve denge için fizyoterapi tedavinin parçasıdır. Hekiminiz yılda en az bir kez ayaklarınızdaki titreşim ve dokunma hissini, yürüyüşünüzü ve dengenizi muayene etmelidir; muayenede ayakkabı ve çoraplarınızı çıkarın.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Her gün ayak bakımı</h2>
      <ul class="tx">
        <li><b>Bakın</b><span>Her akşam ayaklarınızı, parmak araları dahil, kesik, yara, kızarıklık, şişlik, su toplaması ve sıcak nokta açısından kontrol edin. Eğilemiyorsanız ayna kullanın ya da bir yakınınızdan isteyin.</span></li>
        <li><b>Yıkayın ve kurulayın</b><span>Sıcak değil ılık suyla yıkayın; suyu dirseğinizle deneyin. Ayaklarınızı suda bekletmeyin, parmak aralarını iyice kurulayın.</span></li>
        <li><b>Nemlendirin</b><span>Ayağın üstüne ve altına nemlendirici sürün; parmak aralarına sürmeyin.</span></li>
        <li><b>Tırnak ve nasır</b><span>Tırnakları düz kesin, kenarlarını törpüleyin. Nasırı kesmeyin, nasır bandı ve nasır ilacı kullanmayın.</span></li>
        <li><b>Çıplak ayakla dolaşmayın</b><span>Evde bile ayakkabı ya da terlik ve çorap giyin. Giymeden önce ayakkabının içini elinizle yoklayın.</span></li>
        <li><b>Sıcaktan ve soğuktan koruyun</b><span>Sıcak su torbası ve ısıtıcı kullanmayın; ayaklarınız üşüyorsa yatakta çorap giyin.</span></li>
      </ul>
      <div class="callout">
        <p>Otururken ayaklarınızı yükseltin, gün içinde ayak parmaklarınızı ve bileklerinizi sık sık oynatın, sıkı çorap giymeyin. Sigara ayaklara giden kan akımını azaltır; bırakmak ayaklarınız için de önemlidir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Egzersiz dengeyi düzeltir mi?</h2>
      <p class="soft">Ayak tabanındaki his azalınca denge de bozulur; düşme ve kırık riski artar. Sekiz rastgele kontrollü çalışmayı (457 kişi) birleştiren 2021 tarihli derlemede yürüme, denge ve kuvvet egzersizleri tek ayak üzerinde durma süresini ve düşme korkusunu bir miktar iyileştirdi. Düşme sayısına bakan tek çalışmada fark görülmedi; yazarlar bunu çalışmaların küçüklüğüne ve kısa süresine bağlıyor ve kanıtın kesinliğini düşük buluyor.</p>
      <p class="soft">Yaşlı yetişkinlerde 21 çalışmayı inceleyen 2025 tarihli bir derleme de aynı yönde: En çok yarar denge egzersizlerinden ve dengeyi kuvvetle birleştiren programlardan sağlandı. Yürüyüş, yüzme, bisiklet, dans ve yoga gibi eklemleri sarsmayan etkinlikler ayağa giden kan akımını da destekler.</p>
      <div class="callout">
        <p>Denge egzersizlerini tezgâh gibi tutunabileceğiniz sağlam bir yerin yanında yapın. Ayağınızda açık yara, su toplaması ya da kızarık, sıcak ve şiş bir bölge varsa üzerine basarak egzersiz yapmayın; önce hekiminize gösterin.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Denge ve kuvvet için altı egzersiz</h2>
      <p class="soft">Ayağınıza iyi oturan ayakkabıyla, tutunabileceğiniz bir yerin yanında çalışın. Kolaydan zora doğru sıralandı; bir hareketi güvenle yapabildiğinizde sonrakine geçin.</p>
      {ex_grid(["dn_wshift", "dn_sls", "dn_tandem", "dn_heel", "dn_sts", "dn_walk"])}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Ayak bakımı için videolar</h2>
      <p class="soft">İngiltere'deki diyabet derneği Diabetes UK'nin ve ABD'deki Mayo Clinic'in YouTube kanallarından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("jC9hXPURsQA", "Günlük ayak kontrolü videosunu oynat", "How to perform a daily diabetes foot check | Diabetes UK")}
          <h3>Günlük ayak kontrolü</h3>
          <p>Ayakların her gün nasıl kontrol edileceğini gösteren video.</p>
        </div>
        <div class="vid">
          {vbox("SulNOSMMNLY", "Diyabette ayak bakımı videosunu oynat", "Mayo Clinic Minute: 5 steps to diabetic foot care")}
          <h3>Ayak bakımında beş adım</h3>
          <p>Diyabette ayak bakımını özetleyen bir dakikalık video.</p>
        </div>
      </div>
      <p class="meta">Videolar Diabetes UK ve Mayo Clinic kanallarına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(DN_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Ayağınızda birkaç gün içinde iyileşmeye başlamayan kesik, su toplaması ya da morluk</li>
        <li>Kızarık, sıcak ya da ağrılı bir bölge (enfeksiyon belirtisi olabilir)</li>
        <li>İçinde kurumuş kan görülen nasır</li>
        <li>Siyahlaşan ve kötü kokan yara (acil)</li>
        <li>Ayakta kızarıklık, sıcaklık ve şişlikle birlikte şekil değişikliği</li>
        <li>Sık düşme ya da hızla artan güçsüzlük</li>
      </ul>
      {CTA_CARD("Nöropatiye bağlı denge ve yürüme güçlükleriniz", "diyabetik nöropati")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(DN_SRC)}
    </div>
  </section>
</main>'''

page("diyabetik-noropati.html", "Diyabetik Nöropati: Ayaklarda Uyuşma ve Yanma",
     "Diyabette ayaklar neden uyuşur ve yanar? Diyabetik nöropatide tedavi, her gün ayak bakımı, egzersizin dengeye etkisi, evde altı denge ve kuvvet egzersizi ve videolar.",
     "diyabetik-noropati.html", NECK_CSS, DN_BODY, YT_JS,
     seo_title="Diyabetik Nöropati: Ayak Bakımı, Denge Egzersizleri ve Tedavi | İhsan Eren",
     condition="Diyabetik nöropati", faq_items=DN_FAQ)

# -*- coding: utf-8 -*-
# Bel ağrısı + bel fıtığı sayfaları. neck_part.py'den sonra exec edilir
# (fig, anim_t, anim_d, SV, EXT, ex_grid, faq, src_list, ext, CTA_NOTE, NECK_CSS, root_row, vbox, YT_JS tanımlı).

# ---------------------------------------------------------------- egzersiz çizimleri
# Yatarak: zemin y=112, gövde y≈105
SV["ptilt"] = fig(GRD +
    '<circle class="hd" cx="14" cy="100" r="7"/>'
    '<path class="fig" d="M62 104 L78 84 L90 108 M26 104 L46 108"/>'
    f'<path class="fig hl" d="M22 104 Q42 96 62 104">{anim_d("M22 104 Q42 96 62 104;M22 105 Q42 106 62 105;M22 104 Q42 96 62 104")}</path>'
    '<g><animate attributeName="opacity" values="0;1;0" dur="3.2s" repeatCount="indefinite"/>'
    '<path d="M42 84 V92 M38 88 L42 92 L46 88" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>',
    "Pelvik eğme")

SV["k2c"] = fig(GRD +
    '<path class="fig" d="M34 105 H60 M60 105 H104"/>'
    f'<g>{anim_t("0 34 105;22 34 105;0 34 105", typ="rotate")}<path class="fig" d="M22 105 H34"/><circle class="hd" cx="14" cy="100" r="7"/></g>'
    f'<path class="fig hl" d="M60 105 L74 86 L88 106">{anim_d("M60 105 L74 86 L88 106;M60 105 L52 76 L68 70;M60 105 L74 86 L88 106")}</path>'
    f'<path class="fig" d="M26 104 L44 96 L72 88">{anim_d("M26 104 L44 96 L72 88;M27 101 L40 86 L52 78;M26 104 L44 96 L72 88")}</path>',
    "Diz göğse çekme")


SV["cat"] = fig(GRD +
    '<path class="fig" d="M32 76 V108 M82 76 V108 H106"/>'
    f'<path class="fig hl" d="M32 76 Q57 62 82 76">{anim_d("M32 76 Q57 62 82 76;M32 76 Q57 90 82 76;M32 76 Q57 62 82 76")}</path>'
    f'<g>{anim_t("0 6;0 -6;0 6")}<path class="fig" d="M32 76 L25 74"/><circle class="hd" cx="20" cy="74" r="7"/></g>',
    "Kedi-deve")

SV["bridge"] = fig(GRD +
    '<circle class="hd" cx="12" cy="100" r="7"/>'
    '<path class="fig" d="M22 107 H44"/>'
    f'<path class="fig hl" d="M20 104 L58 104 L76 84 L86 108">{anim_d("M20 104 L58 104 L76 84 L86 108;M20 104 L58 86 L78 82 L86 108;M20 104 L58 104 L76 84 L86 108")}</path>',
    "Köprü")

# Kişi sağa bakıyor: bize dönük taraf sağ taraf. Uzanan sağ kol önde (tam renk),
# uzanan sol bacak ve destek sol kol arkada (soluk).
SV["birddog"] = fig(GRD +
    f'<path class="fig hl" d="M38 76 L36 106" opacity=".5">{anim_d("M38 76 L36 106;M38 76 L6 70;M38 76 L36 106")}</path>'
    '<path class="fig" d="M88 76 V108" opacity=".45"/>'
    '<path class="fig" d="M38 76 H88 M38 76 V108 H14 M88 76 L95 79"/>'
    '<circle class="hd" cx="101" cy="83" r="7"/>'
    f'<path class="fig hl" d="M88 76 L90 104">{anim_d("M88 76 L90 104;M88 76 L116 67;M88 76 L90 104")}</path>',
    "Kuş-köpek")


# Önden görünüm: yüzü bize dönük, sağ ön kol üstünde yan yatıyor; üst kol tavana (T şekli), kalça kalkıyor.
SV["sideplank"] = fig(GRD +
    '<path class="fig" d="M30 86 V108 L12 108 M30 86 L34 79 M31 83 L24 79"/>'
    '<path class="fig" d="M34 79 L38 53"/><circle cx="38.5" cy="50" r="3" fill="#2A6F6B"/>'
    '<circle class="hd" cx="18" cy="76" r="7.5"/><circle cx="15.5" cy="75" r="1.2" fill="#efe9d6"/><circle cx="20.5" cy="75" r="1.2" fill="#efe9d6"/>'
    f'<path class="fig hl" d="M32 84 L62 106 L94 109">{anim_d("M32 84 L62 106 L94 109;M32 84 L62 97 L94 109;M32 84 L62 106 L94 109")}</path>'
    f'<path class="fig" d="M62 103 L96 106" opacity=".45">{anim_d("M62 103 L96 106;M62 94.5 L96 106;M62 103 L96 106")}</path>'
    '<g><animate attributeName="opacity" values="0;1;0" dur="3.2s" repeatCount="indefinite"/>'
    '<path d="M64 88 V80 M60 84 L64 80 L68 84" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>',
    "Dizler üstünde yan köprü")




SV["9090"] = fig(GRD +
    '<path class="obj" d="M58 74 H100 M62 74 V112 M96 74 V112 M100 74 V44"/>'
    '<circle class="hd" cx="12" cy="100" r="7"/>'
    '<path class="fig" d="M20 105 H56 M56 105 L56 70 L92 70 M24 104 L44 108"/>'
    '<ellipse cx="38" cy="104" rx="16" ry="5" fill="#C8963E"><animate attributeName="opacity" values="0.15;0.55;0.15" dur="4s" repeatCount="indefinite"/></ellipse>',
    "90/90 dinlenme pozisyonu")

SV["pressup"] = fig(GRD +
    '<path class="fig" d="M60 104 H112"/>'
    f'<g>{anim_t("0 60 104;28 60 104;0 60 104", typ="rotate")}'
    '<path class="fig hl" d="M60 104 L26 104"/><circle class="hd" cx="18" cy="100" r="7"/></g>'
    f'<path class="fig" d="M26 104 L30 108 L12 108">{anim_d("M26 104 L30 108 L12 108;M30 88 L30 108 L12 108;M26 104 L30 108 L12 108")}</path>',
    "Yüzüstü doğrulma")

SV["slump"] = fig(GRD +
    '<path class="obj" d="M36 78 H70 M38 78 V112 M68 78 V112 M36 78 V50"/>'
    '<path class="fig" d="M48 76 L50 44 M48 76 L76 76 M50 50 L60 64 L72 70"/>'
    f'<path class="fig hl" d="M76 76 L78 108">{anim_d("M76 76 L78 108;M76 76 L106 70;M76 76 L78 108")}</path>'
    f'<g>{anim_t("14 50 44;-20 50 44;14 50 44", typ="rotate")}'
    '<path class="fig" d="M50 44 L52 36"/><circle class="hd" cx="53" cy="28" r="7"/><path d="M59 26 L64 29 L59 31 Z" fill="#2A6F6B"/></g>',
    "Oturarak siyatik sinir kaydırma")

EXT.update({
 "ptilt": ("Pelvik eğme", "Sırtüstü yatın, dizleriniz bükülü, ayak tabanlarınız yerde olsun. Karnınızı hafifçe sıkarak belinizin çukurunu yere doğru bastırın, 5 saniye tutun ve bırakın. Nefesinizi tutmayın.", "10 tekrar, günde 2 kez"),
 "k2c": ("Dizi göğse çekme", "Sırtüstü yatın. Bir dizinizi iki elinizle tutup göğsünüze doğru yavaşça çekin, belinizde hafif bir gerilme hissedin. İsterseniz çekerken başınızı da hafifçe dizinize doğru kaldırın, omuzlarınız yerde kalsın (Williams egzersizlerindeki gibi); boyun ağrınız varsa başınızı yerde bırakın. Sonra diğer bacakla tekrarlayın.", "20–30 saniye tutun, her bacakla 3 kez"),
 "cat": ("Kedi-deve", "Ellerinizin ve dizlerinizin üzerinde durun. Nefes verirken sırtınızı kedi gibi yukarı doğru yuvarlayın, başınız aşağı insin. Nefes alırken belinizi yavaşça aşağı bırakın, başınızı kaldırın. Ağrısız aralıkta, yavaş hareket edin.", "10 tekrar"),
 "bridge": ("Köprü", "Sırtüstü yatın, dizleriniz bükülü, ayaklarınız yerde. Kalçanızı sıkarak sırtınızı yerden kaldırın; omuzlarınızdan dizlerinize kadar düz bir çizgi oluşsun. 3–5 saniye bekleyip yavaşça inin.", "10–15 tekrar, günde 1–2 kez"),
 "birddog": ("Kuş-köpek", "Ellerinizin ve dizlerinizin üzerinde, sırtınız düz durun. Sağ kolunuzu öne, sol bacağınızı arkaya uzatın; beliniz çukurlaşmasın, kalçanız dönmesin. 5 saniye tutun, sonra sol kol ve sağ bacakla yapın.", "Her iki yana 8–10 tekrar"),
 "sideplank": ("Dizler üstünde yan köprü", "Yüzünüz karşıya bakacak şekilde yan yatın; dirseğiniz tam omzunuzun altında, ön kolunuz yerde, dizleriniz bükülü olsun. Kalçanızı yerden kaldırarak başınızdan dizlerinize kadar düz bir çizgi oluşturun. Üstteki kolunuzu tavana uzatabilir ya da elinizi belinize koyabilirsiniz. Yavaşça inin, sonra diğer tarafa dönün.", "10–20 saniye, her iki yana 3 kez"),
 "9090": ("90/90 dinlenme pozisyonu", "Ağrı çok şiddetliyken sırtüstü yatın, baldırlarınızı bir sandalyenin ya da kanepenin üzerine koyun; kalçanız ve dizleriniz 90 derece bükülü olsun. Bu pozisyon bel ve sinir kökü üzerindeki yükü azaltır.", "Rahatlatıyorsa 10–15 dakika"),
 "pressup": ("Yüzüstü doğrulma", "Yüzüstü uzanın. Dirseklerinizi omuzlarınızın altına getirip göğsünüzü yavaşça yerden kaldırın, kalçanız yerde kalsın, beliniz gevşek olsun. Bacaktaki ağrı bele doğru çekiliyorsa devam edin; bacağa doğru yayılıyorsa bırakın.", "10 tekrar ya da 1–2 dakika bekleme"),
 "slump": ("Oturarak siyatik sinir kaydırma", "Sandalyenin önüne dik oturun. Dizinizi düzeltirken başınızı hafifçe geriye, tavana doğru kaldırın. Dizinizi bükerken başınızı öne eğin. Sinir bir uçtan gerilirken diğer uçtan gevşer, böylece gerilmeden kayar.", "Yavaşça 10 tekrar. Uyuşma artarsa bırakın"),
})

BACK_SVC = "Evde değerlendirme, manuel terapi ve kişiye özel egzersiz programı"
SRC_NICE59 = ("National Institute for Health and Care Excellence. " + ext("https://www.nice.org.uk/guidance/ng59", "Low back pain and sciatica in over 16s: assessment and management (NG59)") + ". Londra: NICE; 2016, güncelleme 2020.")
SRC_BRINJIKJI = ("Brinjikji W, Luetmer PH, Comstock B, et al. " + ext("https://www.ajnr.org/content/36/4/811", "Systematic literature review of imaging features of spinal degeneration in asymptomatic populations") + ". AJNR Am J Neuroradiol. 2015;36(4):811-816.")

# ------------------------------------------------------------------ BEL AĞRISI
BEL_FAQ = [
 ("Yatak istirahati yapmalı mıyım?", "Hayır. Kılavuzlar hareketli kalmayı öneriyor. Çok ağrılı ilk bir iki günde dinlenmek doğaldır ama uzun süre yatmak kasları zayıflatır ve iyileşmeyi geciktirir. Ağrının izin verdiği ölçüde yürüyün ve günlük işlerinize devam edin."),
 ("Bel korsesi takmalı mıyım?", "Genellikle hayır. Bel ağrısı ve siyatik için hazırlanan İngiltere kılavuzu (NICE) korse, tabanlık ve bel çekme (traksiyon) tedavilerini önermiyor. Korseyi uzun süre kullanmak kasların çalışmasını azaltabilir."),
 ("MR çektirmem gerekir mi?", "Çoğu zaman gerekmez. Ağrısı olmayan kişilerde de disk dejenerasyonu ve disk taşması çok sık görülür; MR'da bir bulgu çıkması ağrının nedeninin o olduğu anlamına gelmez. Uyarı işaretleri varsa ya da ameliyat düşünülüyorsa hekiminiz karar verir."),
 ("Sert yatak mı daha iyi?", "Çok sert yatak şart değil. Uzun süren bel ağrısı olan kişilerle yapılan bir çalışmada orta sertlikteki yatak, sert yataktan daha iyi sonuç verdi. Rahat uyuduğunuz, sabah daha az ağrıyla kalktığınız yatak en uygunudur."),
 ("Ağrım geçti, egzersize devam etmeli miyim?", "Evet. Bel ağrısı sık tekrarlar: bir çalışmada ağrısı geçenlerin %69'u bir yıl içinde yeniden bel ağrısı yaşadı. Düzenli egzersiz ve hareketli bir yaşam tekrar riskini azaltmanın en iyi yoludur."),
]
BEL_SRC = [
 SRC_BRINJIKJI,
 "da Silva T, Mills K, Brown BT, et al. Recurrence of low back pain is common: a prospective inception cohort study. J Physiother. 2019;65(3):159-165.",
 "GBD 2021 Low Back Pain Collaborators. " + ext("https://www.thelancet.com/journals/lanrhe/article/PIIS2665-9913(23)00098-X/fulltext", "Global, regional, and national burden of low back pain, 1990–2020, its attributable risk factors, and projections to 2050") + ". Lancet Rheumatol. 2023;5(6):e316-e329.",
 "Hayden JA, Ellis J, Ogilvie R, Malmivaara A, van Tulder MW. " + ext("https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD009790.pub2/full", "Exercise therapy for chronic low back pain") + ". Cochrane Database Syst Rev. 2021;9:CD009790.",
 "Koes BW, van Tulder MW, Thomas S. Diagnosis and treatment of low back pain. BMJ. 2006;332(7555):1430-1434.",
 "Kovacs FM, Abraira V, Peña A, et al. Effect of firmness of mattress on chronic non-specific low-back pain: randomised, double-blind, controlled, multicentre trial. Lancet. 2003;362(9396):1599-1604.",
 SRC_NICE59,
 "Physiopedia. " + ext("https://www.physio-pedia.com/Non_Specific_Low_Back_Pain", "Non Specific Low Back Pain") + ".",
 "Physiopedia. " + ext("https://www.physio-pedia.com/Williams_Flexion_Exercise", "Williams Flexion Exercise") + ".",
 "Wallwork SB, Braithwaite FA, O'Keeffe M, et al. " + ext("https://www.cmaj.ca/content/196/2/E29", "The clinical course of acute, subacute and persistent low back pain: a systematic review and meta-analysis") + ". CMAJ. 2024;196(2):E29-E46.",
]

BEL_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Bel ağrısı</h1>
    <p class="lede">Dünyada iş göremezliğin bir numaralı nedeni. Kulağa korkutucu gelse de çoğu bel ağrısının altında ciddi bir hastalık yoktur ve yeni başlayan ağrıların çoğu birkaç haftada belirgin şekilde azalır. İyileşmenin anahtarı dinlenmek değil, hareket etmektir.</p>
    <p class="meta">Son güncelleme: {UPDATED}</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>619 milyon</b><span>Dünyada bel ağrısı yaşayan kişi (2020)</span></div>
        <div class="stat"><b>1. sırada</b><span>Dünyada iş göremezliğe en çok yol açan neden</span></div>
        <div class="stat"><b>%90+</b><span>Belirli bir yapısal neden bulunamayan bel ağrısı</span></div>
        <div class="stat"><b>%69</b><span>Ağrısı geçenlerde bir yıl içinde tekrar</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Kaburgaların alt sınırı ile kalça kıvrımı arasındaki ağrıdır. Bel ağrılarının %90'dan fazlasında belirli bir yapısal neden bulunamaz; buna <em>nonspesifik</em> ya da mekanik bel ağrısı denir. Ağrı gerçektir ama beldeki bir "kırılma" ya da "kayma"yı göstermez. Kaslar, bağlar, eklemler ve sinir sisteminin ağrıya duyarlılığı birlikte rol oynar.</p>
        <p class="soft">Ağrı dizin altına, bacağa ve ayağa uyuşma ya da karıncalanmayla yayılıyorsa bir sinir kökü etkileniyor olabilir: <a href="bel-fitigi.html">Bel fıtığı ve siyatik →</a></p>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Uzun süre aynı pozisyonda kalmak, özellikle saatlerce oturmak</li>
          <li>Alışık olunmayan ağır kaldırma, ani dönme ya da zorlanma</li>
          <li>Hareketsizlik, gövde ve kalça kaslarının zayıflığı</li>
          <li>Fazla kilo ve sigara</li>
          <li>Stres, kaygı, yorgunluk ve uykusuzluk</li>
          <li>Fiziksel olarak ağır işler</li>
        </ul>
        <p class="soft">İş kaynaklı etkenler, sigara ve yüksek vücut ağırlığı bel ağrısına bağlı iş göremezliğin yaklaşık %39'undan sorumlu; yani önemli bir kısmı önlenebilir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>MR'daki "düzleşme", "bombeleşme", "aşınma" ne anlama geliyor?</h2>
      <p class="soft">Beldeki diskler yaşla birlikte, tıpkı saçın beyazlaması gibi değişir. Hiç ağrısı olmayan binlerce kişinin MR'larını inceleyen bir derlemede:</p>
      <div class="stats" style="margin-top:14px">
        <div class="stat"><b>%52</b><span>30 yaşında disk dejenerasyonu (aşınma)</span></div>
        <div class="stat"><b>%40</b><span>30 yaşında disk bombeleşmesi</span></div>
        <div class="stat"><b>%80</b><span>50 yaşında disk dejenerasyonu</span></div>
        <div class="stat"><b>%60</b><span>50 yaşında disk bombeleşmesi</span></div>
      </div>
      <div class="callout">
        <p>Bu kişilerin hiçbirinde bel ağrısı yoktu. Yani MR raporundaki bu ifadeler çoğu zaman yaşa bağlı normal değişikliklerdir ve tek başına ağrının nedenini açıklamaz. Bu yüzden kılavuzlar bel ağrısında rutin görüntüleme önermez.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Seyri ve tedavi</h2>
      <p class="soft">Yeni başlayan bel ağrısında ağrı ve kısıtlılık genellikle ilk 6 haftada belirgin şekilde azalır; çalışmalarda ağrı puanı ortalama yarıdan fazla düştü. Üç aydan uzun süren ağrıda düzelme daha yavaştır; burada düzenli egzersiz ve yönlendirilmiş bir tedavi programı daha da önem kazanır.</p>
      <ul class="tx">
        <li><b>Hareketli kalmak</b><span>Yatak istirahati önerilmez. Yürümek ve günlük işlere ağrının izin verdiği ölçüde devam etmek iyileşmeyi hızlandırır; mümkünse işten uzun süre uzak kalmayın.</span></li>
        <li><b>Egzersiz</b><span>Tedavinin temelidir. Uzun süren bel ağrısında egzersiz, ağrıyı 100 üzerinden ortalama 15 puan azaltıyor. En iyi egzersiz, düzenli yapabildiğiniz egzersizdir.</span></li>
        <li><b>Manuel terapi</b><span>Mobilizasyon, manipülasyon ve yumuşak doku teknikleri, kılavuzlara göre egzersizle birlikte bir tedavi paketinin parçası olarak uygulandığında faydalıdır.</span></li>
        <li><b>Ağrıyla baş etme</b><span>Uzun süren ağrıda korku, kaygı ve uykusuzluk ağrıyı besler. Bilişsel davranışçı yaklaşımlar egzersizle birlikte önerilir. <a href="stres.html">Nefes egzersizlerine göz atın →</a></span></li>
        <li><b>İlaçlar</b><span>Hekiminizin önerdiği ağrı kesiciler en düşük dozda ve en kısa süre kullanılmalıdır.</span></li>
        <li><b>Önerilmeyenler</b><span>Korse, tabanlık ve bel çekme (traksiyon) tedavileri kılavuzlarda önerilmiyor.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Bel için altı temel egzersiz</h2>
      <p class="soft">Hafif bir gerginlik ya da rahatsızlık normaldir; ağrının egzersizden sonra kısa sürede eski düzeyine dönmesi zarar görmediğinizi gösterir. Ağrı bacağa yayılmaya başlarsa ya da belirgin şekilde artarsa o egzersizi bırakın. Kolay olanlarla başlayıp zamanla artırın.</p>
      {ex_grid(["ptilt", "k2c", "cat", "bridge", "birddog", "sideplank"])}
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Günlük hayatta beliniz için</h2>
        <p class="soft">Bel, sanıldığından çok daha sağlam bir yapıdır ve düzenli hareketle güçlenir. Eğilmekten ya da yük kaldırmaktan korkmak yerine, vücudunuzu yavaş yavaş alıştırmak daha doğrudur.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Yarım saatte bir kalkın, birkaç adım yürüyün; uzun oturmayı bölün.</li>
        <li>Yükü vücudunuza yakın tutun, acele etmeyin, kaldırırken dönmeyin.</li>
        <li>Haftanın çoğu günü yürüyün; kısa yürüyüşler de sayılır.</li>
        <li>Uyku düzenine dikkat edin; yorgunluk ağrıya duyarlılığı artırır.</li>
        <li>Sigarayı bırakmak ve fazla kiloları vermek bel sağlığını da korur.</li>
      </ul>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Bel ağrısı için egzersiz videoları</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("WxHrtbmZIEU", "Bel ağrısı egzersizleri videosunu oynat", "Low Back Pain Relief: 5 Exercises That Work")}
          <h3>Bel ağrısını hafifleten beş egzersiz</h3>
          <p>Yeni başlayan ya da tekrarlayan bel ağrısında kısa bir program.</p>
        </div>
        <div class="vid">
          {vbox("uGSYKHWLjFo", "Kronik bel ağrısı videosunu oynat", "Top 5 Exercises For Chronic Low Back Pain")}
          <h3>Uzun süren bel ağrısı için beş egzersiz</h3>
          <p>Aylardır süren bel ağrısında güçlendirme ve hareket egzersizleri.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(BEL_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Bel ağrısı çok nadiren ciddi bir hastalığın belirtisidir. Şu durumlarda ise beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>İdrar yapamama ya da tutamama, dışkı kaçırma (acil)</li>
        <li>Kasık, makat ve iç bacaklarda uyuşma, yani "eyer bölgesinde" his kaybı (acil)</li>
        <li>İki bacakta birden güçsüzlük ya da uyuşma, giderek artan güç kaybı</li>
        <li>Düşme ya da darbe sonrası başlayan ağrı, özellikle kemik erimesi olanlarda</li>
        <li>Ateş, titreme, nedensiz kilo kaybı ya da kanser öyküsüyle birlikte ağrı</li>
        <li>Dinlenmekle geçmeyen, giderek artan şiddetli gece ağrısı</li>
        <li>Karın ağrısıyla birlikte ani başlayan çok şiddetli bel ağrısı (<strong>112</strong>)</li>
      </ul>
      {CTA_CARD("Bel ağrınız", "bel ağrım")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(BEL_SRC)}
    </div>
  </section>
</main>'''

page("bel-agrisi.html", "Bel Ağrısı",
     "Bel ağrısı neden olur, ne kadar sürer, MR'daki bulgular ne anlama gelir? Evde yapılabilecek altı egzersiz, günlük hayat önerileri, videolar ve uyarı işaretleri.",
     "bel-agrisi.html", NECK_CSS, BEL_BODY, YT_JS,
     seo_title="Bel Ağrısı: Nedenleri, Egzersizler ve Tedavi | İhsan Eren", condition="Bel ağrısı", about=cond("Bel ağrısı", "low-back-pain"),
     faq_items=pick(BEL_FAQ, 0, 2, 1, 4))

# ------------------------------------------------------------------ BEL FITIĞI
L4, L5, S1 = "#b9b37a", "#e2ab47", "#c96b5a"
LEG = f'''<svg class="hand" viewBox="0 0 200 270" role="img" aria-label="Sağ bacak, önden: dizin önü ve bacağın iç yanı L4, bacağın dış yanı, ayak üstü ve başparmak L5, ayağın dış kenarı ve küçük parmak S1 bölgesi">
  <defs><linearGradient id="thighfade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2d3b29" stop-opacity="0"/><stop offset=".7" stop-color="#2d3b29"/></linearGradient><clipPath id="shinclip"><path d="M72 70 Q70 60 80 56 H120 Q130 60 128 70 L118 196 H82 Z"/></clipPath></defs>
  <path d="M66 0 H134 L126 58 H74 Z" fill="url(#thighfade)"/>
  <path d="M72 70 Q70 60 80 56 H120 Q130 60 128 70 L118 196 H82 Z" fill="#2d3b29"/>
  <g clip-path="url(#shinclip)"><rect x="60" y="50" width="40" height="150" fill="{L5}" opacity=".5"/><rect x="100" y="50" width="40" height="150" fill="{L4}" opacity=".5"/></g>
  <ellipse cx="100" cy="58" rx="22" ry="12" fill="{L4}" opacity=".75"/>
  <path d="M82 196 H118 L146 238 Q146 246 138 246 H62 Q54 246 54 238 Z" fill="{L5}" opacity=".55"/>
  <path d="M82 196 L60 238 Q56 246 62 246 H74 L90 200 Z" fill="{S1}" opacity=".8"/>
  <g>
    <circle cx="136" cy="250" r="9" fill="{L5}"/><circle cx="118" cy="252" r="6.5" fill="{L5}"/><circle cx="102" cy="253" r="6" fill="{L5}"/>
    <circle cx="87" cy="252" r="5.5" fill="{S1}"/><circle cx="73" cy="249" r="5" fill="{S1}"/>
  </g>
  <g font-family="Figtree,system-ui,sans-serif" font-size="15" font-weight="600">
    <text x="146" y="62" fill="{L4}">L4</text><text x="148" y="140" fill="{L4}">L4</text>
    <text x="30" y="140" fill="{L5}">L5</text><text x="150" y="226" fill="{L5}">L5</text>
    <text x="26" y="236" fill="{S1}">S1</text>
  </g>
</svg>'''

FITIK_FAQ2 = [
 ("Bel fıtığı kendiliğinden geçer mi?", "Çoğu kişide evet. Bacak ağrısı genellikle haftalar ya da birkaç ay içinde azalır. Üstelik fıtık MR'da da küçülebilir: dışarı taşmış fıtıkların yaklaşık %70'inde, tamamen kopmuş parçaların ise %96'sında kendiliğinden gerileme görülmüş."),
 ("Ameliyat şart mı?", "Çoğu zaman hayır. 6–12 haftadır siyatiği olan hastaların karşılaştırıldığı bir çalışmada erken ameliyat bacak ağrısını daha hızlı geçirdi, ama bir yılın sonunda iki grubun sonuçları benzerdi ve her iki grupta da hastaların %95'i kendini iyileşmiş hissetti. İdrar ya da dışkı kontrolü kaybı ve ilerleyen güç kaybı ise acil ameliyat gerektirebilir."),
 ("Oturmak mı, ayakta durmak mı daha iyi?", "Bel fıtığında uzun süre oturmak çoğu kişide ağrıyı artırır. Oturma sürelerini kısa tutun, sık sık kalkıp birkaç adım yürüyün. Kısa ve sık yürüyüşler genellikle iyi gelir."),
 ("Bel fıtığında spor yapabilir miyim?", "Evet, ağrının izin verdiği ölçüde. Yürüyüş ve yüzme gibi hafif aktivitelerle başlayıp bel ve kalça kaslarını güçlendiren egzersizlere geçmek iyileşmeyi destekler. Ağrıyı bacağa doğru yayan hareketlerden bir süre kaçının."),
 ("MR'da fıtığım var ama ağrım yok. Ne yapmalıyım?", "Endişelenmeyin. Hiç ağrısı olmayan 20 yaşındakilerin yaklaşık üçte birinde bile MR'da disk fıtığı (protrüzyon) görülür. Şikâyetiniz yoksa tedavi gerekmez; düzenli egzersizle bel sağlığınızı koruyun."),
]
FITIK_SRC2 = [
 SRC_BRINJIKJI,
 "Chiu CC, Chuang TY, Chang KH, Wu CH, Lin PW, Hsu WY. The probability of spontaneous regression of lumbar herniated disc: a systematic review. Clin Rehabil. 2015;29(2):184-195.",
 SRC_NICE59,
 "Peul WC, van Houwelingen HC, van den Hout WB, et al. " + ext("https://www.nejm.org/doi/full/10.1056/NEJMoa064039", "Surgery versus prolonged conservative treatment for sciatica") + ". N Engl J Med. 2007;356(22):2245-2256.",
 "Physiopedia. " + ext("https://www.physio-pedia.com/Lumbar_Radiculopathy", "Lumbar Radiculopathy") + ".",
]

BELF_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Bel fıtığı ve siyatik</h1>
    <p class="lede">Beldeki bir diskin taşarak bacağa giden sinir kökünü sıkıştırmasıyla ortaya çıkar. Ağrı kalçadan bacağa, bazen ayağa kadar vurur. İyi haber: çoğu kişi ameliyatsız iyileşir, fıtık çoğu zaman kendiliğinden küçülür.</p>
    <p class="meta">Son güncelleme: {UPDATED}</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%95</b><span>Bel fıtıklarının L4–L5 ya da L5–S1 seviyesinde görülme oranı</span></div>
        <div class="stat"><b>%70</b><span>Dışarı taşmış fıtıklarda kendiliğinden gerileme</span></div>
        <div class="stat"><b>%95</b><span>Bir yılın sonunda kendini iyileşmiş hisseden siyatik hastası</span></div>
        <div class="stat"><b>%29</b><span>Hiç ağrısı olmayan 20 yaşındakilerin MR'ında disk fıtığı</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Omurlar arasındaki diskin dış halkası zayıflayıp yırtıldığında, içindeki jel kıvamındaki çekirdek dışarı taşar. Taşan kısım bacağa giden sinir köküne baskı yapar ve orada iltihaplanmaya yol açar.</p>
        <p class="soft">Siyatik bir hastalığın adı değil, bir belirtidir: siyatik siniri boyunca kalçadan bacağa yayılan ağrı. En sık nedeni bel fıtığıdır.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Kalçadan bacağa, çoğunlukla dizin altına ve ayağa yayılan ağrı; bacak ağrısı çoğu zaman bel ağrısından baskındır</li>
          <li>Bacakta ya da ayakta uyuşma, karıncalanma, elektriklenme</li>
          <li>Ayakta ya da bacakta güçsüzlük</li>
          <li>Öksürmek, hapşırmak ve uzun oturmak ağrıyı artırabilir</li>
        </ul>
        <p class="soft">Ağrı bacağa yayılmıyorsa: <a href="bel-agrisi.html">Bel ağrısı sayfası →</a></p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap roots">
      <div>
        <h2>Hangi sinir nereye vurur?</h2>
        <p class="soft">Sıkışan sinir köküne göre ağrı ve uyuşma farklı bölgelere yayılır. Bel fıtıklarının %95'i en alttaki iki seviyede olduğu için en sık L5 ve S1 kökleri etkilenir.</p>
        <ul class="rl">
          {root_row(L4, "L4", "Dizin önü, bacağın iç yanı", "Dizi düzeltme, ayak bileğini yukarı kaldırma")}
          {root_row(L5, "L5", "Bacağın dış yanı, ayak üstü ve başparmak", "Başparmağı yukarı kaldırma, topuk üstünde yürüme")}
          {root_row(S1, "S1", "Baldırın arkası, topuk, ayağın dış kenarı ve küçük parmak", "Parmak ucunda yürüme")}
        </ul>
      </div>
      {LEG}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tanı: MR ne zaman gerekir?</h2>
      <p class="soft">Tanı önce muayeneyle konur. Sırtüstü yatarken düz bacağın kaldırılmasıyla bacak ağrısının tetiklenmesi (düz bacak kaldırma testi), kas gücü, refleksler ve duyu muayenesi en önemli ipuçlarıdır.</p>
      <div class="callout">
        <p>MR, ameliyat ya da enjeksiyon düşünülüyorsa ya da uyarı işaretleri varsa gereklidir. Ağrısı olmayan kişilerde de disk fıtığı sık görüldüğü için MR bulgusu mutlaka şikâyetler ve muayeneyle birlikte değerlendirilmelidir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Seyri ve tedavi</h2>
      <p class="soft">Bel fıtığının doğal seyri çoğu zaman iyidir. Vücut taşan disk parçasını zamanla temizleyebilir; ne kadar büyük taşmışsa gerileme olasılığı o kadar yüksektir. 6–12 haftadır şiddetli siyatiği olan 283 hastanın karşılaştırıldığı çalışmada, ameliyatsız izlenen grubun %39'u sonunda ameliyat oldu; bir yılın sonunda iki grubun sonuçları benzerdi.</p>
      <ul class="tx">
        <li><b>Hareketli kalmak</b><span>Yatak istirahati önerilmez. Ağrıyı çok artıran pozisyonlardan kaçınarak kısa ve sık yürüyüşler yapın.</span></li>
        <li><b>Egzersiz</b><span>Ağrıyı bacaktan bele doğru çeken hareketler, sinir kaydırma egzersizleri ve zamanla bel-kalça kaslarını güçlendirme tedavinin temelidir.</span></li>
        <li><b>Manuel terapi</b><span>Egzersizle birlikte uygulanan manuel terapi, kılavuzlarda tedavi paketinin parçası olarak önerilir.</span></li>
        <li><b>İlaç ve enjeksiyon</b><span>Hekiminizin önerdiği ağrı kesiciler. Akut ve şiddetli siyatikte seçilmiş hastalarda sinir köküne yönelik epidural enjeksiyon hekim kararıyla uygulanabilir.</span></li>
        <li><b>Ameliyat</b><span>Ameliyatsız tedaviye rağmen ağrı ve kısıtlılık sürüyorsa ve MR bulguları şikâyetlerle uyuşuyorsa düşünülür. İdrar ya da dışkı kontrolü kaybı ve ilerleyen güç kaybı ise acil değerlendirme gerektirir.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Siyatikte dört egzersiz</h2>
      <p class="soft">Egzersiz sırasında bacak ağrısı bele doğru çekiliyorsa bu iyiye işarettir. Ağrı, uyuşma ya da karıncalanma bacaktan ayağa doğru ilerliyorsa o egzersizi bırakın. Güçlendirme için <a href="bel-agrisi.html#egzersizler">bel ağrısı egzersizlerine</a> de bakabilirsiniz.</p>
      {ex_grid(["9090", "pressup", "slump", "bridge"], "ex four")}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Siyatik ve bel fıtığı için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("UPFQGxojsMY", "Siyatik egzersizleri videosunu oynat", "3 Safe Exercises For Sciatica Pain Relief")}
          <h3>Siyatikte güvenli üç egzersiz</h3>
          <p>Bacağa yayılan ağrıda başlangıç için güvenli hareketler.</p>
        </div>
        <div class="vid">
          {vbox("Nf3lswVsJ1g", "Siyatik ve fıtık egzersizi videosunu oynat", "Best Exercise For Sciatic Pain Relief, Herniated Disc, &amp; Spinal Stenosis")}
          <h3>Siyatik, fıtık ve dar kanal için egzersiz</h3>
          <p>Bel fıtığı ve kanal darlığında öne çıkan egzersiz ve doğru yapılışı.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(FITIK_FAQ2)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu belirtiler kauda ekina sendromu denen ve acil ameliyat gerektirebilen bir tabloyu ya da ciddi sinir hasarını gösterebilir. Beklemeden acile başvurun:</p>
      <ul class="dots redflags">
        <li>İdrar yapamama ya da idrarı tutamama</li>
        <li>Dışkı kaçırma</li>
        <li>Kasık, makat ve iç bacaklarda uyuşma ("eyer bölgesi")</li>
        <li>Cinsel işlevde yeni başlayan kayıp</li>
        <li>İki bacakta birden siyatik ağrısı, uyuşma ya da güçsüzlük</li>
        <li>Ayağı yukarı kaldıramama (düşük ayak) ya da hızla artan güç kaybı</li>
        <li>Ateş, nedensiz kilo kaybı ya da kanser öyküsüyle birlikte ağrı</li>
      </ul>
      {CTA_CARD("Bel fıtığı ve siyatik ağrınız", "bel fıtığı ve siyatik")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(FITIK_SRC2)}
    </div>
  </section>
</main>'''

page("bel-fitigi.html", "Bel Fıtığı",
     "Bel fıtığı ve siyatik: belirtiler, hangi sinir nereye vurur, fıtık kendiliğinden geçer mi, ameliyat ne zaman gerekir? Evde egzersizler, videolar ve acil uyarı işaretleri.",
     "bel-fitigi.html", NECK_CSS, BELF_BODY, YT_JS,
     seo_title="Bel Fıtığı ve Siyatik: Belirtiler, Tedavi ve Egzersizler | İhsan Eren", condition="Bel fıtığı (lomber disk hernisi)",
     faq_items=pick(FITIK_FAQ2, 0, 1, 3, 4))

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
SRC_NICE59 = ("National Institute for Health and Care Excellence. " + ext("https://www.nice.org.uk/guidance/ng59", "Low back pain and sciatica in over 16s: assessment and management (NG59)") + ". Londra: NICE; 2016, güncelleme 2020 ve 2026.")
SRC_BRINJIKJI = ("Brinjikji W, Luetmer PH, Comstock B, et al. " + ext("https://www.ajnr.org/content/36/4/811", "Systematic literature review of imaging features of spinal degeneration in asymptomatic populations") + ". AJNR Am J Neuroradiol. 2015;36(4):811-816.")

# ------------------------------------------------------------------ BEL AĞRISI
BEL_FAQ = [
 ("Yatak istirahati yapmalı mıyım?", "Hayır. Kılavuzlar hareketli kalmayı öneriyor. Çok ağrılı ilk bir iki günde dinlenmek doğaldır ama uzun süre yatmak kasları zayıflatır ve iyileşmeyi geciktirebilir. Ağrının izin verdiği ölçüde yürüyün ve günlük işlerinize devam edin."),
 ("Bel korsesi takmalı mıyım?", "Genellikle hayır. Bel ağrısı ve siyatik için hazırlanan İngiltere kılavuzu (NICE) korse, tabanlık ve bel çekme (traksiyon) tedavilerini önermiyor. Korseyi uzun süre kullanmak kasların çalışmasını azaltabilir."),
 ("MR çektirmem gerekir mi?", "Çoğu zaman gerekmez. Ağrısı olmayan kişilerde de disk dejenerasyonu ve disk bombeleşmesi çok sık görülür; MR'da bir bulgu çıkması ağrının nedeninin o olduğu anlamına gelmez. Uyarı işaretleri varsa ya da ameliyat düşünülüyorsa hekiminiz karar verir."),
 ("Sert yatak mı daha iyi?", "Çok sert yatak şart değil. Uzun süren bel ağrısı olan kişilerle yapılan bir çalışmada orta sertlikteki yatak, sert yataktan daha iyi sonuç verdi. Rahat uyuduğunuz, sabah daha az ağrıyla kalktığınız yatak en uygunudur."),
 ("Sıcak uygulama işe yarar mı?", "12 haftadan kısa süren bel ağrısında sıcak uygulama rahatlama sağlayabilir: Amerikan Hekimler Koleji'nin kılavuzu bunu ilk seçenekler arasında sayıyor ve etkisini orta düzeyde buluyor (kanıt orta kalitede). Cildinizi yakmayacak bir sıcaklıkta kullanın; uyuşukluk ya da his azalması olan bölgeye ve uyurken uygulamayın."),
 ("Duruşum bozuk olduğu için mi belim ağrıyor?", "Araştırmalarda oturma, ayakta durma ve yük kaldırma sırasındaki duruş, bel ağrısının başlaması ya da sürmesiyle ilişkili bulunmadı (bu çalışmalar çoğunlukla gözlemseldir). Uzun süre aynı pozisyonda kalmak ağrınızı artırıyorsa pozisyonunuzu sık sık değiştirin ve ara ara kalkıp yürüyün."),
 ("Ağrım geçti, egzersize devam etmeli miyim?", "Evet. Bel ağrısı sık tekrarlar: bir çalışmada ağrısı geçenlerin %69'u bir yıl içinde yeniden bel ağrısı yaşadı. Düzenli egzersiz ve hareketli bir yaşam tekrar riskini azaltmanın en iyi yoludur."),
]
BEL_SRC = [
 SRC_BRINJIKJI,
 "da Silva T, Mills K, Brown BT, et al. Recurrence of low back pain is common: a prospective inception cohort study. J Physiother. 2019;65(3):159-165.",
 "Deyo RA, Diehl AK, Rosenthal M. " + ext("https://www.qxmd.com/r/2945109", "How many days of bed rest for acute low back pain? A randomized clinical trial") + ". N Engl J Med. 1986;315(17):1064–1070.",
 "GBD 2021 Low Back Pain Collaborators. " + ext("https://www.thelancet.com/journals/lanrhe/article/PIIS2665-9913(23)00098-X/fulltext", "Global, regional, and national burden of low back pain, 1990–2020, its attributable risk factors, and projections to 2050") + ". Lancet Rheumatol. 2023;5(6):e316-e329.",
 "Hayden JA, Ellis J, Ogilvie R, Malmivaara A, van Tulder MW. " + ext("https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD009790.pub2/full", "Exercise therapy for chronic low back pain") + ". Cochrane Database Syst Rev. 2021;9:CD009790.",
 "Hartvigsen J, Hancock MJ, Kongsted A, et al. " + ext("https://core.ac.uk/download/153535953.pdf", "What low back pain is and why we need to pay attention") + ". Lancet. 2018. doi:10.1016/S0140-6736(18)30480-X.",
 "Chiarotto A, Koes BW. " + ext("https://www.nejm.org/doi/full/10.1056/NEJMcp2032396", "Nonspecific low back pain") + ". N Engl J Med. 2022;386(18):1732-1740.",
 "Koes BW, van Tulder MW, Thomas S. Diagnosis and treatment of low back pain. BMJ. 2006;332(7555):1430-1434.",
 "Jarvik JG, et al. " + ext("https://www.qxmd.com/r/12783911", "Rapid magnetic resonance imaging vs radiographs for patients with low back pain: a randomized controlled trial") + ". JAMA. 2003.",
 "Kovacs FM, Abraira V, Peña A, et al. Effect of firmness of mattress on chronic non-specific low-back pain: randomised, double-blind, controlled, multicentre trial. Lancet. 2003;362(9396):1599-1604.",
 "Malmivaara A, Häkkinen U, Aro T, et al. " + ext("https://search.pedro.org.au/search-results/record-detail/1657", "The treatment of acute low back pain: bed rest, exercises, or ordinary activity?") + ". N Engl J Med. 1995;332(6):351–355.",
 "Guideline Central. " + ext("https://www.guidelinecentral.com/insights/aug-2026-nice-lowbackpainsciaticaover16-guideline-spotlight/", "Aug 2026 NICE guideline spotlight: low back pain and sciatica in over 16s") + ". NICE NG59 Temmuz 2026 güncellemesinin özeti; ayrıca " + ext("https://www.physitrack.com/insights/nice-low-back-pain-guideline-update-2026", "Physitrack") + ".",
 SRC_NICE59,
 "Physiopedia. " + ext("https://www.physio-pedia.com/Non_Specific_Low_Back_Pain", "Non Specific Low Back Pain") + ".",
 "O'Sullivan PB, Caneiro JP, O'Sullivan K, et al. " + ext("https://www.paulogentil.com/pdf/Back%20to%20Basics%20-%2010%20Facts%20Every%20Person%20Should%20Know%20About%20Back%20Pain.pdf", "Back to basics: 10 facts every person should know about back pain") + ". Br J Sports Med. 2020. doi:10.1136/bjsports-2019-101611.",
 "Physiopedia. " + ext("https://www.physio-pedia.com/Williams_Flexion_Exercise", "Williams Flexion Exercise") + ".",
 "Qaseem A, et al. " + ext("https://www.aafp.org/pubs/afp/issues/2017/0915/p407.html", "Noninvasive treatments for acute, subacute, and chronic low back pain: a clinical practice guideline from the American College of Physicians") + ". Ann Intern Med. 2017. Özet: American Family Physician.",
 "Sieper J, van der Heijde D, Landewé R, et al. " + ext("https://ard.bmj.com/content/68/6/784", "New criteria for inflammatory back pain in patients with chronic back pain: a real patient exercise by experts from the Assessment of SpondyloArthritis international Society (ASAS)") + ". Ann Rheum Dis. 2009;68(6):784–788.",
 "Wallwork SB, Braithwaite FA, O'Keeffe M, et al. " + ext("https://www.cmaj.ca/content/196/2/E29", "The clinical course of acute, subacute and persistent low back pain: a systematic review and meta-analysis") + ". CMAJ. 2024;196(2):E29-E46.",
]

BEL_TL = [
 ("1986", "Akut bel ağrısı olan 203 kişiyle yapılan çalışmada 2 gün yatak istirahati önerilenler, 7 gün önerilenler kadar iyi sonuç aldı ve %45 daha az iş günü kaybetti."),
 ("1995", "Finlandiya'da akut bel ağrısı olan 186 çalışanla yapılan çalışmada ağrının izin verdiği ölçüde olağan işlerine devam edenler, yatak istirahati yapanlardan ve fizyoterapistin öğrettiği bel hareketlendirme egzersizlerini yapanlardan daha hızlı iyileşti."),
 ("2003", "ABD'de 380 hastayla yapılan çalışmada ilk görüntüleme olarak röntgen yerine hızlı MR çekilenlerin bir yıl sonraki durumu, röntgen çekilenlerle neredeyse aynıydı."),
 ("2015", "Ağrısı olmayan kişilerin MR ve BT görüntülerini inceleyen bir derleme, disk aşınması ve bombeleşmesinin yaşla birlikte çok sık görüldüğünü gösterdi."),
 ("2016", "İngiltere'nin NICE kılavuzu yayımlandı: bel ağrısında rutin görüntüleme, korse, traksiyon, akupunktur, TENS ve omurgaya yapılan iğne (enjeksiyon) tedavilerinin uygulanmaması önerildi; hareketli kalmak öne çıktı."),
 ("2017", "Amerikan Hekimler Koleji (ACP), ilaçlardan önce ilaç dışı tedavileri önerdi: 12 haftadan kısa süren ağrıda sıcak uygulama, masaj, akupunktur ya da manipülasyon; uzun süren ağrıda egzersiz, yoga, tai chi ve bilişsel davranışçı terapi gibi seçenekler."),
 ("2018", "The Lancet'teki bir makale dizisi bel ağrısını küresel bir halk sağlığı sorunu olarak ele aldı; bel ağrısı olanların %1'inden azında ciddi bir hastalık bulunduğunu vurguladı."),
 ("2024", "95 çalışmayı inceleyen bir derleme, yeni başlayan bel ağrısının çoğunlukla ilk 6 haftada belirgin şekilde azaldığını, uzun süren ağrıda ise düzelmenin yavaş olduğunu gösterdi."),
 ("2026", "NICE, dayandığı kanıtın bir kısmı sonradan geri çekildiği için psikolojik tedavilere ilişkin önerilerini kılavuzdan çıkardı ve yerine yeni bir öneri yapmadı; Amerikan Hekimler Koleji'nin 2017 kılavuzu ise bilişsel davranışçı terapiyi seçenekler arasında sayıyor."),
]

BEL_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Bel ağrısı</h1>
    <p class="lede">Dünyada yeti yitimiyle (sakatlıkla) geçirilen yılların bir numaralı nedeni. Kulağa korkutucu gelse de çoğu bel ağrısının altında ciddi bir hastalık yoktur ve yeni başlayan ağrıların çoğu birkaç haftada belirgin şekilde azalır. İyileşmenin anahtarı dinlenmek değil, hareket etmektir.</p>
    <p class="meta">Son güncelleme: 30 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>619 milyon</b><span>Dünyada bel ağrısı yaşayan kişi (2020)</span></div>
        <div class="stat"><b>1. sırada</b><span>Dünyada yeti yitimiyle geçen yıllara en çok yol açan neden</span></div>
        <div class="stat"><b>%80–90</b><span>Belirli bir yapısal neden bulunamayan bel ağrısı</span></div>
        <div class="stat"><b>%69</b><span>Ağrısı geçenlerde bir yıl içinde tekrar</span></div>
      </div>
      {g_toc([("nedir", "Nedir?"), ("turler", "Türleri"), ("mr", "MR ne anlatır?"), ("gercekler", "10 gerçek"), ("tarihce", "Geçmişten bugüne"), ("tedavi", "Tedavi seçenekleri"), ("egzersizler", "Egzersizler"), ("gunluk", "Günlük hayatta"), ("videolar", "Videolar"), ("sss", "Sık sorulan sorular"), ("uyari", "Uyarı işaretleri")])}
    </div>
  </section>

  <section id="nedir">
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Kaburgaların alt sınırı ile kalça kıvrımı arasındaki ağrıdır. Bel ağrılarının yaklaşık %80–90'ında belirli bir yapısal neden bulunamaz; buna <em>nonspesifik</em> ya da mekanik bel ağrısı denir. Ağrı gerçektir ama beldeki bir "kırılma" ya da "kayma"yı göstermez. Kaslar, bağlar, eklemler ve sinir sisteminin ağrıya duyarlılığı birlikte rol oynar.</p>
        <p class="soft">Ağrı dizin altına, bacağa ve ayağa uyuşma ya da karıncalanmayla yayılıyorsa bir sinir kökü etkileniyor olabilir: <a href="bel-fitigi.html">Bel fıtığı ve siyatik →</a></p>
      </div>
      <div>
        <h2>Neler tetikleyebilir, riski artırabilir?</h2>
        <ul class="dots">
          <li>Uzun süre hareketsiz kalmak, örneğin saatlerce oturmak (var olan ağrıyı artırabilir)</li>
          <li>Alışık olunmayan ağır kaldırma, ani dönme ya da zorlanma</li>
          <li>Hareketsizlik ve düşük fiziksel kondisyon</li>
          <li>Fazla kilo ve sigara</li>
          <li>Stres, kaygı, yorgunluk ve uykusuzluk</li>
          <li>Fiziksel olarak ağır işler</li>
        </ul>
        <p class="soft">Küresel hastalık yükü hesaplarına göre bel ağrısına bağlı yeti yitiminin yaklaşık %39'u iş kaynaklı etkenlere, sigaraya ve yüksek vücut ağırlığına bağlanıyor; bu, yükün bir kısmının önlenebilir olabileceğini düşündürüyor.</p>
      </div>
    </div>
  </section>

  <section id="turler">
    <div class="wrap">
      <h2>Bel ağrısının türleri</h2>
      <p class="soft">Bel ağrısı hem ne kadar süredir devam ettiğine hem de nedenine göre gruplandırılır. Bu gruplama, neyin beklenebileceğini ve ne zaman ileri değerlendirme gerektiğini anlamaya yardım eder.</p>
      <h3 class="g-h3">Süreye göre</h3>
      <div class="kinds">
        <div class="kind"><span class="n">6 haftadan kısa</span><h3>Yeni başlayan (akut)</h3><p>Ağrı ve kısıtlılık çoğu zaman ilk 6 haftada belirgin şekilde azalır. 9.224 kişinin verisini birleştiren bir analizde ortalama ağrı puanı 100 üzerinden 56'dan 6. haftada 26'ya, 1. yılda 21'e indi.</p></div>
        <div class="kind"><span class="n">6–12 hafta</span><h3>Subakut</h3><p>Aynı analizde bu gruptaki ağrı puanı sonraki 6 haftada belirgin şekilde azaldı (63'ten 29'a), sonra 1. yılın sonuna kadar pek değişmedi (31).</p></div>
        <div class="kind"><span class="n">12 haftadan uzun</span><h3>Uzun süren (kronik)</h3><p>Düzelme daha yavaştır: aynı analizde ağrı puanı başlangıçta 56, 1. yılda 40'tı (bu grubun sonuçlarının kesinliği çok düşük). Düzenli egzersiz ve aktif bir tedavi programı burada daha da önem kazanır.</p></div>
      </div>
      <h3 class="g-h3">Nedene göre</h3>
      <div class="kinds">
        <div class="kind"><h3>Nonspesifik (mekanik) bel ağrısı</h3><p>En sık türdür: bel ağrılarının yaklaşık %80–90'ında belirli bir yapısal neden bulunamaz. Ağrı genellikle hareketle ve pozisyonla değişir.</p></div>
        <div class="kind"><h3>Sinir kökü kaynaklı ağrı (siyatik)</h3><p>Ağrı dizin altına, bacağa ve ayağa yayılır; uyuşma ve karıncalanma eşlik edebilir. En sık nedeni bel fıtığıdır.</p><a href="bel-fitigi.html">Bel fıtığı ve siyatik →</a></div>
        <div class="kind"><h3>Ciddi bir hastalığa bağlı ağrı</h3><p>Kırık, enfeksiyon, tümör ya da kauda ekina sendromu gibi nedenler bel ağrısı olanların %1'inden azında bulunur. Uyarı işaretleri bu yüzden önemlidir.</p><a href="#uyari">Uyarı işaretleri →</a></div>
      </div>
      <div class="callout">
        <p><strong>Mekanik mi, iltihaplı mı?</strong> Gençlerde yavaş başlayan ve aylarca süren bel ağrısı bazen omurganın iltihaplı bir hastalığından (aksiyel spondiloartrit, örneğin ankilozan spondilit) kaynaklanır. Uluslararası ASAS ölçütlerine göre 3 aydan uzun süren bel ağrısında şu beş özellikten en az dördü varsa iltihaplı (inflamatuvar) bel ağrısından şüphelenilir: 40 yaşından önce başlaması, sinsi ve yavaş başlaması, egzersizle azalması, dinlenmekle geçmemesi ve gece ağrıyıp kalkınca azalması. Bu bir tanı değildir ve ölçütler kusursuz değildir; bu özellikler varsa bir hekime başvurun. <a href="ankilozan-spondilit.html">Ankilozan spondilit rehberi →</a></p>
      </div>
    </div>
  </section>

  <section id="mr">
    <div class="wrap">
      <h2>MR'daki "düzleşme", "bombeleşme", "aşınma" ne anlama geliyor?</h2>
      <p class="soft">Beldeki diskler yaşla birlikte, tıpkı saçın beyazlaması gibi değişir. Hiç ağrısı olmayan binlerce kişinin MR ve BT görüntülerini inceleyen bir derlemede:</p>
      <div class="stats" style="margin-top:14px">
        <div class="stat"><b>%52</b><span>30 yaşında disk dejenerasyonu (aşınma)</span></div>
        <div class="stat"><b>%40</b><span>30 yaşında disk bombeleşmesi</span></div>
        <div class="stat"><b>%80</b><span>50 yaşında disk dejenerasyonu</span></div>
        <div class="stat"><b>%60</b><span>50 yaşında disk bombeleşmesi</span></div>
      </div>
      <div class="callout">
        <p>Bu kişilerin hiçbirinde bel ağrısı yoktu. Yani MR raporundaki bu ifadeler çoğu zaman yaşa bağlı normal değişikliklerdir ve tek başına ağrının nedenini açıklamaz. Bu yüzden kılavuzlar bel ağrısında rutin görüntüleme önermez.</p>
      </div>
      <p class="soft" style="margin-top:14px">ABD'de 380 hastayla yapılan bir çalışmada ilk görüntüleme olarak röntgen yerine hızlı MR çekilenlerin bir yıl sonraki ağrı ve işlev durumu, röntgen çekilenlerle neredeyse aynıydı. MR grubunda daha fazla bel ameliyatı yapıldı (10'a karşı 4), ancak bu fark istatistiksel olarak anlamlı değildi.</p>
    </div>
  </section>

  <section id="gercekler">
    <div class="wrap">
      <p class="eyebrow">Araştırmacılardan</p>
      <h2>Bel ağrısı hakkında 10 gerçek</h2>
      <p class="soft">Bir grup araştırmacının British Journal of Sports Medicine'de yayımladığı yazı, uyarı işaretleri ve ciddi bir neden dışlandıktan sonra bel ağrısı olan herkesin bilmesi gereken 10 gerçeği özetliyor. Bu bir uzman görüşü yazısıdır; dayandığı çalışmalara yazının kaynakçasından ulaşılabilir.</p>
      <ol class="g-facts">
        <li><b>Bel ağrısı hayatı tehdit eden ciddi bir hastalık değildir.</b>Uyarı işaretleri yoksa ve ciddi bir neden dışlandıysa.</li>
        <li><b>Çoğu bel ağrısı atağı düzelir.</b>Bel ağrısı yaşla birlikte kaçınılmaz olarak kötüleşmez.</li>
        <li><b>Düşünceler ve davranışlar önemlidir.</b>Olumsuz düşünceler, hareketten kaçınma, olumsuz iyileşme beklentisi ve ağrıyla baş etmekte zorlanmak, uzun süren ağrıyla doku hasarından daha güçlü ilişkilidir.</li>
        <li><b>Görüntüleme, ağrının seyrini belirlemez.</b>MR ya da röntgen, mevcut ağrının nasıl seyredeceğini göstermez.</li>
        <li><b>Hareket güvenlidir.</b>Kademeli egzersiz ve her yöne hareket omurga için güvenli ve sağlıklıdır.</li>
        <li><b>Duruşun etkisi sanıldığı kadar büyük değil.</b>Otururken, ayakta dururken ve yük kaldırırken omurganın duruşu, araştırmalarda bel ağrısının başlaması ya da sürmesiyle ilişkili bulunmadı (bu çalışmalar çoğunlukla gözlemseldir).</li>
        <li><b>Zayıf karın-gövde kasları bel ağrısına yol açmaz.</b>Gövde kaslarını güçlü tutmak iyidir; ancak bel ağrısı olan bazı kişiler bu kasları gereğinden fazla gerer, gerekmediğinde gevşetebilmek de önemlidir.</li>
        <li><b>Kademeli yük omurgayı güçlendirir.</b>Omurgayı yavaş yavaş artan şekilde hareket ettirmek ve yüklemek güvenlidir ve onu dayanıklı kılar.</li>
        <li><b>Alevlenmeler hasar demek değildir.</b>Ağrı alevlenmeleri yapısal hasardan çok etkinlikteki değişiklikler, stres ve ruh haliyle ilişkilidir.</li>
        <li><b>Etkili bakım görece ucuz ve güvenlidir.</b>Kişiye özel bilgilendirme, olumlu bir bakış kazanmaya destek ve fiziksel ve sosyal etkinlik, uyku, sağlıklı kilo ve işe devam etme konusunda yönlendirme bunun parçalarıdır.</li>
      </ol>
    </div>
  </section>

  <section id="tarihce">
    <div class="wrap">
      <p class="eyebrow">Geçmişten bugüne</p>
      <h2>Bel ağrısı tedavisinin kısa tarihi</h2>
      <p class="soft">Bel ağrısında uzun süre yatak istirahati sık önerilen bir tedaviydi. Son 40 yılın araştırmaları hareketli kalmanın, uzun süren ağrıda egzersizin ve ağrıyı doğru anlamanın daha yararlı olduğunu gösterdi.</p>
      {g_tl(BEL_TL)}
    </div>
  </section>

  <section id="tedavi">
    <div class="wrap">
      <h2>Seyri ve tedavi</h2>
      <p class="soft">Yeni başlayan bel ağrısında ağrı ve kısıtlılık genellikle ilk 6 haftada belirgin şekilde azalır; çalışmalarda ağrı puanı ortalama yarıdan fazla düştü. Üç aydan uzun süren ağrıda düzelme daha yavaştır; burada düzenli egzersiz ve yönlendirilmiş bir tedavi programı daha da önem kazanır.</p>
      <ul class="tx">
        <li><b>Hareketli kalmak</b><span>Yatak istirahati önerilmez. Yürümek ve günlük işlere ağrının izin verdiği ölçüde devam etmek iyileşmeyi destekler; mümkünse işten uzun süre uzak kalmayın.</span></li>
        <li><b>Egzersiz</b><span>Uzun süren bel ağrısında tedavinin temelidir: egzersiz yapanların ağrısı, tedavi almayan, olağan bakım ya da plasebo alanlara göre 3. ayda 100 üzerinden ortalama 15 puan daha az bulundu. En iyi egzersiz, düzenli yapabildiğiniz egzersizdir. Yeni başlayan ağrıda en önemlisi hareketli kalmak ve günlük işlere devam etmektir.</span></li>
        <li><b>Manuel terapi</b><span>Mobilizasyon, manipülasyon ve yumuşak doku teknikleri NICE kılavuzunda tek başına değil, yalnızca egzersizi içeren bir paketin parçası olarak düşünülebilir; ACP kılavuzunda manipülasyon tek başına da seçenekler arasında, ancak etkisi küçük.</span></li>
        <li><b>Ağrıyla baş etme</b><span>Uzun süren ağrıda korku, kaygı ve uykusuzluk ağrıyı besler. Kaygı ya da çökkünlük belirginse destek seçeneklerini hekiminizle konuşabilirsiniz. <a href="stres.html">Nefes egzersizlerine göz atın →</a></span></li>
      </ul>
      <h3 class="g-h3">Tedavi seçenekleri: kılavuzlar ne diyor?</h3>
      <p class="soft">İngiltere'nin NICE kılavuzu (2016, son güncelleme 2026) ile Amerikan Hekimler Koleji'nin (ACP, 2017) önerileri yan yana. Kılavuzlar her konuda aynı fikirde değil; tedavi kişiye göre seçilir. Bacağa yayılan siyatik ağrısında öneriler farklı olabilir: <a href="bel-fitigi.html">Bel fıtığı ve siyatik →</a></p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Egzersiz</h3><dl><dt>NICE</dt><dd>Hareketli kalmayı teşvik ediyor; yeni bir atak ya da alevlenmede grup egzersiz programı düşünülebilir.</dd><dt>ACP</dt><dd>Uzun süren ağrıda ilk seçenekler arasında; yoga, tai chi ve motor kontrol egzersizleri de sayılıyor. 12 haftadan kısa süren ağrı için egzersiz önermiyor, hareketli kalmayı öneriyor.</dd><dt>Kanıt</dt><dd>Uzun süren ağrıda 3. ayda ağrı, tedavi almayan, olağan bakım ya da plasebo alanlara göre 100 üzerinden ortalama 15 puan daha az (Cochrane, 2021; kanıt orta kesinlikte).</dd></dl></div>
        <div class="kind"><h3>Manuel terapi</h3><dl><dt>NICE</dt><dd>Manipülasyon, mobilizasyon ve masaj gibi yumuşak doku teknikleri yalnızca egzersizi içeren bir paketin parçası olarak düşünülebilir.</dd><dt>ACP</dt><dd>Manipülasyon seçenekler arasında; etkisi küçük.</dd></dl></div>
        <div class="kind"><h3>Sıcak uygulama ve masaj</h3><dl><dt>ACP</dt><dd>12 haftadan kısa süren ağrıda ilk seçenekler arasında. Sıcak uygulamanın etkisi orta düzeyde (kanıt orta kalitede); masajın etkisi kısa süreli (kanıt düşük kalitede).</dd></dl></div>
        <div class="kind"><h3>Psikolojik yaklaşımlar</h3><dl><dt>ACP</dt><dd>Uzun süren ağrıda bilişsel davranışçı terapi ve farkındalık temelli stres azaltma seçenekler arasında.</dd><dt>NICE</dt><dd>Dayandığı kanıtın bir kısmı geri çekildiği için Temmuz 2026'da bu önerileri kılavuzdan çıkardı ve yerine yeni bir öneri yapmadı. Bu, psikolojik desteğin işe yaramadığı anlamına gelmez.</dd></dl></div>
        <div class="kind"><h3>Akupunktur</h3><dl><dt>ACP</dt><dd>Seçenekler arasında: 12 haftadan kısa süren ağrıda ağrıya etkisi küçük; uzun süren ağrıda 3 aya kadar orta düzeyde, işleve etkisi yok (kanıt düşük kalitede).</dd><dt>NICE</dt><dd>Bel ağrısında uygulanmamasını öneriyor.</dd><dt>Not</dt><dd>Türkiye'de yalnızca yetkili hekimler uygulayabilir.</dd></dl></div>
        <div class="kind"><h3>Korse, tabanlık, traksiyon, elektroterapi</h3><dl><dt>NICE</dt><dd>Bel ağrısında korse, tabanlık, bel çekme (traksiyon), TENS, ultrason ve enterferansiyel akım tedavilerinin uygulanmamasını öneriyor.</dd></dl></div>
        <div class="kind"><h3>İlaçlar</h3><dl><dt>Kılavuzlar</dt><dd>NICE, önerdiği ilaçların en düşük etkili dozda ve mümkün olan en kısa süre kullanılmasını öneriyor; bazı ilaç gruplarının bel ağrısında kullanılmamasını öneriyor. Kılavuzlar bazı ilaç gruplarında farklı görüşte. Hangisinin size uygun olduğuna hekiminiz karar verir.</dd></dl></div>
        <div class="kind"><h3>Omurgaya enjeksiyon ve ameliyat</h3><dl><dt>NICE</dt><dd>Bel ağrısında omurgaya yapılan iğne (enjeksiyon) tedavilerinin ve disk protezinin uygulanmamasını öneriyor; füzyon ameliyatı yalnızca araştırma kapsamında. Diğer tedavilerin yetmediği seçilmiş uzun süren ağrıda radyofrekans denervasyon için değerlendirme düşünülebilir.</dd></dl></div>
      </div>
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

  <section id="gunluk">
    <div class="wrap two">
      <div>
        <h2>Günlük hayatta beliniz için</h2>
        <p class="soft">Bel, sanıldığından çok daha sağlam bir yapıdır ve düzenli hareketle güçlenir. Eğilmekten ya da yük kaldırmaktan korkmak yerine, vücudunuzu yavaş yavaş alıştırmak daha doğrudur.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Yarım saatte bir kalkın, birkaç adım yürüyün; uzun oturmayı bölün.</li>
        <li>Ağır yükleri kaldırmaya vücudunuzu yavaş yavaş alıştırın. Araştırmalarda kaldırırken belin düz ya da eğik tutulması bel ağrısı riskiyle ilişkili bulunmadı; size rahat gelen ve kontrol edebildiğiniz şekilde kaldırın.</li>
        <li>Haftanın çoğu günü yürüyün; kısa yürüyüşler de sayılır.</li>
        <li>Uyku düzenine dikkat edin; yorgunluk ağrıya duyarlılığı artırır.</li>
        <li>Sigarayı bırakmak ve fazla kiloları vermek bel ağrısı riskini azaltmaya yardımcı olabilir.</li>
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

  <section id="sss">
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(BEL_FAQ)}
    </div>
  </section>

  <section id="uyari">
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
 ("Bel fıtığı kendiliğinden geçer mi?", "Çoğu kişide evet. Bacak ağrısı genellikle haftalar ya da birkaç ay içinde azalır. Üstelik fıtık MR'da da küçülebilir: dışarı taşmış fıtıkların yaklaşık %70'inde, tamamen kopmuş parçaların ise %96'sında kendiliğinden gerileme görülmüş. Amerikan Ağrı Tıbbı Akademisi'nin 2026 kılavuzu da 6 haftadan kısa süren, bacağa yayılan ya da yayılmayan bel ağrısında, ciddi bir hastalık belirtisi yoksa rutin erken görüntüleme yapılmamasını ve opioidlerin ilk tedavi olarak kullanılmamasını öneriyor."),
 ("Ameliyat şart mı?", "Çoğu zaman hayır. 6–12 haftadır şiddetli siyatiği olan hastaların karşılaştırıldığı bir çalışmada erken ameliyat bacak ağrısını daha hızlı geçirdi, ama bir yılın sonunda iki grubun sonuçları benzerdi ve her iki grupta da hastaların %95'i kendini iyileşmiş hissetti. İdrar ya da dışkı kontrolü kaybı ve ilerleyen güç kaybı ise acil ameliyat gerektirebilir."),
 ("Oturmak mı, ayakta durmak mı daha iyi?", "Bel fıtığında uzun süre oturmak çoğu kişide ağrıyı artırır. Oturma sürelerini kısa tutun, sık sık kalkıp birkaç adım yürüyün. Kısa ve sık yürüyüşler genellikle iyi gelir."),
 ("Bel fıtığında spor yapabilir miyim?", "Evet, ağrının izin verdiği ölçüde. Yürüyüş ve yüzme gibi hafif aktivitelerle başlayıp bel ve kalça kaslarını güçlendiren egzersizlere geçmek iyileşmeyi destekler. Ağrıyı bacağa doğru yayan hareketlerden bir süre kaçının."),
 ("MR'da fıtığım var ama ağrım yok. Ne yapmalıyım?", "Endişelenmeyin. Hiç ağrısı olmayan 20 yaşındakilerin yaklaşık üçte birinde bile MR'da disk fıtığı (protrüzyon) görülür. Şikâyetiniz yoksa tedavi gerekmez; düzenli egzersizle bel sağlığınızı koruyun."),
]
FITIK_SRC2 = [
 SRC_BRINJIKJI,
 "de Castro I, dos Santos DP, Christoph DH, Landeiro JA. " + ext("https://www.scielo.br/j/anp/a/Lv8HLX6cMBMJrgt9BFyJfGQ/?lang=en", "The history of spinal surgery for disc disease: an illustrated timeline") + ". SciELO; 2005.",
 "Jordan JL, Konstantinou K, O'Dowd J. " + ext("https://pmc.ncbi.nlm.nih.gov/articles/PMC3275148/", "Herniated lumbar disc") + ". BMJ Clin Evid. 2011;2011:1118.",
 "Chiu CC, Chuang TY, Chang KH, Wu CH, Lin PW, Hsu WY. The probability of spontaneous regression of lumbar herniated disc: a systematic review. Clin Rehabil. 2015;29(2):184-195.",
 "Deyo RA, Diehl AK, Rosenthal M. " + ext("https://www.qxmd.com/r/2945109", "How many days of bed rest for acute low back pain? A randomized clinical trial") + ". N Engl J Med. 1986;315(17):1064–1070.",
 "Gusmão S, Arantes A, Pinheiro-Franco JL. " + ext("https://link.springer.com/chapter/10.1007/978-3-662-47756-4_2", "A historical overview of sciatica") + ". In: Pinheiro-Franco JL, Vaccaro AR, Benzel EC, Mayer HM, eds. Advanced Concepts in Lumbar Degenerative Disk Disease. Berlin: Springer; 2016.",
 "Mixter WJ, Barr JS. Rupture of the intervertebral disc with involvement of the spinal canal. N Engl J Med. 1934;211:210–215.",
 SRC_NICE59,
 "Peul WC, van Houwelingen HC, van den Hout WB, et al. " + ext("https://www.nejm.org/doi/full/10.1056/NEJMoa064039", "Surgery versus prolonged conservative treatment for sciatica") + ". N Engl J Med. 2007;356(22):2245-2256.",
 "Physiopedia. " + ext("https://www.physio-pedia.com/Lumbar_Radiculopathy", "Lumbar Radiculopathy") + ".",
 "Weber H. " + ext("https://search.pedro.org.au/search-results/record-detail/2195", "Lumbar disc herniation: a controlled, prospective study with ten years of observation") + ". Spine. 1983;8(2):131–140.",
 "American Academy of Pain Medicine. " + ext("https://www.painmed.org/news/acute-low-backpain-guideline-systematic-review-available", "New acute low back pain guideline and systematic review") + ". 5 October 2026. Sistematik derleme: Skelly AC, Chou R, et al. Pain Med. 2026. doi:10.1093/pm/pnag131.",
]

BELF_TL = [
 ("1764", "İtalyan hekim Domenico Cotugno, kalçadan bacağa yayılan ağrıyı kalça eklemi ağrısından ayırarak siyatik sinirle ilişkilendirdi."),
 ("1864", "Fransız hekim Charles Lasègue siyatik üzerine yazdı; bugün muayenede kullanılan düz bacak kaldırma testi onun adıyla da anılır (Lasègue testi)."),
 ("1934", "ABD'li cerrahlar William Mixter ve Joseph Barr, siyatiğin sık bir nedeninin yerinden taşan disk olduğunu gösterdi; bel fıtığı ameliyatı bundan sonra yaygınlaştı."),
 ("1977", "Türk beyin cerrahı Gazi Yaşargil ve Caspar, aynı yıl ayrı ayrı yayımladıkları çalışmalarda mikroskopla yapılan, daha küçük kesili fıtık ameliyatının (mikrodiskektomi) sonuçlarını bildirdi."),
 ("1983", "Norveç'te 126 hastanın 10 yıl izlendiği çalışmada ameliyat olanlar 1. yılda daha iyiydi; 4. yılda iki grup arasındaki fark artık anlamlı değildi."),
 ("1986", "Akut bel ağrısı olan 203 kişiyle yapılan çalışmada 2 günlük yatak istirahati 7 gün kadar etkiliydi ve işe gidilemeyen gün sayısı %45 daha azdı. Uzun yatak istirahati önerisi zamanla bırakıldı."),
 ("2007", "Hollanda'da 6–12 haftadır şiddetli siyatiği olan 283 hastayla yapılan çalışmada erken ameliyat ağrıyı daha hızlı geçirdi, ama 1. yılın sonunda iki grubun sonuçları benzerdi."),
 ("2015", "Derlemeler, dışarı taşmış fıtıkların yaklaşık %70'inin kendiliğinden gerilediğini ve ağrısı olmayan kişilerde de disk bombeleşmesinin yaşla sıklaştığını gösterdi (20 yaşında %30, 80 yaşında %84). MR bulgusu tek başına ağrının nedeni sayılmamalı."),
 ("2026", "Amerikan Ağrı Tıbbı Akademisi'nin kılavuzu, 6 haftadan kısa süren bel ağrısında ciddi bir hastalık belirtisi yoksa rutin erken görüntüleme yapılmamasını ve opioidlerin ilk tedavi olarak kullanılmamasını önerdi."),
]

BELF_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Bel fıtığı ve siyatik</h1>
    <p class="lede">Beldeki bir diskin taşarak bacağa giden sinir kökünü sıkıştırmasıyla ortaya çıkar. Ağrı kalçadan bacağa, bazen ayağa kadar vurur. İyi haber: çoğu kişi ameliyatsız iyileşir, fıtık çoğu zaman kendiliğinden küçülür.</p>
    <p class="meta">Son güncelleme: 29 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%95</b><span>Bel fıtıklarının L4–L5 ya da L5–S1 seviyesinde görülme oranı</span></div>
        <div class="stat"><b>%70</b><span>Dışarı taşmış fıtıklarda kendiliğinden gerileme</span></div>
        <div class="stat"><b>%95</b><span>Şiddetli siyatikte bir yıl sonra kendini iyileşmiş hisseden (bir çalışmada, ameliyatlı ve ameliyatsız)</span></div>
        <div class="stat"><b>%29</b><span>Hiç ağrısı olmayan 20 yaşındakilerin MR'ında disk fıtığı</span></div>
      </div>
      {g_toc([("nedir", "Nedir?"), ("sinirler", "Hangi sinir nereye vurur?"), ("tani", "MR ne zaman gerekir?"), ("tarihce", "Geçmişten bugüne"), ("tedavi", "Seyri ve tedavi"), ("egzersizler", "Egzersizler"), ("videolar", "Videolar"), ("sss", "Sık sorulan sorular"), ("uyari", "Acil uyarı işaretleri")])}
    </div>
  </section>

  <section id="nedir">
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

  <section id="sinirler">
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

  <section id="tani">
    <div class="wrap">
      <h2>Tanı: MR ne zaman gerekir?</h2>
      <p class="soft">Tanı önce muayeneyle konur. Sırtüstü yatarken düz bacağın kaldırılmasıyla bacak ağrısının tetiklenmesi (düz bacak kaldırma testi), kas gücü, refleksler ve duyu muayenesi en önemli ipuçlarıdır.</p>
      <div class="callout">
        <p>MR, ameliyat ya da enjeksiyon düşünülüyorsa ya da uyarı işaretleri varsa gereklidir. Ağrısı olmayan kişilerde de disk fıtığı sık görüldüğü için MR bulgusu mutlaka şikâyetler ve muayeneyle birlikte değerlendirilmelidir.</p>
      </div>
    </div>
  </section>

  <section id="tarihce">
    <div class="wrap">
      <p class="eyebrow">Geçmişten bugüne</p>
      <h2>Bel fıtığı ve siyatiğin kısa tarihi</h2>
      <p class="soft">Bacağa vuran siyatik ağrısı yüzyıllardır biliniyor, ama sık bir nedeninin bel fıtığı olduğu ancak 1934'te gösterildi. Sonraki çalışmalar, çoğu kişinin ameliyatsız da iyileştiğini ve uzun yatak istirahatinin gerekmediğini ortaya koydu.</p>
      {g_tl(BELF_TL)}
    </div>
  </section>

  <section id="tedavi">
    <div class="wrap">
      <h2>Seyri ve tedavi</h2>
      <p class="soft">Bel fıtığının doğal seyri çoğu zaman iyidir. Vücut taşan disk parçasını zamanla temizleyebilir; fıtık ne kadar dışarı taşmış ya da kopmuşsa kendiliğinden gerileme olasılığı o kadar yüksektir (bir derlemede kopmuş parçalarda %96, dışarı taşmış fıtıkta %70, daha hafif taşmada (protrüzyon) %41). 6–12 haftadır şiddetli siyatiği olan 283 hastanın karşılaştırıldığı çalışmada, ameliyatsız izlenen grubun %39'u sonunda ameliyat oldu; bir yılın sonunda iki grubun sonuçları benzerdi.</p>
      <ul class="tx">
        <li><b>Hareketli kalmak</b><span>Yatak istirahati önerilmez. Ağrıyı çok artıran pozisyonlardan kaçınarak kısa ve sık yürüyüşler yapın.</span></li>
        <li><b>Egzersiz</b><span>Ağrıyı bacaktan bele doğru çeken hareketler, sinir kaydırma egzersizleri ve zamanla bel-kalça kaslarını güçlendirme tedavinin temelidir.</span></li>
        <li><b>Manuel terapi</b><span>Manuel terapi, kılavuzlarda tek başına değil, yalnızca egzersizi içeren bir tedavi paketinin parçası olarak düşünülebilecek bir seçenektir.</span></li>
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

  <section id="sss">
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(FITIK_FAQ2)}
    </div>
  </section>

  <section id="uyari">
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

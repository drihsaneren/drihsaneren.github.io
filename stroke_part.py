# -*- coding: utf-8 -*-
# İnme (felç) sonrası rehabilitasyon sayfası. knee_part.py'den sonra exec edilir
# (fig, anim_d, anim_t, GRD, SV, EXT, ex_grid, faq, src_list, ext, vbox, CTA_CARD, NECK_CSS, YT_JS, page, cond, pick tanımlı).

STR_CHAIR = '<path class="obj" d="M22 78 H56 M24 78 V112 M54 78 V112 M22 78 V48"/>'

# Oturarak öne uzanma: gövde kalçadan öne eğilir, kol bardağa uzanır.
SV["reach"] = fig(GRD + STR_CHAIR +
    '<path class="obj" d="M70 68 H98 M90 68 V112"/>'
    '<path d="M74 55 H85 L83 68 H76 Z" fill="#C8963E"/>'
    '<path class="fig" d="M34 76 L62 76 L64 108"/>'
    f'<g>{anim_t("0 34 76;30 34 76;0 34 76", typ="rotate")}'
    '<path class="fig" d="M34 76 L37 44"/><circle class="hd" cx="39" cy="34" r="7"/>'
    f'<path class="fig hl" d="M37 50 L48 60 L60 57">{anim_d("M37 50 L48 60 L60 57;M37 50 L51 44 L65 40;M37 50 L48 60 L60 57")}</path></g>',
    "Oturarak öne uzanma")

# Masada havlu kaydırma: kol masada öne uzanır, havlu elle birlikte kayar.
SV["towel"] = fig(GRD + STR_CHAIR +
    '<path class="obj" d="M56 64 H114 M108 64 V112"/>'
    '<path class="fig" d="M34 76 L60 78 L62 108"/>'
    f'<g>{anim_t("0 34 76;8 34 76;0 34 76", typ="rotate")}'
    '<path class="fig" d="M34 76 L37 44"/><circle class="hd" cx="39" cy="34" r="7"/></g>'
    f'<g>{anim_t("0 0;22 0;0 0")}<rect x="60" y="57" width="20" height="6" rx="2" fill="#C8963E"/></g>'
    f'<path class="fig hl" d="M37 50 L52 60 L70 58">{anim_d("M37 50 L52 60 L70 58;M40 50 L66 56 L92 58;M37 50 L52 60 L70 58")}</path>',
    "Masada havlu kaydırma")

# Tezgâha tutunarak ağırlık aktarma (önden): gövde ve kalça sağa-sola kayar, eller ve ayaklar sabit.
WS_DUR, WS_KT = "4.8s", "0;0.25;0.5;0.75;1"
SV["wshift"] = fig(GRD +
    '<path class="obj" d="M22 70 H98"/>'
    f'<g>{anim_t("0 0;-8 0;0 0;8 0;0 0", dur=WS_DUR, kt=WS_KT)}'
    '<circle class="hd" cx="60" cy="20" r="8"/><path class="fig" d="M44 38 H76 M60 30 V38 M60 38 V78"/></g>'
    f'<path class="fig" d="M44 38 L40 70 M76 38 L80 70">{anim_d("M44 38 L40 70 M76 38 L80 70;M36 38 L40 70 M68 38 L80 70;M44 38 L40 70 M76 38 L80 70;M52 38 L40 70 M84 38 L80 70;M44 38 L40 70 M76 38 L80 70", dur=WS_DUR, kt=WS_KT)}</path>'
    f'<path class="fig hl" d="M60 78 L50 112 M60 78 L70 112">{anim_d("M60 78 L50 112 M60 78 L70 112;M52 78 L50 112 M52 78 L70 112;M60 78 L50 112 M60 78 L70 112;M68 78 L50 112 M68 78 L70 112;M60 78 L50 112 M60 78 L70 112", dur=WS_DUR, kt=WS_KT)}</path>'
    '<path d="M44 96 H30 M34 92 L30 96 L34 100 M76 96 H90 M86 92 L90 96 L86 100" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "Tezgâha tutunarak ağırlık aktarma")

# Tezgâha tutunarak topuk yükseltme (yandan): gövde yükselir, el tezgâhta sabit.
SV["heel"] = fig(GRD +
    '<path class="obj" d="M82 62 H110 M104 62 V112"/>'
    f'<g>{anim_t("0 0;0 -8;0 0")}'
    '<circle class="hd" cx="54" cy="20" r="7"/><path class="fig" d="M52 30 L52 72 L52 104"/></g>'
    f'<path class="fig" d="M52 40 L70 52 L86 62">{anim_d("M52 40 L70 52 L86 62;M52 32 L70 46 L86 62;M52 40 L70 52 L86 62")}</path>'
    f'<path class="fig hl" d="M52 104 L48 111 L64 112">{anim_d("M52 104 L48 111 L64 112;M52 96 L55 104 L64 112;M52 104 L48 111 L64 112")}</path>',
    "Tezgâha tutunarak topuk yükseltme")

SV["sts2"] = SV["sts"]
SV["bridge2"] = SV["bridge"]

EXT.update({
 "bridge2": ("Köprü", "Sırtüstü yatın, iki dizinizi bükün, ayak tabanlarınız yere bassın. Etkilenen diziniz yana düşüyorsa biri hafifçe desteklesin. Kalçanızı sıkarak yerden kaldırın, 3–5 saniye tutup yavaşça indirin. Yatakta kaymayı ve dönmeyi de kolaylaştırır.", "10 tekrar, günde 1–2 kez"),
 "reach": ("Oturarak öne uzanma", "Ayaklarınız yere tam basacak şekilde sağlam bir sandalyeye oturun. Önünüze, kol boyunuzdan biraz uzağa bir bardak ya da hafif bir nesne koyun. Gövdenizi kalçanızdan öne eğerek nesneye uzanın, dokunup geri dönün. Mesafeyi zamanla artırın, farklı yönlere uzanmayı da deneyin.", "10 tekrar, günde 2 kez"),
 "towel": ("Masada havlu kaydırma", "Masaya oturun, etkilenen kolunuzu masadaki bir havlunun üzerine koyun; gerekirse sağlam elinizle üstten destekleyin. Havluyu öne doğru kaydırarak kolunuzu uzatın, sonra geri çekin. Yanlara ve daire çizerek kaydırmayı da deneyin.", "10–15 tekrar, günde 2–3 kez"),
 "sts2": ("Sandalyeden kalkıp oturma", "Kollu, sağlam bir sandalyede kalçanızı öne kaydırın, ayaklarınızı biraz geriye alın; etkilenen ayağınız da yere tam bassın. Öne eğilip iki bacağınıza eşit yük vererek kalkın, sonra kontrollü şekilde oturun. Gerekirse ellerinizden destek alın.", "5–10 tekrar, günde 2 kez"),
 "wshift": ("Tezgâha tutunarak ağırlık aktarma", "Mutfak tezgâhı gibi sağlam bir yüzeye iki elinizle tutunun, ayaklarınız omuz genişliğinde açık olsun. Ağırlığınızı yavaşça bir bacağınıza, sonra diğerine aktarın. Etkilenen bacağınıza yük vermeye özellikle zaman ayırın.", "Her iki yana 10 tekrar"),
 "heel": ("Tezgâha tutunarak topuk yükseltme", "Tezgâha tutunarak dik durun. İki topuğunuzu birlikte kaldırıp parmak uçlarınızda yükselin, 2 saniye bekleyip yavaşça inin. Baldır kaslarını güçlendirir, yürürken ayağınızı yerden itmenize yardım eder.", "10 tekrar, günde 1–2 kez"),
})

INME_FAQ = [
 ("İnmeden sonra toparlanma ne kadar sürer?", "Toparlanma en hızlı ilk haftalarda ve ilk 3 ayda olur. Klasik bir çalışmada hastaların %95'i günlük yaşam becerilerindeki en iyi düzeylerine ilk 12,5 hafta içinde ulaştı. Ancak düzenli ve hedefe yönelik çalışmayla aylar, hatta yıllar sonra da gelişme sağlanabilir."),
 ("Aylar geçti, fizyoterapinin hâlâ faydası olur mu?", "Evet. İnmenin üzerinden ortalama 18 ay geçmiş 224 kişinin katıldığı yoğun bir kol rehabilitasyonu programında klinik olarak anlamlı gelişme görüldü ve kazanımlar sonraki 6 ayda da sürdü. Hedefe yönelik, bol tekrarlı çalışma her dönemde değerlidir."),
 ("Rehabilitasyona ne zaman başlanmalı?", "Hekiminizin onayıyla, akut dönemde, yani hastanedeyken başlanmalıdır. Ancak ilk 24 saatte başlatılan yoğun ve sık mobilizasyon ek fayda sağlamadı; zamanlama ve yoğunluk kişiye göre ayarlanır."),
 ("Etkilenen omuzdaki ağrıyı nasıl önleyebilirim?", "Kişiyi etkilenen kolundan çekerek kaldırmayın; oturur ve yatarken kolu bir yastık ya da masa üzerinde destekleyin. Baş üstü makara ile yapılan egzersizler omza zarar verebileceği için önerilmez. Ağrı başladıysa fizyoterapistiniz pozisyonlama, egzersiz ve gerekirse ek tedavileri planlar."),
 ("Evde rehabilitasyon hastanedeki kadar etkili mi?", "Uygun hastalarda evet. Erken taburcu edilip evde ekip desteğiyle rehabilitasyona devam eden hastalarda ölüm ya da bağımlı kalma riski azaldı ve hastanede kalış yaklaşık 6 gün kısaldı. Ev ortamında çalışmak, egzersizleri gerçek günlük işlere uyarlamayı da kolaylaştırır."),
 ("Yeniden inme geçirme riskimi nasıl azaltabilirim?", "Tansiyonunuzu kontrol altında tutmak, ilaçlarınızı düzenli kullanmak, sigarayı bırakmak, düzenli hareket etmek ve sağlıklı beslenmek en etkili adımlardır. Dünyadaki inme yükünün %84'ü değiştirilebilir risk etkenlerine bağlıdır."),
]

INME_SRC = [
 "AVERT Trial Collaboration group. " + ext("https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(15)60690-0/fulltext", "Efficacy and safety of very early mobilisation within 24 h of stroke onset (AVERT): a randomised controlled trial") + ". Lancet. 2015;386(9988):46-55.",
 "Feigin VL, Brainin M, Norrving B, et al. " + ext("https://journals.sagepub.com/doi/10.1177/17474930241308142", "World Stroke Organization: Global Stroke Fact Sheet 2025") + ". Int J Stroke. 2025;20(2):132-144.",
 "French B, Thomas LH, Coupe J, et al. " + ext("https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD006073.pub3/full", "Repetitive task training for improving functional ability after stroke") + ". Cochrane Database Syst Rev. 2016;11:CD006073.",
 "Hackett ML, Pickles K. Part I: frequency of depression after stroke: an updated systematic review and meta-analysis of observational studies. Int J Stroke. 2014;9(8):1017-1025.",
 "Jørgensen HS, Nakayama H, Raaschou HO, et al. Outcome and time course of recovery in stroke. Part II: Time course of recovery. The Copenhagen Stroke Study. Arch Phys Med Rehabil. 1995;76(5):406-412.",
 "Langhorne P, Baylan S; Early Supported Discharge Trialists. " + ext("https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD000443.pub4/abstract", "Early supported discharge services for people with acute stroke") + ". Cochrane Database Syst Rev. 2017;7:CD000443.",
 "National Institute for Health and Care Excellence. " + ext("https://www.nice.org.uk/guidance/ng236", "Stroke rehabilitation in adults (NG236)") + ". Londra: NICE; 2023.",
 "NHS. " + ext("https://www.nhs.uk/conditions/stroke/symptoms/", "Stroke: symptoms") + ".",
 "Richards LG, et al. " + ext("https://www.ahajournals.org/doi/10.1161/STR.0000000000000536", "2026 Guideline for Adult Stroke Rehabilitation and Recovery: a guideline from the American Heart Association/American Stroke Association") + ". Stroke. 2026.",
 "Saunders DH, Sanderson M, Hayes S, et al. " + ext("https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD003316.pub7/full", "Physical fitness training for stroke patients") + ". Cochrane Database Syst Rev. 2020;3:CD003316.",
 "Saver JL. Time is brain—quantified. Stroke. 2006;37(1):263-266.",
 "Thieme H, Morkisch N, Mehrholz J, et al. " + ext("https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD008449.pub3/full", "Mirror therapy for improving motor function after stroke") + ". Cochrane Database Syst Rev. 2018;7:CD008449.",
 "Yang A, Wu HM, Tang JL, Xu L, Yang M, Liu GJ. " + ext("https://www.cochrane.org/CD004131/STROKE_acupuncture-stroke-rehabilitation", "Acupuncture for stroke rehabilitation") + ". Cochrane Database Syst Rev. 2016;(8):CD004131.",
 "Ward NS, Brander F, Kelly K. " + ext("https://discovery.ucl.ac.uk/10069316/", "Intensive upper limb neurorehabilitation in chronic stroke: outcomes from the Queen Square programme") + ". J Neurol Neurosurg Psychiatry. 2019;90(5):498-506.",
]

INME_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>İnme (felç) sonrası rehabilitasyon</h1>
    <p class="lede">İnme, beyne giden kan akışının aniden bozulmasıyla ortaya çıkar ve hareket, konuşma ya da günlük işlerde güçlüğe yol açabilir. Beyin kaybedilen işlevleri yeniden öğrenebilir; erken başlayan, düzenli ve bol tekrarlı rehabilitasyon bu toparlanmanın itici gücüdür.</p>
    <p class="meta">Son güncelleme: {UPDATED}</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>12 milyon</b><span>Dünyada her yıl yeni inme geçiren kişi (2021)</span></div>
        <div class="stat"><b>4'te 1</b><span>25 yaş üstünde hayatı boyunca inme geçirecek kişi oranı</span></div>
        <div class="stat"><b>%84</b><span>İnme yükünün değiştirilebilir risk etkenlerine bağlı kısmı</span></div>
        <div class="stat"><b>3 saat</b><span>İngiltere kılavuzunun önerdiği günlük rehabilitasyon süresi, haftada 5 gün</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Beyindeki bir damarın pıhtıyla tıkanması (iskemik inme) ya da yırtılıp kanaması (beyin kanaması) sonucu beyin dokusu hasar görür. Etkilenen bölgeye göre vücudun bir yarısında güçsüzlük, konuşma ve yutma güçlüğü, görme ve denge sorunları, dikkat ve bellek güçlükleri ortaya çıkabilir.</p>
        <p class="soft">İnme dünyada ölüm nedenleri arasında ikinci, ölüm ve engelliliğin birlikte değerlendirildiği sıralamada üçüncü sıradadır. Dünyada inme geçirmiş yaklaşık 94 milyon kişi yaşıyor.</p>
      </div>
      <div>
        <h2>İnme sonrası sık görülen sorunlar</h2>
        <ul class="dots">
          <li>Vücudun bir yarısında güçsüzlük ve kas sertliği (spastisite)</li>
          <li>Denge kaybı, yürüme güçlüğü ve düşme riski</li>
          <li>Kol ve elde beceri kaybı, etkilenen omuzda ağrı</li>
          <li>Konuşma, yutma, dikkat ve bellek güçlükleri</li>
          <li>Yorgunluk; yaklaşık her üç kişiden birinde depresyon</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Beyin nasıl toparlanır?</h2>
      <p class="soft">Beyin, hasar gören bölgenin görevlerini çevre bölgelere ve yeni bağlantılara devredebilir. Buna nöroplastisite denir; anlamlı görevlerle ve bol tekrarla çalıştıkça güçlenir. Toparlanma en hızlı ilk haftalarda ve aylarda olur: klasik bir Danimarka çalışmasında hastaların %95'i günlük yaşam becerilerindeki en iyi düzeylerine ilk 12,5 hafta içinde ulaştı.</p>
      <div class="callout">
        <p>Ama kapı kapanmaz. İnmenin üzerinden ortalama 18 ay geçmiş 224 kişinin katıldığı yoğun bir kol rehabilitasyonu programında kol işlevinde klinik olarak anlamlı gelişme görüldü ve kazanımlar sonraki 6 ayda da artmaya devam etti.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Rehabilitasyon: ne zaman, ne kadar, nerede?</h2>
      <p class="soft">İnme rehabilitasyonu bir ekip işidir: fizyoterapi, ergoterapi, konuşma ve yutma terapisi, hekim ve hemşire bakımı birlikte yürür. Hasta ve ailesi de bu ekibin parçasıdır.</p>
      <ul class="tx">
        <li><b>Erken başlamak</b><span>Rehabilitasyon akut dönemde, hastanedeyken başlamalıdır. Ancak 2.000'den fazla hastanın katıldığı bir çalışmada ilk 24 saatte başlatılan yoğun ve sık mobilizasyon iyi sonuç oranını artırmadı, biraz azalttı (%46'ya karşı %50). Zamanlamaya hekim karar verir.</span></li>
        <li><b>Yoğunluk ve tekrar</b><span>İngiltere kılavuzu (NICE, 2023) uygun kişiler için fizyoterapi, ergoterapi ve konuşma terapisinin toplamda günde en az 3 saat, haftada en az 5 gün yapılmasını öneriyor. Seanslar arasında evde yapılan tekrarlar da bu sürenin önemli bir parçasıdır.</span></li>
        <li><b>Evde rehabilitasyon</b><span>Uygun hastalarda erken taburculuk ve evde ekip desteğiyle sürdürülen rehabilitasyon, ölüm ya da bağımlı kalma riskini azalttı ve hastanede kalışı yaklaşık 6 gün kısalttı.</span></li>
        <li><b>Görev odaklı çalışma</b><span>Kalkma, uzanma, yürüme gibi gerçek günlük görevlerin bol tekrarla çalışılması kol ve bacak işlevini geliştiriyor; kazanımlar 6 aya kadar sürüyor.</span></li>
        <li><b>Yürüme, denge ve kondisyon</b><span>Yürüyüş içeren kondisyon egzersizleri ve kuvvetle birleştirilmiş programlar yürüme hızını ve dengeyi geliştiriyor, günlük yaşamdaki kısıtlılığı azaltıyor.</span></li>
        <li><b>Kol ve el</b><span>Ayna terapisi, etkilenen kol ve bacağın hareketini ve günlük işlerin yapılabilmesini orta düzeyde geliştiriyor. Etkilenen eli gün içinde küçük işlere katmak da bu çalışmanın bir parçasıdır.</span></li>
        <li><b>Omuz ve kas sertliği</b><span>Etkilenen kolu desteklemek, doğru pozisyonlamak ve düzenli germe temeldir. Kas sertliğinde gerektiğinde botulinum toksini fizyoterapiyle birlikte uygulanabilir. Baş üstü makara egzersizleri omza zarar verebileceği için önerilmez.</span></li>
        <li><b>Duygu durumu</b><span>İnme geçirenlerin yaklaşık %31'inde depresyon görülür. Depresyon ve kaygının taranıp tedavi edilmesi, toparlanmanın ayrılmaz bir parçasıdır. <a href="stres.html">Nefes egzersizlerine göz atın →</a></span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>İnme sonrası altı temel egzersiz</h2>
      <p class="soft">Bu hareketler inme sonrası evde sık kullanılan temel egzersizlerden seçildi. Hangilerinin ve hangi düzeyde size uygun olduğunu fizyoterapistinizle belirleyin. Ayakta yapılan hareketlerde mutlaka sağlam bir destek olsun ve mümkünse yanınızda biri bulunsun. Göğüs ağrısı, nefes darlığı, baş dönmesi ya da yeni bir güçsüzlük olursa durun.</p>
      {ex_grid(["bridge2", "reach", "towel", "sts2", "wshift", "heel"])}
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Evde güvenli ve bağımsız yaşam için</h2>
        <p class="soft">Doğru destek, kişinin yapabileceği işi onun yerine yapmak değil, güvenle yapmasına yardım etmektir. Aile ve bakım verenler de sürecin bir parçasıdır.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Etkilenen koldan tutarak çekmeyin, kaldırmayın; oturur ve yatarken kolu bir yastık ya da masa üzerinde destekleyin.</li>
        <li>Etkilenen eli gün içinde küçük işlere katın: bardak tutmak, masayı silmek, düğme iliklemek.</li>
        <li>Kaygan halıları kaldırın; banyoya tutunma barı ve kaydırmaz paspas, koridora gece lambası koyun.</li>
        <li>Yorgunluk sık görülür: işleri güne yayın, kısa dinlenme araları verin.</li>
        <li>Tansiyon, şeker ve kolesterol ilaçlarınızı düzenli kullanın, sigarayı bırakın.</li>
      </ul>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>İnme sonrası egzersiz videoları</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz. Egzersizleri fizyoterapistinizin önerdiği düzeyde yapın.</p>
      <div class="vids">
        <div class="vid">
          {vbox("1COGgvNjdj0", "Yürüme ve denge egzersizleri videosunu oynat", "After Stroke/CVA; Walking &amp; Balance Exercises at Home")}
          <h3>Evde yürüme ve denge egzersizleri</h3>
          <p>İnme sonrası yürümeyi ve dengeyi geliştirmeye yönelik ev egzersizleri.</p>
        </div>
        <div class="vid">
          {vbox("DoR9H9zuJPY", "Kol ve el egzersizleri videosunu oynat", "Stroke Exercises for Arm &amp; Hand with Little to No Strength-for Home")}
          <h3>Güçsüz kol ve el için egzersizler</h3>
          <p>Kolda ve elde çok az hareket olan dönemde evde yapılabilecek egzersizler.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Akupunktur: araştırmalar ve klinik gözlemim</h2>
      <p class="soft">31 çalışmayı (2.257 kişi) inceleyen Cochrane derlemesine göre akupunktur, inme sonrasında günlük yaşamda bağımsızlık, hareket, yutma ve ağrı gibi alanlarda yararlı olabilir; ciddi bir yan etki bildirilmedi. Ancak kanıtın kalitesi düşük ya da çok düşük olduğu için yazarlar, rutin kullanımı konusunda kesin bir sonuca varılamadığını belirtiyor.</p>
      {OBS("Kendi klinik gözlemimde, inme sonrası felçlerde ve diğer nörolojik sorunlarda akupunkturun çok etkili olduğunu gördüm.")}
      <div class="callout">
        <p>{ACU_LAW}</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(INME_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">İlk dört belirti yeni bir inmeyi gösterebilir: belirtiler geçse bile beklemeden <strong>112</strong>'yi arayın. Tedavi edilmeyen bir inmede her dakika yaklaşık 1,9 milyon sinir hücresi kaybedilir. Diğer durumlarda da gecikmeden hekime başvurun.</p>
      <ul class="dots redflags">
        <li>Yüzün bir tarafında kayma, gülümseyince ağız kenarının düşmesi</li>
        <li>Bir kolda ya da bacakta ani güçsüzlük ya da uyuşma</li>
        <li>Konuşmada ani bozulma, söyleneni anlayamama</li>
        <li>Ani denge kaybı, bir ya da iki gözde ani görme kaybı, ani ve çok şiddetli baş ağrısı</li>
        <li>Baldırda şişlik, ağrı ve kızarıklık; ani nefes darlığı ya da göğüs ağrısı (<strong>112</strong>)</li>
        <li>Yemek yerken sık öksürme ya da boğulma hissi, ateş (yutma sorunu ya da akciğer enfeksiyonu olabilir)</li>
        <li>Düşme sonrası başın çarpması, ağrı ya da bacağa yük verememe</li>
      </ul>
      {CTA_CARD("İnme sonrası rehabilitasyon süreciniz", "inme sonrası rehabilitasyon")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(INME_SRC)}
    </div>
  </section>
</main>'''

page("inme-rehabilitasyonu.html", "İnme Sonrası Rehabilitasyon",
     "İnme (felç) sonrası toparlanma nasıl olur, rehabilitasyona ne zaman başlanmalı, evde fizyoterapi işe yarar mı? Evde altı egzersiz, omuz koruma, güvenli ev önerileri, videolar ve yeni inme belirtileri.",
     "inme-rehabilitasyonu.html", NECK_CSS, INME_BODY, YT_JS,
     seo_title="İnme (Felç) Sonrası Rehabilitasyon: Egzersizler ve Evde Fizyoterapi | İhsan Eren",
     condition="İnme sonrası rehabilitasyon", about=cond("İnme sonrası rehabilitasyon", "stroke-rehabilitation"),
     faq_items=pick(INME_FAQ, 0, 1, 2, 4))

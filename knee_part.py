# -*- coding: utf-8 -*-
# Diz kireçlenmesi sayfası. neck_part.py ve lowback_part.py'den sonra exec edilir.

CHAIR = '<path class="obj" d="M36 78 H70 M38 78 V112 M68 78 V112 M36 78 V50"/>'

SV["kext"] = fig(GRD + CHAIR +
    '<path class="fig" d="M48 76 L50 44 M48 76 L76 76 M50 50 L44 66 L40 76"/>'
    '<path class="fig" d="M50 44 L52 36"/><circle class="hd" cx="53" cy="28" r="7"/><path d="M59 26 L64 29 L59 31 Z" fill="#2A6F6B"/>'
    f'<path class="fig hl" d="M76 76 L78 108">{anim_d("M76 76 L78 108;M76 76 L106 74;M76 76 L78 108")}</path>',
    "Oturarak diz düzeltme")

SV["quad"] = fig(GRD +
    '<circle class="hd" cx="12" cy="100" r="7"/>'
    '<path class="fig" d="M20 105 H58 M24 104 L42 108"/>'
    '<circle cx="84" cy="106" r="5" fill="#8FA8A2"/>'
    f'<path class="fig hl" d="M58 104 L84 99 L110 104">{anim_d("M58 104 L84 99 L110 104;M58 104 L84 101 L110 98;M58 104 L84 99 L110 104")}</path>'
    '<g><animate attributeName="opacity" values="0;1;0" dur="3.2s" repeatCount="indefinite"/>'
    '<path d="M84 80 V90 M80 86 L84 90 L88 86" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>',
    "Havluya bastırma")

SV["slr"] = fig(GRD +
    '<circle class="hd" cx="12" cy="100" r="7"/>'
    '<path class="fig" d="M20 105 H58 M58 105 L74 86 L88 108 M24 104 L42 108"/>'
    f'<path class="fig hl" d="M58 105 L110 105">{anim_d("M58 105 L110 105;M58 105 L104 80;M58 105 L110 105")}</path>',
    "Düz bacak kaldırma")

STS_DUR = "3.6s"
SV["sts"] = fig(GRD +
    '<path class="obj" d="M30 78 H62 M32 78 V112 M60 78 V112 M30 78 V48"/>'
    f'<path class="fig hl" d="M50 44 L46 76 L74 76 L76 108">{anim_d("M50 44 L46 76 L74 76 L76 108;M72 34 L73 66 L76 88 L76 108;M50 44 L46 76 L74 76 L76 108", dur=STS_DUR)}</path>'
    f'<path class="fig" d="M50 50 L60 56">{anim_d("M50 50 L60 56;M72 40 L82 46;M50 50 L60 56", dur=STS_DUR)}</path>'
    f'<g>{anim_t("0 0;21 -10;0 0", dur=STS_DUR)}<circle class="hd" cx="52" cy="34" r="7"/></g>',
    "Sandalyeden kalkıp oturma")

SV["abd"] = fig(GRD +
    '<circle class="hd" cx="14" cy="96" r="7"/>'
    '<path class="fig" d="M22 101 L62 104 M62 105 L110 107 M28 98 L48 100"/>'
    f'<path class="fig hl" d="M62 102 L110 104">{anim_d("M62 102 L110 104;M62 102 L106 80;M62 102 L110 104")}</path>',
    "Yan yatarak bacak kaldırma")

SV["wall"] = fig(GRD +
    '<path class="obj" d="M30 10 V112" stroke-width="5"/>'
    f'<path class="fig hl" d="M38 34 L38 66 L44 88 L42 108">{anim_d("M38 34 L38 66 L44 88 L42 108;M38 46 L38 78 L60 84 L48 108;M38 34 L38 66 L44 88 L42 108")}</path>'
    f'<g>{anim_t("0 0;0 12;0 0")}<circle class="hd" cx="40" cy="24" r="7"/><path class="fig" d="M38 40 L50 56"/></g>',
    "Duvarda yarım çömelme")

EXT.update({
 "kext": ("Oturarak diz düzeltme", "Sandalyeye dik oturun. Bir dizinizi yavaşça düzeltip bacağınızı yere paralel olacak şekilde kaldırın, uyluğunuzun ön kasını sıkın. 5 saniye tutup yavaşça indirin.", "Her bacakla 10 tekrar, günde 2 kez"),
 "quad": ("Havluya bastırma", "Sırtüstü ya da oturarak bacağınızı uzatın, dizinizin altına rulo yapılmış bir havlu koyun. Dizinizin arkasıyla havluyu yere doğru bastırın; uyluğunuzun ön kası sıkılacak, topuğunuz hafifçe kalkacak. 5 saniye tutun.", "10 tekrar, günde 2–3 kez"),
 "slr": ("Düz bacak kaldırma", "Sırtüstü yatın, bir dizinizi bükün. Diğer bacağınızı dizi düz kalacak şekilde, uyluğunuzu sıkarak diğer dizinizin hizasına kadar kaldırın. Yavaşça indirin.", "Her bacakla 10 tekrar"),
 "sts": ("Sandalyeden kalkıp oturma", "Kollarınızı göğsünüzde çaprazlayın. Hafifçe öne eğilerek sandalyeden kalkın, sonra kontrollü şekilde oturun. Zorlanıyorsanız ellerinizden destek alın ya da daha yüksek bir sandalye kullanın.", "10 tekrar, günde 1–2 kez"),
 "abd": ("Yan yatarak bacak kaldırma", "Yan yatın, alttaki dizinizi hafifçe bükün. Üstteki bacağınızı dizi düz, ayak ucu öne bakacak şekilde yukarı kaldırın. Kalça kasları dizi dengede tutmaya yardım eder.", "Her iki yana 10–15 tekrar"),
 "wall": ("Duvarda yarım çömelme", "Sırtınızı duvara yaslayın, ayaklarınızı duvardan yarım adım öne alın. Sırtınız duvarda kayarak dizlerinizi hafifçe bükün, ağrısız olan derinliğe kadar inin, sonra doğrulun. Dizleriniz ayak parmaklarınızı geçmesin.", "10 tekrar"),
})

KNEE_SVC = "Evde değerlendirme ve kişiye özel egzersiz programı"
KNEE_FAQ = [
 ("Kireçlenmiş dizimi dinlendirmeli miyim?", "Uzun süreli dinlenme önerilmez. Eklem kıkırdağı hareketle beslenir; düzenli yürüyüş ve güçlendirme egzersizleri ağrıyı azaltır ve dizi korur. Ağrının çok arttığı günlerde yükü azaltın ama tamamen durmayın."),
 ("Merdiveni nasıl inip çıkmalıyım?", "Tırabzana tutunun. Çıkarken önce sağlam bacağınızla, inerken önce ağrılı bacağınızla adım atın. Baston kullanıyorsanız bastonu ağrılı bacakla birlikte hareket ettirin."),
 ("Baston hangi elde tutulur?", "Ağrılı dizin karşı tarafındaki elde. Baston ağrılı bacakla aynı anda yere basar ve dizin taşıdığı yükü azaltır."),
 ("Glukozamin, kolajen ya da diz iğnesi işe yarar mı?", "İngiltere'nin kireçlenme kılavuzu (NICE) glukozamin takviyelerini ve eklem içine hyaluronik asit iğnesini önermiyor. Eklem içine kortizon iğnesi ise diğer tedaviler yetmediğinde 2–10 haftalık kısa süreli rahatlama için düşünülebilir."),
 ("Diz protezi ne zaman gerekir?", "Egzersiz, kilo kontrolü ve ilaç tedavisine rağmen ağrı ve kısıtlılık günlük yaşamı ciddi şekilde bozuyorsa ortopedi değerlendirmesi gerekir. Karar röntgendeki görüntüye göre değil, yaşam kalitenize göre verilir. Ameliyattan önce ve sonra yapılan egzersizler iyileşmeyi hızlandırır."),
]
KNEE_SRC = [
 "Bedson J, Croft PR. " + ext("https://link.springer.com/article/10.1186/1471-2474-9-116", "The discordance between clinical and radiographic knee osteoarthritis: a systematic search and summary of the literature") + ". BMC Musculoskelet Disord. 2008;9:116.",
 "Fransen M, McConnell S, Harmer AR, Van der Esch M, Simic M, Bennell KL. " + ext("https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD004376.pub3/full", "Exercise for osteoarthritis of the knee") + ". Cochrane Database Syst Rev. 2015;1:CD004376.",
 "GBD 2021 Osteoarthritis Collaborators. " + ext("https://www.thelancet.com/journals/lanrhe/article/PIIS2665-9913(23)00163-7/fulltext", "Global, regional, and national burden of osteoarthritis, 1990–2020 and projections to 2050") + ". Lancet Rheumatol. 2023;5(9):e508-e522.",
 "Messier SP, Gutekunst DJ, Davis C, DeVita P. Weight loss reduces knee-joint loads in overweight and obese older adults with knee osteoarthritis. Arthritis Rheum. 2005;52(7):2026-2032.",
 "National Institute for Health and Care Excellence. " + ext("https://www.nice.org.uk/guidance/ng226", "Osteoarthritis in over 16s: diagnosis and management (NG226)") + ". Londra: NICE; 2022.",
 "Physiopedia. " + ext("https://www.physio-pedia.com/Knee_Osteoarthritis", "Knee Osteoarthritis") + ".",
]

KNEE_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Diz kireçlenmesi (osteoartrit)</h1>
    <p class="lede">Özellikle 45 yaşından sonra sık görülen, merdivende, çömelirken ve uzun yürüyüşlerde kendini gösteren bir diz sorunu. Kireçlenme "bitti, yapacak bir şey yok" demek değildir: doğru egzersiz ve kilo kontrolüyle ağrı belirgin şekilde azalabilir.</p>
    <p class="meta">Son güncelleme: {UPDATED}</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>595 milyon</b><span>Dünyada kireçlenmesi olan kişi (2020); nüfusun %7,6'sı</span></div>
        <div class="stat"><b>%75</b><span>Diz kireçlenmesinde 2050'ye kadar beklenen artış</span></div>
        <div class="stat"><b>1 kg → 4 kg</b><span>Verilen her kilo, her adımda dize binen yükü yaklaşık dört katı kadar azaltır</span></div>
        <div class="stat"><b>12 puan</b><span>Egzersizle ağrıdaki ortalama azalma (100 üzerinden)</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Eklem yüzeylerini kaplayan kıkırdağın incelmesiyle başlayan, ama yalnızca kıkırdağı değil kemiği, eklem zarını, bağları ve çevredeki kasları da etkileyen bir süreçtir. Eklem kenarlarında kemik çıkıntıları oluşabilir, eklem zaman zaman şişebilir.</p>
        <p class="soft">45 yaş üstünde, hareketle artan diz ağrısı ve 30 dakikadan kısa süren sabah tutukluğu varsa tanı çoğu zaman muayeneyle konur; kılavuzlar rutin görüntüleme önermez.</p>
      </div>
      <div>
        <h2>Belirtiler ve risk etkenleri</h2>
        <ul class="dots">
          <li>Merdiven inip çıkarken, çömelirken, uzun yürüyünce artan ağrı</li>
          <li>Sabah ya da uzun oturduktan sonra kısa süren tutukluk</li>
          <li>Dizde çıtırtı, zaman zaman şişlik, hareket kısıtlılığı</li>
          <li>Risk etkenleri: ileri yaş, kadın olmak, fazla kilo, önceki diz yaralanmaları, ağır diz zorlaması gerektiren işler, O ya da X bacak</li>
        </ul>
        <p class="soft">Yüksek vücut ağırlığı, kireçlenmeye bağlı iş göremezliğin yaklaşık %20'sinden sorumlu.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Röntgen ile ağrı her zaman örtüşmez</h2>
      <p class="soft">"Röntgenim çok kötüymüş" cümlesi çoğu zaman gereksiz bir korku yaratır. Çalışmaların derlendiği bir incelemede diz ağrısı olanların yalnızca %15–76'sında röntgende kireçlenme görüldü; röntgende kireçlenmesi olanların ise %15–81'inde ağrı vardı.</p>
      <div class="callout">
        <p>Yani röntgendeki görüntü ağrınızın şiddetini ya da ne yapabileceğinizi belirlemez. Asıl belirleyici olan kas gücü, hareketlilik, kilo ve günlük aktivitedir. Bunların hepsi değiştirilebilir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <p class="soft">Kılavuzlar tedavinin merkezine üç şeyi koyar: egzersiz, kilo kontrolü ve hastalığı doğru anlamak.</p>
      <ul class="tx">
        <li><b>Egzersiz</b><span>Tedavinin temelidir. Egzersiz ağrıyı 100 üzerinden ortalama 12 puan azaltıyor ve günlük işleri kolaylaştırıyor. Programda uyluk ve kalça kaslarını güçlendiren hareketler yer alır; kişiye göre ayarlanmış ve mümkünse bir uzman eşliğinde başlanmış bir program önerilir.</span></li>
        <li><b>Kilo kontrolü</b><span>Fazla kilolu kişilerde her kilo kaybı faydalıdır; vücut ağırlığının %10'unu vermek %5'inden daha etkilidir. Verilen her kilo, her adımda dize binen yükü yaklaşık dört katı kadar azaltır.</span></li>
        <li><b>Yürümeye yardımcılar</b><span>Baston ya da yürüteç, ağrılı dönemlerde hareketliliği ve bağımsızlığı korur. Baston ağrısız taraftaki elde tutulur.</span></li>
        <li><b>İlaçlar</b><span>Dize sürülen ağrı kesici jeller ilk seçenektir. Ağızdan ağrı kesiciler hekiminizin önerisiyle en düşük dozda ve kısa süreli kullanılmalıdır.</span></li>
        <li><b>Eklem içi kortizon</b><span>Diğer tedaviler yetmediğinde 2–10 haftalık kısa süreli rahatlama sağlayabilir; hekim kararıyla uygulanır.</span></li>
        <li><b>Protez ameliyatı</b><span>Ameliyatsız tedaviye rağmen ağrı ve kısıtlılık yaşam kalitesini ciddi şekilde bozuyorsa düşünülür.</span></li>
      </ul>
      <div class="callout">
        <p><strong>Kılavuzlarda önerilmeyenler:</strong> Glukozamin takviyeleri, eklem içine hyaluronik asit iğnesi ve dizin artroskopik olarak "yıkanması / temizlenmesi" (kilitlenme gibi özel durumlar dışında).</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Diz için altı temel egzersiz</h2>
      <p class="soft">Egzersiz sırasında hafif bir ağrı olabilir; ağrı ertesi gün artmıyorsa devam etmek güvenlidir. Ertesi gün belirgin artış ya da şişlik olursa tekrar sayısını azaltın. İlk üçü yatarak ya da oturarak yapıldığı için ağrılı dönemlerde de uygundur.</p>
      {ex_grid(["kext", "quad", "slr", "sts", "abd", "wall"])}
      <div class="callout"><p><b>Sürdürmek zor mu geliyor?</b> Bu hareketleri altı haftalık, sesli sayan ve her seansta kilitli bir sır açan etkileşimli bir programa dönüştürdük: <a href="dizin-12-sirri.html">Dizin 12 Sırrı</a>.</p></div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Günlük hayatta dizleriniz için</h2>
        <p class="soft">Dizi korumak, onu hareketsiz bırakmak değil, yükünü akıllıca dağıtmaktır.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Haftanın çoğu günü yürüyün; ağrı artıyorsa süreyi kısaltıp sıklığı artırın.</li>
        <li>Bisiklet ve suda egzersiz, dize daha az yük bindiren iyi seçeneklerdir.</li>
        <li>Yumuşak tabanlı, rahat ayakkabılar tercih edin.</li>
        <li>Uzun süre çömelmek ve yere oturup kalkmak ağrıyı artırıyorsa alçak tabure ya da sandalye kullanın.</li>
        <li>Uzun oturduktan sonra kalkmadan önce dizlerinizi birkaç kez bükün, düzeltin.</li>
      </ul>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Diz kireçlenmesi için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("3bXcNWx-WAk", "Diz kireçlenmesi egzersizleri videosunu oynat", "Knee Arthritis? We Put Together Our 7 Best Exercises")}
          <h3>Diz kireçlenmesi için yedi egzersiz</h3>
          <p>Kireçlenmiş diz için güçlendirme ve hareket egzersizlerinden oluşan bir program.</p>
        </div>
        <div class="vid">
          {vbox("iL-swm4th_o", "Ameliyatsız tedavi videosunu oynat", "Treating Knee Arthritis Without Surgery")}
          <h3>Diz kireçlenmesinde ameliyatsız tedavi</h3>
          <p>Ameliyat öncesinde denenebilecek yöntemler ve günlük hayat önerileri.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(KNEE_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlar kireçlenme dışında bir soruna işaret edebilir. Beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Dizde ani şişlik, kızarıklık, sıcaklık ve ateş (eklem iltihabı olabilir)</li>
        <li>Düşme ya da burkulma sonrası bacağa yük verememe</li>
        <li>Dizin kilitlenmesi, bükülüp düzelmemesi</li>
        <li>Baldırda şişlik, ağrı ve kızarıklık (damar tıkanıklığı olabilir)</li>
        <li>Dinlenmekle geçmeyen gece ağrısı ya da nedensiz kilo kaybı</li>
      </ul>
      {CTA_CARD("Diz ağrınız ve kireçlenmeniz", "diz kireçlenmesi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(KNEE_SRC)}
    </div>
  </section>
</main>'''

page("diz-kireclenmesi.html", "Diz Kireçlenmesi",
     "Diz kireçlenmesi (osteoartrit) nedir, röntgen ne anlatır, egzersiz ve kilo kontrolü neden önemli? Evde yapılabilecek altı egzersiz, günlük hayat önerileri, videolar ve uyarı işaretleri.",
     "diz-kireclenmesi.html", NECK_CSS, KNEE_BODY, YT_JS,
     seo_title="Diz Kireçlenmesi: Belirtiler, Egzersizler ve Tedavi | İhsan Eren", condition="Diz kireçlenmesi (osteoartrit)", about=cond("Diz kireçlenmesi (osteoartrit)", "knee-osteoarthritis"),
     faq_items=pick(KNEE_FAQ, 0, 3, 4, 2))

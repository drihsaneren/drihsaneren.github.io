# -*- coding: utf-8 -*-
# Yeni hastalık rehberleri (3): rotator manşet yırtığı, çene eklemi, idrar kaçırma, gebelikte bel ağrısı.
# cond3_part.py'den sonra exec edilir.

# ---- yeni çizimler -----------------------------------------------------------------
def _pf_ring(cx, cy):
    """Pelvik taban: kasılıp gevşeyen altın halka ve yukarı ok."""
    return (f'<circle cx="{cx}" cy="{cy}" r="10" fill="none" stroke="#C8963E" stroke-width="2.5" stroke-dasharray="3 3">'
            '<animate attributeName="r" values="10;6;6;10" keyTimes="0;0.3;0.7;1" dur="4s" repeatCount="indefinite"/></circle>'
            f'<path d="M{cx} {cy + 4} V{cy - 5} M{cx - 3} {cy - 2} L{cx} {cy - 5} L{cx + 3} {cy - 2}" stroke="#C8963E" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">'
            '<animate attributeName="opacity" values="0.15;1;1;0.15" keyTimes="0;0.3;0.7;1" dur="4s" repeatCount="indefinite"/></path>')

SV["pf_lie"] = fig(GRD +
    '<circle class="hd" cx="16" cy="102" r="7"/><path class="fig" d="M24 104 H58 L74 84 L90 108 M30 104 L46 108"/>'
    + _pf_ring(60, 96), "Yatarak pelvik taban kasılması")

CHAIR_L = '<path class="obj" d="M36 78 H70 M38 78 V112 M68 78 V112 M36 78 V50"/>'
SV["pf_sit"] = fig(GRD + CHAIR_L +
    '<path class="fig" d="M46 74 H80 V112 M46 74 L48 42 M48 48 L60 62 L72 66"/>'
    '<circle class="hd" cx="50" cy="33" r="8"/><path d="M57 31 L62 34 L57 36 Z" fill="#2A6F6B"/>'
    + _pf_ring(52, 72), "Oturarak pelvik taban kasılması")

SV["pf_stand"] = fig(GRD +
    '<circle class="hd" cx="60" cy="20" r="8"/>'
    '<path class="fig" d="M44 36 H76 M60 28 V72 M60 72 L54 112 M60 72 L66 112 M44 36 L40 58 L42 74 M76 36 L80 58 L78 74"/>'
    + _pf_ring(60, 74), "Ayakta pelvik taban kasılması")

SV["knack"] = fig(GRD +
    '<circle class="hd" cx="60" cy="20" r="8"/>'
    '<path class="fig" d="M44 36 H76 M60 28 V72 M60 72 L54 112 M60 72 L66 112 M44 36 L40 58 L42 74 M76 36 L72 30 L66 24"/>'
    '<g fill="none" stroke="#C8963E" stroke-width="2.2" stroke-linecap="round">'
    '<path d="M72 14 L80 10 M73 20 L82 20 M72 26 L80 30"><animate attributeName="opacity" values="0;0;1;0" keyTimes="0;0.35;0.5;1" dur="3s" repeatCount="indefinite"/></path></g>'
    '<circle cx="60" cy="74" r="7" fill="none" stroke="#C8963E" stroke-width="2.5">'
    '<animate attributeName="r" values="10;6;6;10" keyTimes="0;0.25;0.6;1" dur="3s" repeatCount="indefinite"/></circle>',
    "Öksürmeden önce sıkma")

# Çene figürleri: yandan baş; çene kulak önündeki eklemden döner.
SKULL = ('<path class="fig" d="M40 64 Q24 46 34 28 Q46 12 66 16 Q84 20 86 38 L90 48 L84 50 L84 56"/>'
         '<path class="fig" d="M44 66 L42 104 M60 76 L64 104"/>'
         '<circle cx="50" cy="50" r="3.2" fill="#C8963E"/><circle cx="50" cy="50" r="9" fill="none" stroke="#C8963E" stroke-width="2" stroke-dasharray="3 3"/>')
JAW = '<path class="fig hl" d="M52 56 L56 70 Q60 76 78 72 L84 62"/>'
TONGUE = '<path d="M64 60 Q72 54 80 58" stroke="#C8963E" stroke-width="3" fill="none" stroke-linecap="round"/>'

def _jaw(anim_vals, extra, caption):
    return fig(GRD + SKULL + TONGUE +
        f'<g transform="rotate(0 52 56)"><animateTransform attributeName="transform" type="rotate" values="{anim_vals}" '
        'keyTimes="0;0.5;1" dur="3.6s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>'
        f'{JAW}</g>' + extra, caption)

SV["jaw_rest"] = _jaw("3 52 56;4 52 56;3 52 56", "", "Çenenin dinlenme pozisyonu")
SV["jaw_open"] = _jaw("0 52 56;14 52 56;0 52 56", "", "Dil damakta ağız açma")
SV["jaw_res"] = _jaw("0 52 56;6 52 56;0 52 56",
    '<rect x="70" y="80" width="16" height="12" rx="5" fill="#2A6F6B"/><path class="fig" d="M78 92 L84 104"/>'
    '<path d="M96 88 V76 M92 80 L96 76 L100 80" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round">'
    '<animate attributeName="opacity" values="0.2;1;0.2" dur="1.8s" repeatCount="indefinite"/></path>', "Dirence karşı ağız açma")
SV["jaw_mass"] = fig(GRD + SKULL + '<path class="fig hl" d="M52 56 L56 70 Q60 76 78 72 L84 62"/>' +
    '<g><animateTransform attributeName="transform" type="rotate" values="0 64 60;360 64 60" dur="2.4s" repeatCount="indefinite"/>'
    '<circle cx="64" cy="54" r="3.4" fill="#2A6F6B"/><circle cx="69" cy="60" r="3.4" fill="#2A6F6B"/></g>'
    '<circle cx="64" cy="60" r="11" fill="none" stroke="#C8963E" stroke-width="2" stroke-dasharray="3 3"/>',
    "Çiğneme kası masajı")

EXT.update({
 "pf_lie": ("Yatarak pelvik taban kasılması", "Sırtüstü yatın, dizleriniz bükülü olsun. İdrarınızı tutmaya ve gaz çıkarmamaya çalışıyormuş gibi pelvik taban kaslarınızı içe ve yukarı doğru çekin. Kalça, karın ve uyluk kaslarınızı sıkmayın, nefesinizi tutmayın. Sıkabildiğiniz kadar tutun, sonra aynı süre tamamen gevşeyin.", "8–10 kez, 10 saniyeye kadar tutarak, günde 3 kez"),
 "pf_sit": ("Oturarak pelvik taban kasılması", "Sandalyede dik oturun, ayaklarınız yerde. Aynı kasılmayı oturarak yapın; ardından kasları hızla sıkıp hemen bırakarak birkaç hızlı kasılma ekleyin. Hızlı kasılmalar öksürük ve hapşırıkta kasların çabuk devreye girmesine yardım eder.", "8–10 uzun ve 10 hızlı kasılma, günde 3 kez"),
 "pf_stand": ("Ayakta pelvik taban kasılması", "Kasılmayı yatarak ve oturarak rahatça yapabildiğinizde ayakta deneyin. Ayakta yapmak, günlük hayatta kasların yükü taşımasını öğretir. Bulaşık yıkarken ya da sıra beklerken yapabilirsiniz.", "8–10 kasılma, günde 3 kez"),
 "knack": ("Öksürmeden önce sıkma", "Öksürmeden, hapşırmadan, gülmeden ya da bir şey kaldırmadan hemen önce pelvik taban kaslarınızı sıkın ve hareket bitene kadar tutun. Bu alışkanlık, zorlanma anında idrar kaçırmayı azaltmaya yardım eder.", "Her zorlanmadan önce"),
 "jaw_rest": ("Çenenin dinlenme pozisyonu", "Dudaklarınız kapalı, dişleriniz birbirinden hafifçe ayrık olsun; dilinizin ucu üst ön dişlerinizin hemen arkasında, damakta dursun. Gün içinde dişlerinizi sıktığınızı fark ettiğinizde bu pozisyona dönün.", "Gün içinde sık sık kontrol edin"),
 "jaw_open": ("Dil damakta ağız açma", "Dilinizin ucunu damağınıza, üst ön dişlerinizin arkasına koyun. Dil damaktan ayrılmadan ağzınızı yavaşça açın ve kapatın. Çenenin yana kaymadan, düz bir çizgide hareket etmesine dikkat edin; aynanın karşısında yapabilirsiniz.", "6–10 tekrar, günde 3 kez"),
 "jaw_res": ("Dirence karşı ağız açma", "Yumruğunuzu ya da iki parmağınızı çenenizin altına koyun. Ağzınızı hafifçe açmaya çalışırken elinizle nazikçe karşı koyun, 3–5 saniye tutup gevşeyin. Kuvvetin yarısını kullanmanız yeterli; ağrıyı artırmamalı.", "5–6 tekrar, günde 2 kez"),
 "jaw_mass": ("Çiğneme kası masajı", "Dişlerinizi sıkarak yanaktaki çiğneme kasınızı bulun, sonra gevşeyin. Parmak uçlarınızla bu kasa küçük daireler çizerek hafifçe bastırın. Ilık bir havlu ile birlikte yapmak rahatlatabilir.", "1–2 dakika, günde 2–3 kez"),
})

# ============================================================== ROTATOR MANŞET YIRTIĞI
RC_FAQ = [
 ("MR'da yırtık çıktı, ameliyat olmalı mıyım?", "Her zaman değil. Yaşla birlikte omuzda yırtık görülmesi sıktır ve yırtıkların çoğu şikâyete yol açmaz. Düşme ya da darbeye bağlı olmayan yırtıklarda genellikle önce fizyoterapi denenir; düzelmeyen ya da ani bir yaralanmayla oluşan yırtıklarda ameliyat değerlendirilir."),
 ("Yırtık fizyoterapiyle kapanır mı?", "Tam kat bir yırtık genellikle kendiliğinden kapanmaz. Ancak rotator manşetin sağlam kısımları ve kürek kemiği kasları güçlendiğinde omuz, yırtığa rağmen çoğu zaman ağrısız ve işlevsel hale gelebilir."),
 ("Geceleri hangi tarafa yatmalıyım?", "Ağrılı omzun üzerine yatmak ağrıyı artırabilir. Sağlam tarafınıza yatıp ağrılı kolunuzu önünüzdeki bir yastığa koymak ya da sırtüstü yatarken kolunuzu yastıkla desteklemek rahatlatabilir."),
 ("Egzersiz yırtığı büyütür mü?", "Kontrollü ve kademeli olarak artırılan egzersizler güvenli kabul edilir ve tedavinin temelidir. Ağrıyı belirgin artıran ağır kaldırma ve baş üstü zorlamaları bir süre azaltın; egzersizleri ağrının izin verdiği ölçüde sürdürün."),
]

RC_SRC = [
 "Minagawa H, Yamamoto N, Abe H, et al. " + ext("https://www.sciencedirect.com/science/article/abs/pii/S0972978X13000093", "Prevalence of symptomatic and asymptomatic rotator cuff tears in the general population: from mass-screening in one village") + ". J Orthop. 2013;10(1):8-12.",
 "Kuhn JE, Dunn WR, Sanders R, et al. " + ext("https://www.sciencedirect.com/science/article/abs/pii/S1058274613000839", "Effectiveness of physical therapy in treating atraumatic full-thickness rotator cuff tears: a multicenter prospective cohort study") + ". J Shoulder Elbow Surg. 2013;22(10):1371-1379.",
 "Kukkonen J, Joukainen A, Lehtinen J, et al. " + ext("https://www.sciencedirect.com/science/article/pii/S105827462100330X", "Operative versus conservative treatment of small, nontraumatic supraspinatus tears in patients older than 55 years: over 5-year follow-up of a randomized controlled trial") + ". J Shoulder Elbow Surg. 2021.",
 "Moosmayer S, Lund G, Seljom US, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/31220021/", "At a 10-year follow-up, tendon repair is superior to physiotherapy in the treatment of small and medium-sized rotator cuff tears") + ". J Bone Joint Surg Am. 2019.",
]

RC_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Rotator manşet yırtığı</h1>
    <p class="lede">Rotator manşet, omuz eklemini saran ve kolu kaldırıp döndürmemizi sağlayan dört kasın kirişlerinden oluşur. Yırtıklar çoğunlukla yaşla birlikte, yıpranmayla ortaya çıkar ve birçoğu hiç şikâyete yol açmaz. Düşme ya da darbeye bağlı olmayan yırtıklarda fizyoterapi çoğu hastada ilk ve etkili tedavidir.</p>
    <p class="meta">Son güncelleme: 30 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%22</b><span>Japonya'da bir köyde taranan 664 kişide saptanan tam kat rotator manşet yırtığı oranı</span></div>
        <div class="stat"><b>%65</b><span>Bu yırtıklardan hiç şikâyete yol açmayanların oranı</span></div>
        <div class="stat"><b>%37</b><span>80 yaş üstünde tam kat yırtık görülme sıklığı; 50'li yaşlarda %11</span></div>
        <div class="stat"><b>%75</b><span>Fizyoterapi programıyla 2 yıl boyunca ameliyata gerek kalmayan hastalar</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Rotator manşet kirişleri yaşla birlikte incelir ve yıpranır; zamanla kirişin bir kısmında (kısmi) ya da tüm kalınlığında (tam kat) yırtık oluşabilir. En sık omzun üst kısmındaki supraspinatus kirişi etkilenir. Bazen de düşme, omuz çıkığı ya da ağır bir yükü aniden kaldırmak gibi bir yaralanmayla yırtık oluşur.</p>
        <p class="soft">Tarama çalışmaları, tam kat yırtıkların yaşla birlikte belirgin şekilde arttığını ve çoğunun şikâyet yapmadığını gösteriyor. Bu yüzden MR'da görülen yırtık tek başına tedavi kararını belirlemez.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Kolu yana ya da öne kaldırırken omzun dış yüzünde ağrı</li>
          <li>Geceleri, özellikle o omzun üzerine yatınca artan ağrı</li>
          <li>Kolu kaldırırken ya da döndürürken güçsüzlük</li>
          <li>Saç tararken, üst rafa uzanırken ya da elini arkaya götürürken zorlanma</li>
          <li>Yaralanmadan sonra kolu birden kaldıramama</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ameliyat mı, fizyoterapi mi?</h2>
      <p class="soft">ABD'de travmaya bağlı olmayan tam kat yırtığı olan 452 hastanın izlendiği MOON çalışmasında, fizyoterapi programından sonra hastaların yaklaşık %75'i 2 yıl boyunca ameliyata ihtiyaç duymadı. Ameliyat olmayı seçenler bunu çoğunlukla ilk 6–12 hafta içinde yaptı; sonrasında ameliyata geçen hasta sayısı azdı.</p>
      <p class="soft">Finlandiya'da 55 yaş üstü, küçük ve travmaya bağlı olmayan yırtığı olan hastalarla yapılan bir çalışmada ortalama 6 yıllık takipte fizyoterapi ameliyat kadar iyi sonuç verdi; memnuniyet her grupta %88–92 idi. Norveç'te küçük ve orta boy yırtıklarda yapılan bir başka çalışmada ise 10 yılın sonunda onarım yapılan grupta sonuçlar daha iyiydi.</p>
      <div class="callout">
        <p>Bu yüzden karar kişiye özeldir. Düşme ya da darbeden sonra kolu kaldıramama gibi ani başlayan yırtıklarda ve genç, aktif hastalarda erken ortopedi değerlendirmesi önemlidir. Yıpranmaya bağlı yırtıklarda ise genellikle önce düzenli bir fizyoterapi programı denenir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <ul class="tx">
        <li><b>Egzersiz</b><span>Rotator manşetin sağlam kısımlarını, omzu çevreleyen kasları ve kürek kemiği kaslarını güçlendiren, hareket açıklığını koruyan egzersizler.</span></li>
        <li><b>Yükü ayarlama</b><span>Ağrıyı belirgin artıran baş üstü işler ve ağır kaldırma bir süre azaltılır; kol askıya alınmaz, günlük kullanımı sürdürülür.</span></li>
        <li><b>Ağrı kontrolü</b><span>Soğuk ya da sıcak uygulama ve hekiminizin önerdiği ağrı kesiciler egzersize devam etmeyi kolaylaştırır.</span></li>
        <li><b>Manuel terapi</b><span>Omuz ve sırta yönelik uygulamalar, egzersizle birlikte ağrıyı azaltıp hareketi artırmaya yardımcı olabilir.</span></li>
        <li><b>Ameliyat</b><span>Travmatik yırtıklarda, genç ve aktif hastalarda ve düzenli fizyoterapiye rağmen düzelmeyen şikâyetlerde ortopedi uzmanınca değerlendirilir.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Omuz için altı egzersiz</h2>
      <p class="soft">Egzersizleri ağrısız ya da hafif ağrılı aralıkta yapın; ağrı ertesi gün artmıyorsa devam edin. İzometrik egzersizlerle başlayıp ağrı azaldıkça hafif ağırlıklara geçin.</p>
      {ex_grid(["isoer", "sler", "scaption", "row", "wslide", "scap"])}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Rotator manşet için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("3W1pgU99-VM", "Rotator manşet egzersizleri videosunu oynat", "3 Best Rotator Cuff Exercises To STOP Shoulder Pain")}
          <h3>Rotator manşet için üç egzersiz</h3>
          <p>Omzu çeviren kasları güçlendirmeye yönelik temel hareketler.</p>
        </div>
        <div class="vid">
          {vbox("0IkHB763nPk", "Omuz ağrısı egzersizleri videosunu oynat", "10 Best Exercises for Shoulder Pain, Impingement, Bursitis &amp; Rotator Cuff Disease")}
          <h3>Omuz ağrısı için on egzersiz</h3>
          <p>Sıkışma, bursit ve rotator manşet sorunlarında kullanılan egzersizler.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(RC_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Düşme ya da darbeden sonra kolu hiç kaldıramama</li>
        <li>Omuzda şekil bozukluğu ya da çıkık şüphesi</li>
        <li>Omuzda kızarıklık, sıcaklık ya da ateş</li>
        <li>Kola yayılan uyuşma, karıncalanma ya da güç kaybı</li>
        <li>Göğüs ağrısı, nefes darlığı ya da terlemeyle birlikte sol omuz ve kol ağrısı (<strong>112</strong>)</li>
      </ul>
      {CTA_CARD("Omuz ağrınız", "rotator manşet yırtığı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(RC_SRC)}
    </div>
  </section>
</main>'''

page("rotator-manset-yirtigi.html", "Rotator Manşet Yırtığı",
     "Omuzda rotator manşet yırtığı nedir, her yırtık ameliyat gerektirir mi? MR bulgusu ne anlama gelir, fizyoterapi ne kadar etkili? Evde altı egzersiz ve videolar.",
     "rotator-manset-yirtigi.html", NECK_CSS, RC_BODY, YT_JS,
     seo_title="Rotator Manşet Yırtığı: Ameliyat mı Fizyoterapi mi? | İhsan Eren",
     condition="Rotator manşet yırtığı", faq_items=RC_FAQ)

# ============================================================== ÇENE EKLEMİ
TM_FAQ = [
 ("Çenemden ses geliyor, tedavi gerekir mi?", "Ağrısız klik sesi sık görülür ve tek başına tedavi gerektirmez. Sesle birlikte ağrı, ağız açmada kısıtlılık ya da takılma varsa değerlendirme yapılmalıdır."),
 ("Diş sıkmak çene ağrısı yapar mı?", "Gündüz ya da gece dişleri sıkmak çiğneme kaslarını yorar ve ağrıyı artırabilir. Gün içinde dişlerinizin birbirine değip değmediğini fark etmeye çalışın; gece sıkma için diş hekiminiz gece plağı önerebilir."),
 ("Çene eklemi rahatsızlığı geçer mi?", "Çoğu kişide şikâyetler basit önlemler ve egzersizlerle zamanla hafifler. Uzun süren ya da giderek artan şikâyetlerde diş hekimi ve fizyoterapist birlikte değerlendirme yapar."),
 ("Ameliyat gerekir mi?", "Çok nadiren. Ameliyat, ilaç dışı tedavilere yanıt vermeyen belirli eklem sorunlarında düşünülür; çoğu hastada ilk seçenek basit önlemler, egzersiz ve fizyoterapidir."),
]

TM_SRC = [
 "Valesan LF, Da-Cas CD, Réus JC, et al. " + ext("https://link.springer.com/article/10.1007/s00784-020-03710-w", "Prevalence of temporomandibular joint disorders: a systematic review and meta-analysis") + ". Clin Oral Investig. 2021;25(2):441-453.",
 "Armijo-Olivo S, Pitance L, Singh V, et al. " + ext("https://academic.oup.com/ptj/article-abstract/96/1/9/2686339", "Effectiveness of manual therapy and therapeutic exercise for temporomandibular disorders: systematic review and meta-analysis") + ". Phys Ther. 2016;96(1):9-25.",
]

TM_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Çene eklemi rahatsızlıkları</h1>
    <p class="lede">Kulağın hemen önündeki çene eklemi (temporomandibular eklem) ve çiğneme kaslarında ağrı, ağız açmada kısıtlılık ve çene sesleriyle kendini gösterir. Yetişkinlerin yaklaşık üçte birini etkiler ve çoğu zaman basit önlemler, egzersiz ve fizyoterapiyle düzelir.</p>
    <p class="meta">Son güncelleme: 30 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%31</b><span>Yetişkinlerde çene eklemi rahatsızlığı görülme sıklığı</span></div>
        <div class="stat"><b>%11</b><span>Çocuk ve ergenlerde görülme sıklığı</span></div>
        <div class="stat"><b>%26</b><span>Yetişkinlerde en sık tür olan, açılıp kapanırken ses yapan disk kayması</span></div>
        <div class="stat"><b>48</b><span>Egzersiz ve manuel terapinin etkisini inceleyen derlemedeki çalışma sayısı</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Çene eklemi, alt çene kemiğinin kafatasıyla birleştiği, konuşurken, çiğnerken ve esnerken çalışan eklemdir. Eklemin içinde hareketi kolaylaştıran küçük bir disk bulunur. Rahatsızlık çoğunlukla çiğneme kaslarının aşırı yüklenmesinden, bazen de diskin yer değiştirmesinden ya da eklemin yıpranmasından kaynaklanır.</p>
        <p class="soft">Gündüz ya da gece diş sıkma ve gıcırdatma, stres, uzun süre ağzın açık kalması, sert yiyecekler ve çeneye alınan darbeler şikâyetleri tetikleyebilir.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Kulak önünde, yanakta ya da şakakta ağrı</li>
          <li>Çiğnerken ya da uzun konuşurken artan ağrı</li>
          <li>Ağzı açıp kapatırken klik ya da çıtırtı sesi</li>
          <li>Ağız açmada kısıtlılık ya da çenenin takılması</li>
          <li>Şakakta baş ağrısı, kulakta dolgunluk hissi</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavide ne işe yarar?</h2>
      <p class="soft">Çene eklemi rahatsızlıklarının büyük çoğunluğu cerrahi olmayan yöntemlerle yönetilir. 48 çalışmayı inceleyen bir derlemede çeneye ya da boyuna uygulanan manuel terapi, tek başına ya da egzersizle birlikte umut verici sonuçlar gösterdi; ancak araştırmacılar kanıtın kalitesinin düşük olduğunu ve daha iyi çalışmalara ihtiyaç duyulduğunu vurguluyor.</p>
      <div class="callout">
        <p>Günlük alışkanlıklar çok önemlidir: bir süre yumuşak yiyecekler tüketin, sakız çiğnemeyin, büyük lokmalardan kaçının, esnerken çenenizi elinizle destekleyin ve gün içinde dişlerinizi sıkıp sıkmadığınızı fark etmeye çalışın. Stres şikâyetleri artırıyorsa <a href="stres.html">stres rehberine</a> göz atın.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <ul class="tx">
        <li><b>Bilgilendirme ve alışkanlıklar</b><span>Çeneyi zorlayan alışkanlıkların fark edilmesi ve değiştirilmesi, tedavinin ilk adımıdır.</span></li>
        <li><b>Egzersiz</b><span>Kontrollü ağız açma, çene ve boyun kaslarına yönelik egzersizler ve duruş egzersizleri.</span></li>
        <li><b>Manuel terapi</b><span>Çene eklemine, çiğneme kaslarına ve boyna yönelik uygulamalar ağrıyı azaltıp ağız açıklığını artırmaya yardımcı olabilir.</span></li>
        <li><b>Gece plağı</b><span>Gece diş sıkma ve gıcırdatma varsa diş hekimi tarafından hazırlanabilir.</span></li>
        <li><b>Sıcak uygulama</b><span>Çiğneme kaslarına ılık uygulama gerginliği azaltabilir.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Çene ve boyun için altı egzersiz</h2>
      <p class="soft">Hareketleri yavaş, ağrısız ve aynanın karşısında yapmak, çenenin yana kaymadan hareket etmesini sağlar. Ağrı ya da takılma artarsa bırakın.</p>
      {ex_grid(["jaw_rest", "jaw_open", "jaw_res", "jaw_mass", "chin", "scap"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(TM_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Ağzın birden açılamaması ya da açık kalıp kapanamaması</li>
        <li>Çenede ya da yüzde şişlik, ateş</li>
        <li>Yüzde uyuşma ya da güçsüzlük</li>
        <li>50 yaşından sonra yeni başlayan, çiğnerken artan çene ağrısıyla birlikte şakak ağrısı ya da görme bozukluğu</li>
        <li>Eforla gelen, göğüs ağrısıyla birlikte çeneye yayılan ağrı (<strong>112</strong>)</li>
      </ul>
      {CTA_CARD("Çene ağrınız", "çene eklemi rahatsızlığı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(TM_SRC)}
    </div>
  </section>
</main>'''

page("cene-eklemi.html", "Çene Eklemi Rahatsızlıkları",
     "Çene ağrısı, klik sesi ve ağız açmada kısıtlılık: çene eklemi (TME) rahatsızlıkları neden olur, nasıl geçer? Günlük öneriler ve evde altı çene ve boyun egzersizi.",
     "cene-eklemi.html", NECK_CSS, TM_BODY, "",
     seo_title="Çene Eklemi (TME) Rahatsızlıkları: Belirtiler ve Egzersizler | İhsan Eren",
     condition="Temporomandibular eklem rahatsızlığı", faq_items=TM_FAQ)

# ============================================================== İDRAR KAÇIRMA
_ex2("ui_bridge", "bridge", "Köprü", "Sırtüstü yatın, dizleriniz bükülü, ayaklarınız yerde. Önce pelvik taban kaslarınızı sıkın, sonra kalçanızı yavaşça kaldırın; 3 saniye bekleyip indirin ve kasları gevşetin.", "10 tekrar")

UI_FAQ = [
 ("İdrar kaçırma yaşlanmanın doğal bir sonucu mu?", "Sık görülse de kaçınılmaz değildir ve çoğu zaman tedavi edilebilir. Utanmadan hekiminize ya da fizyoterapistinize başvurun; ilk basamak tedavi çoğu kadında pelvik taban egzersizleridir."),
 ("Egzersizlerin etkisini ne zaman görürüm?", "Kasların güçlenmesi zaman alır; kılavuz en az 3 ay düzenli egzersiz öneriyor. Fayda görürseniz egzersizlere devam etmeniz gerekir."),
 ("Kasları doğru çalıştırdığımdan nasıl emin olabilirim?", "Pek çok kişi başlangıçta karın, kalça ya da uyluk kaslarını sıkar ya da nefesini tutar. Kılavuz, egzersizlerin bir uzman eşliğinde öğretilmesini öneriyor; fizyoterapist doğru kası bulmanıza ve programı ayarlamanıza yardım eder. Tuvalette idrarı yarıda kesmeyi egzersiz olarak yapmayın."),
 ("Erkeklerde de işe yarar mı?", "Pelvik taban egzersizleri erkeklerde de, özellikle prostat ameliyatından sonra kullanılır. Programı ürolojik değerlendirmeyle birlikte planlamak gerekir."),
]

UI_SRC = [
 "Dumoulin C, Cacciari LP, Hay-Smith EJC. " + ext("https://www.cochrane.org/evidence/CD005654_pelvic-floor-muscle-training-urinary-incontinence-women", "Pelvic floor muscle training versus no treatment, or inactive control treatments, for urinary incontinence in women") + ". Cochrane Database Syst Rev. 2018;10:CD005654.",
 "National Institute for Health and Care Excellence. " + ext("https://www.ncbi.nlm.nih.gov/books/NBK542416/", "Urinary incontinence and pelvic organ prolapse in women: management (NG123)") + ". London: NICE; 2019.",
 "NIHR Evidence. " + ext("https://evidence.nihr.ac.uk/alert/pelvic-floor-muscle-training-can-improve-symptoms-of-urinary-incontinence/", "Pelvic floor muscle training can improve symptoms of urinary incontinence") + ".",
]

UI_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>İdrar kaçırma ve pelvik taban egzersizleri</h1>
    <p class="lede">Öksürürken, hapşırırken, gülerken ya da zorlanırken idrar kaçırmak, özellikle doğum yapmış ve orta yaşın üzerindeki kadınlarda çok sıktır ve çoğu zaman utanıldığı için konuşulmaz. İyi haber: düzenli pelvik taban egzersizleri bu tür idrar kaçırmada ilk basamak ve çok etkili bir tedavidir.</p>
    <p class="meta">Son güncelleme: 30 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%34</b><span>İngiltere'de idrar kaçırma yaşayan kadınların oranı; gerçek oran muhtemelen daha yüksek</span></div>
        <div class="stat"><b>8 kat</b><span>Pelvik taban egzersizi yapan, zorlanma tipi idrar kaçırması olan kadınlarda iyileşme olasılığı (%56'ya karşı %6)</span></div>
        <div class="stat"><b>3 ay</b><span>Kılavuzun ilk basamak tedavi olarak önerdiği en kısa denetimli egzersiz süresi</span></div>
        <div class="stat"><b>8 × 3</b><span>Kılavuzun önerdiği günlük program: en az 8 kasılma, günde 3 kez</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Pelvik taban nedir?</h2>
        <p class="soft">Pelvik taban, leğen kemiğinin tabanında bir hamak gibi uzanan ve mesaneyi, rahmi ve bağırsağı destekleyen kaslardır. Bu kaslar idrar ve dışkı kontrolünde görev alır. Gebelik ve doğum, menopoz, uzun süreli öksürük, kabızlık, fazla kilo ve ağır yük kaldırmak bu kasları zayıflatabilir.</p>
      </div>
      <div>
        <h2>İdrar kaçırma türleri</h2>
        <ul class="dots">
          <li><b>Zorlanma tipi:</b> öksürürken, hapşırırken, gülerken, zıplarken ya da kaldırırken kaçırma</li>
          <li><b>Sıkışma tipi:</b> aniden gelen ve ertelenemeyen idrar hissiyle kaçırma</li>
          <li><b>Karışık tip:</b> ikisinin birlikte görülmesi</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Pelvik taban egzersizleri ne kadar etkili?</h2>
      <p class="soft">31 çalışmayı ve 1.817 kadını kapsayan 2018 tarihli Cochrane derlemesinde, zorlanma tipi idrar kaçırması olan kadınlarda pelvik taban egzersizi yapanların iyileşme olasılığı egzersiz yapmayanlara göre 8 kat yüksekti (%56'ya karşı %6). Her tür idrar kaçırmada bu oran 5 kattı (%35'e karşı %6); yaşam kalitesi de belirgin şekilde düzeldi ve yan etkiler nadir ve hafifti.</p>
      <p class="soft">İngiltere'nin NICE kılavuzu, zorlanma tipi ya da karışık tip idrar kaçırmada ilk basamak tedavi olarak en az 3 ay süren, uzman eşliğinde pelvik taban egzersizi öneriyor. Program en az 8 kasılmanın günde 3 kez yapılmasından oluşmalı ve fayda görülürse sürdürülmelidir.</p>
      <div class="callout">
        <p>Kılavuz ayrıca vücut kitle indeksi 30'un üzerinde olanlara kilo vermeyi, sıkışma tipi şikâyetlerde kafeini azaltmayı ve çok fazla ya da çok az sıvı alanlara sıvı alımını düzenlemeyi öneriyor.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Kasları doğru bulmak</h2>
        <p class="soft">İdrarınızı tutmaya ve gaz çıkarmamaya çalışıyormuş gibi, kasları içe ve yukarı doğru çekin. Doğru yaptığınızda dışarıdan neredeyse hiçbir hareket görülmez.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Kalça, karın ve uyluk kaslarınızı sıkmayın.</li>
        <li>Nefesinizi tutmayın; normal nefes almaya devam edin.</li>
        <li>Her kasılmadan sonra kasları tamamen gevşetin.</li>
        <li>Tuvalette idrarı yarıda kesmeyi egzersiz olarak yapmayın.</li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Pelvik taban için altı adım</h2>
      <p class="soft">Yatarak başlayın; kasları rahatça bulabildiğinizde oturarak ve ayakta yapın. Uzun (tutmalı) ve hızlı kasılmaları birlikte çalışın.</p>
      {ex_grid(["pf_lie", "pf_sit", "pf_stand", "knack", "ui_bridge", "walk"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(UI_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>İdrarda kan</li>
        <li>İdrar yaparken yanma, ateş ya da yan ağrısı</li>
        <li>Hiç idrar yapamama ya da mesanenin boşalmadığı hissi</li>
        <li>Ani başlayan idrar ya da dışkı kaçırmayla birlikte bacaklarda güçsüzlük veya kasık ve makat bölgesinde his kaybı (acil)</li>
        <li>Vajinada ele gelen şişlik ya da aşağı doğru sarkma hissi</li>
      </ul>
      {CTA_CARD("İdrar kaçırma şikâyetiniz", "idrar kaçırma ve pelvik taban egzersizleri")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(UI_SRC)}
    </div>
  </section>
</main>'''

page("idrar-kacirma.html", "İdrar Kaçırma ve Pelvik Taban Egzersizleri",
     "Öksürürken, gülerken idrar kaçırma: pelvik taban egzersizleri nasıl yapılır, ne kadar etkili? Cochrane ve NICE kılavuzu önerileri ve evde altı adımlık program.",
     "idrar-kacirma.html", NECK_CSS, UI_BODY, "",
     seo_title="İdrar Kaçırma ve Pelvik Taban (Kegel) Egzersizleri | İhsan Eren",
     condition="İdrar kaçırma", faq_items=UI_FAQ)

# ============================================================== GEBELİKTE BEL AĞRISI
_ex2("pg_cat", "cat", "Kedi-deve", "Ellerinizin ve dizlerinizin üzerinde durun. Nefes verirken sırtınızı yavaşça yukarı yuvarlayın, nefes alırken sırtınızı düz konuma getirin; belinizi aşağı çökertmeyin. Bel ağrısında rahatlatıcı bir harekettir.", "8–10 tekrar")
_ex2("pg_bird", "birddog", "Kuş-köpek", "Ellerinizin ve dizlerinizin üzerinde, sırtınız düz durun. Bir kolunuzu öne ya da karşı bacağınızı arkaya uzatın; dengede zorlanırsanız yalnızca kol ya da yalnızca bacakla yapın. 5 saniye tutup taraf değiştirin.", "Her iki yana 6–8 tekrar")
_ex2("pg_abd", "abd", "Yan yatarak bacak kaldırma", "Yan yatın, başınızın ve karnınızın altına yastık koyabilirsiniz. Alttaki dizinizi bükün, üstteki bacağınızı dizi düz şekilde hafifçe kaldırıp yavaşça indirin. Kalçanın yan kaslarını güçlendirir.", "Her iki yana 10 tekrar")
_ex2("pg_sts", "sts", "Sandalyeden kalkıp oturma", "Sağlam bir sandalyenin önüne oturun, ayaklarınız kalça genişliğinde açık olsun. Ağırlığınızı iki ayağınıza eşit dağıtarak kalkın ve kontrollü oturun.", "8–10 tekrar")
_ex2("pg_pf", "pf_sit", "Oturarak pelvik taban kasılması", "Dik oturun. Pelvik taban kaslarınızı içe ve yukarı doğru çekip birkaç saniye tutun, sonra tamamen gevşeyin. Gebelikte ve doğumdan sonra pelvik taban egzersizleri idrar kaçırmayı önlemeye yardım eder.", "8–10 kasılma, günde 3 kez")
_ex2("pg_walk", "walk", "Yürüyüş", "Konuşabileceğiniz bir tempoda, düz zeminde yürüyün. Leğen kemiği ağrınız varsa adımlarınızı kısa tutun ve ağrıyı artıran uzun yürüyüşleri bölün.", "Günde 20–30 dakika, bölerek yapılabilir")

PG_FAQ = [
 ("Gebelikte egzersiz yapmak güvenli mi?", "Sağlıklı, komplikasyonsuz gebeliklerde evet. Amerikan Kadın Doğum Uzmanları Derneği (ACOG) haftada 150 dakika orta yoğunlukta egzersiz öneriyor. Başlamadan önce kadın doğum uzmanınıza danışın; özel bir risk durumu varsa program buna göre ayarlanır."),
 ("Hangi aktivitelerden kaçınmalıyım?", "Temas sporlarından, ata binme, kayak ve jimnastik gibi düşme riski yüksek aktivitelerden ve dalıştan kaçının. İlerleyen gebelikte uzun süre sırtüstü yatarak egzersiz yapmayın. Yüzme, su içi egzersiz ve sabit bisiklet gebelik boyunca vücudu en az zorlayan seçeneklerdir."),
 ("Doğumdan sonra ağrı geçer mi?", "Çoğu kadında bel ve leğen kemiği ağrısı doğumdan sonraki haftalar ve aylar içinde azalır; bir kısmında ise sürebilir. Devam eden ağrıda doğum sonrası fizyoterapi değerlendirmesi faydalıdır."),
 ("Destek kemeri kullanmalı mıyım?", "Bazı kadınlarda, özellikle leğen kemiği ağrısında, destek kemeri yürürken rahatlama sağlayabilir. Egzersizin yerine değil, gerekirse yanında kullanılmalıdır."),
]

PG_SRC = [
 "Liddle SD, Pennick V. " + ext("https://www.omicsdi.org/dataset/biostudies-literature/S-EPMC7053516", "Interventions for preventing and treating low-back and pelvic pain during pregnancy") + ". Cochrane Database Syst Rev. 2015;(9):CD001139.",
 "Shiri R, Coggon D, Falah-Hassani K. " + ext("https://onlinelibrary.wiley.com/doi/10.1002/ejp.1096", "Exercise for the prevention of low back and pelvic girdle pain in pregnancy: a meta-analysis of randomized controlled trials") + ". Eur J Pain. 2018;22(1):19-27.",
 "American College of Obstetricians and Gynecologists. " + ext("https://www.acog.org/clinical/clinical-guidance/committee-opinion/articles/2020/04/physical-activity-and-exercise-during-pregnancy-and-the-postpartum-period", "Physical activity and exercise during pregnancy and the postpartum period. Committee Opinion No. 804") + ". Obstet Gynecol. 2020;135(4):e178-e188.",
 "MotherToBaby. " + ext("https://www.ncbi.nlm.nih.gov/books/NBK582697/", "Exercise") + ". Fact sheet.",
]

PG_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Gebelikte bel ve leğen kemiği ağrısı</h1>
    <p class="lede">Gebelikte bel ve leğen kemiği (pelvik kuşak) ağrısı çok sıktır ve gebelik ilerledikçe artabilir. Güvenli egzersizler, günlük hayattaki küçük değişiklikler ve gerektiğinde fizyoterapi ağrıyı hafifletmeye ve günlük işleri sürdürmeye yardımcı olur.</p>
    <p class="meta">Son güncelleme: 30 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>3'te 2</b><span>Gebelikte bel ağrısı yaşayan kadınlar (üçte ikiden fazlası)</span></div>
        <div class="stat"><b>5'te 1</b><span>Gebelikte leğen kemiği (pelvik kuşak) ağrısı yaşayan kadınlar</span></div>
        <div class="stat"><b>150 dk</b><span>ACOG'un gebelikte önerdiği haftalık orta yoğunlukta egzersiz</span></div>
        <div class="stat"><b>%21</b><span>Egzersizle bel ve leğen ağrısına bağlı yeni iş göremezlik izinlerindeki azalma</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Bel ağrısı mı, leğen kemiği ağrısı mı?</h2>
        <p class="soft">Gebelikte hormonların etkisiyle bağlar gevşer, bebek büyüdükçe ağırlık merkezi öne kayar ve bel ile leğen kemiği üzerindeki yük artar. Bel ağrısı belin alt kısmında hissedilir. Leğen kemiği (pelvik kuşak) ağrısı ise kasık kemiğinin önünde ya da kalçaların arkasında hissedilir; yürürken, merdiven çıkarken, tek ayak üzerinde dururken ya da yatakta dönerken artar.</p>
        <p class="soft">Ağrı gebelik ilerledikçe artabilir; iş, günlük işler ve uyku üzerinde belirgin etkisi olabilir.</p>
      </div>
      <div>
        <h2>Günlük hayatta öneriler</h2>
        <ul class="dots">
          <li>Yatakta dönerken dizlerinizi birlikte tutun.</li>
          <li>Dizlerinizin arasına yastık koyarak yan yatın.</li>
          <li>Pantolon ve çoraplarınızı oturarak giyin.</li>
          <li>Merdivenleri basamak basamak çıkın, ağır yük taşımayın.</li>
          <li>Uzun süre tek bacak üzerinde durmaktan ve bacak bacak üstüne atmaktan kaçının.</li>
          <li>Alçak topuklu, destekli ayakkabılar giyin.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Egzersiz ne sağlar?</h2>
      <p class="soft">Cochrane derlemesine göre gebe kadınların üçte ikiden fazlası bel ağrısı, yaklaşık beşte biri leğen kemiği ağrısı yaşıyor. 2.347 gebe kadını kapsayan 11 çalışmanın meta-analizinde, gebelikte egzersiz bel ağrısı riskini biraz azalttı ve bel ve leğen ağrısına bağlı yeni iş göremezlik izinlerini %21 azalttı; ancak leğen kemiği ağrısını önlemedi. Leğen kemiği ağrısında kişiye özel egzersizler, günlük hayattaki uyarlamalar ve gerektiğinde destek kemeri birlikte planlanır.</p>
      <p class="soft">Amerikan Kadın Doğum Uzmanları Derneği (ACOG), komplikasyonsuz gebeliklerde haftada 150 dakika orta yoğunlukta egzersiz öneriyor. Yüzme, su içi egzersiz ve sabit bisiklet vücudu en az zorlayan seçenekler arasında.</p>
      <div class="callout">
        <p>İlerleyen gebelikte uzun süre sırtüstü yatmak baş dönmesine yol açabilir. Bu yüzden aşağıdaki egzersizler yan yatarak, oturarak, ayakta ya da eller ve dizler üzerinde yapılır. Egzersize başlamadan önce kadın doğum uzmanınıza danışın.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Gebelikte güvenli altı egzersiz</h2>
      <p class="soft">Hareketleri yavaş ve ağrısız aralıkta yapın; leğen kemiği ağrısını artıran geniş adımlardan ve bacakları iki yana açan hareketlerden kaçının.</p>
      {ex_grid(["pg_cat", "pg_bird", "pg_abd", "pg_sts", "pg_pf", "pg_walk"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(PG_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Egzersiz sırasında ya da herhangi bir zamanda şunlar olursa egzersizi bırakın ve beklemeden hekiminize başvurun:</p>
      <ul class="dots redflags">
        <li>Vajinal kanama ya da sıvı gelmesi</li>
        <li>Düzenli, ağrılı kasılmalar ya da ritmik olarak gelip giden bel ağrısı</li>
        <li>Bebek hareketlerinde azalma</li>
        <li>Göğüs ağrısı, egzersizden önce başlayan nefes darlığı, baş dönmesi ya da baş ağrısı</li>
        <li>Baldırda ağrı ya da şişlik</li>
        <li>Ateşle birlikte bel ağrısı, idrar yaparken yanma; bacaklarda uyuşma ya da güçsüzlük</li>
      </ul>
      {CTA_CARD("Gebelikteki bel ve leğen ağrınız", "gebelikte bel ve leğen kemiği ağrısı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(PG_SRC)}
    </div>
  </section>
</main>'''

page("gebelikte-bel-agrisi.html", "Gebelikte Bel ve Leğen Kemiği Ağrısı",
     "Gebelikte bel ve leğen kemiği ağrısı neden olur, egzersiz güvenli mi, nelere dikkat etmeli? Günlük hayat önerileri, evde altı güvenli egzersiz ve uyarı işaretleri.",
     "gebelikte-bel-agrisi.html", NECK_CSS, PG_BODY, "",
     seo_title="Gebelikte Bel ve Leğen Kemiği Ağrısı: Egzersizler ve Öneriler | İhsan Eren",
     condition="Gebelikte bel ve pelvik kuşak ağrısı", faq_items=PG_FAQ)

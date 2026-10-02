# -*- coding: utf-8 -*-
# Omuz sıkışması (subakromiyal ağrı) sayfası. heel_part.py'den sonra exec edilir.

LEGS_F2 = 'M64 78 L56 112 M64 78 L72 112'

# Kapı pervazında izometrik dışa döndürme (önden): dirsek gövdede, el dışa doğru pervaza iter.
SV["isoer"] = fig(GRD +
    '<path class="obj" d="M22 8 V112" stroke-width="5"/>'
    '<circle class="hd" cx="64" cy="20" r="8"/>'
    f'<path class="fig" d="M48 38 H80 M64 30 V78 {LEGS_F2} M80 38 L84 60 L82 76"/>'
    '<rect x="49" y="50" width="5" height="9" rx="2" fill="#C8963E"/>'
    '<path class="fig hl" d="M48 38 L46 60 L28 58"/>'
    '<g fill="none" stroke="#C8963E" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M40 46 L36 50 L40 54"><animate attributeName="opacity" values="0;1;0" dur="1.6s" repeatCount="indefinite"/></path>'
    '<path d="M34 46 L30 50 L34 54"><animate attributeName="opacity" values="0;1;0" dur="1.6s" begin="0.4s" repeatCount="indefinite"/></path></g>',
    "Kapı pervazında dışa döndürme")

# Yan yatarak dışa döndürme (önden, yan yatmış): üst kolun ön kolu yerden tavana döner.
SV["sler"] = fig(GRD +
    '<circle class="hd" cx="13" cy="99" r="7"/>'
    '<path class="fig" d="M22 104 H70 L90 106 L112 108 M22 106 L12 110"/>'
    '<path class="fig hl" d="M28 97 H48"/>'
    f'<path class="fig hl" d="M48 97 L48 110">{anim_d("M48 97 L48 110;M48 97 L48 72;M48 97 L48 110")}</path>'
    f'<g>{anim_t("0 0;0 -38;0 0")}<rect x="43" y="108" width="10" height="5" rx="2" fill="#C8963E"/></g>',
    "Yan yatarak dışa döndürme")

# Lastik bantla kürek çekme (yandan)
SV["row"] = fig(GRD +
    '<path class="obj" d="M108 30 V112" stroke-width="5"/>'
    '<circle class="hd" cx="52" cy="22" r="7"/>'
    '<path class="fig" d="M50 32 V76 L46 112 M50 76 L56 112"/>'
    f'<path class="band" d="M82 56 L106 56">{anim_d("M82 56 L106 56;M56 56 L106 56;M82 56 L106 56")}</path>'
    f'<path class="fig hl" d="M50 40 L66 50 L82 56">{anim_d("M50 40 L66 50 L82 56;M50 40 L36 54 L56 56;M50 40 L66 50 L82 56")}</path>',
    "Lastik bantla kürek çekme")

# Kolları çapraz düzlemde kaldırma (önden): kollar yandan omuz hizasına kalkar.
SV["scaption"] = fig(GRD +
    '<circle class="hd" cx="64" cy="20" r="8"/>'
    f'<path class="fig" d="M48 38 H80 M64 30 V78 {LEGS_F2}"/>'
    f'<g>{anim_t("0 48 38;78 48 38;0 48 38", typ="rotate")}<path class="fig hl" d="M48 38 L46 70"/><circle cx="46" cy="72" r="3.5" fill="#C8963E"/></g>'
    f'<g>{anim_t("0 80 38;-78 80 38;0 80 38", typ="rotate")}<path class="fig hl" d="M80 38 L82 70"/><circle cx="82" cy="72" r="3.5" fill="#C8963E"/></g>',
    "Kolları çapraz düzlemde kaldırma")

# Duvarda kaydırma (yandan): ön kollar duvarda yukarı kayar.
SV["wslide"] = fig(GRD +
    '<path class="obj" d="M98 6 V112" stroke-width="5"/>'
    '<circle class="hd" cx="68" cy="22" r="7"/>'
    '<path class="fig" d="M66 32 V76 L62 112 M66 76 L72 112"/>'
    f'<path class="fig hl" d="M66 40 L90 56 L94 34">{anim_d("M66 40 L90 56 L94 34;M66 40 L88 24 L93 4;M66 40 L90 56 L94 34")}</path>',
    "Duvarda kaydırma")

SV["scap2"] = SV["scap"]

EXT.update({
 "scap2": ("Kürek kemiği sıkıştırma", "Dik durun ya da oturun. Omuzlarınızı kulaklarınıza kaldırmadan kürek kemiklerinizi geriye ve biraz aşağıya doğru sıkıştırın. 5 saniye tutup gevşeyin.", "10 tekrar, günde 2–3 kez"),
 "isoer": ("Kapı pervazında dışa döndürme", "Ağrılı tarafınız kapı pervazına bakacak şekilde durun. Dirseğinizi 90 derece bükün, kolunuzu gövdenize yaslayın; araya katlanmış küçük bir havlu koyabilirsiniz. Elinizin dış yüzüyle pervaza doğru, kolunuz yer değiştirmeden itin. Ağrıyı artırmayan bir kuvvetle 30–45 saniye tutun.", "5 tekrar, günde 1–2 kez"),
 "sler": ("Yan yatarak dışa döndürme", "Ağrısız tarafınıza yan yatın. Üstteki kolunuzun dirseğini 90 derece bükün, dirseğinizi belinize yaslayın. Elinizdeki hafif ağırlığı (dolu bir su şişesi olabilir) dirseğiniz sabit kalacak şekilde tavana doğru kaldırın, yavaşça indirin.", "10–15 tekrar, 2–3 set"),
 "row": ("Lastik bantla kürek çekme", "Lastik bandı kapı koluna ya da sağlam bir yere göğüs hizasında bağlayın. Bandın uçlarını tutup dirseklerinizi gövdenize yakın tutarak geriye çekin, kürek kemiklerinizi birbirine yaklaştırın. Yavaşça başlangıca dönün.", "10–15 tekrar, 2–3 set"),
 "scaption": ("Kolları çapraz düzlemde kaldırma", "Ayakta durun, kollarınız yanda, başparmaklarınız yukarı baksın. Kollarınızı öne ve hafifçe yana doğru, yaklaşık 30 derecelik açıyla omuz hizasına kadar kaldırın; ellerinizde hafif birer ağırlık olabilir. Omuzlarınızı kulaklarınıza doğru kaldırmadan yavaşça indirin.", "10 tekrar, 2–3 set"),
 "wslide": ("Duvarda kaydırma", "Yüzünüz duvara dönük durun, ön kollarınızı omuz hizasında duvara yaslayın. Kollarınızı duvarda kaydırarak ağrısız aralıkta yukarı uzatın, kürek kemiklerinizin öne ve yukarı kaydığını hissedin. Yavaşça başlangıca dönün.", "10 tekrar, günde 1–2 kez"),
})

OMUZS_FAQ = [
 ("Omuz sıkışması ameliyatsız geçer mi?", "Çoğu kişide evet. Fizyoterapi, ilaç, gerektiğinde iğne ve günlük yükün ayarlanmasıyla hastaların yaklaşık %60'ı 2 yıl içinde tatmin edici sonuç alıyor. Yükü kademeli artırılan bir egzersiz programı iyileşmenin temelidir."),
 ("Ameliyat olmam gerekir mi?", "Çoğu zaman hayır. Kemik çıkıntısını tıraşlayan dekompresyon ameliyatı iki büyük çalışmada sahte ya da yalnızca tanısal ameliyattan üstün bulunmadı ve uluslararası bir uzman paneli bu ameliyatın yapılmamasını öneriyor. Düşme gibi bir travmadan sonra kolu kaldıramama varsa cerrahi değerlendirme ayrıca gerekir."),
 ("MR'ımda tendon yırtığı var, ne yapmalıyım?", "Endişelenmeyin. Japonya'daki bir toplum taramasında her beş kişiden birinde tam kat rotator manşet yırtığı bulundu ve bu yırtıkların üçte ikisi hiç ağrı yapmıyordu. Tedavi kararı MR görüntüsüne değil, şikâyetlerinize ve muayene bulgularınıza göre verilir; travma dışı yırtıklarda da ilk tedavi egzersizdir."),
 ("Kortizon iğnesi yaptırmalı mıyım?", "Kortizon iğnesi ağrıyı azaltabilir ve egzersize başlamayı kolaylaştırabilir; ancak egzersizden üstün olduğu gösterilmemiştir ve tek başına kalıcı çözüm değildir. Kararı hekiminizle birlikte verin."),
 ("Omzum ağrırken spor yapabilir miyim?", "Evet, ağrıyı belirgin artırmayan sporlara devam edebilirsiniz. Yüzme, tenis, voleybol gibi kolun baş üstünde kullanıldığı sporları ağrı azalana kadar azaltın ve dönüşte yükü kademeli artırın."),
 ("Donuk omuzdan farkı nedir?", "Omuz sıkışmasında kolu başkası kaldırdığında hareket genellikle serbesttir ve ağrı belli bir açıda ortaya çıkar. Donuk omuzda ise omuz hem sizin hem de başkası kaldırdığında aynı şekilde kısıtlıdır. <a href=\"donuk-omuz.html\">Donuk omuz rehberine göz atın →</a>"),
]

OMUZS_SRC = [
 "Beard AJ, Rees JL, Cook JA, et al. " + ext("https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(17)32457-1/fulltext", "Arthroscopic subacromial decompression for subacromial shoulder pain (CSAW): a multicentre, pragmatic, parallel group, placebo-controlled, three-group, randomised surgical trial") + ". Lancet. 2018;391(10118):329-338.",
 "Ketola S, Lehtinen J, Arnala I, et al. Does arthroscopic acromioplasty provide any additional value in the treatment of shoulder impingement syndrome? A two-year randomised controlled trial. J Bone Joint Surg Br. 2009;91(10):1326-1334.",
 "Lewis J. Rotator cuff related shoulder pain: assessment, management and uncertainties. Man Ther. 2016;23:57-68.",
 "Minagawa H, Yamamoto N, Abe H, et al. " + ext("https://jortho.org/prevalence-of-symptomatic-and-asymptomatic-rotator-cuff-tears-in-the-general-population-from-mass-screening-in-one-village/", "Prevalence of symptomatic and asymptomatic rotator cuff tears in the general population: from mass-screening in one village") + ". J Orthop. 2013;10(1):8-12.",
 "Paavola M, Malmivaara A, Taimela S, et al. Subacromial decompression versus diagnostic arthroscopy for shoulder impingement: randomised, placebo surgery controlled clinical trial. BMJ. 2018;362:k2860.",
 "Physiopedia. " + ext("https://www.physio-pedia.com/Shoulder_Impingement", "Shoulder Impingement") + ".",
 "StatPearls. " + ext("https://www.ncbi.nlm.nih.gov/books/NBK554518/", "Shoulder Impingement Syndrome") + ". Treasure Island (FL): StatPearls Publishing.",
 "Steuri R, Sattelmayer M, Elsig S, et al. Effectiveness of conservative interventions including exercise, manual therapy and medical management in adults with shoulder impingement: a systematic review and meta-analysis of RCTs. Br J Sports Med. 2017;51(18):1340-1347.",
 "Vandvik PO, Lähdeoja T, Ardern C, et al. " + ext("https://www.bmj.com/content/364/bmj.l294", "Subacromial decompression surgery for adults with shoulder pain: a clinical practice guideline") + ". BMJ. 2019;364:l294.",
]

OMUZS_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Omuz sıkışması (subakromiyal ağrı)</h1>
    <p class="lede">Kolu yana ya da yukarı kaldırırken omzun dış yüzünde, bazen kola doğru yayılan ağrıyla kendini gösterir. Eskiden "sıkışma" denen bu tabloda asıl sorun çoğunlukla omzu çeviren kasların (rotator manşet) tendonlarının aşırı yüklenmesidir. En etkili tedavi egzersizdir; ameliyat çoğu zaman gerekmez.</p>
    <p class="meta">Son güncelleme: {UPDATED}</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%44–65</b><span>Omuz ağrısı şikâyetleri içinde subakromiyal ağrının payı</span></div>
        <div class="stat"><b>%22</b><span>Toplum taramasında tam kat tendon yırtığı bulunan kişi; bu yırtıkların üçte ikisi ağrısız</span></div>
        <div class="stat"><b>2 yıl</b><span>Takipte ameliyat, egzersiz programına ek fayda sağlamadı</span></div>
        <div class="stat"><b>Güçlü öneri</b><span>Uluslararası uzman panelinin dekompresyon ameliyatına karşı önerisi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Omzun üstündeki kemik çatı (akromiyon) ile kol kemiği arasında kalan dar alana subakromiyal alan denir. Burada omzu çeviren kasların (rotator manşet) tendonları ve bir kese (bursa) bulunur. Bu yapıların aşırı ya da alışık olunmayan yüklenmesi ağrıya yol açar.</p>
        <p class="soft">Eskiden tendonun kemiğe "sıkıştığı" düşünülürdü. Bugün sorunun çoğunlukla tendonun kendisinin aşırı yüklenmesi olduğu biliniyor; bu yüzden "rotator manşetle ilişkili omuz ağrısı" adı da kullanılıyor.</p>
      </div>
      <div>
        <h2>Belirtiler ve risk etkenleri</h2>
        <ul class="dots">
          <li>Kolu yana ya da öne kaldırırken belli bir açıda artan ağrı</li>
          <li>Omzun dış yüzüne, bazen dirseğe kadar yayılan ağrı</li>
          <li>Ağrılı tarafa yatınca ve geceleri artan ağrı</li>
          <li>Saç tarama, yüksek rafa uzanma, ceket giyme gibi işlerde zorlanma</li>
          <li>Risk etkenleri: 40 yaş üstü, kolun baş hizasının üstünde tekrarlı kullanıldığı işler ve sporlar</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>MR'daki yırtık her zaman ağrının nedeni mi?</h2>
      <p class="soft">Japonya'da bir köyde 664 kişinin tarandığı çalışmada her beş kişiden birinde (%22,1) tam kat rotator manşet yırtığı bulundu ve bu yırtıkların üçte ikisi hiç ağrı yapmıyordu. Yırtık görülme sıklığı yaşla artıyor: 50'li yaşlarda %10,7 iken 80'li yaşlarda %36,6'ya çıkıyor.</p>
      <div class="callout">
        <p>Yani MR'da tendon yıpranması ya da küçük bir yırtık görülmesi, ağrının tek nedeni olduğu ya da ameliyat gerektiği anlamına gelmez. Karar, şikâyetleriniz ve muayene bulgularınızla birlikte verilir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <p class="soft">Kılavuzlar tedavinin merkezine egzersizi koyuyor. Diğer yöntemler, egzersizi yapılabilir kılmak için destek olarak kullanılır.</p>
      <ul class="tx">
        <li><b>Egzersiz</b><span>Tedavinin temelidir. Omuz ve kürek kemiği kaslarını güçlendiren, yükü kademeli artırılan bir program ağrıyı azaltır ve işlevi iyileştirir. Sonuç için programın haftalarca, düzenli sürdürülmesi gerekir.</span></li>
        <li><b>Manuel terapi ve destekleyici yöntemler</b><span>Manuel terapi, bantlama, şok dalga ve lazer egzersize eklenebilecek yöntemlerdir; kanıtlar sınırlı olsa da ağrıyı azaltmaya yardımcı olabilir.</span></li>
        <li><b>Kortizon iğnesi</b><span>Plaseboya göre daha etkilidir ve egzersize başlamayı kolaylaştırabilir; ancak egzersizden üstün olduğu gösterilmemiştir.</span></li>
        <li><b>Günlük yükü ayarlamak</b><span>Ağrıyı belirgin artıran baş üstü işleri geçici olarak azaltmak, omzu tamamen dinlendirmeden iyileşmeye zaman tanır.</span></li>
        <li><b>Ameliyat</b><span>Kemik çıkıntısını tıraşlayan dekompresyon ameliyatı, Birleşik Krallık'taki CSAW ve Finlandiya'daki FIMPACT çalışmalarında sahte ya da yalnızca tanısal ameliyattan üstün bulunmadı. Uluslararası bir uzman paneli bu ameliyatın yapılmamasını güçlü şekilde öneriyor. Travmaya bağlı büyük tendon yırtıklarında cerrahi değerlendirme ayrıdır.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Omuz için altı egzersiz</h2>
      <p class="soft">Egzersiz sırasında hafif ve katlanılabilir bir ağrı olabilir; ağrı ertesi gün başlangıç düzeyine dönüyorsa devam etmek güvenlidir. İlk iki hareket ağrılı dönemde de uygundur. Kolu kaldırdığınız hareketlerde ağrı artıyorsa hareket aralığını küçültün.</p>
      {ex_grid(["scap2", "isoer", "sler", "row", "scaption", "wslide"])}
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Günlük hayatta omzunuz için</h2>
        <p class="soft">Amaç omzu hareketsiz bırakmak değil, yükünü ağrının izin verdiği ölçüde ayarlamak ve kasları yeniden güçlendirmektir.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Sık kullandığınız eşyaları üst raflardan göğüs hizasına indirin.</li>
        <li>Ağrılı tarafa yatamıyorsanız diğer tarafa yatıp kolunuzu önünüzdeki bir yastığa koyun.</li>
        <li>Masa başında dirseklerinizi destekleyin, klavye ve fareyi gövdenize yakın tutun.</li>
        <li>Ağrısız aralıktaki günlük hareketlere devam edin; omzu askıya almayın.</li>
        <li>Spora dönüşte baş üstü hareketlerin yükünü kademeli artırın.</li>
      </ul>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Omuz sıkışması için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("0IkHB763nPk", "Omuz ağrısı egzersizleri videosunu oynat", "10 Best Exercises for Shoulder Pain, Impingement, Bursitis &amp; Rotator Cuff Disease")}
          <h3>Omuz ağrısı için on egzersiz</h3>
          <p>Sıkışma, bursit ve rotator manşet sorunlarında kullanılan egzersizler.</p>
        </div>
        <div class="vid">
          {vbox("3W1pgU99-VM", "Rotator manşet egzersizleri videosunu oynat", "3 Best Rotator Cuff Exercises To STOP Shoulder Pain")}
          <h3>Rotator manşet için üç egzersiz</h3>
          <p>Omzu çeviren kasları güçlendirmeye yönelik temel hareketler.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(OMUZS_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Omuz ağrısı her zaman omuz sıkışması değildir. Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Düşme ya da darbeden sonra kolu kaldıramama, omuzda şekil bozukluğu</li>
        <li>Omuzda kızarıklık, şişlik, sıcaklık ve ateş</li>
        <li>Boyundan kola yayılan ağrı, kolda uyuşma, karıncalanma ya da ani güç kaybı</li>
        <li>Özellikle sol omuz ağrısına göğüs ağrısı, nefes darlığı ya da terleme eşlik ediyorsa (kalp kaynaklı olabilir, <strong>112</strong>'yi arayın)</li>
        <li>Nedensiz kilo kaybı, dinlenmekle geçmeyen şiddetli gece ağrısı ya da kanser öyküsü</li>
      </ul>
      {CTA_CARD("Omuz ağrınız", "omuz sıkışması")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(OMUZS_SRC)}
    </div>
  </section>
</main>'''

page("omuz-sikismasi.html", "Omuz Sıkışması",
     "Omuz sıkışması (subakromiyal ağrı, rotator manşet tendiniti) nedir, MR'daki yırtık önemli mi, ameliyat gerekir mi? Evde altı egzersiz, günlük hayat önerileri, videolar ve uyarı işaretleri.",
     "omuz-sikismasi.html", NECK_CSS, OMUZS_BODY, YT_JS,
     seo_title="Omuz Sıkışması (Subakromiyal Ağrı): Egzersizler ve Tedavi | İhsan Eren",
     condition="Omuz sıkışması (subakromiyal ağrı sendromu)", about=cond("Omuz sıkışması (subakromiyal ağrı sendromu)"),
     faq_items=pick(OMUZS_FAQ, 0, 1, 2, 3))

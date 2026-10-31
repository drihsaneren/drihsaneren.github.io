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

# Kürek kemiği düzleminde kolları kaldırma (önden): kollar yandan omuz hizasına kalkar.
SV["scaption"] = fig(GRD +
    '<circle class="hd" cx="64" cy="20" r="8"/>'
    f'<path class="fig" d="M48 38 H80 M64 30 V78 {LEGS_F2}"/>'
    f'<g>{anim_t("0 48 38;78 48 38;0 48 38", typ="rotate")}<path class="fig hl" d="M48 38 L46 70"/><circle cx="46" cy="72" r="3.5" fill="#C8963E"/></g>'
    f'<g>{anim_t("0 80 38;-78 80 38;0 80 38", typ="rotate")}<path class="fig hl" d="M80 38 L82 70"/><circle cx="82" cy="72" r="3.5" fill="#C8963E"/></g>',
    "Kürek kemiği düzleminde kolları kaldırma")

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
 "isoer": ("Kapı pervazında dışa döndürme", "Ağrılı tarafınız kapı pervazına bakacak şekilde durun. Dirseğinizi 90 derece bükün, kolunuzu gövdenize yaslayın; araya katlanmış küçük bir havlu koyabilirsiniz. El sırtınızla pervaza doğru, kolunuz yer değiştirmeden itin. Ağrıyı artırmayan bir kuvvetle 30–45 saniye tutun.", "5 tekrar, günde 1–2 kez"),
 "sler": ("Yan yatarak dışa döndürme", "Ağrısız tarafınıza yan yatın. Üstteki kolunuzun dirseğini 90 derece bükün, dirseğinizi belinize yaslayın. Elinizdeki hafif ağırlığı (dolu bir su şişesi olabilir) dirseğiniz sabit kalacak şekilde tavana doğru kaldırın, yavaşça indirin.", "10–15 tekrar, 2–3 set"),
 "row": ("Lastik bantla kürek çekme", "Lastik bandı göğüs hizasında, kapıyı kapatarak kapı arasına sıkıştırın ya da sağlam bir yere bağlayın. Bandın uçlarını tutup dirseklerinizi gövdenize yakın tutarak geriye çekin, kürek kemiklerinizi birbirine yaklaştırın. Yavaşça başlangıca dönün.", "10–15 tekrar, 2–3 set"),
 "scaption": ("Kürek kemiği düzleminde kolları kaldırma", "Ayakta durun, kollarınız yanda, başparmaklarınız yukarı baksın. Kollarınızı tam yana değil, yandan yaklaşık 30 derece öne doğru (önünüzde geniş bir V oluşturacak şekilde) omuz hizasına kadar kaldırın; ellerinizde hafif birer ağırlık olabilir. Omuzlarınızı kulaklarınıza doğru kaldırmadan yavaşça indirin.", "10 tekrar, 2–3 set"),
 "wslide": ("Duvarda kaydırma", "Yüzünüz duvara dönük durun, ön kollarınızı omuz hizasında duvara yaslayın. Kollarınızı duvarda kaydırarak ağrısız aralıkta yukarı uzatın, kürek kemiklerinizin öne ve yukarı kaydığını hissedin. Yavaşça başlangıca dönün.", "10 tekrar, günde 1–2 kez"),
})

OMUZS_FAQ = [
 ("Omuz sıkışması ameliyatsız geçer mi?", "Çoğu kişide ameliyatsız tedaviyle belirgin düzelme olur; ancak bazı kişilerde şikâyetler aylarca sürebilir ya da tekrarlayabilir. İngiliz Omuz ve Dirsek Derneği'nin (BESS) 2025 bakım yoluna göre şikâyetlerin çoğu genellikle 3 ay içinde yanıt verir; 12 haftada düzelme olmazsa uzman değerlendirmesi öneriliyor. Yükü kademeli artırılan bir egzersiz programı tedavinin temelidir."),
 ("Ameliyat olmam gerekir mi?", "Çoğu zaman hayır. Kemik çıkıntısını tıraşlayan dekompresyon ameliyatı iki büyük çalışmada sahte ya da yalnızca tanısal ameliyattan üstün bulunmadı ve uluslararası bir uzman paneli bu ameliyatın yapılmamasını öneriyor. BESS de ameliyatı ilk basamak tedavi olarak önermiyor; 6 ay ameliyatsız tedaviye rağmen düzelmeyen bazı kişilerde düşünülebileceğini, ancak kimin yarar göreceğini belirleyen güvenilir bir ölçüt olmadığını belirtiyor. Düşme gibi bir travmadan sonra kolu kaldıramama varsa cerrahi değerlendirme ayrıca gerekir."),
 ("MR'ımda tendon yırtığı var, ne yapmalıyım?", "Yırtık görülmesi tek başına endişe nedeni değildir. Japon araştırmacıların bir köyde ultrasonla yaptığı toplum taramasında her beş kişiden birinde tam kat rotator manşet yırtığı bulundu ve bu yırtıkların üçte ikisi şikâyete yol açmıyordu. Tedavi kararı MR görüntüsüne değil, şikâyetlerinize ve muayene bulgularınıza göre verilir. Belirgin güç kaybı varsa ya da yırtık bir düşme veya darbe sonrasında oluştuysa hekiminiz cerrahi değerlendirme isteyebilir."),
 ("Kortizon iğnesi yaptırmalı mıyım?", "Kortizon iğnesi ağrıyı azaltabilir; ancak etkisi geçicidir (genellikle 12 haftadan kısa) ve egzersize eklenmesi uzun vadede ek bir fark yaratmadı. 2025 kılavuzları ilk basamak tedavi olarak önermiyor; tekrarlanan iğnelerin tek iğneye göre ek yararı gösterilmedi. Kararı hekiminizle birlikte verebilirsiniz."),
 ("MR ya da ultrason çektirmem gerekir mi?", "Çoğu zaman başlangıçta gerekmez; tanı öykü ve muayeneyle konur. JOSPT kılavuzuna göre yaklaşık 12 hafta düzgün yürütülen tedaviye rağmen düzelme yoksa ilk tercih ultrasondur ve MR rutin olarak önerilmez (uzman görüşü). BESS de görüntüleme gerekirse deneyimli kişinin yaptığı ultrasonu ilk tercih olarak görüyor. Darbe sonrasında, uyarı işaretleri varsa, ağrı ya da tutukluk çok şiddetliyse veya şikâyet uzun sürüyorsa röntgen istenebilir."),
 ("Omzum ağrırken spor yapabilir miyim?", "Evet, ağrıyı belirgin artırmayan sporlara devam edebilirsiniz. Yüzme, tenis, voleybol gibi kolun baş üstünde kullanıldığı sporları ağrı azalana kadar azaltın ve dönüşte yükü kademeli artırın."),
 ("Donuk omuzdan farkı nedir?", "Omuz sıkışmasında kolu başkası kaldırdığında hareket genellikle serbesttir ve ağrı belli bir açıda ortaya çıkar. Donuk omuzda ise omuz hem sizin hem de başkası kaldırdığında aynı şekilde kısıtlıdır. <a href=\"donuk-omuz.html\">Donuk omuz rehberine göz atın →</a>"),
]

OMUZS_SRC = [
 "Beard DJ, Rees JL, et al. " + ext("https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(17)32457-1/fulltext", "Arthroscopic subacromial decompression for subacromial shoulder pain (CSAW): a multicentre, pragmatic, parallel group, placebo-controlled, three-group, randomised surgical trial") + ". Lancet. 2018;391(10118):329-338. Özet: " + ext("https://evidence.nihr.ac.uk/alert/a-surgical-procedure-for-shoulder-pain-is-less-effective-than-previously-thought", "NIHR Evidence") + ".",
 "Desmeules F, Roy JS, Lafrance S, et al. " + ext("https://www.jospt.org/doi/10.2519/jospt.2025.13182", "Rotator cuff tendinopathy diagnosis, nonsurgical medical care, and rehabilitation: a clinical practice guideline") + ". J Orthop Sports Phys Ther. 2025;55(4):235-274. Özetler: " + ext("https://www.physiotutors.com/rotator-cuff-tendinopathy-the-new-2025-clinical-practice-guideline/", "Physiotutors") + "; " + ext("https://glennwellmanndpt.com/2025/10/27/rotator-cuff-tendinopathy-2025-clinical-practice-guideline-insights/", "Wellmann, 2025") + ".",
 "Karjalainen TV, Jain NB, Page CM, et al. " + ext("https://cochranelibrary.com/cdsr/doi/10.1002/14651858.CD005619.pub3/pdf/CDSR/CD005619/CD005619_abstract.pdf", "Subacromial decompression surgery for rotator cuff disease") + ". Cochrane Database Syst Rev. 2019;(1):CD005619.",
 "Ketola S, Lehtinen J, Arnala I, et al. " + ext("https://www.qxmd.com/r/19794168", "Does arthroscopic acromioplasty provide any additional value in the treatment of shoulder impingement syndrome? A two-year randomised controlled trial") + ". J Bone Joint Surg Br. 2009;91(10):1326-1334.",
 "Lewis J. Rotator cuff related shoulder pain: assessment, management and uncertainties. Man Ther. 2016;23:57-68.",
 "Minagawa H, Yamamoto N, Abe H, et al. " + ext("https://pmc.ncbi.nlm.nih.gov/articles/PMC3768248/", "Prevalence of symptomatic and asymptomatic rotator cuff tears in the general population: from mass-screening in one village") + ". J Orthop. 2013;10(1):8-12.",
 "Neer CS II. " + ext("https://shoulderdoc.co.uk/article/455", "Anterior acromioplasty for the chronic impingement syndrome in the shoulder") + ". J Bone Joint Surg Am. 1972;54:41-50.",
 "Paavola M, Malmivaara A, Taimela S, et al. " + ext("https://doi.org/10.1136/bmj.k2860", "Subacromial decompression versus diagnostic arthroscopy for shoulder impingement: randomised, placebo surgery controlled clinical trial") + ". BMJ. 2018;362:k2860.",
 "Paavola M, Kanto K, Ranstam J, et al. " + ext("https://bjsm.bmj.com/content/55/2/99", "Subacromial decompression versus diagnostic arthroscopy for shoulder impingement: a 5-year follow-up of a randomised, placebo surgery controlled clinical trial") + ". Br J Sports Med. 2021;55(2):99-107.",
 "Pandey RA, Singh HP; BESS Subacromial Pain Working Group. " + ext("https://bess.ac.uk/download/1463/subacromial-shoulder-pain/30248/subacromial-shoulder-pain-2025-2.pdf", "BESS patient care pathway: subacromial pain") + ". Shoulder Elbow. 2025;17(6):713-724.",
 "Physiopedia. " + ext("https://www.physio-pedia.com/Shoulder_Impingement", "Shoulder Impingement") + ".",
 "StatPearls. " + ext("https://www.ncbi.nlm.nih.gov/books/NBK554518/", "Shoulder Impingement Syndrome") + ". Treasure Island (FL): StatPearls Publishing.",
 "Steuri R, Sattelmayer M, Elsig S, et al. Effectiveness of conservative interventions including exercise, manual therapy and medical management in adults with shoulder impingement: a systematic review and meta-analysis of RCTs. Br J Sports Med. 2017;51(18):1340-1347.",
 "Vandvik PO, Lähdeoja T, Ardern C, et al. " + ext("https://www.bmj.com/content/364/bmj.l294", "Subacromial decompression surgery for adults with shoulder pain: a clinical practice guideline") + ". BMJ. 2019;364:l294.",
]

OMUZS_TL = [
 ("1972", "Cerrah Neer, omzun üstündeki kemik çatının (akromiyon) ön kısmının ve buraya tutunan bir bağın (korakoakromiyal bağ) omzu çeviren kasların tendonlarına sürtündüğünü öne sürdü. Bunun kendine özgü bir tablo (sıkışma sendromu) oluşturduğunu yazdı ve tedavi olarak kemik çatının ön kenarının ve alt yüzünün bu bağla birlikte alınmasını önerdi."),
 ("2009", "140 hastayla yapılan randomize çalışmada, kemik çatıyı tıraşlayan ameliyat ve ardından egzersiz, yalnızca gözetimli egzersiz programına 2 yılda ağrı açısından ek bir yarar sağlamadı; maliyeti ise belirgin şekilde yüksekti."),
 ("2016", "Bir derleme makalesinde \"rotator manşetle ilişkili omuz ağrısı\" adı kullanıldı. Bu ad, ağrıyı tek bir mekanik \"sıkışma\"ya bağlamadan tanımlıyor."),
 ("2018", "Birleşik Krallık'ta 32 hastanede 313 hastayla yapılan CSAW çalışmasında dekompresyon ameliyatı, yalnızca eklemin içine kamerayla bakılan sahte (plasebo) ameliyattan 6. ayda ve 1. yılda klinik olarak anlamlı bir fark göstermedi."),
 ("2018", "Finlandiya'da üç hastanede 210 hastayla yapılan FIMPACT çalışmasında dekompresyon ameliyatı, yalnızca tanı amaçlı yapılan artroskopiden 2 yılda daha iyi sonuç vermedi. 2021'de yayımlanan 5 yıllık sonuçlar da aynıydı: ameliyat ne sahte ameliyata ne de egzersize üstündü."),
 ("2019", "8 çalışmayı ve 1.062 kişiyi inceleyen Cochrane derlemesi, dekompresyon ameliyatının sahte ameliyata göre ağrı, işlev ve yaşam kalitesinde klinik olarak önemli bir yarar sağlamadığını yüksek kesinlikte gösterdi. Aynı yıl uluslararası bir uzman paneli (BMJ) bu ameliyatın yapılmamasını güçlü şekilde önerdi."),
 ("2025", "İki yeni kaynak yayımlandı: uluslararası bir uzman grubunun hazırladığı ve Amerikan Fizyoterapi Derneği'nin (APTA) ortopedi akademisinin de desteklediği kılavuz (JOSPT) ile İngiliz Omuz ve Dirsek Derneği'nin (BESS) hasta bakım yolu. İkisi de tedavinin ilk basamağına egzersizi koyuyor."),
]

OMUZS_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Omuz sıkışması (subakromiyal ağrı)</h1>
    <p class="lede">Kolu yana ya da yukarı kaldırırken omzun dış yüzünde, bazen kola doğru yayılan ağrıyla kendini gösterir. Eskiden kemiklerin arasında bir "sıkışma" olduğu düşünülen bu tabloda bugün omzu çeviren kasların (rotator manşet) tendonları ve çevresindeki yapılar öne çıkıyor. Tedavinin temeli egzersizdir; ameliyat çoğu zaman gerekmez.</p>
    <p class="meta">Son güncelleme: 31 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%44–65</b><span>Omuz ağrısı şikâyetleri içinde subakromiyal ağrının payı</span></div>
        <div class="stat"><b>%22</b><span>Toplum taramasında tam kat tendon yırtığı bulunan kişi; bu yırtıkların üçte ikisi şikâyetsiz</span></div>
        <div class="stat"><b>5 yıl</b><span>Takipte dekompresyon ameliyatı, sahte ameliyattan ve egzersizden daha iyi değildi</span></div>
        <div class="stat"><b>3 ay</b><span>Şikâyetlerin çoğunun yanıt vermesinin beklendiği süre (BESS)</span></div>
      </div>
      {g_toc([("nedir", "Nedir?"), ("tani", "Nasıl tanınır?"), ("mr", "MR'daki yırtık"), ("tarihce", "Geçmişten bugüne"), ("tedavi", "Tedavi seçenekleri"), ("egzersizler", "Egzersizler"), ("gunluk", "Günlük hayatta"), ("videolar", "Videolar"), ("sss", "Sık sorulan sorular"), ("uyari", "Uyarı işaretleri")])}
    </div>
  </section>

  <section id="nedir">
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Omzun üstündeki kemik çatı (akromiyon) ile kol kemiği arasında kalan dar alana subakromiyal alan denir. Burada omzu çeviren kasların (rotator manşet) tendonları ve bir kese (bursa) bulunur. Bu yapıların aşırı ya da alışık olunmayan yüklenmesi ağrıya yol açabilir.</p>
        <p class="soft">Eskiden tendonun kemiğe "sıkıştığı" düşünülürdü. Bugün ağrının çoğu zaman tek bir mekanik sıkışmayla açıklanamayacağı, tendonun yüklenmeye verdiği yanıtın da rol oynadığı düşünülüyor; bu yüzden "subakromiyal ağrı" ya da "rotator manşetle ilişkili omuz ağrısı" adları da kullanılıyor.</p>
      </div>
      <div>
        <h2>Belirtiler ve risk etkenleri</h2>
        <ul class="dots">
          <li>Kolu yana ya da öne kaldırırken belli bir açıda artan ağrı</li>
          <li>Omzun dış yüzüne, bazen dirseğe kadar yayılan ağrı</li>
          <li>Ağrılı tarafa yatınca ve geceleri artan ağrı</li>
          <li>Saç tarama, yüksek rafa uzanma, ceket giyme gibi işlerde zorlanma</li>
          <li>Risk etkenleri: yaşın ilerlemesi (en sık 50'li yaşlarda), kolun baş hizasının üstünde tekrarlı ya da uzun süre kullanıldığı işler ve sporlar</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="tani">
    <div class="wrap">
      <h2>Nasıl tanınır?</h2>
      <p class="soft">Omuz sıkışması bir muayene tanısıdır: öykü ve muayeneyle konur, tanıyı doğrulamak ya da tedaviye başlamak için görüntüleme gerekmez. Muayenede boyun da değerlendirilir; çünkü boyundan kaynaklanan ağrı omuza yansıyabilir.</p>
      <div class="kinds">
        <div class="kind"><h3>Muayene testleri</h3><p>Kolu yana kaldırırken belli bir açı aralığında ağrı olması (ağrılı ark) tanıyı destekler. Hawkins-Kennedy testinde (kol öne kaldırılıp dirsek bükülüyken içe döndürülür) ağrı olmaması ise omuz sıkışması olasılığını azaltır. Tek bir test tek başına yeterli değildir; testler birlikte yorumlanır.</p></div>
        <div class="kind"><h3>Görüntüleme ne zaman?</h3><p>İlk değerlendirmede genellikle gerekmez. Görüntüleme gerekirse ilk tercih ultrasondur; JOSPT kılavuzu bunu yaklaşık 12 hafta düzgün yürütülen tedaviye rağmen düzelme olmayanlar için öneriyor ve MR'ı rutin olarak önermiyor. Darbe sonrasında, uyarı işaretlerinde, ağrı ya da tutukluk çok şiddetliyse veya şikâyet uzun sürüyorsa röntgen istenebilir.</p></div>
        <div class="kind"><h3>Başka ne olabilir?</h3><p>Omuz ağrısının başka nedenleri de vardır: donuk omuz, tendonda kireç birikmesi, omuz kireçlenmesi, büyük tendon yırtıkları, omuz çıkığı ya da gevşekliği ve boyun kaynaklı ağrı. Muayene bu nedenleri ayırmaya yardım eder.</p><a href="omuzda-kirec-birikmesi.html">Omuzda kireç birikmesi →</a></div>
      </div>
    </div>
  </section>

  <section id="mr">
    <div class="wrap">
      <h2>MR'daki yırtık her zaman ağrının nedeni mi?</h2>
      <p class="soft">Japon araştırmacıların bir köyde 664 kişiyi ultrasonla taradığı çalışmada her beş kişiden birinde (%22,1) tam kat rotator manşet yırtığı bulundu ve bu yırtıkların üçte ikisi şikâyete yol açmıyordu. Yırtık görülme sıklığı yaşla artıyor: 50'li yaşlarda %10,7 iken 80'li yaşlarda %36,6'ya çıkıyor.</p>
      <div class="callout">
        <p>Yani MR'da tendon yıpranması ya da küçük bir yırtık görülmesi, ağrının tek nedeni olduğu ya da ameliyat gerektiği anlamına gelmez. Karar, şikâyetleriniz ve muayene bulgularınızla birlikte verilir.</p>
      </div>
    </div>
  </section>

  <section id="tarihce">
    <div class="wrap">
      <p class="eyebrow">Geçmişten bugüne</p>
      <h2>"Sıkışma" fikrinden egzersize</h2>
      <p class="soft">Yaklaşık yarım yüzyıl boyunca omuz ağrısının nedeni olarak kemiğin tendona sürtünmesi görüldü ve kemiği tıraşlayan ameliyat yaygın olarak yapıldı. Sahte ameliyatla karşılaştırılan çalışmalar bu yaklaşımı ciddi şekilde sorgulattı.</p>
      {g_tl(OMUZS_TL)}
    </div>
  </section>

  <section id="tedavi">
    <div class="wrap">
      <h2>Seyri ve tedavi</h2>
      <p class="soft">Kılavuzlar tedavinin merkezine egzersizi koyuyor; diğer yöntemler egzersizi yapılabilir kılmak için destek olarak kullanılır. İngiliz Omuz ve Dirsek Derneği'nin (BESS) 2025 bakım yoluna göre bu tablo çoğu zaman kendiliğinden sınırlanma eğilimindedir ve şikâyetlerin çoğu 3 ay içinde yanıt verir; 12 haftada düzelme olmazsa uzman değerlendirmesi öneriliyor.</p>
      <ul class="tx">
        <li><b>Bilgilendirme</b><span>Ağrının ne olduğunu, nasıl seyredeceğini ve günlük işlerin nasıl ayarlanacağını öğrenmek tedavinin parçasıdır.</span></li>
        <li><b>Egzersiz</b><span>Tedavinin temelidir. Omuz ve kürek kemiği kaslarını güçlendiren, yükü kademeli artırılan bir program ağrıyı azaltır ve işlevi iyileştirir. Sonuç için programın haftalarca, düzenli sürdürülmesi gerekir. En iyi egzersiz türü ve dozu henüz belli değil; program kişiye göre ayarlanır.</span></li>
        <li><b>Manuel terapi ve bantlama</b><span>Manuel terapi, egzersizle birlikte kısa süreli ağrı azaltmak için kullanılabilir. Bantlamanın yararı konusunda çalışmalar çelişkilidir; kısa süreli ek destek olarak denenebilir. İkisi de tek başına tedavi değildir.</span></li>
        <li><b>Şok dalga, lazer ve ultrason tedavisi</b><span>Şok dalga ve lazer daha çok tendonda kireç birikmesi olan kişilerde düşünülebilir (zayıf öneri); kireç yoksa şok dalga önerilmiyor. Ultrason tedavisi yarar göstermediği için önerilmiyor. <a href="omuzda-kirec-birikmesi.html">Omuzda kireç birikmesi →</a></span></li>
        <li><b>Kortizon iğnesi</b><span>Ağrıyı geçici olarak (genellikle 12 haftadan kısa) azaltabilir; uzun vadeli yararı yoktur ve ilk basamak tedavi olarak önerilmez. Kararı hekiminizle birlikte verebilirsiniz.</span></li>
        <li><b>Günlük yükü ayarlamak</b><span>Ağrıyı belirgin artıran baş üstü işleri geçici olarak azaltmak, omzu tamamen dinlendirmeden iyileşmeye zaman tanır.</span></li>
        <li><b>Ameliyat</b><span>Kemik çıkıntısını tıraşlayan dekompresyon ameliyatı, Birleşik Krallık'taki CSAW ve Finlandiya'daki FIMPACT çalışmalarında sahte ya da yalnızca tanısal ameliyattan üstün bulunmadı. Finlandiya'daki çalışmanın 5 yıllık sonuçları da aynıydı. Uluslararası bir uzman paneli bu ameliyatın yapılmamasını güçlü şekilde öneriyor. Travmaya bağlı büyük tendon yırtıklarında cerrahi değerlendirme ayrıdır.</span></li>
      </ul>
      <h3 class="g-h3">Tedavi seçenekleri: kılavuzlar ne diyor?</h3>
      <p class="soft">2025'te yayımlanan iki kaynak yan yana: uluslararası bir uzman grubunun JOSPT'de yayımlanan, ameliyat dışı tedavi kılavuzu ve İngiliz Omuz ve Dirsek Derneği'nin (BESS) hasta bakım yolu. Parantez içindeki harfler JOSPT kılavuzundaki öneri düzeyidir (A güçlü, B orta, C zayıf). JOSPT kılavuzunun ayrıntıları ikincil özetlerden alındı; tedavi kişiye göre seçilir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Görüntüleme</h3><dl><dt>JOSPT</dt><dd>İlk değerlendirmede gerekmez; 12 hafta ameliyatsız tedaviye rağmen düzelme yoksa ilk tercih ultrason, MR rutin değil (uzman görüşü).</dd><dt>BESS</dt><dd>Tanı için gerekmez; gerekirse deneyimli kişinin yaptığı ultrason ilk tercih; darbe sonrası, uyarı işaretlerinde, ağrı ya da tutukluk çok şiddetliyse veya şikâyet uzun sürüyorsa röntgen.</dd></dl></div>
        <div class="kind"><h3>Egzersiz</h3><dl><dt>JOSPT</dt><dd>Tedavinin temeli (A): kademeli direnç ve hareket kontrolü egzersizleri, ağrı toleransına ve hedeflere göre.</dd><dt>BESS</dt><dd>İlk basamak tedavi; programın 3 ay içinde belirgin düzelme sağlaması beklenir. En iyi egzersiz türü, dozu ve süresi belirsiz.</dd></dl></div>
        <div class="kind"><h3>Manuel terapi</h3><dl><dt>JOSPT</dt><dd>Egzersizle birlikte kısa süreli ağrı azaltmak için (B).</dd><dt>BESS</dt><dd>Başlangıç döneminde önerilebilir.</dd></dl></div>
        <div class="kind"><h3>Kortizon iğnesi</h3><dl><dt>JOSPT</dt><dd>İlk basamak değil; kısa süreli ağrı için, ultrason eşliğinde yapılması tercih edilir.</dd><dt>BESS</dt><dd>Etkisi geçici (12 haftadan kısa); 6–8 haftada düzelme yoksa ortak kararla tek iğne düşünülebilir. Tekrarlı iğnenin ek yararı yok; ultrason eşliğinde yapmanın belirgin bir üstünlüğü bulunmadı.</dd></dl></div>
        <div class="kind"><h3>Şok dalga, lazer, ultrason tedavisi</h3><dl><dt>JOSPT</dt><dd>Şok dalga ve lazer kireç birikmesinde (C); kireç yoksa şok dalga önerilmiyor; ultrason tedavisi önerilmiyor.</dd><dt>BESS</dt><dd>Şok dalga ve ultrason tedavisinin önemli bir etkisi yok; lazerin küçük ve kısa süreli etkisi var. İkinci basamakta (uzman hekim değerlendirmesinde), yarar kanıtının düşük olduğu anlatılarak düşünülebilir.</dd></dl></div>
        <div class="kind"><h3>Akupunktur ve kuru iğneleme</h3><dl><dt>JOSPT</dt><dd>Akupunktur, aktif rehabilitasyonla birlikte kısa süreli ek yarar sağlayabilir (C).</dd><dt>BESS</dt><dd>Kuru iğnelemenin önemli bir etkisi yok; akupunktur için kanıt yetersiz.</dd><dt>Not</dt><dd>Türkiye'de yalnızca yetkili hekimler uygulayabilir.</dd></dl></div>
        <div class="kind"><h3>PRP ve hyaluronik asit iğnesi</h3><dl><dt>JOSPT</dt><dd>İlk basamak değil; diğer tedavilere yanıt vermeyenlerde düşünülebilir; kanıt çelişkili ya da uzman görüşüne dayanıyor.</dd><dt>BESS</dt><dd>Kanıt çok düşük; ikinci basamakta (uzman hekim değerlendirmesinde), yarar kanıtının düşük olduğu anlatılarak düşünülebilir.</dd></dl></div>
        <div class="kind"><h3>Ameliyat</h3><dl><dt>BESS</dt><dd>İlk basamak değil; sahte ameliyattan belirgin üstün değil. 6 ay ameliyatsız tedaviye rağmen düzelmeyenlerde düşünülebilir; hasta seçimi için güvenilir ölçüt yok.</dd><dt>BMJ uzman paneli (2019)</dt><dd>Dekompresyon ameliyatına karşı güçlü öneri.</dd><dt>JOSPT</dt><dd>Kılavuz ameliyat dışı tedaviyi kapsıyor.</dd></dl></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Omuz için altı egzersiz</h2>
      <p class="soft">Ağrısız ya da hafif ağrılı bir aralıkta başlayın ve yükü omzunuzun kaldırabildiği ölçüde kademeli artırın. Egzersiz sırasında hafif ve katlanılabilir bir ağrı olabilir; ağrı ertesi gün başlangıç düzeyine dönüyorsa devam edebilirsiniz. İlk iki hareket ağrılı dönemde de uygundur. Kolu kaldırdığınız hareketlerde ağrı artıyorsa hareket aralığını küçültün.</p>
      {ex_grid(["scap2", "isoer", "sler", "row", "scaption", "wslide"])}
    </div>
  </section>

  <section id="gunluk">
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

  <section id="sss">
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(OMUZS_FAQ)}
    </div>
  </section>

  <section id="uyari">
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Omuz ağrısı her zaman omuz sıkışması değildir. Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Düşme ya da darbeden sonra kolu kaldıramama, omuzda şekil bozukluğu</li>
        <li>Omuzda kızarıklık, şişlik ya da sıcaklık; özellikle ateş eşlik ediyorsa (enfeksiyon olabilir)</li>
        <li>Boyundan kola yayılan ağrı, kolda uyuşma ya da karıncalanma</li>
        <li>Kolda ya da yüzde aniden başlayan güç kaybı ya da uyuşma, konuşma bozukluğu (inme olabilir, <strong>112</strong>'yi arayın)</li>
        <li>Özellikle sol omuz ağrısına göğüs ağrısı, nefes darlığı ya da terleme eşlik ediyorsa (kalp kaynaklı olabilir, <strong>112</strong>'yi arayın)</li>
        <li>Nedensiz kilo kaybı, dinlenmekle geçmeyen şiddetli gece ağrısı ya da kanser öyküsü</li>
        <li>Omuzda ele gelen kitle ya da şişlik</li>
        <li>Birden fazla eklemde ağrı ve şişlik</li>
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
     "Omuz sıkışması (subakromiyal ağrı, rotator manşet tendiniti) nedir, nasıl tanınır, MR'daki yırtık önemli mi, ameliyat gerekir mi? 2025 kılavuzlarının karşılaştırması, kısa tarihçe, evde altı egzersiz, videolar ve uyarı işaretleri.",
     "omuz-sikismasi.html", NECK_CSS, OMUZS_BODY, YT_JS,
     seo_title="Omuz Sıkışması (Subakromiyal Ağrı): Egzersizler ve Tedavi | İhsan Eren",
     condition="Omuz sıkışması (subakromiyal ağrı sendromu)", about=cond("Omuz sıkışması (subakromiyal ağrı sendromu)"),
     faq_items=pick(OMUZS_FAQ, 0, 1, 2, 3))

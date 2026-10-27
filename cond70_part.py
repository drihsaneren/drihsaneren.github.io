# -*- coding: utf-8 -*-
# Yeni rehber (70): Koşucu dizi (iliotibial bant sendromu). self14_part.py'den sonra exec edilir. Video yok.
# Kaynaklar (24 Ekim 2026'da okundu): van der Worp 2012 Sports Med (UMC Utrecht özeti), Aderem & Louw 2015 BMC MSD (Stellenbosch deposu), Fairclough 2006 J Anat (Cardiff deposu),
# Fredericson 2000 Clin J Sport Med (WUSTL özeti), Sanchez-Alvarado 2024 Front Sports Act Living (tam metin), Gunter & Schwellnus 2004 BJSM (özet), Nielsen 2014 JOSPT (AAU özeti),
# Bupa ITB syndrome (BMJ Best Practice Mayıs 2026'ya dayanıyor).

_ex2("it_abd", "abd", "Yan yatarak bacak kaldırma", "Ağrımayan tarafınıza yan yatın, alttaki dizinizi hafifçe bükün. Üstteki bacağınızı düz ve hafifçe geride tutarak, ayak ucunuz öne bakacak şekilde yavaşça kaldırın ve indirin. Kalçanızın yanında yanma hissetmelisiniz.", "10–15 tekrar, 3 set; her iki taraf")
_ex2("it_side", "sideplank", "Dizler üzerinde yan köprü", "Yan yatın, dirseğiniz omzunuzun altında, dizleriniz bükülü olsun. Kalçanızı yerden kaldırarak başınızdan dizinize kadar düz bir çizgi oluşturun ve tutun. Kolaylaşınca dizlerinizi düzeltip ayaklarınız üzerinde yapın.", "20–30 saniye, 3 kez; her iki taraf")
_ex2("it_bridge", "bridge", "Köprü", "Sırtüstü uzanın, dizleriniz bükülü, ayaklarınız yerde. Kalçanızı sıkarak kaldırın, kısa bir süre tutun ve yavaşça indirin. Kolaylaşınca tek bacak üzerinde yapın.", "10–15 tekrar, 3 set")
_ex2("it_sls", "sls", "Tek ayak üzerinde durma", "Tek ayağınızın üzerinde durun. Leğen kemiğinizi düz tutun, dizinizin içe kaçmasına izin vermeyin. Gerekirse bir tezgâha hafifçe tutunun; kolaylaşınca gözlerinizi kapatın ya da yumuşak bir zeminde deneyin.", "30 saniye, her ayakla 3 kez")
_ex2("it_wall", "wall", "Duvarda yarım çömelme", "Sırtınızı duvara dayayın, ayaklarınız kalça genişliğinde olsun. Dizleriniz ikinci parmağınızın üzerinden geçecek şekilde, ağrısız bir derinliğe kadar inip kalkın. Dizlerinizin içe kaçmamasına dikkat edin.", "10–15 tekrar, 3 set")
_ex2("it_walk", "walk", "Yürüyüşten koşuya dönüş", "Ağrısız yürüyebildiğinizde, düz zeminde kısa koşu bölümlerini yürüyüşle değiştirerek başlayın. Ağrının başladığı noktadan önce durun; yokuş aşağı koşuyu en sona bırakın.", "Her seansta koşu bölümlerini az az artırın; gün aşırı")

ITB_FAQ = [
 ("Koşmayı tamamen bırakmam gerekiyor mu?", "Çoğu zaman gerekmez, ama yükü azaltmanız gerekir. Bir İngiliz sağlık kuruluşunun bilgilendirme sayfası, ağrı hafifse koşuyu ağrının genellikle başladığı noktadan önce bitirmeyi, şiddetliyse ağrıya yol açan etkinliği bir süre tamamen bırakmayı öneriyor. Bu sürede yüzme ya da ağrı yapmayan başka egzersizlerle formunuzu koruyabilirsiniz."),
 ("Germe ya da köpük rulo işe yarar mı?", "Rahatlatıcı gelebilir ama iliotibial bandı uzatmaz. 13 çalışmayı inceleyen bir derlemede, germenin bandın uzunluğunu değiştirdiğine dair kanıt bulunmadı. Bant, uyluk kemiğine sıkıca tutunan kalın bir bağ dokusu şeridi; en çok kanıt kalça kaslarını güçlendirmeye dayalı programlarda var."),
 ("İğne (kortizon) yaptırmalı mıyım?", "Kısa süreli rahatlama sağlayabilir. Yeni başlamış yakınması olan 18 koşucuyla yapılan küçük bir çalışmada, bölgeye yapılan kortizon iğnesi ilk iki haftada koşu sırasındaki ağrıyı yalnızca uyuşturucu ilaç yapılanlara göre daha çok azalttı. Uzun dönem etkisi bilinmiyor; iğne, yükü ayarlama ve güçlendirme programının yerine geçmez. Bu kararı hekiminizle birlikte verin."),
 ("Ne kadar sürede düzelir?", "Çoğu kişi 6–8 hafta içinde koşuya dönebiliyor. Kalça kaslarını güçlendirmeye odaklanan 6 haftalık bir programın sonunda 24 koşucunun 22'si ağrısız koşuya döndü ve 6 ay sonra yakınma tekrarlamadı; ancak bu, kontrol grubu olmayan küçük bir çalışmaydı. Ağrınız uzun süredir varsa iyileşme daha uzun sürebilir."),
 ("Ayakkabı değiştirmek gerekir mi?", "Eskimiş ayakkabılar risk etkenleri arasında sayılıyor. Fizyoterapistiniz koşu şeklinize bakarak ayakkabı ya da koşu tekniğinde değişiklik önerebilir. Koşu tekniğini değiştirmeye yönelik kanıt şimdilik birkaç olgu sunumuyla sınırlı."),
 ("Ameliyat gerekir mi?", "Nadiren. Ameliyat yalnızca aylarca süren uygun tedaviye rağmen geçmeyen yakınmalarda düşünülür. Koşucularda iliotibial bant sendromunun tedavisini inceleyen çalışmaların kalitesi genel olarak düşük; bu yüzden önce yük yönetimi ve egzersiz denenir."),
]

ITB_SRC = [
 "van der Worp MP, van der Horst N, de Wijer A, et al. " + ext("https://researchinformation.umcutrecht.nl/en/publications/iliotibial-band-syndrome-in-runners-a-systematic-review/", "Iliotibial band syndrome in runners: a systematic review") + ". Sports Med. 2012;42(11):969–992.",
 "Aderem J, Louw QA. " + ext("https://scholar.sun.ac.za/items/c39ebbbc-5853-4ab3-a8e4-8d9a1c5ff470/full", "Biomechanical risk factors associated with iliotibial band syndrome in runners: a systematic review") + ". BMC Musculoskelet Disord. 2015;16:356.",
 "Fairclough J, Hayashi K, Toumi H, et al. " + ext("https://orca.cardiff.ac.uk/id/eprint/29611/", "The functional anatomy of the iliotibial band during flexion and extension of the knee: implications for understanding iliotibial band syndrome") + ". J Anat. 2006;208(3):309–316.",
 "Fredericson M, Cookingham CL, Chaudhari AM, et al. " + ext("https://profiles.wustl.edu/en/publications/hip-abductor-weakness-in-distance-runners-with-iliotibial-band-sy/", "Hip abductor weakness in distance runners with iliotibial band syndrome") + ". Clin J Sport Med. 2000;10(3):169–175.",
 "Sanchez-Alvarado A, Bokil C, Cassel M, Engel T. " + ext("https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2024.1386456/full", "Effects of conservative treatment strategies for iliotibial band syndrome on pain and function in runners: a systematic review") + ". Front Sports Act Living. 2024;6:1386456.",
 "Gunter P, Schwellnus MP. " + ext("https://bjsm.bmj.com/content/38/3/269", "Local corticosteroid injection in iliotibial band friction syndrome in runners: a randomised controlled trial") + ". Br J Sports Med. 2004;38(3):269–272.",
 "Nielsen RØ, Parner ET, Nohr EA, et al. " + ext("https://vbn.aau.dk/da/publications/excessive-progression-in-weekly-running-distance-and-risk-of-runn", "Excessive progression in weekly running distance and risk of running-related injuries: an association which varies according to type of injury") + ". J Orthop Sports Phys Ther. 2014;44(10):739–747.",
 "Bupa UK. " + ext("https://www.bupa.co.uk/health-information/knee-pain/ilio-tibial-band-itb-friction-syndrome", "Iliotibial band (ITB) syndrome") + ". BMJ Best Practice'e (Mayıs 2026) dayanarak hazırlanmış hasta bilgisi.",
]

ITB_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Koşucu dizi (iliotibial bant sendromu)</h1>
    <p class="lede">Koşarken dizin dış yanında başlayan, çoğu zaman koşunun aynı dakikasında ortaya çıkan ve durunca hafifleyen ağrı, sıklıkla iliotibial bant sendromundan kaynaklanır. Koşucularda dizin dış yanındaki en sık yakınmadır. Bu rehber ağrının nedenini, neden ortaya çıktığını, nasıl tedavi edildiğini ve koşuya güvenle nasıl dönebileceğinizi anlatıyor.</p>
    <p class="meta">Son güncelleme: 24 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%5–14</b><span>Koşucularda iliotibial bant sendromu görülme sıklığı (sistematik derleme)</span></div>
        <div class="stat"><b>2.</b><span>Koşucularda diz önü ağrısından sonra en sık görülen diz ağrısı</span></div>
        <div class="stat"><b>22/24</b><span>6 haftalık kalça güçlendirme programından sonra ağrısız koşuya dönen koşucu (küçük, kontrolsüz çalışma)</span></div>
        <div class="stat"><b>6–8 hafta</b><span>Çoğu kişinin koşuya dönebildiği süre</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Ağrı nereden geliyor?</h2>
        <p class="soft">İliotibial bant, kalçanın dış yanından dizin dış yanına uzanan kalın bir bağ dokusu şerididir. Uzun yıllar bandın dizdeki kemik çıkıntısına sürtünmesiyle ağrı oluştuğu düşünüldü. Kadavra ve MR çalışmaları ise bandın uyluk kemiğine sıkıca tutunduğunu ve kemik üzerinde gerçekten kaymadığını gösterdi. Ağrının, dizin yaklaşık 30 derece büküldüğü anda bandın altındaki sinir ve damardan zengin yağ dokusunun sıkışmasından kaynaklanabileceği düşünülüyor.</p>
        <ul class="dots">
          <li>Dizin dış yanında keskin ya da sızlayan ağrı; bazen yukarı ya da aşağı yayılır.</li>
          <li>Ağrı çoğu zaman koşunun hep aynı noktasında başlar ve durunca azalır.</li>
          <li>Yokuş aşağı koşmak ve her zamankinden uzun koşmak ağrıyı artırır.</li>
          <li>İlerlerse yürürken ya da dizi bükülü otururken de ağrı olabilir.</li>
        </ul>
      </div>
      <div>
        <h2>Neden ortaya çıkar?</h2>
        <p class="soft">Aşırı kullanım yaralanmasıdır; en sık koşucularda ve bisikletçilerde görülür. Nedenlerine ilişkin kanıt sınırlı ve çelişkili, ama öne çıkan etkenler şunlar:</p>
        <ul class="dots">
          <li><b>Yükün hızla artması:</b> Yeni başlayan 874 koşucunun izlendiği bir çalışmada, haftalık mesafesini iki haftada %30'dan fazla artıranlarda bu sendromun da aralarında olduğu mesafeyle ilişkili sakatlıklar daha sık görüldü; fark istatistiksel anlamlılık sınırındaydı.</li>
          <li><b>Kalça ve diz hareketleri:</b> 13 çalışmayı birleştiren bir derlemede, bu sendrom gelişen kadın koşucularda koşarken kalçanın içe kaçması, dizin içe dönmesi ve gövdenin yana eğilmesi daha fazlaydı.</li>
          <li><b>Kalça kaslarında zayıflık:</b> Sendromu olan koşucularda ağrılı taraftaki kalçayı yana açan kasların daha güçsüz olduğu gösterildi; ama bunun neden mi sonuç mu olduğu net değil.</li>
          <li><b>Diğerleri:</b> Eskimiş ayakkabılar, kaygan ya da eğimli zemin ve uzun yokuş aşağı koşular.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <ul class="tx">
        <li><b>Yükü ayarlayın</b><span>Ağrı hafifse koşuyu ağrının başladığı noktadan önce bitirin; şiddetliyse ağrıya yol açan etkinliği bir süre bırakın ve ağrısız bir egzersizle formunuzu koruyun.</span></li>
        <li><b>İlk günler</b><span>Bez sarılmış buz ya da soğuk kompresi 15–20 dakika, birkaç saatte bir uygulayabilirsiniz. Ağrı kesici kullanmak isterseniz hekiminize danışın.</span></li>
        <li><b>Güçlendirme</b><span>Araştırmalarda en sık kullanılan ve en tutarlı sonuç veren yaklaşım kalçayı yana açan kasları güçlendirmek. 13 çalışmayı inceleyen 2024 tarihli bir derlemede, güçlendirme tek başına ya da manuel tedavi veya şok dalga tedavisiyle birlikte uygulandığında 2–8 haftada ağrının belirgin azaldığı görüldü.</span></li>
        <li><b>İğne</b><span>Yeni başlamış yakınmalarda kortizon iğnesi ilk iki haftada ağrıyı azaltabilir; uzun dönem etkisi bilinmiyor.</span></li>
        <li><b>Ameliyat</b><span>Nadiren, aylarca süren uygun tedaviye rağmen geçmeyen yakınmalarda düşünülür.</span></li>
      </ul>
      <div class="callout">
        <p>Bu sendromun tedavisini inceleyen çalışmalar küçük ve kalitesi genel olarak düşük. Bu yüzden önerilerin çoğu, kanıtın en güçlü olduğu yük yönetimi ve kalça güçlendirmesine dayanıyor.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Koşucu dizi için altı egzersiz</h2>
      <p class="soft">Bu hareketler kalçayı yana açan kasları ve koşu sırasında leğen kemiği ile dizin kontrolünü güçlendirmeye yöneliktir. Tekrar sayıları genel önerilerdir. Hareketler hafif bir zorlanma hissi yaratabilir, ama dizin dış yanındaki ağrıyı artırmamalı.</p>
      {ex_grid(["it_abd", "it_side", "it_bridge", "it_sls", "it_wall", "it_walk"])}
      <p class="soft" style="margin-top:14px">Egzersiz sırasındaki ağrıyı yorumlamak için <a href="egzersizde-agri.html">egzersizde ağrı trafik ışığına</a>, kalça ve diz kontrolü için <a href="denge-antrenmani.html">denge antrenmanına</a> bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(ITB_FAQ)}
      <p class="soft" style="margin-top:18px">Dizin ön tarafındaki ağrı için <a href="diz-onu-agrisi.html">diz önü ağrısı</a>, kalçanın yan tarafındaki ağrı için <a href="kalca-yan-agrisi.html">kalça yan ağrısı</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Düşme, burkulma ya da darbe sonrası başlayan ağrı ve şişlik</li>
        <li>Dizde kilitlenme, boşalma ya da belirgin şişlik</li>
        <li>Ateş, kızarıklık, sıcaklık ya da dinlenirken ve gece süren ağrı</li>
        <li>Birkaç haftalık yük ayarlaması ve egzersize rağmen düzelmeyen ağrı</li>
      </ul>
      {CTA_CARD("Koşucu dizi ve koşuya dönüş", "koşucu dizi (iliotibial bant sendromu) ve koşuya dönüş programı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(ITB_SRC)}
    </div>
  </section>
</main>'''

page("kosucu-dizi.html", "Koşucu Dizi (İliotibial Bant Sendromu)",
     "Koşucu dizi (iliotibial bant sendromu): dizin dış yanındaki ağrının nedeni, risk etkenleri, tedavi, kalça güçlendirme egzersizleri ve koşuya güvenli dönüş.",
     "kosucu-dizi.html", NECK_CSS, ITB_BODY, "",
     seo_title="Koşucu Dizi (İliotibial Bant Sendromu): Nedenleri, Tedavi ve Egzersizler | İhsan Eren",
     condition="İliotibial bant sendromu", faq_items=ITB_FAQ)

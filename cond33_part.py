# -*- coding: utf-8 -*-
# Yeni rehber (33): Boyun tutulması (akut tortikolis). cond32_part.py'den sonra exec edilir. Video yok.
# Yeni çizim: başı öne-arkaya yavaşça eğme. Diğerleri boyun rehberindeki çizimler.

SV["bt_nod"] = fig(GRD +
    '<path class="fig" d="M58 40 V80 M58 80 L54 112 M58 80 L62 112 M58 44 L60 66 L67 75"/>'
    f'<g>{anim_t("0 58 40;22 58 40;0 58 40;-14 58 40;0 58 40", dur="5.6s", kt="0;0.25;0.5;0.75;1", typ="rotate")}'
    '<path class="fig hl" d="M58 40 L60 30"/>' + FACE_SIDE + '</g>'
    '<path d="M86 14 Q94 26 86 38 M82 16 L86 14 L88 18 M82 36 L86 38 L88 34" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "Başı öne ve arkaya eğme")

_ex2("bt_rot", "rot", "Yavaşça sağa sola bakma", "Dik oturun, omuzlarınızı sabit tutun. Başınızı ağrının izin verdiği kadar yavaşça bir yana çevirin, 2–3 saniye bekleyin, sonra öbür yana çevirin. Her gün biraz daha uzağa bakmaya çalışın.", "Her yöne 5–10 tekrar, birkaç saatte bir")
_ex2("bt_side", "side", "Kulağı omza yaklaştırma", "Dik oturun. Kulağınızı yavaşça aynı taraftaki omzunuza doğru yaklaştırın; omzunuzu kaldırmayın. Rahat olan son noktada birkaç saniye bekleyip ortaya dönün ve öbür yana geçin.", "Her yana 5–10 tekrar, birkaç saatte bir")
EXT["bt_nod"] = ("Başı öne ve arkaya eğme", "Dik oturun. Çenenizi yavaşça göğsünüze doğru indirin, sonra ortaya dönüp tavana doğru hafifçe bakın. Hareketi küçük tutun, ağrı izin verdikçe genişletin.", "5–10 tekrar, birkaç saatte bir")
_ex2("bt_shrug", "ly_shrug", "Omuz kaldırma ve çevirme", "Dik oturun. Omuzlarınızı kulaklarınıza doğru kaldırın, sonra bırakın. Ardından omuzlarınızı önce öne, sonra arkaya doğru çevirin. Boyun ve omuz kaslarının gevşemesine yardım eder.", "5–10 tekrar, birkaç saatte bir")

BT_FAQ = [
 ("Boyun tutulması ne kadar sürer?", "Genellikle birkaç gün içinde düzelir. Kas spazmı çoğu zaman 24–48 saatte gevşer, tam iyileşme ise bir haftayı bulabilir. Bazen daha uzun sürebilir ya da ilerde belirgin bir neden olmadan tekrarlayabilir."),
 ("Boynumu hareket ettirmem zarar verir mi?", "Hayır. Boynu yavaşça hareket ettirmek ona zarar vermez; tersine, hareketi gün gün artırmak iyileşmeyi destekler. Ağrı çok şiddetliyse bir gün kadar dinlenip sonra yavaşça hareket etmeye başlayabilirsiniz. ABD fizyoterapi kılavuzu, ani başlayan ve hareket kısıtlılığı olan boyun ağrısında boyun hareket egzersizlerini ve kazanımları korumak için kürek kemiği ve kol güçlendirmesini öneriyor."),
 ("Sıcak mı soğuk mu?", "Sıcak uygulama birçok kişide kas tutukluğunu rahatlatır. Cildinizi yakmamak için sıcak torbayı bir havluya sararak kullanabilirsiniz."),
 ("Boyunluk takmalı mıyım?", "Genellikle gerekmez. Önerilen, boynu kademeli olarak hareket ettirmek ve günlük işlere elden geldiğince devam etmektir. Ağrı kontrol altındayken egzersizleri yapmak kolaylaşır; ağrı kesici kullanacaksanız hekiminize ya da eczacınıza danışın."),
]

BT_SRC = [
 "Royal Berkshire NHS Foundation Trust, Emergency Department. " + ext("https://royalberkshire.nhs.uk/media/ufzl1bno/acute-torticollis-wry-neck-_jun24.pdf", "Acute torticollis (wry neck)") + ". June 2024.",
 "Dorset County Hospital NHS Foundation Trust. " + ext("https://www.dchft.nhs.uk/wp-content/uploads/2020/10/ED-Acute-Torticollis-0414.pdf", "Acute torticollis (wryneck)") + ". Patient information, April 2014.",
 "Bussières AE, Stewart G, Al-Zoubi F, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/27836071/", "The treatment of neck pain-associated disorders and whiplash-associated disorders: a clinical practice guideline") + ". J Manipulative Physiol Ther. 2016;39(8):523–564",
 "nidirect. " + ext("https://www.nidirect.gov.uk/node/10321", "Meningitis") + ". Last updated 23 July 2026.",
 "Blanpied PR, Gross AR, Elliott JM, et al. " + ext("https://doi.org/10.2519/jospt.2017.0302", "Neck pain: revision 2017. Clinical practice guidelines linked to the International Classification of Functioning, Disability and Health from the Orthopaedic Section of the American Physical Therapy Association") + ". J Orthop Sports Phys Ther. 2017;47(7):A1–A83.",
]

BT_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Boyun tutulması (akut tortikolis)</h1>
    <p class="lede">Sabah uyandığınızda başınızı çeviremiyor, boynunuz bir yana kilitlenmiş gibi mi? Boyun tutulması, boyun kaslarının bir tarafındaki ani spazmla başın bir yana eğik ve dönük kalmasıdır. Çok ağrılı ve korkutucu olabilir, ama genellikle birkaç gün içinde kendiliğinden düzelir. Yavaş ve düzenli hareket, iyileşmeyi hızlandırmanın en iyi yoludur.</p>
    <p class="meta">Son güncelleme: 27 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>Bir gecede</b><span>Genellikle aniden, çoğu zaman uykudan sonra başlar</span></div>
        <div class="stat"><b>24–48 saat</b><span>Kas spazmının çoğu zaman gevşediği süre</span></div>
        <div class="stat"><b>Bir hafta</b><span>Tam iyileşmenin alabileceği süre; bazen daha uzun</span></div>
        <div class="stat"><b>Birkaç saatte bir</b><span>Boynu her yöne yavaşça hareket ettirmenin önerilen sıklığı</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Boynun bir yanında ağrı ve tutukluk; baş o tarafa eğik kalır.</li>
          <li>Başı çevirmekte ve boynu düzeltmekte zorlanma.</li>
          <li>Bir omzun diğerinden yukarıda durması.</li>
          <li>Boyun kaslarında sertlik, bazen şişlik.</li>
          <li>Baş ağrısı.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Çoğu zaman belirgin bir neden ya da yaralanma yoktur; daha önce boyun sorunu olmayan kişilerde de görülür.</li>
          <li>Boyun desteksiz, alışılmadık bir pozisyonda oturmak ya da uyumak.</li>
          <li>Bilgisayar başında uzun süre öne eğik duruş.</li>
          <li>Ağır ya da dengesiz yük taşımak.</li>
          <li>Soğuğa maruz kalmak, örneğin cereyanda uyumak.</li>
          <li>Gençlerde boyun ağrısının sık nedenlerinden biridir.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Yavaşça hareket</h3><p>Boynunuzu birkaç saatte bir her yöne yavaşça hareket ettirebilir, hareketi gün gün artırabilirsiniz. Hareket boyna zarar vermez.</p></div>
        <div class="kind"><span class="n">2</span><h3>Sıcak uygulama</h3><p>Havluya sarılı bir sıcak torba kas tutukluğunu birçok kişide rahatlatır.</p></div>
        <div class="kind"><span class="n">3</span><h3>Ağrı kesici</h3><p>Ağrı kontrol altındayken egzersizleri yapmak kolaylaşır. Ağrı kesici kullanacaksanız hangisinin ve nasıl kullanılacağını hekiminize ya da eczacınıza sorun; başka bir hastalığınız varsa ya da başka ilaç kullanıyorsanız bu özellikle önemlidir.</p></div>
        <div class="kind"><span class="n">4</span><h3>Duruş ve yastık</h3><p>Otururken ve çalışırken boynunuzu ve sırtınızı dik tutabilirsiniz. Tek, sağlam ve destekleyici bir yastık işe yarayabilir.</p></div>
      </div>
      <p class="soft" style="margin-top:18px">Ağrı haftalarca sürüyor ya da sık tekrarlıyorsa <a href="boyun-agrisi.html">boyun ağrısı</a> ve <a href="masa-basi.html">masa başı</a> rehberlerine bakabilirsiniz.</p>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Boynu çözen altı egzersiz</h2>
      <p class="soft">Hareketleri yavaş ve küçük başlatın, her gün biraz genişletin. Hafif bir gerginlik normaldir; ağrıyı zorlamayın. Kola yayılan ağrı ya da uyuşma olursa egzersizi bırakın.</p>
      {ex_grid(["bt_rot", "bt_side", "bt_nod", "bt_shrug", "chin", "scap"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(BT_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Birkaç gün geçtiği hâlde düzelme yoksa</li>
        <li>Ağrı çok şiddetliyse ya da kola veya ele yayılıyorsa</li>
        <li>Ellerinizde ya da ayaklarınızda uyuşma veya güçsüzlük varsa</li>
        <li>Acil: boyun sertliğine ateş, baş ağrısı, kusma, ışıktan rahatsız olma, uyuklama ya da bastırınca solmayan döküntü eşlik ediyorsa hemen 112’yi arayın (menenjit olabilir; belirtilerin hepsi birden görülmeyebilir)</li>
      </ul>
      {CTA_CARD("Boyun tutulmanız", "boyun tutulması")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(BT_SRC)}
    </div>
  </section>
</main>'''

page("boyun-tutulmasi.html", "Boyun Tutulması (Akut Tortikolis)",
     "Sabah boynunuz tutulmuş, başınızı çeviremiyor musunuz? Boyun tutulması neden olur, ne kadar sürer, neler iyi gelir? Uyarı işaretleri ve evde altı egzersiz.",
     "boyun-tutulmasi.html", NECK_CSS, BT_BODY, "",
     seo_title="Boyun Tutulması (Akut Tortikolis): Nedenleri, Ne Kadar Sürer ve Egzersizler | İhsan Eren",
     condition="Boyun tutulması (akut tortikolis)", faq_items=BT_FAQ)

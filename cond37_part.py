# -*- coding: utf-8 -*-
# Yeni rehber (37): Osgood-Schlatter (büyüme çağında diz altı ağrısı). cond36_part.py'den sonra exec edilir. Video yok.
# Yeni çizim: ayakta ön uyluk germe. Diğerleri hazır çizimler.

SV["os_qstr"] = fig(GRD +
    '<path class="obj" d="M86 50 V112 M80 50 H92"/>'
    '<path class="fig" d="M56 72 L56 112 M56 40 V72 M56 44 L70 50 L84 50"/>'
    '<circle class="hd" cx="57" cy="30" r="8"/>'
    f'<path class="fig hl" d="M56 72 L54 98 L42 76">{anim_d("M56 72 L54 98 L42 76;M56 72 L52 96 L44 72;M56 72 L54 98 L42 76", dur="4s")}</path>'
    f'<path class="fig" d="M56 46 L46 62 L42 76">{anim_d("M56 46 L46 62 L42 76;M56 46 L46 60 L44 72;M56 46 L46 62 L42 76", dur="4s")}</path>',
    "Ayakta ön uyluk germe")

EXT["os_qstr"] = ("Ayakta ön uyluk germe", "Bir sandalyeye ya da duvara tutunarak dik durun. Bir dizinizi bükün ve ayak bileğinizi elinizle tutup topuğunuzu kalçanıza doğru yaklaştırın; dizleriniz yan yana ve aşağı baksın. Uyluğunuzun önünde gerginlik hissedin. Yalnızca ağrı izin verdiğinde yapın.", "20–30 saniye, her bacakla 2–3 kez")
_ex2("os_ham", "lc_ham", "Arka uyluk germe", "Sandalyenin ön kenarına oturun. Bir bacağınızı öne uzatın, topuğunuz yerde, ayak ucunuz yukarı baksın. Sırtınızı düz tutarak kalçanızdan öne eğilin; uyluğunuzun arkasında gerginlik hissedin. Yalnızca ağrı izin verdiğinde yapın.", "20–30 saniye, her bacakla 2–3 kez")
_ex2("os_wall", "wall", "Duvarda yarım çömelme", "Sırtınızı duvara yaslayın, ayaklarınızı duvardan yarım adım öne alın. Sırtınız duvarda kayarak dizlerinizi hafifçe bükün ve ağrının hafif kaldığı derinlikte bekleyin. Ağrı artıyorsa daha az bükün.", "30–45 saniye, 3–5 kez")
_ex2("os_slr", "slr", "Düz bacak kaldırma", "Sırtüstü yatın, bir dizinizi bükün. Diğer bacağınızı dizi düz kalacak şekilde, uyluğunuzu sıkarak diğer dizinizin hizasına kadar kaldırın, yavaşça indirin. Dizin altındaki çıkıntıya yük bindirmeden ön uyluğu çalıştırır.", "10–15 tekrar, 2–3 set")
_ex2("os_abd", "abd", "Yan yatarak bacak kaldırma", "Yan yatın, alttaki dizinizi hafifçe bükün. Üstteki bacağınızı dizi düz, ayak ucu öne bakacak şekilde yukarı kaldırın ve yavaşça indirin. Kalçanın yan kasları dizi dengede tutmaya yardım eder.", "Her iki yana 10–15 tekrar, 2–3 set")
_ex2("os_bridge", "bridge", "Köprü", "Sırtüstü yatın, dizleriniz bükülü, ayaklarınız yerde. Kalçanızı sıkarak kaldırın; omuzlarınızdan dizlerinize kadar düz bir çizgi oluşsun. 3–5 saniye bekleyip yavaşça inin.", "10–15 tekrar, 2–3 set")

OS_FAQ = [
 ("Çocuğum spor yapmayı bırakmalı mı?", "Genellikle tamamen bırakması gerekmez. Spor kalıcı bir hasar yapmaz, ama ağrıyı artırabilir. Ağrı kontrol altına girene kadar özellikle koşu ve sıçrama gibi zorlayıcı aktivitelerin süresini, sıklığını ve toplam miktarını azaltmak önerilir. Ağrı çok şiddetliyse bir süre tam ara gerekebilir."),
 ("Ne kadar sürer?", "Ağrı çoğu zaman birkaç ayda azalır, ama bazı belirtiler 12–24 ay sürebilir. Kemik büyümesi tamamlanınca geçer. Yeni bir büyüme atağında ya da yoğun sporla yeniden alevlenebilir."),
 ("Dizin altındaki sert şişlik nedir?", "Ön uyluk kası, diz kirişi aracılığıyla kaval kemiğinin büyüyen ucunu tekrar tekrar çeker; bu bölge zorlanıp iltihaplanır. İyileşme sırasında burada sert bir kemik çıkıntısı oluşabilir. Çıkıntı dokununca ya da diz çökerken hassas olabilir."),
 ("Dinlenmek mi, egzersiz mi?", "10–14 yaş arası 51 gençle yapılan bir çalışmada, ağrıya göre ayarlanan bir aktivite merdiveni, diz güçlendirme ve kademeli spora dönüşten oluşan 12 haftalık programdan sonra gençlerin %80’i iyileşme bildirdi; 12 ayda %69’u spora döndü. Kontrol grubu olmayan bir çalışma olduğu için sonuçlar dikkatle yorumlanmalı, ama yalnızca dinlenip beklemeye bir alternatif sunuyor."),
]

OS_SRC = [
 "NHS Fife, Paediatric Orthopaedic Service. " + ext("https://www.nhsfife.org/services/all-services/patient-advice/osgood-schlatter-s-disease", "Osgood Schlatter’s disease") + ". Reviewed January 2022.",
 "Bradford Teaching Hospitals NHS Foundation Trust. " + ext("https://bradfordhospitals.nhs.uk/wp-content/uploads/2025/02/25011305-Osgood-Schlatters-Disease-Leaflet-2.pdf", "Osgood Schlatter’s disease") + ". Patient leaflet, February 2025.",
 "Rathleff MS, Winiarski L, Krommes K, et al. " + ext("https://research.regionh.dk/en/publications/activity-modification-and-knee-strengthening-for-osgood-schlatter/", "Activity modification and knee strengthening for Osgood-Schlatter disease: a prospective cohort study") + ". Orthopaedic Journal of Sports Medicine. 2020;8(4):2325967120911106.",
 "Neuhaus C, Appenzeller-Herzog C, Faude O. " + ext("https://doi.org/10.1016/j.ptsp.2021.03.002", "A systematic review on conservative treatment options for Osgood-Schlatter disease") + ". Phys Ther Sport. 2021;49:178–187",
]

OS_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Osgood-Schlatter (büyüme çağında diz altı ağrısı)</h1>
    <p class="lede">Çocuğunuz futbol, basketbol ya da koşudan sonra dizinin hemen altındaki çıkıntının ağrıdığını mı söylüyor? Osgood-Schlatter, büyüme atağındaki aktif çocuk ve gençlerde, ön uyluk kasının diz kirişi aracılığıyla kaval kemiğinin büyüyen ucunu tekrar tekrar çekmesiyle ortaya çıkar. Endişe verici görünse de zararsızdır ve büyüme tamamlanınca geçer. Doğru ayarlanmış aktivite ve egzersizle çocuğunuz sporunu bırakmadan bu dönemi atlatabilir.</p>
    <p class="meta">Son güncelleme: 14 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>10–16 yaş</b><span>En sık görüldüğü dönem; büyüme atağıyla birlikte, erkek çocuklarda daha sık</span></div>
        <div class="stat"><b>12–24 ay</b><span>Bazı belirtilerin sürebileceği zaman; büyüme bitince geçer</span></div>
        <div class="stat"><b>%80</b><span>12 haftalık aktivite ayarı ve güçlendirme programından sonra iyileşme bildiren gençler</span></div>
        <div class="stat"><b>10 dakika</b><span>Aktiviteden sonra, beze sarılı buzun önerilen uygulama süresi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Dizin hemen altında, kaval kemiğinin üst ucundaki çıkıntıda ağrı, şişlik ve hassasiyet.</li>
          <li>Dokununca ya da diz çökünce ağrıyan bir kemik çıkıntısı.</li>
          <li>Koşarken, sıçrarken, merdiven çıkarken ve sporda dizin önünde ağrı; bazen yürürken de.</li>
          <li>Genellikle tek dizde, bazen iki dizde birden.</li>
          <li>Tanı çoğu zaman muayeneyle konur; röntgen ya da başka tetkik genellikle gerekmez.</li>
        </ul>
      </div>
      <div>
        <h2>Kimlerde olur?</h2>
        <ul class="dots">
          <li>Büyüme atağındaki 10–16 yaş arası çocuk ve gençlerde.</li>
          <li>Erkek çocuklarda kızlardan daha sık.</li>
          <li>Koşu, sıçrama ve ani dönüş içeren sporlar yapanlarda.</li>
          <li>Hızlı boy uzaması döneminde.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Yükü ayarlayın</h3><p>Ağrı kontrol altına girene kadar koşu ve sıçramanın süresini ve sıklığını azaltın. Okula bilgi verip beden eğitimi derslerinin daha hafif yapılmasını isteyebilirsiniz.</p></div>
        <div class="kind"><span class="n">2</span><h3>Buz</h3><p>Özellikle aktiviteden sonra, beze sarılı buzu 10 dakika uygulayabilirsiniz; doğrudan cilde koymayın.</p></div>
        <div class="kind"><span class="n">3</span><h3>Germe ve güçlendirme</h3><p>Ön ve arka uyluk germeleri ve dizi zorlamayan güçlendirme egzersizleri, ağrı izin verdiğinde yapılabilir.</p></div>
        <div class="kind"><span class="n">4</span><h3>Kademeli dönüş</h3><p>Ağrıyı izleyerek basamak basamak ilerleyin: önce günlük aktiviteler ve egzersizler, ağrı izin verdikçe koşu, sıçrama ve maç.</p></div>
      </div>
      <p class="soft" style="margin-top:18px">Ağrı kesici için hekiminize ya da eczacınıza danışabilirsiniz. Dizin önündeki diğer ağrılar için <a href="diz-onu-agrisi.html">diz önü ağrısı</a> ve <a href="atlet-dizi.html">atlet dizi</a> rehberlerine bakabilirsiniz.</p>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Dizi rahatlatan altı egzersiz</h2>
      <p class="soft">Germeleri yalnızca ağrı izin verdiğinde yapın. Güçlendirme sırasında hafif bir ağrı olabilir, ama ağrı egzersizden sonra artıyor ya da ertesi gün geçmiyorsa yükü azaltın.</p>
      {ex_grid(["os_qstr", "os_ham", "os_wall", "os_slr", "os_abd", "os_bridge"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(OS_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>6 haftada düzelme yoksa (fizyoterapi gerekebilir)</li>
        <li>Ağrı çocuğunuzu geceleri uyandırıyorsa ya da dinlenirken de sürüyorsa</li>
        <li>Diz sıcak, kızarık ve şişse ya da ateş varsa</li>
        <li>Belirgin topallama, dizde kilitlenme ya da boşalma varsa</li>
      </ul>
      {CTA_CARD("Çocuğunuzun diz ağrısı", "Osgood-Schlatter")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(OS_SRC)}
    </div>
  </section>
</main>'''

page("osgood-schlatter.html", "Osgood-Schlatter (Büyüme Çağında Diz Altı Ağrısı)",
     "Çocuğunuzun dizinin altındaki çıkıntı ağrıyor mu? Osgood-Schlatter neden olur, ne kadar sürer, spor bırakılmalı mı? Aktivite ayarı, kademeli dönüş ve evde altı egzersiz.",
     "osgood-schlatter.html", NECK_CSS, OS_BODY, "",
     seo_title="Osgood-Schlatter: Çocuklarda Diz Altı Ağrısı, Tedavisi ve Egzersizler | İhsan Eren",
     condition="Osgood-Schlatter hastalığı", faq_items=OS_FAQ)

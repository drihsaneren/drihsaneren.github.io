# -*- coding: utf-8 -*-
# Yeni rehber (53): Çocuklarda büyüme ağrıları. cond52_part.py'den sonra exec edilir. Video yok.
# Germeler NHS Lothian (Royal Hospital for Children and Young People, Kasım 2024) broşürüne göre, hazır çizimlerle.

_ex2("gr_ham", "slr", "Arka uyluk germe", "Sırtüstü uzanın, iki dizi de bükülü olsun. Bir dizinizi göğsünüze doğru getirin, uyluğunuzun arkasından tutun ve bacağınızı düzeltip nazikçe başınıza doğru çekin. Yetişemiyorsanız uyluğunuza bir havlu dolayın.", "30 saniye, her bacakla 2–3 kez")
_ex2("gr_quad", "os_qstr", "Ön uyluk germe", "Yüzüstü uzanın ya da bir yere tutunarak ayakta durun. Ayak bileğinizi tutun, bacağınızı gevşek bırakın ve topuğunuzu kalçanıza doğru nazikçe yaklaştırın.", "30 saniye, her bacakla 2–3 kez")
_ex2("gr_k2c", "k2c", "Dizi göğse çekme", "Sırtüstü, bacaklarınız düz uzanın. Bir dizinizi bükün, dizinizin altından tutun ve göğsünüze doğru nazikçe çekin.", "30 saniye, her bacakla 2–3 kez")
_ex2("gr_calf", "calf", "Duvarda baldır germe", "Duvara dönük durun. Bir ayağınız önde, dizi hafif bükülü olsun; arkadaki bacağınız düz, topuğu yerde kalsın. Kalçanızı duvara doğru itin.", "30 saniye, her bacakla 2–3 kez")

GRP_FAQ = [
 ("Gerçekten büyümeden mi oluyor?", "Hayır. Adı böyle olsa da büyüme ağrılarının büyümeyle bir ilgisi yoktur ve ciddi bir hastalığın işareti değildir. Nedeni bilinmiyor. Aktif çocuklarda ve çok spor yapılan günlerden sonra daha sık görülür; eklemleri çok esnek olan çocuklarda da sıktır."),
 ("Kan testi ya da röntgen gerekir mi?", "Genellikle gerekmez. Hekim ya da fizyoterapist, öyküyü dinleyip muayene ederek tanı koyabilir. Bu çocuklarda kan testleri ve röntgen normaldir; yalnızca başka bir nedenden şüphelenilirse istenir."),
 ("Ne kadar sürer?", "Ağrılar aylarca, hatta yıllarca gelip gidebilir, sonra kendiliğinden geçer. Kalıcı bir hasar bırakmaz ve ileride kireçlenme riskini artırmaz."),
 ("Çocuğum sporu bırakmalı mı?", "Bırakması gerekmez. Aktif kalmak ve kasları nazikçe güçlendirmek çoğu zaman ağrıyı azaltır. Ağrının hangi günlerde ve hangi etkinliklerden sonra geldiğini bir günlükle izlemek, düzeni görmeye yardımcı olur. Destekleyici, iyi oturan ve sıkıca bağlanan ayakkabılar da işe yarayabilir."),
 ("Ağrı kesici verebilir miyim?", "Gerektiğinde çocuklara uygun parasetamol ya da ibuprofen verebilirsiniz; dozu için ambalajı okuyun ya da eczacınıza danışın. 16 yaşından küçük çocuklara, hekim önermedikçe aspirin vermeyin."),
]

GRP_SRC = [
 "NHS. " + ext("https://www.nhs.uk/conditions/growing-pains/", "Growing pains") + ". Page last reviewed: 16 June 2026.",
 "NHS Lothian, Royal Hospital for Children and Young People. " + ext("https://children.nhslothian.scot/nhs-leaflets/childhood-growing-pains/", "Childhood growing pains") + ". November 2024.",
 "Cambridge University Hospitals NHS Foundation Trust. " + ext("https://www.cuh.nhs.uk/patient-information/benign-nocturnal-idiopathic-limb-pains/", "Benign nocturnal idiopathic limb pains") + ". Version 2, September 2024.",
 "Royal Berkshire NHS Foundation Trust. " + ext("https://royalberkshire.nhs.uk/media/xbdm44wd/growing-pains_apr25.pdf", "Growing pains") + ". April 2025.",
]

GRP_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Çocuklarda büyüme ağrıları</h1>
    <p class="lede">Çocuğunuz akşamları ya da gece bacak ağrısıyla mı uyanıyor, sabah ise hiçbir şey olmamış gibi koşup oynuyor mu? Buna halk arasında büyüme ağrısı denir. Adı yanıltıcıdır: büyümeyle ilgisi yoktur ve ciddi bir hastalığın işareti değildir. 3–12 yaş arası çocuklarda sık görülür; masaj, ılık uygulama ve basit germelerle rahatlar.</p>
    <p class="meta">Son güncelleme: 18 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>3–12 yaş</b><span>En sık görüldüğü yaş aralığı</span></div>
        <div class="stat"><b>Yarısı</b><span>Çocukların yarısına kadarında bir dönem görülebilir</span></div>
        <div class="stat"><b>Akşam ve gece</b><span>Ağrının geldiği zaman; sabah genellikle geçmiştir</span></div>
        <div class="stat"><b>30 saniye</b><span>Germeleri tutma süresi, her bacakla 2–3 kez</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>İki bacakta, kaslarda hissedilen sızlama ya da zonklama; bazen bir taraf daha fazla ağrır.</li>
          <li>En sık baldır, kaval kemiği önü, ayak bilekleri ve ön uylukta; eklemlerin içinde değil, aralarında.</li>
          <li>Akşam ya da gece başlar, çocuğu uykudan uyandırabilir; sabaha geçer.</li>
          <li>Ağrıyan bölgede görünür bir şişlik, kızarıklık ya da morluk yoktur.</li>
        </ul>
      </div>
      <div>
        <h2>Neler iyi gelir?</h2>
        <ul class="dots">
          <li>Çocuğunuza ağrısının gerçek olduğunu ama tehlikeli olmadığını anlatarak güven verin.</li>
          <li>Bacaklarına nazikçe masaj yapın.</li>
          <li>Kılıfa sarılı sıcak su torbası koyun ya da yatmadan önce ılık banyo yaptırın.</li>
          <li>Gün içinde aktif kalmasına ve aşağıdaki germeleri yapmasına yardım edin.</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde germe</p>
      <h2>Bacakları rahatlatan dört germe</h2>
      <p class="soft">Germeler ağrıyı hafifletebilir. Her birini yavaşça, zorlamadan yapın ve her iki bacağa da uygulayın. Küçük çocuklara ilk zamanlarda bir yetişkin yardım etsin.</p>
      {ex_grid(["gr_ham", "gr_quad", "gr_k2c", "gr_calf"], "ex four")}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(GRP_FAQ)}
      <p class="soft" style="margin-top:18px">Topukta ağrı için <a href="sever-hastaligi.html">Sever hastalığı</a>, dizin hemen altında şişlik ve ağrı için <a href="osgood-schlatter.html">Osgood-Schlatter</a>, çok esnek eklemler için <a href="eklem-hipermobilitesi.html">eklem hipermobilitesi</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Ağrı hep aynı bacakta ya da tek bir eklemde (diz, ayak bileği gibi) oluyorsa</li>
        <li>Ağrı sabahları ya da yürürken, oynarken oluyorsa</li>
        <li>Çocuğunuz topallıyor ya da ağrı yüzünden yürüyemiyorsa</li>
        <li>Bacaklarda döküntü, şişlik, kızarıklık, sıcaklık ya da olağandışı morluk varsa</li>
        <li>Ağrıyla birlikte ateş varsa</li>
        <li>Çocuğunuz sık sık olağandışı yorgun ya da uykulu görünüyorsa, iştahsızsa ya da kilo kaybediyorsa</li>
        <li>Her gece ağrıyla uyanıyor ya da ağrı yüzünden okulu kaçırıyorsa</li>
      </ul>
      {CTA_CARD("Çocuğunuzun bacak ağrıları", "çocuğumun bacak ağrıları (büyüme ağrıları)")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(GRP_SRC)}
    </div>
  </section>
</main>'''

page("buyume-agrilari.html", "Çocuklarda Büyüme Ağrıları",
     "Çocuğunuz gece bacak ağrısıyla mı uyanıyor? Büyüme ağrıları nedir, neden olur, ne iyi gelir, ne zaman hekime gidilmeli? Uyarı işaretleri ve evde dört germe.",
     "buyume-agrilari.html", NECK_CSS, GRP_BODY, "",
     seo_title="Çocuklarda Büyüme Ağrıları: Gece Bacak Ağrısı, Uyarı İşaretleri ve Germeler | İhsan Eren",
     condition="Büyüme ağrıları", faq_items=GRP_FAQ)

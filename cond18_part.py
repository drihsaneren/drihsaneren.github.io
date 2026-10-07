# -*- coding: utf-8 -*-
# Yeni rehberler (17): golfçü dirseği ve Guillain-Barré sendromu.
# cond17_part.py'den sonra exec edilir. Videolar: CommonSpirit Houston, Rehab Science, Mayo Clinic (oEmbed ile doğrulandı).

# ---- yeni çizimler
# Ön kolu içe-dışa çevirme: önden bakış; yumruk sabit, elde tutulan çubuk iki yana döner.
SV["ge_rot"] = fig(
    '<path class="obj" d="M18 84 H102"/>'
    '<path d="M32 44 A30 30 0 0 1 88 44 M36 38 L32 44 L39 46 M84 38 L88 44 L81 46" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="0"/>'
    f'<g>{anim_t("-70 60 70;70 60 70;-70 60 70", dur="4.4s", typ="rotate")}<path d="M60 70 V34" stroke="#C8963E" stroke-width="5" stroke-linecap="round"/><rect x="52" y="26" width="16" height="10" rx="3" fill="#C8963E"/></g>'
    '<circle cx="60" cy="70" r="11" fill="#2A6F6B"/>',
    "Ön kolu çevirme")
# Avuç yukarı bilek kaldırma (yukarı doğru çalışma)
SV["ge_con"] = fig(TABLE +
    '<path class="fig" d="M14 64 H62"/>'
    f'<g>{anim_t("30 62 64;-40 62 64;30 62 64", dur="4s", kt="0;0.5;1", typ="rotate")}'
    '<path class="fig hl" d="M62 64 H82"/><circle cx="85" cy="60" r="6.5" fill="#C8963E"/></g>',
    "Bilek kaldırma")

_ex2("ge_ext", "wext_st", "Bilek açıcıları germe", "Dirseğinizi düzleştirin ve bileğinizi aşağı bırakın. Diğer elinizle elinizin sırtına nazikçe bastırın; ön kolunuzun üst yüzünde gerilme hissedin. Spordan ve işten önce yapmak yararlıdır.", "15 saniye tutun, 3–5 tekrar, günde 2–3 kez")
_ex2("ge_flex", "wflex", "Bilek bükücüleri germe", "Dirseğiniz düz, avucunuz yukarı baksın. Diğer elinizle parmaklarınızı ve elinizi aşağı ve geriye doğru çekin; dirseğin iç yanında ve ön kolda gerilme hissedin. Ağrı olmamalı.", "15–30 saniye tutun, 3–5 tekrar, günde 2–3 kez")
_ex2("ge_elbow", "ly_arm", "Dirseği büküp açma", "Kolunuzu rahatça yanınızda tutun. Dirseğinizi tam bükün, sonra tam açın. Ağrı izin verdikçe tekrar sayısını artırın.", "10 tekrar; zamanla 3 set 15 tekrar")
_ex2("ge_ecc", "eccwe", "Avuç yukarı, ağırlığı yavaş indirme", "Ön kolunuzu masaya koyun, avucunuz yukarı baksın, eliniz masanın kenarından taşsın. Elinizde küçük bir ağırlık (bir konserve kutusu ya da su şişesi) olsun. Diğer elinizle bileğinizi yukarı kaldırın, sonra bırakıp ağırlığı 6 saniyede yavaşça indirin. Hafif bir rahatsızlık olağandır.", "10 tekrar, günde 3 kez; zamanla 3 set")
EXT["ge_rot"] = ("Ön kolu içe-dışa çevirme", "Ön kolunuz masada dursun. Elinizin sırtı masadayken başlayın, sonra avucunuz aşağı bakacak şekilde çevirin; 5 saniye tutup yavaşça geri dönün. Kolaylaşınca elinize bir konserve kutusu ya da çekiç alın.", "10 tekrar; zamanla 3 set")
EXT["ge_con"] = ("Avuç yukarı bilek kaldırma", "Ön kolunuzu masaya koyun, avucunuz yukarı baksın. Elinizde küçük bir ağırlıkla bileğinizi yavaşça, gidebildiği kadar yukarı bükün; sonra elinizi masa hizasına getirin. Kolaylaştıkça ağırlığı artırın.", "10 tekrar; zamanla 3 set")

_ex2("gb_apump", "apump", "Ayak bileği pompası", "Sırtüstü yatın ya da oturun. Ayak uçlarınızı önce kendinize doğru çekin, sonra aşağı doğru itin. Yatakta geçen dönemde baldır kaslarını çalıştırır ve ayak bileğinin sertleşmesini önler.", "10–15 tekrar, günde birkaç kez")
_ex2("gb_quad", "quad", "Havluya bastırma", "Sırtüstü uzanın, dizinizin altına rulo yapılmış bir havlu koyun. Dizinizin arkasını havluya bastırarak uyluğunuzun ön kasını sıkın, birkaç saniye tutup gevşetin.", "5 saniye tutun, 10 tekrar")
_ex2("gb_bridge", "bridge", "Köprü", "Sırtüstü yatın, dizleriniz bükülü olsun. Kalçanızı yavaşça kaldırın, kısa bir an tutup kontrollü biçimde indirin. Yorulduğunuzda durun; kalite sayıdan önemlidir.", "5–10 tekrar")
_ex2("gb_sts", "sts", "Sandalyeden kalkıp oturma", "Sağlam bir sandalyenin ön kısmına oturun. Öne eğilip ellerinizden gerektiği kadar destek alarak ayağa kalkın, sonra yavaşça oturun. Güçlendikçe el desteğini azaltın.", "5–10 tekrar, 1–2 set")
_ex2("gb_heel", "heel2", "Tezgâha tutunarak topuk yükseltme", "Tezgâha tutunarak dik durun. İki topuğunuzu birlikte kaldırın ve yavaşça inin. Ayak bileği gücü çoğu zaman en son dönen güçtür; sabırla çalışın.", "8–10 tekrar")
_ex2("gb_walk", "walk", "Kısa ve sık yürüyüş", "Uzun tek bir yürüyüş yerine gün içine yayılmış kısa yürüyüşler yapın. Gerekirse yürüteç ya da baston kullanın. Ertesi gün belirgin yorgunluk ya da güçsüzlük oluyorsa mesafeyi azaltın.", "Günde birkaç kez, azar azar artırarak")

# ============================================================== GOLFÇÜ DİRSEĞİ
GE_FAQ = [
 ("Golfçü dirseği ile tenisçi dirseği arasındaki fark nedir?", "İkisi de dirseğe yapışan kirişlerin aşırı kullanıma bağlı ağrısıdır; fark yerindedir. Golfçü dirseğinde ağrı dirseğin iç yanındadır ve bileği ile parmakları büken kaslar etkilenir. Tenisçi dirseğinde ağrı dış yandadır ve bileği kaldıran kaslar etkilenir."),
 ("Golf oynamıyorum; neden bende oldu?", "Golfçü dirseği aslında spor yapmayanlarda daha sık görülür. Bahçe işleri, boya, el aletleri kullanmak, uzun süre klavye kullanmak gibi bileği ve parmakları tekrar tekrar ve kuvvetle büken her iş neden olabilir. Bazen dirseğe alınan tek bir darbeden sonra da başlar."),
 ("Dirsek bandı işe yarar mı?", "Ön kola takılan dirsek bandı (epikondil bandı), ağrılı noktadaki baskıyı azaltarak rahatlama sağlayabilir. Eczanelerden alınabilir. Tek başına bir tedavi değildir; yükü azaltma ve egzersizle birlikte kullanılır."),
 ("Kortizon iğnesi yaptırmalı mıyım?", "İğne ilk seçenek değildir. Az sayıda kişide kısa vadede ağrıyı azaltabilir ve diğer yöntemler işe yaramadığında düşünülür. Ameliyat ise nadiren gerekir. Tedavinin temeli yükü azaltmak, germe ve kademeli güçlendirmedir."),
]

GE_SRC = [
 "NHS Fife. " + ext("https://www.nhsfife.org/services/all-services/patient-advice/golfers-elbow/", "Golfer's elbow (medial epicondylosis/itis)") + ". Fife Musculoskeletal Physiotherapy. February 2025.",
 "University Hospitals Plymouth NHS Trust. " + ext("https://www.plymouthhospitals.nhs.uk/display-pil/pil-golfers-elbow-4078", "Golfer's elbow") + ". Patient information leaflet B-275. September 2019.",
]

GE_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Golfçü dirseği</h1>
    <p class="lede">Golfçü dirseği, dirseğin iç yanındaki kemik çıkıntısına yapışan kirişlerin aşırı kullanıma bağlı ağrısıdır. Adına rağmen çoğunlukla golf oynamayanlarda, eliyle tekrarlı ve kuvvetli iş yapanlarda görülür. Tedavinin temeli yükü azaltmak, germe ve kademeli güçlendirmedir.</p>
    <p class="meta">Son güncelleme: 8 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>30–50 yaş</b><span>En sık görüldüğü yaş aralığı</span></div>
        <div class="stat"><b>Eşit</b><span>Kadınlarda ve erkeklerde aynı sıklıkta görülür</span></div>
        <div class="stat"><b>6 saniye</b><span>Güçlendirme hareketinde ağırlığı indirme süresi</span></div>
        <div class="stat"><b>3 × 10</b><span>Güçlendirme hareketlerinde hedeflenen set ve tekrar sayısı</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Bileği ve parmakları büken kasların kirişleri, dirseğin iç yanındaki kemik çıkıntısına yapışır. Bu kirişler tekrarlı ve kuvvetli kullanımla zorlandığında yapışma yerinde ağrı ortaya çıkar. Tenisçi dirseğinin “iç yan” karşılığıdır.</p>
        <p class="soft">Bahçe işleri, boya, el aletleri, klavye kullanımı ve bileği kuvvetle büken sporlar başlıca nedenlerdir. Bazen dirseğe düşme ya da ani bir darbeden sonra da başlar.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Dirseğin iç yanında ağrı ve hassasiyet</li>
          <li>Ağrının ön kola ve bileğe yayılması</li>
          <li>Dirseği bükerken ya da bir şey kavrarken artan ağrı</li>
          <li>Kavrama gücünde azalma, bilekte güçsüzlük</li>
          <li>Dirsekte sertlik</li>
          <li>Ağrının işten sonra artıp dinlenince azalması</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>İlk adım: yükü azaltmak</h2>
      <p class="soft">Kirişin iyileşebilmesi için ağrıya yol açan işleri değiştirmek ya da bir süre bırakmak gerekir. Çoğu kişi çalışmaya devam edebilir; önemli olan iş yükünü ağrıyı azaltacak biçimde düzenlemek ve tekrarlı el hareketlerini kısmaktır.</p>
      <ul class="tx">
        <li><b>Soğuk</b><span>İlk günlerde havluya sarılı buz torbasını 10 dakika, günde 3–4 kez uygulayın.</span></li>
        <li><b>Dirsek bandı</b><span>Ön kola takılan bant ağrılı noktadaki baskıyı azaltabilir.</span></li>
        <li><b>İlaç</b><span>Ağrı kesici ve iltihap giderici ilaçlar için eczacınıza danışın.</span></li>
        <li><b>Isınma</b><span>Spordan ve işten önce ısının, ön kolunuzu nazikçe gerin.</span></li>
        <li><b>Teknik</b><span>Golf oynuyorsanız sopa boyunu, tutuşunuzu ve vuruş tekniğinizi bir eğitmene değerlendirtin.</span></li>
        <li><b>Kademeli dönüş</b><span>Kısa ve hafif çalışmalarla başlayıp yükü yavaş yavaş artırın.</span></li>
      </ul>
      <div class="callout">
        <p>Dirseğinizin dış yanı ağrıyorsa bu rehber yerine <a href="tenisci-dirsegi.html">tenisçi dirseği</a> rehberine bakın; hareketler farklıdır.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Golfçü dirseği için altı egzersiz</h2>
      <p class="soft">İlk ikisi germe, sonraki dördü hareket ve güçlendirme içindir. Güçlendirme hareketlerinde hafif bir rahatsızlık olağandır; ağrı fazlaysa ağırlığı ve tekrarı azaltın. Hareketlerden sonra ağrı olursa buz uygulayabilirsiniz.</p>
      {ex_grid(["ge_ext", "ge_flex", "ge_elbow", "ge_rot", "ge_con", "ge_ecc"])}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Golfçü dirseği için videolar</h2>
      <p class="soft">ABD'deki CommonSpirit Houston hastanesinin ve fizyoterapist Dr. Tom Walters'ın (Rehab Science) YouTube kanallarından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("m8YtVpSR1Bk", "Evde egzersizler videosunu oynat", "Golfer's Elbow Pain Relief: Simple Exercises You Can Do At Home")}
          <h3>Evde yapılabilecek hareketler</h3>
          <p>Hastanenin hazırladığı, evde yapılabilecek egzersizleri gösteren video.</p>
        </div>
        <div class="vid">
          {vbox("yTPQEW1aTTI", "Dört ev egzersizi videosunu oynat", "4 Home Exercises for Golfers Elbow")}
          <h3>Dört ev egzersizi</h3>
          <p>Bir fizyoterapistin gösterdiği dört egzersiz.</p>
        </div>
      </div>
      <p class="meta">Videolar CommonSpirit Houston ve Rehab Science kanallarına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(GE_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Düşme ya da darbeden sonra dirsekte şişlik, şekil bozukluğu ya da hareket ettirememe</li>
        <li>Dirsekte kızarıklık ve sıcaklıkla birlikte ateş</li>
        <li>Yüzük ve serçe parmakta geçmeyen uyuşma ya da elde güçsüzlük</li>
        <li>Dinlenirken ve gece hiç geçmeyen ağrı</li>
        <li>Birkaç haftalık dinlendirme ve egzersize rağmen artan ağrı</li>
      </ul>
      {CTA_CARD("Golfçü dirseğine bağlı ağrınız", "golfçü dirseği")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(GE_SRC)}
    </div>
  </section>
</main>'''

page("golfcu-dirsegi.html", "Golfçü Dirseği",
     "Dirseğin iç yanındaki ağrı neden olur? Golfçü dirseği ile tenisçi dirseğinin farkı, yükü azaltma, dirsek bandı, kortizon iğnesi ve evde altı germe ve güçlendirme egzersizi.",
     "golfcu-dirsegi.html", NECK_CSS, GE_BODY, YT_JS,
     seo_title="Golfçü Dirseği: Dirseğin İç Yanında Ağrı, Egzersiz ve Tedavi | İhsan Eren",
     condition="Golfçü dirseği (medial epikondilit)", faq_items=GE_FAQ)

# ============================================================== GUILLAIN-BARRÉ
GB_FAQ = [
 ("Guillain-Barré sendromu tamamen geçer mi?", "Çoğu kişi, ağır geçirenler de dahil, tamamen iyileşir. Bazı kişilerde ise güçsüzlük, uyuşma, yorgunluk ya da ağrı uzun süre kalabilir. İyileşme birkaç haftadan birkaç yıla kadar sürebilir; bu yüzden rehabilitasyon ve düzenli kontrol önemlidir."),
 ("Ne kadar sürede yeniden yürürüm?", "Çoğu kişi altı ay içinde yürür ve bir yıl içinde toparlanır. Güçsüzlük genellikle ilk iki-dört hafta içinde en ağır düzeyine ulaşır, sonra yavaş yavaş geri döner. Süre kişiden kişiye çok değişir; güç her kasa aynı hızda dönmeyebilir."),
 ("Hastalık tekrarlar mı?", "Tekrarlayabilir; bu yüzden iyileştikten sonra önce birkaç ayda bir, sonra yılda bir kontrol önerilir. Uzun süredir devam eden belirtileriniz kötüleşirse ya da iyileştikten sonra belirtiler geri dönerse beklemeden uzmanınıza başvurun."),
 ("İyileşirken egzersiz yapmak zarar verir mi?", "Eldeki araştırmalar egzersizin yararlı olabileceğini gösteriyor: 16 çalışmayı inceleyen 2025 tarihli derlemeye göre egzersiz gücü artırabilir, yorgunluğu azaltabilir ve bağımsızlığı destekleyebilir. Yine de çalışmalar küçük ve kesin konuşmak için yeterli değil. Programı fizyoterapistinizle, yorgunluğunuza göre ayarlayın."),
]

GB_SRC = [
 "Hughes RAC, Swan AV, van Doorn PA. " + ext("https://www.cochrane.org/CD002063/NEUROMUSC_intravenous-immunoglobulin-for-guillain-barre-syndrome", "Intravenous immunoglobulin for Guillain-Barré syndrome") + ". Cochrane Database Syst Rev. 2014;(9):CD002063.",
 "Kiper P, Chevrot M, Godart J, et al. " + ext("https://search.pedro.org.au/search-results/record-detail/83710", "Physical exercise in Guillain-Barré syndrome: a scoping review") + ". J Clin Med. 2025;14(8):2655.",
 "National Institute of Neurological Disorders and Stroke. " + ext("https://www.ninds.nih.gov/health-information/disorders/guillain-barre-syndrome", "Guillain-Barré syndrome") + ". Last reviewed 13 March 2026.",
 "NHS. " + ext("https://www.nhs.uk/conditions/guillain-barre-syndrome/", "Guillain-Barré syndrome") + ". Page last reviewed 12 August 2024.",
 "World Health Organization. " + ext("https://www.who.int/news-room/fact-sheets/detail/guillain-barr%C3%A9-syndrome", "Guillain–Barré syndrome") + ". Fact sheet. 24 October 2025.",
]

GB_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>Guillain-Barré sendromu</h1>
    <p class="lede">Guillain-Barré sendromu, bağışıklık sisteminin çevresel sinirlere saldırdığı, seyrek görülen ve acil hastane tedavisi gerektiren bir hastalıktır. Güçsüzlük günler ve haftalar içinde ilerler, sonra yavaş yavaş geri döner: Çoğu kişi altı ay içinde yürür, bir yıl içinde toparlanır. İyileşme döneminde fizyoterapi, gücü ve bağımsızlığı geri kazanmanın temelidir.</p>
    <p class="meta">Son güncelleme: 8 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>2–4 hafta</b><span>Belirtilerin genellikle kötüleşmeye devam ettiği süre</span></div>
        <div class="stat"><b>3'te 1</b><span>Solunum kasları etkilenen hastaların oranı (DSÖ)</span></div>
        <div class="stat"><b>6 ay</b><span>Çoğu kişinin yeniden yürüdüğü süre; toparlanma bir yılı bulabilir</span></div>
        <div class="stat"><b>16 çalışma</b><span>İyileşme döneminde egzersizi inceleyen 2025 tarihli derleme</span></div>
      </div>
      <div class="note warn" style="margin-top:22px"><strong>Bu bir acil durumdur.</strong> Ayaklarda ve ellerde başlayıp yukarı doğru yayılan karıncalanma ve güçsüzlük varsa aynı gün hekime başvurun. Nefes almakta, yutmakta ya da konuşmakta güçlük, yüzde sarkma varsa 112'yi arayın. Bu sayfa, hastane tedavisinden sonraki iyileşme dönemi içindir.</div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Bağışıklık sistemi, beyin ve omurilik dışındaki sinirlere saldırır; sinirler kaslara ve duyulara giden sinyalleri iletemez. Çoğu zaman grip ya da mide-bağırsak enfeksiyonu gibi bir enfeksiyondan birkaç hafta sonra başlar. Her yaşta görülebilir; yetişkinlerde ve erkeklerde daha sıktır.</p>
        <p class="soft">Güçsüzlük saatler, günler ya da haftalar içinde ilerler; hastaların onda dokuzu üçüncü haftaya gelindiğinde en zayıf dönemine ulaşmış olur. Sonra iyileşme başlar.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Ayaklarda ve ellerde karıncalanma, uyuşma, iğnelenme</li>
          <li>Bacaklardan başlayıp kollara ve yüze yayılan güçsüzlük</li>
          <li>Özellikle bacaklarda ve sırtta keskin sinir ağrısı</li>
          <li>Yürümede ve dengede bozulma</li>
          <li>Yüzde sarkma, yutma ya da konuşma güçlüğü, çift görme</li>
          <li>Nefes almada güçlük; nabız ve tansiyonda oynamalar</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Hastanede tedavi</h2>
      <p class="soft">Tedavi hastanede, çoğunlukla birkaç hafta sürer. Bağışıklık sisteminin sinirlere saldırısını durdurmak için iki yöntemden biri kullanılır: damardan immünoglobulin (IVIG) ya da plazma değişimi. Cochrane derlemesine göre ağır hastalarda, ilk iki hafta içinde başlanan IVIG iyileşmeyi plazma değişimi kadar hızlandırıyor; ikisini art arda vermek ek yarar sağlamıyor.</p>
      <p class="soft">Bunun yanında solunum, nabız ve tansiyon yakından izlenir; gerekirse solunum cihazı desteği verilir. Yürüyemeyen hastalarda bacak damarlarında pıhtı oluşmasını önlemek için ilaç ve bası çorabı, sinir ağrısı için ilaç kullanılır.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>İyileşme döneminde rehabilitasyon</h2>
      <ul class="tx">
        <li><b>Hareket açıklığı</b><span>Kaslar çalışmazken fizyoterapist kolları ve bacakları hareket ettirir, doğru pozisyon verir; kasların kısalması önlenir.</span></li>
        <li><b>Güçlendirme</b><span>Güç her kasa aynı hızda dönmez; zayıf kalan kaslara yönelik egzersizler yapılır.</span></li>
        <li><b>Yürüme ve denge</b><span>Gerekirse yürüteç ya da bastonla başlanır, destek kademeli olarak azaltılır.</span></li>
        <li><b>İş-uğraşı terapisi</b><span>Günlük işleri yeniden yapabilmek ve işe dönüş için çalışma; yardımcı araçlar.</span></li>
        <li><b>Yorgunluk ve ağrı</b><span>Uzun süre kalabilen yorgunluk ve sinir ağrısı için plan; ağrı ilaçlarını hekiminiz düzenler.</span></li>
        <li><b>Ruh sağlığı</b><span>Kaygı ve depresyon sık görülür; psikolojik destek tedavinin parçasıdır.</span></li>
      </ul>
      <div class="callout">
        <p>16 çalışmayı inceleyen 2025 tarihli derlemeye göre egzersiz, Guillain-Barré sonrasında gücü artırabilir, yorgunluğu azaltabilir ve bağımsızlığı destekleyebilir; ancak çalışmalar küçük ve yazarlar daha büyük araştırmalara gerek olduğunu belirtiyor. Kısa seanslar yapın, araya dinlenme koyun; ertesi gün belirgin yorgunluk ya da güçsüzlük artışı olursa programı hafifletin.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>İyileşme dönemi için altı egzersiz</h2>
      <p class="soft">Bu hareketler hastaneden çıktıktan sonraki dönem içindir ve kolaydan zora sıralanmıştır. Hangi basamakta olduğunuz gücünüze bağlıdır; programınızı fizyoterapistinizle belirleyin ve yorulmadan bırakın.</p>
      {ex_grid(["gb_apump", "gb_quad", "gb_bridge", "gb_sts", "gb_heel", "gb_walk"])}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Guillain-Barré için video</h2>
      <p class="soft">ABD'deki Mayo Clinic'in YouTube kanalından. Video İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("HtkWhtG-MCM", "Guillain-Barré söyleşi videosunu oynat", "Guillain Barre Syndrome: Mayo Clinic Radio")}
          <h3>Mayo Clinic Radio söyleşisi</h3>
          <p>Guillain-Barré sendromunu konu alan radyo söyleşisi.</p>
        </div>
      </div>
      <p class="meta">Video Mayo Clinic kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(GB_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden yardım alın:</p>
      <ul class="dots redflags">
        <li>Nefes almakta, yutmakta ya da konuşmakta güçlük; yüzde sarkma (112)</li>
        <li>Saatler ya da günler içinde hızla artan güçsüzlük</li>
        <li>İyileştikten sonra belirtilerin geri dönmesi ya da uzun süren belirtilerin kötüleşmesi</li>
        <li>Baldırda ağrılı şişlik, sıcaklık ya da kızarıklık</li>
        <li>Göğüs ağrısı ya da ani nefes darlığı (112)</li>
      </ul>
      {CTA_CARD("Guillain-Barré sonrası güçsüzlük ve yürüme güçlükleriniz", "Guillain-Barré sonrası rehabilitasyon")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(GB_SRC)}
    </div>
  </section>
</main>'''

page("guillain-barre.html", "Guillain-Barré Sendromu",
     "Guillain-Barré sendromu nedir, nasıl tedavi edilir, ne kadar sürede iyileşir? Hastane tedavisi, iyileşme döneminde rehabilitasyon, egzersiz için kanıt ve evde altı egzersiz.",
     "guillain-barre.html", NECK_CSS, GB_BODY, YT_JS,
     seo_title="Guillain-Barré Sendromu: Tedavi, İyileşme ve Rehabilitasyon | İhsan Eren",
     condition="Guillain-Barré sendromu", faq_items=GB_FAQ)

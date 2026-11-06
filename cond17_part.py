# -*- coding: utf-8 -*-
# Yeni rehberler (16): halluks valgus (ayak başparmağı çıkıntısı) ve tetik parmak.
# cond16_part.py'den sonra exec edilir. Videolar: Manipal Hospitals, Human 2.0 Fitness (Dr. Chris Raynor), Mayo Clinic, Doctor O'Donovan (oEmbed ile doğrulandı).

_PALM = ('<path class="fig" d="M60 112 L60 84"/><rect x="46" y="48" width="28" height="38" rx="8" fill="#2A6F6B"/>'
         '<path class="fig" d="M48 76 L36 62 L32 50"/>')
# ---- yeni çizimler
# Ayak başparmağını elle germe (üstten ayak; başparmak altın, sağa sola nazikçe oynar)
SV["hv_toe"] = fig(
    '<rect x="46" y="40" width="28" height="68" rx="13" fill="#2A6F6B"/>'
    '<g fill="#2A6F6B"><circle cx="62" cy="31" r="4.5"/><circle cx="70" cy="34" r="4"/><circle cx="76" cy="39" r="3.5"/></g>'
    f'<g>{anim_t("0 0;-5 -1;0 0;4 0;0 0", dur="4.8s", kt="0;0.25;0.5;0.75;1")}<circle cx="52" cy="30" r="6.5" fill="#C8963E"/></g>'
    '<path d="M30 22 H42 M34 18 L30 22 L34 26 M38 18 L42 22 L38 26" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "Başparmağı germe")
# Ilık suda eli gevşetme
SV["tf_warm"] = fig(
    '<path class="obj" d="M22 70 H98 M26 70 Q60 118 94 70"/>'
    '<path class="fig" d="M60 6 V30"/><rect x="48" y="28" width="24" height="30" rx="8" fill="#2A6F6B"/>'
    f'<path class="fig hl" d="M52 58 V80 M58 58 V84 M64 58 V84 M70 58 V80">{anim_d("M52 58 V80 M58 58 V84 M64 58 V84 M70 58 V80;M52 58 V74 M58 58 V77 M64 58 V77 M70 58 V74;M52 58 V80 M58 58 V84 M64 58 V84 M70 58 V80")}</path>'
    '<g fill="none" stroke="#C8963E" stroke-width="2.5" stroke-linecap="round"><path d="M30 60c-3-4 3-6 0-10"><animate attributeName="opacity" values="0;1;0" dur="2.4s" repeatCount="indefinite"/></path>'
    '<path d="M90 60c-3-4 3-6 0-10"><animate attributeName="opacity" values="0;1;0" dur="2.4s" begin="1.2s" repeatCount="indefinite"/></path></g>',
    "Ilık suda gevşetme")
# Parmak dibine buz masajı
SV["tf_ice"] = fig(_PALM +
    '<path class="fig" d="M50 48 V24 M57 48 V18 M64 48 V20 M71 48 V28"/>'
    '<circle class="band" cx="60" cy="54" r="8"/>'
    f'<g>{anim_t("0 60 54;360 60 54", dur="3s", kt="0;1", typ="rotate")}<rect x="55" y="42" width="10" height="10" rx="2.5" fill="#B9CBC6" stroke="#C8963E" stroke-width="2"/></g>',
    "Buz masajı")
# Masa pozisyonu: parmaklar düz, yalnızca parmak diplerinden bükülür (yandan)
SV["tf_table"] = fig(
    '<path class="fig" d="M56 116 L56 84"/><rect x="48" y="54" width="16" height="32" rx="7" fill="#2A6F6B"/>'
    f'<path class="fig hl" d="M56 54 L56 40 L56 24">{anim_d("M56 54 L56 40 L56 24;M56 54 L70 51 L86 51;M56 54 L56 40 L56 24")}</path>',
    "Masa pozisyonu")
# Diğer elle parmakları yumruğa doğru itme (yandan)
SV["tf_passive"] = fig(
    '<path class="fig" d="M56 116 L56 84"/><rect x="48" y="54" width="16" height="32" rx="7" fill="#2A6F6B"/>'
    f'<path class="fig" d="M56 54 L56 40 L56 24">{anim_d("M56 54 L56 40 L56 24;M56 54 L70 46 L66 62;M56 54 L56 40 L56 24")}</path>'
    f'<g>{anim_t("16 -18;0 0;16 -18")}<rect x="72" y="42" width="13" height="24" rx="6" fill="#C8963E"/></g>',
    "Diğer elle yumruk")
# Gece ateli: bir parmak düz tutulur
SV["tf_splint"] = fig(_PALM +
    '<path class="fig" d="M50 48 V24 M64 48 V20 M71 48 V28"/>'
    '<rect x="53" y="14" width="8" height="38" rx="4" fill="#C8963E"/>'
    '<path d="M92 20 a10 10 0 1 0 8 14 a8 8 0 0 1 -8 -14z" fill="#C8963E"><animate attributeName="opacity" values=".45;1;.45" dur="3.2s" repeatCount="indefinite"/></path>',
    "Gece ateli")

_ex2("hv_calf", "calf", "Duvarda baldır germe", "Yüzünüz duvara dönük durun, ellerinizi duvara dayayın. Ağrılı taraftaki bacağınızı arkaya alın ve baldırınızı nazikçe gerin. Gergin baldır, yürürken ayağın ön kısmına binen yükü artırır.", "30 saniye, günde 5–10 kez")
_ex2("hv_short", "ff_short", "Ayak kavsini kaldırma", "Oturun, ayağınız yere düz bassın. Ayak tabanınızdaki kasları sıkarak kavsinizi yükseltin; parmaklarınız kıvrılmasın. Birkaç saniye tutup gevşetin.", "10 tekrar")
_ex2("hv_press", "ff_press", "Başparmakları birbirine bastırma", "Oturun. İki ayak başparmağınızın iç kenarlarını birbirine bastırın ve öylece tutun. Ağrı oluyorsa bu hareketi atlayın.", "5 saniye tutun, 10 tekrar")
_ex2("hv_heel", "heel2", "Tezgâha tutunarak topuk yükseltme", "Tezgâha tutunarak dik durun. İki topuğunuzu birlikte kaldırın ve yavaşça inin. Başparmak ekleminiz ağrıyorsa yükselme miktarını azaltın.", "10 tekrar, 2–3 set")
_ex2("hv_sls", "sls", "Tek ayak üzerinde denge", "Tezgâha hafifçe tutunarak tek ayağınızın üzerinde durun. Ayağın küçük kaslarını ve dengeyi çalıştırır.", "20–30 saniye, her ayakla 3 kez")
EXT["hv_toe"] = ("Ayak başparmağını germe", "Oturun, ayağınızı diğer dizinizin üzerine alın. Başparmağınızı elinizle tutun ve eklemi her yöne nazikçe gerin. Hareketin sonunda ağrısız biçimde bekleyin, sonra bırakıp tekrarlayın.", "10–15 saniye tutun, birkaç tekrar")

_ex2("tf_hook", "tglide", "Kanca ve yumruk", "Parmaklarınız düz olsun. Parmak diplerini düz tutarak uçlarını kanca gibi kıvırın; sonra parmaklarınızı tam yumruk olacak şekilde kapatın ve yeniden açın.", "10 tekrar, günde 4–5 kez")
EXT["tf_warm"] = ("Ilık suda gevşetme", "Elinizi ılık suya sokun ve parmağınızı suyun içinde nazikçe düzeltin. Sabahları parmak takılı kalkıyorsa güne böyle başlamak hareketi kolaylaştırır. Zorlamayın.", "Sabahları ve gerektikçe")
EXT["tf_ice"] = ("Parmak dibine buz masajı", "Parmağınızın dibine biraz bebek yağı sürün. Bir buz küpünü streç filme ya da ince bir beze sarın ve parmak dibinin üzerinde, buz eriyene kadar sıkıca gezdirin. Amaç bölgedeki şişliği azaltmaktır.", "Buz eriyene kadar, günde 1 kez")
EXT["tf_table"] = ("Masa pozisyonu", "Parmaklarınız düz olsun. Yalnızca parmak diplerinizden öne doğru bükün; parmaklarınız masa tablası gibi düz kalsın. Sonra yeniden doğrultun.", "10 tekrar, günde 4–5 kez")
EXT["tf_passive"] = ("Diğer elle yumruğa getirme", "Sağlam elinizle, etkilenen elinizin parmaklarını nazikçe yumruk olacak şekilde kapatın; parmakların kendisi kasılmasın. Sonra bırakın. Kirişi zorlamadan eklem hareketini korur.", "5–10 tekrar, günde 4 kez")
EXT["tf_splint"] = ("Gece ateli", "El terapistinin verdiği ya da parmağın dibindeki hareketi sınırlayan kısa bir ateli gece boyunca takın. Kiriş ve içinden geçtiği halka dinlenir, sabahki takılma azalır. Cildiniz kızarır ya da atel vurursa terapistinize haber verin.", "Her gece; süresini terapistiniz belirler")

# ============================================================== HALLUKS VALGUS
HV_FAQ = [
 ("Ayak başparmağı çıkıntısı egzersizle ya da atelle düzelir mi?", "Hayır. Çıkıntıyı kendi başınıza yok edemez ya da ilerlemesini durduramazsınız; şekil bozukluğu ameliyat dışında kalıcı olarak düzeltilemez. Egzersizlerin ilerlemeyi önlediğine dair kanıt yok, gece atelleri için kanıt da zayıf. Uygun ayakkabı, ped ve tabanlık ise ağrıyı azaltabilir."),
 ("Hangi ayakkabıyı giymeliyim?", "Parmaklarınıza yetecek kadar geniş ve derin, alçak topuklu, bağcıklı ya da ayarlanabilir bantlı ayakkabılar en uygunudur. Yüksek topuklu, dar ve sivri burunlu ayakkabılardan kaçının. Ayakkabı alırken ayağınızın en geniş yerini, yani çıkıntının üzerini ölçtürün."),
 ("Ne zaman ameliyat düşünülür?", "Çıkıntı çok ağrılıysa ya da hayatınızı belirgin biçimde etkiliyorsa ve diğer yöntemler en az üç ay denenip yetersiz kaldıysa. Ameliyat yalnızca görünüşü düzeltmek için yapılmaz. Cochrane derlemesine göre ameliyat, tedavisiz izlemeye kıyasla ağrıyı klinik olarak anlamlı ölçüde azaltabiliyor; kanıtın kesinliği düşük."),
 ("Ameliyattan sonra iyileşme ne kadar sürer?", "Çoğu kişi aynı gün eve döner. En az iki hafta ayağı mümkün olduğunca yukarıda dinlendirmek gerekir; 6–8 hafta araç kullanılmaz, işe dönüş 2–12 hafta, spora dönüş 3–6 ay sürer. Ameliyattan sonra parmak daha sert ya da zayıf kalabilir, tam düz olmayabilir ve çıkıntı bazen yeniden oluşabilir."),
]

HV_SRC = [
 "Aneurin Bevan University Health Board. " + ext("https://abuhb.nhs.wales/files/patient-information-leaflets1/foot-care-podiatry/bunions-hallux-valgus-piu1440-pdf/", "Bunions (hallux valgus)") + ". Patient information leaflet PIU 1440. September 2026.",
 "Dias CGP, Godoy-Santos AL, Ferrari J, Ferretti M, Lenza M. " + ext("https://www.cochrane.org/evidence/CD013726_are-surgical-interventions-better-no-treatment-or-non-surgical-interventions-treating-hallux-valgus", "Surgical interventions for treating hallux valgus and bunions") + ". Cochrane Database Syst Rev. 2024;(7):CD013726.",
 "Gateshead Health NHS Foundation Trust. " + ext("https://www.gatesheadhealth.nhs.uk/wp-content/uploads/2023/09/Patient-Information-on-Bunions.pdf", "Patient information on bunions") + ". Leaflet IL784. October 2020.",
 "Livewell Southwest Podiatry Services. " + ext("https://www.livewellsouthwest.co.uk/wp-content/uploads/2025/10/Hallux-Abducto-Valgus-Bunions-A5.pdf", "Hallux abducto-valgus (bunions)") + ". Patient information leaflet. September 2025.",
 "NHS. " + ext("https://www.nhs.uk/conditions/bunions/", "Bunions") + ". Page last reviewed 12 June 2023.",
 "NHS Borders. " + ext("https://www.nhsborders.scot.nhs.uk/media/450778/Hallux-Valgus-Patient-Information-leaflet-March-2016.pdf", "Hallux valgus") + ". Patient information leaflet. March 2016.",
]

HV_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Halluks valgus: ayak başparmağı çıkıntısı</h1>
    <p class="lede">Halluks valgus, ayak başparmağının diğer parmaklara doğru yatması ve ekleminin iç yanda kemiksi bir çıkıntı yapmasıdır. Çıkıntı kendi başına yok edilemez ve egzersizle düzelmez; ama doğru ayakkabı, ped ve tabanlıkla ağrı çoğu zaman azaltılabilir. Ağrı hayatı belirgin biçimde etkiliyorsa ameliyat seçeneği vardır.</p>
    <p class="meta">Son güncelleme: 8 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>3 kat</b><span>Kadınlarda erkeklere göre daha sık; çoğu zaman ailede de var</span></div>
        <div class="stat"><b>25 çalışma</b><span>Ameliyatı inceleyen Cochrane derlemesi; 1.597 yetişkin</span></div>
        <div class="stat"><b>39 / 21</b><span>Bir yıl sonra ağrı puanı (100 üzerinden): tedavisiz izlem ve ameliyat</span></div>
        <div class="stat"><b>3–6 ay</b><span>Ameliyattan sonra spora dönüş için gereken süre</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Ayak başparmağının kökündeki eklemin hizası bozulur: Parmak ikinci parmağa doğru yatar, eklem iç yana doğru çıkıntı yapar. Çıkıntının büyüklüğü ile ağrı arasında doğrudan bir ilişki yoktur; büyük bir çıkıntı hiç ağrımayabilir.</p>
        <p class="soft">Çoğu zaman tek bir neden bulunmaz. Kalıtsal ayak yapısı en güçlü etkendir; romatoid artrit gibi eklem hastalıkları, içe basan ayak ve fazla kilo da rol oynar. Dar ve sivri burunlu ayakkabıların çıkıntıya yol açıp açmadığı tartışmalıdır; ama var olan çıkıntıyı sıkıştırıp ağrıttığı konusunda kaynaklar birleşiyor.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Başparmak kökünde, ayağın iç yanında sert bir çıkıntı</li>
          <li>Başparmağın diğer parmaklara doğru yönelmesi</li>
          <li>Çıkıntının üzerinde sertleşmiş, şiş ya da kızarmış cilt</li>
          <li>Ayakkabı giyince ve yürüyünce artan ağrı</li>
          <li>İkinci parmağın yerinden itilmesi, parmakların üst üste binmesi</li>
          <li>Ayağın ön tabanında ağrı</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ağrıyı azaltmak için</h2>
      <ul class="tx">
        <li><b>Ayakkabı</b><span>Geniş ve derin burunlu, alçak topuklu, bağcıklı ya da bantlı ayakkabı. Çıkıntıya baskı yapan dikiş ve sert yüzeylerden kaçının.</span></li>
        <li><b>Ped</b><span>Eczaneden alınan çıkıntı pedleri sürtünmeyi azaltır.</span></li>
        <li><b>Parmak arası silikon</b><span>Başparmağınızı ağrısız biçimde düzeltebiliyorsanız işe yarayabilir; bir hafta içinde yavaş yavaş alışın.</span></li>
        <li><b>Tabanlık</b><span>Ayağınız içe basıyorsa eklemdeki baskıyı azaltabilir; çıkıntıyı düzeltmez.</span></li>
        <li><b>Buz ve ağrı kesici</b><span>Beze sarılı buz torbasını bir seferde en fazla 5 dakika uygulayın; ilaç için hekiminize danışın.</span></li>
        <li><b>Kilo</b><span>Fazla kilonuz varsa vermek, başparmak eklemine binen yükü azaltır.</span></li>
      </ul>
      <div class="callout">
        <p>Bu önlemler çıkıntıyı tedavi etmez; ama ağrı, parmakların sıkışması ve ciltte açılma gibi ikincil sorunları azaltabilir. Etkilerini görmek için 6–12 hafta tanıyın.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ameliyat ne zaman?</h2>
      <p class="soft">Ameliyat, çıkıntı çok ağrılı olduğunda ya da hayatı belirgin biçimde etkilediğinde ve diğer yöntemler yeterince denendikten sonra düşünülür; yalnızca ayağın görünüşünü düzeltmek için yapılmaz. En sık uygulanan yöntemde çıkıntı alınır, kemik kesilerek düzeltilir ve vidalarla sabitlenir.</p>
      <p class="soft">25 çalışmayı (1.597 yetişkin) inceleyen Cochrane derlemesinde, ameliyatı tedavisiz izlemle karşılaştıran çalışmada bir yıl sonra ağrı puanı ameliyat olanlarda 100 üzerinden 21, izlenenlerde 39'du; işlevdeki kazanç daha küçüktü, yaşam kalitesinde fark görülmedi. Yazarlar kanıtın kesinliğini düşük buluyor; yeniden ameliyat ve yan etki oranları konusunda net bir şey söylenemiyor.</p>
      <div class="callout">
        <p>Ameliyat ayağı “eski hâline” getirmez: Parmak daha sert ya da zayıf kalabilir, tam düz olmayabilir, ağrı sürebilir ve çıkıntı bazen yeniden oluşur. Kararı bu beklentilerle, cerrahınızla birlikte verebilirsiniz.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Ayağı rahatlatan altı hareket</h2>
      <p class="soft">Dürüst olmak gerekirse: Egzersizlerin çıkıntıyı küçülttüğüne ya da ilerlemesini önlediğine dair kanıt yok. Bu hareketlerin amacı eklemi hareketli, baldırı esnek ve ayağın küçük kaslarını güçlü tutmaktır. İlk ikisi hastane broşürlerinden; diğerleri genel ayak güçlendirme hareketleridir. Ağrı yapan hareketi bırakın.</p>
      {ex_grid(["hv_toe", "hv_calf", "hv_short", "hv_press", "hv_heel", "hv_sls"])}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Halluks valgus için videolar</h2>
      <p class="soft">Hindistan'daki Manipal Hospitals'ın ve ortopedi cerrahı Dr. Chris Raynor'ın yer aldığı Human 2.0 Fitness kanalının YouTube videoları. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("YCmqXvTmfFI", "Halluks valgus tanıtım videosunu oynat", "Hallux Valgus Explained | Manipal Hospitals")}
          <h3>Halluks valgus nedir?</h3>
          <p>Bir ortopedi hekiminin hastalığı anlattığı video.</p>
        </div>
        <div class="vid">
          {vbox("RSefS_rHugY", "Ayak egzersizleri videosunu oynat", "BUNION EXERCISES with ortho surgeon Dr. Chris Raynor")}
          <h3>Ayak egzersizleri</h3>
          <p>Bir ortopedi cerrahının gösterdiği ayak egzersizleri.</p>
        </div>
      </div>
      <p class="meta">Videolar Manipal Hospitals ve Human 2.0 Fitness kanallarına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(HV_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime görünmeli?</h2>
      <p class="soft">Şu durumlarda bir hekime ya da ayak sağlığı uzmanına başvurun:</p>
      <ul class="dots redflags">
        <li>Evde önlemlere rağmen birkaç haftada azalmayan ağrı</li>
        <li>Günlük işlerinizi yapmanızı engelleyen ağrı</li>
        <li>Çıkıntının giderek büyümesi</li>
        <li>Diyabetiniz varsa: ayak sorunları daha ciddi seyredebilir</li>
        <li>Ayakkabı sürtünmesiyle açıklanamayan kızarıklık, sıcaklık ve şişlik</li>
        <li>Gelip geçen, kızarık, sıcak ve şiş bir eklem (gut olabilir)</li>
      </ul>
      {CTA_CARD("Ayak başparmağı çıkıntısına bağlı ağrınız", "halluks valgus")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(HV_SRC)}
    </div>
  </section>
</main>'''

page("halluks-valgus.html", "Halluks Valgus: Ayak Başparmağı Çıkıntısı",
     "Ayak başparmağı çıkıntısı (halluks valgus, bunyon) neden olur, egzersizle ya da atelle düzelir mi? Ayakkabı seçimi, ağrıyı azaltan önlemler, ameliyat için kanıt ve ayağı rahatlatan altı hareket.",
     "halluks-valgus.html", NECK_CSS, HV_BODY, YT_JS,
     seo_title="Halluks Valgus (Ayak Başparmağı Çıkıntısı): Ayakkabı, Egzersiz, Ameliyat | İhsan Eren",
     condition="Halluks valgus", faq_items=HV_FAQ)

# ============================================================== TETİK PARMAK
TF_FAQ = [
 ("Tetik parmak kendiliğinden geçer mi?", "Hafif olgular birkaç haftada tedavisiz düzelebilir. Bazılarında ise ara ara yineler ya da süreğenleşir. Parmak ne kadar uzun süre bükülü takılı kalırsa kiriş o kadar tahriş olur; bu yüzden erken dönemde eli dinlendirmek, gece ateli ve nazik hareketler önemlidir. Öneriler uygulandığında düzelme 12 haftayı bulabilir."),
 ("Kortizon iğnesi işe yarar mı?", "İskoçya'daki ulusal hasta broşürüne göre iğne, olguların yaklaşık %70–80'inde ağrıyı ve takılmayı gideriyor; diyabeti olanlarda başarı daha düşük. Rastgele kontrollü araştırma ise az: 2009 tarihli Cochrane derlemesi 63 kişilik iki küçük çalışma buldu. Derlemenin hasta özetine göre kortizon eklenen iğneden 100 kişinin 37'si, yalnızca uyuşturucu içeren iğneden 100 kişinin 17'si yarar gördü; bir çalışmada etki 4 aya kadar sürdü. Tetik parmak ilerledikçe iğnenin başarısız olma olasılığı artıyor."),
 ("Sabahları takılan parmak için ne yapabilirim?", "Belirtiler çoğu kişide sabahları daha belirgindir. Parmağın dibindeki hareketi gece boyunca sınırlayan kısa bir atel, sabahki takılmayı azaltmada çok etkilidir. Uyanınca elinizi ılık suya sokup parmağınızı nazikçe açmak da hareketi kolaylaştırır; zorla açmayın."),
 ("Kaç kez iğne yapılabilir?", "Bunun kesin bir sınırı yoktur; kararı hekiminiz verir. 2023 tarihli bir derlemede aktarılan bir çalışmada, ikinci ve üçüncü iğnelerin yaklaşık %39'u en az 1,5 yıl süren rahatlama sağladı. İğnelere rağmen takılma sürerse ameliyat seçeneği konuşulur."),
 ("Çocuklarda da olur mu?", "Evet. Çocuklarda tetik başparmak ya da parmak bebeklik döneminde ve daha büyük çocuklarda görülebilir; doğumda nadiren fark edilir. Genellikle ağrısızdır ve eli kullanmayı engellemez. Tedavisiz düzelebilir ama bu 1–2 yıl sürebilir; atelin ya da egzersizin fark yarattığına dair kanıt yoktur. Düzelmeyen az sayıdaki çocukta ameliyat yapılır; bir NHS broşüründe bu ameliyatın 3 yaşından önce yapılmadığı belirtiliyor."),
 ("Ameliyat gerekir mi?", "Çoğu kişide gerekmez. Diğer yöntemler işe yaramazsa, kirişin geçtiği halka küçük bir işlemle gevşetilir; çoğunlukla lokal anesteziyle yapılır. Küçük bir pansuman 10–14 gün kalır, el aynı gün hafif işlerde kullanılabilir. Yineleme seyrektir."),
]

TF_SRC = [
 "Bridges TN, Ohliger E, Kistler JM. " + ext("https://surgicoll.scholasticahq.com/article/68065-trigger-finger-evaluation-management-and-outcomes", "Trigger finger: evaluation, management, and outcomes") + ". SurgiColl. 2023;1(1). doi:10.58616/surgicoll.00003.",
 "Clapham PJ, Chung KC. A historical perspective of the Notta's node in trigger fingers. J Hand Surg Am. 2009;34:1518-1522. Notta ve Lorthioir hakkında: " + ext("https://jbumdc.bahria.edu.pk/index.php/ojs/article/view/155", "Qureshi ve ark. JBUMDC. 2016;6(1):34-37") + ".",
 "Fiorini HJ, Tamaoki MJ, Lenza M, Gomes dos Santos JB, Faloppa F, Belloti JC. " + ext("https://www.cochrane.org/evidence/CD009860_surgery-trigger-finger", "Surgery for trigger finger") + ". Cochrane Database Syst Rev. 2018;(2):CD009860.",
 "Lorthioir J. Surgical treatment of trigger-finger by a subcutaneous method. J Bone Joint Surg Am. 1958;40-A:793-795.",
 "NHS Fife. " + ext("https://www.nhsfife.org/services/all-services/patient-advice/trigger-thumb-finger-children-and-young-people/", "Trigger thumb / finger – children and young people") + ". Version 4, reviewed August 2024.",
 "NHS. " + ext("https://www.nhs.uk/conditions/trigger-finger/", "Trigger finger") + ". Page last reviewed 17 November 2025.",
 "NHS Scotland. " + ext("https://rightdecisions.scot.nhs.uk/media/ww4d10oz/national-trigger-finger-patient-information-leaflet.pdf", "Trigger finger: national patient information leaflet") + ".",
 "North Tees and Hartlepool NHS Foundation Trust. " + ext("https://www.nth.nhs.uk/resources/hand-therapy-trigger-finger/", "Hand therapy: trigger finger") + ". Leaflet PIL1517. Reviewed 30 March 2026.",
 "Peters-Veluthamaningal C, van der Windt DAWM, Winters JC, Meyboom-de Jong B. " + ext("https://www.cochrane.org/evidence/CD005617_local-corticosteroid-injection-trigger-finger", "Corticosteroid injection for trigger finger in adults") + ". Cochrane Database Syst Rev. 2009;(1):CD005617.",
 "St George's University Hospitals NHS Foundation Trust. " + ext("https://www.stgeorges.nhs.uk/wp-content/uploads/2021/09/Trigger-Finger.pdf", "Trigger finger") + ". Hand therapy leaflet THE_TF_02. April 2020.",
 "Torbay and South Devon NHS Foundation Trust. " + ext("https://www.torbayandsouthdevon.nhs.uk/uploads/25909.pdf", "Trigger finger") + ". Hand Physiotherapy leaflet 25909. September 2025.",
]

TF_TL = [
 ("1850", "Notta, parmağı büken kirişte takılmaya yol açan kalınlaşmayı dört yetişkin hastada tanımladı; bu kalınlaşma bugün \"Notta nodülü\" olarak anılıyor."),
 ("1958", "Lorthioir, kirişin geçtiği halkanın deri altından, büyük bir kesi yapılmadan gevşetildiği yöntemi (perkütan gevşetme) 52 hastada tanımladı."),
 ("2009", "Cochrane derlemesi: kortizon iğnesine dair yalnızca iki küçük çalışma (63 kişi) bulundu; kortizon eklenen iğne, yalnızca uyuşturucu içeren iğneden daha etkiliydi."),
 ("2018", "Cochrane derlemesi (14 çalışma, 1.260 kişi): açık ameliyat, kortizon iğnesine göre 6–12 ayda yinelemeyi azaltabilir (düşük kalitede kanıt) ama ilk hafta daha fazla ağrıya yol açıyor."),
 ("2023", "Bir derleme (SurgiColl): ateller için hastaların bildirdiği başarı oranları %47 ile %93 arasında; tek kortizon iğnesiyle başarı %45 ile %80 arasında değişiyor."),
]

TF_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Tetik parmak</h1>
    <p class="lede">Tetik parmak, parmağı büken kirişin kalınlaşıp içinden geçtiği halkaya takılmasıdır: Parmak bükülü kalır, açarken “tık” diye atar. Zararlı bir hastalık değildir ama eli kullanmayı zorlaştırır. Hafif olgular dinlendirme, gece ateli ve nazik hareketlerle düzelebilir; geçmezse iğne ve küçük bir ameliyat seçenekleri vardır.</p>
    <p class="meta">Son güncelleme: 6 Kasım 2026</p>
  </div>
</header>
<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>100'de 2–3</b><span>Hayatının bir döneminde tetik parmak gelişen kişi oranı</span></div>
        <div class="stat"><b>40 yaş üstü</b><span>Daha sık; diyabet ve romatoid artrit riski artırıyor</span></div>
        <div class="stat"><b>%70–80</b><span>Kortizon iğnesinin ağrı ve takılmayı giderdiği olgu oranı (ulusal hasta broşürü)</span></div>
        <div class="stat"><b>12 hafta</b><span>Atel ve egzersizle düzelmenin alabileceği süre</span></div>
      </div>
      {g_toc([("nedir", "Nedir?"), ("tani", "Nasıl tanınır?"), ("tedavi", "Tedavi"), ("tarihce", "Geçmişten bugüne"), ("egzersizler", "Evde uygulamalar"), ("videolar", "Videolar"), ("sss", "Sık sorulan sorular"), ("uyari", "Uyarı işaretleri")])}
    </div>
  </section>
  <section id="nedir">
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Parmakları büken kirişler, kemiğe tutunan küçük tünellerin içinden kayar. Kiriş ya da kılıfı şişip kalınlaştığında tünelin ağzında takılır; bazen küçük bir yumru oluşur. Parmak bükülürken yumru tünelden geçer, açılırken takılır ve birden kurtulur; tetik çekilip bırakılmış gibi.</p>
        <p class="soft">Çoğu zaman neden bilinmez; bazen bir yaralanmadan sonra başlar. 40 yaşın üzerinde, kadınlarda, diyabeti ya da romatoid artriti olanlarda daha sık görülür. Makas ya da budama makası kullanmak gibi tekrarlı, sıkı kavrama gerektiren işler de tetikleyebilir.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Parmağın ya da başparmağın bükülü konumda takılı kalması</li>
          <li>Açarken tıklama ya da atma hissi</li>
          <li>Parmak dibinde, avuç içinde ağrı ve hassasiyet</li>
          <li>Parmak dibinde, parmakla birlikte oynayan küçük bir şişlik</li>
          <li>Parmağı düzeltmek için diğer eli kullanmak zorunda kalma</li>
          <li>Belirtilerin sabahları daha belirgin olması</li>
        </ul>
      </div>
    </div>
  </section>
  <section id="tani">
    <div class="wrap">
      <h2>Nasıl tanınır?</h2>
      <p class="soft">Tanı, yakınmalarınız ve elinizin muayenesiyle konur. Muayenede avuç içinde, etkilenen parmağın dibinde hassasiyet aranır; bazen parmakla birlikte hareket eden küçük bir yumru ele gelir. Parmak bükülüp açılırken takılma ya da atma görülebilir.</p>
      <h3 class="g-h3">Dereceler (Green sınıflaması)</h3>
      <ul class="tx">
        <li><b>I. derece</b><span>Takılma öncesi dönem: ağrı, takılma hissi ve parmak dibinde hassasiyet.</span></li>
        <li><b>II. derece</b><span>Parmak takılıyor ama kendi kendinize açabiliyorsunuz.</span></li>
        <li><b>III. derece</b><span>Takılan parmağı ancak diğer elinizle açabiliyorsunuz (IIIA) ya da parmağı tam bükemiyorsunuz (IIIB).</span></li>
        <li><b>IV. derece</b><span>Takılmayla birlikte parmağın orta ekleminde kalıcı bükülü kalma.</span></li>
      </ul>
      <p class="soft">Derece, tedavi seçimine yön verir. 2023 tarihli bir derlemeye göre tetik parmak ilerledikçe kortizon iğnesinin başarısız olma olasılığı artıyor.</p>
    </div>
  </section>
  <section id="tedavi">
    <div class="wrap">
      <h2>İlk adım: kirişi dinlendirmek</h2>
      <p class="soft">Belirtileri artıran işleri, özellikle tekrarlı ve sıkı kavramayı, düzelene kadar azaltın. Parmak ne kadar uzun süre bükülü takılı kalırsa kiriş o kadar tahriş olup kalınlaşır; bu yüzden erken davranmak önemlidir.</p>
      <p class="soft">Gece ateli bu dönemin en etkili aracıdır: Parmağın dibindeki hareketi sınırlayan kısa bir atel, kirişi ve halkayı dinlendirir, sabahki takılmayı azaltır. Gece boyunca takılır; el terapisti size uygun olanı yapabilir. Geceleri parmak dibine iltihap giderici jel sürmek de yardımcı olabilir; önce hekiminize danışın.</p>
      <div class="callout">
        <p>Atel ve hareketlerle düzelme 12 haftayı bulabilir. Parmak sürekli takılıyorsa ya da düzeltmek için diğer elinizi kullanmak zorunda kalıyorsanız kortizon iğnesi düşünülür; iğne de yetmezse halkayı gevşeten küçük bir ameliyat yapılır.</p>
      </div>
    </div>
  </section>
  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <ul class="tx">
        <li><b>Dinlendirme</b><span>Tekrarlı ve sıkı kavrama gerektiren işleri azaltmak.</span></li>
        <li><b>Gece ateli</b><span>Parmağı düz tutarak kirişi dinlendirir; hafif ve gece olan takılmalarda çok etkilidir.</span></li>
        <li><b>Hareket</b><span>Kirişin kaymasını koruyan nazik hareketler, günde 4–5 kez.</span></li>
        <li><b>İlaç</b><span>Ağrı için ağrı kesici ya da iltihap giderici jel; hekiminize danışın.</span></li>
        <li><b>Kortizon iğnesi</b><span>Şişliği azaltır; diyabeti olanlarda başarı daha düşüktür.</span></li>
        <li><b>Ameliyat</b><span>Diğer yöntemler işe yaramadığında; lokal anesteziyle, günübirlik.</span></li>
      </ul>
      <h3 class="g-h3">Tedavi seçenekleri: kanıtlar ne diyor?</h3>
      <p class="soft">Sistematik derlemelerin bulguları. Kanıtın kalitesi belirtildiği yerde parantez içinde verilmiştir; tedavi kişiye ve tetik parmağın derecesine göre seçilir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Atel</h3><dl><dt>Derleme (2023)</dt><dd>Hastaların bildirdiği başarı oranları %47 ile %93 arasında; çalışmalarda atel tipi ve sabitlenen eklem farklıydı. Önce 6 haftalık bir deneme, belirtiler sürerse 12 haftaya uzatma öneriliyor.</dd></dl></div>
        <div class="kind"><h3>Kortizon iğnesi</h3><dl><dt>Cochrane (2009)</dt><dd>İki küçük çalışma (63 kişi): kortizon eklenen iğneden 100 kişinin 37'si, yalnızca uyuşturucu içeren iğneden 100 kişinin 17'si yarar gördü. Çalışmaların yöntem kalitesi düşüktü.</dd></dl></div>
        <div class="kind"><h3>Açık ameliyat ya da iğne</h3><dl><dt>Cochrane (2018)</dt><dd>6–12 ayda yineleme 100 kişide 7'ye karşı 39 (düşük kalite); ilk hafta ağrı 100 kişide 68'e karşı 19. Belirtilerin geçmesi 92'ye karşı 61 (çok düşük kalite).</dd></dl></div>
        <div class="kind"><h3>Deri altından ya da açık ameliyat</h3><dl><dt>Cochrane (2018)</dt><dd>Beş çalışma iki yöntemi karşılaştırdı; kanıtın kalitesi düşük ya da çok düşük olduğundan birinin diğerinden üstün olup olmadığı belirsiz.</dd></dl></div>
      </div>
    </div>
  </section>
  <section id="tarihce">
    <div class="wrap">
      <p class="eyebrow">Geçmişten bugüne</p>
      <h2>İlk tanımdan bugünkü tedavilere</h2>
      <p class="soft">Tetik parmak 19. yüzyılın ortasında tanımlandı. 20. yüzyılda halkayı deri altından gevşetme yöntemi geliştirildi; son yıllardaki derlemeler ise atelin, iğnenin ve ameliyatın yerini karşılaştırdı.</p>
      {g_tl(TF_TL)}
    </div>
  </section>
  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde bakım</p>
      <h2>Tetik parmak için altı uygulama</h2>
      <p class="soft">Hareketleri zorlamadan, parmağı “attırmadan” yapın. Takılma oluyorsa hareketi küçültün. Hepsi İngiltere'deki hastanelerin el terapisi broşürlerinden alındı.</p>
      {ex_grid(["tf_warm", "tf_ice", "tf_hook", "tf_table", "tf_passive", "tf_splint"])}
    </div>
  </section>
  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Tetik parmak için videolar</h2>
      <p class="soft">ABD'deki Mayo Clinic'in ve İngiltere'de hekim olan Dr. James O'Donovan'ın YouTube kanallarından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("58xQr9tOx24", "Tetik parmak tanıtım videosunu oynat", "Trigger Finger Overview - Mayo Clinic")}
          <h3>Tetik parmak nedir?</h3>
          <p>Hastalığı ve tedavi seçeneklerini özetleyen video.</p>
        </div>
        <div class="vid">
          {vbox("89ACJJ-jsfA", "Tetik parmak egzersizleri videosunu oynat", "Trigger Finger Pain Relief Exercises | Doctor and Physio led")}
          <h3>Rahatlatan egzersizler</h3>
          <p>Bir hekim ve fizyoterapistin anlattığı egzersiz videosu.</p>
        </div>
      </div>
      <p class="meta">Videolar Mayo Clinic ve Doctor O'Donovan kanallarına aittir.</p>
    </div>
  </section>
  <section id="sss">
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(TF_FAQ)}
    </div>
  </section>
  <section id="uyari">
    <div class="wrap">
      <h2>Ne zaman hekime görünmeli?</h2>
      <p class="soft">Aşağıdaki durumlarda gecikmeden başvurun; ne kadar acil olduğu her grubun başında belirtilmiştir.</p>
      <p class="soft"><strong>Aynı gün bir hekime:</strong></p>
      <ul class="dots redflags">
        <li>Parmakta kızarıklık, sıcaklık ve şişlikle birlikte ateş</li>
        <li>Yaralanmadan sonra parmağı hiç bükememe ya da açamama</li>
      </ul>
      <p class="soft"><strong>Birkaç gün içinde bir hekime:</strong></p>
      <ul class="dots redflags">
        <li>Parmağın bükülü kilitlenip hiç açılmaması</li>
        <li>Düzelmeyen ya da giderek artan belirtiler</li>
        <li>Günlük işlerinizi yapmanızı engelleyen belirtiler</li>
      </ul>
      {CTA_CARD("Tetik parmağa bağlı el şikâyetleriniz", "tetik parmak")}
    </div>
  </section>
  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(TF_SRC)}
    </div>
  </section>
</main>'''

page("tetik-parmak.html", "Tetik Parmak",
     "Tetik parmak neden olur, nasıl tanınır ve derecelendirilir, kendiliğinden geçer mi? Gece ateli, kortizon iğnesi ve ameliyat için kanıtlar, kısa tarihçe, çocuklarda tetik başparmak ve evde altı uygulama.",
     "tetik-parmak.html", NECK_CSS, TF_BODY, YT_JS,
     seo_title="Tetik Parmak: Atel, Egzersiz, İğne ve Ameliyat | İhsan Eren",
     condition="Tetik parmak", faq_items=TF_FAQ)

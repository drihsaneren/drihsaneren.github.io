# -*- coding: utf-8 -*-
# Yeni rehberler (13): kalça yan ağrısı (trokanterik ağrı sendromu) ve lenfödem.
# cond13_part.py'den sonra exec edilir. Videolar: Somerset NHS Foundation Trust, UC San Diego Health, Cancer Research UK (oEmbed ile doğrulandı).
# Lenfödem sayfasında bilerek CTA_CARD yok: lenfödem tedavisi özel eğitim gerektirir (kullanıcı isterse eklenir).

# ---- yeni çizimler
# Yatarak, uyluklara bağlı kemere karşı dizleri açma (yandan; hareket yok, basınç var)
SV["gt_belt"] = fig(GRD +
    '<circle class="hd" cx="12" cy="100" r="7"/>'
    '<path class="fig" d="M22 107 H44"/>'
    '<path class="fig" d="M20 104 L58 104 L76 84 L86 108"/>'
    '<path d="M65 90 L78 97" stroke="#C8963E" stroke-width="6" stroke-linecap="round"/>'
    '<g><animate attributeName="opacity" values="0.15;1;0.15" dur="3.2s" repeatCount="indefinite"/>'
    '<path d="M60 76 l-5 -6 M72 70 v-8 M84 76 l5 -6" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round"/></g>',
    "Kemere karşı açma")
# Omuz kaldırma (önden)
SV["ly_shrug"] = fig(GRD +
    f'<path class="fig" d="M60 40 V80 {LEGS_F} M60 32 V40"/>'
    '<circle class="hd" cx="60" cy="22" r="8"/>'
    f'<g>{anim_t("0 0;0 -5;0 0")}<path class="fig hl" d="M44 40 H76"/><path class="fig" d="M44 40 L40 62 L42 78 M76 40 L80 62 L78 78"/></g>'
    '<path d="M30 36 V24 M26 28 L30 24 L34 28 M90 36 V24 M86 28 L90 24 L94 28" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "Omuz kaldırma")
# Elleri dizlerden omuzlara (yandan, oturarak)
SV["ly_arm"] = fig(GRD + CHAIR_L +
    '<path class="fig" d="M46 74 H80 V112"/>'
    '<path class="fig" d="M46 74 L48 42"/><circle class="hd" cx="50" cy="33" r="8"/>'
    f'<path class="fig hl" d="M48 48 L58 62 L74 70">{anim_d("M48 48 L58 62 L74 70;M48 48 L63 58 L55 45;M48 48 L58 62 L74 70")}</path>',
    "Elleri omuzlara")

_ex2("gt_wall", "sabd", "Duvara karşı kalçayı yana bastırma", "Duvarın yanında, ağrılı tarafınız duvara dönük durun. O taraftaki dizinizi bükün ve dizinizin dış yanını duvara bastırın. Üzerinde durduğunuz bacağın dizi içe dönmesin.", "10 saniye tutun, 10 tekrar")
_ex2("gt_bridge", "bridge", "Köprü", "Sırtüstü yatın, dizleriniz bükülü olsun. Karın ve kalça kaslarınızı sıkın; leğeninizi yavaşça kaldırın ve kontrollü biçimde indirin. Beliniz çukurlaşmasın.", "10 tekrar")
_ex2("gt_squat", "sts", "Mini çömelme", "Ayaklarınız kalça genişliğinde açık dursun. Bir sandalyeye oturacakmış gibi dizlerinizi ve kalçanızı bükün; dizleriniz ayak parmaklarınızın hizasında kalsın. Sonra iterek doğrulun.", "10 tekrar")
_ex2("gt_side", "sidestep", "Lastik bantla yana adım", "Dizlerinizin çevresine bir lastik bant takın. Yana doğru, kalça genişliğinden biraz fazla bir adım atın; sonra diğer ayağınızı kalça genişliğine getirin, ayak bileklerinizi birleştirmeyin. Bant hep gergin kalsın.", "Her yöne 10 adım")
_ex2("gt_sls", "sls", "Leğen düz, tek ayak üzerinde durma", "Bir tezgâha hafifçe tutunun ve ağrılı bacağınızın üzerinde durun. Leğen kemiğiniz bir yana düşmesin, kalçanız dışarı kaymasın; aynada kontrol edebilirsiniz. Ağrı artıyorsa süreyi kısaltın.", "10 saniye, 5 tekrar")
EXT["gt_belt"] = ("Yatarak dizleri kemere karşı açma", "Sırtüstü yatın, dizleriniz bükülü olsun. Uyluklarınızın çevresine bir kemer ya da lastik bant bağlayın. Dizlerinizi, kemeri gerecek kadar nazikçe dışa doğru itin ve öylece tutun; bacaklarınız yerinden oynamaz.", "10 saniye tutun, 10 tekrar")

_ex2("ly_breath", "plb", "Derin karın nefesi", "Omuzlarınızı ve göğsünüzün üst kısmını gevşetin. Bir elinizi kaburgalarınızın hemen altına koyun. Burnunuzdan yavaş ve derin bir nefes alın, karnınız yükselirken elinizin kalktığını hissedin; ağzınızdan yavaşça verin. Diğer hareketlere her zaman bununla başlayın.", "5 nefes")
_ex2("ly_fist", "tglide", "Yumruk yapıp parmakları açma", "Elinizi yumruk yapın, sonra parmaklarınızı olabildiğince açın. Ardından başparmağınızı sırayla her parmağınızın ucuna değdirin.", "5–10 tekrar")
_ex2("ly_ball", "grip", "Top sıkma", "Yumuşak bir topu avucunuzda ya da iki elinizin arasında yavaşça sıkın ve bırakın. Kas kasılmaları lenf sıvısının damarlarda ilerlemesine yardım eder.", "5–10 tekrar")
_ex2("ly_walk", "walk", "Yürüyüş", "Uzun süredir hareketsizseniz başlamanın en iyi yolu yürüyüştür. Kısa mesafeyle başlayıp yavaş yavaş artırın. Bası giysiniz varsa egzersiz sırasında giyin; egzersiz sırasında ve sonrasında şiş bölgeyi kontrol edin.", "Her gün, azar azar artırarak")
EXT["ly_shrug"] = ("Omuz kaldırma ve çevirme", "Dik oturun. Omuzlarınızı kulaklarınıza doğru kaldırın, sonra bırakın. Ardından omuzlarınızı önce öne, sonra arkaya doğru çevirin.", "5–10 tekrar")
EXT["ly_arm"] = ("Elleri dizlerden omuzlara", "Dik oturun, elleriniz dizlerinizde olsun. Ellerinizi omuzlarınıza götürün, sonra kollarınızı rahat ettiğiniz kadar yukarı kaldırıp yeniden dizlerinize indirin. Ağrı olmamalı; hafif bir gerilme hissi normaldir.", "5–10 tekrar")

# ============================================================== KALÇA YAN AĞRISI
GT_FAQ = [
 ("Kalça yan ağrısı bursit midir?", "Çoğu zaman tek başına bursit değildir. Ağrının kaynağı genellikle kalçanın yan tarafındaki kemik çıkıntısına yapışan kirişlerin aşırı yüklenmesidir (tendinopati); bazen oradaki kesecik (bursa) de iltihaplanır. Bu yüzden bugün “büyük trokanter ağrı sendromu” adı kullanılıyor."),
 ("Kortizon iğnesi işe yarar mı?", "204 kişilik LEAP çalışmasında iğne, sekizinci haftada beklemekten daha iyi, eğitim ve egzersizden ise daha kötü sonuç verdi. Bir yıl sonra iğne yapılanlarla bekleyenler arasında anlamlı fark kalmadı. Bu yüzden iğne ilk seçenek sayılmıyor; ağrı egzersiz yapmayı engelleyecek kadar şiddetliyse kısa süreli rahatlama için düşünülebilir."),
 ("Kalça yan ağrısı ne kadar sürede geçer?", "Sabır gerektirir: Toparlanma çoğu zaman 6–12 ay sürer. Yine de LEAP çalışmasında eğitim ve egzersiz alanların yaklaşık dörtte üçü sekizinci haftada belirgin biçimde iyileştiğini bildirdi. Alevlenme olursa tekrarları azaltın ya da birkaç gün ara verip yeniden başlayın."),
 ("Hangi yanıma yatmalıyım?", "Ağrılı tarafın üzerine yatmayın. Sırtüstü yatıp dizlerinizin altına yastık koyabilir ya da sağlam yanınıza yatıp dizlerinizin arasına yastık yerleştirebilirsiniz; böylece üstteki bacak öne düşmez ve kalçanın yanı gerilmez."),
]

GT_SRC = [
 "Mellor R, Bennell K, Grimaldi A, et al. " + ext("https://www.bmj.com/content/361/bmj.k1662", "Education plus exercise versus corticosteroid injection use versus a wait and see approach on global outcome and pain from gluteal tendinopathy: prospective, single blinded, randomised clinical trial") + ". BMJ. 2018;361:k1662.",
 "NHS Fife. " + ext("https://www.nhsfife.org/services/all-services/patient-advice/greater-trochanteric-pain-syndrome/", "Greater trochanteric pain syndrome (GTPS)") + ". Fife Musculoskeletal Physiotherapy. February 2025.",
]

GT_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Kalça yan ağrısı (trokanterik bursit)</h1>
    <p class="lede">Kalçanın dış yanındaki ağrı çoğunlukla “bursit” diye bilinir; oysa asıl sorun genellikle kalçanın yan kaslarını kemiğe bağlayan kirişlerin aşırı yüklenmesidir. Yan yatınca, merdiven çıkarken ve uzun yürüyünce artar. 204 kişilik bir çalışmada eğitim ve egzersiz, hem kortizon iğnesinden hem de beklemekten daha iyi sonuç verdi.</p>
    <p class="meta">Son güncelleme: 7 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>4'te 1</b><span>50 yaşın üzerindeki kadınlarda görülme sıklığı (BMJ, 2018)</span></div>
        <div class="stat"><b>204 kişi</b><span>Eğitim ve egzersizi, kortizon iğnesini ve beklemeyi karşılaştıran LEAP çalışması</span></div>
        <div class="stat"><b>%77 / %58 / %29</b><span>8. haftada belirgin iyileşme: eğitim ve egzersiz, iğne, bekleme</span></div>
        <div class="stat"><b>%79 / %58 / %52</b><span>Bir yıl sonra belirgin iyileşme: aynı sırayla</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Kalçanın yan tarafında, elinizle hissedebildiğiniz kemik çıkıntısının (büyük trokanter) üzerindeki dokuların tahriş olmasıdır. Çoğu zaman neden, oraya yapışan kalça yan kaslarının kirişlerinin taşıyabileceğinden fazla yüklenmesidir; bazen bölgedeki kesecik (bursa) de iltihaplanır.</p>
        <p class="soft">En sık orta yaşlı kadınlarda görülür ama her yaşta ortaya çıkabilir. Düşme gibi doğrudan bir darbe, kalça kaslarının zayıflığı, uzun süreli yürüyüş ya da koşu ve fazla kilo zemin hazırlar; çoğu zaman da belirgin bir neden bulunmaz.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Kalçanın ve uyluğun dış yanında ağrı</li>
          <li>Ağrılı tarafın üzerine yatınca ağrı</li>
          <li>Yürürken zorlanma</li>
          <li>Merdiven inip çıkarken ağrı</li>
          <li>Kemik çıkıntısının üzerine bastırınca hassasiyet</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>İğne mi, egzersiz mi, beklemek mi?</h2>
      <p class="soft">Avustralya'da yapılan LEAP çalışması bu soruyu doğrudan sınadı. En az üç aydır kalça yan ağrısı olan, 35–70 yaş arasındaki 204 kişi üç gruba ayrıldı: sekiz hafta boyunca fizyoterapistle eğitim ve egzersiz, tek bir kortizon iğnesi ya da yalnızca bilgilendirme ve bekleme.</p>
      <p class="soft">Sekizinci haftada “belirgin biçimde iyileştim” diyenlerin oranı eğitim ve egzersiz grubunda %77, iğne grubunda %58, bekleyenlerde %29'du. Bir yıl sonra oranlar %79, %58 ve %52 oldu: Eğitim ve egzersiz üstünlüğünü korudu, iğne ile bekleme arasındaki fark ise anlamlı olmaktan çıktı. Ağrı şiddeti bir yıl sonra iğne ve egzersiz gruplarında benzerdi. Ciddi bir yan etki bildirilmedi.</p>
      <div class="callout">
        <p>Çalışmadaki program iki parçadan oluşuyordu: kirişi neyin yorduğunu öğrenip yükü ayarlamak ve kalça yan kaslarını güçlendiren, günde 4–6 hareketlik bir ev programı. Yani egzersiz kadar, gün içindeki duruş ve alışkanlıklar da tedavinin parçası.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Kalçayı rahatlatan alışkanlıklar</h2>
      <ul class="tx">
        <li><b>İki ayağa eşit basın</b><span>Ayakta dururken ağırlığınızı tek bacağa verip kalçanızı yana çıkarmayın.</span></li>
        <li><b>Bacak bacak üstüne atmayın</b><span>Otururken dizlerinizi yan yana tutun; alçak koltuklardan kaçının.</span></li>
        <li><b>Ağrılı yanınıza yatmayın</b><span>Sırtüstü yatıp dizlerinizin altına ya da sağlam yanınıza yatıp dizlerinizin arasına yastık koyun.</span></li>
        <li><b>Hareketi bırakmayın</b><span>Ağrıyı artıran etkinlikleri azaltın ama hareketsiz kalmayın; merdivende tırabzanı kullanın.</span></li>
        <li><b>Kilo</b><span>Fazla kilonuz varsa vermek, kalçanın dış yanına binen yükü azaltır.</span></li>
        <li><b>Soğuk uygulama</b><span>Araya nemli bir havlu koyarak 5–10 dakika, günde iki üç kez buz uygulayabilirsiniz.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Kalça yan ağrısı için altı egzersiz</h2>
      <p class="soft">Hareketler sırasında hafif bir rahatsızlık kabul edilebilir; ağrı şiddetli olmamalı ve uzun sürmemelidir. Ağrı artarsa tekrar sayısını ya da zorluğu azaltın. Egzersizden bir iki gün sonra kaslarda hissedilen yorgunluk ağrısı normaldir.</p>
      {ex_grid(["gt_belt", "gt_wall", "gt_bridge", "gt_squat", "gt_side", "gt_sls"])}
      <div class="callout">
        <p>Alevlenmeler olabilir; o günlerde tekrarları azaltın ya da birkaç gün ara verip yeniden başlayın. Ağrınız şiddetliyse hareketleri bırakıp fizyoterapistinizle konuşun.</p>
      </div>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Kalça yan ağrısı için videolar</h2>
      <p class="soft">İngiltere'deki Somerset NHS Foundation Trust'ın ve ABD'deki UC San Diego Health'in YouTube kanallarından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("z9w5axHITms", "Trokanterik ağrı sendromu videosunu oynat", "Greater trochanteric pain syndrome")}
          <h3>Trokanterik ağrı sendromu</h3>
          <p>Hastanenin fizyoterapi ekibinin hazırladığı bilgilendirme videosu.</p>
        </div>
        <div class="vid">
          {vbox("xqPew4-Pq54", "Evde egzersizler videosunu oynat", "Greater Trochanteric Bursitis Home Exercises | UC San Diego Health")}
          <h3>Evde egzersizler</h3>
          <p>Trokanterik bursit için ev egzersizlerini gösteren video.</p>
        </div>
      </div>
      <p class="meta">Videolar Somerset NHS Foundation Trust ve UC San Diego Health kanallarına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(GT_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Düşme ya da darbeden sonra bacağınızın üzerine basamıyorsanız (acil)</li>
        <li>Kalçada ağrıyla birlikte ateş, kızarıklık ve sıcaklık</li>
        <li>Dinlenirken ve gece hiç geçmeyen ağrı, açıklanamayan kilo kaybı</li>
        <li>Bacakta uyuşma, karıncalanma ya da güçsüzlük</li>
        <li>Ağrı kasıkta hissediliyor ve kalça hareketleri giderek kısıtlanıyorsa</li>
      </ul>
      {CTA_CARD("Kalça yan ağrınız", "kalça yan ağrısı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(GT_SRC)}
    </div>
  </section>
</main>'''

page("kalca-yan-agrisi.html", "Kalça Yan Ağrısı (Trokanterik Bursit)",
     "Kalçanın dış yanındaki ağrı neden olur? Trokanterik bursit denen ağrıda kortizon iğnesi mi, egzersiz mi daha iyi? Rahatlatan alışkanlıklar, yatış pozisyonu, evde altı egzersiz ve videolar.",
     "kalca-yan-agrisi.html", NECK_CSS, GT_BODY, YT_JS,
     seo_title="Kalça Yan Ağrısı (Trokanterik Bursit): Egzersiz ve Tedavi | İhsan Eren",
     condition="Büyük trokanter ağrı sendromu", faq_items=GT_FAQ)

# ============================================================== LENFÖDEM
LY_FAQ = [
 ("Lenfödem tamamen geçer mi?", "Lenfödemin kesin bir tedavisi yoktur; ancak bası giysileri, cilt bakımı, düzenli hareket ve özel masajla belirtiler çoğunlukla kontrol altına alınabilir. Erken başlanan bakım şişliğin ilerlemesini önlemeye yardım eder."),
 ("Egzersiz lenfödemi kötüleştirir mi?", "Araştırmalar bunu göstermiyor. Cochrane derlemesindeki iki çalışmada (358 kişi), belirtiler izlendiği sürece kademeli dirençli egzersiz lenfödem riskini artırmadı. Kas kasılmaları lenf sıvısının ilerlemesine yardım eder. Yavaş başlayın, bası giysiniz varsa egzersizde giyin ve şiş bölgeyi kontrol edin."),
 ("Lenfödemli kolumdan tansiyon ölçtürebilir ya da kan aldırabilir miyim?", "İngiltere Ulusal Sağlık Hizmeti (NHS), mümkün olduğunda etkilenen bölgeden enjeksiyon yapılmamasını ve tansiyon ölçülmemesini öneriyor. Sağlık çalışanına lenfödeminiz olduğunu söyleyin ve diğer kolunuzun kullanılmasını isteyin."),
 ("Şişlik birden artar ve cilt kızarırsa ne yapmalıyım?", "Kızarıklık, sıcaklık, ağrı, şişlikte artış, ateş ya da titreme deri enfeksiyonunun (selülit) belirtileri olabilir. Lenfödemli bölgede enfeksiyon daha kolay gelişir ve lenf sistemine daha fazla zarar verebilir; beklemeden, aynı gün hekime başvurun. Tedavisi çoğunlukla ağızdan antibiyotiktir."),
]

LY_SRC = [
 "Cancer Research UK. " + ext("https://www.cancerresearchuk.org/about-cancer/coping/physically/lymphoedema-and-cancer/treating/exercise", "Exercise, positioning and lymphoedema") + ". Last reviewed 20 May 2026.",
 "National Cancer Institute. " + ext("https://www.cancer.gov/about-cancer/treatment/side-effects/lymphedema/lymphedema-hp-pdq", "Lymphedema (PDQ) – Health Professional Version") + ". Updated 18 December 2024.",
 "NHS. " + ext("https://www.nhs.uk/conditions/lymphoedema/", "Lymphoedema") + ". Page last reviewed 29 March 2023.",
 "NHS. " + ext("https://www.nhs.uk/conditions/lymphoedema/treatment/", "Lymphoedema: treatment") + ". Page last reviewed 29 March 2023.",
 "NHS. " + ext("https://www.nhs.uk/conditions/lymphoedema/prevention/", "Lymphoedema: prevention") + ". Page last reviewed 29 March 2023.",
 "Stuiver MM, ten Tusscher MR, Agasi-Idenburg CS, et al. " + ext("https://www.cochrane.org/CD009765/BREASTCA_conservative-interventions-preventing-clinically-detectable-upper-limb-lymphoedema-patients-who-are", "Conservative interventions for preventing clinically detectable upper-limb lymphoedema in patients who are at risk of developing lymphoedema after breast cancer therapy") + ". Cochrane Database Syst Rev. 2015;(2):CD009765.",
]

LY_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>Lenfödem</h1>
    <p class="lede">Lenfödem, lenf sıvısının yeterince boşalamaması sonucu çoğunlukla kolda ya da bacakta gelişen kalıcı şişliktir; en sık kanser tedavisinden sonra görülür. Tamamen geçmez ama bası giysisi, cilt bakımı, hareket ve özel masajla kontrol altına alınabilir. Araştırmalar, doğru yapılan egzersizin lenfödemi tetiklemediğini ve kötüleştirmediğini gösteriyor.</p>
    <p class="meta">Son güncelleme: 7 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%20 / %6</b><span>Koltuk altı lenf bezleri alındığında ve yalnızca nöbetçi bez örneklendiğinde lenfödem sıklığı</span></div>
        <div class="stat"><b>4 bileşen</b><span>Önerilen tedavi: bası, cilt bakımı, egzersiz ve lenf drenaj masajı</span></div>
        <div class="stat"><b>358 kişi</b><span>Kademeli dirençli egzersizin lenfödem riskini artırmadığı iki çalışma (Cochrane)</span></div>
        <div class="stat"><b>Her gün</b><span>Egzersiz için önerilen sıklık; yavaş başlayıp azar azar artırarak</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Lenf sistemi, vücuttaki fazla sıvıyı toplayan ve enfeksiyonla savaşan damar ve bez ağıdır. Bu sistem iyi çalışmadığında sıvı dokularda birikir ve şişlik oluşur.</p>
        <p class="soft">İki türü vardır. Doğuştan gelen (birincil) lenfödem seyrektir. Sonradan gelişen (ikincil) lenfödem çok daha sıktır: lenf bezlerinin ameliyatla alınması gibi kanser tedavileri, enfeksiyon, yaralanma, iltihap ya da uzun süreli hareketsizlik lenf sistemine zarar verdiğinde ortaya çıkar.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Kolun, bacağın ya da başka bir bölgenin tamamında ya da bir kısmında şişlik</li>
          <li>Giysilerin, yüzüğün ya da saatin dar gelmeye başlaması</li>
          <li>Ağırlık ve sızlama hissi, hareket etmekte zorlanma</li>
          <li>Erken dönemde bastırınca çukur bırakan, gün içinde artıp gece azalan şişlik</li>
          <li>Ciltte sertleşme, kalınlaşma ya da gerginlik</li>
          <li>Tekrarlayan deri enfeksiyonları</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Egzersiz şişliği artırır mı?</h2>
      <p class="soft">Uzun yıllar boyunca, meme kanseri tedavisi görenlere kollarını yormamaları söylendi. Araştırmalar bu korkuyu doğrulamadı. Cochrane derlemesine göre, belirtiler yakından izlendiği sürece kademeli dirençli egzersiz lenfödem riskini artırmıyor (iki çalışma, 358 kişi); ameliyattan sonra omuz hareketlerine erken başlamak da riski artırıyor görünmüyor ve omuz hareketini ilk aylarda iyileştiriyor. Yazarlar, kanıtın genel kalitesi düşük olduğu için sonuçların dikkatle yorumlanmasını istiyor.</p>
      <p class="soft">Amerikan Spor Hekimliği Koleji, gözetim altında yapılan kademeli dirençli egzersizi lenfödemi olan ya da risk altındaki kişiler için güvenli kabul ediyor. Kasılan kaslar lenf sıvısını damarlarda ileri iter; bu yüzden hareket tedavinin dört ana bileşeninden biridir.</p>
      <div class="callout">
        <p>Üç kural: Yavaş başlayıp azar azar artırın. Bası giysiniz varsa egzersiz sırasında giyin. Egzersiz sırasında ve sonrasında şiş bölgeyi kontrol edin; bir değişiklik olursa durun ve lenfödem ekibinize haber verin.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <p class="soft">Önerilen tedavi, dört bileşenli “kompleks boşaltıcı tedavi”dir. Önce birkaç hafta süren, şişliği azaltmaya yönelik yoğun bir dönem gelir; ardından kişinin bakımını kendisinin sürdürdüğü ve birkaç ayda bir kontrole gittiği sürdürme dönemi başlar.</p>
      <ul class="tx">
        <li><b>Bası</b><span>Bandajlar ve bası giysileri (kolluk, eldiven, çorap) sıvının geri birikmesini önler; doğru ölçü ve giyme biçimi öğretilir.</span></li>
        <li><b>Cilt bakımı</b><span>Cildi temiz, nemli ve sağlam tutmak enfeksiyon riskini azaltır.</span></li>
        <li><b>Hareket ve egzersiz</b><span>Etkilenen bölgeye özel hareketler ile yürüyüş, yüzme ve bisiklet gibi tüm vücudu çalıştıran etkinlikler.</span></li>
        <li><b>Lenf drenaj masajı</b><span>Başta uzman terapist uygular; sürdürme döneminde kişinin kendine yapacağı basit teknikler öğretilir.</span></li>
        <li><b>Yükseltme ve kilo</b><span>Dinlenirken etkilenen bölgeyi yastıkla desteklemek ve sağlıklı kiloyu korumak önerilir.</span></li>
        <li><b>Cerrahi</b><span>Az sayıda kişide, yalnızca bazı uzman merkezlerde uygulanır.</span></li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Cildi korumak, enfeksiyonu önlemek</h2>
      <p class="soft">Lenfödemli bölgede cilt enfeksiyona daha açıktır ve her enfeksiyon lenf sistemine biraz daha zarar verebilir. Bu yüzden küçük önlemler önemlidir:</p>
      <ul class="dots">
        <li>Kesik ve çizikleri hemen temizleyip antiseptik krem sürün</li>
        <li>Cildinizi her gün nemlendirin; temiz ve kuru tutun</li>
        <li>Bahçe ve ev işlerinde eldiven giyin; tıraş için elektrikli makine, tırnaklar için tırnak makası kullanın</li>
        <li>Güneş yanığından ve böcek ısırığından korunun</li>
        <li>Çok sıcak banyo, sauna ve buhar odasından kaçının; şişliği artırabilir</li>
        <li>Dar giysi ve takılardan kaçının</li>
        <li>Mümkünse etkilenen bölgeden enjeksiyon yaptırmayın ve tansiyon ölçtürmeyin</li>
        <li>Bacaklar etkilendiyse çıplak ayakla dolaşmayın, ayağınıza iyi oturan ayakkabı giyin</li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Kol lenfödemi için altı hareket</h2>
      <p class="soft">Dik oturun, kolunuz rahatça desteklensin. Hareketler ağrısız olmalı; hafif bir gerilme hissi normaldir. Başlamadan önce hekiminize ya da lenfödem terapistinize danışın. Bacak ya da baş-boyun lenfödeminde hareketler farklıdır.</p>
      {ex_grid(["ly_breath", "ly_shrug", "ly_arm", "ly_fist", "ly_ball", "ly_walk"])}
      <div class="callout">
        <p>Otururken kolunuzu rahat bir yükseklikte, bir yastığın üzerinde dinlendirin. Bacağınız etkilendiyse ayaklarınızı sarkıtarak uzun süre oturmayın; bacağınızı dizinizin altına yastık koyarak uzatın.</p>
      </div>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Lenfödem için videolar</h2>
      <p class="soft">İngiltere'deki kanser araştırma kuruluşu Cancer Research UK'nin YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("Rku5PGz48c8", "Derin nefes videosunu oynat", "Deep Breathing for Lymphoedema | Cancer Research UK")}
          <h3>Derin nefes</h3>
          <p>Hareketlere başlamadan önce yapılan derin nefes çalışmasını gösteren video.</p>
        </div>
        <div class="vid">
          {vbox("zcQB6pZmdN0", "Kol egzersizleri videosunu oynat", "Arm Exercises for Lymphoedema | Cancer Research UK")}
          <h3>Kol egzersizleri</h3>
          <p>Kol lenfödemi için hareketleri gösteren video.</p>
        </div>
      </div>
      <p class="meta">Videolar Cancer Research UK kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(LY_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Şiş bölgede kızarıklık, sıcaklık, ağrı ya da şişlikte ani artış; ateş ya da titreme (aynı gün)</li>
        <li>Tek bacakta aniden gelişen ağrılı şişlik (acil)</li>
        <li>Nefes darlığı ya da göğüs ağrısı (acil)</li>
        <li>Kolda ya da bacakta yeni başlayan, nedeni bilinmeyen şişlik</li>
        <li>Kanser tedavisi gördüyseniz: hızla artan şişlik ya da yeni ele gelen kitle</li>
      </ul>
      <div class="note" style="margin-top:22px">Lenfödem bakımı, bu alanda eğitim almış bir lenfödem terapistinin ve hekiminizin izlemiyle yürütülür. Bu sayfadaki hareketler o bakımın yerini tutmaz; onu destekler.</div>
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(LY_SRC)}
    </div>
  </section>
</main>'''

page("lenfodem.html", "Lenfödem",
     "Lenfödem nedir, neden olur, nasıl kontrol altına alınır? Egzersiz şişliği artırır mı, cilt nasıl korunur, bası giysisi ve lenf drenajı ne işe yarar? Kol için altı hareket ve videolar.",
     "lenfodem.html", NECK_CSS, LY_BODY, YT_JS,
     seo_title="Lenfödem: Egzersiz, Cilt Bakımı ve Tedavi | İhsan Eren",
     condition="Lenfödem", faq_items=LY_FAQ)

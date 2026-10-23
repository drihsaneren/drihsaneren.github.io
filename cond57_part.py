# -*- coding: utf-8 -*-
# Yeni rehber (57): Çekiç parmak (mallet finger). cond56_part.py'den sonra exec edilir. Video yok.
# Royal United Hospitals Bath (ORT056, Haziran 2025), Hull (HEY1342/2025) ve Coventry-Warwickshire (v5, Şubat 2025) NHS broşürlerine göre.

_MF_BASE = '<path class="fig" d="M56 116 L56 84"/><rect x="48" y="54" width="16" height="32" rx="7" fill="#2A6F6B"/>'
# Atel takılıyken orta eklemi bükme: uç bölüm atelde düz kalır (yandan)
SV["mf_pip"] = fig(_MF_BASE +
    f'<path class="fig" d="M56 54 L56 42 L56 32 L56 22">{anim_d("M56 54 L56 42 L56 32 L56 22;M56 54 L56 42 L66 40 L76 38;M56 54 L56 42 L56 32 L56 22")}</path>'
    f'<path d="M56 36 L56 18" stroke="#C8963E" stroke-width="10" stroke-linecap="round" opacity=".9">{anim_d("M56 36 L56 18;M62 40.8 L80 37.2;M56 36 L56 18")}</path>',
    "Atelle orta eklemi bükme")
# Parmakları açıp germe (önden)
SV["mf_spread"] = fig(
    '<path class="fig" d="M60 116 L60 86"/><rect x="44" y="50" width="32" height="38" rx="9" fill="#2A6F6B"/>'
    f'<path class="fig hl" d="M48 50 L48 26">{anim_d("M48 50 L48 26;M47 50 L36 29;M48 50 L48 26")}</path>'
    f'<path class="fig hl" d="M56 50 L56 20">{anim_d("M56 50 L56 20;M55 50 L51 20;M56 50 L56 20")}</path>'
    f'<path class="fig hl" d="M64 50 L64 20">{anim_d("M64 50 L64 20;M65 50 L69 20;M64 50 L64 20")}</path>'
    f'<path class="fig hl" d="M72 50 L72 28">{anim_d("M72 50 L72 28;M73 50 L84 31;M72 50 L72 28")}</path>'
    f'<path class="fig" d="M44 72 L34 60">{anim_d("M44 72 L34 60;M44 72 L24 66;M44 72 L34 60")}</path>',
    "Parmakları açma")
# Kanca yumruk: parmak dibi düz, orta ve uç eklemler bükülür (yandan)
SV["mf_hook"] = fig(_MF_BASE +
    f'<path class="fig hl" d="M56 54 L56 36 L56 24 L56 14">{anim_d("M56 54 L56 36 L56 24 L56 14;M56 54 L56 36 L68 36 L68 46;M56 54 L56 36 L56 24 L56 14")}</path>',
    "Kanca yumruk")
# Tam yumruk ve açma (yandan)
SV["mf_fist"] = fig(_MF_BASE +
    f'<path class="fig hl" d="M56 54 L56 36 L56 24 L56 14">{anim_d("M56 54 L56 36 L56 24 L56 14;M56 54 L70 50 L72 62 L64 64;M56 54 L56 36 L56 24 L56 14")}</path>',
    "Tam yumruk")

_ex2("mf_mid", "mf_pip", "Atel takılıyken orta eklemi bükme", "Ateli çıkarmadan, yaralı parmağınızın orta eklemini tam bükün ve düzeltin; uç eklem atelin içinde düz kalsın. Diğer parmaklarınızı da tam hareket ettirin, tutulmasınlar.", "10 tekrar, günde 3–4 kez")
_ex2("mf_open", "mf_spread", "Parmakları açıp germe", "Kesintisiz atel dönemi bittikten sonra başlayın. Parmaklarınızı ve başparmağınızı olabildiğince düzeltin ve birbirinden ayırın.", "10–20 saniye tutun, az ve sık")
_ex2("mf_hk", "mf_hook", "Kanca yumruk", "Parmak diplerinizdeki eklemleri düz tutarak yalnızca orta ve uç eklemlerinizi bükün, sonra parmaklarınızı düzeltin. Uç eklem düşmeye başlarsa durun.", "10–15 tekrar, günde 4 kez")
_ex2("mf_fs", "mf_fist", "Yumruk yapıp açma", "Elinizi yavaşça tam bir yumruk yapın, sonra parmaklarınızı tamamen açın. İlk günlerde parmağınız tutuk olabilir; zorlamadan, az ve sık çalışın.", "10–15 tekrar, günde 4 kez")

MF_FAQ = [
 ("Ameliyat gerekir mi?", "Çoğu zaman gerekmez; çekiç parmakların çoğu yalnızca atelle iyi sonuç verir. Tendonla birlikte büyük bir kemik parçası koptuysa ameliyat gerekebilir. Bu genellikle bölgesel uyuşturmayla, günübirlik yapılan ve ince tellerle tespit edilen bir işlemdir; teller 3–4 hafta kalır."),
 ("Atel takılıyken parmak ucum bükülürse ne olur?", "Kesintisiz atel döneminde uç eklemin bir kez bile bükülmesi iyileşen tendona zarar verebilir ve iyileşmeyi geciktirir; atel süresi çoğu zaman baştan başlar. Ateli yalnızca temizlik için, parmağınız masaya düz yaslanmışken çıkarın. Böyle bir şey olduysa ekibinize haber verin."),
 ("Parmak ucum tamamen düzelir mi?", "Çoğu kişide iyi düzelir, ama en iyi tedaviyle bile uç eklemde 10 dereceye kadar düzelmeme sık görülür. Parmağın arkasındaki şişlik, hassasiyet ve kızarıklığın geçmesi birkaç ay sürebilir. Kemik parçalı tipte eklemin üzerinde küçük bir şişkinlik kalabilir; bu genellikle elin işlevini etkilemez. İngiliz El Cerrahisi Derneği’ne göre atel genellikle 6–8 hafta kesintisiz takılır, ardından 1–2 hafta yalnızca geceleri ve parmağın zorlanabileceği durumlarda kullanılır; uç eklem biraz sarkık kalsa bile çoğu kişi parmağını iyi kullanır."),
 ("Ne zaman araba kullanabilir, spora dönebilirim?", "Direksiyonu ağrı dikkatinizi dağıtmadan sıkıca kavrayabildiğinizde araç kullanabilirsiniz; atelle araç kullanmak için sigorta şirketinize danışın. Bir NHS broşürü spora en az 8 hafta ara vermeyi öneriyor; dönüş zamanını ekibinizle birlikte belirleyin."),
 ("Neden yüzük takmamalıyım?", "Parmak şişebilir; yüzük kan dolaşımını ve iyileşmeyi olumsuz etkileyebilir. Atel döneminde yaralı parmağa yüzük takmayın."),
]

MF_SRC = [
 "Royal United Hospitals Bath NHS Foundation Trust. " + ext("https://www.ruh.nhs.uk/patients/patient_information/ORT056_Advice_after_a_mallet_finger_injury.pdf", "Advice after a mallet finger injury") + ". ORT056, June 2025.",
 "Hull University Teaching Hospitals NHS Trust. " + ext("https://www.hey.nhs.uk/patient-leaflet/hand-therapy-mallet-injury-of-the-finger-pifu/", "Hand therapy: mallet injury of the finger") + ". HEY1342/2025, updated 30 June 2025.",
 "Handoll HHG, Vaghela MV. " + ext("https://doi.org/10.1002/14651858.CD004574.pub2", "Interventions for treating mallet finger injuries") + ". Cochrane Database Syst Rev. 2004;(3):CD004574",
 "University Hospitals Coventry and Warwickshire NHS Trust. " + ext("https://www.uhcw.nhs.uk/download/clientfiles/files/Patient%20Information%20Leaflets/Trauma%20and%20Neuro%20services/Trauma%20and%20Orthopaedics/Mallet%20Finger.pdf", "Mallet finger") + ". Version 5, February 2025.",
 "British Society for Surgery of the Hand. " + ext("https://www.BSSH.ac.uk/_userfiles/pages/files/Patients/Conditions/Trauma/mallet_finger_leaflet_2016.pdf", "Mallet finger: patient information") + ". 2016.",
]

MF_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Çekiç parmak (mallet finger)</h1>
    <p class="lede">Parmak ucunuza bir top çarptı ya da parmağınızı bir yere sert vurdunuz ve şimdi parmak ucunuz aşağı düşük duruyor, kendi başınıza düzeltemiyor musunuz? Uç eklemi düzelten tendon kopmuş ya da bağlandığı yerden küçük bir kemik parçasıyla birlikte ayrılmış olabilir. Tedavi çoğunlukla basittir ama sabır ister: parmak ucu haftalarca, hiç bükülmeden bir atelle düz tutulur.</p>
    <p class="meta">Son güncelleme: 19 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>6 hafta</b><span>Kemik parçalı tipte kesintisiz atel süresi</span></div>
        <div class="stat"><b>8 hafta</b><span>Tendon kopmasında kesintisiz atel süresi</span></div>
        <div class="stat"><b>2–4 hafta</b><span>Sonrasında ateli gece ve riskli işlerde takma süresi</span></div>
        <div class="stat"><b>10 derece</b><span>Uç eklemde kalabilen ve sık görülen hafif düşüklük</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Yaralanmadan hemen sonra parmak ucunda ağrı ve şişlik.</li>
          <li>Parmak ucu avuca doğru bükük durur.</li>
          <li>Uç eklemi kendi başınıza düzeltemezsiniz, ama elinizle düzeltilebilir.</li>
        </ul>
        <p class="soft">Kemik parçası olup olmadığını anlamak için röntgen çekilir; tedavi buna göre belirlenir. Bu yüzden yaralanmadan sonra kısa sürede bir hekime başvurun.</p>
      </div>
      <div>
        <h2>Neden atel bu kadar önemli?</h2>
        <ul class="dots">
          <li>Atel, uç eklemi düz tutarak kopan tendonun ya da kemik parçasının yerinde iyileşmesini sağlar.</li>
          <li>Ateli banyoda ve yatakta da, gece gündüz çıkarmadan takın.</li>
          <li>Atel sıkıca oturmalı, parmak ucu atelin sonuna kadar ulaşmalı ve atel orta eklemin bükülmesini engellememeli.</li>
          <li>Sigara ve diyabet iyileşmeyi yavaşlatabilir.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ateli günde bir kez temizleyin</h2>
      <p class="soft">Atelin altında ıslak kalan cilt çok çabuk tahriş olur. Parmağınızı ve ateli kuru tutun; atelin havalandırma deliklerini bantla kapatmayın. Bu adımlarda biri size yardım edebilir.</p>
      <ol class="steps">
        <li><span>Parmağınızı uç eklem düz kalacak şekilde masaya düz yaslayın.</span></li>
        <li><span>Bandı kesin ve ateli kaydırarak çıkarın; parmak ucunuz masada düz kalsın.</span></li>
        <li><span>Parmağınızı ve ateli sabunlu suyla yıkayıp kurulayın; bu sırada parmak ucunuzu hiç bükmeyin.</span></li>
        <li><span>Ateli parmak ucunuz düzken geri kaydırın ve esnemeyen bir bantla sabitleyin; bant atelin ortasını sarsın, orta eklemi kapatmasın.</span></li>
      </ol>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Atel döneminde ve sonrasında dört egzersiz</h2>
      <p class="soft">İlk egzersizi atel takılıyken yapın. Diğer üçüne, kesintisiz atel dönemi (6 ya da 8 hafta) bittiğinde ve ekibiniz onayladığında başlayın; bu dönemde ateli 2–4 hafta daha gece ve ağır ya da riskli işlerde takmayı sürdürün. Egzersiz sırasında parmak ucunuz yeniden düşmeye başlarsa durun, ateli sürekli takın ve ekibinize başvurun.</p>
      {ex_grid(["mf_mid", "mf_open", "mf_hk", "mf_fs"], "ex four")}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(MF_FAQ)}
      <p class="soft" style="margin-top:18px">Parmağın takılıp kilitlenmesi için <a href="tetik-parmak.html">tetik parmak</a>, parmak eklemlerinde ağrı ve sertlik için <a href="el-kireclenmesi.html">el kireçlenmesi</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman ekibinize başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Şişlik indikçe atel gevşediyse ve parmak ucunu artık düz tutmuyorsa: beklemeden</li>
        <li>Ağrı ve şişlik belirgin şekilde artıyorsa</li>
        <li>Atel çok sıkı ya da çok gevşekse, orta eklemin bükülmesini engelliyorsa ya da süre dolmadan çıktıysa</li>
        <li>Egzersizlere başladıktan sonra parmak ucu yeniden düşmeye başladıysa</li>
        <li>Egzersizlere başlamanızın üzerinden 2 hafta geçtiği hâlde yumruk yapamıyor ya da parmak ucunu avucunuza değdiremiyorsanız</li>
        <li>12. haftada hâlâ işinize ya da hobilerinize dönmekte zorlanıyorsanız</li>
      </ul>
      {CTA_CARD("Çekiç parmak sonrası el rehabilitasyonunuz", "çekiç parmak sonrası el rehabilitasyonu")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(MF_SRC)}
    </div>
  </section>
</main>'''

page("cekic-parmak.html", "Çekiç Parmak (Mallet Finger)",
     "Parmak ucu düştü ve düzelmiyor mu? Çekiç parmak nedir, atel ne kadar takılır, nasıl temizlenir, ne zaman ameliyat gerekir? Atel dönemi ve sonrası için dört egzersiz.",
     "cekic-parmak.html", NECK_CSS, MF_BODY, "",
     seo_title="Çekiç Parmak (Mallet Finger): Atel Süresi, Bakım ve Egzersizler | İhsan Eren",
     condition="Çekiç parmak", faq_items=MF_FAQ)

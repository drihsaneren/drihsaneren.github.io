# -*- coding: utf-8 -*-
# Yeni rehberler (15): düztabanlık ve omurilik yaralanması sonrası rehabilitasyon.
# cond15_part.py'den sonra exec edilir. Videolar: Doctor O'Donovan, Rehab Science, Shepherd Center (oEmbed ile doğrulandı).

# ---- yeni çizimler
# Ayak kavsini kaldırma (kısa ayak): yandan ayak; taban çizgisinin ortası yükselir, parmaklar ve topuk yerde kalır.
SV["ff_short"] = fig(GRD +
    '<path class="fig" d="M46 34 V90 M46 90 L92 108"/>'
    f'<path class="fig hl" d="M38 110 Q60 108 76 110 H96">{anim_d("M38 110 Q60 108 76 110 H96;M38 110 Q60 94 76 110 H96;M38 110 Q60 108 76 110 H96")}</path>'
    '<g><animate attributeName="opacity" values="0;1;0" dur="3.2s" repeatCount="indefinite"/>'
    '<path d="M60 84 V72 M56 76 L60 72 L64 76" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>',
    "Ayak kavsini kaldırma")
# Başparmakları birbirine bastırma (üstten iki ayak)
SV["ff_press"] = fig(
    '<rect x="30" y="38" width="24" height="66" rx="12" fill="#2A6F6B"/><rect x="66" y="38" width="24" height="66" rx="12" fill="#2A6F6B"/>'
    '<circle cx="50" cy="32" r="6" fill="#C8963E"/><circle cx="70" cy="32" r="6" fill="#C8963E"/>'
    '<g fill="#2A6F6B"><circle cx="40" cy="31" r="4"/><circle cx="32" cy="35" r="3.5"/><circle cx="80" cy="31" r="4"/><circle cx="88" cy="35" r="3.5"/></g>'
    '<g><animate attributeName="opacity" values="0.15;1;0.15" dur="2.4s" repeatCount="indefinite"/>'
    '<path d="M28 18 H44 M40 14 L44 18 L40 22 M92 18 H76 M80 14 L76 18 L80 22" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>',
    "Başparmakları bastırma")
# Tekerlekli sandalyede yana eğilerek basınç azaltma (önden)
SV["sc_sidelean"] = fig(GRD +
    '<circle cx="32" cy="88" r="22" fill="none" stroke="#B9CBC6" stroke-width="3"/><circle cx="88" cy="88" r="22" fill="none" stroke="#B9CBC6" stroke-width="3"/>'
    '<path class="fig" d="M46 84 H74 M50 84 V110 M70 84 V110"/>'
    f'<g>{anim_t("0 60 84;20 60 84;20 60 84;0 60 84", dur="5s", kt="0;0.3;0.7;1", typ="rotate")}'
    '<path class="fig hl" d="M60 84 V48"/><path class="fig" d="M46 52 H74 M46 52 L42 72 M74 52 L80 70"/><circle class="hd" cx="60" cy="36" r="8"/></g>',
    "Yana eğilme")

# Oturarak lastik bantla kürek çekme (yandan)
SV["sc_row"] = fig(GRD + CHAIR_L +
    '<path class="obj" d="M106 30 V112"/>'
    '<path class="fig" d="M46 74 H80 V112"/>'
    '<path class="fig" d="M46 74 L48 42"/><circle class="hd" cx="50" cy="33" r="8"/>'
    f'<path class="band" d="M80 54 H106">{anim_d("M80 54 H106;M60 58 H106;M80 54 H106")}</path>'
    f'<path class="fig hl" d="M48 48 L64 54 L80 54">{anim_d("M48 48 L64 54 L80 54;M48 48 L44 62 L60 58;M48 48 L64 54 L80 54")}</path>',
    "Oturarak kürek çekme")
# Oturarak kürek kemiği sıkıştırma (arkadan, tekerlekli sandalyede)
SV["sc_scap"] = fig(GRD +
    '<circle cx="32" cy="88" r="22" fill="none" stroke="#B9CBC6" stroke-width="3"/><circle cx="88" cy="88" r="22" fill="none" stroke="#B9CBC6" stroke-width="3"/>'
    '<path class="fig" d="M46 84 H74 M50 84 V110 M70 84 V110 M40 42 H80 M60 34 V84 M40 42 L36 62 L40 76 M80 42 L84 62 L80 76"/>'
    '<circle class="hd" cx="60" cy="24" r="8"/>'
    f'<g>{anim_t("0 0;3 0;0 0")}<path d="M43 47 L55 47 L50 64 Z" fill="#C8963E" stroke="#C8963E" stroke-width="2" stroke-linejoin="round"/></g>'
    f'<g>{anim_t("0 0;-3 0;0 0")}<path d="M77 47 L65 47 L70 64 Z" fill="#C8963E" stroke="#C8963E" stroke-width="2" stroke-linejoin="round"/></g>',
    "Kürek kemiği sıkıştırma")

_ex2("ff_calf", "calf", "Duvarda baldır germe", "Duvara ya da bir sandalyeye tutunun. Germek istediğiniz bacağı düz biçimde arkaya alın, öndeki dizinizi bükün. Arkadaki topuğunuz yerde kalsın; baldırınızda gerilme hissedin.", "30 saniye tutun, 3 tekrar")
_ex2("ff_heel", "heel2", "İki ayakla topuk yükseltme", "Tezgâha tutunarak dik durun. İki ayağınızın parmak uçlarında yükselin ve yavaşça inin. Topuklarınız yükselirken ayak bileğiniz dışa ya da içe kaçmasın.", "10 tekrar, 3 set")
_ex2("ff_heel1", "heel3", "Tek ayakla topuk yükseltme", "İki ayakla topuk yükseltmeyi rahat yapabildiğinizde tek ayağa geçin. Tutunarak tek ayağınızın parmak ucunda yükselin ve yavaşça inin.", "Yapabildiğiniz kadar, 10 tekrara doğru")
_ex2("ff_sls", "sls", "Tek ayak üzerinde denge", "Gerekirse bir yere tutunarak tek ayağınızın üzerinde dengede durun. Kolaylaştıkça yastık gibi yumuşak bir zeminde deneyin.", "30 saniye, 3 tekrar")
EXT["ff_short"] = ("Ayak kavsini kaldırma", "Oturun, ayağınız yere düz bassın. Ayak tabanınızdaki kasları sıkarak ayağınızı kısaltır gibi kavsinizi yükseltin; parmaklarınız kıvrılmasın, yerde düz kalsın. Birkaç saniye tutup gevşetin.", "10 tekrar")
EXT["ff_press"] = ("Başparmakları birbirine bastırma", "Bir sandalyeye ya da yere oturun. İki ayak başparmağınızın iç kenarlarını birbirine bastırın ve öylece tutun.", "5 saniye tutun, 10 tekrar")

_ex2("sc_lean", "fwdlean", "Öne eğilerek basınç azaltma", "Ön tekerlekleri öne çevirin ve frenleri kilitleyin. Göğsünüzü dizlerinize doğru getirerek öne eğilin ve bekleyin. Doğrulurken dizlerinizden ya da kolçağın ön kısmından itin. İlk denemeleri sabit bir masanın önünde yapın.", "30–90 saniye, 15–30 dakikada bir")
_ex2("sc_reach", "reach", "Oturarak öne uzanma", "Gövde kontrolünüz izin veriyorsa: Önünüze, kol boyunuzdan biraz uzağa hafif bir nesne koyun. Gövdenizi kalçanızdan öne eğerek nesneye uzanın, sonra doğrulun. Oturma dengesini ve yer değiştirme becerisini geliştirir.", "10 tekrar")
EXT["sc_row"] = ("Lastik bantla kürek çekme", "Lastik bandı göğüs hizasında sağlam bir yere bağlayın, frenleri kilitleyin. Dirseklerinizi gövdenize yakın tutarak bandı geriye çekin, kürek kemiklerinizi birbirine yaklaştırın. Sandalyeyi iterken hep öne çalışan omuzları dengeler.", "3 set, haftada 2 gün")
EXT["sc_scap"] = ("Kürek kemiği sıkıştırma", "Dik oturun. Omuzlarınızı kulaklarınıza kaldırmadan kürek kemiklerinizi geriye ve birbirine doğru sıkıştırın, birkaç saniye tutup gevşetin.", "10 tekrar")
_ex2("sc_breath", "plb", "Derin nefes", "Rahatça oturun. Burnunuzdan yavaş ve derin bir nefes alın, kısa bir an tutun, dudaklarınızı büzerek uzun bir sürede verin. Göğüs ve karın kasları etkilendiğinde akciğerleri havalandırmaya yardım eder.", "5–10 nefes, günde birkaç kez")
EXT["sc_sidelean"] = ("Yana eğilerek basınç azaltma", "Frenleri kilitleyin, bir kolçağı açın. Diğer kolçağı tutarak karşı yana doğru eğilin; bir kalçanızın altındaki yük tamamen kalksın. Bekleyin, doğrulun ve öbür yana tekrarlayın.", "Her yana 30–90 saniye, 15–30 dakikada bir")

# ============================================================== DÜZTABANLIK
FF_FAQ = [
 ("Düztabanlık tedavi edilmeli mi?", "Çoğu zaman hayır. Düztabanlık genellikle sorun yaratmaz, spor yapmaya engel olmaz ve nadiren ciddi bir durumun işaretidir. Ağrı, sertlik, güçsüzlük ya da denge sorunu yoksa bir şey yapmak gerekmez."),
 ("Çocuğumun ayakları düz; tabanlık almalı mıyım?", "Küçük çocukların çoğunun ayağı düzdür; ayak kavsi genellikle 3–10 yaş arasında gelişir. Sorun yoksa bir şey yapmak gerekmez. 16 çalışmayı (1.058 çocuk) inceleyen Cochrane derlemesi, ağrısı olmayan sağlıklı çocuklarda pahalı özel tabanlıkları destekleyen bir kanıt bulamadı."),
 ("Tabanlık ayağın kavsini düzeltir mi?", "Hayır. Tabanlık, uygun ayakkabı ve egzersizler ayağın şeklini değiştirmez; ancak ağrıyı ve sertliği azaltabilir. Bu yüzden yalnızca şikâyet varsa önerilir."),
 ("Düztabanlık sonradan olur mu?", "Olabilir. Ayaktaki dokular yaralanma, yaşlanma ya da fazla kilo nedeniyle gevşeyebilir; yetişkinlerde en sık neden, iç ayak bileğinin arkasından geçip kavsi tutan kirişin zayıflamasıdır. Daha önce düz olmayan ya da yalnızca tek ayakta ortaya çıkan düztabanlıkta hekime görünün."),
]

FF_SRC = [
 "Evans AM, Rome K, Carroll M, Hawke F. " + ext("https://www.cochrane.org/CD006311/MUSKEL_non-surgical-treatments-flat-feet-children", "Foot orthoses for treating paediatric flat feet") + ". Cochrane Database Syst Rev. 2022;(1):CD006311.",
 "NHS. " + ext("https://www.nhs.uk/conditions/flat-feet/", "Flat feet") + ". Page last reviewed 24 June 2025.",
 "NHS Borders. " + ext("https://rightdecisions.scot.nhs.uk/patient-information-leaflets/primary-community-services/physiotherapy/posterior-tibial-tendon-dysfunction-pttd", "Posterior tibial tendon dysfunction (PTTD)") + ". Patient information leaflet.",
]

FF_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Düztabanlık</h1>
    <p class="lede">Düztabanlık, ayakta dururken ayağın iç kavsinin yere değmesidir. Çoğu kişide hiçbir soruna yol açmaz ve tedavi gerektirmez; küçük çocuklarda ise olağandır. Ağrı varsa, kavis sonradan düştüyse ya da yalnızca tek ayak etkilendiyse değerlendirme gerekir.</p>
    <p class="meta">Son güncelleme: 8 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>3–10 yaş</b><span>Çocuklarda ayak kavsinin genellikle geliştiği yaş aralığı</span></div>
        <div class="stat"><b>16 çalışma</b><span>Çocuklarda tabanlığı inceleyen Cochrane derlemesi; 1.058 çocuk</span></div>
        <div class="stat"><b>67 / 79</b><span>Bir yıl sonra ağrısız kalan 100 çocuk içinde: özel tabanlıkla ve yalnızca ayakkabıyla (fark anlamlı değil)</span></div>
        <div class="stat"><b>5 durum</b><span>Hekime görünmeyi gerektiren durum sayısı; aşağıda listelendi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Kendiniz bakabilirsiniz: Ayağa kalkın ve ayağınızın iç yanına bakın. Ayağınız yere tamamen yapışıyor, arada boşluk kalmıyorsa düztabansınız; iç kenar yerden yüksekse değilsiniz.</p>
        <p class="soft">Çoğu zaman belirgin bir neden yoktur; ayağınız böyledir ve ailede de görülebilir. Daha seyrek olarak ayak kemiklerinin anne karnında tam gelişmemesi, dokuların yaralanma, yaşlanma ya da fazla kiloyla gevşemesi veya kasları, sinirleri ve eklemleri etkileyen hastalıklar neden olur.</p>
      </div>
      <div>
        <h2>Belirti verirse</h2>
        <ul class="dots">
          <li>Ayak bileği çevresinde ya da bacağın alt kısmında ağrı</li>
          <li>Ayağın iç kenarı boyunca sızı</li>
          <li>Ayakkabıların çabuk yıpranması</li>
        </ul>
        <p class="soft">Bunların hiçbiri yoksa düztabanlık yalnızca bir ayak biçimidir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Çocuklarda düztabanlık</h2>
      <p class="soft">Küçük çocukların çoğunun ayağı düzdür. Ayağın iç kavsi genellikle 3–10 yaş arasında gelişir. Çocuğunuzun ayağı sorun çıkarmıyorsa bir şey yapmanız gerekmez.</p>
      <p class="soft">Tabanlık konusunda araştırmalar net: 16 rastgele kontrollü çalışmayı (1.058 çocuk) inceleyen Cochrane derlemesinde, ağrısı olmayan düztaban çocuklarda özel yapım tabanlık, hazır tabanlık ve yalnızca ayakkabı arasında ağrı açısından anlamlı fark bulunamadı. Yazarlar, ağrısı olmayan sağlıklı çocuklarda pahalı özel tabanlıkları destekleyen bir kanıt görmediklerini belirtiyor. Tabanlık, çocuk romatizması gibi ayağı ağrılı durumlarda işe yarayabiliyor.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Yetişkinde sonradan düşen kavis</h2>
      <p class="soft">Yetişkinlikte ortaya çıkan düztabanlığın en sık nedeni, iç ayak bileği kemiğinin arkasından geçip ayak tabanına uzanan ve kavsi yukarıda tutan kirişin (tibialis posterior) zorlanıp zayıflamasıdır. Yaş ilerledikçe risk artar; orta yaşlı kadınlarda daha sık görülür. Fazla kilo, diyabet, iltihaplı romatizma ve bölgeye alınan darbe ya da burkulma zemin hazırlar.</p>
      <div class="callout">
        <p>Bu durumda ilk adım yükü azaltmaktır: ağrıyı artıran yürüyüş ve sporu bir süre azaltmak, araya havlu koyarak buz uygulamak, bağcıklı ve sağlam tabanlı bir ayakkabı giymek ve gerekirse tabanlık kullanmak. Kiriş yırtılmışsa ameliyat gündeme gelebilir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <p class="soft">Aşağıdaki yöntemler ayağın şeklini değiştirmez; amaç ağrıyı ve sertliği azaltmaktır.</p>
      <ul class="tx">
        <li><b>Ayakkabı</b><span>Geniş, rahat ve alçak topuklu ayakkabılar çoğu zaman en iyisidir.</span></li>
        <li><b>Tabanlık</b><span>Ayağı destekleyerek ağrıyı azaltabilir; ağrı yoksa gerekmez.</span></li>
        <li><b>Germe ve egzersiz</b><span>Baldırı esnetir, kavsi tutan kasları güçlendirir.</span></li>
        <li><b>Ağrı kesici</b><span>Gerektiğinde, eczacınıza ya da hekiminize danışarak.</span></li>
        <li><b>Ayak sağlığı uzmanı</b><span>Hekiminiz sizi bir fizyoterapiste ya da ayak sağlığı uzmanına yönlendirebilir.</span></li>
        <li><b>Ameliyat</b><span>Nadiren gerekir; kemik, doku ya da kas sorunu varsa ve diğer yöntemler işe yaramadıysa düşünülür.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Düztabanlık için altı egzersiz</h2>
      <p class="soft">Bu hareketler ağrısı olan düztabanlıkta kavsi destekleyen kasları çalıştırmak içindir. Günde birkaç kez yapılabilir; ağrınızı belirgin biçimde artıran hareketi bırakın.</p>
      {ex_grid(["ff_calf", "ff_short", "ff_press", "ff_heel", "ff_heel1", "ff_sls"])}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Düztabanlık için videolar</h2>
      <p class="soft">İngiltere'de hekim olan Dr. James O'Donovan'ın ve ABD'li fizyoterapist Dr. Tom Walters'ın (Rehab Science) YouTube kanallarından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("B5KbzQf5HdU", "Düztabanlık egzersizleri videosunu oynat", "7 Exercises for Flat Feet | Doctor and Physio led demonstration")}
          <h3>Düztabanlık için yedi egzersiz</h3>
          <p>Bir hekim ve fizyoterapistin gösterdiği egzersiz videosu.</p>
        </div>
        <div class="vid">
          {vbox("vcx_NNR7b1k", "Ayak kavsini güçlendirme videosunu oynat", "2 Exercises to Lift and Strengthen Your Arches (Flat Feet)")}
          <h3>Kavsi güçlendiren iki hareket</h3>
          <p>Ayak kavsini kaldıran kasları çalıştıran iki hareketi gösteren video.</p>
        </div>
      </div>
      <p class="meta">Videolar Doctor O'Donovan ve Rehab Science kanallarına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(FF_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime görünmeli?</h2>
      <p class="soft">Düztabanlığınız varsa ve şunlardan biri size uyuyorsa bir hekime görünün:</p>
      <ul class="dots redflags">
        <li>Ayaklarınız ağrılı, sert, güçsüz ya da uyuşuksa</li>
        <li>Ayağınızı ya da ayak bileğinizi sık sık incitiyorsanız</li>
        <li>Yürümekte ya da dengede durmakta zorlanıyorsanız</li>
        <li>Daha önce düztaban değildiyseniz</li>
        <li>Yalnızca tek ayağınız etkilendiyse</li>
      </ul>
      {CTA_CARD("Düztabanlığa bağlı ayak ağrınız", "düztabanlık")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(FF_SRC)}
    </div>
  </section>
</main>'''

page("duztabanlik.html", "Düztabanlık",
     "Düztabanlık tedavi gerektirir mi? Çocuklarda tabanlık işe yarar mı, kavis sonradan neden düşer, ne zaman hekime görünmeli? Evde altı egzersiz ve videolar.",
     "duztabanlik.html", NECK_CSS, FF_BODY, YT_JS,
     seo_title="Düztabanlık: Tabanlık, Egzersizler ve Çocuklarda Durum | İhsan Eren",
     condition="Düztabanlık (pes planus)", faq_items=FF_FAQ)

# ============================================================== OMURİLİK YARALANMASI
SC_FAQ = [
 ("Omurilik yaralanmasından sonra iyileşme olur mu?", "Yaralanmanın tam mı yoksa kısmi mi olduğuna bağlıdır. Kısmi yaralanmada omurilik hâlâ bazı sinyalleri iletebildiği için yaralanma düzeyinin altında bir miktar his ve hareket kalır; sinir hücresi kaybı azsa belirgin toparlanma mümkündür. Tam yaralanmada sinyal geçişi yoktur. Her iki durumda da rehabilitasyonun amacı kalan işlevi en iyi biçimde kullanmak, bağımsızlığı artırmak ve komplikasyonları önlemektir."),
 ("Bası yarası nasıl önlenir?", "Üç alışkanlıkla: Cildinizi günde iki kez, sabah ve yatmadan önce kontrol edin. Tekerlekli sandalyede her 15–30 dakikada bir, 30–90 saniye süreyle basıncı kaldırın. Yatakta, cildinizin dayanıklılığına göre her 2–6 saatte bir dönün. Rengi değişen bir bölge görürseniz rengi normale dönene kadar üzerine yük vermeyin."),
 ("Tekerlekli sandalye kullanırken egzersiz yapabilir miyim?", "Evet, önerilir de. 211 çalışmaya dayanan uluslararası kılavuz, kondisyon ve kas gücü için haftada iki gün en az 20 dakika orta-yüksek şiddette aerobik egzersiz ve haftada iki gün, çalışan her büyük kas grubu için üçer set güçlendirme öneriyor. Yaralanmanız yeniyse ya da 65 yaşın üzerindeyseniz başlamadan önce hekiminize danışın."),
 ("Otonom disrefleksi nedir?", "Göğüs omurgasının altıncı düzeyinde (T6) ya da daha yukarıda yaralanması olan kişilerde görülebilen, tansiyonun aniden tehlikeli biçimde yükseldiği acil bir durumdur. En sık dolu mesane ya da bağırsak tetikler. Şiddetli, zonklayıcı baş ağrısı, yaralanma düzeyinin üstünde terleme ve kızarma olur. Kişiyi oturtun, dar giysileri gevşetin, sondayı ve mesaneyi kontrol edin; hızla düzelmezse 112'yi arayın."),
]

SC_SRC = [
 "Martin Ginis KA, van der Scheer JW, Latimer-Cheung AE, et al. " + ext("https://www.nature.com/articles/s41393-017-0017-3", "Evidence-based scientific exercise guidelines for adults with spinal cord injury: an update and a new guideline") + ". Spinal Cord. 2018;56(4):308-321.",
 "Model Systems Knowledge Translation Center; Northwest Regional Spinal Cord Injury System. " + ext("https://sci.washington.edu/info/pamphlets/msktc-skin2.asp", "Skin care and pressure sores, part 2: Preventing pressure sores") + ". 2009.",
 "Model Systems Knowledge Translation Center; Northwest Regional Spinal Cord Injury System. " + ext("https://sci.washington.edu/info/pamphlets/msktc-pressure_relief.asp", "How to do pressure reliefs (weight shifts)") + ". 2009.",
 "National Institute of Neurological Disorders and Stroke. " + ext("https://www.ninds.nih.gov/health-information/disorders/spinal-cord-injury", "Spinal cord injury") + ". Last reviewed 13 March 2026.",
 "Royal National Orthopaedic Hospital NHS Trust. " + ext("https://www.rnoh.nhs.uk/services/spinal-cord-injury-centre/clinical-resources-advice/autonomic-dysreflexia", "Autonomic dysreflexia") + ". Spinal Cord Injury Centre.",
 "World Health Organization. " + ext("https://www.who.int/news-room/fact-sheets/detail/spinal-cord-injury", "Spinal cord injury") + ". Fact sheet. 16 April 2024.",
]

SC_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>Omurilik yaralanması sonrası rehabilitasyon</h1>
    <p class="lede">Omurilik yaralanması, beyinle beden arasındaki sinyal yolunun zarar görmesidir; yaralanmanın düzeyine göre bacakları ya da dört uzvu birden etkiler. Rehabilitasyon yalnızca hareketi değil, cildi, solunumu, mesaneyi ve bağımsız yaşamı da kapsar. Düzenli egzersiz kondisyonu ve kas gücünü artırır; cilt kontrolü ve basınç azaltma ise bası yaralarını önlemenin temelidir.</p>
    <p class="meta">Son güncelleme: 8 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>15 milyon</b><span>Dünyada omurilik yaralanmasıyla yaşayan kişi sayısı (DSÖ, 2021)</span></div>
        <div class="stat"><b>15–30 dk</b><span>Tekerlekli sandalyede basınç azaltma aralığı; her seferinde 30–90 saniye</span></div>
        <div class="stat"><b>Günde 2 kez</b><span>Cilt kontrolü: sabah ve yatmadan önce</span></div>
        <div class="stat"><b>20 dk × 2</b><span>Haftada iki gün aerobik egzersiz, ayrıca iki gün güçlendirme (uluslararası kılavuz)</span></div>
      </div>
      <div class="note warn" style="margin-top:22px"><strong>Otonom disrefleksi acil bir durumdur.</strong> Yaralanması göğüs omurgasının altıncı düzeyinde (T6) ya da daha yukarıda olan kişilerde aniden şiddetli, zonklayıcı baş ağrısı, yüzde kızarma ve terleme başlarsa: kişiyi dik oturtun, dar giysileri ve kemerleri gevşetin, sonda torbasını ve hortumu kontrol edin. Belirtiler hızla geçmezse 112'yi arayın.</div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Omurilik, beyinle beden arasında sinyal taşıyan sinir demetidir. Zarar gördüğünde yaralanma düzeyinin altındaki his, hareket ve iç organ kontrolü bozulur. En sık nedenler düşmeler ve trafik kazalarıdır; tümör, damar hastalıkları ve enfeksiyonlar da neden olabilir.</p>
        <p class="soft"><strong>Kısmi</strong> yaralanmada omurilik bazı sinyalleri hâlâ iletir; bir miktar his ve hareket kalır. <strong>Tam</strong> yaralanmada sinyal geçişi yoktur. Yaralanma yukarıdaysa dört uzuv birden etkilenir (tetrapleji); daha aşağıdaysa kollar korunur, gövdenin alt kısmı ve bacaklar etkilenir (parapleji).</p>
      </div>
      <div>
        <h2>Yalnızca hareket değil</h2>
        <ul class="dots">
          <li>His ve hareket kaybı; solunum kasları da etkilenebilir</li>
          <li>Mesane, bağırsak ve cinsel işlev sorunları</li>
          <li>Tansiyonu, nabzı ve vücut ısısını düzenlemede güçlük</li>
          <li>Kaslarda istemsiz kasılma ve sertlik (spastisite)</li>
          <li>Süreğen ağrı</li>
          <li>Bası yarası, idrar yolu enfeksiyonu, damarda pıhtı, kemik erimesi</li>
          <li>Depresyon; toparlanmayı da yavaşlatabilir</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Rehabilitasyon neleri kapsar?</h2>
      <ul class="tx">
        <li><b>Fizyoterapi</b><span>Kas gücü, oturma dengesi, yer değiştirme, tekerlekli sandalye becerileri ve uygun olanlarda yürüme çalışmaları.</span></li>
        <li><b>İş-uğraşı terapisi</b><span>Giyinme, yemek yeme, kişisel bakım gibi günlük becerileri yeniden kazanmak; ev düzenlemeleri.</span></li>
        <li><b>Yardımcı araçlar</b><span>Tekerlekli sandalye, minder ve günlük yaşamı kolaylaştıran araçların doğru seçimi ve ayarı.</span></li>
        <li><b>Komplikasyonları önleme</b><span>Cilt, mesane-bağırsak ve solunum bakımı; düzenli sağlık kontrolleri.</span></li>
        <li><b>Ruh sağlığı</b><span>Uyum süreci için psikolojik destek rehabilitasyonun parçasıdır.</span></li>
        <li><b>Aile ve bakım veren</b><span>Bakım verenlerin eğitimi ve desteklenmesi; yük çoğu zaman onların da omuzlarındadır.</span></li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Cildi korumak: bası yarası</h2>
      <p class="soft">His azaldığında, uzun süre aynı noktaya binen basınç fark edilmez ve cilt zarar görür. En çok kuyruk sokumu, oturma kemikleri, kalçanın yanları, topuklar ve ayak bilekleri risk altındadır. Korunmanın üç ayağı var:</p>
      <ul class="dots">
        <li><strong>Bakın:</strong> Cildinizi günde en az iki kez, sabah ve yatmadan önce kontrol edin. Kızarıklık ya da koyulaşma, su toplaması, sertlik, şişlik ve sıcaklık arayın; göremediğiniz yerler için ayna kullanın.</li>
        <li><strong>Basıncı kaldırın:</strong> Tekerlekli sandalyede her 15–30 dakikada bir, 30–90 saniye süreyle ağırlığınızı kaldırın: öne eğilerek, yana eğilerek ya da akülü sandalyede eğim vererek.</li>
        <li><strong>Dönün:</strong> Yatakta, cildinizin dayanıklılığına göre her 2–6 saatte bir pozisyon değiştirin. Sürüklenmeyin, kaldırılarak yer değiştirin; kemik çıkıntılarını yastıkla destekleyin.</li>
      </ul>
      <div class="callout">
        <p>Kollarla kendini yukarı itme, omuzdaki kirişlere zarar verebileceği için yalnızca diğer yöntemler yapılamadığında önerilir. Rengi değişen bir bölge görürseniz rengi normale dönene kadar üzerine yük vermeyin. Minderinizi ve oturuşunuzu en az iki yılda bir değerlendirtin.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Egzersiz: ne kadar?</h2>
      <p class="soft">211 çalışmanın incelenmesine dayanan uluslararası kılavuz, omurilik yaralanması olan yetişkinler için iki düzey tanımlıyor. Kondisyon ve kas gücü için: haftada iki gün en az 20 dakika orta-yüksek şiddette aerobik egzersiz ve haftada iki gün, çalışan her büyük kas grubu için üçer set güçlendirme. Kalp ve metabolizma sağlığı için: haftada üç gün en az 30 dakika orta-yüksek şiddette aerobik egzersiz.</p>
      <p class="soft">Kol ergometresi, tekerlekli sandalyeyle tempolu sürüş, yüzme ve lastik bantla güçlendirme en erişilebilir seçeneklerdir. Kılavuz, yaralanmasının üzerinden bir yıldan fazla geçmiş 18–64 yaş arası yetişkinlere dayanıyor; yaralanması yeni olanların, 65 yaşın üzerindekilerin ve ek hastalığı olanların başlamadan önce hekimlerine danışması öneriliyor.</p>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde uygulama</p>
      <h2>Tekerlekli sandalye kullananlar için altı uygulama</h2>
      <p class="soft">İlk ikisi cildi korumak içindir ve gün boyu yapılır. Diğerleri denge, omuz sağlığı ve solunum içindir. Hangi hareketin size uygun olduğu yaralanmanızın düzeyine bağlıdır; programınızı rehabilitasyon ekibinizle belirleyin.</p>
      {ex_grid(["sc_lean", "sc_sidelean", "sc_reach", "sc_row", "sc_scap", "sc_breath"])}
      <div class="callout">
        <p>Omuzlar tekerlekli sandalye kullanan kişinin “bacaklarıdır”; omuz ağrısını hafife almayın. Yer değiştirirken ve sandalyeyi iterken ağrınız oluyorsa fizyoterapistinize tekniğinizi ve sandalye ayarlarınızı değerlendirtin.</p>
      </div>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Omurilik yaralanması için videolar</h2>
      <p class="soft">ABD'de omurilik ve beyin yaralanması rehabilitasyonunda uzmanlaşmış Shepherd Center hastanesinin YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("ibrZzDZb-PU", "Omurilik yaralanması tanıtım videosunu oynat", "Spinal Cord Injury: Causes, Effects and Classifications")}
          <h3>Nedenler, etkiler ve sınıflama</h3>
          <p>Omurilik yaralanmasının temel bilgilerini anlatan video.</p>
        </div>
        <div class="vid">
          {vbox("-Ew-N5Ux0Ns", "Egzersiz programı videosunu oynat", "Shepherd Center Workout Routine for People with Spinal Cord Injury")}
          <h3>Egzersiz programı</h3>
          <p>Omurilik yaralanması olan kişiler için hazırlanmış egzersiz videosu.</p>
        </div>
      </div>
      <p class="meta">Videolar Shepherd Center kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(SC_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Aniden başlayan şiddetli baş ağrısı, yüzde kızarma ve terleme (T6 ve üzeri yaralanmada; 112)</li>
        <li>Nefes darlığı ya da göğüs ağrısı (112)</li>
        <li>Tek bacakta şişlik, sıcaklık ya da kızarıklık</li>
        <li>Açılmış ya da rengi düzelmeyen cilt bölgesi</li>
        <li>Ateş; idrarda bulanıklık ya da kötü koku</li>
        <li>Kasılmalarda ani artış, yeni başlayan güçsüzlük ya da his kaybı</li>
      </ul>
      {CTA_CARD("Omurilik yaralanması sonrası rehabilitasyon", "omurilik yaralanması sonrası rehabilitasyon")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(SC_SRC)}
    </div>
  </section>
</main>'''

page("omurilik-yaralanmasi.html", "Omurilik Yaralanması Sonrası Rehabilitasyon",
     "Omurilik yaralanmasından sonra rehabilitasyon neleri kapsar? Bası yarasını önleme, basınç azaltma teknikleri, egzersiz kılavuzu, otonom disrefleksi ve tekerlekli sandalye kullananlar için altı uygulama.",
     "omurilik-yaralanmasi.html", NECK_CSS, SC_BODY, YT_JS,
     seo_title="Omurilik Yaralanması: Rehabilitasyon, Bası Yarası ve Egzersiz | İhsan Eren",
     condition="Omurilik yaralanması", faq_items=SC_FAQ)

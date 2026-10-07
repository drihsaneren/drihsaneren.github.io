# -*- coding: utf-8 -*-
# Yeni hastalık rehberleri (12): yüz felci (Bell felci).
# cond12_part.py'den sonra exec edilir. Ana ileti: ilk 72 saatte kortizon + göz koruma; yüzü ZORLAMAK iyileşmeyi hızlandırmaz
# (Facial Palsy UK, Oxford University Hospitals). Bu yüzden "altı egzersiz" değil "altı güvenli uygulama": üçü ilk haftalar için
# (göz, masaj, gevşeme), üçü hareket geri gelirken (küçük, yavaş, iki tarafı eşit). Akupunktur: kanıt özeti + kullanıcının isteğiyle
# "kişisel klinik gözlemim" kutusu (OBS). Videolar Queen Victoria Hospital kanalından (oEmbed ile doğrulandı).

_FC = "#efe9d6"
def _face(brows=None, eyes=None, mouth=None, extra=""):
    brows = brows or f'<path d="M40 45 Q47 41 54 45 M66 45 Q73 41 80 45" stroke="{_FC}" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
    eyes = eyes or f'<circle cx="47" cy="55" r="3.4" fill="{_FC}"/><circle cx="73" cy="55" r="3.4" fill="{_FC}"/>'
    mouth = mouth or f'<path d="M48 79 Q60 82 72 79" stroke="{_FC}" stroke-width="3" fill="none" stroke-linecap="round"/>'
    return '<circle class="hd" cx="60" cy="60" r="36"/>' + brows + eyes + mouth + extra

# 1 · gözü parmağın sırtıyla kapatma
SV["fp_eye"] = fig(_face(
    eyes=f'<circle cx="47" cy="55" r="3.4" fill="{_FC}"/><ellipse cx="73" cy="55" rx="3.6" ry="3.4" fill="{_FC}"><animate attributeName="ry" values="3.4;0.6;3.4" {A}/></ellipse>',
    extra=f'<g>{anim_t("0 0;0 7;0 0")}<rect x="68.5" y="22" width="9" height="27" rx="4.5" fill="#C8963E"/></g>'), "Gözü parmakla kapatma")
# 2 · yüz masajı (küçük daireler)
SV["fp_massage"] = fig(_face(
    extra='<circle class="band" cx="78" cy="70" r="7"/><circle class="band" cx="76" cy="40" r="6"/>'
          f'<g>{anim_t("0 78 70;360 78 70", dur="2.8s", kt="0;1", typ="rotate")}<circle cx="78" cy="63" r="3.6" fill="#C8963E"/></g>'
          f'<g>{anim_t("0 76 40;360 76 40", dur="2.8s", kt="0;1", typ="rotate")}<circle cx="76" cy="34" r="3.2" fill="#C8963E"/></g>'), "Yüz masajı")
# 4 · aynada küçük, iki tarafı eşit gülümseme
SV["fp_smile"] = fig(_face(
    mouth=f'<path d="M48 79 Q60 81 72 79" stroke="{_FC}" stroke-width="3" fill="none" stroke-linecap="round">{anim_d("M48 79 Q60 81 72 79;M45 76 Q60 88 75 76;M48 79 Q60 81 72 79")}</path>',
    extra='<path class="band" d="M60 14 V106"/><path d="M36 76 l-5 3 M84 76 l5 3" stroke="#C8963E" stroke-width="2.5" stroke-linecap="round"/>'), "Küçük gülümseme")
# 5 · nazik kaş kaldırma
SV["fp_brow"] = fig(_face(
    brows=f'<g>{anim_t("0 0;0 -4;0 0")}<path d="M40 45 Q47 41 54 45 M66 45 Q73 41 80 45" stroke="{_FC}" stroke-width="2.6" fill="none" stroke-linecap="round"/></g>',
    extra='<path d="M43 35 l4 -4 l4 4 M69 35 l4 -4 l4 4" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'), "Kaş kaldırma")
# 6 · dudakları öne toplama
SV["fp_lips"] = fig(_face(
    mouth=f'<ellipse cx="60" cy="80" rx="12" ry="1.6" fill="none" stroke="{_FC}" stroke-width="3"><animate attributeName="rx" values="12;5;12" {A}/><animate attributeName="ry" values="1.6;4.6;1.6" {A}/></ellipse>',
    extra='<path d="M40 80 h6 M80 80 h-6" stroke="#C8963E" stroke-width="2.5" stroke-linecap="round"/>'), "Dudakları toplama")

EXT.update({
 "fp_eye": ("Gözü parmakla kapatma", "Gözünüz kendiliğinden kapanmıyorsa, temiz elinizle işaret parmağınızın sırtını üst göz kapağınıza koyun; kapağı nazikçe aşağı indirip birkaç saniye kapalı tutun. Göz yüzeyinin nemli kalmasına yardım eder. Gözünüzü sıkarak kapatmaya çalışmayın.", "Gün içinde sık sık"),
 "fp_massage": ("Yüz masajı", "Parmak uçlarınızla alnınıza, şakağınıza, yanağınıza, çenenize ve boynunuza yavaş, küçük daireler çizin. Bastırmayın; ağrı ya da rahatsızlık olmamalı. Kasların yumuşak ve esnek kalmasına yardım eder.", "Birkaç dakika, günde birkaç kez"),
 "fp_smile": ("Aynada küçük gülümseme", "Hareket geri gelmeye başladıysa aynanın karşısına geçin. Dudaklarınız kapalıyken çok hafif gülümseyin; amaç büyük bir gülüş değil, iki dudak köşesinin eşit hareket etmesi. Sağlam taraf öne geçiyorsa hareketi küçültün. 2–3 saniye tutup yavaşça bırakın.", "5 tekrar, günde 2–3 kez"),
 "fp_brow": ("Nazik kaş kaldırma", "Aynaya bakarak iki kaşınızı birlikte, yavaşça ve az miktarda kaldırın. Gözünüzün ya da ağzınızın çevresinde istemeden bir hareket başlıyorsa durun ve hareketi küçültün.", "5 tekrar, günde 2–3 kez"),
 "fp_lips": ("Dudakları öne toplama", "Aynaya bakarak dudaklarınızı öpücük verir gibi yavaşça öne toplayın; iki tarafın eşit hareket ettiğini izleyin. 2–3 saniye tutup gevşetin. Güç kullanmayın.", "5 tekrar, günde 2–3 kez"),
})
_ex2("fp_breath", "plb", "Gevşeme nefesi", "Rahatça oturun; omuzlarınızı ve çenenizi gevşetin, dişleriniz birbirine değmesin. Burnunuzdan sakin bir nefes alın ve yavaşça verin. Yüzünüzün iki yanının da yumuşadığını hissedin. Gerginlik yüzü zorlamanıza yol açar; gevşemek de bakımın parçasıdır.", "5–10 nefes, günde birkaç kez")

# ============================================================== YÜZ FELCİ
FP_FAQ = [
 ("Yüz felci kendiliğinden geçer mi?", "Çoğu kişide belirtiler birkaç hafta içinde düzelmeye başlar ve altı ay içinde geçer; bazı kişilerde daha uzun sürebilir ya da kalıcı etkiler kalabilir. İlk 72 saatte başlanan kortizon tedavisi tam iyileşme şansını artırır. Üç hafta içinde hiç düzelme yoksa hekiminize yeniden başvurun."),
 ("Yüz felcinde egzersize ne zaman başlanır?", "İlk haftalarda yüzü zorlayarak çalıştırmak iyileşmeyi hızlandırmaz, istenmeyen etkilere de yol açabilir; bu dönemde göz bakımı ve nazik masaj yeterlidir. Hareket geri gelmeye başladığında, tercihen bir fizyoterapist değerlendirdikten sonra, aynada küçük ve iki tarafı eşit hareketlerle başlanır."),
 ("Elektrik tedavisi yüz felcine iyi gelir mi?", "Dört çalışmayı (313 kişi) inceleyen Cochrane derlemesinde elektrik uyarımı, altı aydaki iyileşme açısından sahte uygulamadan üstün bulunmadı; düşük kaliteli bir çalışmada sonuçlar daha kötüydü. Bu yüzden rutin olarak önerilmez."),
 ("Akupunktur yüz felcine iyi gelir mi?", "Araştırmalar kesin bir şey söyleyemiyor: Altı çalışmayı inceleyen Cochrane derlemesi, çalışmaların kalitesi yetersiz olduğu için sonuca varamadı. Kendi klinik gözlemimde ise akupunkturun yüz felcinde ciddi biçimde etkili olduğunu gördüm. Türkiye'de akupunkturu yalnızca sertifikalı hekimler uygulayabilir; kortizon tedavisinin ve göz bakımının yerini tutmaz."),
]

FP_SRC = [
 "Berkshire Healthcare NHS Foundation Trust. " + ext("https://www.berkshirehealthcare.nhs.uk/media/109514454/facial-palsy-physio-leaflet-berkshire-healthcare.pdf", "Facial palsy: physiotherapy advice") + ". Patient leaflet.",
 "Chen N, Zhou M, He L, Zhou D, Li N. " + ext("https://www.cochrane.org/CD002914/NEUROMUSC_acupuncture-for-bells-palsy", "Acupuncture for Bell's palsy") + ". Cochrane Database Syst Rev. 2010;(8):CD002914.",
 "Facial Palsy UK. " + ext("https://www.facialpalsy.org.uk/support/patient-guides/initial-advice-and-guidance/", "Initial advice and guidance") + ".",
 "Facial Palsy UK. " + ext("https://www.facialpalsy.org.uk/support/self-help-videos/management-of-flaccid-facial-paralysis-floppy-face/", "Management of flaccid facial paralysis (floppy face)") + ".",
 "Madhok VB, Gagyor I, Daly F, et al. " + ext("https://www.cochrane.org/CD001942/NEUROMUSC_corticosteroids-bells-palsy", "Corticosteroids for Bell's palsy (idiopathic facial paralysis)") + ". Cochrane Database Syst Rev. 2016;(7):CD001942.",
 "National Institute of Neurological Disorders and Stroke. " + ext("https://www.ninds.nih.gov/health-information/disorders/bells-palsy", "Bell's palsy") + ". Last reviewed 19 May 2026.",
 "NHS. " + ext("https://www.nhs.uk/conditions/bells-palsy/", "Bell's palsy") + ". Page last reviewed 4 July 2023.",
 "Oxford University Hospitals NHS Foundation Trust. " + ext("https://www.ouh.nhs.uk/media/5xqbw1m0/90999palsy.pdf", "Facial palsy") + ". Patient leaflet OMI 90999. October 2025.",
 "Teixeira LJ, Valbuza JS, Prado GF. " + ext("https://www.cochrane.org/CD006283/NEUROMUSC_physical-therapy-for-bells-palsy-idiopathic-facial-paralysis", "Physical therapy for Bell's palsy (idiopathic facial paralysis)") + ". Cochrane Database Syst Rev. 2011;(12):CD006283.",
]

FP_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Yüz felci (Bell felci)</h1>
    <p class="lede">Yüz felci, yüz sinirinin etkilenmesiyle yüzün bir yarısında aniden gelişen güçsüzlüktür. Çoğu kişi haftalar ya da aylar içinde iyileşir. En önemli iki adım, ilk üç gün içinde başlanan kortizon tedavisi ve gözün korunmasıdır; yüzü zorlayarak çalıştırmak ise iyileşmeyi hızlandırmaz.</p>
    <p class="meta">Son güncelleme: 7 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>72 saat</b><span>Tedavi bu süre içinde başlarsa daha etkili oluyor (NHS)</span></div>
        <div class="stat"><b>%17 / %28</b><span>Tam iyileşmeyenlerin oranı: kortizon alanlar ile almayanlar (7 çalışma, 895 kişi)</span></div>
        <div class="stat"><b>6 ay</b><span>Belirtilerin çoğunlukla düzeldiği süre; bazı kişilerde daha uzun sürebilir</span></div>
        <div class="stat"><b>15–45 yaş</b><span>En sık görüldüğü yaş aralığı; her yaşta ortaya çıkabilir</span></div>
      </div>
      <div class="note warn" style="margin-top:22px"><strong>Önce inme olmadığından emin olun.</strong> Yüzde sarkmayla birlikte kolunuzu kaldıramıyor ya da konuşmakta zorlanıyorsanız beklemeden 112'yi arayın. Yalnızca yüzünüz etkilenmiş olsa bile aynı gün bir hekime görünün: Tanıyı hekim koyar ve tedavi erken başladığında daha etkilidir.</div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Yüz kaslarını çalıştıran yüz siniri (yedinci kafa siniri) etkilenir; yüzün bir yanı güçsüzleşir ya da hiç hareket etmez. Belirtiler 48–72 saat içinde, aniden ortaya çıkar.</p>
        <p class="soft">Kesin nedeni bilinmiyor. Vücutta uyuyan bir virüsün (uçuk ya da suçiçeği virüsü gibi) yeniden etkinleşmesi olası tetikleyiciler arasında sayılıyor. Gebelik, diyabet, yüksek tansiyon, obezite ve üst solunum yolu enfeksiyonları riski artırıyor.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Yüzün bir yanında güçsüzlük ya da hareket ettirememe</li>
          <li>Göz kapağında ya da ağız köşesinde sarkma</li>
          <li>Gözü kapatmakta zorlanma; gözde kuruluk ya da sulanma</li>
          <li>Tat almada değişiklik, ağız kuruluğu ya da ağızdan salya akması</li>
          <li>Seslere karşı hassasiyet</li>
          <li>Yüzde ya da çenede ağrı</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>İlk günler: iki öncelik</h2>
      <p class="soft"><strong>Kortizon.</strong> Genellikle on günlük bir kortizon tedavisi verilir, bazen yanına antiviral ilaç eklenir. Yedi çalışmayı (895 kişi) inceleyen Cochrane derlemesinde, kortizon alanların %17'sinde, almayanların %28'inde yüz tam iyileşmedi; yani her on kişi tedavi edildiğinde bir kişide eksik iyileşme önleniyor. Yan etkiler açısından iki grup arasında anlamlı fark görülmedi. Tedavi ilk 72 saatte başladığında daha etkili olduğu için beklememek gerekir.</p>
      <p class="soft"><strong>Gözü korumak.</strong> Göz kapanmadığında yüzeyi kurur ve zarar görebilir. Gündüz göz damlası, gece göz merhemi kullanılır; uyurken göz, hekimin önerdiği bantla kapatılır. Dışarıda gözü rüzgâr ve tozdan korumak için yanları kapalı bir gözlük işe yarar. Göz kırpmak zorsa kapağı parmağınızın sırtıyla nazikçe kapatabilirsiniz.</p>
      <div class="callout">
        <p>Yemek yerken yumuşak ve soslu yiyecekler kolaylık sağlar. Yemekten sonra yanağınızın iç tarafında yiyecek kalıp kalmadığına bakın ve dişlerinizi fırçalayın. İçecek dökülüyorsa pipet ya da ağızlıklı bardak kullanın; alt dudağınızı parmağınızla desteklemek de yardımcı olur.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Yüzümü çalıştırmalı mıyım?</h2>
      <p class="soft">İlk akla gelen, yüzü zorlayarak “çalıştırmak” olur. Oysa yüz felci alanındaki uzman kuruluşlar ilk dönemde tersini öneriyor. İngiltere'deki Facial Palsy UK'ye göre bu dönemde yüzü egzersizle çalıştırmaya gerek yok; bu, iyileşmeyi hızlandırmıyor. Hareketleri zorlamak, gözü sıkarak kapatmaya çalışmak ve sakız çiğnemek istenmeyen yan etkilere yol açabiliyor. Kuruluşun özeti şöyle: Yüzünüzü iyileşme boyunca olabildiğince güçlü değil, olabildiğince nazik kullanırsanız daha iyi ve daha az yan etkili bir iyileşme beklenir.</p>
      <p class="soft">Hareket geri gelmeye başladığında durum değişir. Fizik tedavi yöntemlerini inceleyen Cochrane derlemesine (12 çalışma, 872 kişi) göre kişiye özel yüz egzersizleri, özellikle orta dereceli ve uzun süren felçlerde yüz işlevini iyileştirebiliyor; kanıtın kalitesi düşük. Aynı derlemede elektrik uyarımı sahte uygulamadan üstün bulunmadı.</p>
      <div class="callout">
        <p>İyileşme sırasında bazı kişilerde istemsiz eş hareketler gelişebilir; örneğin gülümserken göz kısılır. Bu yüzden hareketler aynada, yavaş, küçük ve iki tarafı eşit yapılır. Egzersize başlamadan önce yüz rehabilitasyonunda deneyimli bir fizyoterapistin sizi değerlendirmesi en doğrusudur.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Akupunktur: araştırmalar ve klinik gözlemim</h2>
      <p class="soft">Altı çalışmayı (537 kişi) inceleyen Cochrane derlemesi, çalışmaların kalitesi yetersiz olduğu için akupunkturun yüz felcinde etkili olup olmadığı konusunda bir sonuca varamadı; yan etki bildirilmedi, ancak çalışmalar bunu düzenli olarak kaydetmemişti. Facial Palsy UK, ilk dönemde iğnelerden elektrik verilen akupunkturdan kaçınılmasını öneriyor.</p>
      {OBS("Kendi klinik gözlemimde akupunkturun yüz felcinde ciddi biçimde etkili olduğunu gördüm.")}
      <div class="callout">
        <p>{ACU_LAW}</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <ul class="tx">
        <li><b>Kortizon</b><span>İlk 72 saatte başlanır; tam iyileşme şansını artırır. Hekiminiz düzenler.</span></li>
        <li><b>Antiviral ilaç</b><span>Bazı durumlarda kortizona eklenir; kararı hekiminiz verir.</span></li>
        <li><b>Göz bakımı</b><span>Damla, merhem ve gece bantlama; göz kapanmadığı sürece her gün.</span></li>
        <li><b>Masaj ve gevşeme</b><span>İlk haftalarda kasları yumuşak tutmak için nazik masaj; yüzü zorlamak yok.</span></li>
        <li><b>Yüz rehabilitasyonu</b><span>Hareket geri gelirken ya da iyileşme geciktiğinde, kişiye özel yüz egzersizleri.</span></li>
        <li><b>Kalıcı etkilerde</b><span>Uzun süren olgularda hekiminiz ek tedavi seçeneklerini, gerekirse cerrahiyi değerlendirir.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde bakım</p>
      <h2>Yüz felci için altı güvenli uygulama</h2>
      <p class="soft">İlk üçü ilk haftalar içindir: Gözü korur, kasları yumuşak tutar. Son üçü yalnızca hareket geri gelmeye başladığında ve tercihen fizyoterapistiniz onay verdikten sonra yapılır. Hepsinde kural aynı: yavaş, küçük, zorlamadan.</p>
      {ex_grid(["fp_eye", "fp_massage", "fp_breath", "fp_smile", "fp_brow", "fp_lips"])}
      <div class="callout">
        <p>Bu uygulamalar yüz siniri felci içindir. Yüzdeki güçsüzlük inmeye bağlıysa program farklıdır; rehabilitasyon ekibinize danışın.</p>
      </div>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Yüz felci için videolar</h2>
      <p class="soft">İngiltere'de yüz felci tedavisinde uzmanlaşmış Queen Victoria Hospital'ın YouTube kanalından, felcin ilk dönemi için hazırlanmış iki video. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("xmnpEpmmiTQ", "Göz bantlama videosunu oynat", "Eye Taping - Management of Flaccid Paralysis - Facial Palsy DVD 1")}
          <h3>Gözü bantlama</h3>
          <p>Göz kapanmadığında gece için bantlamanın nasıl yapıldığını gösteren video.</p>
        </div>
        <div class="vid">
          {vbox("u0pEAFvnUSg", "Yüz masajı videosunu oynat", "Massage - Management of Flaccid Paralysis - Facial Palsy DVD 1")}
          <h3>Yüz masajı</h3>
          <p>İlk dönemde yüz kaslarına uygulanan masajı gösteren video.</p>
        </div>
      </div>
      <p class="meta">Videolar Queen Victoria Hospital kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(FP_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Yüzde sarkmayla birlikte kolda ya da bacakta güçsüzlük ya da konuşma bozukluğu (112'yi arayın)</li>
        <li>Yüzde güçsüzlük yeni başladıysa: aynı gün, en geç ilk üç gün içinde</li>
        <li>Gözde ağrı, kızarıklık ya da bulanık görme</li>
        <li>Kulakta ya da kulak çevresinde ağrılı kabarcıklar ya da döküntü</li>
        <li>Üç hafta içinde hiçbir düzelme olmaması</li>
      </ul>
      {CTA_CARD("Yüz felcine bağlı şikâyetleriniz", "yüz felci")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(FP_SRC)}
    </div>
  </section>
</main>'''

page("yuz-felci.html", "Yüz Felci (Bell Felci)",
     "Yüz felci neden olur, nasıl geçer? İlk 72 saatte kortizon, göz koruma, yüzü neden zorlamamalı, egzersize ne zaman başlanır, akupunktur ve elektrik tedavisi için kanıt, evde altı güvenli uygulama ve videolar.",
     "yuz-felci.html", NECK_CSS, FP_BODY, YT_JS,
     seo_title="Yüz Felci (Bell Felci): Tedavi, Göz Bakımı ve Egzersiz | İhsan Eren",
     condition="Yüz felci (Bell paralizisi)", faq_items=FP_FAQ)

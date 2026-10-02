# -*- coding: utf-8 -*-
# Karpal tünel sendromu sayfası. shoulder_part.py'den sonra exec edilir.

# Tendon kaydırma (el yandan): düz → kanca → tam yumruk → masa → düz yumruk → düz
TG_DUR, TG_KT = "9s", "0;0.2;0.4;0.6;0.8;1"
TG_STATES = ["M40 52 L40 34 L40 21 L40 11", "M40 52 L40 34 L53 34 L53 44",
             "M40 52 L58 52 L58 65 L48 65", "M40 52 L58 52 L71 52 L81 52",
             "M40 52 L58 52 L58 65 L58 75", "M40 52 L40 34 L40 21 L40 11"]
SV["tglide"] = fig('<g transform="translate(12 0)">'
    '<path class="fig" d="M40 116 L40 92"/>'
    '<rect x="30" y="50" width="20" height="44" rx="8" fill="#2A6F6B"/>'
    '<path class="fig" d="M47 86 L58 75"/>'
    f'<path class="fig hl" d="{TG_STATES[0]}">{anim_d(";".join(TG_STATES), dur=TG_DUR, kt=TG_KT)}</path></g>',
    "Tendon kaydırma")

# Median sinir kaydırma (önden): kol yana açık, bilek geriye bükülürken baş karşı tarafa eğilir.
MG_DUR = "4s"
SV["mglide"] = fig(GRD +
    f'<path class="fig" d="M48 40 H80 M64 40 V80 M64 80 L56 112 M64 80 L72 112 M80 40 L84 62 L82 78"/>'
    '<path class="fig hl" d="M48 40 H20"/>'
    f'<g>{anim_t("0 20 40;-70 20 40;0 20 40", dur=MG_DUR, typ="rotate")}<path class="fig hl" d="M20 40 H8"/></g>'
    f'<g>{anim_t("0 64 40;20 64 40;0 64 40", dur=MG_DUR, typ="rotate")}'
    '<path class="fig" d="M64 40 V30"/><circle class="hd" cx="64" cy="21" r="8"/></g>',
    "Median sinir kaydırma")

# Bilek bükücü germe (yandan): kol önde düz, avuç yukarı; diğer el parmakları aşağı-geri çeker.
SV["wflex"] = fig(GRD +
    '<circle class="hd" cx="44" cy="20" r="7"/>'
    '<path class="fig" d="M44 30 V76 L38 112 M44 76 L50 112"/>'
    '<path class="fig" d="M44 40 H84"/>'
    f'<g>{anim_t("0 84 40;70 84 40;0 84 40", typ="rotate")}<path class="fig hl" d="M84 40 H98"/></g>'
    f'<path class="fig" d="M44 46 L70 58 L96 44">{anim_d("M44 46 L70 58 L96 44;M44 46 L70 62 L89 53;M44 46 L70 58 L96 44")}</path>',
    "Bilek bükücü germe")

# Başparmak germe (avuç yukarı, önden): başparmak dışa açılır.
SV["thumb"] = fig(
    '<path class="fig" d="M60 112 L60 84"/>'
    '<rect x="46" y="48" width="28" height="38" rx="8" fill="#2A6F6B"/>'
    '<path class="fig" d="M50 48 V24 M57 48 V18 M64 48 V20 M71 48 V28"/>'
    f'<g>{anim_t("0 48 76;-40 48 76;0 48 76", typ="rotate")}<path class="fig hl" d="M48 76 L36 62 L32 50"/></g>'
    '<path d="M22 70 A26 26 0 0 1 26 50" fill="none" stroke="#C8963E" stroke-width="2.5" stroke-dasharray="3 4" stroke-linecap="round"/>',
    "Başparmak germe")

EXT.update({
 "tglide": ("Tendon kaydırma", "Elinizi dik tutun, parmaklarınız düz olsun. Sırayla şu pozisyonlara geçin ve her birinde 3 saniye bekleyin: parmak uçlarını kıvırıp kanca yapın, tam yumruk yapın, parmaklarınızı düz tutup yalnızca parmak köklerinden 90 derece bükün (masa pozisyonu), parmak uçları düz kalacak şekilde yumruk yapın, sonra elinizi açın. Parmak kirişlerinin tünel içinde rahat kaymasına yardım eder.", "5–10 tur, günde 3–5 kez"),
 "mglide": ("Median sinir kaydırma", "Dik durun, kolunuzu yana doğru omuz hizasında açın, dirseğiniz düz, avucunuz yukarı baksın. Bileğinizi yavaşça geriye bükerken başınızı karşı tarafa eğin, sonra ikisini birlikte başlangıca döndürün. Sinirin gerilmeden kaymasını amaçlar; karıncalanma artıyorsa hareket aralığını küçültün.", "10 tekrar, günde 2–3 kez"),
 "wflex": ("Bilek bükücü germe", "Kolunuzu önünüze uzatın, dirseğiniz düz, avucunuz yukarı baksın. Diğer elinizle parmaklarınızı nazikçe aşağı ve geriye doğru çekin; ön kolunuzun iç yüzünde hafif gerilme hissedin. Uyuşmayı artıracak kadar zorlamayın.", "15–20 saniye, 3 tekrar"),
 "thumb": ("Başparmak germe", "Elinizi avucunuz yukarı bakacak şekilde masaya koyun. Diğer elinizle başparmağınızı nazikçe dışa ve geriye doğru açın; başparmak kökünde hafif gerilme hissedin.", "15–20 saniye, 3 tekrar"),
})

KT_FAQ = [
 ("Karpal tünel sendromu kendiliğinden geçer mi?", "Hafif durumlarda ve özellikle gebelikte belirtiler birkaç ay içinde kendiliğinden azalabilir. Uzun süren ya da giderek artan uyuşma ve güç kaybında ise sinirin kalıcı hasar görmemesi için tedavi geciktirilmemelidir."),
 ("Gece ateli ne kadar süre kullanılmalı?", "Bileği düz tutan atel özellikle geceleri takılır. İngiltere sağlık hizmeti (NHS) 6 haftaya kadar denenmesini öneriyor. Belirtileriniz gündüz de artıyorsa kullanım şeklini fizyoterapistinizle belirleyin."),
 ("Bilgisayar kullanmak karpal tünele neden olur mu?", "Amerikan Ortopedi Akademisi'nin 2024 kılavuzuna göre yoğun klavye kullanımı ile karpal tünel sendromu arasında güçlü bir ilişkiyi destekleyen kanıt yok. Tekrarlayan kavrama gerektiren işler, fazla kilo ve gebelik ise risk etkenleri arasında yer alıyor."),
 ("Kortizon iğnesi işe yarar mı?", "Kortizon iğnesi belirtileri kısa sürede azaltabilir. Ancak 2024 kılavuzuna göre uzun vadeli faydası gösterilemedi; belirtiler zamanla geri dönebilir."),
 ("Ameliyat ne zaman gerekir?", "Başparmak kökündeki kaslarda incelme, sürekli uyuşma, güç kaybı ya da atel ve diğer tedavilere rağmen geçmeyen belirtiler varsa el cerrahisi değerlendirmesi gerekir. Uygun hastalarda ameliyat, 6 ve 12. ayda ameliyatsız tedaviden daha fazla fayda sağlıyor."),
 ("Egzersizler işe yarar mı?", "Tendon ve sinir kaydırma egzersizleri yaygın olarak kullanılır, ancak Cochrane derlemesine göre etkinliklerini gösteren kanıtlar sınırlı ve düşük kalitelidir. Ağrı ve uyuşmayı artırmadan, atel ve yük ayarlamasına destek olarak yapılmalıdır."),
]

KT_SRC = [
 "American Academy of Orthopaedic Surgeons. " + ext("https://www.aaos.org/quality/quality-programs/upper-extremity-programs/carpal-tunnel-syndrome/", "Management of Carpal Tunnel Syndrome: Evidence-Based Clinical Practice Guideline") + ". Rosemont (IL): AAOS; 2024.",
 "American Academy of Orthopaedic Surgeons. Management of Carpal Tunnel Syndrome: Evidence-Based Clinical Practice Guideline. Rosemont (IL): AAOS; 2016.",
 "Atroshi I, Gummesson C, Johnsson R, Ornstein E, Ranstam J, Rosén I. " + ext("https://jamanetwork.com/journals/jama/fullarticle/774263", "Prevalence of carpal tunnel syndrome in a general population") + ". JAMA. 1999;282(2):153-158.",
 "Erickson M, Lawrence M, Jansen CWS, et al. " + ext("https://www.jospt.org/doi/10.2519/jospt.2019.0301", "Hand pain and sensory deficits: carpal tunnel syndrome. Clinical practice guidelines linked to the International Classification of Functioning, Disability and Health") + ". J Orthop Sports Phys Ther. 2019;49(5):CPG1-CPG85.",
 "NHS. " + ext("https://www.nhs.uk/conditions/carpal-tunnel-syndrome/", "Carpal tunnel syndrome") + ".",
 "Page MJ, O'Connor D, Pitt V, Massy-Westropp N. " + ext("https://www.cochrane.org/evidence/CD009899_exercise-and-mobilisation-interventions-carpal-tunnel-syndrome", "Exercise and mobilisation interventions for carpal tunnel syndrome") + ". Cochrane Database Syst Rev. 2012;6:CD009899.",
 "Physiopedia. " + ext("https://www.physio-pedia.com/Carpal_Tunnel_Syndrome", "Carpal Tunnel Syndrome") + ".",
]

KT_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Karpal tünel sendromu</h1>
    <p class="lede">Bilekteki dar bir kanalda (karpal tünel) orta sinirin (median sinir) sıkışmasıyla ortaya çıkar. Başparmak, işaret ve orta parmakta uyuşma, karıncalanma ve ağrı yapar; belirtiler özellikle geceleri artar. Erken dönemde gece ateli ve günlük yükün ayarlanmasıyla çoğu zaman rahatlar.</p>
    <p class="meta">Son güncelleme: {UPDATED}</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%14</b><span>Toplumda elde uyuşma, karıncalanma ya da ağrı yaşayan kişi</span></div>
        <div class="stat"><b>%3,8</b><span>Muayeneyle karpal tünel sendromu tanısı alan kişi</span></div>
        <div class="stat"><b>%2,7</b><span>Tanısı sinir iletim testiyle de doğrulanan kişi</span></div>
        <div class="stat"><b>6 hafta</b><span>Gece atelinin önerilen deneme süresi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">El bileğinin avuç tarafında kemiklerin ve kalın bir bağın oluşturduğu dar bir kanal vardır. Parmakları büken kirişler ve orta sinir bu kanaldan geçer. Kanal içindeki basınç arttığında sinir sıkışır ve sinirin beslediği parmaklarda belirtiler başlar.</p>
        <p class="soft">Tanı çoğunlukla belirtiler ve muayeneyle konur. Sinir iletim testi (EMG) ya da görüntüleme her hastada gerekmez; tanıdan emin olunamadığında ya da ameliyat planlanırken istenebilir.</p>
      </div>
      <div>
        <h2>Belirtiler ve risk etkenleri</h2>
        <ul class="dots">
          <li>Başparmak, işaret, orta parmak ve yüzük parmağının yarısında uyuşma ve karıncalanma</li>
          <li>Geceleri artan, uykudan uyandıran, elinizi sallayınca geçen belirtiler</li>
          <li>Telefon tutarken, araç kullanırken ya da kitap okurken artan uyuşma</li>
          <li>Başparmakta güçsüzlük, kavramada zorlanma, eşyaları düşürme</li>
          <li>Risk etkenleri: fazla kilo, gebelik, tekrarlayan kavrama gerektiren işler, eklem iltihabı, diyabet, aile öyküsü, önceki bilek yaralanması</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Bilgisayar kullanımı karpal tünele yol açar mı?</h2>
      <p class="soft">Yaygın inanışın aksine, Amerikan Ortopedi Akademisi'nin 2024 kılavuzuna göre yoğun klavye kullanımı ile karpal tünel sendromu arasında güçlü bir ilişkiyi destekleyen kanıt yok.</p>
      <div class="callout">
        <p>Yine de uzun süre bileği bükülü tutmak belirtileri artırabilir. Klavye ve fare kullanırken bileğinizi düz tutmak ve sık ara vermek, var olan şikâyetleri hafifletmeye yardımcı olur.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <p class="soft">Hafif ve orta şiddetteki durumlarda tedaviye ameliyatsız yöntemlerle başlanır. Kalıcı uyuşma ya da kas erimesi varsa cerrahi değerlendirme öne çıkar.</p>
      <ul class="tx">
        <li><b>Gece ateli</b><span>Bileği düz (nötr) tutan gece ateli, fizyoterapi kılavuzunun önerdiği ilk basamak tedavidir. İngiltere sağlık hizmeti (NHS) 6 haftaya kadar denenmesini öneriyor.</span></li>
        <li><b>Günlük yükü ayarlamak</b><span>Bileği tekrar tekrar bükmeyi ve güçlü kavramayı gerektiren işleri azaltmak siniri rahatlatır.</span></li>
        <li><b>Manuel terapi</b><span>Muayene bulgularına göre el, bilek ve üst ekstremiteye yönelik manuel terapi uygulanabilir; kılavuzdaki önerinin kanıt düzeyi zayıftır.</span></li>
        <li><b>Egzersiz</b><span>Tendon ve sinir kaydırma egzersizleri yaygın olarak kullanılır; ancak etkinliklerine dair kanıtlar sınırlı ve düşük kalitelidir. Destekleyici olarak, belirtileri artırmadan yapılmalıdır.</span></li>
        <li><b>Kortizon iğnesi</b><span>Belirtileri kısa sürede azaltabilir; ancak 2024 kılavuzuna göre uzun vadeli faydası gösterilemedi.</span></li>
        <li><b>Ameliyat</b><span>Bileğin avuç tarafındaki bağın gevşetilmesiyle sinir rahatlatılır. Uygun hastalarda 6 ve 12. ayda ameliyatsız tedaviden daha fazla fayda sağlar. Açık ve kapalı (endoskopik) yöntemlerin uzun vadeli sonuçları benzerdir; ameliyat yalnızca lokal anesteziyle de yapılabilir.</span></li>
        <li><b>Gebelikte</b><span>Gebeliğe bağlı karpal tünel sendromu çoğu zaman doğumdan sonraki aylarda kendiliğinden geçer; bu dönemde gece ateli iyi bir seçenektir.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Karpal tünel için dört egzersiz</h2>
      <p class="soft">Bu hareketler nazik olmalı; egzersiz sırasında ya da sonrasında uyuşma ve karıncalanma artıyorsa hareket aralığını küçültün ya da o egzersizi bırakın. Gece atelini ve günlük yük ayarlamasını destekleyici olarak yapılır.</p>
      {ex_grid(["tglide", "mglide", "wflex", "thumb"], cls="ex four")}
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Günlük hayatta bileğiniz için</h2>
        <p class="soft">Amaç eli kullanmayı bırakmak değil, sinirin üzerindeki basıncı artıran pozisyonları azaltmaktır.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Geceleri bileğinizi bükerek uyumamaya dikkat edin; atel bu konuda yardımcı olur.</li>
        <li>Telefonu uzun süre aynı elle ve bileğiniz bükülü şekilde tutmayın, sık ara verin.</li>
        <li>Klavye ve fare kullanırken bileğinizi düz tutun, ön kollarınızı destekleyin.</li>
        <li>Güçlü ve tekrarlayan kavrama gerektiren işleri bölün, mümkünse iki elinizi dönüşümlü kullanın.</li>
        <li>Belirtiler başladığında elinizi sallamak ve pozisyonunuzu değiştirmek rahatlatır.</li>
      </ul>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Karpal tünel sendromu için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("-hlL-E9G-wE", "Karpal tünel germe videosunu oynat", "Single Best Stretch for Carpal Tunnel Syndrome + 5 Helpful Hints")}
          <h3>Karpal tünel için germe ve beş öneri</h3>
          <p>Bilek için germe hareketi ve günlük hayatta dikkat edilecekler.</p>
        </div>
        <div class="vid">
          {vbox("fXgGRnK7k5I", "Karpal tünel egzersizleri videosunu oynat", "Top 2 Exercises &amp; Treatment For Carpal Tunnel Syndrome (Science Proven) Plus 2 Self-Tests")}
          <h3>İki egzersiz ve iki kendi kendine test</h3>
          <p>Karpal tünel için kullanılan egzersizler ve basit testler.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(KT_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlar sinirin ciddi şekilde etkilendiğini ya da uyuşmanın başka bir nedeni olduğunu gösterebilir. Beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Sürekli uyuşma, başparmak kökündeki kaslarda incelme ya da erime</li>
        <li>Elde belirgin güç kaybı, sık sık eşya düşürme, düğme iliklemede zorlanma</li>
        <li>Uyuşmanın boyuna ve kolun tamamına yayılması ya da iki elde birlikte bacaklarda da uyuşma (boyun ya da omurilik kaynaklı olabilir)</li>
        <li>Ani başlayan kol ya da yüz güçsüzlüğü, konuşma bozukluğu (inme olabilir, <strong>112</strong>'yi arayın)</li>
        <li>Bilek yaralanması sonrası başlayan şiddetli ağrı, şişlik ve uyuşma</li>
        <li>Bilekte kızarıklık, sıcaklık ve ateş</li>
      </ul>
      {CTA_CARD("El ve bilek şikâyetleriniz", "karpal tünel sendromu")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(KT_SRC)}
    </div>
  </section>
</main>'''

page("karpal-tunel-sendromu.html", "Karpal Tünel Sendromu",
     "Karpal tünel sendromu nedir, elde uyuşma neden geceleri artar, bilgisayar kullanmak neden olur mu? Gece ateli, tedavi seçenekleri, evde dört egzersiz, videolar ve uyarı işaretleri.",
     "karpal-tunel-sendromu.html", NECK_CSS, KT_BODY, YT_JS,
     seo_title="Karpal Tünel Sendromu: Belirtiler, Egzersizler ve Tedavi | İhsan Eren",
     condition="Karpal tünel sendromu", about=cond("Karpal tünel sendromu"),
     faq_items=pick(KT_FAQ, 0, 1, 2, 4))

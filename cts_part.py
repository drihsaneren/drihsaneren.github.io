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
 ("Karpal tünel sendromu kendiliğinden geçer mi?", "Bazı kişilerde geçebilir. Tedavi görmeyen 196 hastanın (274 el) 10–15 ay izlendiği bir çalışmada bir kısmında belirtiler ve sinir ölçümleri kendiliğinden düzeldi; belirtilerin kısa süredir olması ve genç yaş daha iyi seyirle ilişkiliydi, iki elde birden belirti ve olumlu Phalen testi ise daha kötü seyirle. Uzun süren ya da giderek artan uyuşma ve güç kaybında sinirin kalıcı hasar görmemesi için tedavi geciktirilmemelidir."),
 ("Gece ateli ne kadar süre kullanılmalı?", "Bileği düz tutan atel özellikle geceleri takılır. İngiltere sağlık hizmeti (NHS) 6 haftaya kadar denenmesini öneriyor. 2026 fizyoterapi kılavuzuna göre gece ateli yetmezse gündüz de takmak ya da atelin pozisyonunu değiştirmek düşünülebilir; bunu fizyoterapistinizle birlikte belirleyin."),
 ("Bilgisayar kullanmak karpal tünele neden olur mu?", "Amerikan Ortopedi Cerrahları Akademisi'nin (AAOS) 2024 kılavuzu, uzmanların ortak görüşüne dayanarak, yoğun klavye kullanımı ile karpal tünel sendromu arasında ilişki olmadığını belirtiyor; bu, kılavuzdaki en düşük kanıt düzeyidir. Tekrarlayan kavrama gerektiren işler, fazla kilo ve gebelik ise risk etkenleri arasında yer alıyor."),
 ("Kortizon iğnesi işe yarar mı?", "Kortizon iğnesi belirtileri kısa sürede azaltabilir: 234 kişiyle yapılan bir çalışmada tek iğne, 6. haftada gece atelinden daha fazla rahatlama sağladı; 6. ayda ise iki grup arasında fark kalmadı. 2024 AAOS kılavuzuna göre kortizon iğnesinin uzun vadeli faydası yok; belirtiler zamanla geri dönebilir. Kararı hekiminizle birlikte verebilirsiniz."),
 ("Ameliyat ne zaman gerekir?", "Başparmak kökündeki kaslarda incelme, sürekli uyuşma, güç kaybı ya da atel ve diğer tedavilere rağmen geçmeyen belirtiler varsa el cerrahisi değerlendirmesi gerekir. Uygun hastalarda ameliyat, 6 ve 12. ayda ameliyatsız tedaviden daha fazla fayda sağlıyor: 176 hastayla yapılan bir çalışmada 18. ayda başarı ameliyat olanlarda %90, gece ateli kullananlarda %75'ti."),
 ("Egzersizler işe yarar mı?", "Tendon ve sinir kaydırma egzersizleri yaygın olarak kullanılır, ancak Cochrane derlemesine göre etkinliklerini gösteren kanıtlar sınırlı ve düşük kalitelidir; 2026 fizyoterapi kılavuzu da bu egzersizler için net bir öneri yapmıyor. Kılavuz, başparmak kökünde kas erimesi olmayan hafif ve orta şiddetteki durumlarda atelle birlikte bir germe programını zayıf düzeyde öneriyor. Egzersizler ağrı ve uyuşmayı artırmadan, atel ve yük ayarlamasına destek olarak yapılmalıdır."),
 ("Gebelikte karpal tünel sendromu doğumdan sonra geçer mi?", "Belirtiler genellikle doğumdan sonra, şişlik azaldıkça hafifler; bu dönemde gece ateli el normale dönene kadar kullanılabilir. Ancak 45 kadının izlendiği bir çalışmada doğumdan 3 yıl sonra kadınların yaklaşık yarısında belirtiler hâlâ sürüyordu; yalnızca biri ameliyat olmuştu. Belirtiler geçmiyorsa doğumdan sonra da değerlendirme önemlidir."),
 ("EMG çektirmem gerekir mi?", "Her zaman gerekmez. AAOS'un 2024 kılavuzuna göre muayeneye dayalı CTS-6 puanlaması, rutin EMG ya da ultrason yerine kullanılabilir. Sinir iletim testi, tanıdan emin olunamadığında ya da sonucu tedaviyi (örneğin ameliyat kararını) değiştirecekse istenir."),
]

KT_SRC = [
 "American Academy of Orthopaedic Surgeons. " + ext("https://www.aaos.org/quality/quality-programs/upper-extremity-programs/carpal-tunnel-syndrome/", "Management of Carpal Tunnel Syndrome: Evidence-Based Clinical Practice Guideline") + ". Rosemont (IL): AAOS; 2024. Özetler: " + ext("https://www.aaos.org/globalassets/quality-and-practice-resources/carpal-tunnel/carpal-tunnel-2024/orthoguidelines_infographic_cts-6-5-24.pdf", "AAOS OrthoGuidelines bilgi grafiği") + "; " + ext("https://guidelinecentral.com/guideline/9593", "Guideline Central") + ".",
 "American Academy of Orthopaedic Surgeons. Management of Carpal Tunnel Syndrome: Evidence-Based Clinical Practice Guideline. Rosemont (IL): AAOS; 2016.",
 "Atroshi I, Gummesson C, Johnsson R, Ornstein E, Ranstam J, Rosén I. " + ext("https://jamanetwork.com/journals/jama/fullarticle/774263", "Prevalence of carpal tunnel syndrome in a general population") + ". JAMA. 1999;282(2):153-158.",
 "Chesterton LS, Blagojevic-Bucknall M, Burton C, et al. " + ext("https://eprints.keele.ac.uk/5455/", "The clinical and cost-effectiveness of corticosteroid injection versus night splints for carpal tunnel syndrome (INSTINCTS trial): an open-label, parallel group, randomised controlled trial") + ". Lancet. 2018;392(10156):1423-1433.",
 "Cooke ME, Duncan SFM. " + ext("https://link.springer.com/chapter/10.1007/978-3-319-57010-5_2", "History of carpal tunnel syndrome") + ". In: Duncan S, Kakinoki R, eds. Carpal Tunnel Syndrome and Related Median Neuropathies. Springer; 2017.",
 "Erickson M, Lawrence M, Jansen CWS, et al. " + ext("https://www.jospt.org/doi/10.2519/jospt.2019.0301", "Hand pain and sensory deficits: carpal tunnel syndrome. Clinical practice guidelines linked to the International Classification of Functioning, Disability and Health") + ". J Orthop Sports Phys Ther. 2019;49(5):CPG1-CPG85.",
 "Erickson M, Lawrence M, Stegink Jansen CW, et al. " + ext("https://apta.org/patient-care/evidence-based-practice-resources/cpgs/hand-pain-and-sensory-deficits-carpal-tunnel-syndrome-clinical-practice-guidelines", "Hand pain and sensory deficits: carpal tunnel syndrome. Revision 2026") + ". J Orthop Sports Phys Ther. 2026;56(4):CPG1-CPG79. doi:10.2519/jospt.2026.0301. Özet: " + ext("https://www.physiotutors.com/?p=29289", "Physiotutors") + ".",
 "Gerritsen AAM, et al. " + ext("https://www.qxmd.com/r/12215131", "Splinting vs surgery in the treatment of carpal tunnel syndrome: a randomized controlled trial") + ". JAMA. 2002.",
 "Italian CTS Study Group. " + ext("https://scilit.com/publications/14309ee24fd0bdb4712163384ca48415", "Multiperspective follow-up of untreated carpal tunnel syndrome") + ". Neurology. 2001;56(11):1459-1466.",
 "Jarvik JG, et al. " + ext("https://www.qxmd.com/r/19782873", "Surgery versus non-surgical therapy for carpal tunnel syndrome: a randomised parallel-group trial") + ". Lancet. 2009. Özet: " + ext("https://washington.edu/news/2009/09/25/surgery-provides-modest-benefit-over-non-surgical-treatment-for-patients-with-carpal-tunnel-syndrome", "University of Washington") + ".",
 "Life in the Fast Lane (LITFL). " + ext("https://litfl.com/clinical-signs-in-carpal-tunnel-syndrome/", "Clinical signs in carpal tunnel syndrome") + ".",
 "Mondelli M, Rossi S, Monti E, et al. " + ext("https://publires.unicatt.it/en/publications/long-term-follow-up-of-carpal-tunnel-syndrome-during-pregnancy-a--7/", "Long term follow-up of carpal tunnel syndrome during pregnancy: a cohort study and review of the literature") + ". Electromyogr Clin Neurophysiol. 2007;47:259-271.",
 "NHS. " + ext("https://www.nhs.uk/conditions/carpal-tunnel-syndrome/", "Carpal tunnel syndrome") + ".",
 "Page MJ, O'Connor D, Pitt V, Massy-Westropp N. " + ext("https://www.cochrane.org/evidence/CD009899_exercise-and-mobilisation-interventions-carpal-tunnel-syndrome", "Exercise and mobilisation interventions for carpal tunnel syndrome") + ". Cochrane Database Syst Rev. 2012;6:CD009899.",
 "Physiopedia. " + ext("https://www.physio-pedia.com/Carpal_Tunnel_Syndrome", "Carpal Tunnel Syndrome") + ".",
 "University Hospitals of Leicester NHS Trust. " + ext("https://www.uhleicester.nhs.uk/wp-content/uploads/2025/06/180_082024-Managing-carpal-tunnel-syndrome-in-your-hand-during-pregnancy.pdf", "Managing carpal tunnel syndrome in your hand during pregnancy") + ". Hasta bilgilendirme broşürü 180; Ağustos 2024.",
]

KT_TL = [
 ("1854", "Cerrah James Paget, bilekte orta sinirin sıkıştığı iki vakayı tanımladı: birinde sıkı bir bağ, diğerinde bilek kırığından sonra gelişen kemik çıkıntısı sinire baskı yapıyordu."),
 ("1913", "Pierre Marie ve Charles Foix, başparmak kökündeki kaslarda görülen erimenin bilekteki bağın hizasında orta sinirin etkilenmesinden kaynaklandığını tanımladı ve bu bağın erken dönemde kesilmesini önerdi."),
 ("1924", "İlk karpal tünel gevşetme ameliyatının Herbert Galloway tarafından yapıldığı bildiriliyor."),
 ("1947", "Brain, Wright ve Wilkinson, orta sinirin bilekte belirgin bir dış neden olmadan da sıkışabileceğini, his bozukluğuna ve başparmak kaslarında erimeye yol açabileceğini gösterdi; ameliyatla tedavi edilen altı vaka bildirdiler."),
 ("1950–1966", "George Phalen geniş hasta serileriyle hastalığın tanısını ve tedavisini netleştirdi ve tanınmasını sağladı. Bilekleri bükülü tutarak yapılan Phalen testi onun adını taşıyor. \"Karpal tünel sendromu\" adı ilk kez 1953'te yayımlanmış bir metinde kullanıldı."),
 ("2002", "Hollanda'da 176 hastayla yapılan çalışmada açık ameliyat gece atelinden daha iyi sonuç verdi: 18. ayda başarı %90'a karşı %75'ti. Atel grubundakilerin %41'i de bu sürede ameliyat olmuştu."),
 ("2009", "116 hastayla yapılan çalışmada ameliyat, el terapisi ve ultrason tedavisi içeren ameliyatsız tedaviye göre 12. ayda el işlevinde ve belirtilerde daha iyi sonuç verdi; fark ılımlıydı ve ameliyatsız tedavi alanlar da düzeldi."),
 ("2018", "234 kişiyle yapılan INSTINCTS çalışmasında tek kortizon iğnesi, gece atelinden 6. haftada daha fazla rahatlama sağladı; 6. ayda iki grup arasında fark kalmadı."),
 ("2024", "Amerikan Ortopedi Cerrahları Akademisi (AAOS) kılavuzunu güncelledi: muayeneye dayalı CTS-6 puanlaması rutin EMG ve ultrason yerine kullanılabilir; kortizon ve PRP iğnelerinin uzun vadeli yararı yok; küçük kesili açık ameliyat ile kapalı (endoskopik) ameliyatın sonuçları farksız."),
 ("2026", "Amerikan Fizyoterapi Derneği'nin (APTA) ortopedi ile el ve üst ekstremite akademilerinin fizyoterapi kılavuzu güncellendi: hafif ve orta şiddette gece ateli öneriliyor; manuel terapi, lazer, şok dalga ve bantlama kısa süreli yarar için zayıf düzeyde öneriliyor; mıknatıs tedavisine karşı öneri yapılıyor."),
]

KT_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Karpal tünel sendromu</h1>
    <p class="lede">Bilekteki dar bir kanalda (karpal tünel) orta sinirin (median sinir) sıkışmasıyla ortaya çıkar. Başparmak, işaret ve orta parmakta uyuşma, karıncalanma ve ağrı yapar; belirtiler özellikle geceleri artar. Hafif ve orta şiddetteki durumlarda gece ateli ve günlük yükün ayarlanması ilk basamaktır; geçmeyen ya da ilerleyen durumlarda küçük bir ameliyatla sinir rahatlatılabilir.</p>
    <p class="meta">Son güncelleme: 31 Ekim 2026</p>
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
      {g_toc([("nedir", "Nedir?"), ("tani", "Nasıl tanınır?"), ("seyir", "Kendiliğinden geçer mi?"), ("bilgisayar", "Bilgisayar kullanımı"), ("tarihce", "Geçmişten bugüne"), ("tedavi", "Tedavi seçenekleri"), ("egzersizler", "Egzersizler"), ("gunluk", "Günlük hayatta"), ("videolar", "Videolar"), ("sss", "Sık sorulan sorular"), ("uyari", "Uyarı işaretleri")])}
    </div>
  </section>

  <section id="nedir">
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">El bileğinin avuç tarafında kemiklerin ve kalın bir bağın oluşturduğu dar bir kanal vardır. Parmakları büken kirişler ve orta sinir bu kanaldan geçer. Kanal içindeki basınç arttığında sinir sıkışır ve sinirin beslediği parmaklarda belirtiler başlar.</p>
        <p class="soft">Sinir uzun süre ve belirgin şekilde sıkışık kalırsa uyuşma kalıcı hâle gelebilir ve başparmak kökündeki kaslar zayıflayabilir; bu yüzden ilerleyen belirtiler değerlendirilmelidir.</p>
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

  <section id="tani">
    <div class="wrap">
      <h2>Nasıl tanınır?</h2>
      <p class="soft">Tanı çoğunlukla belirtilerin nerede ve ne zaman olduğuna ve muayeneye dayanır. Belirtilerin elin hangi bölgesinde olduğunu bir el çizimi üzerinde işaretlemek de değerlendirmeye yardım eder.</p>
      <div class="kinds">
        <div class="kind"><h3>CTS-6 puanlaması</h3><p>Altı bulgu birlikte değerlendirilir: uyuşmanın çoğunlukla orta sinirin beslediği parmaklarda olması, gece uyuşması, başparmak kökünde kas erimesi ya da güçsüzlük, olumlu Phalen testi, iki noktayı ayırt etmede azalma ve olumlu Tinel bulgusu. AAOS'un 2024 kılavuzu bu puanlamanın rutin EMG ya da ultrason yerine kullanılabileceğini belirtiyor. Muayenede kullanılan bir araçtır, kendi kendine tanı için değildir.</p></div>
        <div class="kind"><h3>Muayene testleri</h3><p>Phalen testinde bilekler 30–60 saniye bükülü tutulur; Tinel testinde bileğin avuç tarafına hafifçe vurulur. Parmaklarda uyuşma ya da karıncalanma ortaya çıkıyorsa test olumludur. Hiçbir test tek başına yeterince doğru değildir; bulgular birlikte yorumlanır.</p></div>
        <div class="kind"><h3>EMG ve ultrason ne zaman?</h3><p>Sinir iletim testi (EMG) ve ultrason her hastada gerekmez. Tanıdan emin olunamadığında ya da sonuç tedaviyi (örneğin ameliyat kararını) değiştirecekse istenir. AAOS'a göre MR tanı için kullanılmamalıdır.</p></div>
      </div>
    </div>
  </section>

  <section id="seyir">
    <div class="wrap">
      <h2>Kendiliğinden geçer mi?</h2>
      <p class="soft">Bazı kişilerde geçebilir. Tedavi görmeyen 196 hastanın (274 el) 10–15 ay izlendiği bir çalışmada bir kısmında belirtiler ve sinir ölçümleri kendiliğinden düzeldi. Belirtilerin kısa süredir olması ve genç yaş daha iyi seyirle; iki elde birden belirti olması ve olumlu Phalen testi ise daha kötü seyirle ilişkiliydi.</p>
      <div class="callout">
        <p><strong>Gebelikte:</strong> Belirtiler genellikle doğumdan sonra, şişlik azaldıkça hafifler. Ancak 45 kadının izlendiği bir çalışmada doğumdan 3 yıl sonra kadınların yaklaşık yarısında belirtiler hâlâ sürüyordu (yalnızca biri ameliyat olmuştu). Bu yüzden doğumdan sonra da geçmeyen belirtiler değerlendirilmelidir.</p>
      </div>
    </div>
  </section>

  <section id="bilgisayar">
    <div class="wrap">
      <h2>Bilgisayar kullanımı karpal tünele yol açar mı?</h2>
      <p class="soft">Yaygın inanışın aksine, Amerikan Ortopedi Cerrahları Akademisi'nin (AAOS) 2024 kılavuzu yoğun klavye kullanımı ile karpal tünel sendromu arasında ilişki olmadığını belirtiyor. Bu öneri araştırmadan çok uzmanların ortak görüşüne dayanıyor; kılavuzdaki en düşük kanıt düzeyidir.</p>
      <div class="callout">
        <p>Yine de uzun süre bileği bükülü tutmak belirtileri artırabilir. Klavye ve fare kullanırken bileğinizi düz tutmak ve sık ara vermek, var olan şikâyetleri hafifletmeye yardımcı olabilir. 2026 fizyoterapi kılavuzu, belirtileri olan kişilerde daha az kuvvet gerektiren klavye, dokunmatik ekran ya da fareyi eller arasında değiştirmek gibi seçenekleri zayıf düzeyde öneriyor.</p>
      </div>
    </div>
  </section>

  <section id="tarihce">
    <div class="wrap">
      <p class="eyebrow">Geçmişten bugüne</p>
      <h2>Karpal tünel sendromunun kısa tarihi</h2>
      <p class="soft">Bilekte sinir sıkışması yaklaşık 170 yıldır biliniyor; ancak hastalığın yaygın olarak tanınması 20. yüzyılın ortasını buldu. Son yıllarda araştırmalar atel, iğne ve ameliyatın yerini daha net ortaya koydu.</p>
      {g_tl(KT_TL)}
    </div>
  </section>

  <section id="tedavi">
    <div class="wrap">
      <h2>Tedavi</h2>
      <p class="soft">Hafif ve orta şiddetteki durumlarda tedaviye ameliyatsız yöntemlerle başlanır. Kalıcı uyuşma ya da kas erimesi varsa cerrahi değerlendirme öne çıkar.</p>
      <ul class="tx">
        <li><b>Gece ateli</b><span>Bileği düz (nötr) tutan gece ateli, 2026 fizyoterapi kılavuzunda hafif ve orta şiddetteki durumlar için önerilen (B düzeyi) ilk basamak tedavidir; ameliyat bekleyenlerde de kullanılabilir. İngiltere sağlık hizmeti (NHS) 6 haftaya kadar denenmesini öneriyor.</span></li>
        <li><b>Günlük yükü ayarlamak</b><span>Bileği tekrar tekrar bükmeyi ve güçlü kavramayı gerektiren işleri azaltmak siniri rahatlatır.</span></li>
        <li><b>Manuel terapi</b><span>Muayene bulgularına göre boyun ve kol boyunca sinirin sıkışabileceği bölgelere yönelik manuel terapi, hafif ve orta şiddetteki durumlarda kısa süreli yarar için uygulanabilir; kılavuzdaki önerinin kanıt düzeyi zayıftır (C) ve AAOS'a göre uzun vadeli yararı gösterilmedi.</span></li>
        <li><b>Egzersiz</b><span>Tendon ve sinir kaydırma egzersizleri yaygın olarak kullanılır; ancak etkinliklerine dair kanıtlar sınırlı ve düşük kalitelidir. Destekleyici olarak, belirtileri artırmadan yapılmalıdır.</span></li>
        <li><b>Diğer fizik tedavi yöntemleri</b><span>Lazer, şok dalga, enterferansiyel akım, yüzeysel sıcak uygulama ve bantlama 2026 fizyoterapi kılavuzunda kısa süreli yarar için zayıf düzeyde (C) öneriliyor; bantlama atelin yerine geçmez. AAOS'a göre bu yöntemlerin uzun vadeli yararı gösterilmedi. Mıknatıs tedavisi önerilmiyor.</span></li>
        <li><b>Kortizon iğnesi</b><span>Belirtileri kısa sürede azaltabilir: bir çalışmada tek iğne 6. haftada gece atelinden daha fazla rahatlama sağladı, 6. ayda ise fark kalmadı. 2024 AAOS kılavuzuna göre uzun vadeli faydası yok.</span></li>
        <li><b>Ameliyat</b><span>Bileğin avuç tarafındaki bağın gevşetilmesiyle sinir rahatlatılır. Uygun hastalarda 6 ve 12. ayda ameliyatsız tedaviden daha fazla fayda sağlar. Küçük kesili açık ameliyat ile kapalı (endoskopik) yöntem arasında hastaların bildirdiği sonuçlarda fark bulunmadı; ameliyat yalnızca lokal anesteziyle de yapılabilir. AAOS ameliyattan sonra rutin atel kullanılmamasını ve gözetimli terapinin rutin olarak verilmemesini öneriyor.</span></li>
        <li><b>Gebelikte</b><span>Gebeliğe bağlı karpal tünel sendromunda belirtiler genellikle doğumdan sonra hafifler, ancak bazı kadınlarda uzun süre devam edebilir. Gece ateli bu dönemde iyi bir seçenektir; fizyoterapi kılavuzu doğumdan sonra da izlemeyi öneriyor.</span></li>
      </ul>
      <h3 class="g-h3">Tedavi seçenekleri: kılavuzlar ne diyor?</h3>
      <p class="soft">Amerikan Ortopedi Cerrahları Akademisi'nin (AAOS, 2024) kılavuzu ile Amerikan Fizyoterapi Derneği'nin (APTA) akademilerinin hazırladığı fizyoterapi kılavuzunun (JOSPT, 2026) önerileri yan yana. Parantez içindeki harfler fizyoterapi kılavuzundaki öneri düzeyidir (A güçlü, B orta, C zayıf); bu kılavuzun ayrıntıları ikincil bir özetten alındı. AAOS çoğu yöntem için uzun vadeli sonuçlara, fizyoterapi kılavuzu ise kısa süreli yarara bakıyor; tedavi kişiye göre seçilir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Tanı</h3><dl><dt>AAOS</dt><dd>CTS-6 puanlaması rutin ultrason ya da EMG yerine kullanılabilir (güçlü); MR ve sinir germe testleri tanıda kullanılmamalı (orta).</dd><dt>Fizyoterapi (JOSPT)</dt><dd>CTS-6 (B); Phalen, Tinel ve bilek sıkıştırma testleri tek başına yeterince doğru değil (B); ince telle his testi (A). EMG ve ultrason, sonuç tedaviyi değiştirecekse.</dd></dl></div>
        <div class="kind"><h3>Atel</h3><dl><dt>Fizyoterapi (JOSPT)</dt><dd>Hafif ve orta şiddette, bileği düz tutan gece ateli (B); yetmezse gündüz de takmak ya da pozisyonu değiştirmek (C); gebelikte atel ve doğumdan sonra izlem (C).</dd><dt>AAOS</dt><dd>Ameliyattan sonra atel ya da askı kullanılmamalı (orta).</dd></dl></div>
        <div class="kind"><h3>Egzersiz ve manuel terapi</h3><dl><dt>Fizyoterapi (JOSPT)</dt><dd>Boyun ve kola manuel terapi kısa süreli yarar için (C); kas erimesi yoksa atelle birlikte germe programı (C); tendon ve sinir kaydırma için net öneri yok.</dd><dt>AAOS</dt><dd>Egzersiz, manuel terapi ve masajın uzun vadeli yararı gösterilmedi (sınırlı kanıt).</dd></dl></div>
        <div class="kind"><h3>Lazer, şok dalga ve diğer cihazlar</h3><dl><dt>Fizyoterapi (JOSPT)</dt><dd>Lazer, şok dalga, enterferansiyel akım ve yüzeysel sıcak kısa süreli yarar için (C); kortizonlu iyontoforez ve fonoforez önerilmiyor (A); mıknatıs önerilmiyor (B).</dd><dt>AAOS</dt><dd>Lazer, şok dalga ve ultrason tedavisinin uzun vadeli yararı gösterilmedi (sınırlı kanıt).</dd></dl></div>
        <div class="kind"><h3>Bantlama ve iş düzenlemesi</h3><dl><dt>Fizyoterapi (JOSPT)</dt><dd>Hafif durumlarda kinezyo bant kısa ve orta süreli rahatlama için, atelin yerine değil (C); daha az kuvvet gerektiren klavye ve fare seçenekleri (C).</dd><dt>AAOS</dt><dd>Yoğun klavye kullanımıyla ilişki yok (uzman görüşü).</dd></dl></div>
        <div class="kind"><h3>Kortizon ve PRP iğnesi</h3><dl><dt>AAOS</dt><dd>Kortizon iğnesi uzun vadeli iyileşme sağlamıyor (güçlü); PRP iğnesinin uzun vadeli yararı yok (güçlü); ağızdan kortizonun uzun vadeli yararı yok (sınırlı).</dd><dt>Not</dt><dd>Kısa vadede tek kortizon iğnesi gece atelinden daha hızlı rahatlama sağlayabilir (INSTINCTS, 2018). Fizyoterapi kılavuzu iğneleri kapsamıyor.</dd></dl></div>
        <div class="kind"><h3>Ameliyat</h3><dl><dt>AAOS</dt><dd>Küçük kesili açık ve kapalı (endoskopik) ameliyatın sonuçları farksız (güçlü); yalnızca lokal anestezi yeterli olabilir (güçlü); ameliyattan sonra rutin gözetimli terapi önerilmiyor (orta).</dd><dt>Fizyoterapi (JOSPT)</dt><dd>İlerleyen his kaybı, artan güçsüzlük ve başparmak kökünde kas erimesi hekim değerlendirmesi gerektirir.</dd></dl></div>
      </div>
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

  <section id="gunluk">
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

  <section id="sss">
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(KT_FAQ)}
    </div>
  </section>

  <section id="uyari">
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
     "Karpal tünel sendromu nedir, nasıl tanınır, kendiliğinden geçer mi, bilgisayar kullanmak neden olur mu? Gece ateli, AAOS ve fizyoterapi kılavuzlarının karşılaştırması, kısa tarihçe, evde dört egzersiz ve uyarı işaretleri.",
     "karpal-tunel-sendromu.html", NECK_CSS, KT_BODY, YT_JS,
     seo_title="Karpal Tünel Sendromu: Belirtiler, Egzersizler ve Tedavi | İhsan Eren",
     condition="Karpal tünel sendromu", about=cond("Karpal tünel sendromu"),
     faq_items=pick(KT_FAQ, 0, 1, 2, 4))

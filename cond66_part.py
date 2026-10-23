# -*- coding: utf-8 -*-
# Yeni rehber (66): Kemik erimesine bağlı omurga kırığı (osteoporotik vertebra kırığı). cond65_part.py'den sonra exec edilir. Video yok.
# Kaynaklar (22 Ekim 2026'da okundu): Brooke-Wavell 2022 BJSM uzlaşı (Loughborough deposu özeti), Gibbs 2019 Cochrane (cochrane.org özeti), Barker 2019 PROVE (HTA özeti),
# Bristol Vertebral Fractures Study birinci basamak rehberi (25 Kasım 2022), BackCare/ROS (Leyland 2021; 5 Haziran 2024), Leeds Community Healthcare (12 Mart 2026),
# ROS "Exercises for back pain after spinal fractures" (2019).

_ex2("vf_post", "wallpost", "Duvara yaslanarak dik duruş", "Sırtınızı ve başınızı duvara yaslayın, ayaklarınız duvardan bir adım önde olsun. Çenenizi hafifçe içeri alıp göğsünüzü açın, rahat nefes alarak birkaç saniye tutun.", "3–5 saniye tutun, 5 tekrar, günde en az 1 kez")
_ex2("vf_scap", "scap", "Kürek kemiklerini sıkıştırma", "Dik oturun ya da durun. Omuzlarınızı kaldırmadan kürek kemiklerinizi geriye ve hafifçe aşağıya doğru birbirine yaklaştırın. Nefes almayı sürdürün.", "3–5 saniye tutun, 5–10 tekrar, günde en az 1 kez")
_ex2("vf_hinge", "hinge", "Kalçadan eğilme", "Yere ya da alçağa uzanmanız gerektiğinde belinizi yuvarlamak yerine dizlerinizi bükün ve kalçanızdan öne eğilin; sırtınız düz kalsın. Bir şey alırken yükü bedeninize yakın tutun.", "Günlük hayatta her eğilişte")
_ex2("vf_sts", "sts", "Sandalyeden kalkıp oturma", "Sağlam bir sandalyenin önüne oturun. Sırtınızı düz tutarak öne eğilin, ayağa kalkın ve yavaşça oturun. Gerekirse ellerinizden destek alın.", "8–10 tekrar, 1–2 set")
_ex2("vf_tandem", "tandem", "Tandem duruş", "Bir tezgâhın yanında, bir ayağınızı diğerinin tam önüne koyarak durun. Gerekirse tezgâha tutunun; kolaylaştıkça tutunmayı azaltın.", "10 saniye, her ayak önde 2–3 kez")
_ex2("vf_walk", "walk", "Yürüyüş", "Düz bir yolda, rahat bir tempoyla başlayın; ağrınız azaldıkça süreyi ve tempoyu kademeli artırın. Omurga kırığı geçirdiyseniz zıplama ve koşu yerine tempolu yürüyüş düzeyinde kalın.", "Birkaç dakikayla başlayın; hedef günde 30 dakika")

VF_FAQ = [
 ("Korse takmam gerekir mi?", "Genellikle gerekmez. Kraliyet Osteoporoz Derneği’nin danışmanı, kemik erimesine bağlı omurga kırıklarının omuriliği etkilemeyen “sağlam” kırıklar olduğunu ve korse takmaya gerek olmadığını belirtiyor. Hareketsiz kalmak da gerekmez; düzenli hareket ve uygun egzersizler önerilir. Hekiminiz sizin durumunuza özel bir öneride bulunduysa ona uyun."),
 ("Ağrı ne kadar sürer?", "Kırıkların çoğu 6–12 haftada kendiliğinden iyileşir ve ağrı genellikle bu sürede azalır. İlk günlerde güçlü ağrı kesiciler gerekebilir, ağrı azaldıkça doz düşürülür. Bazı kişilerde, özellikle birden fazla kırık omurganın şeklini değiştirdiğinde, ağrı uzun süre devam edebilir; bu durumda ağrı kliniği ve fizyoterapi gibi destekler yardımcı olur."),
 ("Egzersiz güvenli mi?", "Evet; İngiltere’deki uzman uzlaşısına göre fiziksel aktivitenin ciddi zarar verdiğine dair kanıt az ve yararları genellikle risklerinden fazla. Omurga kırığı geçirenler için öneriler: darbeyi tempolu yürüyüş düzeyinde tutmak, egzersizde ve günlük hayatta belin ileri derecede öne bükülmesinden kaçınmak, düşme riski varsa önce güç ve denge çalışmalarıyla başlamak. Cochrane derlemesinde egzersizle ilgili yan etkiler nadirdi; üç çalışmada toplam dört olay, aralarında kaburga kırığı da, bildirildi."),
 ("Kaç seans fizyoterapi gerekir?", "İngiltere’de 615 kişiyle yapılan PROVE çalışmasında 7 seanslık egzersiz programı, 4. ayda fiziksel performans testlerinde tek seferlik 1 saatlik fizyoterapi danışmanlığından daha iyi sonuç verdi. 12. ayda ise yaşam kalitesi ve kas dayanıklılığında gruplar arasında fark kalmadı. İyi anlatılmış tek bir danışma seansı bile önemli; programın yoğunluğu ve süresi kişiye göre ayarlanabilir."),
 ("Yeni bir kırığı nasıl önlerim?", "Kemik güçlendirici ilaç tedavisi, uygun kişilerde yeni kırık riskini %30–50 azaltır; bu konuyu hekiminizle konuşabilirsiniz. Düşme riskinizi değerlendirmek, güç ve denge egzersizleri yapmak ve eğilip kaldırırken belinizi korumak da önemlidir."),
 ("Neden fark edilmemiş olabilir?", "Omurga kırıklarının yaklaşık üçte ikisi teşhis edilmeden kalıyor. Ağrı sıradan bir kas ağrısı sanılabilir, bazı kırıklar ise hiç ağrı yapmaz. Kırıkların yalnızca yaklaşık %20’si bir düşmeden sonra olur; çoğu öksürmek, eğilmek ya da bir şey kaldırmak gibi günlük işler sırasında oluşur."),
]

VF_SRC = [
 "Brooke-Wavell K, Skelton DA, Barker KL, et al. " + ext("https://repository.lboro.ac.uk/articles/journal_contribution/Strong_steady_and_straight_UK_consensus_statement_on_physical_activity_and_exercise_for_osteoporosis/19906744/1", "Strong, steady and straight: UK consensus statement on physical activity and exercise for osteoporosis") + ". Br J Sports Med. 2022;56(15):837–846.",
 "Gibbs JC, MacIntyre NJ, Ponzano M, et al. " + ext("https://www.cochrane.org/evidence/CD008618_exercise-improving-outcomes-after-osteoporotic-spine-fracture", "Exercise for improving outcomes after osteoporotic vertebral fracture") + ". Cochrane Database Syst Rev. 2019;(7):CD008618.",
 "Barker KL, Newman M, Stallard N, et al. " + ext("https://doi.org/10.3310/hta23440", "Exercise or manual physiotherapy compared with a single session of physiotherapy for osteoporotic vertebral fracture: three-arm PROVE RCT") + ". Health Technol Assess. 2019;23(44).",
 "Vertebral Fractures Study (University of Bristol, Keele University, University of the West of England). " + ext("https://www.bristol.ac.uk/media-library/sites/medical-school/a%20guide%20to%20diagnosis%20for%20healthcare%20professionals%20in%20primary%20care.pdf", "Osteoporotic vertebral fractures: a guide to diagnosis for healthcare professionals in primary care") + ". 25 November 2022.",
 "Leyland S (Royal Osteoporosis Society). " + ext("https://backcare.org.uk/i-have-back-or-neck-pain/library/osteoporosis-the-facts-behind-fractures/", "Osteoporosis: the facts behind spinal fractures and back pain") + ". BackCare, TalkBack 2021; updated 5 June 2024.",
 "Leeds Community Healthcare NHS Trust. " + ext("https://leedscommunityhealthcare.nhs.uk/our-services-a-z/musculoskeletal-msk/back-problems/known-and-diagnosed-back-problems/spinal-fractures", "Spinal fractures advice and exercises") + ". Updated 12 March 2026.",
 "Health Service Executive (HSE). " + ext("https://www.hse.ie/conditions/back-pain/", "Back pain") + ". Last reviewed 14 July 2026.",
 "Henschke N, Maher CG, Ostelo RWJG, et al. " + ext("https://cochranelibrary.com/cdsr/doi/10.1002/14651858.CD008686.pub2", "Red flags to screen for malignancy in patients with low-back pain") + ". Cochrane Database Syst Rev. 2013;(2):CD008686.",
 "Royal Osteoporosis Society. " + ext("https://theros.org.uk/information-and-support/osteoporosis/living-with-osteoporosis/exercise-and-physical-activity-for-osteoporosis/caring-for-your-back/exercises-for-back-pain-after-spinal-fractures/", "Exercises for back pain after spinal fractures") + ". Reviewed February 2019.",
]

VF_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Kemik erimesine bağlı omurga kırığı</h1>
    <p class="lede">Kemik erimesi olan birinde bir omur, düşme olmadan da çökebilir: öksürürken, eğilirken ya da bir şey kaldırırken. Ani sırt ağrısı, boy kısalması ya da kamburlaşma bunun işareti olabilir; bazen hiçbir belirti olmaz. Kırıkların çoğu 6–12 haftada iyileşir. Hareketsiz yatmak gerekmez: güvenli hareket ve egzersiz ağrıyı ve hareket kabiliyetini destekler, kemik tedavisi ise yeni kırıkları önlemeye yardım eder.</p>
    <p class="meta">Son güncelleme: 23 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%12</b><span>Avrupa’da omurga kırığıyla yaşadığı tahmin edilen yaşlıların oranı</span></div>
        <div class="stat"><b>3’te 2</b><span>Teşhis edilmeden kalan omurga kırıkları</span></div>
        <div class="stat"><b>%20</b><span>Bir düşmeden sonra oluşan omurga kırıklarının yaklaşık oranı; çoğu günlük işler sırasında olur</span></div>
        <div class="stat"><b>6–12 hafta</b><span>Kırıkların çoğunun kendiliğinden iyileştiği süre</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Ani başlayan sırt ağrısı; çoğu zaman sıradan bir kas ağrısı sanılır.</li>
          <li>Boyda kısalma.</li>
          <li>Sırtta giderek artan kamburlaşma.</li>
          <li>Birden fazla kırıkta uzun süren sırt ağrısı, sinir tahrişi, nefes almada ve hareket etmede güçlük.</li>
        </ul>
        <p class="soft">Kemik erimesinin kendisi, bir kemik kırılmadıkça ağrı yapmaz. Bazı omurga kırıkları ise hiç ağrı yapmadan oluşur. Kemik erimesine bağlı omurga kırıkları “sağlam” kırıklardır; omuriliği etkilemez ve felce yol açmaz.</p>
      </div>
      <div>
        <h2>Kimlerde daha sık?</h2>
        <ul class="dots">
          <li>50 yaş ve üstünde.</li>
          <li>Daha önce hafif bir darbeyle kemik kırmış olanlarda.</li>
          <li>Sık ya da uzun süre kortizon (steroid) kullananlarda.</li>
          <li>Sık düşenlerde ve ailesinde kalça kırığı olanlarda.</li>
          <li>Romatoid artrit ya da emilim bozukluğu gibi kemiği zayıflatan hastalıkları olanlarda.</li>
          <li>Beden kitle indeksi 18,5’in altında olanlarda, sigara içenlerde ve haftada 14 birimden fazla alkol alanlarda.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tanı nasıl konur?</h2>
      <p class="soft">Bir İngiltere birinci basamak rehberi, özellikle yaşlılarda ve risk etkenleri olanlarda sırt ağrısı varsa omurga kırığından şüphelenilmesini öneriyor. Tanı, sırt ve bel bölgesinin ayrı ayrı çekilen röntgenleriyle konur. Kırık bulunursa kırık riski hesaplanır, gerekirse kemik yoğunluğu ölçülür (DEXA) ve kemiği zayıflatan başka nedenler için kan tahlilleri yapılır. Uygun kişilerde kemik güçlendirici ilaç tedavisi yeni kırık riskini %30–50 azaltır.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ağrıyla başa çıkmak</h2>
      <ul class="tx">
        <li><b>Ağrı kesiciler</b><span>İlk günlerde güçlü ağrı kesiciler gerekebilir; ağrı azaldıkça doz düşürülür. Hangi ilacı kullanacağınızı hekiminiz belirler.</span></li>
        <li><b>Hareketli kalın</b><span>Hareketsiz yatmak gerekmez. Ağrınız izin verdiğince nazik hareketlerle başlayın, güveniniz arttıkça artırın; ağrı çok şiddetliyse başta hareket ve dinlenmeyi dönüşümlü yapın.</span></li>
        <li><b>İlaç dışı yöntemler</b><span>TENS cihazı, nazik masaj, gevşeme ve nefes egzersizleri ağrıyı hafifletmeye yardım edebilir.</span></li>
        <li><b>Uzun süren ağrıda</b><span>Fizyoterapi, ağrı kliniği ve ağrıyla yaşama programları destek olabilir. Omura çimento verilen işlemler (vertebroplasti, kifoplasti) bazı merkezlerde yapılıyor; ancak etkileri konusunda uzmanlar arasında görüş ayrılığı var.</span></li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Araştırmalar ne gösteriyor?</h2>
      <p class="soft">2019 tarihli Cochrane derlemesi, omurga kırığı geçirmiş 749 kişiyle yapılmış 9 çalışmayı inceledi. Egzersiz kalk ve yürü testinde süreyi ortalama 1,1 saniye kısalttı (orta düzeyde kanıt); bu fark klinik açıdan küçük. Ağrı, yaşam kalitesi, düşme ve yeni kırık üzerine etkisi ise belirsiz kaldı. İngiltere’de 615 kişiyle yapılan PROVE çalışmasında 7 seanslık egzersiz programı 4. ayda fiziksel performansı tek seferlik danışmanlığa göre daha çok artırdı, ancak 12. ayda gruplar arasında fark kalmadı.</p>
      <p class="soft">Kanıt sınırlı olsa da İngiltere’deki uzman uzlaşısı egzersizi öneriyor: ağrıyı azaltabilir, hareket kabiliyetini ve yaşam kalitesini artırabilir; güç ve denge çalışmaları düşmeleri önlemeye yardım eder, sırtı dikleştiren egzersizler duruşu iyileştirir.</p>
      <div class="callout">
        <p>Omurga kırığı geçirdiyseniz: darbeyi tempolu yürüyüş düzeyinde tutun; yük kaldırırken ve günlük hayatta belinizi ileri derecede öne bükmekten kaçının; eğilmeniz gerekiyorsa kalçanızdan eğilin.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Omurga kırığından sonra altı egzersiz</h2>
      <p class="soft">Kraliyet Osteoporoz Derneği, sırt ağrısı egzersizlerinde her pozisyonu 3–5 saniye tutup nefes almayı sürdürmeyi ve egzersizleri günde en az bir kez yapmayı öneriyor. Ağrınızın izin verdiği kadar, yavaş ve doğru teknikle çalışın; diğer tekrar sayıları genel önerilerdir. Birden fazla kırığınız varsa önce bir fizyoterapistle görüşün.</p>
      {ex_grid(["vf_post", "vf_scap", "vf_hinge", "vf_sts", "vf_tandem", "vf_walk"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(VF_FAQ)}
      <p class="soft" style="margin-top:18px">Kemik erimesinde güvenli egzersiz için <a href="kemik-erimesi.html">kemik erimesi</a>, sırttaki kamburluk için <a href="kambur-durus.html">kambur duruş</a>, düşme riskini azaltmak için <a href="dusme-onleme.html">düşmeleri önleme</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Kemik erimesi ya da risk etkenleriniz varken yeni başlayan ani sırt ağrısı: yeni bir kırığı değerlendirmek için</li>
        <li>Boyunuzun kısaldığını ya da sırtınızın kamburlaştığını fark ettiyseniz</li>
        <li>Genital bölge ya da makat çevresinde uyuşma veya karıncalanma, idrar ya da dışkıyı kontrol etmede sorun, bacaklarda yeni güçsüzlük: hemen acile başvurun (kemik erimesine bağlı kırıklar omuriliği etkilemediği için bu belirtiler başka bir nedeni düşündürür)</li>
        <li>38 °C ve üzeri ateş, titreme ya da açıklanamayan kilo kaybıyla birlikte sırt ağrısı; daha önce kanser geçirdiyseniz yeni başlayan sırt ağrısı (omurgada kanser yayılımını düşündüren işaretler arasında en anlamlısı budur)</li>
      </ul>
      {CTA_CARD("Omurga kırığı sonrası rehabilitasyonunuz", "kemik erimesine bağlı omurga kırığı sonrası rehabilitasyon")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(VF_SRC)}
    </div>
  </section>
</main>'''

page("omurga-kirigi.html", "Kemik Erimesine Bağlı Omurga Kırığı",
     "Kemik erimesinde omurga kırığı: belirtiler, kimlerde sık, tanı, ağrıyla başa çıkma, güvenli hareket ve altı egzersiz; korse gerekir mi, ağrı ne kadar sürer.",
     "omurga-kirigi.html", NECK_CSS, VF_BODY, "",
     seo_title="Kemik Erimesine Bağlı Omurga Kırığı: Ağrı, Güvenli Hareket ve Egzersizler | İhsan Eren",
     condition="Osteoporotik omurga kırığı", faq_items=VF_FAQ)

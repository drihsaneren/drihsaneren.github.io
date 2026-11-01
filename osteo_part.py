# -*- coding: utf-8 -*-
# Kemik erimesi (osteoporoz) sayfası. elbow_part.py'den sonra exec edilir.

# Kalçadan eğilme (yandan): sırt düz, gövde kalçadan öne eğilir, dizler hafif bükük.
SV["hinge"] = fig(GRD +
    f'<path class="fig" d="M56 74 L58 94 L54 112 M56 74 L60 94 L58 112">{anim_d("M56 74 L58 94 L54 112 M56 74 L60 94 L58 112;M56 74 L63 93 L54 112 M56 74 L65 93 L58 112;M56 74 L58 94 L54 112 M56 74 L60 94 L58 112")}</path>'
    f'<g>{anim_t("0 56 74;55 56 74;0 56 74", typ="rotate")}'
    '<path class="fig hl" d="M56 74 L56 34"/><circle class="hd" cx="57" cy="24" r="7"/><path d="M63 22 L68 25 L63 27 Z" fill="#2A6F6B"/>'
    '<path d="M50 30 L50 76" stroke="#8FA8A2" stroke-width="3" stroke-linecap="round" stroke-dasharray="4 3"/>'
    '<path class="fig" d="M56 40 L62 56 L64 70"/></g>',
    "Kalçadan eğilme")

# Yüzüstü göğüs kaldırma (yandan)
SV["pchest"] = fig(GRD +
    '<path class="fig" d="M62 105 L112 107"/>'
    f'<g>{anim_t("0 62 105;14 62 105;0 62 105", typ="rotate")}'
    '<path class="fig hl" d="M62 105 L28 104"/><circle class="hd" cx="18" cy="101" r="7"/>'
    '<path class="fig" d="M30 104 L52 108"/></g>',
    "Yüzüstü göğüs kaldırma")

SV["sts6"] = SV["sts"]
SV["heel3"] = SV["heel"]
SV["sls2"] = SV["sls"]
SV["scap4"] = SV["scap"]

EXT.update({
 "sts6": ("Sandalyeden kalkıp oturma", "Sağlam, kollu bir sandalyede ayaklarınızı biraz geriye alın. Sırtınızı düz tutarak kalçanızdan öne eğilin ve kalkın, sonra kontrollü şekilde oturun. Kolaylaştıkça kollarınızı göğsünüzde çaprazlayın ya da elinize ağırlık alın.", "8–12 tekrar, 2–3 set"),
 "heel3": ("Topuk yükseltme", "Tezgâha tutunarak dik durun. İki topuğunuzu birlikte kaldırıp parmak uçlarınızda yükselin, 2 saniye bekleyip yavaşça inin. Uygun olanlarda topukları hafifçe yere bırakarak yapılan küçük darbeler kemiğe ek uyarı sağlar. Omurga kırığı öykünüz varsa darbeli kısmı fizyoterapistinize danışmadan yapmayın.", "10–15 tekrar"),
 "hinge": ("Kalçadan eğilme", "Ayaklarınız kalça genişliğinde açık, dizleriniz hafif bükülü olsun. Sırtınızı düz tutarak gövdenizi kalçanızdan öne doğru eğin, sonra kalçanızı sıkarak doğrulun. Yerden bir şey alırken ya da yük kaldırırken belinizi yuvarlamak yerine bu hareketi kullanın.", "10 tekrar"),
 "pchest": ("Yüzüstü göğüs kaldırma", "Yüzüstü yatın, kollarınız yanınızda olsun. Bakışınızı yere yöneltip göğsünüzü ve başınızı yerden birkaç santim kaldırın, 3 saniye bekleyip yavaşça inin. Sırt kaslarını güçlendirir ve dik duruşu destekler.", "8–10 tekrar"),
 "sls2": EXT["sls"],
 "scap4": EXT["scap"],
})

KEMIK_FAQ = [
 ("Kemik erimesinde egzersiz yapmak güvenli mi?", "Evet; egzersiz kemik sağlığının en önemli parçalarından biridir. İngiltere Ulusal Osteoporoz Derneği'nin (bugün Royal Osteoporosis Society) uzman görüş bildirisi kas güçlendirme, uygun kişilerde darbe egzersizleri ve denge çalışmalarını öneriyor. Egzersizin tipi ve yoğunluğunun kırık öykünüze ve genel durumunuza göre bir fizyoterapistle ayarlanması önerilir."),
 ("T-skorum −2 çıktı, bu ne demek?", "Dünya Sağlık Örgütü'nün tanımına göre −1 ile −2,5 arasındaki T-skoru osteopeni, yani düşük kemik kütlesi anlamına gelir; DEXA'ya göre kemik erimesi (osteoporoz) tanısı için T-skorunun −2,5 ya da daha düşük olması gerekir. Ancak kırılganlık kırığı geçirenlerin çoğunun T-skoru −2,5'in altında değildir. Bu yüzden kırık riski yalnız T-skoruyla değil, FRAX gibi kemik yoğunluğunu diğer risk etkenleriyle birlikte değerlendiren hesaplamalarla da tahmin edilir; tedavi gerekip gerekmediğine hekiminiz karar verir. Kemik yoğunluğu düşük (osteopeni ya da osteoporoz) menopoz sonrası kadınlarla yapılan LIFTMOR çalışmasında, gözetimli kuvvet ve darbe egzersizi kemik yoğunluğunu artırdı."),
 ("Hangi hareketlerden kaçınmalıyım?", "Omurgayı uzun süre, en uç noktaya kadar ya da yük altında öne bükmeyi gerektiren hareketlerin değiştirilmesi ya da yerine başka hareketler bulunması öneriliyor. Örneğin mekik ya da dizler düzken yere doğru uzanma gibi hareketler yerine başka karın ve sırt egzersizleri seçilebilir. Yerden bir şey alırken de belinizi yuvarlamak yerine dizlerinizi bükün ve kalçanızdan eğilin."),
 ("Yürüyüş kemiklerim için yeterli mi?", "Yürüyüş genel sağlık için çok değerlidir ama kemikler için tek başına genellikle yeterli değildir. Haftada 2–3 gün kas güçlendirme egzersizleri önerilir; uygun olanlarda çoğu gün yaklaşık 50 orta şiddetli darbe (hafif koşu adımları, küçük sıçramalar) eklenebilir. 65 yaş üstündekilerin ve denge sorunu olanların denge egzersizlerini de programa katmaları önerilir. Omurga kırığı ya da birden fazla kırık öyküsü olanlarda ise genel kural olarak orta şiddetli darbeler yerine daha düşük darbeli etkinlikler önerilir."),
 ("Omurgamda kırık oldu, egzersiz yapabilir miyim?", "Evet, ama program size göre uyarlanmalıdır. Ağrılı omurga kırığı olanların kaygıyı azaltacak bilgiyi erkenden almaları ve fizyoterapiste yönlendirilmelerinin düşünülmesi öneriliyor. Başlangıçta darbe egzersizleri yerine güçlendirme, denge ve güvenli hareket öğretimi öne çıkar. İngiltere’nin 2022 osteoporoz kılavuzuna (NOGG) göre kırıktan sonraki ilk dönemde yeni kırık riski özellikle yüksektir; ilaç tedavisinin sizin için uygun olup olmadığını hekiminize sorun."),
 ("Ağır ağırlık kaldırmak kemikleri güçlendirir mi?", "Bazı kişilerde, uzman gözetiminde güçlendirebilir. Kemik yoğunluğu düşük, menopoz sonrası 101 kadının katıldığı bir çalışmada haftada iki kez 30 dakikalık yüksek yoğunluklu kuvvet ve darbe egzersizi, 8 ayda bel omurgası kemik yoğunluğunu düşük yoğunluklu ev egzersizi yapan gruba göre belirgin şekilde artırdı; kırıklar üzerindeki etkisi bu çalışmada ölçülmedi. Ancak bu tür programlar mutlaka kişiye göre planlanmalı ve gözetim altında, kademeli olarak uygulanmalıdır."),
]

KEMIK_SRC = [
 "Giangregorio LM, et al. " + ext("https://link.springer.com/article/10.1007/s00198-013-2523-2", "Too Fit To Fracture: exercise recommendations for individuals with osteoporosis or osteoporotic vertebral fracture") + ". Osteoporos Int. 2014;25. Tam metin: " + ext("https://minerva-access.unimelb.edu.au/server/api/core/bitstreams/724074d1-ca56-5db4-8af6-6a0fc321aa82/content", "Melbourne Üniversitesi") + ".",
 "International Osteoporosis Foundation. " + ext("https://www.osteoporosis.foundation/health-professionals/diagnosis", "Diagnosis") + ".",
 "Albright F, Smith PH, Richardson AM. Postmenopausal osteoporosis: its clinical features. JAMA. 1941;116:2465. Atıf: " + ext("https://link.springer.com/doi/10.1007/s11999-011-1832-z", "Clin Orthop Relat Res, 2011") + ".",
 "International Osteoporosis Foundation. " + ext("https://www.osteoporosis.foundation/facts-statistics/epidemiology-of-osteoporosis-and-fragility-fractures", "Epidemiology of osteoporosis and fragility fractures") + ".",
 "National Osteoporosis Society (bugün Royal Osteoporosis Society). " + ext("https://www.bgs.org.uk/strong-steady-straight-nos-exercise-and-osteoporosis-consensus-statement", "Strong, Steady and Straight: an expert consensus statement on physical activity and exercise for osteoporosis") + ". 2018. Kısa rehber: " + ext("https://www.endocrinology.org/media/3590/final-quick-guide_strong-steady-straight_dec18.pdf", "Quick guide, Aralık 2018") + ".",
 "Watson SL, Weeks BK, Weis LJ, et al. " + ext("https://academic.oup.com/jbmr/article-abstract/33/2/211/7605709", "High-intensity resistance and impact training improves bone mineral density and physical function in postmenopausal women with osteopenia and osteoporosis: the LIFTMOR randomized controlled trial") + ". J Bone Miner Res. 2018;33(2):211-220.",
 "Gregson CL, Armstrong DJ, Bowden J, et al. " + ext("https://eprints.whiterose.ac.uk/185838", "UK clinical guideline for the prevention and treatment of osteoporosis") + ". Arch Osteoporos. 2022;17(1):58.",
 "Massé O, et al. Calcium, vitamin D, or combined supplementation to prevent fractures and falls: systematic review and meta-analysis. BMJ. 2026;393:e088050. Özet: " + ext("https://bmjgroup.com/calcium-and-vitamin-d-supplements-offer-little-to-no-meaningful-benefit-on-fracture-and-fall-prevention/", "BMJ Group, 20 Mayıs 2026") + ".",
]

KEMIK_TL = [
 ("1941", "Fuller Albright ve arkadaşları, menopoz sonrası kemik erimesinin klinik özelliklerini anlatan makalelerini JAMA'da yayımladı."),
 ("2014", "Avustralya, Kanada, Finlandiya ve ABD'den araştırmacılar ve klinisyenler, Osteoporosis Canada iş birliğiyle Too Fit To Fracture egzersiz önerilerini yayımladı (Osteoporosis International): direnç ve denge egzersizlerini içeren çok bileşenli bir program güçlü şekilde önerildi; yalnızca aerobik egzersiz yapılıp direnç ve denge çalışmalarının ihmal edilmemesi vurgulandı."),
 ("2018", "LIFTMOR çalışması (JBMR): kemik yoğunluğu düşük, menopoz sonrası 101 kadında uzman gözetiminde haftada iki kez 30 dakikalık yüksek yoğunluklu kuvvet ve darbe egzersizi, 8 ayda bel omurgası kemik yoğunluğunu düşük yoğunluklu ev egzersizi yapan gruba göre belirgin şekilde artırdı."),
 ("2018", "İngiltere Ulusal Osteoporoz Derneği'nin (bugün Royal Osteoporosis Society) \"Güçlü, Dengeli ve Dik\" uzman görüş bildirisi yayımlandı: haftada 2–3 gün kas güçlendirme, uygun olanlarda çoğu gün yaklaşık 50 darbe, denge egzersizleri ve omurgayı koruyan hareket."),
 ("2022", "İngiltere'nin osteoporoz kılavuzu (NOGG) güncellendi: kırıktan sonraki ilk dönemde yeni kırık riskinin özellikle yüksek olduğu ve gerektiğinde zamanında sevk ya da ilaç tedavisinin önemi vurgulandı."),
 ("2026", "69 çalışmayı kapsayan bir derleme (BMJ): osteoporoz ilacı kullanmayan yetişkinlerde kalsiyum ve D vitamini takviyeleri kırıkları ve düşmeleri klinik açıdan anlamlı ölçüde azaltmadı; sonucun belirli kemik hastalıkları olanlar ve osteoporoz ilacı kullananlar için geçerli olmayabileceği belirtildi."),
]

KEMIK_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Kemik erimesi (osteoporoz)</h1>
    <p class="lede">Kemiklerin yoğunluğunun ve iç yapısının zayıflayarak kolay kırılır hale gelmesidir. Çoğu zaman bir kırık olana kadar belirti vermez. İyi haber: doğru egzersiz, düşmeleri önleme ve gerektiğinde ilaç tedavisiyle kırık riski azaltılabilir.</p>
    <p class="meta">Son güncelleme: 1 Kasım 2026</p>
  </div>
</header>
<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>3'te 1</b><span>50 yaş üstündeki kadınlarda hayat boyu kemik erimesine bağlı kırık</span></div>
        <div class="stat"><b>5'te 1</b><span>50 yaş üstündeki erkeklerde hayat boyu kemik erimesine bağlı kırık</span></div>
        <div class="stat"><b>37 milyon</b><span>Dünyada 55 yaş üstünde yılda görülen kırılganlık kırığı sayısının tahmini üst sınırı; dakikada 70</span></div>
        <div class="stat"><b>%21</b><span>50 yaş üstündeki kadınlarda kemik erimesi sıklığı; erkeklerde %6</span></div>
      </div>
      {g_toc([("nedir", "Nedir?"), ("tani", "Tanı ve T-skoru"), ("tarihce", "Geçmişten bugüne"), ("oneriler", "Egzersiz önerileri"), ("egzersizler", "Egzersizler"), ("gunluk", "Günlük hayatta"), ("videolar", "Videolar"), ("sss", "Sık sorulan sorular"), ("uyari", "Uyarı işaretleri")])}
    </div>
  </section>
  <section id="nedir">
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Kemik, sürekli yıkılıp yeniden yapılan canlı bir dokudur. Yaşla ve özellikle kadınlarda menopozdan sonra yıkım, yapımdan daha hızlı olur; kemik yoğunluğu azalır, iç yapısı incelir. Sonuçta basit bir düşme ya da öne eğilip yük kaldırma gibi zorlamalar kırığa yol açabilir. En sık omurga, kalça ve el bileği kırılır.</p>
        <p class="soft">Tanı kemik yoğunluğu ölçümüyle (DEXA) konur (bkz. <a href="#tani">Tanı ve T-skoru</a>). Kimin ne zaman ölçüm yaptırması gerektiğine risk etkenlerine göre hekim karar verir.</p>
      </div>
      <div>
        <h2>Risk etkenleri</h2>
        <ul class="dots">
          <li>İleri yaş, kadın olmak ve erken menopoz</li>
          <li>Daha önce basit bir düşmeyle kırık geçirmiş olmak, ailede kalça kırığı</li>
          <li>Düşük vücut ağırlığı, hareketsizlik</li>
          <li>Sigara ve fazla alkol</li>
          <li>Uzun süreli kortizon kullanımı, romatoid artrit gibi bazı hastalıklar</li>
        </ul>
        <p class="soft">Boyda belirgin kısalma ya da giderek artan kamburluk, fark edilmemiş omurga kırıklarının işareti olabilir.</p>
      </div>
    </div>
  </section>
  <section id="tani">
    <div class="wrap">
      <h2>Tanı: kemik yoğunluğu ölçümü ve T-skoru</h2>
      <p class="soft">Kemik yoğunluğu en sık DEXA adı verilen, kısa süren bir ölçümle değerlendirilir; genellikle uyluk kemiğinin üst kısmı ve bel omurgası ölçülür. Sonuç, genç yetişkinlerin ortalamasıyla karşılaştırılır ve T-skoru olarak verilir. Uluslararası Osteoporoz Vakfı'nın aktardığı Dünya Sağlık Örgütü tanımına göre uyluk kemiği boynunda ölçülen T-skoru şöyle yorumlanır:</p>
      <div class="kinds">
        <div class="kind"><h3>Normal</h3><p>T-skoru −1 ve üzeri.</p></div>
        <div class="kind"><h3>Osteopeni (düşük kemik kütlesi)</h3><p>T-skoru −1 ile −2,5 arasında.</p></div>
        <div class="kind"><h3>Osteoporoz</h3><p>T-skoru −2,5 ya da daha düşük.</p></div>
        <div class="kind"><h3>Ağır osteoporoz</h3><p>T-skoru −2,5 ya da daha düşük ve en az bir kırılganlık kırığı.</p></div>
      </div>
      <p class="soft">DEXA kemiğin miktarını ölçer, kalitesini göstermez. Kırılganlık kırığı geçirenlerin çoğunun T-skoru −2,5'in altında değildir; yani kırıkların çoğu osteopeni düzeyindeki kişilerde görülür. Bu yüzden kırık riski, FRAX gibi kemik yoğunluğunu yaş, önceki kırıklar ve diğer risk etkenleriyle birlikte değerlendiren hesaplamalarla da tahmin edilir. Farklı cihazların sonuçları birbirinden ayrılabildiği için takip ölçümlerinin aynı cihazla yapılması tercih edilir. Sonucun yorumunu hekiminiz yapar.</p>
    </div>
  </section>
  <section id="tarihce">
    <div class="wrap">
      <p class="eyebrow">Geçmişten bugüne</p>
      <h2>Menopozdan egzersiz önerilerine</h2>
      <p class="soft">Menopoz sonrası kemik erimesi 1940'larda tarif edildi. Son yıllarda ise egzersizin kemik sağlığındaki yeri netleşti; öneriler yalnızca yürüyüşten kas güçlendirme, denge ve omurgayı koruyan harekete doğru genişledi.</p>
      {g_tl(KEMIK_TL)}
    </div>
  </section>
  <section id="oneriler">
    <div class="wrap">
      <h2>Güçlü, dengeli ve dik: egzersiz önerileri</h2>
      <p class="soft">İngiltere Ulusal Osteoporoz Derneği'nin (bugünkü adıyla Royal Osteoporosis Society, ROS) uzman görüş bildirisi egzersizi üç hedef etrafında topluyor: kemiği güçlendirmek, düşmeleri önlemek ve omurgayı korumak.</p>
      <ul class="tx">
        <li><b>Kas güçlendirme</b><span>Haftada 2–3 gün; zamanla her hareket için 8–12 tekrarlık 3 sete kadar çıkılır. Sırt kaslarını güçlendiren hareketlerin de programda yer alması önerilir.</span></li>
        <li><b>Darbe egzersizleri</b><span>Uygun olanlarda çoğu gün yaklaşık 50 orta şiddetli darbe, örneğin hafif koşu adımları ya da küçük sıçramalar önerilir. Omurga kırığı ya da birden fazla kırık öyküsü olanlarda genel kural olarak orta şiddetli darbeler yerine daha düşük darbeli etkinlikler önerilir; kırılgan ve hareketi kısıtlı kişilerde yürüyüş gibi düşük darbeli etkinlik günde 20 dakikaya kadar.</span></li>
        <li><b>Denge</b><span>65 yaş üstündekiler ve denge sorunu olanlar için denge ve güçlendirme egzersizleri önerilir. <a href="dusme-onleme.html">Düşmeleri önleme rehberine göz atın →</a></span></li>
        <li><b>Omurgayı korumak</b><span>Omurgayı uzun süre, en uç noktaya kadar ya da yük altında öne bükmeyi gerektiren hareketlerin değiştirilmesi önerilir. Yük kaldırırken kalçadan eğilmeyi (menteşe hareketi) öğrenmek önemlidir.</span></li>
        <li><b>Gözetimli yoğun programlar</b><span>Menopoz sonrası kemik yoğunluğu düşük kadınlarda uzman gözetiminde yapılan yüksek yoğunluklu kuvvet ve darbe egzersizi, 8 ayda omurga kemik yoğunluğunu düşük yoğunluklu ev egzersizi yapan gruba göre belirgin şekilde artırdı. Bu tür programların kişiye göre planlanıp gözetim altında uygulanması gerekir.</span></li>
      </ul>
      <div class="callout">
        <p>İlaç tedavisi, kalsiyum ve D vitamini ihtiyacı kişiye göre değişir; bunlara hekiminiz karar verir. 2026'da The BMJ'de yayımlanan ve 69 çalışmayı kapsayan bir derlemede, osteoporoz ilacı kullanmayan yetişkinlerde kalsiyum ve D vitamini takviyeleri kırıkları ve düşmeleri klinik açıdan anlamlı ölçüde azaltmadı; araştırmacılar sonucun belirli kemik hastalıkları olanlar ve osteoporoz ilacı kullananlar için geçerli olmayabileceğini belirtiyor. Size önerilen bir takviyeyi kendi kendinize bırakmayın; hangisinin uygun olduğunu hekiminize sorun. Sigarayı bırakmak ve alkolü sınırlamak da kemikleri korumaya yardımcı olur.</p>
      </div>
      <h3 class="g-h3">Egzersiz önerileri: iki kaynak yan yana</h3>
      <p class="soft">İngiltere Ulusal Osteoporoz Derneği'nin (bugünkü adıyla Royal Osteoporosis Society, ROS) uzman görüş bildirisi (2018) ile Osteoporosis Canada iş birliğiyle hazırlanan Too Fit To Fracture önerileri (2014) yan yana. İkisi de uzman görüşüne ve mevcut çalışmalara dayanıyor; program kişiye, kırık öyküsüne ve genel duruma göre ayarlanır.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Kas güçlendirme</h3><dl><dt>ROS</dt><dd>Haftada 2–3 gün; zamanla her hareket için 8–12 tekrarlık 3 sete kadar çıkılır; sırt kaslarını güçlendiren hareketler de programda yer alır.</dd><dt>Too Fit To Fracture</dt><dd>Tüm büyük kas gruplarına en az haftada iki kez kademeli direnç egzersizi; her kas grubu için en az bir hareketle 2 set, uygunsa 8–12 tekrar. Hareketsiz olanlar daha düşük düzeyden başlayabilir.</dd></dl></div>
        <div class="kind"><h3>Denge</h3><dl><dt>ROS</dt><dd>65 yaş üstündekiler ve denge sorunu olanlar için denge ve güçlendirme egzersizleri.</dd><dt>Too Fit To Fracture</dt><dd>Her gün denge çalışması; haftada yaklaşık 2 saat (günde 15–20 dakika).</dd></dl></div>
        <div class="kind"><h3>Darbe ve aerobik egzersiz</h3><dl><dt>ROS</dt><dd>Uygun olanlarda çoğu gün yaklaşık 50 orta şiddetli darbe; omurga kırığı ya da birden fazla kırık öyküsü olanlarda genel kural olarak daha düşük darbeli etkinlikler.</dd><dt>Too Fit To Fracture</dt><dd>Haftada 150–300 dakika orta ya da 75–150 dakika yüksek yoğunluklu aerobik etkinlik hedeflenebilir, ama direnç ve denge egzersizlerinin yerine değil; omurga kırığı olanlarda daha kısa ya da daha düşük yoğunluklu etkinlikler daha uygun olabilir.</dd></dl></div>
        <div class="kind"><h3>Omurgayı korumak</h3><dl><dt>ROS</dt><dd>Omurgayı uzun süre, en uç noktaya kadar ya da yük altında öne bükmeyi gerektiren hareketler değiştirilir.</dd><dt>Too Fit To Fracture</dt><dd>Hareketler arasındaki geçişlerde dönme ve öne eğilmeye dikkat; omurga kırığı riski yüksek olanlarda öne eğilme ve dönme gerektiren direnç makinelerinden, doğru kullanılabileceği kesin değilse, kaçınılır. Duruş kaslarını (sırt kaslarının dayanıklılığını) güçlendiren egzersizler ve duruş eğitimi önerilir.</dd></dl></div>
        <div class="kind"><h3>Fizyoterapist</h3><dl><dt>ROS</dt><dd>Ağrılı kırığı ya da hareket sorunu olanlarda fizyoterapiste yönlendirme düşünülmeli.</dd><dt>Too Fit To Fracture</dt><dd>Omurga kırığı olanlarda güvenli ve uygun egzersiz için fizyoterapiste danışılması öneriliyor.</dd></dl></div>
      </div>
    </div>
  </section>
  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Kemikler ve denge için altı egzersiz</h2>
      <p class="soft">Bu hareketler güçlendirme, denge ve güvenli hareketi birlikte çalıştırır. Omurga kırığı öykünüz varsa ya da hareketler ağrı yapıyorsa, programı bir fizyoterapistle birlikte planlayın. Ayakta yapılan hareketlerde sağlam bir yere tutunun.</p>
      {ex_grid(["sts6", "heel3", "hinge", "pchest", "sls2", "scap4"])}
    </div>
  </section>
  <section id="gunluk">
    <div class="wrap two">
      <div>
        <h2>Günlük hayatta omurganız için</h2>
        <p class="soft">Güvenli hareket etmek, hareketten kaçınmak değil; hareketi doğru biçimde yapmaktır.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Yerden bir şey alırken belinizi yuvarlamayın; dizlerinizi bükün ve kalçanızdan eğilin.</li>
        <li>Yükü vücudunuza yakın tutun, kaldırırken gövdenizi döndürmeyin.</li>
        <li>Çorap giyerken ya da ayakkabı bağlarken oturun, ayağınızı bir tabureye koyun.</li>
        <li>Öksürürken ya da hapşırırken bir elinizle bir yere destek alın, dik kalın.</li>
        <li>Evdeki düşme risklerini azaltın; kaygan halıları kaldırın, geceleri yolunuzu aydınlatın.</li>
      </ul>
    </div>
  </section>
  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Kemik erimesi için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("f4kTFDaN_Rw", "Kemik erimesi egzersizleri videosunu oynat", "3 Things You Should NEVER Do If You Have Osteoporosis. PLUS Exercises You Should Do.")}
          <h3>Kemik erimesinde yapılmaması gereken üç şey</h3>
          <p>Kaçınılması gereken hareketler ve yapılması önerilen egzersizler.</p>
        </div>
        <div class="vid">
          {vbox("f3G_-S_2HUk", "Kaçınılacak egzersizler videosunu oynat", "10 Exercises to Never Do With Osteoporosis")}
          <h3>Kemik erimesinde kaçınılacak on egzersiz</h3>
          <p>Omurgayı zorlayabilecek hareketler ve güvenli alternatifleri.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir. Kanal hakkında: <a href="https://www.startribune.com/meet-the-minnesota-physical-therapists-who-have-become-youtube-superstars/508806552" target="_blank" rel="noopener">Star Tribune, 19 Nisan 2019</a>.</p>
    </div>
  </section>
  <section id="sss">
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(KEMIK_FAQ)}
    </div>
  </section>
  <section id="uyari">
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Aşağıdaki durumlarda belirtilen süre içinde başvurun.</p>
      <p class="soft"><strong>Hemen 112'yi arayın ya da acil servise gidin:</strong></p>
      <ul class="dots redflags">
        <li>Sırt ağrısıyla birlikte bacaklarda uyuşma, güç kaybı ya da idrar ve dışkı kontrolünde bozulma</li>
        <li>Düşme sonrası kalça ağrısı ve bacağa yük verememe ya da kendi başına kalkamama (kalça kırığı olabilir)</li>
        <li>Düşerken başını çarpma, özellikle kan sulandırıcı kullanıyorsanız</li>
      </ul>
      <p class="soft"><strong>Aynı gün:</strong></p>
      <ul class="dots redflags">
        <li>Düşme sonrası el bileğinde şekil bozukluğu ya da belirgin şişlik (kırık olabilir)</li>
        <li>Ateşle ya da kanser öyküsüyle birlikte yeni başlayan sırt ağrısı</li>
      </ul>
      <p class="soft"><strong>Birkaç gün içinde bir hekime:</strong></p>
      <ul class="dots redflags">
        <li>Öne eğilme, yük kaldırma, öksürme ya da küçük bir düşmeden sonra aniden başlayan şiddetli sırt ağrısı (omurga kırığı olabilir)</li>
        <li>Boyda belirgin kısalma ya da hızla artan kamburluk</li>
        <li>Dinlenmekle geçmeyen gece ağrısı ya da nedensiz kilo kaybı</li>
      </ul>
      {CTA_CARD("Kemik sağlığınız ve egzersiz programınız", "kemik erimesi")}
    </div>
  </section>
  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(KEMIK_SRC)}
    </div>
  </section>
</main>'''

page("kemik-erimesi.html", "Kemik Erimesi (Osteoporoz)",
     "Kemik erimesi (osteoporoz) nedir, T-skoru ne anlama gelir, egzersiz güvenli mi, hangi hareketlerden kaçınmalı? İki egzersiz önerisinin karşılaştırması, kısa tarihçe, evde altı egzersiz, günlük hayatta omurgayı koruma ve uyarı işaretleri.",
     "kemik-erimesi.html", NECK_CSS, KEMIK_BODY, YT_JS,
     seo_title="Kemik Erimesi (Osteoporoz): Egzersizler ve Güvenli Hareket | İhsan Eren",
     condition="Kemik erimesi (osteoporoz)", about=cond("Kemik erimesi (osteoporoz)"),
     faq_items=pick(KEMIK_FAQ, 0, 1, 2, 3))

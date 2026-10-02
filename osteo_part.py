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
 "heel3": ("Topuk yükseltme", "Tezgâha tutunarak dik durun. İki topuğunuzu birlikte kaldırıp parmak uçlarınızda yükselin, 2 saniye bekleyip yavaşça inin. Uygun olanlarda topukları hafifçe yere bırakarak yapılan küçük darbeler kemiğe ek uyarı sağlar.", "10–15 tekrar"),
 "hinge": ("Kalçadan eğilme", "Ayaklarınız kalça genişliğinde açık, dizleriniz hafif bükülü olsun. Sırtınızı düz tutarak gövdenizi kalçanızdan öne doğru eğin, sonra kalçanızı sıkarak doğrulun. Yerden bir şey alırken ya da yük kaldırırken belinizi yuvarlamak yerine bu hareketi kullanın.", "10 tekrar"),
 "pchest": ("Yüzüstü göğüs kaldırma", "Yüzüstü yatın, kollarınız yanınızda olsun. Bakışınızı yere yöneltip göğsünüzü ve başınızı yerden birkaç santim kaldırın, 3 saniye bekleyip yavaşça inin. Sırt kaslarını güçlendirir ve dik duruşu destekler.", "8–10 tekrar"),
 "sls2": EXT["sls"],
 "scap4": EXT["scap"],
})

KEMIK_FAQ = [
 ("Kemik erimesinde egzersiz yapmak güvenli mi?", "Evet; egzersiz kemik sağlığının en önemli parçalarından biridir. İngiltere Osteoporoz Derneği'nin uzman görüş bildirisi kas güçlendirme, uygun kişilerde darbe egzersizleri ve denge çalışmalarını öneriyor. Egzersizin tipi ve yoğunluğu kırık öykünüze ve genel durumunuza göre bir fizyoterapist tarafından ayarlanmalıdır."),
 ("Hangi hareketlerden kaçınmalıyım?", "Omurgayı uzun süre, en uç noktaya kadar ya da yük altında öne bükmeyi gerektiren hareketlerin değiştirilmesi ya da yerine başka hareketler bulunması öneriliyor. Örneğin mekik çekmek, dizler düzken yere doğru eğilmek ya da yükü belinizi yuvarlayarak kaldırmak yerine kalçanızdan eğilip dizlerinizi bükmek daha güvenlidir."),
 ("Yürüyüş kemiklerim için yeterli mi?", "Yürüyüş genel sağlık için çok değerlidir ama kemikler için tek başına genellikle yeterli değildir. Haftada 2–3 gün kas güçlendirme egzersizleri önerilir; uygun olanlarda çoğu gün yaklaşık 50 orta şiddetli darbe (hafif koşu adımları, küçük sıçramalar) eklenebilir. 65 yaş üstündekiler ve denge sorunu olanlar denge egzersizlerini de programa katmalıdır."),
 ("Omurgamda kırık oldu, egzersiz yapabilir miyim?", "Evet, ama program size göre uyarlanmalıdır. Ağrılı omurga kırığı olanların kaygıyı azaltacak bilgiyi erkenden almaları ve fizyoterapiste yönlendirilmeleri öneriliyor. Başlangıçta darbe egzersizleri yerine güçlendirme, denge ve güvenli hareket öğretimi öne çıkar."),
 ("Ağır ağırlık kaldırmak kemikleri güçlendirir mi?", "Uzman gözetiminde yapıldığında evet. Kemik yoğunluğu düşük, menopoz sonrası 101 kadının katıldığı bir çalışmada haftada iki kez 30 dakikalık yüksek yoğunluklu kuvvet ve darbe egzersizi, 8 ayda bel omurgası kemik yoğunluğunu kontrol grubuna göre belirgin şekilde artırdı. Ancak bu tür programlar mutlaka kişiye göre planlanmalı ve gözetim altında, kademeli olarak uygulanmalıdır."),
]

KEMIK_SRC = [
 "Giangregorio LM, et al. " + ext("https://link.springer.com/article/10.1007/s00198-013-2523-2", "Too Fit To Fracture: exercise recommendations for individuals with osteoporosis or osteoporotic vertebral fracture") + ". Osteoporos Int. 2014;25.",
 "International Osteoporosis Foundation. " + ext("https://www.osteoporosis.foundation/facts-statistics/epidemiology-of-osteoporosis-and-fragility-fractures", "Epidemiology of osteoporosis and fragility fractures") + ".",
 "Royal Osteoporosis Society. " + ext("https://www.bgs.org.uk/strong-steady-straight-nos-exercise-and-osteoporosis-consensus-statement", "Strong, Steady and Straight: an expert consensus statement on physical activity and exercise for osteoporosis") + ". 2019.",
 "Watson SL, Weeks BK, Weis LJ, et al. " + ext("https://academic.oup.com/jbmr/article-abstract/33/2/211/7605709", "High-intensity resistance and impact training improves bone mineral density and physical function in postmenopausal women with osteopenia and osteoporosis: the LIFTMOR randomized controlled trial") + ". J Bone Miner Res. 2018;33(2):211-220.",
]

KEMIK_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Kemik erimesi (osteoporoz)</h1>
    <p class="lede">Kemiklerin yoğunluğunun ve iç yapısının zayıflayarak kolay kırılır hale gelmesidir. Çoğu zaman bir kırık olana kadar belirti vermez. İyi haber: doğru egzersiz, düşmeleri önleme ve gerektiğinde ilaç tedavisiyle kırık riski azaltılabilir.</p>
    <p class="meta">Son güncelleme: {UPDATED}</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>3'te 1</b><span>50 yaş üstündeki kadınlarda hayat boyu kemik erimesine bağlı kırık</span></div>
        <div class="stat"><b>5'te 1</b><span>50 yaş üstündeki erkeklerde hayat boyu kemik erimesine bağlı kırık</span></div>
        <div class="stat"><b>37 milyon</b><span>Dünyada 55 yaş üstünde yılda görülen kırılganlık kırığı; dakikada 70</span></div>
        <div class="stat"><b>%21</b><span>50 yaş üstündeki kadınlarda kemik erimesi sıklığı; erkeklerde %6</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Kemik, sürekli yıkılıp yeniden yapılan canlı bir dokudur. Yaşla ve özellikle kadınlarda menopozdan sonra yıkım yapımın önüne geçer; kemik yoğunluğu azalır, iç yapısı incelir. Sonuçta basit bir düşme ya da öne eğilip yük kaldırma gibi zorlamalar kırığa yol açabilir. En sık omurga, kalça ve el bileği kırılır.</p>
        <p class="soft">Tanı kemik yoğunluğu ölçümüyle (DEXA) konur. Kimin ne zaman ölçüm yaptırması gerektiğine risk etkenlerine göre hekim karar verir.</p>
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

  <section>
    <div class="wrap">
      <h2>Güçlü, dengeli ve dik: egzersiz önerileri</h2>
      <p class="soft">İngiltere Osteoporoz Derneği'nin uzman görüş bildirisi egzersizi üç hedef etrafında topluyor: kemiği güçlendirmek, düşmeleri önlemek ve omurgayı korumak.</p>
      <ul class="tx">
        <li><b>Kas güçlendirme</b><span>Haftada 2–3 gün; zamanla her hareket için 8–12 tekrarlık 3 sete kadar çıkılır. Sırt kaslarını güçlendiren hareketler de programda yer almalıdır.</span></li>
        <li><b>Darbe egzersizleri</b><span>Uygun olanlarda çoğu gün yaklaşık 50 orta şiddetli darbe, örneğin hafif koşu adımları ya da küçük sıçramalar önerilir. Kırık öyküsü olanlarda program kişiye göre uyarlanır.</span></li>
        <li><b>Denge</b><span>65 yaş üstündekiler ve denge sorunu olanlar için denge ve güçlendirme egzersizleri önerilir. <a href="dusme-onleme.html">Düşmeleri önleme rehberine göz atın →</a></span></li>
        <li><b>Omurgayı korumak</b><span>Omurgayı uzun süre, en uç noktaya kadar ya da yük altında öne bükmeyi gerektiren hareketlerin değiştirilmesi önerilir. Yük kaldırırken kalçadan eğilmeyi (menteşe hareketi) öğrenmek önemlidir.</span></li>
        <li><b>Gözetimli yoğun programlar</b><span>Menopoz sonrası kemik yoğunluğu düşük kadınlarda uzman gözetiminde yapılan yüksek yoğunluklu kuvvet ve darbe egzersizi, 8 ayda omurga kemik yoğunluğunu kontrol grubuna göre belirgin şekilde artırdı. Bu tür programlar yalnızca kişiye göre planlanıp gözetim altında uygulanmalıdır.</span></li>
      </ul>
      <div class="callout">
        <p>İlaç tedavisi, kalsiyum ve D vitamini ihtiyacı kişiye göre değişir; bunlara hekiminiz karar verir. Sigarayı bırakmak ve alkolü sınırlamak da kemikleri korur.</p>
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

  <section>
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
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(KEMIK_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Öne eğilme, yük kaldırma, öksürme ya da küçük bir düşmeden sonra aniden başlayan şiddetli sırt ağrısı (omurga kırığı olabilir)</li>
        <li>Düşme sonrası kalça ağrısı ve bacağa yük verememe (kalça kırığı olabilir)</li>
        <li>Sırt ağrısıyla birlikte bacaklarda uyuşma, güç kaybı ya da idrar ve dışkı kontrolünde bozulma (acil)</li>
        <li>Boyda belirgin kısalma ya da hızla artan kamburluk</li>
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
     "Kemik erimesi (osteoporoz) nedir, kimlerde görülür, egzersiz güvenli mi, hangi hareketlerden kaçınmalı? Güçlü, dengeli ve dik: evde altı egzersiz, günlük hayatta omurgayı koruma, videolar ve uyarı işaretleri.",
     "kemik-erimesi.html", NECK_CSS, KEMIK_BODY, YT_JS,
     seo_title="Kemik Erimesi (Osteoporoz): Egzersizler ve Güvenli Hareket | İhsan Eren",
     condition="Kemik erimesi (osteoporoz)", about=cond("Kemik erimesi (osteoporoz)"),
     faq_items=pick(KEMIK_FAQ, 0, 1, 2, 3))

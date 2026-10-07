# -*- coding: utf-8 -*-
# Yeni rehberler (8): kalp rehabilitasyonu (kalp krizi, stent ve bypass sonrası egzersiz).
# cond8_part.py'den sonra exec edilir. Videolar British Heart Foundation kanalından (kimlikler oEmbed ile doğrulandı).

_ex2("cr_walk", "walk", "Yürüyüş", "Düz bir zeminde, konuşabildiğiniz ama şarkı söyleyemediğiniz bir tempoda yürüyün. İlk birkaç dakikayı yavaş başlayıp hızlanın, son birkaç dakikada yavaşlayın. Süreyi haftadan haftaya azar azar artırın.", "10 dakikayla başlayın; hedef günde 30 dakika")
_ex2("cr_wall", "wall", "Duvarda yarım çömelme", "Sırtınızı duvara dayayın, ayaklarınız duvardan bir adım önde olsun. Nefes verirken dizlerinizi hafifçe bükerek sırtınızı aşağı kaydırın ve beklemeden yukarı çıkın. Nefesinizi tutmayın.", "8–10 tekrar, 2 set")

# ============================================================== KALP REHABİLİTASYONU
CR_FAQ = [
 ("Kalp krizinden sonra egzersiz yapmak güvenli mi?", "Kardiyoloğunuzun onayıyla ve kademeli olarak yapıldığında evet. 85 çalışmanın derlemesinde egzersize dayalı rehabilitasyona katılanlarda yeniden kalp krizi ve hastaneye yatış daha az görüldü. Hangi şiddette başlayacağınızı hekiminiz belirler."),
 ("Ne zaman başlayabilirim?", "Bu, geçirdiğiniz olaya ve yapılan işleme göre değişir; kararı kardiyoloğunuz verir. Genellikle hastanede kısa yürüyüşlerle başlanır, taburcu olduktan sonra program kademeli olarak ilerletilir."),
 ("Evde mi, merkezde mi yapmalıyım?", "24 çalışmayı (3.046 kişi) inceleyen derlemede, sağlık çalışanlarınca desteklenen ev programları ile merkezde yapılan programlar benzer etkili bulundu. Hangisine düzenli devam edebilecekseniz onu seçin; ev programı da hekim onayı ve düzenli izlem gerektirir."),
 ("Egzersiz sırasında nabzım kaç olmalı?", "Hedef nabız kişiye göre değişir ve kullandığınız ilaçlardan etkilenir; bu yüzden herkese tek bir sayı vermek doğru olmaz. Hekiminiz size bir aralık belirlemediyse konuşma testini kullanın: konuşabiliyor ama şarkı söyleyemiyorsanız orta şiddettesiniz."),
]

CR_SRC = [
 "Dibben G, de Vries FBG, Faulkner J, et al. " + ext("https://www.cochrane.org/CD001800", "Exercise-based cardiac rehabilitation for coronary heart disease") + ". Cochrane Database Syst Rev. 2026;(9):CD001800.",
 "McDonagh STJ, Dalal H, Moore S, et al. " + ext("https://www.cochrane.org/CD007130", "Home-based versus centre-based cardiac rehabilitation") + ". Cochrane Database Syst Rev. 2023;(10):CD007130.",
 "World Health Organization. " + ext("https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)", "Cardiovascular diseases (CVDs)") + ". Fact sheet. 31 July 2025.",
]

CR_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>Kalp rehabilitasyonu</h1>
    <p class="lede">Kalp krizi, stent ya da bypass ameliyatından sonra pek çok kişi hareket etmekten korkar. Oysa doğru ayarlanmış egzersiz tedavinin parçasıdır: 85 çalışmanın derlemesinde egzersize dayalı kalp rehabilitasyonu yeniden kalp krizi ve hastaneye yatış riskini azalttı. Program kardiyoloğunuzun onayıyla başlar ve adım adım ilerler.</p>
    <p class="meta">Son güncelleme: 7 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%28</b><span>Kalp rehabilitasyonuyla yeniden kalp krizi riskindeki azalma (85 çalışma, 23.430 kişi)</span></div>
        <div class="stat"><b>%42</b><span>Aynı derlemede 6–12 aylık izlemde hastaneye yatış riskindeki azalma</span></div>
        <div class="stat"><b>24 çalışma</b><span>Evde ve merkezde yapılan rehabilitasyonu karşılaştıran araştırmalar; sonuçlar benzer</span></div>
        <div class="stat"><b>19,8 milyon</b><span>2022'de kalp-damar hastalıklarından ölenler; dünyadaki ölümlerin yaklaşık %32'si (DSÖ)</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Kalp rehabilitasyonu, egzersiz eğitimini risk etkenlerini azaltmaya yönelik eğitim ve duygusal destekle birleştiren bir programdır. Amaç, kalbi zorlamadan dayanıklılığı adım adım artırmak ve yeni bir kalp olayının önüne geçmektir.</p>
        <p class="soft">Program çoğunlukla hastanede kısa yürüyüşlerle başlar, taburcu olduktan sonra haftalarca sürer ve ömür boyu sürdürülecek bir hareket alışkanlığına dönüşür. Egzersizin türü ve şiddeti kardiyoloğunuzun değerlendirmesine göre belirlenir.</p>
      </div>
      <div>
        <h2>Kimler için?</h2>
        <ul class="dots">
          <li>Kalp krizi geçirenler</li>
          <li>Stent takılanlar</li>
          <li>Bypass ameliyatı olanlar</li>
          <li>Kalp yetersizliği olanlar</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Araştırmalar ne gösteriyor?</h2>
      <p class="soft">2026'da güncellenen Cochrane derlemesi, koroner kalp hastalığı olan 23.430 kişiyle yapılmış 85 rastgele kontrollü çalışmayı inceledi; katılımcıların çoğu kalp krizi geçirmiş ya da damar açma işlemi (stent, bypass) görmüştü. Egzersize dayalı rehabilitasyon, 6–12 aylık izlemde yeniden kalp krizi riskini %28, hastaneye yatış riskini %42 azalttı: yaklaşık her 12 kişide bir hastane yatışı önlendi. Ölümlerde küçük bir azalma olası görünüyor, ancak bu sonuç kesin değil. Katılımcıların yalnızca %17'si kadındı.</p>
      <p class="soft">Evde yapılan programlar da işe yarıyor: 24 çalışmayı (3.046 kişi) inceleyen bir başka Cochrane derlemesinde, sağlık çalışanlarınca desteklenen ev programları ile merkezde yapılan programlar arasında egzersiz kapasitesi, yaşam kalitesi ve ölüm açısından fark bulunmadı.</p>
      <div class="callout">
        <p>Kalp olayından sonra hareket etmekten korkmak çok yaygındır. Ne zaman ve hangi şiddette başlayacağınıza kardiyoloğunuz karar verir; programı onun onayıyla, küçük adımlarla ilerletin.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Programın parçaları</h2>
      <ul class="tx">
        <li><b>Değerlendirme</b><span>Başlamadan önce kardiyoloğunuz kalbinizin durumunu değerlendirir, gerekirse efor testi yapar ve sizin için güvenli egzersiz aralığını belirler.</span></li>
        <li><b>Dayanıklılık egzersizi</b><span>Yürüyüş ve bisiklet gibi egzersizler programın temelidir. Hedef, konuşabildiğiniz ama şarkı söyleyemediğiniz orta şiddettir; kısa sürelerle başlanır ve kademeli olarak artırılır.</span></li>
        <li><b>Güçlendirme</b><span>Hafif dirençle yapılan kas güçlendirme egzersizleri eklenir. Nefesinizi tutmayın; zorlandığınız kısımda nefes verin.</span></li>
        <li><b>Isınma ve soğuma</b><span>Her seansa hafif tempoda ısınarak başlayın ve yavaşlayarak bitirin; egzersizi aniden kesmeyin.</span></li>
        <li><b>Risk etkenleri</b><span>Sigarayı bırakmak, tansiyon, kolesterol ve şekerin kontrolü, beslenme ve ilaçların düzenli kullanımı programın egzersiz kadar önemli parçalarıdır.</span></li>
        <li><b>Duygusal destek</b><span>Kalp olayından sonra kaygı ve çökkünlük sık görülür; bunları ekibinizle konuşmak tedavinin parçasıdır.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Kalp rehabilitasyonunda altı egzersiz</h2>
      <p class="soft">Bu hareketler, kardiyoloğunuz egzersize izin verdikten sonra evde yapılabilecek hafif ve orta şiddetli örneklerdir. Göğüs ağrısı, baskı hissi, baş dönmesi ya da alışılmadık nefes darlığı olursa hemen durun.</p>
      {ex_grid(["cr_walk", "copd_sts", "mn_kext", "copd_heel", "pf_sabd", "cr_wall"])}
      <div class="callout">
        <p>Bypass ya da başka bir açık kalp ameliyatı olduysanız, göğüs kemiğiniz kaynayana kadar ağır kaldırma, itme ve çekme hareketlerinden kaçının; süreyi cerrahınız söyler.</p>
      </div>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Kalp rehabilitasyonu için videolar</h2>
      <p class="soft">İngiliz Kalp Vakfı'nın (British Heart Foundation) YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("ESYDPnY5_1A", "Evde kalp rehabilitasyonuna giriş videosunu oynat", "An introduction to Cardiac Rehab at Home")}
          <h3>Evde kalp rehabilitasyonuna giriş</h3>
          <p>Evde kalp rehabilitasyonu video dizisinin tanıtımı.</p>
        </div>
        <div class="vid">
          {vbox("-JsuNKbAAkU", "Evde kalp rehabilitasyonu 1. düzey program videosunu oynat", "Cardiac Rehab at Home - Level 1 Programme")}
          <h3>Evde kalp rehabilitasyonu: 1. düzey program</h3>
          <p>Dizinin başlangıç düzeyindeki egzersiz programı.</p>
        </div>
      </div>
      <p class="meta">Videolar British Heart Foundation kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(CR_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda egzersizi bırakın; “acil” yazanlarda 112'yi arayın:</p>
      <ul class="dots redflags">
        <li>Göğüste baskı, sıkışma ya da ağrı; kola, çeneye ya da sırta yayılan ağrı (acil)</li>
        <li>Dinlenmekle geçmeyen nefes darlığı (acil)</li>
        <li>Bayılma ya da bayılacak gibi olma (acil)</li>
        <li>Soğuk terleme ve bulantıyla birlikte fenalık hissi (acil)</li>
        <li>Düzensiz ya da çok hızlı kalp atışı</li>
        <li>Ayak bileklerinde yeni gelişen şişlik ya da birkaç günde hızlı kilo artışı</li>
      </ul>
      {CTA_CARD("Kalp rehabilitasyonu", "kalp rehabilitasyonu")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(CR_SRC)}
    </div>
  </section>
</main>'''

page("kalp-rehabilitasyonu.html", "Kalp Rehabilitasyonu",
     "Kalp krizi, stent ya da bypass sonrası egzersiz güvenli mi? Kalp rehabilitasyonunun kanıtlanmış yararları, evde ve merkezde programlar, altı egzersiz ve videolar.",
     "kalp-rehabilitasyonu.html", NECK_CSS, CR_BODY, YT_JS,
     seo_title="Kalp Rehabilitasyonu: Kalp Krizi ve Bypass Sonrası Egzersiz | İhsan Eren",
     condition="Koroner kalp hastalığı", faq_items=CR_FAQ)

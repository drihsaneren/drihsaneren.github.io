# -*- coding: utf-8 -*-
# Yeni rehber (26): omuz çıkığı (omuz instabilitesi). cond25_part.py'den sonra exec edilir. Video yok.
# scap2, isoer, scaption, row, sler omuz rehberlerinden (çevirileri hazır); duvarda parmak yürütme bu sayfaya özel.

_ex2("di_wall", "wslide", "Duvarda parmak yürütme", "Yüzünüz duvara dönük durun. Parmaklarınızı duvarda yürütür gibi rahat ettiğiniz yüksekliğe kadar çıkarın, kısa bir süre bekleyin ve yavaşça geri indirin. İlk haftalarda kolunuzu omuz hizasının üstüne zorlamayın.", "10 tekrar, günde 3–4 kez")

DI_FAQ = [
 ("Omzumu kendim yerine takabilir miyim?", "Hayır, omzu kendiniz yerine takmaya çalışmayın. En kısa sürede acil servise gidin; araba kullanmayın, gerekirse 112’yi arayın."),
 ("Askıyı ne kadar takmalıyım?", "Askı rahatlık içindir. Ağrı azaldıkça çıkarabilir, otururken kolunuzu bir yastığa destekleyebilirsiniz. Kırık yoksa genellikle 2 haftadan sonra askı kullanılmaz; size özel bir süre verildiyse ona uyabilirsiniz."),
 ("Omzum yeniden çıkar mı?", "Olabilir. Çalışmaların ortak değerlendirmesinde ilk kez öne çıkan omuzların yaklaşık %39’unda yeniden çıkma ya da yerinden kayma görüldü. 40 yaş ve altında olmak, erkek olmak ve eklemlerin doğuştan gevşek olması bu olasılığı artırıyor. Fizyoterapi omuz kaslarını güçlendirir; gençlerde ve tekrarlayan çıkıklarda ameliyat da konuşulabilir. 22 randomize çalışmayı birleştiren 2018 tarihli bir analizde, ilk çıkıktan sonra ameliyatsız izlenenlerin yaklaşık %47'sinde 2 yıl içinde yeniden çıkık görülmedi. Kolun dışa dönük pozisyonda özel bir askıyla tutulması yeniden çıkmayı azaltmadı; yazarlar rahatlık için sıradan bir kol askısını yeterli buluyor."),
 ("İlk çıkıktan sonra ameliyat gerekir mi?", "Her zaman değil. 22 randomize çalışmayı birleştiren bir ağ meta-analizinde (BJSM, 2018), ilk kez çıkan omuzlarda fizyoterapiyle izlenen hastaların yaklaşık yarısında omuz yeniden çıkmadı. Eklem dudağının (labrum) ameliyatla onarılması ise yeniden çıkma riskini azalttı (orta kalitede kanıt). Bu yüzden karar yaşa, spora, yeniden çıkma riskine ve kişinin tercihine göre verilir; gençlerde ve tekrarlayan çıkıklarda bir omuz uzmanının görüşü alınabilir."),
 ("40 yaşın üstündeyim; çıkıktan sonra kolumu kaldıramıyorum. Normal mi?", "40 yaş üstünde omuz çıkığından sonra rotator manşet yırtığı sık görülür ve çıkık yerine oturtulduktan sonra çekilen röntgen normal olsa bile gözden kaçabilir: çalışmalarda bu yaş grubunda çıkık geçirenlerin yaklaşık yarısında yırtık bulundu. BMJ'deki bir yazıya göre bu durumda acil ultrason ya da MR yapılmalı. Kolunuzu kaldıramıyorsanız ya da güçsüzlük sürüyorsa beklemeden hekiminize başvurun; ayrıntılar için <a href=\"rotator-manset-yirtigi.html\">rotator manşet yırtığı</a> rehberine bakabilirsiniz."),
 ("Ne zaman araba kullanabilir ve spora dönebilirim?", "Askı takılıyken araba kullanılmaz; çoğu kişi 4–6 hafta sonra, kolunun gücü ve hareketi yeterli olunca araba kullanabilir. Hafif etkinliklere yaklaşık 6 hafta sonra dönülebilir; bazı sporlara tam dönüş 16 haftayı bulabilir. Ne zaman güvenli olduğunu hekiminiz ya da fizyoterapistiniz söyleyecektir."),
]

DI_SRC = [
 "Iqbal S, Jacobs U, Akhtar A, Macfarlane R, Waseem M. " + ext("https://openorthopaedicsjournal.com/VOLUME/7/PAGE/305/FULLTEXT/", "A history of shoulder surgery") + ". Open Orthop J. 2013;7:305.",
 "Craig R, Holt T, Rees JL. " + ext("https://ora.ox.ac.uk/objects/uuid:1d27d3d2-1048-48aa-98c7-e69f76ed5ed4/files/m0a9dde391dc1737a24b6a88a156a90bd", "Acute rotator cuff tears (Easily missed?)") + ". BMJ. 2017. doi:10.1136/bmj.j5366.",
 "NHS. " + ext("https://www.nhs.uk/conditions/dislocated-shoulder/", "Dislocated shoulder") + ". Page last reviewed 16 September 2026.",
 "Olds M, Ellis R, Donaldson K, Parmar P, Kersten P. Risk factors which predispose first-time anterior traumatic shoulder dislocations to recurrent instability in adults: a systematic review and meta-analysis. Br J Sports Med. 2015;49(14):913–922. " + ext("https://repository.canterbury.ac.uk/item/91826/-risk-factors-which-predispose-first-time-anterior-traumatic-shoulder-dislocations-to-recurrent-instability-in-adults-a-systematic-review-and-meta-analysis", "Özet") + ".",
 "Kavaja L, Lähdeoja T, Malmivaara A, Paavola M. " + ext("https://bjsm.bmj.com/content/52/23/1498", "Treatment after traumatic shoulder dislocation: a systematic review with a network meta-analysis") + ". Br J Sports Med. 2018;52(23):1498-1506. Özet: " + ext("https://search.pedro.org.au/search-results/record-detail/54445", "PEDro") + ".",
 "Northern Lincolnshire and Goole NHS Foundation Trust. " + ext("https://www.nlg.nhs.uk/resources/anterior-shoulder-dislocation-patients-under-40-years-old-and-no-fracture/", "Anterior shoulder dislocation: patients under 40 years old and no fracture") + ". December 2025.",
 "Worcestershire Acute Hospitals NHS Trust. " + ext("https://www.worcsacute.nhs.uk/leaflets/shoulder-dislocation/", "Shoulder dislocation") + ".",
 "University Hospitals of Leicester NHS Trust. " + ext("https://www.uhleicester.nhs.uk/wp-content/uploads/2025/06/1158_122024-Advice-and-exercises-for-a-dislocated-shoulder.pdf", "Advice and exercises for a dislocated shoulder") + ". Last reviewed December 2024.",
]

DI_TL = [
 ("MÖ 400 dolayı", "Hipokrat, hasta sırtüstü yatarken hekimin ayağını koltuk altına dayayıp kolu çekerek omzu yerine yerleştirme yöntemini tarif etti."),
 ("1870", "Kocher, omzu kaldıraç hareketiyle yerine yerleştiren bir yöntemi yeniden tanıttı; bu yöntem bugün ciddi komplikasyon olasılığı nedeniyle terk edilmiş durumda."),
 ("1906", "Perthes, omuz yuvasının kenarındaki eklem dudağının (labrum) ayrılmasının çıkığın tekrarlamasına yol açtığını gösterdi."),
 ("1923", "Bankart (BMJ) aynı bulguyu anlattı ve ayrılan eklem dudağının yeniden tutturulmasının önemini vurguladı; bu onarım bugün onun adıyla anılıyor."),
 ("1954", "Latarjet, kürek kemiğindeki korakoid çıkıntının omuz yuvasının önüne aktarıldığı ameliyatı ilk kez tarif etti."),
 ("2015", "10 çalışmayı ve 1.324 kişiyi birleştiren meta-analiz (BJSM): ilk kez öne çıkan omuzların yaklaşık %39'unda yeniden çıkma ya da yerinden kayma görüldü; 40 yaş ve altında olmak en güçlü risk etkeniydi."),
 ("2017", "BMJ'de yayımlanan bir yazıda, 40 yaş üstünde omuz çıkığından sonra rotator manşet yırtığının sık olduğu ve kolayca gözden kaçabildiği vurgulandı."),
 ("2018", "22 randomize çalışmayı birleştiren ağ meta-analizi (BJSM): ilk çıkıktan sonra fizyoterapiyle izlenen hastaların yaklaşık yarısında omuz yeniden çıkmadı; eklem dudağının onarımı yeniden çıkma riskini azalttı; kolun dışa dönük askıya alınması içe dönük askıya göre yarar sağlamadı."),
]

DI_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Omuz çıkığı (omuz instabilitesi)</h1>
    <p class="lede">Omuz çıkığı, kol kemiğinin başının omuzdaki yuvasından çıkmasıdır; çoğunlukla düşme ya da spor sırasında olur ve en sık öne doğru çıkar. Omuz bir kez çıktıktan sonra yeniden çıkma ya da yerinden kayma eğilimi gösterebilir; buna omuz instabilitesi denir. Yerine takıldıktan sonra yapılan egzersizler, omzun gücünü ve hareketini geri kazandırmanın temelidir.</p>
    <p class="meta">Son güncelleme: 6 Kasım 2026</p>
  </div>
</header>
<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%39</b><span>İlk kez öne çıkan omuzlarda yeniden çıkma ya da yerinden kayma oranı (10 çalışma, 1.324 kişi)</span></div>
        <div class="stat"><b>40 yaş ve altı</b><span>Yeniden çıkma için en güçlü risk etkeni</span></div>
        <div class="stat"><b>2 hafta</b><span>Kırık yoksa askının genellikle bırakıldığı süre</span></div>
        <div class="stat"><b>6–12 hafta</b><span>Çoğu kişide iyileşme süresi; bazı sporlara tam dönüş 16 haftayı bulabilir</span></div>
      </div>
      {g_toc([("belirtiler", "Belirtiler ve ilk yardım"), ("tedavi", "Tedavi ve iyileşme"), ("40-yas", "40 yaş üstünde dikkat"), ("sonrasi", "Yerine takıldıktan sonra"), ("tarihce", "Geçmişten bugüne"), ("egzersizler", "Egzersizler"), ("sss", "Sık sorulan sorular"), ("uyari", "Uyarı işaretleri")])}
    </div>
  </section>
  <section id="belirtiler">
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Kolu hareket ettirememe.</li>
          <li>Omzun yerinden çıkmış ya da şekli bozulmuş görünmesi.</li>
          <li>Ağrı, şişlik ve morarma.</li>
        </ul>
      </div>
      <div>
        <h2>Omuz çıkarsa ne yapmalı?</h2>
        <ul class="dots">
          <li>Omzu kendiniz yerine takmaya çalışmayın; en kısa sürede acil servise gidin. Araba kullanmayın, gerekirse 112’yi arayın.</li>
          <li>Beklerken kolunuzu bir askı ya da havluyla destekleyip hareketsiz tutun.</li>
          <li>Havluya sarılı buzu en fazla 20 dakika, 2–3 saatte bir uygulayabilirsiniz.</li>
        </ul>
      </div>
    </div>
  </section>
  <section id="tedavi">
    <div class="wrap two">
      <div>
        <h2>Tedavi ve iyileşme</h2>
        <p class="soft">Çıkık genellikle röntgenle doğrulanır ve hekim, lokal uyuşturma ya da sakinleştirici ilaç altında omzu yerine yerleştirir. Ardından bir askı verilir. Çoğu kişi 6–12 haftada iyileşir; omzun gücünün ve işlevinin tamamen geri gelmesi bir yılı bulabilir.</p>
        <p class="soft">Yeniden çıkma olasılığını azaltmak için bazen ameliyat önerilir. Gençlerde bir omuz uzmanına yönlendirme yapılabilir.</p>
      </div>
      <div>
        <h2>Yeniden çıkma riski</h2>
        <p class="soft">10 çalışmanın ve 1.324 kişinin birlikte değerlendirildiği bir analizde, ilk kez öne çıkan omuzların yaklaşık %39’unda yeniden çıkma ya da yerinden kayma görüldü. Riski artıran etkenler:</p>
        <ul class="dots">
          <li>40 yaş ve altında olmak (en güçlü etken)</li>
          <li>Erkek olmak</li>
          <li>Eklemlerin doğuştan gevşek olması</li>
        </ul>
        <p class="soft">Çıkıkla birlikte kol kemiğinin üst dış yanındaki çıkıntıda kırık olanlarda ise yeniden çıkma daha az görüldü.</p>
      </div>
    </div>
  </section>
  <section id="40-yas">
    <div class="wrap">
      <h2>40 yaş üstünde dikkat: rotator manşet yırtığı</h2>
      <p class="soft">BMJ'de yayımlanan bir yazıya göre 40 yaş üstünde omuz çıkığından sonra rotator manşet yırtığı sık görülür: çalışmalarda bu yaş grubunda çıkık geçirenlerin yaklaşık yarısında yırtık bulundu. Yırtık, çıkık yerine oturtulduktan sonra çekilen röntgen normal olsa bile gözden kaçabilir. Bu yüzden 40 yaş üstünde çıkıktan sonra acil ultrason ya da MR öneriliyor. Çıkıktan sonra kolunuzu kaldıramıyorsanız ya da güçsüzlük sürüyorsa beklemeden hekiminize başvurun.</p>
    </div>
  </section>
  <section id="sonrasi">
    <div class="wrap">
      <h2>Yerine takıldıktan sonra</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Askı</h3><p>Askı rahatlık içindir. Otururken çıkarıp kolunuzu bir yastığa destekleyebilirsiniz; kırık yoksa genellikle 2 haftadan sonra kullanılmaz.</p></div>
        <div class="kind"><span class="n">2</span><h3>Kaçınılacak pozisyon</h3><p>İlk haftalarda kolunuzu omuz hizasının üstüne kaldırmaktan ve kolunuzu yana açıp elinizi tavana doğru döndürmekten, özellikle zorlayarak, kaçınabilirsiniz.</p></div>
        <div class="kind"><span class="n">3</span><h3>Dirsek ve bilek</h3><p>Dirsek bükme, avuç çevirme ve bilek hareketlerine hemen başlayabilirsiniz.</p></div>
        <div class="kind"><span class="n">4</span><h3>Buz ve ağrı kesici</h3><p>Havluya sarılı buz ağrıyı hafifletebilir; ağrı kesici için hekiminize danışın.</p></div>
      </div>
      <p class="soft" style="margin-top:18px">Omuz ağrısının diğer nedenleri için <a href="rotator-manset-yirtigi.html">rotator manşet yırtığı</a> ve <a href="donuk-omuz.html">donuk omuz</a> rehberlerine bakabilirsiniz.</p>
    </div>
  </section>
  <section id="tarihce">
    <div class="wrap">
      <p class="eyebrow">Geçmişten bugüne</p>
      <h2>Hipokrat'tan bugüne</h2>
      <p class="soft">Omuz çıkığını yerine yerleştirme yöntemleri iki bin yılı aşkın süredir anlatılıyor. 20. yüzyılda çıkığın neden tekrarladığı anlaşıldı; son yıllardaki çalışmalar ise kimde yeniden çıkma riskinin yüksek olduğunu ve fizyoterapi ile ameliyatın yerini netleştirdi.</p>
      {g_tl(DI_TL)}
      <h3 class="g-h3">Tedavi seçenekleri: kanıtlar ne diyor?</h3>
      <p class="soft">22 randomize çalışmayı birleştiren ağ meta-analizinin (BJSM, 2018) bulguları. Kanıtın kalitesi parantez içinde belirtilmiştir; tedavi kişiye göre seçilir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Fizyoterapi</h3><dl><dt>BJSM</dt><dd>İlk kez çıkan omuzlarda fizyoterapiyle izlenen hastaların yaklaşık yarısında omuz yeniden çıkmadı (orta kalite).</dd></dl></div>
        <div class="kind"><h3>Eklem dudağı onarımı</h3><dl><dt>BJSM</dt><dd>Yeniden çıkma riskini azalttı (orta kalite). Açık ameliyat, yeniden çıkmayı önlemede artroskopik ameliyattan daha iyi olabilir (düşük kalite).</dd></dl></div>
        <div class="kind"><h3>Askının pozisyonu</h3><dl><dt>BJSM</dt><dd>Kolun dışa dönük askıya alınması, içe dönük askıya göre yarar sağlamadı (çok düşük–düşük kalite).</dd></dl></div>
        <div class="kind"><h3>Tekrarlayan çıkık</h3><dl><dt>BJSM</dt><dd>Süreğen dengesizlik gelişirse ameliyat düşünülebilir; ancak bu durumda ameliyatın etkinliğine dair kanıt bulunamadı.</dd></dl></div>
      </div>
    </div>
  </section>
  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Omzu güçlendiren altı egzersiz</h2>
      <p class="soft">Askıyı bıraktıktan sonra, hekiminiz ya da fizyoterapistiniz uygun gördüğünde başlayabilirsiniz. Yavaş başlayın, ağrı yapan hareketi durdurun. İlk haftalarda kolunuzu omuz hizasının üstüne kaldırmayın.</p>
      {ex_grid(["scap2", "isoer", "di_wall", "scaption", "row", "sler"])}
    </div>
  </section>
  <section id="sss">
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(DI_FAQ)}
    </div>
  </section>
  <section id="uyari">
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <p class="soft"><strong>Hemen acil servise ya da 112'ye:</strong></p>
      <ul class="dots redflags">
        <li>Omzunuz yerinden çıktıysa ya da şekli bozuk görünüyorsa</li>
        <li>Elde soğukluk, solukluk ya da renk değişikliği</li>
        <li>Kolunuzda ya da elinizde yeni başlayan uyuşma, karıncalanma ya da güçsüzlük</li>
      </ul>
      <p class="soft"><strong>Beklemeden, en geç birkaç gün içinde bir hekime:</strong></p>
      <ul class="dots redflags">
        <li>40 yaş üstünde çıkıktan sonra kolu kaldıramama ya da süren güçsüzlük</li>
        <li>Omzunuz yeniden çıktıysa ya da sık sık yerinden kayıyormuş gibi hissediyorsanız</li>
        <li>Ağrı ve tutukluk geçmiyor ya da kötüleşiyorsa</li>
      </ul>
      {CTA_CARD("Omuz çıkığı sonrası iyileşmeniz", "omuz çıkığı sonrası")}
    </div>
  </section>
  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(DI_SRC)}
    </div>
  </section>
</main>'''

page("omuz-cikigi.html", "Omuz Çıkığı (Omuz İnstabilitesi)",
     "Omuz çıktığında ne yapmalı, askı ne kadar takılır, omuz yeniden çıkar mı, ameliyat gerekir mi? Risk etkenleri, 40 yaş üstünde rotator manşet yırtığı, kanıtların karşılaştırması, kısa tarihçe, kaçınılacak pozisyon ve evde altı egzersiz.",
     "omuz-cikigi.html", NECK_CSS, DI_BODY, "",
     seo_title="Omuz Çıkığı: Ne Yapmalı, Askı, Egzersiz ve Yeniden Çıkma Riski | İhsan Eren",
     condition="Omuz çıkığı ve omuz instabilitesi", faq_items=DI_FAQ)

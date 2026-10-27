# -*- coding: utf-8 -*-
# Yeni rehber (26): omuz çıkığı (omuz instabilitesi). cond25_part.py'den sonra exec edilir. Video yok.
# scap2, isoer, scaption, row, sler omuz rehberlerinden (çevirileri hazır); duvarda parmak yürütme bu sayfaya özel.

_ex2("di_wall", "wslide", "Duvarda parmak yürütme", "Yüzünüz duvara dönük durun. Parmaklarınızı duvarda yürütür gibi rahat ettiğiniz yüksekliğe kadar çıkarın, kısa bir süre bekleyin ve yavaşça geri indirin. İlk haftalarda kolunuzu omuz hizasının üstüne zorlamayın.", "10 tekrar, günde 3–4 kez")

DI_FAQ = [
 ("Omzumu kendim yerine takabilir miyim?", "Hayır, omzu kendiniz yerine takmaya çalışmayın. En kısa sürede acil servise gidin; araba kullanmayın, gerekirse 112’yi arayın."),
 ("Askıyı ne kadar takmalıyım?", "Askı rahatlık içindir. Ağrı azaldıkça çıkarabilir, otururken kolunuzu bir yastığa destekleyebilirsiniz. Kırık yoksa genellikle 2 haftadan sonra askı kullanılmaz; size özel bir süre verildiyse ona uyabilirsiniz."),
 ("Omzum yeniden çıkar mı?", "Olabilir. Çalışmaların ortak değerlendirmesinde ilk kez öne çıkan omuzların yaklaşık %39’unda yeniden çıkma ya da yerinden kayma görüldü. 40 yaş ve altında olmak, erkek olmak ve eklemlerin doğuştan gevşek olması bu olasılığı artırıyor. Fizyoterapi omuz kaslarını güçlendirir; gençlerde ve tekrarlayan çıkıklarda ameliyat da konuşulabilir. 22 randomize çalışmayı birleştiren 2018 tarihli bir analizde, ilk çıkıktan sonra ameliyatsız izlenenlerin yaklaşık %47'sinde 2 yıl içinde yeniden çıkık görülmedi. Kolun dışa dönük pozisyonda özel bir askıyla tutulması yeniden çıkmayı azaltmadı; yazarlar rahatlık için sıradan bir kol askısını yeterli buluyor."),
 ("Ne zaman araba kullanabilir ve spora dönebilirim?", "Askı takılıyken araba kullanılmaz; çoğu kişi 4–6 hafta sonra, kolunun gücü ve hareketi yeterli olunca araba kullanabilir. Hafif etkinliklere yaklaşık 6 hafta sonra dönülebilir; bazı sporlara tam dönüş 16 haftayı bulabilir. Ne zaman güvenli olduğunu hekiminiz ya da fizyoterapistiniz söyleyecektir."),
]

DI_SRC = [
 "NHS. " + ext("https://www.nhs.uk/conditions/dislocated-shoulder/", "Dislocated shoulder") + ". Page last reviewed 16 September 2026.",
 "Olds M, Ellis R, Donaldson K, Parmar P, Kersten P. Risk factors which predispose first-time anterior traumatic shoulder dislocations to recurrent instability in adults: a systematic review and meta-analysis. Br J Sports Med. 2015;49(14):913–922. " + ext("https://repository.canterbury.ac.uk/item/91826/-risk-factors-which-predispose-first-time-anterior-traumatic-shoulder-dislocations-to-recurrent-instability-in-adults-a-systematic-review-and-meta-analysis", "Özet") + ".",
 "Kavaja L, Lähdeoja T, Malmivaara A, Paavola M. " + ext("https://bjsm.bmj.com/content/52/23/1498", "Treatment after traumatic shoulder dislocation: a systematic review with a network meta-analysis") + ". Br J Sports Med. 2018;52(23):1498.",
 "Northern Lincolnshire and Goole NHS Foundation Trust. " + ext("https://www.nlg.nhs.uk/resources/anterior-shoulder-dislocation-patients-under-40-years-old-and-no-fracture/", "Anterior shoulder dislocation: patients under 40 years old and no fracture") + ". December 2025.",
 "Worcestershire Acute Hospitals NHS Trust. " + ext("https://www.worcsacute.nhs.uk/leaflets/shoulder-dislocation/", "Shoulder dislocation") + ".",
 "University Hospitals of Leicester NHS Trust. " + ext("https://www.uhleicester.nhs.uk/wp-content/uploads/2025/06/1158_122024-Advice-and-exercises-for-a-dislocated-shoulder.pdf", "Advice and exercises for a dislocated shoulder") + ". Last reviewed December 2024.",
]

DI_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Omuz çıkığı (omuz instabilitesi)</h1>
    <p class="lede">Omuz çıkığı, kol kemiğinin başının omuzdaki yuvasından çıkmasıdır; çoğunlukla düşme ya da spor sırasında olur ve en sık öne doğru çıkar. Omuz bir kez çıktıktan sonra yeniden çıkma ya da yerinden kayma eğilimi gösterebilir; buna omuz instabilitesi denir. Yerine takıldıktan sonra yapılan egzersizler, omzun gücünü ve hareketini geri kazandırmanın temelidir.</p>
    <p class="meta">Son güncelleme: 27 Ekim 2026</p>
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
    </div>
  </section>

  <section>
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

  <section>
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

  <section>
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

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Omzu güçlendiren altı egzersiz</h2>
      <p class="soft">Askıyı bıraktıktan sonra, hekiminiz ya da fizyoterapistiniz uygun gördüğünde başlayabilirsiniz. Yavaş başlayın, ağrı yapan hareketi durdurun. İlk haftalarda kolunuzu omuz hizasının üstüne kaldırmayın.</p>
      {ex_grid(["scap2", "isoer", "di_wall", "scaption", "row", "sler"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(DI_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Omzunuz yerinden çıktıysa ya da şekli bozuk görünüyorsa: hemen acil servise</li>
        <li>Ağrı ve tutukluk geçmiyor ya da kötüleşiyorsa</li>
        <li>Omzunuz yeniden çıktıysa ya da sık sık yerinden kayıyormuş gibi hissediyorsanız</li>
        <li>Kolunuzda ya da elinizde uyuşma, karıncalanma ya da güçsüzlük varsa</li>
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
     "Omuz çıktığında ne yapmalı, askı ne kadar takılır, omuz yeniden çıkar mı? 1.324 kişilik analizden risk etkenleri, iyileşme süresi, kaçınılacak pozisyon ve evde altı egzersiz.",
     "omuz-cikigi.html", NECK_CSS, DI_BODY, "",
     seo_title="Omuz Çıkığı: Ne Yapmalı, Askı, Egzersiz ve Yeniden Çıkma Riski | İhsan Eren",
     condition="Omuz çıkığı ve omuz instabilitesi", faq_items=DI_FAQ)

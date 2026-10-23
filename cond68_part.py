# -*- coding: utf-8 -*-
# Yeni rehber (68): Yoğun bakım sonrası iyileşme. cond67_part.py'den sonra exec edilir. Video yok.
# Kaynaklar (23 Ekim 2026'da okundu): NICE CG83 (2009; 2015 ve 2018 küçük değişiklik), NICE QS158 kalite ifadesi 4, Connolly 2016 (Cochrane özeti; HealthManagement),
# Hatch 2018 Crit Care (DOAJ özeti), Herridge 2011 NEJM (HCPLive), Fan 2014 ATS kılavuzu (PDF), UHS Southampton 2684 v5 (Kas 2024), UHL Leicester 1248 v2 (Şub 2025), ICUsteps 2020.

_ex2("yb_breath", "kb_breath", "Derin nefes", "Dik oturun, ellerinizi alt kaburgalarınıza koyun. Burnunuzdan yavaşça, kaburgalarınızın yana açıldığını hissedecek kadar derin nefes alın, 2–3 saniye tutun ve ağzınızdan yavaşça verin. Balgamınız varsa ardından bir iki kez öksürün.", "5 nefes, gün içinde birkaç kez")
_ex2("yb_apump", "apump", "Ayak bileği pompası", "Yatarken ya da otururken ayak bileklerinizi yukarı ve aşağı doğru hareket ettirin. Bacaklardaki kan dolaşımını destekler, hareketsiz kaldığınız dönemde de yapılabilir.", "20 tekrar, saatte bir")
_ex2("yb_quad", "quad", "Uyluğu sıkma", "Bacaklarınız düz uzanın ya da oturun. Uyluğunuzun ön kasını sıkarak dizinizin arkasını yatağa bastırın, 5 saniye tutun ve gevşetin.", "10 tekrar, günde 3 kez")
_ex2("yb_kext", "kext", "Oturarak diz açma", "Sandalyeye dik oturun. Dizinizi yavaşça düzeltip uyluğunuzun ön kasını sıkın, 3 saniye tutun ve indirin.", "Her bacakla 10 tekrar")
_ex2("yb_sts", "sts", "Sandalyeden kalkıp oturma", "Kolçaklı, sağlam bir sandalye kullanın. Öne eğilip ellerinizden destek alarak kalkın, kontrollü şekilde oturun. Yanınızda biri olsun; yoruldukça dinlenin.", "5 tekrarla başlayın, 10’a çıkın")
_ex2("yb_walk", "walk", "Kısa yürüyüşler", "Ev içinde kısa yürüyüşlerle başlayın; gerekirse baston ya da yürüteç kullanın. Her gün süreyi ya da mesafeyi biraz artırın, yorulduğunuzda oturup dinlenin.", "Birkaç dakikayla başlayın, kademeli artırın")

YB_FAQ = [
 ("İyileşme ne kadar sürer?", "Kişiden kişiye çok değişir. Bir İngiltere hastanesinin hasta broşürüne göre tam iyileşme 6–12 ay sürebilir ve sorunların çoğu aylar içinde azalır. Ağır akciğer yetmezliği geçirmiş, ortanca yaşı 45 olan 109 kişinin izlendiği bir çalışmada, 5 yıl sonra bile 6 dakikada yürünen mesafe beklenenin ortalama %76’sındaydı; buna karşın çalışanların %77’si işine dönmüştü."),
 ("Neden bu kadar güçsüzüm?", "Ağır hastalık, uzun süre yatmak ve bazı tedaviler kasları hızla zayıflatabilir. Amerikan Toraks Derneği’nin kılavuzuna göre uzun süre solunum cihazına bağlı kalanların yaklaşık dörtte birinde tüm vücutta yaygın ve kalıcı bir güçsüzlük gelişiyor. Bu güçsüzlük solunum cihazından ayrılmayı ve hastanede kalışı uzatabilir. Kas gücü, kademeli artırılan hareket ve egzersizle zamanla geri kazanılır."),
 ("Kâbuslar ve gözümün önüne gelen anılar normal mi?", "Evet, sık görülür. Yoğun bakımda yaşanan bilinç bulanıklığının (deliryum) anıları rüya gibi ya da kâbus gibi olabilir ve gerçek olaylarla karışabilir. Bir NHS broşürüne göre canlı rüyalar ve beklenmedik anılar travmatik bir deneyime verilen olağan tepkilerdir ve zamanla azalır. Eve döndükten bir ay sonra hâlâ zorlanıyorsanız hekiminizle konuşun."),
 ("Egzersiz gerçekten işe yarıyor mu?", "Kanıt henüz net değil. Yoğun bakımdan çıktıktan sonra yapılan egzersiz programlarını inceleyen Cochrane derlemesinde, 483 kişiyi kapsayan 6 çalışmanın 3’ünde egzersiz kapasitesi lehine sonuç görüldü, ama kanıtın kalitesi çok düşüktü ve egzersizin etkili olduğu sonucuna varılamadı. Yine de İngiltere’nin ulusal kılavuzu (NICE), risk altındaki herkese kişiye özel, düzenli gözden geçirilen bir rehabilitasyon programı öneriyor."),
 ("Ne yemeliyim?", "İştahsızlık, çabuk doyma ve tat değişikliği sık görülür. Bir NHS broşürü öğün aralarında 2–3 ara öğün, enerjisi ve proteini yüksek yiyecekler, gerekirse besin destek içecekleri ve günde 6–8 bardak sıvı öneriyor. Yutmakta zorlanıyorsanız daha yumuşak yiyecekleri deneyebilirsiniz."),
 ("Ailem de zorlanıyor, bu normal mi?", "Evet. Yoğun bakım hastaları ve yakınları için kurulmuş bir İngiliz derneği olan ICUsteps, yakınların da hem taburculuktan sonra hem de kayıp yaşandığında belirgin bir ruhsal yük taşıdığını vurguluyor. Yakınlarınızın da destek alması, sizin iyileşmenize de yardım eder."),
]

YB_SRC = [
 "National Institute for Health and Care Excellence. " + ext("https://nice.org.uk/guidance/cg83/resources/rehabilitation-after-critical-illness-in-adults-975687209413", "Rehabilitation after critical illness in adults") + ". Clinical guideline CG83, 25 March 2009.",
 "National Institute for Health and Care Excellence. " + ext("https://nice.org.uk/guidance/qs158/chapter/Quality-statement-4-Follow-up-after-critical-care-discharge", "Rehabilitation after critical illness in adults. Quality statement 4: follow-up after critical care discharge") + ". NICE quality standard QS158.",
 "Connolly B, Salisbury L, O’Neill B, et al. " + ext("https://www.healthmanagement.org/s/is-exercise-rehabilitation-after-icu-discharge-effective", "Exercise rehabilitation following intensive care unit discharge for recovery from critical illness: executive summary of a Cochrane Collaboration systematic review") + ". J Cachexia Sarcopenia Muscle. 2016;7(5):520–526.",
 "Hatch R, Young D, Barber V, Griffiths J, Harrison DA, Watkinson P. " + ext("https://doaj.org/article/d84b1b7a705f4eaa9e028c24193a81df", "Anxiety, depression and post traumatic stress disorder after critical illness: a UK-wide prospective cohort study") + ". Crit Care. 2018;22.",
 "Herridge MS, Tansey CM, Matté A, et al. Functional disability 5 years after acute respiratory distress syndrome. N Engl J Med. 2011;364(14):1293–1304. Haber: " + ext("https://hcplive.com/view/ards-has-lingering-negative-impact", "HCPLive") + ".",
 "Fan E, Cheek F, Chlan L, et al. " + ext("https://THORACIC.ORG/statements/resources/cc/ICUAW_cpg.pdf", "An official American Thoracic Society clinical practice guideline: the diagnosis of intensive care unit-acquired weakness in adults") + ". Am J Respir Crit Care Med. 2014;190(12):1437–1446.",
 "University Hospital Southampton NHS Foundation Trust. " + ext("https://www.uhs.nhs.uk/Media/UHS-website-2019/Patientinformation/Visitinghospital/Recovering-after-intensive-care-2684-PIL.pdf", "Recovering after intensive care") + ". Version 5, November 2024.",
 "University Hospitals of Leicester NHS Trust. " + ext("https://www.uhleicester.nhs.uk/wp-content/uploads/2025/06/1248_022025-Help-with-your-thoughts-and-feelings-during-after-a-stay-in-intensive-care-.pdf", "Help with your thoughts and feelings during and after a stay in intensive care") + ". Leaflet 1248, February 2025.",
 "ICUsteps. " + ext("https://icusteps.org/professionals/news-and-updates/recovery-and-rehabilitation-position-statement", "Recovery and rehabilitation for patients following the pandemic: position statement") + ". 13 May 2020.",
]

YB_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>Yoğun bakım sonrası iyileşme</h1>
    <p class="lede">Yoğun bakımdan çıkmak iyileşmenin sonu değil, başlangıcıdır. Pek çok kişi eve döndükten sonra da aylarca güçsüzlük, yorgunluk, iştahsızlık, uyku sorunları, unutkanlık ya da kâbuslarla karşılaşır. Bunlar sık görülür ve çoğu zaman zamanla azalır. Bu rehber neler bekleyebileceğinizi, iyileşmeyi nasıl destekleyebileceğinizi ve evde başlayabileceğiniz altı hafif egzersizi anlatıyor.</p>
    <p class="meta">Son güncelleme: 23 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%55</b><span>Ankete yanıt veren yoğun bakım sonrası hastalarda kaygı, depresyon ya da travma sonrası stres belirtilerinden en az biri (4.943 kişi)</span></div>
        <div class="stat"><b>Dörtte bir</b><span>Uzun süre solunum cihazına bağlı kalanlarda yaygın ve kalıcı kas güçsüzlüğü gelişme oranı</span></div>
        <div class="stat"><b>6–12 ay</b><span>Bir NHS broşürüne göre tam iyileşmenin sürebileceği zaman</span></div>
        <div class="stat"><b>2–3 ay</b><span>Taburculuktan sonra önerilen kontrol ve işlevsel değerlendirme zamanı (NICE)</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Bedeninizde neler olabilir?</h2>
        <ul class="dots">
          <li>Kas güçsüzlüğü ve eklemlerde tutukluk; başta basit işler bile zor gelebilir.</li>
          <li>Yorgunluk, kilo kaybı, iştahsızlık ve çabuk doyma.</li>
          <li>Nefes darlığı ve geçmeyen öksürük, özellikle zatürre ya da COVID-19 sonrası.</li>
          <li>Kısık ya da boğuk ses, tat değişikliği, saç dökülmesi ve ciltte değişiklikler.</li>
        </ul>
      </div>
      <div>
        <h2>Ruh hâlinizde neler olabilir?</h2>
        <ul class="dots">
          <li>Dikkati toplamakta ve hatırlamakta güçlük; uyutulduğunuz günlerin “kayıp” gibi gelmesi.</li>
          <li>Canlı, garip ya da korkutucu rüyalar; bazen gerçek olmayan şeyleri görmüş ya da duymuş olma.</li>
          <li>Kaygı, karamsarlık, suçluluk duygusu ve uyku sorunları.</li>
        </ul>
        <p class="soft">İngiltere’de 4.943 hastanın yanıtladığı bir araştırmada, yoğun bakımdan 3 ya da 12 ay sonra katılımcıların %46’sında kaygı, %40’ında depresyon, %22’sinde travma sonrası stres belirtileri vardı. Bu belirtilerden birini yaşayanların üçte ikisinde diğerlerinden en az biri de görülüyordu.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>İyileşmeyi neler destekler?</h2>
      <p class="soft">İngiltere’nin ulusal kılavuzu (NICE), yoğun bakım sonrası risk altındaki her hastaya erken başlayan, kişiye özel ve sık gözden geçirilen bir rehabilitasyon programı öneriyor. Kılavuza göre hastalara olası bedensel ve ruhsal sorunlar hakkında bilgi verilmeli, yoğun bakımdan çıktıktan sonra en az 6 hafta süren, desteklenen bir kendi kendine rehabilitasyon kitapçığı düşünülmeli ve taburculuktan 2–3 ay sonra yüz yüze bir işlevsel değerlendirme yapılmalı. İyileşme beklenenden yavaşsa ya da yeni sorunlar ortaya çıktıysa uzmana yönlendirme öneriliyor.</p>
      <ul class="tx">
        <li><b>Kademeli hareket</b><span>Fizyoterapi ekibinizin verdiği programı sürdürün; yıkanma ve giyinme gibi kendi bakımınızda etkin rol alın. Hareketi her gün biraz artırın, yorulduğunuzda dinlenin.</span></li>
        <li><b>Beslenme</b><span>Öğün aralarında 2–3 ara öğün, enerjisi ve proteini yüksek yiyecekler ve günde 6–8 bardak sıvı.</span></li>
        <li><b>Düzen</b><span>Düzenli bir günlük program, hareket, dengeli öğünler ve düzenli uyku. Gündüz dinlenin ama uzun gündüz uykularından kaçının.</span></li>
        <li><b>Konuşmak ve yazmak</b><span>Yaşadıklarınızı yakınlarınızla konuşmak ve kaygılarınızı bir deftere yazmak, uykuya da yardım edebilir.</span></li>
        <li><b>İşe dönüş</b><span>Kısaltılmış saatler ya da daha hafif görevlerle, kademeli olarak.</span></li>
      </ul>
      <div class="callout">
        <p>Egzersizin yoğun bakım sonrası iyileşmeye etkisi konusunda kanıt henüz sınırlı: 6 çalışmayı inceleyen Cochrane derlemesi, kanıtın kalitesi çok düşük olduğu için kesin bir sonuca varamadı. Yine de ulusal kılavuzlar, hareketi ve rehabilitasyonu iyileşmenin temel parçası olarak görüyor.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Yoğun bakım sonrası altı hafif egzersiz</h2>
      <p class="soft">Bu hareketler, eve döndükten sonraki ilk haftalar için hafif örneklerdir; size verilen rehabilitasyon programı önceliklidir. Yanınızda biri varken başlayın, yorgunluğunuza göre tekrar sayısını azaltın ve her gün biraz artırın.</p>
      {ex_grid(["yb_breath", "yb_apump", "yb_quad", "yb_kext", "yb_sts", "yb_walk"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(YB_FAQ)}
      <p class="soft" style="margin-top:18px">Nefes ve gevşeme için <a href="ic-cekis.html">iç çekiş nefesine</a>, kas kaybı için <a href="sarkopeni.html">sarkopeni</a> rehberine, ilerlemenizi ölçmek için <a href="alti-dakika-yurume-testi.html">6 dakika yürüme testine</a> bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">“Acil” yazan durumlarda 112’yi arayın:</p>
      <ul class="dots redflags">
        <li>Göğüs ağrısı ya da ani başlayan, giderek artan nefes darlığı (acil)</li>
        <li>Bilinç bulanıklığı, aşırı uyku hâli ya da konuşma bozukluğu (acil)</li>
        <li>Kendinize zarar verme ya da yaşamınıza son verme düşünceleri (acil)</li>
        <li>Belirgin kötüleşme, ateş, yeni ağrı ya da şişlik: aynı gün hekiminize</li>
        <li>Eve döndükten bir ay sonra hâlâ belirgin kaygı, karamsarlık, uykusuzluk ya da kâbuslar</li>
      </ul>
      {CTA_CARD("Yoğun bakım sonrası rehabilitasyonunuz", "yoğun bakım sonrası rehabilitasyon")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(YB_SRC)}
    </div>
  </section>
</main>'''

page("yogun-bakim-sonrasi.html", "Yoğun Bakım Sonrası İyileşme",
     "Yoğun bakım sonrası güçsüzlük, yorgunluk, kâbuslar ve kaygı: neler beklenir, iyileşmeyi neler destekler, ne zaman başvurmalı ve evde altı hafif egzersiz.",
     "yogun-bakim-sonrasi.html", NECK_CSS, YB_BODY, "",
     seo_title="Yoğun Bakım Sonrası İyileşme: Güçsüzlük, Ruh Hâli ve Ev Egzersizleri | İhsan Eren",
     condition="Yoğun bakım sonrası iyileşme", faq_items=YB_FAQ)

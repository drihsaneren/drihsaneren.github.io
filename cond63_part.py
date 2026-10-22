# -*- coding: utf-8 -*-
# Yeni rehber (63): Pelvik organ sarkması (rahim, mesane ya da bağırsak sarkması). cond62_part.py'den sonra exec edilir. Video yok.
# Kaynaklar (22 Ekim 2026'da okundu): NICE NG123 öneriler (1.7–1.8), Hagen 2014 POPPY (PEDro özeti + Aberdeen deposundaki tam metin), Hagen & Stark Cochrane
# (cochrane.org sade dil özeti), NHS POP tedavi sayfası (3 Temmuz 2025), NHS 111 Wales POP (8 Nisan 2025), Cambridge University Hospitals broşürü (v5, Temmuz 2024),
# Manchester (Saint Mary's) SMPIL-24-036 (Aralık 2023), Kearney 2024 TOPSY özeti (UroToday).

_ex2("po_slow", "pf_lie", "Uzun kasılma", "Sırtüstü yatın, dizleriniz bükülü olsun. Gaz ve idrarı aynı anda tutuyormuş gibi pelvik taban kaslarınızı içe ve yukarı çekin, gücünüzün yettiğince sıkıp tutun, sonra tamamen gevşeyin. Nefesinizi tutmayın; kalçanızı ve karnınızı sıkmayın.", "Hedef: 10 saniyelik 10 kasılma, günde 3 kez")
_ex2("po_fast", "pf_sit", "Hızlı kasılma", "Dik oturun. Aynı kasları hızla sıkın ve hemen bırakın. Hızlı kasılmalar, öksürük ya da hapşırık gibi ani yüklenmelerde kasların çabuk devreye girmesine yardım eder.", "Hedef: 50’ye kadar hızlı kasılma, günde 3 kez")
_ex2("po_stand", "pf_stand", "Ayakta kasılma", "Yatarak ve oturarak rahatça yapabildiğinizde kasılmaları ayakta da deneyin. Bulaşık yıkarken ya da sıra beklerken yapabilirsiniz.", "Uzun ve hızlı kasılmalar, günde 3 kez")
_ex2("po_knack", "knack", "Zorlanmadan önce sıkma", "Öksürmeden, hapşırmadan, gülmeden ya da bir şey kaldırmadan hemen önce pelvik taban kaslarınızı sıkın ve hareket bitene kadar tutun. Karın içi basıncın arttığı anlarda kasların destek vermesini sağlar.", "Her zorlanmadan önce")
_ex2("po_lift", "hinge", "Kaldırırken korunma", "Kaldırmanız gereken bir şey varsa önce pelvik tabanınızı sıkın, yükü bedeninize yakın tutun, nefesinizi tutmayın; kaldırırken nefes verin. Ağır yükleri hafif parçalara bölüp birkaç seferde taşıyın.", "Her kaldırmada")
_ex2("po_walk", "walk", "Düşük darbeli egzersiz", "Koşu, zıplama ve trambolin gibi iki ayağın birden yerden kesildiği etkinlikler yerine tempolu yürüyüş, bisiklet, yüzme, pilates ya da eliptik bisiklet gibi daha düşük darbeli egzersizleri seçebilirsiniz.", "Haftanın çoğu günü")

PO_FAQ = [
 ("Pelvik taban egzersizleri sarkmayı geçirir mi?", "Belirtileri azaltabilir. Birleşik Krallık, Yeni Zelanda ve Avustralya’da 447 kadınla yapılan POPPY çalışmasında, 16 hafta boyunca bir fizyoterapistle 5 seans pelvik taban egzersizi çalışan kadınların sarkma belirtileri, yalnızca bilgilendirme broşürü alanlara göre daha çok azaldı. 12. ayda sarkmalarının daha iyi olduğunu söyleyenler egzersiz grubunda %57, broşür grubunda %45’ti. Fark anlamlı ama ılımlıydı. Cochrane derlemesinde de pelvik taban egzersizi, sarkma evresinin iyileşme olasılığını egzersiz yapmayanlara göre %17 artırdı."),
 ("Egzersize ne kadar süre devam etmeliyim?", "NICE, evre 1–2 sarkmada ilk seçenek olarak en az 16 hafta süren gözetimli pelvik taban egzersizi öneriyor ve program yarar sağlıyorsa sonrasında da sürdürülmesini istiyor. Kasların güçlenmesi zaman alır; ilk haftalarda fark görmeseniz de düzenli devam edin."),
 ("Pesser nedir, kimler için uygun?", "Pesser, hazneye yerleştirilen ve organları destekleyen plastik ya da silikon bir halkadır. NICE, belirti veren sarkmada tek başına ya da pelvik taban egzersizleriyle birlikte düşünülebileceğini söylüyor. Doğru boyutu bulmak için birden fazla deneme gerekebilir ve pesser en az 6 ayda bir çıkarılmalıdır. 340 kadınla yapılan TOPSY çalışmasında, pesserini kendi takıp çıkarmayı öğrenen kadınların yaşam kalitesi klinikte bakım alanlarla benzerdi ve daha az sorun bildirdiler."),
 ("Ameliyat gerekir mi?", "Belirtileri ameliyatsız tedavilerle düzelmeyen ya da bu tedavileri istemeyen kadınlara ameliyat önerilebilir. Karar; seçenekler, beklenen yararlar, riskler ve sarkmanın yeniden olma olasılığı konuşularak hekiminizle birlikte verilebilir. İngiltere’nin ulusal sağlık hizmetinde (NHS) hazne içine file (mesh) yerleştirilen ameliyatlar, başka seçenek kalmadıkça artık yapılmıyor."),
 ("Spor yapabilir miyim?", "Evet, hareketli kalmak önemli. Pelvik taban kaslarınız zayıfsa koşu, zıplama ve trambolin gibi yüksek darbeli etkinlikler belirtileri artırabilir; tempolu yürüyüş, bisiklet, yüzme ve pilates gibi daha düşük darbeli egzersizler iyi seçeneklerdir. Ağır kaldırmayı mümkün olduğunca azaltın."),
 ("Menopozdan sonra neden arttı?", "Yaşlanma ve menopoz, sarkmanın risk etkenleri arasındadır. Menopoza bağlı hazne kuruluğu ve tahrişi gibi belirtileri olan kadınlara hazne içine uygulanan östrojen kremi, tableti ya da halkası önerilebilir; pesser kullanmadan önce de düşünülebilir. Bu konuyu hekiminizle konuşabilirsiniz."),
]

PO_SRC = [
 "National Institute for Health and Care Excellence. " + ext("https://www.nice.org.uk/guidance/ng123/chapter/Recommendations", "Urinary incontinence and pelvic organ prolapse in women: management") + ". NICE guideline NG123, 2019.",
 "Hagen S, Stark D, Glazener C, et al. " + ext("https://doi.org/10.1016/S0140-6736(13)61977-7", "Individualised pelvic floor muscle training in women with pelvic organ prolapse (POPPY): a multicentre randomised controlled trial") + ". Lancet. 2014;383(9919):796–806.",
 "Hagen S, Stark D. " + ext("https://www.cochrane.org/evidence/CD003882_conservative-management-pelvic-organ-prolapse-women", "Conservative prevention and management of pelvic organ prolapse in women") + ". Cochrane Database Syst Rev. 2011;(12):CD003882.",
 "Kearney R, Hagen S, Bugge C. " + ext("https://doi.org/10.1016/j.ogrm.2024.05.004", "Self-management of vaginal pessaries for prolapse: the TOPSY trial key findings") + ". Obstet Gynaecol Reprod Med. 2024;34(8):229–231.",
 "NHS. " + ext("https://www.nhs.uk/conditions/pelvic-organ-prolapse/treatment/", "Pelvic organ prolapse: treatment") + ". Page last reviewed 3 July 2025.",
 "NHS 111 Wales. " + ext("https://111.wales.nhs.uk/Pelvicorganprolapse", "Pelvic organ prolapse") + ". Last updated 8 April 2025.",
 "Cambridge University Hospitals NHS Foundation Trust, Physiotherapy. " + ext("https://www.cuh.nhs.uk/patient-information/pelvic-organ-prolapse-pop/", "Pelvic organ prolapse (POP)") + ". Document 100927, version 5, July 2024.",
 "Manchester University NHS Foundation Trust, Saint Mary’s Managed Clinical Service. " + ext("https://mft.nhs.uk/app/uploads/sites/4/2024/04/SMPIL-24-036-Prolapse-pelvic-organ.pdf", "Pelvic organ prolapse") + ". SMPIL-24-036, December 2023.",
]

PO_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Pelvik organ sarkması (rahim, mesane ya da bağırsak sarkması)</h1>
    <p class="lede">Kasıkta ağırlık, haznede bir şeyin aşağı doğru indiği ya da küçük bir topun üzerinde oturuyormuş gibi bir his mi var? Rahim, mesane ya da bağırsak normal yerinden aşağı kayarak hazne (vajina) duvarına doğru sarkabilir. Çok sık görülür ve hayatı tehdit etmez. Hafif ve orta sarkmada ilk tedavi seçeneği, bir fizyoterapist eşliğinde en az 16 hafta sürdürülen pelvik taban egzersizleridir; günlük alışkanlıklardaki küçük değişiklikler de belirtileri azaltabilir.</p>
    <p class="meta">Son güncelleme: 22 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%40</b><span>Dünyada yaşamının bir döneminde pelvik organ sarkması yaşayacak kadınların yaklaşık oranı</span></div>
        <div class="stat"><b>16 hafta</b><span>Evre 1–2 sarkmada ilk seçenek olan gözetimli pelvik taban egzersizinin en kısa süresi (NICE)</span></div>
        <div class="stat"><b>%57’ye karşı %45</b><span>12. ayda sarkmasının daha iyi olduğunu söyleyen kadınlar: egzersiz ve broşür grubu (POPPY)</span></div>
        <div class="stat"><b>Günde 3 kez</b><span>POPPY’de evde hedeflenen egzersiz sıklığı</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Kasıkta ya da cinsel bölgede ağırlık hissi.</li>
          <li>Haznede çekilme, aşağı doğru inme hissi; küçük bir topun üzerinde oturuyormuş gibi olma.</li>
          <li>Haznede görülen ya da elle hissedilen bir kabarıklık.</li>
          <li>İdrarı tam boşaltamama, sık idrara çıkma, öksürürken ya da hapşırırken idrar kaçırma.</li>
          <li>Bağırsağı tam boşaltamama.</li>
          <li>Cinsel ilişkide rahatsızlık ya da uyuşukluk.</li>
        </ul>
        <p class="soft">Bazı kadınlarda hiçbir belirti yoktur; sarkma başka bir nedenle yapılan muayenede fark edilir.</p>
      </div>
      <div>
        <h2>Türleri ve nedenleri</h2>
        <ul class="dots">
          <li><b>Ön duvar sarkması:</b> mesane haznenin ön duvarına doğru sarkar.</li>
          <li><b>Arka duvar sarkması:</b> bağırsak haznenin arka duvarına doğru sarkar.</li>
          <li><b>Rahim sarkması:</b> rahim hazneye doğru iner.</li>
          <li><b>Kubbe sarkması:</b> rahim alındıktan sonra haznenin üst kısmı aşağı iner.</li>
        </ul>
        <p class="soft">Bunlar birlikte de görülebilir; şiddeti genellikle 1’den (hafif) 4’e (ağır) kadar evrelendirilir. Gebelik ve doğum (özellikle uzun ya da zor doğum, iri bebek, çoğul doğum), yaşlanma ve menopoz, fazla kilo, uzun süreli kabızlık ya da öksürük, rahim alınması ve ağır kaldırma gerektiren işler riski artırır. Eklem hipermobilitesi gibi bağ dokusunu etkileyen durumlar da riski artırabilir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Günlük hayatta neler yapabilirsiniz?</h2>
      <ul class="tx">
        <li><b>Kabızlığı önleyin</b><span>Bol sebze, meyve ve lifli gıda yiyin, günde 1,5–2 litre sıvı için. Tuvalette ayaklarınızı bir taburenin üzerine koyun ki dizleriniz kalçanızdan yüksekte olsun; dirseklerinizi dizlerinize dayayın, nefes verin ve ıkınmayın.</span></li>
        <li><b>Mesanenizi acele etmeden boşaltın</b><span>İdrarınızı yaparken ıkınmayın; tam boşaltmak için birkaç kez hafifçe öne eğilebilirsiniz.</span></li>
        <li><b>Ağır kaldırmayı azaltın</b><span>Yükleri hafif parçalara bölün, birkaç seferde taşıyın; tekrar tekrar yapılan kaldırma işlerinin sıklığını da düşünün.</span></li>
        <li><b>Sağlıklı kiloya yaklaşın</b><span>Fazla kilo pelvik tabana binen yükü artırır. NICE, beden kitle indeksi 30’un üzerindeyse kilo vermeyi öneriyor.</span></li>
        <li><b>Öksürüğü tedavi ettirin, sigarayı bırakın</b><span>Uzun süren öksürük pelvik tabanı tekrar tekrar zorlar; sigarayı bırakmak öksürük riskini azaltır.</span></li>
        <li><b>Uzun süre ayakta kalmayı bölün</b><span>Gün içinde ara ara oturarak dinlenin.</span></li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Araştırmalar ne gösteriyor?</h2>
      <p class="soft">En büyük çalışma olan POPPY’de, yeni tanı almış ve belirtisi olan evre 1–3 sarkması bulunan 447 kadın iki gruba ayrıldı. Bir gruba 16 hafta içinde 5 seans kişiye özel pelvik taban egzersizi öğretildi; evde günde 3 kez, 10 saniyelik 10 kasılma ve 50’ye kadar hızlı kasılma hedeflendi, zorlanma anlarından önce kasları sıkma alışkanlığı (“püf noktası”) da çalışıldı. Diğer gruba yalnızca yaşam tarzı broşürü verildi. 12. ayda egzersiz grubunda sarkma belirti puanı daha çok azaldı (ortalama 3,77’ye karşı 2,09 puan) ve sarkmasının daha iyi olduğunu söyleyenler %57’ye karşı %45’ti.</p>
      <p class="soft">Cochrane derlemesinde pelvik taban egzersizini hiçbir şey yapmamakla karşılaştıran dört çalışma (857 kadın) vardı. Belirtileri bildiren çalışmaların hepsi egzersizi destekledi; iki çalışmanın birleşik sonucuna göre egzersiz, sarkma evresinin iyileşme olasılığını %17 artırdı. Çalışmaların bazıları küçüktü ve yanlılık riski taşıyordu.</p>
      <div class="callout">
        <p>Pelvik taban kaslarını doğru çalıştırmak ilk başta kolay değildir. Kasları hissedemiyorsanız ya da egzersizler belirtilerinizi artırıyorsa pelvik sağlık alanında çalışan bir fizyoterapistten değerlendirme isteyebilirsiniz.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Pelvik taban için altı uygulama</h2>
      <p class="soft">İlk dört uygulamanın hedef dozları POPPY çalışmasındaki ev programından alındı. Başta daha azıyla başlamanız normaldir; tutabildiğiniz kadar tutun ve haftalar içinde artırın. Saniye saniye eşlik eden bir araç için <a href="pelvik-taban-zamanlayicisi.html">pelvik taban zamanlayıcısını</a> kullanabilirsiniz.</p>
      {ex_grid(["po_slow", "po_fast", "po_stand", "po_knack", "po_lift", "po_walk"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(PO_FAQ)}
      <p class="soft" style="margin-top:18px">Öksürürken ya da sıkışınca idrar kaçırma için <a href="idrar-kacirma.html">idrar kaçırma</a>, doğum sonrası karın kasları için <a href="karin-kasi-ayrilmasi.html">karın kası ayrılması</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Sarkma belirtileri fark ettiğinizde ya da haznede ya da çevresinde bir kabarıklık hissettiğinizde</li>
        <li>İdrarınızı ya da dışkınızı tam boşaltamıyorsanız</li>
        <li>Pesser kullanırken kanama, alışılmadık akıntı ya da ağrı olursa</li>
        <li>Birkaç ay düzenli egzersize rağmen belirtileriniz günlük hayatınızı kısıtlamaya devam ediyorsa</li>
      </ul>
      <p class="soft">Hazneden beklenmedik kanama, özellikle menopozdan sonra, sarkmayla açıklanmamalı ve hekim tarafından değerlendirilmelidir.</p>
      {CTA_CARD("Pelvik organ sarkmasında pelvik taban egzersizleriniz", "pelvik organ sarkması için pelvik taban egzersizleri")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(PO_SRC)}
    </div>
  </section>
</main>'''

page("pelvik-organ-sarkmasi.html", "Pelvik Organ Sarkması: Rahim, Mesane ya da Bağırsak Sarkması",
     "Haznede ağırlık ya da aşağı inme hissi: pelvik organ sarkmasının belirtileri, türleri, pelvik taban egzersizleri, pesser, günlük öneriler ve araştırmaların söyledikleri.",
     "pelvik-organ-sarkmasi.html", NECK_CSS, PO_BODY, "",
     seo_title="Pelvik Organ Sarkması (Rahim Sarkması): Belirtiler ve Pelvik Taban Egzersizleri | İhsan Eren",
     condition="Pelvik organ sarkması", faq_items=PO_FAQ)

# -*- coding: utf-8 -*-
# Yeni rehber (20): bel kayması (spondilolistezis). cond19_part.py'den sonra exec edilir. Video yok.

_ex2("sl_ptilt", "ptilt", "Pelvis tilti", "Sırtüstü yatın, dizleriniz bükülü, ayaklarınız yerde olsun. Karın kaslarınızı hafifçe sıkarak belinizi yere doğru bastırın, 5 saniye tutun ve gevşeyin. Hareket küçük ve ağrısız olsun.", "10 tekrar, günde 1–2 kez")
_ex2("sl_k2c", "k2c", "Dizi göğse çekme", "Sırtüstü yatın. Bir dizinizi iki elinizle göğsünüze doğru yavaşça çekin, belinizin hafifçe esnediğini hissedin; 20 saniye tutun. Sonra diğer bacakla, ardından iki dizle birlikte yapın.", "Her biri 20 saniye, 3 tekrar")
_ex2("sl_bridge", "bridge", "Köprü", "Sırtüstü yatın, dizleriniz bükülü. Karnınızı hafifçe sıkıp kalçanızı omuzlarınızdan dizlerinize düz bir çizgi oluşana kadar kaldırın; belinizi fazla yukarı itmeyin. 3–5 saniye tutup yavaşça inin.", "10 tekrar, 2 set")
_ex2("sl_birddog", "birddog", "Kuş-köpek", "Ellerinizin ve dizlerinizin üzerinde durun, sırtınız düz olsun. Bir kolunuzu öne, karşı bacağınızı arkaya uzatın; belinizi çukurlaştırmadan ve kalçanızı döndürmeden 5 saniye tutun. Taraf değiştirin.", "Her tarafa 8 tekrar")
_ex2("sl_side", "sideplank", "Dizler üzerinde yan köprü", "Yan yatın, dizleriniz bükülü, dirseğiniz omzunuzun altında olsun. Kalçanızı kaldırarak başınızdan dizlerinize düz bir çizgi oluşturun, 10 saniye tutun. Kolaylaşınca süreyi artırın.", "Her tarafa 5 tekrar")
_ex2("sl_walk", "walk", "Yürüyüş", "Rahat bir tempoda, düz zeminde yürüyün. Uzun yürüyüşte bacak ağrısı başlıyorsa kısa molalar verin. Süreyi yavaş yavaş artırın.", "Günde 10–30 dakika")

SL_FAQ = [
 ("Bel kayması geçer mi, düzelir mi?", "Kayan omur genellikle yerine geri gitmez; ancak çoğu kişide kayma zamanla ilerlemez ve belirtiler ameliyatsız tedaviyle azalır. Hafif kaymalar hiç belirti vermeyebilir; birçok kişi bunu başka bir nedenle çekilen röntgende öğrenir."),
 ("Egzersiz yapmak kaymayı artırır mı?", "Gövdeyi ve karın kaslarını güçlendiren egzersizler tedavinin temel parçasıdır. Ağrınızı belirgin biçimde artıran hareketleri bir süre bırakın ve programınızı bir fizyoterapistle planlayın."),
 ("Korse kullanmalı mıyım?", "Korse genellikle omurda bir çatlak (kırık) olduğunda önerilir. Hekiminiz önermediyse kullanmanız gerekmez; gövde kaslarını egzersizle güçlendirmek tedavinin temelidir."),
 ("Ameliyatta vida (füzyon) şart mı?", "Yürürken bacak ağrısına yol açan dar kanalla birlikte hafif bel kayması olan hastalarda yapılan bir İsveç çalışmasında, sinirleri rahatlatan ameliyata vidalı sabitleme (füzyon) eklemek 2 yılda daha iyi sonuç vermedi; hastanede kalış ve maliyet ise arttı. Hangi ameliyatın uygun olduğuna, kaymanın derecesine ve kararlılığına bakılarak cerrahınızla birlikte karar verilir."),
]

SL_SRC = [
 "Cleveland Clinic. " + ext("https://my.clevelandclinic.org/health/diseases/10302-spondylolisthesis", "Spondylolisthesis") + ". Medically reviewed 15 August 2024.",
 "Moley PJ. " + ext("https://www.msdmanuals.com/professional/musculoskeletal-and-connective-tissue-disorders/neck-and-back-pain/spondylolisthesis", "Spondylolisthesis") + ". MSD Manual Professional Version. Reviewed November 2024.",
 "Försth P, Ólafsson G, Carlsson T, et al. A randomized, controlled trial of fusion surgery for lumbar spinal stenosis. N Engl J Med. 2016;374(15):1413–1423. Özet: " + ext("https://www.thebottomline.org.uk/summaries/ssss/", "The Bottom Line, The Swedish Spinal Stenosis Study") + ".",
]

SL_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Bel kayması (spondilolistezis)</h1>
    <p class="lede">Bel kayması, bir omurun alttaki omura göre öne doğru kaymasıdır; en sık belin en alt seviyesinde görülür. Çoğu zaman hafiftir ve hiç belirti vermeyebilir. Ağrı olduğunda tedavinin temeli ameliyatsız yöntemler ve gövdeyi güçlendiren egzersizlerdir; ameliyat ileri kaymalarda ya da geçmeyen sinir belirtilerinde gündeme gelir.</p>
    <p class="meta">Son güncelleme: 11 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>L5–S1</b><span>En sık kaymanın görüldüğü seviye: belin en alt omuru ile kuyruk sokumu arası</span></div>
        <div class="stat"><b>4 derece</b><span>Kayma miktarına göre: I. derece %0–25, IV. derece %75–100</span></div>
        <div class="stat"><b>6 kat</b><span>Yaşa bağlı (dejeneratif) kaymanın kadınlarda erkeklere göre sıklığı</span></div>
        <div class="stat"><b>247 hasta</b><span>Ameliyata vida eklemenin yararını sınayan İsveç çalışması; 2 yılda fark yoktu</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Neden olur?</h2>
        <ul class="tx">
          <li><b>Yaşa bağlı (dejeneratif)</b><span>En sık türdür. Omurlar arasındaki disklerin ve eklemlerin yıpranmasıyla ortaya çıkar; genellikle 50–60 yaşın üzerinde ve kadınlarda görülür.</span></li>
          <li><b>İstmik</b><span>Omurun arka kısmındaki ince kemik köprüde (pars interartikülaris) yorgunluk çatlağı oluşur ve omur kayar. Daha çok gençlerde ve sporcularda, tekrarlayan zorlanmaya bağlı görülür.</span></li>
          <li><b>Diğerleri</b><span>Doğuştan omur gelişim farkı, kaza ya da düşme, kemiği zayıflatan hastalıklar ve nadiren omurga ameliyatı sonrası.</span></li>
        </ul>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Çoğu zaman hiç belirti yoktur</li>
          <li>Bel ağrısı ve tutukluk</li>
          <li>Kalçaya ya da uyluğa yayılan ağrı</li>
          <li>Bacağa yayılan ağrı (siyatik)</li>
          <li>Uzun süre ayakta durmakta ya da yürümekte zorlanma</li>
          <li>Ayaklarda uyuşma, karıncalanma ya da güçsüzlük</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tanı ve dereceler</h2>
      <p class="soft">Tanı muayene ve röntgenle konur; kaymanın derecesi yandan çekilen filmde ölçülür. Öne ve arkaya eğilerek çekilen filmler kaymanın hareketle artıp artmadığını gösterir. Sinir sıkışması düşünülüyorsa MR ya da tomografi istenebilir.</p>
      <ul class="tx">
        <li><b>I. derece</b><span>Omur, alttaki omurun boyunun %25'ine kadar kaymış. En sık görülen ve çoğu zaman ameliyat gerektirmeyen derece.</span></li>
        <li><b>II. derece</b><span>%25–50 arası kayma.</span></li>
        <li><b>III. derece</b><span>%50–75 arası kayma.</span></li>
        <li><b>IV. derece</b><span>%75–100 arası kayma. III ve IV. derecede ameliyat olasılığı çok daha yüksektir.</span></li>
      </ul>
      <div class="callout">
        <p>Bel kayması genellikle zamanla ilerlemeyen, kararlı bir durumdur. Röntgende kayma görülmesi, ağrının tek nedeninin bu olduğu anlamına gelmez; belirtilerle birlikte değerlendirilir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Ameliyatsız tedavi</h2>
        <ul class="tx">
          <li><b>Etkinliği düzenlemek</b><span>Ağrıyı artıran sporlara ve yoğun etkinliklere bir süre ara vermek.</span></li>
          <li><b>Fizyoterapi ve egzersiz</b><span>Gövde ve karın kaslarını güçlendiren, beli dengeleyen egzersizler tedavinin temelidir.</span></li>
          <li><b>Ağrı kesiciler</b><span>Reçetesiz ağrı kesicileri hekime danışmadan 10 günden uzun süre üst üste kullanmayın.</span></li>
          <li><b>İğne</b><span>Bacağa yayılan ağrıda kortizonlu enjeksiyon seçenekler arasındadır.</span></li>
          <li><b>Korse</b><span>Genellikle omurda bir çatlak (kırık) varsa.</span></li>
        </ul>
      </div>
      <div>
        <h2>Ameliyat ne zaman?</h2>
        <ul class="dots">
          <li>III ya da IV. derece (ileri) kayma</li>
          <li>Ayakta durmayı ve yürümeyi belirgin biçimde kısıtlayan şiddetli belirtiler</li>
          <li>Ameliyatsız tedaviye rağmen geçmeyen belirtiler</li>
          <li>İlerleyen güçsüzlük ya da idrar ve dışkı kontrolünde bozulma</li>
        </ul>
        <p class="soft">İsveç'te 247 hastayla yapılan çalışmada, dar kanal nedeniyle ameliyat edilen hastalarda (bir kısmında hafif bel kayması vardı) sinirleri rahatlatan ameliyata vidalı sabitleme eklemek 2 yılda daha iyi sonuç vermedi; hastanede kalış 4,1 günden 7,4 güne uzadı ve maliyet arttı. <a href="dar-kanal.html">Dar kanal rehberine</a> de bakın.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Beli destekleyen altı egzersiz</h2>
      <p class="soft">Amaç, gövdeyi ve karın kaslarını güçlendirip beli dengede tutmaktır. Hareketleri yavaş ve ağrısız bir aralıkta yapın. Beli geriye doğru zorlayan hareketler ağrınızı artırıyorsa bir süre bunlardan kaçının. Belirtileriniz yeni başladıysa ya da bacağınızda uyuşma ve güçsüzlük varsa önce bir hekime ya da fizyoterapiste danışın.</p>
      {ex_grid(["sl_ptilt", "sl_k2c", "sl_bridge", "sl_birddog", "sl_side", "sl_walk"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(SL_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden acil servise başvurun:</p>
      <ul class="dots redflags">
        <li>İdrar ya da dışkı kontrolünde bozulma, idrar yapamama</li>
        <li>Kasıklarda ya da makat çevresinde uyuşma</li>
        <li>Bacaklarda hızla artan güçsüzlük ya da his kaybı</li>
        <li>Düşme ya da kaza sonrası başlayan şiddetli bel ağrısı</li>
      </ul>
      {CTA_CARD("Bel kayması ve bel ağrınız", "bel kayması (spondilolistezis)")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(SL_SRC)}
    </div>
  </section>
</main>'''

page("bel-kaymasi.html", "Bel Kayması (Spondilolistezis)",
     "Bel kayması nedir, neden olur, dereceleri nelerdir? Belirtiler, röntgende tanı, ameliyatsız tedavi, ameliyatın ne zaman gerektiği ve beli destekleyen altı egzersiz.",
     "bel-kaymasi.html", NECK_CSS, SL_BODY, "",
     seo_title="Bel Kayması (Spondilolistezis): Belirtiler, Dereceler, Egzersiz ve Tedavi | İhsan Eren",
     condition="Spondilolistezis (bel kayması)", faq_items=SL_FAQ)

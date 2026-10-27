# -*- coding: utf-8 -*-
# Yeni rehber (32): Ganglion kisti (el bileği kisti). cond31_part.py'den sonra exec edilir. Video yok.
# Egzersizler hazır çizimlerle; kisti küçülttüğüne dair kanıt olmadığı sayfada açıkça yazıyor.

_ex2("gg_wrist", "dq_wrist", "Bileği aşağı yukarı hareket ettirme", "Ön kolunuzu masaya koyun, eliniz masanın kenarından taşsın. Elinizde ağırlık olmadan bileğinizi rahatça yapabildiğiniz kadar yukarı kaldırın, sonra aşağı indirin. Kisti belirgin ağrıtan noktaya kadar zorlamayın.", "Her yöne 10 tekrar, günde 2–3 kez")
_ex2("gg_rot", "ge_rot", "Ön kolu içe-dışa çevirme", "Ön kolunuz masada dursun. Elinizin sırtı masadayken başlayın, sonra avucunuz aşağı bakacak şekilde yavaşça çevirin ve geri dönün. Ağırlık kullanmanız gerekmez.", "10 tekrar, günde 2–3 kez")

GG_FAQ = [
 ("Ganglion kisti kendiliğinden geçer mi?", "Çoğu zaman evet. Birçok kist tedavi gerekmeden kaybolur; bu birkaç aydan bir yıla kadar sürebilir. Ağrı, uyuşma ya da kaygı yaratmıyorsa genellikle tedavi önerilmez. 236 hastanın ortalama 6 yıl izlendiği bir çalışmada, tedavi edilmeyen bilek kistlerinin %58’i kendiliğinden kayboldu; kist boşaltılanların %58’inde, ameliyatla alınanların %39’unda yeniden oluştu ve uzun dönemde iki tedavi de belirtiler açısından tedavisiz izlemeye üstün değildi."),
 ("Kisti kitapla vurarak ya da bastırarak patlatabilir miyim?", "Hayır. Kisti kendiniz patlatmaya çalışmak enfeksiyona ve cilt hasarına yol açabilir."),
 ("İğneyle boşaltmak işe yarar mı?", "Kistlerin bir kısmı boşaltmayla geçer, ama bilekteki kistlerin çoğu yeniden dolar; yeniden dolan kist ağrısız olabilir. Bileğin iç yüzündeki kistler nabız alınan atardamara yakın olabildiği için boşaltma dikkat gerektirir."),
 ("Ameliyattan sonra tekrarlar mı?", "Tekrarlayabilir. El cerrahları derneğinin bilgilendirmesine göre bileğin sırtındaki kistlerde ameliyat sonrası tekrarlama yaklaşık %10, bileğin iç yüzündekilerde yaklaşık %30. Ameliyat sonrası bilek ve el işlevi 4–6 hafta kadar kısıtlı kalabilir; iz, ağrı ve hareket kaybı gibi riskler de vardır."),
]

GG_SRC = [
 "NHS. " + ext("https://www.nhs.uk/conditions/ganglion-cyst/", "Ganglion cyst") + ". Page last reviewed 16 July 2025.",
 "Academy of Medical Royal Colleges. " + ext("https://ebi.aomrc.org.uk/interventions/ganglion-excision/", "Evidence-Based Interventions: Ganglion excision") + ". Last reviewed September 2024.",
 "Lyon C, Eldred SV, DeSanto K. " + ext("https://mdedge.com/content/what-best-treatment-wrist-ganglion-cysts", "What is the best treatment for wrist ganglion cysts?") + ". J Fam Pract. 2020;69(1):E23–E24",
 "British Society for Surgery of the Hand. " + ext("https://apps.nhslothian.scot/files/sites/2/ganglion_cyst_leaflet-2016-BSSH.pdf", "Ganglion cyst") + ". Patient information leaflet, 2016.",
 "Dias JJ, Dhukaram V, Kumar P. " + ext("https://www.qxmd.com/r/17950209", "The natural history of untreated dorsal wrist ganglia and patient reported outcome 6 years after intervention") + ". J Hand Surg Eur Vol. 2007;32(5):502–508.",
]

GG_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Ganglion kisti (el bileği kisti)</h1>
    <p class="lede">Ganglion kisti, çoğunlukla el bileğinde ya da elde, bir eklemin ya da kiriş kılıfının yanında beliren, içi sıvı dolu yumuşak bir şişliktir. Görünümü kaygı verebilir, ama zararsızdır ve çoğu zaman kendiliğinden kaybolur. Ağrı, uyuşma ya da elinizi kullanmanızı kısıtlamıyorsa genellikle tedavi gerekmez.</p>
    <p class="meta">Son güncelleme: 27 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>Aylar – 1 yıl</b><span>Çoğu kistin tedavi gerekmeden kaybolabileceği süre</span></div>
        <div class="stat"><b>Kadınlarda</b><span>Erkeklere göre çok daha sık görülür</span></div>
        <div class="stat"><b>%30</b><span>Bilek kistlerinde iğneyle boşaltmanın kalıcı sonuç verdiği oran; çoğu yeniden dolar</span></div>
        <div class="stat"><b>%10–30</b><span>Ameliyattan sonra tekrarlama oranı; kistin yerine göre değişir</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Deri altında, bezelyeden küçükten birkaç santimetreye kadar değişen, düzgün ve yumuşak bir şişlik.</li>
          <li>Çoğu zaman ağrısızdır; yakındaki eklemi hareket ettirirken ya da sonrasında ağrıyabilir.</li>
          <li>Bazen hareketten sonra uyuşma ya da sızı.</li>
        </ul>
      </div>
      <div>
        <h2>Nerede olur?</h2>
        <ul class="dots">
          <li><b>Bileğin sırtı:</b> En sık yerdir; genellikle genç yetişkinlerde görülür.</li>
          <li><b>Bileğin iç yüzü:</b> Başparmak kökünde, nabız alınan atardamara yakın.</li>
          <li><b>Parmak kökü:</b> Avuç tarafında, kiriş kılıfından çıkan küçük bir kist.</li>
          <li><b>Parmak ucundaki eklem:</b> Tırnağa yakın; genellikle orta yaş ve üzerinde, eklem kireçlenmesiyle birlikte.</li>
          <li>Nedeni çoğu zaman bilinmez; bazen bir yaralanmadan sonra eklemden sıvı sızmasıyla oluşur.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Evde neler yapabilirim?</h2>
        <ul class="dots">
          <li>Ağrı kesici kullanmadan önce hekiminize ya da eczacınıza danışın.</li>
          <li>Eczanelerde bulunan bir bileklik ya da sargı rahatlatabilir.</li>
          <li>Kisti patlatmaya çalışmayın; enfeksiyon ve cilt hasarı yapabilir.</li>
        </ul>
      </div>
      <div>
        <h2>Tedavi seçenekleri</h2>
        <ul class="dots">
          <li><b>Beklemek:</b> Ağrı, uyuşma ya da kaygı yoksa en sık önerilen yoldur.</li>
          <li><b>İğneyle boşaltma:</b> Belirtiler varsa önerilir; kist sıklıkla yeniden dolar ama ağrısız olabilir.</li>
          <li><b>Ameliyat:</b> Boşaltmaya rağmen ağrı ya da uyuşma sürüyor ve el kullanımı kısıtlanıyorsa düşünülür.</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Bileği hareketli tutan altı egzersiz</h2>
      <p class="soft">Bu hareketlerin kisti küçülttüğüne dair kanıt yoktur. Amaç, kist ağrı ya da tutukluk yapıyorsa bileğinizi ve parmaklarınızı hareketli tutmaktır. Kisti belirgin ağrıtan ya da uyuşmayı artıran hareketleri zorlamayın.</p>
      {ex_grid(["gg_wrist", "gg_rot", "tglide", "wflex", "wext_st", "grip"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(GG_FAQ)}
      <p class="soft" style="margin-top:18px">Bilek ve parmak ağrısının diğer sık nedenleri için <a href="de-quervain.html">De Quervain</a>, <a href="tetik-parmak.html">tetik parmak</a> ve <a href="karpal-tunel-sendromu.html">karpal tünel sendromu</a> rehberlerine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Bir şişlik sizi kaygılandırıyorsa</li>
        <li>Şişlik büyüyorsa</li>
        <li>Şişlik sert ve yerinden oynamıyorsa</li>
        <li>Elinizde ya da parmaklarınızda uyuşma, karıncalanma ya da güçsüzlük varsa</li>
        <li>Aynı gün: şişlik çok ağrılı, sıcak ya da kızarıksa (esmer tende kızarıklık daha zor görülebilir)</li>
      </ul>
      {CTA_CARD("Bilek ağrınız", "ganglion kisti")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(GG_SRC)}
    </div>
  </section>
</main>'''

page("ganglion-kisti.html", "Ganglion Kisti (El Bileği Kisti)",
     "El bileğinde şişlik: ganglion kisti neden olur, kendiliğinden geçer mi, boşaltmak ya da ameliyat işe yarar mı? Evde yapılabilecekler, uyarı işaretleri ve altı egzersiz.",
     "ganglion-kisti.html", NECK_CSS, GG_BODY, "",
     seo_title="Ganglion Kisti (El Bileği Kisti): Nedenleri, Tedavisi ve Egzersizler | İhsan Eren",
     condition="Ganglion kisti", faq_items=GG_FAQ)

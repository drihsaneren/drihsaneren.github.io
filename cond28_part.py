# -*- coding: utf-8 -*-
# Yeni rehber (28): kambur duruş (kifoz). cond27_part.py'den sonra exec edilir. Video yok.
# Egzersizlerin hepsi mevcut anahtarlar (çevirileri hazır).

KY_FAQ = [
 ("Kambur duruş düzelir mi?", "Duruşa bağlı kamburluk esnektir; kişi dikleşmeye çalıştığında sırt düzelebilir. Egzersizle sırttaki eğrilik açısında birkaç derecelik azalmalar bildirilmiştir. NHS ise fizyoterapinin duruşu iyileştirip ağrıyı ve tutukluğu azaltabileceğini, ancak yapısal bir eğriliği düzeltmeyeceğini belirtiyor."),
 ("Dik duruş korsesi kullanmalı mıyım?", "NHS, duruşa bağlı kamburluk için korse önermiyor. Korse yalnızca çocuklarda hafif ve orta düzey Scheuermann kifozunda, uzman kontrolünde kullanılır. Duruş için sırt kaslarınızı güçlendirmeyi ve gün içinde sık pozisyon değiştirmeyi tercih edebilirsiniz."),
 ("Kambur durmak sırt ağrısı yapar mı?", "54 çalışmayı inceleyen bir derleme, omurganın yandan görünen eğrileri ile sırt ağrısı arasında güçlü bir ilişki bulamadı. Uzun süre aynı pozisyonda kalmak ise tutukluk ve rahatsızlık yaratabilir; pozisyonunuzu sık değiştirmek iyi gelebilir."),
 ("İleri yaşta kamburluk neden artar?", "Kemik erimesi ve kireçlenme gibi durumlar ve omurga kırıkları kamburluğu artırabilir. Kemik sağlığı için kemik erimesi rehberimize bakabilirsiniz. 45 yaş üstünde belirgin kamburluğu olanlarda egzersizi inceleyen 13 çalışmanın 8’inde duruşta en az bir ölçümde iyileşme görüldü; çalışmaların az ve küçük olması nedeniyle kesin bir sonuca varılamadı."),
]

KY_SRC = [
 "NHS. " + ext("https://www.nhs.uk/conditions/kyphosis/", "Kyphosis") + ". Page last reviewed 30 December 2025.",
 "Katzman WB, Vittinghoff E, Lin F, et al. Targeted spine strengthening exercise and posture training program to reduce hyperkyphosis in older adults: results from the study of hyperkyphosis, exercise, and function (SHEAF) randomized controlled trial. Osteoporos Int. 2017;28(10):2831–2841. " + ext("https://beta.escholarship.org/uc/item/0bf5w0h5", "escholarship.org") + ".",
 "Oliveira-Costa E, Alonso-Fernández D, Gutiérrez-Sánchez Á. The impact of exercise on spinal posture in adolescents: a systematic review. Rev Paul Pediatr. 2025;43:e2025013. " + ext("https://www.scielo.br/j/rpp/a/LLrncxbBfMVvXTJfL4kswZC/?lang=en", "scielo.br") + ".",
 "Christensen ST, Hartvigsen J. Spinal curves and health: a systematic critical review of the epidemiological literature dealing with associations between sagittal spinal curves and health. J Manipulative Physiol Ther. 2008;31(9):690–714. Özet: " + ext("https://www.painscience.com/biblio/no-association-between-measurements-of-spinal-curves-and-pain-review.html", "PainScience, No association between measurements of spinal curves and pain") + ".",
 "Bansal S, Katzman WB, Giangregorio LM. " + ext("https://search.pedro.org.au/search-results/record-detail/36465", "Exercise for improving age-related hyperkyphotic posture: a systematic review") + ". Arch Phys Med Rehabil. 2014;95(1):129–140.",
]

KY_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Kambur duruş (kifoz)</h1>
    <p class="lede">Kifoz, sırtın üst kısmının öne doğru belirgin biçimde yuvarlanmasıdır; halk arasında kambur duruş denir. En sık görülen tipi duruşa bağlı kifozdur ve çoğunlukla gençlerde görülür. Hafif kamburluk çoğu zaman tedavi gerektirmez. Egzersiz sırttaki eğriliği birkaç derece azaltabilir; asıl kazanç ise daha güçlü bir sırt ve daha rahat bir gövdedir.</p>
    <p class="meta">Son güncelleme: 12 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>3 derece</b><span>60 yaş üstü 99 kişide, 6 ay boyunca haftada 3 gün yapılan egzersizle kifoz açısındaki azalma (kontrol grubuna göre)</span></div>
        <div class="stat"><b>8–12 hafta</b><span>Gençlerde kifozu azaltan egzersiz programlarının tipik süresi; haftada 2–3 gün</span></div>
        <div class="stat"><b>54 çalışma</b><span>Omurga eğrileri ile sırt ağrısı arasında güçlü bir ilişki bulunamayan derlemede incelendi</span></div>
        <div class="stat"><b>3 tip</b><span>Duruşa bağlı, Scheuermann ve doğuştan kifoz; en sık görüleni duruşa bağlı olanı</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Sırtın üst kısmının kambur ya da yuvarlak görünmesi; bazen omuzların da öne düşmesi.</li>
          <li>Hafif kamburluk çoğu zaman başka bir belirti yapmaz.</li>
          <li>Belirgin ya da artan eğrilik sırt ağrısına ve tutukluğa yol açabilir.</li>
          <li>Çok ileri eğrilik şiddetli ağrıya ve nefes almada zorluğa neden olabilir.</li>
        </ul>
      </div>
      <div>
        <h2>Tipleri ve nedenleri</h2>
        <ul class="dots">
          <li><b>Duruşa bağlı kifoz:</b> En sık tiptir, çoğunlukla gençlerde ve kötü duruşla ilişkilidir.</li>
          <li><b>Scheuermann kifozu:</b> Omurların arka kısmı ön kısmından hızlı büyür ve kama biçimini alır.</li>
          <li><b>Doğuştan kifoz:</b> Omurga anne karnında düzgün gelişmez; nadirdir.</li>
          <li>Omurga yaralanması, kireçlenme ve kemik erimesi de kamburluğa yol açabilir.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Kamburluk ağrının nedeni mi?</h2>
        <p class="soft">54 çalışmayı inceleyen bir derleme, omurganın yandan görünen eğrileri ile sırt ağrısı dahil sağlık sorunları arasında güçlü bir ilişki bulamadı. Yani "dik dur" uyarısı ağrıyı tek başına açıklamıyor. Yine de uzun süre aynı pozisyonda kalmak tutukluk yaratabilir.</p>
      </div>
      <div>
        <h2>Egzersiz eğriliği değiştirir mi?</h2>
        <p class="soft">60 yaş üstü 99 kişide fizyoterapist eşliğinde 6 ay, haftada 3 gün yapılan sırt güçlendirme ve duruş eğitimi, kifoz açısını kontrol grubuna göre 3 derece azalttı ve kişilerin kendi görünüşlerine dair algısını iyileştirdi; ancak fiziksel performans testlerinde fark bulunmadı.</p>
        <p class="soft">Gençlerde yapılan çalışmalarda 6–12 haftalık düzeltici egzersiz ve pilates programlarıyla 2 ile 9 derece arasında azalmalar bildirildi; çalışmalar küçük ve uzun dönem sonuçlar bilinmiyor.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Sırtınızı güçlendirin</h3><p>Sırt ve gövde kaslarını güçlendiren egzersizler duruşu destekler. Uzun süredir egzersiz yapmıyorsanız önce bir sağlık profesyoneline danışabilirsiniz.</p></div>
        <div class="kind"><span class="n">2</span><h3>Pozisyon değiştirin</h3><p>Masa başında ya da telefon kullanırken uzun süre aynı pozisyonda kalmamaya çalışabilir, sık sık kalkıp gerinebilirsiniz.</p></div>
        <div class="kind"><span class="n">3</span><h3>Göğsü açın</h3><p>Göğüs kafesini açan ve kürek kemiklerini geriye toplayan hareketler, öne düşen omuzlarda rahatlama sağlayabilir.</p></div>
        <div class="kind"><span class="n">4</span><h3>Ağrı kesici</h3><p>Ağrı varsa parasetamol ya da iltihap giderici bir ilacı hekiminize ya da eczacınıza danışarak kullanabilirsiniz.</p></div>
      </div>
      <p class="soft" style="margin-top:18px">Uzun saatler bilgisayar başında çalışıyorsanız <a href="masa-basi.html">masa başında çalışanlar için</a>, ileri yaşta kemik sağlığı için <a href="kemik-erimesi.html">kemik erimesi</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Sırtı dikleştiren altı egzersiz</h2>
      <p class="soft">Gençlerdeki çalışmalarda en etkili görünen düzen haftada 2–3 gün, 15–45 dakika ve 8–12 haftaydı. Hareketleri ağrısız bir aralıkta, yavaş ve kontrollü yapın.</p>
      {ex_grid(["pchest", "thor", "wallpost", "row", "scap", "cat"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(KY_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Kendinizde ya da çocuğunuzda kamburluk fark ettiyseniz</li>
        <li>Kamburluk belirginleşiyor ya da artıyorsa</li>
        <li>Sırt ağrısı şiddetliyse ya da nefes almada zorluk varsa</li>
        <li>Kemik erimesi olan birinde sırt ağrısı aniden başladıysa</li>
      </ul>
      {CTA_CARD("Duruşunuz ve sırt ağrınız", "kambur duruş")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(KY_SRC)}
    </div>
  </section>
</main>'''

page("kambur-durus.html", "Kambur Duruş (Kifoz)",
     "Kambur duruş neden olur, ağrı yapar mı, egzersiz eğriliği değiştirir mi? Kifoz tipleri, çalışmaların sonuçları, korse sorusu ve evde sırtı dikleştiren altı egzersiz.",
     "kambur-durus.html", NECK_CSS, KY_BODY, "",
     seo_title="Kambur Duruş (Kifoz): Nedenleri, Egzersizler ve Düzelir mi? | İhsan Eren",
     condition="Kifoz (kambur duruş)", faq_items=KY_FAQ)

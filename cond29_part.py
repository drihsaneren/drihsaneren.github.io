# -*- coding: utf-8 -*-
# Yeni rehber (29): Baker kisti (diz arkası kisti). cond28_part.py'den sonra exec edilir. Video yok.
# Egzersizlerin çoğu diz rehberindeki anahtarlar (çevirileri hazır); topuk kaydırma bu sayfaya özel.

_ex2("bk_hslide", "hslide", "Topuk kaydırma", "Sırtüstü yatın, bacaklarınız düz olsun. Bir topuğunuzu yerde kaydırarak kalçanıza doğru çekin ve dizinizi rahat ettiğiniz kadar bükün; dizinizin arkasında hafif bir gerginlik olabilir, ağrıyı zorlamayın. Sonra yavaşça geri kaydırın.", "Her bacakla 10 tekrar, günde 2 kez")

BK_FAQ = [
 ("Baker kisti kendiliğinden geçer mi?", "Geçebilir; özellikle çocuklarda sık görülür. Yetişkinlerde kist çoğu zaman dizdeki başka bir sorundan kaynaklandığı için, o sorun tedavi edildiğinde belirtiler de genellikle düzelir. İyileşme birkaç aydan birkaç yıla kadar sürebilir."),
 ("Kisti iğneyle boşaltmak işe yarar mı?", "Boşaltmak belirtileri rahatlatabilir, ancak kist sıklıkla yeniden dolar ve uzun süredir var olan kistlerde işe yaramayabilir. Boşaltmanın ardından yapılabilen kortizon iğnesi ağrıyı ve iltihabı azaltabilir, ama kistin tekrarlamasını önlemez."),
 ("Ameliyat gerekir mi?", "Çoğu zaman gerekmez. Kistin kendisinin çıkarılması nadirdir; ameliyat daha çok dizin içindeki menisküs yırtığı gibi önemli bir hasarı onarmak için ya da diğer tedavilerle geçmeyen büyük ve ağrılı kistlerde düşünülür."),
 ("Egzersiz yapabilir miyim?", "Evet. Dizi hareketli tutmak ve çevresindeki kasları güçlendirmek önerilir. Dizin arkasındaki gerginliği belirgin artıran hareketleri bir süre azaltabilir, ağrısız bir aralıkta çalışabilirsiniz."),
]

BK_SRC = [
 "NHS 111 Wales. " + ext("https://111.wales.nhs.uk/bakerscyst/?locale=en", "Baker’s cyst") + ". Last updated 6 November 2025.",
 "Royal Berkshire NHS Foundation Trust. " + ext("https://www.royalberkshire.nhs.uk/media/llfjmsmb/bakers-cyst_feb25.pdf", "Baker’s cyst") + ". Venous Thrombosis Clinic, February 2025.",
 "Prevalence and associated injuries in patients with knee cysts: an epidemiological study. Orthopaedic Research Society 2025 Annual Meeting, conference abstract. " + ext("https://scholarlyworks.corewellhealth.org/orthopaedic_surgery_confabstract/138", "scholarlyworks.corewellhealth.org") + ".",
]

BK_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Baker kisti (diz arkası kisti)</h1>
    <p class="lede">Baker kisti, dizin arkasında oluşan, içi eklem sıvısıyla dolu bir şişliktir. Yetişkinlerde çoğu zaman kireçlenme ya da menisküs yırtığı gibi dizdeki başka bir sorunun sonucudur; o sorun tedavi edildiğinde kist de genellikle geriler. Çoğu zaman tehlikeli değildir, ama baldırda ani şişlik ve ağrı yaparsa bacaktaki pıhtıyla karışabileceği için hemen değerlendirilmelidir.</p>
    <p class="meta">Son güncelleme: 14 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>35–70 yaş</b><span>Yetişkinlerde en sık görüldüğü yaş aralığı; çocuklarda ise çoğunlukla 4–7 yaşta, sağlıklı bir dizde görülür</span></div>
        <div class="stat"><b>20’de 1–2</b><span>Kistin patlama sıklığı; baldıra sızan sıvı bacakta pıhtıya benzer belirtiler yapabilir</span></div>
        <div class="stat"><b>Aylar – yıllar</b><span>Kendiliğinden ya da altta yatan sorun tedavi edildikçe gerileme süresi</span></div>
        <div class="stat"><b>10–20 dakika</b><span>Havluya sarılı buz uygulamasının önerilen süresi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Dizin arkasında, özellikle ayakta dururken belirginleşen yumuşak bir şişlik.</li>
          <li>Dizde ya da bacakta ağrı, gerginlik, tutukluk ve sızı.</li>
          <li>Dizi bükmekte zorlanma; bazen tıklama ya da kilitlenme hissi.</li>
          <li>Yürüdükten sonra artan şikâyetler.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li><b>Yetişkinlerde:</b> Çoğu zaman dizdeki başka bir sorunun sonucudur: kireçlenme, romatoid artrit, gut ya da menisküs veya bağ yırtığı gibi bir yaralanma.</li>
          <li><b>Çocuklarda:</b> Genellikle sağlıklı bir dizde, belirgin bir neden olmadan oluşur.</li>
          <li>Bir araştırmada diz MR’larında en sık görülen kist türü Baker kistiydi; özellikle eklemde sıvı artışı ve iç menisküs yırtığıyla birlikte görüldü.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Kist patlarsa ya da pıhtı mı?</h2>
        <p class="soft">Kist patlarsa içindeki sıvı baldıra sızar; baldırda ani ağrı, şişlik, gerginlik ve kızarıklık olabilir. Bu belirtiler bacak toplardamarında pıhtıyla (derin ven trombozu) çok benzerdir ve ayırt etmek için muayene ve tetkik gerekir. Esmer tende kızarıklığın görülmesi daha zor olabilir.</p>
      </div>
      <div>
        <h2>Tedavi</h2>
        <ul class="dots">
          <li>Şikâyet yapmıyorsa tedavi gerekmeyebilir.</li>
          <li>Asıl hedef, kiste yol açan diz sorununu tedavi etmektir.</li>
          <li>Fizyoterapi, dizi hareketli tutmaya ve çevresindeki kasları güçlendirmeye yardım eder.</li>
          <li>İğneyle boşaltma ve kortizon iğnesi rahatlatabilir, ama kist sıklıkla tekrarlar.</li>
          <li>Ameliyat nadiren gerekir; çoğu zaman kistin kendisi değil, dizdeki hasar onarılır.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Dinlendirin, yükseltin</h3><p>Ağrılı dönemde dizinizi dinlendirebilir, otururken bacağınızı bir yastıkla yükseltebilirsiniz.</p></div>
        <div class="kind"><span class="n">2</span><h3>Buz</h3><p>Havluya sardığınız buzu doğrudan cilde değdirmeden 10–20 dakika uygulayabilirsiniz.</p></div>
        <div class="kind"><span class="n">3</span><h3>Ağrı kesici</h3><p>İbuprofen ya da parasetamol ağrıyı ve şişliği azaltabilir. Astım, yüksek tansiyon, böbrek, kalp ya da mide sorununuz varsa önce hekiminize veya eczacınıza danışabilirsiniz.</p></div>
        <div class="kind"><span class="n">4</span><h3>Dizlik ve hareket</h3><p>Eczanelerde bulunan bir dizlik destek sağlayabilir. Şikâyetler azaldıkça dizinizi hareketli tutmak ve kaslarınızı güçlendirmek önemlidir.</p></div>
      </div>
      <p class="soft" style="margin-top:18px">Kistin sık nedenleri için <a href="diz-kireclenmesi.html">diz kireçlenmesi</a> ve <a href="menisku-yirtigi.html">menisküs yırtığı</a> rehberlerine bakabilirsiniz.</p>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Dizi rahatlatan altı egzersiz</h2>
      <p class="soft">Hareketleri ağrısız bir aralıkta, yavaş ve kontrollü yapın. Baldırınızda yeni bir şişlik ya da ağrı olursa egzersizi bırakıp hekiminize başvurun.</p>
      {ex_grid(["bk_hslide", "quad", "kext", "slr", "dn_heel", "sts"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(BK_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Dizin arkasında ne olduğunu bilmediğiniz bir şişlik fark ettiyseniz</li>
        <li>Acil: bacakta ani ve artan ağrı ya da şişlik, morarma, sıcaklık ya da kızarıklık varsa (kist patlamış ya da pıhtı olabilir)</li>
        <li>Acil: bacaktaki bu belirtilere nefes darlığı ya da göğüs ağrısı eşlik ediyorsa hemen 112’yi arayın</li>
      </ul>
      {CTA_CARD("Diz ağrınız", "Baker kisti")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(BK_SRC)}
    </div>
  </section>
</main>'''

page("baker-kisti.html", "Baker Kisti (Diz Arkası Kisti)",
     "Dizin arkasında şişlik: Baker kisti neden olur, kendiliğinden geçer mi, boşaltmak işe yarar mı? Pıhtıyla karışan belirtiler, tedavi seçenekleri ve evde altı egzersiz.",
     "baker-kisti.html", NECK_CSS, BK_BODY, "",
     seo_title="Baker Kisti (Diz Arkası Şişlik): Nedenleri, Tedavisi ve Egzersizler | İhsan Eren",
     condition="Baker kisti (popliteal kist)", faq_items=BK_FAQ)

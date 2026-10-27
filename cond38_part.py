# -*- coding: utf-8 -*-
# Yeni rehber (38): Morton nöroması. cond37_part.py'den sonra exec edilir. Video yok.
# Dört hazır çizimli egzersiz; nöromayı geçirdiğine dair kanıt olmadığı sayfada yazıyor.

_ex2("mn_calf", "calf", "Duvarda baldır germe", "Ellerinizi duvara dayayın, bir bacağınızı arkaya alın. Arkadaki dizinizi düz, topuğunuzu yerde tutarak kalçanızı duvara doğru ilerletin; baldırınızda gerginlik hissedin.", "20–30 saniye, her bacakla 2–3 kez")
_ex2("mn_soleus", "soleus", "Dizi bükük baldır germe", "Aynı pozisyonda arkadaki ayağınızı biraz öne alın ve dizinizi bükün. Topuğunuz yerden kalkmadan kalçanızı aşağı indirin; gerilmeyi baldırın alt kısmında hissedin.", "20–30 saniye, her bacakla 2–3 kez")
_ex2("mn_arch", "ff_short", "Ayak kavsini kaldırma", "Oturun, ayağınız yere düz bassın. Ayak tabanınızdaki kasları sıkarak ayağınızı kısaltır gibi kavsinizi yükseltin; parmaklarınız kıvrılmasın, yerde düz kalsın. Birkaç saniye tutup gevşetin.", "10 tekrar, günde 2 kez")
_ex2("mn_toe", "dm_toe", "Ayak ucu ve topuk kaldırma", "Oturun, ayaklarınız yere düz bassın. Önce topuklarınız yerde kalarak ayak uçlarınızı kaldırın, sonra indirip topuklarınızı kaldırın. Ayak ve ayak bileğini, ayak önüne yük bindirmeden hareket ettirir.", "10–15 tekrar, günde 2 kez")

MN_FAQ = [
 ("Gerçekten bir tümör mü?", "Hayır. Adındaki “nöroma” sözcüğüne rağmen bir tümör değildir. Ayak parmağı kemikleri arasındaki bir sinirin tahriş olması ya da zarar görmesiyle çevresindeki dokunun kalınlaşmasıdır."),
 ("Hangi ayakkabıları giymeliyim?", "Geniş burunlu, alçak topuklu ve yumuşak tabanlı rahat ayakkabılar önerilir. Dar ve sivri burunlu ayakkabılar, yüksek topuklar ve ince tabanlı ayakkabılar ayak önündeki baskıyı artırdığı için bir süre kaçınmanız iyi olur. Eczanelerde bulunan ayak önü pedleri ya da yumuşak tabanlıklar da rahatlatabilir."),
 ("İğne tedavisi işe yarar mı?", "Belirtiler çok şiddetliyse ya da diğer tedaviler işe yaramadıysa kortizon iğnesi düşünülebilir. 25 çalışmayı inceleyen bir derlemede ameliyatsız tedaviler arasında ağrıyı azaltmada en güçlü kanıt kortizon iğnesi ve fizyoterapistin uyguladığı ayak eklemi mobilizasyonu için bulundu; ama altın standart sayılabilecek bir tedavi gösterilemedi. 131 hastayla yapılan, hastaların hangi iğneyi aldığını bilmediği bir çalışmada kortizonlu iğne, yalnızca uyuşturucu içeren iğneye göre 3 ayda ayak sağlığını ve ağrıyı daha çok iyileştirdi."),
 ("Ameliyat gerekir mi?", "Çoğu kişi ayakkabı değişikliği ve pedlerle rahatlar. Ameliyat, çok şiddetli belirtilerde ya da diğer tedaviler işe yaramadığında bir ayak cerrahıyla birlikte değerlendirilen bir seçenektir."),
]

MN_SRC = [
 "NHS. " + ext("https://www.nhs.uk/conditions/mortons-neuroma/", "Morton’s neuroma") + ". Page last reviewed 12 June 2025.",
 "Matthews BG, Hurn SE, Harding MP, et al. " + ext("https://link.springer.com/doi/10.1186/s13047-019-0320-7", "The effectiveness of non-surgical interventions for common plantar digital compressive neuropathy (Morton’s neuroma): a systematic review and meta-analysis") + ". Journal of Foot and Ankle Research. 2019;12:12.",
 "NHS Tayside, Referral Help System. " + ext("https://www.nhstayside.scot.nhs.uk/WorkingWithUs/ReferralHelpSystem/PROD_351192", "Morton’s neuroma") + ".",
 "Matthews BG, Thomson CE, Harding MP, McKinley JC, Ware RS. " + ext("https://doi.org/10.1002/14651858.CD014687.pub2", "Treatments for Morton’s neuroma") + ". Cochrane Database Syst Rev. 2024;CD014687",
 "Thomson CE, Beggs I, Martin DJ, et al. " + ext("https://doi.org/10.2106/JBJS.I.01780", "Methylprednisolone injections for the treatment of Morton neuroma: a patient-blinded randomized trial") + ". J Bone Joint Surg Am. 2013;95(9):790–798.",
]

MN_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Morton nöroması</h1>
    <p class="lede">Yürürken ayak parmaklarınızın arasında yanma ya da batma, ayakkabının içinde bir çakıl taşı varmış gibi bir his mi var? Morton nöroması, ayak parmağı kemikleri arasındaki bir sinirin tahriş olmasıyla çevresindeki dokunun kalınlaşmasıdır; en sık 3. ve 4. parmaklar arasında görülür. Adı korkutucu olsa da bir tümör değildir ve belirtiler çoğu zaman ayakkabı değişikliği ve basit önlemlerle hafifler.</p>
    <p class="meta">Son güncelleme: 27 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>3. ve 4. parmak</b><span>Ağrının en sık hissedildiği yer: bu iki parmağın arası</span></div>
        <div class="stat"><b>2 hafta</b><span>Evde önlemlere rağmen düzelmezse hekime başvurmanız önerilen süre</span></div>
        <div class="stat"><b>25 çalışma</b><span>Ameliyatsız tedavileri inceleyen derlemede altın standart bir tedavi bulunamadı</span></div>
        <div class="stat"><b>Tümör değil</b><span>Tahriş olan sinirin çevresindeki dokunun kalınlaşması</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>3. ve 4. ayak parmakları arasında ani, batıcı ya da yanıcı ağrı.</li>
          <li>Ayak tabanında bir çakıl taşı ya da yumru varmış gibi his.</li>
          <li>Ayakta karıncalanma ya da uyuşma.</li>
          <li>Dar ya da yüksek topuklu ayakkabılarla ve ayak hareketleriyle artan ağrı; zamanla kötüleşebilir.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Dar, sivri burunlu ya da yüksek topuklu ayakkabılar.</li>
          <li>Çok koşmak ya da ayak önüne baskı bindiren diğer sporlar.</li>
          <li>Düz tabanlık, yüksek ayak kavsi, <a href="halluks-valgus.html">halluks valgus</a> ya da çekiç parmak gibi diğer ayak sorunları.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Ayakkabı</h3><p>Geniş burunlu, alçak topuklu, yumuşak tabanlı ayakkabılar giyebilirsiniz. Dar, sivri, yüksek topuklu ve ince tabanlı ayakkabılardan kaçının.</p></div>
        <div class="kind"><span class="n">2</span><h3>Ped ve tabanlık</h3><p>Eczanelerde bulunan ayak önü pedleri ya da yumuşak tabanlıklar ağrılı bölgedeki baskıyı azaltabilir. Ayak uzmanı size özel ped hazırlayabilir.</p></div>
        <div class="kind"><span class="n">3</span><h3>Yükü azaltın</h3><p>Koşu ve sıçrama gibi darbeli aktiviteleri bir süre azaltabilir, fırsat buldukça ayağınızı dinlendirip yükseltebilirsiniz. Fazla kilo varsa vermek ayak önündeki yükü azaltır.</p></div>
        <div class="kind"><span class="n">4</span><h3>Ağrı kesici</h3><p>Ağrı kesici kullanmanız gerekiyorsa hangisinin size uygun olduğunu hekiminize sorun.</p></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Ayağı ve baldırı rahatlatan dört egzersiz</h2>
      <p class="soft">Bu egzersizlerin nöromayı geçirdiğine dair kanıt yoktur; amaç ayak ve baldırı esnek ve güçlü tutmaktır. Parmak arasındaki ağrıyı artıran hareketleri yapmayın.</p>
      {ex_grid(["mn_calf", "mn_soleus", "mn_arch", "mn_toe"], "ex four")}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(MN_FAQ)}
      <p class="soft" style="margin-top:18px">Ayak yapısıyla ilgili sorunlar için <a href="duztabanlik.html">düz tabanlık</a> ve <a href="halluks-valgus.html">halluks valgus</a> rehberlerine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Ağrı şiddetliyse ya da günlük işlerinizi yapmanızı engelliyorsa</li>
        <li>Ağrı giderek artıyor ya da tekrar tekrar geliyorsa</li>
        <li>2 hafta evde önlem almanıza rağmen düzelme yoksa</li>
        <li>Ayağınızda karıncalanma, güçsüzlük ya da uyuşma varsa</li>
        <li>Ağrı yakın zamanda bir ayak yaralanmasından ya da ayak-ayak bileği ameliyatından sonra başladıysa</li>
      </ul>
      {CTA_CARD("Ayak ağrınız", "Morton nöroması")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(MN_SRC)}
    </div>
  </section>
</main>'''

page("morton-noromasi.html", "Morton Nöroması",
     "Ayak parmaklarınızın arasında yanma, batma ya da ayakkabıda çakıl taşı hissi mi var? Morton nöroması neden olur, hangi ayakkabılar iyi gelir, iğne ve ameliyat ne zaman gerekir? Evde dört egzersiz.",
     "morton-noromasi.html", NECK_CSS, MN_BODY, "",
     seo_title="Morton Nöroması: Belirtiler, Ayakkabı Seçimi, Tedavi ve Egzersizler | İhsan Eren",
     condition="Morton nöroması", faq_items=MN_FAQ)

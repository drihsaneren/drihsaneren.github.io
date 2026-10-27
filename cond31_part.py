# -*- coding: utf-8 -*-
# Yeni rehber (31): Gece bacak krampları. cond30_part.py'den sonra exec edilir. Video yok.
# Yeni çizim: sandalyede arka uyluk germe. Diğerleri hazır çizimler, metinler bu sayfaya göre.

SV["lc_ham"] = fig(GRD + CHAIR_L +
    '<path class="fig" d="M62 78 L82 78 L82 110 L90 111"/>'
    '<path class="fig hl" d="M62 80 L104 106 L107 97"/>'
    f'<g>{anim_t("0 62 78;30 62 78;30 62 78;0 62 78", dur="5s", kt="0;0.35;0.7;1", typ="rotate")}'
    '<path class="fig" d="M62 78 L62 46 M62 50 L72 66"/><circle class="hd" cx="64" cy="36" r="8"/></g>',
    "Sandalyede arka uyluk germe")

_ex2("lc_relief", "towelst2", "Kramp anında germe", "Bacağınızı düz uzatın ve ayak ucunuzu kendinize doğru çekin; yetişmiyorsanız bir havluyla çekebilirsiniz. Kasılan kası avucunuzla ovun. Ayağa kalkabiliyorsanız topuğunuza basarak birkaç adım atmak da gevşetebilir.", "Kramp geçene kadar")
_ex2("lc_calf", "calf", "Duvarda baldır germe", "Yüzünüz duvara dönük durun, ellerinizi kollarınız uzanmış şekilde duvara koyun. Bir bacağınızı arkaya alın, dizinizi düz ve topuğunuzu yerde tutun. Baldırınızda gerginlik hissedene kadar öne doğru eğilip 2–3 saniye bekleyin, sonra doğrulun. Bacak değiştirerek tekrarlayın.", "5 dakika, günde 3 kez; sonuncusu yatmadan hemen önce")
_ex2("lc_soleus", "soleus", "Dizi bükük baldır germe", "Aynı pozisyonda arkadaki ayağınızı biraz öne alın ve dizinizi bükün. Topuğunuz yerden kalkmadan kalçanızı aşağı indirin; gerilmeyi baldırın alt kısmında hissedin.", "Her bacakla 20–30 saniye, 2–3 kez")
_ex2("lc_ham", "lc_ham", "Sandalyede arka uyluk germe", "Sandalyenin ön kenarına oturun. Bir bacağınızı öne uzatın, topuğunuz yerde, ayak ucunuz yukarı baksın. Sırtınızı düz tutarak kalçanızdan öne eğilin; uyluğunuzun arkasında gerginlik hissedin. Bekleyin, sonra bacak değiştirin.", "Her bacakla 20–30 saniye, yatmadan önce")
_ex2("lc_towel", "towelst2", "Yatakta havluyla baldır germe", "Yatağa bacaklarınız düz olacak şekilde oturun. Havluyu ayağınızın ön kısmına dolayıp uçlarından tutun. Dizinizi düz tutarak havluyu kendinize doğru çekin; baldırınızda gerginlik hissedin.", "Her bacakla 20–30 saniye, yatmadan önce")
_ex2("lc_walk", "walk", "Yatmadan önce hafif hareket", "Yatmadan önce birkaç dakika sakin bir tempoda yürüyebilir ya da sabit bisiklet çevirebilirsiniz. Bunun yararı araştırmalarla kanıtlanmış değil; bazı kişiler fayda gördüğünü söylüyor.", "Birkaç dakika")

LC_FAQ = [
 ("Magnezyum işe yarar mı?", "Büyük bir Cochrane derlemesine göre belirgin bir neden olmadan kramp yaşayan yaşlı yetişkinlerde magnezyumun krampları anlamlı ölçüde azaltması beklenmiyor. Gebelikteki kramplar için ise araştırmalar çelişkili ve kanıt çok belirsiz. Takviye kullanmadan önce hekiminize danışabilirsiniz."),
 ("Kinin ya da tonik suyu kullanmalı mıyım?", "Kendi başınıza kullanmayın. Kinin bazı ülkelerde egzersiz işe yaramadığında hekim kontrolünde verilebiliyor; ama kan pulcuklarında düşme ve kalp ritim bozukluğu gibi ciddi yan etkileri olabildiği için ABD’de bacak krampı için kullanılması önerilmiyor."),
 ("Kullandığım ilaç kramp yapabilir mi?", "Yapabilir. Kolesterol için kullanılan statinler ve tansiyon için kullanılan idrar söktürücüler kramplarla ilişkilendirilen ilaçlar arasında. Kramplarınız yeni bir ilaçtan sonra başladıysa ilacı kendiniz bırakmayın; hekiminizle konuşabilirsiniz."),
 ("Kramp mı, huzursuz bacak mı?", "Kramp ani, ağrılı bir kasılmadır; kas sertleşir ve gözle görülebilir. Huzursuz bacak sendromunda ise bacakları hareket ettirmek için karşı konulamaz bir istek olur, genellikle akşamları artar, hareketle rahatlar ve ağrılı bir kasılma yoktur."),
]

LC_SRC = [
 "HSE. " + ext("https://www2.hse.ie/conditions/leg-cramps/", "Leg cramps") + ". Page last reviewed 1 July 2024.",
 "Allen RE, Kirby KA. " + ext("https://www.aafp.org/pubs/afp/issues/2012/0815/p350.html", "Nocturnal leg cramps") + ". American Family Physician. 2012;86(4):350–355.",
 "Hallegraeff JM, van der Schans CP, de Ruiter R, de Greef MH. " + ext("https://search.pedro.org.au/search-results/record-detail/31037", "Stretching before sleep reduces the frequency and severity of nocturnal leg cramps in older adults: a randomised trial") + ". Journal of Physiotherapy. 2012;58(1):17–22.",
 "Garrison SR, Korownyk CS, Kolber MR, et al. " + ext("https://cochranelibrary.com/cdsr/doi/10.1002/14651858.CD009402.pub3/information", "Magnesium for skeletal muscle cramps") + ". Cochrane Database of Systematic Reviews. 2020;(9):CD009402.",
 "NHS. " + ext("https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/", "DVT (deep vein thrombosis)") + ". Page last reviewed 30 April 2026.",
]

LC_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Gece bacak krampları</h1>
    <p class="lede">Gece uykudan baldırınızdaki ani ve sert bir kasılmayla uyanmak çok yorucu olabilir. Bacak krampları çok yaygındır ve çoğu zaman zararsızdır. Çoğu zaman belirgin bir nedeni bulunmaz, ama yaş, bazı ilaçlar, gebelik ve sıvı kaybı riski artırabilir. Yatmadan önce düzenli germe, araştırmalarda krampları azaltmaya yardımcı olmuştur.</p>
    <p class="meta">Son güncelleme: 27 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%50–60</b><span>Gece bacak krampı yaşadığını bildiren yetişkinlerin oranı; yaşla artar</span></div>
        <div class="stat"><b>Saniyeler – 10 dk</b><span>Bir krampın süresi; sonrasında kas 24 saate kadar ağrılı kalabilir</span></div>
        <div class="stat"><b>6 hafta</b><span>Her gece yatmadan önce germe yapılan araştırmada kramp sıklığı ve şiddeti azaldı</span></div>
        <div class="stat"><b>Günde 3 kez</b><span>Önerilen baldır germe sıklığı; sonuncusu yatmadan hemen önce</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Bacak kasında ani, ağrılı bir kasılma; kas sertleşir ve hareket etmek zorlaşır.</li>
          <li>En sık baldırda, daha az sıklıkla ayakta ya da uylukta.</li>
          <li>Genellikle gece ya da dinlenirken başlar.</li>
          <li>Birkaç saniyeden 10 dakikaya kadar sürer; sonrasında kas bir gün kadar hassas kalabilir.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Çoğu zaman belirgin bir neden bulunmaz.</li>
          <li><b>Yaş:</b> Yaş ilerledikçe daha sık görülür.</li>
          <li><b>Kasları zorlamak:</b> Özellikle sıcak ve nemli havada yapılan yorucu egzersiz.</li>
          <li><b>Gebelik:</b> Genellikle son dönemde.</li>
          <li><b>İlaçlar:</b> Kolesterol için statinler, tansiyon için idrar söktürücüler.</li>
          <li><b>Diğer:</b> Yeterince sıvı almamak; alkole bağlı karaciğer hastalığı.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Kramp anında ne yapabilirim?</h2>
        <ul class="dots">
          <li>Kası germek ya da ovmak ağrıyı hafifletebilir; kramp çoğu zaman tedavi gerekmeden geçer.</li>
          <li>Bacağınızı düz uzatıp ayak ucunuzu kendinize doğru çekebilirsiniz.</li>
          <li>Ağrı kesiciler kramp anında etki etmek için çok yavaştır; sonrasında kalan ağrı için ilaç kullanmadan önce hekiminize danışın.</li>
        </ul>
      </div>
      <div>
        <h2>Kramp sanılan başka durumlar</h2>
        <ul class="dots">
          <li><b>Huzursuz bacak:</b> Bacakları oynatmak için karşı konulamaz bir istek; ağrılı kasılma yoktur. <a href="huzursuz-bacak.html">Rehbere bakın</a>.</li>
          <li><b>Yürürken gelen baldır ağrısı:</b> Yürüyünce başlayıp dinlenince geçen ağrı, bacak atardamarlarında daralmanın belirtisi olabilir.</li>
          <li><b>Uyuşma, karıncalanma, elektrik çarpması gibi ağrı:</b> Sinirlerle ilgili bir sorunu düşündürür. <a href="diyabetik-noropati.html">Diyabetik nöropati</a> rehberine bakabilirsiniz.</li>
          <li><b>Tek bacakta şişlik ve zonklayan ağrı:</b> Bacakta pıhtı olabilir; aşağıdaki uyarı işaretlerine bakın.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Krampları azaltmak için</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Yatmadan önce germe</h3><p>55 yaş üstü 80 kişinin katıldığı bir araştırmada, 6 hafta boyunca her gece yatmadan önce baldır ve arka uyluk germe yapanlarda kramplar daha seyrek ve daha hafif oldu.</p></div>
        <div class="kind"><span class="n">2</span><h3>Gün içinde de germe</h3><p>Baldır germeyi günde 3 kez yapabilirsiniz. Kramplar seyrekleşirse günde 1–2 kez yeterli olabilir. Germe krampları tamamen durdurmayabilir.</p></div>
        <div class="kind"><span class="n">3</span><h3>İlaçlarınıza bakın</h3><p>Kramplar yeni bir ilaçtan sonra başladıysa ilacı kendiniz bırakmadan hekiminizle konuşabilirsiniz.</p></div>
        <div class="kind"><span class="n">4</span><h3>Yeterince sıvı</h3><p>Sıvı kaybı kramplarla ilişkilidir; özellikle sıcak havada ve egzersizde yeterince su içmeye dikkat edebilirsiniz.</p></div>
      </div>
      <p class="soft" style="margin-top:18px">Kramplar uykunuzu bölüyorsa <a href="uyku.html">uyku rehberi</a> de işinize yarayabilir.</p>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Kramplara karşı altı hareket</h2>
      <p class="soft">Germeleri yavaş yapın ve sıçratmayın; hafif bir gerginlik yeterlidir. Germe sırasında kramp başlarsa hareketi bırakıp kası ovun.</p>
      {ex_grid(["lc_relief", "lc_calf", "lc_soleus", "lc_ham", "lc_towel", "lc_walk"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(LC_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Kramplar uykunuzu bozuyorsa</li>
        <li>Bacaklarınızda uyuşma ya da şişlik de varsa</li>
        <li>Bir kramp 10 dakikadan uzun sürüyorsa</li>
        <li>Aynı gün: tek bacakta zonklayan ağrı, şişlik, kızarık ya da koyulaşmış cilt varsa (bacakta pıhtı olabilir)</li>
        <li>Acil: bu belirtilere nefes darlığı ya da göğüs ağrısı eşlik ediyorsa hemen 112’yi arayın</li>
      </ul>
      {CTA_CARD("Bacak kramplarınız", "gece bacak krampları")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(LC_SRC)}
    </div>
  </section>
</main>'''

page("gece-bacak-kramplari.html", "Gece Bacak Krampları",
     "Gece baldırınızda kramp neden olur, nasıl önlenir? Kramp anında yapılacaklar, ilaçlar ve magnezyum hakkında bilinenler, uyarı işaretleri ve evde altı hareket.",
     "gece-bacak-kramplari.html", NECK_CSS, LC_BODY, "",
     seo_title="Gece Bacak Krampları (Baldır Krampı): Nedenleri, Önleme ve Germe Egzersizleri | İhsan Eren",
     condition="Gece bacak krampları", faq_items=LC_FAQ)

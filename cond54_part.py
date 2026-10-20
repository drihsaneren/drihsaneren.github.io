# -*- coding: utf-8 -*-
# Yeni rehber (54): Bel fıtığı ameliyatı sonrası (mikrodiskektomi). cond53_part.py'den sonra exec edilir. Video yok.
# Egzersizler Royal Berkshire (Eylül 2025) ve James Paget NHS broşürlerine göre, hazır çizimlerle.

_ex2("bfa_tra", "pf_lie", "Derin karın kaslarını sıkma", "Sırtüstü uzanın, dizleriniz bükülü olsun. Göbeğinizin altındaki derin karın kaslarınızı ve pelvik taban kaslarınızı nazikçe içeri çekin. Nefesinizi tutmayın.", "Yapabiliyorsanız 10 saniye tutun, 10 tekrar")
_ex2("bfa_tilt", "ptilt", "Pelvik eğme", "Sırtüstü uzanın, dizleriniz bükülü olsun. Belinizin çukurunu yatağa doğru nazikçe düzleştirin, sonra gevşeyin.", "15 tekrar")
_ex2("bfa_prone", "pressup", "Yüzüstü uzanma ve doğrulma", "Önce 3–5 dakika yüzüstü uzanın. Rahat ettikçe dirsekleriniz üzerinde doğrulun; daha sonra kalçanız yatakta kalacak şekilde kollarınızla iterek doğrulun. Kuvveti belinizle değil, kollarınızla verin.", "5–10 saniye tutun, 10 tekrar")
_ex2("bfa_slump", "slump", "Oturarak siyatik sinir kaydırma", "Ameliyattan önce ağrınız bacağınızın arkasına yayılıyorduysa, 2.–3. günden itibaren başlayabilirsiniz. Dik oturun, dizinizi bacağınızın arkasında hafif bir çekilme hissedene kadar yavaşça düzeltin, kısa bir süre tutun ve bükün.", "10 tekrar")
_ex2("bfa_walk", "walk", "Kısa ve sık yürüyüşler", "Cerrahınız onaylarsa ameliyat günü yürümeye başlayabilirsiniz. Az sayıda uzun yürüyüş yerine kısa ve sık yürüyüşler yapın; dik durun ve süreyi kademeli artırın.", "Gün içinde sık sık")
_ex2("bfa_ankle", "apump", "Ayak bileği hareketleri", "Uzanırken ya da otururken ayak uçlarınızı kendinize doğru çekin, sonra aşağı doğru itin. Bacaklarınızda kan dolaşımını destekler.", "5–10 tekrar, günde 3–4 kez")

BFA_FAQ = [
 ("Ne zaman araba kullanabilirim?", "Ani frene basabildiğinizde ve yolculuk boyunca rahat oturabildiğinizde; bu genellikle en az 4–6 hafta sürer. Ağrınızın iyi kontrol altında olduğundan emin olun ve kesin zamanı cerrahınıza sorun."),
 ("İşe ne zaman dönerim?", "İşinize göre değişir. NHS genellikle 4–6 hafta diyor; bir NHS broşürüne göre masa başı işlere 6–8 hafta, ağır bedensel işlere en az 3 ay, bazen 6 ay sonra dönülebilir. Kararı cerrahınızla birlikte verin."),
 ("Spora ne zaman başlayabilirim?", "Bir NHS broşürüne göre yara iyileştikten sonra 4. haftadan itibaren serbest stil ya da sırtüstü yüzme, 4–6 haftadan itibaren bisiklet ve tempolu yürüyüş, 3 aydan itibaren golf ve hafif tenis yapılabilir. İlk 6 ay koşudan ve ağır yük kaldırmaktan kaçının."),
 ("Ameliyattan sonra egzersiz programı işe yarar mı?", "22 randomize çalışmayı ve 2.503 kişiyi inceleyen bir Cochrane derlemesine göre ameliyattan 4–6 hafta sonra başlayan egzersiz programları, kısa vadede ağrıyı ve günlük işlevi hiç tedavi almamaya göre daha çok iyileştirdi. Yoğun programlar hafiflerden biraz daha etkiliydi; gözetimli program ile evde yapılan program arasında fark yoktu. Hiçbir çalışmada egzersiz yeniden ameliyat oranını artırmadı. Kanıtın kalitesi düşük ile çok düşük arasında."),
 ("Bu kısıtlamalara uymak şart mı?", "Broşürlerdeki süreler genel önerilerdir ve cerrahtan cerraha değişir. Tek taraflı mikrodiskektomi olan 200 kişinin katıldığı ve 2026'da yayımlanan randomize bir çalışmada, ilk iki hafta oturma süresini, 5 kg'dan ağır kaldırmayı ve yorucu etkinliği kısıtlamak ile rahat ettiği ölçüde olağan etkinliğe dönmek arasında bir yılın sonunda fark bulunmadı; yeniden fıtıklaşma, ağrı, işlev ve yeniden ameliyat oranları benzerdi. Bu sonuç yalnızca bu ameliyat türü için geçerlidir, diğer omurga ameliyatlarına genellenemez. Size özel kısıtlamaları cerrahınıza sorun."),
 ("Hangi riskler var?", "Ciddi komplikasyonlar nadirdir. Bunlar arasında omurilik sıvısı sızıntısı, sinir hasarı, geçmeyen bel ağrısı ve omurların yerinden kayması sayılabilir; bazıları yeniden ameliyat gerektirebilir. Bacak ağrısı çoğu zaman hemen azalır, ama bel kaslarında bir süre sızı olabilir."),
]

BFA_SRC = [
 "NHS. " + ext("https://www.nhs.uk/tests-and-treatments/lumbar-decompression-surgery/", "Lumbar decompression surgery") + ". Page last reviewed: 10 March 2026.",
 "Royal Berkshire NHS Foundation Trust. " + ext("https://www.royalberkshire.nhs.uk/media/3o2oorsg/information-and-exercises-following-microdiscectomy_sep25.pdf", "Information and exercises following microdiscectomy") + ". September 2025.",
 "James Paget University Hospitals NHS Foundation Trust. " + ext("https://www.jpaget.nhs.uk/media/pcuj555q/ph-37-lumbar-discectomy-decompression-advice-v1-web.pdf", "Lumbar discectomy / decompression advice") + ". PH 37.",
 "Oosterhuis T, Costa LOP, Maher CG, de Vet HCW, van Tulder MW, Ostelo RWJG. " + ext("https://www.cochrane.org/CD003007/rehabilitation-after-lumbar-disc-surgery", "Rehabilitation after lumbar disc surgery") + ". Cochrane Database Syst Rev. 2014;(3):CD003007.",
 "Roadley J, Daly C, Rogers M, et al. " + ext("https://doi.org/10.1097/BRS.0000000000005720", "Lumbar microdiscectomy and post-operative activity restrictions: a randomised controlled trial") + ". Spine. 2026 (çevrimiçi 29 Nisan 2026).",
]

BFA_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Bel fıtığı ameliyatı sonrası</h1>
    <p class="lede">Bel fıtığı ameliyatı (mikrodiskektomi) oldunuz ya da olacak mısınız? Bu ameliyatta sinire baskı yapan disk parçası, küçük bir kesiden mikroskop yardımıyla çıkarılır. Bacak ağrısı çoğu zaman hemen azalır, ama bel kaslarında bir süre sızı olabilir. Ameliyattan sonraki haftalarda hareketli kalmak ve doğru egzersizler, iyileşmenin en önemli parçasıdır.</p>
    <p class="meta">Son güncelleme: 18 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>Ameliyat günü</b><span>Cerrahınız onaylarsa yürümeye başlanabilir</span></div>
        <div class="stat"><b>4–6 hafta</b><span>İşinize göre işe dönüş için genellikle gereken süre</span></div>
        <div class="stat"><b>6 hafta</b><span>Hastane broşürlerinde yük kaldırmaktan ve uzun süre öne eğilmekten kaçınma için önerilen süre</span></div>
        <div class="stat"><b>12 hafta</b><span>Tüm olağan etkinliklere dönmenin sürebileceği süre</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Günlük hayatta</h2>
        <ul class="dots">
          <li>Yataktan kalkarken önce yana dönün, bacaklarınızı yataktan sarkıtın, sonra elinizle ve dirseğinizle iterek doğrulun; doğrudan doğrulmayın.</li>
          <li>Beliniz ağrıdığında oturmak yerine uzanın: yüzüstü, dizlerinizin arasında yastıkla yan, ya da dizleriniz bükülü sırtüstü.</li>
          <li>Önce sert bir sandalyede kısa sürelerle oturun, süreyi kademeli artırın. Çökük oturmayın.</li>
          <li>Ani dönüşlerden ve ağır yük kaldırmaktan kaçının.</li>
        </ul>
      </div>
      <div>
        <h2>Akıllıca ilerleyin</h2>
        <ul class="dots">
          <li>Yeni bir etkinlikten sonra hafif sızı kabul edilebilir, şiddetli ağrı değil.</li>
          <li>Fazla yüklendiyseniz ve beliniz çok ağrıyorsa, ağrı yatışana kadar hafif egzersize ve yürüyüşe devam edin, sonra yeniden artırın.</li>
          <li>Ağrınızı hareket edebileceğiniz ölçüde kontrol altında tutun; egzersiz sırasında ağrıya zorlamayın.</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Ameliyat sonrası egzersiz</p>
      <h2>İlk haftalar için altı egzersiz</h2>
      <p class="soft">Egzersizleri günde 3–4 kez yapın. Cerrahınızın ya da fizyoterapistinizin size özel önerileri varsa önce onlara uyun. Belirtileriniz artarsa egzersizi bırakın ve ekibinize haber verin.</p>
      {ex_grid(["bfa_tra", "bfa_tilt", "bfa_prone", "bfa_slump", "bfa_walk", "bfa_ankle"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(BFA_FAQ)}
      <p class="soft" style="margin-top:18px">Ameliyat öncesi dönem ve ameliyatsız tedavi için <a href="bel-fitigi.html">bel fıtığı ve siyatik</a>, uzun süren bel ağrısı için <a href="bel-agrisi.html">bel ağrısı</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman acile ya da hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Kasıkta, iki bacak arasında ya da makat çevresinde uyuşma varsa (tuvalette silerken fark edilebilir)</li>
        <li>İdrar yapmakta zorlanıyorsanız ya da idrar veya dışkı kontrolünüzü kaybettiyseniz</li>
        <li>Bacaklarınızda ya da iki ayağınızda, ameliyattan öncekinden farklı yeni uyuşma, güçsüzlük ya da ağrı varsa</li>
        <li>Özellikle otururken artan şiddetli baş ağrısı ya da baş dönmesi varsa</li>
        <li>Yara çevresinde sıcaklık, kaşıntı, kızarıklık ya da akıntı varsa</li>
      </ul>
      <p class="soft">İlk üç durumda beklemeden acil servise başvurun. Diğerlerinde cerrahi ekibinize haber verin.</p>
      {CTA_CARD("Bel fıtığı ameliyatı sonrası rehabilitasyonunuz", "bel fıtığı ameliyatı sonrası rehabilitasyon")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(BFA_SRC)}
    </div>
  </section>
</main>'''

page("bel-fitigi-ameliyati-sonrasi.html", "Bel Fıtığı Ameliyatı Sonrası",
     "Bel fıtığı ameliyatından (mikrodiskektomi) sonra ne zaman yürünür, oturulur, araba kullanılır, işe ve spora dönülür? Uyarı işaretleri ve ilk haftalar için altı egzersiz.",
     "bel-fitigi-ameliyati-sonrasi.html", NECK_CSS, BFA_BODY, "",
     seo_title="Bel Fıtığı Ameliyatı Sonrası: İyileşme Süreci ve Egzersizler | İhsan Eren",
     condition="Mikrodiskektomi sonrası", faq_items=BFA_FAQ)

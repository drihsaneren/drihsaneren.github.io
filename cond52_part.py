# -*- coding: utf-8 -*-
# Yeni rehber (52): Köprücük kemiği kırığı. cond51_part.py'den sonra exec edilir. Video yok.
# Egzersizler East Sussex (Kasım 2025), Oxford (Ekim 2025) ve United Lincolnshire (Haziran 2025) NHS broşürlerine göre; sarkaç ve sopa çizimleri donuk omuz rehberinden.

_ex2("kl_post", "scap", "Dik duruş", "Askı takılıyken de yapabilirsiniz. Omuzlarınızı geriye alın ve kürek kemiklerinizi hafifçe birbirine yaklaştırın, gözleriniz karşıya baksın.", "20–30 saniye tutun, 5 tekrar")
_ex2("kl_elbow", "ly_arm", "Dirseği bükme ve açma", "Askıyı çıkarın. Dirseğinizi rahat ettiğiniz kadar bükün, sonra tam düzeltin. Diğer elinizle hafifçe yardım edebilirsiniz; ağrıya doğru zorlamayın.", "5 saniye tutun, 10 tekrar")
_ex2("kl_grip", "grip", "El ve parmaklar", "Elinizi açıp kapatın, sonra bileğinizi yukarı aşağı oynatın. Birkaç gün sonra yumuşak bir topu rahat edebildiğiniz kadar sıkın.", "Topu 5 saniye sıkın, 10 tekrar")
_ex2("kl_pend", "cf_pendf", "Sarkaç", "Askıyı çıkarın, sağlam elinizle bir masaya dayanıp öne eğilin. Kolunuzu gevşek bırakın ve gövdenizi hafifçe sallayarak kolunuzu öne arkaya ve yandan yana salınacak şekilde hareket ettirin.", "Toplam 1–2 dakika")
_ex2("kl_slide", "towel", "Masada kaydırma", "Masaya oturun, kollarınızı masadaki bir bezin üzerine koyun. Kollarınızı öne doğru kaydırın, sonra geri çekin. Masaya yaslanmayın ve ağırlık vermeyin; ilk iki hafta yalnızca omuz hizasına kadar ilerleyin.", "5–10 tekrar")
_ex2("kl_stick", "cf_stickf", "Sopa ile dışa döndürme", "3. haftadan sonra başlayın. Dirseğiniz gövdenize yapışık ve bükülü olsun. Bir sopayla ya da diğer elinizle kolunuzu dışa doğru itin.", "5 saniye tutun, 10 tekrar")

KL_FAQ = [
 ("Ameliyat gerekir mi?", "Nadiren. Köprücük kemiği kırıklarının çoğu kol askısı ve egzersizlerle iyileşir; ameliyat yalnızca çok kötü kırıklarda gerekir. Karar röntgen ve muayene sonrası hekiminizle birlikte verilir."),
 ("Kırık yerindeki şişlik kalıcı mı?", "Kırığın üzerinde bir tümsek oluşması beklenen bir durumdur. Bu tümsek 12 ay içinde küçülür, ama küçük bir tümsek kalabilir."),
 ("Ne zaman araba kullanabilirim?", "Bir NHS broşürüne göre kendinizi yeterli ve güvende hissediyorsanız 4. haftadan itibaren. Askıyı takarken araç kullanmayın."),
 ("Spora ne zaman dönebilirim?", "Bir NHS broşürüne göre kurbağalama yüzmeye 6–8 hafta, serbest stil yüzme ve golfe 3 ay, futbol, raket sporları ve binicilik gibi temas ve düşme riski olan sporlara 6 ay sonra dönülebilir. Ağır yük kaldırmaya en az 3 ay ara verin. Kesin süreyi hekiminiz belirler."),
 ("Çocuklarda iyileşme farklı mı?", "Evet, daha hızlıdır. Çocuklarda köprücük kemiği kırığı genellikle 3–4 haftada, yetişkinlerde 6–8 haftada iyileşir."),
]

KL_SRC = [
 "NHS. " + ext("https://www.nhs.uk/conditions/broken-collarbone/", "Broken collarbone") + ". Page last reviewed: 2 August 2023.",
 "East Sussex Healthcare NHS Trust. " + ext("https://www.esht.nhs.uk/wp-content/uploads/2026/01/2025.pdf", "Clavicle (collar bone) fracture (displaced)") + ". November 2025.",
 "Oxford University Hospitals NHS Foundation Trust. " + ext("https://www.ouh.nhs.uk/media/mlfjrk0i/116943clavicle.pdf", "Clavicle fracture") + ". October 2025.",
 "United Lincolnshire Teaching Hospitals NHS Trust. " + ext("https://www.ulh.nhs.uk/wp-content/uploads/2025/07/Clavicle-fracture.pdf", "Clavicle fracture") + ". ULHT-LFT-4054, June 2025.",
]

KL_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Köprücük kemiği kırığı</h1>
    <p class="lede">Düşerken omzunuzun ya da elinizin üzerine mi geldiniz, omzunuzda şişlik ve şekil değişikliği mi var? Köprücük kemiği kırıklarının çoğu ameliyatsız, kol askısıyla iyileşir. Yetişkinlerde iyileşme yaklaşık 6–8 hafta, çocuklarda 3–4 hafta sürer. Bu dönemde dirsek, el ve omuz egzersizleri tutukluğu önler ve kolunuzu yeniden kullanmanızı kolaylaştırır.</p>
    <p class="meta">Son güncelleme: 18 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>2–3 hafta</b><span>Kol askısının genellikle kullanıldığı süre</span></div>
        <div class="stat"><b>6–8 hafta</b><span>Yetişkinlerde iyileşme süresi</span></div>
        <div class="stat"><b>3–4 hafta</b><span>Çocuklarda iyileşme süresi</span></div>
        <div class="stat"><b>3 ay</b><span>Ağır yük kaldırmaya dönmeden önce beklenmesi önerilen en kısa süre</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Bir yaralanmadan sonra şiddetli omuz ağrısı.</li>
          <li>Şişlik ya da morluk.</li>
          <li>Omzun şeklinin değişmesi.</li>
          <li>Kolu normal kullanamama.</li>
        </ul>
      </div>
      <div>
        <h2>İlk anda ne yapmalı?</h2>
        <ul class="dots">
          <li>Kolunuzu bir havlu ya da bandajdan yapılmış askıyla destekleyin.</li>
          <li>Kanama varsa temiz bir havlu ya da bezle bastırın.</li>
          <li>Omzunuzu ve kolunuzu kullanmayın.</li>
          <li>Deriden dışarı çıkan bir kemik varsa ona dokunmayın.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>İyileşme döneminde neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Askıyı doğru kullanın</h3><p>İlk iki hafta gündüzleri askıyı takın; yalnızca egzersiz ve yıkanma için çıkarın. Gece takmak isteğe bağlıdır. İlk iki hafta dirseğinizi omuz hizasının üzerine kaldırmayın.</p></div>
        <div class="kind"><span class="n">2</span><h3>Buz ve ağrı kesici</h3><p>İlk 24–48 saatte havluya sarılı buzu iki saatte bir en fazla 20 dakika uygulayabilirsiniz. Hekiminize ya da eczacınıza danışarak düzenli ağrı kesici kullanabilirsiniz.</p></div>
        <div class="kind"><span class="n">3</span><h3>Rahat uyuyun</h3><p>Yastıklarla desteklenmiş, yarı oturur bir pozisyonda uyumak daha rahat olabilir. Kolunuzla gövdeniz arasına yumuşak bir yastık koyabilirsiniz.</p></div>
        <div class="kind"><span class="n">4</span><h3>Sigarayı bırakın</h3><p>Sigara kırığın kaynamasını yavaşlatır, uç durumlarda durdurabilir. İyileşme döneminde bırakmak kemiğinize iyi gelir.</p></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Kolu hareketli tutan altı egzersiz</h2>
      <p class="soft">İlk dört egzersize hemen, günde 3–5 kez başlayabilirsiniz. Masada kaydırma ve sopa ile dışa döndürme genellikle sonraki haftalarda eklenir. Hareketleri yavaş yapın; şiddetli ağrı olursa durun. 6. haftadan sonra, ağrının izin verdiği ölçüde kolunuzu baş üstüne kaldırmaya başlayabilirsiniz.</p>
      {ex_grid(["kl_post", "kl_elbow", "kl_grip", "kl_pend", "kl_slide", "kl_stick"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(KL_FAQ)}
      <p class="soft" style="margin-top:18px">Omzun yerinden çıkması için <a href="omuz-cikigi.html">omuz çıkığı</a>, kolda benzer bir iyileşme süreci için <a href="el-bilegi-kirigi.html">el bileği kırığı sonrası</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman acile ya da hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Omzunuzun şekli değiştiyse, omzunuz çok hızlı şiştiyse ya da kemik deriden dışarı çıktıysa</li>
        <li>Çok kanama varsa</li>
        <li>Nefes almakta zorlanıyorsanız, göğüs ağrınız varsa ya da kanlı öksürüyorsanız: hemen 112’yi arayın</li>
        <li>Kolunuzda uyuşma ya da karıncalanma varsa</li>
        <li>12. haftada hâlâ belirgin ağrınız ve tutukluğunuz varsa</li>
      </ul>
      {CTA_CARD("Köprücük kemiği kırığı sonrası rehabilitasyonunuz", "köprücük kemiği kırığı sonrası rehabilitasyon")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(KL_SRC)}
    </div>
  </section>
</main>'''

page("koprucuk-kemigi-kirigi.html", "Köprücük Kemiği Kırığı",
     "Köprücük kemiği kırığı ne kadar sürede iyileşir, askı ne kadar takılır, ne zaman araba kullanılır ve spora dönülür? İlk yardım, uyarı işaretleri ve evde altı egzersiz.",
     "koprucuk-kemigi-kirigi.html", NECK_CSS, KL_BODY, "",
     seo_title="Köprücük Kemiği Kırığı: İyileşme Süresi, Askı ve Egzersizler | İhsan Eren",
     condition="Köprücük kemiği kırığı", faq_items=KL_FAQ)

# -*- coding: utf-8 -*-
# Yeni rehber (56): Kasık zorlanması (addüktör zorlanması). cond55_part.py'den sonra exec edilir. Video yok.
# Berkshire Healthcare NHS (BH1165h, Şubat 2026 ve fizyoterapi broşürü), NHS sprains and strains (23 Nisan 2024), ELHT (2014) uyarı işaretleri.

# Sırtüstü, dizler bükülü, dizlerin arasında top sıkma
SV["ks_ball"] = fig(GRD +
    '<circle class="hd" cx="12" cy="100" r="7"/>'
    '<path class="fig" d="M22 107 H44"/>'
    '<path class="fig" d="M20 104 L58 104 L76 84 L86 108"/>'
    f'<ellipse cx="78" cy="76" rx="7" ry="7" fill="#C8963E"><animate attributeName="rx" values="7;4.5;7" dur="3.2s" repeatCount="indefinite"/></ellipse>'
    '<path d="M64 70 l6 6 l-6 6 M92 70 l-6 6 l6 6" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"><animate attributeName="opacity" values=".3;1;.3" dur="3.2s" repeatCount="indefinite"/></path>',
    "Top sıkma")
# Köprü + dizler arasında top
SV["ks_bridge"] = fig(GRD +
    '<circle class="hd" cx="12" cy="100" r="7"/>'
    '<path class="fig" d="M22 107 H44"/>'
    f'<path class="fig hl" d="M20 104 L58 104 L76 84 L86 108">{anim_d("M20 104 L58 104 L76 84 L86 108;M20 104 L58 86 L78 82 L86 108;M20 104 L58 104 L76 84 L86 108")}</path>'
    f'<g>{anim_t("0 0;2 -2;0 0")}<circle cx="78" cy="76" r="6" fill="#C8963E"/></g>',
    "Toplu köprü")
# Yan yatarak alttaki bacağı kaldırma (üstteki bacak önde, ayak yerde)
SV["ks_low"] = fig(GRD +
    '<circle class="hd" cx="12" cy="98" r="7"/>'
    '<path class="fig" d="M20 100 L58 102"/>'
    '<path class="fig" d="M58 100 L70 80 L78 110" opacity=".55"/>'
    f'<path class="fig hl" d="M58 104 L104 106">{anim_d("M58 104 L104 106;M58 104 L102 92;M58 104 L104 106")}</path>',
    "Alttaki bacağı kaldırma")
# Ayakta lastik bantla bacağı içe çekme (önden)
SV["ks_band"] = fig(GRD +
    '<path class="obj" d="M112 60 V112"/>'
    '<circle class="hd" cx="56" cy="20" r="8"/>'
    '<path class="fig" d="M56 30 V80 M56 42 L42 62 M56 42 L70 62 M56 80 L48 112"/>'
    f'<path class="fig hl" d="M56 80 L80 110">{anim_d("M56 80 L80 110;M56 80 L62 111;M56 80 L80 110")}</path>'
    f'<path class="band" d="M112 104 L80 110" fill="none">{anim_d("M112 104 L80 110;M112 104 L62 111;M112 104 L80 110")}</path>',
    "Bantla içe çekme")

_ex2("ks_sq", "ks_ball", "Dizlerle top sıkma", "Sırtüstü uzanın, dizleriniz bükülü, ayaklarınız dizlerinizle aynı hizada olsun. Dizlerinizin arasına bir top ya da yastık koyun ve dizlerinizi birbirine bastırarak nazikçe sıkın.", "5 saniye tutun, 10–20 tekrar, günde 2 kez")
_ex2("ks_br", "ks_bridge", "Toplu köprü", "Aynı pozisyonda, dizlerinizin arasında top ya da yastık varken kalça ve karın kaslarınızı sıkarak kalçanızı kaldırın. Yukarı çıkarken topu da hafifçe sıkın, birkaç saniye tutup yavaşça inin.", "10–20 tekrar, günde 2 kez")
_ex2("ks_lo", "ks_low", "Alttaki bacağı kaldırma", "Ağrılı tarafınızın üzerine yan yatın. Üstteki bacağınızı dizden bükerek öne, yere koyun; alttaki bacağınız düz kalsın. Kalçanızı sabit tutarak alttaki bacağınızı yukarı kaldırın, 5 saniye tutup indirin.", "10–20 tekrar, günde 2 kez")
_ex2("ks_bd", "ks_band", "Lastik bantla bacağı içe çekme", "Lastik bandı sabit bir yere bağlayın ve ağrılı bacağınızın ayak bileğine geçirin. Bacağınız yana açıkken dizleriniz birbirine değene kadar bacağınızı içe çekin, yavaşça geri bırakın.", "10–12 tekrar, günde 2–3 kez")

KS_FAQ = [
 ("Egzersiz yaparken ağrı olursa ne yapmalıyım?", "Hafif bir rahatsızlık kabul edilebilir, ama egzersizler belirtilerinizi belirgin şekilde artırmamalı. Bir egzersiz çok ağrıtıyorsa tekrar sayısını ya da sıklığını azaltın; yine de ağrıtıyorsa bırakın ve bir hekime ya da fizyoterapiste danışın."),
 ("Buz mu, sıcak mı?", "İlk 2–3 günde buz kullanın: nemli bir havluya sarılı buzu ya da donmuş bezelye paketini 15–20 dakika, 2–3 saatte bir uygulayın; buz yanığına dikkat edin. Bu dönemde sıcak banyo, sıcak uygulama, alkol ve masajdan kaçının; şişliği artırabilirler."),
 ("Ne zaman koşabilirim, spora dönebilirim?", "Zorlanmaların çoğu yaklaşık 2 haftada belirgin şekilde düzelir. Yeniden zarar görmemek için koşu gibi zorlu egzersizlerden 8 haftaya kadar kaçınmanız önerilir; ciddi zorlanmaların iyileşmesi aylar sürebilir. Spora, ağrısız yürüyebildiğinizde ve gücünüz neredeyse tamamen geri döndüğünde, bir fizyoterapistle birlikte kademeli dönmek en güvenlisidir."),
 ("Koltuk değneği kullanmalı mıyım?", "Gerekirse ilk birkaç gün kısa süreliğine koltuk değneği ya da başka bir yürüme yardımcısı kullanabilirsiniz. Rahat ettikçe bacağınızı korurken nazikçe hareket ettirmeye başlayın; erken ve hafif hareket iyileşmeyi destekler, tutukluğu ve güç kaybını önler."),
]

KS_SRC = [
 "Berkshire Healthcare NHS Foundation Trust. " + ext("https://www.berkshirehealthcare.nhs.uk/media/w13npqcr/bh1165h-groin-strain-v1-feb-2026.pdf", "Groin strain") + ". BH1165h, version 1.0, February 2026.",
 "Berkshire Healthcare NHS Foundation Trust, Physiotherapy. " + ext("https://www.berkshirehealthcare.nhs.uk/media/109514456/groin-strain-physio-leaflet-berkshire-healthcare.pdf", "Groin strain: exercises") + ".",
 "NHS. " + ext("https://www.nhs.uk/conditions/sprains-and-strains/", "Sprains and strains") + ". Page last reviewed: 23 April 2024.",
 "East Lancashire Hospitals NHS Trust, Integrated Musculoskeletal Service. " + ext("https://elht.nhs.uk/download_file/view/577", "Groin pain: patient information and exercises") + ". November 2014.",
]

KS_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Kasık zorlanması</h1>
    <p class="lede">Futbolda ani bir yön değiştirme, dönme ya da tekme atma ya da ıslak zeminde kayma sırasında kasıkta veya iç uylukta ağrı mı başladı? Bu genellikle iç uyluk kaslarının fazla gerilmesiyle olan bir kasık zorlanmasıdır. İlk günlerde doğru bakım ve ardından kademeli güçlendirme egzersizleriyle çoğu kişi birkaç hafta içinde belirgin şekilde düzelir.</p>
    <p class="meta">Son güncelleme: 19 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>48–72 saat</b><span>İlk bakım dönemi; egzersizlere bundan sonra başlanır</span></div>
        <div class="stat"><b>2 hafta</b><span>Zorlanmaların çoğunun belirgin şekilde düzeldiği süre</span></div>
        <div class="stat"><b>8 hafta</b><span>Koşu gibi zorlu egzersizlerden kaçınma süresi</span></div>
        <div class="stat"><b>5–7 gün</b><span>Hâlâ yürümekte zorlanıyorsanız hekime başvurun</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Kasıkta ve iç uylukta ağrı ve hassasiyet.</li>
          <li>Hızlı ya da güçlü bacak hareketlerinde ağrı.</li>
          <li>Dizinizi kaldırırken ya da merdiven çıkarken ağrı.</li>
          <li>Kasıkta sıcaklık; kasıkta ya da iç uylukta morluk veya şişlik.</li>
        </ul>
      </div>
      <div>
        <h2>İlk 48–72 saatte</h2>
        <ul class="dots">
          <li><strong>Koruma:</strong> Bölgeyi dinlendirin; gerekirse kısa süre koltuk değneği kullanın.</li>
          <li><strong>Erken ve hafif hareket:</strong> Rahat ettiğiniz ölçüde bacağınızı nazikçe hareket ettirin; tutukluğu ve güç kaybını önler.</li>
          <li><strong>Buz:</strong> Nemli havluya sarılı buzu 15–20 dakika, 2–3 saatte bir uygulayın.</li>
          <li><strong>Bandaj ve yükseltme:</strong> Sıkı değil, rahat saran elastik bir bandaj kullanın; dinlenirken bacağınızı kalça hizasına kaldırın.</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>İç uyluğu güçlendiren dört egzersiz</h2>
      <p class="soft">İlk 48–72 saatten sonra başlayın. Az ve sık yapın; hafif rahatsızlık olabilir, ama egzersizler ağrınızı belirgin şekilde artırmamalı. Rahatladıkça tekrar sayısını artırın.</p>
      {ex_grid(["ks_sq", "ks_br", "ks_lo", "ks_bd"], "ex four")}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(KS_FAQ)}
      <p class="soft" style="margin-top:18px">Uyluğun arkasındaki zorlanma için <a href="arka-uyluk-zorlanmasi.html">arka uyluk zorlanması</a>, kasıkta derin ve uzun süren ağrı için <a href="kalca-sikismasi.html">kalça sıkışması</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Yaralanma anında bir çatırtı duyduysanız, bacağınızın şekli değiştiyse, uyuşma ya da karıncalanma varsa ya da cilt mavi, gri veya soğuk görünüyorsa: hemen acil servise</li>
        <li>Ağrı şiddetliyse ya da giderek artıyorsa, bacağınıza hiç yük veremiyorsanız</li>
        <li>Kasıkta ele gelen bir şişlik ya da testislerde ağrı veya şişlik varsa</li>
        <li>Ateş, gece terlemesi ya da kendinizi hasta hissetme varsa</li>
        <li>5–7 gün sonra hâlâ yürümekte zorlanıyorsanız ya da hiç düzelme yoksa</li>
        <li>6–8 hafta içinde belirtileriniz geçmediyse: bir fizyoterapiste başvurabilirsiniz</li>
      </ul>
      {CTA_CARD("Kasık zorlanması sonrası rehabilitasyonunuz", "kasık zorlanması sonrası rehabilitasyon")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(KS_SRC)}
    </div>
  </section>
</main>'''

page("kasik-zorlanmasi.html", "Kasık Zorlanması",
     "Kasıkta ve iç uylukta ağrı neden olur, ilk günlerde ne yapılmalı, ne zaman koşuya ve spora dönülür? Uyarı işaretleri ve iç uyluğu güçlendiren dört egzersiz.",
     "kasik-zorlanmasi.html", NECK_CSS, KS_BODY, "",
     seo_title="Kasık Zorlanması: İlk Bakım, Egzersizler ve Spora Dönüş | İhsan Eren",
     condition="Kasık zorlanması", faq_items=KS_FAQ)

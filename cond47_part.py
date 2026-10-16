# -*- coding: utf-8 -*-
# Yeni rehber (47): Kübital tünel sendromu (dirsekte ulnar sinir sıkışması). cond46_part.py'den sonra exec edilir. Video yok.
# Egzersizler East Kent Hospitals (2025) ve NHS Scotland Right Decision Service sayfasına göre.

# Ulnar sinir kaydırma (önden): kol yana açık, bilek geriye bükülü (el yukarı); dirsek bükülerek el başa doğru gelir.
SV["uglide"] = fig(GRD +
    '<path class="fig" d="M48 40 H80 M64 40 V80 M64 80 L56 112 M64 80 L72 112 M80 40 L84 62 L82 78"/>'
    '<path class="fig" d="M64 40 V30"/><circle class="hd" cx="64" cy="21" r="8"/>'
    '<path class="fig hl" d="M48 40 H30"/>'
    f'<g>{anim_t("0 30 40;0 30 40;110 30 40;110 30 40;0 30 40", dur="5s", kt="0;0.2;0.45;0.75;1", typ="rotate")}'
    '<path class="fig hl" d="M30 40 H12 V30"/></g>',
    "Ulnar sinir kaydırma")

_ex2("cu_glide", "uglide", "Ulnar sinir kaydırma", "Kolunuzu yana açın, avucunuz yere baksın. Bileğinizi geriye bükerek parmaklarınızı tavana çevirin ve 10 saniye tutun. Sonra dirseğinizi bükerek elinizi başınıza doğru getirin ve 10 saniye tutun. Dirseğinizi ve bileğinizi düzelterek başlangıca dönün. Serçe parmağınıza doğru hafif bir çekilme hissedebilirsiniz, ama ağrı olmamalı.", "3 tekrarla başlayın, günde en fazla 3 kez; rahatladıkça 5’e, en çok 10’a çıkın")
_ex2("cu_roll", "ly_shrug", "Omuz çevirme", "Dik oturun ya da ayakta durun, omuzlarınız gevşek olsun. Omuzlarınızı yavaşça yukarı, geriye ve aşağıya doğru yuvarlak bir hareketle çevirin.", "10 tekrar, günde 5 kez")

CU_FAQ = [
 ("Karpal tünel sendromundan farkı ne?", "Karpal tünel sendromunda bilekteki median sinir sıkışır ve daha çok başparmak, işaret ve orta parmak uyuşur. Kübital tünel sendromunda ise dirsekteki ulnar sinir etkilenir; uyuşma serçe parmakta ve yüzük parmağının serçe parmak tarafındaki yarısındadır."),
 ("Gece ateli işe yarar mı?", "Dirseği gece daha düz tutmak sinirin gerilmesini azaltır. Bir NHS broşürü, atelin ya da havlu sargısının 6–8 hafta her gece kullanılmasını, düzelme sürüyorsa 12 haftaya kadar devam edilmesini öneriyor. Hafif ve orta düzeyde belirtisi olan 51 kişide yapılan küçük bir araştırmada ise yalnızca yazılı bilgilendirme, iş etkinliklerini iyileştirmede ve gece ağrısını azaltmada atel ya da sinir kaydırma eklemek kadar etkili bulundu; kanıtın kalitesi düşük."),
 ("Kortizon iğnesi yardımcı olur mu?", "55 kişilik bir araştırmada kortizon iğnesi 3. ayda plaseboya göre fark yaratmadı: olumlu sonuç oranı iğne grubunda %28, plasebo grubunda %30’du."),
 ("Ameliyat ne zaman gerekir?", "Belirtiler ağırsa ya da atel, öneriler ve egzersizlere rağmen ilerliyorsa ameliyat düşünülebilir. Ameliyatın asıl amacı güçsüzlüğün ve kas erimesinin ilerlemesini önlemektir. Araştırmalarda sinir üzerindeki dokuyu gevşetmek ile siniri yerinden taşımak benzer sonuç verdi (6–12 ayda yaklaşık %70’e karşı %75 düzelme); siniri taşımada yara enfeksiyonu daha sıktı."),
 ("Ameliyattan sonra ne zaman işe dönerim?", "Bir NHS broşürüne göre hafif işlere 1–2 hafta, ağır işlere yaklaşık 3–6 hafta sonra dönülebilir; ilk 4 hafta ağır kaldırma ve sıkı kavramadan kaçınılır. Uyuşma çoğu zaman düzelir ama bu yavaş olabilir; güç kaybının toparlanması da zaman alır ve tam olmayabilir."),
]

CU_SRC = [
 "East Kent Hospitals University NHS Foundation Trust. " + ext("https://leaflets.ekhuft.nhs.uk/cubital-tunnel-syndrome/html", "Cubital tunnel syndrome") + ". Web 597, last reviewed March 2025.",
 "Royal Berkshire NHS Foundation Trust. " + ext("https://royalberkshire.nhs.uk/media/svmk5mdd/cubital-tunnel-syndrome_jan24.pdf", "Cubital tunnel syndrome") + ". January 2024.",
 "Right Decision Service, NHS Scotland. " + ext("https://www.rightdecisions.scot.nhs.uk/media/dscm3fzw/cubital-tunnel-syndrome.pdf", "Cubital tunnel syndrome") + ".",
 "Caliandro P, La Torre G, Padua R, Giannini F, Padua L. " + ext("https://pmc.ncbi.nlm.nih.gov/articles/PMC6734129/", "Treatment for ulnar neuropathy at the elbow") + ". Cochrane Database Syst Rev. 2016;(11):CD006839.",
]

CU_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Kübital tünel sendromu (dirsekte sinir sıkışması)</h1>
    <p class="lede">Serçe parmağınız ve yüzük parmağınızın yarısı uyuşuyor ya da karıncalanıyor mu; özellikle sabah uyandığınızda ya da telefonla uzun konuştuktan sonra? Dirseğin iç yanından geçen ulnar sinir sıkıştığında ya da tahriş olduğunda kübital tünel sendromu ortaya çıkar. Çoğu kişide dirseği uzun süre bükülü tutmamak ve geceleri dirseği düz tutmak gibi basit önlemlerle belirtiler yatışır.</p>
    <p class="meta">Son güncelleme: 16 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>Gece ve sabah</b><span>Belirtilerin en sık görüldüğü zamanlar</span></div>
        <div class="stat"><b>6–8 hafta</b><span>Gece ateli ya da havlu sargısının önerilen kullanım süresi</span></div>
        <div class="stat"><b>%28</b><span>Kortizon iğnesinde olumlu sonuç oranı; plaseboda %30</span></div>
        <div class="stat"><b>%70</b><span>Ameliyatla siniri gevşetenlerde 6–12 ayda düzelme oranı</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Serçe parmakta ve yüzük parmağının yarısında gelip giden karıncalanma ve uyuşma.</li>
          <li>Dirseğin iç yanında ağrı.</li>
          <li>Belirtiler çoğu zaman gece ya da sabah uyanınca olur; ilerledikçe sıklaşır.</li>
          <li>Ağır durumlarda elin sırtında, başparmak ile işaret parmağı arasında kas erimesi ve kavramada güçsüzlük: kavanoz açmak ya da kapı kolunu çevirmek zorlaşır.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Çoğu zaman belirgin bir neden yoktur.</li>
          <li>Dirseği iş ya da hobi nedeniyle tekrar tekrar bükmek ya da uzun süre bükülü tutmak, örneğin uyurken ya da telefonla konuşurken.</li>
          <li>Dirseğe darbe ya da eski bir dirsek kırığı.</li>
          <li>Fazla kilo, kireçlenme, şeker hastalığı ve tiroidin az çalışması riski artırır.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Geceleri dirseği düz tutun</h3><p>Katlanmış bir el havlusunu dirseğinize sarıp çok sıkmadan bantlayabilir ya da eczaneden bir dirsek ateli alabilirsiniz. Düzelme birkaç hafta sürebilir.</p></div>
        <div class="kind"><span class="n">2</span><h3>Dirseğe yaslanmayın</h3><p>Dirseğinizin iç yanına yaslanmaktan ve baskı yapmaktan kaçının. Sinirin üzerine gelen bir dirsek pedi işe yarayabilir.</p></div>
        <div class="kind"><span class="n">3</span><h3>Bükülü kalmayı azaltın</h3><p>Telefonda kulaklık kullanın, klavyeyi masanın kenarına yakın tutun. Sık ara verin, el pozisyonunuzu değiştirin ve tuttuğunuz şeyleri sıkı kavramayın.</p></div>
        <div class="kind"><span class="n">4</span><h3>Bilgi de tedavidir</h3><p>Belirtileri artıran pozisyonları bilmek ve değiştirmek, erken dönemde en önemli tedavidir. Çoğu kişi basit önerilerle düzelir; ameliyat nadiren gerekir.</p></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Sinire iyi gelen iki egzersiz</h2>
      <p class="soft">Egzersiz sırasında hafif bir rahatsızlık olabilir, ama kısa sürede geçmeli. Belirtileriniz artarsa tekrar sayısını azaltın ya da egzersizi bırakıp bir uzmana danışın.</p>
      {ex_grid(["cu_glide", "cu_roll"], "ex four")}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(CU_FAQ)}
      <p class="soft" style="margin-top:18px">Başparmak ve ilk parmaklarda uyuşma için <a href="karpal-tunel-sendromu.html">karpal tünel sendromu</a>, dirseğin iç yanında kirişe bağlı ağrı için <a href="golfcu-dirsegi.html">golfçü dirseği</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Belirtileriniz düzelmeyi bıraktıysa ya da sürekli hale geldiyse</li>
        <li>Elinizde güçsüzlük ya da kas erimesi fark ettiyseniz</li>
        <li>Serçe ve yüzük parmağınız kıvrılıyor ve düzeltmekte zorlanıyorsanız</li>
        <li>Egzersizler belirtilerinizi artırıyorsa</li>
      </ul>
      {CTA_CARD("Dirseğinizdeki sinir sıkışması", "kübital tünel sendromu")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(CU_SRC)}
    </div>
  </section>
</main>'''

page("kubital-tunel-sendromu.html", "Kübital Tünel Sendromu (Dirsekte Sinir Sıkışması)",
     "Serçe ve yüzük parmağınız mı uyuşuyor? Kübital tünel sendromu nedir, gece ateli işe yarar mı, ameliyat ne zaman gerekir? Uyarı işaretleri ve evde iki egzersiz.",
     "kubital-tunel-sendromu.html", NECK_CSS, CU_BODY, "",
     seo_title="Kübital Tünel Sendromu: Serçe Parmakta Uyuşma, Gece Ateli ve Egzersizler | İhsan Eren",
     condition="Kübital tünel sendromu", faq_items=CU_FAQ)

# -*- coding: utf-8 -*-
# Yeni rehber (35): Arka uyluk zorlanması (hamstring). cond34_part.py'den sonra exec edilir. Video yok.
# Yeni çizim: Nordic hamstring. Diğerleri hazır çizimler (hslide, bridge, lc_ham, hinge, walk).

SV["hs_nordic"] = fig(GRD +
    '<rect class="obj" x="8" y="98" width="20" height="8" rx="2" fill="#B9CBC6" stroke="none"/>'
    '<path class="fig" d="M44 110 L14 110"/>'
    f'<g>{anim_t("0 44 110;48 44 110;48 44 110;0 44 110", dur="5.6s", kt="0;0.55;0.7;1", typ="rotate")}'
    '<path class="fig hl" d="M44 110 L44 78"/><path class="fig" d="M44 78 L44 48 M44 54 L56 60 L50 66"/>'
    '<circle class="hd" cx="45" cy="38" r="8"/></g>'
    '<path d="M86 30 Q100 54 92 80 M88 74 L92 80 L97 75" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "Nordic hamstring")

_ex2("hs_slide", "hslide", "Topuk kaydırma", "Sırtüstü yatın. Topuğunuzu yerde ya da yatakta kaydırarak kalçanıza doğru çekin ve dizinizi rahat ettiğiniz kadar bükün, sonra yavaşça düzeltin. İlk günlerde uyluğun arkasını ağrıtmadan çalıştırmanın kolay bir yoludur.", "10 tekrar, günde 2–3 kez")
_ex2("hs_bridge", "bridge", "Köprü", "Sırtüstü yatın, dizleriniz bükülü, ayaklarınız yerde. Topuklarınızı yere bastırıp kalçanızı sıkarak kaldırın; omuzlarınızdan dizlerinize kadar düz bir çizgi oluşsun. 3–5 saniye bekleyip yavaşça inin. Kolaylaşınca ayaklarınızı biraz daha uzağa koyabilirsiniz.", "10–15 tekrar, 2–3 set")
_ex2("hs_stretch", "lc_ham", "Sandalyede arka uyluk germe", "Ağrı azalmaya başlayınca, birkaç gün sonra başlayabilirsiniz. Sandalyenin ön kenarına oturun, bir bacağınızı öne uzatın, topuğunuz yerde olsun. Sırtınızı düz tutarak kalçanızdan hafifçe öne eğilin; yalnızca hafif bir gerginlik hissedin, ağrıya kadar zorlamayın.", "20–30 saniye, 2–3 kez")
_ex2("hs_hinge", "hinge", "Kalçadan eğilme", "Ayaklarınız kalça genişliğinde açık, dizleriniz hafif bükülü olsun. Sırtınızı düz tutarak gövdenizi kalçanızdan öne doğru eğin, uyluk arkanızda gerginlik hissedince kalçanızı sıkarak doğrulun. Ağrısız oldukça zamanla elinize hafif bir ağırlık alabilirsiniz.", "10 tekrar, 2–3 set")
_ex2("hs_walk", "walk", "Yürüyüş ve bisiklet", "Ağrı izin verdikçe kısa ve rahat yürüyüşlerle başlayın; sabit bisiklet de iyi bir seçenektir. Süreyi gün gün artırın. Koşu ve sprinti, kaslarınız yeterince güçlenene kadar erteleyin.", "10–20 dakika, her gün")
EXT["hs_nordic"] = ("Nordic hamstring", "Yalnızca iyileştikten sonra, sakatlığı önlemek için. Dizlerinizin altına yastık koyup diz çökün; bir yardımcı ayak bileklerinizi tutsun ya da topuklarınızı koltuğun altına sabitleyin. Gövdeniz dik ve kalçanız düz kalarak kendinizi olabildiğince yavaş öne bırakın, ellerinizle yere düşüşünüzü karşılayın, sonra ellerinizle itip başlangıca dönün.", "Haftada 1–2 kez, 2–3 set × 3–6 tekrar")

HS_FAQ = [
 ("Ne kadar sürede iyileşir?", "Yaralanmanın şiddetine göre günler, haftalar ya da aylar sürebilir. Hafif zorlanmalarda kas gücü genellikle korunur; kısmi yırtıklarda güç kaybı ve morarma olabilir. Tam yırtılan bir arka uyluk kasının iyileşmesi birkaç ay sürebilir. Birçok kişinin en az birkaç hafta spora ara vermesi gerekir."),
 ("İlk günlerde masaj ya da sıcak uygulama yapılır mı?", "İlk 72 saatte sıcak uygulama, alkol, koşu ve masajdan kaçınmanız önerilir. Bu dönemde dinlenme, buz, hafif bası ve bacağı yükseltme önerilir."),
 ("Ne zaman spora dönebilirim?", "Arka uyluk kaslarınız yeterince güçlendiğinde. Erken dönmek yaralanmayı kötüleştirebilir, çok uzun süre hareketsiz kalmak da kasın zayıflamasına ve iz dokusuna yol açabilir. Dönüş zamanını bir fizyoterapist ya da hekimle birlikte belirlemek en güvenlisidir. 2023 tarihli uluslararası bir uzman uzlaşısına göre rehabilitasyonda ilerlemenin en önemli ölçütü ağrıdır; sprint ağrısız yapılabilmeli ve spora dönmeden önce kısıtlamasız tam antrenmanlar tamamlanmalıdır. İsveç’te 75 elit futbolcuyla yapılan bir çalışmada, kası uzarken çalıştıran egzersizlere dayalı programla sahaya dönüş ortalama 28 gün, geleneksel programla 51 gün sürdü."),
 ("Tekrarlamasını nasıl önlerim?", "Daha önce arka uyluğunu sakatlamış olanlarda yeniden sakatlanma riski yüksektir. Egzersiz öncesi ısınma, düzenli germe ve güçlendirme yardımcı olabilir. 8.459 sporcuyu kapsayan bir derlemede, Nordic hamstring egzersizini içeren programlar arka uyluk sakatlıklarını yaklaşık yarıya indirdi."),
]

HS_SRC = [
 "nidirect. " + ext("https://nidirect.gov.uk/conditions/hamstring-injury-muscle-strain", "Hamstring injury (muscle strain)") + ". Last updated 19 December 2024.",
 "van Dyk N, Behan FP, Whiteley R. " + ext("https://bjsm.bmj.com/content/53/21/1362", "Including the Nordic hamstring exercise in injury prevention programmes halves the rate of hamstring injuries: a systematic review and meta-analysis of 8459 athletes") + ". British Journal of Sports Medicine. 2019;53(21):1362.",
 "Paton BM, Read P, van Dyk N, et al. " + ext("https://bjsm.bmj.com/content/57/5/278", "London International Consensus and Delphi study on hamstring injuries part 3: rehabilitation, running and return to sport") + ". Br J Sports Med. 2023;57(5):278.",
 "NHS. " + ext("https://www.nhs.uk/conditions/hamstring-injury", "Hamstring injury") + ". Page last reviewed 28 July 2025",
 "Askling CM, Tengvar M, Thorstensson A. " + ext("https://bjsm.bmj.com/content/47/15/953", "Acute hamstring injuries in Swedish elite football: a prospective randomised controlled clinical trial comparing two rehabilitation protocols") + ". Br J Sports Med. 2013;47(15):953–959.",
]

HS_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Arka uyluk zorlanması (hamstring sakatlığı)</h1>
    <p class="lede">Koşarken, sprint atarken ya da ani bir hamlede uyluğunuzun arkasında keskin bir ağrı mı hissettiniz? Arka uyluk sakatlığı, uyluğun arkasındaki büyük kasların ya da kirişlerinin aşırı gerilip zorlanması ya da yırtılmasıdır. Hafif zorlanmalar birkaç günde toparlanabilir; daha ciddi yırtıklar haftalar ya da aylar sürebilir. Doğru zamanda başlanan kademeli egzersiz, hem iyileşmeyi hem de tekrarlamayı önlemeyi destekler.</p>
    <p class="meta">Son güncelleme: 27 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>48–72 saat</b><span>İlk dönem: dinlenme, buz, hafif bası ve bacağı yükseltme</span></div>
        <div class="stat"><b>15–20 dakika</b><span>Islak havluya sarılı buzun, gündüz 2–3 saatte bir uygulama süresi</span></div>
        <div class="stat"><b>3 derece</b><span>Hafif zorlanmadan tam yırtığa kadar şiddet</span></div>
        <div class="stat"><b>~%50</b><span>Nordic hamstring içeren programlarla sakatlık oranındaki azalma</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler ve şiddet</h2>
        <ul class="dots">
          <li><b>1. derece (hafif zorlanma):</b> Uyluğun arkasında ani ağrı ve hassasiyet, bacağı hareket ettirince ağrı; kas gücü genellikle korunur.</li>
          <li><b>2. derece (kısmi yırtık):</b> Daha fazla ağrı ve hassasiyet, şişlik ve morarma olabilir, bacakta bir miktar güç kaybı.</li>
          <li><b>3. derece (ciddi yırtık):</b> Çok ağrılı, şiş ve morarmış; yaralanma anında “pat” diye bir his olabilir ve bacak kullanılamaz.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Kas ya da kiriş sınırının ötesinde gerildiğinde.</li>
          <li>En sık sprint, hamle ve sıçrama gibi ani, patlayıcı hareketlerde.</li>
          <li>Zamanla yavaş yavaş aşırı gerilmeyle de olabilir.</li>
          <li>Daha önce arka uyluğunu sakatlamış olanlarda tekrar sık görülür.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>İlk 2–3 gün</h2>
        <ul class="dots">
          <li><b>Koruyun ve dinlendirin:</b> İlk 48–72 saat zorlayıcı hareketlerden kaçının.</li>
          <li><b>Buz:</b> Islak havluya sarılı buzu gündüz 2–3 saatte bir 15–20 dakika uygulayın; uyurken bırakmayın.</li>
          <li><b>Bası ve yükseltme:</b> Sıkmayan elastik bir bandaj kullanabilir (uyumadan önce çıkarın), bacağınızı yastıkla yükseltebilirsiniz.</li>
          <li><b>Kaçının:</b> İlk 72 saat sıcak uygulama, alkol, koşu ve masaj.</li>
          <li><b>Ağrı kesici:</b> Kullanmanız gerekip gerekmediğini ve hangisinin size uygun olduğunu hekiminize sorun.</li>
        </ul>
      </div>
      <div>
        <h2>Sonrasında</h2>
        <ul class="dots">
          <li>Ağrı azalmaya başlayınca, birkaç gün sonra hafif germelere başlayabilirsiniz.</li>
          <li>Ardından yürüyüş, bisiklet ve arka uyluk güçlendirme egzersizleri gelir.</li>
          <li>Çok erken zorlamak yaralanmayı kötüleştirebilir; çok uzun hareketsiz kalmak da kasın zayıflamasına ve iz dokusuna yol açabilir.</li>
          <li>Tam aktiviteye, arka uyluk kaslarınız yeterince güçlendiğinde dönün.</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Arka uyluğu güçlendiren altı egzersiz</h2>
      <p class="soft">Sıralama kolaydan zora doğrudur. Hareketleri ağrısız ya da çok hafif ağrılı bir aralıkta yapın; ağrı ertesi gün artıyorsa bir önceki seviyeye dönün. Son egzersiz yalnızca tam iyileştikten sonra, tekrarlamayı önlemek içindir.</p>
      {ex_grid(["hs_slide", "hs_bridge", "hs_stretch", "hs_walk", "hs_hinge", "hs_nordic"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(HS_FAQ)}
      <p class="soft" style="margin-top:18px">Kalça ve diz çevresindeki diğer spor sakatlıkları için <a href="kalca-sikismasi.html">kalça sıkışması</a> ve <a href="atlet-dizi.html">atlet dizi</a> rehberlerine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Yaralanmanın ciddi olduğunu düşünüyorsanız</li>
        <li>İyileşmiyor ya da belirtiler kötüleşiyorsa</li>
        <li>Yaralanma anında “pat” diye bir his olduysa, bacağınızı kullanamıyorsanız ya da geniş bir morarma ve şişlik varsa (ciddi yırtık olabilir)</li>
        <li>Yaralanmayla ilgili herhangi bir kaygınız varsa</li>
      </ul>
      {CTA_CARD("Arka uyluk sakatlığınız", "arka uyluk zorlanması")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(HS_SRC)}
    </div>
  </section>
</main>'''

page("arka-uyluk-zorlanmasi.html", "Arka Uyluk Zorlanması (Hamstring Sakatlığı)",
     "Koşarken uyluğunuzun arkasında keskin ağrı mı oldu? Arka uyluk zorlanmasının dereceleri, ilk 72 saatte yapılacaklar, spora dönüş ve tekrarlamayı önleyen Nordic hamstring dahil altı egzersiz.",
     "arka-uyluk-zorlanmasi.html", NECK_CSS, HS_BODY, "",
     seo_title="Arka Uyluk Zorlanması (Hamstring Sakatlığı): Tedavi, Spora Dönüş ve Egzersizler | İhsan Eren",
     condition="Arka uyluk (hamstring) zorlanması", faq_items=HS_FAQ)

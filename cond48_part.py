# -*- coding: utf-8 -*-
# Yeni rehber (48): Aşil tendonu kopması. cond47_part.py'den sonra exec edilir. Video yok.
# Egzersizler Sherwood Forest Hospitals (Haziran 2026) NHS broşüründeki bot dönemi egzersizlerine göre, hazır çizimlerle.

_ex2("ar_quad", "quad", "Uyluğu sıkıp topuğu kaldırma", "Bacaklarınız düz olacak şekilde oturun, dizinizin altına rulo yapılmış bir havlu koyun. Uyluğunuzu sıkarak dizinizin arkasını havluya bastırın ve topuğunuzu kaldırın. 3 saniye tutun.", "10 tekrar, bot takılıyken")
_ex2("ar_slr", "slr", "Düz bacak kaldırma", "Sırtüstü uzanın ya da bacaklarınız düz oturun. Dizinizi düz tutarak bacağınızı kaldırın, 3 saniye tutun ve yavaşça indirin.", "10 tekrar, bot takılıyken")
_ex2("ar_kext", "kext", "Oturarak diz düzeltme", "Sandalyeye oturun. Uyluğunuzu sıkarak dizinizi düzeltin ve 3 saniye tutun, sonra yavaşça indirin.", "10 tekrar, bot takılıyken")
_ex2("ar_hext", "hext", "Kalçayı arkaya açma", "Bir tezgâha ya da sandalye arkalığına tutunarak dik durun. Bacağınızı geriye doğru kaydırın ve kalçanızı sıkın. 3 saniye tutun, başlangıca dönün.", "10 tekrar, bot takılıyken")
_ex2("ar_sabd", "sabd", "Kalçayı yana açma", "Bir tezgâha tutunarak dik durun. Bacağınızı yana doğru kaydırın, 3 saniye tutun ve başlangıca dönün.", "10 tekrar, bot takılıyken")

AR_FAQ = [
 ("Ameliyat mı, bot mu?", "Norveç’te 18–60 yaş arası 554 kişinin katıldığı bir araştırmada ameliyatsız tedavi, açık ameliyat ve küçük kesili ameliyat bir yıl sonra benzer sonuç verdi. Tendonun yeniden kopması ameliyatsız grupta %6,2, ameliyatlı gruplarda %0,6 oldu; sinir hasarı ise ameliyatsız grupta %0,6, açık ameliyatta %2,8, küçük kesili ameliyatta %5,2’ydi. Geç başvuru (2–3 haftadan fazla), yeniden kopma, tendonun kemikten kopması ve üst düzey sporcularda ameliyat daha çok düşünülür. 29 çalışmayı birleştiren 2019 tarihli bir meta-analizde de ameliyatta yeniden kopma daha az, diğer komplikasyonlar daha sıktı; erken hareketli (fonksiyonel) rehabilitasyon uygulanan çalışmalarda ise yeniden kopma oranı iki grupta farklı değildi. Karar hekiminizle birlikte verilir. Ameliyatsız tedavide ise İngiltere'de 540 kişiyle yapılan UKSTAR çalışmasında, hemen yük vermeye izin veren yürüme botu alçıyla benzer sonuç verdi: 9. aydaki işlev puanları farksızdı, yeniden kopma botla tedavi edilenlerde %5, alçıyla tedavi edilenlerde %6 oldu."),
 ("Ağrım geçti, yine de doktora gitmeli miyim?", "Evet. Kopmadan sonra ağrı hafifleyebilir, hatta geçebilir; bu tendonun sağlam olduğu anlamına gelmez. Tanı ve tedavi gecikirse ameliyatsız tedavi seçeneği daralabilir."),
 ("Yeniden kopmayı nasıl önlerim?", "Botu çıkardıktan sonraki ilk 6 hafta, yeniden kopma riskinin en yüksek olduğu dönemdir; bu sürede tendonu ani germekten kaçının. İki tekinin yüksekliği aynı, topuğu en az 2,5 cm olan ayakkabı giyin. Engebeli zeminde dikkatli olun; merdivende ve kaldırımda ayağınızı topuğunuzla birlikte basamağa tam basın."),
 ("Ne zaman araba kullanabilirim?", "Alçı ya da botla araç kullanmayın. Bot dönemi bitip ani frene ağrısız ve güvenle basabildiğinizde başlayabilirsiniz. Sol tarafınızda kopma varsa ve otomatik vitesli araç kullanıyorsanız daha erken mümkün olabilir; hekiminize danışın."),
 ("İşe ve spora ne zaman dönerim?", "Masa başı işlere genellikle 8–12 hafta, bedensel işlere 3–6 ay sonra dönülür. Bir NHS kılavuzuna göre bisiklet ve yüzmeye 12–14 hafta, golfe 6–9 ay, raket sporlarına 9–12 ay, temas sporlarına yaklaşık 12 ay sonra dönülebilir. Belirtiler 4–6 ayda yatışır, düzelme 12–18 aya kadar sürebilir."),
]

AR_SRC = [
 "Royal Berkshire NHS Foundation Trust. " + ext("https://royalberkshire.nhs.uk/media/vq0plc5n/achilles-tendon-rupture-conservative-management_oct25.pdf", "Achilles tendon rupture: conservative management") + ". October 2025.",
 "Sherwood Forest Hospitals NHS Foundation Trust. " + ext("https://www.sfh-tr.nhs.uk/media/uz3il1th/pil202606-03-atr-achilles-tendon-rupture.pdf", "Achilles tendon rupture") + ". PIL202606-03-ATR, June 2026.",
 "NHS Fife. " + ext("https://www.nhsfife.org/services/all-services/patient-advice/achilles-tendon-rupture/", "Achilles tendon rupture") + ". February 2024.",
 "Myhrvold SB, Brouwer EF, Andresen TKM, et al. " + ext("https://www.nejm.org/doi/full/10.1056/NEJMoa2108447", "Nonoperative or surgical treatment of acute Achilles’ tendon rupture") + ". N Engl J Med. 2022;386(15):1409–1420.",
 "Ochen Y, Beks RB, van Heijl M, et al. " + ext("https://www.bmj.com/content/364/bmj.k5120", "Operative treatment versus nonoperative treatment of Achilles tendon ruptures: systematic review and meta-analysis") + ". BMJ. 2019;364:k5120",
 "UKSTAR Trial Collaborators (Costa ML, Achten J, Marian IR, et al.). " + ext("https://wrap.warwick.ac.uk/132184/", "Plaster cast versus functional brace for non-surgical treatment of Achilles tendon rupture (UKSTAR): a multicentre randomised controlled trial and economic evaluation") + ". Lancet. 2020;395(10222):441–448.",
]

AR_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Aşil tendonu kopması</h1>
    <p class="lede">Koşarken, sıçrarken ya da ani bir hamlede bacağınızın arkasına biri vurmuş gibi mi hissettiniz, belki bir “çat” sesiyle birlikte? Bu, aşil tendonu kopmasının tipik öyküsüdür ve beklemeden acil servise başvurmayı gerektirir. Bugün çoğu kişi ameliyatsız, özel bir botla tedavi ediliyor. İyileşme aylar sürer; sabır ve doğru bir rehabilitasyon programı ister.</p>
    <p class="meta">Son güncelleme: 24 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>30–50 yaş</b><span>En sık görüldüğü yaş aralığı</span></div>
        <div class="stat"><b>9–10 hafta</b><span>Ameliyatsız tedavide alçı ve botla geçen yaklaşık süre</span></div>
        <div class="stat"><b>%6,2</b><span>Bir araştırmada ameliyatsız tedavide yeniden kopma; ameliyatta %0,6</span></div>
        <div class="stat"><b>4–12 ay</b><span>Sporun türüne göre spora dönüş süresi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Topukta ya da baldırda ani ağrı; sonra hafifleyebilir ya da geçebilir.</li>
          <li>Kopma anında “çat” sesi ve bacağın arkasına darbe almış gibi bir his.</li>
          <li>Baldırda şişlik ve morluk.</li>
          <li>Düztaban yürüme; parmak ucuna kalkamama, merdiven çıkamama.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Futbol, tenis, badminton ya da squash gibi sporlarda güçlü bir itiş ya da ani hamle.</li>
          <li>Ayağın zorla yukarı büküldüğü düşme ve kaymalar.</li>
          <li>Tendonu zayıflatan durumlar: uzun süredir devam eden aşil tendinopatisi, bazı romatizmal hastalıklar, uzun süreli kortizon ve bazı antibiyotikler.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi nasıl ilerler?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Hemen acil servise</h3><p>Tanı çoğu zaman muayeneyle konur: tendonda bir boşluk hissedilir ve baldır sıkıldığında ayak hareket etmez. Gerekirse ultrason yapılır. Ayak ucu aşağı bakacak şekilde alçıya alınır.</p></div>
        <div class="kind"><span class="n">2</span><h3>Bot ve topuk takozları</h3><p>Alçının ardından topuğu yükselten takozlu ya da açısı ayarlanabilen bir bot verilir; takozlar birkaç haftada bir azaltılır. Bot, yatarken de dahil her zaman takılı kalır.</p></div>
        <div class="kind"><span class="n">3</span><h3>Pıhtıya karşı önlem</h3><p>Hareketsizlik bacakta pıhtı riskini artırır. Riskiniz varsa birkaç hafta pıhtı önleyici iğne verilebilir.</p></div>
        <div class="kind"><span class="n">4</span><h3>Aşamalı rehabilitasyon</h3><p>Bot döneminin sonuna doğru fizyoterapi başlar. Ayak bileği hareketleri, topuk kaldırma ve bisiklet aşama aşama eklenir; koşu ve sıçrama en son gelir.</p></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Bot döneminde egzersiz</p>
      <h2>Bacağı güçlü tutan beş egzersiz</h2>
      <p class="soft">Bu egzersizler bot takılıyken, diz ve kalça kaslarınızı korumak içindir. Botu çıkarmayın ve ayak bileğinizi kendi başınıza hareket ettirmeyin. Ayakta yapılanlar için ekibinizin size ayağınıza basma izni vermiş olması gerekir. Ayak bileği egzersizlerine fizyoterapistinizin söylediği zamanda ve onun gözetiminde başlayın.</p>
      {ex_grid(["ar_quad", "ar_slr", "ar_kext", "ar_hext", "ar_sabd"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(AR_FAQ)}
      <p class="soft" style="margin-top:18px">Kopma olmadan, yavaş yavaş artan aşil ağrısı için <a href="asil-tendinopatisi.html">aşil tendinopatisi</a>, burkulma sonrası ağrı için <a href="ayak-bilegi-burkulmasi.html">ayak bileği burkulması</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman acile ya da hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Kopma belirtileri varsa: hemen acil servise başvurun</li>
        <li>Baldırınızda, uyluğunuzda ya da kasığınızda ani, kramp benzeri ağrı varsa (pıhtı belirtisi olabilir)</li>
        <li>Göğüs ağrısı ya da nefes darlığı varsa: hemen 112’yi arayın</li>
        <li>Şişlikte ani artış, uyuşma ya da karıncalanma varsa</li>
        <li>Ameliyat olduysanız yaranızda kızarıklık, akıntı ya da açılma varsa</li>
      </ul>
      {CTA_CARD("Aşil tendonu kopması sonrası rehabilitasyonunuz", "aşil tendonu kopması")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(AR_SRC)}
    </div>
  </section>
</main>'''

page("asil-tendonu-kopmasi.html", "Aşil Tendonu Kopması",
     "Bacağınızın arkasında “çat” diye bir ses ve ani ağrı mı? Aşil tendonu kopması nasıl anlaşılır, ameliyat mı bot mu, ne zaman yürünür, spora ne zaman dönülür? Uyarı işaretleri ve bot döneminde beş egzersiz.",
     "asil-tendonu-kopmasi.html", NECK_CSS, AR_BODY, "",
     seo_title="Aşil Tendonu Kopması: Belirtiler, Bot Tedavisi, Ameliyat ve İyileşme | İhsan Eren",
     condition="Aşil tendonu kopması", faq_items=AR_FAQ)

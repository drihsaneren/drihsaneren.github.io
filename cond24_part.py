# -*- coding: utf-8 -*-
# Yeni rehber (24): kalça sıkışması (FAI). cond23_part.py'den sonra exec edilir. Video yok.
# Egzersizlerin çoğu bel ağrısı / diz rehberlerindekilerle aynı anahtar (çevirileri hazır); topuk kaydırma bu sayfaya özel.

_ex2("fai_hslide", "hslide", "Topuk kaydırma", "Sırtüstü yatın, bacaklarınız düz olsun. Karın kaslarınızı hafifçe sıkın; bir topuğunuzu yerde kaydırarak kalçanıza doğru çekin, diziniz tavana baksın. Kasıkta sıkışma hissetmeden önce durun, sonra yavaşça geri kaydırın ve diğer bacakla yapın.", "Her bacakla 10 tekrar")

FAI_FAQ = [
 ("Kalça sıkışması kireçlenmeye yol açar mı?", "Bu konu henüz netleşmedi. Uluslararası uzman görüşüne göre, ağrısı olmayan kişilerde bu kemik şeklini ameliyatla düzeltmenin kireçlenme riskini değiştirdiğine dair kanıt yok. Kireçlenme hakkında kalça kireçlenmesi rehberimize bakabilirsiniz."),
 ("Ameliyat olmam gerekir mi?", "Herkesin ameliyata ihtiyacı yoktur. Genellikle önce fizyoterapi, zorlayan hareketleri azaltma ve ağrı kesicilerle başlanır; belirtiler bunlarla geçmezse ameliyat düşünülebilir. Kararı, olası yararları ve riskleri konuşarak cerrahınızla birlikte verebilirsiniz."),
 ("Spor yapmayı bırakmalı mıyım?", "Çoğu zaman tamamen bırakmanız gerekmez. Ağrıyı artıran derin çömelme, hamle ve sıçrama gibi hareketleri bir süre azaltıp yüzme gibi kalçayı daha az zorlayan sporlara yönelebilirsiniz."),
 ("Röntgende sıkışma görüldü ama ağrım yok, ne yapmalıyım?", "Bu kemik şekli ağrısı olmayan pek çok kişide de görülür. Uluslararası uzman görüşüne göre ağrısı olmayan kişilere ameliyat nadiren önerilir; düzenli egzersizle aktif kalmaya devam edebilirsiniz."),
]

FAI_SRC = [
 "Griffin DR, Dickenson EJ, O’Donnell J, et al. The Warwick Agreement on femoroacetabular impingement syndrome (FAI syndrome): an international consensus statement. Br J Sports Med. 2016;50(19):1169–1176. " + ext("https://bjsm.bmj.com/content/50/19/1169.full", "bjsm.bmj.com") + ".",
 "NIHR Evidence. " + ext("https://evidence.nihr.ac.uk/alert/keyhole-surgery-is-more-effective-than-physiotherapy-for-hip-impingement/", "Keyhole surgery is more effective than physiotherapy for hip impingement") + ". 2 October 2018 (UK FASHIoN çalışmasının özeti: Griffin DR, et al. Lancet. 2018).",
 "Midlands Partnership University NHS Foundation Trust. " + ext("https://mpft.nhs.uk/services/msk/self-help/hip/hip-impingement-fai", "Hip impingement (FAI)") + ".",
 "George Eliot Hospital NHS Trust. " + ext("https://www.geh.nhs.uk/patients-and-visitors/patients/patient-leaflets/hip-impingement-fai", "Hip impingement (FAI)") + ". GEH-5029-1-2025, approved 20 August 2025.",
 "Kemp JL, Risberg MA, Mosler A, et al. " + ext("https://bjsm.bmj.com/content/54/9/504", "Physiotherapist-led treatment for young to middle-aged active adults with hip-related pain: consensus recommendations from the International Hip-related Pain Research Network, Zurich 2018") + ". Br J Sports Med. 2020;54(9):504–511.",
]

FAI_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Kalça sıkışması (FAI)</h1>
    <p class="lede">Kalça sıkışması (femoroasetabular sıkışma, FAI), uyluk kemiğinin başı ya da leğen kemiğindeki yuvası farklı şekilli olduğu için kalçanın hareket ederken düzgün kayamaması ve çevresindeki dokuların tahriş olmasıdır. En sık kasıkta, hareketle artan bir ağrıya yol açar. Bu kemik şekli ağrısı olmayan pek çok kişide de görülür; bu yüzden tanı, şikâyetler, muayene ve görüntüleme birlikte değerlendirilerek konur. Tedavi çoğu zaman fizyoterapi ve zorlayan hareketleri azaltmakla başlar.</p>
    <p class="meta">Son güncelleme: 11 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>348 kişi</b><span>Kalça artroskopisini kişiye özel fizyoterapiyle karşılaştıran İngiltere çalışması</span></div>
        <div class="stat"><b>6–10 seans</b><span>Bu çalışmadaki fizyoterapi programı; 12–24 haftaya yayıldı</span></div>
        <div class="stat"><b>6,8 puan</b><span>12. ayda artroskopi lehine fark (100 puanlık ölçekte); anlamlı sayılan eşik 6,1 puan</span></div>
        <div class="stat"><b>24–48 saat</b><span>Egzersizden sonra artan ağrının eski düzeyine dönmesi beklenen süre</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>En sık kasıkta ağrı; bazen kalçanın dış yanında, uylukta ya da kalçanın arkasında.</li>
          <li>Hareketle ya da belirli pozisyonlarda başlayan, etkinlikten sonra artan ağrı.</li>
          <li>Derin bükülmede zorlanma: çömelmek, çorap ve ayakkabı giymek, arabaya binip inmek.</li>
          <li>Kalçada takılma, kilitlenme, tıklama, tutukluk ya da boşalma hissi.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <p class="soft">İki ana şekil farkı vardır: uyluk kemiğinin başı ile boynunun birleştiği yerde fazlalık (cam tipi, erkeklerde daha sık) ve yuvanın uyluk kemiğinin başını fazla örtmesi (pincer tipi, kadınlarda daha sık). Bu şekil doğuştan olabilir ya da zamanla gelişebilir; spor yapan gençlerde daha sık görülür. Yapılan iş ve spor, geçirilmiş kalça yaralanması ve kalça çevresindeki kasların kontrolü de rol oynar.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Tanı nasıl konur?</h2>
        <p class="soft">Uluslararası uzmanların ortak görüşüne göre tanı için üç şey birlikte gerekir: hareketle ilgili kalça ya da kasık ağrısı, muayenede bu ağrının ortaya çıkması ve görüntülemede kemik şekli farkı. Muayenede kalça bükülüp içe çevrildiğinde tanıdık ağrının ortaya çıkması tanıyı destekler, ama tek başına yeterli değildir.</p>
        <p class="soft">İlk görüntüleme düz röntgendir; ameliyat düşünülüyorsa MR ya da tomografi istenebilir.</p>
      </div>
      <div>
        <h2>Fizyoterapi mi, ameliyat mı?</h2>
        <p class="soft">İngiltere’de 23 hastanede yapılan bir çalışmada 348 kişi ya kalça artroskopisine (kapalı ameliyat) ya da kişiye özel fizyoterapiye ayrıldı. 12 ay sonra iki grup da iyileşti; artroskopi grubunda yaşam kalitesi puanı 6,8 puan daha fazla arttı. Ancak sahte ameliyat grubu yoktu, yarar en çok cam tipinde görüldü ve uzun dönem sonuçlar henüz bilinmiyor.</p>
        <p class="soft">Uluslararası Kalça Ağrısı Araştırma Ağı’nın 2018 uzlaşısı, genç ve orta yaşlı aktif yetişkinlerde kalça, gövde ve işlevsel güçlendirmeye dayanan, en az 3 ay süren, fizyoterapist eşliğinde bir egzersiz programını öneriyor; daha uzun programlar daha büyük etki gösterdi.</p>
        <p class="soft">Ameliyat genellikle diğer tedavilerle geçmeyen belirtilerde düşünülür; herkesin ameliyata ihtiyacı yoktur.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Aktif kalın</h3><p>Düzenli hareket ağrıyı ve tutukluğu azaltır, kaslarınızı güçlendirir. Yüzme gibi kalçayı daha az zorlayan egzersizleri deneyebilirsiniz.</p></div>
        <div class="kind"><span class="n">2</span><h3>Zorlayan hareketleri azaltın</h3><p>Derin çömelme, hamle (lunge), leg press, deadlift, yüksek kutu sıçraması ve kürek makinesi ağrıyı artırabilir. Ağrı yatışana kadar bunlara ara verebilirsiniz.</p></div>
        <div class="kind"><span class="n">3</span><h3>Günlük hayatta</h3><p>Bağdaş kurmak ve kalçayı derin bükmek rahatsızlık verebilir. Çorap giyerken ya da arabaya binerken kalçanızı fazla bükmeden hareket etmeyi deneyebilirsiniz.</p></div>
        <div class="kind"><span class="n">4</span><h3>Ağrı kesici, sıcak, soğuk</h3><p>Sıcak ya da soğuk uygulama, parasetamol veya ağrı kesici jel rahatlatabilir. Hangisinin size uygun olduğunu eczacınıza ya da hekiminize sorabilirsiniz.</p></div>
      </div>
      <p class="soft" style="margin-top:18px">Kalçanın dış yanındaki ağrı için <a href="kalca-yan-agrisi.html">kalça yan ağrısı</a>, ileri yaşta kasık ağrısı için <a href="kalca-kireclenmesi.html">kalça kireçlenmesi</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Kalçayı güçlendiren altı egzersiz</h2>
      <p class="soft">Hafif bir rahatsızlık normaldir; ancak ağrı egzersiz sırasında belirgin artmamalı ve 24–48 saat içinde eski düzeyine dönmelidir. Tekrar sayıları yol göstericidir, size rahat gelen düzeye göre ayarlayabilirsiniz.</p>
      {ex_grid(["ptilt", "fai_hslide", "bridge", "abd", "sideplank", "sls"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(FAI_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Ağrı yaklaşık iki hafta kendi uyguladığınız önlemlere rağmen düzelmiyor ya da artıyorsa</li>
        <li>Ağrı birden ya da hızla kötüleşiyorsa</li>
        <li>Bacaklarda ya da ayaklarda ağrı, karıncalanma, uyuşma ya da güçsüzlük varsa</li>
        <li>Kalça aniden tamamen hareketsiz kaldıysa</li>
        <li>Ateş, halsizlik ya da açıklanamayan kilo kaybı varsa</li>
        <li>Ağrı düşme ya da kaza sonrası başladıysa</li>
      </ul>
      {CTA_CARD("Kalça ağrınız", "kalça sıkışması")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(FAI_SRC)}
    </div>
  </section>
</main>'''

page("kalca-sikismasi.html", "Kalça Sıkışması (FAI)",
     "Kasıkta hareketle artan ağrı kalça sıkışması olabilir mi? Belirtiler, tanı, fizyoterapi ile ameliyatı karşılaştıran 348 kişilik çalışma, günlük hayat önerileri ve evde altı egzersiz.",
     "kalca-sikismasi.html", NECK_CSS, FAI_BODY, "",
     seo_title="Kalça Sıkışması (FAI): Belirtiler, Egzersiz ve Tedavi | İhsan Eren",
     condition="Femoroasetabular sıkışma sendromu (kalça sıkışması)", faq_items=FAI_FAQ)

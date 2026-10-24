# -*- coding: utf-8 -*-
# Yeni rehber (49): Omuz kireçlenmesi (glenohumeral osteoartrit). cond48_part.py'den sonra exec edilir. Video yok.
# Egzersizler Northern Devon (Royal Devon), RUH Bath ve East Lancashire NHS broşürlerine göre; sarkaç, sopa ve havlu çizimleri donuk omuz rehberinden (EX).

_EXF2 = {e[0]: e[3] for e in EX}
SV["so_backf"] = _EXF2["Havlu ile germe"]
_ex2("so_pend", "cf_pendf", "Sarkaç", "Sağlam elinizle bir masaya dayanıp öne eğilin ve ağrılı kolunuzu gevşekçe sarkıtın. Kolunuzu önce öne ve arkaya, sonra yandan yana, sonra iki yöne de daireler çizerek sallayın. Kolu kasla değil, gövdenizin hafif sallanmasıyla hareket ettirin.", "Her hareketten 5–10 tekrar")
_ex2("so_stick", "cf_stickf", "Sopa ile dışa döndürme", "Oturun, ağrılı kolunuzun dirseği gövdenize yapışık ve 90 derece bükülü olsun. Bir sopayı iki elinizle tutun ve sağlam kolunuzla iterek ağrılı elinizi rahat ettiğiniz kadar dışa doğru götürün, sonra geri getirin.", "5–10 tekrar")
_ex2("so_table", "towel", "Masada kaydırma", "Masaya oturun ya da önünde durun, ellerinizi masadaki bir havlunun üzerine koyun. Omuzlarınızı kaldırmadan, ellerinizi rahat ettiğiniz kadar öne doğru kaydırın, sonra geri çekin.", "5 tekrarla başlayın, her gün 1–2 artırın; günde en az 3 kez")
_ex2("so_back", "so_backf", "Havluyla eli sırta kaydırma", "Bir havluyu sırtınızın arkasında tutun: sağlam kolunuz yukarıda, ağrılı kolunuz aşağıda olsun. Sağlam kolunuzla havluyu yavaşça yukarı çekin; ağrılı eliniz sırtınız boyunca yukarı kaysın. Zorlamayın.", "5–10 tekrar")

SO_FAQ = [
 ("Kortizon iğnesi yapılabilir mi?", "Eklem içine yapılan kortizon iğnesi bazı kişilerde ağrıyı bir süre azaltabilir, ama etkisi kişiden kişiye değişir ve herkes için uygun değildir. Uzun süre tekrar tekrar yapılamaz, çünkü zamanla omuz kirişlerine zarar verir."),
 ("Kapalı (artroskopik) ameliyat işe yarar mı?", "Bir NHS broşürüne göre kapalı ameliyat omuz kireçlenmesinde yararlı değildir. Çoğu kişi fizyoterapi, ağrı kesiciler, kendi kendine bakım ve gerekirse iğnelerle ameliyatsız tedavi edilir."),
 ("Protez ne zaman gerekir?", "Ağrı belirginse ve ameliyatsız tedaviler yeterince yardımcı olmadıysa omuz protezi düşünülebilir. Hangi protezin uygun olduğuna cerrahınız karar verir. 20 randomize çalışmayı (1.083 kişi) inceleyen 2020 tarihli bir Cochrane derlemesinde, omuz protezini fizyoterapi ya da başka tedavilerle karşılaştıran bir çalışma bulunmadı. Kireçlenmede tam omuz protezi yarım proteze göre ağrı ve işlevde küçük bir yarar sağlıyor olabilir, ancak kanıtın kesinliği düşük."),
 ("Donuk omuzdan farkı ne?", "İkisinde de omuz ağrılı ve tutuktur. Ayırt etmek için hekiminiz sizi muayene eder ve kireçlenmeyi görmek için röntgen ister."),
 ("Hangi sporları yapabilirim?", "Yürüyüş, bisiklet, yüzme ve düşük tempolu aerobik, tai chi, yoga, pilates gibi eklemi zorlamayan etkinlikler uygundur. Egzersiz ağrıyı ve tutukluğu azaltır, kasları güçlendirir ve genel kondisyonu artırır."),
]

SO_SRC = [
 "Northern Devon Healthcare NHS Trust. " + ext("https://www.royaldevon.nhs.uk/media/1pckxvhv/osteoarthritis_in_the_shoulder.pdf", "Osteoarthritis in the shoulder") + ". Leaflet 527.",
 "Royal United Hospitals Bath NHS Foundation Trust. " + ext("https://ruh.nhs.uk/patients/patient_information/PHY024_Shoulder_Osteoarthritis.pdf", "Shoulder osteoarthritis") + ". RUH PHY/024, April 2020.",
 "NHS Lothian. " + ext("https://policyonline.nhslothian.scot/wp-content/uploads/2024/05/Shoulder-osteoarthritis.pdf", "Shoulder osteoarthritis") + ". Version 1.0, May 2024.",
 "East Lancashire Hospitals NHS Trust. " + ext("https://www.elht.nhs.uk/application/files/3415/2293/8362/Osteoarthritis_of_the_Shoulder_-_Patient__Information_and_Exercises_-_PHYSIO_001.pdf", "Osteoarthritis of the shoulder: patient information and exercises") + ". PHYSIO-001.",
 "Craig RS, Goodier H, Singh JA, Hopewell S, Rees JL. " + ext("https://www.cochrane.org/evidence/CD012879_shoulder-replacement-surgery-osteoarthritis-and-arthritis-associated-torn-rotator-cuff-tendons", "Shoulder replacement surgery for osteoarthritis and rotator cuff tear arthropathy") + ". Cochrane Database Syst Rev. 2020;(4):CD012879.",
 "NICE. " + ext("https://www.nice.org.uk/guidance/ng226", "Osteoarthritis in over 16s: diagnosis and management") + ". NICE guideline NG226, 2022",
]

SO_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Omuz kireçlenmesi</h1>
    <p class="lede">Omzunuz hareket ettikçe ağrıyor, uzanmak zorlaşıyor ya da hareket ederken eklemden takılma ve sürtünme sesleri mi geliyor? Omuz kireçlenmesi, eklemi kaplayan kıkırdağın zamanla incelmesiyle ortaya çıkar. Kalça, diz ve ellere göre daha seyrek görülür ve genellikle 50 yaşından sonra başlar. Çoğu kişi ameliyatsız; hareket, egzersiz ve doğru günlük alışkanlıklarla durumunu yönetir.</p>
    <p class="meta">Son güncelleme: 24 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>50 yaş</b><span>Kireçlenme genellikle bu yaştan sonra görülür</span></div>
        <div class="stat"><b>30 dakika</b><span>Sabah tutukluğu ve egzersiz sonrası hafif sızı genellikle bu sürede geçer</span></div>
        <div class="stat"><b>Günde 1–2 kez</b><span>Egzersizler için önerilen sıklık; tercihen ılık bir duştan sonra</span></div>
        <div class="stat"><b>10 dakika</b><span>Buz uygulaması için en uzun süre, günde 2–3 kez</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Omuzda ve üst kolda ağrı; bazen geceleri artar ve uykuyu böler.</li>
          <li>Tutukluk ve hareket kısıtlılığı.</li>
          <li>Hareket ederken takılma, sürtünme ya da çıtırtı hissi.</li>
          <li>Ağrı hem aşırı kullanımla hem de hiç kullanmamakla artabilir.</li>
          <li>Köprücük kemiğinin omuzla birleştiği eklem etkilenmişse, emniyet kemerine uzanırken, kolu vücudun önünden karşıya götürürken ya da o tarafa yatınca ağrı olur.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Eklem kıkırdağı yıllar içinde incelir, kemik uçlarında küçük çıkıntılar oluşur.</li>
          <li>Omuzda eski bir kırık ya da yaralanma.</li>
          <li>Rotator manşet kaslarında hasar.</li>
          <li>Romatoid artrit gibi iltihaplı eklem hastalıkları.</li>
          <li>Tekrarlayan ağır iş ya da sporla omzun zorlanması.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Hareketli kalın</h3><p>Omzunuzu hareket ettirmeye devam edin; yalnızca ağrılı olduğunda dinlendirin. Hareket, kasların gücünü ve eklemin esnekliğini korur.</p></div>
        <div class="kind"><span class="n">2</span><h3>İşleri bölün</h3><p>Günlük işlerinizi güne yayın, dinlenme aralarıyla bölün. Kolu baş üstüne tekrar tekrar kaldırmayı gerektiren işleri azaltın.</p></div>
        <div class="kind"><span class="n">3</span><h3>Rahat uyuyun</h3><p>Sırtüstü yatıp ağrılı kolunuzu bir yastıkla destekleyin ya da sağlam tarafınıza yatıp ağrılı kolunuzun altına bir yastık koyun.</p></div>
        <div class="kind"><span class="n">4</span><h3>Ağrıyı yönetin</h3><p>Hekiminize ya da eczacınıza danışarak düzenli ağrı kesici kullanabilirsiniz. Havluya sarılı buz ya da sıcak uygulama da bazı kişilerde ağrıyı hafifletir.</p></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Omzu açan dört egzersiz</h2>
      <p class="soft">Hareketleri zorlamadan, rahat edebildiğiniz aralıkta yapın. Hafif bir sızı ya da gerilme normaldir ve yarım saat içinde geçmelidir. Ağrınız artıyorsa egzersizi bırakın ve hekiminize ya da fizyoterapistinize danışın.</p>
      {ex_grid(["so_pend", "so_stick", "so_table", "so_back"], "ex four")}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(SO_FAQ)}
      <p class="soft" style="margin-top:18px">Omuzda ani başlayan tutukluk için <a href="donuk-omuz.html">donuk omuz</a>, kolu kaldırınca artan ağrı için <a href="omuz-sikismasi.html">omuz sıkışması</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Egzersizler ağrınızı artırıyorsa</li>
        <li>Ağrınız ilaçlara rağmen sürüyorsa</li>
        <li>Giyinmek, yıkanmak ya da araba kullanmak gibi günlük işlerde zorlanıyorsanız</li>
      </ul>
      {CTA_CARD("Omuz kireçlenmesi", "omuz kireçlenmesi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(SO_SRC)}
    </div>
  </section>
</main>'''

page("omuz-kireclenmesi.html", "Omuz Kireçlenmesi",
     "Omzunuz ağrıyor, tutuk ve hareket ederken takılıyor mu? Omuz kireçlenmesi nedir, kortizon iğnesi ve ameliyat ne zaman düşünülür? Uyku önerileri ve evde dört egzersiz.",
     "omuz-kireclenmesi.html", NECK_CSS, SO_BODY, "",
     seo_title="Omuz Kireçlenmesi: Belirtiler, Tedavi ve Evde Egzersizler | İhsan Eren",
     condition="Omuz kireçlenmesi", faq_items=SO_FAQ)

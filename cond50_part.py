# -*- coding: utf-8 -*-
# Yeni rehber (50): Baldır kası zorlanması (calf strain / yırtığı). cond49_part.py'den sonra exec edilir. Video yok.
# Egzersizler Hull (HEY, 2025), Plymouth (2025) ve Royal Free (2026) NHS broşürlerine göre, hazır çizimlerle.

_ex2("cz_pump", "apump", "Ayak bileğini çekip itme", "Oturun ya da uzanın. Ayak ucunuzu ve bileğinizi kendinize doğru çekin, 5 saniye tutun; sonra ayak ucunuzu ileri doğru itin, 5 saniye tutun. Ağrısız aralıkta kalın.", "10 tekrar, günde 3–4 kez")
_ex2("cz_towel", "towelst2", "Havluyla baldır germe", "Bacağınız düz oturun, bir havluyu ya da kemeri ayağınızın ön kısmına dolayın. Uçlarından tutup ayağınızı kendinize doğru çekin; baldırınızda hafif bir gerilme hissedin.", "30 saniye tutun, tekrarlayın")
_ex2("cz_calf", "calf", "Düz dizle baldır germe", "Bir sandalyeye ya da duvara dönük durun. Ağrılı bacağınızı geriye alın; dizi düz, topuğu yerde kalsın. Öndeki dizinizi bükerek baldırınızda gerilme hissedene kadar öne eğilin.", "30 saniye, günde 3 kez")
_ex2("cz_sol", "soleus", "Diz bükülü baldır germe", "Ağrılı bacağınız diğerinin biraz gerisinde, ayak uçlarınız öne baksın. Ağrılı topuğunuzu yerde tutarak iki dizinizi birden bükün; gerilmeyi baldırın alt kısmında hissedin.", "30 saniye, günde 3 kez")
_ex2("cz_heel", "heel2", "Topuk kaldırma", "Parmak ucunuzda ağrısız durabildiğinizde başlayın. Bir sandalyeye tutunun, ağırlığınızı iki ayağınıza eşit verin. Parmak uçlarınızda olabildiğince yükselin, 5 saniye tutun ve yavaşça inin. Kolaylaştıkça tekrar sayısını artırın, sonra tek ayakla yapın.", "10 tekrar, günde 2 kez")
_ex2("cz_sls", "sls", "Tek ayak üzerinde denge", "Yaralanmadan önce tek ayak üzerinde durabiliyorsanız 2. haftadan itibaren başlayabilirsiniz. Sağlam bir yere tutunarak ağrılı bacağınızın üzerinde durun; kolaylaştıkça desteksiz, güvenliyse gözleriniz kapalı deneyin.", "30 saniye; ağrı olursa bırakın")

CZ_FAQ = [
 ("Aşil tendonu kopmasından nasıl ayırt ederim?", "Her zaman kolay değildir. Topuğun üstünde “çat” diye bir ses, bacağın arkasına darbe almış gibi bir his, tendonda boşluk hissi, düztaban yürüme ve parmak ucuna hiç kalkamama aşil tendonu kopmasını düşündürür. Bu durumda beklemeden acil servise başvurun."),
 ("Ne zaman koşuya ve spora dönebilirim?", "Çoğu kişi yaklaşık 2 haftada kendini daha iyi hisseder, ama yeniden sakatlanmamak için 8 haftaya kadar ağır egzersizden kaçınmak önerilir. Tam güce, tam harekete kavuşup hızlı tempoda ağrısız ve şişliksiz yürüyebildiğinizde sporunuza özgü hareketlere başlayın ve antrenmanı kademeli artırın."),
 ("Bandaj kullanmalı mıyım?", "Şişliği kontrol etmek için baldıra bası bandajı ya da çorap kullanılabilir. Uyurken çıkarın. Ayağınızda karıncalanma, uyuşma, morarma ya da artan ağrı olursa bandajı hemen çıkarın."),
 ("Fizyoterapi gerekli mi?", "Her zaman gerekmez; çoğu kişi bu önerilerle iyileşir. Yaralanmadan 10 gün sonra hâlâ ayağınıza basamıyorsanız ve baldırınız ağrılı ve şişse bir fizyoterapiste başvurun."),
 ("Ne kadar sürer?", "Çoğu kişi yaklaşık 2 haftada kendini daha iyi hisseder; iyileşme genellikle 6 hafta kadar sürer. Ciddi yırtıkların tam iyileşmesi 3 aya kadar sürebilir; hafif ağrı ve şişlik bazen 3–6 ay devam eder."),
]

CZ_SRC = [
 "Hull University Teaching Hospitals NHS Trust. " + ext("https://hey.nhs.uk/patient-leaflet/soft-tissue-injury-calf-strain", "Soft tissue injury: calf strain") + ". HEY231/2025, updated June 2025.",
 "University Hospitals Plymouth NHS Trust. " + ext("https://www.plymouthhospitals.nhs.uk/display-pil/pil-calf-muscle-tears-and-strains-6064", "Calf muscle tears and strains") + ". February 2025.",
 "Royal Free London NHS Foundation Trust. " + ext("https://royalfree.nhs.uk/patients-and-visitors/patient-information-leaflets/calf-muscle-tear", "Calf muscle tear") + ". RFL1181, June 2026.",
 "Green B, Pizzari T. " + ext("https://bjsm.bmj.com/content/51/16/1189", "Calf muscle strain injuries in sport: a systematic review of risk factors for injury") + ". Br J Sports Med. 2017;51(16):1189–1194",
 "NHS. " + ext("https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/", "DVT (deep vein thrombosis)") + ". Page last reviewed: 30 April 2026.",
]

CZ_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Baldır kası zorlanması</h1>
    <p class="lede">Koşarken, sıçrarken ya da ani bir hamlede baldırınıza bıçak saplanmış gibi keskin bir ağrı mı girdi? Baldırdaki iki büyük kasın birinde küçük bir yırtık olduğunda baldır kası zorlanması ortaya çıkar. Sık görülen bir spor yaralanmasıdır ve çoğu zaman birkaç hafta içinde düzelir. İlk günlerde doğru bakım ve sonra kademeli egzersiz, iyileşmeyi hızlandırır ve yeniden sakatlanmayı önler.</p>
    <p class="meta">Son güncelleme: 16 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>72 saat</b><span>Sıcak, alkol, koşu ve masajdan kaçınılması gereken ilk dönem</span></div>
        <div class="stat"><b>2 hafta</b><span>Çoğu kişinin kendini daha iyi hissettiği süre</span></div>
        <div class="stat"><b>8 hafta</b><span>Yeniden sakatlanmamak için ağır egzersizden kaçınma süresi</span></div>
        <div class="stat"><b>3 ay</b><span>Ciddi yırtıkların tam iyileşmesinin sürebileceği süre</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Bacağın arkasında ani, keskin, yırtılır ya da bıçak saplanır gibi ağrı.</li>
          <li>Baldırda gerginlik ve tutukluk; hafif zorlanmada etkinliğe devam edilebilir.</li>
          <li>Baldırda şişlik ve morluk; ayak bileğine doğru yayılabilir.</li>
          <li>Parmak ucunda dururken ağrı ya da zorlanma; ciddi yırtıkta bacağa basmak çok ağrılıdır.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Baldırda iki ana kas vardır: yüzeydeki büyük kas (gastroknemius) ve onun altında, daha aşağıda yer alan kas (soleus). İkisi de aşil tendonunda birleşir.</li>
          <li>Kas aşırı gerildiğinde ya da ani ve güçlü bir yüklenmeyle karşılaştığında bir kısmı yırtılabilir.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>İlk günlerde neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Koruyun ve dinlendirin</h3><p>İlk 72 saat etkinliğinizi azaltın, ama tamamen hareketsiz kalmayın. Hafif topuklu, destekleyici bir ayakkabı yürümeyi kolaylaştırır.</p></div>
        <div class="kind"><span class="n">2</span><h3>Buz uygulayın</h3><p>Nemli bir havluya sarılı buzu 15–20 dakika uygulayın; cildinizi 5 dakikada bir kontrol edin. Buzu doğrudan cilde koymayın.</p></div>
        <div class="kind"><span class="n">3</span><h3>Bası ve yükseltme</h3><p>Şişlik varsa bası bandajı ya da çorap kullanabilirsiniz. Dinlenirken bacağınızı kalp seviyesinin üzerinde tutun.</p></div>
        <div class="kind"><span class="n">4</span><h3>Zarar verenlerden kaçının</h3><p>İlk 72 saat sıcak uygulama, alkol, koşu ve masajdan kaçının. Sigara iyileşmeyi yavaşlatır.</p></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Baldırı iyileştiren altı egzersiz</h2>
      <p class="soft">İlk iki egzersizle başlayın. Ağrı yatışıp koltuk değneğine ihtiyacınız kalmadığında germe ve güçlendirme egzersizlerine geçin. Hareketleri ağrısız aralıkta yapın; ağrının başladığı yerde durun.</p>
      {ex_grid(["cz_pump", "cz_towel", "cz_calf", "cz_sol", "cz_heel", "cz_sls"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(CZ_FAQ)}
      <p class="soft" style="margin-top:18px">Ani “çat” sesi ve parmak ucuna kalkamama için <a href="asil-tendonu-kopmasi.html">aşil tendonu kopması</a>, kaval kemiği boyunca ağrı için <a href="kaval-kemigi-agrisi.html">kaval kemiği ağrısı</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Bir bacakta zonklayan ya da kramp gibi ağrı, şişlik, kızarık ya da koyulaşmış cilt veya şişkin damarlar varsa (pıhtı belirtisi olabilir)</li>
        <li>Bu belirtilerle birlikte göğüs ağrısı ya da nefes darlığı varsa: hemen 112’yi arayın</li>
        <li>Belirtiler düzelmiyor ve baldır giderek daha hassas, kırmızı ve sıcak oluyorsa</li>
        <li>Yaralanmadan 10 gün sonra hâlâ ayağınıza basamıyorsanız</li>
      </ul>
      {CTA_CARD("Baldır kası zorlanması sonrası iyileşmeniz", "baldır kası zorlanması")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(CZ_SRC)}
    </div>
  </section>
</main>'''

page("baldir-kasi-zorlanmasi.html", "Baldır Kası Zorlanması",
     "Baldırınıza ani, keskin bir ağrı mı girdi? Baldır kası zorlanmasında ilk 72 saatte ne yapmalı, ne zaman spora dönülür, pıhtıdan nasıl ayırt edilir? Uyarı işaretleri ve evde altı egzersiz.",
     "baldir-kasi-zorlanmasi.html", NECK_CSS, CZ_BODY, "",
     seo_title="Baldır Kası Zorlanması ve Yırtığı: İlk 72 Saat, İyileşme ve Egzersizler | İhsan Eren",
     condition="Baldır kası zorlanması", faq_items=CZ_FAQ)

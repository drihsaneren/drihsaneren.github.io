# -*- coding: utf-8 -*-
# Yeni rehber (51): Ayak bileği kırığı sonrası. cond50_part.py'den sonra exec edilir. Video yok.
# Egzersizler RUH Bath, WWL (2026), NHS Lothian (2025), United Lincolnshire (2025) ve Worcestershire NHS broşürlerine göre, hazır çizimlerle.

_ex2("ak_pump", "apump", "Ayak bileğini yukarı aşağı oynatma", "Oturun ya da uzanın. Ayağınızı rahat ettiğiniz aralıkta yukarı doğru çekin, sonra aşağı doğru itin. Bot kullanıyorsanız ekibiniz izin verdiyse botu çıkarıp yapabilirsiniz.", "10 tekrar, günde 3–4 kez")
_ex2("ak_towel", "towelst2", "Havluyla baldır germe", "Ağrı yatıştıktan sonra başlayın. Bacağınız düz oturun, havluyu ayağınızın ön kısmına dolayıp uçlarından tutun ve ayağınızı kendinize doğru çekin.", "20–30 saniye tutun, günde 3 kez")
_ex2("ak_calf", "calf", "Duvarda baldır germe", "Duvara dönük durun, ellerinizi duvara koyun. Ağrılı ayağınızı geriye alın; dizi düz, topuğu yerde kalsın. Öndeki dizinizi bükerek rahat ettiğiniz kadar öne eğilin.", "Rahat ettiğiniz kadar, günde 3–4 kez")
_ex2("ak_heel", "heel2", "Topuk kaldırma", "Bir tezgâha tutunarak dik durun. Topuklarınızı kaldırıp parmak uçlarınızda yükselin, 3 saniye tutun ve yavaşça inin. Kendinize güvendiğinizde tek ayakla, tutunarak yapın.", "Ağrınızın izin verdiği kadar, gün içinde")
_ex2("ak_sts", "sts", "Sandalyeden kalkıp oturma", "Genellikle 6. haftadan sonra başlanır. Ellerinizi kullanmadan sandalyeden kalkın ve kontrollü şekilde oturun.", "10 tekrar")
_ex2("ak_sls", "sls", "Tek ayak üzerinde denge", "Genellikle 6. haftadan sonra başlanır. Bir tezgâha tutunarak ağrılı ayağınızın üzerinde durun. Kolaylaştıkça tutunmayı azaltın, sonra gözleriniz kapalı deneyin.", "20–30 saniye")

AK_FAQ = [
 ("Ne kadar süre bot ya da alçı kullanacağım?", "Kırığın türüne göre değişir. Dış bilekteki dengeli kırıklarda bot genellikle ayaktayken 1 ile 4 hafta kullanılır ve 6 haftada bot ve koltuk değneği bırakılır. Alçıyla tedavi edilen kırıklarda bu süre çoğu zaman 6 haftadır. Finlandiya’da yapılan randomize bir çalışmada, dış bilekteki dengeli kırıklarda 3 haftalık alçı ya da ortez, alışılmış 6 haftalık alçı kadar iyi sonuç verdi."),
 ("Şişlik ne zaman geçer?", "Kırık genellikle 6–12 haftada kaynar, ama ağrı, tutukluk, şişlik ve güç kaybının tamamen geçmesi 6–12 ayı bulabilir. Gün sonunda biraz şişlik ve sızı olması normaldir. Dinlenirken ayağınızı yüksekte tutun."),
 ("Egzersiz ağrıtırsa ne yapmalıyım?", "Egzersiz sırasında hafif rahatsızlık olabilir, ama 2 saat içinde geçmeli ve belirtilerinizi genel olarak kötüleştirmemeli. Ağrı uzun sürüyorsa tekrar sayısını azaltın ve fizyoterapistinize danışın."),
 ("Ne zaman araba kullanabilirim?", "Bot ya da alçıyla araç kullanmayın. Botu bıraktığınızda, normal yürüyebildiğinizde ve ani frene güvenle basabildiğinizde başlayabilirsiniz; önce sakin bir yerde deneyin. Kırık sol ayağınızdaysa ve otomatik vitesli araç kullanıyorsanız daha erken mümkün olabilir."),
 ("İşe ne zaman dönebilirim?", "Dış bilekteki dengeli kırıklarda masa başı işlere genellikle 1–2 hafta, bedensel işlere 4–6 hafta sonra dönülebilir. İşinizi yapabildiğinizi hissettiğinizde, mümkünse kademeli dönün."),
]

AK_SRC = [
 "WWL Teaching Hospitals NHS Foundation Trust. " + ext("https://www.wwl.nhs.uk/pdfreader/accessiblePDF/cnv-wwl-68ca8bd00632b3.14985575", "Stable ankle fracture") + ". Musc 080, version 3, July 2026.",
 "NHS Lothian. " + ext("https://policyonline.nhslothian.scot/wp-content/uploads/2023/03/Simple_ankle_fracture.pdf", "Simple ankle fracture") + ". Version 2.1, June 2025.",
 "Royal United Hospitals Bath NHS Foundation Trust. " + ext("https://www.ruh.nhs.uk/patients/patient_information/ORT037_Advice_after_breaking_your_ankle.pdf", "Advice after an ankle fracture") + ". 2017.",
 "United Lincolnshire Teaching Hospitals NHS Trust. " + ext("https://www.ulh.nhs.uk/wp-content/uploads/2025/07/Ankle-Fracture-Exercises.pdf", "Ankle fracture exercises") + ". June 2025.",
 "Kortekangas T, et al. " + ext("https://www.bmj.com/content/364/bmj.k5432", "Three week versus six week immobilisation for stable Weber B type ankle fractures: randomised, multicentre, non-inferiority clinical trial") + ". BMJ. 2019;364:k5432.",
 "NHS. " + ext("https://www.nhs.uk/conditions/deep-vein-thrombosis-dvt/", "DVT (deep vein thrombosis)") + ". Page last reviewed: 30 April 2026.",
]

AK_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Ayak bileği kırığı sonrası</h1>
    <p class="lede">Ayak bileğiniz kırıldı ve şimdi bot ya da alçıyla mı yürüyorsunuz? Dış bilekteki ince kemiğin (fibula) dengeli kırıkları neredeyse her zaman ameliyatsız iyileşir. Kemik genellikle 6–12 haftada kaynar; asıl iş ondan sonra başlar: ayak bileğinin hareketini, gücünü ve dengesini geri kazanmak. Bu rehber, bot ya da alçı döneminden sonra evde yapabileceğiniz egzersizleri anlatıyor.</p>
    <p class="meta">Son güncelleme: 16 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>6–12 hafta</b><span>Kırığın genellikle kaynadığı süre</span></div>
        <div class="stat"><b>6–12 ay</b><span>Ağrı, tutukluk ve şişliğin tamamen geçmesi için gerekebilecek süre</span></div>
        <div class="stat"><b>3 hafta</b><span>Dengeli dış bilek kırığında, 6 haftalık alçı kadar iyi sonuç veren hareketsizlik süresi</span></div>
        <div class="stat"><b>1–2 hafta</b><span>Dengeli dış bilek kırığında masa başı işe dönüş için genellikle gereken süre</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Tedavi nasıl ilerler?</h2>
        <ul class="dots">
          <li>Dış bilekteki dengeli kırıklar çoğu zaman bir bot ya da destekleyici çorapla, ayağa basılarak tedavi edilir.</li>
          <li>Bazı kırıklarda bir süre ayağa basmadan alçı gerekir; eklemin dengesi bozulmuşsa ameliyat yapılır, ardından alçı ve bot kullanılır.</li>
          <li>Egzersizlere ne zaman başlayacağınızı ve ne zaman ilerleyeceğinizi ekibiniz söyler.</li>
        </ul>
      </div>
      <div>
        <h2>İyileşmeyi yavaşlatanlar</h2>
        <ul class="dots">
          <li>Sigara kemiğin kaynamasını yavaşlatır; bırakmak iyileşmeye yardım eder.</li>
          <li>Şeker hastalığı da iyileşmeyi yavaşlatabilir.</li>
          <li>Hareketsizlik bacakta pıhtı riskini artırır; erken ve düzenli hareket bu yüzden önemlidir.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>İlk günler</h3><p>İlk 24–72 saat dinlenin ve ayağınızı yüksekte tutun. Gerekirse havluya sarılı buzu saatte en fazla 15 dakika uygulayın; hissiniz azsa ya da cildinizde sorun varsa buz kullanmayın.</p></div>
        <div class="kind"><span class="n">2</span><h3>Şişliği yönetin</h3><p>Dinlenirken ayağınızı yükseltin, ayakta kalma sürenizi kademeli artırın. Hekiminize ya da eczacınıza danışarak ağrı kesici kullanabilirsiniz.</p></div>
        <div class="kind"><span class="n">3</span><h3>Değnekleri kademeli bırakın</h3><p>Önce iki değnekten bire geçin; tek değneği sağlam tarafınızdaki elinizde tutun. Sonra değneksiz yürüyün ve topuktan parmağa basarak yürümeyi hedefleyin.</p></div>
        <div class="kind"><span class="n">4</span><h3>Güç ve denge</h3><p>Kırık kaynadıktan sonra, genellikle 6. haftadan itibaren, güçlendirme ve denge egzersizleri eklenir. Spora ağrısız ve tam hareketle dönün.</p></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Ayak bileğini yeniden güçlendiren altı egzersiz</h2>
      <p class="soft">İlk üç egzersiz bot ya da alçı döneminden sonra, ekibiniz izin verdiğinde başlar; son üçü genellikle 6. haftadan sonra eklenir. Hafif rahatsızlık normaldir ama 2 saat içinde geçmelidir.</p>
      {ex_grid(["ak_pump", "ak_towel", "ak_calf", "ak_heel", "ak_sts", "ak_sls"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(AK_FAQ)}
      <p class="soft" style="margin-top:18px">Kırık olmadan burkulan bilek için <a href="ayak-bilegi-burkulmasi.html">ayak bileği burkulması</a>, kolda benzer süreç için <a href="el-bilegi-kirigi.html">el bileği kırığı sonrası</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Bir bacakta zonklayan ağrı, şişlik, kızarık ya da koyulaşmış cilt veya şişkin damarlar varsa (pıhtı belirtisi olabilir)</li>
        <li>Bu belirtilerle birlikte göğüs ağrısı ya da nefes darlığı varsa: hemen 112’yi arayın</li>
        <li>6. haftada hâlâ bot ya da koltuk değneğine ihtiyacınız varsa</li>
        <li>12. haftada hâlâ belirgin ağrınız ya da tutukluğunuz varsa</li>
      </ul>
      {CTA_CARD("Ayak bileği kırığı sonrası rehabilitasyonunuz", "ayak bileği kırığı sonrası rehabilitasyon")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(AK_SRC)}
    </div>
  </section>
</main>'''

page("ayak-bilegi-kirigi.html", "Ayak Bileği Kırığı Sonrası",
     "Ayak bileği kırığından sonra bot ne kadar kullanılır, şişlik ne zaman geçer, ne zaman araba kullanılır? İyileşmeyi hızlandıran öneriler, uyarı işaretleri ve evde altı egzersiz.",
     "ayak-bilegi-kirigi.html", NECK_CSS, AK_BODY, "",
     seo_title="Ayak Bileği Kırığı Sonrası: İyileşme Süresi ve Evde Egzersizler | İhsan Eren",
     condition="Ayak bileği kırığı", faq_items=AK_FAQ)

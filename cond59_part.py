# -*- coding: utf-8 -*-
# Yeni rehber (59): Ayak dış kenarı (5. metatars, tarak kemiği) kırığı. cond58_part.py'den sonra exec edilir. Video yok.
# University Hospitals Sussex (2559, Ağustos 2025), Royal Free London (RFL949 v4, Haziran 2025) ve East Sussex (Jones kırığı, Kasım 2025) NHS broşürlerine göre.

# Ayakla daire çizme (yandan, oturarak; ayak ucu daire çizer)
SV["mt_circle"] = fig(GRD + CHAIR_L +
    '<circle class="hd" cx="50" cy="33" r="8"/><path class="fig" d="M48 42 L46 74 H80"/>'
    f'<g>{anim_t("0 80 74;360 80 74", dur="3.6s", kt="0;1", typ="rotate")}<path class="fig hl" d="M80 74 L80 104 L92 104"/></g>'
    '<circle cx="86" cy="104" r="12" fill="none" stroke="#C8963E" stroke-width="2.5" stroke-dasharray="3 4"/>',
    "Ayak bileği daireleri")
# Topuklar birlikte, ayak parmaklarını açma (üstten)
SV["mt_toes"] = fig(
    '<rect x="30" y="50" width="22" height="58" rx="11" fill="#2A6F6B"/><rect x="68" y="50" width="22" height="58" rx="11" fill="#2A6F6B"/>'
    f'<g fill="#C8963E">{anim_t("0 0;-6 2;0 0")}<circle cx="34" cy="44" r="4"/><circle cx="41" cy="41" r="4"/><circle cx="48" cy="44" r="4.5"/></g>'
    f'<g fill="#C8963E">{anim_t("0 0;6 2;0 0")}<circle cx="72" cy="44" r="4.5"/><circle cx="79" cy="41" r="4"/><circle cx="86" cy="44" r="4"/></g>'
    '<path d="M22 30 l-8 0 m3 -3 l-3 3 l3 3 M98 30 l8 0 m-3 -3 l3 3 l-3 3" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "Parmakları açma")
# Ayağı içe ve dışa çevirme (önden)
SV["mt_inout"] = fig(GRD +
    '<path class="fig" d="M60 10 V86"/>'
    f'<g>{anim_t("0 60 90;-22 60 90;0 60 90;22 60 90;0 60 90", dur="4s", kt="0;0.25;0.5;0.75;1", typ="rotate")}<rect x="44" y="86" width="32" height="12" rx="6" fill="#C8963E"/></g>'
    '<path d="M34 104 A28 28 0 0 0 86 104" fill="none" stroke="#C8963E" stroke-width="2.5" stroke-dasharray="3 4"/>',
    "İçe ve dışa çevirme")

_ex2("mt_pump", "apump", "Ayak bileğini yukarı aşağı oynatma", "Ayağınızı rahat ettiğiniz ölçüde yukarı çekin ve aşağı itin. Erken hareket dolaşımı destekler ve bacakta pıhtı riskini azaltır.", "10 tekrar, günde 3–5 kez")
_ex2("mt_circ", "mt_circle", "Ayak bileğiyle daire çizme", "Ayağınızla bir yöne yavaş daireler çizin, sonra yönü değiştirin.", "Her yöne 10 tekrar, günde 3–5 kez")
_ex2("mt_spread", "mt_toes", "Ayak parmaklarını açma", "Topuklarınız birbirine değerken ayak parmaklarınızı birbirinden ayırın ve ayaklarınızı hafifçe dışa çevirin. Ağrıya doğru zorlamayın.", "10 tekrar, günde 3–5 kez")
_ex2("mt_io", "mt_inout", "Ayağı içe ve dışa çevirme", "Oturun ya da uzanın. Ayağınızı rahat ettiğiniz kadar içe, sonra dışa doğru çevirin.", "10 tekrar, günde 3–4 kez")
_ex2("mt_stand", "sls", "Yaralı bacak üzerinde durma", "Rahatça yürüyebildiğinizde başlayın. Bir tezgâha tutunarak yaralı bacağınızın üzerinde durun; kolaylaştıkça tutunmadan deneyin.", "30 saniyeye kadar, günde 3–4 kez")
_ex2("mt_toe", "heel2", "Parmak ucunda yükselme", "Tutunarak iki ayağınızın parmak uçlarında yükselin ve yavaşça inin. Çok rahatsız edici olmadan yapın.", "8–12 tekrar, günde 3–4 kez")

MT5_FAQ = [
 ("Bot kırığın iyileşmesine yardım eder mi?", "Kemiğin tabanındaki kırıklarda bot ya da sert tabanlı ayakkabı yalnızca rahat etmeniz için verilir; iyileşmeyi hızlandırmaz. Yürürken giyin, dinlenirken ve gece çıkarabilirsiniz. Sağlam ayağınıza destekleyici bir ayakkabı giymek diğer eklemlerinizi korur. Taban çıkıntısındaki kopma kırığı olan 78 hastayla yapılan çok merkezli bir çalışmada, sert tabanlı ayakkabıyla tedavi edilenlerde 6. aydaki ağrı alçıyla tedavi edilenlerden farklı değildi (iki grupta da ağrının izin verdiği ölçüde basılabiliyordu) ve önceki etkinliklere dönüş daha erkendi (ortalama 37’ye karşı 43 gün)."),
 ("Jones kırığı nedir, neden farklı tedavi edilir?", "Jones kırığı, 5. tarak kemiğinin tabanına yakın ama biraz daha ileride olan bir kırıktır ve daha yavaş iyileşebilir. Bir NHS broşürüne göre ilk 6 hafta alçı ve koltuk değnekleriyle ayağa yük verilmez; daha sonra bota geçilebilir. Bu kırıkların küçük bir kısmı kendiliğinden kaynamaz ve ameliyat düşünülebilir. Kırık tipinizi ve ne kadar yük verebileceğinizi ekibiniz söyler."),
 ("Ne zaman araba kullanabilirim?", "Bottan ya da sert tabanlı ayakkabıdan çıktığınızda, rahat yürüyebildiğinizde, ani fren gibi acil manevraları ağrı ya da tereddüt olmadan yapabildiğinizde ve sigortanız sizi kapsadığında. Önce güvenli bir yerde deneyin."),
 ("Ne zaman spora dönebilirim?", "Ağrısız çömelebildiğiniz, sekebildiğiniz, zıplayabildiğiniz ve koşabildiğiniz zaman. Çoğu kişi 6–12 hafta içinde olağan etkinliklerine döner; koşu gibi daha zorlu etkinlikler bir süre daha rahatsızlık verebilir. Yapamıyorsanız fizyoterapi için hekiminize başvurun."),
 ("Ağrı ve şişlik ne kadar sürer?", "Kırık yaklaşık 6 haftada kaynar, ama ağrı ve şişlik 3–6 ay sürebilir. Şişlik genellikle günün sonunda artar ve 4. haftadan itibaren belirgin şekilde azalmalıdır. Sigara iyileşmeyi yavaşlatır, ileri durumlarda durdurabilir."),
]

MT5_SRC = [
 "University Hospitals Sussex NHS Foundation Trust, Physiotherapy. " + ext("https://www.uhsussex.nhs.uk/wp-content/uploads/2025/06/2559-Base-of-5th-metatarsal-fracture-no-follow-up-appointment-2025.pdf", "Base of 5th metatarsal fracture") + ". 2559, August 2025.",
 "Royal Free London NHS Foundation Trust, Virtual fracture clinic. " + ext("https://www.royalfree.nhs.uk/patients-and-visitors/patient-information-leaflets/fifth-metatarsal-fractures", "Fifth metatarsal fractures") + ". RFL949 version 4, June 2025.",
 "East Sussex Healthcare NHS Trust. " + ext("https://www.esht.nhs.uk/wp-content/uploads/2026/01/2033.pdf", "Fracture of the base of the 5th metatarsal (Jones)") + ". November 2025.",
 "Vu D, McDiarmid T, Brown M. " + ext("https://mdedge.com/content/what-most-effective-management-acute-fractures-base-fifth-metatarsal", "What is the most effective management of acute fractures of the base of the fifth metatarsal?") + ". J Fam Pract. 2006;55(8):713–717",
 "Choi YR, Kim BS, Kim YM, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/33252586/", "Hard-soled shoe versus short leg cast for a fifth metatarsal base avulsion fracture: a multicenter, noninferiority, randomized controlled trial") + ". J Bone Joint Surg Am. 2021;103(1):23–29.",
]

MT5_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Ayak dış kenarı (5. tarak kemiği) kırığı</h1>
    <p class="lede">Ayağınızı burktuktan sonra ayağınızın dış kenarında, küçük parmağa giden uzun kemikte ağrı ve şişlik mi var? Bu kemik 5. metatars ya da 5. tarak kemiğidir. Kırıkların çoğu sorunsuz iyileşir: kemik yaklaşık 6 haftada kaynar, ağrının izin verdiği ölçüde yürümek de iyileşmeye yardım eder. Bu sayfa hangi kırıkta neye dikkat etmeniz gerektiğini ve evde yapabileceğiniz egzersizleri anlatıyor.</p>
    <p class="meta">Son güncelleme: 19 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>6 hafta</b><span>Kırığın kaynaması için gereken yaklaşık süre</span></div>
        <div class="stat"><b>3–6 ay</b><span>Ağrı ve şişliğin sürebileceği süre</span></div>
        <div class="stat"><b>4. hafta</b><span>Şişliğin belirgin şekilde azalmaya başlaması beklenir</span></div>
        <div class="stat"><b>6–12 hafta</b><span>Çoğu kişinin olağan etkinliklerine döndüğü süre</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Kırığın yeri tedaviyi belirler</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Taban kırığı</h3><p>Kemiğin ayak bileğine yakın ucundaki kırıklar. Bot ya da sert tabanlı ayakkabı yalnızca rahatlık içindir; ağrının izin verdiği ölçüde ayağınıza basarak yürüyebilirsiniz. Gerekirse koltuk değneği kullanın.</p></div>
        <div class="kind"><span class="n">2</span><h3>Jones kırığı</h3><p>Tabana yakın ama biraz daha ileride. Daha yavaş iyileşebilir: ilk haftalarda alçı ve koltuk değnekleriyle ayağa yük verilmeyebilir. Küçük bir kısmı kaynamaz ve ameliyat gerekebilir.</p></div>
        <div class="kind"><span class="n">3</span><h3>Gövde kırığı</h3><p>Kemiğin orta kısmındaki kırıklar. Bot genellikle rahatlık içindir, rahat ettiğiniz ölçüde yürümek teşvik edilir; ilk adımlarda topuğa basmak daha kolay olabilir.</p></div>
        <div class="kind"><span class="n">4</span><h3>İlk 24–72 saat</h3><p>Ayağınızı dinlendirin ve yastıklarla kalça hizasının üzerine kaldırın. Havluya sarılı buzu 15 dakikaya kadar, birkaç saatte bir uygulayın.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Haftalara göre</h2>
        <ul class="dots">
          <li><strong>0–3. hafta:</strong> Yürürken botu giyin, dinlenirken ve gece çıkarın. Ağrı izin verdikçe ayağınıza basın, kendinizi hazır hissettiğinizde koltuk değneğini bırakın.</li>
          <li><strong>3–6. hafta:</strong> Botu kademeli olarak azaltın, olağan işlerinize dönün.</li>
          <li><strong>6–12. hafta:</strong> Çoğu kişi olağan etkinliklerine döner; uzun yürüyüşler ve koşu bir süre daha rahatsızlık ve şişlik yapabilir.</li>
        </ul>
        <p class="soft">Jones kırığında bu takvim farklıdır; ne zaman ve ne kadar yük vereceğinizi kırık kliniği söyler.</p>
      </div>
      <div>
        <h2>Neler iyi gelir?</h2>
        <ul class="dots">
          <li>Ağrı kesicinizi kutusundaki dozda kullanın; ağrınız geçmiyorsa hekiminize ya da eczacınıza danışın.</li>
          <li>Gün sonunda artan şişlik için ayağınızı yükseğe kaldırın.</li>
          <li>Sağlam ayağınıza destekleyici bir ayakkabı ya da spor ayakkabı giyin.</li>
          <li>Sigara içiyorsanız bırakın ya da azaltın; özellikle ilk 2 hafta önemlidir.</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Ayağı ve ayak bileğini hareketli tutan altı egzersiz</h2>
      <p class="soft">İlk dört egzersize olabildiğince erken başlayın; ağrınızı belirgin şekilde artırmadan yapın. Son ikisi ayakta yapılır: rahatça yürüyebildiğinizde başlayın. Jones kırığında ayakta yapılan egzersizler için ekibinizin onayını bekleyin.</p>
      {ex_grid(["mt_pump", "mt_circ", "mt_spread", "mt_io", "mt_stand", "mt_toe"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(MT5_FAQ)}
      <p class="soft" style="margin-top:18px">Ayak bileğinin burkulması için <a href="ayak-bilegi-burkulmasi.html">ayak bileği burkulması</a>, ayak bileği kemiklerinin kırılması için <a href="ayak-bilegi-kirigi.html">ayak bileği kırığı</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman acile ya da hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Baldırınızda hareketle artan ağrı, ağırlık hissi, kızarıklık, sıcaklık ya da artan şişlik varsa: bacakta pıhtı olabilir, hemen acil servise başvurun</li>
        <li>Diyabetiniz varsa ve ayağınızda renk değişikliği ya da kızarıklık fark ederseniz</li>
        <li>Şişlik 4. haftadan sonra belirgin şekilde azalmıyorsa</li>
        <li>6. haftada hâlâ belirgin ağrı ve şişlik varsa ya da botsuz yürümekte zorlanıyorsanız</li>
        <li>Kırığın bulunduğu bölgeden uzakta ağrı ya da başka belirtiler varsa</li>
      </ul>
      {CTA_CARD("Ayak kırığı sonrası rehabilitasyonunuz", "5. metatars (ayak dış kenarı) kırığı sonrası rehabilitasyon")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(MT5_SRC)}
    </div>
  </section>
</main>'''

page("besinci-metatars-kirigi.html", "Ayak Dış Kenarı (5. Tarak Kemiği) Kırığı",
     "Ayak dış kenarında kırık: 5. metatars kırığı ne kadar sürede iyileşir, bot ne zaman bırakılır, Jones kırığı neden farklıdır? Haftalara göre iyileşme ve altı egzersiz.",
     "besinci-metatars-kirigi.html", NECK_CSS, MT5_BODY, "",
     seo_title="5. Metatars (Ayak Dış Kenarı) Kırığı: İyileşme, Bot ve Egzersizler | İhsan Eren",
     condition="Beşinci metatars kırığı", faq_items=MT5_FAQ)

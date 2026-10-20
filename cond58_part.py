# -*- coding: utf-8 -*-
# Yeni rehber (58): Omuz ucu (akromiyoklaviküler eklem) yaralanması. cond57_part.py'den sonra exec edilir. Video yok.
# University Hospitals Sussex (2654, Kasım 2025), Sherwood Forest (PIL202511-01, Kasım 2025) ve King's College Hospital (Ocak 2025) NHS broşürlerine göre.

# Sırtüstü yatarak sağlam elle yaralı kolu baş üstüne doğru kaldırma
SV["ac_assist"] = fig(GRD +
    '<circle class="hd" cx="96" cy="100" r="7"/>'
    '<path class="fig" d="M88 106 H40 M40 106 L28 90 L18 108"/>'
    f'<path class="fig hl" d="M80 104 L66 84">{anim_d("M80 104 L66 84;M80 104 L100 76;M80 104 L66 84", dur="4s")}</path>'
    f'<path class="fig" d="M78 104 L64 88">{anim_d("M78 104 L64 88;M78 104 L98 80;M78 104 L64 88", dur="4s")}</path>',
    "Destekli kol kaldırma")

_ex2("ac_hand", "grip", "El ve el bileği", "Elinizi 10 kez açıp kapatın, sonra bileğinizi 10 kez yukarı aşağı oynatın. Birkaç gün sonra yumuşak bir topu 5 saniye sıkıp bırakın.", "10 tekrar, günde 5 kez")
_ex2("ac_elbow", "ly_arm", "Dirseği bükme ve düzeltme", "Dirseğinizi bükün ve düzeltin; gerekirse diğer elinizle yardım edin. Dirseğiniz gövdenizin yanında 90 derece bükülüyken avucunuzu yukarı ve aşağı çevirin. Ağrı artarsa durun.", "10 tekrar, günde 5 kez")
_ex2("ac_post", "scap", "Dik duruş", "Omuzlarınızı geriye alın ve kürek kemiklerinizi hafifçe birbirine yaklaştırın.", "30 saniye tutun, 5 tekrar")
_ex2("ac_pend", "cf_pendf", "Sarkaç", "Sağlam elinizle sağlam bir yüzeye dayanıp öne eğilin. Yaralı kolunuzu gevşek bırakın ve hafifçe öne arkaya, yandan yana ve küçük daireler çizecek şekilde sallayın.", "Toplam 1–2 dakika")
_ex2("ac_lift", "ac_assist", "Destekli kol kaldırma", "3. haftadan itibaren başlayın. Sırtüstü uzanın, sağlam elinizle yaralı kolunuzu bileğinden tutun ve başınıza doğru rahat ettiğiniz kadar kaldırın, sonra indirin.", "10 tekrar, günde 5 kez")
_ex2("ac_rot", "cf_stickf", "Sopayla dışa döndürme", "3. haftadan itibaren başlayın. Dirseğinizi gövdenizin yanında bükülü tutun, bir sopa ya da şemsiyeyle ön kolunuzu dışa doğru itin. Sopa yoksa sağlam elinizle bileğinizi dışa doğru yönlendirin.", "10 tekrar, günde 5 kez")

ACJ_FAQ = [
 ("Ameliyat gerekir mi?", "Çoğu zaman gerekmez; omuz ucu yaralanmalarının çoğu askı, egzersiz ve fizyoterapiyle iyileşir. Bağların ciddi yırtıldığı ve eklemin belirgin şekilde ayrıldığı bazı durumlarda ameliyat düşünülebilir. Ameliyattan sonra askı genellikle 6 hafta takılır ve temas sporlarına dönüş 12 haftayı bulur. Altı çalışmayı inceleyen 2019 tarihli bir Cochrane derlemesi, yetişkinlerde ameliyatın ameliyatsız tedaviden daha iyi sonuç verdiğini göstermedi; yan etkilerin çoğu ameliyat grubunda görüldü."),
 ("Omzumdaki tümsek geçer mi?", "Hafif yaralanmalarda iyileşmeden sonra köprücük kemiğinin ucunda küçük ve ağrısız bir tümsek kalması normaldir; günlük işlerinizi etkilemez. Belirtiler 3–6 ay sürebilir."),
 ("Ne zaman işe dönebilirim?", "İşinize göre değişir. Bir NHS broşürüne göre kaldırma gerektirmeyen hafif işlere 1–3 hafta, omuz hizasının altında hafif kaldırma gerektiren işlere 3–6 hafta, omuz hizasının üstünde çalışılan ağır işlere 6–12 hafta sonra dönülebilir."),
 ("Ne zaman araba kullanabilirim?", "Askıyı bıraktığınızda, direksiyonu ağrısız çevirebildiğinizde ve ani fren gibi acil durumlarda ağrı ya da tereddüt olmadan tepki verebildiğinizde. Askıyla araç kullanmayın, önce güvenli bir yerde deneyin ve sigortanızın sizi kapsadığından emin olun."),
 ("Nasıl uyumalıyım?", "Sırtüstü ya da sağlam tarafınıza yatın, yaralı omzunuzun üzerine yatmayın. Sırtüstü yatarken yaralı kolunuzun dirseğinin altına bir yastık koyabilirsiniz. Yan yatarken önünüze koyduğunuz bir yastık elinizi dinlendirmenize yardım eder."),
]

ACJ_SRC = [
 "University Hospitals Sussex NHS Foundation Trust, Physiotherapy. " + ext("https://www.uhsussex.nhs.uk/wp-content/uploads/2025/11/2654-Minor-injury-to-acromioclavicular-joint-ACJ-grade-1-to-2-injury-2025.pdf", "Minor injury to acromioclavicular joint (ACJ): grade 1 to 2 injury") + ". 2654, November 2025.",
 "Sherwood Forest Hospitals NHS Foundation Trust. " + ext("https://sfh-tr.nhs.uk/media/s0rej40i/pil202511-01-acji-acromioclavicular-joint-injury.pdf", "Acromioclavicular (AC) joint injury") + ". PIL202511-01-ACJI, November 2025.",
 "King’s College Hospital NHS Foundation Trust. " + ext("https://kch.nhs.uk/wp-content/uploads/2025/01/4132-Acromioclavicular-joint-patient-leaflet-v5_FINAL.pdf", "Acromioclavicular joint stabilisation") + ". PL1217.1, January 2025.",
 "Tamaoki MJS, Lenza M, Matsunaga FT, et al. " + ext("https://doi.org/10.1002/14651858.CD007429.pub3", "Surgical versus conservative interventions for treating acromioclavicular dislocation of the shoulder in adults") + ". Cochrane Database Syst Rev. 2019;(10):CD007429",
]

ACJ_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Omuz ucu (AC eklem) yaralanması</h1>
    <p class="lede">Bisikletten ya da sporda omzunuzun üzerine düştünüz ve omzunuzun en üst ucunda ağrı, şişlik ya da bir tümsek mi var? Köprücük kemiğinin kürek kemiğiyle birleştiği bu küçük eklemin bağları burkulmuş ya da yırtılmış olabilir. Hafif yaralanmalar genellikle 3–6 haftada iyileşir; çoğu yaralanma ameliyat gerektirmez, askı ve egzersizlerle düzelir.</p>
    <p class="meta">Son güncelleme: 19 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>3–6 hafta</b><span>Hafif yaralanmaların genellikle iyileştiği süre</span></div>
        <div class="stat"><b>En fazla 3 hafta</b><span>Askının kullanıldığı süre; gece takmak gerekmez</span></div>
        <div class="stat"><b>2 hafta</b><span>Kolu omuz hizasının üzerine kaldırmama süresi</span></div>
        <div class="stat"><b>6 hafta</b><span>Ağır yük kaldırmaktan kaçınma süresi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Omuz ucunda, tam köprücük kemiğinin bittiği yerde ağrı.</li>
          <li>Şişlik ve bazen görünür bir tümsek ya da şekil değişikliği.</li>
          <li>Omuz hareketlerinde azalma.</li>
        </ul>
        <p class="soft">Yaralanmalar, röntgeni normal olan bir burkulmadan bağların gerildiği ya da yırtıldığı durumlara kadar değişir. Hafif yaralanmalarda eklemin kemikleri ya hiç kaymaz ya da çok az kayar.</p>
      </div>
      <div>
        <h2>İlk günlerde</h2>
        <ul class="dots">
          <li>Havluya sarılı buzu 15 dakika, birkaç saatte bir uygulayın; buzu doğrudan cildinize koymayın.</li>
          <li>Ağrı kesicinizi kutusundaki dozda kullanın; ağrınız geçmiyorsa hekiminize ya da eczacınıza danışın.</li>
          <li>Askıyı ağrıyı azaltmak için kullanın. Yemek yemek, giyinmek ve duş almak için rahat ettiğinizde çıkarabilirsiniz; bu yaralanmayı kötüleştirmez.</li>
          <li>Kolunuzu 24–72 saat dinlendirin, ama parmaklarınızı, bileğinizi ve omzunuzu nazikçe hareket ettirmeyi sürdürün.</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Omzu hareketli tutan altı egzersiz</h2>
      <p class="soft">İlk dört egzersize hemen başlayın, günde 5 kez yapmayı hedefleyin; ağrı artarsa sayıyı azaltın. Son ikisini 3. haftadan itibaren ekleyin. 6. haftadan sonra kolunuzu öne ve yana rahat ettiğiniz kadar yükseğe kaldırmaya başlayabilir, ağrıya göre günlük işlerinize dönebilirsiniz.</p>
      {ex_grid(["ac_hand", "ac_elbow", "ac_post", "ac_pend", "ac_lift", "ac_rot"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(ACJ_FAQ)}
      <p class="soft" style="margin-top:18px">Köprücük kemiğinin ortasından kırılması için <a href="koprucuk-kemigi-kirigi.html">köprücük kemiği kırığı</a>, omzun yerinden çıkması için <a href="omuz-cikigi.html">omuz çıkığı</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman ekibinize ya da hekiminize başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Ağrınız basit ağrı kesicilerle kontrol altına alınamıyorsa</li>
        <li>3. haftada hâlâ belirgin ağrı ve şişlik varsa</li>
        <li>Omzunuzdan uzak bölgelerde ağrı varsa</li>
        <li>6. haftada omzunuzu yaralanmadan önceki gibi hareket ettiremiyorsanız</li>
      </ul>
      <p class="soft">Sigara ve elektronik sigara iyileşmeyi yavaşlatır; özellikle ilk 2 haftada bırakmak ya da azaltmak önemlidir.</p>
      {CTA_CARD("Omuz ucu yaralanması sonrası rehabilitasyonunuz", "omuz ucu (AC eklem) yaralanması sonrası rehabilitasyon")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(ACJ_SRC)}
    </div>
  </section>
</main>'''

page("omuz-ucu-yaralanmasi.html", "Omuz Ucu (AC Eklem) Yaralanması",
     "Omzun üstüne düştükten sonra omuz ucunda ağrı ve tümsek: AC eklem yaralanması ne kadar sürede iyileşir, askı ne kadar takılır, ne zaman işe ve araç kullanmaya dönülür? Altı egzersiz.",
     "omuz-ucu-yaralanmasi.html", NECK_CSS, ACJ_BODY, "",
     seo_title="Omuz Ucu (AC Eklem) Yaralanması: İyileşme Süresi, Askı ve Egzersizler | İhsan Eren",
     condition="Akromiyoklaviküler eklem yaralanması", faq_items=ACJ_FAQ)

# -*- coding: utf-8 -*-
# Yeni rehber (60): Bebeklerde (doğumsal kas kaynaklı) tortikolis. cond59_part.py'den sonra exec edilir. Video yok.
# Royal Berkshire (Haziran 2025) ve NHS Lothian, Royal Hospital for Children and Young People (V4.0, Eylül 2023) broşürlerine göre.

_BABY = ('<rect x="47" y="46" width="26" height="40" rx="12" fill="#2A6F6B"/>'
         '<path class="fig" d="M50 56 L38 66 M70 56 L82 66 M54 84 L50 104 M66 84 L70 104"/>')
# Yana eğme: sırtüstü bebek, bir omuz sabit, kulak karşı omza doğru (üstten)
SV["tor_side"] = fig(_BABY +
    f'<g>{anim_t("0 60 44;-22 60 44;0 60 44", dur="4s", typ="rotate")}<circle class="hd" cx="60" cy="32" r="12"/></g>'
    '<rect x="70" y="44" width="14" height="9" rx="4" fill="#C8963E"/>'
    '<path d="M36 22 A26 26 0 0 0 40 46" fill="none" stroke="#C8963E" stroke-width="2.5" stroke-dasharray="3 4" stroke-linecap="round"/>',
    "Yana eğme")
# Döndürme: çene etkilenen omza doğru çevrilir (üstten)
SV["tor_rot"] = fig(_BABY +
    '<circle class="hd" cx="60" cy="32" r="12"/>'
    f'<g>{anim_t("0 60 32;-55 60 32;0 60 32", dur="4s", typ="rotate")}<circle cx="60" cy="22" r="3.2" fill="#C8963E"/></g>'
    '<rect x="70" y="44" width="14" height="9" rx="4" fill="#C8963E"/>'
    '<path d="M44 16 A20 20 0 0 0 40 34" fill="none" stroke="#C8963E" stroke-width="2.5" stroke-dasharray="3 4" stroke-linecap="round"/>',
    "Başı çevirme")
# Ön kolda yan yatırarak taşıma (yandan)
SV["tor_carry"] = fig(
    '<path class="fig" d="M14 78 L96 78" stroke-width="9"/>'
    '<rect x="40" y="56" width="40" height="18" rx="9" fill="#2A6F6B"/>'
    '<path class="fig" d="M80 66 L98 60 M80 70 L98 74"/>'
    f'<g>{anim_t("0 40 66;-14 40 66;0 40 66", dur="4s", typ="rotate")}<circle class="hd" cx="28" cy="62" r="11"/></g>'
    '<path d="M96 78 L108 92" class="fig"/>'
    '<path d="M22 86 q8 8 18 0" fill="none" stroke="#C8963E" stroke-width="2.5" stroke-linecap="round"/>',
    "Kolda taşıma")
# Karın üstü oyun: başını kaldırır, oyuncak zor tarafta (yandan)
SV["tor_tummy"] = fig(GRD +
    '<rect x="40" y="96" width="40" height="14" rx="7" fill="#2A6F6B"/>'
    '<path class="fig" d="M80 104 L102 108"/>'
    f'<g>{anim_t("0 40 102;18 40 102;0 40 102", dur="4s", typ="rotate")}<circle class="hd" cx="28" cy="96" r="10"/></g>'
    '<path class="fig" d="M44 100 L40 110"/>'
    '<circle cx="12" cy="74" r="7" fill="#C8963E"/><path d="M12 81 V90" stroke="#C8963E" stroke-width="2.5"/>',
    "Karın üstü oyun")

_ex2("tor_s", "tor_side", "Yana eğme germesi", "Bebeğinizi sırtüstü yatırın. Etkilenen taraftaki omzunu bir elinizle nazikçe sabitleyin, diğer elinizle başını kavrayın ve karşı taraftaki kulağını karşı omzuna doğru yavaşça yaklaştırın.", "10–15 saniye tutun, gün içinde birkaç kez")
_ex2("tor_r", "tor_rot", "Başı çevirme germesi", "Bebeğiniz sırtüstüyken karşı taraftaki omzunu nazikçe sabitleyin ve başını yavaşça etkilenen tarafa, o omzun üzerinden bakacak şekilde çevirin.", "10–15 saniye tutun, gün içinde birkaç kez")
_ex2("tor_c", "tor_carry", "Kolda yan yatırarak taşıma", "Bebeğinizi yüzü sizden uzağa bakacak şekilde, etkilenen taraftaki kulağı ön kolunuza gelecek biçimde yan yatırarak taşıyın. Ön kolunuz başını omzundan hafifçe uzaklaştırarak yana eğme germesi yapar; diğer kolunuzla gövdesini destekleyin.", "Gün içinde taşırken")
_ex2("tor_t", "tor_tummy", "Karın üstü oyun", "Bebeğiniz uyanıkken ve siz yanındayken her gün karın üstünde zaman geçirmesini sağlayın. Oyuncakları ve yüzünüzü, başını çevirmekte zorlandığı tarafa koyun; dirsekleri omuzlarının altında olsun, göğsünün altına rulo yapılmış bir havlu koyabilirsiniz.", "Her gün, uyanıkken")

TOR_FAQ = [
 ("Tortikolis bebeğimi acıtır mı?", "Çoğu bebek tortikolisten ağrı duymaz. Germeler sırasında bebeğiniz itiraz edebilir, ama canı yanmamalıdır; hareketleri yavaş ve nazik yapın."),
 ("Düzelir mi, ne kadar sürer?", "Tedaviyle çoğu bebek boynunu tam olarak hareket ettirebilir hâle gelir; kas büyüdükçe ve gerildikçe esner. Tedavi edilmezse boyun hareketlerinde kalıcı kısıtlılık kalabilir ve ileride ameliyat gerekebilir. Fizyoterapiyle 3 ay içinde düzelme olmazsa ortopedi değerlendirmesi istenebilir."),
 ("Fizyoterapi ne zaman biter?", "Amerikan Fizyoterapi Derneği’nin kılavuzuna göre, bebeğin boynu sağlam tarafla arasında 5 dereceden az fark kalacak kadar hareket ettiğinde, başında görünür bir eğiklik kalmadığında, yaşına uygun hareketleri yapabildiğinde ve iki yana eşit hareket ettiğinde, siz de egzersizleri ve neye dikkat edeceğinizi öğrendiğinizde tedavi sonlandırılabilir."),
 ("Boynundaki şişlik nedir?", "Etkilenen kasta küçük bir şişlik olabilir. Genellikle ilk ayda en büyük hâline ulaşır, sonra yavaş yavaş küçülür. Geçmezse ultrason istenebilir."),
 ("Başının arkası düzleşti, bu tehlikeli mi?", "Tortikolis, bebeğin hep aynı tarafa yatmasına ve başın o tarafta düzleşmesine (plajiyosefali) yol açabilir. Bu yalnızca görünümle ilgilidir, başka belirtisi yoktur ve beyni etkilemez. Fizyoterapistiniz gerekirse ayrıca önerilerde bulunur."),
 ("Nasıl beslemeliyim?", "Biberonla besliyorsanız bebeğinizi, başını zorlandığı tarafa çevirmesini gerektirecek kolunuzda tutun. Emziriyorsanız iki taraftan da emzirmeyi sürdürün ve bu tarafa dönmesini teşvik eden farklı tutuşlar deneyin."),
]

TOR_SRC = [
 "Royal Berkshire NHS Foundation Trust, Paediatric Physiotherapy. " + ext("https://royalberkshire.nhs.uk/media/4r0hxeui/congenital-muscular-torticollis-affecting-the-left_jun25.pdf", "Congenital muscular torticollis affecting the left") + ". June 2025.",
 "NHS Lothian, Royal Hospital for Children and Young People. " + ext("https://apps.nhslothian.scot/files/sites/2/Congenital-Torticollis-left-RHCYP-V4.0.pdf", "Congenital torticollis (left side)") + ". Version 4.0, September 2023.",
 "Kaplan SL, Coulter C, Sargent B. " + ext("https://www.apta.org/patient-care/evidence-based-practice-resources/cpgs/physical-therapy-management-of-congenital-muscular-torticollis-a-2018-evidence-based-clinical-practice-guideline-from-the-apta-academy-of-pediatric-physical-therapy-cpg", "Physical therapy management of congenital muscular torticollis: a 2018 evidence-based clinical practice guideline from the APTA Academy of Pediatric Physical Therapy") + ". Pediatr Phys Ther. 2018;30(4):240–290.",
]

TOR_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Bebeklerde tortikolis</h1>
    <p class="lede">Bebeğinizin başı hep bir yana eğik, yüzü hep diğer tarafa mı dönük? Bu, boynun yan tarafındaki bir kasın (sternokleidomastoid) kısa ya da gergin olmasından kaynaklanan doğumsal kas tortikolisi olabilir. Doğumda ya da ilk üç ay içinde ortaya çıkar ve oldukça sık görülür. İyi haber: düzenli germeler, doğru taşıma ve oyunla çoğu bebek boynunu tam olarak hareket ettirebilir hâle gelir.</p>
    <p class="meta">Son güncelleme: 19 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>0–3 ay</b><span>Tortikolisin ortaya çıktığı dönem</span></div>
        <div class="stat"><b>10–15 saniye</b><span>Her germenin tutulduğu süre</span></div>
        <div class="stat"><b>Her gün</b><span>Uyanıkken, gözetim altında karın üstü oyun</span></div>
        <div class="stat"><b>3 ay</b><span>Düzelme olmazsa ortopedi değerlendirmesi düşünülür</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Baş etkilenen tarafa eğik, çene ise diğer tarafa dönük durur.</li>
          <li>Bebek hep aynı tarafa bakar, başını ortada tutmakta zorlanır.</li>
          <li>Emzirirken başını bir tarafa çevirmekte zorlanabilir.</li>
          <li>Boynun yan tarafında küçük bir şişlik olabilir.</li>
          <li>Başın, yatmayı tercih ettiği tarafta düzleşmesi (plajiyosefali).</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Anne karnındaki pozisyon; makattan gelişte daha sık.</li>
          <li>Forseps (doğum maşası) ile doğum ya da doğum sırasında zorlanma.</li>
          <li>Bebeğin dikkatinin hep aynı tarafa çekilmesi, örneğin arabasında hep aynı yerde duran sevdiği bir oyuncak.</li>
          <li>Bazen nedeni bilinmez.</li>
        </ul>
        <p class="soft">Bebeklerde baş eğikliğinin başka nedenleri de olabileceği için önce bir hekimin ve çocuk fizyoterapistinin değerlendirmesi gerekir.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Günlük hayatta: zor tarafa baktırın</h2>
      <p class="soft">Aşağıdaki örnekler, başı sola eğik ve sağa bakmayı tercih eden (sol taraflı) bir bebek içindir. Bebeğinizin sağ tarafı etkilenmişse yönleri tersine çevirin.</p>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Karşı tarafa ilgi</h3><p>Oyuncakları, sesleri ve yüzünüzü bebeğinizin sola bakması gereken yere koyun. Beşiğini, sizi görmek için sola bakacağı şekilde yerleştirin.</p></div>
        <div class="kind"><span class="n">2</span><h3>Araba koltuğu</h3><p>Araba koltuğunu, pencere bebeğinizin sol tarafında kalacak şekilde yerleştirin; ışığa doğru bakmak için başını sola çevirir.</p></div>
        <div class="kind"><span class="n">3</span><h3>Omuzda taşırken</h3><p>Bebeğinizi sağ omzunuzda taşıyın: etrafına bakmak için başını sola çevirir, sağa dönmesini ise yanağınız sınırlar.</p></div>
        <div class="kind"><span class="n">4</span><h3>Yan yatarak oyun</h3><p>Yan yatarak oynamak ellerini birleştirmesini ve göz-el uyumunu destekler; yer çekimi boynuna nazik bir germe de sağlar.</p></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde germe ve oyun</p>
      <h2>Fizyoterapistin gösterdiği dört uygulama</h2>
      <p class="soft">Germeleri önce bir çocuk fizyoterapistinin size göstermesi gerekir. Yavaş ve nazik yapın, gün içinde birkaç kez tekrarlayın. Bebeğiniz itiraz edebilir ama canı yanmamalıdır. Örnekler sol taraflı tortikolis içindir.</p>
      {ex_grid(["tor_s", "tor_r", "tor_c", "tor_t"], "ex four")}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(TOR_FAQ)}
      <p class="soft" style="margin-top:18px">Yetişkinlerde ani başlayan boyun tutulması için <a href="boyun-tutulmasi.html">boyun tutulması</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman fizyoterapistinize ya da hekiminize başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Bebeğinizin başındaki eğiklik ya da tek tarafa bakma isteği artıyorsa</li>
        <li>Germeleri yapmakta zorlanıyorsanız ya da bebeğinizin canı yanıyor gibi görünüyorsa</li>
        <li>Boynundaki şişlik küçülmüyorsa</li>
        <li>Başının arkasında ya da yanında belirgin bir düzleşme fark ediyorsanız</li>
      </ul>
      {CTA_CARD("Bebeğinizin tortikolisi", "bebeğimin tortikolisi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(TOR_SRC)}
    </div>
  </section>
</main>'''

page("bebeklerde-tortikolis.html", "Bebeklerde Tortikolis",
     "Bebeğinizin başı hep bir yana mı eğik? Doğumsal kas tortikolisi nedir, neden olur, nasıl düzelir? Günlük taşıma ve oyun önerileri, fizyoterapistin gösterdiği germeler.",
     "bebeklerde-tortikolis.html", NECK_CSS, TOR_BODY, "",
     seo_title="Bebeklerde Tortikolis: Belirtiler, Germeler ve Günlük Öneriler | İhsan Eren",
     condition="Doğumsal kas tortikolisi", faq_items=TOR_FAQ)

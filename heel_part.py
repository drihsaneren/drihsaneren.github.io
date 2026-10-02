# -*- coding: utf-8 -*-
# Topuk dikeni (plantar fasiit) sayfası. stroke_part.py'den sonra exec edilir.

WALL_R = '<path class="obj" d="M104 10 V112" stroke-width="5"/>'

# Parmakları geriye çekerek germe (yakın plan ayak, içten görünüm)
SV["pfst"] = fig(
    '<path class="fig" d="M40 8 L44 62"/>'
    '<path d="M38 60 L50 60 L56 70 L86 82 Q92 85 90 90 L46 92 Q32 92 32 82 Z" fill="#2A6F6B"/>'
    '<path class="band" d="M40 96 Q64 99 88 95"><animate attributeName="opacity" values=".35;1;.35" dur="3.2s" repeatCount="indefinite"/></path>'
    f'<g>{anim_t("0 88 88;-42 88 88;0 88 88", typ="rotate")}<path class="fig hl" d="M88 88 L106 88"/></g>'
    f'<path class="fig" d="M114 40 L108 86">{anim_d("M114 40 L108 86;M114 40 L102 76;M114 40 L108 86")}</path>',
    "Parmakları geriye çekerek germe")

# Havluyla germe (yerde, bacaklar düz)
SV["towelst"] = fig(GRD + '<g transform="translate(0 4)">' +
    '<circle class="hd" cx="36" cy="62" r="7"/>'
    '<path class="fig" d="M34 72 L30 104 L92 104"/>'
    f'<path class="fig hl" d="M92 104 L98 92">{anim_d("M92 104 L98 92;M92 104 L90 91;M92 104 L98 92")}</path>'
    f'<path class="band" d="M68 88 L98 92">{anim_d("M68 88 L98 92;M60 86 L90 91;M68 88 L98 92")}</path>'
    f'<path class="fig" d="M34 78 L54 88 L68 88">{anim_d("M34 78 L54 88 L68 88;M34 78 L48 90 L60 86;M34 78 L54 88 L68 88")}</path></g>',
    "Havluyla germe")

# Duvarda baldır germe (arka diz düz)
SV["calf"] = fig(GRD + WALL_R +
    f'<g>{anim_t("0 0;6 4;0 0")}<path class="fig" d="M56 68 L70 38"/><circle class="hd" cx="74" cy="28" r="7"/></g>'
    f'<path class="fig" d="M68 44 L86 46 L101 38">{anim_d("M68 44 L86 46 L101 38;M74 48 L90 50 L101 38;M68 44 L86 46 L101 38")}</path>'
    f'<path class="fig" d="M56 68 L72 86 L70 108 L80 111">{anim_d("M56 68 L72 86 L70 108 L80 111;M62 72 L80 88 L70 108 L80 111;M56 68 L72 86 L70 108 L80 111")}</path>'
    f'<path class="fig hl" d="M56 68 L28 108 L40 111">{anim_d("M56 68 L28 108 L40 111;M62 72 L28 108 L40 111;M56 68 L28 108 L40 111")}</path>',
    "Duvarda baldır germe")

# Dizi bükük baldır germe (arka diz bükülü, kalça aşağı iner)
SV["soleus"] = fig(GRD + WALL_R +
    f'<g>{anim_t("0 0;2 8;0 0")}<path class="fig" d="M56 70 L70 40"/><circle class="hd" cx="74" cy="30" r="7"/></g>'
    f'<path class="fig" d="M68 46 L86 46 L101 40">{anim_d("M68 46 L86 46 L101 40;M70 54 L88 50 L101 40;M68 46 L86 46 L101 40")}</path>'
    f'<path class="fig" d="M56 70 L72 88 L70 108 L80 111">{anim_d("M56 70 L72 88 L70 108 L80 111;M58 78 L78 92 L70 108 L80 111;M56 70 L72 88 L70 108 L80 111")}</path>'
    f'<path class="fig hl" d="M56 70 L46 90 L34 108 L44 111">{anim_d("M56 70 L46 90 L34 108 L44 111;M58 78 L50 96 L34 108 L44 111;M56 70 L46 90 L34 108 L44 111")}</path>',
    "Dizi bükük baldır germe")

# Havlulu topuk kaldırma (Rathleff): basamakta tek ayak, parmak altında havlu rulosu
SV["rathleff"] = fig(GRD +
    '<path class="obj" d="M50 96 H82 V112 M50 96 V112"/>'
    '<path class="obj" d="M88 58 H114 M108 58 V112"/>'
    '<circle cx="63" cy="92" r="3.2" fill="#C8963E"/>'
    f'<g>{anim_t("0 0;0 -9;0 0")}<path class="fig" d="M48 58 L48 28 M48 58 L42 78 L32 74"/><circle class="hd" cx="49" cy="19" r="7"/></g>'
    f'<path class="fig" d="M48 34 L68 46 L90 58">{anim_d("M48 34 L68 46 L90 58;M48 25 L68 40 L90 58;M48 34 L68 46 L90 58")}</path>'
    f'<path class="fig hl" d="M48 58 L47 94 L58 96 L66 89">{anim_d("M48 58 L47 94 L58 96 L66 89;M48 49 L51 84 L58 96 L66 89;M48 58 L47 94 L58 96 L66 89")}</path>',
    "Havlulu topuk kaldırma")

# Şişe ile ayak altı masajı (oturarak)
SV["roll"] = fig(GRD + STR_CHAIR +
    '<path class="fig" d="M34 76 L37 44 M37 50 L48 64 L58 70 M34 76 L62 76"/><circle class="hd" cx="39" cy="34" r="7"/>'
    f'<g>{anim_t("0 68 106;360 68 106;0 68 106", dur="3.2s")}<circle cx="68" cy="106" r="5.5" fill="#C8963E"/><path d="M68 101.5 V104" stroke="#f3ecd8" stroke-width="2" stroke-linecap="round"/></g>'
    f'<path class="fig hl" d="M62 76 L64 97 L80 100">{anim_d("M62 76 L64 97 L80 100;M62 76 L54 97 L70 100;M62 76 L64 97 L80 100")}</path>',
    "Şişe ile ayak altı masajı")

EXT.update({
 "pfst": ("Parmakları geriye çekerek germe", "Oturun, ağrılı ayağınızı diğer dizinizin üzerine alın. Bir elinizle ayak parmaklarınızı ayak sırtınıza doğru geriye çekin; ayak tabanınızda, topuğun önünde gerilme hissedin. Sabah ilk adımlardan önce ve uzun oturduktan sonra yapmak özellikle faydalıdır.", "10 saniye, 10 tekrar, günde 3 kez"),
 "towelst": ("Havluyla germe", "Yere ya da yatağa bacaklarınız düz olacak şekilde oturun. Bir havluyu ayağınızın ön kısmına dolayıp uçlarından tutun. Dizinizi düz tutarak havluyu kendinize doğru çekin; baldırınızda ve ayak tabanınızda gerilme hissedin.", "30 saniye, 3 tekrar"),
 "calf": ("Duvarda baldır germe", "Ellerinizi duvara dayayın, ağrılı bacağınızı arkaya alın. Arkadaki dizinizi düz, topuğunuzu yerde tutarak kalçanızı duvara doğru ilerletin; baldırınızın üst kısmında gerilme hissedin.", "30 saniye, 3 tekrar, günde 2–3 kez"),
 "soleus": ("Dizi bükük baldır germe", "Aynı pozisyonda arkadaki ayağınızı biraz öne alın ve dizinizi bükün. Topuğunuz yerden kalkmadan kalçanızı aşağı indirin; gerilmeyi baldırın alt kısmında, aşil tendonuna yakın hissedeceksiniz.", "30 saniye, 3 tekrar, günde 2–3 kez"),
 "rathleff": ("Havlulu topuk kaldırma", "Bir basamağa çıkın, ağrılı ayağınızın parmaklarının altına rulo yapılmış bir havlu koyun; topuğunuz basamaktan taşsın. Tezgâh ya da duvardan destek alarak tek ayak üzerinde 3 saniyede yükselin, 2 saniye bekleyin, 3 saniyede inin. Kolaylaştıkça sırt çantasıyla yük ekleyin.", "8–12 tekrar, 3 set, iki günde bir"),
 "roll": ("Şişe ile ayak altı masajı", "Oturun, ağrılı ayağınızın altına bir tenis topu ya da su şişesi koyun. Ayağınızı topuktan parmak uçlarına doğru ileri geri yuvarlayın. Ağrılı dönemde şişeyi dondurucuda soğutmak da rahatlatabilir.", "1–2 dakika, günde 2–3 kez"),
})

TOPUK_FAQ = [
 ("Topuk dikeni kendiliğinden geçer mi?", "Çoğu zaman evet, ama sabır ister. Uygun tedaviyle hastaların yaklaşık %80'i 12 ay içinde iyileşir. Germe, güçlendirme ve yük yönetimi bu süreci kısaltır."),
 ("Dikeni ameliyatla aldırmak gerekir mi?", "Çok nadiren. Röntgendeki kemik çıkıntısı ağrısı olmayan kişilerde de sık görülür ve ağrının asıl kaynağı değildir. Ameliyat, uzun süre tüm tedavilere yanıt vermeyen az sayıda hastada düşünülür."),
 ("Kortizon iğnesi yaptırmalı mıyım?", "Kortizon iğnesi kısa süreli rahatlama sağlayabilir, ancak etkisi geçicidir ve birden fazla enjeksiyon yapılanların yaklaşık %2,4'ünde fasya yırtılabilir. Önce egzersiz, bantlama, gece ateli ve tabanlık gibi yöntemler denenmelidir."),
 ("Sabahları neden daha çok ağrıyor?", "Gece boyunca ayak aşağı doğru uzanmış durduğu için fasya ve baldır kasları kısalmış konumda dinlenir; ilk adımlarda bu dokular birden gerilir. Yataktan kalkmadan önce yapılan germeler ve gece ateli bu ağrıyı azaltır."),
 ("Tabanlık işe yarar mı?", "Tabanlıklar tek başına değil, germe ve güçlendirme egzersizleriyle birlikte kullanıldığında yararlıdır. Kılavuz hazır ya da kişiye özel tabanlıkları diğer tedavilerle birlikte kullanılmak üzere öneriyor."),
 ("Spor yapmayı bırakmalı mıyım?", "Tamamen bırakmanız gerekmez. Ağrıyı belirgin artıran koşu ve zıplama gibi yükleri geçici olarak azaltın, bisiklet ve yüzmeyle formunuzu koruyun. Ağrı azaldıkça yükü kademeli artırın."),
]

TOPUK_SRC = [
 "Buchbinder R. Clinical practice. Plantar fasciitis. N Engl J Med. 2004;350(21):2159-2166.",
 "DiGiovanni BF, Nawoczenski DA, Lintal ME, et al. Tissue-specific plantar fascia-stretching exercise enhances outcomes in patients with chronic heel pain: a prospective, randomized study. J Bone Joint Surg Am. 2003;85(7):1270-1277.",
 "Koc TA Jr, Bise CG, Neville C, Carreira D, Martin RL, McDonough CM. " + ext("https://www.jospt.org/doi/10.2519/jospt.2023.0303", "Heel pain – plantar fasciitis: revision 2023. Clinical practice guidelines linked to the International Classification of Functioning, Disability and Health") + ". J Orthop Sports Phys Ther. 2023;53(12):CPG1-CPG39.",
 "Lemont H, Ammirati KM, Usen N. Plantar fasciitis: a degenerative process (fasciosis) without inflammation. J Am Podiatr Med Assoc. 2003;93(3):234-237.",
 "Physiopedia. " + ext("https://www.physio-pedia.com/Plantar_Fasciitis", "Plantar Fasciitis") + ".",
 "Rathleff MS, Mølgaard CM, Fredberg U, et al. " + ext("https://onlinelibrary.wiley.com/doi/10.1111/sms.12313", "High-load strength training improves outcome in patients with plantar fasciitis: a randomized controlled trial with 12-month follow-up") + ". Scand J Med Sci Sports. 2015;25(3):e292-e300.",
 "Trojian T, Tucker AK. " + ext("https://www.aafp.org/pubs/afp/issues/2019/0615/p744.html", "Plantar fasciitis") + ". Am Fam Physician. 2019;99(12):744-750.",
]

TOPUK_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Topuk dikeni (plantar fasiit)</h1>
    <p class="lede">Sabah ilk adımlarda topuğa saplanan ağrıyla kendini gösterir. Halk arasında "topuk dikeni" dense de ağrının asıl kaynağı çoğu zaman kemik çıkıntısı değil, ayak tabanındaki bağ dokusunun (plantar fasya) zorlanmasıdır. İyi haber: hastaların büyük çoğunluğu ameliyatsız iyileşir.</p>
    <p class="meta">Son güncelleme: {UPDATED}</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>10'da 1</b><span>Hayatının bir döneminde topuk dikeni yaşayan kişi</span></div>
        <div class="stat"><b>%80</b><span>Uygun tedaviyle 12 ay içinde iyileşenler</span></div>
        <div class="stat"><b>40–60</b><span>En sık görüldüğü yaş aralığı</span></div>
        <div class="stat"><b>3,7 kat</b><span>Beden kitle indeksi 27'nin üzerinde olanlarda artan risk</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Ayak tabanında topuktan parmaklara uzanan kalın bağ dokusuna plantar fasya denir; ayak kemerini destekler ve her adımda gerilir. Tekrarlayan aşırı yüklenmeyle fasyanın topuğa yapıştığı yerde yıpranma ve ağrı gelişir. Adındaki "-it" iltihabı çağrıştırsa da sorun çoğu zaman iltihaptan çok dokunun yıpranmasıdır.</p>
        <p class="soft">Tanı çoğunlukla muayeneyle konur: ağrı topuğun iç ve alt kısmındadır, sabah ilk adımlarda ve uzun oturduktan sonra kalkınca en belirgindir, uzun süre ayakta kalınca artar.</p>
      </div>
      <div>
        <h2>Risk etkenleri</h2>
        <ul class="dots">
          <li>Fazla kilo (beden kitle indeksi 27'nin üzerinde)</li>
          <li>İş gününün çoğunu ayakta geçirmek</li>
          <li>Baldır kaslarının gerginliği, ayak bileğinin yukarı doğru hareketinin kısıtlı olması</li>
          <li>Koşu gibi tekrarlayan yüklenmeler</li>
          <li>40–60 yaş arası olmak</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Röntgendeki "diken" ağrının nedeni mi?</h2>
      <p class="soft">Topukta röntgende görülen kemik çıkıntısı (kalkaneal spur), hiç ağrısı olmayan kişilerde de sık rastlanan bir bulgudur ve tek başına ağrıyı açıklamaz. Ağrı, çıkıntının kendisinden çok fasyanın zorlanmasından kaynaklanır.</p>
      <div class="callout">
        <p>Bu yüzden tedavinin hedefi dikeni "eritmek" ya da ameliyatla almak değil, fasyanın yükünü azaltmak ve dokuyu güçlendirmektir. Ağrı geçtikten sonra da çıkıntı genellikle röntgende yerinde durur; yani iyileşmek için dikenin kaybolması gerekmez.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <p class="soft">Amerikan Fizyoterapi Derneği'nin 2023 kılavuzu, ameliyatsız tedavinin temeline germe, manuel terapi ve kısa vadeli destekleri koyuyor.</p>
      <ul class="tx">
        <li><b>Germe</b><span>Plantar fasya ve baldır germeleri kısa ve uzun vadede ağrıyı azaltır, işlevi iyileştirir. Kılavuzdaki en güçlü önerilerdendir.</span></li>
        <li><b>Güçlendirme</b><span>Ayak ve ayak bileği kaslarını giderek artan yükle çalıştıran egzersizler önerilir. Havlulu topuk kaldırma egzersizi bir çalışmada 3. ayda germeye göre daha iyi sonuç verdi; 12. ayda iki grup benzerdi.</span></li>
        <li><b>Manuel terapi</b><span>Ayak ve bacaktaki eklem ve yumuşak dokulara yönelik manuel terapi, hareket kısıtlılığını ve ağrıyı azaltır.</span></li>
        <li><b>Kuru iğneleme</b><span>Baldır ve ayak tabanı kaslarındaki tetik noktalara uygulanan kuru iğneleme, kısa ve uzun vadede ağrıyı azaltmak için önerilir.</span></li>
        <li><b>Bantlama ve gece ateli</b><span>Esnek ya da sert bantlama kısa vadede ağrıyı ve işlevi iyileştirir. Sabah ilk adımlarda ağrısı olanlarda 1–3 ay gece ateli önerilir.</span></li>
        <li><b>Tabanlık ve ayakkabı</b><span>Hazır ya da kişiye özel tabanlıklar tek başına değil, diğer tedavilerle birlikte kullanıldığında yararlıdır. Topuğu destekleyen, yastıklı ayakkabılar tercih edilmelidir.</span></li>
        <li><b>İnatçı ağrıda</b><span>Aylarca süren ağrıda şok dalga tedavisi (ESWT) bir seçenektir. Kortizon iğnesi kısa süreli rahatlama sağlayabilir ama birden fazla enjeksiyon yapılanların yaklaşık %2,4'ünde fasya yırtılabilir. Ameliyat, uzun süre tüm tedavilere yanıt vermeyen az sayıda hastada düşünülür.</span></li>
      </ul>
      <div class="callout">
        <p><strong>Kılavuzda önerilmeyen:</strong> Germe egzersizlerine terapötik ultrason eklemek ek fayda sağlamıyor.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Topuk dikeni için altı egzersiz</h2>
      <p class="soft">Egzersizler sırasında hafif bir rahatsızlık olabilir; ağrı ertesi sabah belirgin şekilde artmıyorsa devam etmek güvenlidir. Germe hareketlerini sabah ilk adımlardan önce ve uzun oturduktan sonra yapmak en çok faydayı sağlar.</p>
      {ex_grid(["pfst", "towelst", "calf", "soleus", "rathleff", "roll"])}
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Günlük hayatta topuğunuz için</h2>
        <p class="soft">Amaç topuğu tamamen dinlendirmek değil, yükü ağrının izin verdiği ölçüde ayarlamak ve dokuyu yeniden güçlendirmektir.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Yataktan kalkmadan önce ayak parmaklarınızı geriye çekin, ayak bileğinizle daireler çizin.</li>
        <li>Evde de çıplak ayakla ya da ince tabanlı terlikle sert zeminde yürümeyin; topuğu destekleyen, yastıklı ayakkabı giyin.</li>
        <li>Uzun süre ayakta kalıyorsanız ara verin, mümkünse yumuşak bir paspas üzerinde durun.</li>
        <li>Ağrı azalana kadar koşu ve zıplama gibi yükleri azaltın; bisiklet ve yüzme iyi alternatiflerdir.</li>
        <li>Fazla kilolarınızı vermek topuğa binen yükü azaltır.</li>
      </ul>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Topuk dikeni için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("fx-mXmboEM4", "Topuk dikeni germe videosunu oynat", "Single BEST Stretch for Plantar Fasciitis, Bone Spur &amp; Heel Pain")}
          <h3>Topuk dikeni için en etkili germe</h3>
          <p>Ayak tabanındaki fasyayı hedefleyen germe hareketi.</p>
        </div>
        <div class="vid">
          {vbox("75JvDlvGF_s", "Sabah rutini videosunu oynat", "The 5 Things Anyone With Plantar Fasciitis Should Do Every Morning")}
          <h3>Her sabah yapılacak beş şey</h3>
          <p>Sabah ilk adım ağrısını azaltmaya yönelik kısa bir rutin.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(TOPUK_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Topuk ağrısı çoğunlukla zararsızdır. Şu durumlarda ise beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Ayak tabanında uyuşma, karıncalanma ya da yanma (sinir sıkışması olabilir)</li>
        <li>Topuğu iki yandan sıkınca artan ağrı, özellikle yürüyüş ya da koşu yükünüzü yeni artırdıysanız (stres kırığı olabilir)</li>
        <li>Ayak tabanında aniden kopma hissi, morarma ve basamama</li>
        <li>Topukta kızarıklık, şişlik, sıcaklık ya da ateş</li>
        <li>Dinlenmekle geçmeyen gece ağrısı ya da nedensiz kilo kaybı</li>
        <li>İki topukta birden ağrıyla birlikte sabahları uzun süren bel ya da eklem tutukluğu (romatizmal bir hastalık olabilir)</li>
      </ul>
      {CTA_CARD("Topuk ağrınız", "topuk dikeni")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(TOPUK_SRC)}
    </div>
  </section>
</main>'''

page("topuk-dikeni.html", "Topuk Dikeni",
     "Topuk dikeni (plantar fasiit) nedir, röntgendeki diken ağrının nedeni mi, kendiliğinden geçer mi? Evde altı egzersiz, tabanlık ve ayakkabı önerileri, videolar ve uyarı işaretleri.",
     "topuk-dikeni.html", NECK_CSS, TOPUK_BODY, YT_JS,
     seo_title="Topuk Dikeni (Plantar Fasiit): Egzersizler ve Tedavi | İhsan Eren",
     condition="Topuk dikeni (plantar fasiit)", about=cond("Topuk dikeni (plantar fasiit)"),
     faq_items=pick(TOPUK_FAQ, 0, 1, 2, 3))

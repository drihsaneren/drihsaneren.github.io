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
 "pfst": ("Parmakları geriye çekerek germe", "Oturun, ağrılı ayağınızı diğer dizinizin üzerine alın. Bir elinizle ayak parmaklarınızı bacağınıza doğru geriye çekin; ayak tabanınızda, topuğun önünde gerilme hissedin. Sabah ilk adımlardan önce ve uzun oturduktan sonra yapmak özellikle faydalıdır.", "10 saniye, 10 tekrar, günde 3 kez"),
 "towelst": ("Havluyla germe", "Yere ya da yatağa bacaklarınız düz olacak şekilde oturun. Bir havluyu ayağınızın ön kısmına dolayıp uçlarından tutun. Dizinizi düz tutarak havluyu kendinize doğru çekin; baldırınızda ve ayak tabanınızda gerilme hissedin.", "30 saniye, 3 tekrar, günde 2–3 kez"),
 "calf": ("Duvarda baldır germe", "Ellerinizi duvara dayayın, ağrılı bacağınızı arkaya alın. Arkadaki dizinizi düz, topuğunuzu yerde tutarak kalçanızı duvara doğru ilerletin; baldırınızın üst kısmında gerilme hissedin.", "30 saniye, 3 tekrar, günde 2–3 kez"),
 "soleus": ("Dizi bükük baldır germe", "Aynı pozisyonda arkadaki ayağınızı biraz öne alın ve dizinizi bükün. Topuğunuz yerden kalkmadan kalçanızı aşağı indirin; gerilmeyi baldırın alt kısmında, Aşil tendonuna yakın hissedeceksiniz.", "30 saniye, 3 tekrar, günde 2–3 kez"),
 "rathleff": ("Havlulu topuk kaldırma", "En alt basamağa çıkın, ağrılı ayağınızın parmaklarının altına rulo yapılmış bir havlu koyun. Tırabzan ya da duvardan mutlaka tutunarak tek ayak üzerinde 3 saniyede yükselin, 2 saniye bekleyin, 3 saniyede inin; inerken topuğunuzu basamak hizasına kadar indirin. Tek ayakla zorlanıyorsanız iki ayakla başlayın. Kolaylaştıkça sırt çantasıyla yük ekleyin.", "8–12 tekrar, 3 set, iki günde bir"),
 "roll": ("Şişe ile ayak altı masajı", "Oturun, ağrılı ayağınızın altına bir tenis topu ya da su şişesi koyun. Ayağınızı topuktan parmak uçlarına doğru ileri geri yuvarlayın. Ağrılı dönemde şişeyi dondurucuda soğutup ince bir beze sararak kullanmak rahatlatabilir; ayağınızda his kaybı ya da diyabetiniz varsa soğuk uygulamayın.", "1–2 dakika, günde 2–3 kez"),
})

TOPUK_FAQ = [
 ("Topuk dikeni kendiliğinden geçer mi?", "Çoğu zaman düzelir, ama sabır ister. Ameliyatsız tedaviyle hastaların yaklaşık %80'inde 12 ay içinde düzelme görülüyor. Ancak Danimarka'da bir uzman kliniğinde ultrasonla tanı konmuş 174 hastanın uzun süre izlendiği bir çalışmada, en ufak ağrısı kalan herkes hasta sayıldığında, şikâyetlerin sürme olasılığı belirtilerin başlangıcından itibaren 5. yılda %50, 10. yılda %46 idi. Yani ağrı çoğu kişide bir yıl içinde azalır, ama tamamen geçmesi bazı kişilerde yıllar alabilir. Germe, bantlama ve yük yönetimi bu süreçte temel tedavidir."),
 ("Röntgen ya da MR gerekir mi?", "Çoğu zaman gerekmez; tanı öykü ve muayeneyle konur. ABD fizyoterapi kılavuzuna göre görüntüleme genellikle ameliyatsız tedavi yetersiz kaldığında düşünülür; ilk tercih ayakta çekilen röntgendir, gerekirse ultrason ya da MR istenir. Ultrasonda fasyanın 4 milimetreden kalın ve koyu görünmesi plantar fasiiti düşündürür."),
 ("Dikeni ameliyatla aldırmak gerekir mi?", "Çok nadiren. Röntgendeki kemik çıkıntısı ağrısı olmayan kişilerde de sık görülür ve ağrının asıl kaynağı değildir. Ameliyat, uzun süre tüm tedavilere yanıt vermeyen az sayıda hastada düşünülür."),
 ("Kortizon iğnesi yaptırmalı mıyım?", "Kortizon iğnesi kısa süreli rahatlama sağlayabilir, ancak etkisi geçicidir ve birden fazla enjeksiyon yapılanların yaklaşık %2,4'ünde fasya yırtılabilir. Önce egzersiz, bantlama, gece ateli ve tabanlık gibi yöntemler denenmelidir."),
 ("Sabahları neden daha çok ağrıyor?", "Gece boyunca ayak aşağı doğru uzanmış durduğu için fasya ve baldır kaslarının kısalmış konumda dinlendiği, ilk adımlarda bu dokuların birden gerildiği düşünülüyor. Yataktan kalkmadan önce yapılan germeler bu ağrıyı azaltabilir; sabah ağrısı sürekli olanlarda gece ateli de denenebilir."),
 ("Tabanlık işe yarar mı?", "Tabanlıklar tek başına değil, germe ve güçlendirme egzersizleriyle birlikte kısa vadede yararlı olabilir. ABD fizyoterapi kılavuzu bunu zayıf kanıtla, kullanılabilir düzeyinde belirtiyor; bir derlemede yarar yaklaşık 12 haftaya kadar görüldü, uzun vadede belirgin değildi. BJSM rehberi ise ancak yaklaşık 12 haftada düzelme yetersizse kişiye özel tabanlık ekliyor."),
 ("Spor yapmayı bırakmalı mıyım?", "Tamamen bırakmanız gerekmez. Ağrıyı belirgin artıran koşu ve zıplama gibi yükleri geçici olarak azaltın, bisiklet ve yüzmeyle formunuzu koruyun. Ağrı azaldıkça yükü kademeli artırın."),
]

TOPUK_SRC = [
 "Hansen L, Krogh TP, Ellingsen T, Bolvig L, Fredberg U. " + ext("https://portal.findresearcher.sdu.dk/da/publications/long-term-prognosis-of-plantar-fasciitis-a-5-to-15-year-follow-up/", "Long-term prognosis of plantar fasciitis: a 5- to 15-year follow-up study of 174 patients with ultrasound examination") + ". Orthop J Sports Med. 2018;6(3):2325967118757983.",
 "Morrissey D, Cotchett M, Said J'Bari A, et al. " + ext("https://vbn.aau.dk/files/449173957/1106.full.pdf", "Management of plantar heel pain: a best practice guide informed by a systematic review, expert clinical reasoning and patient values") + ". Br J Sports Med. 2021;55(19):1106-1118.",
 "Buchbinder R. Clinical practice. Plantar fasciitis. N Engl J Med. 2004;350(21):2159-2166.",
 "DiGiovanni BF, Nawoczenski DA, Lintal ME, et al. Tissue-specific plantar fascia-stretching exercise enhances outcomes in patients with chronic heel pain: a prospective, randomized study. J Bone Joint Surg Am. 2003;85(7):1270-1277.",
 "Koc TA Jr, Bise CG, Neville C, Carreira D, Martin RL, McDonough CM. " + ext("https://www.jospt.org/doi/10.2519/jospt.2023.0303", "Heel pain – plantar fasciitis: revision 2023. Clinical practice guidelines linked to the International Classification of Functioning, Disability and Health") + ". J Orthop Sports Phys Ther. 2023;53(12):CPG1-CPG39. Özet: " + ext("https://physicaltherapyfirst.com/blog/heel-pain-plantar-fasciitis-revision-2023/", "Physical Therapy First") + ".",
 "Lemont H, Ammirati KM, Usen N. Plantar fasciitis: a degenerative process (fasciosis) without inflammation. J Am Podiatr Med Assoc. 2003;93(3):234-237.",
 "Physiopedia. " + ext("https://www.physio-pedia.com/Plantar_Fasciitis", "Plantar Fasciitis") + ".",
 "Rathleff MS, Mølgaard CM, Fredberg U, et al. " + ext("https://onlinelibrary.wiley.com/doi/10.1111/sms.12313", "High-load strength training improves outcome in patients with plantar fasciitis: a randomized controlled trial with 12-month follow-up") + ". Scand J Med Sci Sports. 2015;25(3):e292-e300.",
 "Trojian T, Tucker AK. " + ext("https://www.aafp.org/pubs/afp/issues/2019/0615/p744.html", "Plantar fasciitis") + ". Am Fam Physician. 2019;99(12):744-750.",
]

TOPUK_TL = [
 ("2003", "Bir inceleme, plantar fasiitin iltihaptan çok dokunun yıpranmasıyla seyreden bir süreç olduğunu öne sürdü ve \"fasyoz\" adını kullandı."),
 ("2003", "Uzun süren topuk ağrısında fasyaya özgü germe egzersizinin sonuçları iyileştirdiği bildirildi; bu germe bugün de tedavinin temel parçalarından biri."),
 ("2015", "Ağır yüklü güçlendirmeyi (havlulu topuk kaldırma) germeyle karşılaştıran bir çalışmada güçlendirme grubu 3. ayda daha iyi sonuç aldı; 12. ayda iki grup benzerdi."),
 ("2018", "Danimarka'da bir uzman kliniğinde ultrasonla tanı konmuş 174 hasta ortalama yaklaşık 9 yıl izlendi: en ufak ağrısı kalan herkes hasta sayıldığında şikâyetlerin sürme olasılığı belirtilerin başlangıcından itibaren 5. yılda %50, 10. yılda %46'ydı. Başlangıçtaki fasya kalınlığı ve topuk dikeni varlığı uzun vadeli seyri etkilemedi."),
 ("2021", "51 randomize çalışma, 14 uzman ve 40 hastanın görüşüyle hazırlanan bir en iyi uygulama rehberi (BJSM) yayımlandı: temel tedavi germe, bantlama ve kişiye özel eğitim; bu yaklaşım yaklaşık 4–6 haftada yeterli olmazsa şok dalga, yaklaşık 12 haftada hâlâ yetersizse kişiye özel tabanlık ekleniyor."),
 ("2023", "Amerikan Fizyoterapi Derneği'ne (APTA) bağlı Ortopedik Fizyoterapi Akademisi'nin kılavuzu güncellendi (JOSPT): manuel terapi, germe, bantlama ve gece ateli en güçlü (A) düzeyde önerildi; germe egzersizlerine ultrason tedavisinin eklenmemesi de A düzeyinde önerildi."),
]

TOPUK_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Topuk dikeni (plantar fasiit)</h1>
    <p class="lede">Sabah ilk adımlarda topuğa saplanan ağrıyla kendini gösterir. Halk arasında "topuk dikeni" dense de ağrının asıl kaynağı çoğu zaman kemik çıkıntısı değil, ayak tabanındaki bağ dokusunun (plantar fasya) zorlanmasıdır. Hastaların büyük çoğunluğu ameliyatsız düzelir; ancak iyileşme aylar, bazı kişilerde yıllar sürebilir.</p>
    <p class="meta">Son güncelleme: 31 Ekim 2026</p>
  </div>
</header>
<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>10'da 1</b><span>Hayatının bir döneminde plantar fasiit (topuk ağrısı) yaşayan kişi</span></div>
        <div class="stat"><b>%80</b><span>Ameliyatsız tedaviyle 12 ay içinde düzelme görülenler</span></div>
        <div class="stat"><b>40–60</b><span>En sık görüldüğü yaş aralığı</span></div>
        <div class="stat"><b>3,7</b><span>Sporcu olmayanlarda beden kitle indeksi 27'nin üzerindeyse plantar fasiit olasılığı belirgin şekilde yüksek (olasılık oranı)</span></div>
      </div>
      {g_toc([("nedir", "Nedir?"), ("tani", "Nasıl tanınır?"), ("seyir", "Ne kadar sürer?"), ("diken", "Röntgendeki diken"), ("tarihce", "Geçmişten bugüne"), ("tedavi", "Tedavi seçenekleri"), ("egzersizler", "Egzersizler"), ("gunluk", "Günlük hayatta"), ("videolar", "Videolar"), ("sss", "Sık sorulan sorular"), ("uyari", "Uyarı işaretleri")])}
    </div>
  </section>
  <section id="nedir">
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Ayak tabanında topuktan parmaklara uzanan kalın bağ dokusuna plantar fasya denir; ayak kemerini destekler ve her adımda gerilir. Tekrarlayan aşırı yüklenmeyle fasyanın topuğa yapıştığı yerde yıpranma ve ağrı gelişir. Adındaki "-it" iltihabı çağrıştırsa da sorun çoğu zaman iltihaptan çok dokunun yıpranmasıdır.</p>
        <p class="soft">Ağrı topuğun iç ve alt kısmındadır, sabah ilk adımlarda ve uzun oturduktan sonra kalkınca en belirgindir, uzun süre ayakta kalınca artar.</p>
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
  <section id="tani">
    <div class="wrap">
      <h2>Nasıl tanınır?</h2>
      <p class="soft">Tanı çoğunlukla öykü ve muayeneyle konur; görüntüleme tanıyı koymaktan çok başka nedenleri dışlamaya yarar.</p>
      <div class="kinds">
        <div class="kind"><h3>Tipik bulgular</h3><p>Hareketsiz kaldıktan sonraki ilk adımlarda en belirgin olan topuğun iç-alt kısmında ağrı, fasyanın topuğa yapıştığı yerde bastırınca hassasiyet, ayak başparmağını yukarı kaldırınca ağrının ortaya çıkması (windlass testi) ve ayak bileğinin yukarı hareketinde kısıtlılık ABD fizyoterapi kılavuzunun saydığı bulgular arasında.</p></div>
        <div class="kind"><h3>Görüntüleme ne zaman?</h3><p>Genellikle ameliyatsız tedavi yetersiz kaldığında düşünülür. İlk tercih ayakta çekilen röntgendir; gerekirse ultrason ya da MR istenir. Ultrasonda fasyanın 4 milimetreden kalın ve koyu görünmesi plantar fasiiti düşündürür.</p></div>
        <div class="kind"><h3>Başka ne olabilir?</h3><p>Ayak tabanında uyuşma ya da yanma varsa sinir sıkışması (tarsal tünel), topuğu iki yandan sıkınca ağrı varsa stres kırığı akla gelir. Belirtiler uymuyor ya da geçmiyorsa romatizmal hastalıklar, topuktaki yağ yastığının incelmesi ve fasyada nodül gibi nedenler de değerlendirilir.</p><a href="#uyari">Uyarı işaretleri →</a></div>
      </div>
    </div>
  </section>
  <section id="seyir">
    <div class="wrap">
      <h2>Ne kadar sürer?</h2>
      <p class="soft">Birinci basamak hekimleri için yazılmış bir derlemeye göre hastaların yaklaşık %80'inde ameliyatsız tedaviyle 12 ay içinde düzelme görülüyor. Ancak Danimarka'da bir uzman kliniğinde ultrasonla tanı konmuş 174 hastanın ortalama yaklaşık 9 yıl izlendiği çalışmada şikâyetlerin sürme olasılığı belirtilerin başlangıcından itibaren 1. yılda yaklaşık %80, 5. yılda %50, 10. yılda %46 idi. Kadınlarda ve iki topukta birden ağrısı olanlarda seyir daha kötüydü.</p>
      <div class="callout">
        <p>Bu iki rakam farklı şeyleri ölçüyor: derlemedeki %80 ağrıda düzelmeyi anlatıyor; Danimarka çalışmasında ise en ufak ağrısı kalan herkes hâlâ hasta sayıldı. Katılanlar kliniğe başvurduklarında ortalama 10 aya yakın süredir şikâyetliydi ve yazarlar bu grubun daha ağır hastaları temsil ettiğini belirtiyor. Yani ağrı çoğu kişide bir yıl içinde azalır, ama tamamen geçmesi bazı kişilerde yıllar alabilir. Gerçekçi ama umutlu bir beklenti ve düzenli egzersiz bu süreci yönetmenin temelidir.</p>
      </div>
    </div>
  </section>
  <section id="diken">
    <div class="wrap">
      <h2>Röntgendeki "diken" ağrının nedeni mi?</h2>
      <p class="soft">Topukta röntgende görülen kemik çıkıntısı (kalkaneal spur), hiç ağrısı olmayan kişilerde de sık rastlanan bir bulgudur ve tek başına ağrıyı açıklamaz. Ağrı, çıkıntının kendisinden çok fasyanın zorlanmasından kaynaklanır.</p>
      <div class="callout">
        <p>Bu yüzden tedavinin hedefi dikeni "eritmek" ya da ameliyatla almak değil, fasyanın yükünü azaltmak ve dokuyu güçlendirmektir. Ağrı geçtikten sonra da çıkıntı genellikle röntgende yerinde durur; yani iyileşmek için dikenin kaybolması gerekmez. 174 hastanın uzun süre izlendiği çalışmada da topuk dikeni olup olmaması uzun vadeli seyri etkilemedi.</p>
      </div>
    </div>
  </section>
  <section id="tarihce">
    <div class="wrap">
      <p class="eyebrow">Geçmişten bugüne</p>
      <h2>Topuk dikeni tedavisinin kısa tarihi</h2>
      <p class="soft">Uzun süre topuk ağrısının nedeni olarak kemik çıkıntısı ve iltihap görüldü. Son yirmi yılın araştırmaları dikkati fasyanın yüklenmesine, germe ve güçlendirmeye ve hastalığın uzun sürebilen seyrine çevirdi.</p>
      {g_tl(TOPUK_TL)}
    </div>
  </section>
  <section id="tedavi">
    <div class="wrap">
      <h2>Tedavi</h2>
      <p class="soft">Amerikan Fizyoterapi Derneği'ne (APTA) bağlı Ortopedik Fizyoterapi Akademisi'nin 2023 kılavuzunun en güçlü (A) düzeyde önerdiği tedaviler germe, manuel terapi, bantlama ve sabah ilk adım ağrısı sürekli olanlarda gece atelidir.</p>
      <ul class="tx">
        <li><b>Germe</b><span>Plantar fasya ve baldır germeleri kısa ve uzun vadede ağrıyı azaltmak ve işlevi iyileştirmek için en güçlü (A) düzeyde önerilir.</span></li>
        <li><b>Güçlendirme</b><span>Ayak ve ayak bileği kaslarını giderek artan yükle çalıştıran egzersizler önerilir. Havlulu topuk kaldırma egzersizi bir çalışmada 3. ayda germeye göre daha iyi sonuç verdi; 12. ayda iki grup benzerdi.</span></li>
        <li><b>Manuel terapi</b><span>Ayak ve bacaktaki eklem ve yumuşak dokulara yönelik manuel terapi, hareket kısıtlılığını ve ağrıyı azaltmak için önerilir (A).</span></li>
        <li><b>Kuru iğneleme</b><span>Baldır ve ayak tabanı kaslarındaki tetik noktalara kuru iğneleme ABD fizyoterapi kılavuzunda B düzeyinde öneriliyor. Türkiye'de yalnızca yetkili hekimler uygulayabilir.</span></li>
        <li><b>Bantlama ve gece ateli</b><span>Esnek ya da sert bantlama, diğer tedavilerle birlikte kısa vadede ağrıyı ve işlevi iyileştirmek için önerilir (A); çalışmalarda yarar 1–6 hafta boyunca ölçüldü. Sabah ilk adımlarda sürekli ağrısı olanlarda 1–3 ay gece ateli önerilir (A); ancak başka kaynaklarda gece atelinin yararı konusunda kanıt çelişkili bulunuyor.</span></li>
        <li><b>Tabanlık ve ayakkabı</b><span>Hazır ya da kişiye özel tabanlıklar tek başına değil, diğer tedavilerle birlikte kısa vadede yararlı olabilir (C). Topuğu destekleyen, yastıklı ayakkabılar tercih edilmelidir.</span></li>
        <li><b>İnatçı ağrıda</b><span>Temel tedaviye rağmen düzelmeyen ağrıda şok dalga tedavisi (ESWT) bir seçenektir. Kortizon iğnesi kısa süreli rahatlama sağlayabilir: tuzlu su (plasebo) iğnesiyle karşılaştıran bir çalışmada ağrı 4. haftada daha fazla azaldı, ancak uzun süreli yararı gösterilmedi. Birden fazla enjeksiyon yapılanların yaklaşık %2,4'ünde fasya yırtılabilir. Ameliyat, uzun süre tüm tedavilere yanıt vermeyen az sayıda hastada düşünülür.</span></li>
      </ul>
      <h3 class="g-h3">Tedavi seçenekleri: kaynaklar ne diyor?</h3>
      <p class="soft">Amerikan Fizyoterapi Derneği'ne (APTA) bağlı Ortopedik Fizyoterapi Akademisi'nin kılavuzu (JOSPT, 2023) ile 51 randomize çalışma, uzman görüşleri ve hasta tercihleriyle hazırlanan en iyi uygulama rehberinin (BJSM, 2021) önerileri yan yana. Parantez içindeki harfler JOSPT kılavuzundaki öneri düzeyidir (A güçlü, B orta, C zayıf, D çelişkili, E kuramsal kanıt). BJSM rehberi tedaviyi basamaklar hâlinde sıralıyor; tedavi kişiye göre seçilir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Germe</h3><dl><dt>JOSPT</dt><dd>Fasya ve baldır germeleri kısa ve uzun vadede (A).</dd><dt>BJSM rehberi</dt><dd>Fasya germe, herkese uygulanan temel tedavi.</dd></dl></div>
        <div class="kind"><h3>Bantlama</h3><dl><dt>JOSPT</dt><dd>Sert ya da esnek bant, diğer tedavilerle birlikte kısa vadede (A).</dd><dt>BJSM rehberi</dt><dd>Ayak kemerini destekleyen (low-dye) bantlama, temel tedavi.</dd></dl></div>
        <div class="kind"><h3>Eğitim ve ayakkabı</h3><dl><dt>BJSM rehberi</dt><dd>Kişiye özel eğitim temel tedavi: yük yönetimi, ağrının anlatılması, ayakkabı önerisi ve eşlik eden diyabet ya da fazla kilo. Rahat ve destekleyici, topuğu ön ayaktan biraz yüksek ayakkabı; düzelene kadar çıplak ayakla ve düz, desteksiz ayakkabıyla yürümekten kaçınmak.</dd><dt>JOSPT</dt><dd>Kas kütlesini korumaya ya da artırmaya yönelik egzersiz konusunda eğitim; gerekirse beslenme için yönlendirme (E, zayıf ya da kuramsal kanıt).</dd></dl></div>
        <div class="kind"><h3>Tabanlık</h3><dl><dt>JOSPT</dt><dd>Kısa vadeli ağrı için tek başına kullanılmamalı; diğer tedavilerle birlikte kullanılabilir.</dd><dt>BJSM rehberi</dt><dd>Temel tedavi değil; yaklaşık 12 haftada düzelme yetersizse kişiye özel tabanlık. Herkese aynı tabanlık verilmemeli.</dd></dl></div>
        <div class="kind"><h3>Gece ateli</h3><dl><dt>JOSPT</dt><dd>Sabah ilk adımda sürekli ağrısı olanlarda 1–3 ay (A).</dd><dt>BJSM rehberi</dt><dd>Öneri yapılmıyor.</dd></dl></div>
        <div class="kind"><h3>Şok dalga</h3><dl><dt>BJSM rehberi</dt><dd>Temel tedavi yaklaşık 4–6 haftada yeterli olmazsa ikinci basamak.</dd><dt>JOSPT</dt><dd>Fizyoterapi kapsamı dışında sayıldığı için öneri yapılmadı.</dd></dl></div>
        <div class="kind"><h3>Manuel terapi, kuru iğneleme ve cihazlar</h3><dl><dt>JOSPT</dt><dd>Manuel terapi (A); kuru iğneleme (B); düşük düzeyli lazer kısa vadeli ağrı için; germeye ultrason tedavisi eklenmemeli (A); elektroterapi yerine manuel terapi, germe ve tabanlık tercih edilebilir (D, çelişkili kanıt).</dd><dt>Not</dt><dd>Kuru iğnelemeyi Türkiye'de yalnızca yetkili hekimler uygulayabilir.</dd></dl></div>
        <div class="kind"><h3>Kortizon ve PRP iğnesi</h3><dl><dt>BJSM rehberi</dt><dd>Rehberin değerlendirdiği çalışmalarda etkinliği kanıtlanmamış. Temel tedavi, şok dalga ve tabanlık yetersiz kaldığında deneysel bir seçenek olarak, tercihen bir araştırma kapsamında ya da yapılandırılmış değerlendirmeyle düşünülebilir.</dd><dt>Not</dt><dd>PRP, kişinin kendi kanından hazırlanan plazmadır. Birden fazla kortizon iğnesi yapılanların yaklaşık %2,4'ünde fasya yırtılabilir (AAFP derlemesi).</dd></dl></div>
      </div>
      <div class="callout">
        <p><strong>Kılavuzda önerilmeyen:</strong> Germe egzersizlerine terapötik ultrason eklemek ek fayda sağlamıyor.</p>
      </div>
    </div>
  </section>
  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Topuk dikeni için altı egzersiz</h2>
      <p class="soft">Egzersizler sırasında hafif bir rahatsızlık olabilir; ağrı ertesi sabah belirgin şekilde artmıyorsa devam edebilirsiniz. Germe hareketlerini sabah ilk adımlardan önce ve uzun oturduktan sonra yapmak en çok faydayı sağlar.</p>
      {ex_grid(["pfst", "towelst", "calf", "soleus", "rathleff", "roll"])}
    </div>
  </section>
  <section id="gunluk">
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
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir. Kanal hakkında: <a href="https://www.startribune.com/meet-the-minnesota-physical-therapists-who-have-become-youtube-superstars/508806552" target="_blank" rel="noopener">Star Tribune, 19 Nisan 2019</a>.</p>
    </div>
  </section>
  <section id="sss">
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(TOPUK_FAQ)}
    </div>
  </section>
  <section id="uyari">
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Topuk ağrısı çoğunlukla zararsızdır. Şu durumlarda ise beklemeden başvurun.</p>
      <p class="soft"><strong>Aynı gün ya da acil servise:</strong></p>
      <ul class="dots redflags">
        <li>Topukta ateşle birlikte kızarıklık, şişlik ve sıcaklık (özellikle diyabetiniz varsa)</li>
        <li>Düşme ya da darbe sonrası topuğa basamama (kırık olabilir)</li>
        <li>Ayak tabanında aniden kopma hissi, morarma ve basamama (fasya yırtığı olabilir; özellikle kortizon iğnesinden sonra)</li>
        <li>Diyabetiniz varsa ayakta yara, renk değişikliği ya da soğukluk</li>
        <li>Bel ağrısıyla birlikte bacakta güç kaybı ya da idrar veya dışkı kontrolünde sorun</li>
      </ul>
      <p class="soft"><strong>Birkaç gün içinde bir hekime:</strong></p>
      <ul class="dots redflags">
        <li>Ayak tabanında uyuşma, karıncalanma ya da yanma (sinir sıkışması olabilir)</li>
        <li>Topuğu iki yandan sıkınca artan ağrı, özellikle yürüyüş ya da koşu yükünüzü yeni artırdıysanız (stres kırığı olabilir)</li>
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
     "Topuk dikeni (plantar fasiit) nedir, nasıl tanınır, ne kadar sürer, röntgendeki diken ağrının nedeni mi? ABD kılavuzu ve BJSM rehberinin karşılaştırması, kısa tarihçe, evde altı egzersiz ve uyarı işaretleri.",
     "topuk-dikeni.html", NECK_CSS, TOPUK_BODY, YT_JS,
     seo_title="Topuk Dikeni (Plantar Fasiit): Egzersizler ve Tedavi | İhsan Eren",
     condition="Topuk dikeni (plantar fasiit)", about=cond("Topuk dikeni (plantar fasiit)"),
     faq_items=pick(TOPUK_FAQ, 0, 1, 2, 3))

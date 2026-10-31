# -*- coding: utf-8 -*-
# Ayak bileği burkulması sayfası. osteo_part.py'den sonra exec edilir.

# Lastik bantla ayağı dışa çevirme (yukarıdan görünüm)
SV["evert"] = fig(
    '<path class="fig" d="M60 6 L60 66"/>'
    f'<g>{anim_t("0 60 70;-28 60 70;0 60 70", typ="rotate")}'
    '<rect x="52" y="64" width="16" height="42" rx="8" fill="#2A6F6B"/><circle cx="60" cy="104" r="3" fill="#C8963E"/></g>'
    f'<path class="band" d="M20 112 L60 104">{anim_d("M20 112 L60 104;M20 112 L80 100;M20 112 L60 104")}</path>'
    '<circle cx="18" cy="112" r="4" fill="#8FA8A2"/>'
    '<path d="M90 90 A30 30 0 0 0 96 70" fill="none" stroke="#C8963E" stroke-width="2.5" stroke-dasharray="3 4" stroke-linecap="round"/>',
    "Bantla ayağı dışa çevirme")

SV["apump2"] = SV["apump"]
SV["towelst2"] = SV["towelst"]
SV["heel4"] = SV["heel"]
SV["sls3"] = SV["sls"]
SV["tandem2"] = SV["tandem"]

EXT.update({
 "apump2": ("Ayak bileği pompası ve daireler", "Oturun ya da uzanın, bacağınız düz olsun. Ayak ucunuzu kendinize doğru çekin ve aşağı itin; sonra ayak bileğinizle iki yöne daireler çizin. İlk günlerden itibaren şişliği azaltmaya ve hareketi korumaya yardım eder.", "Her yöne 10 tekrar, günde 3–4 kez"),
 "towelst2": ("Havluyla baldır germe", "Bacaklarınız düz oturun, havluyu ayağınızın ön kısmına dolayıp uçlarından tutun. Dizinizi düz tutarak havluyu kendinize doğru çekin; baldırınızda gerilme hissedin. Ağrısız aralıkta kalın.", "30 saniye, 3 tekrar"),
 "evert": ("Bantla ayağı dışa çevirme", "Oturun, lastik bandı ayağınızın ön kısmına dolayıp diğer ucunu karşı tarafta sabitleyin. Topuğunuz yerde kalacak şekilde ayağınızı dışa doğru çevirin, yavaşça geri getirin. Ayak bileğinin dış yanındaki kasları güçlendirir.", "10–15 tekrar, 2–3 set"),
 "heel4": ("Topuk yükseltme", "Tezgâha tutunarak iki ayağınızla parmak uçlarınızda yükselin, yavaşça inin. Kolaylaştıkça yalnızca burkulan ayağınızla yapın.", "10–15 tekrar, 2–3 set"),
 "sls3": ("Tek ayak üzerinde durma", "Tezgâha yakın durup burkulan ayağınızın üzerinde dengede kalın. Kolaylaştıkça desteği bırakın, gözlerinizi kapatın ya da yastık gibi yumuşak bir zeminde deneyin. Yeni burkulmaları önlemenin temel egzersizidir.", "30 saniye, 3–5 tekrar"),
 "tandem2": ("Topuk-parmak yürüyüşü", "Tezgâh ya da duvar boyunca, öndeki ayağınızın topuğunu arkadaki ayağınızın parmak uçlarının hemen önüne koyarak düz bir çizgide yürüyün.", "10–15 adım, 2–3 tur"),
})

BILEK_FAQ = [
 ("Burkulan ayağıma basmalı mıyım?", "Evet, ağrının izin verdiği ölçüde. Amerikan Fizyoterapi Derneği'nin kılavuzu, yeni burkulmada ayak bileğini bant ya da bileklik gibi bir destekle korumayı ve ayağa kademeli olarak yük vermeyi öneriyor. Uzun süre hiç basmamak iyileşmeyi geciktirebilir."),
 ("Röntgen çektirmem gerekir mi?", "Çoğu burkulmada gerekmez. Ottawa kurallarına göre, yaralanmadan hemen sonra ve muayenede 4 adım atamıyorsanız ya da ayak bileğinin iç veya dış kemik çıkıntısının arka kenarında, alttaki 6 santimlik bölümde kemik üzerinde hassasiyet varsa röntgen gerekir. Bu kurallar kırıkların neredeyse tamamını yakalıyor."),
 ("Ne kadar sürede iyileşir?", "Burkulmanın derecesine göre değişir. ABD fizyoterapi kılavuzuna göre işe ya da spora dönüş, etkinliğe bağlı olarak 1 günden 3 haftayı biraz aşan sürelere kadar uzanabiliyor. Ancak ağrı geçse de toparlanma tamamlanmamış olabilir: çalışmalarda kişilerin %5–33'ünde ağrı 1 yıl ya da daha uzun sürdü ve yaklaşık 3 yılda tam iyileşme %50–85 arasında bildirildi. Bu yüzden denge ve güçlendirme egzersizlerine ağrı geçtikten sonra da devam etmek önemlidir."),
 ("Bağ yırtıldıysa ameliyat gerekir mi?", "Çoğu zaman hayır. Tam bağ yırtıklarında da tedavi genellikle ameliyatsızdır: kısa süreli destek, kademeli yük ve egzersiz programı. 2018'de BJSM'de yayımlanan kılavuz, ameliyatı kapsamlı ve düzgün yürütülen egzersiz temelli tedaviye yanıt vermeyen durumlara ayırıyor."),
 ("Buz mu uygulamalıyım?", "Egzersiz programıyla birlikte, aralıklı ve tekrarlayan buz uygulaması kılavuzda ağrı ve şişliği azaltmak için kullanılabilecek yöntemler arasında yer alıyor. Buzu doğrudan cilde koymayın, arada ince bir bez bulundurun."),
 ("Bileklik kullanmalı mıyım?", "Yeni burkulmada bant ya da bileklik gibi bir destek kullanmak önerilir. Burkulma geçirmiş kişilerde yeni burkulmaları önlemek için de spor sırasında bileklik kullanmak ve denge egzersizleri yapmak öneriliyor. 46 sistematik derlemeyi bir araya getiren bir çalışmada, tekrar burkulmayı önlemede bileklik için güçlü, denge ve koordinasyon çalışmaları için orta düzeyde kanıt bulundu; yeni burkulmada iltihap giderici ağrı kesiciler ve erken hareket için kanıt güçlüydü."),
 ("Neden sürekli aynı ayağımı burkuyorum?", "Burkulma sonrasında denge, kas gücü ve ayak bileğinin konum algısı tam olarak toparlanmadıysa bilek yeniden burkulmaya yatkın hale gelir. Ağrı geçse de denge ve güçlendirme egzersizlerine devam etmek ve spora kademeli dönmek bu döngüyü kırmanın yoludur. Futbolcularla yapılan 4 çalışmayı birleştiren bir meta-analizde, antrenman öncesi düzenli yapılan yapılandırılmış bir ısınma programı (FIFA 11+) ayak bileği sakatlıklarını %32 azalttı."),
]

BILEK_SRC = [
 "Bachmann LM, et al. " + ext("https://www.qxmd.com/r/12595378", "Accuracy of Ottawa ankle rules to exclude fractures of the ankle and mid-foot: systematic review") + ". BMJ. 2003. Özet: " + ext("https://www.aafp.org/pubs/afp/issues/2003/0815/p745a.html", "American Family Physician, 2003") + ".",
 "Bleakley CM, O'Connor SR, Tully MA, et al. " + ext("https://www.bmj.com/content/340/bmj.c1964.abstract", "Effect of accelerated rehabilitation on function after ankle sprain: randomised controlled trial") + ". BMJ. 2010;340:c1964.",
 "Lamb SE, et al. " + ext("https://read.qxmd.com/read/19217992/mechanical-supports-for-acute-severe-ankle-sprain-a-pragmatic-multicentre-randomised-controlled-trial", "Mechanical supports for acute, severe ankle sprain: a pragmatic, multicentre, randomised controlled trial") + ". Lancet. 2009.",
 "Wolfe MW, Uhl TL, Mattacola CG, McCluskey LC. " + ext("https://www.aafp.org/afp/2001/0101/p93.pdf", "Management of ankle sprains") + ". Am Fam Physician. 2001;63(1):93-104.",
 "Martin RL, Davenport TE, Fraser JJ, et al. " + ext("https://www.orthopt.org/uploads/content_files/files/jospt.2021.0302.pdf", "Ankle stability and movement coordination impairments: lateral ankle ligament sprains revision 2021. Clinical practice guidelines linked to the International Classification of Functioning, Disability and Health") + ". J Orthop Sports Phys Ther. 2021;51(4):CPG1-CPG80.",
 "Vuurberg G, Hoorntje A, Wink LM, et al. " + ext("https://bjsm.bmj.com/content/52/15/956", "Diagnosis, treatment and prevention of ankle sprains: update of an evidence-based clinical guideline") + ". Br J Sports Med. 2018;52(15):956.",
 "NHS. " + ext("https://www.nhs.uk/conditions/sprains-and-strains/", "Sprains and strains") + ". Page last reviewed 23 April 2024.",
 "Physiopedia. " + ext("https://www.physio-pedia.com/Ottawa_Ankle_Rules", "Ottawa Ankle Rules") + ".",
 "Doherty C, Bleakley C, Delahunt E, Holden S. " + ext("https://bjsm.bmj.com/content/51/2/113", "Treatment and prevention of acute and recurrent ankle sprain: an overview of systematic reviews with meta-analysis") + ". Br J Sports Med. 2017;51(2):113–125.",
 "Thorborg K, Krommes KK, Esteve E, et al. " + ext("https://bjsm.bmj.com/content/51/7/562", "Effect of specific exercise-based football injury prevention programmes on the overall injury rate in football: a systematic review and meta-analysis of the FIFA 11 and 11+ programmes") + ". Br J Sports Med. 2017;51(7):562–571.",
]

BILEK_TL = [
 ("2003", "27 çalışmayı ve 15.581 kişiyi birleştiren bir derlemede Ottawa ayak bileği kuralları kırıkların %97,6'sını yakaladı; kuralların röntgen gerekmeyen hastaları ayırmada güvenilir olduğu sonucuna varıldı."),
 ("2009", "Birleşik Krallık'ta 8 acil serviste 584 ağır burkulma hastasıyla yapılan çalışmada 10 günlük diz altı alçı ve Aircast tipi bileklik, yalnızca elastik bandaja göre 3. ayda daha hızlı toparlanma sağladı; yazarlar en geniş yararı gösteren diz altı alçıyı önerdi."),
 ("2010", "Kuzey İrlanda'da (Belfast) hafif ve orta burkulması olan 101 kişiyle yapılan çalışmada ilk hafta erken egzersiz programı uygulananlar, koruma, dinlenme, buz, bandaj ve yükseltmeden oluşan geleneksel bakım alanlara göre 1. ve 2. haftada daha iyi işlev gösterdi."),
 ("2017", "46 sistematik derlemeyi bir araya getiren bir çalışma, tekrar burkulmayı önlemede bileklik için güçlü, denge ve koordinasyon egzersizleri için orta düzeyde kanıt buldu."),
 ("2018", "Bir kanıta dayalı kılavuz güncellendi (BJSM): bağ hasarı en iyi yaralanmadan 4–5 gün sonra yapılan muayeneyle değerlendiriliyor; denetimli egzersiz programları pasif yöntemlere tercih ediliyor; ameliyat yalnızca kapsamlı egzersiz tedavisine yanıt vermeyenlere ayrılıyor."),
 ("2021", "Amerikan Fizyoterapi Derneği'nin (APTA) kılavuzu güncellendi (JOSPT): dış destek ve kademeli yük, yapılandırılmış egzersiz ve manuel terapi en güçlü (A) düzeyde önerildi; ultrason tedavisi önerilmedi (A)."),
]

BILEK_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Ayak bileği burkulması</h1>
    <p class="lede">Ayak bileği çoğunlukla içe doğru burkulur ve dış yandaki bağlar zorlanır ya da yırtılır. Çoğu burkulma ameliyatsız iyileşir. Erken ve kademeli yük verme, egzersiz ve denge çalışmaları iyileşmeyi destekler ve aynı bileğin yeniden burkulma riskini azaltır.</p>
    <p class="meta">Son güncelleme: 31 Ekim 2026</p>
  </div>
</header>
<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>Erken yük</b><span>Destekle, kademeli olarak ayağa basmak önerilir</span></div>
        <div class="stat"><b>4 adım</b><span>Atılamıyorsa röntgen gerekebilir (Ottawa kuralları)</span></div>
        <div class="stat"><b>%97,6</b><span>Ottawa kurallarının kırığı atlamama başarısı (27 çalışma)</span></div>
        <div class="stat"><b>%40</b><span>İlk kez burkulma geçirenlerin izlendiği bir çalışmada 12. ayda kronik instabilite gelişenler</span></div>
      </div>
      {g_toc([("nedir", "Nedir?"), ("derece", "Dereceleri"), ("rontgen", "Röntgen gerekir mi?"), ("seyir", "Ne kadar sürer?"), ("tarihce", "Geçmişten bugüne"), ("tedavi", "Tedavi seçenekleri"), ("egzersizler", "Egzersizler"), ("donus", "Spora dönüş"), ("videolar", "Videolar"), ("sss", "Sık sorulan sorular"), ("uyari", "Uyarı işaretleri")])}
    </div>
  </section>
  <section id="nedir">
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Ayak bileği içe doğru ani ve zorlu bir şekilde döndüğünde, dış kemik çıkıntısının önündeki ve altındaki bağlar gerilir ya da yırtılır. Ağrı, şişlik ve morarma olur; basmak zorlaşır.</p>
        <p class="soft">Burkulmadan sonra rehabilitasyon yarım kalırsa bilek yeniden burkulmaya yatkın hale gelebilir ve bazı kişilerde bilekte sık sık boşalma hissi (kronik instabilite) gelişebilir.</p>
      </div>
      <div>
        <h2>İlk günlerde</h2>
        <ul class="dots">
          <li>Bileği bant ya da bileklikle destekleyin, ağrının izin verdiği ölçüde basın.</li>
          <li>Gerekirse ilk günler koltuk değneği kullanın, ama kademeli olarak ayağa yük verin.</li>
          <li>Aralıklı buz uygulaması ve bacağı yükseltmek şişliği azaltmaya yardım eder.</li>
          <li>Ayak bileği pompasıyla hareketi erkenden koruyun.</li>
          <li>Ağrı kesici gerekiyorsa hekiminize danışın.</li>
        </ul>
      </div>
    </div>
  </section>
  <section id="derece">
    <div class="wrap">
      <h2>Burkulmanın dereceleri</h2>
      <p class="soft">Burkulmalar bağdaki hasara göre üç dereceye ayrılır. Derece, iyileşme süresi ve ne kadar destek gerektiği hakkında fikir verir. Kılavuzlara göre bağ hasarı en doğru şekilde yaralanmadan 4–5 gün sonra yapılan muayeneyle değerlendirilir.</p>
      <div class="kinds">
        <div class="kind"><span class="n">I</span><h3>Hafif</h3><p>Bağda kısmi, hafif hasar; hafif hassasiyet ve şişlik. Az ağrıyla basılabilir ve yürünebilir; eklemde gevşeklik yok.</p></div>
        <div class="kind"><span class="n">II</span><h3>Orta</h3><p>Bağda daha belirgin ama tam olmayan yırtık; orta düzeyde ağrı, şişlik ve morarma. Basarken ve yürürken ağrı olur; hafif ya da orta derecede gevşeklik olabilir.</p></div>
        <div class="kind"><span class="n">III</span><h3>Ağır</h3><p>Bağın tam yırtığı; belirgin şişlik ve morarma, basamama ve yürüyememe, muayenede eklemde belirgin gevşeklik.</p></div>
      </div>
    </div>
  </section>
  <section id="rontgen">
    <div class="wrap">
      <h2>Röntgen gerekir mi?</h2>
      <p class="soft">Çoğu burkulmada kırık yoktur ve röntgen gerekmez. Ottawa ayak bileği kuralları, röntgen gereken hastaları ayırmak için geliştirildi ve 27 çalışmanın birleştirildiği bir derlemede kırıkların %97,6'sını yakaladı. Kuralın yalnızca bir kısmını (örneğin yalnızca basabilmeyi) kullanmak doğruluğunu düşürür; tamamı uygulanmalıdır.</p>
      <div class="callout">
        <p>Ayak bileği bölgesinde ağrıyla birlikte şunlardan biri varsa röntgen gerekir: iç ya da dış kemik çıkıntısının arka kenarında, alttaki 6 santimlik bölümde ya da ucunda kemik üzerinde hassasiyet; yaralanmadan hemen sonra ve muayenede 4 adım atamamak.</p>
      </div>
    </div>
  </section>
  <section id="seyir">
    <div class="wrap">
      <h2>Ne kadar sürer?</h2>
      <p class="soft">ABD fizyoterapi kılavuzunun aktardığı verilere göre burkulma geçirenlerin yalnızca yaklaşık yarısı sağlık hizmetine başvuruyor. İşe ya da spora dönüş, etkinliğe göre 1 günden 3 haftayı biraz aşan sürelere kadar değişebiliyor. Ancak ağrının geçmesi bileğin tamamen toparlandığı anlamına gelmiyor: kişilerin %5–33'ünde ağrı 1 yıl ya da daha uzun sürüyor ve yaklaşık 3 yılda tam iyileşme %50–85 arasında bildiriliyor.</p>
      <div class="callout">
        <p><strong>Kronik instabilite:</strong> İlk kez burkulma geçirenlerin izlendiği bir çalışmada 12. ayda %40'ında bilekte tekrarlayan boşalma ve burkulmalarla seyreden kronik instabilite gelişti, %60'ı ise sorunsuz toparlandı. Denge ve kas-sinir kontrolü egzersizleri hem iyileşmede hem de bu durumu önlemede önemlidir.</p>
      </div>
    </div>
  </section>
  <section id="tarihce">
    <div class="wrap">
      <p class="eyebrow">Geçmişten bugüne</p>
      <h2>Burkulma tedavisinin kısa tarihi</h2>
      <p class="soft">Burkulmada uzun süre dinlenme ve hareketsizlik ön plandaydı. Son yirmi yılın araştırmaları röntgen kararının nasıl verileceğini netleştirdi, erken ve kademeli hareketin ve denge egzersizlerinin önemini gösterdi.</p>
      {g_tl(BILEK_TL)}
    </div>
  </section>
  <section id="tedavi">
    <div class="wrap">
      <h2>Tedavi</h2>
      <p class="soft">Amerikan Fizyoterapi Derneği'nin (APTA) 2021 kılavuzu burkulma sonrası tedaviyi şu başlıklarda topluyor.</p>
      <ul class="tx">
        <li><b>Koruma ve kademeli yük</b><span>Bant ya da bileklik gibi dış destekle ayak bileğini korumak ve ayağa kademeli olarak yük vermek önerilir (A). Ağır yaralanmalarda 10 güne kadar hareketsizleştirme gerekebilir.</span></li>
        <li><b>Egzersiz</b><span>Korunarak yapılan aktif hareket, kas-sinir kontrolü ve denge egzersizlerini içeren yapılandırılmış bir program önerilir (A).</span></li>
        <li><b>Manuel terapi</b><span>Lenf drenajı, yumuşak doku ve eklem mobilizasyonları ağrısız aralıkta uygulanır (A).</span></li>
        <li><b>Buz ve ilaç</b><span>Egzersizle birlikte aralıklı buz uygulaması ve hekim önerisiyle iltihap giderici ağrı kesiciler kullanılabilir.</span></li>
        <li><b>İşe ve spora dönüş</b><span>Rehabilitasyonun erken döneminden itibaren işe ve spora özgü çalışmalar planlanır; dönüşte bileklik kullanılabilir.</span></li>
        <li><b>Yeni burkulmaları önlemek</b><span>Burkulma geçirmiş kişilerde bileklik kullanmak ve denge odaklı egzersiz programı yapmak önerilir (A).</span></li>
      </ul>
      <h3 class="g-h3">Tedavi seçenekleri: kılavuzlar ne diyor?</h3>
      <p class="soft">Amerikan Fizyoterapi Derneği'nin (APTA) kılavuzu (JOSPT, 2021) ile British Journal of Sports Medicine'de yayımlanan kanıta dayalı kılavuz güncellemesinin (2018) önerileri yan yana. Parantez içindeki harfler JOSPT kılavuzundaki öneri düzeyidir (A güçlü, B orta, C zayıf, D çelişkili kanıt). İkinci kılavuzun önerileri özetinden alındı; tedavi kişiye göre seçilir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Tanı ve röntgen</h3><dl><dt>JOSPT</dt><dd>Röntgen kararı için Ottawa kurallarının tamamı kullanılmalı; muayene en doğru sonucu yaralanmadan 4–5 gün sonra verir.</dd><dt>BJSM kılavuzu</dt><dd>Bağ hasarı en iyi 4–5 gün sonra yapılan muayeneyle değerlendirilir.</dd></dl></div>
        <div class="kind"><h3>Destek ve hareketsizleştirme</h3><dl><dt>JOSPT</dt><dd>Bant ya da bileklik ve kademeli yük (A); ağır yaralanmada 10 güne kadar hareketsizleştirme gerekebilir.</dd><dt>BJSM kılavuzu</dt><dd>Kısa süreli hareketsizleştirme ağrı ve şişliği azaltmaya yardımcı olabilir; bağ yırtığında en yararlısı bant ya da bileklikle birlikte egzersiz programı.</dd></dl></div>
        <div class="kind"><h3>Egzersiz</h3><dl><dt>JOSPT</dt><dd>Korunarak aktif hareket, kas-sinir kontrolü ve denge içeren yapılandırılmış program (A).</dd><dt>BJSM kılavuzu</dt><dd>Denetimli egzersiz programları pasif yöntemlere tercih edilmeli.</dd></dl></div>
        <div class="kind"><h3>Manuel terapi</h3><dl><dt>JOSPT</dt><dd>Lenf drenajı, yumuşak doku ve eklem mobilizasyonu ağrısız aralıkta (A); uzun süren instabilitede eklem mobilizasyonu kısa vadede hareket ve denge için (A).</dd></dl></div>
        <div class="kind"><h3>Buz ve ilaç</h3><dl><dt>JOSPT</dt><dd>Egzersizle birlikte aralıklı, tekrarlanan buz (C); iltihap giderici ağrı kesiciler yetkili meslek mensubunca verilebilir (C).</dd><dt>BJSM kılavuzu</dt><dd>İltihap giderici ağrı kesiciler ağrı ve şişliği azaltabilir, ancak doğal iyileşmeyi baskılayabilir.</dd><dt>Not</dt><dd>Hangisinin size uygun olduğunu hekiminize sorun.</dd></dl></div>
        <div class="kind"><h3>Cihazlar ve iğneler</h3><dl><dt>JOSPT</dt><dd>Ultrason tedavisi kullanılmamalı (A); düşük düzeyli lazer erken dönemde ağrı için (C); kısa dalga diatermi şişlik için (C); elektroterapi ve akupunktur konusunda kanıt çelişkili (D).</dd></dl></div>
        <div class="kind"><h3>Ameliyat</h3><dl><dt>BJSM kılavuzu</dt><dd>Yalnızca kapsamlı, egzersiz temelli tedaviye yanıt vermeyen durumlara ayrılmalı.</dd></dl></div>
        <div class="kind"><h3>Yeniden burkulmayı önleme</h3><dl><dt>JOSPT</dt><dd>Burkulma geçirenlerde bileklik ile denge ve kas-sinir kontrolü egzersizleri (A); hiç burkulmamış ama riskli kişilerde bileklik (A), denge egzersizi (C).</dd><dt>BJSM kılavuzu</dt><dd>Tekrarlayan burkulmalarda bileklik etkili bir seçenek olarak düşünülmeli.</dd></dl></div>
      </div>
    </div>
  </section>
  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Ayak bileği için altı egzersiz</h2>
      <p class="soft">İlk iki egzersizle erken dönemde başlayabilirsiniz. Ağrı ve şişlik azaldıkça güçlendirme ve denge egzersizlerine geçin. Ayakta yapılan hareketlerde sağlam bir yere tutunun; keskin ağrı olursa durun.</p>
      {ex_grid(["apump2", "towelst2", "evert", "heel4", "sls3", "tandem2"])}
    </div>
  </section>
  <section id="donus">
    <div class="wrap two">
      <div>
        <h2>Spora ve günlük hayata dönüş</h2>
        <p class="soft">Ağrının geçmesi, bileğin tamamen toparlandığı anlamına gelmez. Dönüşü kademeli yapmak yeni burkulmaları önler.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Önce düz zeminde yürüyün, sonra hafif koşuya, en son yön değiştirme ve zıplamalara geçin.</li>
        <li>Burkulan ayağınızın üzerinde rahatça dengede durabilmeden koşuya başlamayın.</li>
        <li>Spora dönüşte bir süre bileklik ya da bantla destek kullanın.</li>
        <li>Ağrı geçtikten sonra da denge egzersizlerine haftada birkaç kez devam edin.</li>
        <li>Engebeli zeminde ve karanlıkta dikkatli olun; topuğu destekleyen ayakkabılar giyin.</li>
      </ul>
    </div>
  </section>
  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Ayak bileği burkulması için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("JlImzKN7w-E", "Ayak bileği rehabilitasyon videosunu oynat", "REBUILD Your Ankles-Stop Pain &amp; Return To Action!")}
          <h3>Ayak bileğini yeniden güçlendirmek</h3>
          <p>Burkulma sonrası hareket ve güçlendirme çalışmaları.</p>
        </div>
        <div class="vid">
          {vbox("Zk1vdqlCFUI", "Ayak bileği güçlendirme videosunu oynat", "The 8 Best At-Home Ankle Strengthening Exercises")}
          <h3>Evde ayak bileği güçlendirme</h3>
          <p>Hareket açıklığı kazanıldıktan sonra yapılacak güçlendirme egzersizleri.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir. Kanal hakkında: <a href="https://www.startribune.com/meet-the-minnesota-physical-therapists-who-have-become-youtube-superstars/508806552" target="_blank" rel="noopener">Star Tribune, 19 Nisan 2019</a>.</p>
    </div>
  </section>
  <section id="sss">
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(BILEK_FAQ)}
    </div>
  </section>
  <section id="uyari">
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft"><strong>Hemen acil servise başvurun:</strong></p>
      <ul class="dots redflags">
        <li>Ayak bileğinde şekil bozukluğu</li>
        <li>Ayakta uyuşma, soğukluk ya da renk değişikliği (dolaşım ya da sinir etkilenmiş olabilir)</li>
        <li>Yaralanmadan hemen sonra ve muayenede 4 adım atamamak ya da kemik üzerinde belirgin hassasiyet (kırık olabilir; röntgen gerekebilir)</li>
        <li>Topuğun arkasında "pat" sesiyle başlayan ağrı ve parmak ucunda yükselememe (aşil tendonu yırtığı olabilir)</li>
        <li>Baldırda şişlik, ağrı ve kızarıklık (pıhtı olabilir)</li>
        <li>Ateş ve giderek artan kızarıklık</li>
      </ul>
      <p class="soft"><strong>Kısa sürede bir hekime başvurun:</strong></p>
      <ul class="dots redflags">
        <li>Haftalar geçtiği hâlde düzelmeyen ağrı ve şişlik ya da bilekte sık sık boşalma hissi (eşlik eden bağ ya da kıkırdak hasarı ya da kronik instabilite olabilir)</li>
      </ul>
      {CTA_CARD("Ayak bileği burkulmanız", "ayak bileği burkulması")}
    </div>
  </section>
  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(BILEK_SRC)}
    </div>
  </section>
</main>'''

page("ayak-bilegi-burkulmasi.html", "Ayak Bileği Burkulması",
     "Ayak bileği burkulması: dereceleri, burkulan ayağa basılır mı, röntgen gerekir mi, ne kadar sürer, neden tekrarlar? İki kılavuzun karşılaştırması, kısa tarihçe, evde altı egzersiz ve uyarı işaretleri.",
     "ayak-bilegi-burkulmasi.html", NECK_CSS, BILEK_BODY, YT_JS,
     seo_title="Ayak Bileği Burkulması: İlk Günler, Egzersizler ve Spora Dönüş | İhsan Eren",
     condition="Ayak bileği burkulması", about=cond("Ayak bileği burkulması"),
     faq_items=pick(BILEK_FAQ, 0, 1, 3, 4))

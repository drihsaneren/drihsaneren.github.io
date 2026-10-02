# -*- coding: utf-8 -*-
# Evde rehabilitasyon: Parkinson, kalça kırığı, kanser ve egzersiz. self_part.py'den sonra exec edilir.

def _ex(key, base, title, text, dose):
    SV[key] = SV[base]
    EXT[key] = (title, text, dose)

# ------------------------------------------------------------------ PARKİNSON
_ex("pd_sts", "sts", "Güçlü kalkış",
    "Sağlam bir sandalyenin önüne oturun, ayaklarınızı biraz geriye alın. Burnunuz ayak parmaklarınızın üzerine gelecek kadar öne eğilin ve içinizden “bir, iki, kalk” diye sayarak tek hamlede, güçlü şekilde ayağa kalkın. Kontrollü oturun.",
    "10 tekrar, günde 2 kez")
_ex("pd_bext", "bext", "Büyük esneme",
    "Ayakta durun, ellerinizi belinizin arkasına koyun. Göğsünüzü açıp gövdenizi rahat ettiğiniz kadar geriye esnetin, gözleriniz ileriye baksın. Öne kapanan duruşa karşı iyi bir alışkanlıktır.",
    "5–10 tekrar, gün içinde birkaç kez")
_ex("pd_thor", "thor", "Göğüs kafesini açma",
    "Sırtı alçak bir sandalyeye oturun, ellerinizi ensenizde birleştirin. Dirseklerinizi iki yana açıp göğsünüzü tavana doğru kaldırın ve hafifçe geriye esneyin. Hareketi büyük ve yavaş yapın.",
    "10 tekrar")
_ex("pd_side", "sidestep", "Büyük yana adımlar",
    "Tezgâha tutunarak durun. Bir bacağınızı yana doğru olabildiğince büyük bir adımla açın, ağırlığınızı o ayağa aktarın, sonra diğer ayağı yanına getirin. Adımları sayarak ritimli yapın.",
    "Her yöne 10 adım, 2 tur")
_ex("pd_tandem", "tandem", "Topuk-parmak yürüyüşü",
    "Tezgâh boyunca, bir elinizle hafifçe tutunarak yürüyün; her adımda öndeki ayağın topuğunu arkadaki ayağın parmaklarının önüne koyun. Gözleriniz ileriye baksın.",
    "10 adım, 2–3 tur")
_ex("pd_wshift", "wshift", "Ağırlık aktarma",
    "Tezgâhın önünde, ayaklarınız omuz genişliğinde durun. Ağırlığınızı yavaşça sağ ayağınıza, sonra sol ayağınıza aktarın; ardından öne ve arkaya. Parkinson'da dönüşler ve adım başlatma için önemlidir.",
    "Her yöne 10 kez")

PD_FAQ = [
 ("Egzersiz Parkinson'un ilerlemesini yavaşlatır mı?", "Umut verici bulgular var ama henüz kesin değil. Yeni tanı almış ve ilaç kullanmayan 128 kişilik SPARX çalışmasında haftada 3 kez, maksimum kalp hızının %80–85'ine ulaşan koşu bandı egzersizi yapanların hareket puanı 6 ayda neredeyse değişmedi; egzersiz yapmayanlarda ise 3 puan kötüleşti. Bu bulgu daha büyük bir faz III çalışmasında (SPARX3) test ediliyor."),
 ("Hangi egzersiz en iyisi?", "154 çalışmayı inceleyen Cochrane derlemesi, egzersiz türleri arasında belirgin bir fark bulmadı: dans ile yürüme, denge ve günlük işlev eğitimi hareket belirtilerinde muhtemelen orta düzeyde fayda sağlıyor. Araştırmacılara göre asıl önemli olan egzersiz yapmak; tür ikinci planda. Keyif aldığınız ve düzenli yapabileceğiniz bir hareketi seçin."),
 ("Yürürken ayaklarım yere yapışıyor, ne yapabilirim?", "Buna donma denir. Durun, dik durup ağırlığınızı bir ayağınıza aktarın, sonra büyük bir adımla başlayın. Yere çizilmiş bir çizgiyi ya da ayağınızın önündeki hayali bir engeli adımlamayı düşünmek, içinizden ya da yüksek sesle ritim saymak ya da müzik dinlemek adım başlatmayı kolaylaştırabilir."),
 ("Günün hangi saatinde egzersiz yapmalıyım?", "Genellikle ilaçlarınızın en iyi etki ettiği saatler egzersiz için en uygun zamandır; hareketleriniz daha rahat olur. Önemli olan haftanın çoğu günü düzenli hareket etmektir."),
]

PD_SRC = [
 "World Health Organization. " + ext("https://www.who.int/news-room/fact-sheets/detail/parkinson-disease", "Parkinson disease") + ". Fact sheet.",
 "Ernst M, Folkerts AK, Gollan R, et al. " + ext("https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD013856.pub3/full", "Physical exercise for people with Parkinson's disease: a systematic review and network meta-analysis") + ". Cochrane Database Syst Rev. 2024.",
 "Schenkman M, Moore CG, Kohrt WM, et al. " + ext("https://jamanetwork.com/journals/jamaneurology/fullarticle/2664948", "Effect of high-intensity treadmill exercise on motor symptoms in patients with de novo Parkinson disease: a phase 2 randomized clinical trial") + ". JAMA Neurol. 2018;75(2):219-226.",
 "Osborne JA, Botkin R, Colon-Semenza C, et al. " + ext("https://academic.oup.com/ptj/article/102/4/pzab302/6485202", "Physical therapist management of Parkinson disease: a clinical practice guideline from the American Physical Therapy Association") + ". Phys Ther. 2022;102(4):pzab302.",
 "Van Bladel A, Herssens N, Bouche K, et al. " + ext("https://journals.sagepub.com/doi/abs/10.1177/02692155231158565", "Proportion of falls reported in persons with Parkinson's disease: a meta-analysis") + ". Clin Rehabil. 2023.",
]

PD_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>Parkinson hastalığında egzersiz ve evde rehabilitasyon</h1>
    <p class="lede">Parkinson ilerleyici bir hastalık; ama düzenli egzersiz, ilaç tedavisinin yanında hareket belirtilerini ve yaşam kalitesini iyileştirmenin en önemli yollarından biri. Araştırmaların ortak mesajı: hangi egzersizi seçtiğinizden çok, düzenli yapmanız önemli.</p>
    <p class="meta">Son güncelleme: 29 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>8,5 milyon</b><span>Dünyada Parkinson hastalığıyla yaşayan kişi (2019)</span></div>
        <div class="stat"><b>2 kat</b><span>Son 25 yılda hastalığın yaygınlığındaki artış</span></div>
        <div class="stat"><b>2'de 1</b><span>Parkinson hastalarında izlem süresince en az bir kez düşenler</span></div>
        <div class="stat"><b>154</b><span>Parkinson'da egzersizi inceleyen 2024 tarihli Cochrane derlemesindeki çalışma sayısı</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Parkinson hastalığı, beyinde dopamin üreten hücrelerin zamanla azalmasıyla ortaya çıkar. Hareketlerde yavaşlama, titreme, kaslarda sertlik, yürüme güçlüğü ve denge sorunları en bilinen belirtilerdir. Uyku sorunları, ruh hali değişiklikleri, ağrı ve düşünme becerilerinde güçlükler de eşlik edebilir.</p>
        <p class="soft">Dünya Sağlık Örgütü'ne göre fizyoterapiyi de içeren rehabilitasyon; kuvvet, yürüme ve denge eğitimi ile su içi egzersizler, Parkinson hastalarının işlevselliğini ve yaşam kalitesini iyileştirebilir ve bakım verenlerin yükünü azaltabilir.</p>
      </div>
      <div>
        <h2>Evde rehabilitasyon neleri hedefler?</h2>
        <ul class="dots">
          <li>Hareketleri büyütmek: adımları uzatmak, kolları sallamak, sesi yükseltmek</li>
          <li>Dik duruşu korumak, öne kapanmayı azaltmak</li>
          <li>Denge ve dönüşleri güvenli hale getirmek, düşmeleri önlemek</li>
          <li>Sandalyeden kalkma, yataktan çıkma gibi günlük işleri kolaylaştırmak</li>
          <li>Yürürken donmalarla başa çıkma yolları öğrenmek</li>
          <li>Kondisyon ve kas gücünü korumak</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Egzersiz neden bu kadar önemli?</h2>
      <p class="soft">154 çalışmayı ve 7.837 kişiyi kapsayan 2024 tarihli Cochrane derlemesinde dans ile yürüme, denge ve günlük işlev eğitiminin hareket belirtilerinde muhtemelen orta düzeyde fayda sağladığı, su içi egzersizin yaşam kalitesini belirgin şekilde iyileştirdiği görüldü. Egzersiz türleri arasında belirgin bir fark bulunmadı; araştırmacılara göre asıl önemli olan egzersiz yapmak.</p>
      <p class="soft">Yoğunluk da önemli olabilir. Yeni tanı almış, henüz ilaç kullanmayan 128 kişilik SPARX çalışmasında haftada 3 kez, maksimum kalp hızının %80–85'ine ulaşan koşu bandı egzersizi yapan grubun hareket puanı 6 ayda neredeyse değişmedi; egzersiz yapmayanlarda ise 3 puan kötüleşti.</p>
      <div class="callout">
        <p>ABD Fizyoterapi Derneği'nin 2022 kılavuzu aerobik egzersiz, kuvvet ve denge eğitimi, yürürken ritim ya da yere çizgi gibi dış uyaranların kullanımı, günlük işlere yönelik eğitim ve gerektiğinde uzaktan rehabilitasyonu içeren bir fizyoterapi yaklaşımı öneriyor.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Büyük ve ritimli: altı egzersiz</h2>
      <p class="soft">Parkinson'da hareketler zamanla küçülür. Bu yüzden egzersizleri bilerek “büyük” yapın: adımları uzatın, kolları açın, sayarak ritim tutun. Ayakta yapılan hareketlerde tezgâh gibi sağlam bir desteğin yanında durun; mümkünse ilk zamanlarda yanınızda biri bulunsun.</p>
      {ex_grid(["pd_sts", "pd_bext", "pd_thor", "pd_side", "pd_tandem", "pd_wshift"])}
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Günlük hayatta pratik öneriler</h2>
        <p class="soft">Küçük değişiklikler hem güvenliği artırır hem de bağımsızlığı korur.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Dönerken yerinde dönmek yerine geniş bir yay çizerek birkaç adımla dönün.</li>
        <li>Yürürken adımlarınızı içinizden sayın ya da ritimli bir müzik dinleyin.</li>
        <li>Kaygan halıları kaldırın, geceleri koridoru aydınlatın, banyoya tutunma barı taktırın.</li>
        <li>Aynı anda iki iş yapmaktan kaçının; yürürken konuşmanız gerekiyorsa durun.</li>
        <li>Egzersizi ilaçlarınızın en iyi etki ettiği saatlere planlayın.</li>
        <li>Düşme riskiniz varsa <a href="dusme-onleme.html">düşmeleri önleme rehberine</a> göz atın.</li>
      </ul>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Parkinson için egzersiz videoları</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("GpWFZdeJqxQ", "Ayakta Parkinson programı videosunu oynat", "The LARGE 10 Parkinson’s Program (Standing Version)")}
          <h3>Büyük hareketlerle 10 egzersiz: ayakta</h3>
          <p>Hareketleri bilerek büyütmeye dayanan, ayakta yapılan 10 egzersizlik program.</p>
        </div>
        <div class="vid">
          {vbox("JtZ4pO0AzbM", "Parkinson programı videosunu oynat", "The LARGE 10 Parkinson’s Program")}
          <h3>Büyük hareketlerle 10 egzersiz</h3>
          <p>Aynı yaklaşımın ilk sürümü; günlük hareketleri büyütmeye odaklanır.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(PD_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden hekiminize başvurun:</p>
      <ul class="dots redflags">
        <li>Belirtilerde birkaç gün içinde belirgin ve açıklanamayan kötüleşme</li>
        <li>Yaralanmayla sonuçlanan düşme ya da sık tekrarlayan düşmeler</li>
        <li>Yutkunma güçlüğü, yemek sırasında sık öksürme ya da boğulma hissi</li>
        <li>Yeni başlayan karışıklık, halüsinasyon ya da aşırı uyku hali</li>
        <li>Ayağa kalkınca bayılacak gibi olma</li>
      </ul>
      {CTA_CARD("Parkinson hastalığında evde rehabilitasyon", "Parkinson hastalığı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(PD_SRC)}
    </div>
  </section>
</main>'''

page("parkinson.html", "Parkinson Hastalığında Egzersiz",
     "Parkinson hastalığında egzersiz neden önemli, hangi egzersiz daha iyi, donmalarla nasıl başa çıkılır? Evde altı egzersiz, günlük hayat önerileri ve videolar.",
     "parkinson.html", NECK_CSS, PD_BODY, YT_JS,
     seo_title="Parkinson Hastalığında Egzersiz ve Evde Rehabilitasyon | İhsan Eren",
     condition="Parkinson hastalığı", faq_items=PD_FAQ)

# ------------------------------------------------------------------ KALÇA KIRIĞI
_ex("hf_apump", "apump", "Ayak bileği pompası",
    "Sırtüstü ya da oturarak, ayak bileklerinizi yukarı ve aşağı doğru hareket ettirin. Bacaklardaki kan dolaşımını destekler; ameliyattan sonraki ilk günlerden itibaren yapılabilir.",
    "Saatte 10–20 tekrar")
_ex("hf_quad", "quad", "Havluya bastırma",
    "Sırtüstü uzanın, ameliyatlı dizinizin altına rulo yapılmış bir havlu koyun. Dizinizin arkasını havluya bastırarak uyluğunuzun ön kasını sıkın, 5 saniye tutun ve gevşeyin.",
    "10 tekrar, günde 3 kez")
_ex("hf_hslide", "hslide", "Topuk kaydırma",
    "Sırtüstü uzanın. Ameliyatlı bacağınızın topuğunu yatakta kaydırarak dizinizi rahat ettiğiniz kadar bükün, sonra yavaşça düzeltin. Cerrahınızın verdiği hareket sınırlarını aşmayın.",
    "10 tekrar, günde 2–3 kez")
_ex("hf_sabd", "sabd", "Kalçayı yana açma",
    "Tezgâha tutunarak dik durun. Ameliyatlı bacağınızı dizi düz, ayak ucu öne bakacak şekilde yana doğru açın ve yavaşça indirin. Gövdenizi yana eğmeyin.",
    "10 tekrar, günde 2 kez")
_ex("hf_sts", "sts", "Sandalyeden kalkıp oturma",
    "Kollu, sağlam bir sandalyede oturun. Ellerinizden destek alarak ve ağırlığınızı iki bacağa dağıtarak ayağa kalkın, kontrollü şekilde oturun. Kolaylaştıkça el desteğini azaltın.",
    "5–10 tekrar, günde 2 kez")
_ex("hf_heel", "heel2", "Tezgâha tutunarak topuk yükseltme",
    "Mutfak tezgâhına iki elinizle tutunun. Parmak uçlarınıza yükselin, bir an bekleyip yavaşça inin. Baldır kaslarını güçlendirir, dengeye yardım eder.",
    "10 tekrar, günde 2 kez")

HF_FAQ = [
 ("Ameliyattan sonra ne zaman yürüyebilirim?", "Çoğu hastada ameliyattan sonraki gün, fizyoterapist eşliğinde ve yürüteçle ayağa kalkılır. İngiltere'nin kalça kırığı kılavuzu, tıbbi bir engel yoksa ameliyattan sonraki gün fizyoterapi değerlendirmesi ve ayağa kaldırma, sonrasında da en az günde bir kez hareket ettirme öneriyor. Bacağınıza ne kadar yük verebileceğinizi cerrahınız belirler."),
 ("Evde egzersize devam etmek gerçekten fark eder mi?", "Evet. 40 çalışmayı inceleyen Cochrane derlemesi, hastaneden çıktıktan sonra yürüme, denge ve günlük işlere yönelik egzersizlerin hareket kabiliyetini anlamlı şekilde artırdığını gösterdi. ABD'de 232 hastayla yapılan bir çalışmada 6 ay süren ev egzersiz programı, rehabilitasyonu tamamlamış hastalarda bile işlevi daha da iyileştirdi."),
 ("Kırığım protezle mi, vidayla mı tedavi edildi; fark eder mi?", "Evet. Kırığın türüne göre kırık vida ya da çivi ile sabitlenebilir ya da kalçanın bir kısmı protezle değiştirilebilir. Protez uygulandıysa bazı pozisyonlardan bir süre kaçınmanız gerekebilir. Hangi hareketlerin sizin için güvenli olduğunu cerrahınıza sorun; ayrıntılar için protez sonrası rehberine bakabilirsiniz."),
 ("Yeniden kırılmaması için ne yapmalıyım?", "Kalça kırıkları çoğu zaman bir düşme ve kemik erimesi birlikteliğinde ortaya çıkar. Kemik sağlığınızın değerlendirilmesini isteyin, düzenli denge ve güçlendirme egzersizleri yapın ve evinizi düşmelere karşı güvenli hale getirin."),
]

HF_SRC = [
 "National Institute for Health and Care Excellence. " + ext("https://www.nice.org.uk/guidance/cg124/chapter/recommendations", "Hip fracture: management (CG124)") + ". London: NICE; 2011, updated 2023.",
 "Fairhall NJ, Dyer SM, Mak JCS, et al. " + ext("https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD001704.pub5/full", "Interventions for improving mobility after hip fracture surgery in adults") + ". Cochrane Database Syst Rev. 2022;9:CD001704.",
 "Latham NK, Harris BA, Bean JF, et al. " + ext("https://jamanetwork.com/journals/jama/fullarticle/1829991", "Effect of a home-based exercise program on functional recovery following rehabilitation after hip fracture: a randomized clinical trial") + ". JAMA. 2014;311(7):700-708.",
 "The Chartered Society of Physiotherapy. " + ext("https://www.csp.org.uk/frontline/article/mobility-strategies-are-effective-adults-after-hip-fracture-surgery", "Mobility strategies are effective in adults after hip fracture surgery") + ".",
]

HF_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>Kalça kırığı sonrası evde rehabilitasyon</h1>
    <p class="lede">Kalça kırığı, özellikle ileri yaşta bağımsızlığı tehdit eden ciddi bir yaralanma. Ameliyattan sonra ne kadar erken ve düzenli hareket edilirse toparlanma o kadar iyi olur; evde sürdürülen egzersiz programı, hastaneden sonra da kazanım sağlıyor.</p>
    <p class="meta">Son güncelleme: 29 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>1. gün</b><span>Kılavuzun önerdiği fizyoterapi değerlendirmesi ve ayağa kalkma zamanı: ameliyattan sonraki gün</span></div>
        <div class="stat"><b>80 yaş</b><span>Kalça kırığı rehabilitasyonu çalışmalarındaki hastaların ortalama yaşı; %80'i kadın</span></div>
        <div class="stat"><b>40</b><span>Hareket odaklı rehabilitasyonu inceleyen Cochrane derlemesindeki çalışma sayısı (4.059 kişi)</span></div>
        <div class="stat"><b>6 ay</b><span>Rehabilitasyon sonrası bile işlevi iyileştiren ev egzersiz programının süresi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Ameliyattan sonraki ilk günler</h2>
        <p class="soft">İngiltere'nin kalça kırığı kılavuzu ameliyatın başvurunun yapıldığı gün ya da ertesi gün yapılmasını, ameliyattan sonraki gün fizyoterapi değerlendirmesi ve ayağa kaldırmayı, sonrasında da en az günde bir kez hareket ettirmeyi öneriyor. Rehabilitasyonun hedefi, kişinin hareket kabiliyetini ve bağımsızlığını geri kazanarak kırık öncesindeki evine dönebilmesi.</p>
        <p class="soft">Bacağa ne kadar yük verilebileceği ve hangi hareketlerden kaçınılacağı, kırığın türüne ve yapılan ameliyata göre değişir. Bu konuda cerrahınızın önerilerine uyun.</p>
      </div>
      <div>
        <h2>Evde neler çalışılır?</h2>
        <ul class="dots">
          <li>Yataktan çıkma, sandalyeden kalkma ve tuvalete oturup kalkma</li>
          <li>Yürüteçle, sonra bastonla güvenli yürüme</li>
          <li>Kalça ve bacak kaslarını güçlendirme</li>
          <li>Denge ve dönüşler, düşme korkusuyla başa çıkma</li>
          <li>Merdiven inip çıkma</li>
          <li>Evde düşmelere karşı güvenlik düzenlemeleri</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Hastaneden sonra da egzersiz</h2>
      <p class="soft">40 çalışmayı ve 4.059 kişiyi kapsayan 2022 tarihli Cochrane derlemesinde, yürüme, denge ve günlük işlere yönelik egzersizlerin hareket kabiliyetini artırdığı görüldü. Hastaneden çıktıktan sonra yapılan programlarda kuvvet ve dayanıklılık egzersizleri de fayda sağladı; bu dönemdeki iyileşme küçük ama anlamlıydı ve kanıtın güvenilirliği yüksekti.</p>
      <p class="soft">ABD'de 232 hastayla yapılan bir çalışmada ise standart rehabilitasyonu tamamlamış hastalara 6 ay süren bir ev egzersiz programı verildi. Program bitiminde bu hastaların günlük işlevi, egzersiz almayan gruba göre daha iyiydi ve fark 3 ay sonra da sürüyordu.</p>
      <div class="callout">
        <p>Kalça kırığı çoğu zaman bir düşmenin ve kemik erimesinin birlikte sonucudur. Rehabilitasyonun yanında kemik sağlığınızın değerlendirilmesi ve düşmelerin önlenmesi de önemli: <a href="kemik-erimesi.html">kemik erimesi</a> ve <a href="dusme-onleme.html">düşmeleri önleme</a> rehberlerine göz atın.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>İyileşme için altı egzersiz</h2>
      <p class="soft">İlk üç egzersiz yatakta, son üçü ayakta ya da sandalyede yapılır. Hangi egzersizlere ne zaman başlayacağınızı ve bacağınıza ne kadar yük verebileceğinizi cerrahınız ve fizyoterapistiniz belirler. Ağrı belirgin şekilde artarsa durun.</p>
      {ex_grid(["hf_apump", "hf_quad", "hf_hslide", "hf_sabd", "hf_sts", "hf_heel"])}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Denge ve düşme videoları</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("uSCWsP0hR14", "Denge egzersizi videosunu oynat", "Best Standing Balance Exercise For Seniors To Stay Active &amp; Alert")}
          <h3>Yaşlılar için ayakta denge egzersizi</h3>
          <p>Tutunarak yapılan, adım adım zorlaşan denge egzersizleri.</p>
        </div>
        <div class="vid">
          {vbox("3H7eSIvife4", "Düştükten sonra kalkma videosunu oynat", "The Life-Saving Trick to Get Up After a Fall")}
          <h3>Düştükten sonra güvenle kalkmak</h3>
          <p>Yere düştüğünüzde paniğe kapılmadan, güvenli şekilde kalkmanın yolu.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(HF_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden cerrahınıza ya da bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Kasık ya da uylukta giderek artan ağrı, bacağa yeniden yük verememe</li>
        <li>Yarada kızarıklık, akıntı, ateş ya da titreme</li>
        <li>Baldırda şişlik, ağrı ve kızarıklık (pıhtı olabilir)</li>
        <li>Ani nefes darlığı ya da göğüs ağrısı (<strong>112</strong>'yi arayın)</li>
        <li>Yeni başlayan karışıklık ya da bilinç bulanıklığı</li>
      </ul>
      {CTA_CARD("Kalça kırığı sonrası süreciniz", "kalça kırığı sonrası rehabilitasyon")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(HF_SRC)}
    </div>
  </section>
</main>'''

page("kalca-kirigi.html", "Kalça Kırığı Sonrası Evde Rehabilitasyon",
     "Kalça kırığı ameliyatından sonra ne zaman yürünür, evde egzersiz neden önemli, yeniden kırılmaması için ne yapılmalı? Evde altı egzersiz ve güvenlik önerileri.",
     "kalca-kirigi.html", NECK_CSS, HF_BODY, YT_JS,
     seo_title="Kalça Kırığı Sonrası Evde Rehabilitasyon ve Egzersizler | İhsan Eren",
     condition="Kalça kırığı", faq_items=HF_FAQ)

# ------------------------------------------------------------------ KANSER VE EGZERSİZ
_ex("cx_sts", "sts", "Sandalyeden kalkıp oturma",
    "Sağlam bir sandalyenin önüne oturun. Kollarınızı göğsünüzde çaprazlayarak ayağa kalkın ve kontrollü şekilde oturun. Yorgun günlerde ellerinizden destek alın ya da tekrar sayısını azaltın.",
    "8–12 tekrar, 1–2 set")
_ex("cx_row", "row", "Lastik bantla kürek çekme",
    "Lastik bandı göğüs hizasında sağlam bir yere bağlayın. Dirseklerinizi gövdenize yakın tutarak bandı geriye çekin, kürek kemiklerinizi birbirine yaklaştırın ve yavaşça bırakın.",
    "8–12 tekrar, 1–2 set")
_ex("cx_bridge", "bridge", "Köprü",
    "Sırtüstü yatın, dizleriniz bükülü, ayaklarınız yerde. Kalçanızı sıkarak yavaşça kaldırın, 2–3 saniye bekleyip indirin.",
    "8–12 tekrar, 1–2 set")
_ex("cx_heel", "heel2", "Tezgâha tutunarak topuk yükseltme",
    "Mutfak tezgâhına hafifçe tutunun. Parmak uçlarınıza yükselin, bir an bekleyip yavaşça inin. Ellerinizde ya da ayaklarınızda uyuşma varsa desteği bırakmayın.",
    "10–15 tekrar, 1–2 set")
_ex("cx_wall", "wall", "Duvarda yarım çömelme",
    "Sırtınızı duvara dayayın, ayaklarınız duvardan bir adım önde olsun. Dizlerinizi rahat ettiğiniz kadar bükerek sırtınızı duvarda aşağı kaydırın, birkaç saniye bekleyip yukarı çıkın.",
    "8–10 tekrar")
_ex("cx_scap", "scap", "Kürek kemiği sıkıştırma",
    "Dik oturun ya da durun. Omuzlarınızı kaldırmadan kürek kemiklerinizi geriye ve aşağıya doğru yaklaştırın, 5 saniye tutup bırakın. Göğüs ameliyatlarından sonra duruşa iyi gelir.",
    "10 tekrar, günde 2 kez")

CX_FAQ = [
 ("Kemoterapi sırasında egzersiz yapabilir miyim?", "Çoğu kişi için evet; kılavuzlar tedavi sırasında da egzersizi öneriyor. Yorgun hissettiğiniz günlerde süreyi ve yoğunluğu azaltın. Ateşiniz, bir enfeksiyonunuz varsa ya da kan değerleriniz çok düşükse egzersize ara verin ve tedavi ekibinize danışın."),
 ("Çok yorgunum, dinlenmem daha iyi değil mi?", "Uzun süre dinlenmek yorgunluğu çoğu zaman artırır. 113 çalışmayı ve 11.525 kişiyi kapsayan bir meta-analizde egzersiz ve psikolojik destek, kansere bağlı yorgunlukta ilaçlardan daha etkili bulundu; araştırmacılar bu yaklaşımları ilk tercih olarak öneriyor. Kısa ve hafif başlayın, yavaş yavaş artırın."),
 ("Lenfödem riskim var, ağırlık kaldırabilir miyim?", "Yavaş yavaş artırılan ağırlık çalışması güvenli görünüyor. Koltuk altından lenf bezi alınmış 154 meme kanseri hastasıyla yapılan bir çalışmada, kontrollü ağırlık programına katılanlarda lenfödem gelişme oranı %11, katılmayanlarda %17 oldu. Başlarken bir fizyoterapist eşliğinde, hafif ağırlıklarla başlayın."),
 ("Hangi egzersizi seçmeliyim?", "En iyisi, yürüyüş gibi aerobik bir egzersizi kas güçlendirme hareketleriyle birleştirmek. Kılavuz haftada üç kez, yaklaşık 30 dakikalık aerobik ve direnç egzersizini öneriyor. Bu hedef size uzak geliyorsa daha kısa sürelerle başlayın; az da olsa hareket, hiç hareket etmemekten iyidir."),
]

CX_SRC = [
 "Campbell KL, Winters-Stone KM, Wiskemann J, et al. " + ext("https://www.sciencedaily.com/releases/2019/10/191016131226.htm", "Exercise guidelines for cancer survivors: consensus statement from international multidisciplinary roundtable") + ". Med Sci Sports Exerc. 2019;51(11):2375-2390.",
 "Mustian KM, Alfano CM, Heckler C, et al. " + ext("https://jamanetwork.com/journals/jamaoncology/fullarticle/2606439", "Comparison of pharmaceutical, psychological, and exercise treatments for cancer-related fatigue: a meta-analysis") + ". JAMA Oncol. 2017;3(7):961-968.",
 "Schmitz KH, Ahmed RL, Troxel AB, et al. " + ext("https://www.nejm.org/doi/full/10.1056/NEJMoa0810118", "Weight lifting in women with breast-cancer-related lymphedema") + ". N Engl J Med. 2009;361(7):664-673.",
 "Schmitz KH, et al. " + ext("https://ecancer.org/en/news/1437-weight-lifting-reduces-risk-of-lymphedema-among-breast-cancer-survivors", "Weight lifting for women at risk for breast cancer-related lymphedema: a randomized trial") + ". JAMA. 2010.",
 "Courneya KS, Vardy JL, O'Callaghan CJ, et al. " + ext("https://www.nejm.org/doi/abs/10.1056/NEJMoa2502760", "Structured exercise after adjuvant chemotherapy for colon cancer") + ". N Engl J Med. 2025.",
]

CX_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Rehabilitasyon rehberi</p>
    <h1>Kanser tedavisi sırasında ve sonrasında egzersiz</h1>
    <p class="lede">Eskiden kanser tedavisi sırasında dinlenmek önerilirdi. Bugün kılavuzlar tersini söylüyor: uygun dozda egzersiz yorgunluğu, kaygıyı ve çökkünlüğü azaltıyor, beden işlevini ve yaşam kalitesini iyileştiriyor. Bazı kanserlerde hastalığın seyrini de olumlu etkileyebiliyor.</p>
    <p class="meta">Son güncelleme: 29 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>3 × 30 dk</b><span>Kılavuzun önerdiği haftalık aerobik ve direnç egzersizi</span></div>
        <div class="stat"><b>113</b><span>Egzersizin kansere bağlı yorgunlukta ilaçlardan daha etkili bulunduğu meta-analizdeki çalışma sayısı</span></div>
        <div class="stat"><b>%28</b><span>Kolon kanseri sonrası egzersiz programıyla kanserin geri dönme, yeni kanser ya da ölüm riskindeki azalma</span></div>
        <div class="stat"><b>%90</b><span>Aynı çalışmada egzersiz grubunda 8 yıllık yaşam oranı (sağlık eğitimi grubunda %83)</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Egzersiz ne sağlar?</h2>
        <p class="soft">2019'da uluslararası uzmanların hazırladığı kılavuza göre kanser tedavisi sırasında ve sonrasında egzersiz yorgunluğu, kaygıyı ve çökkünlüğü azaltıyor, beden işlevini ve yaşam kalitesini iyileştiriyor ve lenfödemi kötüleştirmiyor. Kılavuz, eskiden önerilen haftada 150 dakikadan daha ulaşılabilir bir hedef koyuyor: haftada üç kez, yaklaşık 30 dakikalık aerobik ve direnç egzersizi.</p>
      </div>
      <div>
        <h2>Kansere bağlı yorgunluk</h2>
        <p class="soft">Kanser hastalarının en sık yaşadığı şikâyetlerden biri, dinlenmekle geçmeyen yorgunluk. 113 çalışmayı ve 11.525 kişiyi kapsayan bir meta-analizde egzersiz ve psikolojik destek bu yorgunluğu belirgin şekilde azaltırken ilaçların etkisi çok daha sınırlı kaldı. Araştırmacılar egzersiz ve psikolojik desteği ilk tercih olarak öneriyor.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Egzersiz tedavinin bir parçası olabilir mi?</h2>
      <p class="soft">6 ülkede, kemoterapisini tamamlamış 889 kolon kanseri hastasıyla yapılan CHALLENGE çalışmasında 3 yıllık, antrenör destekli egzersiz programına katılanlarda kanserin geri dönme, yeni kanser ya da ölüm riski %28, ölüm riski %37 daha düşüktü. Egzersizin bazı kanserlerde tedavinin bir parçası olabileceğini gösteren ilk büyük randomize çalışma bu.</p>
      <div class="callout">
        <p>Lenfödem riski olanlar için de iyi haber var: koltuk altından lenf bezi alınmış 154 meme kanseri hastasıyla yapılan bir çalışmada, yavaş yavaş artırılan ağırlık programı lenfödem riskini artırmadı; program grubunda lenfödem gelişme oranı %11, diğer grupta %17 oldu.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Güvenle egzersiz yapmak</h2>
        <p class="soft">Egzersiz programına başlamadan önce tedavi ekibinizle konuşun. Tedavinize, ameliyatınıza ve genel durumunuza göre bazı uyarlamalar gerekebilir.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Ateş, enfeksiyon ya da çok düşük kan değerleri varsa egzersize ara verin.</li>
        <li>Kemiğe yayılım varsa zıplama ve darbe içeren hareketlerden kaçının, program için uzman desteği alın.</li>
        <li>Ellerde ya da ayaklarda uyuşma varsa denge hareketlerinde desteğe tutunun.</li>
        <li>Ameliyattan sonra cerrahınızın önerdiği süre ve kısıtlamalara uyun.</li>
        <li>Kötü günlerde hiç yapmamak yerine süreyi ve yoğunluğu azaltın.</li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Güç için altı egzersiz</h2>
      <p class="soft">Bu hareketleri haftada iki üç gün, yürüyüş gibi aerobik bir egzersizle birlikte yapabilirsiniz. Hafif başlayın; bir hareketi 12 kez rahatça yapabildiğinizde tekrar ya da set sayısını artırın.</p>
      {ex_grid(["cx_sts", "cx_row", "cx_bridge", "cx_heel", "cx_wall", "cx_scap"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(CX_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman egzersizi bırakıp başvurmalı?</h2>
      <p class="soft">Egzersiz sırasında ya da sonrasında şunlar olursa durun ve tedavi ekibinize başvurun:</p>
      <ul class="dots redflags">
        <li>Göğüs ağrısı, alışılmadık nefes darlığı ya da bayılacak gibi olma (<strong>112</strong>)</li>
        <li>Yeni başlayan ya da artan kemik ağrısı</li>
        <li>Baldırda şişlik, ağrı ve kızarıklık</li>
        <li>Ateş ya da titreme</li>
        <li>Kolda ya da bacakta yeni başlayan şişlik veya ağırlık hissi</li>
      </ul>
      {CTA_CARD("Kanser tedavisi sırasında ya da sonrasında egzersiz", "kanser tedavisi sırasında ve sonrasında egzersiz")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(CX_SRC)}
    </div>
  </section>
</main>'''

page("kanser-egzersiz.html", "Kanser Tedavisi Sırasında ve Sonrasında Egzersiz",
     "Kanser tedavisi sırasında egzersiz güvenli mi, yorgunluğa iyi gelir mi, lenfödem riski varken ağırlık kaldırılır mı? Kılavuz önerileri, güncel çalışmalar ve evde altı egzersiz.",
     "kanser-egzersiz.html", NECK_CSS, CX_BODY, "",
     seo_title="Kanser Tedavisi Sırasında ve Sonrasında Egzersiz | İhsan Eren",
     about={"@type": "Thing", "name": "Kanser tedavisi sırasında ve sonrasında egzersiz"}, faq_items=CX_FAQ)

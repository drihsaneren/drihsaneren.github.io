# -*- coding: utf-8 -*-
# Yeni rehber (22): kuyruk sokumu ağrısı (koksidini). cond21_part.py'den sonra exec edilir. Video yok.
# Üslup notu (kullanıcı, 11 Ekim 2026): karar cümlelerinde emir kipi yerine "-ebilirsiniz".

_ex2("cx_pflie", "pf_lie", "Yatarak pelvik taban çalışması", "Sırtüstü yatın, dizleriniz bükülü olsun. İdrarınızı tutuyormuş gibi pelvik taban kaslarınızı içe ve yukarı doğru hafifçe çekin, 5 saniye tutun, sonra tamamen gevşetin. Kalçanızı ve karnınızı sıkmamaya çalışın.", "10 tekrar, günde 2–3 kez")
_ex2("cx_pfsit", "pf_sit", "Oturarak pelvik taban çalışması", "Rahat ettiğiniz bir minderle ya da sandalyenin ön kısmına dik oturun. Aynı kasılmayı oturarak yapın ve tamamen gevşetin.", "10 tekrar, günde 2 kez")
_ex2("cx_ptilt", "ptilt", "Pelvis tilti", "Sırtüstü yatın, dizleriniz bükülü. Belinizi yere doğru hafifçe bastırıp bırakın; hareket küçük ve ağrısız olsun.", "10 tekrar")
_ex2("cx_k2c", "k2c", "Dizi göğse çekme", "Sırtüstü yatın. Bir dizinizi iki elinizle yavaşça göğsünüze çekin, 20 saniye tutun; sonra diğer bacakla yapın. Kalçanızın ve belinizin gevşediğini hissedin.", "Her bacakla 20 saniye, 3 tekrar")
_ex2("cx_cat", "cat", "Kedi-deve", "Ellerinizin ve dizlerinizin üzerinde durun. Nefes verirken sırtınızı yukarı yuvarlayın, nefes alırken belinizi yavaşça aşağı bırakın. Hareketi rahat bir aralıkta yapın.", "8–10 tekrar")
_ex2("cx_walk", "walk", "Kısa yürüyüş molaları", "Uzun süre oturmak ağrıyı artırabileceği için her 30–45 dakikada bir kalkıp birkaç dakika yürüyebilirsiniz.", "Gün içinde sık sık")

CX_FAQ = [
 ("Kuyruk sokumu ağrısı ne kadar sürer?", "Ağrı çoğu zaman birkaç haftada azalır, ancak bazen daha uzun sürebilir. Uzun süredir devam eden ağrısı olan hastaların izlendiği bir çalışmada, kişilerin yarısından fazlasında 3 yıl sonra da belirgin yakınma sürüyordu. Bu yüzden geçmeyen ağrıda erken değerlendirme yararlı olabilir."),
 ("Nasıl bir minder kullanmalıyım?", "Kuyruk sokumu için özel tasarlanmış minderler otururken baskıyı azaltabilir. Kuyruk sokumunu boşta bırakan farklı biçimleri var; size en rahat geleni deneyerek seçebilirsiniz."),
 ("Kortizon iğnesi yaptırmalı mıyım?", "Ev önlemleri ve fizyoterapiye rağmen geçmeyen ağrıda, kuyruk sokumunun eklemine ya da çevresindeki sinir düğümüne (ganglion impar) yapılan enjeksiyonlar seçenekler arasında yer alır ve çalışmalarda ağrıyı azalttığı görülmüştür. Bu kararı, ağrınızın süresini ve şiddetini göz önüne alarak hekiminizle birlikte verebilirsiniz."),
 ("Ameliyat gerekir mi?", "Nadiren. Ameliyat (kuyruk sokumunun bir kısmının ya da tamamının alınması), diğer tedavilerin işe yaramadığı durumlarda gündeme gelir. Bir çalışmada ameliyat olanların yaklaşık %70'inde 2 yılda anlamlı düzelme görüldü; yara sorunları ise ameliyatın bilinen riskleri arasında."),
]

CX_SRC = [
 "NHS. " + ext("https://www.nhs.uk/conditions/tailbone-coccyx-pain/", "Tailbone (coccyx) pain") + ". Page last reviewed 20 November 2025.",
 "Patel R, Appannagari A, Whang PG. " + ext("https://link.springer.com/article/10.1007/s12178-008-9028-1", "Coccydynia") + ". Curr Rev Musculoskelet Med. 2008;1(3–4):223–226.",
 "Mazzoleni MG, Maffulli N, Bardazzi T, Memminger M, Bertini FA, Migliorini F. " + ext("https://aoj.amegroups.org/article/view/9061/html", "Management of coccygodynia: talking points from a systematic review of recent clinical trials") + ". Ann Joint. 2025;10:9.",
]

CX_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Kuyruk sokumu ağrısı (koksidini)</h1>
    <p class="lede">Kuyruk sokumu ağrısı, omurganın en alt ucunda, kalçaların hemen üstünde hissedilen ağrıdır. Oturunca, otururken ayağa kalkınca ve öne eğilince artar. Çoğu zaman düşme, doğum ya da uzun süre oturmayla ilişkilidir ve büyük çoğunluğu ameliyatsız yöntemlerle düzelir.</p>
    <p class="meta">Son güncelleme: 11 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>5 kat</b><span>Kadınlarda erkeklere göre daha sık görülür; ortalama başlangıç yaşı 40</span></div>
        <div class="stat"><b>%70'e kadar</b><span>Oturarak ve ayakta çekilen röntgenlerde kuyruk sokumunun hareketinde bozukluk görülen hasta oranı</span></div>
        <div class="stat"><b>~%90</b><span>Kaynaklara göre ameliyatsız tedaviyle düzelen hastaların oranı</span></div>
        <div class="stat"><b>16 çalışma</b><span>Tedavileri inceleyen 2025 tarihli sistematik derleme; 858 hasta</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Omurganın en alt ucunda, kalçaların üstünde ağrı ve hassasiyet</li>
          <li>Genellikle künt, zaman zaman keskin ağrı</li>
          <li>Otururken ve oturup kalkarken artma</li>
          <li>Öne eğilirken ya da tuvalette artma</li>
          <li>Uyumayı ve günlük işleri zorlaştırabilir</li>
          <li>Tek kalçanın ya da bacakların üzerine oturunca rahatlama</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Kuyruk sokumu üzerine düşme</li>
          <li>Gebelik ve doğum</li>
          <li>Araba ya da bisiklette olduğu gibi uzun süre oturma</li>
          <li>Kötü oturuş alışkanlıkları</li>
          <li>Fazla kilo ya da çok zayıf olma (fazla kilo, kuyruk sokumu ağrısı olanlarda 3 kat daha sık)</li>
          <li>Eklemlerin aşırı esnek ya da kuyruk sokumu ekleminin kısıtlı olması</li>
          <li>Bazen belirgin bir neden bulunmaz</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Kendiniz neler yapabilirsiniz?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Oturuşu düzenleyin</h3><p>Beliniz destekli, dik oturabilir ve uzun süre oturmaktan kaçınabilirsiniz.</p></div>
        <div class="kind"><span class="n">2</span><h3>Özel minder</h3><p>Kuyruk sokumu için tasarlanmış bir minder otururken baskıyı azaltabilir. Yatarken yan yatmak da rahatlatır.</p></div>
        <div class="kind"><span class="n">3</span><h3>Sıcak ya da soğuk</h3><p>Havluya sarılı buz torbasını 20–30 dakika uygulayabilir ya da sıcak uygulamayı daha uzun süre kullanabilirsiniz.</p></div>
        <div class="kind"><span class="n">4</span><h3>Kabızlığı önleyin</h3><p>Ağrı tuvalette artıyorsa dışkıyı yumuşatan önlemler işe yarar; eczacınıza danışabilirsiniz. Ağrı kesiciler de kısa süreli rahatlama sağlayabilir.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tanı nasıl konur?</h2>
      <p class="soft">Tanı muayeneyle konur; kıl dönmesi (pilonidal kist) gibi bölgedeki başka sorunlar da ayırt edilir. Tek pozisyonda çekilen röntgen çoğu zaman yol göstermez. Oturarak ve ayakta çekilen (dinamik) röntgenler, hastaların %70'ine kadarında kuyruk sokumunun aşırı hareketli, kaymış ya da hareketsiz olduğunu gösterir; normalde kuyruk sokumu otururken 5 ile 25 derece arasında hareket eder. Gerekirse MR çekilebilir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi seçenekleri</h2>
      <p class="soft">2025'te yayımlanan sistematik derleme, 16 çalışmada 858 hastayı inceledi. Önerilen yol, önce ameliyatsız yöntemleri denemek ve gerekirse adım adım ilerlemek. Yeni başlayan (2 aydan kısa süren) ağrıda ilk adım, en az 8 hafta boyunca kuyruk sokumunu yükten korumak, oturuşu düzenlemek, kabızlığı önlemek ve ağrı kesici kullanmaktır; 2 aydan uzun süren ağrıda dinamik röntgen ve MR ile ayrıntılı değerlendirme yapılabilir.</p>
      <ul class="tx">
        <li><b>Fizyoterapi</b><span>Kuyruk sokumu çevresindeki kaslara yönelik elle tedavi, pelvik taban çalışmaları ve egzersiz. Elle yapılan uygulamanın etkisi çalışmalarda hafif düzeyde bulundu; bantlama ile egzersizin birlikte kullanıldığı bir çalışmada ağrı ve işlev 1 ayda düzeldi.</span></li>
        <li><b>Şok dalga tedavisi (ESWT)</b><span>Birkaç küçük randomize çalışmada ağrıyı azalttı; bir çalışmada etkisi kortizon iğnesinden daha uzun sürdü. Umut verici, ancak daha büyük çalışmalara ihtiyaç var.</span></li>
        <li><b>Enjeksiyonlar</b><span>Kortizonlu iğne ya da kuyruk sokumunun önündeki sinir düğümüne (ganglion impar) yapılan blok, geçmeyen ağrıda seçenekler arasındadır. Eski bir çalışmada iğne tek başına hastaların %59'unda, kuyruk sokumuna elle yapılan uygulamayla birlikte %85'inde başarılı oldu.</span></li>
        <li><b>Radyofrekans</b><span>Sinirlerin ısıyla uyuşturulması; şimdilik az ve düşük kaliteli çalışma var.</span></li>
        <li><b>Ameliyat</b><span>Diğer yöntemler işe yaramadığında, kuyruk sokumunun bir kısmı ya da tamamı alınabilir. Yayımlanan başarı oranları %60 ile %91 arasında; en iyi sonuç, kuyruk sokumu aşırı hareketli ya da kaymış olanlarda alınıyor. En sık sorun yara enfeksiyonu (%22'ye kadar).</span></li>
      </ul>
      <div class="callout">
        <p>Uzun süredir devam eden ağrısı olan hastaların izlendiği bir çalışmada, yarıdan fazlasında 3 yıl sonra da belirgin yakınma sürüyordu. Birkaç haftada düzelmeyen ağrıda bir hekime ya da fizyoterapiste başvurmak, doğru tedaviye erken başlamanıza yardımcı olabilir.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Kuyruk sokumunu rahatlatan altı hareket</h2>
      <p class="soft">Pelvik taban kaslarını çalıştıran ve kalça ile beli gevşeten hareketler. Yavaş ve ağrısız bir aralıkta yapın; bir hareket ağrınızı belirgin biçimde artırıyorsa onu atlayabilirsiniz.</p>
      {ex_grid(["cx_pflie", "cx_pfsit", "cx_ptilt", "cx_k2c", "cx_cat", "cx_walk"])}
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
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Birkaç haftalık ev önlemlerine rağmen ağrı düzelmiyorsa</li>
        <li>Ağrı günlük işlerinizi engelliyorsa</li>
        <li>Kuyruk sokumu ağrısıyla birlikte ateşiniz ve karnınızda ya da belinizde de ağrı varsa</li>
      </ul>
      {CTA_CARD("Kuyruk sokumu ağrınız", "kuyruk sokumu ağrısı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(CX_SRC)}
    </div>
  </section>
</main>'''

page("kuyruk-sokumu-agrisi.html", "Kuyruk Sokumu Ağrısı (Koksidini)",
     "Kuyruk sokumu ağrısı neden olur, ne kadar sürer? Belirtiler, evde alınabilecek önlemler, minder seçimi, fizyoterapi, şok dalga, iğne ve ameliyat için kanıt ve altı egzersiz.",
     "kuyruk-sokumu-agrisi.html", NECK_CSS, CX_BODY, "",
     seo_title="Kuyruk Sokumu Ağrısı (Koksidini): Nedenleri, Minder, Tedavi ve Egzersiz | İhsan Eren",
     condition="Koksidini (kuyruk sokumu ağrısı)", faq_items=CX_FAQ)

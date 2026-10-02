# -*- coding: utf-8 -*-
# Yeni hastalık rehberleri (2): diz önü ağrısı, aşil tendinopatisi, baş ağrısı, skolyoz.
# cond2_part.py'den sonra exec edilir (_ex2 orada tanımlı).

# ---- yeni çizimler -----------------------------------------------------------------
STEP = '<path class="obj" d="M52 96 H94 V112"/>'
FACE_R = '<path d="M63 25 L68 28 L63 30 Z" fill="#2A6F6B"/>'

def _heeldrop(bent, caption):
    if bent:
        body = ('<path class="fig" d="M50 64 L53 36 M53 42 L74 50 L98 48"/>'
                '<path class="fig hl" d="M50 64 L60 80 L49 92"/>'
                '<circle class="hd" cx="56" cy="27" r="8"/><path d="M63 25 L68 28 L63 30 Z" fill="#2A6F6B"/>')
    else:
        body = ('<path class="fig" d="M52 60 L54 30 M54 36 L76 44 L98 44"/>'
                '<path class="fig hl" d="M52 60 L51 78 L49 92"/>'
                '<circle class="hd" cx="56" cy="21" r="8"/><path d="M63 19 L68 22 L63 24 Z" fill="#2A6F6B"/>')
    return fig(GRD + STEP + '<path class="obj" d="M104 10 V112" stroke-width="5"/>' +
        '<g transform="translate(0 0)"><animateTransform attributeName="transform" type="translate" '
        'values="3 -8;0 0;3 -8" keyTimes="0;0.75;1" dur="4s" repeatCount="indefinite" calcMode="spline" '
        f'keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>{body}</g>'
        '<path class="fig" d="M42 99 L62 96"><animate attributeName="d" values="M53 83 L62 96;M42 99 L62 96;M53 83 L62 96" '
        'keyTimes="0;0.75;1" dur="4s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/></path>'
        '<path d="M34 84 V100 M30 96 L34 100 L38 96" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round">'
        '<animate attributeName="opacity" values="0;1;0" dur="4s" repeatCount="indefinite"/></path>',
        caption)

SV["heeldrop"] = _heeldrop(False, "Basamaktan topuk indirme")
SV["heeldropb"] = _heeldrop(True, "Diz bükülü topuk indirme")

SV["adams"] = fig(GRD +
    '<path class="fig" d="M40 62 L38 112 M40 62 L46 112"/>'
    '<path class="fig hl" d="M40 62 Q58 48 76 66"/>'
    '<path class="fig" d="M74 68 L74 96"/><circle class="hd" cx="85" cy="74" r="8"/>'
    '<path d="M48 44 Q58 36 68 44" stroke="#C8963E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-dasharray="3 4">'
    '<animate attributeName="opacity" values="0.2;1;0.2" dur="2.4s" repeatCount="indefinite"/></path>'
    '<path d="M8 30 Q17 22 26 30 Q17 38 8 30 Z" fill="none" stroke="#2A6F6B" stroke-width="2.2"/><circle cx="17" cy="30" r="2.6" fill="#2A6F6B"/>'
    '<path d="M28 32 L46 46" stroke="#B9CBC6" stroke-width="2" stroke-dasharray="2 3"/>',
    "Öne eğilme testi")

# ============================================================== DİZ ÖNÜ AĞRISI
_ex2("pf_abd", "abd", "Yan yatarak bacak kaldırma", "Yan yatın, alttaki dizinizi hafifçe bükün. Üstteki bacağınızı dizi düz, ayak ucu öne bakacak şekilde yukarı kaldırın, 2 saniye tutup yavaşça indirin. Kalçanın yan kasları dizi dengede tutmaya yardım eder.", "Her iki yana 10–15 tekrar, 2–3 set")
_ex2("pf_bridge", "bridge", "Köprü", "Sırtüstü yatın, dizleriniz bükülü, ayaklarınız yerde. Kalçanızı sıkarak yavaşça kaldırın, 3 saniye bekleyip indirin. Kolaylaştıkça tek bacakla deneyin.", "10–15 tekrar, 2–3 set")
_ex2("pf_wall", "wall", "Duvarda yarım çömelme", "Sırtınızı duvara dayayın, ayaklarınız duvardan bir adım önde olsun. Dizleriniz ayak parmaklarınızın hizasında kalacak şekilde, ağrıyı belirgin artırmayan bir derinliğe kadar inin, birkaç saniye bekleyip yukarı çıkın.", "8–10 tekrar, 2–3 set")
_ex2("pf_kext", "kext", "Oturarak diz açma", "Sandalyeye dik oturun. Dizinizi yavaşça düzeltip uyluğunuzun ön kasını sıkın, 3 saniye tutun ve yavaşça indirin. Ağrı olursa hareketi daha kısa bir açıklıkta yapın.", "10–15 tekrar, 2–3 set")
_ex2("pf_sabd", "sabd", "Ayakta kalçayı yana açma", "Tezgâha tutunarak dik durun. Bir bacağınızı dizi düz, ayak ucu öne bakacak şekilde yana doğru açın ve yavaşça indirin. Gövdenizi yana eğmeyin. Kolaylaştıkça ayak bileğinize lastik bant ekleyin.", "Her iki yana 10–15 tekrar")
_ex2("pf_sls", "sls", "Tek ayak üzerinde denge", "Tezgâha hafifçe tutunarak tek ayağınızın üzerinde durun, dizinizi hafifçe bükülü tutun ve içe kaçmamasına dikkat edin. Kolaylaştıkça tutunmayı azaltın.", "30 saniye, her bacakta 3 kez")

PF_FAQ = [
 ("Diz kapağımdan ses geliyor, zarar mı veriyor?", "Çoğu zaman hayır. Ağrısız çıtırtılar diz ağrısı olmayan pek çok kişide de vardır ve tek başına bir hastalık belirtisi değildir. Sesle birlikte ağrı ya da şişlik varsa değerlendirme yapılmalıdır."),
 ("Koşmayı bırakmalı mıyım?", "Genellikle tamamen bırakmak gerekmez. Ağrıyı belirgin artırmayan bir mesafe ve hızda devam edip egzersizlerle birlikte yükü kademeli olarak artırabilirsiniz. Yokuş aşağı koşuyu ve merdiven antrenmanlarını bir süre azaltın."),
 ("Dizlik ya da bant işe yarar mı?", "Bazı kişilerde ağrıyı kısa sürede hafifletebilir; ancak uluslararası uzlaşı raporuna göre bu konudaki kanıt yetersizdir. Egzersizin yerine değil, gerekirse yanında kullanılmalıdır."),
 ("MR çektirmem gerekiyor mu?", "Genellikle hayır. Tanı muayeneyle konur ve görüntülemede çoğu zaman ağrıyı açıklayan bir bulgu çıkmaz. Yaralanma sonrası başlayan ağrı, kilitlenme ya da belirgin şişlik gibi durumlarda görüntüleme gerekebilir."),
]

PF_SRC = [
 "Collins NJ, Barton CJ, van Middelkoop M, et al. " + ext("https://pure.eur.nl/en/publications/2018-consensus-statement-on-exercise-therapy-and-physical-interve/", "2018 Consensus statement on exercise therapy and physical interventions (orthoses, taping and manual therapy) to treat patellofemoral pain: recommendations from the 5th International Patellofemoral Pain Research Retreat, Gold Coast, Australia, 2017") + ". Br J Sports Med. 2018;52(18):1170-1178.",
 "Smith BE, Selfe J, Thacker D, et al. " + ext("https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0190892", "Incidence and prevalence of patellofemoral pain: a systematic review and meta-analysis") + ". PLoS One. 2018;13(1):e0190892.",
 "Lankhorst NE, van Middelkoop M, Crossley KM, et al. " + ext("https://repub.eur.nl/pub/97015", "Factors that predict a poor outcome 5-8 years after the diagnosis of patellofemoral pain: a multicentre observational analysis") + ". Br J Sports Med. 2016;50(14):881-886.",
]

PF_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Diz önü ağrısı (patellofemoral ağrı)</h1>
    <p class="lede">Diz kapağının çevresinde ya da arkasında hissedilen, çömelirken, merdiven inerken ve uzun süre dizler bükülü otururken artan ağrıdır. Özellikle gençlerde, koşucularda ve sporcularda sık görülür. Tedavinin temeli, kalça ve diz kaslarını birlikte güçlendiren egzersizlerdir.</p>
    <p class="meta">Son güncelleme: 30 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%22,7</b><span>Toplumda bir yıl içinde diz önü ağrısı yaşayanların oranı</span></div>
        <div class="stat"><b>%28,9</b><span>Ergenlerde bir yıl içindeki görülme sıklığı</span></div>
        <div class="stat"><b>%57</b><span>Tanıdan 5–8 yıl sonra ulaşılabilen hastalarda iyileşmediğini bildirenler</span></div>
        <div class="stat"><b>Kalça + diz</b><span>Uluslararası uzlaşı raporunun önerdiği egzersiz birlikteliği</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Diz kapağı, uyluk kemiğinin ön yüzündeki bir olukta kayar. Bu eklemin taşıdığı yük, dokuların kaldırabileceği düzeyi aştığında ağrı ortaya çıkar. Görüntülemede çoğu zaman belirgin bir hasar görülmez; sorun yapısal bir bozukluktan çok yük ile dayanıklılık arasındaki dengesizliktir.</p>
        <p class="soft">Koşu, zıplama ya da merdiven gibi aktivitelerin kısa sürede artırılması, kalça ve uyluk kaslarındaki zayıflık ve büyüme dönemi sık görülen etkenlerdir.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Diz kapağının çevresinde ya da arkasında, yaygın ve sızlayıcı ağrı</li>
          <li>Merdiven inerken, çömelirken, yokuş aşağı yürürken ya da koşarken artış</li>
          <li>Uzun süre dizler bükülü oturunca, örneğin sinemada ya da araba yolculuğunda ağrı</li>
          <li>Diz kapağında çıtırtı ya da sürtünme hissi</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavide ne işe yarar?</h2>
      <p class="soft">2018'de uluslararası araştırmacıların hazırladığı uzlaşı raporu egzersiz tedavisini, özellikle kalça ve diz egzersizlerinin birlikte yapılmasını öneriyor. Egzersizin başka yöntemlerle birleştirilmesi ve ayak tabanlıkları da önerilenler arasında. Buna karşılık dize ya da bele tek başına uygulanan mobilizasyonlar ve elektroterapi yöntemleri önerilmiyor; bantlama, dizlik, kuru iğneleme ve koşu tekniğinin değiştirilmesi konusunda ise kanıt yetersiz.</p>
      <div class="callout">
        <p>Diz önü ağrısı kendiliğinden her zaman geçmeyebilir. Hollanda'da yapılan bir izlem çalışmasında tanıdan 5–8 yıl sonra ulaşılabilen hastaların %57'si iyileşmediğini bildirdi; ağrının başlangıçta 12 aydan uzun süredir devam ediyor olması kötü sonucun en güçlü göstergesiydi. Bu yüzden erken ve düzenli tedavi önemli.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <ul class="tx">
        <li><b>Kalça ve diz egzersizleri</b><span>Kalçanın yan ve arka kaslarıyla uyluğun ön kasını güçlendiren, dizin içe kaçmasını önleyen egzersizler tedavinin temelidir.</span></li>
        <li><b>Yükü ayarlama</b><span>Ağrıyı belirgin artıran koşu, zıplama, derin çömelme ve merdiven yükü bir süre azaltılır, sonra kademeli olarak artırılır.</span></li>
        <li><b>Ayak tabanlığı</b><span>Bazı kişilerde, özellikle kısa vadede ağrıyı azaltmaya yardımcı olabilir.</span></li>
        <li><b>Bantlama ve dizlik</b><span>Ağrıyı geçici olarak hafifletebilir; kanıt sınırlıdır, egzersizin yerine geçmez.</span></li>
        <li><b>Bilgilendirme</b><span>Ağrının neden olduğunu ve yükün nasıl ayarlanacağını bilmek, tedavinin başarısını artırır.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Kalça ve diz için altı egzersiz</h2>
      <p class="soft">Egzersiz sırasında hafif ve katlanılabilir bir ağrı kabul edilebilir; ağrı ertesi gün artmıyorsa devam edin. Dizinizin ayak parmaklarınızla aynı hizada kalmasına, içe doğru kaçmamasına dikkat edin.</p>
      {ex_grid(["pf_abd", "pf_bridge", "pf_wall", "pf_kext", "pf_sabd", "pf_sls"])}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Diz kapağı ağrısı için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("BeeHf7yD0Q0", "Diz kapağı güçlendirme videosunu oynat", "Strengthening Exercises To Help Stop Kneecap Pain (Patellofemoral Pain Syndrome)")}
          <h3>Diz kapağı ağrısı için güçlendirme</h3>
          <p>Diz kapağı çevresindeki yükü azaltmaya yönelik güçlendirme egzersizleri.</p>
        </div>
        <div class="vid">
          {vbox("rXqTKxL60GE", "Diz kapağı germe videosunu oynat", "The 5 Stretches You Should Do for Kneecap Pain (Patellofemoral Pain Syndrome)")}
          <h3>Diz kapağı ağrısı için beş germe</h3>
          <p>Uyluk, kalça ve baldır kaslarına yönelik germe hareketleri.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(PF_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlar diz önü ağrısı dışında bir soruna işaret edebilir. Beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Dizde belirgin şişlik, kızarıklık, sıcaklık ya da ateş</li>
        <li>Yaralanmadan sonra dizin boşalması, kilitlenmesi ya da bacağa yük verememe</li>
        <li>Dinlenmekle geçmeyen, geceleri uyandıran ağrı</li>
        <li>Çocuk ve ergenlerde topallamayla birlikte diz ağrısı (ağrı kalçadan kaynaklanıyor olabilir)</li>
      </ul>
      {CTA_CARD("Diz önü ağrınız", "diz önü ağrısı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(PF_SRC)}
    </div>
  </section>
</main>'''

page("diz-onu-agrisi.html", "Diz Önü Ağrısı",
     "Diz kapağı çevresinde merdiven inerken ve çömelirken artan ağrı: patellofemoral ağrı nedir, neden olur, nasıl tedavi edilir? Evde altı egzersiz ve videolar.",
     "diz-onu-agrisi.html", NECK_CSS, PF_BODY, YT_JS,
     seo_title="Diz Önü Ağrısı (Patellofemoral Ağrı): Nedenleri ve Egzersizler | İhsan Eren",
     condition="Patellofemoral ağrı sendromu", faq_items=PF_FAQ)

# ============================================================== AŞİL TENDİNOPATİSİ
_ex2("ac_heel", "heel2", "İki ayakla topuk yükseltme", "Tezgâha hafifçe tutunun. İki topuğunuzu birlikte kaldırıp parmak uçlarınızda yükselin, yukarıda bir an bekleyip 3 saniyede yavaşça inin.", "15 tekrar, 3 set, günde 1 kez")
_ex2("ac_heel1", "heel3", "Tek ayakla topuk yükseltme", "İki ayakla kolaylaştığında aynı hareketi ağrılı taraftaki ayağınızın üzerinde yapın. Kolaylaştıkça sırt çantasına ağırlık koyarak yükü artırabilirsiniz.", "10–15 tekrar, 3 set, günde 1 kez")
EXT["heeldrop"] = ("Basamaktan topuk indirme (diz düz)", "Ayağınızın ön kısmıyla bir basamağın kenarına basın, duvara ya da tırabzana tutunun. İki ayakla parmak uçlarınıza yükselin, sonra ağırlığınızı ağrılı bacağa verip topuğunuzu 3 saniyede basamak seviyesinin altına kadar yavaşça indirin. Yukarı iki ayakla çıkın.", "15 tekrar, 3 set, günde 2 kez, 12 hafta")
EXT["heeldropb"] = ("Basamaktan topuk indirme (diz bükülü)", "Aynı hareketi dizinizi hafifçe bükerek yapın. Bu şekilde baldırın derin kası (soleus) daha çok çalışır.", "15 tekrar, 3 set, günde 2 kez, 12 hafta")
_ex2("ac_calf", "calf", "Duvarda baldır germe", "Ellerinizi duvara dayayın, ağrılı bacağınızı arkaya alın. Arkadaki dizinizi düz, topuğunuzu yerde tutarak kalçanızı duvara doğru ilerletin; baldırınızda hafif bir gerilme hissedin.", "30 saniye, 3 tekrar")
_ex2("ac_sls", "sls", "Tek ayak üzerinde denge", "Tezgâha hafifçe tutunarak ağrılı taraftaki ayağınızın üzerinde durun. Kolaylaştıkça tutunmayı azaltın ya da gözlerinizi kısa süre kapatın.", "30 saniye, 3 kez")

AC_FAQ = [
 ("Koşmaya devam edebilir miyim?", "Çoğu zaman evet, ama yükü azaltarak. Koşu sırasındaki ağrı hafif düzeyde kalıyor ve ertesi sabah artmıyorsa devam edebilirsiniz. Yokuş, tempo ve hız antrenmanlarını bir süre azaltın."),
 ("Ne kadar sürede iyileşir?", "Sabır gerektirir. Çalışmalarda egzersiz programları 12 hafta sürdü ve kazanımlar 1 yıl sonra da korundu. Bazı kişilerde tam iyileşme birkaç ay daha sürebilir."),
 ("Kortizon iğnesi yaptırmalı mıyım?", "Aşil kirişine kortizon iğnesi, kirişi zayıflatıp yırtılma riskini artırabileceği için genellikle önerilmez. Önce düzenli yüklenme egzersizlerinin denenmesi gerekir."),
 ("Germe egzersizleri yeterli mi?", "Tek başına genellikle yeterli değildir. Kirişin iyileşmesi için asıl gereken, kademeli olarak artırılan yüklenme egzersizleridir; germe hareketleri bunlara eklenebilir."),
]

AC_SRC = [
 "Martin RL, Chimenti R, Cuddeford T, et al. " + ext("https://www.jospt.org/doi/10.2519/jospt.2018.0302", "Achilles pain, stiffness, and muscle power deficits: midportion Achilles tendinopathy revision 2018") + ". J Orthop Sports Phys Ther. 2018;48(5):A1-A38.",
 "Beyer R, Kongsgaard M, Hougs Kjær B, et al. " + ext("https://journals.sagepub.com/doi/abs/10.1177/0363546515584760", "Heavy slow resistance versus eccentric training as treatment for Achilles tendinopathy: a randomized controlled trial") + ". Am J Sports Med. 2015;43(7):1704-1711.",
 "Alfredson H, Pietilä T, Jonsson P, Lorentzon R. " + ext("https://journals.sagepub.com/doi/10.1177/03635465980260030301", "Heavy-load eccentric calf muscle training for the treatment of chronic Achilles tendinosis") + ". Am J Sports Med. 1998;26(3):360-366.",
]

AC_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Aşil tendinopatisi</h1>
    <p class="lede">Topuğun hemen üstünde, aşil kirişinde ağrı, sabah tutukluğu ve kalınlaşmayla kendini gösterir. Özellikle koşucularda ve orta yaşta sık görülür. Sorun iltihaptan çok kirişin aşırı yüke uyum sağlayamamasıdır; tedavinin temeli kademeli olarak artırılan yüklenme egzersizleridir.</p>
    <p class="meta">Son güncelleme: 30 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>12 hafta</b><span>Etkisi kanıtlanmış yüklenme egzersizi programlarının süresi</span></div>
        <div class="stat"><b>%100</b><span>Ağır ve yavaş direnç egzersizi yapanlarda 12. haftada tedaviden memnun olanlar; eksantrik egzersizde %80</span></div>
        <div class="stat"><b>%92</b><span>Ağır ve yavaş direnç programına uyum; eksantrik programda %78</span></div>
        <div class="stat"><b>1 yıl</b><span>İki programda da kazanımların sürdüğü takip süresi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Aşil kirişi, baldır kaslarını topuk kemiğine bağlayan, vücudun en güçlü kirişidir. Koşu, zıplama ya da yürüyüş yükünün kısa sürede artırılması kirişin uyum kapasitesini aşınca kirişte yıpranma ve ağrı gelişir. Ağrı çoğunlukla kirişin orta bölümündedir; bazen de kirişin topuğa yapıştığı yerde görülür.</p>
        <p class="soft">Koşu mesafesinin ya da hızının hızla artırılması, yokuş antrenmanları, ayakkabı değişikliği, ileri yaş, fazla kilo, diyabet ve florokinolon grubu antibiyotikler risk etkenleri arasındadır.</p>
      </div>
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Topuğun birkaç santim üstünde, kirişte ağrı ve hassasiyet</li>
          <li>Sabah ilk adımlarda ya da uzun süre oturduktan sonra ağrı ve tutukluk</li>
          <li>Aktivitenin başında artan, ısındıkça azalan, sonra yeniden artan ağrı</li>
          <li>Kirişte kalınlaşma ya da şişlik</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Yüklenme egzersizleri neden temel tedavi?</h2>
      <p class="soft">Kirişler, kademeli olarak artırılan yüke uyum sağlayarak güçlenir. Amerikan Fizyoterapi Derneği'nin 2018 kılavuzu da yüklenme egzersizlerini tedavinin temeli olarak öneriyor. Klasik yöntem, İsveçli ortopedist Alfredson'un geliştirdiği eksantrik programdır: 12 hafta boyunca, günde iki kez, basamaktan topuğu yavaşça indirmek.</p>
      <p class="soft">Danimarka'da 58 hastayla yapılan bir çalışmada bu eksantrik program ile haftada üç gün yapılan ağır ve yavaş direnç egzersizleri karşılaştırıldı. İki program da ağrıyı ve işlevi belirgin şekilde iyileştirdi ve kazanımlar 1 yıl sonra da sürdü. Ağır ve yavaş direnç grubunda 12. haftada memnuniyet (%100'e karşı %80) ve programa uyum (%92'ye karşı %78) daha yüksekti.</p>
      <div class="callout">
        <p>Egzersiz sırasında hafif ve katlanılabilir bir ağrı olabilir. Önemli olan ağrının ertesi sabah artmamasıdır; artıyorsa bir sonraki seansta tekrar sayısını ya da yükü azaltın.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi</h2>
      <ul class="tx">
        <li><b>Yüklenme egzersizleri</b><span>Eksantrik ya da ağır ve yavaş direnç egzersizleri; yük, kirişin uyum sağlayabileceği hızda artırılır.</span></li>
        <li><b>Yükü ayarlama</b><span>Koşu mesafesi, hızı ve yokuşlar bir süre azaltılır; tamamen dinlenmek yerine ağrıyı artırmayan aktiviteler sürdürülür.</span></li>
        <li><b>Ayakkabı</b><span>Topuğu biraz yüksek, rahat ayakkabılar ağrılı dönemde kirişin yükünü azaltabilir.</span></li>
        <li><b>Kortizon iğnesi</b><span>Kirişin içine yapılan kortizon iğnesi yırtılma riski nedeniyle genellikle önerilmez.</span></li>
        <li><b>Kademeli dönüş</b><span>Koşu ve zıplama gerektiren sporlara ağrı kontrol altına alındıktan sonra aşamalı olarak dönülür.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Aşil kirişi için altı egzersiz</h2>
      <p class="soft">İki ayakla topuk yükseltmeyle başlayın; kolaylaştıkça tek ayağa ve basamaktan topuk indirmeye geçin. Hareketleri yavaş ve kontrollü yapın.</p>
      {ex_grid(["ac_heel", "ac_heel1", "heeldrop", "heeldropb", "ac_calf", "ac_sls"])}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Aşil tendinopatisi için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("E260D8a28ws", "Aşil tendinopatisi videosunu oynat", "Fix Achilles Tendonitis: Absolute 2 Best Self-Treatments (Updated &amp; Science Based)")}
          <h3>Aşil kirişi için iki temel uygulama</h3>
          <p>Bilimsel kanıtlara dayanan iki temel kendi kendine uygulama.</p>
        </div>
        <div class="vid">
          {vbox("qvfm3Lb3Ojs", "Aşil ağrısı videosunu oynat", "Achilles Tendon Pain Fast Relief In Minutes!")}
          <h3>Aşil ağrısını hafifletmek için</h3>
          <p>Ağrılı dönemde rahatlatmaya yönelik kısa uygulamalar.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(AC_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Ani bir “pat” sesi ya da topuğa tekme yemiş gibi bir his, ardından parmak ucuna kalkamama (kiriş yırtılmış olabilir)</li>
        <li>Topukta kızarıklık, sıcaklık ya da ateş</li>
        <li>Baldırda şişlik, ağrı ve kızarıklık</li>
        <li>Florokinolon grubu bir antibiyotik kullanırken başlayan kiriş ağrısı</li>
        <li>İki taraflı aşil ağrısıyla birlikte eklem ağrıları ya da bel tutukluğu</li>
      </ul>
      {CTA_CARD("Aşil ağrınız", "aşil tendinopatisi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(AC_SRC)}
    </div>
  </section>
</main>'''

page("asil-tendinopatisi.html", "Aşil Tendinopatisi",
     "Topuğun üstünde, aşil kirişinde ağrı ve sabah tutukluğu: aşil tendinopatisi nedir, neden olur, hangi egzersizler iyileştirir? Evde altı egzersiz ve videolar.",
     "asil-tendinopatisi.html", NECK_CSS, AC_BODY, YT_JS,
     seo_title="Aşil Tendinopatisi (Aşil Tendiniti): Tedavi ve Egzersizler | İhsan Eren",
     condition="Aşil tendinopatisi", faq_items=AC_FAQ)

# ============================================================== BAŞ AĞRISI
_ex2("ha_chin", "chin", "Çene içe çekme", "Dik oturun, gözleriniz karşıya baksın. Başınızı eğmeden çenenizi düz bir çizgide geriye çekin; ensenizin uzadığını hissedin. 5 saniye tutup bırakın. Gün içinde sık sık tekrarlayın.", "10 tekrar, günde 2–3 kez")
_ex2("ha_iso", "iso", "İzometrik boyun güçlendirme", "Avucunuzu alnınıza koyun. Başınızı hareket ettirmeden elinize doğru hafifçe itin, eliniz de karşı koysun. Aynısını başınızın arkası ve iki yanı için tekrarlayın. Kuvvetin yarısını kullanmanız yeterli.", "Her yöne 5 saniye, 5 tekrar")
_ex2("ha_scap", "scap", "Kürek kemiği sıkıştırma", "Dik oturun ya da durun. Omuzlarınızı kaldırmadan kürek kemiklerinizi geriye ve aşağıya doğru yaklaştırın, 5 saniye tutup bırakın. Uzun süre masa başında çalışanlar için iyi bir moladır.", "10–15 tekrar, günde 2 kez")
_ex2("ha_thor", "thor", "Göğüs kafesini açma", "Sırtı alçak bir sandalyeye oturun, ellerinizi ensenizde birleştirin. Göğsünüzü tavana doğru kaldırarak sırtınızı hafifçe geriye esnetin. Boynunuzu değil sırtınızı esnetin.", "5–10 tekrar")
_ex2("ha_side", "side", "Boyun yana germe", "Bir elinizle oturduğunuz sandalyenin kenarını tutun. Kulağınızı karşı omzunuza doğru yavaşça yaklaştırın; boynunuzun yanında hafif bir gerginlik hissedin. Omzunuzu kaldırmayın.", "20–30 saniye, her iki yana 2–3 kez")
_ex2("ha_rot", "rot", "Boyun döndürme", "Omuzlarınızı sabit tutun. Başınızı yavaşça sağa çevirin, rahat olan son noktada 2–3 saniye bekleyin, sonra aynı şekilde sola çevirin.", "Her yöne 10 tekrar")

HA_FAQ = [
 ("Baş ağrım için MR ya da tomografi gerekir mi?", "Tipik gerilim tipi ya da boyun kaynaklı baş ağrısında genellikle gerekmez. Aşağıdaki uyarı işaretlerinden biri varsa ya da ağrının özellikleri değiştiyse hekiminiz görüntüleme isteyebilir."),
 ("Ağrı kesiciyi ne sıklıkla kullanabilirim?", "Ara sıra kullanım sorun değildir. Ancak ağrı kesicileri ayda 10–15 günden fazla kullanmak, ilaç aşırı kullanımına bağlı baş ağrısına yol açabilir. Bu kadar sık ihtiyaç duyuyorsanız hekiminize başvurun."),
 ("Boyun egzersizleri migrene iyi gelir mi?", "Migrenin asıl tedavisi hekim tarafından planlanır. Düzenli aerobik egzersiz, uyku düzeni ve stres yönetimi atakları azaltmaya yardım edebilir; migrene boyun ağrısı da eşlik ediyorsa boyun egzersizleri ek fayda sağlayabilir."),
 ("Yastık ve uyku pozisyonu önemli mi?", "Boynunuzu gövdenizle aynı hizada tutan bir yastık, sabah başlayan boyun kaynaklı ağrılarda rahatlatabilir. Yüzüstü yatmak boynu uzun süre döndürdüğü için ağrıyı artırabilir."),
]

HA_SRC = [
 "World Health Organization. " + ext("https://www.who.int/news-room/fact-sheets/detail/headache-disorders", "Migraine and other headache disorders") + ". Fact sheet.",
 "Jull G, Trott P, Potter H, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/12221344/", "A randomized controlled trial of exercise and manipulative therapy for cervicogenic headache") + ". Spine. 2002;27(17):1835-1843.",
 "Headache Classification Committee of the International Headache Society. " + ext("https://ichd-3.org/", "The International Classification of Headache Disorders, 3rd edition") + ". Cephalalgia. 2018;38(1):1-211.",
]

HA_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Baş ağrısı: gerilim tipi ve boyun kaynaklı</h1>
    <p class="lede">Baş ağrısı en sık yaşanan sağlık sorunlarından biridir. En yaygın türü olan gerilim tipi baş ağrısında ve boyundan kaynaklanan baş ağrısında egzersiz, duruş ve boyuna yönelik fizyoterapi ağrının sıklığını azaltabilir. Bazı baş ağrıları ise acil değerlendirme gerektirir.</p>
    <p class="meta">Son güncelleme: 30 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%40</b><span>Dünyada baş ağrısı bozukluğu yaşayan insanların oranı (3,1 milyar kişi, 2021)</span></div>
        <div class="stat"><b>%50</b><span>Gerilim tipi baş ağrısının kadınlarda erkeklere göre daha sık görülme oranı</span></div>
        <div class="stat"><b>200</b><span>Boyun kaynaklı baş ağrısında egzersizin ve manuel terapinin etkisini gösteren çalışmadaki hasta sayısı</span></div>
        <div class="stat"><b>15 gün</b><span>Ayda bu kadar ve daha fazla gün süren baş ağrısı kronik kabul edilir</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Baş ağrınız hangi türde?</h2>
      <ul class="tx">
        <li><b>Gerilim tipi</b><span>Başın iki yanında, bant gibi saran, sıkıştırıcı ya da baskı şeklinde ağrı. Genellikle hafif ya da orta şiddettedir ve günlük hareketlerle artmaz. Stres, uykusuzluk ve uzun süre aynı duruşta kalmak tetikleyebilir.</span></li>
        <li><b>Boyun kaynaklı</b><span>Çoğunlukla tek taraflı; boyundan başlayıp başın arkasına, bazen alna ve göz çevresine yayılır. Boyun hareketleri ya da uzun süre aynı duruşta kalmak ağrıyı başlatabilir; boyun hareketleri kısıtlı olabilir.</span></li>
        <li><b>Migren</b><span>Genellikle tek taraflı, zonklayıcı, orta ya da şiddetli ağrı; bulantı, ışığa ve sese hassasiyet eşlik edebilir ve fiziksel aktiviteyle artar. Tanı ve tedavisini hekim planlar.</span></li>
        <li><b>İlaç aşırı kullanımı</b><span>Ağrı kesicilerin uzun süre ve çok sık kullanılması baş ağrısını kalıcı hale getirebilir. Bu durumda ilaçların hekim eşliğinde azaltılması gerekir.</span></li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Egzersiz ve fizyoterapi ne sağlar?</h2>
      <p class="soft">Avustralya'da boyun kaynaklı baş ağrısı olan 200 kişiyle yapılan bir çalışmada, 6 hafta boyunca uygulanan manuel terapi de, boyun ve kürek kemiği kaslarına yönelik özel egzersizler de baş ağrısının sıklığını ve şiddetini anlamlı şekilde azalttı; etki 12 ay sonra da sürüyordu.</p>
      <p class="soft">Dünya Sağlık Örgütü, baş ağrısı tedavisinde bilgilendirmenin ve düzenli uyku, yeterli sıvı alımı, alkolden kaçınma ve düzenli egzersiz gibi yaşam tarzı değişikliklerinin önemini vurguluyor.</p>
      <div class="callout">
        <p>Uzun süre ekran başında çalışıyorsanız <a href="masa-basi.html">masa başı rehberine</a>, stres baş ağrınızı tetikliyorsa <a href="stres.html">stres rehberine</a> ve uykunuz düzensizse <a href="uyku.html">iyi uyku rehberine</a> göz atın.</p>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Boyun ve duruş için altı egzersiz</h2>
      <p class="soft">Bu egzersizler özellikle gerilim tipi ve boyun kaynaklı baş ağrısında boyun ve omuz kaslarını güçlendirip gevşetmeye yardım eder. Hareketleri yavaş ve ağrısız aralıkta yapın; baş dönmesi ya da kollara yayılan uyuşma olursa bırakın.</p>
      {ex_grid(["ha_chin", "ha_iso", "ha_scap", "ha_thor", "ha_side", "ha_rot"])}
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Boyun kaynaklı baş ağrısı için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("Wsb78V2UYVA", "Temel boyun egzersizi videosunu oynat", "The One Exercise Everyone Should Do For Neck Pain")}
          <h3>Herkesin yapması gereken tek boyun egzersizi</h3>
          <p>Boyun ağrısında en temel egzersizin doğru yapılışı.</p>
        </div>
        <div class="vid">
          {vbox("W8Lk6E6_cgg", "Tutulan boyun videosunu oynat", "Top 6 Exercises For A Stiff Neck")}
          <h3>Tutulan boyun için altı egzersiz</h3>
          <p>Boyun tutulmasında hareketi geri kazanmaya yönelik kısa bir program.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(HA_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda baş ağrısı ciddi bir soruna işaret edebilir. Beklemeden acil servise başvurun ya da <strong>112</strong>'yi arayın:</p>
      <ul class="dots redflags">
        <li>Ani başlayan, hayatınızın en şiddetli baş ağrısı</li>
        <li>Ateş, ense sertliği ya da döküntüyle birlikte baş ağrısı</li>
        <li>Konuşma bozukluğu, güçsüzlük, uyuşma, görme kaybı ya da bilinç değişikliği</li>
        <li>Baş darbesinden sonra başlayan ya da giderek artan baş ağrısı</li>
        <li>50 yaşından sonra ilk kez başlayan ya da giderek kötüleşen baş ağrısı; kanser öyküsü ya da bağışıklığı baskılayan tedavi</li>
        <li>Öksürme, ıkınma ya da eğilmeyle belirgin artan, sabahları kusmayla uyandıran baş ağrısı</li>
      </ul>
      {CTA_CARD("Baş ve boyun ağrınız", "baş ağrısı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(HA_SRC)}
    </div>
  </section>
</main>'''

page("bas-agrisi.html", "Baş Ağrısı",
     "Gerilim tipi ve boyun kaynaklı baş ağrısı: türleri, egzersiz ve fizyoterapinin etkisi, ağrı kesicilerle ilgili uyarılar ve acil başvuru gerektiren belirtiler. Evde altı egzersiz.",
     "bas-agrisi.html", NECK_CSS, HA_BODY, YT_JS,
     seo_title="Baş Ağrısı: Gerilim Tipi ve Boyun Kaynaklı Baş Ağrısında Egzersiz | İhsan Eren",
     about=[cond("Gerilim tipi baş ağrısı"), cond("Servikojenik baş ağrısı")], faq_items=HA_FAQ)

# ============================================================== SKOLYOZ
EXT["adams"] = ("Öne eğilme testi (evde kontrol)", "Çocuğunuz ayakları bitişik, dizleri düz şekilde öne eğilsin, kolları serbestçe sarksın. Arkasından bakarak sırtın iki yanının aynı yükseklikte olup olmadığını kontrol edin. Bir tarafta belirgin bir kabarıklık varsa bir uzmana başvurun.", "Büyüme döneminde birkaç ayda bir")
_ex2("sc_bird", "birddog", "Kuş-köpek", "Ellerinizin ve dizlerinizin üzerinde, sırtınız düz durun. Bir kolunuzu öne, karşı bacağınızı arkaya uzatın; beliniz çukurlaşmasın. 5 saniye tutun, sonra taraf değiştirin.", "Her iki yana 8–10 tekrar")
_ex2("sc_side", "sideplank", "Dizler üstünde yan köprü", "Yan yatın; dirseğiniz omzunuzun altında, dizleriniz bükülü olsun. Kalçanızı kaldırarak başınızdan dizlerinize kadar düz bir çizgi oluşturun, sonra yavaşça inin. Hangi tarafta daha çok çalışmanız gerektiğini fizyoterapistiniz belirler.", "10–20 saniye, her iki yana 3 kez")
_ex2("sc_cat", "cat", "Kedi-deve", "Ellerinizin ve dizlerinizin üzerinde durun. Nefes verirken sırtınızı yukarı doğru yuvarlayın, nefes alırken belinizi yavaşça aşağı bırakın. Hareketi yavaş ve ağrısız aralıkta yapın.", "10 tekrar")
_ex2("sc_bridge", "bridge", "Köprü", "Sırtüstü yatın, dizleriniz bükülü, ayaklarınız yerde. Kalçanızı sıkarak yavaşça kaldırın, 3 saniye bekleyip indirin.", "10–15 tekrar")
_ex2("sc_scap", "scap", "Kürek kemiği sıkıştırma", "Dik oturun ya da durun. Omuzlarınızı kaldırmadan kürek kemiklerinizi geriye ve aşağıya doğru yaklaştırın, 5 saniye tutup bırakın.", "10–15 tekrar")

SC_FAQ = [
 ("Ağır çanta ya da kötü duruş skolyoza yol açar mı?", "Hayır. Ergenlik döneminde görülen skolyozun nedeni bilinmiyor; ağır çanta ya da kötü duruş skolyoza yol açmaz. Ancak dik durunca düzelen duruş bozukluğu ile gerçek skolyozun birbirinden ayırt edilmesi gerekir."),
 ("Yüzme skolyozu düzeltir mi?", "Hayır. Uluslararası kılavuz, sporun skolyoz tedavisi olarak önerilmemesini, ama genel sağlık ve psikolojik faydaları nedeniyle bırakılmamasını öneriyor. Yüzme de dahil hiçbir spor tek başına eğriliği düzeltmez."),
 ("Egzersizle skolyoz tamamen düzelir mi?", "Skolyoza özgü egzersizler küçük eğriliklerde ilerlemeyi önlemeye ve bazı hastalarda açıyı birkaç derece azaltmaya yardım edebilir; ancak eğriliği tamamen ortadan kaldırması beklenmez. Hangi tedavinin gerektiğine eğrilik açısı ve büyüme durumu birlikte değerlendirilerek karar verilir."),
 ("Korse ne kadar süre takılmalı?", "Korsenin etkisi takılan süreye bağlıdır. BrAIST çalışmasında korseyi günde ortalama 13 saat ve üzerinde takanlarda başarı oranı %90'ın üzerindeydi; 6 saatten az takanlarda ise sonuç korse takmayanlardan farksızdı. Süreyi hekiminiz belirler."),
]

SC_SRC = [
 "Negrini S, Donzelli S, Aulisa AG, et al. " + ext("https://link.springer.com/article/10.1186/s13013-017-0145-8", "2016 SOSORT guidelines: orthopaedic and rehabilitation treatment of idiopathic scoliosis during growth") + ". Scoliosis Spinal Disord. 2018;13:3.",
 "Weinstein SL, Dolan LA, Wright JG, Dobbs MB. " + ext("https://www.nejm.org/doi/full/10.1056/NEJMoa1307337", "Effects of bracing in adolescents with idiopathic scoliosis") + ". N Engl J Med. 2013;369(16):1512-1521.",
 "Kuru T, Yeldan İ, Dereli EE, et al. " + ext("https://journals.sagepub.com/doi/abs/10.1177/0269215515575745", "The efficacy of three-dimensional Schroth exercises in adolescent idiopathic scoliosis: a randomised controlled clinical trial") + ". Clin Rehabil. 2016;30(2):181-190.",
]

SC_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Skolyoz</h1>
    <p class="lede">Omurganın yana doğru eğrilmesi ve aynı zamanda kendi etrafında dönmesidir. En sık ergenlik döneminde, nedeni bilinmeyen (idiyopatik) tipte görülür ve çoğu zaman ağrısızdır. Hızlı büyüme döneminde ilerleyebildiği için erken fark etmek önemlidir.</p>
    <p class="meta">Son güncelleme: 30 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%2–3</b><span>Ergenlerde 10 dereceden büyük skolyozun en sık bildirilen görülme sıklığı</span></div>
        <div class="stat"><b>%10</b><span>Tanı alan ergenlerden egzersiz ya da korse tedavisi gerekenler; ameliyat gerekenler %0,1–0,3</span></div>
        <div class="stat"><b>7'ye 1</b><span>30 derecenin üzerindeki eğriliklerde kızların erkeklere oranı</span></div>
        <div class="stat"><b>%72</b><span>Korse takan ergenlerde eğriliğin ameliyat sınırına ulaşmasının önlenme oranı; izlenenlerde %48</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Röntgende omurganın yana doğru 10 derece ya da daha fazla eğrildiği ve omurlarda dönme olduğu durumlara skolyoz denir. Olguların yaklaşık %80'inde belirli bir neden bulunamaz; buna idiyopatik skolyoz denir. Küçük eğrilikler kız ve erkeklerde benzer sıklıkta görülürken, ilerleyen büyük eğrilikler kızlarda çok daha sıktır.</p>
        <p class="soft">Eğrilik en çok hızlı büyüme döneminde ilerler. Büyüme tamamlandığında eğrilik belli bir eşiği aştıysa, yetişkinlikte ağrı ve başka sağlık sorunları riski artar.</p>
      </div>
      <div>
        <h2>Nasıl fark edilir?</h2>
        <ul class="dots">
          <li>Omuzlardan birinin ya da kürek kemiklerinden birinin daha yüksek görünmesi</li>
          <li>Belin iki yanındaki boşlukların farklı olması</li>
          <li>Öne eğilince sırtın bir tarafında kabarıklık (kaburga kamburu)</li>
          <li>Kıyafetlerin, eteğin ya da pantolonun bir tarafa kayması</li>
          <li>Ergenlik skolyozu çoğu zaman ağrı yapmaz; bu yüzden gözden kaçabilir</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Tedavi eğriliğe ve büyümeye göre planlanır</h2>
      <p class="soft">Uluslararası Skolyoz Ortopedik ve Rehabilitasyon Tedavisi Derneği'nin (SOSORT) kılavuzuna göre tedavinin amacı, büyüme döneminde eğriliğin ilerlemesini önlemek ya da sınırlamaktır. Kılavuz, skolyoza özgü fizyoterapi egzersizlerini ilerlemeyi ve korse ihtiyacını önlemede ilk basamak olarak öneriyor. Bu egzersizler üç boyutlu kendi kendine düzeltme, düzeltilmiş duruşu günlük hayata taşıma ve eğitim üzerine kuruludur ve bu yöntemlerde eğitim almış fizyoterapistlerce kişiye özel olarak planlanmalıdır.</p>
      <p class="soft">Türkiye'de 45 ergenle yapılan bir çalışmada, klinikte fizyoterapist eşliğinde yapılan Schroth egzersizleri 24 haftada eğrilik açısını, omurga rotasyonunu ve kaburga kamburunu azalttı; evde tek başına egzersiz yapan ve egzersiz yapmayan gruplarda ise bulgular kötüleşti.</p>
      <div class="callout">
        <p>Büyümesi süren ve eğriliği 20–25 dereceyi aşan ergenlerde korse önerilir. ABD ve Kanada'da 383 ergenle yapılan BrAIST çalışmasında eğriliğin ameliyat sınırı olan 50 dereceye ulaşmasını önlemede başarı oranı korse takanlarda %72, yalnızca izlenenlerde %48 oldu. Korseyi günde ortalama 13 saat ve üzerinde takanlarda başarı %90'ı aştı.</p>
      </div>
      <ul class="tx" style="margin-top:22px">
        <li><b>Gözlem</b><span>Küçük eğriliklerde, büyüme süresince düzenli aralıklarla muayene ve gerektiğinde röntgen.</span></li>
        <li><b>Skolyoza özgü egzersizler</b><span>Schroth gibi yöntemlerle, eğriliğin tipine göre kişiye özel program; ilk basamak tedavi.</span></li>
        <li><b>Korse</b><span>Büyümesi süren ve eğriliği ilerleyen ya da 20–25 dereceyi aşan ergenlerde; egzersizlerle birlikte.</span></li>
        <li><b>Ameliyat</b><span>İleri eğriliklerde ortopedi uzmanınca değerlendirilir.</span></li>
        <li><b>Spor</b><span>Genel sağlık ve psikolojik faydaları nedeniyle, korse tedavisi sırasında da bırakılmamalıdır; ancak tek başına tedavi yerine geçmez.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde</p>
      <h2>Kontrol ve genel egzersizler</h2>
      <p class="soft">İlk karttaki test, büyüme döneminde evde yapabileceğiniz basit bir kontroldür. Diğer egzersizler gövde kaslarını güçlendirir ve duruşu destekler, ancak eğriliği tek başına düzeltmez; skolyoza özgü egzersizler eğriliğin tipine göre kişiye özel olarak öğretilmelidir.</p>
      {ex_grid(["adams", "sc_bird", "sc_side", "sc_cat", "sc_bridge", "sc_scap"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(SC_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlarda beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Belirgin ya da geceleri uyandıran sırt ağrısı (ergenlik skolyozu genellikle ağrısızdır)</li>
        <li>Kol ya da bacaklarda uyuşma, güçsüzlük, yürüme bozukluğu; idrar ya da dışkı kontrolünde sorun</li>
        <li>Eğriliğin ya da kamburluğun kısa sürede belirgin artması</li>
        <li>10 yaşından önce fark edilen eğrilik</li>
        <li>Nefes darlığı</li>
      </ul>
      {CTA_CARD("Skolyoz", "skolyoz")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(SC_SRC)}
    </div>
  </section>
</main>'''

page("skolyoz.html", "Skolyoz",
     "Skolyoz nedir, evde nasıl fark edilir, ne zaman egzersiz, korse ya da ameliyat gerekir? Uluslararası kılavuz önerileri, korse çalışması ve evde kontrol testi.",
     "skolyoz.html", NECK_CSS, SC_BODY, "",
     seo_title="Skolyoz: Belirtiler, Egzersiz ve Korse Tedavisi | İhsan Eren",
     condition="Skolyoz", faq_items=SC_FAQ)

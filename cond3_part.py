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
 ("Dizlik ya da bant işe yarar mı?", "Bazı kişilerde ağrıyı kısa sürede hafifletebilir; ancak uluslararası uzlaşı raporuna göre bu konudaki kanıt yetersizdir. Egzersizin yerine değil, gerekirse yanında kullanılmalıdır. 2024’te yayımlanan bir en iyi uygulama rehberi, bandı yalnızca ağrı rehabilitasyonu zorlaştıracak kadar şiddetliyse öneriyor; tedavinin merkezinde dize yönelik egzersiz ve eğitim duruyor, en az 6 haftada yanıt yoksa değerlendirmenin gözden geçirilmesi gerekiyor."),
 ("MR çektirmem gerekiyor mu?", "Genellikle hayır. Tanı muayeneyle konur ve görüntülemede çoğu zaman ağrıyı açıklayan bir bulgu çıkmaz. Yaralanma sonrası başlayan ağrı, kilitlenme ya da belirgin şişlik gibi durumlarda görüntüleme gerekebilir."),
]

PF_SRC = [
 "Collins NJ, Barton CJ, van Middelkoop M, et al. " + ext("https://pure.eur.nl/en/publications/2018-consensus-statement-on-exercise-therapy-and-physical-interve/", "2018 Consensus statement on exercise therapy and physical interventions (orthoses, taping and manual therapy) to treat patellofemoral pain: recommendations from the 5th International Patellofemoral Pain Research Retreat, Gold Coast, Australia, 2017") + ". Br J Sports Med. 2018;52(18):1170-1178.",
 "Smith BE, Selfe J, Thacker D, et al. " + ext("https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0190892", "Incidence and prevalence of patellofemoral pain: a systematic review and meta-analysis") + ". PLoS One. 2018;13(1):e0190892.",
 "Lankhorst NE, van Middelkoop M, Crossley KM, et al. " + ext("https://repub.eur.nl/pub/97015", "Factors that predict a poor outcome 5-8 years after the diagnosis of patellofemoral pain: a multicentre observational analysis") + ". Br J Sports Med. 2016;50(14):881-886.",
 "Willy RW, Hoglund LT, Barton CJ, et al. " + ext("https://doi.org/10.2519/jospt.2019.0302", "Patellofemoral pain: clinical practice guidelines linked to the International Classification of Functioning, Disability and Health from the Academy of Orthopaedic Physical Therapy of the American Physical Therapy Association") + ". J Orthop Sports Phys Ther. 2019;49(9)",
 "Neal BS, Lack SD, Bartholomew C, Morrissey D. " + ext("https://bjsm.bmj.com/content/58/24/1486", "Best practice guide for patellofemoral pain based on synthesis of a systematic review, the patient voice and expert clinical reasoning") + ". Br J Sports Med. 2024;58(24):1486.",
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
        <div class="stat"><b>%57</b><span>Bir izlem çalışmasında 5–8 yıl sonra yanıt veren 60 hastadan iyileşmediğini bildirenler</span></div>
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
        <p>Diz önü ağrısı kendiliğinden her zaman geçmeyebilir. Hollanda'da yapılan bir izlem çalışmasında, başlangıçtaki 310 hastadan 5–8 yıl sonra soruları yanıtlayan 60'ının (%19) %57'si iyileşmediğini bildirdi. Yanıt verenler küçük ve seçilmiş bir grup olduğu için bu oran herkes için bir tahmin değildir. Çalışmada ağrının başlangıçta 12 aydan uzun süredir devam ediyor olması kötü sonucun en güçlü göstergesiydi. Bu yüzden erken ve düzenli tedavi önemli.</p>
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
 ("Koşmaya devam edebilir miyim?", "Çoğu zaman evet, ama yükü azaltarak. Koşu sırasındaki ağrı hafif düzeyde kalıyor ve ertesi sabah artmıyorsa devam edebilirsiniz. Yokuş, tempo ve hız antrenmanlarını bir süre azaltın. 38 hastayla yapılan randomize bir çalışmada, ağrıyı izleyerek koşu ve sıçramaya devam edenler ile ilk 6 hafta bu etkinliklere ara verenler aynı egzersiz programıyla benzer şekilde iyileşti; etkinliğe devam etmenin olumsuz bir etkisi görülmedi."),
 ("Ne kadar sürede iyileşir?", "Sabır gerektirir. Çalışmalarda egzersiz programları 12 hafta sürdü ve kazanımlar 1 yıl sonra da korundu. Bazı kişilerde tam iyileşme birkaç ay daha sürebilir."),
 ("Kortizon iğnesi yaptırmalı mıyım?", "Aşil kirişine kortizon iğnesi, kirişi zayıflatıp yırtılma riskini artırabileceği için genellikle önerilmez. Önce düzenli yüklenme egzersizlerinin denenmesi gerekir."),
 ("Germe egzersizleri yeterli mi?", "Tek başına genellikle yeterli değildir. Kirişin iyileşmesi için asıl gereken, kademeli olarak artırılan yüklenme egzersizleridir; germe hareketleri bunlara eklenebilir."),
]

AC_SRC = [
 "Martin RL, Chimenti R, Cuddeford T, et al. " + ext("https://www.jospt.org/doi/10.2519/jospt.2018.0302", "Achilles pain, stiffness, and muscle power deficits: midportion Achilles tendinopathy revision 2018") + ". J Orthop Sports Phys Ther. 2018;48(5):A1-A38.",
 "Beyer R, Kongsgaard M, Hougs Kjær B, et al. " + ext("https://journals.sagepub.com/doi/abs/10.1177/0363546515584760", "Heavy slow resistance versus eccentric training as treatment for Achilles tendinopathy: a randomized controlled trial") + ". Am J Sports Med. 2015;43(7):1704-1711.",
 "Alfredson H, Pietilä T, Jonsson P, Lorentzon R. " + ext("https://journals.sagepub.com/doi/10.1177/03635465980260030301", "Heavy-load eccentric calf muscle training for the treatment of chronic Achilles tendinosis") + ". Am J Sports Med. 1998;26(3):360-366.",
 "Silbernagel KG, Hanlon S, Sprague A. " + ext("https://pmc.ncbi.nlm.nih.gov/articles/PMC7249277", "Current clinical concepts: conservative management of Achilles tendinopathy") + ". J Athl Train. 2020;55(5)",
 "Chimenti RL, Neville C, Houck J, Cuddeford T, Carreira D, Martin RL. " + ext("https://doi.org/10.2519/jospt.2024.0302", "Achilles pain, stiffness, and muscle power deficits: midportion Achilles tendinopathy revision – 2024") + ". J Orthop Sports Phys Ther. 2024;54(12):CPG1–CPG32.",
 "Silbernagel KG, Thomeé R, Eriksson BI, Karlsson J. " + ext("https://search.pedro.org.au/search-results/record-detail/18389", "Continued sports activity, using a pain-monitoring model, during rehabilitation in patients with Achilles tendinopathy: a randomized controlled study") + ". Am J Sports Med. 2007;35(6):897–906.",
]

AC_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Aşil tendinopatisi</h1>
    <p class="lede">Topuğun hemen üstünde, aşil kirişinde ağrı, sabah tutukluğu ve kalınlaşmayla kendini gösterir. Özellikle koşucularda ve orta yaşta sık görülür. Sorun iltihaptan çok kirişin aşırı yüke uyum sağlayamamasıdır; tedavinin temeli kademeli olarak artırılan yüklenme egzersizleridir.</p>
    <p class="meta">Son güncelleme: 24 Ekim 2026</p>
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
      <p class="soft">Kirişler, kademeli olarak artırılan yüke uyum sağlayarak güçlenir. Amerikan Fizyoterapi Derneği'nin 2018 kılavuzu ve 2024 güncellemesi de yüklenme egzersizlerini tedavinin temeli olarak öneriyor; güncelleme, egzersizin dayanılabilen en yüksek yükte ve haftada en az 3 kez yapılmasını, tam dinlenme yerine ağrı sınırları içinde aktif kalmayı öneriyor. Klasik yöntem, İsveçli ortopedist Alfredson'un geliştirdiği eksantrik programdır: 12 hafta boyunca, günde iki kez, basamaktan topuğu yavaşça indirmek.</p>
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
 ("Yastık ve uyku pozisyonu önemli mi?", "Boynunuzu gövdenizle aynı hizada tutan bir yastık, sabah başlayan boyun kaynaklı ağrılarda rahatlatabilir. Yüzüstü yatmak boynu uzun süre döndürdüğü için ağrıyı artırabilir. Egzersizin gerilim tipi baş ağrısındaki yeri için kanıt hâlâ zayıf: bir meta-analizde kuvvet egzersizleri ağrı şiddetini orta düzeyde azalttı, ama kanıtın kesinliği çok düşüktü. ABD fizyoterapi kılavuzu ise uzun süren boyun kaynaklı baş ağrısında boyun eklemlerine yönelik manuel tedaviyi boyun ve omuz kuşağı germe, güçlendirme ve dayanıklılık egzersizleriyle birlikte öneriyor."),
]

HA_SRC = [
 "World Health Organization. " + ext("https://www.who.int/news-room/fact-sheets/detail/headache-disorders", "Migraine and other headache disorders") + ". Fact sheet.",
 "Jull G, Trott P, Potter H, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/12221344/", "A randomized controlled trial of exercise and manipulative therapy for cervicogenic headache") + ". Spine. 2002;27(17):1835-1843.",
 "Headache Classification Committee of the International Headache Society. " + ext("https://ichd-3.org/", "The International Classification of Headache Disorders, 3rd edition") + ". Cephalalgia. 2018;38(1):1-211.",
 "NICE. " + ext("https://www.nice.org.uk/guidance/cg150", "Headaches in over 12s: diagnosis and management") + ". NICE clinical guideline CG150, 2012",
 "Varangot-Reille C, Suso-Martí L, Romero-Palau M, Suárez-Pastor P, Cuenca-Martínez F. " + ext("https://pubmed.ncbi.nlm.nih.gov/34929374/", "Effects of different therapeutic exercise modalities on migraine or tension-type headache: a systematic review and meta-analysis with a replicability analysis") + ". J Pain. 2022.",
 "Blanpied PR, Gross AR, Elliott JM, et al. " + ext("https://doi.org/10.2519/jospt.2017.0302", "Neck pain: revision 2017. Clinical practice guidelines linked to the International Classification of Functioning, Disability and Health from the Orthopaedic Section of the American Physical Therapy Association") + ". J Orthop Sports Phys Ther. 2017;47(7):A1–A83.",
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
_ex2("sc_side", "sideplank", "Dizler üstünde yan köprü", "Yan yatın; dirseğiniz omzunuzun altında, dizleriniz bükülü olsun. Kalçanızı kaldırarak başınızdan dizlerinize kadar düz bir çizgi oluşturun, sonra yavaşça inin. İki tarafa da eşit yapın; eğriliğinize göre bir tarafa ağırlık verilmesi gerekiyorsa bunu fizyoterapistiniz belirler.", "10–20 saniye, her iki yana 3 kez")
_ex2("sc_cat", "cat", "Kedi-deve", "Ellerinizin ve dizlerinizin üzerinde durun. Nefes verirken sırtınızı yukarı doğru yuvarlayın, nefes alırken belinizi yavaşça aşağı bırakın. Hareketi yavaş ve ağrısız aralıkta yapın.", "10 tekrar")
_ex2("sc_bridge", "bridge", "Köprü", "Sırtüstü yatın, dizleriniz bükülü, ayaklarınız yerde. Kalçanızı sıkarak yavaşça kaldırın, 3 saniye bekleyip indirin.", "10–15 tekrar")
_ex2("sc_scap", "scap", "Kürek kemiği sıkıştırma", "Dik oturun ya da durun. Omuzlarınızı kaldırmadan kürek kemiklerinizi geriye ve aşağıya doğru yaklaştırın, 5 saniye tutup bırakın.", "10–15 tekrar")

SC_FAQ = [
 ("Ağır çanta ya da kötü duruş skolyoza yol açar mı?", "Araştırmalara göre hayır: Skolyoz Araştırma Derneği (SRS), ağır çantanın, kötü duruşun ve sporun skolyoza yol açmadığını ve eğriliği kötüleştirmediğini belirtiyor; Portekiz'de 966 öğrenciyle yapılan bir çalışmada da çanta ağırlığı ve duruş alışkanlıkları skolyozla ilişkili bulunmadı. Ağır çanta ise bel ve sırt ağrısına yol açabilir. Klinik deneyimimizde, büyüme atağındaki ve bağ dokusu esnek olan gençlerde tek taraflı yüklenmenin duruş asimetrisini ve ağrıyı belirginleştirebildiğini görüyoruz; bu yüzden çantanın iki omuzda taşınmasını öneriyoruz."),
 ("C ve S eğrilik arasındaki fark nedir?", "C eğrilikte omurgada tek bir yay vardır. S eğrilikte ise biri göğüs, diğeri bel bölgesinde, ters yönlere bakan iki yay bulunur. İkisinde de eğriliğin büyüklüğü röntgende Cobb açısıyla ölçülür; tedavi kararında eğrilik tipi, açı ve kalan büyüme birlikte değerlendirilir."),
 ("Skolyozlu çocuğum spor yapabilir mi?", "Evet. SRS'ye göre sırt ağrısı olmadıkça skolyozlu çocuklar her sporu yapabilir; uluslararası kılavuz (SOSORT) da sporun genel sağlık ve psikolojik faydaları nedeniyle korse tedavisi sırasında bile bırakılmamasını öneriyor. Ancak hiçbir spor tek başına eğriliği düzeltmez."),
 ("Yüzme skolyozu düzeltir mi?", "Hayır. Uluslararası kılavuz, sporun skolyoz tedavisi olarak önerilmemesini, ama genel sağlık ve psikolojik faydaları nedeniyle bırakılmamasını öneriyor. Yüzme de dahil hiçbir spor tek başına eğriliği düzeltmez."),
 ("Egzersizle skolyoz tamamen düzelir mi?", "Skolyoza özgü egzersizler küçük eğriliklerde ilerlemeyi önlemeye ve bazı hastalarda açıyı birkaç derece azaltmaya yardım edebilir; ancak eğriliği tamamen ortadan kaldırması beklenmez. 13 çalışmayı inceleyen 2024 tarihli Cochrane derlemesine göre egzersizin yararına ilişkin kanıtların güvenilirliği düşük ya da çok düşük. Hangi tedavinin gerektiğine eğrilik açısı ve büyüme durumu birlikte değerlendirilerek karar verilir."),
 ("Korse ne kadar süre takılmalı?", "Korsenin etkisi takılan süreye bağlıdır. BrAIST çalışmasında korseyi günde ortalama 13 saat ve üzerinde takanlarda başarı oranı %90'ın üzerindeydi; 6 saatten az takanlarda ise sonuç korse takmayanlardan farksızdı. Süreyi hekiminiz belirler. 7 çalışmayı ve 662 ergeni kapsayan Cochrane derlemesinde sert korse, 20–40 derecelik eğriliklerde izlemeye göre 2 yılda başarı oranını artırdı; çalışmaların tümü korsenin eğriliğin ilerlemesini önlediğini gösterdi, ancak kanıtın kalitesi düşük ile çok düşük arasındaydı."),
 ("Eğriliğim 50 derecenin üzerinde; ameliyat şart mı?", "Her zaman değil. Büyümesi süren ve eğriliği 45 derecenin üzerinde ilerleyen gençlerde ameliyat genellikle önerilir. Büyümesi tamamlanmış kişilerde ise karar yalnızca dereceye göre değil; eğriliğin ilerleyip ilerlemediğine, gövde dengesine, ağrıya, akciğer işlevine ve kişinin beklentisine göre verilir. Gövdesi dengeli, eğriliği ilerlemeyen ve günlük hayatı kısıtlanmayan bazı hastalarda cerrahlar düzenli izlemi önerebilir. Kararı omurga cerrahınızla birlikte verirsiniz."),
 ("Büyüme bittikten sonra skolyoz ilerler mi?", "Küçük eğrilikler genellikle ilerlemez. Danimarka'da korse ya da izlemle tedavi edilmiş hastaların ortalama 41 yıl izlendiği bir çalışmada eğrilikler yetişkinlikte yılda ortalama 0,2–0,5 derece arttı; ancak kişiler arasındaki fark büyüktü. Yazarlar, büyüme sonunda eğriliği orta düzeyde olanların erken yetişkinlikte bir kez daha röntgenle kontrol edilmesini öneriyor."),
 ("Skolyoz gebeliği etkiler mi?", "SRS'ye göre gebelik, ameliyat edilmemiş bir omurgada eğriliği genellikle artırmaz ve skolyoz doğumu zorlaştırmaz. Gebelikte egzersize başlamadan önce kadın doğum hekiminize danışın."),
]

SC_SRC = [
 "Negrini S, Donzelli S, Aulisa AG, et al. " + ext("https://link.springer.com/article/10.1186/s13013-017-0145-8", "2016 SOSORT guidelines: orthopaedic and rehabilitation treatment of idiopathic scoliosis during growth") + ". Scoliosis Spinal Disord. 2018;13:3.",
 "Scoliosis Research Society. " + ext("https://www.srs.org/Files/Patient-Brochures/Patient.Adolescent_Idiopathic_Scoliosis_Handbook_for_Patients.pdf", "Adolescent idiopathic scoliosis: handbook for patients") + ".",
 "Weinstein SL, Dolan LA, Wright JG, Dobbs MB. " + ext("https://www.nejm.org/doi/full/10.1056/NEJMoa1307337", "Effects of bracing in adolescents with idiopathic scoliosis") + ". N Engl J Med. 2013;369(16):1512-1521.",
 "Negrini S, Minozzi S, Bettany-Saltikov J, et al. " + ext("https://www.cochrane.org/evidence/CD006850_braces-idiopathic-scoliosis-adolescents", "Braces for idiopathic scoliosis in adolescents") + ". Cochrane Database Syst Rev. 2015;(6):CD006850.",
 "Romano M, Minozzi S, Bettany-Saltikov J, et al. " + ext("https://www.cochrane.org/evidence/CD007837_what-type-therapeutic-exercise-best-treating-scoliosis-adolescents", "Therapeutic exercises for idiopathic scoliosis in adolescents") + ". Cochrane Database Syst Rev. 2024;(2):CD007837.",
 "Charalampidis A, Diarbakerli E, Dufvenberg M, et al. " + ext("https://search.pedro.org.au/search-results/record-detail/75548", "Nighttime bracing or exercise in moderate-grade adolescent idiopathic scoliosis: a randomized clinical trial") + ". JAMA Netw Open. 2024;7(1):e2352492.",
 "Kuru T, Yeldan İ, Dereli EE, et al. " + ext("https://journals.sagepub.com/doi/abs/10.1177/0269215515575745", "The efficacy of three-dimensional Schroth exercises in adolescent idiopathic scoliosis: a randomised controlled clinical trial") + ". Clin Rehabil. 2016;30(2):181-190.",
 "Berdishevsky H, Lebel VA, Bettany-Saltikov J, et al. " + ext("https://research.tees.ac.uk/en/publications/physiotherapy-scoliosis-specific-exercises-a-comprehensive-review-3/", "Physiotherapy scoliosis-specific exercises – a comprehensive review of seven major schools") + ". Scoliosis Spinal Disord. 2016;11.",
 "Lonstein JE, Carlson JM. " + ext("https://www.qxmd.com/r/6480635", "The prediction of curve progression in untreated idiopathic scoliosis during growth") + ". J Bone Joint Surg Am. 1984;66(7):1061-1071. Özet ve sayılar: " + ext("https://www.spinemd.com/will-my-curve-worsen-four-key-factors-for-scoliosis-curve-progression/", "Virginia Spine Institute, 8 June 2016") + ".",
 "Little DG, Song KM, Katz D, Herring JA. " + ext("https://www.qxmd.com/r/10819279", "Relationship of peak height velocity to other maturity indicators in idiopathic scoliosis in girls") + ". J Bone Joint Surg Am. 2000;82(5):685-693.",
 "Weinstein SL, Dolan LA, Spratt KF, et al. Health and function of patients with untreated idiopathic scoliosis: a 50-year natural history study. JAMA. 2003;289(5):559-567. Özet: " + ext("https://www.aafp.org/afp/2003/0601/p2391a", "American Family Physician") + ".",
 "Dragsted C, Ragborg L, Ohrt-Nissen S, et al. " + ext("https://actaorthop.org/actao/article/download/42659/48814?inline=1", "Curve progression in non-surgically treated patients with idiopathic scoliosis: a cohort study with 40-year follow-up") + ". Acta Orthop. 2025;96:110-115.",
 "Minghelli B, Oliveira R, Nunes C. " + ext("https://journals.sagepub.com/doi/10.3233/WOR-162284", "Postural habits and weight of backpacks of Portuguese adolescents: are they associated with scoliosis and low back pain?") + ". Work. 2016;54(1):197-208.",
 "Czaprowski D, Kotwicki T, Pawłowska P, Stoliński L. " + ext("https://pmc.ncbi.nlm.nih.gov/articles/PMC3204294", "Joint hypermobility in children with idiopathic scoliosis: SOSORT award 2011 winner") + ". Scoliosis. 2011;6:22.",
 "Tanchev PI, Dzherov AD, Parushev AD, Dikov DM, Todorov MB. " + ext("https://sponet.de/sponet/Record/4004104", "Scoliosis in rhythmic gymnasts") + ". Spine. 2000;25(11):1367-1372.",
 "Moramarco K, Borysov M. " + ext("https://openorthopaedicsjournal.com/VOLUME/11/PAGE/1452/ABSTRACT/", "A modern historical perspective of Schroth scoliosis rehabilitation and corrective bracing techniques for idiopathic scoliosis") + ". Open Orthop J. 2017;11:1452.",
 "Scoliosis Research Society. " + ext("https://www.srs.org/About-SRS/SRS-History/Historical-Timeline", "Historical timeline") + ".",
 "National Scoliosis Foundation. " + ext("https://www.scoliosis.org/resources/medicalupdates/bracingworks.php", "Bracing works: report from the 1993 SRS annual meeting") + ".",
 "MD+DI. " + ext("https://www.mddionline.com/orthopedic/scoliosis-win-fda-approves-vertebral-body-tethering", "Scoliosis win: FDA approves vertebral body tethering") + ". 16 August 2019.",
 "Radiopaedia. " + ext("https://images.radiopaedia.org/articles/cobb-angle/changesets/171866/edits?lang=us", "Cobb angle") + "; " + ext("https://radiopaedia.org/articles/scoliosis-surgery-overview?lang=gb", "Scoliosis surgery overview") + ".",
 "Children's Hospital Los Angeles. " + ext("https://chla.org/blog/rn-remedies/do-you-know-how-heavy-your-childs-backpack", "Do you know how heavy your child's backpack is?") + ".",
]

# ---------------------------------------------------------------- çizimler (gerçek fotoğraf değil)
import math as _m
_SK_V = "#cfc6a8"; _SK_HL = "#e2ab47"; _SK_AP = "#8fa476"; _SK_LN = "rgba(236,229,207,.35)"

def _sk_pts(f, top, bot, n=17, cx=80):
    pts = []
    for i in range(n):
        t = i / (n - 1); y = top + (bot - top) * t
        x = cx + f(t)
        e = 1e-3; dx = (f(min(1, t + e)) - f(max(0, t - e))) / ((min(1, t + e) - max(0, t - e)) * (bot - top))
        ang = _m.degrees(_m.atan2(-dx, 1.0))
        pts.append((x, y, ang))
    return pts

def _sk_verts(pts, hl=(), ap=(), w=24, h=9):
    out = []
    for i, (x, y, a) in enumerate(pts):
        c = _SK_HL if i in hl else (_SK_AP if i in ap else _SK_V)
        out.append(f'<rect x="{x - w / 2:.1f}" y="{y - h / 2:.1f}" width="{w}" height="{h}" rx="2.6" fill="{c}" transform="rotate({a:.1f} {x:.1f} {y:.1f})"/>')
    line = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y, _ in pts)
    return f'<path d="{line}" fill="none" stroke="{_SK_LN}" stroke-width="12" stroke-linecap="round"/>' + "".join(out)

def _sk_pelvis(cx, y):
    return (f'<path d="M{cx - 46} {y + 4} Q{cx - 40} {y + 34} {cx - 12} {y + 40} M{cx + 46} {y + 4} Q{cx + 40} {y + 34} {cx + 12} {y + 40}" '
            f'fill="none" stroke="{_SK_LN}" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M{cx - 12} {y + 2} L{cx + 12} {y + 2} L{cx} {y + 30} Z" fill="{_SK_V}" opacity=".55"/>')

def _sk_shoulders(cx, y, tilt):
    return (f'<path d="M{cx - 54} {y + tilt} Q{cx} {y - 8} {cx + 54} {y - tilt}" fill="none" stroke="{_SK_LN}" stroke-width="5" stroke-linecap="round"/>')

def SK_SPINE(kind):
    if kind == "C":
        f = lambda t: 26 * _m.sin(_m.pi * t); tilt = 4
    elif kind == "S":
        f = lambda t: 22 * _m.sin(2 * _m.pi * t); tilt = 7
    else:
        f = lambda t: 0; tilt = 0
    pts = _sk_pts(f, 40, 220)
    return (f'<svg viewBox="0 0 160 270" role="img" aria-hidden="true">'
            + _sk_shoulders(80, 30, tilt) + _sk_verts(pts) + _sk_pelvis(80, 228) + '</svg>')

def SK_COBB():
    a, b = 0.12, 0.88
    def f(t):
        if t <= a or t >= b: return 0.0
        return 34 * _m.sin(_m.pi * (t - a) / (b - a))
    cx = 200
    pts = _sk_pts(f, 30, 250, n=19, cx=cx)
    n = len(pts)
    up = max(range(0, n // 2), key=lambda i: abs(pts[i][2])); lo = max(range(n // 2, n), key=lambda i: abs(pts[i][2]))
    apx = max(range(n), key=lambda i: pts[i][0])
    def endline(i):
        x, y, ang = pts[i]; r = _m.radians(ang)
        return x, y, _m.cos(r), _m.sin(r)
    x1, y1, c1, s1 = endline(up); x2, y2, c2, s2 = endline(lo)
    det = c1 * (-s2) - (-c2) * s1
    t1 = ((x2 - x1) * (-s2) - (-c2) * (y2 - y1)) / det
    ix, iy = x1 + c1 * t1, y1 + s1 * t1
    def seg(x, y, px, py):
        ex, ey = px + (px - x) * 0.18, py + (py - y) * 0.18
        return f'<path d="M{x + (x - px) * 0.25:.1f} {y + (y - py) * 0.25:.1f} L{ex:.1f} {ey:.1f}" stroke="{_SK_HL}" stroke-width="2.4" stroke-dasharray="6 5" fill="none"/>'
    r = 26
    def ang_to(px, py): return _m.atan2(py - iy, px - ix)
    a1, a2 = ang_to(x1, y1), ang_to(x2, y2)
    p1 = (ix + r * _m.cos(a1), iy + r * _m.sin(a1)); p2 = (ix + r * _m.cos(a2), iy + r * _m.sin(a2))
    sweep = 1 if (a2 - a1) % (2 * _m.pi) < _m.pi else 0
    arc = f'<path d="M{p1[0]:.1f} {p1[1]:.1f} A{r} {r} 0 0 {sweep} {p2[0]:.1f} {p2[1]:.1f}" stroke="#ece5cf" stroke-width="3" fill="none"/>'
    return (f'<svg viewBox="0 0 320 300" role="img" aria-hidden="true">'
            + _sk_verts(pts, hl=(up, lo), ap=(apx,)) + seg(x1, y1, ix, iy) + seg(x2, y2, ix, iy) + arc
            + f'<circle cx="{ix:.1f}" cy="{iy:.1f}" r="3.5" fill="#ece5cf"/>' + '</svg>')

def SK_ADAMS():
    return ('<svg viewBox="0 0 320 190" role="img" aria-hidden="true">'
            '<path d="M20 170 H140" stroke="rgba(236,229,207,.25)" stroke-width="3" stroke-linecap="round"/>'
            '<path d="M46 168 L50 112 M58 168 L56 112" stroke="#8fa476" stroke-width="7" stroke-linecap="round" fill="none"/>'
            '<path d="M52 110 Q78 76 112 96" stroke="#8fa476" stroke-width="8" stroke-linecap="round" fill="none"/>'
            '<path d="M108 98 L112 140" stroke="#8fa476" stroke-width="6" stroke-linecap="round" fill="none"/><circle cx="122" cy="108" r="10" fill="#8fa476"/>'
            '<path d="M62 74 Q78 62 96 72" stroke="#e2ab47" stroke-width="3" stroke-dasharray="4 5" fill="none"/>'
            '<path d="M170 140 C190 104 222 84 246 88 C262 92 282 112 304 140" fill="none" stroke="#cfc6a8" stroke-width="5" stroke-linecap="round"/>'
            '<path d="M172 140 C192 120 218 112 236 112 C258 112 280 122 302 140" fill="none" stroke="rgba(236,229,207,.25)" stroke-width="3" stroke-dasharray="5 6"/>'
            '<circle cx="238" cy="96" r="5" fill="#8fa476"/>'
            '<g transform="rotate(-11 238 70)"><rect x="196" y="62" width="84" height="16" rx="6" fill="none" stroke="#e2ab47" stroke-width="2.6"/><circle cx="238" cy="70" r="4" fill="#e2ab47"/></g>'
            '<path d="M196 70 H280" stroke="rgba(236,229,207,.35)" stroke-width="2" stroke-dasharray="3 5"/>'
            '</svg>')

def SK_RISSER():
    segs = ""
    pts = [(170, 70), (196, 44), (232, 32), (268, 40), (294, 62)]
    cols = ["#5e6b4f", "#8fa476", "#b5b46a", "#e2ab47"]
    for k in range(4):
        (xa, ya), (xb, yb) = pts[k], pts[k + 1]
        segs += f'<path d="M{xa} {ya} L{xb} {yb}" stroke="{cols[k]}" stroke-width="9" stroke-linecap="round"/>'
        segs += f'<text x="{(xa + xb) / 2:.0f}" y="{(ya + yb) / 2 - 12:.0f}" fill="#ece5cf" font-size="14" text-anchor="middle" font-family="sans-serif">{k + 1}</text>'
    return ('<svg viewBox="0 0 320 190" role="img" aria-hidden="true">'
            '<path d="M150 70 L124 44 L88 32 L52 40 L26 62 C14 92 34 124 68 150 L90 170" fill="none" stroke="rgba(236,229,207,.35)" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
            '<path d="M150 74 C144 120 124 150 104 170" fill="none" stroke="rgba(236,229,207,.35)" stroke-width="5" stroke-linecap="round"/>'
            '<path d="M170 74 C176 120 196 150 216 170" fill="none" stroke="rgba(236,229,207,.35)" stroke-width="5" stroke-linecap="round"/>'
            '<path d="M294 62 C306 92 286 124 252 150 L230 170" fill="none" stroke="rgba(236,229,207,.35)" stroke-width="5" stroke-linecap="round"/>'
            '<path d="M144 120 L176 120 L160 168 Z" fill="#cfc6a8" opacity=".5"/>'
            + segs + '</svg>')

def SK_BALANCE(ok):
    if ok:
        f = lambda t: 22 * _m.sin(2 * _m.pi * t)
    else:
        f = lambda t: 30 * _m.sin(_m.pi * t) + 26 * (1 - t)
    pts = _sk_pts(f, 40, 220)
    x0 = pts[0][0]
    shift = "" if ok else (f'<path d="M80 252 L{x0:.1f} 252" stroke="#e2ab47" stroke-width="2.5"/>'
                           f'<path d="M{x0 - 6:.1f} 246 L{x0:.1f} 252 L{x0 - 6:.1f} 258" stroke="#e2ab47" stroke-width="2.5" fill="none"/>')
    return (f'<svg viewBox="0 0 160 270" role="img" aria-hidden="true">'
            + _sk_verts(pts) + _sk_pelvis(80, 228)
            + f'<path d="M{x0:.1f} 30 L{x0:.1f} 262" stroke="#ece5cf" stroke-width="2" stroke-dasharray="4 5"/>'
            + f'<circle cx="{x0:.1f}" cy="30" r="5" fill="#ece5cf"/>' + shift + '</svg>')

SC_CSS = NECK_CSS + """
  .sk-toc{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}
  .sk-toc a{border:1px solid var(--line);border-radius:999px;padding:6px 12px;font-size:14px;text-decoration:none;color:var(--ink-soft)}
  .sk-toc a:hover{color:var(--ink);border-color:var(--gold)}
  .sk-figs{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;max-width:640px;margin:20px 0 8px}
  .sk-figs.two{grid-template-columns:repeat(2,minmax(0,1fr));max-width:460px}
  .sk-figs.one{grid-template-columns:1fr;max-width:420px}
  .sk-figs figure{margin:0;border:1px solid var(--line);border-radius:12px;background:var(--ground-2);padding:10px 8px;text-align:center}
  .sk-figs svg{width:100%;height:auto;display:block}
  .sk-figs figcaption{font-size:14px;color:var(--ink-soft);margin-top:6px;line-height:1.45}
  .sk-figs figcaption b{display:block;color:var(--ink);font-size:15px}
  @media (max-width:420px){.sk-figs{gap:8px}.sk-figs figure{padding:8px 4px}.sk-figs figcaption{font-size:13px}}
  .sk-key{font-size:14px;color:var(--ink-soft);max-width:640px;margin:6px 0 0}
  .sk-key i{display:inline-block;width:12px;height:12px;border-radius:3px;margin:0 6px -1px 0}
  .sk-more{font-size:15px;margin-top:10px}
  .sk-tl{list-style:none;margin:8px 0 0;padding:0 0 0 18px;max-width:820px;border-left:2px solid var(--line)}
  .sk-tl li{position:relative;padding:10px 0 10px 4px}
  .sk-tl li::before{content:"";position:absolute;left:-25px;top:17px;width:12px;height:12px;border-radius:50%;background:var(--gold)}
  .sk-tl b{font-family:var(--display);color:var(--foil);font-size:18px;margin-right:6px}
  .sk-tl span{color:var(--ink-soft)}
  .sk-cmp{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-top:10px}
  @media (max-width:980px){.sk-cmp{grid-template-columns:repeat(2,minmax(0,1fr))}}
  @media (max-width:600px){.sk-cmp{grid-template-columns:1fr}}
  .sk-cmp .kind dl{margin:4px 0 0;display:grid;gap:6px}
  .sk-cmp .kind dt{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:600}
  .sk-cmp .kind dd{margin:0;font-size:15px;color:var(--ink-soft)}
  .sk-split{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:28px;align-items:start}
  @media (max-width:820px){.sk-split{grid-template-columns:1fr;gap:10px}}
  .callout.obs .obs-t{font-size:14px;color:var(--ink-soft)}
"""

def SK_CLIN(text):
    return (f'<div class="callout obs"><p class="obs-k">Klinik deneyimden</p><p>{text}</p>'
            f'<p class="obs-t">Bu bilgi bir araştırma sonucu değil, klinik deneyime dayanıyor; herkes için geçerli olmayabilir.</p></div>')

SC_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Skolyoz</h1>
    <p class="lede">Omurganın yana doğru eğrilmesi ve aynı zamanda kendi etrafında dönmesidir. En sık ergenlik döneminde, nedeni bilinmeyen (idiyopatik) tipte görülür ve çoğu zaman ağrısızdır. Hızlı büyüme döneminde ilerleyebildiği için erken fark etmek önemlidir. Bu rehberde eğrilik tiplerini, röntgende ölçümü, büyümenin önemini ve geçmişten bugüne tedavileri araştırmalarla ve klinik deneyimle birlikte, ayrımını yaparak anlatıyoruz.</p>
    <p class="meta">Son güncelleme: 28 Ekim 2026</p>
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
      <p class="eyebrow" style="margin-top:26px">Bu sayfada</p>
      <nav class="sk-toc" aria-label="Bu sayfada">
        <a href="#nedir">Skolyoz nedir?</a><a href="#egrilik">C ve S eğrilik</a><a href="#cobb">Röntgen ve Cobb açısı</a><a href="#turler">Türleri</a><a href="#buyume">Büyüme dönemi</a><a href="#risk">Çanta, alışkanlıklar, esneklik</a><a href="#tarihce">Geçmişten bugüne</a><a href="#tedavi">Tedaviler</a><a href="#ameliyat">Ameliyat ve denge</a><a href="#egzersizler">Egzersizler</a>
      </nav>
    </div>
  </section>

  <section id="nedir">
    <div class="wrap two">
      <div>
        <h2>Skolyoz nedir?</h2>
        <p class="soft">Röntgende omurganın yana doğru 10 derece ya da daha fazla eğrildiği ve omurlarda dönme olduğu durumlara skolyoz denir. Yani skolyoz yalnızca yana eğrilik değil, üç boyutlu bir şekil değişikliğidir: omurlar yana kayarken kendi eksenleri etrafında da döner ve kaburgaları bir tarafta geriye iter. Olguların yaklaşık %80'inde belirli bir neden bulunamaz; buna idiyopatik skolyoz denir. Ergenlikte tanı alanların yaklaşık %30'unun ailesinde de skolyoz vardır.</p>
        <p class="soft">Küçük eğrilikler kız ve erkeklerde benzer sıklıkta görülürken, ilerleyen büyük eğrilikler kızlarda çok daha sıktır: Skolyoz Araştırma Derneği'ne (SRS) göre kızlarda tedavi gerektirecek kadar ilerleme olasılığı erkeklere göre 5–8 kat fazladır.</p>
      </div>
      <div>
        <h2>Duruş bozukluğu ile farkı</h2>
        <p class="soft">Kötü duruş, ağrıya bağlı kas kasılması ya da bacak boyu farkı da omurgayı yana eğik gösterebilir. Bu tür <strong>fonksiyonel</strong> eğriliklerde omurlarda dönme yoktur ve neden ortadan kalkınca, örneğin dik durunca, öne eğilince ya da yatınca eğrilik düzelir. Gerçek (yapısal) skolyozda ise öne eğilince sırtın bir tarafında kabarıklık belirir. SRS'ye göre bacak boyu farkı skolyoza yol açmaz, ama eğriliği daha belirgin gösterebilir.</p>
        <p class="sk-more">Ayrıntılı bilgi: <a href="kambur-durus.html">Kambur duruş rehberi</a></p>
        <h2 style="margin-top:22px">Nasıl fark edilir?</h2>
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

  <section id="egrilik">
    <div class="wrap">
      <h2>C ve S eğrilik</h2>
      <p class="soft">Arkadan çekilen röntgende skolyozlu bir omurga çoğu zaman bir <strong>C</strong> ya da bir <strong>S</strong> harfine benzer. C eğrilikte tek bir yay vardır. S eğrilikte ise biri göğüs, diğeri bel bölgesinde, ters yönlere bakan iki yay bulunur; bunlardan biri asıl (yapısal) eğrilik, diğeri gövdeyi dengelemek için gelişen ikincil eğrilik olabileceği gibi, ikisi birden yapısal da olabilir. Eğrilikler tepe noktasının yerine göre göğüs (torakal), göğüs-bel geçişi (torakolomber) ve bel (lomber) eğriliği olarak adlandırılır; göğüs bölgesindeki eğrilikler çoğunlukla sağa doğrudur.</p>
      <div class="sk-figs">
        <figure>{SK_SPINE("N")}<figcaption><b>Düz omurga</b>Arkadan bakıldığında omurlar üst üste dizilir.</figcaption></figure>
        <figure>{SK_SPINE("C")}<figcaption><b>C eğrilik</b>Tek yay; omuz ve bel hizası bozulabilir.</figcaption></figure>
        <figure>{SK_SPINE("S")}<figcaption><b>S eğrilik</b>Göğüs ve bel bölgesinde ters yönlü iki yay.</figcaption></figure>
      </div>
      <p class="sk-key">Çizimler eğrilik tiplerini anlatmak için basitleştirilmiştir; gerçek röntgen görüntüsü değildir.</p>
      <p class="soft" style="margin-top:14px">Cerrahlar ameliyat planlarken eğrilikleri daha ayrıntılı sınıflandırır (örneğin Lenke sınıflaması); fizyoterapistler de skolyoza özgü egzersizleri eğrilik tipine göre seçer. Bu yüzden aynı derecedeki iki eğrilik bile farklı bir program gerektirebilir.</p>
      <p class="sk-more">Ayrıntılı bilgi: <a href="https://www.srs.org/Files/Patient-Brochures/Patient.Adolescent_Idiopathic_Scoliosis_Handbook_for_Patients.pdf" target="_blank" rel="noopener">SRS hasta el kitabı (İngilizce)</a></p>
    </div>
  </section>

  <section id="cobb">
    <div class="wrap">
      <h2>Röntgen ve Cobb açısı</h2>
      <div class="sk-split">
        <div>
          <p class="soft">Skolyozun büyüklüğü ayakta çekilen tüm omurga röntgeninde <strong>Cobb açısı</strong> ile ölçülür. Eğriliğin iki ucunda, birbirine doğru en çok eğilmiş omurlar (uç omurlar) seçilir; bu omurların üst ve alt yüzeylerinden çizilen çizgiler arasındaki açı eğriliğin derecesidir. 10 derece ve üzeri skolyoz kabul edilir.</p>
          <p class="soft">Ölçümün bir payı vardır: Aynı röntgende farklı ölçümler arasında 5–10 derecelik fark olabilir, açı gün içinde de yaklaşık 5 derece değişebilir. Bu yüzden birkaç derecelik bir değişiklik tek başına ilerleme sayılmaz; karar, zaman içindeki ölçümlerin ve muayenenin birlikte değerlendirilmesiyle verilir.</p>
          <ul class="tx" style="margin-top:14px">
            <li><b>25 derecenin altı</b><span>Büyümesi süren çocuklarda genellikle yakın izlem; skolyoza özgü egzersizler ilk basamak olabilir.</span></li>
            <li><b>20–25 ile 40–45 derece</b><span>Büyümesi süren çocuklarda genellikle korse önerilir; egzersizler korsenin yanında sürdürülür.</span></li>
            <li><b>45–50 derecenin üzeri</b><span>Büyümesi süren çocuklarda ameliyat değerlendirilir. Bel eğriliklerinde eşik daha düşüktür (35–40 derece); bu sınırları aşan eğrilikler yetişkinlikte de ilerleme eğilimindedir.</span></li>
          </ul>
          <p class="sk-key" style="margin-top:10px">Bu sınırlar SRS hasta el kitabındaki genel yaklaşımdır; kesin karar hekiminizindir.</p>
        </div>
        <div>
          <div class="sk-figs one">
            <figure>{SK_COBB()}<figcaption><b>Cobb açısı</b>Sarı: uç omurlar; yeşil: eğriliğin tepe noktası. Kesikli çizgilerin kesiştiği yerdeki açı eğriliğin derecesidir.</figcaption></figure>
          </div>
        </div>
      </div>
      <h3 style="margin-top:26px">Evde kontrol ve kalan büyümenin ölçülmesi</h3>
      <div class="sk-figs two">
        <figure>{SK_ADAMS()}<figcaption><b>Öne eğilme testi</b>Öne eğilince sırtın bir tarafı yükselirse dönme vardır. Skolyometre bu farkı derece olarak ölçer.</figcaption></figure>
        <figure>{SK_RISSER()}<figcaption><b>Risser işareti</b>Leğen kemiği kenarındaki büyüme kıkırdağının kemikleşmesi 1'den 4'e ilerler, 5'te kaynaşır. 0–1 daha çok büyüme kaldığını gösterir.</figcaption></figure>
      </div>
      <p class="soft" style="margin-top:14px">Okul taramalarında gövdedeki dönme skolyometreyle ölçülür; Portekiz'de 966 öğrenciyle yapılan çalışmada 7 derece ve üzeri belirgin dönme olarak kabul edildi ve öğrencilerin %4,2'sinde görüldü. Risser işareti ise röntgende leğen kemiğinin kenarına bakılarak belirlenir ve kalan büyümeyi tahmin etmek için kullanılır.</p>
      <p class="sk-more">Ayrıntılı bilgi: <a href="https://images.radiopaedia.org/articles/cobb-angle/changesets/171866/edits?lang=us" target="_blank" rel="noopener">Radiopaedia, Cobb açısı (İngilizce)</a></p>
    </div>
  </section>

  <section id="turler">
    <div class="wrap">
      <h2>Türleri ve nedenleri</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>İdiyopatik</h3><p>En sık tip (yaklaşık %80). Görüldüğü yaşa göre bebeklik (3 yaş öncesi), çocukluk (3–10 yaş) ve ergenlik (10 yaş ve sonrası) olarak ayrılır; en sık ergenlik tipidir.</p></div>
        <div class="kind"><span class="n">2</span><h3>Doğumsal</h3><p>Anne karnında omurların eksik ya da yapışık gelişmesine bağlıdır; genellikle erken yaşta fark edilir.</p></div>
        <div class="kind"><span class="n">3</span><h3>Nöromüsküler ve sendromik</h3><p>Serebral palsi ya da kas hastalıkları gibi durumlarda kas dengesizliğine; Marfan ya da Ehlers-Danlos gibi bağ dokusu hastalıklarında doku gevşekliğine bağlı gelişebilir.</p></div>
        <div class="kind"><span class="n">4</span><h3>Yetişkin tipi</h3><p>Ergenlikte başlayıp yetişkinlikte yavaşça ilerleyen eğrilik ya da ileri yaşta disk ve eklem yıpranmasıyla sonradan ortaya çıkan (dejeneratif) skolyoz.</p></div>
      </div>
    </div>
  </section>

  <section id="buyume">
    <div class="wrap">
      <h2>Büyüme dönemi neden bu kadar önemli?</h2>
      <p class="soft">Eğrilik en çok ergenlikteki hızlı büyüme atağında ilerler. Büyüme atağının zirvesi kızlarda erkeklerden daha erken gelir; kızlarda ilk adetten önceki dönem en riskli dönemdir. Bu yüzden büyüme atağındaki gençlerde (kabaca 10–18 yaş arası) eğrilik birkaç ay gibi kısa sürelerde de artabilir.</p>
      <ul class="tx" style="margin-top:14px">
        <li><b>727 çocuk</b><span>Eğriliği 5–29 derece olan ve tedavi almayan çocukların büyüme bitene kadar izlendiği klasik çalışmada %23'ünde eğrilik ilerledi. İlerlemeyi en iyi eğriliğin büyüklüğü, yaş, Risser işareti ve ilk adetin olup olmadığı öngördü.</span></li>
        <li><b>%68'e karşı %23</b><span>20–29 derecelik eğriliklerde ilerleme olasılığı, büyümenin çoğu önünde olan çocuklarda (Risser 0–1) %68, büyümesi daha ilerlemiş olanlarda (Risser 2–4) yaklaşık %23 olarak bildirildi.</span></li>
        <li><b>%83'e karşı %4</b><span>Korse kullanan 120 kız çocukta, büyüme atağının zirvesinde eğriliği 30 dereceyi aşanların %83'ünde eğrilik 45 dereceye ve üzerine ilerledi; 30 derece ve altında olanlarda bu oran %4'tü. Çocukların %90'ında büyüme, zirveden sonraki 3,6 yıl içinde durdu.</span></li>
      </ul>
      <p class="soft" style="margin-top:14px">Büyüme bittikten sonra 30 derecenin altındaki eğrilikler nadiren ilerler. Daha büyük eğrilikler yetişkinlikte yavaş ilerleyebilir: Danimarka'da ortalama 41 yıl izlenen hastalarda eğrilikler yılda ortalama 0,2–0,5 derece arttı, ama kişiler arasındaki fark büyüktü. Büyüme sonunda eğriliği 50 dereceyi aşanlarda ileri yaşta nefes darlığı riski artıyor.</p>
    </div>
  </section>

  <section id="risk">
    <div class="wrap">
      <h2>Çanta, tek taraflı alışkanlıklar ve bağ dokusu esnekliği</h2>
      <p class="soft">Bu konu ailelerin en çok sorduğu konulardan biri. Araştırmaların gösterdikleriyle klinikte gördüklerimizi ayrı ayrı yazıyoruz.</p>
      <div class="sk-split" style="margin-top:12px">
        <div>
          <h3>Araştırmalar ne diyor?</h3>
          <ul class="dots">
            <li>SRS'ye göre ağır çanta, kötü duruş ve spor skolyoza yol açmaz ya da eğriliği kötüleştirmez; ancak ağır çanta sırt ve bel ağrısına yol açabilir.</li>
            <li>Portekiz'de 10–16 yaş arası 966 öğrencide çanta ağırlığı ve duruş alışkanlıkları skolyozla ilişkili bulunmadı; yanlış oturma ve ayakta durma alışkanlıkları ise bel ağrısıyla ilişkiliydi. Bu bir kesitsel çalışmadır; neden-sonuç ilişkisi göstermez.</li>
            <li>Bir çalışmada idiyopatik skolyozlu 70 çocuğun %51,4'ünde, sağlıklı akranlarının ise %19'unda yaygın eklem hipermobilitesi (bağ dokusu gevşekliğine bağlı aşırı eklem hareketliliği) vardı; gevşeklik eğriliğin derecesiyle ilişkili değildi. Yazarlar, fizyoterapi planlanırken bu çocuklarda eklem gevşekliğine bakılmasını öneriyor.</li>
            <li>Ritmik cimnastik yapan 100 kız çocukta skolyoz sıklığı %12, akranlarında %1,1'di. Yazarlar; eklem gevşekliği, gecikmiş ergenlik ve büyüyen omurgaya tekrar tekrar binen tek taraflı yükün birlikteliğini “tehlikeli üçlü” olarak tanımladı. Bu da bir gözlem çalışmasıdır.</li>
          </ul>
        </div>
        <div>
          <h3>Klinikte ne görüyoruz?</h3>
          {SK_CLIN("Büyüme atağındaki gençlerde çantayı hep aynı omuzda taşımak, ağır bir eşyayı ya da çalgıyı sürekli aynı tarafta taşımak ve tek tarafı yükleyen alışkanlıklar duruş asimetrisini belirginleştirebiliyor. Benign eklem hipermobilite sendromunda olduğu gibi bağ dokusu esnekliği de eşlik ediyorsa bu asimetrilerin ve sırt ağrısının daha belirgin olabildiğini görüyoruz. Bu, tek taraflı yükün yapısal skolyoza yol açtığı anlamına gelmez; ama büyüme döneminde yükü iki tarafa dağıtmak için iyi bir neden.")}
          <ul class="dots" style="margin-top:14px">
            <li>Çantayı iki askısıyla, iki omuzda taşıyın; ağırlık vücut ağırlığının %10–15'ini geçmesin, ağır eşyalar sırta yakın dursun.</li>
            <li>Tek taraflı bir spor ya da etkinlik yapılıyorsa sporu bırakmak gerekmez; karşı tarafı da çalıştıran dengeleyici egzersizler eklenebilir.</li>
            <li>Bağ dokusu çok esnek olan çocuklarda germe yerine güçlendirme ve duruş kontrolü ön plana çıkar.</li>
          </ul>
          <p class="sk-more">Ayrıntılı bilgi: <a href="eklem-hipermobilitesi.html">Eklem hipermobilitesi rehberi</a></p>
        </div>
      </div>
    </div>
  </section>

  <section id="tarihce">
    <div class="wrap">
      <p class="eyebrow">Geçmişten bugüne</p>
      <h2>Skolyoz tedavisinin kısa tarihi</h2>
      <p class="soft">Skolyoz tedavisi germe masalarından bilgisayarla tasarlanan korselere ve büyümeyi yönlendiren ameliyatlara uzanan uzun bir yol izledi. Bazı yöntemler denendi ve bırakıldı; bugün kullanılanların çoğu son 30 yılda randomize çalışmalarla sınandı.</p>
      <ol class="sk-tl">
        <li><b>Antik çağ</b><span>Hipokrat, omurgayı germe ve bastırmaya dayanan bir masa kullandı.</span></li>
        <li><b>1911</b><span>İlk omurga füzyonu ameliyatı yapıldı (önce omurga tüberkülozunda).</span></li>
        <li><b>1921</b><span>Katharina Schroth, kendi skolyozlu gövdesinin nefesle nasıl değiştiğini gözlemleyerek nefes ve duruşa dayalı üç boyutlu egzersiz yöntemini geliştirdi.</span></li>
        <li><b>1945</b><span>Milwaukee korsesi kullanılmaya başlandı.</span></li>
        <li><b>1950</b><span>Risser alçısı ve kalan büyümeyi gösteren Risser işareti tanımlandı.</span></li>
        <li><b>1960</b><span>Harrington çubukları ile metal implantla düzeltme dönemi başladı.</span></li>
        <li><b>1972</b><span>Koltuk altına kadar uzanan, daha az göze batan Boston korsesi geliştirildi.</span></li>
        <li><b>1980'ler</b><span>Kaslara elektrik uyarımı denendi; 1993'te sunulan çok merkezli çalışmada korse takan kızların yaklaşık %80'inde ilerleme durdu, elektrik uyarımı ve yalnızca izlem gruplarında ise yaklaşık %70'inde eğrilik 5 yılda 6 derece ya da daha fazla arttı. Yöntem bırakıldı.</span></li>
        <li><b>1983</b><span>Cotrel-Dubousset sistemiyle omurganın üç boyutlu düzeltilmesi yaygınlaştı; 1990'larda göğüs omurlarına pedikül vidaları uygulanmaya başlandı.</span></li>
        <li><b>2013</b><span>BrAIST, korsenin ameliyat gereksinimini azalttığını gösteren ilk büyük randomize çalışma oldu.</span></li>
        <li><b>2016–2018</b><span>Uluslararası SOSORT kılavuzu skolyoza özgü fizyoterapi egzersizlerini ve korseyi büyüme dönemindeki tedavinin temeline yerleştirdi.</span></li>
        <li><b>2019</b><span>ABD'de, büyüyen çocuklarda eğriliği omurgayı kaynaştırmadan düzeltmeyi amaçlayan omurga bağlama (tethering) cihazına insani kullanım izni verildi.</span></li>
        <li><b>2024</b><span>Cochrane egzersiz derlemesi güncellendi; İsveç'teki CONTRAIS çalışması gece korsesinin orta derecedeki eğriliklerde ilerlemeyi azaltabildiğini gösterdi.</span></li>
      </ol>
    </div>
  </section>

  <section id="tedavi">
    <div class="wrap">
      <h2>Tedavi yöntemleri: kime, ne amaçla, kanıt ne diyor?</h2>
      <p class="soft">Uluslararası Skolyoz Ortopedik ve Rehabilitasyon Tedavisi Derneği'nin (SOSORT) kılavuzuna göre büyüme dönemindeki tedavinin amacı eğriliğin ilerlemesini önlemek ya da sınırlamaktır. Tedavi; eğrilik açısına, eğrilik tipine, kalan büyümeye, gövde görünümüne ve kişinin tercihine göre planlanır.</p>
      <div class="sk-cmp">
        <div class="kind"><h3>İzlem</h3><dl><dt>Kime</dt><dd>Küçük eğrilikler; büyümesi bitmiş ve ilerlemeyen eğrilikler.</dd><dt>Amaç</dt><dd>İlerlemeyi zamanında fark etmek.</dd><dt>Dikkat</dt><dd>Büyüme atağında kontroller sık olmalı.</dd></dl></div>
        <div class="kind"><h3>Skolyoza özgü egzersiz</h3><dl><dt>Kime</dt><dd>Küçük ve orta eğrilikler; korse kullananlarda korsenin yanında.</dd><dt>Amaç</dt><dd>İlerlemeyi sınırlamak, duruşu ve gövde görünümünü iyileştirmek.</dd><dt>Kanıt</dt><dd>Düşük ya da çok düşük güvenilirlikte; bazı çalışmalar yararlı, bazıları genel egzersizden farksız.</dd></dl></div>
        <div class="kind"><h3>Gece korsesi</h3><dl><dt>Kime</dt><dd>Orta derecede, büyümesi süren ve tam gün korse istemeyen gençler.</dd><dt>Amaç</dt><dd>Yalnızca uykuda takılarak ilerlemeyi durdurmak.</dd><dt>Kanıt</dt><dd>CONTRAIS çalışmasında başarı %76; yalnızca fiziksel aktivitede %53.</dd></dl></div>
        <div class="kind"><h3>Tam gün korse</h3><dl><dt>Kime</dt><dd>Büyümesi süren, eğriliği 20–25 ile 40–45 derece arasında olanlar.</dd><dt>Amaç</dt><dd>Ameliyat sınırına ulaşmayı önlemek; eğriliği düzeltmez.</dd><dt>Kanıt</dt><dd>BrAIST'te başarı %72, izlemde %48; günde 13 saat ve üzeri takanlarda %90'ın üzerinde.</dd></dl></div>
        <div class="kind"><h3>Füzyon ameliyatı</h3><dl><dt>Kime</dt><dd>İlerleyen ileri eğrilikler; korsenin yetmediği durumlar.</dd><dt>Amaç</dt><dd>Eğriliği kısmen düzeltip kaynaştırarak sabitlemek.</dd><dt>Dikkat</dt><dd>En sık yapılan ameliyat; düzeltme genellikle kısmidir.</dd></dl></div>
        <div class="kind"><h3>Omurga bağlama (tethering)</h3><dl><dt>Kime</dt><dd>Seçilmiş, büyümesi süren gençler.</dd><dt>Amaç</dt><dd>Büyümeyi yönlendirerek kaynaştırmadan düzeltmek.</dd><dt>Kanıt</dt><dd>Onaya dayanak olan 57 hastanın 43'ü 2 yılda füzyondan kaçındı; kordon kopması ve aşırı düzelme gibi sorunlar bildirildi.</dd></dl></div>
      </div>

      <h3 style="margin-top:30px">Skolyoza özgü fizyoterapi egzersizleri</h3>
      <p class="soft">Bu egzersizler üç temel ilkeye dayanır: gövdeyi üç boyutlu olarak kendi kendine düzeltmek, düzeltilmiş duruşu sabit tutmak ve bu duruşu günlük hayata (oturma, çanta taşıma, ders çalışma) taşımak. Bunlara eğitim ve gerektiğinde psikolojik destek eşlik eder. Dünyada en bilinen yedi okul vardır: Lyon (Fransa), Schroth (Almanya), SEAS (İtalya), Barselona (BSPTS, İspanya), Dobomed ve FITS (Polonya) ve Side Shift (İngiltere). Schroth yönteminde dönme yönüne göre yönlendirilen nefes de programın parçasıdır.</p>
      <p class="soft">Kanıtlar karışık. Türkiye'de 45 ergenle yapılan bir çalışmada klinikte fizyoterapist eşliğinde yapılan Schroth egzersizleri 24 haftada eğrilik açısını, omurga rotasyonunu ve kaburga kamburunu azalttı; evde tek başına egzersiz yapan ve egzersiz yapmayan gruplarda ise bulgular kötüleşti. 13 çalışmayı ve 583 ergeni kapsayan 2024 tarihli Cochrane derlemesinde ise kanıtların güvenilirliği düşük ya da çok düşüktü: Skolyoza özgü egzersizler genel egzersize göre gövde rotasyonunu muhtemelen azaltıyor ve korseyle birlikte yapıldığında ilerlemeyi biraz azaltabiliyor. İsveç'te 135 ergenle yapılan CONTRAIS çalışmasında ise orta derecedeki eğriliklerde skolyoza özgü egzersiz, yalnızca fiziksel aktiviteden daha iyi sonuç vermedi (başarı %58'e karşı %53).</p>
      {SK_CLIN("Egzersizden en çok yarar görenler, programı düzenli sürdüren ve düzeltilmiş duruşu günlük hayatına taşıyabilen gençler oluyor. Egzersizin katkısı yalnızca açıda değil; duruş farkındalığında, ağrıda ve gencin kendi bedenine güveninde de görülüyor. Korse gereken bir eğrilikte egzersiz korsenin yerine geçmez.")}

      <h3 style="margin-top:30px">Korse</h3>
      <p class="soft">Korse eğriliği düzeltmez; büyüme bitene kadar ilerlemesini durdurmayı amaçlar. Bugün çoğunlukla koltuk altına kadar uzanan sert korseler (Boston gibi) ve eğriliğe karşı üç boyutlu baskı uygulayan Chêneau tipi korseler kullanılıyor; yalnızca uykuda takılan gece korseleri de bir seçenek. ABD ve Kanada'da 383 ergenle yapılan BrAIST çalışmasında eğriliğin ameliyat sınırı olan 50 dereceye ulaşmasını önlemede başarı oranı korse takanlarda %72, yalnızca izlenenlerde %48 oldu. Korsenin etkisi takılan süreye bağlıydı. İsveç'teki CONTRAIS çalışmasında gece korsesi, orta derecedeki eğriliklerde 6 dereceden fazla ilerlemeyi önlemede yalnızca fiziksel aktiviteden daha başarılıydı (%76'ya karşı %53).</p>
    </div>
  </section>

  <section id="ameliyat">
    <div class="wrap">
      <h2>Ameliyat, gövde dengesi ve yüksek dereceli eğrilikler</h2>
      <div class="sk-split">
        <div>
          <p class="soft">Ameliyat genellikle ameliyatsız tedavinin yetmediği durumlarda düşünülür. Büyümesi süren gençlerde eğriliğin 45 dereceyi aşması, büyümesi bitmiş kişilerde 40–50 dereceyi aşması ve ilerlemesi en sık ölçütlerdir. Ağrının ameliyatsız tedaviyle geçmemesi, akciğer işlevinin etkilenmesi ve görünüm de kararda yer alır. En sık yapılan ameliyat, omurgayı vida ve çubuklarla düzeltip kaynaştıran füzyondur.</p>
          <p class="soft">Yüksek derece tek başına ameliyat demek değildir. ABD'de tedavi edilmeden yaklaşık 50 yıl izlenen 117 hastada sırt ağrısı akranlarından daha sık görüldü, ama günlük işleri yapabilme yetenekleri farklı değildi ve ölüm oranı artmamıştı; büyüme sonunda 50 dereceyi aşan eğrilik ise ileri yaşta nefes darlığı riskini artırıyordu. Bu yüzden karar; eğriliğin ilerleyip ilerlemediğine, gövdenin dengeli olup olmadığına, ağrıya, akciğer işlevine ve kişinin beklentisine göre omurga cerrahıyla birlikte verilir.</p>
          {SK_CLIN("Büyümesi tamamlanmış, gövdesi dengede (vücudu eğriliği dengelemiş), eğriliği ilerlemeyen ve günlük hayatı kısıtlanmayan bazı hastalarda, açı yüksek olsa bile cerrahların ameliyatı önermediğini ya da ertelediğini görüyoruz. Bu hastalarda düzenli kontrol, güçlendirme ve duruş egzersizleri ön planda kalıyor. Gövde dengesinin bozulması, ağrının artması ya da eğriliğin ilerlemesi kararı değiştirebilir.")}
        </div>
        <div>
          <div class="sk-figs two">
            <figure>{SK_BALANCE(True)}<figcaption><b>Dengeli gövde</b>Boyun dibinden sarkıtılan çekül çizgisi leğen kemiğinin ortasına düşer.</figcaption></figure>
            <figure>{SK_BALANCE(False)}<figcaption><b>Dengesiz gövde</b>Gövde bir yana kaymıştır; çekül çizgisi leğen kemiğinin dışına düşer.</figcaption></figure>
          </div>
          <p class="sk-key">Basitleştirilmiş çizim; gerçek röntgen değildir.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde</p>
      <h2>Kontrol ve genel egzersizler</h2>
      <div class="callout">
        <p><strong>Skolyoz egzersizleri kişiye özel olmalıdır.</strong> Eğriliğin yeri, yönü, derecesi, esnekliği, kalan büyüme ve ağrı her gençte farklıdır; tek tarafa yönelik egzersizler (örneğin bir tarafa ağırlık verilen yan köprü ya da germe) eğrilik tipine göre seçilmezse işe yaramayabilir. Bu yüzden skolyoza özgü egzersizleri muayene ve röntgene göre, bu yöntemlerde eğitim almış bir fizyoterapistle planlayın.</p>
        <p>Aşağıdaki egzersizler ise vücudun iki tarafını eşit çalıştıran genel egzersizlerdir. <strong>Ağrı yapmadığı sürece bunları genellikle güvenle yapabilirsiniz</strong>; gövde kaslarını güçlendirir ve duruşu destekler, ama eğriliği tek başına düzeltmez ve skolyoza özgü egzersizlerin yerini tutmaz. Ağrı artarsa, kol ya da bacaklarda uyuşma ve karıncalanma olursa egzersizi bırakın ve hekiminize danışın.</p>
      </div>
      <p class="soft" style="margin-top:18px">İlk karttaki test, büyüme döneminde evde yapabileceğiniz basit bir kontroldür.</p>
      {ex_grid(["adams", "sc_bird", "sc_side", "sc_cat", "sc_bridge", "sc_scap"])}
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Yetişkinlerde skolyoz</h2>
        <p class="soft">Yetişkinlerde iki tip görülür: ergenlikte başlayıp yavaşça ilerleyen idiyopatik skolyoz ve ileri yaşta disklerin ve küçük eklemlerin yıpranmasıyla sonradan gelişen dejeneratif skolyoz. SRS'ye göre 30 derecenin altındaki eğriliklerde bel ağrısı riski skolyozu olmayanlarla benzer; 50–60 derecenin üzerindeki tedavi edilmemiş eğriliklerde ise bel ağrısı daha olasıdır.</p>
        <p class="sk-more">Ayrıntılı bilgi: <a href="bel-agrisi.html">Bel ağrısı</a> ve <a href="dar-kanal.html">Dar kanal</a> rehberleri</p>
      </div>
      <div>
        <h2>Sporu bırakmayın</h2>
        <p class="soft">SRS'ye göre sırt ağrısı olmadıkça skolyozlu çocuklar her sporu yapabilir. Uluslararası kılavuz da sporun genel sağlık ve psikolojik faydaları nedeniyle korse tedavisi sırasında bile bırakılmamasını öneriyor; ancak hiçbir spor tek başına tedavi yerine geçmez.</p>
      </div>
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
     "Skolyoz nedir, C ve S eğrilik, Cobb açısı ve büyüme döneminin önemi; çanta, tek taraflı alışkanlıklar ve bağ dokusu esnekliği; geçmişten bugüne tedaviler, egzersiz, korse ve ameliyatın karşılaştırması.",
     "skolyoz.html", SC_CSS, SC_BODY, "",
     seo_title="Skolyoz: C ve S Eğrilik, Cobb Açısı, Egzersiz, Korse ve Ameliyat | İhsan Eren",
     condition="Skolyoz", faq_items=SC_FAQ)

# -*- coding: utf-8 -*-
# Tenisçi dirseği sayfası. hip_part.py'den sonra exec edilir.

TABLE = '<path class="obj" d="M8 70 H72 M64 70 V112"/>'

# İzometrik bilek açma: ön kol masada, avuç aşağı; diğer el elin üstüne bastırır, el yerinde kalır.
SV["isowe"] = fig(TABLE +
    '<path class="fig" d="M14 64 H62"/>'
    '<path class="fig hl" d="M62 64 H86"/>'
    '<path class="fig" d="M76 30 V56"/><rect x="70" y="54" width="14" height="6" rx="2" fill="#2A6F6B"/>'
    '<g fill="none" stroke="#C8963E" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M92 38 V50 M88 46 L92 50 L96 46"><animate attributeName="opacity" values="0;1;0" dur="1.6s" repeatCount="indefinite"/></path>'
    '<path d="M100 74 V62 M96 66 L100 62 L104 66"><animate attributeName="opacity" values="0;1;0" dur="1.6s" begin="0.8s" repeatCount="indefinite"/></path></g>',
    "İzometrik bilek açma")

# Eksantrik bilek açma: ön kol masada, el masanın kenarından taşar; ağırlık yavaşça indirilir.
SV["eccwe"] = fig(TABLE +
    '<path class="fig" d="M14 64 H62"/>'
    f'<g>{anim_t("-40 62 64;45 62 64;-40 62 64", dur="4s", kt="0;0.75;1", typ="rotate")}'
    '<path class="fig hl" d="M62 64 H82"/><rect x="80" y="54" width="9" height="20" rx="3" fill="#C8963E"/></g>',
    "Eksantrik bilek açma")

# Top sıkma (yandan)
SV["grip"] = fig(
    '<path class="fig" d="M56 116 L56 84"/>'
    '<rect x="48" y="54" width="16" height="32" rx="7" fill="#2A6F6B"/>'
    '<circle cx="72" cy="46" r="9" fill="#C8963E"><animate attributeName="r" values="9.5;7.5;9.5" dur="2.4s" repeatCount="indefinite"/></circle>'
    f'<path class="fig hl" d="M58 56 Q60 34 74 34 Q86 38 82 52">{anim_d("M58 56 Q60 34 74 34 Q86 38 82 52;M58 56 Q62 38 73 37 Q82 40 79 50;M58 56 Q60 34 74 34 Q86 38 82 52", dur="2.4s")}</path>'
    '<path class="fig" d="M60 76 L72 60"/>',
    "Top sıkma")

SV["wext_st"] = SV["wflex"].replace("<figcaption>Bilek bükücü germe</figcaption>", "<figcaption>Bilek açıcı germe</figcaption>")
SV["scap3"] = SV["scap"]
SV["row2"] = SV["row"]

EXT.update({
 "isowe": ("İzometrik bilek açma", "Ön kolunuzu masaya koyun, avucunuz aşağı baksın, eliniz masanın kenarından taşsın. Bileğinizi yukarı kaldırmaya çalışırken diğer elinizle elinizin üstüne bastırın; el yerinden oynamasın. Ağrıyı belirgin artırmayan bir kuvvetle tutun; kas boyu değişmeden çalışır (izometrik). Ağrılı dönemde de genellikle iyi tolere edilir.", "30–45 saniye, 5 tekrar, günde 1–2 kez"),
 "eccwe": ("Eksantrik bilek açma", "Ön kolunuzu masaya koyun, avucunuz aşağı baksın. Elinize yarım litrelik dolu bir su şişesi gibi hafif bir ağırlık alın. Diğer elinizle yardım ederek bileğinizi yukarı kaldırın, sonra yardımı bırakıp ağırlığı 3–4 saniyede yavaşça aşağı indirin; kas uzayarak çalışır (eksantrik). Kolaylaştıkça ağırlığı artırın.", "15 tekrar, 3 set, günde 1 kez"),
 "wext_st": ("Bilek açıcı germe", "Kolunuzu önünüze uzatın, dirseğiniz düz, avucunuz aşağı baksın. Diğer elinizle elinizin sırtından tutup bileğinizi nazikçe aşağı ve kendinize doğru bükün; ön kolunuzun dış yüzünde, ağrıyı belirgin artırmayacak kadar gerilme hissedin.", "20–30 saniye, 3 tekrar"),
 "grip": ("Top sıkma", "Elinize yumuşak bir top ya da rulo yapılmış bir havlu alın. Ağrıyı artırmayacak bir kuvvetle sıkın, birkaç saniye tutun ve bırakın. Kavrama gücünü artırır; ağrı artıyorsa daha yumuşak bir nesne seçin.", "10 tekrar, günde 2–3 kez"),
 "scap3": EXT["scap"],
 "row2": EXT["row"],
})

DIRSEK_FAQ = [
 ("Tenis oynamıyorum, neden tenisçi dirseği oldum?", "Adına rağmen hastaların çoğu tenis oynamaz. Sorun, bileği ve parmakları açan kasların dirseğin dış yüzüne yapıştığı ortak kirişin aşırı yüklenmesidir. El ve bileğin yoğun kullanıldığı işlerde görülme sıklığı %29'a kadar çıkabiliyor; en sık 40–60 yaş arasında görülür."),
 ("Kortizon iğnesi yaptırmalı mıyım?", "Kortizon iğnesi kısa sürede ağrıyı azaltabilir, ancak uzun vadede sonuçları kötüleştirebilir. 165 hastalık bir çalışmada 1 yılın sonunda tamamen ya da çok iyileşenlerin oranı kortizon grubunda %83, plasebo iğne grubunda %96 oldu; nüks ise kortizon grubunda %54, plasebo grubunda %12 idi. 30 çalışmayı ve 2.123 kişiyi kapsayan bir meta-analizde egzersiz, kısa dönem ağrı dışında tüm sonuçlarda kortizon iğnesinden daha iyiydi; ancak egzersizin pasif tedavilere üstünlüğü küçüktü ve kanıtın kesinliği düşük ile çok düşük arasındaydı."),
 ("Dirsek bandı işe yarar mı?", "Ön kola takılan bant ya da bilek desteği, aktivite sırasında kullanıldığında ağrıyı hemen hafifletebilir. Uzun vadeli etkisi konusunda ise kılavuz bir öneride bulunamıyor. Bant tedavinin tamamı değil, yük ayarlamaya yardımcı bir araçtır."),
 ("Ne kadar sürede geçer?", "Sabır gerektirir. Birinci basamakta (aile hekimine) başvuranların yarısından fazlasında şikâyetler 1 yıl sonra da sürebiliyor ve 6–12 ay sonunda şikâyetlerin tam geçmemesi ya da geri dönmesi %20–38 oranında bildiriliyor. Yükü kademeli artırılan bir egzersiz programına düzenli devam etmek bu süreci yönetmenin temelidir. 198 kişiyle yapılan bir çalışmada fizyoterapi alanların da bekleyip izleyenlerin de çoğu 1 yılın sonunda iyileşmişti; kortizon iğnesiyle ilk 6 haftada düzelen 65 kişinin 47'sinde ise şikâyetler sonradan geri döndü."),
 ("Röntgen ya da MR çektirmem gerekir mi?", "Çoğu zaman gerekmez. Tanı öykü ve muayeneyle konur. İngiliz Dirsek ve Omuz Derneği'nin (BESS) 2023 bakım yolu, görüntülemenin yalnızca tanıdan emin olunamadığında düşünülmesini öneriyor; ABD fizyoterapi kılavuzu da röntgenin daha çok uzun süren ve tedaviye yanıt vermeyen durumlarda başka nedenleri dışlamak için istendiğini belirtiyor."),
 ("Ameliyat gerekir mi?", "Çok az kişide. BESS'e göre 3–6 ay ameliyatsız tedaviye rağmen düzelmeyen kişilerde ameliyat düşünülebilir; ancak ameliyatın sahte ameliyata üstün olduğunu gösteren kanıt yok. BESS'in incelediği, sahte ameliyatla karşılaştıran tek çalışmada her grupta 13 hasta vardı ve iki grup arasında fark bulunmadı. Bu yüzden ameliyat kararı, beklentiler açıkça konuşularak verilmelidir."),
 ("Kolumu tamamen dinlendirmeli miyim?", "Hayır. Ağrıyı belirgin artıran kavrama ve kaldırma işlerini geçici olarak azaltın, ama kolu askıya almayın. Kiriş, kademeli olarak artırılan yüke uyum sağlayarak güçlenir; ABD kılavuzu da uzman görüşüne dayanarak, özellikle kolunu yoğun kullananlarda yükün aşamalı olarak yeniden artırılmasını öneriyor."),
]

DIRSEK_SRC = [
 "Singh HP, Watts AC, Bateman M, et al.; BESS LET Guideline Development Group. " + ext("https://escholarship.org/content/qt7fk3s418/qt7fk3s418.pdf", "BESS patient care pathway: tennis elbow") + ". Shoulder Elbow. 2023;15(4):348-359.",
 "Smidt N, et al. " + ext("https://www.qxmd.com/r/11879861", "Corticosteroid injections, physiotherapy, or a wait-and-see policy for lateral epicondylitis: a randomised controlled trial") + ". Lancet. 2002.",
 "Morris T. " + ext("https://www.thomas-morris.uk/?p=1966", "The lawn-tennis elbow") + ". (\"Lawn-tennis elbow\" başlıklı 1883 British Medical Journal mektubu ve Henry Morris'in 1882 Lancet yazısı üzerine tarih yazısı.)",
 "Kroslak M, Murrell GAC. Am J Sports Med. 2018 (ameliyat ile sahte ameliyatı karşılaştıran randomize çalışma). Özet: " + ext("https://www.mendcolorado.com/physical-therapy-blog/2018/3/21/no-difference-between-surgery-and-placebo-surgery-for-tennis-elbow/", "Mend Colorado") + ".",
 "Coombes BK, Bisset L, Brooks P, Khan A, Vicenzino B. " + ext("https://jamanetwork.com/journals/jama/fullarticle/1568252", "Effect of corticosteroid injection, physiotherapy, or both on clinical outcomes in patients with unilateral lateral epicondylalgia: a randomized controlled trial") + ". JAMA. 2013;309(5):461-469.",
 "Lucado AM, Day JM, Vincent JI, et al. " + ext("https://www.orthopt.org/uploads/content_files/files/jospt.2022.0302.pdf", "Lateral elbow pain and muscle function impairments: clinical practice guidelines linked to the International Classification of Functioning, Disability and Health") + ". J Orthop Sports Phys Ther. 2022;52(12):CPG1-CPG111.",
 "Bisset LM, Vicenzino B. " + ext("https://pubmed.ncbi.nlm.nih.gov/26361816/", "Physiotherapy management of lateral epicondylalgia") + ". J Physiother. 2015;61(4):174–181",
 "Physiopedia. " + ext("https://www.physio-pedia.com/Lateral_Epicondylitis", "Lateral Epicondylitis") + ".",
 "Karanasios S, Korakakis V, Whiteley R, et al. " + ext("https://bjsm.bmj.com/content/55/9/477", "Exercise interventions in lateral elbow tendinopathy have better outcomes than passive interventions, but the effects are small: a systematic review and meta-analysis of 2123 subjects in 30 trials") + ". Br J Sports Med. 2021;55(9):477–485.",
 "Bisset L, Beller E, Jull G, Brooks P, Darnell R, Vicenzino B. " + ext("https://doi.org/10.1136/bmj.38961.584653.AE", "Mobilisation with movement and exercise, corticosteroid injection, or wait and see for tennis elbow: randomised trial") + ". BMJ. 2006;333(7575):939-944.",
]

DIRSEK_TL = [
 ("1882", "Middlesex Hastanesi'nden cerrah Henry Morris, çoğunlukla binicilik yaralanmalarını ele aldığı bir Lancet yazısında bu tabloyu \"çim tenisi kolu\" olarak andı."),
 ("1883", "British Medical Journal'a yazılan bir okur mektubunda \"Lawn-Tennis Elbow\" (çim tenisi dirseği) başlığı kullanıldı. Henry Morris iki hafta kadar sonra yanıt vererek okurları bir önceki yıl Lancet'te yayımladığı yazısına yönlendirdi."),
 ("2002", "Aile hekimlerine başvuran 185 hastayla yapılan çalışmada kortizon iğnesi 6. haftada en hızlı sonucu verdi (%92 başarı); ancak 52. haftada başarı fizyoterapi grubunda %91, bekle-gör grubunda %83, iğne grubunda %69'du. İğnenin ardından şikâyetlerin geri dönmesi sıktı."),
 ("2006", "198 kişiyle yapılan çalışmada 1 yılın sonunda fizyoterapi alanların da bekleyip izleyenlerin de çoğu iyileşmişti; kortizon iğnesiyle ilk 6 haftada düzelen 65 kişinin 47'sinde şikâyetler sonradan geri döndü."),
 ("2013", "Avustralya'da 165 hastayla yapılan plasebo kontrollü çalışmada 1 yılın sonunda tamamen ya da çok iyileşenler kortizon iğnesi grubunda %83, plasebo iğne grubunda %96'ydı; nüks kortizon grubunda %54, plaseboda %12 oldu."),
 ("2018", "Ameliyatı sahte (plasebo) ameliyatla karşılaştıran, BESS'e göre bu türdeki tek çalışmada iki grup da 6. ayda düzeldi ve aralarında fark bulunmadı. Çalışma erken durduruldu; her grupta yalnızca 13 hasta vardı."),
 ("2021", "30 çalışmayı ve 2.123 kişiyi inceleyen bir meta-analiz, egzersizin pasif tedavilerden daha iyi olduğunu, ancak farkın küçük ve kanıtın kesinliğinin düşük ya da çok düşük olduğunu düşündürdü."),
 ("2022", "Amerikan Fizyoterapi Derneği'nin (APTA) kılavuzu (JOSPT) yayımlandı: bileği açan kaslara direnç egzersizleri, dirsek mobilizasyonu, sert bantlama ve kuru iğneleme B düzeyinde önerildi."),
 ("2023", "İngiliz Dirsek ve Omuz Derneği'nin (BESS) hasta bakım yolu yayımlandı: fizyoterapi güçlü şekilde öneriliyor; kortizon iğnesi ve şok dalga tedavisi güçlü şekilde önerilmiyor."),
]

DIRSEK_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Tenisçi dirseği (lateral epikondilit)</h1>
    <p class="lede">Dirseğin dış yüzünde, kavramakla ve bileği kaldırmakla artan ağrıdır. Adına rağmen hastaların çoğu tenis oynamaz: bileği açan kasların ortak kirişinin aşırı yüklenmesiyle ortaya çıkar. Kademeli güçlendirme egzersizleri tedavinin temelidir; çoğu kişi bir yıl içinde belirgin şekilde düzelir, ama süreç sabır gerektirir.</p>
    <p class="meta">Son güncelleme: 31 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>Binde 2–5</b><span>ABD'de bir nüfus çalışmasında yıllık görülme sıklığı (2000–2012)</span></div>
        <div class="stat"><b>40–60 yaş</b><span>En sık görüldüğü yaş aralığı</span></div>
        <div class="stat"><b>%29'a kadar</b><span>El ve bileğin yoğun kullanıldığı işlerde çalışanlarda yaygınlık</span></div>
        <div class="stat"><b>%54</b><span>Kortizon iğnesi yapılanlarda 1 yıl içinde nüks (yeniden başlama); plasebo iğnede %12 (165 hastalık bir çalışma)</span></div>
      </div>
      {g_toc([("nedir", "Nedir?"), ("tani", "Nasıl tanınır?"), ("seyir", "Ne kadar sürer?"), ("kortizon", "Kortizon iğnesi"), ("tarihce", "Geçmişten bugüne"), ("tedavi", "Tedavi seçenekleri"), ("egzersizler", "Egzersizler"), ("gunluk", "Günlük hayatta"), ("videolar", "Videolar"), ("sss", "Sık sorulan sorular"), ("uyari", "Uyarı işaretleri")])}
    </div>
  </section>

  <section id="nedir">
    <div class="wrap two">
      <div>
        <h2>Nedir?</h2>
        <p class="soft">Bileği ve parmakları geriye doğru açan kaslar, dirseğin dış yüzündeki kemik çıkıntısına (lateral epikondil) ortak bir kirişle yapışır. Bu kirişin kaldırabileceğinden fazla ya da alışık olmadığı biçimde yüklenmesi ağrıya yol açar. Sorunun iltihaptan çok kirişte yıpranma ve yüke uyum sağlamada zorlanma olduğu düşünülüyor; bu yüzden "lateral dirsek tendinopatisi" adı da kullanılır.</p>
      </div>
      <div>
        <h2>Belirtiler ve risk etkenleri</h2>
        <ul class="dots">
          <li>Dirseğin dış yüzünde, bazen ön kola yayılan ağrı</li>
          <li>Kavrarken, çanta taşırken, kapı kolu ya da kavanoz kapağı çevirirken artan ağrı</li>
          <li>Kavrama gücünde azalma, fincan tutarken zorlanma</li>
          <li>Risk etkenleri: 40–60 yaş, el ve bileğin yoğun, tekrarlayan kullanıldığı işler, raket sporları</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="tani">
    <div class="wrap">
      <h2>Nasıl tanınır?</h2>
      <p class="soft">Tanı öykü ve muayeneyle konur; iki kılavuz da bunu temel alıyor.</p>
      <div class="kinds">
        <div class="kind"><h3>Muayene testleri</h3><p>Bileği dirence karşı yukarı kaldırırken (Cozen testi) ya da orta parmağı dirence karşı kaldırırken (Maudsley testi) dirseğin dış yüzünde ağrı olması tanıyı destekler. Bu testleri destekleyen kanıt zayıftır; bulgular birlikte değerlendirilir.</p></div>
        <div class="kind"><h3>Görüntüleme ne zaman?</h3><p>Çoğu zaman gerekmez. BESS görüntülemenin yalnızca tanıdan emin olunamadığında düşünülmesini öneriyor. Röntgen daha çok uzun süren, tedaviye yanıt vermeyen durumlarda başka nedenleri dışlamak için istenir; gerekirse ultrason ya da MR kullanılabilir.</p></div>
        <div class="kind"><h3>Başka ne olabilir?</h3><p>Ön koldaki bir sinirin (radyal sinir) sıkışması, boyundan yansıyan ağrı ve dirsek ekleminin kendi sorunları benzer ağrı yapabilir. Elde uyuşma ya da karıncalanma varsa bu nedenler ayrıca değerlendirilir.</p></div>
      </div>
    </div>
  </section>

  <section id="seyir">
    <div class="wrap">
      <h2>Ne kadar sürer?</h2>
      <p class="soft">Tenisçi dirseği çoğu zaman zamanla düzelir, ama bu aylar sürebilir. BESS'in aktardığı verilere göre ilk yıl içinde hastaların %89'unda genel bir iyileşme oluyor ve düzelme ilk aylarda daha hızlı. Öte yandan ABD fizyoterapi kılavuzu, birinci basamakta (aile hekimine) başvuranların yarısından fazlasında 1 yıl sonra da bir miktar şikâyet sürebildiğini ve 6–12 ay içinde şikâyetlerin tam geçmemesi ya da geri dönmesinin %20–38 oranında görüldüğünü belirtiyor.</p>
      <div class="callout">
        <p>Yani "düzelme" ile "tamamen geçme" aynı şey değil: çoğu kişi belirgin şekilde rahatlar, bazılarında hafif şikâyetler uzun süre kalabilir. Yükü kademeli artırılan bir egzersiz programına düzenli devam etmek bu süreci yönetmenin temelidir.</p>
      </div>
    </div>
  </section>

  <section id="kortizon">
    <div class="wrap">
      <h2>Kortizon iğnesi: kısa vadede rahatlama, uzun vadede risk</h2>
      <p class="soft">Avustralya'da 165 hastayla yapılan bir çalışmada kortizon iğnesi ilk haftalarda ağrıyı azalttı; ancak 1 yılın sonunda tamamen ya da çok iyileşenlerin oranı kortizon grubunda %83, plasebo iğne grubunda %96 oldu. Nüks oranı ise kortizon grubunda %54, plasebo grubunda %12 idi.</p>
      <div class="callout">
        <p>Yani iğnenin getirdiği kısa süreli rahatlama, uzun vadede iyileşmeyi yavaşlatabiliyor ve ağrının geri dönme olasılığını artırabiliyor. İğne düşünülüyorsa bu risk hekiminizle birlikte değerlendirilmelidir. İngiliz Dirsek ve Omuz Derneği'nin (BESS) 2023 bakım yolu, tenisçi dirseğinde kortizon iğnesinin kullanılmamasını güçlü şekilde öneriyor.</p>
      </div>
    </div>
  </section>

  <section id="tarihce">
    <div class="wrap">
      <p class="eyebrow">Geçmişten bugüne</p>
      <h2>"Çim tenisi kolu"ndan bugüne</h2>
      <p class="soft">Hastalığın adı 19. yüzyılın sonunda, çim tenisinin yaygınlaştığı dönemde ortaya çıktı. Son 25 yılın araştırmaları, kısa vadede hızlı rahatlama sağlayan tedavilerin uzun vadede her zaman en iyisi olmadığını gösterdi.</p>
      {g_tl(DIRSEK_TL)}
    </div>
  </section>

  <section id="tedavi">
    <div class="wrap">
      <h2>Tedavi</h2>
      <p class="soft">Amerikan Fizyoterapi Derneği'nin (APTA) 2022 kılavuzu tedavinin merkezine kademeli güçlendirme egzersizlerini koyuyor; İngiliz Dirsek ve Omuz Derneği (BESS) de fizyoterapiyi güçlü şekilde öneriyor.</p>
      <ul class="tx">
        <li><b>Güçlendirme egzersizleri</b><span>Bileği açan kaslara yönelik izometrik (kas boyu değişmeden), konsantrik (kısalarak) ya da eksantrik (uzayarak) direnç egzersizleri önerilir (B). Yük, kirişin uyum sağlayabileceği hızda, aşamalı olarak artırılır.</span></li>
        <li><b>Manuel terapi</b><span>Dirsek eklemine yönelik mobilizasyon kısa vadede ağrıyı azaltmak ve ağrısız kavrama gücünü artırmak için önerilir (B); boyun, sırt ve bileğe yönelik uygulamalar, bu bölgelerde kısıtlılık varsa destek olarak eklenebilir (C).</span></li>
        <li><b>Kuru iğneleme</b><span>ABD fizyoterapi kılavuzunda ağrıyı ve işlev kaybını azaltmak için B düzeyinde öneriliyor; BESS ise plaseboya üstünlüğüne dair kanıt olmadığını, bu yüzden şu an önerilemeyeceğini belirtiyor. Türkiye'de yalnızca yetkili hekimler uygulayabilir.</span></li>
        <li><b>Bantlama ve dirsek bandı</b><span>Ağrının kolay alevlendiği dönemde sert bantlama kısa vadede ağrıyı azaltabilir (B). Ön kol bandı ya da bilek desteği aktivite sırasında kullanıldığında ağrıyı hemen hafifletebilir (uzman görüşü); orta ve uzun vadeli etkisi konusunda çalışmalar çelişkili.</span></li>
        <li><b>Omuz ve kürek kemiği</b><span>Muayenede zayıflık saptanırsa omuz ve kürek kemiği kaslarını güçlendiren egzersizler programa eklenebilir (C).</span></li>
        <li><b>Ergonomi</b><span>İş ve günlük hayattaki kavrama, kaldırma ve bilek kullanımının düzenlenmesi şikâyetleri hafifletebilir (E, kuramsal kanıt).</span></li>
        <li><b>Ameliyat</b><span>BESS'e göre 3–6 ay ameliyatsız tedaviye rağmen düzelmeyen az sayıda kişide düşünülebilir; ancak sahte ameliyata üstün olduğunu gösteren kanıt yok.</span></li>
      </ul>
      <h3 class="g-h3">Tedavi seçenekleri: kılavuzlar ne diyor?</h3>
      <p class="soft">Amerikan Fizyoterapi Derneği'nin (APTA) kılavuzu (JOSPT, 2022) ile İngiliz Dirsek ve Omuz Derneği'nin (BESS) hasta bakım yolu (2023) yan yana. Parantez içindeki harfler JOSPT kılavuzundaki öneri düzeyidir (A güçlü, B orta, C zayıf, D çelişkili kanıt, E kuramsal kanıt, F uzman görüşü); BESS önerilerini "güçlü" ve "koşullu" diye ayırıyor. JOSPT kılavuzu ilaç ve enjeksiyon tedavilerini (kortizon, PRP) ve ameliyatı kapsamıyor, şok dalga tedavisine de yer vermiyor; tedavi kişiye göre seçilir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Egzersiz ve fizyoterapi</h3><dl><dt>JOSPT</dt><dd>Uzun süren ağrıda bileği açan kaslara izometrik, konsantrik ya da eksantrik direnç egzersizleri (B); zayıflık varsa omuz ve kürek kemiği egzersizleri (C).</dd><dt>BESS</dt><dd>Fizyoterapi önerilmeli (güçlü); birinci basamakta germe ve eksantrik yükleme egzersiz föyleri.</dd></dl></div>
        <div class="kind"><h3>Manuel terapi</h3><dl><dt>JOSPT</dt><dd>Dirsek mobilizasyonu kısa vadede ağrı ve ağrısız kavrama gücü için (B); kısıtlılık varsa boyun, sırt ve bilek (C); yumuşak doku mobilizasyonu (C).</dd></dl></div>
        <div class="kind"><h3>Bant ve dirsek bandı</h3><dl><dt>JOSPT</dt><dd>Ağrının kolay alevlendiği dönemde sert bantlama kısa vadede (B); aktivite sırasında bant ya da bilek desteği anında rahatlama için (uzman görüşü); orta ve uzun vadede kanıt çelişkili (D).</dd><dt>BESS</dt><dd>Ortez önerilebilir, ancak yarar sağlamayabileceği anlatılmalı (koşullu).</dd></dl></div>
        <div class="kind"><h3>Kortizon iğnesi</h3><dl><dt>BESS</dt><dd>Kullanılmamalı (güçlü).</dd><dt>Kanıt</dt><dd>Kısa vadede ağrıyı azaltabilir; 1 yılda daha kötü sonuç ve daha sık nüks (165 hastalık plasebo kontrollü çalışma).</dd></dl></div>
        <div class="kind"><h3>PRP ve kan iğnesi</h3><dl><dt>BESS</dt><dd>PRP'nin (kişinin kendi kanından hazırlanan, trombositten zengin plazma) plaseboya göre yararı olmayabileceği anlatılmalı (koşullu); kişinin kendi kanının enjeksiyonu kullanılmamalı (koşullu).</dd></dl></div>
        <div class="kind"><h3>Şok dalga ve diğer cihazlar</h3><dl><dt>BESS</dt><dd>Şok dalga tedavisi kullanılmamalı (güçlü).</dd><dt>JOSPT</dt><dd>Lazer 4 haftadan 6 aya kadar izlemde ağrı ve kavrama gücü için (C); TENS kısa vadede ağrı için (C); ultrason tedavisi tek başına çelişkili (D); kortizonlu ya da ağrı kesici jelin ultrasonla deriden verilmesi (fonoforez) önerilmiyor (C).</dd></dl></div>
        <div class="kind"><h3>Kuru iğneleme</h3><dl><dt>JOSPT</dt><dd>Kiriş ya da tetik noktalara kuru iğneleme (B).</dd><dt>BESS</dt><dd>Plaseboya üstünlüğüne dair kanıt yok; şu an önerilemiyor (koşullu).</dd><dt>Not</dt><dd>Türkiye'de yalnızca yetkili hekimler uygulayabilir.</dd></dl></div>
        <div class="kind"><h3>Ameliyat ve sevk</h3><dl><dt>BESS</dt><dd>3–6 ay ameliyatsız tedaviye rağmen düzelmeyenlerde ameliyat düşünülebilir; sahte ameliyata üstünlüğüne dair kanıt olmadığı anlatılmalı (koşullu). Bakım yoluna göre birinci basamakta 12–24 haftada düzelme yoksa uzmana sevk edilir.</dd></dl></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Tenisçi dirseği için altı egzersiz</h2>
      <p class="soft">Egzersiz sırasında hafif ve katlanılabilir bir ağrı olabilir; ağrı ertesi gün başlangıç düzeyine dönüyorsa devam edin. Keskin ya da giderek artan ağrı ya da elde uyuşma olursa durun. İzometrik egzersizle başlayıp ağrı azaldıkça eksantrik egzersize geçin.</p>
      {ex_grid(["isowe", "eccwe", "wext_st", "grip", "scap3", "row2"])}
    </div>
  </section>

  <section id="gunluk">
    <div class="wrap two">
      <div>
        <h2>Günlük hayatta dirseğiniz için</h2>
        <p class="soft">Amaç kolu kullanmayı bırakmak değil, kirişin yükünü ayarlamaktır.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Eşyaları avucunuz yukarı bakacak şekilde (alttan) kaldırın.</li>
        <li>Ağır çantaları elde değil, omzunuzda ya da sırt çantasıyla taşıyın.</li>
        <li>Kalın saplı aletler ve fincanlar kavramayı kolaylaştırır.</li>
        <li>Klavye ve fare kullanırken bileğinizi düz tutun, sık ara verin.</li>
        <li>Raket sporlarında raket sapı, tel gerginliği ve teknik için destek alın.</li>
      </ul>
    </div>
  </section>

  <section id="videolar">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Tenisçi dirseği için videolar</h2>
      <p class="soft">ABD'li fizyoterapistler Bob Schrupp ve Brad Heineck'in YouTube kanalından. Videolar İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("Wy3vqiB9X9A", "Dirsek ağrısı videosunu oynat", "Elbow Pain Gone! Fast &amp; Easy (Proven)")}
          <h3>Dirsek ağrısı için pozisyonel gevşetme</h3>
          <p>Ağrıyı hafifletmeye yönelik basit bir kendi kendine uygulama.</p>
        </div>
        <div class="vid">
          {vbox("CaYoIOWro_4", "Tenisçi dirseği kendi kendine tedavi videosunu oynat", "Stop Tennis Elbow Pain Now! (3 Minute Self-Treatment)")}
          <h3>Üç dakikalık kendi kendine uygulama</h3>
          <p>Ön kol kaslarına yönelik yumuşak doku uygulaması.</p>
        </div>
      </div>
      <p class="meta">Videolar Bob &amp; Brad kanalına aittir. Kanal hakkında: <a href="https://www.startribune.com/meet-the-minnesota-physical-therapists-who-have-become-youtube-superstars/508806552" target="_blank" rel="noopener">Star Tribune, 19 Nisan 2019</a>.</p>
    </div>
  </section>

  <section id="sss">
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(DIRSEK_FAQ)}
    </div>
  </section>

  <section id="uyari">
    <div class="wrap">
      <h2>Ne zaman hemen başvurmalı?</h2>
      <p class="soft">Şu durumlar tenisçi dirseği dışında bir soruna işaret edebilir. Beklemeden bir hekime başvurun:</p>
      <ul class="dots redflags">
        <li>Düşme ya da darbe sonrası dirsekte şişlik, şekil bozukluğu ya da hareket kaybı (kırık ya da çıkık olabilir; acil servise başvurun)</li>
        <li>Dirseğin kilitlenmesi, tam bükülüp düzelmemesi</li>
        <li>Dirsekte kızarıklık, şişlik ya da sıcaklık; özellikle ateş eşlik ediyorsa aynı gün, gerekirse acil serviste değerlendirilmelidir (eklem ya da kese enfeksiyonu olabilir)</li>
        <li>Kol ağrısına göğüs ağrısı, nefes darlığı ya da terleme eşlik ediyorsa hemen <strong>112</strong>'yi arayın</li>
        <li>Çocuk ya da ergende dirsek ağrısı</li>
        <li>Dirsekte ele gelen kitle ya da birden fazla eklemde ağrı ve şişlik</li>
        <li>Boyundan kola yayılan ağrı, elde uyuşma, karıncalanma ya da güç kaybı</li>
        <li>Dinlenmekle geçmeyen gece ağrısı ya da nedensiz kilo kaybı</li>
      </ul>
      {CTA_CARD("Dirsek ağrınız", "tenisçi dirseği")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(DIRSEK_SRC)}
    </div>
  </section>
</main>'''

page("tenisci-dirsegi.html", "Tenisçi Dirseği",
     "Tenisçi dirseği (lateral epikondilit) nedir, nasıl tanınır, ne kadar sürer, kortizon iğnesi yapılmalı mı? ABD ve İngiliz kılavuzlarının karşılaştırması, kısa tarihçe, evde altı egzersiz ve uyarı işaretleri.",
     "tenisci-dirsegi.html", NECK_CSS, DIRSEK_BODY, YT_JS,
     seo_title="Tenisçi Dirseği (Lateral Epikondilit): Egzersizler ve Tedavi | İhsan Eren",
     condition="Tenisçi dirseği (lateral epikondilit)", about=cond("Tenisçi dirseği (lateral epikondilit)"),
     faq_items=pick(DIRSEK_FAQ, 0, 1, 2, 3))

# -*- coding: utf-8 -*-
# Yeni rehber (45): Çocuklarda topuk ağrısı (Sever hastalığı). cond44_part.py'den sonra exec edilir. Video yok.
# Egzersizler Cambridge University Hospitals (2024) ve NHS Lothian (2022) broşürlerine göre, hazır çizimlerle.

_ex2("sv_calf", "calf", "Düz dizle baldır germe", "Bir duvara dönük durun, ellerinizi duvara koyun. Bir bacağınız arkada ve dizi düz olsun; arkadaki topuğu yere bastırarak öne doğru eğilin, baldırınızda gerilme hissedene kadar.", "20–30 saniye, günde 3–4 kez")
_ex2("sv_sol", "soleus", "Diz bükülü baldır germe", "Bir ayağınız önde, diğeri arkada dursun; iki topuk da yerde kalsın. İki dizinizi birden hafifçe bükün; gerilmeyi baldırın alt kısmında, topuğa yakın hissedersiniz.", "20–30 saniye, günde 3–4 kez")
_ex2("sv_ankle", "apump", "Ayak bileği hareketi", "Oturun ya da uzanın. Ayağınızı kendinize doğru çekin ve 5 saniye tutun, sonra parmaklarınızı yere doğru uzatın ve 5 saniye tutun.", "10 tekrar, günde 2–3 kez")

SV_FAQ = [
 ("Çocuğum sporu bırakmalı mı?", "Tamamen bırakması gerekmez. Ağrı şiddetliyse koşma ve zıplama içeren sporlara, ağrı yatışana kadar ara verebilir; bu sürede yüzme ve bisiklet gibi daha az yüklenen etkinlikler iyi bir seçenektir. Ağrı geçince etkinliğini kademeli olarak artırabilir."),
 ("Ne kadar sürer?", "Topuk ağrısı genellikle büyüme tamamlanınca geçer. Büyüme dönemlerinde birkaç kez tekrarlayabilir. Önerilere rağmen 6 hafta içinde düzelme yoksa bir uzmana görünebilirsiniz."),
 ("Topukluk ya da tabanlık işe yarar mı?", "Küçük çalışmalarda jel topukluk ve şok emici tabanlıkların kısa vadede ağrıyı azalttığı görüldü. 124 çocuğun katıldığı bir araştırmada tüm gruplar 2 ayda belirgin şekilde iyileşti; topukluğun sağladığı ek fark küçüktü, ayakkabı değişikliği ise ek bir fark yaratmadı."),
 ("Fizyoterapi gerekli mi?", "101 çocuğun katıldığı bir araştırmada bekleyip izlemek, şok emici topukluk ve baldır güçlendirmeli fizyoterapi arasında 3 ayda fark bulunmadı. Yani çoğu çocuk basit önlemlerle iyileşir. Ağrı geçmiyor ya da sık tekrarlıyorsa kişiye özel bir değerlendirme yol gösterici olabilir."),
 ("Neden bazen iki topuk birden ağrıyor?", "Durum büyümeyle ilgili olduğu için tek ya da iki topukta birden görülebilir."),
]

SV_SRC = [
 "Cambridge University Hospitals NHS Foundation Trust. " + ext("https://www.cuh.nhs.uk/patient-information/severs-diseasesevers-disease", "Sever’s disease") + ". Version 3, September 2024.",
 "NHS Lothian. " + ext("https://policyonline.nhslothian.scot/wp-content/uploads/2023/03/Severs_Disease_self-management_guide.pdf", "Sever’s disease: self-management guide") + ". May 2022.",
 "Uvelli K, Neher JO, Safranek S. " + ext("https://www.aafp.org/pubs/afp/issues/2017/0715/p126.html", "Treatment for calcaneal apophysitis") + ". Am Fam Physician. 2017;96(2):126–127.",
 "James AM, Williams CM, Haines TP. " + ext("https://doi.org/10.1186/1757-1146-6-16", "Effectiveness of interventions in reducing pain and maintaining physical activity in children and adolescents with calcaneal apophysitis (Sever’s disease): a systematic review") + ". J Foot Ankle Res. 2013;6:16",
 "NHS. " + ext("https://www.nhs.uk/conditions/heel-pain/", "Heel pain") + ". Page last reviewed: 24 October 2025.",
]

SV_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Çocuklarda topuk ağrısı (Sever hastalığı)</h1>
    <p class="lede">Çocuğunuz koşup zıpladıktan sonra topuğunun ağrıdığını mı söylüyor, aksıyor ya da parmak uçlarında mı yürüyor? Büyüme döneminde topuk kemiğinin büyüme bölgesinin tahriş olmasına Sever hastalığı denir. Adı ürkütücü olsa da büyümeyle ilgili, sık görülen ve geçici bir durumdur; büyüme tamamlanınca topuk ağrısı geçer.</p>
    <p class="meta">Son güncelleme: 16 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>8–10 yaş</b><span>Kızlarda en sık görüldüğü dönem</span></div>
        <div class="stat"><b>10–14 yaş</b><span>Erkeklerde en sık görüldüğü dönem</span></div>
        <div class="stat"><b>3 ay</b><span>Bekleyip izleme, topukluk ve fizyoterapinin bu sürede aynı sonucu verdiği araştırma bulgusu</span></div>
        <div class="stat"><b>6 hafta</b><span>Önerilere rağmen düzelme yoksa bir uzmana görünme süresi</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Belirtiler</h2>
        <ul class="dots">
          <li>Koşma, zıplama gibi etkinliklerle artan, dinlenince azalan topuk ağrısı.</li>
          <li>Aksama ya da parmak uçlarında yürüme.</li>
          <li>Topuk iki yandan sıkıldığında hassasiyet; aşil tendonunun kemiğe yapıştığı yerde hafif şişlik.</li>
          <li>Baldır kaslarında gerginlik; tek ya da iki topukta birden.</li>
        </ul>
      </div>
      <div>
        <h2>Neden olur?</h2>
        <ul class="dots">
          <li>Hızlı büyüme dönemlerinde kemikler, baldır kasları ve aşil tendonundan daha hızlı uzar.</li>
          <li>Gerilen aşil tendonu, topuk kemiğinin büyüme bölgesini tekrar tekrar çeker ve tahriş eder.</li>
          <li>Bu yüzden her yeni büyüme atağında yeniden ortaya çıkabilir.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neler iyi gelir?</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Etkinliği ayarlayın</h3><p>Ağrı şiddetliyse koşma ve zıplamaya ara verin; yüzme ve bisiklet iyi seçeneklerdir. Spordan sonra bacağı yükseğe kaldırarak dinlendirin.</p></div>
        <div class="kind"><span class="n">2</span><h3>Buz uygulayın</h3><p>Havluya sarılı buzu, özellikle etkinlikten sonra 10–15 dakika topuğa koyabilirsiniz.</p></div>
        <div class="kind"><span class="n">3</span><h3>Topukluk ve ayakkabı</h3><p>Şok emici tabanlık ya da jel topukluk ve destekleyici bir ayakkabı kullanın; çıplak ayakla dolaşmaktan kaçının.</p></div>
        <div class="kind"><span class="n">4</span><h3>Baldırları esnetin</h3><p>Baldır germe egzersizleri gerginliği azaltır. Yeni bir büyüme atağında ağrı dönerse esnemelere yeniden başlayın.</p></div>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Baldırı rahatlatan üç egzersiz</h2>
      <p class="soft">Germeleri yavaşça ve zorlamadan yapın. Bir egzersiz ağrıyı artırıyor ya da yeni bir ağrı yapıyorsa bırakın ve bir uzmana danışın.</p>
      {ex_grid(["sv_calf", "sv_sol", "sv_ankle"])}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(SV_FAQ)}
      <p class="soft" style="margin-top:18px">Büyüme dönemindeki diz ağrısı için <a href="osgood-schlatter.html">Osgood-Schlatter</a>, yetişkinlerde topuk ağrısı için <a href="topuk-dikeni.html">topuk dikeni</a> rehberine bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman hekime başvurmalı?</h2>
      <ul class="dots redflags">
        <li>Bir yaralanmadan sonra şiddetli topuk ağrısı başladıysa ya da o sırada çatırtı, kırılma sesi duyulduysa</li>
        <li>Çocuğunuz yürüyemiyor, parmak ucunda duramıyor ya da merdiven çıkamıyorsa</li>
        <li>Ayak ya da ayak bileğinde şekil bozukluğu, baldırda ve bilekte şişlik ve morluk varsa</li>
        <li>Ayakta uyuşma ya da karıncalanma varsa</li>
        <li>Ağrı çok şiddetliyse, günlük hayatı engelliyorsa ya da evde bakıma rağmen düzelmiyorsa</li>
      </ul>
      {CTA_CARD("Çocuğunuzun topuk ağrısı", "çocuğumun topuk ağrısı (Sever hastalığı)")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(SV_SRC)}
    </div>
  </section>
</main>'''

page("sever-hastaligi.html", "Çocuklarda Topuk Ağrısı (Sever Hastalığı)",
     "Çocuğunuzun topuğu koşup zıpladıktan sonra mı ağrıyor? Sever hastalığı nedir, ne kadar sürer, spor bırakılmalı mı, topukluk işe yarar mı? Uyarı işaretleri ve evde üç egzersiz.",
     "sever-hastaligi.html", NECK_CSS, SV_BODY, "",
     seo_title="Çocuklarda Topuk Ağrısı (Sever Hastalığı): Belirtiler, Tedavi ve Egzersizler | İhsan Eren",
     condition="Sever hastalığı", faq_items=SV_FAQ)

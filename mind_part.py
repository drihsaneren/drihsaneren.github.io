# -*- coding: utf-8 -*-
# Kendine iyi bak, ruh sağlığı turu (10 Ekim 2026): egzersizle ruh sağlığı rehberi.
# knee12_part.py'den sonra exec edilir. SELF2_CSS (self2_part.py) kullanılır.

MIND_CSS = SELF2_CSS + """
  .cmp .row > span small{display:block;font-size:12.5px;color:var(--muted);margin-top:2px}
  .cmp .row.few .bar i{opacity:.5}
  .scale{display:flex;gap:18px;flex-wrap:wrap;margin-top:12px;font-size:13.5px;color:var(--muted)}
  .scale b{color:var(--ink);font-weight:600}
"""

# ---- egzersizler: araştırmalarda en etkili bulunan türlerden (yürüyüş, güç, yoga) ve müzikle hareket
_ex2("mh_walk", "walk", "Tempolu yürüyüş", "Rahat ayakkabılarla, konuşabileceğiniz ama şarkı söylemekte zorlanacağınız bir tempoda yürüyün. Kollarınızı serbestçe sallayın. Mümkünse açık havada, ağaçlık bir yolda ya da parkta yürüyün.", "10 dakikayla başlayın; günde 20–30 dakikaya çıkın")
_ex2("mh_step", "sidestep", "Müzikle yana adım", "Sevdiğiniz, tempolu bir şarkı açın. Bir ayağınızla yana adım atın, diğerini yanına getirin; sonra öbür yöne dönün. Kollarınızı da katın. Doğru ya da yanlış yoktur; önemli olan ritmi sürdürmek.", "1–2 şarkı boyunca")
_ex2("mh_sts", "sts", "Sandalyeden kalkıp oturma", "Sağlam bir sandalyenin ön kısmına oturun. Hafifçe öne eğilip kollarınızı kullanmadan ayağa kalkın, sonra yavaşça oturun. Kolaylaştıkça tekrar sayısını artırın.", "10 tekrar, 2–3 set")
_ex2("mh_push", "sk_push", "Duvar şınavı", "Duvardan bir kol boyu uzakta durun, ellerinizi göğüs hizasında duvara koyun. Gövdeniz düz kalsın; dirseklerinizi bükerek duvara yaklaşın, sonra itin. Kolaylaşınca ellerinizi tezgâha koyarak zorlaştırın.", "10 tekrar, 2–3 set")
_ex2("mh_cat", "cat", "Kedi-deve", "Ellerinizin ve dizlerinizin üzerinde durun. Nefes verirken sırtınızı yukarı doğru yuvarlayın, nefes alırken belinizi yavaşça aşağı bırakın. Hareketi nefesinizle birlikte, acele etmeden yapın.", "8–10 tekrar")
_ex2("mh_child", "childp", "Çocuk pozu", "Ellerinizin ve dizlerinizin üzerinden kalçanızı yavaşça topuklarınıza doğru götürün, kollarınız önde uzansın. Alnınızı yere ya da bir yastığa bırakın. Burnunuzdan yavaşça nefes alıp verin. Dizleriniz ağrıyorsa atlayın.", "30–60 saniye, 2–3 kez")

MX_ROWS_DATA = [("Dans", "5 çalışma, 107 kişi", 0.96), ("Yürüyüş ya da koşu", "51 çalışma, 1.210 kişi", 0.62), ("Yoga", "33 çalışma, 1.047 kişi", 0.55),
                ("Güç (direnç) çalışması", "22 çalışma, 643 kişi", 0.49), ("Karma aerobik egzersiz", "51 çalışma, 1.286 kişi", 0.43), ("Tai chi ya da qigong", "12 çalışma, 343 kişi", 0.42)]
MX_ROWS = "\n".join(
    f'<div class="row{" few" if i == 0 else ""}"><span>{t}<small>{n}</small></span><span class="bar"><i style="width:{v / 1.0 * 100:.0f}%"></i></span><b>{str(v).replace(".", ",")}</b></div>'
    for i, (t, n, v) in enumerate(MX_ROWS_DATA))

MX_FAQ = [
 ("Egzersiz ilacın ya da terapinin yerine geçer mi?", "Hafif depresyonda egzersiz, önerilen seçeneklerden biridir. Orta ve ağır depresyonda genellikle terapi ve ilaç önerilir; egzersiz bunlara eklenebilir. Araştırmalarda egzersiz, ilaç ya da terapiyle birlikte yapıldığında da etkiliydi. Kullandığınız ilacı kendi başınıza bırakmayın; değişiklik için hekiminizle konuşun."),
 ("Ne kadar sürede fark ederim?", "İngiltere'deki kılavuzda önerilen grup programı 10 hafta, kaygı çalışmasındaki program 12 hafta sürdü. Sonucu birkaç haftalık düzenli egzersizden sonra değerlendirin. Bu arada tek bir tempolu yürüyüş bile zihni toparlamaya yardımcı olabilir."),
 ("Hiç enerjim yok; nasıl başlayayım?", "Çok küçük başlayın: 10 dakikalık bir yürüyüş ya da tek bir şarkı boyunca hareket. Hafif egzersiz de işe yarıyor. Ne zaman yapacağınızı önceden belirleyin, mümkünse biriyle birlikte yapın. Yapamadığınız günler için kendinize yüklenmeyin; ertesi gün kaldığınız yerden devam edin."),
 ("En iyi egzersiz hangisi?", "Araştırmalarda yürüyüş ya da koşu, yoga ve güç çalışması öne çıktı. Ama en iyi egzersiz, düzenli yapabileceğiniz ve sevdiğiniz egzersizdir. Yoga ve güç çalışmasında yarıda bırakma daha azdı."),
]

MX_SRC = [
 "Noetel M, Sanders T, Gallardo-Gómez D, et al. " + ext("https://www.bmj.com/content/384/bmj-2023-075847", "Effect of exercise for depression: systematic review and network meta-analysis of randomised controlled trials") + ". BMJ. 2024;384:e075847.",
 "Singh B, Olds T, Curtis R, et al. " + ext("https://bjsm.bmj.com/content/57/18/1203", "Effectiveness of physical activity interventions for improving depression, anxiety and distress: an overview of systematic reviews") + ". Br J Sports Med. 2023;57(18):1203–1209.",
 "Pearce M, Garcia L, Abbas A, et al. " + ext("https://jamanetwork.com/journals/jamapsychiatry/fullarticle/2790780", "Association between physical activity and risk of depression: a systematic review and meta-analysis") + ". JAMA Psychiatry. 2022;79(6):550–559.",
 "Henriksson M, Wall A, Nyberg J, et al. Effects of exercise on symptoms of anxiety in primary care patients: a randomized controlled trial. J Affect Disord. 2022;297:26–34. Özet: " + ext("https://www.gu.se/en/news/anxiety-effectively-treated-with-exercise", "University of Gothenburg, Anxiety effectively treated with exercise") + ", 9 November 2021.",
 "National Institute for Health and Care Excellence. " + ext("https://www.nice.org.uk/guidance/ng222/chapter/Recommendations", "Depression in adults: treatment and management (NG222)") + ". 2022.",
 "World Health Organization. " + ext("https://www.who.int/news-room/fact-sheets/detail/physical-activity", "Physical activity") + ". Fact sheet. 26 June 2024.",
 "NHS. " + ext("https://www.nhs.uk/mental-health/self-help/guides-tools-and-activities/exercise-for-depression/", "Exercise for depression") + ". Page last reviewed 16 April 2026.",
 "NHS. " + ext("https://www.nhs.uk/mental-health/conditions/depression-in-adults/overview/", "Depression in adults: overview") + ". Page last reviewed 5 July 2023.",
]

MX_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Ruh sağlığı için egzersiz</h1>
    <p class="lede">Egzersiz yalnızca bedene değil, ruh hâline de iyi gelir. Yüzlerce çalışmayı bir araya getiren analizlere göre depresyon ve kaygı belirtilerini azaltır; düzenli hareket edenlerde depresyon da daha seyrek görülür. Bu rehber hangi egzersizin, ne kadar ve nasıl yapıldığında işe yaradığını anlatır. Egzersiz tedavinin yerine geçmez; onu tamamlar.</p>
    <p class="meta">Son güncelleme: 10 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>218 çalışma</b><span>Depresyonda egzersizi inceleyen 2024 tarihli analiz; 14.170 katılımcı (BMJ)</span></div>
        <div class="stat"><b>%25</b><span>Haftada 2,5 saat tempolu yürüyüşe denk hareket edenlerde daha düşük depresyon riski</span></div>
        <div class="stat"><b>%18</b><span>Bunun yarısı kadar hareketle bile görülen risk düşüşü (aynı analiz, 191.130 kişi)</span></div>
        <div class="stat"><b>12 hafta</b><span>Kaygıda grup egzersizinin denendiği çalışmanın süresi; belirtiler belirgin biçimde azaldı</span></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Kimlere iyi gelir?</h2>
        <p class="soft">97 derlemeyi ve 1.039 çalışmayı kapsayan bir incelemede hareket; depresyon, kaygı ve psikolojik sıkıntıyı pek çok grupta azalttı. Yararı en belirgin görülenler depresyonu olanlar, gebeler ve doğum sonrası dönemdeki kadınlar, sağlıklı yetişkinler ve HIV ya da böbrek hastalığı olanlardı.</p>
        <p class="soft">Depresyon analizinde etki, başka hastalığı olan ve olmayanlarda, hafif ve ağır belirtileri olanlarda benzerdi.</p>
      </div>
      <div>
        <h2>Nasıl yorumlamalı?</h2>
        <ul class="dots">
          <li>Etkiler, bilişsel davranışçı terapiyle benzer büyüklükte bulundu.</li>
          <li>Egzersiz, ilaç ya da terapiyle birlikte yapıldığında da etkiliydi.</li>
          <li>Çalışmaların çoğu küçük ve katılımcılar hangi grupta olduğunu biliyordu; bu yüzden kanıtın güvenilirliği düşük ya da çok düşük kabul edildi.</li>
          <li>Yine de yazarlara göre egzersiz, terapi ve ilaçla birlikte temel tedavi seçeneklerinden biri olarak düşünülebilir.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <p class="eyebrow">Depresyon</p>
      <h2>Hangi egzersiz ne kadar işe yaradı?</h2>
      <p class="soft">BMJ'de 2024'te yayımlanan analiz, her egzersiz türünü karşılaştırma gruplarıyla kıyasladı. Çubuk uzadıkça depresyon belirtilerindeki azalma büyüyor.</p>
      <div class="cmp">
{MX_ROWS}
      </div>
      <div class="scale"><span>Etki büyüklüğü: <b>0,2</b> küçük</span><span><b>0,5</b> orta</span><span><b>0,8</b> büyük</span></div>
      <ul class="dots" style="margin-top:18px">
        <li><b>Dans</b> en büyük etkiyi gösterdi ama yalnızca 5 çalışmaya dayanıyor; umut verici, henüz kesin değil.</li>
        <li><b>Yürüyüş ya da koşu, yoga ve güç çalışması</b> yazarların öne çıkardığı üç tür oldu.</li>
        <li><b>Şiddet önemli:</b> Koşu ya da aralıklı yüksek tempo gibi zorlayıcı egzersizlerde etki daha büyüktü; ancak yürüyüş gibi hafif egzersizler de belirgin yarar sağladı.</li>
        <li><b>Yoga ve güç çalışması</b> daha iyi tolere edildi; bu gruplarda yarıda bırakma daha azdı.</li>
        <li>Güç çalışması kadınlarda ve gençlerde, yoga erkeklerde ve ileri yaştakilerde daha etkili görünüyordu; bu alt grup sonuçları kesin değildir.</li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <p class="eyebrow">Kaygı</p>
        <h2>Kaygıda 12 haftalık egzersiz</h2>
        <p class="soft">İsveç'te birinci basamakta yapılan çalışmaya kaygı bozukluğu olan 286 kişi katıldı; yarısı en az on yıldır kaygıyla yaşıyordu. Katılımcılar 12 hafta boyunca, haftada üç kez 60 dakikalık grup egzersizine, yanlarında bir fizyoterapist varken katıldı. Seanslar ısınma, kalp-dolaşım ve güç istasyonlarından oluşan 45 dakikalık bir devre ve esnemeyle bitiyordu.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Hem orta hem de yüksek tempoda çalışanlarda kaygı belirtileri, yalnızca hareket önerisi alan gruba göre belirgin biçimde azaldı; uzun süredir kaygısı olanlarda da.</li>
        <li>İyileşme olasılığı orta tempoda 3,6 kat, yüksek tempoda 4,9 kat arttı.</li>
        <li>Egzersiz zorlaştıkça iyileşme de arttı.</li>
        <li>97 derlemeyi kapsayan incelemede de hareket, kaygı belirtilerini depresyondakine benzer ölçüde azalttı.</li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <p class="eyebrow">Ne kadar?</p>
      <h2>Doz: az da olsa başlayın</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Hiç yoktan iyidir</h3><p>Önerilenin yarısı kadar hareket edenlerde bile depresyon riski %18 daha düşüktü. Dünya Sağlık Örgütü'ne göre her hareket, hiç hareket etmemekten iyidir.</p></div>
        <div class="kind"><span class="n">2</span><h3>Hedef 150 dakika</h3><p>Yetişkinler için hedef, haftada en az 150 dakika orta şiddette hareket. Bu, haftanın beş günü 30 dakika tempolu yürüyüş demektir; yavaş yavaş ulaşın.</p></div>
        <div class="kind"><span class="n">3</span><h3>Biraz zorlayın</h3><p>Orta ve yüksek şiddette yapılan egzersizlerde etki daha büyüktü. Rahat ettiğiniz tempodan başlayıp zamanla biraz hızlanın.</p></div>
        <div class="kind"><span class="n">4</span><h3>Haftalarca sürdürün</h3><p>İngiltere'deki kılavuz hafif depresyonda, eğitimli biri eşliğinde 10 hafta boyunca haftada birden fazla grup egzersizini seçenekler arasında sayıyor. Kaygı çalışmasındaki program 12 hafta sürdü. Sonrasında da hareketi alışkanlık hâline getirin.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Başlamak zor geliyorsa</h2>
        <p class="soft">Depresyonda yorgunluk ve eskiden sevilen şeylere ilgisizlik sık görülür; bu yüzden başlamak zor gelebilir. Bu bir irade sorunu değildir. Küçük, somut ve keyifli adımlar işinizi kolaylaştırır.</p>
      </div>
      <ul class="dots">
        <li><b>Sevdiğiniz bir şeyi seçin.</b> Düzenli yapabileceğiniz her egzersiz işe yarar.</li>
        <li><b>Küçük başlayın.</b> Tempolu 10 dakikalık bir yürüyüş bile zihninizi toparlamaya yardımcı olabilir.</li>
        <li><b>Gün ve saati baştan belirleyin.</b> "Salı ve perşembe, akşam yemeğinden önce" gibi.</li>
        <li><b>Birlikte yapın.</b> Bir arkadaşla yürüyüş ya da bir grup dersi hem düzeni hem bağı güçlendirir; <a href="bag-kurmak.html">sosyal bağ</a> sayfasına da bakın.</li>
        <li><b>Dışarı çıkın.</b> Park ya da sahil yürüyüşleri için <a href="doga-recetesi.html">doğa reçetesi</a> sayfasına bakın.</li>
        <li><b>Kendinize nazik olun.</b> Kaçırdığınız günler için kendinize yüklenmeyin; <a href="dost-molasi.html">DOST molası</a> zor günler için.</li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Evde egzersiz</p>
      <h2>Ruh hâliniz için altı hareket</h2>
      <p class="soft">Araştırmalarda en çok yarar görülen türlerden seçildi: yürüyüş ve müzikle hareket, güç çalışması ve yoga. Haftada en az iki gün güç hareketlerini, diğer günlerde yürüyüşü deneyin. Bir hareket ağrınızı artırıyorsa onu atlayın.</p>
      {ex_grid(["mh_walk", "mh_step", "mh_sts", "mh_push", "mh_cat", "mh_child"])}
      <p class="soft" style="margin-top:18px">Gergin anlar için <a href="ic-cekis.html">5 dakikalık iç çekiş nefesi</a> ve <a href="stres.html">Stresli anlarda</a> sayfası, haftalık hareketinizi ölçmek için <a href="hareket.html">Ne kadar hareket yeterli?</a> sayfası işinize yarayabilir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(MX_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman yardım almalı?</h2>
      <ul class="dots redflags">
        <li>Kendinize zarar verme ya da yaşamınıza son verme düşünceleriniz varsa beklemeden 112'yi arayın ya da en yakın acil servise gidin.</li>
        <li>Haftalardır süren mutsuzluk, umutsuzluk, eskiden keyif aldığınız şeylere ilgisizlik, uyku ya da iştah değişiklikleri varsa bir hekime ya da ruh sağlığı uzmanına başvurun.</li>
        <li>Kaygı ya da çökkünlük işinizi, ilişkilerinizi ya da günlük işlerinizi aksatıyorsa destek almayı ertelemeyin.</li>
        <li>Egzersiz sırasında göğüs ağrısı, nefes darlığı, baş dönmesi ya da bayılma hissi olursa durun ve hekiminize danışın.</li>
      </ul>
      <div class="note" style="margin-top:22px"><strong>Önemli:</strong> Bu sayfa bilgilendirme amaçlıdır; tanı koymaz ve tedavinin yerine geçmez. Kullandığınız ilaçları hekiminize danışmadan bırakmayın.</div>
      {CTA_CARD("Ruh hâlinize iyi gelecek, size uygun ve düzenli bir egzersiz programı", "ruh sağlığı için egzersiz programı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(MX_SRC)}
    </div>
  </section>
</main>'''

page("ruh-sagligi-egzersiz.html", "Ruh Sağlığı İçin Egzersiz",
     "Egzersiz depresyon ve kaygıya iyi gelir mi? 218 çalışmanın bulguları, hangi egzersizin ne kadar işe yaradığı, ne kadar ve ne şiddette yapılmalı, başlamak zor geliyorsa ne yapmalı ve evde altı hareket.",
     "ruh-sagligi-egzersiz.html", MIND_CSS, MX_BODY, "",
     seo_title="Depresyon ve Kaygı İçin Egzersiz: Hangisi, Ne Kadar? | İhsan Eren",
     about=[cond("Depresyon"), cond("Kaygı bozukluğu (anksiyete)")], faq_items=MX_FAQ)

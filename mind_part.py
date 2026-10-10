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

# ============================================================== 2 · RUH HÂLİ ÖLÇÜMÜ (WHO-5 + PHQ-4)
MOOD_CSS = MIND_CSS + """
  .mood{max-width:680px;padding:clamp(18px,4vw,30px)}
  .mq-start p{color:var(--ink-soft);margin:0 0 14px}
  .mq-start .priv{font-size:14px;color:var(--muted)}
  .mq-top{display:flex;align-items:center;gap:14px;margin-bottom:20px;min-height:18px}
  .mq-k{font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--foil);font-weight:600;white-space:nowrap}
  .mq-prog{flex:1;height:4px;border-radius:2px;background:rgba(236,229,207,.12);overflow:hidden}
  .mq-prog i{display:block;height:100%;width:0;background:var(--foil);transition:width .3s ease}
  fieldset.mq{border:0;margin:0;padding:0;min-width:0}
  .mq legend{padding:0;margin-bottom:16px;width:100%}
  .mq-h{display:block;color:var(--muted);font-size:14px;line-height:1.45;margin-bottom:10px}
  .mq legend b{display:block;font-family:var(--display);font-weight:400;font-size:clamp(22px,4.6vw,28px);line-height:1.25;color:var(--ink)}
  .opts{display:grid;gap:9px}
  .opts button{all:unset;box-sizing:border-box;cursor:pointer;display:block;width:100%;padding:13px 16px;border-radius:12px;border:1px solid var(--line-strong);color:var(--ink);font-size:15.5px;line-height:1.35;background:rgba(236,229,207,.03);transition:background .15s,border-color .15s}
  .opts button:hover{border-color:var(--foil)}
  .opts button[aria-pressed="true"]{background:var(--foil);color:var(--ground);border-color:var(--foil);font-weight:600}
  .opts button:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .mq-nav{margin-top:14px}
  .mq .lnk,.mood .lnk{all:unset;cursor:pointer;color:var(--foil);font-size:14.5px;text-decoration:underline;text-underline-offset:3px}
  .mood .lnk:disabled{opacity:.35;cursor:default;text-decoration:none}
  .mood .lnk:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .rs-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:14px 0 18px}
  @media (max-width:640px){.rs-grid{grid-template-columns:1fr}}
  .rs{border:1px solid var(--line);border-radius:14px;padding:16px 16px 14px;background:rgba(236,229,207,.03)}
  .rs .k{margin:0;font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--foil);font-weight:600}
  .rs .v{margin:6px 0 10px;display:flex;align-items:baseline;gap:4px}
  .rs .v b{font-family:var(--display);font-weight:400;font-size:44px;line-height:1;color:var(--ink)}
  .rs .v span{color:var(--muted);font-size:15px}
  .rs .v em{font-style:normal;margin-left:10px;font-size:13px;font-weight:600;padding:3px 9px;border-radius:999px;background:rgba(236,229,207,.08);color:var(--ink-soft)}
  .gauge{position:relative;height:9px;border-radius:5px;margin:4px 0 12px}
  .gauge.w{background:linear-gradient(90deg,#c96b5a 0 30%,#d8b25e 30% 51%,#8fa476 51% 100%)}
  .gauge.p{background:linear-gradient(90deg,#8fa476 0 20.8%,#b7ba7c 20.8% 45.8%,#d8b25e 45.8% 70.8%,#c96b5a 70.8% 100%)}
  .gauge i{position:absolute;top:-5px;width:5px;height:19px;border-radius:3px;background:var(--ink);box-shadow:0 0 0 2px var(--ground);transform:translateX(-50%);transition:left .6s cubic-bezier(.2,.8,.2,1)}
  .rs .t{margin:0;color:var(--ink-soft);font-size:14.5px;line-height:1.5}
  .rs .sub{list-style:none;margin:10px 0 0;padding:0;display:flex;gap:8px;flex-wrap:wrap}
  .rs .sub li{font-size:13.5px;padding:4px 10px;border-radius:999px;border:1px solid var(--line);color:var(--ink-soft)}
  .rs .sub li.hi{border-color:#d8b25e;color:var(--ink)}
  .rs .note2{margin:8px 0 0;font-size:13px;color:var(--muted)}
  .adv{border-left:4px solid var(--sage);border-radius:4px 12px 12px 4px;background:rgba(236,229,207,.05);padding:14px 16px;margin:0 0 14px}
  .adv.m{border-color:#b7ba7c}.adv.y{border-color:#d8b25e}.adv.r{border-color:#c96b5a}
  .adv h3{font-size:19px;margin:0 0 6px}
  .adv p{margin:0;color:var(--ink-soft);font-size:15px}
  .adv p + p{margin-top:8px}
  .crisis{max-width:none;font-size:14.5px;color:var(--ink);background:rgba(201,107,90,.14);border:1px solid rgba(201,107,90,.45);border-radius:12px;padding:12px 14px;margin:0 0 16px}
  .mq-acts{display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center}
  .mq-hist{margin-top:20px}
  .mq-hist h3{font-size:17px;margin:0 0 8px}
  .mq-tab{width:100%;border-collapse:collapse;font-size:14.5px}
  .mq-tab th,.mq-tab td{text-align:left;padding:7px 8px;border-bottom:1px solid var(--line)}
  .mq-tab th{font-weight:600;color:var(--muted);font-size:12.5px;letter-spacing:.06em}
  .mq-tab td b{font-weight:600;color:var(--ink)}
  .mq-tab td small{color:var(--muted);margin-left:6px}
  .bands{display:grid;grid-template-columns:1fr 1fr;gap:clamp(18px,4vw,40px)}
  @media (max-width:760px){.bands{grid-template-columns:1fr}}
"""

WHO5_ITEMS = ["Kendimi neşeli ve keyifli hissettim", "Kendimi sakin ve gevşemiş hissettim", "Kendimi aktif ve dinç hissettim",
              "Sabahları kendimi taze ve dinlenmiş hissederek uyandım", "Günlük yaşantım beni ilgilendiren şeylerle dolu"]
# "Her zaman" ve "Bazen" başka sayfalarda "Always"/"Sometimes" diye çevrili; görünmez sözcük birleştirici (U+2060) bu sayfaya özgü
# çeviri anahtarı sağlar, böylece İngilizcede ölçeğin resmî ifadeleri ("All of the time", "Some of the time") kullanılır.
WHO5_OPTS = [(5, "Her zaman&#8288;"), (4, "Çoğu zaman"), (3, "Geçen zamanın yarısından çoğunda"), (2, "Geçen zamanın yarısından daha azında"), (1, "Bazen&#8288;"), (0, "Hiçbir zaman")]
PHQ4_ITEMS = [("a", "Sinirli, kaygılı ya da diken üstünde hissetme"), ("a", "Endişelenmeyi durduramama ya da kontrol edememe"),
              ("d", "Bir şeyler yapmaktan çok az ilgi ya da zevk alma"), ("d", "Kendini çökkün, depresif ya da umutsuz hissetme")]
PHQ4_OPTS = [(0, "Hiç"), (1, "Birkaç gün"), (2, "Günlerin yarısından fazlasında"), (3, "Neredeyse her gün")]

def _mq(group, stem, item, opts):
    bs = "".join(f'<button type="button" data-v="{v}" aria-pressed="false">{t}</button>' for v, t in opts)
    return f'<fieldset class="mq" data-g="{group}" hidden><legend><span class="mq-h">{stem}</span><b>{item}</b></legend><div class="opts">{bs}</div></fieldset>'

MQ_HTML = "\n".join(
    [_mq("w", "Aşağıdaki beş tanımlamadan her biri için, son iki hafta süresince kendinizi nasıl hissettiğinize en yakın olan yanıtı veriniz.", it, WHO5_OPTS) for it in WHO5_ITEMS] +
    [_mq(g, "Son 2 hafta içinde aşağıdaki sorunlar sizi ne sıklıkla rahatsız etti?", it, PHQ4_OPTS) for g, it in PHQ4_ITEMS])

MOOD_FAQ = [
 ("Yanıtlarım nereye gidiyor?", "Hiçbir yere. Puanlar telefonunuzda ya da bilgisayarınızda hesaplanır; sunucuya gönderilmez. Sonucu kaydetmeyi seçerseniz yalnızca bu tarayıcıda saklanır ve istediğiniz an silebilirsiniz."),
 ("Puanım düşük çıktı; depresyonum var mı?", "Bu ölçekler tanı koymaz; daha ayrıntılı değerlendirme gerekip gerekmediğini gösteren tarama araçlarıdır. Tanı, bir hekim ya da ruh sağlığı uzmanının görüşmesiyle konur. Puanınız sınırın altındaysa ya da kendinizi iyi hissetmiyorsanız bir uzmanla konuşun."),
 ("Ne sıklıkla tekrarlamalıyım?", "Sorular son iki haftayı kapsadığı için iki haftada bir tekrarlamak yeterlidir. İyi oluş puanında 10 puanlık bir değişim, araştırmalarda anlamlı kabul edilir."),
 ("Puanım iyi ama kendimi kötü hissediyorum; ne yapmalıyım?", "Kısa ölçekler her durumu yakalayamaz. Kendinizi kötü hissediyorsanız ya da belirtileriniz günlük hayatınızı etkiliyorsa, puan ne olursa olsun bir hekime ya da ruh sağlığı uzmanına başvurun."),
]

MOOD_SRC = [
 "Topp CW, Østergaard SD, Søndergaard S, Bech P. " + ext("https://karger.com/pps/article/84/3/167/282903/The-WHO-5-Well-Being-Index-A-Systematic-Review-of", "The WHO-5 Well-Being Index: a systematic review of the literature") + ". Psychother Psychosom. 2015;84(3):167–176.",
 "Psychiatric Research Unit, WHO Collaborating Centre in Mental Health, Frederiksborg General Hospital. " + ext("https://www.psykiatri-regionh.dk/who-5/Documents/WHO5_Turkish.pdf", "WHO (Beş) İyilik Durumu İndeksi (1998 sürümü), Türkçe") + "; " + ext("https://www.psykiatri-regionh.dk/who-5/who-5-questionnaires/Pages/default.aspx", "WHO-5 questionnaires") + ".",
 "Eser E, Çevik C, Baydur H, et al. " + ext("https://acikerisim.comu.edu.tr/items/052b02e4-bd78-4283-ba47-600999f3f936", "Reliability and validity of the Turkish version of the WHO-5, in adults and older adults for its use in primary care settings") + ". Prim Health Care Res Dev. 2019;20:e100.",
 "Kroenke K, Spitzer RL, Williams JBW, Löwe B. " + ext("https://fis.uke.de/portal/en/publications/an-ultrabrief-screening-scale-for-anxiety-and-depression-the-phq4(3969b34b-29e4-403d-ba80-11112c46edcb).html", "An ultra-brief screening scale for anxiety and depression: the PHQ-4") + ". Psychosomatics. 2009;50(6):613–621.",
 ext("https://www.sralab.org/sites/default/files/2018-03/PHQ4.pdf", "Patient Health Questionnaire-4 (PHQ-4)") + ". Developed by Drs. Robert L. Spitzer, Janet B.W. Williams, Kurt Kroenke and colleagues, with an educational grant from Pfizer Inc. No permission required to reproduce, translate, display or distribute.",
 "Oregon Pain Guidance. " + ext("https://www.oregon.gov/oha/HPA/dsi-pmc/PainCareToolbox/PHQ-4.pdf", "PHQ-4 scoring") + ". 2016.",
 "NHS. " + ext("https://www.nhs.uk/mental-health/conditions/depression-in-adults/overview/", "Depression in adults: overview") + ". Page last reviewed 5 July 2023.",
]

MOOD_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Ruh hâlinizi ölçün</h1>
    <p class="lede">Dünyada yaygın kullanılan iki kısa ölçekle son iki haftanızı değerlendirin: Dünya Sağlık Örgütü'nün iyi oluş indeksi (WHO-5) ve kaygı ile depresyon belirtilerini tarayan PHQ-4. Toplam dokuz soru, yaklaşık iki dakika. Sonuçlar tanı koymaz; ne zaman destek almanız gerektiğini görmenize yardımcı olur.</p>
    <p class="meta">Son güncelleme: 10 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>9 soru</b><span>Yaklaşık 2 dakika; son iki haftanızı sorar</span></div>
        <div class="stat"><b>213 çalışma</b><span>WHO-5'in kullanıldığı çalışmaları inceleyen sistematik derleme</span></div>
        <div class="stat"><b>%86</b><span>WHO-5'in 50 ve altı sınırıyla depresyonu yakalama oranı (18 çalışma); özgüllük %81</span></div>
        <div class="stat"><b>1.752 kişi</b><span>Türkçe WHO-5'in geçerlik ve güvenirlik çalışmasına katılanlar</span></div>
      </div>
    </div>
  </section>

  <section id="olcum">
    <div class="wrap">
      <p class="eyebrow">Birlikte yapalım</p>
      <h2>Son iki haftanız</h2>
      <div class="tool mood" id="mood">
        <div class="mq-top"><span class="mq-k" id="mq-k"></span><div class="mq-prog"><i id="mq-bar"></i></div></div>
        <div class="mq-start" id="mq-start">
          <p>Önce beş soruda iyi oluşunuzu, sonra dört soruda kaygı ve depresyon belirtilerini değerlendireceğiz. Her soruda size en yakın yanıtı seçin; doğru ya da yanlış yanıt yoktur.</p>
          <p class="priv">Yanıtlarınız yalnızca bu cihazda hesaplanır, hiçbir yere gönderilmez.</p>
          <button type="button" class="cta" id="mq-go">Başlayalım</button>
        </div>
{MQ_HTML}
        <div class="mq-nav" id="mq-nav" hidden><button type="button" class="lnk" id="mq-back">← Önceki soru</button></div>
        <div class="mq-res" id="mq-res" hidden aria-live="polite">
          <h3 style="margin:0">Sonuçlarınız</h3>
          <div class="rs-grid">
            <div class="rs"><p class="k">İyi oluş · WHO-5</p><p class="v"><b id="rw-v">0</b><span>/ 100</span></p><div class="gauge w"><i id="rw-i"></i></div><p class="t" id="rw-t"></p><p class="note2" id="rw-n"></p></div>
            <div class="rs"><p class="k">Kaygı ve depresyon · PHQ-4</p><p class="v"><b id="rp-v">0</b><span>/ 12</span><em id="rp-b"></em></p><div class="gauge p"><i id="rp-i"></i></div><p class="t" id="rp-t"></p><ul class="sub"><li id="rp-a"></li><li id="rp-d"></li></ul><p class="note2" id="rp-n"></p></div>
          </div>
          <div class="adv" id="mq-adv"><h3 id="mq-ah"></h3><p id="mq-ap"></p></div>
          <p class="crisis">Kendinize zarar verme ya da yaşamınıza son verme düşünceleriniz varsa beklemeden <b>112</b>'yi arayın ya da en yakın acil servise gidin.</p>
          <div class="mq-acts"><button type="button" class="cta" id="mq-save">Bu sonucu kaydet</button><button type="button" class="lnk" id="mq-ics">İki hafta sonrası için takvime ekle</button><button type="button" class="lnk" id="mq-again">Yeniden yap</button></div>
          <p class="count" style="margin-top:10px">Kaydederseniz sonuç yalnızca bu tarayıcıda saklanır.</p>
        </div>
        <div class="mq-hist" id="mq-hist" hidden></div>
        <div class="mq-s" hidden>
          <span data-k="kw">İyi oluş</span>
          <span data-k="kp">Belirtiler</span>
          <span data-k="w_hi">Olağan aralıkta. Danimarka'daki genel nüfus çalışmalarında ortalama puan yaklaşık 70.</span>
          <span data-k="w_mid">Düşük. Araştırmalarda 50 ve altı, depresyon açısından değerlendirme önerilen sınır.</span>
          <span data-k="w_lo">Çok düşük. Bu düzey, araştırmalarda majör depresyonu olan hastaların iyi oluş düzeyine denk geliyor.</span>
          <span data-k="w_item">Ölçeğin yönergesine göre bir soruya “Bazen” ya da “Hiçbir zaman” yanıtı verilmesi de daha ayrıntılı değerlendirme için bir işarettir.</span>
          <span data-k="p0">Olağan</span>
          <span data-k="p1">Hafif</span>
          <span data-k="p2">Orta</span>
          <span data-k="p3">Ağır</span>
          <span data-k="p_t0">Toplam puana göre belirti yok ya da çok az.</span>
          <span data-k="p_t1">Toplam puana göre hafif düzeyde belirtiler.</span>
          <span data-k="p_t2">Toplam puana göre orta düzeyde belirtiler.</span>
          <span data-k="p_t3">Toplam puana göre ağır düzeyde belirtiler.</span>
          <span data-k="sa">Kaygı</span>
          <span data-k="sd">Depresyon</span>
          <span data-k="lv_g_h">Sonuçlarınız olağan aralıkta</span>
          <span data-k="lv_g">İyi gelen alışkanlıklarınızı sürdürün. Ruh hâli zamanla değişebilir; iki hafta sonra yeniden ölçebilirsiniz.</span>
          <span data-k="lv_m_h">Hafif belirtiler var</span>
          <span data-k="lv_m">Aşağıdaki önerilerden size uygun olanları deneyin ve iki hafta sonra yeniden ölçün. Belirtiler artarsa ya da sürerse bir hekimle konuşun.</span>
          <span data-k="lv_y_h">Bir uzmanla konuşmanızı öneririz</span>
          <span data-k="lv_y">Sonuçlarınız daha ayrıntılı bir değerlendirmeyi gerektirebilir. Bir hekime ya da ruh sağlığı uzmanına başvurun; belirtileriniz günlük hayatınızı etkiliyorsa beklemeyin. Bu arada aşağıdaki öneriler de destek olabilir.</span>
          <span data-k="lv_r_h">Lütfen yakın zamanda destek alın</span>
          <span data-k="lv_r">Sonuçlarınız belirgin belirtilere işaret ediyor. Yakın zamanda bir hekime ya da ruh sağlığı uzmanına başvurmanızı öneririz. Güvendiğiniz biriyle de konuşun; yalnız değilsiniz.</span>
          <span data-k="sub_hi">İşaretli alt puan 3 ve üzerinde: bu alanda daha ayrıntılı değerlendirme önerilir.</span>
          <span data-k="saved">Kaydedildi</span>
          <span data-k="h_h">Kayıtlarınız (yalnızca bu cihazda)</span>
          <span data-k="h_date">Tarih</span>
          <span data-k="h_w">İyi oluş</span>
          <span data-k="h_p">Belirtiler</span>
          <span data-k="h_clear">Tüm kayıtları sil</span>
          <span data-k="h_conf">Bu cihazdaki tüm kayıtlar silinsin mi?</span>
          <span data-k="ch_sig">anlamlı değişim</span>
          <span data-k="ics_t">Ruh hâli ölçümü</span>
          <span data-k="ics_d">İki hafta oldu: ruh hâlinizi yeniden ölçün.</span>
          <span data-k="ics_f">ruh-hali-olcumu.ics</span>
        </div>
      </div>
      <p class="count">WHO-5'in soruları ve yanıt seçenekleri ölçeğin resmî Türkçe sürümünden alınmıştır. PHQ-4'ün geliştiricileri çoğaltma ve çeviri için izin istemez; Türkçe ifadeler bu sayfa için çevrilmiştir.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>WHO-5 nedir?</h2>
        <p class="soft">Dünya Sağlık Örgütü'nün ruh sağlığı iş birliği merkezinde geliştirilen, son iki haftadaki iyi oluşu soran beş soruluk bir ölçektir. Otuzdan fazla dile çevrildi; 213 çalışmayı inceleyen derlemeye göre hem depresyon taraması hem de tedavinin izlenmesi için uygundur.</p>
        <p class="soft">Türkçe sürümü, birinci basamakta 1.752 yetişkin ve yaşlıyla sınandı; güvenirliği yüksek bulundu.</p>
      </div>
      <div>
        <h2>PHQ-4 nedir?</h2>
        <p class="soft">Kaygı için iki, depresyon için iki sorudan oluşan çok kısa bir tarama ölçeğidir. ABD'de 15 aile hekimliği kliniğinde 2.149 hastayla geliştirildi. Puan yükseldikçe günlük işlevlerde bozulma, işe gidilemeyen günler ve sağlık hizmeti kullanımı da arttı.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Puanlar ne anlama gelir?</h2>
      <div class="bands">
        <ul class="tx">
          <li><b>WHO-5: 51–100</b><span>Olağan aralık. Genel nüfusta ortalama yaklaşık 70.</span></li>
          <li><b>WHO-5: 50 ve altı</b><span>Düşük iyi oluş; depresyon açısından değerlendirme önerilir.</span></li>
          <li><b>WHO-5: 28 ve altı</b><span>Majör depresyonu olan hastalardaki iyi oluş düzeyine denk gelir.</span></li>
          <li><b>WHO-5: 10 puanlık değişim</b><span>İki ölçüm arasında anlamlı kabul edilen fark.</span></li>
        </ul>
        <ul class="tx">
          <li><b>PHQ-4: 0–2</b><span>Olağan.</span></li>
          <li><b>PHQ-4: 3–5</b><span>Hafif belirtiler.</span></li>
          <li><b>PHQ-4: 6–8</b><span>Orta düzeyde belirtiler.</span></li>
          <li><b>PHQ-4: 9–12</b><span>Ağır belirtiler.</span></li>
          <li><b>Alt puanlar: 3 ve üzeri</b><span>İlk iki soruda kaygı, son iki soruda depresyon açısından daha ayrıntılı değerlendirme önerilir.</span></li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Sonuç ne söyler, ne söylemez?</h2>
        <p class="soft">Bu ölçekler tanı koymaz; daha ayrıntılı bir değerlendirmeye ihtiyaç olup olmadığını gösterir. Tanı, bir hekim ya da ruh sağlığı uzmanının görüşmesiyle konur.</p>
      </div>
      <ul class="dots">
        <li>Sonuç yalnızca son iki haftayı yansıtır.</li>
        <li>Yas, yoğun stres, uykusuzluk ya da bedensel bir hastalık puanları etkileyebilir.</li>
        <li>Yüksek belirti puanı, kesin bir sorun olduğu anlamına gelmez; düşük puan da her şeyin yolunda olduğunu garanti etmez.</li>
        <li>Kendinizi kötü hissediyorsanız puan ne olursa olsun bir uzmanla konuşun.</li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ruh hâlinize iyi gelebilecekler</h2>
      <ul class="tx">
        <li><b><a href="ruh-sagligi-egzersiz.html">Ruh sağlığı için egzersiz</a></b><span>Depresyon ve kaygıda hangi egzersiz ne kadar işe yarıyor; evde altı hareket.</span></li>
        <li><b><a href="ic-cekis.html">5 dakikalık iç çekiş nefesi</a></b><span>Ruh hâlini iyileştiren kısa bir nefes egzersizi, zamanlayıcıyla.</span></li>
        <li><b><a href="dost-molasi.html">DOST molası</a></b><span>Zor bir günde kendinize dost olmanın dört adımı.</span></li>
        <li><b><a href="doga-recetesi.html">Doğa reçetesi</a></b><span>Haftada 120 dakika doğada vakit geçirmek için bir plan.</span></li>
        <li><b><a href="bag-kurmak.html">Sosyal bağ ve sağlık</a></b><span>Yalnızlıkla baş etmek ve bağları güçlendirmek için.</span></li>
        <li><b><a href="uyku.html">İyi uyku için</a></b><span>Uykunuzu düzenlemek için öneriler ve yatma saati planlayıcı.</span></li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(MOOD_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Ne zaman yardım almalı?</h2>
      <ul class="dots redflags">
        <li>Kendinize zarar verme ya da yaşamınıza son verme düşünceleriniz varsa beklemeden 112'yi arayın ya da en yakın acil servise gidin.</li>
        <li>Haftalardır süren mutsuzluk, umutsuzluk, eskiden keyif aldığınız şeylere ilgisizlik, uyku ya da iştah değişiklikleri varsa bir hekime ya da ruh sağlığı uzmanına başvurun.</li>
        <li>Kaygı ya da çökkünlük işinizi, ilişkilerinizi ya da günlük işlerinizi aksatıyorsa destek almayı ertelemeyin.</li>
        <li>Bir yakınınız için endişeleniyorsanız onunla konuşun ve destek almasına yardımcı olun.</li>
      </ul>
      <div class="note" style="margin-top:22px"><strong>Önemli:</strong> Bu sayfa bilgilendirme amaçlıdır; tanı koymaz ve tedavinin yerine geçmez.</div>
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(MOOD_SRC)}
    </div>
  </section>
</main>'''

MOOD_JS = '''<script>
(function(){
  var root = document.getElementById('mood'); if (!root) return;
  var S = {}; root.querySelectorAll('.mq-s [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.innerHTML; });
  var EN = document.documentElement.lang === 'en', LANG = EN ? 'en-GB' : 'tr-TR', KEY = 'drihsaneren.ruhhali.v1';
  var $ = function(id){ return document.getElementById(id); };
  var Q = [].slice.call(root.querySelectorAll('fieldset.mq')), N = Q.length, ans = [], cur = -1, last = null, savedNow = false;
  function txt(h){ var d = document.createElement('div'); d.innerHTML = h; return d.textContent; }
  function load(){ try { var v = JSON.parse(localStorage.getItem(KEY) || '[]'); return Array.isArray(v) ? v : []; } catch (e) { return []; } }
  function store(v){ try { localStorage.setItem(KEY, JSON.stringify(v)); return true; } catch (e) { return false; } }
  function keep(){ var r = root.getBoundingClientRect(); if (r.top < 0 || r.top > innerHeight * .6) root.scrollIntoView({block: 'start'}); }
  function show(i){
    cur = i; $('mq-start').hidden = i !== -1; root.querySelector('.mq-top').style.visibility = i === -1 ? 'hidden' : ''; $('mq-res').hidden = i !== N; $('mq-nav').hidden = i < 0 || i >= N;
    Q.forEach(function(q, j){ q.hidden = j !== i; });
    $('mq-bar').style.width = (i < 0 ? 0 : Math.min(1, i / N) * 100) + '%';
    $('mq-k').textContent = i < 0 || i >= N ? '' : txt(Q[i].getAttribute('data-g') === 'w' ? S.kw : S.kp) + ' · ' + (i + 1) + ' / ' + N;
    $('mq-back').disabled = i <= 0;
  }
  Q.forEach(function(q, i){
    q.querySelector('.opts').addEventListener('click', function(e){
      var b = e.target.closest('button'); if (!b) return;
      q.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      ans[i] = +b.getAttribute('data-v');
      setTimeout(function(){ if (cur !== i) return; if (i < N - 1) { show(i + 1); var f = Q[i + 1].querySelector('button[aria-pressed="true"]') || Q[i + 1].querySelector('button'); try { f.focus({preventScroll: true}); } catch (e) {} } else result(); keep(); }, 260);
    });
  });
  $('mq-go').addEventListener('click', function(){ show(0); try { Q[0].querySelector('button').focus({preventScroll: true}); } catch (e) {} keep(); });
  $('mq-back').addEventListener('click', function(){ if (cur > 0) { show(cur - 1); keep(); } });
  $('mq-again').addEventListener('click', function(){ ans = []; Q.forEach(function(q){ q.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', 'false'); }); }); show(0); keep(); });
  function result(){
    var w = 0, low = false; for (var i = 0; i < 5; i++){ w += ans[i]; if (ans[i] <= 1) low = true; }
    var W = w * 4, a = ans[5] + ans[6], d = ans[7] + ans[8], P = a + d;
    last = {d: new Date().toISOString(), w: W, p: P, a: a, dp: d}; savedNow = false;
    show(N); $('mq-bar').style.width = '100%';
    $('rw-v').textContent = W; $('rw-i').style.left = W + '%';
    $('rw-t').innerHTML = W > 50 ? S.w_hi : (W > 28 ? S.w_mid : S.w_lo);
    $('rw-n').innerHTML = low && W > 50 ? S.w_item : ''; $('rw-n').hidden = !(low && W > 50);
    var pb = P <= 2 ? 0 : P <= 5 ? 1 : P <= 8 ? 2 : 3;
    $('rp-v').textContent = P; $('rp-i').style.left = (P / 12 * 100) + '%'; $('rp-b').innerHTML = S['p' + pb]; $('rp-t').innerHTML = S['p_t' + pb];
    $('rp-a').innerHTML = S.sa + ': <b>' + a + '</b>/6'; $('rp-a').className = a >= 3 ? 'hi' : '';
    $('rp-d').innerHTML = S.sd + ': <b>' + d + '</b>/6'; $('rp-d').className = d >= 3 ? 'hi' : '';
    $('rp-n').innerHTML = (a >= 3 || d >= 3) ? S.sub_hi : ''; $('rp-n').hidden = !(a >= 3 || d >= 3);
    var lv = (W <= 28 || P >= 9) ? 'r' : (W <= 50 || P >= 6 || a >= 3 || d >= 3) ? 'y' : (P >= 3 || low) ? 'm' : 'g';
    $('mq-adv').className = 'adv ' + lv; $('mq-ah').innerHTML = S['lv_' + lv + '_h']; $('mq-ap').innerHTML = S['lv_' + lv];
    var b = $('mq-save'); b.disabled = false; b.textContent = b.getAttribute('data-l');
    hist();
  }
  $('mq-save').setAttribute('data-l', $('mq-save').textContent);
  $('mq-save').addEventListener('click', function(){
    if (!last || savedNow) return; var h = load(); h.push(last); if (h.length > 26) h = h.slice(-26);
    if (store(h)) { savedNow = true; this.textContent = txt(S.saved) + ' ✓'; this.disabled = true; hist(); }
  });
  function fmt(iso){ try { return new Date(iso).toLocaleDateString(LANG, {day: 'numeric', month: 'short', year: 'numeric'}); } catch (e) { return iso.slice(0, 10); } }
  function hist(){
    var h = load(), box = $('mq-hist'); if (!h.length) { box.hidden = true; box.innerHTML = ''; return; }
    var rows = h.slice().reverse().slice(0, 8).map(function(r, i, arr){
      var prev = arr[i + 1], ch = '';
      if (prev) { var n = r.w - prev.w; ch = '<small>' + (n > 0 ? '+' : n < 0 ? '−' : '±') + Math.abs(n) + (Math.abs(n) >= 10 ? ' · ' + txt(S.ch_sig) : '') + '</small>'; }
      return '<tr><td>' + fmt(r.d) + '</td><td><b>' + r.w + '</b>' + ch + '</td><td><b>' + r.p + '</b></td></tr>';
    }).join('');
    box.innerHTML = '<h3>' + S.h_h + '</h3><table class="mq-tab"><thead><tr><th>' + S.h_date + '</th><th>' + S.h_w + ' · WHO-5</th><th>' + S.h_p + ' · PHQ-4</th></tr></thead><tbody>' + rows + '</tbody></table>' +
      '<p style="margin:10px 0 0"><button type="button" class="lnk" id="mq-clear">' + S.h_clear + '</button></p>';
    box.hidden = false;
    $('mq-clear').addEventListener('click', function(){ if (!confirm(txt(S.h_conf))) return; try { localStorage.removeItem(KEY); } catch (e) {} savedNow = false; var b = $('mq-save'); b.disabled = false; b.textContent = b.getAttribute('data-l'); hist(); });
  }
  $('mq-ics').addEventListener('click', function(){
    var t = new Date(); t.setDate(t.getDate() + 14); t.setHours(20, 0, 0, 0);
    function p2(n){ return (n < 10 ? '0' : '') + n; }
    var ds = t.getFullYear() + p2(t.getMonth() + 1) + p2(t.getDate()) + 'T' + p2(t.getHours()) + p2(t.getMinutes()) + '00';
    var n = new Date(), stamp = n.getUTCFullYear() + p2(n.getUTCMonth() + 1) + p2(n.getUTCDate()) + 'T' + p2(n.getUTCHours()) + p2(n.getUTCMinutes()) + p2(n.getUTCSeconds()) + 'Z';
    function esc(s){ return s.replace(/([,;\\\\])/g, '\\\\$1').replace(/\\n/g, '\\\\n'); }
    var body = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//drihsaneren.com//mood//' + (EN ? 'EN' : 'TR'), 'BEGIN:VEVENT', 'UID:mood-' + Date.now() + '@drihsaneren.com', 'DTSTAMP:' + stamp, 'DTSTART:' + ds, 'DURATION:PT10M',
      'SUMMARY:' + esc(txt(S.ics_t)), 'DESCRIPTION:' + esc(txt(S.ics_d)) + ' ' + location.href.split('#')[0], 'END:VEVENT', 'END:VCALENDAR'].join('\\r\\n');
    var a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([body], {type: 'text/calendar;charset=utf-8'})); a.download = txt(S.ics_f); document.body.appendChild(a); a.click();
    setTimeout(function(){ URL.revokeObjectURL(a.href); a.remove(); }, 1500);
  });
  show(-1); hist();
})();
</script>
'''

page("ruh-hali-olcumu.html", "Ruh Hâlinizi Ölçün",
     "Dünya Sağlık Örgütü'nün iyi oluş indeksi (WHO-5) ve kaygı ile depresyonu tarayan PHQ-4 ile son iki haftanızı değerlendirin: 9 soru, 2 dakika. Puanların anlamı, ne zaman destek almalı ve sonuçlarınızı cihazınızda izleme.",
     "ruh-hali-olcumu.html", MOOD_CSS, MOOD_BODY, MOOD_JS,
     seo_title="Ruh Hâli Testi: WHO-5 İyi Oluş ve PHQ-4 Kaygı-Depresyon Taraması | İhsan Eren",
     about=[cond("Depresyon"), cond("Kaygı bozukluğu (anksiyete)")], faq_items=MOOD_FAQ)

# ============================================================== 3 · AŞAMALI KAS GEVŞETME (zamanlayıcılı)
PMR_CSS = MIND_CSS + """
  .pm{display:grid;grid-template-columns:200px minmax(0,1fr);gap:clamp(18px,4vw,36px);align-items:center}
  @media (max-width:640px){.pm{grid-template-columns:1fr;gap:10px}.pm-fig svg{height:190px}}
  .pm-fig{display:grid;place-items:center}
  .pm-fig svg{width:auto;height:300px;overflow:visible}
  .pm-fig .rg{fill:rgba(236,229,207,.08);stroke:rgba(236,229,207,.28);stroke-width:1.2;transition:fill .5s ease,stroke .5s ease;transform-box:fill-box;transform-origin:center}
  .pm-fig .rg.done{fill:rgba(143,164,118,.28);stroke:rgba(143,164,118,.6)}
  .pm-fig .rg.on{fill:rgba(226,171,71,.35);stroke:#e2ab47}
  .pm-fig .rg.tense{fill:#e2ab47;stroke:#f3d58f;animation:pmq .5s ease-in-out infinite alternate;filter:drop-shadow(0 0 6px rgba(226,171,71,.7))}
  .pm-fig .rg.rel{fill:#8fa476;stroke:#b9cba0;transition:fill 2.5s ease,stroke 2.5s ease}
  @keyframes pmq{from{transform:scale(1)}to{transform:scale(.94)}}
  @media (prefers-reduced-motion:reduce){.pm-fig .rg.tense{animation:none}}
  .pm-ph{margin:0;font-size:12px;letter-spacing:.2em;text-transform:uppercase;font-weight:700;color:var(--foil);min-height:16px}
  .pm-ph.t{color:#f3d58f}.pm-ph.r{color:#b9cba0}
  .pm-row{display:flex;align-items:baseline;gap:16px;margin:6px 0 4px}
  .pm-n{font-family:var(--display);font-size:clamp(46px,9vw,64px);line-height:1;color:var(--ink);min-width:1.2ch;font-variant-numeric:tabular-nums}
  .pm-n:empty{display:none}
  .pm-name{font-family:var(--display);font-size:clamp(21px,4vw,26px);line-height:1.2;color:var(--ink);margin:0}
  .pm-cue{margin:4px 0 0;color:var(--ink-soft);font-size:15.5px;min-height:3em}
  .pm-meta{display:flex;justify-content:space-between;gap:10px;font-size:13px;color:var(--muted);margin:14px 0 6px;font-variant-numeric:tabular-nums}
  .pm-bar{height:4px;border-radius:2px;background:rgba(236,229,207,.12);overflow:hidden}
  .pm-bar i{display:block;height:100%;width:0;background:var(--foil)}
  .pm-lists{display:grid;grid-template-columns:1fr 1fr;gap:clamp(18px,4vw,40px)}
  @media (max-width:760px){.pm-lists{grid-template-columns:1fr}}
  .pm-lists h3{font-size:19px;margin:0 0 12px}
  ol.steps li span{color:var(--ink-soft)}
"""

# (bölge kimlikleri, ad, nasıl sıkılır) — sıra ve tarifler CCI (Batı Avustralya) PMR bilgi sayfasından
PMR_FULL = [
 ("farm-r", "Sağ el ve ön kol", "Sağ elinizi sıkıca yumruk yapın."),
 ("uarm-r", "Sağ üst kol", "Sağ ön kolunuzu omzunuza doğru bükün, pazınızı sıkın."),
 ("farm-l", "Sol el ve ön kol", "Sol elinizi sıkıca yumruk yapın."),
 ("uarm-l", "Sol üst kol", "Sol ön kolunuzu omzunuza doğru bükün, pazınızı sıkın."),
 ("head", "Alın", "Kaşlarınızı olabildiğince yukarı kaldırın."),
 ("head", "Gözler ve yanaklar", "Gözlerinizi sıkıca yumun."),
 ("head", "Ağız ve çene", "Ağzınızı esner gibi geniş açın."),
 ("neck", "Boyun", "Yüzünüz önde, başınızı yavaşça geriye, tavana bakar gibi götürün. Zorlamayın."),
 ("shoulders", "Omuzlar", "Omuzlarınızı kulaklarınıza doğru kaldırın."),
 ("chest", "Sırt", "Kürek kemiklerinizi geriye doğru sıkıştırın, göğsünüzü öne itin."),
 ("chest belly", "Göğüs ve karın", "Derin bir nefes alın; göğsünüzü ve karnınızı havayla doldurun."),
 ("hips", "Kalçalar", "Kalça kaslarınızı birbirine doğru sıkın."),
 ("thigh-r", "Sağ uyluk", "Sağ uyluğunuzun kaslarını sıkın."),
 ("calf-r", "Sağ baldır", "Sağ ayak parmaklarınızı yavaşça kendinize doğru çekin. Kramp girmemesi için yavaş olun."),
 ("foot-r", "Sağ ayak", "Sağ ayak parmaklarınızı aşağı doğru kıvırın."),
 ("thigh-l", "Sol uyluk", "Sol uyluğunuzun kaslarını sıkın."),
 ("calf-l", "Sol baldır", "Sol ayak parmaklarınızı yavaşça kendinize doğru çekin. Kramp girmemesi için yavaş olun."),
 ("foot-l", "Sol ayak", "Sol ayak parmaklarınızı aşağı doğru kıvırın."),
]
PMR_SHORT = [
 ("farm-r farm-l uarm-r uarm-l", "Eller ve kollar", "İki elinizi yumruk yapın, ön kollarınızı omuzlarınıza doğru bükün."),
 ("head", "Yüz", "Kaşlarınızı kaldırın, gözlerinizi sıkıca yumun, dişlerinizi hafifçe sıkın."),
 ("neck shoulders", "Boyun ve omuzlar", "Omuzlarınızı kulaklarınıza doğru kaldırın."),
 ("chest", "Sırt ve göğüs", "Kürek kemiklerinizi geriye sıkıştırın, derin bir nefes alın."),
 ("belly hips", "Karın ve kalçalar", "Karın ve kalça kaslarınızı birlikte sıkın."),
 ("thigh-r thigh-l calf-r calf-l", "Bacaklar", "Uyluklarınızı sıkın, ayak parmaklarınızı yavaşça kendinize doğru çekin."),
 ("foot-r foot-l", "Ayaklar", "Ayak parmaklarınızı aşağı doğru kıvırın."),
]
def _pm_list(rows, lid):
    return f'<ol class="steps" id="{lid}">' + "".join(f'<li data-r="{r}"><div><strong>{n}.</strong> <span>{c}</span></div></li>' for r, n, c in rows) + '</ol>'

PMR_FIG = '''<svg viewBox="0 0 120 244" aria-hidden="true">
  <circle class="rg" data-g="head" cx="60" cy="22" r="16"/>
  <rect class="rg" data-g="neck" x="54" y="38" width="12" height="11" rx="3"/>
  <rect class="rg" data-g="shoulders" x="30" y="49" width="60" height="12" rx="6"/>
  <rect class="rg" data-g="chest" x="36" y="62" width="48" height="34" rx="7"/>
  <rect class="rg" data-g="belly" x="38" y="97" width="44" height="27" rx="7"/>
  <rect class="rg" data-g="hips" x="36" y="125" width="48" height="18" rx="8"/>
  <rect class="rg" data-g="uarm-r" x="17" y="56" width="12" height="44" rx="6"/>
  <rect class="rg" data-g="uarm-l" x="91" y="56" width="12" height="44" rx="6"/>
  <path class="rg" data-g="farm-r" d="M15 107 a6 6 0 0 1 12 0 V142 a8 8 0 1 1 -12 0 Z"/>
  <path class="rg" data-g="farm-l" d="M93 107 a6 6 0 0 1 12 0 V142 a8 8 0 1 1 -12 0 Z"/>
  <rect class="rg" data-g="thigh-r" x="38" y="145" width="21" height="48" rx="9"/>
  <rect class="rg" data-g="thigh-l" x="61" y="145" width="21" height="48" rx="9"/>
  <rect class="rg" data-g="calf-r" x="40" y="195" width="17" height="34" rx="8"/>
  <rect class="rg" data-g="calf-l" x="63" y="195" width="17" height="34" rx="8"/>
  <ellipse class="rg" data-g="foot-r" cx="46" cy="236" rx="11" ry="5.5"/>
  <ellipse class="rg" data-g="foot-l" cx="74" cy="236" rx="11" ry="5.5"/>
</svg>'''

PMR_FAQ = [
 ("Uykuya dalmak için işe yarar mı?", "Amerikan Uyku Tıbbı Akademisi'nin kılavuzu, gevşeme yöntemlerini süregelen uykusuzlukta tek başına kullanılabilecek tedaviler arasında sayıyor (koşullu öneri). Akşam yatmadan önce ya da yatakta yapabilirsiniz. Uzun süren uykusuzlukta en güçlü önerilen tedavi, uykusuzluk için bilişsel davranışçı terapidir."),
 ("Ne sıklıkla yapmalıyım?", "İncelenen çalışmalarda uygulama her günden haftada birkaç güne kadar değişiyordu. Kaygıda gevşeme eğitimini inceleyen analizde evde düzenli pratik yapılan programlar daha etkiliydi. Öğrenirken her gün yapmayı deneyin; zamanla kısa sürümü gün içinde de kullanabilirsiniz."),
 ("Ağrılı ya da yaralı bir bölgem var; yapabilir miyim?", "O bölgeyi atlayın ya da yalnızca çok hafif sıkın. Yaralanmanız ya da kas ağrısına yol açan bir sorununuz varsa başlamadan önce hekiminize danışın. Kaslarınızı ağrı yapacak kadar değil, gerginliği hissedecek kadar sıkın."),
 ("Nefes egzersizlerinden farkı ne?", "Nefes egzersizleri soluk alıp vermeye, kas gevşetme ise kasların gerilip bırakılmasına odaklanır. İncelenen çalışmalarda kas gevşetme başka yöntemlerle birleştirildiğinde etkisi daha belirgindi; ikisini birlikte de deneyebilirsiniz."),
]

PMR_SRC = [
 "Muhammad Khir S, Wan Mohd Yunus WMA, Mahmud N, et al. " + ext("https://dovepress.com/efficacy-of-progressive-muscle-relaxation-in-adults-for-stress-anxiety-peer-reviewed-fulltext-article-PRBM", "Efficacy of progressive muscle relaxation in adults for stress, anxiety, and depression: a systematic review") + ". Psychol Res Behav Manag. 2024;17:345–365.",
 "Manzoni GM, Pagnini F, Castelnuovo G, Molinari E. " + ext("https://www.biomedcentral.com/1471-244X/8/41", "Relaxation training for anxiety: a ten-years systematic review with meta-analysis") + ". BMC Psychiatry. 2008;8:41.",
 "Edinger JD, Arnedt JT, Bertisch SM, et al. Behavioral and psychological treatments for chronic insomnia disorder in adults: an American Academy of Sleep Medicine clinical practice guideline. J Clin Sleep Med. 2021;17(2):255–262. Özet: " + ext("https://www.ajmc.com/view/new-aasm-guidelines-support-behavioral-psychological-treatments-for-insomnia", "AJMC, New AASM guidelines support behavioral, psychological treatments for insomnia") + ", 5 January 2021.",
 "Centre for Clinical Interventions (Government of Western Australia). " + ext("https://www.cci.health.wa.gov.au/-/media/CCI/Mental-Health-Professionals/Social-Anxiety/Social-Anxiety---Information-Sheets/Social-Anxiety-Information-Sheet---04---Progressive-Muscle-Relaxation.pdf", "Progressive muscle relaxation") + ". Information sheet.",
 "University College London Hospitals NHS Foundation Trust. " + ext("https://uclh.nhs.uk/patients-and-visitors/patient-information-pages/relaxation-techniques", "Relaxation techniques") + ". Last updated 29 May 2024.",
 "Anxiety Canada. " + ext("https://admin.heretohelp.bc.ca/infosheet/how-to-do-progressive-muscle-relaxation", "How to do progressive muscle relaxation") + ". HeretoHelp.",
]

PMR_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Kas gevşetme: sesli rehberle</h1>
    <p class="lede">Aşamalı kas gevşetme, 1930'larda Edmund Jacobson'ın geliştirdiği bir yöntemdir: Bir kas grubunu birkaç saniye sıkar, sonra bırakır ve aradaki farkı fark edersiniz. Araştırmalar stres, kaygı ve uykusuzlukta yararlı olabildiğini gösteriyor. Aşağıdaki zamanlayıcı her adımı söyler; gözlerinizi kapatıp izleyebilirsiniz.</p>
    <p class="meta">Son güncelleme: 10 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>46 çalışma</b><span>Yetişkinlerde kas gevşetmeyi inceleyen 2024 tarihli sistematik derleme; 3.402 kişi, 16 ülke</span></div>
        <div class="stat"><b>27 çalışma</b><span>Kaygıda gevşeme eğitimini inceleyen analiz; orta-büyük düzeyde etki</span></div>
        <div class="stat"><b>5 + 10 sn</b><span>Her kas grubunu yaklaşık 5 saniye sıkın, 10 saniye bırakın</span></div>
        <div class="stat"><b>6 dakika</b><span>18 bölgelik tam sürüm; kısa sürüm yaklaşık 3 dakika</span></div>
      </div>
    </div>
  </section>

  <section id="gevsetme">
    <div class="wrap">
      <p class="eyebrow">Birlikte yapalım</p>
      <h2>Sesli kas gevşetme rehberi</h2>
      <p class="soft">Rahat bir sandalyeye oturun ya da uzanın. Sesi açın; rehber her bölgeyi söyleyecek. Kaslarınızı ağrı yapacak kadar değil, gerginliği hissedecek kadar sıkın.</p>
      <div class="tool">
        <div class="pm" id="pm">
          <div class="pm-fig">{PMR_FIG}</div>
          <div>
            <p class="pm-ph" id="pm-ph" aria-live="polite"></p>
            <div class="pm-row"><span class="pm-n" id="pm-n"></span><div><p class="pm-name" id="pm-name">Hazır olduğunuzda başlayın</p></div></div>
            <p class="pm-cue" id="pm-cue">Rahat bir yere oturun ya da uzanın; isterseniz gözlerinizi kapatın.</p>
            <div class="pm-meta"><span id="pm-step">&nbsp;</span><span id="pm-left">6:00</span></div>
            <div class="pm-bar"><i id="pm-bar"></i></div>
            <p class="q">Sürüm</p>
            <div class="seg" role="group" aria-label="Sürüm" id="pm-ver">
              <button type="button" data-v="f" aria-pressed="true">Tam (18 bölge)</button>
              <button type="button" data-v="s" aria-pressed="false">Kısa (7 bölge)</button>
            </div>
            <p class="q">Gevşeme süresi</p>
            <div class="seg" role="group" aria-label="Gevşeme süresi" id="pm-pace">
              <button type="button" data-v="10" aria-pressed="true">10 saniye</button>
              <button type="button" data-v="20" aria-pressed="false">20 saniye</button>
            </div>
            <div class="controls" style="margin-top:14px">
              <button type="button" class="cta" id="pm-go">Başlat</button>
              <button type="button" class="cta ghost" id="pm-reset">Sıfırla</button>
            </div>
            <label class="snd"><input type="checkbox" id="pm-voice" checked> Sesli yönlendirme</label>
          </div>
        </div>
        <div class="pm-s" hidden>
          <span data-k="ready">Hazır olduğunuzda başlayın</span>
          <span data-k="readys">Rahat bir yere oturun ya da uzanın; isterseniz gözlerinizi kapatın.</span>
          <span data-k="intro">Başlıyoruz</span>
          <span data-k="intros">Rahat bir pozisyon bulun. Nefesinizi yavaşlatın ve kendinize gevşemek için izin verin.</span>
          <span data-k="prep">Sıradaki bölge</span>
          <span data-k="tense">Sıkın</span>
          <span data-k="rel">Bırakın</span>
          <span data-k="rels">Gerginliğin akıp gittiğini, kaslarınızın ağırlaştığını fark edin.</span>
          <span data-k="outro">Tüm bedeniniz gevşek</span>
          <span data-k="outros">Bir süre böyle kalın, nefesinizi izleyin. Kalkmadan önce birkaç dakika oturun.</span>
          <span data-k="done">Tamamlandı</span>
          <span data-k="dones">Nasıl hissediyorsunuz? Bu rehberi her gün, özellikle yatmadan önce tekrarlayabilirsiniz.</span>
          <span data-k="paused">Duraklatıldı</span>
          <span data-k="step">{{i}} / {{n}}</span>
          <span data-k="start">Başlat</span>
          <span data-k="pause">Duraklat</span>
          <span data-k="resume">Devam et</span>
          <span data-k="again">Baştan başla</span>
          <span data-k="v_rel">Ve bırakın.</span>
        </div>
      </div>
      <p class="count">Bir bölge ağrıyorsa ya da yaralıysa o adımı hafif yapın ya da yalnızca gevşemeye odaklanın. Baş dönmesi ya da kramp olursa durun.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <p class="eyebrow">Adım adım</p>
      <h2>Hangi bölge, nasıl sıkılır?</h2>
      <p class="soft">Her bölgeyi yaklaşık 5 saniye sıkın, sonra bırakıp 10 saniye gevşemeyi fark edin. Sıra ve tarifler Batı Avustralya hükümetinin klinik müdahale merkezinin (CCI) kılavuzundan alındı; kısa sürüm bu bölgeleri birleştirir.</p>
      <div class="pm-lists">
        <div><h3>Tam sürüm</h3>{_pm_list(PMR_FULL, "pm-full")}</div>
        <div><h3>Kısa sürüm</h3>{_pm_list(PMR_SHORT, "pm-short")}</div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Araştırma ne buldu?</h2>
        <p class="soft">2024'te yayımlanan sistematik derleme 16 ülkeden 46 çalışmayı inceledi; katılımcıların çoğu hemşireler, öğrenciler, bakım verenler, yaşlılar ve çalışanlar gibi hastalık tanısı olmayan yetişkinlerdi.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Çalışmaların 24'ü stresin, 21'i kaygının, 11'i depresyon belirtilerinin azaldığını gösterdi; bazı çalışmalarda fark bulunmadı.</li>
        <li>Seanslar 5 ile 28 dakika arasındaydı; seans süresi ve sıklığı sonucu belirgin biçimde değiştirmedi.</li>
        <li>Kas gevşetme başka yöntemlerle birleştirildiğinde etkisi daha belirgindi.</li>
        <li>Kaygıda gevşeme eğitimini inceleyen 27 çalışmalık analizde etki orta-büyük düzeydeydi; daha uzun süren ve evde pratik yapılan programlar daha etkiliydi.</li>
        <li>Amerikan Uyku Tıbbı Akademisi, gevşeme yöntemlerini süregelen uykusuzlukta koşullu olarak öneriyor.</li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Püf noktaları</h2>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Sakin bir an seçin</h3><p>Ağır bir yemekten ya da alkolden hemen sonra yapmayın. Telefonunuzun bildirimlerini kısa bir süre kapatın.</p></div>
        <div class="kind"><span class="n">2</span><h3>Ağrıtmadan sıkın</h3><p>Gerginliği hissetmeniz yeterli. Boyun ve baldırda özellikle yavaş ve dikkatli olun; baldırda kramp girebilir.</p></div>
        <div class="kind"><span class="n">3</span><h3>Farkı fark edin</h3><p>Asıl beceri, bıraktığınız andaki gevşemeyi fark etmektir. Zamanla gergin olduğunuz anları daha erken yakalarsınız.</p></div>
        <div class="kind"><span class="n">4</span><h3>Düzenli pratik yapın</h3><p>Öğrenirken her gün, örneğin yatmadan önce yapın. Alıştıkça kısa sürümü gün içinde gergin anlarda kullanın.</p></div>
      </div>
      <p class="soft" style="margin-top:18px">Nefese odaklanan bir yöntem için <a href="ic-cekis.html">5 dakikalık iç çekiş nefesi</a>, uykunuz için <a href="uyku.html">İyi uyku için</a> sayfasına, ruh hâlinizi izlemek için <a href="ruh-hali-olcumu.html">Ruh hâlinizi ölçün</a> sayfasına bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(PMR_FAQ)}
      <div class="note" style="margin-top:22px"><strong>Destek almak önemlidir:</strong> Haftalardır süren kaygı, çökkünlük ya da uyku sorunları gevşeme egzersizleriyle geçmiyorsa bir hekime ya da ruh sağlığı uzmanına başvurun. Kendinize zarar verme düşünceleriniz varsa 112'yi arayın.</div>
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(PMR_SRC)}
    </div>
  </section>
</main>'''

PMR_JS = '''<script>
(function(){
  var root = document.getElementById('pm'); if (!root) return;
  var S = {}; document.querySelectorAll('.pm-s [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var EN = document.documentElement.lang === 'en', LANG = EN ? 'en-GB' : 'tr-TR';
  var $ = function(id){ return document.getElementById(id); };
  function read(id){ return [].map.call(document.querySelectorAll('#' + id + ' li'), function(li){
    return { n: li.querySelector('strong').textContent.replace(/[.:]\\s*$/, ''), c: li.querySelector('span').textContent, r: li.getAttribute('data-r').split(' ') }; }); }
  var LISTS = { f: read('pm-full'), s: read('pm-short') }, ver = 'f', rel = 10, PREP = 4, TENSE = 5, INTRO = 10, OUTRO = 20;
  var RG = [].slice.call(root.querySelectorAll('.rg'));
  var segs = [], total = 0, el = 0, si = -1, running = false, state = 'idle', raf = 0, last = 0, ctx = null, lock = null, snd = $('pm-voice');
''' + WAKE_JS + '''
  function say(t){ if (!snd.checked || !('speechSynthesis' in window)) return; try { var u = new SpeechSynthesisUtterance(t); u.lang = LANG; u.rate = .92; speechSynthesis.speak(u); } catch (e) {} }
  function hush(){ try { speechSynthesis.cancel(); } catch (e) {} }
  function build(){
    segs = [{k: 'intro', d: INTRO}]; var L = LISTS[ver];
    L.forEach(function(s, i){ segs.push({k: 'prep', i: i, d: PREP}, {k: 'tense', i: i, d: TENSE}, {k: 'rel', i: i, d: rel}); });
    segs.push({k: 'outro', d: OUTRO}); total = segs.reduce(function(a, s){ return a + s.d; }, 0);
  }
  function mmss(s){ s = Math.max(0, Math.ceil(s)); var m = Math.floor(s / 60), r = s % 60; return m + ':' + (r < 10 ? '0' : '') + r; }
  function paint(i, k){
    var L = LISTS[ver], cur = i >= 0 ? L[i].r : [];
    var doneSet = {}; for (var j = 0; j < (k === 'outro' ? L.length : i); j++) L[j].r.forEach(function(g){ doneSet[g] = 1; });
    RG.forEach(function(e){ var g = e.getAttribute('data-g'), on = cur.indexOf(g) >= 0;
      e.classList.toggle('on', on && k === 'prep'); e.classList.toggle('tense', on && k === 'tense'); e.classList.toggle('rel', on && k === 'rel');
      e.classList.toggle('done', !on && !!doneSet[g] && k !== 'outro'); if (k === 'outro') { e.classList.remove('done'); e.classList.add('rel'); } });
  }
  function enter(n){
    si = n; var s = segs[n], L = LISTS[ver], ph = $('pm-ph');
    ph.className = 'pm-ph' + (s.k === 'tense' ? ' t' : s.k === 'rel' || s.k === 'outro' ? ' r' : '');
    if (s.k === 'intro') { ph.textContent = S.intro; $('pm-name').textContent = S.intro; $('pm-cue').textContent = S.intros; say(S.intros); }
    else if (s.k === 'outro') { ph.textContent = ''; $('pm-name').textContent = S.outro; $('pm-cue').textContent = S.outros; say(S.outro + '. ' + S.outros); beep(392, .5, .07); }
    else {
      var st = L[s.i]; $('pm-name').textContent = st.n;
      if (s.k === 'prep') { ph.textContent = S.prep; $('pm-cue').textContent = st.c; say(st.n + '. ' + st.c); }
      if (s.k === 'tense') { ph.textContent = S.tense; beep(660, .18, .09); }
      if (s.k === 'rel') { ph.textContent = S.rel; $('pm-cue').textContent = S.rels; beep(330, .6, .07); say(S.v_rel); }
      $('pm-step').textContent = S.step.replace('{i}', s.i + 1).replace('{n}', L.length);
    }
    if (s.k === 'intro' || s.k === 'outro') $('pm-step').textContent = '\\u00a0';
    paint(s.i === undefined ? -1 : s.i, s.k);
  }
  function startOf(n){ var t = 0; for (var j = 0; j < n; j++) t += segs[j].d; return t; }
  function draw(){
    var s = segs[si]; if (!s) return; var into = el - startOf(si), left = s.d - into;
    $('pm-n').textContent = (s.k === 'tense' || s.k === 'rel') ? Math.max(1, Math.ceil(left)) : '';
    $('pm-left').textContent = mmss(total - el); $('pm-bar').style.width = (Math.min(1, el / total) * 100).toFixed(2) + '%';
  }
  function frame(now){
    if (!running) return;
    var dt = Math.min(.25, (now - last) / 1000); last = now; el += dt;
    while (si < segs.length && el >= startOf(si) + segs[si].d) { if (si + 1 >= segs.length) { finish(); return; } enter(si + 1); }
    draw(); raf = requestAnimationFrame(frame);
  }
  function run(){ running = true; last = performance.now(); cancelAnimationFrame(raf); raf = requestAnimationFrame(frame); $('pm-go').textContent = S.pause; wake(true); }
  function pause(){ running = false; cancelAnimationFrame(raf); hush(); $('pm-go').textContent = S.resume; $('pm-ph').textContent = S.paused; wake(false); }
  function finish(){ running = false; cancelAnimationFrame(raf); state = 'done'; el = total; $('pm-name').textContent = S.done; $('pm-cue').textContent = S.dones; $('pm-ph').textContent = ''; draw(); $('pm-n').textContent = '✓'; $('pm-go').textContent = S.again; wake(false); beep(523, .4, .07); setTimeout(function(){ beep(659, .6, .07); }, 300); }
  function reset(){ running = false; cancelAnimationFrame(raf); hush(); state = 'idle'; el = 0; si = -1; build();
    $('pm-ph').textContent = ''; $('pm-name').textContent = S.ready; $('pm-cue').textContent = S.readys; $('pm-n').textContent = ''; $('pm-step').textContent = '\\u00a0';
    $('pm-left').textContent = mmss(total); $('pm-bar').style.width = '0%'; $('pm-go').textContent = S.start; paint(-1, 'idle'); RG.forEach(function(e){ e.classList.remove('rel'); }); wake(false); }
  $('pm-go').addEventListener('click', function(){
    if (state === 'idle' || state === 'done') { reset(); state = 'run'; enter(0); run(); }
    else if (running) pause(); else { enter(si); run(); }
  });
  $('pm-reset').addEventListener('click', reset);
  function seg(id, fn){ $(id).addEventListener('click', function(e){ var b = e.target.closest('button'); if (!b) return;
    this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); fn(b.getAttribute('data-v')); reset(); }); }
  seg('pm-ver', function(v){ ver = v; }); seg('pm-pace', function(v){ rel = +v; });
  document.addEventListener('visibilitychange', function(){ if (!document.hidden && running) wake(true); });
  reset();
})();
</script>
'''

page("kas-gevsetme.html", "Kas Gevşetme: Sesli Rehber",
     "Aşamalı kas gevşetme nedir, stres, kaygı ve uykusuzlukta işe yarar mı? 46 çalışmanın bulguları, 18 bölgelik tam ve 7 bölgelik kısa sürüm, sesli zamanlayıcıyla adım adım.",
     "kas-gevsetme.html", PMR_CSS, PMR_BODY, PMR_JS,
     seo_title="Aşamalı Kas Gevşetme: Sesli Rehberle 6 Dakika | İhsan Eren",
     about={"@type": "Thing", "name": "Aşamalı kas gevşetme"}, faq_items=PMR_FAQ)

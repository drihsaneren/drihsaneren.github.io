# -*- coding: utf-8 -*-
# Yeni rehber (73): Diş sıkma ve gıcırdatma (bruksizm). self15_part.py'den sonra exec edilir. Video yok.
# Kullanıcı isteği (7–8 Kasım 2026): ders niteliğinde, kapsamlı; Cihan Hoca (Prof. Dr. Cihan Aksoy) tanıtımı; dört alan (diş, eklem, boyun, beyin);
# çene sesi, dilde diş izleri, kuvvet, ruhsal etkenler, plak, ilaçlar (etken madde adıyla, marka adı yok), botulinum toksini çizimi, tarihçe, klinik gözlem kutusu.
# Kaynaklar ve notlar: denetim/notlar_bruksizm.md (7–8 Kasım 2026'da okundu).

_ex2("br_breath", "plb", "Gevşeme nefesi", "Rahatça oturun; omuzlarınızı ve çenenizi gevşetin, dişleriniz birbirine değmesin. Burnunuzdan sakin bir nefes alın ve yavaşça verin. Nefes verirken yüzünüzün iki yanındaki kasların ve şakaklarınızın yumuşadığını hissedin.", "5–10 nefes, günde birkaç kez")

# Dört alan çizimi (diş, eklem, boyun, beyin) — numaralar dilden bağımsız, açıklamalar HTML'de
_BR_HEAD = ('<path d="M84 226 L80 180 C60 160 50 130 54 100 C58 58 92 30 134 30 C174 30 198 58 198 90 L202 104 L214 124 L203 131 L206 141 L202 149 L204 157 L196 168 C184 172 166 172 156 176 L160 226" '
            'fill="none" stroke="#2A6F6B" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>'
            '<ellipse cx="122" cy="114" rx="8" ry="13" fill="none" stroke="#2A6F6B" stroke-width="2.5"/>'
            '<path d="M176 98 Q182 94 188 98" fill="none" stroke="#2A6F6B" stroke-width="2.5" stroke-linecap="round"/>'
            '<path d="M130 106 Q152 100 178 108" fill="none" stroke="#8FA8A2" stroke-width="2.5" stroke-linecap="round"/>'
            '<path d="M130 124 L137 160 Q140 166 150 166 L194 166" fill="none" stroke="#8FA8A2" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
            '<path d="M186 148 H203" stroke="#8FA8A2" stroke-width="2.5" stroke-linecap="round"/>')

def _br_mark(x, y, n, col, delay):
    return (f'<circle cx="{x}" cy="{y}" r="10" fill="{col}"><animate attributeName="r" values="10;12;10" dur="2.4s" begin="{delay}s" repeatCount="indefinite"/></circle>'
            f'<text x="{x}" y="{y + 4.5}" text-anchor="middle" font-size="13" font-weight="700" fill="#FFFFFF" font-family="sans-serif">{n}</text>')

BR_FIG_AREAS = ('<figure class="br-fig"><svg viewBox="0 0 240 230" role="img" aria-labelledby="br-fa-t"><title id="br-fa-t">Diş sıkmanın etkilediği dört alan: beyin, eklem, diş ve boyun</title>'
                + _BR_HEAD +
                '<path d="M146 170 C138 186 128 194 122 198" fill="none" stroke="#C8963E" stroke-width="2.5" stroke-dasharray="4 4" stroke-linecap="round"/>'
                '<path d="M112 76 C120 92 132 104 138 112" fill="none" stroke="#C8963E" stroke-width="2.5" stroke-dasharray="4 4" stroke-linecap="round"/>'
                + _br_mark(108, 66, 1, "#2A6F6B", 0) + _br_mark(140, 118, 2, "#C8963E", 0.6) + _br_mark(190, 148, 3, "#2A6F6B", 1.2) + _br_mark(120, 202, 4, "#C8963E", 1.8) +
                '</svg></figure>')

# Botulinum toksini uygulama bölgeleri — şematik
def _br_dot(x, y, d):
    return (f'<circle cx="{x}" cy="{y}" r="3.6" fill="#7A2E2E"><animate attributeName="opacity" values="1;.3;1" dur="2s" begin="{d}s" repeatCount="indefinite"/></circle>')

BR_FIG_BOTOX = ('<figure class="br-fig"><svg viewBox="0 0 240 230" role="img" aria-labelledby="br-fb-t"><title id="br-fb-t">Şakak kası ve çiğneme kası: botulinum toksini uygulamasında kullanılan kaslar (şematik)</title>'
                '<path d="M120 102 C108 74 126 46 160 46 C186 48 194 70 186 92 C170 100 146 104 126 106 Z" fill="#C8963E" fill-opacity=".28" stroke="#C8963E" stroke-width="2" stroke-linejoin="round"/>'
                '<path d="M138 110 L176 112 L180 162 L146 164 Z" fill="#2A6F6B" fill-opacity=".28" stroke="#2A6F6B" stroke-width="2" stroke-linejoin="round"/>'
                + _BR_HEAD +
                _br_dot(140, 76, 0) + _br_dot(160, 64, .3) + _br_dot(176, 82, .6) + _br_dot(152, 126, .9) + _br_dot(166, 134, 1.2) + _br_dot(156, 150, 1.5) +
                '</svg></figure>')

BR_FAQ = [
 ("Plak takarsam diş sıkmam geçer mi?", "Genellikle geçmez. Beş çalışmayı inceleyen Cochrane derlemesi, plağın uyku bruksizmini azalttığını gösterecek yeterli kanıt bulamadı; plak daha çok dişleri aşınmaya karşı korur. Plak sıkmayı durdurmadığı için çiğneme kaslarındaki, çene eklemindeki ve boyundaki yük sürebilir. Bu yüzden plak tek başına değil; stres yönetimi, alışkanlıkları değiştirme ve kas çalışmasıyla birlikte düşünülür. Plağın türüne ve ne zaman takılacağına diş hekiminiz karar verir."),
 ("Dilimin kenarında diş izleri var; diş sıktığım anlamına mı gelir?", "Olabilir. Türkiye'de 98 hastanın incelendiği 2026 tarihli bir çalışmada, uyku testiyle doğrulanmış bruksizmi olanların %65,3'ünde dil kenarında diş izleri vardı; yalnızca kendisi diş sıktığını söyleyenlerde bu oran %34,7 idi. Yanağın iç yüzünde dişlerin hizasında beyaz bir çizgi de sırasıyla %75,5 ve %42,9 oranında görüldü. Bu işaretler tek başına tanı koydurmaz; diş hekimi muayenesiyle birlikte değerlendirilir."),
 ("Çenemden klik sesi geliyor; diş sıkmayla ilgisi var mı?", "Klik sesi, çene ekleminin içindeki diskin ağız açılıp kapanırken yer değiştirmesiyle ilgili olabilir. Ağrısız klik sesi sık görülür ve tek başına tedavi gerektirmez. Sesle birlikte ağrı, ağız açmada kısıtlılık ya da takılma varsa değerlendirme yapılmalıdır. Diş sıkma, çiğneme kası ve çene eklemi ağrısı için bir risk etkeni olabilir; ayrıntılar için <a href=\"cene-eklemi.html\">çene eklemi rahatsızlıkları</a> rehberine bakabilirsiniz."),
 ("Stres diş sıkmaya neden olur mu?", "Stres ve kaygı en sık sayılan etkenler arasında. Altı çalışmayı inceleyen bir sistematik derlemede, stresi olanlarda bruksizm olasılığı yaklaşık iki kat (OR 2,07) daha yüksekti; ancak kanıtın kesinliği düşüktü. Cihan Hoca'nın da yazarları arasında olduğu ve çene eklemi polikliniğine başvuran 273 hastanın incelendiği çalışmada, kadın olmak, sosyal desteğin yetersiz olması ve kas kaynaklı yüz ağrısı, kaygı ya da depresyon olasılığını artırıyordu; yazarlar tedavi planlanırken kaygı ve depresyonun da göz önünde bulundurulmasını önerdi."),
 ("Botoks diş sıkmayı tedavi eder mi?", "Botulinum toksini, yalnızca hekimlerin uyguladığı bir iğnedir ve diş sıkmada çiğneme kasına ve şakak kasına yapılır. 14 sistematik derlemeyi inceleyen 2025 tarihli bir genel değerlendirmede, derlemelerin çoğu ağrının, diş sıkma olaylarının sıklığının ve en büyük ısırma kuvvetinin azaldığını bildirdi. Ancak derlemelerin hepsinin güvenilirliği düşük ya da çok düşüktü ve kesin bir sonuç çıkarılamadı. Uygun olup olmadığına hekiminiz karar verir."),
 ("Diş sıkma için ilaç kullanmam gerekir mi?", "Çoğu kişide gerekmez. Uyku bruksizminde ilaçları inceleyen Cochrane derlemesi, yedi küçük çalışmada ilaçların etkili olduğunu gösterecek yeterli kanıt bulamadı; bazı ilaçlarda yan etkiler görüldü. Sinir ağrısında kullanılan bir ilaç olan gabapentin, 20 kişilik küçük bir çalışmada gece çiğneme kası etkinliğini plak kadar azalttı. Benzer etkili pregabalinle ilgili yayımlanmış veri ise kaygı bozukluğu olan tek bir hastanın olgu sunumuyla sınırlı. Bu ilaçlar yalnızca uzman hekim reçetesiyle ve kontrolle kullanılır; kendi başınıza kullanmayın. Hangisinin uygun olduğunu hekiminize sorun."),
 ("Çocuğum gece diş gıcırdatıyor; ne yapmalıyım?", "Çocuklarda diş gıcırdatma sıktır; çoğunlukla süt dişleri ya da kalıcı dişler çıkarken başlar ve kalıcı dişler tamamen çıktıktan sonra genellikle kendiliğinden durur. Dişlerde aşınma, ağrı ya da uyku sorunu fark ederseniz çocuğunuzu bir diş hekimine götürün."),
 ("Diş sıkma tamamen geçer mi?", "Şu an dünyada diş sıkmayı kesin olarak ortadan kaldırdığı gösterilmiş bir tedavi yok; plak, biyolojik geri bildirim, ilaçlar ve botulinum toksiniyle ilgili derlemelerin hiçbiri kesin bir etkinlik gösteremedi. Bruksizm esas olarak beyin tarafından düzenlenen bir davranış olduğu için amaç; dişleri, eklemi ve kasları korumak, tetikleyicileri azaltmak ve yakınmaları hafifletmektir. Bu da çoğu zaman birden fazla branşın birlikte çalışmasını gerektirir."),
]

BR_SRC = [
 "Lobbezoo F, Ahlberg J, Raphael KG, et al. " + ext("https://pure.uva.nl/ws/files/31008698/Lobbezoo_et_al_2018_Journal_of_Oral_Rehabilitation.pdf", "International consensus on the assessment of bruxism: report of a work in progress") + ". J Oral Rehabil. 2018;45(11):837-844.",
 "Zieliński G, Pająk A, Wójcicki M. " + ext("https://mdpi.com/2077-0383/13/14/4259", "Global prevalence of sleep bruxism and awake bruxism in pediatric and adult populations: a systematic review and meta-analysis") + ". J Clin Med. 2024;13(14):4259.",
 "Nishigawa K, Bando E, Nakano M. " + ext("https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/82533805", "Quantitative study of bite force during sleep associated bruxism") + ". J Oral Rehabil. 2001;28(5):485-491.",
 "Guinness World Records. " + ext("https://www.guinnessworldrecords.com/world-records/75273-strongest-human-bite", "Strongest human bite") + ".",
 "Diraçoğlu D, Alptekin K, Çifter ED, Güçlü B, Karan A, Aksoy C. " + ext("https://research.bau.edu.tr/en/publications/relationship-between-maximal-bite-force-and-tooth-wear-in-bruxist-2/", "Relationship between maximal bite force and tooth wear in bruxist and non-bruxist individuals") + ". Arch Oral Biol. 2011;56(12):1569-1575.",
 "Diraçoğlu D, Yıldırım NK, Saral İ, Özkan M, Karan A, Özkan S, Aksoy C. " + ext("https://content.iospress.com/articles/journal-of-back-and-musculoskeletal-rehabilitation/bmr644", "Temporomandibular dysfunction and risk factors for anxiety and depression") + ". J Back Musculoskelet Rehabil. 2016;29(3):487-491.",
 "Lobbezoo F, Naeije M. " + ext("https://read.qxmd.com/read/11874505/bruxism-is-mainly-regulated-centrally-not-peripherally", "Bruxism is mainly regulated centrally, not peripherally") + ". J Oral Rehabil. 2001.",
 "Kato T, Rompré P, Montplaisir JY, Sessle BJ, Lavigne GJ. " + ext("https://pubmed.ncbi.nlm.nih.gov/11706956/", "Sleep bruxism: an oromotor activity secondary to micro-arousal") + ". J Dent Res. 2001;80(10):1940-1944.",
 "Chemelo VS, et al. " + ext("https://www.frontiersin.org/articles/10.3389/fneur.2020.590779", "Is there association between stress and bruxism? A systematic review and meta-analysis") + ". Front Neurol. 2020;11:590779.",
 "Koca CG, Yıldırım B, Tunç S, Ongun İ, Sadry S. " + ext("https://dergipark.org.tr/en/download/article-file/6249057", "Intraoral findings, soft palate dimensions, and body mass index in PSG-confirmed versus self-reported bruxism: a comparative study") + ". Cumhuriyet Dent J. 2026;29(3):552-560.",
 "nidirect (NHS içeriği). " + ext("https://www.nidirect.gov.uk/conditions/teeth-grinding", "Teeth grinding (bruxism)") + ".",
 "Macedo CR, Silva AB, Machado MAC, Saconato H, Prado GF. " + ext("https://www.cochrane.org/fr/evidence/CD005514_occlusal-splints-treating-sleep-bruxism-tooth-grinding", "Occlusal splints for treating sleep bruxism (tooth grinding)") + ". Cochrane Database Syst Rev. 2007;(4):CD005514.",
 ext("https://cochranelibrary.com/cdsr/doi/10.1002/14651858.CD005578.pub2", "Pharmacotherapy for sleep bruxism") + ". Cochrane Database Syst Rev. CD005578.",
 "Cerón L, et al. " + ext("https://dmp.umw.edu.pl/pdf/2023/60/2/335.pdf", "Therapies for sleep bruxism in dentistry: a critical evaluation of systematic reviews") + ". Dent Med Probl. 2023;60(2):335-344.",
 "Coelho MS, de Oliveira JMD, Polmann H, Pauletto P, Stefani CM, Maciel LCDL, De Luca Canto G. " + ext("https://library.kab.ac.ug/Record/doaj-art-b1abe2df885144ff93dd46bfee1a2751/Description", "Botulinum toxin for bruxism: an overview") + ". Toxins. 2025.",
 "Madani AS ve ark. 2012; özet: " + ext("https://cats.uthscsa.edu/published_cats_friendly.php?id=2762", "Gabapentin is as effective as an occlusal appliance in controlling nighttime masticatory EMG activity") + " (UT Health San Antonio).",
 "Tecco JM, Tecco S. " + ext("https://hrcak.srce.hr/en/262356", "Awake bruxism treated with pregabaline in a patient with generalized anxiety disorder") + ". Psychiatr Danub. 2020;32(Suppl 1):33-35.",
 "Amorim CSM, Espirito Santo AS, Sommer M, Marques AP. " + ext("https://search.pedro.org.au/search-results/record-detail/54184", "Effect of physical therapy in bruxism treatment: a systematic review") + ". J Manipulative Physiol Ther. 2018;41(5):389-404.",
 "Headache Classification Committee of the International Headache Society. " + ext("https://ichd-3.org/11-headache-or-facial-pain-attributed-to-disorder-of-the-cranium-neck-eyes-ears-nose-sinuses-teeth-mouth-or-other-facial-or-cervical-structure/11-7-headache-attributed-to-temporomandibular-disorder-tmd/", "ICHD-3, 11.7 Headache attributed to temporomandibular disorder (TMD)") + ".",
 "Réus JC, Polmann H, Mendes Souza BD, et al. " + ext("https://repositorio.unesp.br/entities/publication/a1c9007f-994a-416c-a323-fe9c7c7e8316/full", "Association between primary headaches and temporomandibular disorders: a systematic review and meta-analysis") + ". J Am Dent Assoc. 2022;153(2):120-.",
 "Yakkaphan P, Renton T, Tan H, et al. " + ext("https://kclpure.kcl.ac.uk/portal/en/publications/temporomandibular-disorders-and-fibromyalgia-prevalence-a-systema/", "Temporomandibular disorders and fibromyalgia prevalence: a systematic review and meta-analysis") + ". J Oral Facial Pain Headache. 2023;37(3):177-193.",
 "Bizzarri P, Giusti A, Pernici M, et al. " + ext("https://research.birmingham.ac.uk/en/publications/temporomandibular-disorders-and-orofacial-outcomes-in-subjects-wi/", "Temporomandibular disorders and orofacial outcomes in subjects with neck pain and/or cervicogenic headache: a systematic review with meta-analysis") + ". J Clin Med. 2026;15(1):266.",
 "Ciuffolo F, Manzoli L, Ferritto AL, Tecco S, D'Attilio M, Festa F. " + ext("https://cris.unibo.it/handle/11585/918009", "Surface electromyographic response of the neck muscles to maximal voluntary clenching of the teeth") + ". J Oral Rehabil. 2005;32:79-84.",
 "NHS Lothian. " + ext("https://policyonline.nhslothian.scot/wp-content/uploads/2024/07/Physio-Temporomandibular-Joint-Disorders.pdf", "Physiotherapy: temporomandibular joint disorders") + ". Version 2.0, June 2024.",
 "University Hospitals of Leicester. " + ext("https://www.uhleicester.nhs.uk/wp-content/uploads/2025/06/436_122022-Managing-jaw-joint-disorders.pdf", "Managing jaw joint disorders") + ". Leaflet 436.",
 "Dentalcare (Procter & Gamble). " + ext("https://dentalcare.com/en-us/ce-courses/ce485/history-of-bruxism", "Bruxism: history") + ".",
]

BR_TL = [
 ("Eski metinler", "Diş gıcırdatma, Mezmurlar'da da geçen ve bilinen en eski anılardan biri olarak aktarılan bir davranış."),
 ("20. yüzyıl başı", "Viyanalı diş hekimi Karolyi, diş sıkma ve gıcırdatmayı \"travmatik nevralji\" olarak tanımladı."),
 ("1907", "Marie ve Pietkiewicz, diş gıcırdatma için Fransızca bir terim önerdi."),
 ("1931", "Frohman, Yunanca \"dişleri gıcırdatmak\" anlamındaki sözcüklerden türeyen \"bruksizm\" terimini kullandı."),
 ("1960'lar–2007", "Dişlerin kapanışındaki (oklüzyon) bozuklukların ana neden olduğu düşüncesi öne çıktı; araştırma ve tedaviler kapanış düzeltmelerine ve plaklara odaklandı."),
 ("2001", "Uykuda diş sıkmadan önce beyin dalgalarında bir uyanma artışı ve kalp hızında hızlanma olduğu gösterildi (J Dent Res). Aynı yıl bruksizmin esas olarak beyin tarafından düzenlendiği, kapanışın ise küçük bir rol oynadığı yazıldı."),
 ("2007", "Cochrane derlemesi: plağın uyku bruksizmini azalttığına dair yeterli kanıt yok; plak dişleri aşınmaya karşı koruyabilir."),
 ("2011", "Cihan Hoca'nın da yazarları arasında olduğu çalışma (Arch Oral Biol): diş sıkanlarda en büyük ısırma kuvveti ve diş aşınması daha yüksekti ve ikisi birbiriyle güçlü biçimde ilişkiliydi; araştırmacılar bunun bu ilişkiyi gösteren ilk çalışma olduğunu yazdı."),
 ("2013", "Uluslararası uzmanlar bruksizmin ilk ortak tanımını yayımladı."),
 ("2018", "Uluslararası uzlaşı: uyku ve uyanıklık bruksizmi için iki ayrı tanım; sağlıklı kişilerde bir hastalık değil, sonuçları olabilecek bir davranış."),
 ("2024", "176 popülasyonu birleştiren meta-analiz (J Clin Med): dünyada uyku bruksizmi yaklaşık %21, uyanıklık bruksizmi %23."),
]

BR_OBS = '''Pek çok kişi yorgun uyanma, sabah baş ağrısı, boyun ve omuz ağrısı gibi yakınmalar için farklı farklı tedavilere yöneliyor; klinikte bu yakınmaların altından zaman zaman diş sıkmanın çıkabildiğini görüyorum. İlerlemiş ve geçmeyen olgularda, boyundan kola yayılan ve sinir kökü basısını andıran ama gerçek bir kök basısı olmayan ağrılarla da karşılaşıyorum. Sinir kökü basısının ne olduğunu <a href="boyun-fitigi.html">boyun fıtığı</a> rehberinde okuyabilirsiniz.'''

BR_CSS = '''.br-fig{margin:18px auto 8px;max-width:340px;background:#F7F2E7;border-radius:18px;padding:12px}.br-fig svg{display:block;width:100%;height:auto}
.br-leg{list-style:none;padding:0;margin:8px auto 18px;max-width:560px;display:grid;gap:8px}
.br-leg li{display:flex;gap:10px;align-items:flex-start;line-height:1.5}
.br-num{flex:0 0 26px;height:26px;border-radius:50%;color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center;font-size:14px}
.br-sw{flex:0 0 16px;height:16px;border-radius:4px;margin-top:4px}'''

BR_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Hastalık rehberi</p>
    <h1>Diş sıkma ve gıcırdatma (bruksizm)</h1>
    <p class="lede">Diş sıkma ve gıcırdatma (bruksizm), çiğneme kaslarının uykuda ya da gün içinde gereğinden fazla çalışmasıdır. Dünyada yaklaşık her dört-beş kişiden birinde görülüyor ve çoğu kişi bunu fark etmiyor. Etkileri yalnızca dişlerle sınırlı değil: çene eklemi, boyun kasları, uyku ve baş ağrısı da etkilenebilir. Bu rehberde bruksizmi bir ders gibi baştan sona anlatıyoruz.</p>
    <p class="meta">Son güncelleme: 8 Kasım 2026</p>
  </div>
</header>
<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>%23</b><span>Dünyada uyanıkken diş sıkan ya da dişlerini birbirine bastıranların tahmini oranı; uykuda %21 (2024 meta-analizi)</span></div>
        <div class="stat"><b>42 kg</b><span>Gece diş sıkmasında ölçülen en yüksek kuvvetin kişi başına ortalaması (kilogram-kuvvet); bazı kişilerde 81 kg</span></div>
        <div class="stat"><b>%77</b><span>Fibromiyaljisi olanlarda çene eklemi sorunu görülme oranı</span></div>
        <div class="stat"><b>4–5 kat</b><span>Migreni olanlarda çene eklemi sorunu görülme olasılığı (2022 meta-analizi)</span></div>
      </div>
      {g_toc([("nedir", "Bruksizm nedir?"), ("kuvvet", "Dişlere binen kuvvet"), ("etkiler", "Dört alanda etkiler"), ("karisabilir", "Başka bir şey sanılabilir"), ("nedenler", "Nedenler ve ruhsal etkenler"), ("plak", "Plak"), ("tedavi", "Çok yönlü tedavi"), ("evde", "Evde neler yapılabilir?"), ("egzersizler", "Egzersizler"), ("cocuklar", "Çocuklarda"), ("tarihce", "Geçmişten bugüne"), ("sss", "Sık sorulan sorular"), ("uyari", "Uyarı işaretleri")])}
      <div class="callout">
        <p><strong>Bu rehber hakkında.</strong> Bu rehberdeki yaklaşımı yazarımız İhsan Eren, Türkiye'de çene eklemi bozuklukları ve diş sıkma alanında 2005'ten bu yana uluslararası dergilerde yayımlanan çalışmalarıyla bu alanın öncülerinden olan Fiziksel Tıp ve Rehabilitasyon uzmanı Prof. Dr. Cihan Aksoy'un (Cihan Hoca) yanında öğrendi. Cihan Hoca, diş sıkmada diş hekimliği, psikiyatri ve diğer branşların birlikte çalışmasını ve hangi durumda hangi tedavinin tıbben uygun olduğunu ortaya koyan bir yaklaşım geliştirdi. Bu sayfada Cihan Hoca'nın da yazarları arasında olduğu iki çalışmaya yer veriyoruz.</p>
      </div>
    </div>
  </section>

  <section id="nedir">
    <div class="wrap">
      <h2>Bruksizm nedir?</h2>
      <p class="soft">2018'deki uluslararası uzlaşıya göre bruksizm, çiğneme kaslarının tekrarlayan ya da süren etkinliğidir ve iki ayrı biçimi vardır. Kişi dişlerini gıcırdatmadan, yalnızca sıkarak ya da alt çenesini iterek de bruksizm yaşayabilir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Uyku bruksizmi</h3><dl><dt>Uykuda</dt><dd>Uyku sırasında çiğneme kaslarının ritmik ya da ritmik olmayan etkinliği: diş gıcırdatma ve sıkma. Çoğu kişi fark etmez; genellikle birlikte uyuyan kişi gıcırtıyı duyar.</dd></dl></div>
        <div class="kind"><h3>Uyanıklık bruksizmi</h3><dl><dt>Gün içinde</dt><dd>Uyanıkken dişlerin tekrarlayan ya da süren biçimde birbirine değmesi, sıkılması ya da alt çenenin itilmesi. Çoğunlukla konsantrasyon, stres ya da yoğun iş sırasında, farkında olmadan olur.</dd></dl></div>
      </div>
      <h3 class="g-h3">Hastalık mı, davranış mı?</h3>
      <p class="soft">Uzlaşıya göre bruksizm, sağlıklı kişilerde tek başına bir hastalık değil, bir davranıştır; ancak diş aşınması, çiğneme kası ve çene eklemi ağrısı gibi sonuçlar için risk etkeni olabilir. Bruksizmin varlığı üç düzeyde değerlendirilir:</p>
      <ul class="tx">
        <li><b>Olası</b><span>Yalnızca kişinin kendi bildirimine dayanır (\"dişlerimi sıkıyorum\").</span></li>
        <li><b>Muhtemel</b><span>Muayene bulguları da vardır (diş aşınması, dilde diş izleri gibi).</span></li>
        <li><b>Kesin</b><span>Uyku testi (polisomnografi) gibi bir cihazla ölçülerek doğrulanır.</span></li>
      </ul>
      <h3 class="g-h3">Ne kadar yaygın?</h3>
      <p class="soft">176 popülasyonu birleştiren 2024 tarihli meta-analize göre dünyada bruksizm yaklaşık %22 oranında görülüyor: uyku bruksizmi %21, uyanıklık bruksizmi %23. Yani yaklaşık her dört kişiden biri gün içinde dişlerini sıkıyor olabilir. Uyanıklık bruksizmi kadınlarda erkeklere göre yaklaşık iki kat daha sık bildirildi (%17'ye karşı %8); kıtalar arasında anlamlı bir fark bulunmadı.</p>
    </div>
  </section>

  <section id="kuvvet">
    <div class="wrap">
      <h2>Dişlere ne kadar kuvvet biner?</h2>
      <p class="soft">Normalde dişler gün boyu birbirine değmez: Dinlenme sırasında dudaklar kapalı, dişler hafifçe ayrık, dil damakta durur. Diş sıkmada ise kaslar dişleri saatlerce birbirine bastırabilir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Gece diş sıkması</h3><dl><dt>J Oral Rehabil, 2001</dt><dd>Uykuda ölçülen en yüksek kuvvet kişi başına ortalama 42 kilogram-kuvvet oldu, bazı kişilerde 81'e ulaştı. Bazı kişilerde gece kuvveti, gündüz bilerek yapılan en güçlü ısırmayı (ortalama 79 kilogram-kuvvet) aştı.</dd></dl></div>
        <div class="kind"><h3>Rekor ısırma</h3><dl><dt>Guinness Dünya Rekorları</dt><dd>Kayıtlara geçen en güçlü insan ısırması 442 kilogram, yani yarım tona yakın; 1986'da bir diş hekimliği fakültesinde ölçüldü ve yaklaşık 2 saniye sürdü.</dd></dl></div>
        <div class="kind"><h3>Kuvvet ve aşınma</h3><dl><dt>Arch Oral Biol, 2011</dt><dd>Cihan Hoca'nın da yazarları arasında olduğu çalışmada, diş sıkanlarda en büyük ısırma kuvveti ve diş aşınması daha yüksekti; ikisi arasındaki ilişki güçlüydü. Araştırmacılar bunun, bu ilişkiyi gösteren ilk çalışma olduğunu yazdı.</dd></dl></div>
      </div>
    </div>
  </section>

  <section id="etkiler">
    <div class="wrap">
      <p class="eyebrow">Halk için özet</p>
      <h2>Dört alanda etkiler: diş, eklem, boyun, beyin</h2>
      <p class="soft">Diş sıkmayı yalnızca bir diş sorunu gibi düşünmek, tablonun yarısını görmek olur. Kesikli çizgiler, etkinin çeneden eklem ve boyun kaslarına doğru bir zincir gibi yayılabileceğini gösteriyor.</p>
      {BR_FIG_AREAS}
      <ul class="br-leg">
        <li><span class="br-num" style="background:#2A6F6B">1</span><span><b>Beyin:</b> Bruksizmi başlatan ve düzenleyen merkez; uyku, stres ve baş ağrısıyla bağlantılı.</span></li>
        <li><span class="br-num" style="background:#C8963E">2</span><span><b>Eklem:</b> Kulağın hemen önündeki çene eklemi ve çevresindeki çiğneme kasları.</span></li>
        <li><span class="br-num" style="background:#2A6F6B">3</span><span><b>Diş:</b> Aşınma, kırık ve çatlaklar; dil ve yanakta izler.</span></li>
        <li><span class="br-num" style="background:#C8963E">4</span><span><b>Boyun:</b> Diş sıkarken birlikte kasılan boyun kasları.</span></li>
      </ul>
      <h3 class="g-h3">1. Beyin: işin başladığı yer</h3>
      <p class="soft">Bruksizm bugün esas olarak beyin tarafından düzenlenen bir davranış olarak kabul ediliyor; dişlerin kapanışı ve çenenin yapısı ise küçük bir rol oynuyor. Uyku bruksizmi olan hastalarla yapılan bir çalışmada, diş sıkma olaylarının %79'unda kas etkinliğinden yaklaşık 4 saniye önce beyin dalgalarında bir uyanma artışı, hemen öncesinde de kalp hızında hızlanma görüldü. Yani uykuda diş sıkma, çoğu zaman uykunun kısa süreli hafiflemesiyle (mikro uyanma) birlikte ortaya çıkıyor. Bu yüzden uykunun bölünmesi, sabah yorgun uyanma ve sabah baş ağrısı sık bildirilen yakınmalar arasında. Horlama ve uykuda nefes durması (uyku apnesi) de bruksizmle ilişkili bulunuyor.</p>
      <h3 class="g-h3">2. Eklem: çene eklemi ve çiğneme kasları</h3>
      <p class="soft">Uzun süre sıkılan çiğneme kasları yorulur ve ağrır; çene ekleminde ağrı, ağız açmada kısıtlılık ve klik sesi görülebilir. Uluslararası baş ağrısı sınıflamasına göre çene eklemi sorunları, diş ağrısından sonra yüz ağrısının en sık nedenidir. Ağrısız klik sesi sık görülür ve tek başına tedavi gerektirmez; ağrı, kilitlenme ya da ağız açmada kısıtlılık varsa değerlendirme gerekir. Ayrıntılar için <a href="cene-eklemi.html">çene eklemi rahatsızlıkları</a> rehberine bakabilirsiniz.</p>
      <h3 class="g-h3">3. Diş: aşınma, kırık ve ağız içindeki izler</h3>
      <p class="soft">Diş sıkma ve gıcırdatma dişlerde aşınmaya, sıcak-soğuk hassasiyetine, dolgu ve diş kırıklarına, dişlerde çatlaklara ve protez sorunlarına yol açabilir. Ağız içinde de ipuçları vardır: Türkiye'de 98 hastanın incelendiği 2026 tarihli bir çalışmada, uyku testiyle doğrulanmış bruksizmi olanların %65,3'ünde dil kenarında diş izleri, %75,5'inde yanağın iç yüzünde dişlerin hizasında beyaz bir çizgi vardı. Diş hekimi dişlerdeki aşınmayı ve kapanışı (oklüzyon) inceler; ancak kapanış bugün bruksizmin ana nedeni olarak görülmüyor.</p>
      <h3 class="g-h3">4. Boyun: zincirin devamı</h3>
      <p class="soft">Diş sıkarken yalnızca çene kasları çalışmaz: Sağlıklı kişilerde yapılan bir kas aktivitesi çalışmasında, en güçlü diş sıkma sırasında ön boyun kaslarının etkinliği belirgin olarak arttı. Boyun ağrısı olanlarda da çene eklemi sorunları daha sık: Dokuz çalışmayı birleştiren 2026 tarihli bir meta-analizde boyun ağrısı olanlarda çene eklemi sorunu görülme olasılığı yaklaşık 3,6 kat yüksekti (kanıtın kesinliği çok düşük).</p>
      {OBS(BR_OBS)}
    </div>
  </section>

  <section id="karisabilir">
    <div class="wrap">
      <h2>Migren, fibromiyalji ya da boyun ağrısı sanılabilir</h2>
      <p class="soft">Çene eklemi ve çiğneme kası sorunları, başka tanılarla sık sık birlikte görülür ve belirtileri örtüşebilir. Bu yüzden baş ağrısı, yaygın vücut ağrısı ya da boyun ağrısı nedeniyle değerlendirilen birinde çene eklemi ve çiğneme kasları da muayene edilmelidir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Baş ağrısı ve migren</h3><dl><dt>ICHD-3; JADA, 2022</dt><dd>Sınıflamada ayrı bir başlık var: çene eklemi bozukluğuna bağlı baş ağrısı. Genellikle şakakta olur, çiğneme ve diş sıkmayla artar; gerilim tipi baş ağrısıyla karışabilir. Bir meta-analizde migreni olanlarda çene eklemi sorunu görülme olasılığı 4–5 kat yüksekti (kanıt düşük–çok düşük kesinlikte).</dd></dl></div>
        <div class="kind"><h3>Fibromiyalji</h3><dl><dt>J Oral Facial Pain Headache, 2023</dt><dd>19 çalışmayı birleştiren meta-analizde fibromiyaljisi olanların %76,8'inde çene eklemi sorunu vardı; çene eklemi sorunu olanların yaklaşık üçte birinde (%32,7) de fibromiyalji bulunuyordu.</dd></dl></div>
        <div class="kind"><h3>Boyun ağrısı</h3><dl><dt>J Clin Med, 2026</dt><dd>Boyun ağrısı olanlarda çene eklemi sorunu görülme olasılığı yaklaşık 3,6 kat yüksekti. Yazarlar boyun ve çenenin birlikte değerlendirilmesini öneriyor.</dd></dl></div>
      </div>
      <p class="soft">İlgili rehberler: <a href="bas-agrisi.html">baş ağrısı</a>, <a href="fibromiyalji.html">fibromiyalji</a>, <a href="boyun-agrisi.html">boyun ağrısı</a>.</p>
    </div>
  </section>

  <section id="nedenler">
    <div class="wrap">
      <h2>Neden olur? Ruhsal ve diğer etkenler</h2>
      <p class="soft">Bruksizmin tek bir nedeni yok; birden fazla etken birlikte rol oynuyor. Eskiden dişlerin kapanışındaki bozuklukların ana neden olduğu düşünülürdü; bugün bu etkenlerin küçük bir rol oynadığı, bruksizmin esas olarak beyin tarafından düzenlendiği kabul ediliyor.</p>
      <ul class="tx">
        <li><b>Stres ve kaygı</b><span>En sık sayılan etkenler. Bir sistematik derlemede stresi olanlarda bruksizm olasılığı yaklaşık iki kat yüksekti (kanıtın kesinliği düşük).</span></li>
        <li><b>Uyku sorunları</b><span>Horlama ve uykuda nefes durması (uyku apnesi) bruksizmle ilişkili.</span></li>
        <li><b>İlaçlar</b><span>Bazı ilaçların yan etkisi olarak ortaya çıkabilir; ilacınızı kendi başınıza bırakmayın, hekiminizle konuşun.</span></li>
        <li><b>Alışkanlıklar</b><span>Alkol, sigara, bazı uyuşturucu maddeler ve günde altı fincandan fazla kafeinli içecek riski artırabilir.</span></li>
      </ul>
      <h3 class="g-h3">Ruhsal etkenler: neden önemli?</h3>
      <p class="soft">Cihan Hoca'nın da yazarları arasında olduğu ve çok branşlı bir çene eklemi polikliniğine başvuran 273 hastanın incelendiği çalışmada, kadın olmak, sosyal desteğin yetersiz olması ve kas kaynaklı yüz ağrısı kaygı ya da depresyon olasılığını artırıyordu. Yazarlar, tedavi planlanırken kas ve eklem sorunlarının yanında kaygı ve depresyonun da göz önünde bulundurulmasını önerdi. Stresle başa çıkmak için <a href="stres.html">stresli anlarda ne yapabilirsiniz?</a> sayfasına bakabilirsiniz.</p>
    </div>
  </section>

  <section id="plak">
    <div class="wrap">
      <h2>Plak: dişi korur, sorunu çözmez</h2>
      <p class="soft">Gece plağı (ağız koruyucu), diş hekiminin hazırladığı ve genellikle geceleri takılan bir apareydir. Dişleri birbirinden ayırarak aşınmayı önler ve sıkma hissini azaltabilir. Ancak plak, beyin tarafından başlatılan sıkma davranışını durdurmaz.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Dişler</h3><dl><dt>Cochrane, 2007</dt><dd>Plak dişleri aşınmaya karşı koruyabilir.</dd></dl></div>
        <div class="kind"><h3>Diş sıkma</h3><dl><dt>Cochrane, 2007; Dent Med Probl, 2023</dt><dd>Plağın uyku bruksizmini azalttığına dair yeterli kanıt yok; derlemelerde plaklar kısa vadede etkinlik göstermedi.</dd></dl></div>
        <div class="kind"><h3>Kaslar, eklem ve boyun</h3><dl><dt>Sonuç</dt><dd>Sıkma sürdüğü için çiğneme kaslarındaki, çene eklemindeki ve boyundaki yük devam edebilir. Bu yüzden plak, diğer yaklaşımlarla birlikte kullanılır.</dd></dl></div>
      </div>
      <p class="soft">Diş hekimi dişlerdeki aşınmayı, kırık ve çatlakları ve dişlerin kapanışını (oklüzyon) değerlendirir; plağın gerekip gerekmediğine ve türüne karar verir.</p>
    </div>
  </section>

  <section id="tedavi">
    <div class="wrap">
      <h2>Çok yönlü tedavi: kim ne yapar?</h2>
      <p class="soft">Şu an dünyada diş sıkmayı kesin olarak ortadan kaldırdığı gösterilmiş bir tedavi yok: Plak, biyolojik geri bildirim, ilaç ve botulinum toksiniyle ilgili derlemelerin hiçbiri kesin bir etkinlik gösteremedi. Bu yüzden amaç; dişleri, eklemi ve kasları korumak, tetikleyicileri azaltmak ve yakınmaları hafifletmektir. Bu da çoğu zaman birden fazla branşın birlikte çalışmasını gerektirir.</p>
      <div class="kinds g-cmp">
        <div class="kind"><h3>Diş hekimi</h3><dl><dt>Dişler ve kapanış</dt><dd>Aşınma, kırık ve kapanış değerlendirmesi; gerekirse plak.</dd></dl></div>
        <div class="kind"><h3>Psikiyatri ve psikoloji</h3><dl><dt>Stres ve kaygı</dt><dd>Kaygı, depresyon ya da yoğun stres varsa değerlendirme ve tedavi; bilişsel davranışçı terapi gibi yöntemler.</dd></dl></div>
        <div class="kind"><h3>Uyku değerlendirmesi</h3><dl><dt>Horlama ve nefes durması</dt><dd>Uyku apnesinden şüpheleniliyorsa hekim değerlendirmesi ve gerekirse uyku testi.</dd></dl></div>
        <div class="kind"><h3>Fizyoterapi</h3><dl><dt>Kaslar ve alışkanlıklar</dt><dd>Farkındalık ve alışkanlık değiştirme, gevşeme, çene ve boyun egzersizleri, kas masajı, duruş. 24 çalışmayı inceleyen bir derlemede kas ağrısı ve etkinliği, ağız açıklığı, kaygı ve stres iyileşebildi; ancak kanıtın kalitesi çok düşüktü.</dd></dl></div>
        <div class="kind"><h3>İlaçlar</h3><dl><dt>Yalnızca uzman hekim reçetesiyle</dt><dd>Kanıt sınırlı: Cochrane derlemesi yedi küçük çalışmada yeterli kanıt bulamadı. Gabapentin 20 kişilik bir çalışmada gece kas etkinliğini plak kadar azalttı; pregabalinle ilgili veri tek bir olgu sunumuyla sınırlı. Kendi başınıza kullanmayın; hangisinin uygun olduğunu hekiminize sorun.</dd></dl></div>
        <div class="kind"><h3>Botulinum toksini</h3><dl><dt>Yalnızca hekim uygular</dt><dd>Çiğneme ve şakak kasına yapılır. 14 derlemeyi inceleyen 2025 tarihli değerlendirmede çoğu derleme ağrıda, diş sıkma olaylarında ve ısırma kuvvetinde azalma bildirdi; ancak hepsinin güvenilirliği düşük ya da çok düşüktü ve kesin sonuç çıkarılamadı.</dd></dl></div>
      </div>
      <h3 class="g-h3">Botulinum toksini hangi kaslara yapılır?</h3>
      <p class="soft">Aşağıdaki şematik çizim, diş sıkmada botulinum toksini uygulamasında kullanılan iki kası gösteriyor. Noktalar yalnızca bölgeyi anlatmak içindir; gerçek uygulama noktalarını ve dozu hekim belirler.</p>
      {BR_FIG_BOTOX}
      <ul class="br-leg">
        <li><span class="br-sw" style="background:#C8963E"></span><span><b>Şakak kası (temporalis):</b> Şakakta, kulağın üstünde yelpaze biçiminde uzanır; çeneyi kapatır ve dişleri sıkar.</span></li>
        <li><span class="br-sw" style="background:#2A6F6B"></span><span><b>Çiğneme kası (masseter):</b> Elmacık kemiğinden alt çenenin köşesine uzanır; dişleri sıktığınızda yanağınızda sertleştiğini hissedebilirsiniz.</span></li>
      </ul>
    </div>
  </section>

  <section id="evde">
    <div class="wrap">
      <h2>Evde neler yapılabilir?</h2>
      <ul class="tx">
        <li><b>Dinlenme pozisyonu</b><span>Dudaklar kapalı, dişler hafifçe ayrık, dil damakta. Gün içinde dişlerinizi sıktığınızı fark ettiğinizde bu pozisyona dönün.</span></li>
        <li><b>Hatırlatıcılar</b><span>Konsantrasyon ya da endişe anlarında sıkmayı fark etmek için telefon hatırlatıcısı ya da masanıza küçük bir not koyabilirsiniz; alışkanlığı değiştirmenin ilk adımı fark etmektir.</span></li>
        <li><b>Çeneyi yormayın</b><span>Sakız çiğnemeyin; tırnak, dudak, yanak ya da dil ısırmaktan kaçının; esnerken çenenizi elinizle destekleyin.</span></li>
        <li><b>Ilık ve soğuk</b><span>Ağrılı kaslara 10–15 dakika ılık uygulama ya da 5–10 dakika buz masajı rahatlatabilir.</span></li>
        <li><b>Uyku ve alışkanlıklar</b><span>Düzenli uyku saatleri; özellikle akşamları kafein, alkol ve sigarayı azaltmak. Uyku için öneriler <a href="uyku.html">uyku</a> sayfasında.</span></li>
        <li><b>Gevşeme</b><span>Yavaş nefes, düzenli egzersiz ve farkındalık çalışmaları stresin kaslara yansımasını azaltabilir.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Egzersizler</p>
      <h2>Çene ve boyun için altı egzersiz</h2>
      <p class="soft">Hareketleri ağrısız aralıkta, yavaşça yapın. Ağrı artıyorsa durun ve bir fizyoterapiste ya da hekime danışın.</p>
      {ex_grid(["jaw_rest", "jaw_mass", "jaw_open", "jaw_res", "chin", "br_breath"])}
    </div>
  </section>

  <section id="cocuklar">
    <div class="wrap">
      <h2>Çocuklarda diş gıcırdatma</h2>
      <p class="soft">Çocuklarda diş gıcırdatma sıktır. Çoğunlukla süt dişleri ya da kalıcı dişler çıkarken başlar ve kalıcı dişler tamamen çıktıktan sonra genellikle kendiliğinden durur. Dişlerde aşınma, ağrı ya da uyku sorunu fark ederseniz çocuğunuzu bir diş hekimine götürün.</p>
    </div>
  </section>

  <section id="tarihce">
    <div class="wrap">
      <p class="eyebrow">Geçmişten bugüne</p>
      <h2>Mezmurlar'dan uluslararası uzlaşıya</h2>
      <p class="soft">Diş gıcırdatma çok eski çağlardan beri biliniyor. 20. yüzyılda adı kondu; uzun yıllar dişlerin kapanışı ana neden sayıldı. Son 25 yılda ise bruksizmin esas olarak beyin tarafından düzenlenen bir davranış olduğu anlaşıldı.</p>
      {g_tl(BR_TL)}
    </div>
  </section>

  <section id="sss">
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(BR_FAQ)}
    </div>
  </section>

  <section id="uyari">
    <div class="wrap">
      <h2>Ne zaman başvurmalı?</h2>
      <p class="soft">Aşağıdaki durumlarda bir hekime ya da diş hekimine başvurun; ne kadar acil olduğu her grubun başında belirtilmiştir.</p>
      <p class="soft"><strong>Hemen 112'yi arayın:</strong></p>
      <ul class="dots redflags">
        <li>Göğüs ağrısı, nefes darlığı ya da terlemeyle birlikte çene ağrısı</li>
        <li>Yüzde ani uyuşma ya da güçsüzlük, konuşma bozukluğu</li>
      </ul>
      <p class="soft"><strong>Aynı gün bir hekime ya da diş hekimine:</strong></p>
      <ul class="dots redflags">
        <li>Çenenin kilitlenmesi: ağzın açılmaması ya da kapanmaması</li>
        <li>Yüzde ya da çenede şişlikle birlikte ateş</li>
      </ul>
      <p class="soft"><strong>Birkaç gün içinde bir hekime ya da diş hekimine:</strong></p>
      <ul class="dots redflags">
        <li>Kırık ya da çatlak diş, kırık dolgu</li>
        <li>Horlama ve uykuda nefes durması fark edildiyse</li>
        <li>Birkaç haftada geçmeyen çene, yüz ya da şakak ağrısı</li>
      </ul>
      {CTA_CARD("Diş sıkma ve çene ağrısı", "diş sıkma ve çene ağrısı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(BR_SRC)}
    </div>
  </section>
</main>'''

page("dis-sikma.html", "Diş Sıkma ve Gıcırdatma (Bruksizm)",
     "Diş sıkma ve gıcırdatma (bruksizm) nedir, dişlere ne kadar kuvvet biner, diş, eklem, boyun ve beyin nasıl etkilenir? Migren ve fibromiyaljiyle ilişkisi, ruhsal etkenler, plağın yeri, çok yönlü tedavi, botulinum toksini, tarihçe ve evde altı egzersiz.",
     "dis-sikma.html", NECK_CSS + BR_CSS, BR_BODY, "",
     seo_title="Diş Sıkma ve Gıcırdatma (Bruksizm): Nedenleri, Etkileri ve Tedavi | İhsan Eren",
     condition="Bruksizm", faq_items=BR_FAQ)

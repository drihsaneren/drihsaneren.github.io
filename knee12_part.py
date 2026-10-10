# -*- coding: utf-8 -*-
# "Dizin 12 Sırrı": diz kireçlenmesi için 6 haftalık, davranış bilimiyle tasarlanmış etkileşimli ev programı.
# self3_part.py'den sonra exec edilir. Arayüz metinlerinin tamamı HTML içinde (gizli kaplarda) durur;
# böylece İngilizce sürüm normal çeviri hattından geçer. Betikte görünen Türkçe metin yoktur.
# Veriler yalnızca ziyaretçinin cihazında (localStorage) saklanır.

# ---- program hareketleri: diz kireçlenmesi rehberindeki çizimler ve anlatımlar (knee_part.py) yeniden kullanılır
D12_EX = {
    # anahtar: (ilk evre, ikinci evre)
    "quad": ("Bastırın", "Gevşeyin"),
    "kext": ("Kaldırın", "İndirin"),
    "slr": ("Kaldırın", "İndirin"),
    "sts": ("Kalkın", "Oturun"),
    "abd": ("Kaldırın", "İndirin"),
    "wall": ("Aşağı kayın", "Doğrulun"),
}
_ex2("d12_quad", "quad", "Havluya bastırma", EXT["quad"][1], "1. bölüm: her bacakla 8 tekrar × 2 set, 5 saniye tutarak")
_ex2("d12_kext", "kext", "Oturarak diz düzeltme", EXT["kext"][1], "1. bölüm 10, 2. bölüm 12 tekrar; her bacakla 2 set")
_ex2("d12_slr", "slr", "Düz bacak kaldırma", EXT["slr"][1], "1. bölüm 10, 3. bölüm 12 tekrar; her bacakla 2 set")
_ex2("d12_sts", "sts", "Sandalyeden kalkıp oturma", EXT["sts"][1], "8 tekrardan 12'ye; 3. bölümde 3 saniyede oturarak, 2 set")
_ex2("d12_abd", "abd", "Yan yatarak bacak kaldırma", EXT["abd"][1], "2. bölüm 10, 3. bölüm 12 tekrar; her yana 2 set")
_ex2("d12_wall", "wall", "Duvarda yarım çömelme", EXT["wall"][1], "2. bölüm 8 tekrar 3 saniye, 3. bölüm 10 tekrar 5 saniye tutarak; 2 set")

def _d12_exdata():
    out = []
    for k, (p1, p2) in D12_EX.items():
        nm, how, _dose = EXT["d12_" + k]
        out.append(f'<div data-ex="{k}"><p class="nm">{nm}</p><p class="how">{how}</p>'
                   f'<span class="p1">{p1}</span><span class="p2">{p2}</span>{SV[k]}</div>')
    return "\n          ".join(out)

D12_LOCK = ('<svg class="lk" viewBox="0 0 40 48" aria-hidden="true"><path class="sh" d="M11 21v-6a9 9 0 0 1 18 0v6" fill="none" stroke-width="3.4" stroke-linecap="round"/>'
            '<rect x="6" y="20" width="28" height="23" rx="6"/><circle class="kh" cx="20" cy="30" r="3.2"/><path class="kh" d="M18.6 31.5h2.8l.9 6h-4.6z"/></svg>')

# ---- 12 sır: soru (önceden görünür), cevap (seans sonunda açılır), kısa kaynak
D12_SECRETS = [
 ("Evde egzersiz yapanların çoğu neden bırakır?",
  "<p>Sebep çoğu zaman irade eksikliği değil. Fizyoterapide tedaviye uyumu inceleyen sistematik derlemede, egzersizi sürdürememekle güçlü biçimde ilişkili bulunan etkenler şunlar: egzersiz sırasında artan ağrı, kendine güvenin düşük olması, önünde çok engel görmek, sosyal desteğin az olması, kaygı, depresyon ve çaresizlik hissi.</p><p>Bu program tam da bunlar için kuruldu: ağrı trafik ışığı, küçük ve ölçülebilir adımlar, söz kartı ve sözünüzü paylaşabileceğiniz bir yakınınız.</p>",
  "Jack ve ark., Manual Therapy, 2010"),
 ("Röntgen, ağrınızı neden tam anlatmaz?",
  "<p>Röntgen ile ağrı her zaman aynı hikâyeyi anlatmaz. Çalışmaları derleyen bir incelemede diz ağrısı olanların yalnızca %15 ile %76'sında röntgende kireçlenme görüldü; röntgende kireçlenmesi olanların ise %15 ile %81'inde ağrı vardı.</p><p>Yani filminiz kötü görünse de diziniz güçlenebilir ve ağrınız azalabilir. Egzersizin hedefi filmdeki görüntü değil; ağrınız ve günlük işleriniz.</p>",
  "Bedson ve Croft, BMC Musculoskeletal Disorders, 2008"),
 ("Dizinizin gizli amortisörü nerede?",
  "<p>Uyluğunuzun ön yüzünde: dört başlı uyluk kasında. Diz her adımda bükülüp açılırken yükü bu kas karşılar.</p><p>46.819 kişiyi kapsayan bir meta-analizde bu kası zayıf olanlarda, belirtili diz kireçlenmesi gelişme olasılığı kadınlarda yaklaşık 1,85 kat, erkeklerde 1,43 kat daha yüksek bulundu. Kanıtın kalitesi düşük; yine de bu programdaki hareketlerin çoğu bu kası hedefliyor.</p>",
  "Øiestad ve ark., British Journal of Sports Medicine, 2022"),
 ("Egzersiz sırasındaki ağrı zarar mı demek?",
  "<p>Her zaman değil. Bir NHS kas-iskelet servisinin diz ağrısı rehberine göre egzersiz sırasında ya da sonrasında 10 üzerinden 5'in altında kalan ve bir gün içinde geçen ağrı kabul edilebilir; egzersize devam edilir. Kasın yorulması da olağandır.</p><p>Ağrı 5'i aşıyorsa ya da 24 saatten uzun sürüyorsa yaptıklarınızı gözden geçirip yükü azaltın. Seans sonundaki ağrı ışığı bu kuralla çalışıyor.</p>",
  "East Lancashire Hospitals NHS Trust, diz ağrısı hasta rehberi"),
 ("Bir seansı kaçırırsanız ne olur?",
  "<p>Neredeyse hiçbir şey. Alışkanlık oluşumunu gerçek hayatta izleyen bir araştırmada yeni bir davranışın kendiliğinden yapılır hâle gelmesi ortalama 66 gün sürdü ve tek bir fırsatı kaçırmak bu süreci anlamlı biçimde etkilemedi.</p><p>Sorun bir kez kaçırmak değil, sık sık kaçırmak. Kaçırdığınızda kendinizi suçlamayın; bir sonraki sözünüze dönün.</p>",
  "Lally ve ark., European Journal of Social Psychology, 2010"),
 ("Üç haftada bacaklarınızda ne değişti?",
  '<p data-case="up">Başlangıçta 30 saniyede <b data-v="a"></b> kez kalkmıştınız; bugün <b data-v="b"></b>. Fark tam <b data-v="d"></b> kalkış. Bacaklarınız güçleniyor ve bunu siz ölçtünüz.</p>'
  '<p data-case="same">Başlangıçta 30 saniyede <b data-v="a"></b> kez kalkmıştınız; bugün de <b data-v="b"></b>. Endişelenmeyin: ölçüm günden güne değişebilir ve güç kazanmak zaman alır. Asıl karşılaştırma altıncı haftanın sonunda.</p>'
  '<p data-case="down">Başlangıçta 30 saniyede <b data-v="a"></b> kez kalkmıştınız; bugün <b data-v="b"></b>. Yorgunluk, ağrı ya da uykusuzluk sonucu etkileyebilir. Programa devam edin; asıl karşılaştırma altıncı haftanın sonunda.</p>'
  '<p data-case="none">Bugünkü sonucunuz yeni başlangıç noktanız olsun. Altıncı haftanın sonunda aynı ölçümü yeniden yapacağız.</p>'
  "<p>Sır şu: İlerlemeyi hissetmek zor, ölçmek kolay. Kendi sayınızı görmek, devam etmenin en güçlü nedenlerinden biri.</p>",
  "Ölçüm yöntemi: CDC STEADI, 30 saniye sandalyeden kalkma testi"),
 ("Verdiğiniz her kilo, dizinizden ne kadar yük kaldırır?",
  "<p>Yaklaşık dört katını. Diz kireçlenmesi olan, fazla kilolu yaşlı yetişkinlerin yürüyüşünü inceleyen bir çalışmada verilen her bir kilo, her adımda dize binen yükte yaklaşık dört kiloluk azalmayla ilişkili bulundu.</p><p>Bir günde atılan adımları düşünün: küçük bir kilo kaybı bile dizinize büyük bir mola demek. Kilo vermeniz gerekiyorsa hekiminizle konuşun.</p>",
  "Messier ve ark., Arthritis &amp; Rheumatism, 2005"),
 ("“Ne zaman ve nerede” demek neden bu kadar güçlü?",
  "<p>Çünkü kararı bir kez veriyorsunuz. “Şu olunca bunu yapacağım” biçimindeki planları inceleyen bir meta-analizde 94 ayrı testin ortalamasında, hedefe ulaşmada orta-büyük bir etki bulundu.</p><p>Söz kartınızdaki gün, saat ve “neyin ardından” tam olarak böyle bir plan. İpucu geldiğinde düşünmeniz gerekmiyor; sadece başlıyorsunuz.</p>",
  "Gollwitzer ve Sheeran, Advances in Experimental Social Psychology, 2006"),
 ("Egzersiz gerçekten ne kadar fark ettirir?",
  "<p>Dürüst cevap: belirgin ama mucize değil. 139 çalışmayı ve 12.468 kişiyi kapsayan güncel Cochrane derlemesinde egzersiz, egzersiz yapmamaya göre program sonunda ağrıyı 100 üzerinden yaklaşık 13 puan, günlük işlevi yaklaşık 12,5 puan iyileştirdi.</p><p>Kanıtın kesinliği düşük ile orta arasında ve etkiler program bitiminde ölçüldü. Bu yüzden sürdürmek, başlamak kadar önemli.</p>",
  "Cochrane Database of Systematic Reviews, 2024"),
 ("Egzersizi sevdiğiniz bir şeyle eşleştirmek işe yarar mı?",
  "<p>Bir deneyde katılımcılar sevdikleri sesli kitapları yalnızca spor salonunda dinleyebildi. Bu grup, kontrol grubuna göre spor salonuna %51 daha fazla gitti; etki zamanla bir miktar azaldı.</p><p>Söz kartınızda seçtiğiniz “yalnızca egzersizde dinleyeceğim” şey bu yüzden orada. Kuralı koruyun: onu başka zaman dinlemeyin.</p>",
  "Milkman ve ark., Management Science, 2014"),
 ("Sabah tutukluğu ne kadar sürmeli?",
  "<p>Kılavuzlara göre diz kireçlenmesinde sabah tutukluğu ya hiç olmaz ya da 30 dakikadan kısa sürer. 45 yaşın üstünde, hareketle artan ağrıyla birlikteyse tanı çoğu zaman muayeneyle konur.</p><p>Tutukluğunuz her sabah yarım saatten uzun sürüyorsa ya da eklemleriniz şişip ısınıyorsa hekiminize söyleyin; başka bir neden olabilir.</p>",
  "NICE, NG226, 2022"),
 ("Asıl sır ne?",
  "<p>Altı haftadır söz verdiğiniz günlerde dizinize zaman ayırdınız.</p>"
  '<p data-case="up">Başlangıçta 30 saniyede <b data-v="a"></b> kez kalkıyordunuz; bugün <b data-v="b"></b>. Fark tam <b data-v="d"></b> kalkış.</p>'
  '<p data-case="same">Başlangıçta 30 saniyede <b data-v="a"></b> kez kalkıyordunuz; bugün de <b data-v="b"></b>. Sayı aynı kaldıysa bile altı hafta boyunca sözünüzü tuttunuz; bu da ölçülebilir bir kazanım.</p>'
  '<p data-case="down">Başlangıçta 30 saniyede <b data-v="a"></b> kez kalkıyordunuz; bugün <b data-v="b"></b>. Sonuç beklediğiniz gibi değilse bir fizyoterapistle programınızı birlikte gözden geçirin.</p>'
  '<p data-case="none">Bugünkü sayınızı not edin; birkaç hafta sonra yeniden ölçün.</p>'
  "<p>Asıl sır şu: Program bitti, alışkanlık yeni başlıyor. Haftada iki gün devam edin. İsterseniz haritayı sıfırlayıp sırları bir kez daha açabilirsiniz.</p>",
  "Ölçüm yöntemi: CDC STEADI, 30 saniye sandalyeden kalkma testi"),
]

def _d12_secrets():
    return "\n          ".join(f'<article data-n="{i + 1}"><h3>{q}</h3><div class="a">{a}</div><p class="src">Kaynak: {s}</p></article>'
                               for i, (q, a, s) in enumerate(D12_SECRETS))

def _d12_ring():
    import math
    return "".join(f'<i style="--i:{i};left:{50 + 40 * math.sin(i * math.pi / 6):.2f}%;top:{50 - 40 * math.cos(i * math.pi / 6):.2f}%">{D12_LOCK}</i>' for i in range(12))

def _d12_tiles():
    names = ["Uyanış", "Güç", "Özgürlük"]
    out = []
    for c in range(3):
        tiles = "".join(f'<button type="button" class="tile" data-n="{n}"><span class="no">{n}</span>{D12_LOCK}<span class="tq">{D12_SECRETS[n - 1][0]}</span></button>'
                        for n in range(c * 4 + 1, c * 4 + 5))
        out.append(f'<div class="ch"><p class="ch-h"><b>{c + 1}. bölüm</b> · {names[c]}</p><div class="tiles">{tiles}</div></div>')
    return "\n          ".join(out)

D12_FAQ = [
 ("Neden 12 seans?", "Program altı hafta sürüyor ve haftada iki seanstan oluşuyor. Seanslar arasında en az bir gün ara vermeniz kasların toparlanmasına zaman tanır. Her seans yaklaşık 15 dakika sürer."),
 ("Bir seansı kaçırırsam ne olur?", "Hiçbir şey kaybolmaz; harita kaldığınız yerden devam eder. Alışkanlık araştırmalarında tek bir fırsatı kaçırmak süreci anlamlı biçimde etkilemiyor. Önemli olan sık sık kaçırmamak."),
 ("Egzersiz sırasında ağrım artarsa?", "10 üzerinden 5'in altında kalan ve bir gün içinde geçen ağrı kabul edilebilir. Ağrı 5'i aşıyorsa ya da 24 saatten uzun sürüyorsa seans sonundaki ağrı ışığında bunu işaretleyin; bir sonraki seans hafifler. Ağrı artmaya devam ederse hekiminize ya da fizyoterapistinize danışın."),
 ("Verilerim nereye gidiyor?", "Hiçbir yere. Sözünüz, seanslarınız ve ölçümleriniz yalnızca bu cihazın tarayıcısında saklanır; bize ya da başka birine gönderilmez. Tarayıcı verilerini silerseniz ilerlemeniz de silinir."),
]

D12_SRC = [
 "Jack K, McLean SM, Moffett JK, Gardiner E. " + ext("https://pubmed.ncbi.nlm.nih.gov/20163979/", "Barriers to treatment adherence in physiotherapy outpatient clinics: a systematic review") + ". Man Ther. 2010;15(3):220–228.",
 "Bedson J, Croft PR. " + ext("https://link.springer.com/article/10.1186/1471-2474-9-116", "The discordance between clinical and radiographic knee osteoarthritis: a systematic search and summary of the literature") + ". BMC Musculoskelet Disord. 2008;9:116.",
 "Øiestad BE, Juhl CB, Culvenor AG, Berg B, Thorlund JB. " + ext("https://bjsm.bmj.com/content/56/6/349", "Knee extensor muscle weakness is a risk factor for the development of knee osteoarthritis: an updated systematic review and meta-analysis including 46 819 men and women") + ". Br J Sports Med. 2022;56(6):349–355.",
 "East Lancashire Hospitals NHS Trust. " + ext("https://elht.nhs.uk/services/integrated-msk-pain-and-rheumatology-service/knee-pain-not-caused-accident-or-injury", "Knee pain not caused by accident or injury") + ". Integrated MSK, Pain and Rheumatology Service.",
 "Lally P, van Jaarsveld CHM, Potts HWW, Wardle J. How are habits formed: modelling habit formation in the real world. Eur J Soc Psychol. 2010;40(6):998–1009. Özeti: " + ext("https://www.ucl.ac.uk/news/2009/aug/how-long-does-it-take-form-habit", "UCL News, How long does it take to form a habit?") + ", 4 August 2009.",
 "Messier SP, Gutekunst DJ, Davis C, DeVita P. " + ext("https://pubmed.ncbi.nlm.nih.gov/15986358/", "Weight loss reduces knee-joint loads in overweight and obese older adults with knee osteoarthritis") + ". Arthritis Rheum. 2005;52(7):2026–2032.",
 "Gollwitzer PM, Sheeran P. " + ext("https://search.worldcat.org/title/Implementation-Intentions-and-Goal-Achievement:-A-Metaanalysis-of-Effects-and-Processes/oclc/4922448186", "Implementation intentions and goal achievement: a meta-analysis of effects and processes") + ". Adv Exp Soc Psychol. 2006;38:69–119.",
 "Lawford BJ, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/39625083/", "Exercise for osteoarthritis of the knee") + ". Cochrane Database Syst Rev. 2024;12:CD004376.",
 "Milkman KL, Minson JA, Volpp KGM. " + ext("https://pubmed.ncbi.nlm.nih.gov/25843979/", "Holding the Hunger Games hostage at the gym: an evaluation of temptation bundling") + ". Manage Sci. 2014;60(2):283–299.",
 "National Institute for Health and Care Excellence. " + ext("https://www.nice.org.uk/guidance/ng226", "Osteoarthritis in over 16s: diagnosis and management (NG226)") + ". London: NICE; 2022.",
 "Centers for Disease Control and Prevention. " + ext("https://www.cdc.gov/steadi/media/pdfs/STEADI-Assessment-30Sec-508.pdf", "STEADI Assessment: 30-Second Chair Stand") + ". 2017.",
]

D12_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak · Diz kireçlenmesi</p>
    <h1>Dizin 12 Sırrı</h1>
    <p class="lede">Diz kireçlenmesinde egzersiz, ağrıyı ve günlük işlevi iyileştiren yöntemlerin başında gelir; zor olan onu sürdürmektir. Bu altı haftalık ev programında her seans, dizinizle ya da alışkanlıklarınızla ilgili kilitli bir sırrı açar. Sorular baştan görünür; cevaplar ancak seansı bitirince.</p>
    <p class="meta">Son güncelleme: 10 Ekim 2026</p>
  </div>
</header>

<main>
  <section class="d12-sec">
    <div class="wrap">
      <div id="d12" class="d12">

        <div data-view="intro">
          <div class="d12-hero">
            <div class="ring" aria-hidden="true">{_d12_ring()}<span class="core">12</span></div>
            <ol class="how4">
              <li><b>Söz verin.</b><span>Haftada hangi iki gün, saat kaçta, neyin ardından?</span></li>
              <li><b>Ölçün.</b><span>30 saniyede sandalyeden kaç kez kalkabiliyorsunuz?</span></li>
              <li><b>Seansı yapın.</b><span>Yaklaşık 15 dakika; telefon sizin için sayar.</span></li>
              <li><b>Sırrı açın.</b><span>Her seansın sonunda bir kilit açılır.</span></li>
            </ol>
            <button type="button" class="cta" data-act="begin">Başlayalım</button>
            <p class="hint">Verileriniz yalnızca bu cihazda saklanır.</p>
          </div>
        </div>

        <div data-view="plan" hidden>
          <p class="eyebrow">Adım 1 · Söz kartı</p>
          <h2>Sözünüzü yazalım</h2>
          <p class="soft">Kararı bir kez verin; gün geldiğinde düşünmeniz gerekmesin.</p>
          <div class="q"><p class="ql">Haftada hangi iki gün? <small>Arada en az bir gün olsun.</small></p><div class="chips" id="d12-days"></div></div>
          <div class="q"><p class="ql">Saat kaçta?</p><div class="chips" id="d12-time">
            <button type="button" data-t="09:00">Sabah</button><button type="button" data-t="13:00">Öğle</button><button type="button" data-t="19:00">Akşam</button>
            <label class="tin"><input type="time" id="d12-tval" value="19:00" aria-label="Saat"></label></div></div>
          <div class="q"><p class="ql">Neyin ardından? <small>Her gün zaten yaptığınız bir şey seçin.</small></p><div class="chips" id="d12-cue">
            <button type="button">Sabah kahvemden sonra</button><button type="button">Öğle yemeğinden sonra</button><button type="button">Akşam haberlerinden önce</button><button type="button">Dişlerimi fırçalamadan önce</button>
            <input type="text" id="d12-cue-x" maxlength="60" placeholder="Ya da kendiniz yazın" aria-label="Kendi ipucunuz"></div></div>
          <div class="q"><p class="ql">Yalnızca egzersiz yaparken neyi dinleyeceksiniz? <small>İsteğe bağlı.</small></p><div class="chips" id="d12-bun">
            <button type="button">En sevdiğim şarkıları</button><button type="button">Bir radyo programını</button><button type="button">Bir sesli kitabı</button>
            <input type="text" id="d12-bun-x" maxlength="60" placeholder="Ya da kendiniz yazın" aria-label="Kendi seçiminiz"></div></div>
          <div class="pact" id="d12-pact" aria-live="polite"></div>
          <div class="controls"><button type="button" class="cta" data-act="pact" disabled>Söz veriyorum</button></div>
        </div>

        <div data-view="test" hidden><div class="d12-test" id="d12-test0"></div></div>

        <div data-view="map" hidden>
          <div class="fresh" id="d12-fresh" hidden><b>Yeni bir hafta, temiz bir sayfa.</b> Ara verdiyseniz sorun değil; hiçbir şey kaybolmadı. Kaldığınız yerden devam edin.</div>
          <div class="next" id="d12-next"></div>
          <div class="mrow">
            <div class="week"><svg viewBox="0 0 44 44" aria-hidden="true"><circle cx="22" cy="22" r="18"/><circle class="wv" cx="22" cy="22" r="18"/></svg><p><b id="d12-wk"></b><span>Bu hafta</span></p></div>
            <div class="mpact"><p class="k">Söz kartınız</p><p id="d12-pact2"></p>
              <div class="acts"><button type="button" class="lnk" data-act="ics">Takvime ekle</button><a class="lnk" id="d12-wa" target="_blank" rel="noopener">Bir yakınıma söyle</a><button type="button" class="lnk" data-act="edit">Değiştir</button></div></div>
          </div>
          <div class="map">
            {_d12_tiles()}
          </div>
          <div class="tests" id="d12-tests"></div>
          <p class="hint foot">Verileriniz yalnızca bu cihazda saklanır. <button type="button" class="lnk" data-act="reset">Programı sıfırla</button></p>
        </div>

        <div class="ov" id="d12-ov" hidden role="dialog" aria-modal="true" aria-label="Seans"></div>

        <div class="d12-s" hidden>
          <span data-k="and"> ve </span>
          <span data-k="pact">Her <b data-v="days"></b> saat <b data-v="time"></b> gibi, <b data-v="cue"></b>, dizim için 15 dakika ayıracağım.</span>
          <span data-k="bun"><b data-v="b"></b> yalnızca egzersiz yaparken dinleyeceğim.</span>
          <span data-k="pact0">Gün seçtikçe sözünüz burada belirecek.</span>
          <span data-k="nx_k">Sıradaki sır</span>
          <span data-k="nx_m">Seans <b data-v="n"></b> / 12 · yaklaşık 15 dakika · 4 hareket</span>
          <span data-k="nx_go">Seansı başlat</span>
          <span data-k="nx_done">On iki kilidin hepsi açık. Programı sürdürmek için haftada iki gün devam edin.</span>
          <span data-k="wk"><b data-v="a"></b> / 2</span>
          <span data-k="t_base">Başlangıç</span><span data-k="t_mid">3. hafta</span><span data-k="t_final">6. hafta</span>
          <span data-k="t_h">30 saniyede sandalyeden kalkma</span>
          <span data-k="t_none">Henüz ölçülmedi</span>
          <span data-k="warm">Isınma: yerinde yürüyün</span>
          <span data-k="warm_s">Kollarınızı sallayarak, rahat bir tempoda.</span>
          <span data-k="rest">Dinlenin</span>
          <span data-k="rest_side">Diğer bacağa geçin</span>
          <span data-k="lockp">Sırrın kilidi açılıyor</span>
          <span data-k="this_s">Bu seansın sırrı</span>
          <span data-k="skip">Atla</span>
          <span data-k="go">Başlat</span><span data-k="pause">Duraklat</span><span data-k="plus">+1 tekrar</span><span data-k="next">Sonraki</span>
          <span data-k="hold">Tutun</span>
          <span data-k="howq">Nasıl yapılır?</span>
          <span data-k="mv">Hareket <b data-v="i"></b> / <b data-v="m"></b> · Set <b data-v="s"></b> / 2</span>
          <span data-k="right">Sağ bacak</span><span data-k="left">Sol bacak</span>
          <span data-k="dose_r"><b data-v="r"></b> tekrar</span>
          <span data-k="dose_h"><b data-v="r"></b> tekrar · <b data-v="h"></b> saniye tutarak</span>
          <span data-k="slow">Oturuşu 3 saniyeye yayın.</span>
          <span data-k="voice">Sesli sayma</span>
          <span data-k="quit">Seanstan çık</span>
          <span data-k="quit_q">Seanstan çıkılsın mı? Bu seans kaydedilmeyecek.</span>
          <span data-k="end_h">Seans tamam!</span>
          <span data-k="end_p">Şu an dizinizdeki ağrı 10 üzerinden kaç?</span>
          <span data-k="pain_g">Yeşil ışık: harika. Bir sonraki seans biraz zorlaşabilir.</span>
          <span data-k="pain_y">Sarı ışık: kabul edilebilir. Yarına kadar geçmesi gerekir; geçmezse yükü azaltın.</span>
          <span data-k="pain_r">Kırmızı ışık: bugün fazla geldi. Bir sonraki seans hafifleyecek; ağrı 24 saatten uzun sürerse hekiminize danışın.</span>
          <span data-k="eff">Nasıl geldi?</span>
          <span data-k="e1">Kolaydı</span><span data-k="e2">Tam kararında</span><span data-k="e3">Zordu</span>
          <span data-k="open">Sırrı aç</span>
          <span data-k="sec_k">Sır <b data-v="n"></b> / 12</span>
          <span data-k="teaser">Sıradaki sır, seans <b data-v="n"></b> sonunda açılacak:</span>
          <span data-k="when">Sözünüze göre bir sonraki seans: <b data-v="d"></b></span>
          <span data-k="back">Haritaya dön</span>
          <span data-k="close">Kapat</span>
          <span data-k="reset_q">Tüm ilerlemeniz bu cihazdan silinsin mi?</span>
          <span data-k="ics_t">Dizin 12 Sırrı · seans</span>
          <span data-k="wa">Dizim için 6 hafta boyunca haftada iki gün egzersiz yapmaya söz verdim: <b data-v="p"></b> Arada bir bana sorar mısın?</span>
          <span data-k="test_base">Başlangıç noktanız</span>
          <span data-k="test_mid">Yarı yol ölçümü</span>
          <span data-k="test_final">Son ölçüm</span>
          <span data-k="test_q">30 saniyede sandalyeden kaç kez kalkabiliyorsunuz?</span>
          <span data-k="t_go">Süreyi başlat</span>
          <span data-k="t_run">Kalkın, oturun… sayın!</span>
          <span data-k="t_end">Süre doldu. Kaç kez kalktınız?</span>
          <span data-k="t_save">Kaydet</span>
          <span data-k="t_skip">Şimdi değil</span>
          <span data-k="t_ready">Hazır olun</span>
        </div>

        <div class="d12-testhow" hidden>
          <ol class="steps">
            <li><span>Kolsuz, sırtı düz, sağlam bir sandalyeyi duvara dayayın. Yanınızda biri olsun.</span></li>
            <li><span>Sandalyenin ortasına oturun; ayaklarınız yerde, sırtınız dik. Kollarınızı bileklerden çaprazlayıp ellerinizi karşı omuzlarınıza koyun.</span></li>
            <li><span>Başlama sesiyle tam ayağa kalkıp yeniden oturun; 30 saniye boyunca tekrarlayın ve içinizden sayın.</span></li>
            <li><span>Süre bittiğinde yarıdan fazla kalkmışsanız onu da sayın.</span></li>
          </ol>
          <p class="note warn"><strong>Güvenlik:</strong> Kalkmak için kollarınızı kullanmanız gerekiyorsa testi durdurun ve sonucu 0 olarak kaydedin. Baş dönmesi, göğüs ağrısı ya da nefes darlığı olursa hemen bırakın.</p>
        </div>

        <div class="d12-ex" hidden>
          {_d12_exdata()}
        </div>

        <div class="d12-secrets" hidden>
          {_d12_secrets()}
        </div>

        <noscript><p class="note">Program, tarayıcınızda JavaScript açıkken çalışır. Aşağıda programın tamamını okuyabilirsiniz.</p></noscript>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <p class="eyebrow">Neden böyle tasarlandı?</p>
      <h2>Egzersizi sürdürmek için yedi bilimsel ipucu</h2>
      <p class="soft">Evde egzersiz önerilenlerin önemli bir kısmı programı sürdüremiyor. Bu sayfanın her parçası, bu sorunu inceleyen araştırmalardan bir fikre dayanıyor. Suçluluk, utanç ya da sahte aciliyet gibi baskı yöntemleri kullanmadık.</p>
      <ul class="tx">
        <li><b>Söz kartı</b><span>“Şu olunca bunu yapacağım” biçimindeki planlar, hedefe ulaşmada orta-büyük bir etkiyle ilişkili bulundu.</span></li>
        <li><b>Kilitli sırlar</b><span>Sorusunu bildiğiniz ama cevabını henüz öğrenmediğiniz bir şey, merak uyandırır. Her seans bir sonrakini merak ettirecek biçimde biter.</span></li>
        <li><b>Esnek takvim</b><span>Seri bozulunca cezalandırma yok: Alışkanlık araştırmalarında tek bir fırsatı kaçırmak süreci anlamlı biçimde etkilemiyor.</span></li>
        <li><b>Ağrı trafik ışığı</b><span>Egzersiz sırasında artan ağrı, bırakmanın güçlü nedenlerinden biri. Işık, kabul edilebilir ağrıyı ayırt etmenize ve programı ayarlamanıza yardım eder.</span></li>
        <li><b>Kendi ölçümünüz</b><span>30 saniye sandalyeden kalkma testi başta, üçüncü haftada ve sonda tekrarlanır; ilerlemenizi kendiniz görürsünüz.</span></li>
        <li><b>Eşleştirme</b><span>Sevdiğiniz bir şeyi yalnızca egzersiz yaparken dinlemek, bir deneyde spor salonuna gitme sıklığını belirgin biçimde artırdı.</span></li>
        <li><b>Bir yakınınız</b><span>Sosyal desteğin az olması, egzersizi bırakmayla ilişkili bulunan etkenlerden. Sözünüzü bir yakınınızla paylaşabilirsiniz.</span></li>
      </ul>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Program</p>
      <h2>Üç bölüm, altı hareket</h2>
      <p class="soft">Altı hafta, haftada iki seans. Her seans bir dakikalık ısınma ve dört hareketten oluşur; her hareket iki set yapılır. Seans sonundaki ağrı ve zorluk yanıtınıza göre bir sonraki seansın tekrar sayısı ayarlanır.</p>
      <ul class="tx">
        <li><b>1. bölüm · Uyanış</b><span>Seans 1–4: Havluya bastırma, oturarak diz düzeltme, düz bacak kaldırma, sandalyeden kalkıp oturma.</span></li>
        <li><b>2. bölüm · Güç</b><span>Seans 5–8: Oturarak diz düzeltme, sandalyeden kalkıp oturma, yan yatarak bacak kaldırma, duvarda yarım çömelme.</span></li>
        <li><b>3. bölüm · Özgürlük</b><span>Seans 9–12: Yavaş oturuşla sandalyeden kalkma, duvarda yarım çömelme, yan yatarak bacak kaldırma, düz bacak kaldırma.</span></li>
      </ul>
      {ex_grid(["d12_quad", "d12_kext", "d12_slr", "d12_sts", "d12_abd", "d12_wall"])}
      <div class="callout"><p>Hareketlerin ayrıntılı anlatımı ve diz kireçlenmesi hakkında daha fazlası için <a href="diz-kireclenmesi.html">diz kireçlenmesi rehberine</a> bakın.</p></div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(D12_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Başlamadan önce danışın</h2>
      <p class="soft">Şu durumlarda programa başlamadan önce hekiminize ya da fizyoterapistinize danışın:</p>
      <ul class="dots redflags">
        <li>Yakın zamanda diz ameliyatı ya da diz yaralanması geçirdiyseniz</li>
        <li>Dizinizde yeni başlayan şişlik, kızarıklık ve ısı varsa ya da ateşiniz varsa</li>
        <li>Dizinizin üzerine basamıyorsanız</li>
        <li>Ağrınız dinlenirken ve geceleri giderek artıyorsa</li>
        <li>Sık düşüyorsanız ya da dengeniz çok bozuksa</li>
      </ul>
      {CTA_CARD("Diz ağrınız", "diz kireçlenmesi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(D12_SRC)}
    </div>
  </section>
</main>'''

D12_CSS = SELF_CSS + """
  .d12{position:relative;max-width:720px;margin:0 auto}
  .d12 h2{margin:6px 0 6px}
  .d12 .chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
  .d12 .chips button{all:unset;box-sizing:border-box;cursor:pointer;min-height:42px;padding:9px 15px;border-radius:999px;border:1px solid var(--line-strong);font-size:15px;color:var(--ink-soft);line-height:1.3}
  .d12 .chips button.on{background:var(--foil);border-color:var(--foil);color:var(--ground);font-weight:600}
  .d12 .chips input[type=text]{flex:1 1 220px;min-width:0;min-height:42px;padding:9px 15px;border-radius:999px;border:1px dashed var(--line-strong);background:transparent;color:var(--ink);font:inherit;font-size:15px}
  .d12 .chips input[type=text]:focus{outline:none;border-style:solid;border-color:var(--foil)}
  .d12 .tin input{min-height:42px;padding:6px 14px;border-radius:999px;border:1px solid var(--line-strong);background:transparent;color:var(--ink);font:inherit;font-size:15px;color-scheme:dark}
  .d12 .q{margin-top:22px}
  .d12 .ql{margin:0;font-weight:600;color:var(--ink)}
  .d12 .ql small{display:block;font-weight:400;color:var(--muted);font-size:13.5px;margin-top:2px}
  .d12 .pact{margin:26px 0 18px;padding:22px 22px 20px;border-radius:18px;background:var(--paper);color:var(--paper-ink);font-family:var(--display);font-size:20px;line-height:1.45;box-shadow:0 18px 40px rgba(0,0,0,.35);position:relative}
  .d12 .pact::before{content:"";position:absolute;inset:8px;border:1px dashed rgba(43,51,37,.25);border-radius:12px;pointer-events:none}
  .d12 .pact b{color:#7a5a12;font-weight:400;border-bottom:1.5px solid rgba(122,90,18,.35)}
  .d12 .pact.empty{font-family:var(--body);font-size:15px;color:#6b705c}
  .d12 button.cta[disabled]{opacity:.45;cursor:not-allowed}
  .d12 .lnk,.ov .lnk{all:unset;cursor:pointer;color:var(--foil);font-size:14px;font-weight:600;text-decoration:underline;text-underline-offset:3px}
  /* giriş */
  .d12-hero{display:grid;justify-items:center;text-align:center;gap:18px;padding:8px 0 4px}
  .d12-hero .ring{position:relative;width:min(280px,72vw);aspect-ratio:1;margin-bottom:10px}
  .d12-hero .ring i{position:absolute;width:12%;transform:translate(-50%,-50%);animation:d12glow 4.8s ease-in-out infinite;animation-delay:calc(var(--i)*.4s)}
  .d12-hero .ring .core{position:absolute;inset:30%;display:grid;place-items:center;border-radius:50%;font-family:var(--display);font-size:clamp(44px,12vw,64px);color:var(--gold);
    background:radial-gradient(closest-side,rgba(226,171,71,.16),transparent);border:1px solid var(--line-strong)}
  @keyframes d12glow{0%,70%,100%{opacity:.45;filter:none}80%{opacity:1;filter:drop-shadow(0 0 8px rgba(226,171,71,.8))}}
  .lk{display:block;width:100%;height:auto}
  .lk rect{fill:none;stroke:var(--foil);stroke-width:3.4}
  .lk .sh{stroke:var(--foil);transition:transform .5s cubic-bezier(.3,1.6,.5,1)}
  .lk .kh{fill:var(--foil)}
  .how4{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:10px;width:100%;text-align:left;counter-reset:h}
  .how4 li{display:grid;grid-template-columns:34px 1fr;gap:2px 12px;align-items:baseline;padding:12px 14px;border:1px solid var(--line);border-radius:14px;counter-increment:h}
  .how4 li::before{content:counter(h);grid-row:span 2;font-family:var(--display);font-size:24px;color:var(--gold)}
  .how4 b{color:var(--ink)}
  .how4 span{color:var(--ink-soft);font-size:14.5px}
  @media (min-width:700px){.how4{grid-template-columns:1fr 1fr}}
  /* harita */
  .next{display:grid;grid-template-columns:64px 1fr;gap:6px 16px;align-items:center;padding:20px;border-radius:20px;border:1px solid var(--line-strong);
    background:radial-gradient(120% 100% at 0% 0%,rgba(226,171,71,.14),transparent 60%),var(--panel);box-shadow:0 18px 40px rgba(0,0,0,.3)}
  .next .nl{grid-row:span 3;align-self:start}
  .next .lk{width:56px;animation:d12bob 3s ease-in-out infinite}
  @keyframes d12bob{50%{transform:translateY(-4px) rotate(-3deg)}}
  .next .k{margin:0;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);font-weight:600}
  .next h3{margin:2px 0 0;font-family:var(--display);font-weight:400;font-size:clamp(21px,5vw,26px);line-height:1.25;color:var(--ink)}
  .next .m{margin:4px 0 0;color:var(--muted);font-size:14px}
  .next .cta{grid-column:1 / -1;justify-self:start;margin-top:10px}
  .next.done{grid-template-columns:1fr}
  .fresh{margin-bottom:14px;padding:12px 16px;border-radius:14px;border:1px solid var(--line-strong);background:rgba(143,164,118,.12);color:var(--ink-soft);font-size:15px}
  .fresh b{color:var(--ink)}
  .mrow{display:grid;grid-template-columns:auto 1fr;gap:16px;align-items:center;margin:18px 0 6px;padding:16px;border:1px solid var(--line);border-radius:18px}
  .week{display:grid;justify-items:center;gap:4px;text-align:center}
  .week svg{width:62px;height:62px;transform:rotate(-90deg)}
  .week circle{fill:none;stroke:var(--line);stroke-width:5}
  .week .wv{stroke:var(--gold);stroke-linecap:round;stroke-dasharray:113.1;stroke-dashoffset:113.1;transition:stroke-dashoffset .8s ease}
  .week p{margin:0;display:grid}
  .week b{font-family:var(--display);font-size:18px;color:var(--ink);font-weight:400}
  .week span{font-size:12px;color:var(--muted)}
  .mpact .k{margin:0;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
  .mpact p{margin:4px 0 0;color:var(--ink-soft);font-size:14.5px;line-height:1.5}
  .mpact .acts{display:flex;flex-wrap:wrap;gap:6px 16px;margin-top:8px}
  .map{display:grid;gap:18px;margin-top:22px}
  .ch-h{margin:0 0 8px;color:var(--muted);font-size:14px}
  .ch-h b{color:var(--gold);font-weight:600}
  .tiles{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
  @media (min-width:700px){.tiles{grid-template-columns:repeat(4,minmax(0,1fr))}}
  .tile{all:unset;box-sizing:border-box;position:relative;display:grid;grid-template-columns:30px 1fr;gap:4px 10px;align-items:start;padding:12px;border-radius:14px;border:1px solid var(--line);cursor:default;min-height:92px}
  .tile .no{position:absolute;right:10px;top:8px;font-family:var(--display);font-size:15px;color:var(--muted)}
  .tile .lk{width:26px;opacity:.55}
  .tile .tq{font-size:13.5px;line-height:1.35;color:var(--muted);padding-right:14px}
  .tile.cur{border-color:var(--foil);background:rgba(226,171,71,.08)}
  .tile.cur .lk{opacity:1;filter:drop-shadow(0 0 6px rgba(226,171,71,.6))}
  .tile.cur .tq{color:var(--ink)}
  .tile.open{cursor:pointer;border-color:var(--line-strong);background:linear-gradient(160deg,rgba(226,171,71,.16),rgba(226,171,71,.04))}
  .tile.open .lk{opacity:1}
  .tile.open .lk .sh{transform:translateY(-4px) rotate(-14deg);transform-origin:29px 20px}
  .tile.open .lk rect{fill:var(--foil)}
  .tile.open .lk .kh{fill:var(--ground)}
  .tile.open .tq{color:var(--ink)}
  .tile.open:hover{border-color:var(--foil)}
  .tests{margin-top:22px;padding:16px;border:1px solid var(--line);border-radius:18px}
  .tests h3{margin:0 0 10px;font-size:15px;font-weight:600;color:var(--ink)}
  .tests .bars{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;align-items:end;height:130px}
  .tests .bar{display:grid;justify-items:center;align-content:end;gap:6px;height:100%}
  .tests .bar i{display:block;width:44px;max-width:80%;border-radius:10px 10px 4px 4px;background:linear-gradient(var(--gold),rgba(226,171,71,.35));min-height:4px;transition:height .8s ease}
  .tests .bar b{font-family:var(--display);font-size:20px;font-weight:400;color:var(--ink)}
  .tests .bar span{font-size:12.5px;color:var(--muted)}
  .tests .bar.none i{background:var(--line)}
  .foot{margin-top:18px}
  /* tam ekran katman */
  .ov{position:fixed;inset:0;z-index:300;overflow-y:auto;background:radial-gradient(90% 60% at 50% 0%,rgba(226,171,71,.10),transparent 60%),var(--ground);
    padding:calc(14px + env(safe-area-inset-top,0px)) 18px calc(24px + env(safe-area-inset-bottom,0px))}
  .ov .in{max-width:560px;margin:0 auto;display:grid;gap:14px}
  .ov .top{display:flex;align-items:center;gap:10px}
  .ov .segs{flex:1;display:flex;gap:3px}
  .ov .segs i{flex:1;height:4px;border-radius:2px;background:var(--line)}
  .ov .segs i.d{background:var(--gold)}
  .ov .segs i.c{background:linear-gradient(90deg,var(--gold) var(--p,0%),var(--line) var(--p,0%))}
  .ov .ib{all:unset;cursor:pointer;width:40px;height:40px;display:grid;place-items:center;border-radius:50%;border:1px solid var(--line);color:var(--ink-soft);flex:none}
  .ov .ib svg{width:20px;height:20px}
  .ov .ib.off{opacity:.45}
  .ov .meta{margin:0;font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);font-weight:600}
  .ov h2{margin:0;font-family:var(--display);font-weight:400;font-size:clamp(26px,7vw,34px);line-height:1.15;color:var(--ink)}
  .ov .dose{margin:0;color:var(--ink-soft)}
  .ov .fig{display:grid;grid-template-columns:minmax(0,1fr) 150px;gap:12px;align-items:center}
  .ov .fig figure{margin:0;border-radius:18px;overflow:hidden;background:var(--paper)}
  .ov .fig figure svg{display:block;width:100%;height:auto}
  .ov .fig figcaption{display:none}
  .ring2{position:relative;width:150px;aspect-ratio:1}
  .ring2 svg{width:100%;height:100%;transform:rotate(-90deg)}
  .ring2 circle{fill:none;stroke-width:9}
  .ring2 .bg{stroke:var(--line)}
  .ring2 .fg{stroke:var(--gold);stroke-linecap:round;stroke-dasharray:314.16;stroke-dashoffset:314.16}
  .ring2 .c{position:absolute;inset:0;display:grid;place-content:center;text-align:center}
  .ring2 .c b{font-family:var(--display);font-size:46px;font-weight:400;line-height:1;color:var(--ink)}
  .ring2 .c small{font-size:13px;color:var(--muted)}
  .ring2 .c em{font-style:normal;font-size:15px;font-weight:600;color:var(--gold);margin-top:6px;min-height:1.3em}
  .ov .btns{display:flex;flex-wrap:wrap;gap:10px}
  .ov .btns .cta{min-width:120px;justify-content:center}
  .ov details{border:1px solid var(--line);border-radius:14px;padding:10px 14px}
  .ov details summary{cursor:pointer;color:var(--ink);font-weight:600;font-size:15px}
  .ov details p{margin:8px 0 2px;color:var(--ink-soft);font-size:15px}
  .ov .rest{display:grid;justify-items:center;text-align:center;gap:14px;padding-top:4vh}
  .ov .rest .ring2{width:200px}
  .ov .rest .ring2 .c b{font-size:60px}
  .ov .tease{width:100%;padding:16px;border-radius:16px;border:1px dashed var(--line-strong);text-align:left}
  .ov .tease p{margin:0}
  .ov .tease .k{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);font-weight:600}
  .ov .tease .qq{margin-top:6px;font-family:var(--display);font-size:20px;color:var(--ink);line-height:1.3}
  .ov .lbar{height:6px;border-radius:3px;background:var(--line);overflow:hidden;margin-top:12px}
  .ov .lbar i{display:block;height:100%;background:linear-gradient(90deg,var(--foil),#f3d58f);width:0;transition:width .6s ease}
  .ov .pain input{width:100%;accent-color:var(--gold)}
  .ov .pain .pv{display:flex;align-items:center;gap:14px;margin-top:10px}
  .ov .pain .pv b{font-family:var(--display);font-size:42px;font-weight:400;min-width:56px;color:var(--ink)}
  .ov .light{display:flex;gap:8px}
  .ov .light i{width:18px;height:18px;border-radius:50%;background:rgba(236,229,207,.12);transition:background .3s,box-shadow .3s}
  .ov .light.g i:nth-child(1){background:#7fbf6a;box-shadow:0 0 12px #7fbf6a}
  .ov .light.y i:nth-child(2){background:#e7c24a;box-shadow:0 0 12px #e7c24a}
  .ov .light.r i:nth-child(3){background:#e0624f;box-shadow:0 0 12px #e0624f}
  .ov .pmsg{margin:10px 0 0;color:var(--ink-soft);font-size:15px;min-height:3em}
  .ov .chips{display:flex;flex-wrap:wrap;gap:8px}
  .ov .chips button{all:unset;cursor:pointer;padding:9px 15px;border-radius:999px;border:1px solid var(--line-strong);color:var(--ink-soft);font-size:15px}
  .ov .chips button.on{background:var(--foil);border-color:var(--foil);color:var(--ground);font-weight:600}
  /* sır açılışı */
  .rv{display:grid;justify-items:center;gap:18px;padding-top:2vh}
  .rv .big{width:96px;position:relative}
  .rv .big .lk rect{fill:rgba(226,171,71,.12)}
  .rv.go .big{animation:d12shake .5s ease .1s 1}
  .rv.go .big .lk .sh{transform:translateY(-7px) rotate(-22deg);transform-origin:29px 20px;transition-delay:.65s}
  .rv.go .big .lk rect{fill:var(--foil);transition:fill .4s ease .8s}
  .rv.go .big .lk .kh{fill:var(--ground);transition:fill .4s ease .8s}
  .rv .burst{position:absolute;left:50%;top:58%;width:0;height:0}
  .rv .burst i{position:absolute;width:6px;height:6px;margin:-3px;border-radius:50%;background:var(--gold);opacity:0}
  .rv.go .burst i{animation:d12burst .9s cubic-bezier(.2,.8,.2,1) .85s forwards}
  @keyframes d12burst{0%{opacity:1;transform:rotate(var(--a)) translateY(0) scale(1)}100%{opacity:0;transform:rotate(var(--a)) translateY(-70px) scale(.4)}}
  @keyframes d12shake{20%{transform:rotate(-8deg)}40%{transform:rotate(7deg)}60%{transform:rotate(-5deg)}80%{transform:rotate(3deg)}}
  .card{width:100%;padding:22px 20px 18px;border-radius:20px;background:var(--paper);color:var(--paper-ink);box-shadow:0 22px 50px rgba(0,0,0,.45);
    opacity:0;transform:translateY(24px) scale(.97)}
  .rv.go .card,.rv.ro .card{animation:d12card .7s cubic-bezier(.2,.8,.2,1) 1.25s forwards}
  .rv.ro .card{animation-delay:0s}
  @keyframes d12card{to{opacity:1;transform:none}}
  .card .k{margin:0;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:#7a5a12;font-weight:700}
  .card h3{margin:6px 0 10px;font-family:var(--display);font-weight:400;font-size:clamp(22px,6vw,28px);line-height:1.2;color:var(--paper-ink)}
  .card .a p{margin:0 0 10px;font-size:16px;line-height:1.6;color:#3a4232}
  .card .a b{color:#7a5a12}
  .card .a p[data-case]{display:none}
  .card .a p.show{display:block}
  .card .src{margin:6px 0 0;font-size:12.5px;color:#6b705c}
  .rv .tease{opacity:0}
  .rv.go .tease,.rv.ro .tease{animation:d12card .6s ease 1.9s forwards}
  .rv.ro .tease{animation-delay:.3s}
  .rv .tease .when{margin-top:8px;color:var(--muted);font-size:14px}
  /* ölçüm */
  .d12-test{display:grid;gap:14px}
  .d12-test .ring2{width:190px;justify-self:center}
  .d12-test .ring2 .c b{font-size:58px}
  .d12-test .step{display:flex;align-items:center;justify-content:center;gap:18px}
  .d12-test .step button{all:unset;cursor:pointer;width:52px;height:52px;border-radius:50%;border:1px solid var(--line-strong);display:grid;place-items:center;font-size:26px;color:var(--ink)}
  .d12-test .step b{font-family:var(--display);font-size:52px;font-weight:400;min-width:80px;text-align:center;color:var(--ink)}
  .d12-test .center{justify-self:center;text-align:center}
  @media (prefers-reduced-motion:reduce){.d12-hero .ring i,.next .lk{animation:none}.rv.go .big{animation:none}}
"""

D12_JS = r'''<script>
(function(){
  var R = document.getElementById('d12'); if (!R) return;
  var EN = document.documentElement.lang === 'en', LANG = EN ? 'en-GB' : 'tr-TR';
  function $(s, el){ return (el || R).querySelector(s); }
  function $$(s, el){ return Array.prototype.slice.call((el || R).querySelectorAll(s)); }
  var S = {}; $$('.d12-s [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.innerHTML.trim(); });
  function fill(html, v){ var d = document.createElement('div'); d.innerHTML = html; $$('[data-v]', d).forEach(function(e){ var x = v[e.getAttribute('data-v')]; if (x !== undefined) e.textContent = x; }); return d.innerHTML; }
  function txt(html){ var d = document.createElement('div'); d.innerHTML = html; return d.textContent.replace(/\s+/g, ' ').trim(); }
  function lc(s){ s = (s || '').trim(); return s ? s.charAt(0).toLocaleLowerCase(LANG) + s.slice(1) : s; }
  var KEY = 'drihsaneren.diz12.v1', st;
  function load(){ try { st = JSON.parse(localStorage.getItem(KEY)); } catch (e) { st = null; }
    if (!st || typeof st !== 'object') st = {}; st.done = st.done || []; st.tests = st.tests || {}; st.adj = st.adj || 0; if (st.voice === undefined) st.voice = true; }
  function save(){ try { localStorage.setItem(KEY, JSON.stringify(st)); } catch (e) {} }
  load();

  /* ---- görünümler */
  function show(v){ $$('[data-view]').forEach(function(e){ e.hidden = e.getAttribute('data-view') !== v; }); }
  var wd = [1, 2, 3, 4, 5, 6, 0];
  function dayName(d, f){ var b = new Date(2024, 0, 7 + d); return new Intl.DateTimeFormat(LANG, {weekday: f || 'long'}).format(b); }

  /* ---- söz kartı */
  var pick = {days: [], time: '19:00', cue: '', bun: ''};
  function initPlan(){
    var p = st.plan; if (p) pick = {days: p.days.slice(), time: p.time, cue: p.cue, bun: p.bun || ''};
    var box = $('#d12-days'); box.innerHTML = '';
    wd.forEach(function(d){ var b = document.createElement('button'); b.type = 'button'; b.textContent = dayName(d, 'short'); b.setAttribute('aria-label', dayName(d));
      b.className = pick.days.indexOf(d) >= 0 ? 'on' : ''; b.onclick = function(){ var i = pick.days.indexOf(d); if (i >= 0) pick.days.splice(i, 1); else { pick.days.push(d); if (pick.days.length > 2) pick.days.shift(); }
        $$('#d12-days button').forEach(function(x, j){ x.className = pick.days.indexOf(wd[j]) >= 0 ? 'on' : ''; }); renderPact(); }; box.appendChild(b); });
    $('#d12-tval').value = pick.time;
    $$('#d12-time button').forEach(function(b){ b.className = b.getAttribute('data-t') === pick.time ? 'on' : ''; b.onclick = function(){ pick.time = b.getAttribute('data-t'); $('#d12-tval').value = pick.time; $$('#d12-time button').forEach(function(x){ x.className = x === b ? 'on' : ''; }); renderPact(); }; });
    $('#d12-tval').oninput = function(){ pick.time = this.value || '19:00'; $$('#d12-time button').forEach(function(x){ x.className = x.getAttribute('data-t') === pick.time ? 'on' : ''; }); renderPact(); };
    ['cue', 'bun'].forEach(function(k){ var x = $('#d12-' + k + '-x');
      $$('#d12-' + k + ' button').forEach(function(b){ b.className = lc(b.textContent) === pick[k] ? 'on' : ''; b.onclick = function(){ var on = b.className !== 'on'; $$('#d12-' + k + ' button').forEach(function(y){ y.className = ''; }); b.className = on ? 'on' : ''; pick[k] = on ? lc(b.textContent) : ''; x.value = ''; renderPact(); }; });
      x.value = ($$('#d12-' + k + ' button.on').length || !pick[k]) ? '' : pick[k];
      x.oninput = function(){ $$('#d12-' + k + ' button').forEach(function(y){ y.className = ''; }); pick[k] = lc(x.value); renderPact(); }; });
    renderPact();
  }
  function pactHTML(p){
    var ds = p.days.slice().sort(function(a, b){ return wd.indexOf(a) - wd.indexOf(b); }).map(function(d){ return dayName(d); }).join(' ' + txt(S.and) + ' ');
    var h = fill(S.pact, {days: ds, time: p.time, cue: p.cue || '…'});
    if (p.bun) h += ' ' + fill(S.bun, {b: /^\s*<b/.test(S.bun) ? p.bun.charAt(0).toLocaleUpperCase(LANG) + p.bun.slice(1) : p.bun});
    return h;
  }
  function renderPact(){ var el = $('#d12-pact'), ok = pick.days.length === 2 && !!pick.cue;
    el.className = 'pact' + (pick.days.length ? '' : ' empty'); el.innerHTML = pick.days.length ? pactHTML(pick) : S.pact0;
    $('[data-act="pact"]').disabled = !ok; }

  /* ---- ses, titreşim, ekranın kapanmaması */
  var AC = null, WL = null;
  function beep(f, d, v){ try { if (!AC) AC = new (window.AudioContext || window.webkitAudioContext)(); var o = AC.createOscillator(), g = AC.createGain(), t = AC.currentTime;
    o.type = 'sine'; o.frequency.value = f || 880; g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(v || .2, t + .015); g.gain.exponentialRampToValueAtTime(.0001, t + (d || .16));
    o.connect(g); g.connect(AC.destination); o.start(t); o.stop(t + (d || .16) + .03); } catch (e) {} }
  function say(n){ if (!st.voice || !('speechSynthesis' in window)) return; try { speechSynthesis.cancel(); var u = new SpeechSynthesisUtterance(String(n)); u.lang = LANG; u.rate = 1.05; speechSynthesis.speak(u); } catch (e) {} }
  function buzz(p){ try { if (navigator.vibrate) navigator.vibrate(p); } catch (e) {} }
  function wake(on){ try { if (on && navigator.wakeLock) navigator.wakeLock.request('screen').then(function(l){ WL = l; }, function(){}); else if (!on && WL) { WL.release(); WL = null; } } catch (e) {} }

  /* ---- program */
  var CH = [
    [{k: 'quad', r: 8, h: 5, side: 2}, {k: 'kext', r: 10, h: 3, side: 2}, {k: 'slr', r: 10, side: 2}, {k: 'sts', r: 8}],
    [{k: 'kext', r: 12, h: 5, side: 2}, {k: 'sts', r: 10}, {k: 'abd', r: 10, side: 2}, {k: 'wall', r: 8, h: 3}],
    [{k: 'sts', r: 12, slow: 1}, {k: 'wall', r: 10, h: 5}, {k: 'abd', r: 12, side: 2}, {k: 'slr', r: 12, side: 2}]
  ];
  function plan(n){ return CH[Math.floor((n - 1) / 4)].map(function(x){ var y = {}; for (var k in x) y[k] = x[k]; y.r = Math.max(5, Math.min(x.r + 4, x.r + st.adj)); return y; }); }
  function exData(k){ var e = $('.d12-ex [data-ex="' + k + '"]'); return {nm: $('.nm', e).textContent, how: $('.how', e).textContent, p1: $('.p1', e).textContent, p2: $('.p2', e).textContent, fig: $('figure', e).outerHTML}; }
  function secret(n){ var a = $('.d12-secrets [data-n="' + n + '"]'); return {q: $('h3', a).innerHTML, a: $('.a', a).innerHTML, src: $('.src', a).innerHTML}; }
  function nextN(){ return st.done.length + 1; }

  /* ---- harita */
  function weekCount(){ var now = new Date(), d = (now.getDay() + 6) % 7, m = new Date(now.getFullYear(), now.getMonth(), now.getDate() - d);
    return st.done.filter(function(x){ return new Date(x.d) >= m; }).length; }
  function nextDate(){ if (!st.plan) return ''; var now = new Date(), best = null;
    for (var i = 1; i <= 8 && !best; i++) { var c = new Date(now.getFullYear(), now.getMonth(), now.getDate() + i); if (st.plan.days.indexOf(c.getDay()) >= 0) best = c; }
    return best ? dayName(best.getDay()) + ' ' + st.plan.time : ''; }
  function renderMap(){
    var n = nextN(), nx = $('#d12-next');
    if (n <= 12) { var sc = secret(n);
      nx.className = 'next'; nx.innerHTML = '<div class="nl">' + $('.lk', R).outerHTML + '</div><p class="k">' + S.nx_k + '</p><h3>' + sc.q + '</h3><p class="m">' + fill(S.nx_m, {n: n}) + '</p><button type="button" class="cta" data-act="start">' + S.nx_go + '</button>';
    } else { nx.className = 'next done'; nx.innerHTML = '<p class="k">' + S.nx_k + '</p><h3>' + S.nx_done + '</h3>'; }
    var w = Math.min(2, weekCount()); $('#d12-wk').innerHTML = fill(S.wk, {a: w}); $('.week .wv').style.strokeDashoffset = 113.1 * (1 - w / 2);
    $('#d12-pact2').innerHTML = st.plan ? pactHTML(st.plan) : '';
    $('#d12-wa').href = 'https://wa.me/?text=' + encodeURIComponent(txt(fill(S.wa, {p: st.plan ? txt(pactHTML(st.plan)) : ''})));
    var last = st.done.length ? new Date(st.done[st.done.length - 1].d) : null;
    $('#d12-fresh').hidden = !(last && (Date.now() - last) > 7 * 864e5 && n <= 12);
    $$('.tile').forEach(function(t){ var k = +t.getAttribute('data-n'); t.className = 'tile' + (k < n ? ' open' : k === n ? ' cur' : '');
      t.onclick = k < n ? function(){ reveal(k, true); } : null; t.setAttribute('aria-disabled', k < n ? 'false' : 'true'); });
    var T = st.tests, mx = Math.max(10, T.base || 0, T.mid || 0, T.final || 0);
    $('#d12-tests').innerHTML = '<h3>' + S.t_h + '</h3><div class="bars">' + ['base', 'mid', 'final'].map(function(k){ var v = T[k];
      return '<div class="bar' + (v == null ? ' none' : '') + '"><b>' + (v == null ? '–' : v) + '</b><i style="height:' + (v == null ? 4 : Math.max(6, 100 * v / mx)) + '%"></i><span>' + S['t_' + k] + '</span></div>'; }).join('') + '</div>';
    show('map');
  }

  /* ---- 30 saniye ölçümü */
  function testUI(box, mode, done){
    var v = st.tests[mode] != null ? st.tests[mode] : (st.tests.base != null ? st.tests.base : 10), timer = null;
    box.innerHTML = '<p class="eyebrow">' + S['test_' + mode] + '</p><h2>' + S.test_q + '</h2>' + $('.d12-testhow').innerHTML +
      '<div class="ring2"><svg viewBox="0 0 120 120"><circle class="bg" cx="60" cy="60" r="50"/><circle class="fg" cx="60" cy="60" r="50"/></svg><div class="c"><b>30</b><em></em></div></div>' +
      '<div class="center"><button type="button" class="cta" data-t="go">' + S.t_go + '</button></div>' +
      '<div class="cnt" hidden><p class="center soft">' + S.t_end + '</p><div class="step"><button type="button" data-d="-1" aria-label="−">−</button><b>' + v + '</b><button type="button" data-d="1" aria-label="+">+</button></div>' +
      '<div class="btns" style="justify-content:center;margin-top:12px"><button type="button" class="cta" data-t="save">' + S.t_save + '</button></div></div>' +
      '<p class="center"><button type="button" class="lnk" data-t="skip">' + S.t_skip + '</button></p>';
    var fg = $('.fg', box), num = $('.c b', box), em = $('.c em', box);
    function ring(p){ fg.style.strokeDashoffset = 314.16 * (1 - p); }
    $('[data-t="go"]', box).onclick = function(){ var b = this; b.disabled = true; var c = 3; em.innerHTML = S.t_ready; num.textContent = c; beep(660, .12);
      timer = setInterval(function(){ c--; if (c > 0) { num.textContent = c; beep(660, .12); return; }
        clearInterval(timer); beep(990, .35, .3); buzz(200); em.innerHTML = S.t_run; var t0 = Date.now();
        timer = setInterval(function(){ var e = (Date.now() - t0) / 1000, left = Math.max(0, 30 - e); num.textContent = Math.ceil(left); ring(e / 30);
          if (left <= 0) { clearInterval(timer); beep(990, .5, .3); setTimeout(function(){ beep(990, .5, .3); }, 300); buzz([200, 100, 200]); em.innerHTML = ''; b.parentNode.hidden = true; $('.cnt', box).hidden = false; } }, 100);
      }, 1000); };
    $$('.step button', box).forEach(function(b){ b.onclick = function(){ v = Math.max(0, Math.min(60, v + (+b.getAttribute('data-d')))); $('.step b', box).textContent = v; }; });
    $('[data-t="save"]', box).onclick = function(){ clearInterval(timer); st.tests[mode] = v; save(); done(v); };
    $('[data-t="skip"]', box).onclick = function(){ clearInterval(timer); done(null); };
  }

  /* ---- seans oynatıcı */
  var OV = $('#d12-ov'), Q = [], qi = 0, run = null, curN = 0; document.body.appendChild(OV);
  var ICON_X = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>';
  var ICON_V = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 9v6h4l5 4V5L8 9z"/><path d="M16.5 8.5a5 5 0 0 1 0 7"/></svg>';
  function open(){ OV.hidden = false; document.documentElement.style.overflow = 'hidden'; wake(true); }
  function close(){ stop(); OV.hidden = true; OV.innerHTML = ''; document.documentElement.style.overflow = ''; wake(false); try { speechSynthesis.cancel(); } catch (e) {} }
  function stop(){ if (run) { clearInterval(run.iv); run = null; } }
  function build(n){ var ex = plan(n), L = [{t: 'warm', s: 60}];
    ex.forEach(function(x, i){ for (var s = 1; s <= 2; s++) { var sides = x.side === 2 ? [1, 2] : [0];
      sides.forEach(function(sd, j){ L.push({t: 'work', x: x, i: i, s: s, sd: sd, m: ex.length});
        var last = i === ex.length - 1 && s === 2 && j === sides.length - 1; if (!last) L.push({t: 'rest', s: j < sides.length - 1 ? 12 : 30, side: j < sides.length - 1}); }); } });
    L.push({t: 'end'}); return L; }
  function top(){ var works = Q.filter(function(q){ return q.t === 'work'; }), cur = Q[qi];
    var segs = works.map(function(w){ var k = Q.indexOf(w); return '<i class="' + (k < qi ? 'd' : k === qi ? 'c' : '') + '"></i>'; }).join('');
    return '<div class="top"><button type="button" class="ib" data-o="quit" aria-label="' + txt(S.quit) + '">' + ICON_X + '</button><div class="segs">' + segs + '</div><button type="button" class="ib' + (st.voice ? '' : ' off') + '" data-o="voice" aria-label="' + txt(S.voice) + '" aria-pressed="' + st.voice + '">' + ICON_V + '</button></div>'; }
  function bindTop(){ $('[data-o="quit"]', OV).onclick = function(){ if (confirm(txt(S.quit_q))) { close(); renderMap(); } };
    $('[data-o="voice"]', OV).onclick = function(){ st.voice = !st.voice; save(); this.className = 'ib' + (st.voice ? '' : ' off'); this.setAttribute('aria-pressed', st.voice); }; }
  function ringHTML(big, small, em){ return '<div class="ring2"><svg viewBox="0 0 120 120"><circle class="bg" cx="60" cy="60" r="50"/><circle class="fg" cx="60" cy="60" r="50"/></svg><div class="c"><b>' + big + '</b><small>' + (small || '') + '</small><em>' + (em || '') + '</em></div></div>'; }
  function setRing(p){ var f = $('.fg', OV); if (f) f.style.strokeDashoffset = 314.16 * (1 - Math.max(0, Math.min(1, p))); }
  function lockPct(){ var w = Q.filter(function(q){ return q.t === 'work'; }), d = w.filter(function(q){ return Q.indexOf(q) < qi; }).length; return Math.round(100 * d / w.length); }
  function step(){ stop(); var q = Q[qi]; if (!q) return;
    if (q.t === 'warm' || q.t === 'rest') return timed(q);
    if (q.t === 'work') return work(q);
    if (q.t === 'end') return end(); }
  function next(){ qi++; step(); OV.scrollTop = 0; }
  function timed(q){ var sc = secret(curN), title = q.t === 'warm' ? S.warm : (q.side ? S.rest_side : S.rest);
    OV.innerHTML = '<div class="in">' + top() + '<div class="rest"><p class="meta">' + (q.t === 'warm' ? '' : S.lockp + ' · %' + lockPct()) + '</p><h2>' + title + '</h2>' + (q.t === 'warm' ? '<p class="dose">' + S.warm_s + '</p>' : '') +
      ringHTML(q.s, '', '') + (q.t === 'rest' ? '<div class="tease"><p class="k">' + S.this_s + '</p><p class="qq">' + sc.q + '</p><div class="lbar"><i style="width:' + lockPct() + '%"></i></div></div>' : '') +
      '<div class="btns"><button type="button" class="cta ghost" data-o="skip">' + S.skip + '</button></div></div></div>';
    bindTop(); $('[data-o="skip"]', OV).onclick = next;
    var t0 = Date.now(), last = q.s;
    run = {iv: setInterval(function(){ var e = (Date.now() - t0) / 1000, left = Math.max(0, q.s - e), c = Math.ceil(left); setRing(e / q.s);
      if (c !== last) { last = c; $('.c b', OV).textContent = c; if (c <= 3 && c > 0) beep(660, .1, .14); }
      if (left <= 0) { beep(990, .25, .22); next(); } }, 100)};
  }
  function work(q){ var x = q.x, d = exData(x.k), dose = x.h ? fill(S.dose_h, {r: x.r, h: x.h}) : fill(S.dose_r, {r: x.r});
    var side = q.sd === 1 ? S.right : q.sd === 2 ? S.left : '';
    OV.innerHTML = '<div class="in">' + top() + '<p class="meta">' + fill(S.mv, {i: x === undefined ? 1 : q.i + 1, m: q.m, s: q.s}) + (side ? ' · ' + side : '') + '</p><h2>' + d.nm + '</h2><p class="dose">' + dose + (x.slow ? ' · ' + S.slow : '') + '</p>' +
      '<div class="fig">' + d.fig + ringHTML(0, '/ ' + x.r, '') + '</div>' +
      '<div class="btns"><button type="button" class="cta" data-o="go">' + S.go + '</button><button type="button" class="cta ghost" data-o="plus">' + S.plus + '</button><button type="button" class="cta ghost" data-o="next">' + S.next + '</button></div>' +
      '<details><summary>' + S.howq + '</summary><p>' + d.how + '</p></details></div>';
    bindTop();
    var rep = 0, ph = [], pi = 0, pEnd = 0, rStart = 0, playing = false, num = $('.c b', OV), em = $('.c em', OV);
    var seq = [[d.p1, 2]]; if (x.h) seq.push([S.hold, x.h]); seq.push([d.p2, x.slow ? 3 : 2]);
    var repDur = seq.reduce(function(a, s){ return a + s[1]; }, 0);
    function label(){ var s = seq[pi]; em.textContent = s ? (s[0] === S.hold ? txt(S.hold) + ' ' + Math.max(1, Math.ceil((pEnd - Date.now()) / 1000)) : txt(s[0])) : ''; }
    function done(){ pause(); em.textContent = ''; beep(880, .14); setTimeout(function(){ beep(1175, .2, .25); }, 160); buzz([60, 60, 120]); setTimeout(next, 1300); }
    function addRep(){ rep++; num.textContent = rep; beep(784, .12); say(rep); buzz(40); setRing(rep / x.r); if (rep >= x.r) { done(); return true; } return false; }
    function startPhase(i){ pi = i; pEnd = Date.now() + seq[i][1] * 1000; if (i === 0) rStart = Date.now(); label(); }
    function tick(){ if (!playing) return; var now = Date.now(); setRing((rep + Math.min(1, (now - rStart) / (repDur * 1000))) / x.r); label();
      if (now >= pEnd) { if (pi < seq.length - 1) { startPhase(pi + 1); if (seq[pi][0] === S.hold) beep(523, .1, .12); } else { if (!addRep()) startPhase(0); } } }
    function play(){ playing = true; $('[data-o="go"]', OV).innerHTML = S.pause; startPhase(0); run = {iv: setInterval(tick, 80)}; }
    function pause(){ playing = false; stop(); var g = $('[data-o="go"]', OV); if (g) g.innerHTML = S.go; em.textContent = ''; }
    $('[data-o="go"]', OV).onclick = function(){ if (!AC) beep(440, .01, .001); if (playing) pause(); else play(); };
    $('[data-o="plus"]', OV).onclick = function(){ if (!addRep() && playing) startPhase(0); };
    $('[data-o="next"]', OV).onclick = function(){ pause(); next(); };
  }
  function end(){ var p = 0, e = 2;
    OV.innerHTML = '<div class="in">' + top() + '<p class="meta">' + fill(S.sec_k, {n: curN}) + '</p><h2>' + S.end_h + '</h2>' +
      '<div class="pain"><p class="dose">' + S.end_p + '</p><div class="pv"><b>0</b><div class="light"><i></i><i></i><i></i></div></div><input type="range" min="0" max="10" step="1" value="0" aria-label="' + txt(S.end_p) + '"><p class="pmsg"></p></div>' +
      '<p class="dose">' + S.eff + '</p><div class="chips"><button type="button" data-e="1">' + S.e1 + '</button><button type="button" data-e="2" class="on">' + S.e2 + '</button><button type="button" data-e="3">' + S.e3 + '</button></div>' +
      '<div class="btns"><button type="button" class="cta" data-o="open">' + S.open + '</button></div></div>';
    bindTop();
    var rg = $('input[type=range]', OV); function paint(){ p = +rg.value; $('.pv b', OV).textContent = p; var c = p <= 2 ? 'g' : p <= 5 ? 'y' : 'r'; $('.light', OV).className = 'light ' + c; $('.pmsg', OV).innerHTML = S['pain_' + c]; }
    rg.oninput = paint; paint();
    $$('[data-e]', OV).forEach(function(b){ b.onclick = function(){ e = +b.getAttribute('data-e'); $$('[data-e]', OV).forEach(function(y){ y.className = y === b ? 'on' : ''; }); }; });
    $('[data-o="open"]', OV).onclick = function(){ finish(p, e); };
  }
  function finish(p, e){
    st.done.push({n: curN, d: new Date().toISOString(), p: p, e: e});
    if (p >= 6) st.adj = Math.max(-3, st.adj - 2); else if (p <= 2 && e === 1) st.adj = Math.min(4, st.adj + 2); else if (e === 3) st.adj = Math.max(-3, st.adj - 1);
    save();
    if (curN === 6 || curN === 12) { var mode = curN === 6 ? 'mid' : 'final';
      OV.innerHTML = '<div class="in"><div class="d12-test" id="d12-test1"></div></div>'; OV.scrollTop = 0;
      testUI($('#d12-test1', OV), mode, function(){ reveal(curN, false); }); return; }
    reveal(curN, false);
  }
  function reveal(n, ro){ stop(); open(); var sc = secret(n);
    var burst = ''; for (var i = 0; i < 14; i++) burst += '<i style="--a:' + (i * 360 / 14) + 'deg"></i>';
    var tease = '';
    if (n < 12) { var nq = secret(n + 1); tease = '<div class="tease"><p class="k">' + fill(S.teaser, {n: n + 1}) + '</p><p class="qq">' + nq.q + '</p>' + (st.plan && !ro ? '<p class="when">' + fill(S.when, {d: nextDate()}) + '</p>' : '') + '</div>'; }
    OV.innerHTML = '<div class="in"><div class="top"><span style="flex:1"></span><button type="button" class="ib" data-o="x" aria-label="' + txt(S.close) + '">' + ICON_X + '</button></div>' +
      '<div class="rv' + (ro ? ' ro' : '') + '">' + (ro ? '' : '<div class="big">' + $('.lk', R).outerHTML + '<div class="burst">' + burst + '</div></div>') +
      '<div class="card"><p class="k">' + fill(S.sec_k, {n: n}) + '</p><h3>' + sc.q + '</h3><div class="a">' + sc.a + '</div><p class="src">' + sc.src + '</p></div>' + tease +
      '<div class="btns"><button type="button" class="cta" data-o="back">' + S.back + '</button></div></div></div>';
    var T = st.tests, b = n === 6 ? T.mid : T.final, a = T.base, cs = 'none';
    if (n === 6 || n === 12) { if (a != null && b != null) cs = b > a ? 'up' : b === a ? 'same' : 'down';
      $$('.card [data-case]', OV).forEach(function(p){ p.classList.toggle('show', p.getAttribute('data-case') === cs); });
      $$('.card [data-v]', OV).forEach(function(s){ var k = s.getAttribute('data-v'); s.textContent = k === 'a' ? a : k === 'b' ? b : (b - a); }); }
    OV.scrollTop = 0;
    $('[data-o="x"]', OV).onclick = $('[data-o="back"]', OV).onclick = function(){ close(); renderMap(); };
    if (!ro) { requestAnimationFrame(function(){ requestAnimationFrame(function(){ $('.rv', OV).classList.add('go'); }); }); setTimeout(function(){ beep(1046, .18, .2); setTimeout(function(){ beep(1318, .3, .22); }, 140); buzz([30, 40, 80]); }, 900); }
  }
  function start(){ curN = nextN(); if (curN > 12) return; Q = build(curN); qi = 0; open(); step(); }

  /* ---- takvim dosyası */
  function ics(){ if (!st.plan) return; var p = st.plan, BY = ['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA'], now = new Date(), first = null;
    for (var i = 0; i < 8 && !first; i++) { var c = new Date(now.getFullYear(), now.getMonth(), now.getDate() + i); if (p.days.indexOf(c.getDay()) >= 0) first = c; }
    var hm = (p.time || '19:00').split(':'), pad = function(v){ return (v < 10 ? '0' : '') + v; };
    var ds = first.getFullYear() + pad(first.getMonth() + 1) + pad(first.getDate()) + 'T' + pad(+hm[0]) + pad(+hm[1]) + '00';
    var stamp = new Date().toISOString().replace(/[-:]/g, '').replace(/\.\d+/, '');
    var esc = function(s){ return s.replace(/([,;\\])/g, '\\$1'); };
    var body = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//drihsaneren.com//d12//' + (EN ? 'EN' : 'TR'), 'BEGIN:VEVENT', 'UID:d12-' + Date.now() + '@drihsaneren.com', 'DTSTAMP:' + stamp, 'DTSTART:' + ds, 'DURATION:PT15M',
      'RRULE:FREQ=WEEKLY;BYDAY=' + p.days.map(function(d){ return BY[d]; }).join(',') + ';COUNT=' + Math.max(1, 12 - st.done.length),
      'SUMMARY:' + esc(txt(S.ics_t)), 'DESCRIPTION:' + esc(txt(pactHTML(p))) + ' ' + location.href.split('#')[0],
      'BEGIN:VALARM', 'TRIGGER:-PT10M', 'ACTION:DISPLAY', 'DESCRIPTION:' + esc(txt(S.ics_t)), 'END:VALARM', 'END:VEVENT', 'END:VCALENDAR'].join('\r\n');
    var a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([body], {type: 'text/calendar;charset=utf-8'})); a.download = 'dizin-12-sirri.ics'; document.body.appendChild(a); a.click(); setTimeout(function(){ URL.revokeObjectURL(a.href); a.remove(); }, 1500); }

  /* ---- düğmeler */
  R.addEventListener('click', function(ev){ var b = ev.target.closest('[data-act]'); if (!b || b.disabled) return; var a = b.getAttribute('data-act');
    if (a === 'begin') { initPlan(); show('plan'); R.scrollIntoView({behavior: 'smooth', block: 'start'}); }
    if (a === 'pact') { st.plan = {days: pick.days.slice(), time: pick.time, cue: pick.cue, bun: pick.bun}; save();
      if (st.tests.base == null && !st.skipBase) { show('test'); R.scrollIntoView({behavior: 'smooth', block: 'start'}); testUI($('#d12-test0'), 'base', function(v){ if (v == null) { st.skipBase = 1; save(); } renderMap(); R.scrollIntoView({behavior: 'smooth', block: 'start'}); }); }
      else renderMap(); }
    if (a === 'edit') { initPlan(); show('plan'); }
    if (a === 'start') start();
    if (a === 'ics') ics();
    if (a === 'reset' && confirm(txt(S.reset_q))) { try { localStorage.removeItem(KEY); } catch (e) {} load(); pick = {days: [], time: '19:00', cue: '', bun: ''}; show('intro'); }
  });
  if (st.plan) renderMap(); else show('intro');
})();
</script>'''

page("dizin-12-sirri.html", "Dizin 12 Sırrı",
     "Diz kireçlenmesi için 6 haftalık etkileşimli ev egzersiz programı: söz kartı, sesli sayan seans oynatıcı, ağrı trafik ışığı, 30 saniye ölçümü ve her seansta açılan bir sır.",
     "dizin-12-sirri.html", D12_CSS, D12_BODY, D12_JS,
     seo_title="Dizin 12 Sırrı: Diz Kireçlenmesi İçin 6 Haftalık Ev Egzersiz Programı | İhsan Eren",
     about={"@type": "ExercisePlan", "name": "Dizin 12 Sırrı"}, faq_items=D12_FAQ)

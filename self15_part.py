# -*- coding: utf-8 -*-
# Kendine iyi bak, 15. tur: sakatlanmayı önleyen ısınma ve adım hedefi planlayıcısı. cond72_part.py'den sonra exec edilir (SELF14_CSS, WAKE_JS hazır).
# Kaynaklar (24 Ekim 2026'da okundu): Thorborg 2017 BJSM (özet), Soligard 2008 BMJ (PEDro), van Dyk 2019 BJSM (özet), WakeMed FIFA 11+ el kitapçığı (dozlar), Physiopedia FIFA 11+ (yapı),
# Football West FIFA 11+ Referee el kitabı (ilerleme kuralı); Ding 2025 Lancet Public Health (Epocrates), Paluch 2022 Lancet Public Health (Hospital Healthcare Europe),
# Banach 2023 EJPC (Community Practitioner), Ekelund 2026 Lancet (EurekAlert), Bull 2020 DSÖ kılavuzu.
import json as _json

SELF15_CSS = SELF14_CSS + """
  .is-ex[hidden]{display:none}
  .is-part{font-size:12.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--foil);margin:0 0 6px}
  .is-next{font-size:13.5px;color:var(--muted);margin:8px 0 0;text-align:center}
  .ah-in{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:8px;align-items:end;margin-top:10px}
  .ah-in label{display:block;font-size:12.5px;color:var(--muted);margin-bottom:4px}
  .ah-in input{width:100%;box-sizing:border-box;padding:10px 10px;border-radius:12px;border:1px solid var(--line-strong);background:rgba(236,229,207,.04);color:var(--ink);font:inherit;font-size:16px}
  .ah-big{font-family:var(--display);font-size:clamp(40px,7vw,56px);line-height:1;color:var(--ink);font-variant-numeric:tabular-nums;margin:6px 0 0}
  .ah-big small{font-family:var(--body,inherit);font-size:14px;color:var(--muted);margin-left:6px}
  .ah-plan{list-style:none;margin:12px 0 0;padding:0;display:grid;gap:6px}
  .ah-plan li{display:flex;justify-content:space-between;gap:10px;border-bottom:1px solid var(--line);padding:6px 0;font-size:14.5px;color:var(--ink-soft)}
  .ah-plan li b{color:var(--ink);font-variant-numeric:tabular-nums}
  .ah-bars{display:grid;gap:6px;margin-top:10px}
  .ah-bar{display:grid;grid-template-columns:5.5em minmax(0,1fr) 4.2em;gap:8px;align-items:center;font-size:13px;color:var(--muted)}
  .ah-bar i{display:block;height:10px;border-radius:6px;background:rgba(143,164,118,.75)}
  .ah-bar i.hit{background:var(--foil)}
  .ah-bar b{color:var(--ink-soft);text-align:right;font-variant-numeric:tabular-nums;font-weight:500}
"""

SV["plank"] = fig(GRD +
    '<path class="fig" d="M20 110 L36 110 M32 110 L32 92"/>'
    '<circle class="hd" cx="22" cy="86" r="7.5"/>'
    f'<path class="fig hl" d="M32 92 L66 99 L100 108">{anim_d("M32 92 L66 99 L100 108;M32 92 L66 95 L100 108;M32 92 L66 99 L100 108")}</path>',
    "Dirsekler üzerinde plank")
SV["squat"] = fig(GRD +
    f'<circle class="hd" cx="60" cy="22" r="8"><animate attributeName="cy" values="22;40;22" {A}/><animate attributeName="cx" values="60;54;60" {A}/></circle>'
    f'<path class="fig" d="M60 32 L60 64">{anim_d("M60 32 L60 64;M54 50 L48 79;M60 32 L60 64")}</path>'
    f'<path class="fig hl" d="M60 64 L60 88 L60 110">{anim_d("M60 64 L60 88 L60 110;M48 79 L68 92 L60 110;M60 64 L60 88 L60 110")}</path>'
    f'<path class="fig" d="M60 40 L72 54">{anim_d("M60 40 L72 54;M54 57 L76 60;M60 40 L72 54")}</path>',
    "Çömelme")

# ------------------------------------------------------------------ 1 · SAKATLANMAYI ÖNLEYEN ISINMA
_ex2("is_run", "walk", "Düz koşu", "Yaklaşık 30 metre arayla iki işaret koyun. Rahat bir tempoda gidip gelin; dizlerinizin içe kaçmamasına, ayağınızın üzerine yumuşak basmaya dikkat edin.", "")
_ex2("is_out", "walk", "Koşarken kalçayı dışa açma", "Yavaş koşun; birkaç adımda bir durup bir dizinizi öne kaldırın ve yana doğru açın, sonra koşuya devam edin. Bacakları değiştirin.", "")
_ex2("is_in", "walk", "Koşarken kalçayı içe kapama", "Yavaş koşun; birkaç adımda bir durup bir dizinizi yandan kaldırın ve öne doğru kapatın, sonra koşuya devam edin. Bacakları değiştirin.", "")
_ex2("is_circ", "sidestep", "Yan adımlarla daire çizme", "Bir arkadaşınızla karşılıklı durun. Yan adımlarla birbirinizin etrafında küçük bir daire çizin, sonra yer değiştirip yön değiştirin. Dizlerinizi hafif bükük tutun.", "")
_ex2("is_jmp", "walk", "Yana sıçrayıp yumuşak inme", "Yavaş koşun; birkaç adımda bir yana doğru sıçrayın ve iki ayağınızın üzerine, dizleriniz hafif bükük ve içe kaçmadan, yumuşakça inin.", "")
_ex2("is_fb", "walk", "İleri-geri kısa koşular", "İki işaret arasında hızlıca ileri koşun, sonra küçük adımlarla geri geri dönün. Kalçanızı ve dizinizi hafif bükük tutun.", "")
_ex2("is_plank", "plank", "Dirsekler üzerinde plank", "Yüzüstü, dirsekleriniz omuzlarınızın altında olacak şekilde ön kollarınız ve ayak parmaklarınız üzerinde yükselin. Başınızdan topuklarınıza kadar vücudunuz düz bir çizgi olsun; kalçanızı düşürmeyin.", "")
_ex2("is_side", "sideplank", "Yan plank", "Yan yatın, dirseğiniz omzunuzun altında olsun. Kalçanızı kaldırarak omzunuzdan dizinize (kolaylaştıkça ayağınıza) kadar düz bir çizgi oluşturun ve tutun.", "")
_ex2("is_nord", "hs_nordic", "Nordic hamstring", "Dizlerinizin üzerine çökün; bir arkadaşınız ayak bileklerinizi yere bastırsın. Gövdeniz ve kalçanız düz kalacak şekilde yavaşça öne doğru eğilin, uyluk arka kaslarınızla olabildiğince uzun süre direnin, sonra ellerinizle yere düşüşünüzü karşılayın.", "")
_ex2("is_sls", "sls", "Tek ayak üzerinde durma", "Tek ayağınızın üzerinde, diziniz hafif bükük durun. Bir topu iki elinizle tutun ya da bir arkadaşınızla atıp tutun. Dizinizi ayak parmaklarınızın üzerinde tutun, içe kaçırmayın.", "")
_ex2("is_sq", "squat", "Çömelip parmak ucunda yükselme", "Ayaklarınız kalça genişliğinde, kalçanızdan ve dizlerinizden bükülerek yavaşça çömelin; dizleriniz içe kaçmasın. Doğrulurken parmak uçlarınızda yükselin ve yavaşça inin.", "")
_ex2("is_vj", "squat", "Dikey sıçrama", "Hafifçe çömelip olabildiğince yükseğe sıçrayın; dizleriniz hafif bükük ve ayak parmaklarınızın üzerinde olacak şekilde, iki ayağınızla yumuşakça inin.", "")
_ex2("is_acr", "walk", "Saha boyunca koşu", "Sahanın bir yanından diğer yanına, en yüksek hızınızın yaklaşık %75–80'i ile koşun; dönüşte yavaş koşarak dinlenin.", "")
_ex2("is_bnd", "walk", "Sekerek koşu", "Dizinizi yukarı kaldırarak uzun, sekmeli adımlarla koşun; her inişte dizinizi bükerek ayağınızın ön tarafına yumuşakça basın.", "")
_ex2("is_cut", "sidestep", "Ani yön değiştirme", "Birkaç adım koşun, dış bacağınızı yere sağlamca basıp ani yön değiştirin ve en yüksek hızınızın yaklaşık %80–90'ı ile depar atın. Diziniz içe kaçmasın.", "")

# Her hareketin bölüm, hareket ve zamanlama planı: (anahtar, bölüm, dilimler)
# dilim: (tür, saniye, set no). Türler: run, hold, rest, sr, sl, sw, lr, ll, work, reps
def _sets(kind, sec, n, rest):
    out = []
    for i in range(1, n + 1):
        out.append((kind, sec, i))
        if i < n:
            out.append(("rest", rest, 0))
    return out

def _sides(a, b, sec, n, sw):
    out = []
    for i in range(1, n + 1):
        out += [(a, sec, i), ("sw", sw, 0), (b, sec, i)]
        if i < n:
            out.append(("sw", sw, 0))
    return out

IS_PLAN = [
    ("is_run", 1, [("run", 80, 0)]), ("is_out", 1, [("run", 80, 0)]), ("is_in", 1, [("run", 80, 0)]),
    ("is_circ", 1, [("run", 80, 0)]), ("is_jmp", 1, [("run", 80, 0)]), ("is_fb", 1, [("run", 80, 0)]),
    ("is_plank", 2, _sets("hold", 25, 3, 15)),
    ("is_side", 2, _sides("sr", "sl", 25, 3, 8)),
    ("is_nord", 2, [("reps", 60, 0)]),
    ("is_sls", 2, _sides("lr", "ll", 30, 2, 5)),
    ("is_sq", 2, _sets("work", 30, 2, 20)),
    ("is_vj", 2, _sets("work", 30, 2, 20)),
    ("is_acr", 3, [("run", 40, 0)]), ("is_bnd", 3, [("run", 40, 0)]), ("is_cut", 3, [("run", 40, 0)]),
]
IS_STAGE = "\n".join(
    f'''            <div class="is-ex gu-step" data-i="{i}" data-part="{part}" data-plan='{_json.dumps([list(x) for x in plan])}'{" hidden" if i else ""}>
              {SV[k]}
              <div><p class="is-part">{part}. bölüm</p><h3>{EXT[k][0]}</h3><p>{EXT[k][1]}</p></div>
            </div>''' for i, (k, part, plan) in enumerate(IS_PLAN))

IS_FAQ = [
 ("Gerçekten işe yarıyor mu?", "Evet, özellikle düzenli yapıldığında. Amatör ve alt düzey futbolcularla yapılan 4 çalışmayı birleştiren bir meta-analizde bu ısınma programı sakatlanmaları %39, diz sakatlıklarını %48, uyluk arka kası sakatlıklarını %60 azalttı. Norveç'te 13–17 yaşındaki 1.892 kadın futbolcuyla yapılan çalışmada ağır sakatlanmalar %45 azaldı."),
 ("Ne sıklıkla yapmalıyım?", "Programın önerisi, her antrenmanın başında ve haftada en az 2 kez yapılmasıdır. Meta-analizdeki takımların yalnızca %13'ü bu sıklığa ulaşabildi; yani gerçek hayatta en zor kısım düzenli yapmak. Maç öncesinde yalnızca koşu bölümleri (1. ve 3. bölüm) yapılır."),
 ("Futbol oynamıyorum; bana da uygun mu?", "Program futbol için geliştirildi ve kanıtların çoğu futboldan geliyor. Ancak koşu, yön değiştirme, sıçrayıp inme ve uyluk arka kası egzersizi içeren yapısı basketbol, voleybol, hentbol gibi benzer hareketler gerektiren sporlarda da kullanılıyor. Programı kendi sporunuza uyarlamak için bir fizyoterapistten destek alabilirsiniz."),
 ("Nordic hamstring çok zor, ne yapmalıyım?", "Başta yalnızca birkaç tekrar yapın ve öne eğilmeyi kontrol edebildiğiniz kadar sürdürün. 15 çalışmayı ve 8.459 sporcuyu kapsayan bir meta-analizde, bu egzersizi içeren programlar uyluk arka kası sakatlıklarını yaklaşık yarı yarıya azalttı. İlk haftalarda uyluk arkasında gecikmiş kas ağrısı olağandır; tekrar sayısını yavaş artırın."),
 ("Ne zaman bir üst seviyeye geçmeliyim?", "Bir hareketi belirtilen süre ve tekrar sayısında zorlanmadan, doğru teknikle yapabildiğinizde. Program el kitabı, takımların genellikle 3–4 hafta sonra birlikte ilerleyebileceğini belirtiyor. Bu sayfa temel seviyeyi sayar; ileri seviyeler için antrenörünüz ya da fizyoterapistinizle çalışın."),
]

IS_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Sakatlanmayı önleyen ısınma</h1>
    <p class="lede">Futbolda sakatlanmaları azalttığı en iyi kanıtlanmış yöntemlerden biri, antrenmandan önce yapılan yaklaşık 20 dakikalık yapılandırılmış bir ısınmadır: koşu hareketleri, güç, denge ve sıçrama egzersizleri ve hızlı koşular. Bu sayfa, uluslararası futbol federasyonunun FIFA 11+ programından uyarlanmış 15 hareketi sırayla gösterir, süreleri sayar ve haftalık seanslarınızı kaydeder.</p>
    <p class="meta">Son güncelleme: 24 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>−%39</b><span>Program düzenli uygulandığında tüm sakatlanmalarda azalma (4 randomize çalışma)</span></div>
        <div class="stat"><b>−%51</b><span>Nordic hamstring egzersizi içeren programlarla uyluk arka kası sakatlıklarında azalma (15 çalışma)</span></div>
        <div class="stat"><b>~20 dk</b><span>Bir seansın süresi; maç öncesinde yalnızca koşu bölümleri</span></div>
        <div class="stat"><b>Haftada 2+</b><span>Önerilen en az seans sayısı</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Zamanlayıcıyla birlikte yapın</p>
      <h2>Isınmayı başlatın</h2>
      <p class="soft">Yaklaşık 30 metre arayla iki işaret koyun. Koşu hareketlerinde iki işaret arasında gidip gelin; zamanlayıcı her hareketin süresini, plank ve denge hareketlerinde setleri ve dinlenmeleri sayar. Nordic hamstring için bir arkadaşınızın ayak bileklerinizi tutması gerekir; tekrarları bitirince İleri'ye basın.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <p class="lbl">Seans türü</p>
            <div class="seg" role="group" aria-label="Seans türü" id="is-mode">
              <button type="button" data-v="full" aria-pressed="true">Antrenman öncesi</button>
              <button type="button" data-v="match" aria-pressed="false">Maç öncesi</button>
            </div>
            <p class="db-sup" id="is-info"></p>
            <label class="mz-chk"><input type="checkbox" id="is-sound" checked> Sesli uyarı</label>
            <p class="gd-week" id="is-week"></p>
            <div class="days7" id="is-days" aria-label="Son 7 gün"></div>
          </div>
          <div class="bt-out">
            <div class="gd-stage">
{IS_STAGE}
            </div>
            <div class="gu-dots" id="is-dots" aria-hidden="true"></div>
          </div>
          <div class="bt-run">
            <div class="yh-time"><b id="is-sec">–</b><span id="is-unit">saniye</span></div>
            <p class="bt-phase" id="is-phase" aria-live="polite">Hazır</p>
            <p class="bt-cue" id="is-cue">İşaretlerinizi koyun ve Başla'ya basın.</p>
            <button type="button" class="bt-tap" id="is-go">Başla</button>
            <p class="is-next" id="is-next"></p>
            <div class="controls" style="margin-top:10px;justify-content:center">
              <button type="button" class="cta ghost" id="is-prev">Geri</button>
              <button type="button" class="cta ghost" id="is-skip">Hareketi atla</button>
              <button type="button" class="cta ghost" id="is-reset">Sıfırla</button>
            </div>
          </div>
        </div>
        <div class="is-strings" hidden>
          <span data-k="full">15 hareket, yaklaşık 21 dakika: 6 koşu hareketi, 6 güç, denge ve sıçrama hareketi ve 3 hızlı koşu.</span>
          <span data-k="match">Maç öncesi: yalnızca 9 koşu hareketi, yaklaşık 10 dakika.</span>
          <span data-k="ready">Hazır</span>
          <span data-k="readyc">İşaretlerinizi koyun ve Başla'ya basın.</span>
          <span data-k="start">Başla</span>
          <span data-k="pause">Durdur</span>
          <span data-k="next">İleri</span>
          <span data-k="paused">Durduruldu</span>
          <span data-k="pausedc">Devam etmek için Başla'ya basın.</span>
          <span data-k="run">İki işaret arasında gidip gelin</span>
          <span data-k="runc">Dizleriniz içe kaçmasın, yumuşak basın.</span>
          <span data-k="hold">{{n}}. set: tutun</span>
          <span data-k="holdc">Vücudunuz düz bir çizgide; nefesinizi tutmayın.</span>
          <span data-k="sr">{{n}}. set: sağ taraf</span>
          <span data-k="sl">{{n}}. set: sol taraf</span>
          <span data-k="lr">{{n}}. set: sağ ayak</span>
          <span data-k="ll">{{n}}. set: sol ayak</span>
          <span data-k="sidec">Leğen kemiğinizi düz tutun.</span>
          <span data-k="work">{{n}}. set</span>
          <span data-k="workc">Kontrollü yapın; dizleriniz ayak parmaklarınızın üzerinde.</span>
          <span data-k="rest">Dinlenin</span>
          <span data-k="restc">Bir sonraki sete hazırlanın.</span>
          <span data-k="sw">Taraf değiştirin</span>
          <span data-k="swc">Hazırlanın.</span>
          <span data-k="reps">3–5 tekrar yapın</span>
          <span data-k="repsc">Bitince İleri'ye basın.</span>
          <span data-k="nextis">Sıradaki: {{t}}</span>
          <span data-k="done">Isınma tamam</span>
          <span data-k="donec">Haftada en az 2 seans hedefleyin; hareketler kolaylaşınca bir üst seviyeye geçin.</span>
          <span data-k="sec">saniye</span>
          <span data-k="week">Bu hafta: {{n}} seans · hedef en az 2</span>
          <span data-k="weekok">Bu hafta {{n}} seans yaptınız; haftalık hedefe ulaştınız.</span>
          <span data-k="d0">Pzt</span><span data-k="d1">Sal</span><span data-k="d2">Çar</span><span data-k="d3">Per</span><span data-k="d4">Cum</span><span data-k="d5">Cmt</span><span data-k="d6">Paz</span>
        </div>
      </div>
      <p class="count">Seanslarınız yalnızca bu cihazda saklanır; hiçbir yere gönderilmez.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Üç bölüm</h2>
        <ul class="tx">
          <li><b>1. bölüm (8 dk)</b><span>Yavaş tempoda koşu hareketleri: kalçayı açıp kapama, yan adımlar, sıçrayıp yumuşak inme ve ileri-geri kısa koşular.</span></li>
          <li><b>2. bölüm (10 dk)</b><span>Güç, denge ve sıçrama: plank, yan plank, Nordic hamstring, tek ayakta denge, çömelme ve sıçrama. Her hareketin zorlaşan üç seviyesi var; bu sayfa temel seviyeyi sayar.</span></li>
          <li><b>3. bölüm (2 dk)</b><span>Orta ve yüksek hızda koşular, sekerek koşu ve ani yön değiştirme.</span></li>
        </ul>
      </div>
      <div>
        <h2>Doğru teknik</h2>
        <ul class="dots">
          <li>Sıçrayıp inerken ve yön değiştirirken dizlerinizi içe kaçırmayın; dizleriniz ayak parmaklarınızın üzerinde olsun.</li>
          <li>İnişlerde dizlerinizi ve kalçanızı hafif bükerek ayağınızın ön tarafına yumuşakça basın.</li>
          <li>Plank ve yan plankta vücudunuzu düz bir çizgide tutun.</li>
          <li>Bir hareketi doğru teknikle zorlanmadan yapabildiğinizde bir üst seviyeye geçin.</li>
          <li>Ağrı, sakatlık ya da yakın zamanda geçirilmiş bir ameliyat varsa programı fizyoterapistinizle uyarlayın.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(IS_FAQ)}
      <p class="soft" style="margin-top:18px">Sakatlanma sonrası rehberler için <a href="on-capraz-bag.html">ön çapraz bağ yaralanması</a>, <a href="arka-uyluk-zorlanmasi.html">arka uyluk zorlanması</a> ve <a href="ayak-bilegi-burkulmasi.html">ayak bileği burkulması</a> sayfalarına bakabilirsiniz.</p>
      {CTA_CARD("Sakatlanmayı önleme ve sahaya dönüş", "sakatlanmayı önleyen ısınma ve sporcu değerlendirmesi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Thorborg K, Krommes KK, Esteve E, et al. " + ext("https://bjsm.bmj.com/content/51/7/562", "Effect of specific exercise-based football injury prevention programmes on the overall injury rate in football: a systematic review and meta-analysis of the FIFA 11 and 11+ programmes") + ". Br J Sports Med. 2017;51(7):562–571.",
        "Soligard T, Myklebust G, Steffen K, et al. " + ext("https://search.pedro.org.au/search-results/record-detail/22230", "Comprehensive warm-up programme to prevent injuries in young female footballers: cluster randomised controlled trial") + ". BMJ. 2008;337:a2469.",
        "van Dyk N, Behan FP, Whiteley R. " + ext("https://bjsm.bmj.com/content/53/21/1362", "Including the Nordic hamstring exercise in injury prevention programmes halves the rate of hamstring injuries: a systematic review and meta-analysis of 8459 athletes") + ". Br J Sports Med. 2019;53(21):1362–1370.",
        "WakeMed Health & Hospitals. " + ext("https://www.wakemed.org/sites/default/files/pdf/Ortho/fifa%20basic%20warm%20up%20exercises.pdf", "FIFA 11+ basic warm-up exercises") + " (bölüm süreleri ve temel seviye dozları).",
        "Physiopedia. " + ext("https://www.physio-pedia.com/The_F%C3%A9d%C3%A9ration_Internationale_de_Football_Association_FIFA_11%2B", "The Fédération Internationale de Football Association FIFA 11+") + ".",
        "FIFA Medical. " + ext("https://www.footballwest.com.au/sites/fw/files/2020-12/FIFA-11Ref-low-res.pdf", "The 11+ Referee: a complete warm-up programme") + " (ilerleme kuralı ve maç öncesi uygulama).",
      ])}
    </div>
  </section>
</main>'''

IS_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.is-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var $ = function(id){ return document.getElementById(id); }, KEY = 'drihsaneren.isinma.v1';
  var lock = null, ctx = null, snd = $('is-sound');
''' + WAKE_JS + '''
  var EX = [].slice.call(root.querySelectorAll('.is-ex'));
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function mode(){ return $('is-mode').querySelector('[aria-pressed="true"]').getAttribute('data-v'); }
  function title(i){ return EX[i].querySelector('h3').textContent; }
  function build(){
    var segs = [];
    EX.forEach(function(e, i){
      if (mode() === 'match' && e.getAttribute('data-part') === '2') return;
      JSON.parse(e.getAttribute('data-plan')).forEach(function(p){ segs.push({ex: i, k: p[0], sec: p[1], n: p[2]}); });
    });
    return segs;
  }
  function load(){ try { return JSON.parse(localStorage.getItem(KEY)) || {d: {}}; } catch (e) { return {d: {}}; } }
  function save(o){ try { localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {} }
  function dkey(d){ return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2); }
  function monday(d){ return new Date(d.getFullYear(), d.getMonth(), d.getDate() - ((d.getDay() + 6) % 7)); }
  function paintDays(){
    var o = load(), box = $('is-days'), now = new Date(); box.innerHTML = '';
    for (var i = 6; i >= 0; i--){
      var d = new Date(now.getFullYear(), now.getMonth(), now.getDate() - i), n = o.d[dkey(d)] || 0, el = document.createElement('div');
      el.innerHTML = '<b>' + n + '</b>' + S['d' + ((d.getDay() + 6) % 7)];
      if (n) el.classList.add('on'); if (!i) el.classList.add('now');
      box.appendChild(el);
    }
    var cur = monday(now), w = 0;
    Object.keys(o.d).forEach(function(k){ var p = k.split('-'), d = new Date(+p[0], +p[1] - 1, +p[2]); if (d >= cur) w += o.d[k]; });
    var el = $('is-week'); el.textContent = fill(w >= 2 ? S.weekok : S.week, {n: w}); el.classList.toggle('ok', w >= 2);
  }
  function info(){ $('is-info').textContent = S[mode()]; }
  var segs = build(), si = 0, stage = 'idle', left = 0, t0 = 0, iv = null, run = false, lastBeep = -1;
  function dots(){
    var box = $('is-dots'), seen = [], curEx = stage === 'idle' ? -1 : segs[si].ex; box.innerHTML = '';
    segs.forEach(function(s){ if (seen.indexOf(s.ex) < 0) seen.push(s.ex); });
    seen.forEach(function(ex){ var d = document.createElement('i'); if (stage === 'done' || (curEx >= 0 && seen.indexOf(ex) < seen.indexOf(curEx))) d.className = 'on'; box.appendChild(d); });
  }
  function show(ex){ EX.forEach(function(e, j){ e.hidden = j !== ex; }); }
  function setTime(v, unit){ $('is-sec').textContent = v; $('is-unit').textContent = unit; }
  function nextTitle(){
    for (var j = si + 1; j < segs.length; j++) if (segs[j].ex !== segs[si].ex) return title(segs[j].ex);
    return '';
  }
  function enter(i){
    si = i; var s = segs[i]; show(s.ex); clearInterval(iv); iv = null; lastBeep = -1;
    var lab = S[s.k], cue = S[s.k + 'c'] || (s.k === 'sr' || s.k === 'sl' ? S.holdc : (s.k === 'lr' || s.k === 'll' ? S.sidec : ''));
    $('is-phase').textContent = fill(lab, {n: s.n}); $('is-cue').textContent = cue;
    var nt = nextTitle(); $('is-next').textContent = nt ? fill(S.nextis, {t: nt}) : '';
    stage = s.k === 'reps' ? 'reps' : 'time'; left = s.sec; t0 = performance.now(); run = true;
    $('is-go').textContent = stage === 'reps' ? S.next : S.pause;
    beep(s.k === 'rest' || s.k === 'sw' ? 520 : 880, .3, .18);
    iv = setInterval(tick, 100); tick(); dots();
  }
  function tick(){
    var rem = left - (performance.now() - t0) / 1000, c = Math.ceil(rem);
    setTime(String(Math.max(0, c)), S.sec);
    if (c <= 3 && c >= 1 && c !== lastBeep && segs[si].k !== 'rest' && segs[si].k !== 'sw'){ lastBeep = c; beep(660, .08, .1); }
    if (rem > 0) return;
    advance();
  }
  function advance(){ if (si + 1 < segs.length) enter(si + 1); else finish(); }
  function finish(){
    clearInterval(iv); iv = null; run = false; stage = 'done'; wake(false); dots();
    beep(660, .2, .18); setTimeout(function(){ beep(880, .2, .18); }, 220); setTimeout(function(){ beep(1100, .35, .18); }, 440);
    var o = load(), k = dkey(new Date()); o.d[k] = (o.d[k] || 0) + 1;
    var ks = Object.keys(o.d).sort(); while (ks.length > 400) delete o.d[ks.shift()];
    save(o); paintDays();
    $('is-phase').textContent = S.done; $('is-cue').textContent = S.donec; $('is-next').textContent = ''; setTime('✓', ''); $('is-go').textContent = S.start;
  }
  function reset(){
    clearInterval(iv); iv = null; run = false; stage = 'idle'; si = 0; wake(false); segs = build(); show(segs[0].ex); dots();
    setTime('–', S.sec); $('is-phase').textContent = S.ready; $('is-cue').textContent = S.readyc; $('is-next').textContent = ''; $('is-go').textContent = S.start;
  }
  $('is-go').addEventListener('click', function(){
    try { ctx = ctx || new (window.AudioContext || window.webkitAudioContext)(); if (ctx.resume) ctx.resume(); } catch (e) {}
    if (stage === 'idle' || stage === 'done'){ segs = build(); wake(true); enter(0); return; }
    if (stage === 'reps'){ advance(); return; }
    if (run){ clearInterval(iv); iv = null; run = false; left = Math.max(0, left - (performance.now() - t0) / 1000); $('is-phase').textContent = S.paused; $('is-cue').textContent = S.pausedc; this.textContent = S.start; return; }
    run = true; t0 = performance.now(); this.textContent = S.pause; $('is-phase').textContent = fill(S[segs[si].k], {n: segs[si].n}); iv = setInterval(tick, 100); tick();
  });
  $('is-skip').addEventListener('click', function(){
    if (stage === 'idle' || stage === 'done') return;
    var ex = segs[si].ex, j = si; while (j < segs.length && segs[j].ex === ex) j++;
    if (j < segs.length) enter(j); else finish();
  });
  $('is-prev').addEventListener('click', function(){
    if (stage === 'idle' || stage === 'done') return;
    var ex = segs[si].ex, j = si; while (j > 0 && segs[j - 1].ex === ex) j--;
    if (j === si || j === 0){ if (j > 0){ var px = segs[j - 1].ex; j = j - 1; while (j > 0 && segs[j - 1].ex === px) j--; } }
    enter(j);
  });
  $('is-reset').addEventListener('click', reset);
  $('is-mode').addEventListener('click', function(e){
    var b = e.target.closest('button'); if (!b) return;
    this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); info(); reset();
  });
  info(); reset(); paintDays();
  window.__is = {st: function(){ return [stage, si, segs.length, stage === 'idle' ? -1 : segs[si].ex, run]; }, skip: function(){ left = 0; t0 = performance.now(); }, total: function(){ return segs.reduce(function(a, s){ return a + s.sec; }, 0); }};
})();
</script>
'''

page("sakatlanmayi-onleyen-isinma.html", "Sakatlanmayı Önleyen Isınma",
     "Futbolda sakatlanmaları azalttığı gösterilen FIFA 11+ programından uyarlanmış 20 dakikalık ısınma: 15 hareket, süre ve set sayacı, maç öncesi kısa sürüm ve haftalık takip.",
     "sakatlanmayi-onleyen-isinma.html", SELF15_CSS, IS_BODY, IS_JS,
     seo_title="Sakatlanmayı Önleyen Isınma (FIFA 11+ Uyarlaması): Zamanlayıcı ve Takip | İhsan Eren",
     about={"@type": "ExercisePlan", "name": "Sakatlanmayı önleyen ısınma"},
     faq_items=IS_FAQ)

# ------------------------------------------------------------------ 2 · ADIM HEDEFİ PLANLAYICISI
AH_FAQ = [
 ("10.000 adım şart mı?", "Hayır. 57 çalışmayı inceleyen 2025 tarihli bir derlemede, günde 7.000 adım atanlarda 2.000 adım atanlara göre ölüm riski %47 daha düşüktü; ölüm, kalp-damar hastalığı, demans ve düşmelerde yararın büyük kısmı 5.000–7.000 adım civarında ortaya çıkıyordu. Daha fazla adım bazı hastalıklarda ek yarar sağlayabilir, ama 7.000 adım çoğu kişi için gerçekçi ve etkili bir hedef."),
 ("Yaşım ileri, hedefim farklı mı?", "15 çalışmayı birleştiren bir analizde ölüm riskindeki azalma 60 yaş ve üzerindekilerde günde yaklaşık 6.000–8.000, 60 yaşın altındakilerde 8.000–10.000 adımda düzleşti. Bu sayfa hedefinizi yaşınıza göre bu aralıklara göre gösterir."),
 ("Her gün ne kadar artırmalıyım?", "Küçük artışlar da önemli. Yaklaşık 227 bin kişiyi kapsayan bir meta-analizde her ek 1.000 adım, ölüm riskinde yaklaşık %15 azalmayla ilişkiliydi. Bu sayfa her hafta günlük ortalamanıza 1.000 adım eklemeyi önerir; bu genel bir öneridir, eklem ağrınız ya da bir sağlık sorununuz varsa artışı yavaşlatın."),
 ("Adımlarımı nasıl ölçerim?", "Telefonunuzun sağlık uygulaması ya da bir adımsayar yeterlidir. Son 7 günün günlük ortalamasını alın; tek bir güne değil, haftalık ortalamaya bakın. Telefonu üzerinizde taşımadığınız zamanlar sayılmayacağı için gerçek adım sayınız biraz daha yüksek olabilir."),
 ("Adımların hızı önemli mi?", "Toplam adım sayısı en tutarlı ölçüt. 15 çalışmalık analizde, günün en hızlı 30–60 dakikasındaki adım hızı da düşük ölümle ilişkiliydi, ama yürüme süresinin belirli bir hızın üzerinde geçmesi ayrıca anlamlı değildi. Yürüyüşlerinizin bir kısmını tempolu yapmak yine de kondisyonunuzu artırır."),
]

AH_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Adım hedefi planlayıcısı</h1>
    <p class="lede">Günlük adım sayısı, sağlığınızla ilgili en kolay izlenen ölçülerden biri. Büyük araştırmalara göre çok az hareket edenlerde bile her ek adım değerli ve yararın büyük kısmı 10.000 adımdan çok önce başlıyor. Bu sayfa son haftanızın ortalamasına göre gerçekçi bir haftalık hedef önerir, sizi araştırmalardaki eşiklere yaklaştıracak bir plan çıkarır ve haftalık ortalamalarınızı kaydeder.</p>
    <p class="meta">Son güncelleme: 24 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>7.000</b><span>Günlük adım: 2.000 adıma göre ölüm riski %47 daha düşük (57 çalışmalık derleme)</span></div>
        <div class="stat"><b>−%15</b><span>Her ek 1.000 adımla ilişkili ölüm riskindeki azalma</span></div>
        <div class="stat"><b>6–8 bin</b><span>60 yaş ve üzerinde yararın düzleştiği aralık; 60 yaş altında 8–10 bin</span></div>
        <div class="stat"><b>+5 dk</b><span>Günde 5 dakika daha tempolu yürümenin toplumdaki ölümlerin tahminen %10'unu önleyebileceği hesaplandı</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Planınızı çıkarın</p>
      <h2>Adım hedefinizi belirleyin</h2>
      <p class="soft">Telefonunuzun sağlık uygulamasından ya da adımsayarınızdan son 7 günün günlük ortalamasını girin ve yaş grubunuzu seçin. Haftalık ortalamanızı her hafta kaydederek ilerlemenizi izleyebilirsiniz.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <p class="lbl">Yaş grubu</p>
            <div class="seg" role="group" aria-label="Yaş grubu" id="ah-age">
              <button type="button" data-v="u" aria-pressed="true">60 yaş altı</button>
              <button type="button" data-v="o" aria-pressed="false">60 yaş ve üzeri</button>
            </div>
            <div class="ah-in">
              <div><label for="ah-avg">Günlük ortalama adım (son 7 gün)</label><input id="ah-avg" type="text" inputmode="numeric" autocomplete="off" placeholder="ör. 4200"></div>
              <button type="button" class="cta" id="ah-calc">Planı göster</button>
            </div>
            <p class="tg-msg" id="ah-msg" aria-live="polite"></p>
            <div class="controls" style="margin-top:12px"><button type="button" class="cta ghost" id="ah-save" disabled>Bu haftayı kaydet</button></div>
          </div>
          <div class="bt-out">
            <p class="lbl">Haftalık ortalamalarınız (bu cihazda)</p>
            <div class="ah-bars" id="ah-bars"></div>
            <p class="tg-msg" id="ah-none">Henüz kayıt yok. Planı gösterip haftanızı kaydedin.</p>
            <div class="tg-tools"><button type="button" class="cta ghost" id="ah-clear">Kayıtları sil</button></div>
          </div>
          <div class="bt-run" style="text-align:left">
            <div class="res" id="ah-res" hidden>
              <p class="lab" id="ah-lab"></p>
              <p class="ah-big" id="ah-big"></p>
              <p id="ah-txt"></p>
              <ul class="ah-plan" id="ah-plan"></ul>
            </div>
          </div>
        </div>
        <div class="ah-strings" hidden>
          <span data-k="bad">Lütfen 0 ile 40.000 arasında bir sayı girin.</span>
          <span data-k="lab">Bu haftaki hedefiniz</span>
          <span data-k="unit">adım / gün</span>
          <span data-k="low">Günlük ortalamanız {{a}} adım. Bu düzeyde her ek adım değerli: önce günde {{t}} adımı hedefleyin; örneğin günde iki kez 5 dakikalık bir yürüyüş eklemek yaklaşık 1.000 adım eder.</span>
          <span data-k="mid">Günlük ortalamanız {{a}} adım. Araştırmalarda yararın büyük kısmının ortaya çıktığı 7.000 adıma yaklaşıyorsunuz; bu hafta günde {{t}} adımı hedefleyin.</span>
          <span data-k="hi">Günlük ortalamanız {{a}} adım; 7.000 adım eşiğini geçtiniz. Yaş grubunuz için yararın düzleştiği {{r}} aralığına {{msg}}</span>
          <span data-k="hi1">ulaşmak için bu hafta günde {{t}} adımı hedefleyebilirsiniz.</span>
          <span data-k="hi2">ulaştınız ya da geçtiniz; bu düzeyi korumak harika bir hedef. Yürüyüşlerinizin bir kısmını tempolu yapmayı ve haftada 2 gün güç egzersizi eklemeyi düşünebilirsiniz.</span>
          <span data-k="ru">8.000–10.000 adım</span>
          <span data-k="ro">6.000–8.000 adım</span>
          <span data-k="wk">{{n}}. hafta</span>
          <span data-k="steps">{{n}} adım/gün</span>
          <span data-k="saved">Bu haftanın ortalaması kaydedildi.</span>
          <span data-k="sure">Emin misiniz? Silmek için yeniden basın</span>
          <span data-k="clear">Kayıtları sil</span>
        </div>
      </div>
      <p class="count">Kayıtlarınız yalnızca bu cihazda saklanır; hiçbir yere gönderilmez.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Araştırmalar ne diyor?</h2>
        <p class="soft">57 çalışmayı inceleyen 2025 tarihli bir derlemede, günde 7.000 adım atanlarda 2.000 adım atanlara göre ölüm riski %47, kalp-damar hastalığından ölüm riski %47, demans riski %38, depresyon belirtileri %22, düşmeler %28 daha düşüktü. Ölüm, kalp-damar hastalığı, demans ve düşmelerde yararın büyük kısmı 5.000–7.000 adım civarında ortaya çıkıyordu.</p>
        <p class="soft">Bunlar gözlem çalışmalarıdır: Çok yürüyenler başka açılardan da daha sağlıklı olabilir. Yine de farklı ülkelerden gelen sonuçlar tutarlı ve küçük artışların bile anlamlı olduğunu gösteriyor.</p>
      </div>
      <div>
        <h2>Adımlarınızı artırmanın yolları</h2>
        <ul class="dots">
          <li>Günde iki ya da üç kez 5–10 dakikalık yürüyüş ekleyin; özellikle yemeklerden sonra.</li>
          <li>Telefonla konuşurken ayakta yürüyün; asansör yerine merdiveni kullanın.</li>
          <li>Bir durak önce inin ya da arabanızı biraz uzağa park edin.</li>
          <li>Uzun oturmaları her yarım saatte bir kısa bir yürüyüşle bölün.</li>
          <li>Yürüyüşlerinizin bir kısmını konuşabileceğiniz ama biraz nefes nefese kalacağınız bir tempoda yapın.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(AH_FAQ)}
      <p class="soft" style="margin-top:18px">Yürüyüş temposunu ayarlamak için <a href="tempolu-yuruyus.html">tempolu yürüyüş metronomuna</a>, yemekten sonra yürümek için <a href="yemek-sonrasi-yuruyus.html">yemek sonrası yürüyüş zamanlayıcısına</a>, haftalık önerilerin tamamı için <a href="hareket.html">ne kadar hareket yeterli?</a> sayfasına bakabilirsiniz.</p>
      {CTA_CARD("Hareket planınız", "günlük adım ve hareket planı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Ding D, et al. Daily steps and health outcomes in adults: a systematic review and dose-response meta-analysis. Lancet Public Health. 2025. Özet: " + ext("https://epocrates.com/online/article/7-000-daily-steps-associated-with-substantial-reductions-in-mortality-and", "Epocrates, 29 July 2025") + ".",
        "Paluch AE, Bajpai S, Bassett DR, et al. Daily steps and all-cause mortality: a meta-analysis of 15 international cohorts. Lancet Public Health. 2022;7(3):e219–e228. Özet: " + ext("https://hospitalhealthcare.com/specialisms/cardiovascular/mortality-benefit-from-higher-daily-steps-plateaus/", "Hospital Healthcare Europe, 15 March 2022") + ".",
        "Banach M, Lewek J, Surma S, et al. The association between daily step count and all-cause and cardiovascular mortality: a meta-analysis. Eur J Prev Cardiol. 2023. doi:10.1093/eurjpc/zwad229. Özet: " + ext("https://www.communitypractitioner.co.uk/just-4000-steps-a-day-can-reduce-the-risk-of-death-from-any-cause/", "Community Practitioner, 11 August 2023") + ".",
        "Ekelund U, Tarp J, Ding D, et al. Deaths potentially averted by small changes in physical activity and sedentary time: an individual participant data meta-analysis of prospective cohort studies. Lancet. 2026;407(10526):339–349. Basın bülteni: " + ext("https://www.eurekalert.org/news-releases/1112291", "EurekAlert!, 13 January 2026") + ".",
        "Bull FC, Al-Ansari SS, Biddle S, et al. " + ext("https://bjsm.bmj.com/content/54/24/1451", "World Health Organization 2020 guidelines on physical activity and sedentary behaviour") + ". Br J Sports Med. 2020;54(24):1451–1462.",
      ])}
    </div>
  </section>
</main>'''

AH_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.ah-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var EN = document.documentElement.lang === 'en';
  var $ = function(id){ return document.getElementById(id); }, KEY = 'drihsaneren.adimhedefi.v1';
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function fmt(n){ return Math.round(n).toLocaleString(EN ? 'en-GB' : 'tr-TR'); }
  function age(){ return $('ah-age').querySelector('[aria-pressed="true"]').getAttribute('data-v'); }
  function load(){ try { return JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { return []; } }
  function keep(l){ try { localStorage.setItem(KEY, JSON.stringify(l.slice(-26))); } catch (e) {} }
  function r500(n){ return Math.round(n / 500) * 500; }
  var cur = null;
  function plan(a){
    var top = age() === 'o' ? 8000 : 10000, lowEdge = age() === 'o' ? 6000 : 8000, t, txt, steps = [];
    if (a < 7000){
      t = r500(Math.min(7000, a + 1000)); if (t <= a) t = r500(a + 500);
      txt = fill(a < 4000 ? S.low : S.mid, {a: fmt(a), t: fmt(t)});
      var x = a; while (x < 7000 && steps.length < 8){ x = Math.min(7000, r500(x + 1000)); steps.push(x); }
    } else if (a < lowEdge){
      t = r500(Math.min(lowEdge, a + 1000));
      txt = fill(S.hi, {a: fmt(a), r: S[age() === 'o' ? 'ro' : 'ru'], msg: fill(S.hi1, {t: fmt(t)})});
      var y = a; while (y < lowEdge && steps.length < 8){ y = Math.min(lowEdge, r500(y + 1000)); steps.push(y); }
    } else {
      t = Math.round(a / 100) * 100;
      txt = fill(S.hi, {a: fmt(a), r: S[age() === 'o' ? 'ro' : 'ru'], msg: S.hi2});
    }
    return {t: t, txt: txt, steps: steps, top: top};
  }
  function paintPlan(){
    if (cur == null){ $('ah-res').hidden = true; return; }
    var p = plan(cur); $('ah-res').hidden = false;
    $('ah-lab').textContent = S.lab;
    $('ah-big').innerHTML = ''; $('ah-big').appendChild(document.createTextNode(fmt(p.t)));
    var sm = document.createElement('small'); sm.textContent = S.unit; $('ah-big').appendChild(sm);
    $('ah-txt').textContent = p.txt;
    var ul = $('ah-plan'); ul.innerHTML = '';
    p.steps.forEach(function(v, i){ var li = document.createElement('li'), sp = document.createElement('span'), b = document.createElement('b'); sp.textContent = fill(S.wk, {n: i + 1}); b.textContent = fill(S.steps, {n: fmt(v)}); li.appendChild(sp); li.appendChild(b); ul.appendChild(li); });
  }
  function paintBars(){
    var l = load(), box = $('ah-bars'); box.innerHTML = ''; $('ah-none').hidden = !!l.length;
    var max = Math.max.apply(null, [10000].concat(l.map(function(r){ return r.a; })));
    l.slice(-8).forEach(function(r){
      var row = document.createElement('div'), sp = document.createElement('span'), i = document.createElement('i'), b = document.createElement('b');
      row.className = 'ah-bar'; sp.textContent = new Date(r.t).toLocaleDateString(EN ? 'en-GB' : 'tr-TR', {day: 'numeric', month: 'short'});
      i.style.width = Math.max(2, Math.round(r.a / max * 100)) + '%'; if (r.a >= 7000) i.className = 'hit';
      b.textContent = fmt(r.a); row.appendChild(sp); row.appendChild(i); row.appendChild(b); box.appendChild(row);
    });
  }
  $('ah-calc').addEventListener('click', function(){
    var v = parseInt(String($('ah-avg').value).replace(/[.,\\s]/g, ''), 10), msg = $('ah-msg');
    msg.classList.remove('warn'); msg.textContent = '';
    if (isNaN(v) || v < 0 || v > 40000){ msg.textContent = S.bad; msg.classList.add('warn'); cur = null; $('ah-save').disabled = true; paintPlan(); return; }
    cur = v; $('ah-save').disabled = false; paintPlan();
  });
  $('ah-age').addEventListener('click', function(e){
    var b = e.target.closest('button'); if (!b) return;
    this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); paintPlan();
  });
  $('ah-save').addEventListener('click', function(){
    if (cur == null) return;
    var l = load(), now = new Date(), wk = function(d){ var m = new Date(d.getFullYear(), d.getMonth(), d.getDate() - ((d.getDay() + 6) % 7)); return m.toDateString(); };
    if (l.length && wk(new Date(l[l.length - 1].t)) === wk(now)) l.pop();
    l.push({t: now.toISOString(), a: cur}); keep(l); paintBars(); $('ah-msg').textContent = S.saved;
  });
  var armed = false;
  $('ah-clear').addEventListener('click', function(){
    if (!armed){ armed = true; this.textContent = S.sure; var b = this; setTimeout(function(){ armed = false; b.textContent = S.clear; }, 4000); return; }
    keep([]); armed = false; this.textContent = S.clear; paintBars();
  });
  paintBars();
  window.__ah = {st: function(){ return [cur, cur == null ? null : plan(cur).t, load().length]; }};
})();
</script>
'''

page("adim-hedefi.html", "Adım Hedefi Planlayıcısı",
     "Günlük adım ortalamanıza göre haftalık hedef ve plan: 7.000 adım eşiği, yaşa göre 6.000–10.000 adım aralığı, her 1.000 adımın değeri ve haftalık kayıt.",
     "adim-hedefi.html", SELF15_CSS, AH_BODY, AH_JS,
     seo_title="Adım Hedefi Planlayıcısı: Günde Kaç Adım Yeterli? 7.000 Adım ve Haftalık Plan | İhsan Eren",
     about={"@type": "ExercisePlan", "name": "Günlük adım hedefi"},
     faq_items=AH_FAQ)

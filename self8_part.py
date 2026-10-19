# -*- coding: utf-8 -*-
# Kendine iyi bak, 8. tur: kalk ve yürü testi (TUG), masa başı mola zamanlayıcısı. self7_part.py'den sonra exec edilir
# (SELF7_CSS, WAKE_JS, cs_sts, cs_heel hazır).

SELF8_CSS = SELF7_CSS + """
  .mz-chk{display:flex;gap:10px;align-items:flex-start;font-size:14.5px;color:var(--ink-soft);margin:8px 0;cursor:pointer;line-height:1.45}
  .mz-chk input{flex:none;width:18px;height:18px;margin-top:2px;accent-color:var(--foil)}
  .tug-obs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 18px;margin:4px 0 0}
  @media (max-width:600px){.tug-obs{grid-template-columns:1fr}}
  .mz-today{font-size:14px;color:var(--ink-soft);margin:14px 0 0}
  .bt-run.brk .yh-time b{color:var(--foil)}
"""

# ------------------------------------------------------------------ 1 · KALK VE YÜRÜ TESTİ (TUG)
# Bohannon 2006: ortalama (95% GA) saniye
TUG_NORM = [("60–69", 8.1, 7.1, 9.0), ("70–79", 9.2, 8.2, 10.2), ("80–99", 11.3, 10.0, 12.7)]
TUG_ROWS = "\n".join(f'<tr data-i="{i}"><td>{a}</td><td>{str(m).replace(".", ",")}</td><td>{str(lo).replace(".", ",")}–{str(hi).replace(".", ",")}</td></tr>' for i, (a, m, lo, hi) in enumerate(TUG_NORM))
TUG_OBS = ["Yavaş, çekingen adımlar", "Denge kaybı", "Kısa adımlar", "Kolların az sallanması ya da hiç sallanmaması", "Duvara ya da eşyalara tutunma", "Ayakları sürüme", "Dönerken bütün gövdeyle, tek parça dönme", "Baston ya da yürütecin doğru kullanılmaması"]
TUG_OBSH = "\n".join(f'<label class="mz-chk"><input type="checkbox" class="tug-o"> {o}</label>' for o in TUG_OBS)

TUG_FAQ = [
 ("Testi tek başıma yapabilir miyim?", "Hayır. Süreyi tutacak ve güvenliğiniz için yanınızda yürüyecek birinin olması gerekir."),
 ("Baston ya da yürüteçle yapabilir miyim?", "Evet. Her zamanki ayakkabılarınızla ve günlük hayatta kullandığınız yürüme yardımcısıyla yapın. Zaman içinde karşılaştırmak için her seferinde aynı şekilde yapmanız yeterli."),
 ("Sürem 12 saniyenin üzerinde çıktı, ne yapmalıyım?", "Bu bir tanı değildir. ABD Hastalık Kontrol ve Önleme Merkezleri (CDC), testi 12 saniye ya da daha uzun sürede tamamlayan yaşlıları düşme açısından riskli kabul ediyor ve daha ayrıntılı değerlendirme öneriyor. Bir hekim ya da fizyoterapistle konuşabilir, aşağıdaki güç ve denge egzersizleriyle başlayabilirsiniz."),
 ("Bu test düşüp düşmeyeceğimi kesin olarak söyler mi?", "Hayır. İngiltere’nin ulusal sağlık kılavuzu NICE (2025), düşme riskini tahmin etmek için tek başına bir test ya da puanlama aracı kullanılmamasını öneriyor; bu tür testler yürüme ve denge sorunlarını fark etmeye yardım eder. Sağlıklı ve bağımsız yaşayan yaşlılarda yapılan çalışmalar da bu testin tek başına düşmeleri öngörmediğini gösteriyor. Bu yüzden son bir yılda düştüyseniz, sonucunuz ne olursa olsun bunu hekiminize söyleyin. Birden fazla kez düştüyseniz, düşmede yaralandıysanız, bilincinizi kaybettiyseniz ya da yerden yardımsız kalkamadıysanız kapsamlı bir düşme değerlendirmesi isteyebilirsiniz."),
 ("Daha genç yaştaysam ne olacak?", "Buradaki karşılaştırma değerleri 60 yaş ve üstü kişilerden elde edildi. Daha genç yaştaysanız sürenizi kaydedip zaman içindeki değişimini izleyebilirsiniz."),
]

TUG_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Kalk ve yürü testi</h1>
    <p class="lede">Sandalyeden kalkıp 3 metre yürümek, dönüp geri gelmek ve yeniden oturmak kaç saniyenizi alıyor? “Süreli kalk ve yürü testi” (Timed Up and Go, kısaca TUG), hareketliliği ve düşme riskini değerlendirmek için kullanılan basit bir test. ABD Hastalık Kontrol ve Önleme Merkezleri (CDC), testi 12 saniye ya da daha uzun sürede tamamlayan yaşlıları düşme açısından riskli kabul ediyor. Yanınızda biriyle, aşağıdaki süreölçerle deneyin.</p>
    <p class="meta">Son güncelleme: 16 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>3 metre</b><span>Sandalyeden yürüme çizgisine kadar olan mesafe</span></div>
        <div class="stat"><b>12 saniye</b><span>Bu süre ve üzeri, yaşlılarda düşme riski işareti</span></div>
        <div class="stat"><b>8,1 saniye</b><span>60–69 yaş grubunun ortalama süresi</span></div>
        <div class="stat"><b>11,3 saniye</b><span>80–99 yaş grubunun ortalama süresi</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Kendinizi ölçün</p>
      <h2>Süreölçerle ölçün</h2>
      <p class="soft">Kolçaklı bir sandalyeden 3 metre uzağa yere bir çizgi çekin. Süreyi yanınızdaki biri tutsun: “Başla” dediği anda süreölçeri başlatsın, siz yeniden oturduğunuzda durdursun.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <p class="lbl"><label for="tug-age">Yaşınız</label></p>
            <input class="cs-age" id="tug-age" type="number" inputmode="numeric" min="18" max="110" placeholder="ör. 72">
          </div>
          <div class="bt-out">
            <div class="res" id="tug-res" hidden>
              <p class="lab" id="tug-lab"></p>
              <p id="tug-txt"></p>
              <span class="bt-badge" id="tug-badge"></span>
              <div class="cs-acts"><a class="cta" id="tug-wa" href="#" target="_blank" rel="noopener">Sonucumu WhatsApp’tan gönder</a></div>
            </div>
            <div id="tug-histw" style="margin-top:20px" hidden>
              <p class="lbl">Önceki sonuçlarınız (bu cihazda)</p>
              <ul class="cs-hist" id="tug-hist"></ul>
            </div>
          </div>
          <div class="bt-run">
            <div class="yh-time"><b id="tug-sec">0,00</b><span>saniye</span></div>
            <p class="bt-phase" id="tug-phase" aria-live="polite">Hazır</p>
            <p class="bt-cue" id="tug-cue">Kişi sırtı yaslanmış şekilde sandalyede otursun. “Başla” derken süreölçeri başlatın.</p>
            <button type="button" class="bt-tap" id="tug-go">Başla</button>
          </div>
        </div>
        <div style="margin-top:22px">
          <p class="lbl">Test sırasında gözlediklerinizi işaretleyin</p>
          <div class="tug-obs" id="tug-obs">
{TUG_OBSH}
          </div>
        </div>
        <div class="tug-strings" hidden>
          <span data-k="ready">Hazır</span>
          <span data-k="readyc">Kişi sırtı yaslanmış şekilde sandalyede otursun. “Başla” derken süreölçeri başlatın.</span>
          <span data-k="run">Test sürüyor</span>
          <span data-k="runc">Kişi yeniden oturduğu anda durdurun.</span>
          <span data-k="start">Başla</span>
          <span data-k="stop">Oturdu</span>
          <span data-k="done">Sonuç kaydedildi</span>
          <span data-k="donec">İsterseniz testi bir kez daha yapabilirsiniz.</span>
          <span data-k="lab">Süreniz: {{s}} saniye</span>
          <span data-k="noage">Yaş grubunuzun ortalamasıyla karşılaştırmak için yaşınızı girin.</span>
          <span data-k="young">Buradaki karşılaştırma değerleri 60 yaş ve üstü kişilerden elde edildi.</span>
          <span data-k="avg">Yaş grubunuzun ortalaması {{m}} saniye.</span>
          <span data-k="fast">Ortalama kadar ya da daha hızlısınız.</span>
          <span data-k="mid">Ortalamaya yakınsınız.</span>
          <span data-k="slow">Yaş grubunuzun ortalamasından belirgin şekilde yavaşsınız.</span>
          <span data-k="risk">12 saniye ve üzeri, yaşlılarda düşme riski açısından ayrıntılı değerlendirme gerektiren bir işaret kabul ediliyor. Bu bir tanı değildir; bir hekim ya da fizyoterapistle konuşabilirsiniz.</span>
          <span data-k="obs">İşaretlediğiniz bulgular ayrıntılı bir değerlendirme gerektirebilir; bunları bir hekim ya da fizyoterapistle paylaşın.</span>
          <span data-k="bok">12 saniyenin altında</span>
          <span data-k="bno">Değerlendirme önerilir</span>
          <span data-k="sec">saniye</span>
          <span data-k="wa">Merhaba, drihsaneren.com’daki kalk ve yürü testini yaptım: {{s}} saniye. Değerlendirme hakkında bilgi almak istiyorum.</span>
        </div>
      </div>
      <p class="count">Sonuçlarınız yalnızca bu cihazda saklanır; hiçbir yere gönderilmez.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Nasıl yapılır?</h2>
        <ol class="steps">
          <li><span>Kolçaklı, standart bir sandalye koyun ve <strong>3 metre</strong> ileride yere bir çizgi çekin.</span></li>
          <li><span>Kişi her zamanki ayakkabılarıyla, sırtı yaslanmış şekilde otursun. Kullanıyorsa bastonunu ya da yürütecini yanına alsın.</span></li>
          <li><span>“Başla” deyin ve süreölçeri başlatın. Kişi kalksın, <strong>her zamanki temposuyla</strong> çizgiye kadar yürüsün, dönsün, aynı tempoyla geri gelip otursun.</span></li>
          <li><span>Kişi <strong>yeniden oturduğu anda</strong> durdurun. Test sırasında güvenlik için yanında durun.</span></li>
        </ol>
      </div>
      <div>
        <h2>Yaşa göre ortalama süreler</h2>
        <p class="soft">21 çalışmanın birleştirildiği bir analizden ortalama süreler (saniye) ve %95 güven aralığı. Süresi aralığın üst sınırından uzun olanlar ortalamanın altında kabul edilir.</p>
        <table class="nt" id="tug-nt">
          <thead><tr><th>Yaş</th><th>Ortalama</th><th>Güven aralığı</th></tr></thead>
          <tbody>
{TUG_ROWS}
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Güç ve denge</p>
      <h2>Evde dört egzersiz</h2>
      <p class="soft">Kalkmak, yürümek ve dönmek bacak gücü ve denge ister. Ayrıntılı öneriler için <a href="dusme-onleme.html">düşmeleri önleme</a> rehberine, bacak gücünüz için <a href="sandalye-testi.html">30 saniye sandalye testine</a> bakabilirsiniz.</p>
      {ex_grid(["cs_sts", "cs_heel", "tandem", "sls"], "ex four")}
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(TUG_FAQ)}
      {CTA_CARD("Yürüyüşünüz, dengeniz ve düşme riskiniz", "kalk ve yürü testi, denge değerlendirmesi")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Centers for Disease Control and Prevention (STEADI). " + ext("https://www.cdc.gov/steadi/pdf/steadi-assessment-tug-508.pdf", "Assessment: Timed Up & Go (TUG)") + ". 2017.",
        "Bohannon RW. " + ext("https://read.qxmd.com/doi/10.1519/00139143-200608000-00004", "Reference values for the timed up and go test: a descriptive meta-analysis") + ". J Geriatr Phys Ther. 2006.",
        "Browne W, Nair BR. " + ext("https://doi.org/10.5694/mja2.12045", "The Timed Up and Go test") + ". Med J Aust. 2019;210(1):13–14.",
        "NICE. " + ext("https://www.nice.org.uk/guidance/ng249", "Falls: assessment and prevention in older people and in people 50 and over at higher risk") + ". NICE guideline NG249, 29 April 2025.",
      ])}
    </div>
  </section>
</main>'''

TUG_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.tug-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var EN = document.documentElement.lang === 'en';
  var $ = function(id){ return document.getElementById(id); };
  var NORM = [[8.1, 9.0], [9.2, 10.2], [11.3, 12.7]];
  var KEY = 'drihsaneren.tug.v1', WA = 'https://wa.me/905538815568?text=';
  var phase = 'idle', t0 = 0, iv = null, last = null, lock = null, ctx = null, snd = null;
''' + WAKE_JS + '''
  function fmt(x, d){ var s = x.toFixed(d); return EN ? s : s.replace('.', ','); }
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function age(){ var a = parseInt($('tug-age').value, 10); return isNaN(a) ? null : a; }
  function band(a){ if (a == null || a < 60) return -1; if (a < 70) return 0; if (a < 80) return 1; return a <= 99 ? 2 : -1; }
  function store(){ try { return JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { return []; } }
  function save(l){ try { localStorage.setItem(KEY, JSON.stringify(l.slice(-10))); } catch (e) {} }
  function paintNorm(){ var b = band(age()); $('tug-nt').querySelectorAll('tbody tr').forEach(function(r){ r.classList.toggle('me', +r.getAttribute('data-i') === b); }); }
  function paintRes(){
    var res = $('tug-res'); if (last == null){ res.hidden = true; return; }
    res.hidden = false;
    var a = age(), b = band(a), txt = '', badge = $('tug-badge');
    $('tug-lab').textContent = fill(S.lab, {s: fmt(last, 2)});
    if (a == null) txt = S.noage;
    else if (b < 0) txt = S.young;
    else { var n = NORM[b]; txt = fill(S.avg, {m: fmt(n[0], 1)}) + ' ' + (last <= n[0] ? S.fast : last <= n[1] ? S.mid : S.slow); }
    var obs = root.querySelectorAll('.tug-o:checked').length, bad = last >= 12 || obs > 0;
    if (last >= 12) txt += ' ' + S.risk;
    if (obs) txt += ' ' + S.obs;
    $('tug-txt').textContent = txt;
    badge.hidden = false; badge.textContent = bad ? S.bno : S.bok; badge.classList.toggle('no', bad);
    $('tug-wa').href = WA + encodeURIComponent(fill(S.wa, {s: fmt(last, 2)}));
  }
  function paintHist(){
    var h = store(), ul = $('tug-hist'); $('tug-histw').hidden = !h.length; ul.innerHTML = '';
    h.slice().reverse().forEach(function(r){
      var li = document.createElement('li'), sp = document.createElement('span'), bb = document.createElement('b');
      sp.textContent = new Date(r.t).toLocaleDateString(EN ? 'en-GB' : 'tr-TR', {day: 'numeric', month: 'short', year: 'numeric'});
      bb.textContent = fmt(r.s, 2) + ' ' + S.sec; li.appendChild(sp); li.appendChild(bb); ul.appendChild(li);
    });
  }
  function idle(p, c){
    phase = 'idle'; clearInterval(iv); iv = null; wake(false);
    $('tug-go').textContent = S.start; $('tug-go').classList.remove('stop');
    $('tug-phase').textContent = p || S.ready; $('tug-cue').textContent = c || S.readyc;
  }
  function start(){
    phase = 'run'; t0 = performance.now(); wake(true);
    $('tug-go').textContent = S.stop; $('tug-go').classList.add('stop');
    $('tug-phase').textContent = S.run; $('tug-cue').textContent = S.runc;
    clearInterval(iv); iv = setInterval(function(){ $('tug-sec').textContent = fmt((performance.now() - t0) / 1000, 2); }, 31);
  }
  function stop(){
    var x = (performance.now() - t0) / 1000; clearInterval(iv); iv = null;
    if (x < 2){ $('tug-sec').textContent = fmt(0, 2); idle(); return; }
    last = Math.round(x * 100) / 100; $('tug-sec').textContent = fmt(last, 2);
    var h = store(); h.push({t: new Date().toISOString(), s: last}); save(h); paintHist(); paintRes();
    idle(S.done, S.donec);
  }
  $('tug-go').addEventListener('click', function(){ if (phase === 'idle') start(); else stop(); });
  document.addEventListener('keydown', function(e){ if (phase === 'run' && (e.code === 'Space' || e.key === ' ')){ e.preventDefault(); stop(); } });
  $('tug-age').addEventListener('input', function(){ paintNorm(); paintRes(); });
  root.querySelectorAll('.tug-o').forEach(function(c){ c.addEventListener('change', paintRes); });
  if (EN) $('tug-nt').querySelectorAll('td').forEach(function(td){ td.textContent = td.textContent.replace(/(\\d),(\\d)/g, '$1.$2'); });
  $('tug-sec').textContent = fmt(0, 2); paintNorm(); paintHist(); idle();
})();
</script>
'''

page("kalk-yuru-testi.html", "Kalk ve Yürü Testi (TUG)",
     "Sandalyeden kalkıp 3 metre yürüyüp geri oturmanız kaç saniye sürüyor? Süreölçerle kalk ve yürü testini (TUG) yapın, yaşınızdaki ortalamayla karşılaştırın, düşme riski işaretlerini öğrenin.",
     "kalk-yuru-testi.html", SELF8_CSS, TUG_BODY, TUG_JS,
     seo_title="Kalk ve Yürü Testi (TUG): Süreölçer, Yaşa Göre Ortalamalar ve Düşme Riski | İhsan Eren",
     about={"@type": "MedicalTest", "name": "Kalk ve yürü testi (Timed Up and Go)"},
     faq_items=TUG_FAQ)

# ------------------------------------------------------------------ 2 · MASA BAŞI MOLA ZAMANLAYICISI
MZ_FAQ = [
 ("Ekranlar gözlerime kalıcı zarar verir mi?", "Hayır. Amerikan Oftalmoloji Akademisi, uzun ekran kullanımının gözlere kalıcı zarar verdiği düşüncesinin yanlış olduğunu belirtiyor. Ancak ekran başında uzun süre kalmak bulanık görme, ağrı ve kuruluk gibi geçici rahatsızlıklara yol açabilir."),
 ("Neden 30 dakikada bir 5 dakika?", "Orta yaş ve üzeri 11 kişinin katıldığı bir araştırmada 8 saatlik oturma farklı mola düzenleriyle bölündü. Kan şekerindeki yükselmeyi yalnızca her 30 dakikada 5 dakikalık hafif yürüyüş anlamlı olarak azalttı; bu düzen büyük tansiyonu da yaklaşık 4 mmHg düşürdü. Saatte bir 1 dakikalık yürüyüş dahil, denenen tüm mola türleri büyük tansiyonu düşürdü. Küçük bir çalışma olduğu için sonuçlar dikkatle yorumlanmalı."),
 ("Sekmeyi arka plana alırsam çalışır mı?", "Sayfa açık kaldığı sürece çalışır. Bazı tarayıcılar arka plandaki sekmelerde zamanlayıcıları yavaşlatabilir; bu durumda uyarı birkaç saniye ile bir dakika arasında gecikebilir. Bildirimlere izin verirseniz uyarıyı başka bir pencerede çalışırken de görürsünüz."),
 ("Molada ne yapabilirim?", "Hafif tempolu yürüyüş, merdiven inip çıkmak, ayakta telefon görüşmesi yapmak ya da birkaç germe hareketi. Dünya Sağlık Örgütü, oturarak geçen zamanın yerine hangi yoğunlukta olursa olsun hareket koymayı öneriyor."),
]

MZ_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Masa başı mola zamanlayıcısı</h1>
    <p class="lede">Ekran başında saatler nasıl geçiyor? Bu zamanlayıcı size iki küçük molayı hatırlatır: her 20 dakikada gözleriniz için 20 saniyelik bir uzağa bakma molası, her 30 dakikada bedeniniz için 5 dakikalık bir hareket molası. Başlatın, sayfayı açık bırakın ve işinize dönün; zamanı gelince sesli uyarı alırsınız.</p>
    <p class="meta">Son güncelleme: 16 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>20-20-20</b><span>Her 20 dakikada, en az 6 metre uzağa, en az 20 saniye bakın</span></div>
        <div class="stat"><b>15 → 5–7</b><span>Ekrana bakarken dakikadaki göz kırpma sayısının düştüğü aralık</span></div>
        <div class="stat"><b>30 dk · 5 dk</b><span>Küçük bir çalışmada kan şekeri yükselmesini azaltan mola düzeni</span></div>
        <div class="stat"><b>4 mmHg</b><span>Aynı mola düzeniyle büyük tansiyonda görülen düşüş</span></div>
      </div>
    </div>
  </section>

  <section id="test">
    <div class="wrap">
      <p class="eyebrow">Zamanlayıcıyla birlikte yapın</p>
      <h2>Molalarınızı hatırlatsın</h2>
      <p class="soft">Hangi molaları istediğinizi seçin ve başlatın. Mola zamanı gelince ne yapacağınız ekranda yazar; mola bitince sayaç kendiliğinden yeniden başlar.</p>
      <div class="tool">
        <div class="bt">
          <div class="bt-opt">
            <p class="lbl">Hatırlatmalar</p>
            <label class="mz-chk"><input type="checkbox" id="mz-eye" checked> Göz molası: her 20 dakikada 20 saniye</label>
            <label class="mz-chk"><input type="checkbox" id="mz-mv" checked> Hareket molası: 5 dakika</label>
            <div class="seg" role="group" aria-label="Hareket molası sıklığı" id="mz-int">
              <button type="button" data-v="30" aria-pressed="true">Her 30 dakikada</button>
              <button type="button" data-v="60" aria-pressed="false">Her 60 dakikada</button>
            </div>
            <label class="mz-chk"><input type="checkbox" id="mz-sound" checked> Sesli uyarı</label>
            <label class="mz-chk"><input type="checkbox" id="mz-notif"> Tarayıcı bildirimi gönder</label>
          </div>
          <div class="bt-out">
            <div class="trials" style="grid-template-columns:repeat(2,minmax(0,1fr))">
              <div><span>Göz molasına</span><b id="mz-te">20:00</b></div>
              <div><span>Hareket molasına</span><b id="mz-tm">30:00</b></div>
            </div>
            <p class="mz-today" id="mz-today"></p>
          </div>
          <div class="bt-run" id="mz-run">
            <div class="yh-time"><b id="mz-big">20:00</b><span id="mz-bigl">Göz molasına</span></div>
            <p class="bt-phase" id="mz-phase" aria-live="polite">Hazır</p>
            <p class="bt-cue" id="mz-cue">Başlat’a basın ve işinize dönün.</p>
            <button type="button" class="bt-tap" id="mz-go">Başlat</button>
            <div class="controls" style="margin-top:10px;justify-content:center">
              <button type="button" class="cta ghost" id="mz-reset">Sıfırla</button>
            </div>
          </div>
        </div>
        <div class="mz-strings" hidden>
          <span data-k="ready">Hazır</span>
          <span data-k="readyc">Başlat’a basın ve işinize dönün.</span>
          <span data-k="run">Çalışıyor</span>
          <span data-k="runc">Sayfayı açık bırakın; mola zamanı gelince uyarı alırsınız.</span>
          <span data-k="paused">Duraklatıldı</span>
          <span data-k="pausedc">Hazır olduğunuzda devam edin.</span>
          <span data-k="eye">Göz molası</span>
          <span data-k="eyec">Ekrandan başınızı kaldırın, en az 6 metre uzaktaki bir noktaya bakın ve gözlerinizi sık sık kırpın.</span>
          <span data-k="move">Hareket molası</span>
          <span data-k="movec">Kalkın ve 5 dakika hafif tempoda yürüyün, merdiven inip çıkın ya da birkaç germe hareketi yapın.</span>
          <span data-k="start">Başlat</span>
          <span data-k="pause">Duraklat</span>
          <span data-k="resume">Devam et</span>
          <span data-k="skip">Molayı bitir</span>
          <span data-k="nexte">Göz molasına</span>
          <span data-k="nextm">Hareket molasına</span>
          <span data-k="left">Molanın bitmesine</span>
          <span data-k="today">Bugün: {{e}} göz molası, {{m}} hareket molası</span>
        </div>
      </div>
      <p class="count">Sayaçlar yalnızca bu cihazda çalışır; hiçbir yere bilgi gönderilmez.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Gözleriniz için</h2>
        <ul class="dots">
          <li>Her 20 dakikada en az 6 metre uzaktaki bir noktaya en az 20 saniye bakın.</li>
          <li>Bilinçli olarak sık sık göz kırpın: ekrana bakarken kırpma sayısı dakikada yaklaşık 15’ten 5–7’ye düşer.</li>
          <li>Ekranı yaklaşık bir kol boyu (63 cm) uzağa koyun; gözleriniz ekrana hafifçe aşağı baksın.</li>
          <li>Ekran parlaklığını odanın ışığına uydurun, kontrastı artırın; parlamayı azaltmak için mat bir ekran filtresi kullanabilirsiniz.</li>
          <li>Gözleriniz kuruysa suni gözyaşı, kuru ve sıcak odada nemlendirici işe yarayabilir.</li>
        </ul>
      </div>
      <div>
        <h2>Bedeniniz için</h2>
        <ul class="dots">
          <li>Oturarak geçen zamanın yerine, hangi yoğunlukta olursa olsun hareket koyun.</li>
          <li>Hareket molasında hafif tempoda yürüyün ya da merdiven inip çıkın.</li>
          <li>Molada yapabileceğiniz kısa hareketler için <a href="hareket-atistirmaliklari.html">hareket atıştırmalıkları</a>, çalışma düzeniniz için <a href="masa-basi.html">masa başında çalışanlar için</a> rehberine bakabilirsiniz.</li>
        </ul>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(MZ_FAQ)}
      {CTA_CARD("Masa başı çalışmaya bağlı boyun, sırt ve bel ağrınız", "masa başı çalışmaya bağlı ağrılar")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "American Academy of Ophthalmology. " + ext("https://www.aao.org/eye-health/diseases/computer-usage", "Computers, digital devices and eye strain") + ".",
        "Duran AT, Friel CP, Serafini MA, Ensari I, Cheung YK, Diaz KM. " + ext("https://scholars.mssm.edu/en/publications/breaking-up-prolonged-sitting-to-improve-cardiometabolic-risk-dos/", "Breaking up prolonged sitting to improve cardiometabolic risk: dose-response analysis of a randomized crossover trial") + ". Med Sci Sports Exerc. 2023;55(5):847–855.",
        "Bull FC, Al-Ansari SS, Biddle S, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/33239350/", "World Health Organization 2020 guidelines on physical activity and sedentary behaviour") + ". Br J Sports Med. 2020;54(24):1451–1462.",
      ])}
    </div>
  </section>
</main>'''

MZ_JS = '''<script>
(function(){
  var root = document.getElementById('test'); if (!root) return;
  var S = {}; root.querySelectorAll('.mz-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var $ = function(id){ return document.getElementById(id); };
  var KEY = 'drihsaneren.mola.v1', EYE = 20 * 60e3, EYEB = 20e3, MVB = 5 * 60e3, mvInt = 30 * 60e3;
  var st = 'idle', eyeDue = 0, mvDue = 0, eyeLeft = EYE, mvLeft = mvInt, bEnd = 0, title = document.title;
  var lock = null, ctx = null, snd = $('mz-sound');
''' + WAKE_JS + '''
  function fmt(ms){ var s = Math.max(0, Math.ceil(ms / 1000)), m = Math.floor(s / 60); s = s % 60; return m + ':' + (s < 10 ? '0' : '') + s; }
  function fill(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(m, k){ return o[k] != null ? o[k] : m; }); }
  function today(){ var d = new Date(); return d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate(); }
  function load(){ var o = null; try { o = JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) {} if (!o || o.d !== today()) o = {d: today(), e: 0, m: 0}; return o; }
  function count(k){ var o = load(); o[k === 'eye' ? 'e' : 'm']++; try { localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {} }
  function on(k){ return $(k === 'eye' ? 'mz-eye' : 'mz-mv').checked; }
  function alertNow(k){
    beep(880, 0.35, 0.25); setTimeout(function(){ beep(880, 0.35, 0.25); }, 450);
    try { navigator.vibrate && navigator.vibrate([200, 120, 200]); } catch (e) {}
    document.title = '● ' + S[k] + ' · ' + title;
    try { if ($('mz-notif').checked && 'Notification' in window && Notification.permission === 'granted') new Notification(S[k], {body: S[k + 'c']}); } catch (e) {}
  }
  function begin(k){ st = k; bEnd = Date.now() + (k === 'eye' ? EYEB : MVB); alertNow(k); }
  function finish(){
    var k = st, t = Date.now(); count(k); st = 'run'; document.title = title;
    eyeDue = t + EYE; if (k === 'move') mvDue = t + mvInt;
    beep(660, 0.25, 0.2);
  }
  function tick(){
    var t = Date.now();
    if (st === 'run'){
      if (on('move') && t >= mvDue) begin('move');
      else if (on('eye') && t >= eyeDue) begin('eye');
    } else if ((st === 'eye' || st === 'move') && t >= bEnd) finish();
    paint();
  }
  function rem(k){ var t = Date.now(); if (k === 'eye') return st === 'idle' || st === 'pause' ? eyeLeft : eyeDue - t; return st === 'idle' || st === 'pause' ? mvLeft : mvDue - t; }
  function paint(){
    var brk = st === 'eye' || st === 'move', re = rem('eye'), rm = rem('move'), eo = on('eye'), mo = on('move');
    $('mz-te').textContent = eo ? fmt(re) : '–'; $('mz-tm').textContent = mo ? fmt(rm) : '–';
    if (brk){ $('mz-big').textContent = fmt(bEnd - Date.now()); $('mz-bigl').textContent = S.left; }
    else if (mo && (!eo || rm <= re)){ $('mz-big').textContent = fmt(rm); $('mz-bigl').textContent = S.nextm; }
    else if (eo){ $('mz-big').textContent = fmt(re); $('mz-bigl').textContent = S.nexte; }
    else { $('mz-big').textContent = '–'; $('mz-bigl').textContent = ''; }
    $('mz-run').classList.toggle('brk', brk);
    $('mz-phase').textContent = brk ? S[st] : st === 'run' ? S.run : st === 'pause' ? S.paused : S.ready;
    $('mz-cue').textContent = brk ? S[st + 'c'] : st === 'run' ? S.runc : st === 'pause' ? S.pausedc : S.readyc;
    $('mz-go').textContent = brk ? S.skip : st === 'run' ? S.pause : st === 'pause' ? S.resume : S.start;
    $('mz-go').classList.toggle('stop', st === 'run');
    var o = load(); $('mz-today').textContent = fill(S.today, {e: o.e, m: o.m});
  }
  $('mz-go').addEventListener('click', function(){
    var t = Date.now();
    if (st === 'idle' || st === 'pause'){ eyeDue = t + eyeLeft; mvDue = t + mvLeft; st = 'run'; try { if (ctx === null && snd.checked) beep(660, 0.05, 0.01); } catch (e) {} }
    else if (st === 'run'){ eyeLeft = Math.max(0, eyeDue - t); mvLeft = Math.max(0, mvDue - t); st = 'pause'; }
    else finish();
    paint();
  });
  $('mz-reset').addEventListener('click', function(){ st = 'idle'; eyeLeft = EYE; mvLeft = mvInt; document.title = title; paint(); });
  $('mz-int').addEventListener('click', function(e){
    var b = e.target.closest('button'); if (!b) return;
    this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
    mvInt = +b.getAttribute('data-v') * 60e3; mvLeft = mvInt; if (st === 'run') mvDue = Date.now() + mvInt; paint();
  });
  ['mz-eye', 'mz-mv'].forEach(function(id){ $(id).addEventListener('change', function(){
    var t = Date.now(); if (st === 'run'){ if (id === 'mz-eye') eyeDue = t + EYE; else mvDue = t + mvInt; } paint(); }); });
  $('mz-notif').addEventListener('change', function(){
    var c = this; if (!c.checked) return;
    if (!('Notification' in window)){ c.checked = false; return; }
    try { Notification.requestPermission().then(function(p){ if (p !== 'granted') c.checked = false; }); } catch (e) { c.checked = false; }
  });
  document.addEventListener('visibilitychange', tick);
  setInterval(tick, 500); paint();
  window.__mz = {set: function(a, b){ eyeDue = Date.now() + a; mvDue = Date.now() + b; }, st: function(){ return st; }, end: function(){ bEnd = Date.now(); }};
})();
</script>
'''

page("mola-zamanlayicisi.html", "Masa Başı Mola Zamanlayıcısı",
     "Ekran başında göz ve hareket molalarını unutmayın: her 20 dakikada 20 saniyelik göz molası, her 30 dakikada 5 dakikalık hareket molası için sesli hatırlatıcı.",
     "mola-zamanlayicisi.html", SELF8_CSS, MZ_BODY, MZ_JS,
     seo_title="Masa Başı Mola Zamanlayıcısı: 20-20-20 Göz Molası ve Hareket Molası | İhsan Eren",
     faq_items=MZ_FAQ)

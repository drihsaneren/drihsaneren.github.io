# -*- coding: utf-8 -*-
S = open('site/index.html', encoding='utf-8').read()

CSS = '''  /* hızlı longevity testi */
  .qt{margin-top:clamp(32px,6vw,52px);border:1px solid var(--line-strong);border-radius:16px;background:radial-gradient(120% 90% at 100% 0%, rgba(226,171,71,.10), transparent 55%),var(--ground-2);padding:clamp(18px,4vw,32px);max-width:880px}
  .qt:not(.js){display:none}
  .qt .eyebrow{color:var(--foil)}
  .qt h3{font-size:clamp(23px,3.6vw,30px);margin:6px 0 8px;line-height:1.2}
  .qt-lede{margin:0;color:var(--ink-soft);max-width:60ch}
  .qt-bar{height:4px;border-radius:2px;background:var(--line);margin:20px 0 22px;overflow:hidden}
  .qt-bar span{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--sage),var(--gold));transition:width .4s ease}
  .qt-step{display:none;border:0;margin:0;padding:0;min-width:0}
  .qt-step.on{display:block;animation:qtin .35s ease}
  @keyframes qtin{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
  .qt-step legend{padding:0;font-family:var(--display);font-size:clamp(20px,3vw,24px);color:var(--ink);margin-bottom:8px;line-height:1.25}
  .qt-step legend .k{display:block;font-family:var(--body);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--foil);font-weight:600;margin-bottom:4px}
  .qt-how{margin:0 0 16px;color:var(--ink-soft);font-size:15px;max-width:62ch}
  .qt-val{font-family:var(--display);font-size:clamp(34px,6vw,44px);color:var(--gold);line-height:1;font-variant-numeric:tabular-nums}
  .qt-val small{font-family:var(--body);font-size:15px;color:var(--muted);margin-left:6px}
  .qt input[type=range]{width:100%;max-width:520px;accent-color:var(--gold);height:28px;margin:10px 0 2px;display:block}
  .qt-scale{display:flex;justify-content:space-between;max-width:520px;font-size:12px;color:var(--muted)}
  .qt-row{display:flex;flex-wrap:wrap;align-items:center;gap:12px;margin-top:12px}
  .qt-check{display:inline-flex;align-items:center;gap:8px;font-size:15px;color:var(--ink-soft);cursor:pointer}
  .qt-check input{accent-color:var(--gold);width:18px;height:18px}
  .qt-opts{display:grid;gap:10px;max-width:560px}
  .qt-opt{display:flex;align-items:center;gap:12px;padding:12px 14px;border:1px solid var(--line);border-radius:12px;cursor:pointer;color:var(--ink);transition:border-color .2s,background .2s}
  .qt-opt:hover{border-color:var(--line-strong)}
  .qt-opt input{position:absolute;opacity:0;pointer-events:none}
  .qt-opt .dot{flex:none;width:18px;height:18px;border-radius:50%;border:1.5px solid var(--foil);display:grid;place-items:center}
  .qt-opt input:checked + .dot::after{content:"";width:9px;height:9px;border-radius:50%;background:var(--gold)}
  .qt-opt:has(input:checked){border-color:var(--foil);background:rgba(216,178,94,.08)}
  .qt-opt:has(input:focus-visible){outline:2px solid var(--gold);outline-offset:2px}
  .qt-note{margin:14px 0 0;font-size:13px;color:var(--muted);max-width:62ch}
  .qt-safe{margin:14px 0 0;padding:0;list-style:none;display:grid;gap:6px;font-size:14px;color:var(--ink-soft);max-width:62ch}
  .qt-safe li{position:relative;padding-left:16px}
  .qt-safe li::before{content:"";position:absolute;left:2px;top:.62em;width:6px;height:6px;border-radius:50%;background:var(--gold)}
  .qt-nav{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px;align-items:center}
  .qt button.cta{font:inherit;font-weight:600;font-size:15px;cursor:pointer}
  .qt button.cta[disabled]{opacity:.45;cursor:not-allowed}
  .qt .sw{font:inherit;font-size:14px;cursor:pointer;padding:9px 16px;border-radius:999px;border:1px solid var(--foil);background:transparent;color:var(--foil);font-variant-numeric:tabular-nums;min-width:150px}
  .qt .sw.run{background:var(--gold);color:var(--ground);border-color:var(--gold)}
  .qt-res-head{display:flex;align-items:center;gap:14px;margin-bottom:10px}
  .qt-badge{flex:none;width:52px;height:52px;border-radius:50%;display:grid;place-items:center;font-family:var(--display);font-size:22px;color:var(--ground)}
  .qt-badge.g{background:#8fa476}.qt-badge.m{background:var(--gold)}.qt-badge.l{background:#c96b5a}
  .qt-res-head h4{margin:0;font-family:var(--display);font-weight:400;font-size:clamp(22px,3.4vw,28px);line-height:1.2}
  .qt-res-text{margin:0 0 16px;color:var(--ink-soft);max-width:62ch}
  .qt-list{list-style:none;margin:0 0 6px;padding:0;display:grid;gap:0;max-width:680px}
  .qt-list li{display:grid;grid-template-columns:14px minmax(0,1fr);gap:12px;padding:12px 0;border-top:1px solid var(--line)}
  .qt-list li:last-child{border-bottom:1px solid var(--line)}
  .qt-list i{width:10px;height:10px;border-radius:50%;margin-top:.5em}
  .qt-list i.g{background:#8fa476}.qt-list i.m{background:var(--gold)}.qt-list i.l{background:#c96b5a}.qt-list i.n{background:var(--line-strong)}
  .qt-list b{display:block;font-weight:600;color:var(--ink)}
  .qt-list span{font-size:14px;color:var(--ink-soft)}
  .qt-src{margin-top:14px;font-size:13px;color:var(--muted)}
  .qt-src summary{cursor:pointer;color:var(--ink-soft)}
  .qt-src ol{margin:8px 0 0;padding-left:18px;display:grid;gap:4px}
  .qt-src a{color:var(--ink-soft)}
'''
anchor = '  /* logo story */'
assert S.count(anchor) == 1
S = S.replace(anchor, CSS + anchor)

def opt(name, val, text):
    return f'<label class="qt-opt"><input type="radio" name="{name}" value="{val}"><span class="dot"></span><span>{text}</span></label>'

HTML = f'''
      <div class="qt" id="hizli-test">
        <p class="eyebrow">Hızlı test</p>
        <h3>Bedeniniz kaç yaşında gösteriyor?</h3>
        <p class="qt-lede">Evde 2–3 dakikada yapabileceğiniz dört basit test. Kas gücü, denge, günlük hareket ve kondisyon; bilimsel çalışmalarda uzun ve sağlıklı yaşamla ilişkili bulunan dört gösterge.</p>
        <div class="qt-bar" aria-hidden="true"><span id="qt-bar"></span></div>
        <form id="qt-form" novalidate>
          <fieldset class="qt-step on" data-s="0">
            <legend><span class="k">Başlarken</span>Yaşınız</legend>
            <div class="qt-val"><span id="qt-age-v">45</span><small>yaş</small></div>
            <input type="range" id="qt-age" min="18" max="90" step="1" value="45" aria-label="Yaşınız">
            <div class="qt-scale"><span>18</span><span>90</span></div>
            <ul class="qt-safe">
              <li>Testleri sağlam bir sandalye ve tutunabileceğiniz bir duvar ya da masa yanında yapın.</li>
              <li>Baş dönmesi, göğüs ağrısı ya da nefes darlığı olursa hemen durun.</li>
              <li>Kalp hastalığınız varsa merdiven testini atlayın.</li>
            </ul>
            <div class="qt-nav"><button type="button" class="cta" data-next>Teste başla</button></div>
          </fieldset>

          <fieldset class="qt-step" data-s="1">
            <legend><span class="k">1 / 4 · Kas gücü</legend>Sandalyeden 5 kez kalkıp oturun</legend>
            <p class="qt-how">Kollarınız göğsünüzde çapraz, sırtı duvara dayalı sağlam bir sandalyeye oturun. Kollarınızdan destek almadan olabildiğince hızlı 5 kez tam kalkıp oturun. Aşağıdaki kronometreyi kullanabilirsiniz.</p>
            <div class="qt-val"><span id="qt-sts-v">10,0</span><small>saniye</small></div>
            <input type="range" id="qt-sts" min="4" max="30" step="0.1" value="10" aria-label="5 kez kalkıp oturma süresi (saniye)">
            <div class="qt-scale"><span>4 sn</span><span>30 sn</span></div>
            <div class="qt-row">
              <button type="button" class="sw" id="qt-sw" aria-live="polite">Kronometreyi başlat</button>
              <label class="qt-check"><input type="checkbox" id="qt-sts-no"> Kollarımdan destek almadan yapamadım</label>
            </div>
            <div class="qt-nav"><button type="button" class="cta ghost" data-prev>Geri</button><button type="button" class="cta" data-next>Devam</button></div>
          </fieldset>

          <fieldset class="qt-step" data-s="2">
            <legend><span class="k">2 / 4 · Denge</span>Tek ayak üzerinde 10 saniye durun</legend>
            <p class="qt-how">Duvarın yanında durun; kollarınız yanda, gözleriniz karşıda olsun. Kaldırdığınız ayağın ucunu diğer bacağınızın baldırının arkasına koyun. Her ayak için 3 deneme hakkınız var.</p>
            <div class="qt-row" style="margin:0 0 14px"><button type="button" class="sw" id="qt-cd">10 saniye say</button></div>
            <div class="qt-opts">
              {opt("bal", "2", "İki ayağımda da 10 saniye durabildim")}
              {opt("bal", "1", "Yalnızca bir ayağımda durabildim")}
              {opt("bal", "0", "İkisinde de 10 saniye duramadım")}
            </div>
            <div class="qt-nav"><button type="button" class="cta ghost" data-prev>Geri</button><button type="button" class="cta" data-next data-need="bal">Devam</button></div>
          </fieldset>

          <fieldset class="qt-step" data-s="3">
            <legend><span class="k">3 / 4 · Günlük hareket</span>Günde ortalama kaç adım atıyorsunuz?</legend>
            <p class="qt-how">Telefonunuzun sağlık uygulamasındaki son haftanın ortalamasına bakabilirsiniz. Bilmiyorsanız tahmin edin: 30 dakikalık tempolu bir yürüyüş yaklaşık 3.000–4.000 adımdır.</p>
            <div class="qt-val"><span id="qt-steps-v">5.000</span><small>adım / gün</small></div>
            <input type="range" id="qt-steps" min="0" max="15000" step="500" value="5000" aria-label="Günlük ortalama adım sayısı">
            <div class="qt-scale"><span>0</span><span>15.000+</span></div>
            <div class="qt-nav"><button type="button" class="cta ghost" data-prev>Geri</button><button type="button" class="cta" data-next>Devam</button></div>
          </fieldset>

          <fieldset class="qt-step" data-s="4">
            <legend><span class="k">4 / 4 · Kondisyon</span>Dört kat merdiveni ne kadar sürede çıkarsınız?</legend>
            <p class="qt-how">Yaklaşık 60 basamak; durmadan, hızlı ama koşmadan. Yakın zamanda denemediyseniz tahmininizi seçin.</p>
            <div class="qt-opts">
              {opt("stair", "2", "1 dakikadan kısa sürede")}
              {opt("stair", "1", "1 ile 1,5 dakika arasında")}
              {opt("stair", "0", "1,5 dakikadan uzun ya da durarak")}
              {opt("stair", "x", "Denemedim ya da deneyemem")}
            </div>
            <p class="qt-note">Kalp hastalığınız, göğüs ağrınız ya da nefes darlığınız varsa bu testi yapmayın; "Denemedim" seçeneğini işaretleyin.</p>
            <div class="qt-nav"><button type="button" class="cta ghost" data-prev>Geri</button><button type="button" class="cta" data-next data-need="stair">Sonucu gör</button></div>
          </fieldset>

          <fieldset class="qt-step" data-s="5" aria-live="polite">
            <legend class="sr">Sonuç</legend>
            <div class="qt-res-head"><span class="qt-badge" id="qt-badge"></span><h4 id="qt-title"></h4></div>
            <p class="qt-res-text" id="qt-text"></p>
            <ul class="qt-list" id="qt-list"></ul>
            <div class="qt-nav">
              <a class="cta" id="qt-wa" href="#" target="_blank" rel="noopener">Evde ayrıntılı analiz için yazın <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg></a>
              <button type="button" class="cta ghost" id="qt-again">Testi yeniden yap</button>
            </div>
            <p class="qt-note">Bu test tanı koymaz, bilgilendirme amaçlıdır ve kaba bir tahmin verir. Kesin değerlendirme; kuvvet, güç, denge, yürüyüş ve esneklik ölçümleriyle yapılan ayrıntılı analizle yapılır.</p>
            <details class="qt-src"><summary>Testlerin bilimsel dayanağı</summary>
              <ol>
                <li>Bohannon RW. Reference values for the five-repetition sit-to-stand test. Percept Mot Skills. 2006;103(1):215-222.</li>
                <li>Tiedemann A, et al. Age Ageing. 2008 · Buatois S, et al. J Am Geriatr Soc. 2008 (5 kez kalkıp oturma ve düşme riski).</li>
                <li>Araújo CG, et al. <a href="https://www.bristol.ac.uk/news/2022/june/tne-second-one-legged-stance.html" target="_blank" rel="noopener">Successful 10-second one-legged stance performance predicts survival in middle-aged and older individuals</a>. Br J Sports Med. 2022.</li>
                <li>Paluch AE, et al. <a href="https://www.thelancet.com/journals/lanpub/article/PIIS2468-2667(21)00302-9/fulltext" target="_blank" rel="noopener">Daily steps and all-cause mortality: a meta-analysis of 15 international cohorts</a>. Lancet Public Health. 2022;7(3):e219-e228.</li>
                <li>Peteiro J. <a href="https://www.sciencedaily.com/releases/2020/12/201211083104.htm" target="_blank" rel="noopener">Merdiven testi ve kalp sağlığı</a>. ESC EACVI Best of Imaging 2020.</li>
              </ol>
            </details>
          </fieldset>
        </form>
      </div>
'''
# fix a typo-safe legend for step 1 (closing span)
HTML = HTML.replace('<span class="k">1 / 4 · Kas gücü</legend>', '<span class="k">1 / 4 · Kas gücü</span>')
a = S.index('<section id="analiz">'); b = S.index('<section id="ornek-plan">')
sec = S[a:b]
end = sec.rindex('    </div>\n  </section>')
sec = sec[:end] + HTML + sec[end:]
# giriş paragrafına teste bağlantı
sec = sec.replace('Sonuca göre ona özel, animasyonlu bir egzersiz reçetesi veriyoruz.</p>',
                  'Sonuca göre ona özel, animasyonlu bir egzersiz reçetesi veriyoruz. <a href="#hizli-test">2 dakikalık hızlı testi deneyin ↓</a></p>', 1)
S = S[:a] + sec + S[b:]

JS = r'''<script>
(function(){
  var box = document.getElementById('hizli-test'); if (!box) return;
  box.classList.add('js');
  var WA = '905538815568';
  var steps = [].slice.call(box.querySelectorAll('.qt-step')), cur = 0, bar = document.getElementById('qt-bar');
  var $ = function(id){ return document.getElementById(id); };
  var fmt1 = function(x){ return x.toFixed(1).replace('.', ','); };
  var fmtN = function(x){ return x.toLocaleString('tr-TR'); };
  var age = $('qt-age'), sts = $('qt-sts'), stsNo = $('qt-sts-no'), stp = $('qt-steps');
  age.oninput = function(){ $('qt-age-v').textContent = age.value; };
  sts.oninput = function(){ $('qt-sts-v').textContent = fmt1(+sts.value); };
  stp.oninput = function(){ $('qt-steps-v').textContent = (+stp.value >= 15000 ? '15.000+' : fmtN(+stp.value)); };
  function radio(n){ var r = box.querySelector('input[name="' + n + '"]:checked'); return r ? r.value : null; }
  function show(i){
    cur = i;
    steps.forEach(function(s, k){ s.classList.toggle('on', k === i); });
    bar.style.width = (i / 5 * 100) + '%';
    if (i > 0) { var top = box.getBoundingClientRect().top; if (top < 0) box.scrollIntoView({behavior:'smooth', block:'start'}); }
    updNext();
  }
  function updNext(){
    var s = steps[cur], n = s.querySelector('[data-need]');
    if (n) n.disabled = !radio(n.getAttribute('data-need'));
  }
  box.addEventListener('change', updNext);
  box.querySelectorAll('[data-next]').forEach(function(b){ b.onclick = function(){ if (cur === 4) result(); show(cur + 1); }; });
  box.querySelectorAll('[data-prev]').forEach(function(b){ b.onclick = function(){ show(cur - 1); }; });
  $('qt-again').onclick = function(){ box.querySelectorAll('input[type=radio]').forEach(function(r){ r.checked = false; }); stsNo.checked = false; show(0); };

  // kronometre (otur-kalk)
  var sw = $('qt-sw'), t0 = 0, tm = null;
  sw.onclick = function(){
    if (tm){ clearInterval(tm); tm = null; var t = (Date.now() - t0) / 1000; t = Math.min(30, Math.max(4, Math.round(t * 10) / 10));
      sts.value = t; sts.oninput(); sw.classList.remove('run'); sw.textContent = 'Yeniden ölç'; return; }
    t0 = Date.now(); sw.classList.add('run');
    tm = setInterval(function(){ sw.textContent = 'Durdur · ' + fmt1((Date.now() - t0) / 1000) + ' sn'; }, 100);
  };
  // 10 saniye geri sayım (denge)
  var cd = $('qt-cd'), ct = null;
  cd.onclick = function(){
    if (ct){ clearInterval(ct); ct = null; cd.classList.remove('run'); cd.textContent = '10 saniye say'; return; }
    var end = Date.now() + 10000; cd.classList.add('run');
    ct = setInterval(function(){ var r = Math.ceil((end - Date.now()) / 1000);
      if (r <= 0){ clearInterval(ct); ct = null; cd.classList.remove('run'); cd.textContent = '10 saniye tamam ✓ Tekrar say'; }
      else cd.textContent = r + ' · durdurmak için dokunun'; }, 100);
  };

  function result(){
    var a = +age.value, t = +sts.value, no = stsNo.checked, bal = +radio('bal'), st = radio('stair'), s = +stp.value;
    var norm = a < 50 ? 6.2 : a < 60 ? 7.1 : a < 70 ? 11.4 : a < 80 ? 12.6 : 14.8;
    var p1 = no ? 0 : (t <= norm ? 2 : t <= norm * 1.3 ? 1 : 0);
    var tgt = a >= 60 ? 6000 : 8000, mid = a >= 60 ? 3500 : 5000, tgtTxt = a >= 60 ? '6.000–8.000' : '8.000–10.000';
    var p3 = s >= tgt ? 2 : s >= mid ? 1 : 0;
    var p4 = st === 'x' ? null : +st;
    var pts = [p1, bal, p3].concat(p4 === null ? [] : [p4]);
    var ratio = pts.reduce(function(x, y){ return x + y; }, 0) / (pts.length * 2);
    var cls = function(p){ return p === null ? 'n' : p === 2 ? 'g' : p === 1 ? 'm' : 'l'; };
    var band = ratio >= .75 ? 'g' : ratio >= .45 ? 'm' : 'l';
    var T = {
      g: ['Güçlü görünüyorsunuz', 'Sonuçlarınız kas gücü, denge ve kondisyon açısından yaşıtlarınızla aynı düzeyde ya da daha iyi. Fonksiyonel yaşınız takvim yaşınızdan genç olabilir. Bunu kesin olarak ölçmek ve korumak için evde ayrıntılı longevity analizi yapabiliriz.'],
      m: ['Gelişime açık alanlar var', 'Bazı sonuçlarınız yaşıtlarınızın gerisinde; fonksiyonel yaşınız takvim yaşınızdan ileride olabilir. İyi haber: kas gücü ve denge her yaşta, birkaç haftalık düzenli egzersizle belirgin şekilde gelişebilir.'],
      l: ['Dikkat edilmesi gereken sonuçlar', 'Sonuçlarınız kas gücü, denge ya da kondisyon açısından dikkat gerektiren alanlar gösteriyor. Düşme riskini azaltmak ve kondisyonunuzu geri kazanmak için kişiye özel bir program iyi bir başlangıç olur.']
    };
    $('qt-badge').className = 'qt-badge ' + band; $('qt-badge').textContent = band === 'g' ? '✓' : band === 'm' ? '↗' : '!';
    $('qt-title').textContent = T[band][0]; $('qt-text').textContent = T[band][1];
    var stsTxt = no ? 'Kol desteği olmadan yapılamadı' : fmt1(t) + ' sn';
    var fall = (a >= 65 && (no || t >= 12)) ? ' 65 yaş üstünde 12 saniye ve üzeri, düşme riskinin ayrıca değerlendirilmesi gerektiğine işaret eder.' : '';
    var balTxt = ['İkisinde de 10 saniye duramadınız', 'Yalnızca bir ayakta 10 saniye', 'İki ayakta da 10 saniye'][bal];
    var stTxt = st === 'x' ? 'Değerlendirilmedi' : ['1,5 dakikadan uzun', '1–1,5 dakika', '1 dakikadan kısa'][p4];
    var rows = [
      [cls(p1), 'Kas gücü · 5 kez kalkıp oturma: ' + stsTxt, 'Yaş grubunuzun ortalaması yaklaşık ' + fmt1(norm) + ' sn.' + fall],
      [cls(bal), 'Denge · tek ayak: ' + balTxt, bal === 2 ? 'Orta ve ileri yaşta 10 saniye tek ayak üzerinde durabilmek iyi bir işarettir.' : 'Orta ve ileri yaşta 10 saniye tek ayak üzerinde duramamak, bir izlem çalışmasında daha yüksek ölüm riskiyle ilişkili bulundu. Denge, egzersizle hızla gelişir.'],
      [cls(p3), 'Günlük hareket: ' + (s >= 15000 ? '15.000+' : fmtN(s)) + ' adım', 'Yaşınız için faydanın en yüksek olduğu aralık günde ' + tgtTxt + ' adım.'],
      [cls(p4), 'Kondisyon · 4 kat merdiven: ' + stTxt, p4 === null ? 'Bu test sonuca katılmadı.' : '1 dakikanın altı iyi kondisyonu, 1,5 dakikanın üstü geliştirilmesi gereken bir kondisyonu gösterir.']
    ];
    $('qt-list').innerHTML = rows.map(function(r){ return '<li><i class="' + r[0] + '"></i><div><b>' + r[1] + '</b><span>' + r[2] + '</span></div></li>'; }).join('');
    var msg = 'Merhaba, sitedeki hızlı fonksiyonel testi yaptım (' + a + ' yaş). Otur-kalk: ' + stsTxt + '; tek ayak: ' + balTxt.toLowerCase() + '; günlük adım: ~' + (s >= 15000 ? '15.000+' : fmtN(s)) + '; merdiven: ' + stTxt.toLowerCase() + '. Sonuç: ' + T[band][0] + '. Evde ayrıntılı longevity analizi hakkında bilgi almak istiyorum.';
    $('qt-wa').href = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(msg);
  }
  show(0);
})();
</script>
'''
S = S.rstrip('\n') + '\n' + JS
open('site/index.html', 'w', encoding='utf-8').write(S)
print('ok')

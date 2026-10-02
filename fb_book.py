# -*- coding: utf-8 -*-
# "Tanışma görüşmesi" bölümü: gün + saat aralığı + görüşme şekli seçilir, WhatsApp ya da
# e-postayla hazır mesaj gider. Calendly / Google Takvim bağlantısı gelince data-embed
# doldurulur ve aynı yerde gerçek takvim açılır.
p = "site/index.html"
s = open(p, encoding="utf-8").read()


def rep(old, new, cnt=1):
    global s
    assert s.count(old) == cnt, (old[:80], s.count(old))
    s = s.replace(old, new)


CHK = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="11" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M7 12.4l3.2 3.1L17 8.8" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>'
CAL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/><circle cx="12" cy="15" r="1.4" fill="currentColor" stroke="none"/></svg>'
PARTS = [("Sabah", "9-12"), ("Öğleden sonra", "12-18"), ("Akşam", "18-21")]
parts = "\n".join(f'              <label><input type="radio" name="bp" value="{v}"{" checked" if i == 0 else ""}><span>{n}</span></label>' for i, (n, v) in enumerate(PARTS))

SEC = f'''  <section id="tanisma" class="book-sec">
    <div class="wrap">
      <div class="book">
        <div class="book-intro">
          <p class="eyebrow">Ücretsiz ön görüşme</p>
          <h2>Önce tanışalım</h2>
          <p class="intro">Kısa ve ücretsiz bir ön görüşmede neler yaşadığınızı dinleyeyim, evde nasıl bir yol izleyebileceğimizi birlikte konuşalım. Size uygun günü ve saat aralığını seçin; onaylayıp size dönüş yapayım.</p>
          <ul class="book-pts">
            <li>{CHK}<span>Ücretsiz, yarım saatlik bir sohbet; telefonla ya da görüntülü</span></li>
            <li>{CHK}<span>Şikâyetinizi ve hedefinizi birlikte konuşuruz</span></li>
            <li>{CHK}<span>Uygunsa ilk ev ziyaretini planlarız</span></li>
          </ul>
        </div>
        <div class="book-card" id="book" data-embed="">
          <div class="book-head">{CAL}<div><b>Zaman seçin</b><span>Seçtiğiniz zaman bir taleptir; onayladığımda kesinleşir.</span></div></div>
          <form class="book-form" id="book-form" autocomplete="off" novalidate>
            <p class="book-step"><span>1</span>Gün</p>
            <div class="book-days" id="book-days" role="radiogroup" aria-label="Gün"></div>
            <p class="book-step"><span>2</span>Saat <small>· 30 dakika</small></p>
            <div class="book-parts" role="radiogroup" aria-label="Günün bölümü">
{parts}
            </div>
            <div class="book-slots" id="book-slots" role="radiogroup" aria-label="Saat"></div>
            <p class="book-step"><span>3</span>Görüşme şekli</p>
            <div class="book-modes" role="radiogroup" aria-label="Görüşme şekli">
              <label><input type="radio" name="bm" value="1" checked><span>Telefon</span></label>
              <label><input type="radio" name="bm" value="2"><span>Görüntülü</span></label>
            </div>
            <p class="book-sum" id="book-sum" aria-live="polite"><span class="book-hint">Bir gün ve saat seçin.</span><span class="book-sel" hidden><b id="bs-d"></b> · <b id="bs-t"></b> · <span id="bs-m"></span></span></p>
            <p class="book-add" id="book-add" hidden>Günlük Hareket Skalası sonucunuz da mesaja eklenecek.</p>
            <div class="book-acts">
              <a class="cta" id="book-wa" href="https://wa.me/905538815568" target="_blank" rel="noopener" aria-disabled="true">WhatsApp’tan gönder {ARR}</a>
              <a class="cta ghost" id="book-mail" href="mailto:ihsneren@gmail.com" aria-disabled="true">E-postayla gönder</a>
            </div>
            <p class="book-tpl" hidden>Merhaba, ücretsiz ön görüşme için {{day}}, {{time}} arası bana uygun. Görüşme şekli: {{mode}}.</p>
            <p class="book-subj" hidden>Ücretsiz ön görüşme</p>
            <p class="book-tpl2" hidden>Günlük Hareket Skalası sonucum: {{band}} bölge, {{score}}/{{max}} puan.</p>
            <p class="book-tpl3" hidden>En çok zorlandığım anlar: {{list}}.</p>
          </form>
          <p class="book-nojs">Size uygun günü ve saati WhatsApp’tan ya da e-postayla yazabilirsiniz.</p>
        </div>
      </div>
    </div>
  </section>

'''
rep('  <section id="iletisim" class="contact-sec">', SEC + '  <section id="iletisim" class="contact-sec">')

CSS = r'''  /* tanışma görüşmesi */
  .book-sec{background:radial-gradient(90% 70% at 100% 0%,rgba(226,171,71,.08),transparent 60%),var(--ground)}
  .book{display:grid;grid-template-columns:minmax(0,1fr);gap:28px}
  .book-card,.book-intro{min-width:0}
  @media (min-width:900px){.book{grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr);gap:52px;align-items:center}}
  .book-intro h2{font-size:clamp(28px,6.4vw,40px);line-height:1.12;margin:8px 0 12px}
  .book-intro .intro{margin:0 0 18px;color:var(--ink-soft);max-width:50ch}
  .book-pts{list-style:none;margin:0;padding:0;display:grid;gap:10px}
  .book-pts li{display:flex;align-items:flex-start;gap:10px;color:var(--ink)}
  .book-pts svg{flex:none;width:20px;height:20px;color:var(--foil);margin-top:2px}
  .book-card{position:relative;border:1px solid var(--line-strong);border-radius:18px;padding:clamp(16px,3.4vw,26px);
    background:radial-gradient(120% 80% at 0% 0%,rgba(143,164,118,.12),transparent 60%),var(--ground-2);box-shadow:0 20px 56px rgba(0,0,0,.3)}
  .book-head{display:flex;align-items:center;gap:12px;margin:0 0 18px}
  .book-head > svg{flex:none;width:42px;height:42px;padding:9px;border-radius:12px;color:var(--ground);background:var(--foil);box-shadow:0 0 18px rgba(226,171,71,.35)}
  .book-head b{display:block;font-family:var(--display);font-weight:400;font-size:22px;color:var(--ink);line-height:1.2}
  .book-head span{display:block;font-size:13.5px;color:var(--muted);line-height:1.4}
  .book-form{margin:0}
  .book-card:not(.js) .book-form{display:none}
  .book-card.js .book-nojs{display:none}
  .book-nojs{margin:0;color:var(--ink-soft)}
  .book-step{margin:0 0 10px;display:flex;align-items:center;gap:10px;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);font-weight:600}
  .book-step span{width:22px;height:22px;border-radius:50%;display:grid;place-items:center;background:rgba(216,178,94,.16);color:var(--foil);font-size:12px;letter-spacing:0;border:1px solid var(--line-strong)}
  .book-days{display:flex;gap:8px;overflow-x:auto;scroll-snap-type:x proximity;padding:3px 3px 12px;margin:0 -3px 12px;scrollbar-width:thin;scrollbar-color:rgba(216,178,94,.45) transparent;overscroll-behavior-x:contain;
    -webkit-mask-image:linear-gradient(90deg,#000 calc(100% - 36px),transparent);mask-image:linear-gradient(90deg,#000 calc(100% - 36px),transparent)}
  .book-form label{position:relative}
  .book-days label{flex:none;scroll-snap-align:start}
  .book-form input{position:absolute;opacity:0;pointer-events:none;width:1px;height:1px}
  .book-form label > span{cursor:pointer;border:1px solid var(--line);background:rgba(236,229,207,.03);transition:border-color .2s,background .2s,box-shadow .25s,transform .2s}
  .book-form label > span:hover{border-color:var(--line-strong)}
  .book-form input:checked + span{border-color:var(--foil);background:rgba(216,178,94,.13);box-shadow:0 0 0 1px var(--foil),0 0 20px rgba(226,171,71,.22)}
  .book-form input:focus-visible + span{outline:2px solid var(--gold);outline-offset:2px}
  .book-days label > span{display:grid;justify-items:center;width:62px;padding:8px 0 7px;border-radius:14px;line-height:1.15}
  .book-days .wd{font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}
  .book-days .dn{font-family:var(--display);font-size:25px;color:var(--ink);margin:2px 0 1px}
  .book-days .mo{font-size:12px;color:var(--ink-soft)}
  .book-days input:checked + span .dn{color:var(--gold)}
  .book-step small{font-size:11px;letter-spacing:.08em;color:var(--muted);font-weight:500}
  .book-parts{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 10px}
  .book-parts label > span{display:inline-flex;padding:6px 14px;border-radius:999px;font-size:13.5px;color:var(--ink-soft)}
  .book-parts input:checked + span{color:var(--ink)}
  .book-slots{display:grid;grid-template-columns:repeat(auto-fill,minmax(74px,1fr));gap:8px;margin:0 0 16px;min-height:44px}
  .book-slots label > span{display:block;padding:9px 0;border-radius:10px;text-align:center;font-size:14.5px;font-weight:600;color:var(--ink);font-variant-numeric:tabular-nums}
  .book-slots input:checked + span{color:var(--gold)}
  .book-modes{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 16px}
  .book-modes label > span{display:inline-flex;padding:8px 18px;border-radius:999px;font-size:14.5px;color:var(--ink)}
  .book-sum{margin:0 0 14px;padding:12px 14px;border-radius:12px;border:1px dashed var(--line-strong);color:var(--ink-soft);font-size:14.5px;min-height:48px;display:flex;align-items:center}
  .book-sum b{color:var(--gold);font-weight:600}
  .book-add{margin:-4px 0 14px;font-size:13.5px;color:var(--foil)}
  .book-acts{display:flex;flex-wrap:wrap;gap:10px}
  .book-acts .cta[aria-disabled="true"]{opacity:.42;cursor:not-allowed}
  .book-card iframe{display:block;width:100%;height:720px;border:0;border-radius:12px;background:#fff}
'''
rep("  /* contact */", CSS + "  /* contact */")

# hero: ikinci düğme
rep('''    <div class="hero-ctas">
      <a class="cta" href="https://wa.me/905538815568?text=Merhaba%2C%20evde%20fizyoterapi%20i%C3%A7in%20seans%20planlamak%20istiyorum." target="_blank" rel="noopener">WhatsApp'tan seans planla''',
    '''    <div class="hero-ctas">
      <a class="cta" href="https://wa.me/905538815568?text=Merhaba%2C%20evde%20fizyoterapi%20i%C3%A7in%20seans%20planlamak%20istiyorum." target="_blank" rel="noopener">WhatsApp'tan seans planla''')
i = s.index('    <div class="hero-ctas">')
j = s.index('    </div>', i)
s = s[:j] + '      <a class="cta ghost" href="#tanisma">Ücretsiz ön görüşme</a>\n' + s[j:]

JS = r'''<script>
(function(){
  var card = document.getElementById('book'); if (!card) return;
  var url = card.getAttribute('data-embed');
  if (url) {  // Calendly / Google Takvim randevu sayfası bağlanınca doğrudan takvim açılır
    var f = document.createElement('iframe'); f.src = url; f.loading = 'lazy'; f.title = card.querySelector('.book-head b').textContent;
    card.querySelector('.book-form').replaceWith(f); card.querySelector('.book-nojs').remove(); card.classList.add('js'); return;
  }
  card.classList.add('js');
  var lang = document.documentElement.lang === 'en' ? 'en-GB' : 'tr-TR';
  var days = document.getElementById('book-days'), today = new Date();
  var fWd = new Intl.DateTimeFormat(lang, {weekday: 'short'}), fMo = new Intl.DateTimeFormat(lang, {month: 'short'}),
      fLong = new Intl.DateTimeFormat(lang, {weekday: 'long', day: 'numeric', month: 'long'});
  for (var i = 1; i <= 14; i++) {
    var d = new Date(today.getFullYear(), today.getMonth(), today.getDate() + i);
    var l = document.createElement('label');
    l.innerHTML = '<input type="radio" name="bd"><span><span class="wd"></span><span class="dn"></span><span class="mo"></span></span>';
    var inp = l.querySelector('input'); inp.value = fLong.format(d);
    l.querySelector('.wd').textContent = fWd.format(d).replace('.', '');
    l.querySelector('.dn').textContent = d.getDate();
    l.querySelector('.mo').textContent = fMo.format(d).replace('.', '');
    days.appendChild(l);
  }
  var form = document.getElementById('book-form'), wa = document.getElementById('book-wa'), ml = document.getElementById('book-mail');
  var tpl = card.querySelector('.book-tpl').textContent.trim(), subj = card.querySelector('.book-subj').textContent.trim(),
      tpl2 = card.querySelector('.book-tpl2').textContent.trim(), tpl3 = card.querySelector('.book-tpl3').textContent.trim(), add = document.getElementById('book-add');
  function val(n){ var r = form.querySelector('input[name="' + n + '"]:checked'); return r; }
  function upd(){
    var d = val('bd'), t = selT, m = val('bm');
    var ok = !!(d && t);
    var mode = m ? m.nextElementSibling.textContent.trim() : '';
    card.querySelector('.book-hint').hidden = ok; card.querySelector('.book-sel').hidden = !ok;
    [wa, ml].forEach(function(a){ a.setAttribute('aria-disabled', ok ? 'false' : 'true'); });
    var sk = window.drSkala || null;
    add.hidden = !sk;
    if (!ok) return;
    document.getElementById('bs-d').textContent = d.value;
    document.getElementById('bs-t').textContent = t;
    document.getElementById('bs-m').textContent = mode;
    var msg = tpl.replace('{day}', d.value).replace('{time}', t).replace('{mode}', mode.toLocaleLowerCase(lang));
    if (sk) { msg += ' ' + tpl2.replace('{band}', sk.band).replace('{score}', sk.score).replace('{max}', sk.max);
      if (sk.top.length) msg += ' ' + tpl3.replace('{list}', sk.top.join(', ')); }
    wa.href = 'https://wa.me/905538815568?text=' + encodeURIComponent(msg);
    ml.href = 'mailto:ihsneren@gmail.com?subject=' + encodeURIComponent(subj) + '&body=' + encodeURIComponent(msg);
  }
  // 30 dakikalık saatler: seçilen gün bölümüne göre
  var slots = document.getElementById('book-slots'), selT = null;
  function pad(n){ return (n < 10 ? '0' : '') + n; }
  function hm(m){ return pad(Math.floor(m / 60)) + ':' + pad(m % 60); }
  function drawSlots(){
    var pv = (val('bp') || {value: '9-12'}).value.split('-'), a = +pv[0] * 60, b = +pv[1] * 60, html = '';
    for (var m = a; m < b; m += 30) {
      var v = hm(m) + '–' + hm(m + 30);
      html += '<label><input type="radio" name="bt" value="' + v + '"' + (v === selT ? ' checked' : '') + '><span>' + hm(m) + '</span></label>';
    }
    slots.innerHTML = html;
  }
  form.addEventListener('change', function(e){
    if (e.target.name === 'bp') drawSlots();
    if (e.target.name === 'bt') selT = e.target.value;
    upd();
  });
  drawSlots(); document.addEventListener('dr-skala', upd);
  [wa, ml].forEach(function(a){ a.addEventListener('click', function(e){
    if (a.getAttribute('aria-disabled') === 'true') { e.preventDefault(); var h = card.querySelector('.book-hint'); h.animate && h.animate([{opacity:.3},{opacity:1}], {duration: 500}); (val('bd') ? form.querySelector('input[name="bt"]') : days.querySelector('input')).focus(); }
  }); });
  upd();
})();
</script>
'''
anchor = "<script>\n(function(){\n  var sec = document.getElementById('logo'); if (!sec) return;"
assert s.count(anchor) == 1
s = s.replace(anchor, JS + anchor, 1)
open(p, "w", encoding="utf-8").write(s)
print("ok")

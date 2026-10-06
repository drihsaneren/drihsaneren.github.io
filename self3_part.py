# -*- coding: utf-8 -*-
# Kendine iyi bak · DOST molası: Dur, Omuzlarını bırak, Seslen, Teşekkür et.
# Dört adımın her biri ayrı ayrı araştırılmış küçük bir uygulama (duyguya ad koyma, yatıştırıcı dokunuş,
# kendine adıyla ve dostça seslenme, bedenin yaptıklarına teşekkür). Sıralama bu siteye özgü; bütün olarak
# sınanmadığı sayfada açıkça yazıyor. Sonunda kişi kendine kısa bir not yazmış olur; hiçbir şey kaydedilmez.
# build_pages.py içinden exec edilir (self2_part.py'den sonra).

DOST_CSS = SELF2_CSS + """
  #dost{scroll-margin-top:70px}
  .ds{max-width:720px;margin-inline:auto}
  .ds-nav{display:flex;align-items:center;justify-content:center;margin:0 0 24px;padding:0;list-style:none}
  .ds-nav li{display:flex;align-items:center}
  .ds-nav li + li::before{content:"";width:clamp(16px,7vw,56px);height:1px;background:var(--line-strong);transition:background .4s}
  .ds-nav li.on::before,.ds-nav li.done::before{background:var(--foil)}
  .ds-nav b{width:46px;height:46px;border-radius:50%;display:grid;place-items:center;border:1px solid var(--line-strong);
    font-family:var(--display);font-weight:400;font-size:22px;line-height:1;color:var(--ink-soft);transition:background .4s,color .4s,border-color .4s,box-shadow .4s}
  .ds-nav li.done b{border-color:var(--foil);color:var(--foil)}
  .ds-nav li.on b{border-color:var(--foil);background:var(--foil);color:var(--ground);box-shadow:0 0 0 6px rgba(216,178,94,.16)}
  .ds-p{animation:ds-in .7s cubic-bezier(.2,.8,.2,1) both}
  @keyframes ds-in{from{opacity:0;transform:translateY(12px)}}
  .ds-p h3{font-family:var(--display);font-weight:400;font-size:clamp(25px,4.4vw,32px);line-height:1.15;color:var(--foil);margin:0 0 10px}
  .ds-p > .soft{margin:0 0 16px}
  .ds-echo{margin:16px 0 0;color:var(--ink);font-size:17px;animation:ds-in .6s ease both}
  .ds-lines{display:grid;gap:9px}
  .ds-lines button{all:unset;box-sizing:border-box;width:100%;cursor:pointer;padding:13px 16px;border-radius:12px;border:1px solid var(--line-strong);
    color:var(--ink);font-size:16.5px;line-height:1.4;transition:border-color .25s,background .25s,transform .25s}
  .ds-lines button:hover{border-color:var(--foil)}
  .ds-lines button[aria-pressed="true"]{border-color:var(--foil);background:rgba(216,178,94,.15);transform:translateX(3px)}
  .ds-lines button:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .ds-lab{display:block;font-size:14px;color:var(--ink-soft);margin:0 0 6px}
  .ds-name{font:inherit;font-size:17px;color:var(--ink);background:rgba(236,229,207,.06);border:1px solid var(--line-strong);border-radius:10px;
    padding:11px 14px;width:min(100%,280px);box-sizing:border-box;margin:0 0 18px}
  .ds-name:focus{outline:2px solid var(--gold);outline-offset:1px;border-color:var(--foil)}
  .ds-name::placeholder{color:var(--muted)}
  .ds-touch{display:grid;justify-items:center;gap:14px;margin:6px 0 4px;text-align:center}
  .ds-heart{position:relative;width:168px;height:168px;display:grid;place-items:center}
  .ds-heart svg.prog{position:absolute;inset:0;width:100%;height:100%;transform:rotate(-90deg)}
  .ds-heart svg.prog circle{fill:none;stroke-width:4}
  .ds-heart svg.prog .bg{stroke:rgba(236,229,207,.10)}
  .ds-heart svg.prog .fg{stroke:var(--foil);stroke-linecap:round}
  .ds-heart svg.hrt{position:absolute;width:56%;height:56%;fill:rgba(226,171,71,.20);stroke:var(--foil);stroke-width:2;stroke-linejoin:round;
    filter:drop-shadow(0 0 14px rgba(226,171,71,.25));transform-origin:50% 55%}
  .ds.beat .ds-heart svg.hrt{animation:ds-beat 5s ease-in-out infinite;fill:rgba(226,171,71,.32)}
  @keyframes ds-beat{0%,100%{transform:scale(.94)}50%{transform:scale(1.08)}}
  .ds-heart b{position:relative;font-family:var(--display);font-weight:400;font-size:30px;color:var(--ink);font-variant-numeric:tabular-nums}
  .ds-cue{margin:0;color:var(--ink);font-size:17px;min-height:1.5em}
  .ds-foot{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px;padding-top:18px;border-top:1px solid var(--line)}
  .ds-foot .cta:disabled{opacity:.4;cursor:default}
  .ds-note{position:relative;max-width:520px;margin:8px auto 22px;padding:30px 26px 24px;background:var(--paper);color:#22301c;
    border-radius:4px 14px 6px 16px;box-shadow:0 20px 44px rgba(0,0,0,.42),inset 0 0 0 1px rgba(200,150,62,.28);transform:rotate(-.7deg)}
  .ds-note::before{content:"";position:absolute;top:-9px;left:50%;width:92px;height:20px;margin-left:-46px;background:rgba(216,178,94,.55);border-radius:2px;transform:rotate(1.4deg)}
  .ds-note p{margin:0 0 11px;max-width:none;color:inherit;font-size:17.5px;line-height:1.6;opacity:0;animation:ds-ink 1s ease forwards}
  .ds-note p.hi{font-family:var(--display);font-size:25px;line-height:1.2;margin-bottom:14px;color:#3a2e12}
  .ds-note p.sig{font-family:var(--display);font-style:italic;text-align:right;margin:16px 0 0;color:#5a4a22}
  @keyframes ds-ink{from{opacity:0;transform:translateY(6px);filter:blur(2px)}to{opacity:1;transform:none;filter:none}}
  .kind .n.ltr{font-family:var(--display)}
  body.ds-on #fab{visibility:hidden!important}   /* mola sırasında telefondaki yüzen WhatsApp düğmesi araya girmesin */
  @media (prefers-reduced-motion:reduce){.ds-p,.ds-echo,.ds.beat .ds-heart svg.hrt{animation:none}.ds-note p{animation:none;opacity:1}}
"""

DOST_FAQ = [
 ("Bu, kendine acımak olmuyor mu?", "Hayır. Kendine acımak “neden hep ben” der ve insanı yalnızlaştırır. Kendine şefkat ise “bu zor ve zorlanan tek kişi ben değilim” der. Amaç kendinizi kandırmak ya da sorumluluktan kaçmak değil; kendinize, sevdiğiniz bir dosta davrandığınız kadar adil davranmak."),
 ("Elimi kalbime koymak bana tuhaf geliyor. Ne yapayım?", "Çok doğal. Çalışmada katılımcılar kendilerine uyan dokunuşu seçti; neredeyse hepsi bir elini kalbine, diğerini karnına koydu. Siz kollarınızı kavuşturup omuzlarınızı tutabilir ya da bir elinizi diğerinin içine alabilirsiniz. Kimse fark etmeden, otobüste bile yapılabilir."),
 ("Ne sıklıkta yapmalıyım?", "Bir kural yok. Mektup çalışmasında katılımcılar yedi gün üst üste yazdı; siz de bir hafta deneyip nasıl hissettiğinize bakabilirsiniz. Zor bir anın hemen ardından tek bir tur yapmak da olur."),
 ("Yaparken daha kötü hissedersem?", "Kendinize yumuşak davranmaya başladığınızda, uzun süredir ertelediğiniz duygular yüzeye çıkabilir. Molayı kısaltın, yalnızca dokunuş adımını yapın ya da ara verin. Sıkıntı sürüyorsa bunu tek başınıza taşımayın; bir ruh sağlığı uzmanıyla konuşun."),
]

_HEART = "M50 86 C22 64 8 46 8 30 C8 16 19 7 31 7 C39 7 46 12 50 20 C54 12 61 7 69 7 C81 7 92 16 92 30 C92 46 78 64 50 86Z"

DOST_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>DOST molası: kendinize dost olmanın beş dakikası</h1>
    <p class="lede">En yakın dostunuz zor bir gün geçirse ona ne söylerdiniz? Büyük ihtimalle, aynı gün kendinize söylediğinizden çok daha yumuşak bir şey. DOST molası o sesi beş dakikalığına kendinize çevirir: <strong>D</strong>ur, <strong>O</strong>muzlarını bırak, <strong>S</strong>eslen, <strong>T</strong>eşekkür et. Sonunda kendinize kısa bir not yazmış olacaksınız.</p>
    <p class="meta">Son güncelleme: 6 Ekim 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>5 dk</b><span>Dört adımın toplam süresi; gereken tek şey sessiz bir köşe</span></div>
        <div class="stat"><b>20 sn</b><span>Bir çalışmada stres hormonu yanıtını azaltan yatıştırıcı dokunuşun süresi</span></div>
        <div class="stat"><b>7 gün</b><span>Kendine dost gibi yazılan süre; ruh hâlindeki iyileşme aylarca izlendi</span></div>
        <div class="stat"><b>27 çalışma</b><span>Kendine şefkat uygulamalarını sınayan rastgele kontrollü çalışmaların derlemesi</span></div>
      </div>
    </div>
  </section>

  <section id="dost">
    <div class="wrap">
      <p class="eyebrow">Birlikte yapalım</p>
      <h2>Beş dakikalık mola</h2>
      <p class="soft">Telefonu sessize alın, rahat bir yere oturun. Acele yok; her adımda istediğiniz kadar kalabilirsiniz.</p>
      <div class="tool ds" id="ds">
        <ol class="ds-nav" aria-hidden="true"><li class="on"><b>D</b></li><li><b>O</b></li><li><b>S</b></li><li><b>T</b></li></ol>

        <div class="ds-p">
          <h3>Dur ve adını koy</h3>
          <p class="soft">Bir an durun. Şu anda içinizde en çok hangisi var? Doğru ya da yanlış cevap yok; size en yakın geleni seçin.</p>
          <div class="seg" role="group" aria-label="Şu anki duygunuz" id="ds-feel">
            <button type="button" aria-pressed="false">yorgun</button>
            <button type="button" aria-pressed="false">kaygılı</button>
            <button type="button" aria-pressed="false">kırgın</button>
            <button type="button" aria-pressed="false">öfkeli</button>
            <button type="button" aria-pressed="false">yalnız</button>
            <button type="button" aria-pressed="false">bunalmış</button>
            <button type="button" aria-pressed="false">üzgün</button>
            <button type="button" aria-pressed="false">incinmiş</button>
            <button type="button" aria-pressed="false" data-none>adını koyamıyorum</button>
          </div>
          <p class="ds-echo" id="ds-echo" aria-live="polite" hidden></p>
        </div>

        <div class="ds-p" hidden>
          <h3>Omuzlarını bırak</h3>
          <p class="soft">Omuzlarınızı kulaklarınızdan uzaklaştırın, çenenizi gevşetin. Bir elinizi kalbinizin, diğerini karnınızın üstüne koyun ve elinizin sıcaklığını hissedin. Başlat'a dokunun; 20 saniye yalnızca böyle kalın.</p>
          <div class="ds-touch">
            <div class="ds-heart">
              <svg class="prog" viewBox="0 0 200 200" aria-hidden="true"><circle class="bg" cx="100" cy="100" r="96"/><circle class="fg" id="ds-arc" cx="100" cy="100" r="96" stroke-dasharray="603.2" stroke-dashoffset="603.2"/></svg>
              <svg class="hrt" viewBox="0 0 100 100" aria-hidden="true"><path d="{_HEART}"/></svg>
              <b id="ds-sec">20</b>
            </div>
            <p class="ds-cue" id="ds-cue" aria-live="polite">Hazır olduğunuzda başlayın</p>
            <button type="button" class="cta" id="ds-touch-go">Başlat</button>
          </div>
        </div>

        <div class="ds-p" hidden>
          <h3>Seslen</h3>
          <p class="soft">En yakın dostunuz bugün sizin yerinizde olsaydı ona ne derdiniz? Şimdi aynı sesle kendinize seslenin. İsterseniz adınızı yazın, sonra size en iyi gelen cümleyi seçin.</p>
          <label class="ds-lab" for="ds-name">Adınız (isterseniz)</label>
          <input class="ds-name" id="ds-name" type="text" maxlength="24" autocomplete="given-name" placeholder="Adınız">
          <div class="ds-lines" role="group" aria-label="Kendinize söyleyeceğiniz cümle" id="ds-say">
            <button type="button" aria-pressed="false">Zor bir gün geçiriyorsun; bunu görüyorum.</button>
            <button type="button" aria-pressed="false">Elinden geleni yapıyorsun. Bugünlük bu yeter.</button>
            <button type="button" aria-pressed="false">Böyle hissetmen çok insanca. Yalnız değilsin.</button>
            <button type="button" aria-pressed="false">Yavaşlamaya hakkın var.</button>
            <button type="button" aria-pressed="false">Hata yaptın diye değerin azalmadı.</button>
          </div>
        </div>

        <div class="ds-p" hidden>
          <h3>Teşekkür et</h3>
          <p class="soft">Son adımda bedeninize dönün. Nasıl göründüğüne değil, bugün sizin için ne yaptığına bakın ve ona bir cümleyle teşekkür edin.</p>
          <div class="ds-lines" role="group" aria-label="Bedeninize teşekkür cümlesi" id="ds-body">
            <button type="button" aria-pressed="false">Beni bugün de ayağa kaldırdın.</button>
            <button type="button" aria-pressed="false">Ağrıya rağmen beni taşıdın.</button>
            <button type="button" aria-pressed="false">Sevdiğim birine sarılmamı sağladın.</button>
            <button type="button" aria-pressed="false">Yorulduğunu söyledin; seni duydum.</button>
            <button type="button" aria-pressed="false">Ben fark etmeden binlerce kez nefes aldın.</button>
          </div>
        </div>

        <div class="ds-p" hidden>
          <h3>Notunuz hazır</h3>
          <p class="soft">Bunu kendinize siz yazdınız. Yavaşça, içinizden okuyun.</p>
          <div class="ds-note" id="ds-note" aria-live="polite"></div>
          <div class="controls">
            <button type="button" class="cta" id="ds-copy">Notu kopyala</button>
            <button type="button" class="cta ghost" id="ds-again">Baştan başla</button>
          </div>
          <p class="count">Yazdıklarınız yalnızca bu cihazda, bu sayfa açıkken durur; hiçbir yere gönderilmez ve kaydedilmez.</p>
        </div>

        <div class="ds-foot" id="ds-foot">
          <button type="button" class="cta ghost" id="ds-back" hidden>Geri</button>
          <button type="button" class="cta" id="ds-next" disabled>Devam</button>
        </div>

        <div class="ds-strings" hidden>
          <span data-k="next">Devam</span>
          <span data-k="last">Notumu göster</span>
          <span data-k="echo">Demek {{x}}. Adını koydunuz; şimdi ona biraz yer açalım.</span>
          <span data-k="echo0">Adını koyamamak da bir cevap. Şimdi ona biraz yer açalım.</span>
          <span data-k="ready">Hazır olduğunuzda başlayın</span>
          <span data-k="cue1">Elinizin sıcaklığını hissedin</span>
          <span data-k="cue2">Nefesiniz kendi hızında aksın</span>
          <span data-k="cued">Güzel. Hazır olduğunuzda devam edin.</span>
          <span data-k="hi">Sevgili {{n}},</span>
          <span data-k="hi0">Sevgili ben,</span>
          <span data-k="feel">Bugün {{x}} hissediyorsun. Bunu fark ettim ve geçiştirmiyorum.</span>
          <span data-k="feel0">Bugün içinde adını koyamadığın bir şey var. Olsun; fark etmen yeter.</span>
          <span data-k="body">Bedenime de bir sözüm var: {{x}} Teşekkür ederim.</span>
          <span data-k="end">Yarın yine buradayım.</span>
          <span data-k="sig">Kendi dostun</span>
          <span data-k="copy">Notu kopyala</span>
          <span data-k="copied">Kopyalandı</span>
        </div>
      </div>
      <p class="count">Dört adımı sırayla yapmak zorunda değilsiniz. Yalnızca 20 saniyelik dokunuş bile tek başına bir moladır.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neden bu dört adım?</h2>
      <p class="soft">Her adım, ayrı ayrı araştırılmış küçük bir uygulamaya dayanıyor. Ne bulunduğunu, bulunmayanla birlikte yazdık.</p>
      <div class="kinds">
        <div class="kind"><span class="n ltr">D</span><h3>Dur ve adını koy</h3><p>Duygunun içindeyken her şey birbirine karışır. Ona bir ad verdiğinizde aranıza küçük bir mesafe girer. Bir beyin görüntüleme çalışmasında 30 kişi öfkeli ve korkmuş yüzlere bakarken duygunun adını seçtiğinde, beynin alarm bölgesi (amigdala) daha az etkinleşti.</p></div>
        <div class="kind"><span class="n ltr">O</span><h3>Omuzlarını bırak</h3><p>Dokunmak, bedenin en eski teselli dilidir. Stresli bir sınavdan geçirilen 159 kişilik bir çalışmada, 20 saniye boyunca elini kalbine ve karnına koyanların stres hormonu (kortizol) düzeyi, bunu yapmayanlara göre daha düşük seyretti. Kalp hızı ve hissedilen stres ise değişmedi.</p></div>
        <div class="kind"><span class="n ltr">S</span><h3>Seslen</h3><p>Kendimizle konuşurken çoğu zaman en sert eleştirmenimiz oluruz. Toplam 585 kişiyle yapılan yedi çalışmada, kendine “ben” yerine adıyla seslenenler stresli durumlarda daha az sıkıntı duydu. Yedi gün boyunca kendine bir dost gibi yazanlar ise üç ay sonra daha az çökkün, altı ay sonra daha mutluydu.</p></div>
        <div class="kind"><span class="n ltr">T</span><h3>Teşekkür et</h3><p>Bedenimizi çoğu zaman yalnızca ağrıdığında ya da aynada fark ederiz. Bedeninden hoşnut olmayan 81 genç kadınla yapılan bir çalışmada, bedenin neler yapabildiği üzerine yazanlar bedenlerinden daha hoşnut hâle geldi; etki bir hafta sonra da sürüyordu.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Açık konuşalım</h2>
        <p class="soft">DOST molası bir tedavi değil, kendinize ayırdığınız beş dakikadır. Dört adımın her biri ayrı ayrı araştırıldı; bu sırayla birleştirilmiş hâli ise bir bütün olarak sınanmadı. Sıralama bu site için hazırlandı.</p>
        <p class="soft">Kendine şefkat uygulamalarını sınayan 27 rastgele kontrollü çalışmanın derlemesinde stres, çökkünlük ve kaygıda orta düzeyde iyileşme görüldü. Yazarlar, çalışmaların birbirinden çok farklı olduğunu ve olumlu sonuçların daha çok yayımlanmış olabileceğini de belirtiyor.</p>
      </div>
      <div>
        <h2>Ne zaman iyi gelir?</h2>
        <ul class="dots">
          <li>Ağrının arttığı bir akşam, bedeninize kızmak üzereyken.</li>
          <li>Egzersizi aksattığınız gün, kendinizi suçlamaya başladığınızda.</li>
          <li>Zor bir haberin ya da kırıcı bir konuşmanın hemen ardından.</li>
          <li>Uyumadan önce, günü kapatırken.</li>
        </ul>
        <p class="soft" style="margin-top:14px">Önce bedeni yatıştırmak isterseniz <a href="ic-cekis.html">5 dakikalık iç çekiş nefesi</a>, bir başkasına uzanmak isterseniz <a href="bag-kurmak.html">Sosyal bağ ve sağlık</a> sayfasına bakabilirsiniz.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(DOST_FAQ)}
      <div class="note" style="margin-top:22px"><strong>Destek almak önemlidir:</strong> Haftalardır süren çökkünlük, kaygı ya da uyku sorunları bu tür uygulamalarla geçmiyorsa bir hekime ya da ruh sağlığı uzmanına başvurun. Kendinize zarar verme düşünceleriniz varsa 112'yi arayın.</div>
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Lieberman MD, Eisenberger NI, Crockett MJ, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/17576282/", "Putting feelings into words: affect labeling disrupts amygdala activity in response to affective stimuli") + ". Psychol Sci. 2007;18(5):421-428.",
        "Dreisoerner A, Junker NM, Schlotz W, et al. " + ext("https://pmc.ncbi.nlm.nih.gov/articles/PMC9216399/", "Self-soothing touch and being hugged reduce cortisol responses to stress: A randomized controlled trial on stress, physical touch, and social identity") + ". Compr Psychoneuroendocrinol. 2021;8:100091.",
        "Kross E, Bruehlman-Senecal E, Park J, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/24467424/", "Self-talk as a regulatory mechanism: How you do it matters") + ". J Pers Soc Psychol. 2014;106(2):304-324.",
        "Shapira LB, Mongrain M. " + ext("https://self-compassion.org/wp-content/uploads/publications/Shapira-%26-Mongrain%282010%29.pdf", "The benefits of self-compassion and optimism exercises for individuals vulnerable to depression") + ". J Posit Psychol. 2010;5(5):377-389.",
        "Alleva JM, Martijn C, van Breukelen GJP, Jansen A, Karos K. " + ext("https://cris.maastrichtuniversity.nl/en/publications/expand-your-horizon-a-programme-that-improves-body-image-and-redu", "Expand Your Horizon: A programme that improves body image and reduces self-objectification by training women to focus on body functionality") + ". Body Image. 2015;15:81-89.",
        "Ferrari M, Hunt C, Harrysunker A, Abbott MJ, Beath AP, Einstein DA. " + ext("https://acuresearchbank.acu.edu.au/item/87545/self-compassion-interventions-and-psychosocial-outcomes-a-meta-analysis-of-rcts", "Self-compassion interventions and psychosocial outcomes: A meta-analysis of RCTs") + ". Mindfulness. 2019;10:1455-1473.",
      ])}
    </div>
  </section>
</main>'''

DOST_JS = r'''<script>
(function(){
  var root = document.getElementById('ds'); if (!root) return;
  var S = {}; root.querySelectorAll('.ds-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var $ = function(id){ return document.getElementById(id); };
  var panels = root.querySelectorAll('.ds-p'), nav = root.querySelectorAll('.ds-nav li'), next = $('ds-next'), back = $('ds-back'), foot = $('ds-foot');
  var arc = $('ds-arc'), sec = $('ds-sec'), cue = $('ds-cue'), tgo = $('ds-touch-go'), copy = $('ds-copy');
  var step = 0, pick = {feel: null, none: false, say: null, body: null}, raf = 0, DUR = 20, C = 603.2, txt = '';
  function ok(){ return step === 0 ? pick.feel !== null : step === 2 ? !!pick.say : step === 3 ? !!pick.body : true; }
  function show(n, user){
    step = n; cancelAnimationFrame(raf); root.classList.remove('beat');
    panels.forEach(function(p, i){ p.hidden = i !== n; });
    nav.forEach(function(li, i){ li.className = i < n ? 'done' : (i === n ? 'on' : ''); });
    foot.hidden = n === 4; back.hidden = n === 0;
    next.textContent = n === 3 ? S.last : S.next; next.disabled = !ok();
    if (n === 1){ arc.style.strokeDashoffset = C; sec.textContent = DUR; cue.textContent = S.ready; tgo.hidden = false; }
    if (n === 4) note();
    if (user){ var r = root.getBoundingClientRect(); if (r.top < 60 || r.top > innerHeight * 0.5) window.scrollTo({top: scrollY + r.top - 84, behavior: 'smooth'}); }
  }
  function choose(id, key){
    $(id).addEventListener('click', function(e){
      var b = e.target.closest('button'); if (!b) return;
      this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      pick[key] = b.textContent.trim();
      if (key === 'feel'){
        pick.none = b.hasAttribute('data-none');
        var e2 = $('ds-echo'); e2.hidden = true; void e2.offsetWidth;
        e2.textContent = pick.none ? S.echo0 : S.echo.replace('{x}', pick.feel); e2.hidden = false;
      }
      next.disabled = !ok();
    });
  }
  choose('ds-feel', 'feel'); choose('ds-say', 'say'); choose('ds-body', 'body');
  tgo.addEventListener('click', function(){
    tgo.hidden = true; root.classList.add('beat'); cue.textContent = S.cue1;
    var t0 = performance.now();
    (function f(now){
      var el = (now - t0) / 1000;
      if (el >= DUR){ arc.style.strokeDashoffset = 0; sec.textContent = '✓'; cue.textContent = S.cued; root.classList.remove('beat'); return; }
      arc.style.strokeDashoffset = (C * (1 - el / DUR)).toFixed(1); sec.textContent = Math.ceil(DUR - el);
      if (el > 9) cue.textContent = S.cue2;
      raf = requestAnimationFrame(f);
    })(t0);
  });
  function note(){
    var name = $('ds-name').value.replace(/[<>]/g, '').trim();
    var L = [name ? S.hi.replace('{n}', name) : S.hi0, pick.none ? S.feel0 : S.feel.replace('{x}', pick.feel), pick.say, S.body.replace('{x}', pick.body), S.end];
    var box = $('ds-note'); box.textContent = '';
    L.concat(['— ' + S.sig]).forEach(function(t, i){
      var p = document.createElement('p'); p.textContent = t;
      if (i === 0) p.className = 'hi'; if (i === L.length) p.className = 'sig';
      p.style.animationDelay = (0.4 + i * 1.1).toFixed(1) + 's'; box.appendChild(p);
    });
    txt = L.join('\n') + '\n— ' + S.sig; copy.textContent = S.copy;
  }
  next.addEventListener('click', function(){ if (ok() && step < 4) show(step + 1, true); });
  back.addEventListener('click', function(){ if (step > 0) show(step - 1, true); });
  copy.addEventListener('click', function(){
    function done(){ copy.textContent = S.copied; setTimeout(function(){ copy.textContent = S.copy; }, 2200); }
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(done, function(){});
    else { var ta = document.createElement('textarea'); ta.value = txt; document.body.appendChild(ta); ta.select(); try { document.execCommand('copy'); done(); } catch (e) {} ta.remove(); }
  });
  $('ds-again').addEventListener('click', function(){
    pick = {feel: null, none: false, say: null, body: null};
    root.querySelectorAll('[aria-pressed]').forEach(function(x){ x.setAttribute('aria-pressed', 'false'); });
    $('ds-echo').hidden = true; show(0, true);
  });
  show(0, false);
  if ('IntersectionObserver' in window) new IntersectionObserver(function(es){ document.body.classList.toggle('ds-on', es[0].isIntersecting); }, {threshold: 0.12}).observe(root);
})();
</script>
'''

page("dost-molasi.html", "DOST Molası: Kendinize Dost Olmanın Beş Dakikası",
     "Zor bir günde kendinize bir dost gibi davranmanın dört adımı: dur ve adını koy, omuzlarını bırak, seslen, teşekkür et. Beş dakikalık rehberle yapın, kendinize kısa bir not yazın.",
     "dost-molasi.html", DOST_CSS, DOST_BODY, DOST_JS,
     seo_title="DOST Molası: 5 Dakikada Kendine Şefkat Egzersizi | İhsan Eren",
     about={"@type": "Thing", "name": "Kendine şefkat"},
     faq_items=pick(DOST_FAQ, 0, 1, 2, 3))

# -*- coding: utf-8 -*-
import re
S = open('site/index.html', encoding='utf-8').read()

# ---- mevcut açıklamaları al
m = re.search(r'<ol class="meanings">(.*?)</ol>\n      </div>', S, re.S)
items = re.findall(r'<li>\s*<span class="pin-no">(\d)</span>\s*<div>(.*?)</div>\s*</li>', m.group(1), re.S)
assert len(items) == 6, len(items)

V = [(52.53,14.30),(51.71,18.78),(50.77,22.71),(51.0,26.91),(51.71,30.69),(52.77,34.22),
     (53.95,37.76),(54.89,41.53),(55.36,45.61),(55.24,49.78),(54.77,53.79),(53.83,57.44)]
W = 3.3
left = [(x-W, y) for x, y in V]; right = [(x+W, y) for x, y in V][::-1]
spine = "M%.2f 11.5 " % (V[0][0]-W) + " ".join("L%.2f %.2f" % p for p in left) + " L%.2f 61 L%.2f 61 " % (V[-1][0]-W, V[-1][0]+W) + " ".join("L%.2f %.2f" % p for p in right) + " L%.2f 11.5 Z" % (V[0][0]+W)
motion = "M" + " L".join("%.2f %.2f" % p for p in V)
Y1 = (39.9, 47.2); Y2 = (64.6, 22.0); R = 6.4
TIPS = [(35.56,44.71),(43.11,44.83),(40.75,50.96)]
IMG = '<image href="img/logo.png" x="18" y="9" width="64" height="52.8" preserveAspectRatio="xMidYMid meet"'

hl = "\n".join(f'          {IMG} class="hl hl{i}" clip-path="url(#lc{i})"/>' for i in range(1, 7))
vdots = "".join(
    f'<circle cx="{x}" cy="{y}" r=".75"><animate attributeName="opacity" values=".15;1;.15" dur="2.4s" begin="{k*0.18:.2f}s" repeatCount="indefinite"/></circle>'
    for k, (x, y) in enumerate(V))
tipdots = "".join(
    f'<circle cx="{x}" cy="{y}" r=".85"><animate attributeName="r" values=".6;1.3;.6" dur="1.8s" begin="{k*0.3:.1f}s" repeatCount="indefinite"/></circle>'
    for k, (x, y) in enumerate(TIPS))

SVG = f'''<svg viewBox="0 0 100 84" role="img" aria-labelledby="logo-svg-t">
          <title id="logo-svg-t">İhsan Eren logosu ve numaralı bölümleri</title>
          <defs>
            <clipPath id="lc1"><path clip-rule="evenodd" d="M0 0H100V84H0Z {spine}"/></clipPath>
            <clipPath id="lc2"><path d="{spine}"/></clipPath>
            <clipPath id="lc3"><circle cx="{Y1[0]}" cy="{Y1[1]}" r="{R}"/></clipPath>
            <clipPath id="lc4"><circle cx="{Y1[0]}" cy="{Y1[1]}" r="{R}"/><circle cx="{Y2[0]}" cy="{Y2[1]}" r="{R}"/></clipPath>
            <clipPath id="lc5"><circle cx="{Y2[0]}" cy="{Y2[1]}" r="{R}"/></clipPath>
            <clipPath id="lc6"><path d="{spine}"/></clipPath>
          </defs>
          {IMG} class="base"/>
{hl}
          <g class="fx fx1" fill="none" stroke="#e2ab47" stroke-width=".3" stroke-dasharray="1 1.3">
            <ellipse cx="36.4" cy="35.4" rx="14.4" ry="27"/><ellipse cx="68.2" cy="35" rx="14.6" ry="27"/>
          </g>
          <g class="fx fx2">
            <path d="{spine}" fill="none" stroke="#e2ab47" stroke-width=".3" stroke-dasharray="1 1.1"/>
            <circle r="1.1" fill="#e2ab47"><animateMotion dur="2.6s" repeatCount="indefinite" path="{motion}"/></circle>
            <circle r=".8" fill="#ece5cf"><animateMotion dur="2.6s" begin="1.3s" repeatCount="indefinite" path="{motion}"/></circle>
          </g>
          <g class="fx fx3">
            <circle cx="{Y1[0]}" cy="{Y1[1]}" r="{R+0.8}" fill="none" stroke="#e2ab47" stroke-width=".35"/>
            <g fill="#ece5cf">{tipdots}</g>
          </g>
          <g class="fx fx4" fill="none" stroke="#e2ab47">
            <circle cx="{Y1[0]}" cy="{Y1[1]}" r="{R+0.8}" stroke-width=".35"/><circle cx="{Y2[0]}" cy="{Y2[1]}" r="{R+0.8}" stroke-width=".35"/>
            <path d="M{Y1[0]+6.4} {Y1[1]-1.5} C48 44 47 36 52.4 34.5 S57 26 {Y2[0]-6.6} {Y2[1]+1.8}" stroke-width=".45" stroke-dasharray="1.2 1.2" stroke-linecap="round">
              <animate attributeName="stroke-dashoffset" values="0;-4.8" dur="1.2s" repeatCount="indefinite"/></path>
          </g>
          <g class="fx fx5" fill="none" stroke="#e2ab47" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="{Y2[0]}" cy="{Y2[1]}" r="{R+0.8}" stroke-width=".35"/>
            <path d="M73.6 15.5 l2.2 -1.2 -1 2.4 2.4 -1.1" stroke-width=".45"><animate attributeName="opacity" values="0;1;0;0" dur="1.4s" repeatCount="indefinite"/></path>
            <path d="M74.2 27.5 l2.4 .6 -2 1.4 2.5 .5" stroke-width=".45"><animate attributeName="opacity" values="0;0;1;0" dur="1.4s" repeatCount="indefinite"/></path>
            <path d="M58.4 12.8 l-1.4 -2 2.4 .3 -1.2 -2" stroke-width=".45"><animate attributeName="opacity" values="1;0;0;1" dur="1.4s" repeatCount="indefinite"/></path>
          </g>
          <g class="fx fx6">
            <g fill="#e2ab47">{vdots}</g>
            <text x="66" y="71" class="fx-num">12</text>
            <g transform="translate(76.5 69.4)"><text class="fx-lambda" x="0" y="0">λ<animateTransform attributeName="transform" type="rotate" values="0;0;180;180;0" keyTimes="0;.3;.5;.8;1" dur="4s" repeatCount="indefinite"/></text></g>
          </g>
          <path class="lead l1" d="M8 30 H20 L27 32"/><circle class="dot l1" cx="27" cy="32" r=".8"/>
          <path class="lead l2" d="M52.3 6 V13.6"/><circle class="dot l2" cx="52.3" cy="13.6" r=".8"/>
          <path class="lead l3" d="M8 50 H30 L39.8 46.8"/><circle class="dot l3" cx="39.8" cy="46.8" r=".8"/>
          <path class="lead l4" d="M40.6 57.3 L54.2 77 L64 57.3"/><circle class="dot l4" cx="40.6" cy="57.3" r=".8"/><circle class="dot l4" cx="64" cy="57.3" r=".8"/>
          <path class="lead l5" d="M92 20 H78 L64.7 22.5"/><circle class="dot l5" cx="64.7" cy="22.5" r=".8"/>
          <path class="lead l6" d="M54.2 64 V56.6"/><circle class="dot l6" cx="54.2" cy="56.6" r=".8"/>
'''
PINS = [(5,30),(52.3,3),(5,50),(54.2,80),(95,20),(54.2,67)]
TITLES = ["Beyin", "Omurga", "Üç kol", "İki Y", "Sarı ton", "Lambda"]
for i, (x, y) in enumerate(PINS, 1):
    SVG += (f'          <g class="pin p{i}" data-p="{i}" tabindex="0" role="button" aria-label="{i}. {TITLES[i-1]}">'
            f'<circle class="hit" cx="{x}" cy="{y}" r="5.5"/><circle class="ring" cx="{x}" cy="{y}" r="3"/>'
            f'<circle class="c" cx="{x}" cy="{y}" r="3"/><text x="{x}" y="{y+0.2}">{i}</text></g>\n')
SVG += '        </svg>'

chips = "\n".join(
    f'            <button type="button" class="chip" role="tab" id="lt{i}" aria-controls="lp{i}" aria-selected="{"true" if i == 1 else "false"}" data-p="{i}"><span class="n">{i}</span>{TITLES[i-1]}</button>'
    for i in range(1, 7))
panels = "\n".join(
    f'            <div class="panel{" on" if int(n) == 1 else ""}" role="tabpanel" id="lp{n}" aria-labelledby="lt{n}">{body.strip()}</div>'
    for n, body in items)

NEW = f'''<div class="logo-grid">
      <figure class="annot" data-a="1">
        {SVG}
        <figcaption class="hint">Numaralara dokunarak logonun her bölümünü keşfedin.</figcaption>
      </figure>

      <div class="story">
        <div class="chips" role="tablist" aria-label="Logonun bölümleri">
{chips}
        </div>
        <div class="panels">
{panels}
        </div>
        <div class="story-nav">
          <button type="button" class="btn" id="lg-prev" aria-label="Önceki bölüm"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 6-6 6 6 6"/></svg></button>
          <span id="lg-count" aria-live="polite">1 / 6</span>
          <button type="button" class="btn" id="lg-next" aria-label="Sonraki bölüm"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 6 6 6-6 6"/></svg></button>
        </div>
      </div>
      </div>'''

i = S.index('<div class="logo-grid">'); j = S.index('\n\n      <p class="summary">')
S = S[:i] + NEW + S[j:]

# ---- CSS
ci = S.index('  /* logo story */'); cj = S.index('  .statement{')
CSS = '''  /* logo story */
  .logo-grid{display:grid;gap:18px}
  .annot{max-width:540px;margin:0 auto;width:100%}
  @media (min-width:1000px){
    .logo-grid{grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);gap:56px;align-items:center}
    .logo-grid .annot{margin:0;max-width:none}
  }
  .annot svg{width:100%;height:auto;display:block;overflow:visible;-webkit-tap-highlight-color:transparent}
  .annot .base{transition:opacity .5s ease,filter .5s ease}
  .annot[data-a] .base{opacity:.2;filter:saturate(.4)}
  .annot[data-a="4"] .base{opacity:.42}
  .annot .hl,.annot .fx{opacity:0;transition:opacity .5s ease;pointer-events:none}
  .annot .lead{stroke:var(--foil);stroke-width:.25;fill:none;opacity:.35;transition:opacity .35s,stroke .35s}
  .annot .dot{fill:var(--gold);opacity:.35;transition:opacity .35s}
  .annot .pin{cursor:pointer;outline:none}
  .annot .pin .hit{fill:transparent}
  .annot .pin .c{fill:var(--ground);stroke:var(--foil);stroke-width:.35;transition:fill .3s,stroke .3s}
  .annot .pin text{fill:var(--foil);font-family:var(--display);font-size:3.6px;text-anchor:middle;dominant-baseline:central;pointer-events:none;transition:fill .3s}
  .annot .pin:hover .c{stroke:var(--gold);stroke-width:.55}
  .annot .pin:focus-visible .c{stroke:var(--gold);stroke-width:.8}
  .annot .pin .ring{fill:none;stroke:var(--gold);stroke-width:.3;opacity:0;transform-box:fill-box;transform-origin:center}
  .annot:not(.touched) .pin .ring{animation:pinpulse 2.6s ease-out infinite}
  .annot:not(.touched) .p2 .ring{animation-delay:.4s} .annot:not(.touched) .p3 .ring{animation-delay:.8s}
  .annot:not(.touched) .p4 .ring{animation-delay:1.2s} .annot:not(.touched) .p5 .ring{animation-delay:1.6s} .annot:not(.touched) .p6 .ring{animation-delay:2s}
  @keyframes pinpulse{0%{opacity:.9;transform:scale(1)}70%,100%{opacity:0;transform:scale(1.9)}}
  .annot .fx-num{fill:var(--gold);font-family:var(--display);font-size:5px;dominant-baseline:central}
  .annot .fx-lambda{fill:var(--foil);font-family:var(--display);font-size:6px;text-anchor:middle;dominant-baseline:central}
  .hint{margin:10px 0 0;text-align:center;font-size:13px;color:var(--muted)}
''' + "".join(
    f'  .annot[data-a="{i}"] .hl{i},.annot[data-a="{i}"] .fx{i}{{opacity:1}}\n'
    f'  .annot[data-a="{i}"] .l{i}{{opacity:1}} .annot[data-a="{i}"] path.l{i}{{stroke:var(--gold);stroke-width:.35}}\n'
    f'  .annot[data-a="{i}"] .p{i} .c{{fill:var(--gold);stroke:var(--gold)}} .annot[data-a="{i}"] .p{i} text{{fill:var(--ground)}}\n'
    for i in range(1, 7)) + '''
  .story{display:grid;gap:18px;align-content:start}
  .chips{display:flex;flex-wrap:wrap;gap:8px}
  .chip{all:unset;box-sizing:border-box;cursor:pointer;display:inline-flex;align-items:center;gap:8px;padding:6px 14px 6px 6px;border-radius:999px;border:1px solid var(--line);color:var(--ink-soft);font-size:14px;transition:border-color .2s,color .2s,background .2s}
  .chip .n{width:24px;height:24px;border-radius:50%;border:1px solid var(--foil);display:grid;place-items:center;font-family:var(--display);font-size:13px;color:var(--foil);transition:background .2s,color .2s}
  .chip:hover{border-color:var(--line-strong);color:var(--ink)}
  .chip:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .chip[aria-selected="true"]{border-color:var(--foil);color:var(--ink);background:rgba(216,178,94,.08)}
  .chip[aria-selected="true"] .n{background:var(--gold);border-color:var(--gold);color:var(--ground)}
  .panels{display:grid}
  .panel{padding:4px 0 0}
  .panel h3{font-size:clamp(22px,3.4vw,28px);margin-bottom:10px;color:var(--ink)}
  .panel p{margin:0;color:var(--ink-soft);max-width:62ch}
  .panel p + p{margin-top:10px}
  #logo:not(.js) .chips,#logo:not(.js) .story-nav,#logo:not(.js) .hint{display:none}
  #logo:not(.js) .panel{padding-block:18px;border-top:1px solid var(--line)}
  #logo.js .panel{grid-area:1/1;visibility:hidden;opacity:0;transform:translateY(6px);transition:opacity .35s ease,transform .35s ease,visibility 0s linear .35s}
  #logo.js .panel.on{visibility:visible;opacity:1;transform:none;transition:opacity .35s ease,transform .35s ease,visibility 0s}
  .story-nav{display:flex;align-items:center;gap:14px;color:var(--muted);font-size:14px;font-variant-numeric:tabular-nums}
  @media (prefers-reduced-motion:reduce){.annot .fx *{animation:none!important}}
'''
S = S[:ci] + CSS + S[cj:]

# eski .meanings/.pin-no stilleri artık gereksiz ama zararsız; kaldır
S = re.sub(r'  \.meanings\{[^\n]*\n  \.meanings li\{[^\n]*\n  \.meanings li:last-child\{[^\n]*\n', '', S)
S = re.sub(r'  \.meanings h3\{[^\n]*\n  \.meanings p\{[^\n]*\n  \.meanings p \+ p\{[^\n]*\n', '', S)

# ---- JS (sayfanın son script'inden önce)
JS = '''<script>
(function(){
  var sec = document.getElementById('logo'); if (!sec) return;
  sec.classList.add('js');
  var fig = sec.querySelector('.annot'), count = document.getElementById('lg-count');
  var tabs = Array.prototype.slice.call(sec.querySelectorAll('.chip'));
  var panels = Array.prototype.slice.call(sec.querySelectorAll('.panel'));
  var pins = Array.prototype.slice.call(sec.querySelectorAll('.pin'));
  var cur = 1;
  function set(n, focusTab){
    cur = (n - 1 + 6) % 6 + 1;
    fig.setAttribute('data-a', cur);
    tabs.forEach(function(t, i){ var on = i + 1 === cur; t.setAttribute('aria-selected', on ? 'true' : 'false'); t.tabIndex = on ? 0 : -1; });
    panels.forEach(function(p, i){ p.classList.toggle('on', i + 1 === cur); });
    pins.forEach(function(p){ p.setAttribute('aria-pressed', +p.dataset.p === cur ? 'true' : 'false'); });
    count.textContent = cur + ' / 6';
    if (focusTab) tabs[cur - 1].focus();
  }
  function touch(){ fig.classList.add('touched'); }
  pins.forEach(function(p){
    p.addEventListener('click', function(){ touch(); set(+p.dataset.p); });
    p.addEventListener('keydown', function(e){ if (e.key === 'Enter' || e.key === ' '){ e.preventDefault(); touch(); set(+p.dataset.p); } });
  });
  tabs.forEach(function(t){
    t.addEventListener('click', function(){ touch(); set(+t.dataset.p); });
    t.addEventListener('keydown', function(e){
      var k = e.key, n = null;
      if (k === 'ArrowRight' || k === 'ArrowDown') n = cur + 1;
      else if (k === 'ArrowLeft' || k === 'ArrowUp') n = cur - 1;
      else if (k === 'Home') n = 1; else if (k === 'End') n = 6;
      if (n !== null){ e.preventDefault(); touch(); set(n, true); }
    });
  });
  document.getElementById('lg-prev').onclick = function(){ touch(); set(cur - 1); };
  document.getElementById('lg-next').onclick = function(){ touch(); set(cur + 1); };
  set(1);
})();
</script>
'''
k = S.rindex('</body>') if '</body>' in S else len(S)
S = S[:k] + JS + S[k:]
open('site/index.html', 'w', encoding='utf-8').write(S)
print("ok", len(S))

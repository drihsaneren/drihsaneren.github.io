# -*- coding: utf-8 -*-
# Bilim gündemi · 2026 Nobel ödülleri: "Işık, ayna ve buz".
# Üç ödül (tıp: optogenetik, kimya: tek elli moleküller, fizik: IceCube), her biri için sade anlatım,
# küçük bir canlandırma ve "dün – bugün – yarın" şeridi. SVG içinde yazı YOK (çeviri SVG'leri maskeler);
# bütün yazılar HTML'de. build_pages.py içinden exec edilir (NEWS listesinden önce; IL_NOBEL'i de tanımlar).

NB_BLUE = "#7cc4ff"
_MIT = "M-24 44V-8a24 24 0 0 1 48 0V2c12-9 25-3 23 9c-2 10-11 16-23 22V44a8 8 0 0 1-8 8H-16a8 8 0 0 1-8-8z"

# ---- haber kartı çizimi (320×180, sabit)
def _il_nobel():
    lip = "".join(f'<circle cx="{x}" cy="92" r="3.2"/><circle cx="{x}" cy="106" r="3.2"/>' for x in (12, 24, 36, 70, 82, 94))
    doms = "".join(f'<circle cx="{x}" cy="{y}" r="2.2"/>' for x in (236, 258, 280, 302) for y in (70, 86, 102, 118, 134, 150))
    lit = "".join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in ((236, 134, 3.6), (258, 118, 4.4), (280, 102, 4.4), (302, 86, 3.6), (258, 134, 3), (280, 118, 3)))
    return f'''<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="#223020"/>
<path d="M107 22V158M213 22V158" stroke="rgba(236,229,207,.14)"/>
<path d="M48 26h10l22 60H26z" fill="{NB_BLUE}" opacity=".45"/><rect x="47" y="14" width="12" height="12" rx="3" fill="#3a4d37" stroke="rgba(236,229,207,.4)"/>
<g fill="rgba(236,229,207,.16)" stroke="rgba(236,229,207,.5)">{lip}</g>
<rect x="41" y="82" width="9" height="34" rx="4.5" fill="#8fa476"/><rect x="56" y="82" width="9" height="34" rx="4.5" fill="#8fa476"/>
<g fill="#e2ab47"><circle cx="53" cy="100" r="3"/><circle cx="53" cy="126" r="3"/><circle cx="46" cy="144" r="3"/><circle cx="62" cy="150" r="3"/></g>
<path d="M160 40V140" stroke="#d8b25e" stroke-dasharray="3 5" opacity=".7"/>
<g transform="translate(135 90) scale(.62)"><path d="{_MIT}" fill="rgba(143,164,118,.3)" stroke="#8fa476" stroke-width="3" stroke-linejoin="round"/></g>
<g transform="translate(185 90) scale(-.62 .62)"><path d="{_MIT}" fill="rgba(226,171,71,.25)" stroke="#e2ab47" stroke-width="3" stroke-linejoin="round"/></g>
<path d="M225 52H313" stroke="rgba(236,229,207,.55)" stroke-linecap="round"/>
<path d="M236 52V158M258 52V158M280 52V158M302 52V158" stroke="rgba(236,229,207,.14)"/>
<g fill="rgba(236,229,207,.28)">{doms}</g>
<path d="M226 142L312 80" stroke="{NB_BLUE}" stroke-width="2" stroke-linecap="round" opacity=".85"/>
<g fill="{NB_BLUE}">{lit}</g></svg>'''
IL_NOBEL = _il_nobel()

# ---- canlandırma 1: ışıkla açılan kapı
def _og_svg():
    xs = [x for x in range(10, 360, 17) if not 150 < x < 210]
    lip = "".join(f'<path d="M{x-2} 109v8M{x+2} 109v8M{x-2} 119v8M{x+2} 119v8"/>' for x in xs)
    heads = "".join(f'<circle cx="{x}" cy="104" r="5.2"/><circle cx="{x}" cy="132" r="5.2"/>' for x in xs)
    out = "".join(f'<circle cx="{x}" cy="{y}" r="3.6"/>' for x, y in ((34, 42), (74, 72), (112, 34), (136, 80), (246, 66), (288, 36), (326, 76), (228, 30), (58, 86), (306, 62)))
    ins = "".join(f'<circle cx="{x}" cy="{y}" r="3.6"/>' for x, y in ((84, 166), (290, 160)))
    return f'''<svg viewBox="0 0 360 240" aria-hidden="true" focusable="false">
<defs><linearGradient id="og-b" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{NB_BLUE}" stop-opacity=".9"/><stop offset="1" stop-color="{NB_BLUE}" stop-opacity=".1"/></linearGradient>
<radialGradient id="og-c" cx="50%" cy="0%" r="75%"><stop offset="0" stop-color="#e2ab47" stop-opacity=".4"/><stop offset="1" stop-color="#e2ab47" stop-opacity="0"/></radialGradient></defs>
<rect class="cell" x="0" y="138" width="360" height="70" fill="url(#og-c)"/>
<polygon class="beam" points="174,16 186,16 224,100 136,100" fill="url(#og-b)"/>
<rect x="173" y="0" width="14" height="17" rx="3" fill="#3a4d37" stroke="rgba(236,229,207,.4)"/>
<g stroke="rgba(236,229,207,.28)" stroke-width="1.4" stroke-linecap="round">{lip}</g>
<g fill="rgba(236,229,207,.16)" stroke="rgba(236,229,207,.5)">{heads}</g>
<g class="idle" fill="#e2ab47">{out}</g><g fill="#e2ab47" opacity=".55">{ins}</g>
<g class="flow" fill="#e2ab47"><circle cx="180" cy="74" r="3.6"/><circle cx="180" cy="74" r="3.6"/><circle cx="180" cy="74" r="3.6"/><circle cx="180" cy="74" r="3.6"/></g>
<g class="gl"><rect x="161" y="92" width="17" height="52" rx="8.5" fill="#8fa476"/></g>
<g class="gr"><rect x="182" y="92" width="17" height="52" rx="8.5" fill="#8fa476"/></g>
<path d="M12 222H348" stroke="rgba(236,229,207,.22)" stroke-linecap="round"/>
<g class="spk" fill="none" stroke="#e2ab47" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"></g></svg>'''

# ---- canlandırma 2: aynadaki el (eldivenler üst üste oturmaz)
MIT_SVG = f'''<svg viewBox="0 0 360 160" aria-hidden="true" focusable="false">
<path d="M180 14V146" stroke="#d8b25e" stroke-dasharray="4 6" opacity=".7"/>
<path d="M172 20l-6 6M172 34l-10 10M188 126l10-10M188 140l6-6" stroke="#d8b25e" stroke-linecap="round" opacity=".35"/>
<g transform="translate(105 78)"><path d="{_MIT}" fill="rgba(143,164,118,.3)" stroke="#8fa476" stroke-width="2.4" stroke-linejoin="round"/><path d="M-24 36H24" stroke="#8fa476" stroke-width="2.4" opacity=".6"/></g>
<g class="mv"><g transform="translate(255 78) scale(-1 1)"><path d="{_MIT}" fill="rgba(226,171,71,.22)" stroke="#e2ab47" stroke-width="2.4" stroke-linejoin="round"/><path d="M-24 36H24" stroke="#e2ab47" stroke-width="2.4" opacity=".6"/></g></g>
<g class="no" fill="none" stroke="#d9705f" stroke-width="2.4" stroke-linecap="round"><circle cx="105" cy="22" r="11" fill="#1f2c1d"/><path d="M100 17l10 10M110 17l-10 10"/></g></svg>'''

# ---- canlandırma 3: buzun içindeki teleskop
def _ic_svg():
    xs = [48 + i * 38 for i in range(8)]
    strings = "".join(f"M{x} 38V238" for x in xs)
    doms = "".join(f'<circle class="dom" cx="{x}" cy="{128 + j * 15}" r="2.7"/>' for x in xs for j in range(8))
    stars = "".join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in ((22, 12, 1.1), (64, 24, .9), (104, 9, 1.2), (146, 20, .8), (214, 11, 1.1), (252, 25, .9), (296, 8, 1.2), (338, 20, 1)))
    return f'''<svg viewBox="0 0 360 250" aria-hidden="true" focusable="false">
<defs><linearGradient id="ic-i" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#22332d"/><stop offset="1" stop-color="#15212a"/></linearGradient></defs>
<rect width="360" height="38" fill="#141d16"/><rect y="38" width="360" height="212" fill="url(#ic-i)"/>
<g class="st" fill="#ece5cf">{stars}</g>
<path d="M0 38q45-5 90 0t90 0 90 0 90 0" fill="none" stroke="rgba(236,229,207,.6)" stroke-width="1.6"/>
<rect x="171" y="27" width="18" height="10" rx="1.5" fill="#c9c6ad"/><path d="M186 27V17h7" fill="none" stroke="#e2ab47" stroke-width="1.5" stroke-linecap="round"/>
<path d="{strings}" stroke="rgba(236,229,207,.13)"/>
<g fill="rgba(236,229,207,.3)">{doms}</g>
<line class="gh" x1="20" y1="250" x2="96" y2="205" stroke="#ece5cf" stroke-width="1.3" stroke-dasharray="2 6" stroke-linecap="round"/>
<line class="mu" x1="96" y1="205" x2="330" y2="96" pathLength="1" stroke="{NB_BLUE}" stroke-width="2.2" stroke-linecap="round"/>
<circle class="vx" cx="96" cy="205" r="9" fill="{NB_BLUE}"/></svg>'''

# ---- küçük simgeler (atlama kartları)
IC_LIGHT = f'<svg viewBox="0 0 40 40" aria-hidden="true"><path d="M17 4h6l8 16H9z" fill="{NB_BLUE}" opacity=".5"/><rect x="11" y="17" width="7" height="19" rx="3.5" fill="#8fa476"/><rect x="22" y="17" width="7" height="19" rx="3.5" fill="#8fa476"/><circle cx="20" cy="30" r="2.2" fill="#e2ab47"/></svg>'
IC_MIRROR = f'<svg viewBox="0 0 40 40" aria-hidden="true"><path d="M20 4V36" stroke="#d8b25e" stroke-dasharray="2.5 3.5"/><g transform="translate(9.5 20) scale(.26)"><path d="{_MIT}" fill="rgba(143,164,118,.35)" stroke="#8fa476" stroke-width="7" stroke-linejoin="round"/></g><g transform="translate(30.5 20) scale(-.26 .26)"><path d="{_MIT}" fill="rgba(226,171,71,.3)" stroke="#e2ab47" stroke-width="7" stroke-linejoin="round"/></g></svg>'
IC_ICE = f'<svg viewBox="0 0 40 40" aria-hidden="true"><path d="M3 9H37" stroke="rgba(236,229,207,.6)" stroke-linecap="round"/><path d="M10 9V37M20 9V37M30 9V37" stroke="rgba(236,229,207,.2)"/><g fill="rgba(236,229,207,.35)"><circle cx="10" cy="17" r="1.7"/><circle cx="20" cy="17" r="1.7"/><circle cx="30" cy="33" r="1.7"/><circle cx="10" cy="25" r="1.7"/></g><path d="M5 35L35 13" stroke="{NB_BLUE}" stroke-width="1.6" stroke-linecap="round"/><g fill="{NB_BLUE}"><circle cx="10" cy="33" r="2.4"/><circle cx="20" cy="25" r="2.8"/><circle cx="30" cy="17" r="2.4"/><circle cx="20" cy="33" r="1.9"/><circle cx="30" cy="25" r="1.9"/></g></svg>'

NOBEL_CSS = """
  [hidden]{display:none!important}
  .nb-jump{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-top:26px;max-width:880px}
  @media (max-width:680px){.nb-jump{grid-template-columns:minmax(0,1fr);gap:8px}}
  .nb-jump a{display:grid;grid-template-columns:auto minmax(0,1fr);gap:1px 12px;align-items:center;padding:12px 14px;border:1px solid var(--line);border-radius:14px;background:var(--ground-2);text-decoration:none;color:var(--ink);transition:border-color .2s,transform .2s}
  .nb-jump a:hover{border-color:var(--line-strong);transform:translateY(-2px)}
  .nb-jump svg{grid-row:1/3;width:40px;height:40px;display:block}
  .nb-jump .k{font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:var(--foil)}
  .nb-jump .t{font-family:var(--display);font-size:19px;line-height:1.2}
  .nb{scroll-margin-top:66px}
  .nb .eyebrow{color:var(--foil);margin-bottom:10px}
  .nb h2{font-size:clamp(30px,6vw,44px);margin-bottom:10px}
  .nb-who{font-family:var(--display);font-size:clamp(18px,2.6vw,22px);color:var(--ink);margin:0 0 6px;max-width:none}
  .nb-cite{font-style:italic;color:var(--muted);font-size:15px;margin:0 0 18px;max-width:62ch}
  .nb-one{border-left:2px solid var(--foil);padding-left:14px;font-size:clamp(17px,2.2vw,19px);color:var(--ink);max-width:64ch;margin:0 0 26px}
  .nb-one b{color:var(--foil);font-weight:600}
  .nb-two{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,440px);gap:32px;align-items:start}
  .nb-two .tx p{color:var(--ink-soft)}
  @media (max-width:880px){.nb-two{grid-template-columns:minmax(0,1fr);gap:22px}.nb-two .nb-fig{order:-1;max-width:520px}}
  .nb-fig{margin:0;min-width:0}
  .nb-stage{border:1px solid var(--line);border-radius:16px;background:#1f2c1d;overflow:hidden}
  .nb-stage svg{display:block;width:100%;height:auto}
  .nb-fig figcaption{font-size:14px;color:var(--muted);margin-top:10px}
  .nb-ctl{display:flex;flex-wrap:wrap;align-items:center;gap:10px 16px;margin-top:12px}
  .nb-ctl button.cta{font:inherit;font-weight:600;font-size:15px;cursor:pointer}
  .nb-n{font-size:14px;color:var(--ink-soft);font-variant-numeric:tabular-nums;margin:0}
  .nb-n b{font-family:var(--display);font-weight:400;font-size:24px;line-height:1;color:var(--gold);margin-right:5px}
  /* dün – bugün – yarın */
  .dby{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin:30px 0 24px;padding:0;list-style:none}
  @media (max-width:760px){.dby{grid-template-columns:minmax(0,1fr);gap:10px}}
  .dby li{border:1px solid var(--line);border-radius:14px;background:var(--ground-2);padding:16px 16px 15px}
  .dby b{display:flex;align-items:center;gap:9px;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--foil);font-weight:600;margin-bottom:8px}
  .dby b::before{content:"";flex:none;width:9px;height:9px;border-radius:50%;box-shadow:inset 0 0 0 2px var(--foil);opacity:.6}
  .dby li:nth-child(2) b::before{background:var(--foil);opacity:1}
  .dby li:nth-child(3) b::before{background:var(--gold);opacity:1;box-shadow:0 0 0 4px rgba(226,171,71,.2)}
  .dby p{margin:0;font-size:15.5px;line-height:1.6;color:var(--ink-soft);max-width:none}
  .nb-val{max-width:72ch;margin:0;color:var(--ink)}
  .nb-val strong{color:var(--foil);font-weight:600}
  .rv{transition:opacity .7s ease,transform .7s cubic-bezier(.2,.7,.2,1)}
  .nb-js .rv:not(.in){opacity:0;transform:translateY(16px)}
  /* 1 · ışıkla açılan kapı */
  #og .beam{opacity:0}
  #og.fire .beam{animation:og-beam .95s ease-out}
  @keyframes og-beam{0%{opacity:0}10%{opacity:1}60%{opacity:.9}100%{opacity:0}}
  #og .gl,#og .gr{transition:transform .22s cubic-bezier(.3,.8,.3,1)}
  #og .gl{transform:translateX(1.5px)} #og .gr{transform:translateX(-1.5px)}
  #og.fire .gl{transform:translateX(-6px)} #og.fire .gr{transform:translateX(6px)}
  #og .flow circle{opacity:0}
  #og.fire .flow circle{animation:og-ion .62s cubic-bezier(.4,0,.6,1) .1s both}
  #og.fire .flow circle:nth-child(2){animation-delay:.22s}
  #og.fire .flow circle:nth-child(3){animation-delay:.34s}
  #og.fire .flow circle:nth-child(4){animation-delay:.46s}
  @keyframes og-ion{0%{opacity:0;transform:translateY(0)}15%{opacity:1}80%{opacity:1}100%{opacity:0;transform:translateY(92px)}}
  #og .cell{opacity:0}
  #og.fire .cell{animation:og-cell 1s ease-out .2s}
  @keyframes og-cell{0%{opacity:0}35%{opacity:1}100%{opacity:0}}
  #og.run .idle circle{animation:og-bob 3.4s ease-in-out infinite alternate}
  #og .idle circle:nth-child(2n){animation-delay:-1.2s}
  #og .idle circle:nth-child(3n){animation-delay:-2.3s}
  @keyframes og-bob{from{transform:translate(0,0)}to{transform:translate(3px,5px)}}
  #og .spk path{stroke-dasharray:1;stroke-dashoffset:1;animation:og-draw .45s ease-out .32s forwards}
  @keyframes og-draw{to{stroke-dashoffset:0}}
  /* 2 · aynadaki el */
  #mt .no{opacity:0}
  #mt.run .mv{animation:mt-mv 8s cubic-bezier(.5,0,.3,1) infinite}
  #mt.run .no{animation:mt-no 8s linear infinite}
  @keyframes mt-mv{0%,12%{transform:translateX(0)}36%{transform:translateX(-150px)}40%{transform:translateX(-146px)}44%{transform:translateX(-153px)}48%{transform:translateX(-148px)}52%,62%{transform:translateX(-150px)}86%,100%{transform:translateX(0)}}
  @keyframes mt-no{0%,40%{opacity:0}46%,60%{opacity:1}66%,100%{opacity:0}}
  .nb-duo{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:30px}
  @media (max-width:820px){.nb-duo{grid-template-columns:minmax(0,1fr)}}
  .nb-box{border:1px solid var(--line);border-radius:16px;background:var(--ground-2);padding:20px 18px 18px;min-width:0}
  .nb-box h3{font-size:23px;margin-bottom:8px}
  .nb-box p{font-size:16px;color:var(--ink-soft);max-width:none}
  .kb{display:flex;height:34px;border-radius:10px;overflow:hidden;margin:16px 0 12px;background:rgba(236,229,207,.06)}
  .kb i{flex:0 0 calc(var(--w)*1%);transform-origin:0 50%}
  .kb .rr{background:var(--gold)} .kb .ll{background:var(--sage)}
  .kb .rl{background:repeating-linear-gradient(135deg,rgba(236,229,207,.16) 0 6px,rgba(236,229,207,.05) 6px 12px)}
  .run .kb i{animation:kb-grow .9s cubic-bezier(.2,.7,.2,1) both}
  .run .kb .ll{animation-delay:.25s} .run .kb .rl{animation-delay:.4s}
  @keyframes kb-grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}
  .kb-l{list-style:none;margin:0 0 14px;padding:0;display:grid;gap:6px;font-size:15px;color:var(--ink-soft)}
  .kb-l li{display:flex;align-items:baseline;gap:8px}
  .kb-l li::before{content:"";flex:none;width:10px;height:10px;border-radius:3px;transform:translateY(1px)}
  .kb-l .rr::before{background:var(--gold)} .kb-l .ll::before{background:var(--sage)} .kb-l .rl::before{background:rgba(236,229,207,.22)}
  .kb-l b{color:var(--ink);font-weight:600;font-variant-numeric:tabular-nums;min-width:3.2ch}
  .nb-box .sum{margin:0;color:var(--ink);font-size:16px}
  .so-tabs{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0 14px}
  .so-tabs button{all:unset;cursor:pointer;padding:7px 14px;border-radius:999px;border:1px solid var(--line-strong);font-size:14px;color:var(--ink-soft)}
  .so-tabs button:hover{border-color:var(--foil);color:var(--ink)}
  .so-tabs button[aria-pressed="true"]{background:var(--foil);border-color:var(--foil);color:var(--ground);font-weight:600}
  .so-tabs button:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .so-grid{display:grid;grid-template-columns:repeat(10,minmax(0,1fr));gap:5px;max-width:290px;margin:0 0 14px}
  .so-grid i{aspect-ratio:1/1;border-radius:50%;background:var(--sage);opacity:.5;transition:background .4s,opacity .4s,transform .4s}
  .so-grid i.a{background:var(--gold);opacity:1}
  .so-grid i.pop{transform:scale(1.35)}
  .so-lab{margin:0;color:var(--ink);font-size:16px;min-height:3.2em}
  /* 3 · buzun içindeki teleskop */
  #ic .gh,#ic .vx{opacity:0}
  #ic .mu{stroke-dasharray:1;stroke-dashoffset:1;filter:drop-shadow(0 0 3px rgba(124,196,255,.8))}
  #ic.go .gh{animation:ic-gh .55s linear forwards}
  @keyframes ic-gh{from{opacity:0}to{opacity:.55}}
  #ic.go .mu{animation:ic-mu .9s linear .55s forwards}
  @keyframes ic-mu{to{stroke-dashoffset:0}}
  #ic .vx{transform-box:fill-box;transform-origin:center}
  #ic.go .vx{animation:ic-vx .8s ease-out .5s both}
  @keyframes ic-vx{0%{opacity:.9;transform:scale(.2)}100%{opacity:0;transform:scale(2.4)}}
  #ic .dom{transform-box:fill-box;transform-origin:center}
  #ic .dom.hit{animation:ic-dom 1.5s ease-out var(--dl,0s) both}
  @keyframes ic-dom{0%{fill:rgba(236,229,207,.3);transform:scale(1)}12%{fill:#d6ecff;transform:scale(var(--s,2))}100%{fill:#7cc4ff;transform:scale(calc(1 + (var(--s,2) - 1)*.5))}}
  #ic.run .st circle{animation:ic-tw 3s ease-in-out infinite alternate}
  #ic .st circle:nth-child(2n){animation-delay:-1.4s}
  #ic .st circle:nth-child(3n){animation-delay:-2.2s}
  @keyframes ic-tw{from{opacity:.25}to{opacity:.95}}
  .nb-end h2{max-width:22ch}
  .nb-end p{color:var(--ink-soft)}
  .nb-end .big{font-family:var(--display);font-size:clamp(21px,3.2vw,26px);line-height:1.4;color:var(--ink);max-width:34ch;margin:22px 0 0}
  @media (prefers-reduced-motion:reduce){
    #mt.run .mv,#mt.run .no,#og.run .idle circle,#ic.run .st circle,.run .kb i{animation:none}
    .rv{transition:none}
  }
"""

def _dby(d, b, y):
    return f'''<ul class="dby">
        <li class="rv"><b>Dün</b><p>{d}</p></li>
        <li class="rv"><b>Bugün</b><p>{b}</p></li>
        <li class="rv"><b>Yarın</b><p>{y}</p></li>
      </ul>'''

NOBEL_FAQ = [
 ("Optogenetik nedir?", "Sinir hücrelerine ışığa duyarlı bir protein yerleştirip onları ışıkla açıp kapatma yöntemidir. Böylece araştırmacılar beyindeki belirli bir hücre grubunun ne işe yaradığını doğrudan sınayabilir."),
 ("Optogenetik insanlarda tedavi olarak kullanılıyor mu?", "Henüz rutin bir tedavi değildir. 2021'de, retinitis pigmentosa nedeniyle görmesini yitirmiş bir hastada kısmi görme kazanımı bildirildi; klinik çalışmalar sürüyor. Yöntem bugün ağırlıklı olarak araştırma laboratuvarlarında kullanılıyor."),
 ("Moleküllerin “sağ elli” ya da “sol elli” olması ne demek?", "Bazı moleküller, tıpkı sağ ve sol el gibi, ayna görüntüsüyle üst üste oturmaz; buna kiralite denir. İki biçim aynı atomlardan oluşur ama bedende farklı davranabilir. Bu yüzden ilaç üretiminde doğru biçimi elde etmek önemlidir."),
 ("Nötrino nedir, zararlı mıdır?", "Nötrino, elektrik yükü olmayan ve kütlesi çok küçük bir temel parçacıktır. Her saniye vücudumuzdan trilyonlarcası geçer; maddeyle neredeyse hiç etkileşmedikleri için bize bir zararları yoktur."),
]

NOBEL_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="yenilikler.html">{BACK}Bilim gündemi</a>
    <p class="eyebrow">Nobel 2026</p>
    <h1>Işık, ayna ve buz</h1>
    <p class="lede">Bu yılın Nobel ödülleri üç soruya verildi: Beyindeki tek bir hücreyle konuşabilir miyiz? Hayat neden hep tek elini kullanıyor? Evrenin öbür ucundan haber alabilir miyiz? Üçünü de bir çay molasında okunacak sadelikte anlatmaya çalıştım.</p>
    <p class="meta">7 Ekim 2026 · Yaklaşık 6 dakikalık okuma</p>
    <nav class="nb-jump" aria-label="Ödüller">
      <a href="#tip">{IC_LIGHT}<span class="k">Tıp</span><span class="t">Işıkla açılan kapı</span></a>
      <a href="#kimya">{IC_MIRROR}<span class="k">Kimya</span><span class="t">Aynadaki el</span></a>
      <a href="#fizik">{IC_ICE}<span class="k">Fizik</span><span class="t">Buzun içindeki teleskop</span></a>
    </nav>
  </div>
</header>
<main>
  <section class="nb" id="tip">
    <div class="wrap">
      <p class="eyebrow">Fizyoloji veya Tıp · 5 Ekim 2026</p>
      <h2>Işıkla açılan kapı</h2>
      <p class="nb-who">Karl Deisseroth · Peter Hegemann · Georg Nagel</p>
      <p class="nb-cite">“Işıkla açılan iyon kanalları ve optogenetiğe ilişkin keşifleri için”</p>
      <p class="nb-one"><b>Tek cümleyle:</b> Bir su yosununun ışığı görmesini sağlayan protein, beyin hücrelerine yerleştirildi; artık seçtiğimiz hücreleri ışıkla, saniyenin binde biri hassasiyetle çalıştırıp durdurabiliyoruz.</p>
      <div class="nb-two">
        <div class="tx">
          <p>Beyin hücreleri birbirleriyle küçük elektrik sinyalleriyle konuşur. Hücrenin zarında kapı gibi çalışan proteinler vardır; kapı açılınca yüklü tanecikler içeri dolar ve hücre “ateşler”.</p>
          <p>Yıllarca sorun şuydu: Milyarlarca hücrenin arasından yalnızca istediğimizi nasıl çalıştıracağız? Elektrot yakınındaki bütün hücreleri birden uyarır, ilaç ise yavaştır.</p>
          <p>Çözüm hiç beklenmedik bir yerden, gölet suyunda yaşayan tek hücreli yeşil bir yosundan geldi. Bu yosun ışığa doğru yüzer, çünkü zarında ışık değince açılan bir kapı taşır. Hegemann ve Nagel bu kapıyı buldu ve nasıl çalıştığını gösterdi. Deisseroth ve ekibi de onun genini sinir hücrelerine yerleştirdi: Mavi ışık yandı, hücre ateşledi.</p>
        </div>
        <figure class="nb-fig">
          <div class="nb-stage" id="og">{_og_svg()}</div>
          <div class="nb-ctl"><button type="button" class="cta" id="og-btn">Işığı yak</button><p class="nb-n"><b id="og-n">0</b><span>ateşleme</span></p></div>
          <figcaption>Üstte hücrenin dışı, altta içi. Mavi ışık ortadaki kapıyı açar, yüklü tanecikler içeri dolar ve hücre ateşler. Deneyin: Her dokunuşta bir sinyal.</figcaption>
        </figure>
      </div>
      {_dby("2002–2003: Yosundaki ışık kapıları (kanalrodopsinler) tanımlandı. 2005: Kapı, sıçan sinir hücrelerine yerleştirildi; hücreler mavi ışıkla milisaniyeler içinde ateşledi.",
            "Dünyanın dört bir yanındaki laboratuvarlar uykunun, hafızanın, korkunun, ağrının ve hareketin hangi devrelerden geçtiğini bu yöntemle haritalıyor. Parkinson ve depresyon gibi hastalıkları devre düzeyinde anlamanın temel araçlarından biri.",
            "2021'de, retinitis pigmentosa nedeniyle görmesini yitirmiş bir hasta, gözüne yerleştirilen ışık kapısı ve özel bir gözlük sayesinde önündeki nesneleri yeniden fark edip sayabildi, onlara dokunabildi. Bu tek bir hastaydı ve görme kısmiydi; çalışmalar sürüyor.")}
      <p class="nb-val rv"><strong>İnsanlık için değeri:</strong> Beyni artık yalnızca seyretmiyoruz; ona soru sorup cevabını alabiliyoruz. Deisseroth'un sözleriyle: “Işığı bilgi toplamak için değil, bir şeylerin olmasını sağlamak için kullanıyoruz.”</p>
    </div>
  </section>

  <section class="nb" id="kimya">
    <div class="wrap">
      <p class="eyebrow">Kimya · 7 Ekim 2026</p>
      <h2>Aynadaki el</h2>
      <p class="nb-who">Henri B. Kagan · Kenso Soai</p>
      <p class="nb-cite">“Asimetrik organik sentezde doğrusal olmayan etkilerin ve otokatalizin keşfi için”</p>
      <p class="nb-one"><b>Tek cümleyle:</b> Birbirinin ayna görüntüsü olan iki molekülden yalnızca birini üretmenin, hatta küçücük bir farkı kendi kendine büyütmenin yolunu gösterdiler.</p>
      <div class="nb-two">
        <div class="tx">
          <p>Ellerinize bakın: Birbirinin ayna görüntüsü, ama sağ eldiven sol ele olmuyor. Pek çok molekül de böyle “sağ elli” ve “sol elli” iki biçimde bulunur. Atomlar aynı, bağlar aynı; fark yalnızca ayna görüntüsü.</p>
          <p>Beden bu farkı hemen anlar: Aynı molekülün bir eli nane, öteki eli Frenk kimyonu gibi kokar. İlaçlarda da durum aynı. Kullandığımız ilaçların yarısından fazlası böyle “elli” moleküllerdir ve çoğu zaman yalnızca bir eli işe yarar.</p>
          <p>İşin tuhafı şu: Laboratuvarda sıradan bir tepkime iki elden eşit miktarda üretir. Canlılar ise hep tek eli kullanır; proteinlerimizin yapı taşları sol elli, DNA'mızdaki şekerler sağ ellidir. Bu tercih nasıl başladı? Yüz yılı aşkın süredir yanıtsız bir soruydu.</p>
        </div>
        <figure class="nb-fig">
          <div class="nb-stage" id="mt">{MIT_SVG}</div>
          <figcaption>Sağ ve sol eldiven birbirinin ayna görüntüsü, ama üst üste oturmuyor: Başparmaklar ters tarafta kalıyor.</figcaption>
        </figure>
      </div>
      <div class="nb-duo">
        <div class="nb-box rv" id="kg">
          <h3>Kagan: Uyuyan çiftler</h3>
          <p>Henri Kagan 1986'da şaşırtıcı bir şey gösterdi: Tepkimeyi yönlendiren yardımcı molekül (katalizör) tam saf olmasa bile ürün neredeyse saf çıkabiliyordu. Çünkü yardımcılar çift çift dolaşır; bir sağ ile bir sol eşleşirse o çift uykuya dalar.</p>
          <p>Yardımcıların dörtte üçü sağ, dörtte biri sol elliyse çiftler şöyle dağılır:</p>
          <div class="kb" aria-hidden="true"><i class="rr" style="--w:56"></i><i class="ll" style="--w:6"></i><i class="rl" style="--w:38"></i></div>
          <ul class="kb-l">
            <li class="rr"><b>%56</b><span>sağ + sağ: iş başında</span></li>
            <li class="ll"><b>%6</b><span>sol + sol: iş başında</span></li>
            <li class="rl"><b>%38</b><span>sağ + sol: uykuda</span></li>
          </ul>
          <p class="sum">Karışımın dörtte üçü sağ elliydi; iş başındaki çiftlerin onda dokuzu sağ elli oldu.</p>
        </div>
        <div class="nb-box rv" id="so">
          <h3>Soai: Kendini çoğaltan fark</h3>
          <p>Kenso Soai 1995'te daha da ileri gitti: Öyle bir tepkime buldu ki ortaya çıkan ürün, kendi kopyasının üretilmesine yardım ediyor. Başta bir elden gözle görülmeyecek kadar küçük bir fazlalık varsa, her turda bu fark büyüyor.</p>
          <div class="so-tabs" role="group" aria-label="Tepkime turu"><button type="button" aria-pressed="true">Başlangıç</button><button type="button" aria-pressed="false">1. tur</button><button type="button" aria-pressed="false">2. tur</button></div>
          <div class="so-grid" aria-hidden="true"></div>
          <p class="so-lab">İki el neredeyse eşit. Bir elin fazlalığı yalnızca %0,00005.</p>
          <p class="so-lab" hidden>Fazlalık %57: Her 100 molekülün yaklaşık 79'u artık aynı elli.</p>
          <p class="so-lab" hidden>Fazlalık %99: Moleküllerin neredeyse hepsi aynı elli.</p>
        </div>
      </div>
      {_dby("1848: Louis Pasteur, kristalleri cımbızla tek tek ayırırken moleküllerin iki “elli” olabildiğini fark etti. 1986: Kagan doğrusal olmayan etkiyi, 1995: Soai kendini çoğaltan tepkimeyi gösterdi.",
            "İlaç, koku ve tat moleküllerinde yalnızca doğru eli üretmek artık kimya sanayisinin gündelik işi. Kagan'ın bulgusu, tam saf olmayan bir yardımcıyla bile saf ürün alınabileceğini gösterdi.",
            "Hayatın neden tek eli seçtiği sorusu artık deneyle çalışılabiliyor: Küçücük bir tesadüf, kendini çoğaltan bir tepkimeyle bütün bir dünyanın tercihine dönüşebilir. Bu, hayatın başlangıcına dair önemli bir ipucu; kesin yanıt değil.")}
      <p class="nb-val rv"><strong>İnsanlık için değeri:</strong> Aldığınız ilacın doğru “elden” olması bu kimyanın eseri. Ödül komitesi başkanı Heiner Linke'ye göre iki bilim insanı, yüz yılı aşkın bir kimya bilmecesine çözüm getirdi: Tek ellilik kendiliğinden nasıl ortaya çıkabilir? Henri Kagan ödülü 95 yaşında aldı.</p>
    </div>
  </section>

  <section class="nb" id="fizik">
    <div class="wrap">
      <p class="eyebrow">Fizik · 6 Ekim 2026</p>
      <h2>Buzun içindeki teleskop</h2>
      <p class="nb-who">Francis Halzen</p>
      <p class="nb-cite">“IceCube Nötrino Gözlemevi'ne belirleyici katkıları ve astrofizik kökenli yüksek enerjili nötrinoların keşfi için”</p>
      <p class="nb-one"><b>Tek cümleyle:</b> Güney Kutbu'nun buzuna gömülü dev bir dedektörle, evrenin en şiddetli olaylarından gelen “hayalet” parçacıkları yakalamayı başardı.</p>
      <div class="nb-two">
        <div class="tx">
          <p>Nötrinolar neredeyse hiçbir şeyle etkileşmeyen parçacıklardır. Şu an her saniye vücudunuzdan trilyonlarcası geçiyor ve hiçbir şey hissetmiyorsunuz. Yıldızların, hatta bütün Dünya'nın içinden bile durmadan geçerler.</p>
          <p>Bu yüzden eşsiz habercilerdir: Işığın çıkamadığı yerlerden yola çıkıp bize dosdoğru ulaşırlar. Aynı sebeple yakalanmaları da çok zordur.</p>
          <p>Halzen'in fikri şuydu: Çok nadiren de olsa bir nötrino bir atoma çarpar ve küçük bir mavi ışık çakar. Bu ışığı görmek için çok büyük, çok saydam ve çok karanlık bir ortam gerekir. Güney Kutbu'nun buzu tam böyledir. Sıcak suyla buzda yaklaşık 2,5 kilometre derine inen delikler açıldı, içlerine binlerce ışık algılayıcısı sarkıtıldı. Bir kilometreküp buz teleskopa dönüştü.</p>
        </div>
        <figure class="nb-fig">
          <div class="nb-stage" id="ic">{_ic_svg()}</div>
          <div class="nb-ctl"><button type="button" class="cta" id="ic-btn">Bir nötrino gönder</button></div>
          <figcaption>Üstte Güney Kutbu'nun yüzeyi, altta buzun derinindeki algılayıcı dizileri. Nötrino görünmeden gelir, bir atoma çarpar; ortaya çıkan parçacığın mavi ışığını algılayıcılar sırayla görür ve geldiği yönü ele verir.</figcaption>
        </figure>
      </div>
      {_dby("1930: Wolfgang Pauli, kendisinin bile hiç yakalanamayacağını düşündüğü bir parçacık öngördü. 1956'da ilk nötrino yakalandı. Halzen 1980'lerin sonunda buzu dedektöre çevirmeyi önerdi; IceCube 2011'de tamamlandı.",
            "2013: Güneş Sistemi'nin çok ötesinden gelen ilk yüksek enerjili nötrinolar bulundu. Ardından kaynaklar belirmeye başladı: uzak bir gökadanın merkezindeki dev kara delik, NGC 1068 gökadası ve 2023'te kendi Samanyolu'muz.",
            "Sekiz kat daha büyük bir dedektör (IceCube-Gen2) öneriliyor. Işık, kütleçekim dalgaları ve nötrinolar birlikte okunarak evrenin en şiddetli olayları farklı “duyularla” izlenecek.")}
      <p class="nb-val rv"><strong>İnsanlık için değeri:</strong> Gökyüzüne bakmanın yepyeni bir yolu. Binlerce yıl yalnızca ışıkla baktık; şimdi maddenin içinden geçip gelen habercileri de okuyabiliyoruz. Halzen'in itirafı işin insan tarafını anlatıyor: “İşe yarayacağını çok az kişi düşünüyordu; ben de dahil.” Ödülün ardından da sözü 14 ülkeden 450 bilim insanından oluşan ekibine getirdi: Bu büyük ekibin hak ettiği takdiri sonunda ona ulaştırabildiği için içinin rahatladığını söyledi.</p>
    </div>
  </section>

  <section class="nb-end">
    <div class="wrap">
      <p class="eyebrow" style="color:var(--foil);margin-bottom:10px">Üçünün ortak yanı</p>
      <h2>“İşe yaramaz” görünen bir merak</h2>
      <p>Bir gölet yosunu ışığı nasıl görüyor? Bu tepkime neden hesaba uymuyor? Buzun dibinde bir şey parlar mı? Üç soru da sorulduğu gün kimsenin derdine derman olacak gibi görünmüyordu. Kimse “körlüğü tedavi edeceğim” diye yosun incelemeye başlamadı.</p>
      <p>Aradaki süre de düşündürücü: Yosundaki kapının bulunmasından ödüle yirmi yılı aşkın, Kagan'ın bulgusundan ödüle kırk yıl geçti. Bilim çoğu zaman bir maraton; ödül ise bitiş çizgisinde çekilen fotoğraf.</p>
      <p>Fizyoterapist gözüyle bana en yakın geleni ışıkla açılan kapı: İnme ya da Parkinson sonrasında hareketi yeniden kurarken yaslandığımız bilgilerin bir kısmı, beyin devrelerinin bu yöntemle çıkarılan haritalarından geliyor.</p>
      <p class="big rv">Sabırla sorulan küçük bir soru, bir gün hiç tanımadığımız birinin hayatına dokunabilir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(NOBEL_FAQ)}
    </div>
  </section>

  <section>
    <div class="wrap sources">
      <p class="eyebrow">Kaynaklar</p>
      <ol>
        <li>Nobel Ödülü resmî duyuruları: <a href="https://www.nobelprize.org/prizes/medicine/2026/summary/" target="_blank" rel="noopener">Fizyoloji veya Tıp 2026</a>, <a href="https://www.nobelprize.org/prizes/physics/2026/summary/" target="_blank" rel="noopener">Fizik 2026</a>, <a href="https://www.nobelprize.org/prizes/chemistry/2026/summary/" target="_blank" rel="noopener">Kimya 2026</a>. Gerekçe cümleleri ve kimya bölümündeki sayılar resmî duyuru görsellerinden alındı.</li>
        <li><a href="https://www.statnews.com/2026/10/05/nobel-prize-medicine-2026-winner-deisseroth-hegemann-nagel/" target="_blank" rel="noopener">STAT, 5 Ekim 2026: Deisseroth, Hegemann, Nagel awarded 2026 Nobel Prize in Medicine</a></li>
        <li><a href="https://icecube.wisc.edu/news/awards/2026/10/francis-halzen-icecube-principal-investigator-wins-2026-physics-nobel-prize/" target="_blank" rel="noopener">IceCube, 6 Ekim 2026: Francis Halzen wins 2026 Physics Nobel Prize</a></li>
        <li><a href="https://www.forbes.com/sites/michaeltnietzel/2026/10/07/the-2026-nobel-prize-in-chemistry-is-awarded-to-henri-kagan-and-kenso-soai/" target="_blank" rel="noopener">Forbes, 7 Ekim 2026: The 2026 Nobel Prize in Chemistry is awarded to Henri Kagan and Kenso Soai</a></li>
        <li>Sahel J-A, et al. Partial recovery of visual function in a blind patient after optogenetic therapy. <a href="https://www.nature.com/articles/s41591-021-01351-4" target="_blank" rel="noopener">Nature Medicine 2021;27:1223–1229</a></li>
      </ol>
      <div class="note" style="margin-top:22px">Bu sayfa bilgilendirme amaçlıdır. Optogenetik bugün ağırlıklı olarak bir araştırma yöntemidir; insanlardaki uygulamaları klinik çalışma aşamasındadır. Canlandırmalar temsilidir, ölçekli değildir.</div>
    </div>
  </section>
</main>'''

NOBEL_JS = """<script>
(function(){
  var RM = !!(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches);
  var IO = 'IntersectionObserver' in window, NS = 'http://www.w3.org/2000/svg';
  function $(id){ return document.getElementById(id); }
  function watch(el, onIn){
    if (!IO) { el.vis = true; el.classList.add('run'); if (onIn) onIn(); return; }
    var first = true;
    new IntersectionObserver(function(es){
      el.vis = es[0].isIntersecting; el.classList.toggle('run', el.vis);
      if (el.vis && first) { first = false; if (onIn) onIn(); }
    }, {threshold: 0.3}).observe(el);
  }
  // görünürken kendi kendine oynat: ilk gösterim 'first' ms sonra, ardından her 'ms' ms'de bir; kullanıcı dokununca durur
  function auto(el, fn, ms, first){
    watch(el, function(){ el.due = Date.now() + first; });
    if (RM) return;
    setInterval(function(){
      if (el.vis && el.due && !el.manual && !document.hidden && Date.now() >= el.due) { el.due = Date.now() + ms; fn(); }
    }, 150);
  }

  // yumuşak beliriş
  if (IO && !RM) {
    document.body.classList.add('nb-js');
    var ro = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting) { e.target.classList.add('in'); ro.unobserve(e.target); } }); }, {rootMargin: '0px 0px -8% 0px'});
    document.querySelectorAll('.rv').forEach(function(el, i){ el.style.transitionDelay = (i % 3) * 90 + 'ms'; ro.observe(el); });
  }

  // 1 · ışıkla açılan kapı
  var og = $('og');
  if (og) {
    var spk = og.querySelector('.spk'), nEl = $('og-n'), n = 0, k = 0, busy = false;
    var fire = function(){
      if (busy) return; busy = true;
      if (k === 9) { while (spk.firstChild) spk.removeChild(spk.firstChild); k = 0; }
      var p = document.createElementNS(NS, 'path');
      p.setAttribute('d', 'M' + (16 + k * 36) + ' 222l5-2 5-34 6 46 5-10h6'); p.setAttribute('pathLength', '1');
      spk.appendChild(p); k++; n++; nEl.textContent = n;
      og.classList.add('fire');
      setTimeout(function(){ og.classList.remove('fire'); busy = false; }, 980);
    };
    $('og-btn').addEventListener('click', function(){ og.manual = true; fire(); });
    auto(og, fire, 3000, 600);
  }

  // 2 · aynadaki el, uyuyan çiftler
  var mt = $('mt'); if (mt) watch(mt);
  var kg = $('kg'); if (kg) watch(kg);

  // 2 · kendini çoğaltan fark
  var so = $('so');
  if (so) {
    var grid = so.querySelector('.so-grid'), tabs = so.querySelectorAll('.so-tabs button'), labs = so.querySelectorAll('.so-lab');
    var G = [50, 79, 99], st = 0, dots = [], seed = 11, order = [], i, j, t;
    var rnd = function(){ seed = (seed * 1103515245 + 12345) % 2147483648; return seed / 2147483648; };
    for (i = 0; i < 100; i++) order.push(i);
    for (i = 99; i > 0; i--) { j = Math.floor(rnd() * (i + 1)); t = order[i]; order[i] = order[j]; order[j] = t; }
    for (i = 0; i < 100; i++) { t = document.createElement('i'); t.r = order[i]; if (t.r < G[0]) t.className = 'a'; grid.appendChild(t); dots.push(t); }
    var byRank = dots.slice().sort(function(a, b){ return a.r - b.r; });
    var setStage = function(s){
      var c = 0; st = s;
      byRank.forEach(function(d){
        var on = d.r < G[s];
        if (on !== d.classList.contains('a')) {
          d.style.transitionDelay = (RM ? 0 : c * 16) + 'ms'; c++;
          d.classList.toggle('a', on);
        }
      });
      tabs.forEach(function(b, x){ b.setAttribute('aria-pressed', x === s ? 'true' : 'false'); });
      labs.forEach(function(l, x){ l.hidden = x !== s; });
    };
    tabs.forEach(function(b, x){ b.addEventListener('click', function(){ so.manual = true; setStage(x); }); });
    auto(so, function(){ setStage((st + 1) % 3); }, 3200, 1800);
  }

  // 3 · buzun içindeki teleskop
  var ic = $('ic');
  if (ic) {
    var gh = ic.querySelector('.gh'), mu = ic.querySelector('.mu'), vx = ic.querySelector('.vx'), doms = ic.querySelectorAll('.dom');
    var T = [[20, 250, 96, 205, 330, 96], [352, 250, 300, 224, 36, 122], [0, 148, 62, 158, 352, 214], [150, 250, 168, 226, 250, 110]], ti = 0;
    var send = function(){
      var a = T[ti % T.length]; ti++;
      ic.classList.remove('go');
      doms.forEach(function(d){ d.classList.remove('hit'); });
      gh.setAttribute('x1', a[0]); gh.setAttribute('y1', a[1]); gh.setAttribute('x2', a[2]); gh.setAttribute('y2', a[3]);
      mu.setAttribute('x1', a[2]); mu.setAttribute('y1', a[3]); mu.setAttribute('x2', a[4]); mu.setAttribute('y2', a[5]);
      vx.setAttribute('cx', a[2]); vx.setAttribute('cy', a[3]);
      var dx = a[4] - a[2], dy = a[5] - a[3], L2 = dx * dx + dy * dy;
      void ic.offsetWidth;
      doms.forEach(function(d){
        var x = +d.getAttribute('cx'), y = +d.getAttribute('cy');
        var u = Math.max(0, Math.min(1, ((x - a[2]) * dx + (y - a[3]) * dy) / L2));
        var px = a[2] + u * dx - x, py = a[3] + u * dy - y, dist = Math.sqrt(px * px + py * py);
        if (dist < 30) {
          d.style.setProperty('--dl', (RM ? 0 : 0.55 + u * 0.9).toFixed(2) + 's');
          d.style.setProperty('--s', (1.3 + (30 - dist) / 30 * 2).toFixed(2));
          d.classList.add('hit');
        }
      });
      ic.classList.add('go');
    };
    $('ic-btn').addEventListener('click', function(){ ic.manual = true; send(); });
    auto(ic, send, 4800, 500);
  }
})();
</script>
"""

page("nobel-2026.html", "Işık, Ayna ve Buz: 2026 Nobel Ödülleri",
     "2026 Nobel ödülleri sade bir dille: beyin hücrelerini ışıkla çalıştıran optogenetik, tek elli moleküllerin kimyası ve Güney Kutbu'nun buzunda yakalanan kozmik nötrinolar. Canlandırmalarla, dünü ve yarınıyla.",
     "nobel-2026.html", NOBEL_CSS, NOBEL_BODY, NOBEL_JS,
     seo_title="2026 Nobel Ödülleri: Optogenetik, Tek Elli Moleküller, IceCube | İhsan Eren")

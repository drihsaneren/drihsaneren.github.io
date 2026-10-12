# -*- coding: utf-8 -*-
# ÜÇ KAPI: beden, nefes, zihin. Disiplinler arası öz bakım yaklaşımı + sesli etkileşimli seans,
# kanıt pusulası (1895'ten bugüne zaman çizelgesi), "bilimin kenarında" bölümü.
# mind_part.py'den sonra exec edilir. MIND_CSS, WAKE_JS, faq, src_list, ext, BACK kullanılır.

KAPI_CSS = MIND_CSS + """
  :root{--k-b:#8fa476;--k-n:#d8b25e;--k-z:#8fb3c4}
  .k-hero{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:clamp(20px,4vw,52px);align-items:center}
  @media (max-width:860px){.k-hero{grid-template-columns:1fr}}
  .k-sub{font-family:var(--display);font-size:clamp(22px,3.4vw,30px);color:var(--foil);margin:6px 0 14px;letter-spacing:.02em}
  .k-hero .controls{margin-top:20px}
  .k-hero .lede + .soft{margin-top:14px}
  .k-venn{position:relative;width:min(360px,80vw);aspect-ratio:1;margin:0 auto}
  .k-venn .orb{position:absolute;inset:-4%;width:108%;height:108%;animation:kspin 48s linear infinite;pointer-events:none}
  .k-venn .orb circle{fill:none;stroke:rgba(236,229,207,.16);stroke-width:1;stroke-dasharray:2 7}
  .k-venn .orb .dot{fill:var(--foil);stroke:none}
  @keyframes kspin{to{transform:rotate(360deg)}}
  .k-venn a.c{position:absolute;width:58%;aspect-ratio:1;border-radius:50%;mix-blend-mode:screen;text-decoration:none;animation:kbr 9s ease-in-out infinite;transition:filter .3s ease}
  .k-venn a.c:hover,.k-venn a.c:focus-visible{filter:brightness(1.35)}
  .k-venn a.c span{position:absolute;font-family:var(--display);font-size:clamp(14px,2.3vw,18px);letter-spacing:.16em;text-transform:uppercase;color:var(--ink);white-space:nowrap}
  .k-venn .cb{left:0;top:36%;background:radial-gradient(circle at 42% 42%,rgba(143,164,118,.62),rgba(143,164,118,.10) 72%);border:1.5px solid rgba(143,164,118,.85)}
  .k-venn .cn{left:21%;top:0;background:radial-gradient(circle at 50% 42%,rgba(216,178,94,.55),rgba(216,178,94,.08) 72%);border:1.5px solid rgba(216,178,94,.85);animation-delay:-3s}
  .k-venn .cz{left:42%;top:36%;background:radial-gradient(circle at 58% 42%,rgba(143,179,196,.58),rgba(143,179,196,.08) 72%);border:1.5px solid rgba(143,179,196,.85);animation-delay:-6s}
  .k-venn .cb span{left:12%;top:58%}
  .k-venn .cn span{left:50%;top:20%;transform:translateX(-50%)}
  .k-venn .cz span{right:12%;top:58%}
  @keyframes kbr{0%,100%{transform:scale(.97)}50%{transform:scale(1.04)}}
  .k-you{position:absolute;left:50%;top:53%;transform:translate(-50%,-50%);display:grid;justify-items:center;gap:6px;pointer-events:none}
  .k-you i{width:12px;height:12px;border-radius:50%;background:var(--ink);box-shadow:0 0 0 6px rgba(236,229,207,.12),0 0 24px rgba(236,229,207,.7);animation:kpulse 3s ease-in-out infinite}
  .k-you b{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink);font-weight:700}
  @keyframes kpulse{0%,100%{box-shadow:0 0 0 4px rgba(236,229,207,.10),0 0 16px rgba(236,229,207,.5)}50%{box-shadow:0 0 0 10px rgba(236,229,207,.06),0 0 30px rgba(236,229,207,.85)}}
  @media (prefers-reduced-motion:reduce){.k-venn .orb,.k-venn a.c,.k-you i{animation:none}}

  /* seans */
  .k-tool{max-width:900px;margin:0 auto;scroll-margin-top:84px}
  .k-steps{list-style:none;margin:0 0 20px;padding:0;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:6px}
  .k-steps li{font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;font-weight:700;color:var(--muted);text-align:center;padding-top:10px;position:relative;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .k-steps li::before{content:"";position:absolute;left:0;right:0;top:0;height:5px;border-radius:3px;background:rgba(236,229,207,.12)}
  .k-steps li.done::before{background:var(--sc,var(--sage));opacity:.55}
  .k-steps li.on{color:var(--ink)}
  .k-steps li.on::before{background:var(--sc,var(--foil))}
  .k-steps .sb{--sc:var(--k-b)}.k-steps .sn{--sc:var(--k-n)}.k-steps .sz{--sc:var(--k-z)}
  @media (max-width:420px){.k-steps li{font-size:10.5px;letter-spacing:.04em}}
  .k-v h3{font-size:clamp(24px,3.4vw,30px);margin:2px 0 6px;outline:none}
  .k-v .kk{font-size:12px;letter-spacing:.18em;text-transform:uppercase;font-weight:700;margin:0;color:var(--foil)}
  .k-v.vb .kk{color:var(--k-b)}.k-v.vn .kk{color:var(--k-n)}.k-v.vz .kk{color:var(--k-z)}
  .k-sl{display:grid;gap:16px;margin:16px 0 8px}
  .k-sl .r{display:grid;grid-template-columns:minmax(0,1fr) 46px;gap:2px 14px;align-items:center}
  .k-sl .r p{margin:0;font-weight:600;color:var(--ink);font-size:16px}
  .k-sl .r p small{display:block;font-weight:400;color:var(--muted);font-size:13.5px}
  .k-sl .r output{grid-row:1 / span 2;grid-column:2;font-family:var(--display);font-size:30px;color:var(--ink);text-align:right;font-variant-numeric:tabular-nums}
  .k-sl .r input{grid-column:1;margin:4px 0 0}
  .k-sl .rb input{accent-color:var(--k-b)}.k-sl .rn input{accent-color:var(--k-n)}.k-sl .rz input{accent-color:var(--k-z)}
  .k-rec{margin:14px 0 0;padding:14px 16px;border-radius:12px;background:var(--ground);border:1px solid var(--line);color:var(--ink-soft);font-size:15.5px}
  .k-rec b{color:var(--ink)}
  .k-rec small{display:block;color:var(--muted);font-size:13px;margin-top:4px}
  .k-one{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
  .k-one button{all:unset;box-sizing:border-box;cursor:pointer;min-height:40px;padding:8px 15px;border-radius:999px;border:1px solid var(--line-strong);font-size:14.5px;color:var(--ink-soft)}
  .k-one button:hover,.k-one button.rec{color:var(--ink);border-color:var(--foil)}
  .k-one button.rec{background:rgba(216,178,94,.14)}
  .k-one button:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .k-door{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:clamp(18px,4vw,44px);align-items:center}
  @media (max-width:760px){.k-door{grid-template-columns:1fr}}
  .k-stage{border-radius:14px;background:var(--ground);border:1px solid var(--line);min-height:260px;display:grid;place-items:center;padding:12px;position:relative;overflow:hidden}
  .k-cue{font-family:var(--display);font-size:clamp(20px,2.8vw,25px);line-height:1.3;color:var(--ink);margin:6px 0 4px;min-height:2.6em}
  .k-mid{display:flex;align-items:center;gap:18px;margin:10px 0 12px}
  .k-mid .ws-ring .fg{stroke:var(--k-b)}
  .k-v.vn .ws-ring .fg{stroke:var(--k-n)}
  .k-small{font-size:14px;color:var(--muted);margin:8px 0 0}
  .k-tool .lnk{all:unset;cursor:pointer;color:var(--foil);font-size:14px;font-weight:600;text-decoration:underline;text-underline-offset:3px}
  .k-tool .lnk:focus-visible{outline:2px solid var(--gold);outline-offset:2px}

  /* beden figürü */
  .k-fig{width:min(210px,52vw);height:auto;overflow:visible}
  .k-fig .l{fill:none;stroke:var(--k-b);stroke-width:9;stroke-linecap:round;stroke-linejoin:round}
  .k-fig .far{opacity:.42}
  .k-fig .hd{fill:var(--k-b)}
  .k-fig .gr{stroke:rgba(236,229,207,.25);stroke-width:3;stroke-linecap:round}
  .k-fig .ch{fill:none;stroke:rgba(236,229,207,.35);stroke-width:4;stroke-linecap:round;stroke-linejoin:round}
  .k-fig g{transform-box:view-box}
  .k-fig .bob{transform-origin:70px 200px}
  .k-fig .thA,.k-fig .thB{transform-origin:70px 104px}
  .k-fig .shA,.k-fig .shB{transform-origin:70px 150px}
  .k-fig .arA,.k-fig .arB{transform-origin:70px 52px}
  .k-fig .s-thA,.k-fig .s-thB{transform-origin:62px 120px}
  .k-fig .s-shA,.k-fig .s-shB{transform-origin:104px 120px}
  .k-fig .s-arA,.k-fig .s-arB{transform-origin:62px 66px}
  .k-run .k-fig .bob{animation:kbob .6s ease-in-out infinite}
  .k-run .k-fig .thA{animation:kth 1.2s ease-in-out infinite}
  .k-run .k-fig .thB{animation:kth 1.2s ease-in-out infinite -.6s}
  .k-run .k-fig .shA{animation:ksh 1.2s ease-in-out infinite}
  .k-run .k-fig .shB{animation:ksh 1.2s ease-in-out infinite -.6s}
  .k-run .k-fig .arA{animation:kar 1.2s ease-in-out infinite}
  .k-run .k-fig .arB{animation:kar 1.2s ease-in-out infinite -.6s}
  .k-run .k-fig .s-thA{animation:ksth 1.2s ease-in-out infinite}
  .k-run .k-fig .s-thB{animation:ksth 1.2s ease-in-out infinite -.6s}
  .k-run .k-fig .s-shA{animation:kssh 1.2s ease-in-out infinite}
  .k-run .k-fig .s-shB{animation:kssh 1.2s ease-in-out infinite -.6s}
  .k-run .k-fig .s-arA{animation:kar 1.2s ease-in-out infinite}
  .k-run .k-fig .s-arB{animation:kar 1.2s ease-in-out infinite -.6s}
  @keyframes kbob{0%,100%{transform:translateY(0)}50%{transform:translateY(-3px)}}
  @keyframes kth{0%,50%,100%{transform:rotate(0)}25%{transform:rotate(-58deg)}}
  @keyframes ksh{0%,50%,100%{transform:rotate(0)}25%{transform:rotate(72deg)}}
  @keyframes kar{0%,100%{transform:rotate(30deg)}50%{transform:rotate(-30deg)}}
  @keyframes ksth{0%,50%,100%{transform:rotate(0)}25%{transform:rotate(-20deg)}}
  @keyframes kssh{0%,50%,100%{transform:rotate(0)}25%{transform:rotate(20deg)}}
  .k-fig .sit{display:none}
  .k-seated .k-fig .std{display:none}
  .k-seated .k-fig .sit{display:inline}
  @media (prefers-reduced-motion:reduce){.k-run .k-fig *{animation:none!important}}

  /* zihin */
  .k-map{display:grid;grid-template-columns:150px minmax(0,1fr);gap:clamp(14px,3vw,28px);align-items:start}
  @media (max-width:560px){.k-map{grid-template-columns:110px minmax(0,1fr)}}
  .k-body svg{width:100%;height:auto;overflow:visible}
  .k-body .z{fill:rgba(236,229,207,.07);stroke:rgba(236,229,207,.28);stroke-width:1.2;cursor:pointer;transition:fill .35s ease,stroke .35s ease}
  .k-body .z:hover{fill:rgba(143,179,196,.18)}
  .k-body .z.on{fill:rgba(143,179,196,.55);stroke:var(--k-z);filter:drop-shadow(0 0 7px rgba(143,179,196,.7))}
  .k-q{font-weight:600;color:var(--ink);margin:0 0 8px;font-size:16px}
  .k-q small{font-weight:400;color:var(--muted);font-size:13.5px}
  .k-chips{display:flex;flex-wrap:wrap;gap:7px;margin:0 0 14px}
  .k-chips button{all:unset;box-sizing:border-box;cursor:pointer;min-height:36px;padding:6px 13px;border-radius:999px;border:1px solid var(--line);font-size:14px;color:var(--ink-soft);line-height:1.3}
  .k-chips button:hover{border-color:var(--k-z);color:var(--ink)}
  .k-chips button[aria-pressed="true"]{background:var(--k-z);border-color:var(--k-z);color:var(--ground);font-weight:600}
  .k-chips button:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .k-say{font-family:var(--display);font-size:clamp(21px,3vw,27px);line-height:1.35;color:var(--ink);margin:6px 0 14px;padding:12px 0 12px 16px;border-left:3px solid var(--k-z);min-height:2.7em}
  .k-say.empty{font-family:var(--body);font-size:15px;color:var(--muted)}
  .k-msg textarea{width:100%;min-height:76px;resize:vertical;font:inherit;font-size:15.5px;color:var(--ink);background:var(--ground);border:1px solid var(--line-strong);border-radius:10px;padding:10px 12px}
  .k-msg label{display:block;font-weight:600;color:var(--ink);margin:0 0 6px}
  .k-msg label small{font-weight:400;color:var(--muted)}
  .k-stay{display:flex;align-items:center;gap:16px;margin-top:14px}
  .k-pulse{width:56px;height:56px;border-radius:50%;flex:none;background:radial-gradient(circle,rgba(143,179,196,.55),rgba(143,179,196,.1) 70%);border:1px solid rgba(143,179,196,.7);transform:scale(.7)}
  .k-stay.on .k-pulse{animation:kst 6s ease-in-out infinite}
  @keyframes kst{0%,100%{transform:scale(.65)}45%{transform:scale(1)}}
  .k-stay p{margin:0;color:var(--ink-soft)}
  .k-stay b{font-family:var(--display);font-weight:400;font-size:26px;color:var(--ink);margin-right:6px}

  /* çıkış */
  .k-res{display:grid;gap:12px;margin:14px 0 6px}
  .k-res .row{display:grid;grid-template-columns:76px minmax(0,1fr) 92px;gap:14px;align-items:center}
  .k-res .row > span{font-weight:600;color:var(--ink);font-size:15px}
  .k-res .bars{display:grid;gap:4px}
  .k-res .bars i{display:block;height:10px;border-radius:5px;width:0;transition:width .9s cubic-bezier(.2,.8,.2,1)}
  .k-res .bars i.pre{background:rgba(236,229,207,.16)}
  .k-res .rb .bars i.post{background:var(--k-b)}.k-res .rn .bars i.post{background:var(--k-n)}.k-res .rz .bars i.post{background:var(--k-z)}
  .k-res b{font-variant-numeric:tabular-nums;color:var(--ink);text-align:right;font-weight:600;white-space:nowrap}
  .k-res b em{font-style:normal;font-size:13px;margin-left:6px;color:var(--muted)}
  .k-res b em.up{color:#e0a07a}.k-res b em.dn{color:#b9cba0}
  .k-final{font-family:var(--display);font-size:clamp(20px,2.8vw,24px);line-height:1.35;color:var(--ink);margin:16px 0 4px}
  .k-hist{margin-top:22px;padding-top:16px;border-top:1px solid var(--line);display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:clamp(16px,3vw,32px)}
  @media (max-width:700px){.k-hist{grid-template-columns:1fr}}
  .k-hist h4{font-family:var(--display);font-weight:400;font-size:19px;margin:0 0 8px;color:var(--ink)}
  .k-hist ul{list-style:none;margin:0;padding:0;display:grid;gap:6px}
  .k-hist li{display:flex;justify-content:space-between;gap:12px;font-size:14px;color:var(--ink-soft);border-bottom:1px dashed var(--line);padding-bottom:6px}
  .k-hist li b{color:var(--ink);font-weight:600;font-variant-numeric:tabular-nums;white-space:nowrap}
  .k-doors{display:flex;gap:16px}
  .k-doors div{display:grid;justify-items:center;gap:2px;font-size:12.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.1em}
  .k-doors svg{width:40px;height:50px}
  .k-doors b{font-weight:600;font-size:22px;color:var(--ink);letter-spacing:0;font-variant-numeric:tabular-nums}

  /* üç kapı neden */
  .k-why{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
  @media (max-width:900px){.k-why{grid-template-columns:1fr}}
  .k-why article{border:1px solid var(--line);border-radius:16px;padding:20px 20px 18px;background:var(--ground-2);border-top:3px solid var(--dc);display:grid;gap:10px;align-content:start;scroll-margin-top:90px}
  .k-why .wb{--dc:var(--k-b)}.k-why .wn{--dc:var(--k-n)}.k-why .wz{--dc:var(--k-z)}
  .k-why .kk{font-size:12px;letter-spacing:.18em;text-transform:uppercase;font-weight:700;color:var(--dc);margin:0}
  .k-why h3{font-size:22px}
  .k-why p{margin:0;color:var(--ink-soft);font-size:15.5px}
  .k-why p.k-small{font-size:13.5px}

  /* ilkeler */
  .k-pr{list-style:none;margin:16px 0 0;padding:0;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px;counter-reset:p}
  @media (max-width:980px){.k-pr{grid-template-columns:repeat(2,minmax(0,1fr))}}
  @media (max-width:560px){.k-pr{grid-template-columns:1fr}}
  .k-pr li{counter-increment:p;border:1px solid var(--line);border-radius:14px;padding:16px;background:var(--ground-2);display:grid;gap:6px;align-content:start}
  .k-pr li::before{content:counter(p);font-family:var(--display);font-size:30px;line-height:1;color:var(--foil)}
  .k-pr b{font-family:var(--display);font-weight:400;font-size:19px;color:var(--ink);line-height:1.25}
  .k-pr span{font-size:14.5px;color:var(--ink-soft)}
  .k-pr small{font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;font-weight:700;color:var(--muted)}

  /* kanıt pusulası + zaman çizelgesi */
  .lv1{--bc:#8fa476}.lv2{--bc:#d8b25e}.lv3{--bc:#dd8f52}.lv4{--bc:#c48a9b}.lv5{--bc:#8fb3c4}
  .bdg{display:inline-flex;align-items:center;gap:7px;font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;font-weight:700;color:var(--bc)}
  .bdg::before{content:"";width:9px;height:9px;border-radius:50%;background:var(--bc);flex:none}
  .k-leg{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px;margin:16px 0 6px}
  @media (max-width:900px){.k-leg{grid-template-columns:repeat(2,minmax(0,1fr))}}
  @media (max-width:480px){.k-leg{grid-template-columns:1fr}}
  .k-leg div{border:1px solid var(--line);border-left:3px solid var(--bc);border-radius:10px;padding:10px 12px;background:var(--ground-2)}
  .k-leg p{margin:4px 0 0;font-size:13.5px;color:var(--ink-soft);line-height:1.45}
  .k-filt{margin-top:18px}
  .k-tl{list-style:none;margin:22px 0 0;padding:0;position:relative;display:grid;gap:14px}
  .k-tl::before{content:"";position:absolute;left:62px;top:6px;bottom:6px;width:2px;background:linear-gradient(var(--line-strong),rgba(216,178,94,.08))}
  .k-tl li{display:grid;grid-template-columns:52px minmax(0,1fr);gap:28px;align-items:start;transition:opacity .6s ease,transform .6s ease}
  .k-tl li[hidden]{display:none}
  .k-tl.js li:not(.in){opacity:0;transform:translateY(16px)}
  .k-tl .yr{font-family:var(--display);font-size:20px;color:var(--ink);text-align:right;line-height:1.2;padding-top:12px;font-variant-numeric:tabular-nums;position:relative}
  .k-tl .yr::after{content:"";position:absolute;right:-21px;top:19px;width:12px;height:12px;border-radius:50%;background:var(--bc);box-shadow:0 0 0 4px var(--ground)}
  .k-tl article{border:1px solid var(--line);border-radius:14px;padding:14px 16px;background:var(--ground-2);display:grid;gap:6px}
  .k-tl h3{font-size:20px}
  .k-tl p{margin:0;font-size:15px;color:var(--ink-soft)}
  .k-tl .src{font-size:13px;color:var(--muted)}
  @media (max-width:520px){.k-tl::before{left:40px}.k-tl li{grid-template-columns:34px minmax(0,1fr);gap:18px}.k-tl .yr{font-size:15px;padding-top:14px}.k-tl .yr::after{right:-14px;top:19px;width:10px;height:10px}}
  @media (prefers-reduced-motion:reduce){.k-tl.js li:not(.in){opacity:1;transform:none}}

  /* bilimin kenarında */
  .k-fr{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:16px}
  @media (max-width:820px){.k-fr{grid-template-columns:1fr}}
  .k-fr article{border:1px solid var(--line);border-radius:16px;padding:20px;background:var(--ground-2);display:grid;gap:10px;align-content:start}
  .k-fr h3{font-size:23px}
  .k-fr p.role{font-size:13.5px;color:var(--muted);margin-top:-6px}
  .k-fr p{margin:0;color:var(--ink-soft);font-size:15.5px}
  .k-fr p.ev{color:var(--ink);border-top:1px solid var(--line);padding-top:10px}
  .k-why2{margin-top:22px;border:1px solid var(--line);border-radius:16px;padding:20px;background:var(--ground)}
  .k-why2 h3{font-size:22px;margin-bottom:10px}
  .k-quote{margin:26px 0 0;padding:clamp(20px,3vw,30px);border-radius:16px;background:radial-gradient(120% 140% at 0% 0%,rgba(143,179,196,.14),transparent 60%),radial-gradient(120% 140% at 100% 100%,rgba(216,178,94,.12),transparent 60%),var(--ground-2);border:1px solid var(--line-strong)}
  .k-quote blockquote{margin:0;font-family:var(--display);font-size:clamp(22px,3.2vw,30px);line-height:1.35;color:var(--ink)}
  .k-quote p{margin:12px 0 0;color:var(--ink-soft)}
  .k-quote p b{color:var(--foil);font-weight:600}
"""

# ---------------------------------------------------------------- seans figürleri
K_FIG = '''<svg class="k-fig" viewBox="0 0 140 214" aria-hidden="true">
  <g class="std"><g class="bob">
    <g class="arB far"><path class="l" d="M70 52 L70 84 L84 102"/></g>
    <g class="thB far"><path class="l" d="M70 104 L70 150"/><g class="shB"><path class="l" d="M70 150 L70 192 L86 192"/></g></g>
    <path class="l" d="M70 42 L70 104"/>
    <circle class="hd" cx="72" cy="24" r="14"/>
    <g class="thA"><path class="l" d="M70 104 L70 150"/><g class="shA"><path class="l" d="M70 150 L70 192 L86 192"/></g></g>
    <g class="arA"><path class="l" d="M70 52 L70 84 L84 102"/></g>
  </g><path class="gr" d="M28 202 H112"/></g>
  <g class="sit">
    <path class="ch" d="M40 72 L40 124 L104 124 M44 124 L44 176 M100 124 L100 176"/>
    <g class="s-arB far"><path class="l" d="M62 66 L62 94 L76 110"/></g>
    <g class="s-thB far"><path class="l" d="M62 120 L104 120"/><g class="s-shB"><path class="l" d="M104 120 L104 166 L120 166"/></g></g>
    <path class="l" d="M60 54 L62 120"/>
    <circle class="hd" cx="62" cy="36" r="14"/>
    <g class="s-thA"><path class="l" d="M62 120 L104 120"/><g class="s-shA"><path class="l" d="M104 120 L104 166 L120 166"/></g></g>
    <g class="s-arA"><path class="l" d="M62 66 L62 94 L76 110"/></g>
    <path class="gr" d="M24 178 H128"/>
  </g>
</svg>'''

# (kimlik, düğme metni, -de hâli) — svg bölgeleri aynı kimliği taşır
K_ZONES = [
 ("head", "Baş", "başımda"), ("throat", "Boğaz", "boğazımda"), ("shoulders", "Omuzlar", "omuzlarımda"),
 ("chest", "Göğüs", "göğsümde"), ("belly", "Karın", "karnımda"), ("back", "Sırt", "sırtımda"),
 ("arms", "Kollar ve eller", "kollarımda ve ellerimde"), ("legs", "Bacaklar", "bacaklarımda"),
]
K_EMOS = ["Kaygı", "Gerginlik", "Korku", "Öfke", "Üzüntü", "Yorgunluk", "Yalnızlık", "Utanç", "Suçluluk",
          "Hayal kırıklığı", "Huzursuzluk", "Boşluk", "Merak", "Sakinlik", "Umut", "Minnet"]

K_BODY_SVG = '''<svg viewBox="0 0 120 244" aria-hidden="true">
  <circle class="z" data-z="head" cx="60" cy="22" r="16"/>
  <rect class="z" data-z="throat" x="53" y="38" width="14" height="11" rx="3"/>
  <rect class="z" data-z="shoulders" x="28" y="49" width="64" height="12" rx="6"/>
  <rect class="z" data-z="chest" x="36" y="62" width="48" height="34" rx="7"/>
  <rect class="z" data-z="belly" x="38" y="97" width="44" height="44" rx="8"/>
  <rect class="z" data-z="arms" x="16" y="62" width="13" height="40" rx="6"/>
  <rect class="z" data-z="arms" x="91" y="62" width="13" height="40" rx="6"/>
  <path class="z" data-z="arms" d="M15 108 a6.5 6.5 0 0 1 13 0 V142 a8.5 8.5 0 1 1 -13 0 Z"/>
  <path class="z" data-z="arms" d="M92 108 a6.5 6.5 0 0 1 13 0 V142 a8.5 8.5 0 1 1 -13 0 Z"/>
  <rect class="z" data-z="legs" x="38" y="144" width="21" height="50" rx="9"/>
  <rect class="z" data-z="legs" x="61" y="144" width="21" height="50" rx="9"/>
  <rect class="z" data-z="legs" x="40" y="196" width="17" height="34" rx="8"/>
  <rect class="z" data-z="legs" x="63" y="196" width="17" height="34" rx="8"/>
  <ellipse class="z" data-z="legs" cx="46" cy="237" rx="11" ry="5.5"/>
  <ellipse class="z" data-z="legs" cx="74" cy="237" rx="11" ry="5.5"/>
</svg>'''

def _k_door_icon(col):
    return (f'<svg viewBox="0 0 40 50" aria-hidden="true"><path d="M6 48 V20 a14 14 0 0 1 28 0 V48" fill="none" stroke="{col}" stroke-width="3"/>'
            f'<path d="M12 48 V22 a8 8 0 0 1 16 0 V48" fill="{col}" opacity=".25"/><circle cx="24" cy="34" r="1.8" fill="{col}"/></svg>')

K_ZONE_CHIPS = "".join(f'<button type="button" data-z="{z}" aria-pressed="false">{t}</button>' for z, t, _ in K_ZONES)
K_ZONE_LOCS = "".join(f'<span data-k="loc_{z}">{l}</span>' for z, _, l in K_ZONES)
K_EMO_CHIPS = "".join(f'<button type="button" aria-pressed="false">{e}</button>' for e in K_EMOS)

# ---------------------------------------------------------------- kanıt pusulası
K_LEVELS = [
 (1, "Güçlü kanıt", "Pek çok araştırmada işe yaradığı görüldü ya da bir sağlık otoritesi öneriyor."),
 (2, "Umut verici", "İlk sonuçlar iyi, ama araştırmalar az ya da küçük; daha fazlası gerekiyor."),
 (3, "Tartışmalı", "Çok kullanılıyor, ama temel fikri bilim insanları arasında tartışılıyor."),
 (4, "Yeterli kanıt yok", "Uygulayanlar var, ama işe yaradığı araştırmalarla yeterince gösterilmedi."),
 (5, "Tarihsel fikir", "Bugünkü düşünceyi şekillendirdi, ama kendisi kanıtlanmış değil."),
]
K_LVNAME = {n: t for n, t, _ in K_LEVELS}

# (yıl, düzey, başlık, metin, kaynak notu)
K_TL = [
 ("1895", 5, "Bastırılmış duygu, bedensel belirti", "Breuer ve Freud, açıklanamayan bedensel şikâyetlerin bastırılmış acı anılarla ilgili olabileceğini öne sürdü. Bugün bu tablonun bir bölümüne fonksiyonel nörolojik bozukluk deniyor: Beyin sağlam, ama çalışma biçiminde bir aksama var. Tedavide fizyoterapi ve psikoterapi birlikte kullanılıyor.", "Breuer ve Freud, 1895; Worcestershire NHS"),
 ("1907", 5, "Duyguyu deride ölçmek", "Jung, insanlara kelimeler söyleyip akıllarına gelen ilk kelimeyi sordu ve bu sırada derideki elektriksel değişimi ölçtü. Duygusal yükü olan kelimelerde ibre belirgin biçimde oynadı. Psikolojinin bedeni ölçtüğü ilk deneylerden biri; bu ölçüm bugün de araştırmalarda kullanılıyor.", "Peterson ve Jung, Brain, 1907"),
 ("1929", 1, "Kasları sıkıp bırakmak", "Edmund Jacobson, aşamalı kas gevşetmeyi kitaplaştırdı. Kaygıda gevşeme eğitimini inceleyen 27 çalışmalık analizde etki orta-büyük düzeydeydi.", "Jacobson, 1929; Manzoni ve ark., 2008"),
 ("1933", 5, "Kas zırhı", "Wilhelm Reich, Karakter Analizi’nde ve sonraki çalışmalarında, bastırılan duyguların bedende süregiden kas gerginliği olarak bir “zırh” oluşturduğunu öne sürdü. Fikir bilimsel olarak doğrulanmadı; ama beden odaklı pek çok terapiye ilham verdi.", "Reich, Karakter Analizi, 1933"),
 ("1987", 1, "Bir park yürüyüşü", "Francine Shapiro, yürürken göz hareketlerinin rahatsız edici anılarının yükünü hafiflettiğini fark etti. 1989’daki ilk kontrollü çalışmanın ardından gelişen EMDR, 2013’te Dünya Sağlık Örgütü’nün travma sonrası stres bozukluğunda önerdiği tedaviler arasına girdi.", "Shapiro, 1989; EMDR Institute"),
 ("1995", 3, "Polivagal teori", "Stephen Porges, güvende hissetme ile vagus siniri arasında bağ kuran bir kuram öne sürdü. Klinikte çok popüler; ancak temel varsayımları 2023’te ayrıntılı biçimde eleştirildi. Bazı klinisyenler, kuram tartışmalı olsa da önerdiği nefes, ses ve hareket pratiklerini yararlı buluyor.", "Porges, 1995; Grossman, 2023; Giroux ve ark., 2023"),
 ("1996", 4, "Ruhsal Teknoloji ve PEAT", "Živorad Mihajlović Slavinski’nin Sırbistan’da kurduğu topluluk ve geliştirdiği PEAT yöntemi. İşe yaradığını gösteren karşılaştırmalı bir araştırma bulamadık; ne aldığımızı aşağıda anlatıyoruz.", "Pinal Villanueva, 2024"),
 ("2006", 1, "Tek bir egzersiz seansı", "158 çalışmayı ve 13.101 kişiyi bir araya getiren analizde, tek bir egzersiz seansı bile insanları daha canlı ve enerjik hissettirdi. En iyi sonuçlar hafif tempoda ve 35 dakikaya kadar süren seanslarda görüldü.", "Reed ve Ones, 2006"),
 ("2006", 2, "Duyguları yazmak", "Duygularını yazıya döken kişileri inceleyen 146 çalışmanın birlikte değerlendirmesinde küçük ama gerçek bir fayda görüldü.", "Frattaroli, 2006"),
 ("2007", 2, "Adını koymak", "UCLA’da 30 kişiyle yapılan beyin görüntüleme çalışmasında, öfkeli ya da korkmuş bir yüze bakarken duyguya isim vermek, beyindeki tehlike alarmı sayılan bölgenin (amigdala) tepkisini azalttı.", "Lieberman ve ark., 2007"),
 ("2007", 4, "Duygu Kodu", "Bradley Nelson’ın, “hapsolmuş duyguları” kas testi ve mıknatısla bulup serbest bırakmayı öne süren yöntemi. Yöntemi test eden bir araştırma bulamadık; dayandığı kas testi ise çift kör bir araştırmada şanstan iyi sonuç vermedi.", "Schwartz ve ark., 2014"),
 ("2014", 2, "Duyguların beden haritası", "Finlandiya’da 701 kişi, farklı duyguları hissettiklerinde bedenlerinin neresinde bir şeylerin canlandığını ya da söndüğünü boyadı. Her duygunun kendine özgü bir haritası çıktı; haritalar Batı Avrupa ile Doğu Asya’da benzerdi.", "Nummenmaa ve ark., 2014"),
 ("2016", 2, "Bilerek alınan plasebo", "Portekiz’de 97 bel ağrılı hasta, içinde ilaç olmadığını bilerek 3 hafta boyunca hap aldı ve ağrıları yaklaşık %30 azaldı; yalnızca olağan tedaviye devam edenlerde azalma yaklaşık %9’du. Beklenti ve ilişki, iyileşmenin gerçek bir parçası olabilir.", "Carvalho ve ark., 2016"),
 ("2017", 2, "Somatik Deneyimleme", "Beden duyumlarına odaklanan bir travma terapisi, 63 kişilik bir araştırmada 15 seansta, bekleyen gruba göre travma sonrası stres belirtilerini belirgin biçimde azalttı. Tek bir araştırma; tekrarlanması gerekiyor.", "Brom ve ark., 2017"),
 ("2017", 2, "Dakikada 6 nefes", "Nefesini dakikada yaklaşık 6’ya yavaşlatan grup, ardından gelen stresli bir zihin görevinde daha düşük büyük tansiyon değerleri gösterdi ve kendini daha iyi hissettiğini söyledi.", "Front Public Health, 2017"),
 ("2023", 2, "Döngüsel iç çekiş", "Bir ay boyunca her gün 5 dakika iki kez alıp uzun veren kişilerin olumlu duyguları, meditasyon yapanlara göre daha çok arttı ve dinlenirken daha yavaş nefes almaya başladılar.", "Balban ve ark., 2023"),
 ("2024", 1, "Egzersiz ve depresyon", "218 çalışmayı ve 14.170 kişiyi inceleyen analizde yürüyüş ya da koşu, yoga ve güç çalışması depresyon belirtilerini azalttı; önerilen tempo arttıkça fayda da büyüdü.", "Noetel ve ark., 2024"),
]

def _k_legend():
    return "".join(f'<div class="lv{n}"><span class="bdg">{t}</span><p>{d}</p></div>' for n, t, d in K_LEVELS)

def _k_filter():
    b = '<button type="button" data-v="0" aria-pressed="true">Tümü</button>'
    b += "".join(f'<button type="button" data-v="{n}" aria-pressed="false">{t}</button>' for n, t, _ in K_LEVELS)
    return f'<div class="seg k-filt" role="group" aria-label="Kanıt düzeyi" id="k-filt">{b}</div>'

def _k_tl():
    out = []
    for y, lv, h, p, s in K_TL:
        out.append(f'<li class="lv{lv}" data-lv="{lv}"><span class="yr">{y}</span><article><span class="bdg">{K_LVNAME[lv]}</span>'
                   f'<h3>{h}</h3><p>{p}</p><p class="src">{s}</p></article></li>')
    return "\n".join(out)

K_MASTERS = [
 (5, "Carl Gustav Jung", "İsviçreli psikiyatrist, 1875–1961",
  "Görmezden geldiğimiz duygular ve yanlarımız kaybolmaz; fark edilmeyi bekler. Jung, insanları iç dünyalarındaki duygu ve imgelerle konuşmaya davet etti.",
  "Zihin kapısındaki “Bu duygu size bir şey söylemek isteseydi, ne derdi?” sorusu."),
 (4, "Eugene Gendlin", "Amerikalı filozof ve psikolog, 1926–2017",
  "“Odaklanma” adını verdiği yöntemde, bir sorunun bedende henüz kelimelere dökülmemiş bulanık bir hissi olduğunu anlattı. O hisse sabırla eşlik edip ona uyan kelimeyi ya da imgeyi bulmak, bedende bir rahatlama getirebilir.",
  "Duyguyu önce bedende bulup sonra ona isim vermek ve “Bu his bir şekil ya da renk olsaydı?” sorusu. Yöntem 1980’lerden sonra az araştırıldı."),
 (2, "Peter Levine", "Amerikalı psikolog, Somatik Deneyimleme’nin kurucusu",
  "Zor yaşantıların yükü bedende kalabilir. Levine bu yükle küçük parçalar hâlinde çalışmayı ve dikkati, zorlayan bir duyum ile rahat hissettiren bir bölge arasında sarkaç gibi gidip getirmeyi önerir.",
  "Duygunun yanında kalırken zorlanırsanız dikkatinizi ayaklarınıza götürmeniz. Yöntemi sınayan ilk karşılaştırmalı araştırmanın sonucu umut verici."),
 (4, "Živorad Mihajlović Slavinski", "Sırp yazar, 1937 doğumlu",
  "Batı ezoterizmi üzerine 30 kadar kitap yazdı ve “ruhsal teknoloji” adını verdiği yirmi kadar yöntem geliştirdi. Bunlardan PEAT’te, bir sorunun altında birbirine zıt kutuplar bulunduğunu ve bunları bulup “nötrleştirmenin” rahatlattığını öne sürer.",
  "Zihin kapısındaki “Bu duygunun karşıtı ne olurdu? İkisini birden fark edebilir misiniz?” sorusu. PEAT’in işe yaradığını gösteren bir araştırma bulamadık."),
 (4, "Bradley Nelson", "ABD’li kiropraktör, Duygu Kodu’nun kurucusu",
  "Yaşanmış zor duyguların bedende “hapsolmuş duygular” olarak kaldığını öne sürer. Uygulayıcı bunları kolu bastırarak yapılan bir kas testiyle arar ve alından enseye doğru gezdirilen bir mıknatısla “serbest bırakmaya” çalışır.",
  "Duyguyu bedende aramak fikri bizde de var. Ama kas testi ya da mıknatıs yerine sizin kendi farkındalığınızı kullanıyoruz; çünkü kas testi, 51 kişilik çift kör bir araştırmada şanstan iyi sonuç vermedi."),
 (1, "Edmund Jacobson", "Amerikalı hekim, 1888–1983",
  "Gerginliği fark etmenin yolunun, kası önce bilerek sıkıp sonra bırakmak olduğunu gösterdi ve aşamalı kas gevşetmeyi geliştirdi.",
  "Beden kapısında omuzlarınızı sıkıp bırakarak gerginlik ile gevşeme arasındaki farkı fark etmeniz. Ayrıntılı rehber: <a href=\"kas-gevsetme.html\">Kas gevşetme</a>."),
 (1, "Francine Shapiro", "Amerikalı psikolog, 1948–2019",
  "Bir park yürüyüşünde fark ettiği küçük bir şeyi ciddiye aldı, sonra sınadı. Bu gözlemden doğan EMDR, bugün travma sonrası stres bozukluğunda önerilen tedaviler arasında.",
  "Gözlemi ciddiye almak, sonra sınamak: yaklaşımımızın ruhu."),
 (5, "Viktor Frankl", "Avusturyalı psikiyatrist, 1905–1997",
  "Toplama kamplarından sağ çıktıktan sonra yazdığı İnsanın Anlam Arayışı’nda, değiştiremediğimiz durumlarda bile o duruma karşı tutumumuzu seçebileceğimizi anlattı.",
  "Zihin kapısındaki “Bu durumda neyi değiştiremiyorsunuz, neyi seçebilirsiniz?” sorusu."),
]

def _k_masters():
    return "\n".join(f'        <article class="lv{lv}"><span class="bdg">{K_LVNAME[lv]}</span><h3>{n}</h3><p class="role">{r}</p><p>{i}</p><p class="ev"><b>Üç Kapı’da:</b> {u}</p></article>' for lv, n, r, i, u in K_MASTERS)

K_FAQ = [
 ("Üç Kapı bir terapi mi?", "Hayır. Üç Kapı, günlük hayatta kullanabileceğiniz bir öz bakım pratiğidir; bir tanının ya da tedavinin yerini tutmaz. Haftalardır süren kaygı, çökkünlük ya da travma belirtileriniz varsa bir ruh sağlığı uzmanına başvurabilirsiniz; travma sonrası stres bozukluğunda EMDR gibi etkinliği gösterilmiş tedaviler var."),
 ("Hangi kapıdan başlamalıyım?", "Seansın başındaki üç soru size bir öneri sunar. Bizim yaklaşımımızda zihin çok doluyken önce beden ve nefesle başlamak, sonra kelimelere geçmek öneriliyor; ama en iyi kapı, sizin için açılandır. Seans sonundaki ölçümlerle hangi kapının size daha çok iyi geldiğini zamanla görebilirsiniz."),
 ("Seans sırasında duygularım yoğunlaşırsa ne yapmalıyım?", "Durabilirsiniz. Gözlerinizi açıp çevrenize bakın, ayaklarınızın yere bastığını hissedin ve normal nefesinize dönün. Bir duyguya yaklaşmak bazen onu önce daha belirgin kılar; kendinizi zorlamanız gerekmez."),
 ("Başım dönerse ya da dengem zayıfsa?", "Nefes kapısında baş dönmesi olursa hemen normal nefesinize dönün; ikinci nefes kısa ve hafif olabilir. Beden kapısında dengeniz zayıfsa oturarak yapma seçeneğini kullanabilirsiniz."),
 ("Kanıtı olmayan yöntemleri denemeli miyim?", "Bu sizin kararınız. Denemeyi düşünüyorsanız hekiminizin önerdiği tedaviyi bırakmayın, bu yöntemleri tanı koymak için kullanmayın ve uygulayıcıya “Bu yöntem bir araştırmayla sınandı mı?” diye sorabilirsiniz. Kesin sonuç vaat eden ve yüksek ücret isteyen uygulamalara karşı dikkatli olabilirsiniz."),
]

K_SRC = [
 "Nummenmaa L, Glerean E, Hari R, Hietanen JK. Bodily maps of emotions. Proc Natl Acad Sci U S A. 2014;111(2):646–651. Haber: " + ext("https://www.aalto.fi/news/finnish-research-team-reveals-how-emotions-are-mapped-in-the-body", "Aalto University, Finnish research team reveals how emotions are mapped in the body") + ".",
 "Reed J, Ones DS. The effect of acute aerobic exercise on positive activated affect: a meta-analysis. Psychol Sport Exerc. 2006;7(5):477–514. " + ext("https://experts.umn.edu/en/publications/the-effect-of-acute-aerobic-exercise-on-positive-activated-affect/", "experts.umn.edu") + ".",
 "Noetel M, Sanders T, Gallardo-Gómez D, et al. " + ext("https://www.bmj.com/content/384/bmj-2023-075847", "Effect of exercise for depression: systematic review and network meta-analysis of randomised controlled trials") + ". BMJ. 2024;384:e075847.",
 "Balban MY, Neri E, Kogon MM, et al. " + ext("https://www.cell.com/cell-reports-medicine/fulltext/S2666-3791(22)00474-8", "Brief structured respiration practices enhance mood and reduce physiological arousal") + ". Cell Rep Med. 2023;4(1):100895.",
 "Steffen PR, Austin T, DeBarros A, Brown T. The impact of resonance frequency breathing on measures of heart rate variability, blood pressure, and mood. Front Public Health. 2017;5:222. " + ext("https://pubmed.ncbi.nlm.nih.gov/28890890/", "PubMed") + ".",
 "Lieberman MD, Eisenberger NI, Crockett MJ, et al. Putting feelings into words: affect labeling disrupts amygdala activity in response to affective stimuli. Psychol Sci. 2007;18(5):421–428. Haber: " + ext("https://www.sciencedaily.com/releases/2007/06/070622090727.htm", "ScienceDaily, Putting feelings into words produces therapeutic effects in the brain") + ".",
 "Frattaroli J. Experimental disclosure and its moderators: a meta-analysis. Psychol Bull. 2006;132(6):823–865. " + ext("https://stafforini.com/works/frattaroli-2006-experimental-disclosure-its/", "Özet") + ".",
 "Manzoni GM, Pagnini F, Castelnuovo G, Molinari E. " + ext("https://www.biomedcentral.com/1471-244X/8/41", "Relaxation training for anxiety: a ten-years systematic review with meta-analysis") + ". BMC Psychiatry. 2008;8:41.",
 "Shapiro F. Efficacy of the eye movement desensitization procedure in the treatment of traumatic memories. J Trauma Stress. 1989;2(2):199–223. Tarihçe: " + ext("https://www.emdr.com/history-of-emdr/", "EMDR Institute, The history of EMDR therapy") + ".",
 "Brom D, Stokar Y, Lawi C, et al. Somatic experiencing for posttraumatic stress disorder: a randomized controlled outcome study. J Trauma Stress. 2017;30(3):304–312. " + ext("https://cris.huji.ac.il/en/publications/somatic-experiencing-for-posttraumatic-stress-disorder-a-randomiz/", "cris.huji.ac.il") + ".",
 "Carvalho C, Caetano JM, Cunha L, et al. Open-label placebo treatment in chronic low back pain: a randomized controlled trial. Pain. 2016;157(12):2766–2772. Haber: " + ext("https://www.medicalnewstoday.com/articles/313522", "Medical News Today") + ".",
 "Porges SW. Orienting in a defensive world: mammalian modifications of our evolutionary heritage. A polyvagal theory. Psychophysiology. 1995;32(4):301–318.",
 "Grossman P. " + ext("https://zenodo.org/records/7955274", "Fundamental challenges and likely refutations of the five basic premises of the polyvagal theory") + ". 2023.",
 "Giroux C, Ahlers D, Miawotoe A. " + ext("https://journalofpsychiatryreform.com/2023/10/17/polyvagal-approaches-scientifically-questionable-but-useful-in-practice/", "Polyvagal approaches: scientifically questionable but useful in practice") + ". J Psychiatry Reform. 2023;10(11).",
 "Breuer J, Freud S. Studien über Hysterie. Leipzig, Wien: Deuticke; 1895.",
 "Worcestershire Acute Hospitals NHS Trust. " + ext("https://www.worcsacute.nhs.uk/leaflets/what-is-functional-neurological-disorder-fnd/", "What is functional neurological disorder (FND)?") + ".",
 "Peterson F, Jung CG. Psycho-physical investigations with the galvanometer and pneumograph in normal and insane individuals. Brain. 1907;30(2):153–218. " + ext("https://www.mpi.nl/node/47641", "mpi.nl") + ".",
 "Jacobson E. Progressive relaxation. Chicago: University of Chicago Press; 1929.",
 "Reich W. Charakteranalyse. Wien: Selbstverlag; 1933.",
 "Elezović N. " + ext("https://www.bib.irb.hr/1046538", "Živorad Mihajlović Slavinski – author of globally influental systems of spiritual technology") + ". CEENASWE konferansı, Belgrad, 2016.",
 "Pinal Villanueva M. " + ext("https://eap-iea.org/index.php/eap/article/view/1259", "Processing entities: healing practices and body conceptions in the New Age group “Spiritual Technology”") + ". Etnoantropološki problemi. 2024;19(2):573–595.",
 "Mihajlović Slavinski Ž. PEAT: Primordial Energy Activation and Transcendence and the Neutralization of Polarities. Kitap.",
 "Nelson B. The Emotion Code. Kitap. Yöntemin anlatımı: " + ext("https://allwithin.substack.com/p/what-is-emotion-code", "All Within, What is Emotion Code?") + ".",
 "Schwartz SA, Utts J, Spottiswoode SJP, et al. A double-blind, randomized study to assess the validity of applied kinesiology (AK) as a diagnostic tool and as a nonlocal proximity effect. Explore (NY). 2014;10(2):99–108. Özet: " + ext("https://skepdoc.info/?p=6276", "SkepDoc") + ".",
]

K_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <div class="k-hero">
      <div>
        <p class="eyebrow">Kendine iyi bak · Yeni bir yaklaşım</p>
        <h1>Üç Kapı</h1>
        <p class="k-sub">Beden, nefes, zihin</p>
        <p class="lede">Bazen ne kadar düşünseniz de içinizdeki düğüm çözülmez. Bu, bir şeyi yanlış yaptığınız anlamına gelmez: Duygular yalnızca kafada yaşamaz; göğsünüzde, omuzlarınızda, nefesinizde de yaşar. Üç Kapı, o düğüme üç yoldan yaklaşmanın bir yolu: bedeninizi hareket ettirmek, nefesinizi yavaşlatmak ve hissettiğinize bir isim vermek.</p>
        <p class="soft">Fizyoterapiden, psikolojiden ve beyin araştırmalarından gelen bulguları, kendi alanında iz bırakmış ustaların fikirleriyle bir araya getirdik. Neyin araştırmalarla desteklendiğini, neyin yalnızca deneyime dayandığını her adımda açıkça söylüyoruz.</p>
        <div class="controls">
          <a class="cta" href="#seans">6 dakikalık seansa başla</a>
          <a class="cta ghost" href="#pusula">Kanıt pusulası</a>
        </div>
        <p class="meta">Son güncelleme: 12 Ekim 2026</p>
      </div>
      <div class="k-venn">
        <svg class="orb" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="49"/><circle class="dot" cx="50" cy="1" r="1.3"/></svg>
        <a class="c cn" href="#kapi-nefes"><span>Nefes</span></a>
        <a class="c cb" href="#kapi-beden"><span>Beden</span></a>
        <a class="c cz" href="#kapi-zihin"><span>Zihin</span></a>
        <div class="k-you"><i></i><b>Siz</b></div>
      </div>
    </div>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>701 kişi</b><span>Duyguları bedenlerinin neresinde hissettiklerini işaretledi: her duygunun kendine özgü bir haritası çıktı</span></div>
        <div class="stat"><b>158 çalışma</b><span>Tek bir egzersiz seansı bile insanı daha canlı hissettiriyor; en iyi sonuç hafif tempoda</span></div>
        <div class="stat"><b>5 dakika</b><span>Her gün iki kez alıp uzun veren nefesle bir ayda olumlu duygular, meditasyona göre daha çok arttı</span></div>
        <div class="stat"><b>30 kişi</b><span>Beyin görüntülemede, bir duyguya isim vermek beyindeki tehlike alarmının tepkisini azalttı</span></div>
      </div>
    </div>
  </section>

  <section id="seans">
    <div class="wrap">
      <p class="eyebrow">Birlikte yapalım</p>
      <h2>Üç Kapı seansı</h2>
      <p class="soft">Yaklaşık 6 dakika, sadece sizin için. Önce nasıl olduğunuza bakın, sonra üç kapıdan sırayla geçin ve sonunda yeniden bakın. Sesi açarsanız rehber her adımda yanınızda olur; gözlerinizi kapatabilirsiniz.</p>
      <div class="tool k-tool" id="kapi">
        <ol class="k-steps" aria-hidden="true">
          <li data-s="in">Giriş</li><li class="sb" data-s="body">Beden</li><li class="sn" data-s="breath">Nefes</li><li class="sz" data-s="mind">Zihin</li><li data-s="out">Çıkış</li>
        </ol>

        <div class="k-v" data-v="in">
          <p class="kk">Giriş</p>
          <h3 tabindex="-1">Bugün hangi kapı açık?</h3>
          <p class="soft">Şu an nasılsınız? 0 ile 10 arasında puanlayın. Doğru ya da yanlış cevap yok; yalnızca şu anı fark ediyoruz.</p>
          <div class="k-sl" id="k-sl-in">
            <div class="r rb"><p>Bedenim gergin <small>0 gevşek · 10 çok gergin</small></p><output>5</output><input type="range" min="0" max="10" step="1" value="5" aria-label="Bedenim gergin"></div>
            <div class="r rn"><p>Nefesim sıkışık <small>0 rahat · 10 çok sıkışık ya da hızlı</small></p><output>5</output><input type="range" min="0" max="10" step="1" value="5" aria-label="Nefesim sıkışık"></div>
            <div class="r rz"><p>Zihnim dolu <small>0 sakin · 10 çok dolu ya da karışık</small></p><output>5</output><input type="range" min="0" max="10" step="1" value="5" aria-label="Zihnim dolu"></div>
          </div>
          <div class="k-rec" id="k-rec" aria-live="polite"></div>
          <div class="controls" style="margin-top:16px"><button type="button" class="cta" id="k-full">Tam tur · 6 dakika</button></div>
          <p class="k-small">Ya da yalnızca bir kapı:</p>
          <div class="k-one" id="k-one">
            <button type="button" data-m="body">Beden · 1,5 dk</button><button type="button" data-m="breath">Nefes · 2 dk</button><button type="button" data-m="mind">Zihin · 2 dk</button>
          </div>
          <label class="snd"><input type="checkbox" id="k-voice" checked> Sesli rehber</label>
        </div>

        <div class="k-v vb" data-v="body" hidden>
          <div class="k-door">
            <div class="k-stage" id="k-bstage">{K_FIG}</div>
            <div>
              <p class="kk">Kapı 1 · Beden</p>
              <h3 tabindex="-1">Hareket edin</h3>
              <p class="k-cue" id="k-bcue" aria-live="polite"></p>
              <div class="k-mid">
                <div class="ws-ring"><svg viewBox="0 0 132 132" aria-hidden="true"><circle class="bg" cx="66" cy="66" r="58"/><circle class="fg" id="k-barc" cx="66" cy="66" r="58" stroke-dasharray="364.4" stroke-dashoffset="0"/></svg><b id="k-btime">1:30</b></div>
              </div>
              <div class="seg" role="group" aria-label="Pozisyon" id="k-pos">
                <button type="button" data-v="std" aria-pressed="true">Ayakta</button>
                <button type="button" data-v="sit" aria-pressed="false">Oturarak</button>
              </div>
              <div class="controls" style="margin-top:12px"><button type="button" class="cta" id="k-bgo">Duraklat</button><button type="button" class="cta ghost" data-act="skip">Sonraki kapı</button></div>
            </div>
          </div>
        </div>

        <div class="k-v vn" data-v="breath" hidden>
          <div class="k-door">
            <div class="k-stage">
              <div class="br-stage">
                <svg class="prog" viewBox="0 0 200 200" aria-hidden="true"><circle class="bg" cx="100" cy="100" r="96"/><circle class="fg" id="k-narc" cx="100" cy="100" r="96" stroke-dasharray="603.2" stroke-dashoffset="603.2"/></svg>
                <div class="br-core" id="k-ncore" style="background:radial-gradient(circle at 38% 35%, rgba(236,229,207,.28), rgba(216,178,94,.5) 45%, rgba(216,178,94,.14) 75%);border-color:rgba(216,178,94,.6)"></div>
                <div class="br-center"><b id="k-ntime">2:00</b><span id="k-ncount">&nbsp;</span></div>
              </div>
            </div>
            <div>
              <p class="kk">Kapı 2 · Nefes</p>
              <h3 tabindex="-1">İki kez alın, uzun verin</h3>
              <p class="k-cue" id="k-ncue" aria-live="polite"></p>
              <p class="br-sub" id="k-nsub"></p>
              <div class="rhythm" aria-hidden="true"><i id="k-rh0"></i><i id="k-rh1"></i><i class="out" id="k-rh2"></i></div>
              <div class="controls"><button type="button" class="cta" id="k-ngo">Duraklat</button><button type="button" class="cta ghost" data-act="skip">Sonraki kapı</button></div>
              <p class="k-small">Baş dönmesi olursa normal nefesinize dönün. Daha uzun bir uygulama için <a href="ic-cekis.html">5 dakikalık iç çekiş nefesi</a>.</p>
            </div>
          </div>
        </div>

        <div class="k-v vz" data-v="mind" hidden>
          <p class="kk">Kapı 3 · Zihin</p>
          <h3 tabindex="-1">Fark edin, adını koyun</h3>
          <div class="k-map">
            <div class="k-body" id="k-body">{K_BODY_SVG}</div>
            <div>
              <p class="k-q">Bedeninizde nerede hissediyorsunuz? <small>Birden fazla seçebilirsiniz.</small></p>
              <div class="k-chips" id="k-zones">{K_ZONE_CHIPS}</div>
              <p class="k-q">Ona bir isim verin <small>En fazla üç kelime.</small></p>
              <div class="k-chips" id="k-emos">{K_EMO_CHIPS}</div>
            </div>
          </div>
          <p class="k-say empty" id="k-say" aria-live="polite"></p>
          <div class="k-msg">
            <p class="k-q">Ustaların soruları <small id="k-qsrc"></small></p>
            <label for="k-note" id="k-qtxt"></label>
            <textarea id="k-note" maxlength="400" placeholder="İsterseniz buraya yazın; hiçbir yere kaydedilmez."></textarea>
            <div class="controls" style="margin-top:8px"><button type="button" class="lnk" id="k-qnext">Başka bir soru</button></div>
          </div>
          <div class="k-stay" id="k-stay"><div class="k-pulse" aria-hidden="true"></div><p id="k-stayp">Bu duyguyu değiştirmeye çalışmadan, üç nefes boyunca yanında kalın. Zorlanırsanız dikkatinizi ayaklarınıza götürün.</p></div>
          <div class="controls" style="margin-top:14px"><button type="button" class="cta" id="k-zgo">Üç nefes yanında kal</button><button type="button" class="cta ghost" data-act="skip">Çıkışa geç</button></div>
        </div>

        <div class="k-v" data-v="out" hidden>
          <div data-o="ask">
            <p class="kk">Çıkış</p>
            <h3 tabindex="-1">Şimdi nasılsınız?</h3>
            <p class="soft">Aynı üç soruyu yeniden puanlayın.</p>
            <div class="k-sl" id="k-sl-out">
              <div class="r rb"><p>Bedenim gergin <small>0 gevşek · 10 çok gergin</small></p><output>5</output><input type="range" min="0" max="10" step="1" value="5" aria-label="Bedenim gergin"></div>
              <div class="r rn"><p>Nefesim sıkışık <small>0 rahat · 10 çok sıkışık ya da hızlı</small></p><output>5</output><input type="range" min="0" max="10" step="1" value="5" aria-label="Nefesim sıkışık"></div>
              <div class="r rz"><p>Zihnim dolu <small>0 sakin · 10 çok dolu ya da karışık</small></p><output>5</output><input type="range" min="0" max="10" step="1" value="5" aria-label="Zihnim dolu"></div>
            </div>
            <div class="controls" style="margin-top:14px"><button type="button" class="cta" id="k-see">Sonucu gör</button></div>
          </div>
          <div data-o="res" hidden>
            <p class="kk">Sonuç</p>
            <h3 tabindex="-1">Seans tamam</h3>
            <div class="k-res" id="k-res">
              <div class="row rb"><span>Beden</span><div class="bars"><i class="pre"></i><i class="post"></i></div><b></b></div>
              <div class="row rn"><span>Nefes</span><div class="bars"><i class="pre"></i><i class="post"></i></div><b></b></div>
              <div class="row rz"><span>Zihin</span><div class="bars"><i class="pre"></i><i class="post"></i></div><b></b></div>
            </div>
            <p class="k-final" id="k-final"></p>
            <p class="k-small">Gri çizgi seans öncesini, renkli çizgi sonrasını gösterir.</p>
            <div class="controls" style="margin-top:14px"><button type="button" class="cta" data-act="again">Yeni seans</button></div>
          </div>
        </div>

        <div class="k-hist" id="k-hist">
          <div><h4>Son seanslarınız</h4><ul id="k-hlist"></ul></div>
          <div><h4>Açtığınız kapılar</h4>
            <div class="k-doors">
              <div>{_k_door_icon("#8fa476")}<b id="k-cb">0</b>Beden</div>
              <div>{_k_door_icon("#d8b25e")}<b id="k-cn">0</b>Nefes</div>
              <div>{_k_door_icon("#8fb3c4")}<b id="k-cz">0</b>Zihin</div>
            </div>
            <p class="k-small">Verileriniz yalnızca bu cihazda saklanır. <button type="button" class="lnk" data-act="reset">Kayıtları sil</button></p>
          </div>
        </div>

        <div class="k-s" hidden>
          <span data-k="rec_ok">Bugün kapılarınız açık görünüyor. Tam tur, iyi hâlinizi pekiştirmek için de güzel bir alışkanlık.</span>
          <span data-k="rec_body">Bedeniniz gergin görünüyor. Hareket, gerginliği boşaltmanın en doğrudan yolu olabilir.</span>
          <span data-k="rec_bodyz">Zihniniz çok doluyken düşünerek sakinleşmek zordur. Önce bedenden girmeyi deneyin.</span>
          <span data-k="rec_breath">Nefesiniz sıkışmış görünüyor. Uzun nefes verişler, nefesinizi ve ruh hâlinizi yavaşça toparlayabilir.</span>
          <span data-k="rec_mind">Zihniniz dolu ama ulaşılabilir görünüyor. Hissettiğinize bir isim vermek iyi gelebilir.</span>
          <span data-k="rec_lab">Öneri:</span>
          <span data-k="rec_note">Bu bir öneri, kural değil.</span>
          <span data-k="b1">Yerinde canlı bir tempoda yürüyün, kollarınızı serbestçe sallayın.</span>
          <span data-k="b2">Omuzlarınızı kulaklarınıza doğru kaldırıp sıkın… ve bırakın. Farkı hissedin, sonra yürümeye devam edin.</span>
          <span data-k="b3">Ellerinizi silkeleyin; gerginlik parmak uçlarınızdan akıp gitsin.</span>
          <span data-k="b4">Son yarım dakika: biraz daha canlı, dizlerinizi biraz daha yükseğe kaldırın.</span>
          <span data-k="s1">Sandalyede dik oturun; dizlerinizi sırayla kaldırarak yerinde yürüyün, kollarınızı sallayın.</span>
          <span data-k="s2">Omuzlarınızı kulaklarınıza doğru kaldırıp sıkın… ve bırakın. Farkı hissedin, sonra devam edin.</span>
          <span data-k="s4">Son yarım dakika: biraz daha canlı.</span>
          <span data-k="b_in">Birinci kapı: beden.</span>
          <span data-k="b_done">Beden kapısı tamam. Bir an durun ve kalbinizin atışını fark edin.</span>
          <span data-k="n_in">İkinci kapı: nefes. Burundan iki kez alın, ağızdan uzun verin.</span>
          <span data-k="in1">Burundan nefes alın</span>
          <span data-k="in1s">Göğsünüz ve karnınız yavaşça dolsun.</span>
          <span data-k="in2">Bir kez daha</span>
          <span data-k="in2s">Kısa bir nefes daha ekleyin.</span>
          <span data-k="out">Ağızdan yavaşça verin</span>
          <span data-k="outs">Havanın tamamı çıkana kadar, acele etmeden.</span>
          <span data-k="count">{{n}} nefes</span>
          <span data-k="count1">1 nefes</span>
          <span data-k="n_done">Nefes kapısı tamam.</span>
          <span data-k="z_in">Üçüncü kapı: zihin. Bedeninizde bir şey hissettiğiniz yeri seçin ve ona bir isim verin.</span>
          <span data-k="tpl_both">Şu an {{loc}} {{emo}} fark ediyorum.</span>
          <span data-k="tpl_emo">Şu an {{emo}} fark ediyorum.</span>
          <span data-k="tpl_loc">Şu an {{loc}} bir şey fark ediyorum.</span>
          <span data-k="tpl_none">Seçtikçe cümleniz burada belirecek.</span>
          <span data-k="named">Adını koydunuz. Şimdi onu değiştirmeye çalışmadan, üç nefes boyunca yanında kalın. Zorlanırsanız dikkatinizi ayaklarınıza götürün.</span>
          <span data-k="q1">Bu duygu size bir şey söylemek isteseydi, ne derdi?</span><span data-k="q1s">Jung’dan esinlenen bir soru</span>
          <span data-k="q2">Bu his bedeninizde bir şekil, renk ya da sıcaklık olsaydı, nasıl olurdu?</span><span data-k="q2s">Gendlin’den esinlenen bir soru</span>
          <span data-k="q3">Bu duygunun karşıtı ne olurdu? İkisini birden fark edebilir misiniz?</span><span data-k="q3s">Slavinski’den esinlenen bir soru</span>
          <span data-k="q4">Bu durumda neyi değiştiremiyorsunuz, neyi seçebilirsiniz?</span><span data-k="q4s">Frankl’dan esinlenen bir soru</span>
          <span data-k="stay_n">{{n}}. nefes</span>
          <span data-k="stay_done">Teşekkürler. Şimdi çıkışa geçelim.</span>
          <span data-k="and"> ve </span>
          <span data-k="comma">, </span>
          {K_ZONE_LOCS}
          <span data-k="o_in">Şimdi nasılsınız? Aynı üç soruyu yeniden puanlayın.</span>
          <span data-k="f_good">Bir kapıyı araladınız. Bedeniniz, nefesiniz ve zihniniz aynı ağın parçaları; birini değiştirince ötekiler de kıpırdar.</span>
          <span data-k="f_some">Küçük bir değişim de değişimdir. Yarın aynı saatte yeniden denemeye ne dersiniz?</span>
          <span data-k="f_same">Bugün kapılar ağır açıldı; bu da bir bilgi. Başka bir kapıyla ya da daha uzun bir nefesle yeniden deneyebilirsiniz.</span>
          <span data-k="f_worse">Bazen bir duyguya yaklaşmak onu önce daha belirgin kılar. Kendinizi zorlamayın; bir yakınınızla konuşmak ya da bir uzmandan destek almak iyi gelebilir.</span>
          <span data-k="same">aynı</span>
          <span data-k="m_full">Tam tur</span><span data-k="m_body">Beden</span><span data-k="m_breath">Nefes</span><span data-k="m_mind">Zihin</span>
          <span data-k="h_none">Henüz kayıtlı bir seansınız yok.</span>
          <span data-k="h_row">ortalama {{a}} → {{b}}</span>
          <span data-k="pause">Duraklat</span><span data-k="resume">Devam et</span>
          <span data-k="reset_q">Tüm seans kayıtlarınız bu cihazdan silinsin mi?</span>
        </div>
        <noscript><p class="note">Seans, tarayıcınızda JavaScript açıkken çalışır.</p></noscript>
      </div>
    </div>
  </section>

  <section id="kapilar">
    <div class="wrap">
      <p class="eyebrow">Neden üç kapı?</p>
      <h2>Duyguya üç yoldan ulaşılır</h2>
      <p class="soft">Duygu yalnızca bir düşünce değildir; kaslarda, nefeste ve kelimelerde de yaşar. Her kapının arkasında farklı bir bilim dalı, farklı bir kanıt düzeyi var.</p>
      <div class="k-why">
        <article class="wb" id="kapi-beden">
          <p class="kk">Kapı 1 · Beden</p>
          <h3>Hareket, duyguya en hızlı uzanan yol olabilir</h3>
          <p>158 çalışmayı birleştiren bir analizde tek bir aerobik egzersiz seansı, kendini canlı ve enerjik hissetmeyi orta düzeyde artırdı; etki en az yarım saat sürdü ve en iyi sonuçlar hafif tempoda görüldü. Uzun vadede ise 218 çalışmayı inceleyen 2024 tarihli analizde yürüyüş ya da koşu, yoga ve güç çalışması depresyon belirtilerini azalttı.</p>
          <p class="k-small">Seanstaki 90 saniyelik yürüyüş bu etkileri tek başına sağlamaz; amacı kapıyı aralamaktır. Daha fazlası için <a href="ruh-sagligi-egzersiz.html">Ruh sağlığı için egzersiz</a> ve <a href="kas-gevsetme.html">Kas gevşetme</a> sayfalarına bakabilirsiniz.</p>
        </article>
        <article class="wn" id="kapi-nefes">
          <p class="kk">Kapı 2 · Nefes</p>
          <h3>Hem kendiliğinden hem isteğinizle çalışan sistem</h3>
          <p>Nefes, kendiliğinden işleyen ama istediğimizde yönetebildiğimiz ender bedensel işlevlerden biridir. Stanford’daki bir çalışmada bir ay boyunca her gün 5 dakika döngüsel iç çekiş yapanların olumlu duyguları meditasyon yapanlardan daha çok arttı ve dinlenme hâlindeki solunum hızları düştü. Dakikada yaklaşık 6 nefese yavaşlatılan başka bir çalışmada katılımcılar, stres altında daha düşük büyük tansiyon değerleri gösterdi.</p>
          <p class="k-small">Tek tek çalışmalar; sonuçlar umut verici ama kesin değil. Daha uzun bir uygulama için <a href="ic-cekis.html">5 dakikalık iç çekiş nefesi</a>.</p>
        </article>
        <article class="wz" id="kapi-zihin">
          <p class="kk">Kapı 3 · Zihin</p>
          <h3>Adını koymak</h3>
          <p>UCLA’da 30 kişiyle yapılan bir beyin görüntüleme çalışmasında, öfkeli ya da korkmuş yüzlere bakarken duyguya bir isim vermek, beyindeki tehlike alarmı sayılan bölgenin (amigdala) tepkisini azalttı. Finlandiya’da 701 kişiyle yapılan çalışmada ise her duygu bedende kendine özgü bir harita çizdi. Duyguları yazmak da işe yarayabilir: 146 çalışmayı birleştiren analizde etki küçük ama anlamlıydı.</p>
          <p class="k-small">Çoğu laboratuvar bulgusu; günlük hayattaki etkileri hâlâ araştırılıyor. Ruh hâlinizi izlemek için <a href="ruh-hali-olcumu.html">Ruh hâlinizi ölçün</a>.</p>
        </article>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <p class="eyebrow">Yaklaşımımız</p>
      <h2>Üç Kapı’nın beş ilkesi</h2>
      <ol class="k-pr">
        <li><small>Bilimsel bulgu</small><b>Duygu bedende yaşar</b><span>Duygular yalnızca kafada değil; göğüste, karında, omuzlarda hissedilir. Bedeni dinlemek, duyguyu anlamanın bir yoludur.</span></li>
        <li><small>Klinik yaklaşım</small><b>Aşağıdan yukarıya</b><span>Zihin çok doluyken düşünerek çıkmak zordur. Önce beden ve nefes, sonra kelimeler.</span></li>
        <li><small>Bulgu ve yaklaşım</small><b>Adını koy, yanında kal</b><span>Bir duyguyu hemen değiştirmeye çalışmak yerine önce fark edip adlandırın ve birkaç nefes boyunca yanında kalın.</span></li>
        <li><small>Ölçüm</small><b>Kendi verinize bakın</b><span>Her seansın öncesinde ve sonrasında ölçün; size neyin iyi geldiğini zamanla kendi sonuçlarınız gösterir.</span></li>
        <li><small>Dürüstlük</small><b>Kanıtı etiketleyin</b><span>Bilineni, umulanı ve inanılanı ayırt edin. Merakla bakın, ama kanıt isteyin.</span></li>
      </ol>
      <p class="note" style="margin-top:18px"><strong>Dürüst bir not:</strong> Üç Kapı seansı bir bütün olarak henüz bir araştırmayla sınanmadı; parçaları ayrı ayrı, farklı düzeylerde kanıta dayanıyor. Bu yüzden seansın başında ve sonunda kendi ölçümünüzü yapmanızı istiyoruz: Size neyin iyi geldiğini en iyi kendi verileriniz gösterir.</p>
    </div>
  </section>

  <section id="pusula">
    <div class="wrap">
      <p class="eyebrow">Kanıt pusulası</p>
      <h2>Bedenin hafızası: 1895’ten bugüne</h2>
      <p class="soft">Freud’dan Jung’a, park yürüyüşünden beyin görüntülemeye: beden ile duygu arasındaki bağı anlamaya çalışan fikirler ve yöntemler. Her birinin yanında, bugün ne kadar kanıtla desteklendiğini gösteren bir etiket var.</p>
      <div class="k-leg">{_k_legend()}</div>
      {_k_filter()}
      <ol class="k-tl" id="k-tl">
{_k_tl()}
      </ol>
    </div>
  </section>

  <section id="ustalar">
    <div class="wrap">
      <p class="eyebrow">Ustalardan öğrendiklerimiz</p>
      <h2>Kitaplarıyla, klinikleriyle iz bırakanlar</h2>
      <p class="soft">Bu yaklaşımı kurarken yalnızca araştırma makalelerinden değil, kendi alanında iz bırakmış, kitaplar yazmış, insanlarla yıllarca çalışmış ustalardan da yararlandık. Bazılarının yöntemi araştırmalarla sınandı; bazılarınınki sınanmadı ya da sınavı geçemedi. Her birinden ne aldığımızı ve kanıtın nerede durduğunu açıkça yazıyoruz. Burada yer almaları, yöntemlerinin tümünü önerdiğimiz anlamına gelmez.</p>
      <div class="k-fr">
{_k_masters()}
      </div>
      <div class="k-why2">
        <h3>Kanıtı olmayan bir yöntem neden bazı insanlara iyi geliyor?</h3>
        <ul class="dots">
          <li><b>Beklenti ve ilişki:</b> Portekiz’de 97 kişiyle yapılan bir araştırmada, içinde ilaç olmadığını bilerek hap alan bel ağrılı hastaların ağrısı yaklaşık %30 azaldı; yalnızca olağan tedaviye devam edenlerde bu oran yaklaşık %9’du. Araştırmacılar sıcak ve anlayışlı bir ilişkinin önemine dikkat çekti.</li>
          <li><b>Dikkat ve adlandırma:</b> Bu yöntemlerin çoğu, kişiyi bir duyguyu fark edip adlandırmaya yönlendirir; bunun kendisi bile duygusal tepkiyi azaltabilir.</li>
          <li><b>Sakin bir ortam:</b> Yavaş nefes, dokunuş ve birinin size zaman ayırması kendi başına rahatlatıcı olabilir.</li>
          <li><b>Zamanla hafifleme:</b> Pek çok sıkıntı zaman içinde kendiliğinden azalır ve bu, o sırada yapılan şeye mal edilebilir.</li>
        </ul>
      </div>
      <div class="k-quote">
        <blockquote>Bir yöntemin iyi hissettirmesi, açıklamasının doğru olduğunu göstermez. Ama bir gözlemin değersiz olduğu anlamına da gelmez.</blockquote>
        <p>EMDR de 1987’de bir park yürüyüşünde yapılan kişisel bir gözlemle başladı; 1989’da ilk karşılaştırmalı araştırmayla sınandı ve 2013’te Dünya Sağlık Örgütü’nün önerdiği tedaviler arasına girdi. <b>Klinik gözlem soruyu sorar; bilim cevabını arar.</b> Üç Kapı’nın yolu da bu.</p>
      </div>
      <p class="note" style="margin-top:22px"><strong>Kanıtı olmayan bir yöntemi denemeyi düşünüyorsanız:</strong> Onu tanı koymak için kullanmayın, hekiminizin önerdiği tedaviyi bırakmayın ve kesin sonuç vaat eden, yüksek ücret isteyen uygulamalara karşı dikkatli olun.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(K_FAQ)}
      <div class="note" style="margin-top:22px"><strong>Destek almak önemlidir:</strong> Haftalardır süren kaygı, çökkünlük ya da uyku sorunları geçmiyorsa bir hekime ya da ruh sağlığı uzmanına başvurun. Kendinize zarar verme düşünceleriniz varsa 112'yi arayın.</div>
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list(K_SRC)}
    </div>
  </section>
</main>'''

K_JS = r'''<script>
(function(){
  var root = document.getElementById('kapi'); if (!root) return;
  var S = {}; root.querySelectorAll('.k-s [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var EN = document.documentElement.lang === 'en', LANG = EN ? 'en-GB' : 'tr-TR';
  var $ = function(id){ return document.getElementById(id); };
  var Q = new URLSearchParams(location.search), X = Math.min(50, Math.max(1, +(Q.get('x') || 1)));
  var KEY = 'drihsaneren.ucKapi.v1', snd = $('k-voice'), ctx = null, lock = null;
''' + WAKE_JS + r'''
  function say(t){ if (!snd.checked || !('speechSynthesis' in window) || X > 1) return; try { var u = new SpeechSynthesisUtterance(t); u.lang = LANG; u.rate = .92; speechSynthesis.speak(u); } catch (e) {} }
  function hush(){ try { speechSynthesis.cancel(); } catch (e) {} }
  function load(){ try { return JSON.parse(localStorage.getItem(KEY)) || []; } catch (e) { return []; } }
  function save(h){ try { localStorage.setItem(KEY, JSON.stringify(h.slice(-60))); } catch (e) {} }
  function fmt(n){ return (Math.round(n * 10) / 10).toLocaleString(LANG); }
  function mmss(s){ s = Math.max(0, Math.ceil(s)); var m = Math.floor(s / 60), r = s % 60; return m + ':' + (r < 10 ? '0' : '') + r; }
  function sliders(id){ return [].slice.call($(id).querySelectorAll('input')); }
  function bindSl(id, fn){ sliders(id).forEach(function(i){ i.addEventListener('input', function(){ i.parentNode.querySelector('output').textContent = i.value; if (fn) fn(); }); }); }
  function vals(id){ return sliders(id).map(function(i){ return +i.value; }); }
  function setVals(id, v){ sliders(id).forEach(function(i, k){ i.value = v[k]; i.parentNode.querySelector('output').textContent = v[k]; }); }

  // ---- görünüm yönetimi
  var views = {}; root.querySelectorAll('.k-v').forEach(function(v){ views[v.getAttribute('data-v')] = v; });
  var steps = [].slice.call(root.querySelectorAll('.k-steps li')), ORDER = ['in', 'body', 'breath', 'mind', 'out'];
  var mode = 'full', plan = [], pi = 0, before = [5, 5, 5], cur = 'in';
  function show(v, focus){
    cur = v; for (var k in views) views[k].hidden = k !== v;
    var idx = ORDER.indexOf(v);
    steps.forEach(function(li){ var s = li.getAttribute('data-s'), i = ORDER.indexOf(s);
      li.classList.toggle('on', s === v); li.classList.toggle('done', i < idx && (s === 'in' || plan.indexOf(s) >= 0)); });
    if (focus === false) return;
    var h = views[v].querySelector('h3'); if (h) try { h.focus({preventScroll: true}); } catch (e) {}
    var top = root.getBoundingClientRect().top; if (top < 0 || top > innerHeight * .5) root.scrollIntoView({behavior: 'smooth', block: 'start'});
  }
  function next(){ stopAll(); pi++; if (pi < plan.length) enter(plan[pi]); else toOut(); }
  function enter(d){ if (d === 'body') startBody(); else if (d === 'breath') startBreath(); else startMind(); }

  // ---- giriş: öneri
  var rec = 'body';
  function recommend(){
    var v = vals('k-sl-in'), b = v[0], n = v[1], z = v[2], key;
    if (b <= 3 && n <= 3 && z <= 3) { rec = 'full'; key = 'rec_ok'; }
    else if (z >= 7 && z >= b && z >= n) { rec = 'body'; key = 'rec_bodyz'; }
    else if (b >= n && b >= z) { rec = 'body'; key = 'rec_body'; }
    else if (n >= b && n >= z) { rec = 'breath'; key = 'rec_breath'; }
    else { rec = 'mind'; key = 'rec_mind'; }
    $('k-rec').innerHTML = '<b>' + S.rec_lab + '</b> ' + S[key] + '<small>' + S.rec_note + '</small>';
    root.querySelectorAll('#k-one button').forEach(function(x){ x.classList.toggle('rec', x.getAttribute('data-m') === rec); });
  }
  bindSl('k-sl-in', recommend); bindSl('k-sl-out');
  function begin(m){
    unlockAudio(); mode = m; plan = m === 'full' ? ['body', 'breath', 'mind'] : [m]; pi = 0; before = vals('k-sl-in');
    enter(plan[0]);
  }
  $('k-full').addEventListener('click', function(){ begin('full'); });
  $('k-one').addEventListener('click', function(e){ var b = e.target.closest('button'); if (b) begin(b.getAttribute('data-m')); });
  function unlockAudio(){ try { if ('speechSynthesis' in window) speechSynthesis.getVoices(); } catch (e) {} }

  // ---- ortak zamanlayıcı
  var raf = 0, last = 0, running = false, tick = null;
  function loop(now){ if (!running) return; var dt = Math.min(.25, (now - last) / 1000) * X; last = now; if (tick) tick(dt); if (running) raf = requestAnimationFrame(loop); }
  function run(fn){ tick = fn; running = true; last = performance.now(); cancelAnimationFrame(raf); raf = requestAnimationFrame(loop); wake(true); }
  function halt(){ running = false; cancelAnimationFrame(raf); wake(false); }
  function stopAll(){ halt(); hush(); $('k-bstage').classList.remove('k-run'); $('k-stay').classList.remove('on'); stayT = -1; }
  root.addEventListener('click', function(e){
    var a = e.target.closest('[data-act]'); if (!a) return; var act = a.getAttribute('data-act');
    if (act === 'skip') { if (cur === 'mind') { stopAll(); toOut(); } else next(); }
    if (act === 'again') { stopAll(); setVals('k-sl-in', [5, 5, 5]); recommend(); show('in'); }
    if (act === 'reset' && confirm(S.reset_q)) { save([]); history(); }
  });

  // ---- 1 · beden (90 sn)
  var BT = 90, bel = 0, bcue = -1, seated = false, bstage = $('k-bstage');
  var BCUE = [0, 22, 45, 62];
  function bkeys(){ return seated ? ['s1', 's2', 'b3', 's4'] : ['b1', 'b2', 'b3', 'b4']; }
  function bdraw(){ $('k-btime').textContent = mmss(BT - bel); $('k-barc').style.strokeDashoffset = (364.4 * Math.min(1, bel / BT)).toFixed(1); }
  function bsetCue(i, speak){ bcue = i; var t = S[bkeys()[i]]; $('k-bcue').textContent = t; if (speak) say(i === 0 ? S.b_in + ' ' + t : t); }
  function btick(dt){
    bel += dt; var i = 0; for (var j = 0; j < BCUE.length; j++) if (bel >= BCUE[j]) i = j;
    if (i !== bcue) bsetCue(i, true);
    if (bel >= BT) { bel = BT; bdraw(); halt(); bstage.classList.remove('k-run'); say(S.b_done); beep(523, .4, .07); setTimeout(next, 2200 / X); return; }
    bdraw();
  }
  function startBody(){ show('body'); bel = 0; bcue = -1; bstage.classList.add('k-run'); $('k-bgo').textContent = S.pause; bsetCue(0, true); bdraw(); run(btick); }
  $('k-bgo').addEventListener('click', function(){
    if (running) { halt(); hush(); bstage.classList.remove('k-run'); this.textContent = S.resume; }
    else if (bel < BT) { bstage.classList.add('k-run'); this.textContent = S.pause; run(btick); }
  });
  $('k-pos').addEventListener('click', function(e){ var b = e.target.closest('button'); if (!b) return;
    this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
    seated = b.getAttribute('data-v') === 'sit'; bstage.classList.toggle('k-seated', seated); if (bcue >= 0) bsetCue(bcue, false); });

  // ---- 2 · nefes (120 sn, döngüsel iç çekiş)
  var NT = 120, P = [2.5, 1, 6.5], nel = 0, ph = 0, pt = 0, breaths = 0, C = 603.2, LO = .6, MID = .9, HI = 1;
  var rh = [$('k-rh0'), $('k-rh1'), $('k-rh2')];
  (function(){ var tot = P[0] + P[1] + P[2]; rh.forEach(function(r, j){ r.style.flex = (P[j] / tot).toFixed(3); }); })();
  function ease(x){ return x < .5 ? 2 * x * x : 1 - Math.pow(-2 * x + 2, 2) / 2; }
  function nscale(){ var x = Math.min(1, pt / P[ph]); return ph === 0 ? LO + (MID - LO) * ease(x) : ph === 1 ? MID + (HI - MID) * ease(x) : HI - (HI - LO) * ease(x); }
  function nphase(n){ ph = n; pt = 0; var k = ['in1', 'in2', 'out'][n]; $('k-ncue').textContent = S[k]; $('k-nsub').textContent = S[k + 's']; beep([392, 523, 330][n], n === 2 ? .6 : .3, .07); }
  function ndraw(){
    $('k-ncore').style.transform = 'scale(' + nscale().toFixed(4) + ')';
    $('k-narc').style.strokeDashoffset = (C * (1 - Math.min(1, nel / NT))).toFixed(1);
    $('k-ntime').textContent = mmss(NT - nel);
    $('k-ncount').textContent = breaths ? (breaths === 1 ? S.count1 : S.count.replace('{n}', breaths)) : ' ';
    for (var j = 0; j < 3; j++) rh[j].style.setProperty('--p', (j < ph ? 1 : j === ph ? Math.min(1, pt / P[j]) : 0).toFixed(3));
  }
  function ntick(dt){
    pt += dt; nel += dt;
    if (pt >= P[ph]) { if (ph < 2) nphase(ph + 1); else { breaths++; if (nel >= NT - .5) { nel = NT; ndraw(); halt(); say(S.n_done); setTimeout(next, 1800 / X); return; } nphase(0); } }
    ndraw();
  }
  function startBreath(){ show('breath'); nel = 0; breaths = 0; $('k-ngo').textContent = S.pause; say(S.n_in); nphase(0); ndraw(); run(ntick); }
  $('k-ngo').addEventListener('click', function(){
    if (running) { halt(); this.textContent = S.resume; }
    else if (nel < NT) { this.textContent = S.pause; run(ntick); }
  });

  // ---- 3 · zihin
  var zones = [], emos = [], stayT = -1;
  function listJoin(a){ if (a.length < 2) return a.join(''); return a.slice(0, -1).join(S.comma) + S.and + a[a.length - 1]; }
  function sentence(){
    var loc = listJoin(zones.map(function(z){ return S['loc_' + z]; })), emo = listJoin(emos.map(function(e){ return e.toLocaleLowerCase(LANG); }));
    var t = zones.length && emos.length ? S.tpl_both : emos.length ? S.tpl_emo : zones.length ? S.tpl_loc : S.tpl_none;
    var el = $('k-say'); el.textContent = t.replace('{loc}', loc).replace('{emo}', emo); el.classList.toggle('empty', !zones.length && !emos.length);
  }
  function paintZones(){
    root.querySelectorAll('#k-body .z').forEach(function(p){ p.classList.toggle('on', zones.indexOf(p.getAttribute('data-z')) >= 0); });
    root.querySelectorAll('#k-zones button').forEach(function(b){ b.setAttribute('aria-pressed', zones.indexOf(b.getAttribute('data-z')) >= 0 ? 'true' : 'false'); });
    sentence();
  }
  function toggleZone(z){ var i = zones.indexOf(z); if (i >= 0) zones.splice(i, 1); else zones.push(z); paintZones(); }
  $('k-body').addEventListener('click', function(e){ var p = e.target.closest('.z'); if (p) toggleZone(p.getAttribute('data-z')); });
  $('k-zones').addEventListener('click', function(e){ var b = e.target.closest('button'); if (b) toggleZone(b.getAttribute('data-z')); });
  $('k-emos').addEventListener('click', function(e){
    var b = e.target.closest('button'); if (!b) return; var w = b.textContent, i = emos.indexOf(w);
    if (i >= 0) emos.splice(i, 1); else { if (emos.length >= 3) return; emos.push(w); }
    b.setAttribute('aria-pressed', i >= 0 ? 'false' : 'true'); sentence();
  });
  function startMind(){
    show('mind'); zones = []; emos = []; $('k-note').value = '';
    root.querySelectorAll('#k-emos button').forEach(function(b){ b.setAttribute('aria-pressed', 'false'); });
    paintZones(); $('k-stayp').textContent = S.named.split('. ').slice(1).join('. ') || S.named; $('k-zgo').disabled = false; setQ(0); say(S.z_in);
  }
  var qi = 0;
  function setQ(i){ qi = i % 4; $('k-qtxt').textContent = S['q' + (qi + 1)]; $('k-qsrc').textContent = '· ' + S['q' + (qi + 1) + 's']; }
  $('k-qnext').addEventListener('click', function(){ setQ(qi + 1); });
  setQ(0);
  $('k-zgo').addEventListener('click', function(){
    var said = $('k-say').classList.contains('empty') ? '' : $('k-say').textContent + ' ';
    say(said + S.named); this.disabled = true; $('k-stay').classList.add('on'); stayT = 0; var p = $('k-stayp'), btn = this, lastN = 0;
    run(function(dt){ stayT += dt; var n = Math.min(3, Math.floor(stayT / 6) + 1);
      if (n !== lastN) { lastN = n; p.innerHTML = '<b>' + n + '</b>' + S.stay_n.replace('{n}', n); }
      if (stayT >= 18 + 3 * (X > 1 ? 0 : 1)) { halt(); $('k-stay').classList.remove('on'); p.textContent = S.stay_done; say(S.stay_done); btn.disabled = false; setTimeout(toOut, 1600 / X); } });
  });

  // ---- çıkış
  function toOut(){ stopAll(); setVals('k-sl-out', before); views.out.querySelector('[data-o="ask"]').hidden = false; views.out.querySelector('[data-o="res"]').hidden = true; show('out'); say(S.o_in); }
  $('k-see').addEventListener('click', function(){
    var after = vals('k-sl-out'), rows = root.querySelectorAll('#k-res .row'), d = 0;
    views.out.querySelector('[data-o="ask"]').hidden = true; var res = views.out.querySelector('[data-o="res"]'); res.hidden = false;
    rows.forEach(function(r, i){ var pre = r.querySelector('.pre'), post = r.querySelector('.post'); pre.style.width = '0'; post.style.width = '0';
      var dd = after[i] - before[i]; d += dd;
      r.querySelector('b').innerHTML = before[i] + ' → ' + after[i] + '<em class="' + (dd < 0 ? 'dn' : dd > 0 ? 'up' : '') + '">' + (dd === 0 ? S.same : (dd > 0 ? '+' : '−') + Math.abs(dd)) + '</em>';
      setTimeout(function(){ pre.style.width = (before[i] * 10) + '%'; post.style.width = (after[i] * 10) + '%'; }, 60); });
    var avg = d / 3, key = avg <= -2 ? 'f_good' : avg < 0 ? 'f_some' : avg === 0 ? 'f_same' : 'f_worse';
    $('k-final').textContent = S[key]; say(S[key]);
    var h = load(); h.push({t: Date.now(), m: mode, b: before, a: after, w: emos.length, z: zones.length}); save(h); history();
    var hh = res.querySelector('h3'); try { hh.focus({preventScroll: true}); } catch (e) {}
  });
  function history(){
    var h = load(), ul = $('k-hlist'), cb = 0, cn = 0, cz = 0;
    h.forEach(function(s){ if (s.m === 'full' || s.m === 'body') cb++; if (s.m === 'full' || s.m === 'breath') cn++; if (s.m === 'full' || s.m === 'mind') cz++; });
    $('k-cb').textContent = cb; $('k-cn').textContent = cn; $('k-cz').textContent = cz;
    if (!h.length) { ul.innerHTML = '<li>' + S.h_none + '</li>'; return; }
    ul.innerHTML = h.slice(-5).reverse().map(function(s){
      var a = (s.b[0] + s.b[1] + s.b[2]) / 3, b = (s.a[0] + s.a[1] + s.a[2]) / 3, dt = new Date(s.t);
      return '<li><span>' + dt.toLocaleDateString(LANG, {day: 'numeric', month: 'short'}) + ' · ' + S['m_' + s.m] + '</span><b>' + S.h_row.replace('{a}', fmt(a)).replace('{b}', fmt(b)) + '</b></li>';
    }).join('');
  }
  document.addEventListener('visibilitychange', function(){ if (!document.hidden && running) wake(true); });
  recommend(); history(); show('in', false);

  // ---- zaman çizelgesi: süzgeç ve kayarak belirme
  var tl = $('k-tl'), items = [].slice.call(tl.querySelectorAll('li'));
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    tl.classList.add('js');
    var io = new IntersectionObserver(function(es){ es.forEach(function(en){ if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } }); }, {rootMargin: '0px 0px -8% 0px'});
    items.forEach(function(li){ io.observe(li); });
  }
  $('k-filt').addEventListener('click', function(e){ var b = e.target.closest('button'); if (!b) return;
    this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
    var v = b.getAttribute('data-v'); items.forEach(function(li){ li.hidden = v !== '0' && li.getAttribute('data-lv') !== v; li.classList.add('in'); }); });
})();
</script>
'''

page("uc-kapi.html", "Üç Kapı: Beden, Nefes, Zihin",
     "Duygular yalnızca kafada yaşamaz. Hareket, nefes ve kelimelerle duyguya üç kapıdan yaklaşın: 6 dakikalık sesli seans, Freud’dan beyin araştırmalarına kanıt pusulası ve ustalardan öğrendiklerimiz.",
     "uc-kapi.html", KAPI_CSS, K_BODY, K_JS,
     seo_title="Üç Kapı: Beden, Nefes ve Zihinle Duygulara Yaklaşmak | İhsan Eren",
     about={"@type": "Thing", "name": "Duygu düzenleme"}, faq_items=K_FAQ)

# -*- coding: utf-8 -*-
# Kendine iyi bak, 2. tur: yere oturup kalkma testi, duvar oturuşu (tansiyon),
# döngüsel iç çekiş, doğa reçetesi, sosyal bağ. cond4_part.py'den sonra exec edilir.

SELF2_CSS = SELF_CSS + """
  .seg{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0 4px}
  .seg button{all:unset;cursor:pointer;padding:8px 14px;border-radius:999px;border:1px solid var(--line-strong);font-size:14px;color:var(--ink-soft)}
  .seg button:hover{border-color:var(--foil);color:var(--ink)}
  .seg button[aria-pressed="true"]{background:var(--foil);border-color:var(--foil);color:var(--ground);font-weight:600}
  .seg button:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .stepper{display:inline-flex;align-items:center;border:1px solid var(--line-strong);border-radius:999px;overflow:hidden;flex:none}
  .stepper button{all:unset;cursor:pointer;width:38px;height:36px;display:grid;place-items:center;color:var(--ink);font-size:20px;line-height:1}
  .stepper button:hover{background:rgba(216,178,94,.16)}
  .stepper button:focus-visible{outline:2px solid var(--gold);outline-offset:-2px}
  .stepper button:disabled{opacity:.3;cursor:default;background:none}
  .stepper b{min-width:28px;text-align:center;font-variant-numeric:tabular-nums;color:var(--foil);font-weight:600}
  .howto{display:grid;grid-template-columns:260px minmax(0,1fr);gap:clamp(18px,4vw,40px);align-items:center}
  @media (max-width:760px){.howto{grid-template-columns:1fr}}
  .howto .an{border-radius:14px}
  .howto .an svg{max-width:220px}
  ol.steps{margin:0;padding:0;list-style:none;counter-reset:s;display:grid;gap:12px;max-width:65ch}
  ol.steps li{counter-increment:s;display:grid;grid-template-columns:34px minmax(0,1fr);gap:12px;align-items:start;color:var(--ink-soft)}
  ol.steps li::before{content:counter(s);width:30px;height:30px;border-radius:50%;border:1px solid var(--line-strong);display:grid;place-items:center;font-family:var(--display);color:var(--foil);font-size:16px}
  ol.steps strong{color:var(--ink)}
  .cmp{display:grid;gap:12px;max-width:780px;margin-top:10px}
  .cmp .row{display:grid;grid-template-columns:minmax(0,210px) minmax(0,1fr) 70px;gap:14px;align-items:center;border-radius:10px;padding:4px 6px;margin:0 -6px}
  .cmp .row > span{font-size:15px;color:var(--ink-soft)}
  .cmp .bar{height:14px;border-radius:7px;background:rgba(236,229,207,.10);overflow:hidden}
  .cmp .bar i{display:block;height:100%;border-radius:7px;background:var(--sage);transition:width .45s ease}
  .cmp .row.top .bar i{background:var(--foil)}
  .cmp .row.top > span{color:var(--ink);font-weight:600}
  .cmp b{font-variant-numeric:tabular-nums;color:var(--ink);text-align:right;font-weight:600}
  .cmp .row.me{background:rgba(216,178,94,.12);outline:1px solid var(--line-strong)}
  .cmp .row .you{display:none;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--ground);background:var(--foil);font-weight:700;margin-left:10px;padding:2px 7px;border-radius:999px;vertical-align:2px}
  .cmp .row.me .you{display:inline}
  @media (max-width:560px){.cmp .row{grid-template-columns:minmax(0,1fr) 62px;gap:6px 10px}.cmp .row .bar{grid-column:1 / -1;grid-row:2}}
  .res{margin-top:16px;border-top:1px solid var(--line);padding-top:14px}
  .res .lab{font-family:var(--display);font-size:clamp(22px,3vw,26px);color:var(--foil);margin:0 0 6px}
  .res p{margin:0;color:var(--ink-soft)}
  .split{display:flex;justify-content:center;gap:18px;margin-top:10px;font-size:14px;color:var(--muted)}
  .split b{color:var(--ink);font-variant-numeric:tabular-nums}

  /* yere oturup kalkma puanlayıcı */
  .srt{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:clamp(20px,4vw,44px);align-items:start}
  @media (max-width:860px){.srt{grid-template-columns:1fr}}
  .srt-col h3{font-size:21px;margin:0 0 2px;display:flex;justify-content:space-between;align-items:baseline;gap:12px}
  .srt-col h3 output{font-family:var(--display);font-weight:400;color:var(--foil);font-size:26px;font-variant-numeric:tabular-nums}
  .srt-col + .srt-col{margin-top:20px;padding-top:18px;border-top:1px solid var(--line)}
  .sup{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:12px;align-items:center;padding:7px 0}
  .sup > span{font-size:15px;color:var(--ink-soft)}
  .srt-col .chk{margin-top:8px;font-size:15px}
  .srt-out{position:sticky;top:84px}
  .srt-ctl{margin-top:16px;align-items:center;justify-content:space-between}
  .srt-mini{display:none;margin:0;font-size:16px;color:var(--ink-soft)}
  .srt-mini b{font-family:var(--display);font-weight:400;font-size:26px;color:var(--foil);font-variant-numeric:tabular-nums}
  @media (max-width:860px){.srt-mini{display:block}}
  @media (max-width:860px){.srt-out{position:static}}
  .gauge .c small{display:block;font-size:13px;color:var(--muted);margin-top:4px}

  /* duvar oturuşu zamanlayıcı */
  .ws{display:grid;grid-template-columns:minmax(0,0.9fr) minmax(0,1.1fr);gap:clamp(18px,4vw,40px);align-items:center}
  @media (max-width:760px){.ws{grid-template-columns:1fr}}
  .ws-stage{border-radius:14px;overflow:hidden;background:var(--paper);display:grid;place-items:center;min-height:230px}
  .ws-stage .an svg{max-width:230px}
  @media (max-width:760px){.ws-stage .an svg{max-width:170px}}
  .ws-mid{display:flex;align-items:center;gap:20px;margin:6px 0 12px}
  .ws-ring{position:relative;width:132px;height:132px;flex:none}
  .ws-ring svg{width:132px;height:132px;transform:rotate(-90deg)}
  .ws-ring circle{fill:none;stroke-width:8}
  .ws-ring .bg{stroke:rgba(236,229,207,.12)}
  .ws-ring .fg{stroke:var(--foil);stroke-linecap:round;transition:stroke-dashoffset .12s linear}
  .ws-ring.rest .fg{stroke:var(--sage)}
  .ws-ring b{position:absolute;inset:0;display:grid;place-items:center;font-family:var(--display);font-weight:400;font-size:34px;color:var(--ink);font-variant-numeric:tabular-nums}
  .ws-info{flex:1;min-width:0}
  .ws-phase{font-family:var(--display);font-size:clamp(24px,3.2vw,30px);color:var(--ink);margin:0 0 4px;line-height:1.15}
  .ws-cue{margin:0;color:var(--ink-soft);font-size:15px}
  .ws-rpe{margin:8px 0 0;font-size:14px;color:var(--foil);font-weight:600;min-height:1.4em}
  .rounds{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:6px;margin:4px 0 14px}
  .rounds i{height:6px;border-radius:3px;background:rgba(236,229,207,.12)}
  .rounds i.done{background:var(--sage)}
  .rounds i.cur{background:var(--foil)}
  @media (max-width:420px){.ws-mid{gap:14px;align-items:flex-start}.ws-ring,.ws-ring svg{width:100px;height:100px}.ws-ring b{font-size:27px}}

  /* iç çekiş */
  .br{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(18px,4vw,44px);align-items:center}
  @media (max-width:760px){.br{grid-template-columns:1fr}}
  .br-stage{position:relative;width:min(290px,78vw);aspect-ratio:1;margin:0 auto}
  .br-stage svg.prog{position:absolute;inset:0;width:100%;height:100%;transform:rotate(-90deg)}
  .br-stage svg.prog circle{fill:none;stroke-width:4}
  .br-stage svg.prog .bg{stroke:rgba(236,229,207,.10)}
  .br-stage svg.prog .fg{stroke:var(--foil);stroke-linecap:round}
  .br-core{position:absolute;inset:12%;border-radius:50%;background:radial-gradient(circle at 38% 35%, rgba(236,229,207,.28), rgba(143,164,118,.55) 45%, rgba(143,164,118,.18) 75%);border:1px solid rgba(143,164,118,.6);transform:scale(.6);will-change:transform;box-shadow:0 0 60px rgba(143,164,118,.25)}
  .br-center{position:absolute;inset:0;display:grid;place-content:center;text-align:center;pointer-events:none}
  .br-center b{font-family:var(--display);font-weight:400;font-size:clamp(30px,5vw,40px);color:var(--ink);font-variant-numeric:tabular-nums;line-height:1}
  .br-center span{font-size:13px;color:var(--ink-soft);margin-top:6px}
  .br-cue{font-family:var(--display);font-size:clamp(24px,3.4vw,32px);color:var(--ink);margin:0 0 4px;min-height:1.3em;line-height:1.2}
  .br-sub{color:var(--ink-soft);margin:0 0 14px;min-height:1.5em}
  .rhythm{display:flex;gap:6px;margin:4px 0 16px;max-width:360px}
  .rhythm i{position:relative;height:10px;border-radius:5px;background:rgba(236,229,207,.12);overflow:hidden}
  .rhythm i::after{content:"";position:absolute;inset:0;background:var(--foil);transform-origin:left;transform:scaleX(var(--p,0))}
  .rhythm i.out::after{background:var(--sage)}
  .rhythm-lab{display:flex;gap:6px;max-width:360px;font-size:12px;color:var(--muted);margin-top:-10px;margin-bottom:14px}
  .rhythm-lab span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}

  /* doğa takvimi */
  .nt{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);gap:clamp(18px,4vw,40px);align-items:center}
  @media (max-width:860px){.nt{grid-template-columns:1fr}}
  .wk{display:grid;gap:6px}
  .dy{display:grid;grid-template-columns:96px minmax(0,1fr) 62px auto;gap:12px;align-items:center;padding:4px 0}
  .dy > span{font-size:15px;color:var(--ink-soft)}
  .dy .bar{height:10px;border-radius:5px;background:rgba(236,229,207,.10);overflow:hidden}
  .dy .bar i{display:block;height:100%;width:0;border-radius:5px;background:var(--sage);transition:width .3s ease}
  .dy .v{font-variant-numeric:tabular-nums;color:var(--ink);font-size:15px;text-align:right;white-space:nowrap}
  .dy .v output{font-weight:600}
  @media (max-width:480px){.dy{grid-template-columns:78px minmax(0,1fr) auto;gap:8px 10px}.dy .bar{grid-column:1 / -1;grid-row:2}.dy .v{text-align:left}}
  .places{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-top:8px}
  @media (max-width:700px){.places{grid-template-columns:1fr}}
  .place{border:1px solid var(--line);border-radius:12px;padding:16px;background:var(--ground-2)}
  .place h3{font-size:19px;margin:0 0 10px}
  .place ul{margin:0;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:8px}
  .place li{font-size:14px;color:var(--ink-soft);border:1px solid var(--line-strong);border-radius:999px;padding:6px 12px}

  /* bağ önerisi */
  .gv{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:clamp(18px,4vw,40px);align-items:center}
  @media (max-width:820px){.gv{grid-template-columns:1fr}}
  .task{border:1px solid var(--line-strong);border-radius:14px;padding:clamp(18px,3vw,26px);background:var(--ground);min-height:210px;display:grid;align-content:start;gap:10px}
  .task .k{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--foil);font-weight:700}
  .task p{font-family:var(--display);font-size:clamp(22px,3vw,27px);line-height:1.3;color:var(--ink);margin:0}
  .task small{font-size:14px;color:var(--ink-soft);line-height:1.5}
  .task small strong{color:var(--ink)}
  .task.pop{animation:pop .35s ease}
  @keyframes pop{from{opacity:.2;transform:translateY(6px)}to{opacity:1;transform:none}}
  .wkdots{display:flex;gap:8px;margin:10px 0 6px}
  .wkdots i{width:16px;height:16px;border-radius:50%;border:1px solid var(--line-strong)}
  .wkdots i.on{background:var(--sage);border-color:var(--sage)}
  .gv-count{font-family:var(--display);font-size:clamp(40px,6vw,54px);color:var(--ink);line-height:1;font-variant-numeric:tabular-nums}
  .def{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-top:8px}
  @media (max-width:700px){.def{grid-template-columns:1fr}}
  .def div{border:1px solid var(--line);border-radius:12px;padding:16px;background:var(--ground-2)}
  .def h3{font-size:19px;margin:0 0 6px}
  .def p{margin:0;color:var(--ink-soft);font-size:15px}
"""

def STEPPER(key, mx=2, label=""):
    return (f'<span class="stepper" data-k="{key}" data-max="{mx}" role="group" aria-label="{label}">'
            f'<button type="button" data-d="-1" aria-label="Azalt" disabled>−</button><b>0</b>'
            f'<button type="button" data-d="1" aria-label="Artır">+</button></span>')

WAKE_JS = """  function wake(on){
    try {
      if (on && navigator.wakeLock && !lock) navigator.wakeLock.request('screen').then(function(l){ lock = l; }).catch(function(){});
      if (!on && lock){ lock.release(); lock = null; }
    } catch (e) {}
  }
  function beep(f, d, v){
    if (!snd || !snd.checked) return;
    try {
      ctx = ctx || new (window.AudioContext || window.webkitAudioContext)();
      var o = ctx.createOscillator(), g = ctx.createGain(), n = ctx.currentTime;
      o.frequency.value = f; g.gain.setValueAtTime(0.0001, n);
      g.gain.exponentialRampToValueAtTime(v || 0.2, n + 0.03); g.gain.exponentialRampToValueAtTime(0.0001, n + d);
      o.connect(g); g.connect(ctx.destination); o.start(n); o.stop(n + d + 0.05);
    } catch (e) {}
  }
"""

# ------------------------------------------------------------------ çizimler
# Ayakta çapraz bacak -> yere bağdaş kurarak oturma -> kalkma (önden)
SRT_DUR, SRT_KT = "6s", "0;0.18;0.5;0.68;1"
def _srt(a, b):
    return f"{a};{a};{b};{b};{a}"
SV["srt"] = fig(GRD +
    f'<path class="fig" d="M60 28 L60 70">{anim_d(_srt("M60 28 L60 70", "M60 66 L60 106"), dur=SRT_DUR, kt=SRT_KT)}</path>'
    f'<path class="fig hl" d="M57 70 L60 91 L66 112">{anim_d(_srt("M57 70 L60 91 L66 112", "M57 106 L37 100 L64 110"), dur=SRT_DUR, kt=SRT_KT)}</path>'
    f'<path class="fig hl" d="M63 70 L60 91 L54 112">{anim_d(_srt("M63 70 L60 91 L54 112", "M63 106 L83 100 L56 110"), dur=SRT_DUR, kt=SRT_KT)}</path>'
    f'<path class="fig" d="M60 36 L46 48 L34 50">{anim_d(_srt("M60 36 L46 48 L34 50", "M60 74 L46 84 L34 84"), dur=SRT_DUR, kt=SRT_KT)}</path>'
    f'<path class="fig" d="M60 36 L74 48 L86 50">{anim_d(_srt("M60 36 L74 48 L86 50", "M60 74 L74 84 L86 84"), dur=SRT_DUR, kt=SRT_KT)}</path>'
    f'<g>{anim_t(_srt("0 0", "0 38"), dur=SRT_DUR, kt=SRT_KT)}<circle class="hd" cx="60" cy="19" r="7"/></g>',
    "Yere oturup kalkma testi")

# Tek dizden ayağa kalkma (yandan)
HK_DUR = "6s"
SV["hkneel"] = fig(GRD +
    f'<path class="fig" d="M54 78 L44 110 L26 110">{anim_d(_srt("M54 78 L44 110 L26 110", "M64 70 L60 91 L56 112"), dur=HK_DUR, kt=SRT_KT)}</path>'
    f'<path class="fig" d="M56 42 L54 78">{anim_d(_srt("M56 42 L54 78", "M65 32 L64 70"), dur=HK_DUR, kt=SRT_KT)}</path>'
    f'<path class="fig hl" d="M54 78 L78 78 L80 112">{anim_d(_srt("M54 78 L78 78 L80 112", "M64 70 L72 91 L80 112"), dur=HK_DUR, kt=SRT_KT)}</path>'
    f'<path class="fig" d="M56 48 L66 62 L76 68">{anim_d(_srt("M56 48 L66 62 L76 68", "M65 38 L70 54 L74 68"), dur=HK_DUR, kt=SRT_KT)}</path>'
    f'<g>{anim_t(_srt("0 0", "8 -10"), dur=HK_DUR, kt=SRT_KT)}<circle class="hd" cx="58" cy="32" r="7"/></g>',
    "Tek dizden ayağa kalkma")

# Duvar oturuşu: sabit tutuş + süre halkası
SV["wallsit"] = fig(GRD +
    '<path class="obj" d="M26 8 V112" stroke-width="5"/>'
    '<circle class="hd" cx="36" cy="28" r="7"/>'
    '<path class="fig" d="M34 38 L34 72 M34 46 L48 58 L58 60"/>'
    '<path class="fig hl" d="M34 72 L66 74 L67 110"/>'
    '<path class="fig" d="M67 110 L78 111"/>'
    '<circle cx="94" cy="30" r="13" fill="none" stroke="#B9CBC6" stroke-width="3"/>'
    '<circle cx="94" cy="30" r="13" fill="none" stroke="#C8963E" stroke-width="3.5" stroke-linecap="round" stroke-dasharray="81.7" stroke-dashoffset="81.7" transform="rotate(-90 94 30)">'
    '<animate attributeName="stroke-dashoffset" values="81.7;0" dur="4s" repeatCount="indefinite"/></circle>'
    '<path d="M94 30 V22 M90 13 H98" stroke="#2A6F6B" stroke-width="2.5" stroke-linecap="round"/>',
    "Duvar oturuşu")

EXT.update({
 "srt_practice": ("Testi alıştırma olarak yapın", "Yumuşak bir zeminde, yanınızda sağlam bir sandalye ya da duvar varken yavaşça yere oturun ve kalkın. Başta istediğiniz kadar destek alın; her hafta bir desteği azaltmayı hedefleyin.", "3–5 tekrar, haftada 3 gün"),
 "srt_kneel": ("Tek dizden ayağa kalkma", "Yanınızda sağlam bir sandalye varken tek dizinizin üzerine çökün, öndeki ayağınız yere tam bassın. Öndeki bacağınıza yüklenerek ayağa kalkın. Başta sandalyeden destek alın. Diz ağrınız varsa dizinizin altına yastık koyun.", "Her iki tarafa 5 tekrar"),
 "srt_sts": ("Kollar göğüste sandalyeden kalkma", "Kollarınızı göğsünüzde çaprazlayın. Ellerinizi kullanmadan sandalyeden kalkın, sonra kontrollü şekilde oturun. Kolaylaştıkça daha alçak bir oturak kullanın.", "10 tekrar, 2–3 set"),
 "srt_wall": ("Duvarda yarım çömelme", "Sırtınızı duvara dayayın, ayaklarınız duvardan bir adım önde olsun. Dizlerinizi rahat ettiğiniz kadar bükerek sırtınızı duvarda aşağı kaydırın, 2–3 saniye bekleyip doğrulun.", "10 tekrar, 2 set"),
 "srt_bridge": ("Köprü", "Sırtüstü yatın, dizleriniz bükülü, ayaklarınız yerde. Kalçanızı sıkarak yavaşça kaldırın, 3 saniye bekleyip indirin. Yerden kalkarken gereken kalça kuvvetini artırır.", "10–15 tekrar, 2 set"),
 "srt_sls": ("Tek ayak üzerinde denge", "Mutfak tezgâhına hafifçe tutunarak tek ayağınızın üzerinde durun. Kolaylaştıkça tutunmayı azaltın.", "30 saniye, her bacakta 3 kez"),
})
for _k, _b in (("srt_practice", "srt"), ("srt_kneel", "hkneel"), ("srt_sts", "sts"), ("srt_wall", "wall"), ("srt_bridge", "bridge"), ("srt_sls", "sls")):
    SV[_k] = SV[_b]

# ------------------------------------------------------------------ 1 · YERE OTURUP KALKMA TESTİ
SRT_SUPS = [("hand", "El"), ("forearm", "Ön kol"), ("knee", "Diz"), ("side", "Bacağın yan tarafı"), ("thigh", "Eli dize ya da uyluğa dayama")]
def _srt_col(p, title):
    rows = "\n".join(f'<div class="sup"><span>{t}</span>{STEPPER(p + "-" + k, 2, t)}</div>' for k, t in SRT_SUPS)
    return f'''<div class="srt-col">
            <h3>{title} <output id="{p}-v">5</output></h3>
            {rows}
            <label class="chk"><input type="checkbox" id="{p}-wob"> Sallandım ya da dengemi kısmen kaybettim (−0,5)</label>
          </div>'''

SRT_GROUPS = [("g10", "10", 3.7), ("g9", "8,5–9,5", 7.0), ("g8", "8", 11.1), ("g6", "4,5–7,5", 20.4), ("g4", "0–4", 42.1)]
SRT_ROWS = "\n".join(
    f'<div class="row{" top" if g == "g4" else ""}" data-g="{g}"><span>{lab} puan<span class="you">Siz</span></span><span class="bar"><i style="width:{v / 45 * 100:.1f}%"></i></span><b>%{str(v).replace(".", ",")}</b></div>'
    for g, lab, v in SRT_GROUPS)

SRT_FAQ = [
 ("Puanım düşük çıktı, endişelenmeli miyim?", "Düşük puan tek başına bir teşhis değildir; kas gücü, esneklik, denge ve vücut ağırlığı gibi pek çok özelliği birlikte yansıtır. Araştırmalardaki ilişki gözleme dayanır. Puanınızı, bu özellikler üzerinde çalışmak için bir başlangıç noktası olarak görün. Kalp-damar hastalığı için risk etkenleriniz varsa ya da yakın zamanda zorlanmaya başladıysanız hekiminizle de konuşun."),
 ("Puanımı yükseltebilir miyim?", "Evet. Bacak kuvveti, kalça esnekliği ve denge düzenli egzersizle her yaşta gelişir; aşağıdaki altı egzersiz iyi bir başlangıçtır. Puanı yükseltmenin ömrü uzatıp uzatmadığı ise henüz ayrıca araştırılmadı; ama yerden kalkabilmek günlük hayatta, özellikle düştükten sonra kalkarken çok değerlidir."),
 ("Kimler bu testi yapmamalı?", "Kalça ya da diz protezi ameliyatınız yeni olduysa, kalçada ya da dizde şiddetli ağrınız varsa, baş dönmesi ya da sık düşme öykünüz varsa testi tek başınıza yapmayın; önce fizyoterapistinize ya da hekiminize danışın. Kalça protezi olanlar cerrahları izin vermeden bacak çaprazlamamalıdır."),
 ("Test neden bu kadar çok şey anlatıyor?", "Yere desteksiz oturup kalkmak için vücut ağırlığınıza göre yeterli kas gücü, kalça ve dizlerde esneklik, iyi bir denge ve koordinasyon gerekir. Bunların hepsi yaşla birlikte azalabilir ve bağımsız yaşamla, düşme riskiyle yakından ilişkilidir."),
]

SRT_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Yere oturup kalkabiliyor musunuz?</h1>
    <p class="lede">Ellerinizi kullanmadan yere oturup yeniden kalkabilmek; kas gücü, esneklik, denge ve koordinasyonu tek bir harekette ölçer. 4.282 yetişkinin yaklaşık 12 yıl izlendiği bir araştırmada bu basit testin puanı, sonraki yıllardaki sağlık hakkında çarpıcı ipuçları verdi. Testi deneyin, puanınızı aşağıda hesaplayın.</p>
    <p class="meta">Son güncelleme: 30 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>10 puan</b><span>Testin en yüksek puanı: oturma için 5, kalkma için 5</span></div>
        <div class="stat"><b>4.282 kişi</b><span>46–75 yaş arası yetişkinlerin yaklaşık 12 yıl izlendiği 2026 tarihli araştırma</span></div>
        <div class="stat"><b>6 kat</b><span>0–4 puan alanlarda, tam puan alanlara göre daha yüksek kalp-damar kaynaklı ölüm riski</span></div>
        <div class="stat"><b>%21</b><span>İlk araştırmada (2.002 kişi) her 1 puanlık artışla ilişkili daha düşük ölüm riski</span></div>
      </div>
    </div>
  </section>

  <section id="nasil">
    <div class="wrap">
      <p class="eyebrow">Testi nasıl yaparsınız?</p>
      <h2>Hız değil, destek önemli</h2>
      <div class="howto">
        {SV["srt"]}
        <ol class="steps">
          <li><span><strong>Hazırlanın.</strong> Rahat kıyafetler giyin, ayakkabı ve çoraplarınızı çıkarın. Kaymayan, boş bir alanda durun; yanınızda sağlam bir sandalye ya da duvar olsun.</span></li>
          <li><span><strong>Oturun.</strong> Ellerinizi, kollarınızı ya da dizlerinizi yere koymadan yavaşça yere oturun. Bacaklarınızı çaprazlayabilir, istediğiniz oturuş şeklini seçebilirsiniz.</span></li>
          <li><span><strong>Kalkın.</strong> Yine mümkün olduğunca destek almadan ayağa kalkın. Hız önemli değil; gerekirse destek alın, puanlayıcıya işlersiniz.</span></li>
          <li><span><strong>Puanlayın.</strong> Oturma ve kalkma 5'er puanla başlar. Kullandığınız her destek (el, ön kol, diz, bacağın yan tarafı, eli dize ya da uyluğa dayama) için 1 puan, sallanma ya da kısmi denge kaybı için 0,5 puan düşülür.</span></li>
        </ol>
      </div>
      <div class="note warn" style="margin-top:22px"><strong>Güvenlik:</strong> Kalça ya da diz protezi ameliyatınız yeni olduysa, eklemlerinizde şiddetli ağrı, baş dönmesi ya da sık düşme öykünüz varsa testi tek başınıza yapmayın. Yaşlı bir yakınınız deneyecekse yanında durun. Kalça protezi olanlar cerrahları izin vermeden bacak çaprazlamamalıdır.</div>
    </div>
  </section>

  <section id="puan">
    <div class="wrap">
      <p class="eyebrow">Hemen hesaplayın</p>
      <h2>Puanlayıcı</h2>
      <p class="soft">Oturma ve kalkma sırasında kullandığınız destekleri işaretleyin. İki elinizi de yere koyduysanız “El” için 2 seçin.</p>
      <div class="tool">
        <div class="srt">
          <div>
            {_srt_col("sit", "Oturma")}
            {_srt_col("rise", "Kalkma")}
            <div class="controls srt-ctl"><button type="button" class="cta ghost" id="srt-reset">Sıfırla</button><p class="srt-mini">Toplam: <b id="srt-mini">10</b> / 10</p></div>
          </div>
          <div class="srt-out">
            <div class="gauge">
              <svg viewBox="0 0 240 240" aria-hidden="true"><circle class="bg" cx="120" cy="120" r="100"/><circle class="fg" id="srt-arc" cx="120" cy="120" r="100" stroke-dasharray="628.3" stroke-dashoffset="0"/></svg>
              <div class="c"><b id="srt-tot">10</b><span>/ 10 puan</span></div>
            </div>
            <div class="res" aria-live="polite">
              <p class="lab" id="srt-lab"></p>
              <p id="srt-msg"></p>
            </div>
          </div>
        </div>
        <div class="srt-strings" hidden>
          <span data-k="g10l">Tam puan</span>
          <span data-k="g10">Kas gücünüz, esnekliğiniz ve dengeniz bu hareketi desteksiz yapmaya yetiyor. Bu düzeyi korumak için düzenli hareket etmeye devam edin.</span>
          <span data-k="g9l">Çok iyi</span>
          <span data-k="g9">Küçük bir destek ya da sallanma puanınızı biraz düşürdü. Aşağıdaki egzersizlerle tam puanı hedefleyebilirsiniz.</span>
          <span data-k="g8l">İyi</span>
          <span data-k="g8">Araştırmada izlem süresindeki ölüm oranı 8 puan alanlarda %11,1, tam puan alanlarda %3,7'ydi. Kuvvet, esneklik ve denge egzersizleriyle puanınızı artırabilirsiniz.</span>
          <span data-k="g6l">Geliştirilebilir</span>
          <span data-k="g6">Bu aralıktaki puanlar, araştırmada belirgin şekilde daha yüksek riskle ilişkiliydi. Bacak kuvveti, kalça esnekliği ve denge üzerine çalışmak iyi bir başlangıç olur.</span>
          <span data-k="g4l">Güçlenmeye öncelik verin</span>
          <span data-k="g4">Yere inip kalkmak sizin için zor. Bu tek başına bir teşhis değil, ama kas gücü ve dengenin güçlendirilmesi gerektiğini gösterir. Güvenli bir başlangıç için fizyoterapistinizden destek alın; kalp-damar hastalığı için risk etkenleriniz varsa hekiminizle de konuşun.</span>
        </div>
      </div>
      <p class="count">Bu puanlayıcı bilgilendirme amaçlıdır; bir teşhis aracı değildir. Araştırmalarda test, deneyimli bir değerlendiricinin gözetiminde yapıldı.</p>
    </div>
  </section>

  <section id="oran">
    <div class="wrap">
      <p class="eyebrow">Araştırma ne buldu?</p>
      <h2>Puana göre 12 yıllık izlemdeki ölüm oranı</h2>
      <p class="soft">Brezilya'da 46–75 yaş arası 4.282 yetişkin test edildi ve yaklaşık 12 yıl izlendi. Puan düştükçe izlem süresindeki ölüm oranı belirgin şekilde arttı:</p>
      <div class="cmp">
{SRT_ROWS}
      </div>
      <p class="soft" style="margin-top:16px">Hiç kalkamayanlarda (kalkma puanı 0) ölüm oranı %49,5, kalkma puanı tam olanlarda %4,4'tü. 2012'de çevrim içi yayımlanan ilk araştırmada da 51–80 yaş arası 2.002 kişide her 1 puanlık artış, %21 daha düşük ölüm riskiyle ilişkiliydi.</p>
      <div class="callout"><p><strong>Önemli:</strong> Bunlar gözlem çalışmalarıdır. Düşük puan ölüme yol açmaz; sağlığı etkileyen pek çok özelliği bir arada yansıtır. Puanı yükseltmenin ömrü uzattığı henüz ayrıca test edilmedi. Ama kas gücü, esneklik ve denge; bağımsız yaşamak ve düşmeleri önlemek için her yaşta çalışmaya değer.</p></div>
    </div>
  </section>

  <section id="egzersizler">
    <div class="wrap">
      <p class="eyebrow">Puanınızı yükseltmek için</p>
      <h2>Altı egzersiz</h2>
      <p class="soft">Kuvvet, kalça esnekliği ve denge birlikte gelişince yere inip kalkmak da kolaylaşır. Bir hareket ağrınızı belirgin şekilde artırıyorsa onu atlayın.</p>
      {ex_grid(["srt_practice", "srt_kneel", "srt_sts", "srt_wall", "srt_bridge", "srt_sls"])}
      <p class="soft" style="margin-top:18px">Yaşlılarda denge ve düşmeleri önleme üzerine daha fazlası için <a href="dusme-onleme.html">düşmeleri önleme</a> rehberine, haftalık hareket hedefleriniz için <a href="hareket.html">Ne kadar hareket yeterli?</a> sayfasına bakabilirsiniz.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(SRT_FAQ)}
      {CTA_CARD("Yere inip kalkmak, kuvvet ve denge", "kuvvet ve denge çalışması")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Araújo CGS, et al. " + ext("https://academic.oup.com/eurjpc/article/33/12/2170/8163161", "Sitting–rising test scores predict natural and cardiovascular causes of deaths in middle-aged and older men and women") + ". Eur J Prev Cardiol. 2026;33(12):2170-2178.",
        "Brito LBB, Ricardo DR, Araújo DSMS, Ramos PS, Myers J, Araújo CGS. " + ext("https://academic.oup.com/eurjpc/article-abstract/21/7/892/5925784", "Ability to sit and rise from the floor as a predictor of all-cause mortality") + ". Eur J Prev Cardiol. 2014;21(7):892-898.",
      ])}
    </div>
  </section>
</main>'''

SRT_JS = '''<script>
(function(){
  var root = document.getElementById('puan'); if (!root) return;
  var S = {}; root.querySelectorAll('.srt-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var EN = document.documentElement.lang === 'en';
  function f(x){ var s = String(Math.round(x * 2) / 2); return EN ? s : s.replace('.', ','); }
  var $ = function(id){ return document.getElementById(id); };
  var arc = $('srt-arc'), C = 628.3, val = {}, steps = root.querySelectorAll('.stepper');
  function paint(st){
    var k = st.getAttribute('data-k'), mx = +st.getAttribute('data-max');
    st.querySelector('b').textContent = val[k];
    st.querySelector('[data-d="-1"]').disabled = val[k] <= 0;
    st.querySelector('[data-d="1"]').disabled = val[k] >= mx;
  }
  steps.forEach(function(st){
    var k = st.getAttribute('data-k'), mx = +st.getAttribute('data-max'); val[k] = 0;
    st.addEventListener('click', function(e){
      var b = e.target.closest('button'); if (!b || b.disabled) return;
      val[k] = Math.max(0, Math.min(mx, val[k] + (+b.getAttribute('data-d')))); paint(st); upd();
    });
  });
  function half(p){
    var d = 0; for (var k in val) if (k.indexOf(p + '-') === 0) d += val[k];
    if ($(p + '-wob').checked) d += 0.5;
    return Math.max(0, 5 - d);
  }
  function upd(){
    var a = half('sit'), b = half('rise'), t = a + b;
    $('sit-v').textContent = f(a); $('rise-v').textContent = f(b); $('srt-tot').textContent = f(t); $('srt-mini').textContent = f(t);
    arc.style.strokeDashoffset = (C * (1 - t / 10)).toFixed(1);
    var g = t >= 10 ? 'g10' : t >= 8.5 ? 'g9' : t >= 8 ? 'g8' : t >= 4.5 ? 'g6' : 'g4';
    $('srt-lab').textContent = S[g + 'l']; $('srt-msg').textContent = S[g];
    document.querySelectorAll('#oran [data-g]').forEach(function(r){ r.classList.toggle('me', r.getAttribute('data-g') === g); });
  }
  $('sit-wob').addEventListener('change', upd); $('rise-wob').addEventListener('change', upd);
  $('srt-reset').addEventListener('click', function(){
    for (var k in val) val[k] = 0; steps.forEach(paint);
    $('sit-wob').checked = false; $('rise-wob').checked = false; upd();
  });
  upd();
})();
</script>
'''

page("otur-kalk-testi.html", "Yere Oturup Kalkma Testi",
     "Ellerinizi kullanmadan yere oturup kalkabiliyor musunuz? 12 yıllık araştırmada sağlığın güçlü göstergesi çıkan testi deneyin, puanınızı hesaplayın, geliştirin.",
     "otur-kalk-testi.html", SELF2_CSS, SRT_BODY, SRT_JS,
     seo_title="Yere Oturup Kalkma Testi: Puanınızı Hesaplayın | İhsan Eren",
     about={"@type": "MedicalTest", "name": "Yere oturup kalkma testi"},
     faq_items=pick(SRT_FAQ, 0, 1, 2, 3))

# ------------------------------------------------------------------ 2 · DUVAR OTURUŞU (TANSİYON)
BP_TYPES = [("Aerobik (yürüyüş, koşu, bisiklet)", 4.49, 2.53), ("Direnç (ağırlık, lastik bant)", 4.55, 3.04),
            ("Aerobik ve direnç birlikte", 6.04, 2.54), ("Yüksek yoğunluklu aralıklı (HIIT)", 4.08, 2.50),
            ("İzometrik (duvar oturuşu gibi)", 8.24, 4.00)]
def _n(x):
    return f"{x:.2f}".replace(".", ",")
BP_ROWS = "\n".join(
    f'<div class="row{" top" if i == 4 else ""}" data-s="{s}" data-d="{d}"><span>{t}</span><span class="bar"><i style="width:{s / 9 * 100:.1f}%"></i></span><b>{_n(s)}</b></div>'
    for i, (t, s, d) in enumerate(BP_TYPES))

WS_FAQ = [
 ("Hareketsiz bir egzersiz tansiyonu nasıl düşürüyor?", "Mekanizma tam olarak bilinmiyor. Evde yapılan bir çalışmada tansiyondaki düşüş, çoğunlukla dinlenme nabzındaki ve kalbin dakikada pompaladığı kan miktarındaki azalmayla ilişkiliydi. Kasılma sırasında sıkışan damarların bırakınca genişlemesinin damar sağlığına etkisi de araştırılıyor."),
 ("Tansiyon ilacı kullanıyorum, yapabilir miyim?", "Çoğu kişi yapabilir, ama önce hekiminize danışın ve ilacınızı kendi başınıza bırakmayın ya da azaltmayın. Egzersiz tedavinin yerine değil, yanına eklenir. Evde tansiyonunuzu düzenli ölçüp sonuçları hekiminizle paylaşın."),
 ("Yürüyüşü bırakıp sadece duvar oturuşu mu yapmalıyım?", "Hayır. Analizde tüm egzersiz türleri tansiyonu düşürdü. Yürüyüş gibi aerobik egzersiz kalp, kilo, kan şekeri ve ruh sağlığı için de önemlidir. Duvar oturuşu, haftalık hareketinize eklenebilecek kısa ve etkili bir parçadır."),
 ("Ne kadar sürede etkisini görürüm?", "Evde yapılan küçük çalışmalarda 4 haftalık programın sonunda büyük tansiyonda ortalama 4 ile 9 mmHg arasında düşüşler ölçüldü. Etkinin sürmesi için egzersize devam etmek gerekir."),
]

WS_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Tansiyon için duvar oturuşu</h1>
    <p class="lede">270 çalışmayı bir araya getiren büyük bir analizde, tansiyonu en çok düşüren egzersiz türü koşu ya da bisiklet değil, duvara yaslanıp hareketsiz beklemek gibi “izometrik” egzersizler çıktı. Haftada 3 gün, seans başına yaklaşık 14 dakika. Aşağıdaki zamanlayıcıyla birlikte yapabilirsiniz.</p>
    <p class="meta">Son güncelleme: 30 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>8,2 / 4,0</b><span>İzometrik egzersizle büyük ve küçük tansiyonda ortalama düşüş (mmHg)</span></div>
        <div class="stat"><b>4 × 2 dk</b><span>Bir seans: 2 dakika duvar oturuşu, 2 dakika dinlenme, 4 tur</span></div>
        <div class="stat"><b>Haftada 3</b><span>Araştırmalarda kullanılan seans sayısı; aralarda birer gün dinlenme</span></div>
        <div class="stat"><b>%10</b><span>İlaç çalışmalarında büyük tansiyondaki her 5 mmHg düşüşle azalan ciddi kalp-damar olayı riski</span></div>
      </div>
    </div>
  </section>

  <section id="karsilastirma">
    <div class="wrap">
      <p class="eyebrow">Araştırma ne buldu?</p>
      <h2>Egzersiz türüne göre tansiyondaki ortalama düşüş</h2>
      <p class="soft">1990–2023 arasında yayımlanan 270 randomize çalışma ve 15.827 katılımcı. Egzersiz yapmayanlarla karşılaştırıldığında dinlenme tansiyonundaki ortalama düşüş (mmHg):</p>
      <div class="seg" role="group" aria-label="Tansiyon türü">
        <button type="button" data-v="s" aria-pressed="true">Büyük tansiyon</button>
        <button type="button" data-v="d" aria-pressed="false">Küçük tansiyon</button>
      </div>
      <div class="cmp" id="bp-cmp">
{BP_ROWS}
      </div>
      <p class="soft" style="margin-top:16px">Tek tek egzersizler arasında büyük tansiyon için en etkili bulunan duvar oturuşu, küçük tansiyon için ise koşu oldu. Tüm egzersiz türleri tansiyonu anlamlı şekilde düşürdü; yani en iyi egzersiz, düzenli yapabildiğinizdir.</p>
    </div>
  </section>

  <section id="zamanlayici">
    <div class="wrap">
      <p class="eyebrow">Birlikte yapalım</p>
      <h2>Duvar oturuşu zamanlayıcısı</h2>
      <p class="soft">Araştırmalardaki program: 2 dakika duvar oturuşu, 2 dakika dinlenme, 4 tur; haftada 3 gün. İlk günlerde alışmak için 1 dakikalık turlarla başlayabilirsiniz.</p>
      <div class="tool">
        <div class="ws">
          <div class="ws-stage" aria-hidden="true">{SV["wallsit"]}</div>
          <div>
            <div class="seg" role="group" aria-label="Tur süresi" id="ws-mode">
              <button type="button" data-v="120" aria-pressed="true">2 dakika</button>
              <button type="button" data-v="60" aria-pressed="false">1 dakika (başlangıç)</button>
            </div>
            <div class="ws-mid">
              <div class="ws-ring" id="ws-ring"><svg viewBox="0 0 132 132" aria-hidden="true"><circle class="bg" cx="66" cy="66" r="58"/><circle class="fg" id="ws-arc" cx="66" cy="66" r="58" stroke-dasharray="364.4" stroke-dashoffset="0"/></svg><b id="ws-sec">2:00</b></div>
              <div class="ws-info">
                <p class="eyebrow" id="ws-step">Tur 1 / 4</p>
                <p class="ws-phase" id="ws-phase" aria-live="polite">Hazır</p>
                <p class="ws-cue" id="ws-cue">Başlat'a basınca 10 saniyelik hazırlanma süresi başlar.</p>
              </div>
            </div>
            <div class="rounds" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
            <p class="ws-rpe" id="ws-rpe"></p>
            <div class="controls">
              <button type="button" class="cta" id="ws-go">Başlat</button>
              <button type="button" class="cta ghost" id="ws-reset">Sıfırla</button>
            </div>
            <label class="snd"><input type="checkbox" id="ws-sound" checked> Sesli uyarı</label>
          </div>
        </div>
        <div class="ws-strings" hidden>
          <span data-k="round">Tur {{i}} / 4</span>
          <span data-k="prep">Hazırlanın</span>
          <span data-k="prepc">Sırtınızı duvara yaslayın, ayaklarınızı duvardan öne alın ve pozisyonunuzu seçin.</span>
          <span data-k="hold">Duvar oturuşu</span>
          <span data-k="holdc">Sırtınız duvarda, dizleriniz ayak bileklerinizin üzerinde. Nefesinizi tutmayın; normal nefes alıp verin.</span>
          <span data-k="half">Yarısı bitti. Nefesinizi tutmayın.</span>
          <span data-k="rest">Dinlenin</span>
          <span data-k="restc">Ayağa kalkın, bacaklarınızı hafifçe sallayın ve rahat nefes alın.</span>
          <span data-k="rpe">Bu turun sonunda hedef zorlanma: 10 üzerinden yaklaşık {{r}}</span>
          <span data-k="paused">Duraklatıldı</span>
          <span data-k="done">Tamamlandı</span>
          <span data-k="donec">Harika, bugünkü seansınızı tamamladınız. Bir sonraki seans için bir gün ara verin.</span>
          <span data-k="ready">Hazır</span>
          <span data-k="readyc">Başlat'a basınca 10 saniyelik hazırlanma süresi başlar.</span>
          <span data-k="start">Başlat</span>
          <span data-k="pause">Duraklat</span>
          <span data-k="resume">Devam et</span>
          <span data-k="again">Baştan başla</span>
        </div>
      </div>
      <p class="count">Ekran, seans sürerken kapanmayacak şekilde ayarlanır (tarayıcınız destekliyorsa).</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Doğru derinlik nasıl seçilir?</h2>
        <p class="soft">Evde yapılan bir çalışmada katılımcılar derinliği zorlanma hissine göre seçti ve 4 hafta sonunda büyük tansiyonda ortalama 9 mmHg düşüş ölçüldü. Hedef: 4 turun sonunda zorlanma, 10 üzerinden sırasıyla yaklaşık 4, 5,5, 7 ve 8,5 olsun. Yani ilk tur rahat, son tur zor ama tamamlanabilir.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Sırtınızı duvara yaslayın, ayaklarınız kalça genişliğinde açık ve duvardan yaklaşık iki ayak boyu önde olsun.</li>
        <li>Sırtınız duvarda kayarak inin. Dizleriniz ayak bileklerinizin üzerinde kalsın, ayak parmaklarınızı geçmesin.</li>
        <li>Uyluklarınız yere paralelden aşağı inmesin; daha yüksekte kalmak da işe yarar.</li>
        <li>Tur çok kolay geliyorsa biraz daha aşağı, bitiremiyorsanız biraz daha yukarı konum seçin.</li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Güvenle yapmak için</h2>
      <ul class="dots">
        <li><strong>Nefesinizi tutmayın.</strong> Ikınmak tansiyonu geçici olarak yükseltir. Tur boyunca normal nefes alıp verin, isterseniz sesli sayın.</li>
        <li>Tansiyonunuz kontrol altında değilse (örneğin 180/110 mmHg ve üzeri) önce hekiminize danışın.</li>
        <li>Kalp hastalığı, ritim bozukluğu, anevrizma, yakın zamanda geçirilmiş kalp krizi ya da inme, göz dibi hastalığı varsa ya da gebeyseniz önce hekiminize danışın.</li>
        <li>Diz ağrınız varsa daha yüksek bir konumda kalın; ağrı artıyorsa durun.</li>
        <li>Tansiyon ilacınızı kendi başınıza bırakmayın ya da azaltmayın; egzersiz tedavinin yanına eklenir.</li>
      </ul>
      <div class="note warn" style="margin-top:18px"><strong>Hemen durun:</strong> Göğüs ağrısı, baş dönmesi, çarpıntı ya da alışılmadık nefes darlığı olursa egzersizi bırakın; geçmiyorsa 112'yi arayın.</div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(WS_FAQ)}
      {CTA_CARD("Tansiyonunuza ve eklemlerinize uygun bir egzersiz programı", "tansiyona uygun egzersiz programı")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Edwards JJ, Deenmamode AHP, Griffiths M, et al. " + ext("https://bjsm.bmj.com/content/57/20/1317", "Exercise training and resting blood pressure: a large-scale pairwise and network meta-analysis of randomised controlled trials") + ". Br J Sports Med. 2023;57(20):1317-1326.",
        "Wiles JD, et al. " + ext("https://link.springer.com/article/10.1007/s00421-016-3501-0", "Home-based isometric exercise training induced reductions resting blood pressure") + ". Eur J Appl Physiol. 2017;117(1):83-93.",
        "Lea JWD, O'Driscoll JM, Wiles JD. " + ext("https://link.springer.com/article/10.1007/s00421-023-05269-2", "The implementation of a home-based isometric wall squat intervention using ratings of perceived exertion to select and control exercise intensity: a pilot study in normotensive and pre-hypertensive adults") + ". Eur J Appl Physiol. 2024;124(1):281-293.",
        "Blood Pressure Lowering Treatment Trialists' Collaboration. " + ext("https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(21)00590-0/fulltext", "Pharmacological blood pressure lowering for primary and secondary prevention of cardiovascular disease across different levels of blood pressure: an individual participant-level data meta-analysis") + ". Lancet. 2021;397(10285):1625-1636.",
      ])}
    </div>
  </section>
</main>'''

WS_JS = '''<script>
(function(){
  var sec = document.getElementById('bp-cmp');
  if (sec){
    var EN0 = document.documentElement.lang === 'en';
    var seg = sec.previousElementSibling;
    seg.addEventListener('click', function(e){
      var b = e.target.closest('button'); if (!b) return;
      var v = b.getAttribute('data-v');
      seg.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      var rows = sec.querySelectorAll('.row'), mx = v === 's' ? 9 : 4.5;
      rows.forEach(function(r){
        var n = +r.getAttribute(v === 's' ? 'data-s' : 'data-d');
        r.querySelector('i').style.width = (n / mx * 100).toFixed(1) + '%';
        var t = n.toFixed(2); r.querySelector('b').textContent = EN0 ? t : t.replace('.', ',');
      });
    });
  }
  var root = document.getElementById('zamanlayici'); if (!root) return;
  var S = {}; root.querySelectorAll('.ws-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var EN = document.documentElement.lang === 'en';
  var $ = function(id){ return document.getElementById(id); };
  var go = $('ws-go'), secEl = $('ws-sec'), arc = $('ws-arc'), ring = $('ws-ring'), phaseEl = $('ws-phase'), cue = $('ws-cue'),
      stepEl = $('ws-step'), rpeEl = $('ws-rpe'), snd = $('ws-sound'), bars = root.querySelectorAll('.rounds i');
  var C = 364.4, PREP = 10, N = 4, RPE = [4, 5.5, 7, 8.5], HOLD = 120;
  var phase = 'idle', i = 0, left = 0, tot = 1, running = false, t = null, last = 0, halfDone = false, ctx = null, lock = null;
''' + WAKE_JS + '''
  function mmss(s){ s = Math.max(0, Math.ceil(s)); var m = Math.floor(s / 60), r = s % 60; return m + ':' + (r < 10 ? '0' : '') + r; }
  function fr(x){ var s = String(x); return EN ? s : s.replace('.', ','); }
  function paint(){
    secEl.textContent = phase === 'done' ? '✓' : mmss(phase === 'idle' ? HOLD : left);
    arc.style.strokeDashoffset = (phase === 'idle' || phase === 'done') ? 0 : (C * (1 - left / tot)).toFixed(1);
    ring.classList.toggle('rest', phase === 'rest' || phase === 'prep');
    stepEl.textContent = S.round.replace('{i}', Math.min(i + 1, N));
    for (var j = 0; j < N; j++) bars[j].className = (phase === 'done' || j < i || (j === i && phase === 'rest')) ? 'done' : (j === i && phase !== 'idle' ? 'cur' : '');
  }
  function enter(p){
    phase = p; halfDone = false;
    if (p === 'prep'){ left = tot = PREP; phaseEl.textContent = S.prep; cue.textContent = S.prepc; rpeEl.textContent = S.rpe.replace('{r}', fr(RPE[i])); }
    else if (p === 'hold'){ left = tot = HOLD; phaseEl.textContent = S.hold; cue.textContent = S.holdc; rpeEl.textContent = S.rpe.replace('{r}', fr(RPE[i])); beep(880, 0.3); }
    else if (p === 'rest'){ left = tot = HOLD; phaseEl.textContent = S.rest; cue.textContent = S.restc; rpeEl.textContent = ''; beep(660, 0.15); setTimeout(function(){ beep(660, 0.15); }, 220); }
    paint();
  }
  function finish(){
    running = false; clearInterval(t); phase = 'done'; i = N - 1;
    phaseEl.textContent = S.done; cue.textContent = S.donec; rpeEl.textContent = ''; go.textContent = S.again; paint(); wake(false);
    beep(660, 0.15); setTimeout(function(){ beep(880, 0.35); }, 200);
  }
  function tick(){
    var now = performance.now(), dt = (now - last) / 1000; last = now;
    var before = Math.ceil(left); left -= dt;
    if (phase === 'hold' && !halfDone && left <= HOLD / 2){ halfDone = true; cue.textContent = S.half; beep(520, 0.12, 0.12); }
    if (left <= 0){
      if (phase === 'prep') enter('hold');
      else if (phase === 'hold'){ if (i < N - 1) enter('rest'); else finish(); }
      else if (phase === 'rest'){ i++; enter('hold'); }
      return;
    }
    if ((phase === 'prep' || phase === 'rest') && left <= 3 && Math.ceil(left) !== before) beep(520, 0.08);
    paint();
  }
  function run(){ running = true; last = performance.now(); clearInterval(t); t = setInterval(tick, 100); go.textContent = S.pause; wake(true); }
  function pause(){ running = false; clearInterval(t); go.textContent = S.resume; phaseEl.textContent = S.paused; wake(false); }
  function reset(){
    running = false; clearInterval(t); phase = 'idle'; i = 0; wake(false);
    go.textContent = S.start; phaseEl.textContent = S.ready; cue.textContent = S.readyc; rpeEl.textContent = ''; paint();
  }
  go.addEventListener('click', function(){
    if (phase === 'idle' || phase === 'done'){ i = 0; enter('prep'); run(); }
    else if (running) pause();
    else { phaseEl.textContent = phase === 'prep' ? S.prep : (phase === 'hold' ? S.hold : S.rest); run(); }
  });
  $('ws-reset').addEventListener('click', reset);
  $('ws-mode').addEventListener('click', function(e){
    var b = e.target.closest('button'); if (!b) return;
    this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
    HOLD = +b.getAttribute('data-v'); reset();
  });
  document.addEventListener('visibilitychange', function(){ if (!document.hidden && running) wake(true); });
  reset();
})();
</script>
'''

page("duvar-oturusu.html", "Tansiyon İçin Duvar Oturuşu",
     "270 çalışmalık analizde tansiyonu en çok düşüren egzersiz türü izometrik egzersizler çıktı. Duvar oturuşu nasıl yapılır, kimler dikkat etmeli? Zamanlayıcıyla birlikte yapın.",
     "duvar-oturusu.html", SELF2_CSS, WS_BODY, WS_JS,
     seo_title="Tansiyon İçin Duvar Oturuşu: İzometrik Egzersiz Zamanlayıcı | İhsan Eren",
     about=[{"@type": "Thing", "name": "İzometrik egzersiz"}, cond("Yüksek tansiyon (hipertansiyon)")],
     faq_items=pick(WS_FAQ, 0, 1, 2, 3))

# ------------------------------------------------------------------ 3 · DÖNGÜSEL İÇ ÇEKİŞ
SIGH_FAQ = [
 ("Günün hangi saatinde yapmalıyım?", "Çalışmada katılımcılar günün istedikleri bir saatinde yaptı. Kendinize bir alışkanlık zamanı seçin: sabah kahvesinden önce, öğle arasında ya da yatmadan önce. Gergin bir anda birkaç tur da yapabilirsiniz."),
 ("Meditasyondan daha mı iyi?", "Bu çalışmada olumlu duygulardaki artış ve solunum hızındaki düşüş döngüsel iç çekişte daha belirgindi; kaygı ise tüm gruplarda benzer şekilde azaldı. Bu tek bir çalışmadır ve meditasyon da yararlı bir yöntem olmayı sürdürüyor. Size iyi geleni seçin."),
 ("Başım dönerse ne yapmalıyım?", "Hemen normal nefesinize dönün. Nefesi zorlamayın; ikinci nefes kısa ve hafif olabilir. Astım ya da KOAH gibi bir akciğer hastalığınız varsa rahat olduğunuz bir tempoda yapın."),
 ("Stres sayfasındaki nefes egzersizlerinden farkı ne?", "Stresli anlarda sayfasında 4-6, kutu ve 4-7-8 nefesleri var. Döngüsel iç çekişte fark, üst üste iki kez nefes alıp uzun bir nefes vermektir. Hepsi nefes verişi uzatmaya dayanır; hangisini daha rahat yapıyorsanız onu seçin."),
]

SIGH_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>5 dakikalık iç çekiş nefesi</h1>
    <p class="lede">Stanford Üniversitesi'nde yapılan bir çalışmada, bir ay boyunca her gün 5 dakika “döngüsel iç çekiş” yapanların ruh hâli, aynı sürede farkındalık meditasyonu yapanlardan daha fazla iyileşti. Yöntem çok basit: burundan iki kez nefes alın, ağızdan uzun uzun verin. Aşağıdaki rehberle birlikte yapın.</p>
    <p class="meta">Son güncelleme: 30 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>5 dk</b><span>Günlük uygulama süresi; çalışma 28 gün sürdü</span></div>
        <div class="stat"><b>108 kişi</b><span>Dört yöntemden birine rastgele ayrılan katılımcı: üç nefes tekniği ve meditasyon</span></div>
        <div class="stat"><b>1,91 / 1,22</b><span>Olumlu duygulardaki ortalama günlük artış (puan): nefes egzersizleri ile meditasyon</span></div>
        <div class="stat"><b>Birkaç dakikada bir</b><span>Farkında olmadan kendiliğinden iç çekme sıklığımız</span></div>
      </div>
    </div>
  </section>

  <section id="nefes">
    <div class="wrap">
      <p class="eyebrow">Birlikte yapalım</p>
      <h2>Nefes rehberi</h2>
      <p class="soft">Rahat bir yerde oturun ya da uzanın. Daire büyürken burundan nefes alın, iyice dolunca bir kez daha kısa bir nefes ekleyin; daire küçülürken ağızdan yavaşça verin.</p>
      <div class="tool">
        <div class="br">
          <div class="br-stage">
            <svg class="prog" viewBox="0 0 200 200" aria-hidden="true"><circle class="bg" cx="100" cy="100" r="96"/><circle class="fg" id="br-arc" cx="100" cy="100" r="96" stroke-dasharray="603.2" stroke-dashoffset="603.2"/></svg>
            <div class="br-core" id="br-core"></div>
            <div class="br-center"><b id="br-time">5:00</b><span id="br-count">&nbsp;</span></div>
          </div>
          <div>
            <p class="br-cue" id="br-cue" aria-live="polite">Hazır olduğunuzda başlayın</p>
            <p class="br-sub" id="br-sub">Burundan iki kez alın, ağızdan uzun verin.</p>
            <div class="rhythm" aria-hidden="true"><i id="rh-a"></i><i id="rh-b"></i><i class="out" id="rh-c"></i></div>
            <div class="rhythm-lab" aria-hidden="true"><span id="rl-a">1. nefes</span><span id="rl-b">2.</span><span id="rl-c">Uzun nefes verme</span></div>
            <p class="q">Süre</p>
            <div class="seg" role="group" aria-label="Süre" id="br-dur">
              <button type="button" data-v="60" aria-pressed="false">1 dk</button>
              <button type="button" data-v="180" aria-pressed="false">3 dk</button>
              <button type="button" data-v="300" aria-pressed="true">5 dk</button>
            </div>
            <p class="q">Tempo</p>
            <div class="seg" role="group" aria-label="Tempo" id="br-pace">
              <button type="button" data-v="n" aria-pressed="true">Rahat (yaklaşık 10 sn)</button>
              <button type="button" data-v="s" aria-pressed="false">Yavaş (yaklaşık 14 sn)</button>
            </div>
            <div class="controls" style="margin-top:14px">
              <button type="button" class="cta" id="br-go">Başlat</button>
              <button type="button" class="cta ghost" id="br-reset">Sıfırla</button>
            </div>
            <label class="snd"><input type="checkbox" id="br-sound"> Yumuşak sesli yönlendirme</label>
          </div>
        </div>
        <div class="br-strings" hidden>
          <span data-k="in1">Burundan nefes alın</span>
          <span data-k="in1s">Göğsünüz ve karnınız yavaşça dolsun.</span>
          <span data-k="in2">Bir kez daha</span>
          <span data-k="in2s">Kısa bir nefes daha ekleyin.</span>
          <span data-k="out">Ağızdan yavaşça verin</span>
          <span data-k="outs">Havanın tamamı çıkana kadar, acele etmeden.</span>
          <span data-k="ready">Hazır olduğunuzda başlayın</span>
          <span data-k="readys">Burundan iki kez alın, ağızdan uzun verin.</span>
          <span data-k="paused">Duraklatıldı</span>
          <span data-k="done">Tamamlandı</span>
          <span data-k="dones">Nasıl hissediyorsunuz? Yarın aynı saatte tekrar etmeye ne dersiniz?</span>
          <span data-k="count">{{n}} nefes</span>
          <span data-k="count1">1 nefes</span>
          <span data-k="start">Başlat</span>
          <span data-k="pause">Duraklat</span>
          <span data-k="resume">Devam et</span>
          <span data-k="again">Baştan başla</span>
        </div>
      </div>
      <p class="count">Baş dönmesi olursa normal nefesinize dönün. Tempo size uymuyorsa değiştirin; önemli olan nefes verişin nefes alıştan uzun olması.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Araştırma ne buldu?</h2>
        <p class="soft">Stanford'daki çalışmada 108 kişi, bir ay boyunca her gün 5 dakika dört yöntemden birini uyguladı: döngüsel iç çekiş, kutu nefesi, hızlı nefes alıp tutma ya da farkındalık meditasyonu. Katılımcılar her uygulamadan önce ve sonra duygularını puanladı, bileklerindeki cihaz da solunum ve kalp hızını ölçtü.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Olumlu duygulardaki günlük artış, nefes gruplarında meditasyona göre daha fazlaydı; en belirgin etki döngüsel iç çekişteydi.</li>
        <li>Düzenli uygulayanlarda fayda zamanla büyüdü.</li>
        <li>Dinlenme hâlindeki solunum hızı nefes gruplarında, özellikle döngüsel iç çekişte düştü; meditasyonda benzer bir değişiklik görülmedi.</li>
        <li>Kaygı tüm gruplarda azaldı; gruplar arasında fark yoktu.</li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Neden iki kez nefes almak?</h2>
      <p class="soft">İç çekmek, bedenimizin kendi yöntemidir: farkında olmadan birkaç dakikada bir kendiliğinden iç çekeriz. Bu derin nefesler, akciğerlerdeki küçük hava keseciklerinden sönmüş olanları yeniden açar. Döngüsel iç çekişte bu doğal refleksi bilinçli olarak tekrarlarsınız.</p>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Burundan alın</h3><p>Akciğerleriniz rahatça dolana kadar yavaşça nefes alın.</p></div>
        <div class="kind"><span class="n">2</span><h3>Bir kez daha</h3><p>Dolduğunu hissettiğiniz noktada kısa, ikinci bir nefes ekleyin; küçük olabilir.</p></div>
        <div class="kind"><span class="n">3</span><h3>Uzun verin</h3><p>Ağzınızdan, havanın tamamı çıkana kadar yavaşça verin. Nefes veriş, alıştan uzun sürsün.</p></div>
        <div class="kind"><span class="n">4</span><h3>5 dakika</h3><p>Her gün 5 dakika tekrarlayın. Gergin bir anda birkaç tur da işe yarayabilir.</p></div>
      </div>
      <p class="soft" style="margin-top:18px">Başka nefes egzersizleri ve stresle baş etme becerileri için <a href="stres.html">Stresli anlarda ne yapabilirsiniz?</a> sayfasına, uykuya dalmakta zorlanıyorsanız <a href="uyku.html">İyi uyku için</a> sayfasına bakabilirsiniz.</p>
    </div>
  </section>

  <section id="video">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>Fizyolojik iç çekiş</h2>
      <p class="soft">Çalışmanın yazarlarından Stanford'lu nörobilimci Andrew Huberman'ın, iç çekişin nasıl yapıldığını ve neden işe yaradığını anlattığı kısa ve çok izlenen videosu. Video İngilizcedir; oynatıcıda Ayarlar → Altyazılar → Otomatik çevir → Türkçe seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("rBdhqBGqiMc", "Fizyolojik iç çekiş videosunu oynat", "Reduce Anxiety &amp; Stress with the Physiological Sigh | Huberman Lab Quantal Clip")}
          <h3>Kaygı ve stresi fizyolojik iç çekişle azaltın</h3>
          <p>İki kez nefes alıp uzun vermenin bedendeki etkisini anlatıyor.</p>
        </div>
      </div>
      <p class="meta">Video Huberman Lab kanalına aittir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(SIGH_FAQ)}
      <div class="note" style="margin-top:22px"><strong>Destek almak önemlidir:</strong> Haftalardır süren kaygı, çökkünlük ya da uyku sorunları nefes egzersizleriyle geçmiyorsa bir hekime ya da ruh sağlığı uzmanına başvurun. Kendinize zarar verme düşünceleriniz varsa 112'yi arayın.</div>
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "Balban MY, Neri E, Kogon MM, et al. " + ext("https://www.cell.com/cell-reports-medicine/fulltext/S2666-3791(22)00474-8", "Brief structured respiration practices enhance mood and reduce physiological arousal") + ". Cell Rep Med. 2023;4(1):100895.",
        "Li P, Janczewski WA, Yackle K, et al. " + ext("https://www.nature.com/articles/nature16964", "The peptidergic control circuit for sighing") + ". Nature. 2016;530(7590):293-297.",
      ])}
    </div>
  </section>
</main>'''

SIGH_JS = '''<script>
(function(){
  var root = document.getElementById('nefes'); if (!root) return;
  var S = {}; root.querySelectorAll('.br-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var $ = function(id){ return document.getElementById(id); };
  var core = $('br-core'), arc = $('br-arc'), timeEl = $('br-time'), countEl = $('br-count'), cue = $('br-cue'), sub = $('br-sub'),
      go = $('br-go'), snd = $('br-sound'), rh = [$('rh-a'), $('rh-b'), $('rh-c')];
  var PACE = { n: [2.5, 1, 6.5], s: [3.5, 1.5, 9] }, pace = 'n', TOTAL = 300, C = 603.2;
  var LO = 0.6, MID = 0.9, HI = 1.0;
  var state = 'idle', ph = 0, pt = 0, el = 0, breaths = 0, running = false, raf = 0, last = 0, ctx = null, lock = null;
''' + WAKE_JS + '''
  function mmss(s){ s = Math.max(0, Math.ceil(s)); var m = Math.floor(s / 60), r = s % 60; return m + ':' + (r < 10 ? '0' : '') + r; }
  function ease(x){ return x < 0.5 ? 2 * x * x : 1 - Math.pow(-2 * x + 2, 2) / 2; }
  function layout(){
    var p = PACE[pace], tot = p[0] + p[1] + p[2];
    for (var j = 0; j < 3; j++){ rh[j].style.flex = (p[j] / tot).toFixed(3); rh[j].style.setProperty('--p', 0); }
    var lab = ['rl-a', 'rl-b', 'rl-c']; for (j = 0; j < 3; j++) $(lab[j]).style.flex = (p[j] / tot).toFixed(3);
  }
  function scaleAt(){
    var p = PACE[pace], x = Math.min(1, pt / p[ph]);
    if (ph === 0) return LO + (MID - LO) * ease(x);
    if (ph === 1) return MID + (HI - MID) * ease(x);
    return HI - (HI - LO) * ease(x);
  }
  function setPhase(n){
    ph = n; pt = 0;
    var k = ['in1', 'in2', 'out'][n]; cue.textContent = S[k]; sub.textContent = S[k + 's'];
    beep([392, 523, 330][n], n === 2 ? 0.6 : 0.3, 0.08);
  }
  function draw(){
    core.style.transform = 'scale(' + (state === 'idle' ? LO : scaleAt()).toFixed(4) + ')';
    arc.style.strokeDashoffset = (C * (1 - Math.min(1, el / TOTAL))).toFixed(1);
    timeEl.textContent = state === 'done' ? '✓' : mmss(TOTAL - el);
    countEl.textContent = breaths ? (breaths === 1 ? S.count1 : S.count.replace('{n}', breaths)) : '\\u00a0';
    var p = PACE[pace];
    for (var j = 0; j < 3; j++) rh[j].style.setProperty('--p', state === 'idle' ? 0 : (j < ph ? 1 : (j === ph ? Math.min(1, pt / p[j]) : 0)).toFixed(3));
  }
  function frame(now){
    if (!running) return;
    var dt = Math.min(0.25, (now - last) / 1000); last = now; pt += dt; el += dt;
    var p = PACE[pace];
    if (pt >= p[ph]){
      if (ph < 2) setPhase(ph + 1);
      else {
        breaths++;
        if (el >= TOTAL - 0.5){ finish(); return; }
        setPhase(0);
      }
    }
    draw(); raf = requestAnimationFrame(frame);
  }
  function run(){ running = true; last = performance.now(); cancelAnimationFrame(raf); raf = requestAnimationFrame(frame); go.textContent = S.pause; wake(true); }
  function pause(){ running = false; cancelAnimationFrame(raf); go.textContent = S.resume; cue.textContent = S.paused; wake(false); }
  function finish(){
    running = false; cancelAnimationFrame(raf); state = 'done'; el = TOTAL; ph = 2; pt = PACE[pace][2];
    cue.textContent = S.done; sub.textContent = S.dones; go.textContent = S.again; draw(); wake(false);
    beep(523, 0.4, 0.08); setTimeout(function(){ beep(659, 0.6, 0.08); }, 300);
  }
  function reset(){
    running = false; cancelAnimationFrame(raf); state = 'idle'; ph = 0; pt = 0; el = 0; breaths = 0;
    cue.textContent = S.ready; sub.textContent = S.readys; go.textContent = S.start; layout(); draw(); wake(false);
  }
  go.addEventListener('click', function(){
    if (state === 'idle' || state === 'done'){ reset(); state = 'run'; setPhase(0); run(); }
    else if (running) pause();
    else { var k = ['in1', 'in2', 'out'][ph]; cue.textContent = S[k]; run(); }
  });
  $('br-reset').addEventListener('click', reset);
  function seg(id, fn){
    $(id).addEventListener('click', function(e){
      var b = e.target.closest('button'); if (!b) return;
      this.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      fn(b.getAttribute('data-v')); reset();
    });
  }
  seg('br-dur', function(v){ TOTAL = +v; });
  seg('br-pace', function(v){ pace = v; });
  document.addEventListener('visibilitychange', function(){ if (!document.hidden && running) wake(true); });
  reset();
})();
</script>
'''

page("ic-cekis.html", "5 Dakikalık İç Çekiş Nefesi",
     "Stanford'daki çalışmada ruh hâlini meditasyondan daha çok iyileştiren nefes tekniği: döngüsel iç çekiş. İki kez alın, uzun verin; 5 dakikalık rehberle birlikte yapın.",
     "ic-cekis.html", SELF2_CSS, SIGH_BODY, SIGH_JS + YT_JS,
     seo_title="Döngüsel İç Çekiş: 5 Dakikalık Nefes Egzersizi | İhsan Eren",
     about={"@type": "Thing", "name": "Nefes egzersizi"},
     faq_items=pick(SIGH_FAQ, 0, 1, 2, 3))

# ------------------------------------------------------------------ 4 · DOĞA REÇETESİ
DAYS_TR = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
NT_ROWS = "\n".join(
    f'<div class="dy"><span>{d}</span><span class="bar"><i></i></span><span class="v"><output>0</output> dk</span>'
    f'<span class="stepper" role="group" aria-label="{d}"><button type="button" data-d="-10" aria-label="10 dakika azalt" disabled>−</button>'
    f'<button type="button" data-d="10" aria-label="10 dakika artır">+</button></span></div>'
    for d in DAYS_TR)

NATURE_FAQ = [
 ("Mutlaka ormana ya da kıra mı gitmeliyim?", "Hayır. Araştırmada şehir parkları, korular, sahiller ve kırlar gibi açık yeşil ve mavi alanlara yapılan ziyaretler birlikte sayıldı. Mahallenizdeki park ya da deniz kenarı da işe yarar."),
 ("Spor yapmam gerekir mi?", "Hayır. Doğada oturmak ya da yavaş yürümek de sayılır. Stres hormonunu ölçen çalışmada katılımcılardan özellikle tempolu egzersiz yapmamaları, telefonla uğraşmamaları istendi. Yürürseniz hareketin faydası da eklenir."),
 ("120 dakikayı tek seferde mi geçirmeliyim?", "Gerekmez. Araştırmada haftalık sürenin tek uzun ziyaretle ya da birkaç kısa ziyaretle tamamlanması fark etmedi. Örneğin 4 gün 30 dakika da olur."),
 ("Evden çıkamıyorum, ne yapabilirim?", "Pencereden yeşil görmek bile iyileşmeyle ilişkili bulundu. Perdeleri açın, mümkünse pencereye yakın oturun, balkonda ya da pencere önünde bitki yetiştirin. Evden çıkmakta zorlanıyorsanız yeniden güvenle yürümek için fizyoterapiden destek alabilirsiniz."),
]

NATURE_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Doğa reçetesi: haftada 120 dakika</h1>
    <p class="lede">İngiltere'de yaklaşık 20 bin kişiyle yapılan bir araştırmada, haftada en az 2 saatini doğada geçirenler sağlıklarını ve iyi oluşlarını belirgin şekilde daha iyi bildirdi. Bu 2 saati tek seferde ya da parça parça geçirmek fark etmiyordu. İstanbul'da doğa sandığınızdan yakın: park, koru, sahil ya da deniz kenarı da sayılır.</p>
    <p class="meta">Son güncelleme: 30 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>120 dk</b><span>Haftalık eşik: bu sürenin altında belirgin bir fark görülmedi (19.806 kişi)</span></div>
        <div class="stat"><b>1,59</b><span>Olasılık oranı: haftada 120–179 dk doğada vakit geçirenlerde iyi sağlık bildirme, hiç çıkmayanlara göre</span></div>
        <div class="stat"><b>200–300 dk</b><span>Faydanın en yüksek görüldüğü aralık; daha fazlasında ek fayda görülmedi</span></div>
        <div class="stat"><b>20–30 dk</b><span>Stres hormonu kortizolün en verimli düştüğü doğa molası süresi</span></div>
      </div>
    </div>
  </section>

  <section id="takvim">
    <div class="wrap">
      <p class="eyebrow">Haftanızı planlayın</p>
      <h2>Doğa takvimi</h2>
      <p class="soft">Bu hafta doğada geçirdiğiniz ya da geçirmeyi planladığınız süreleri girin. Takvim bu cihazda saklanır ve her pazartesi sıfırlanır.</p>
      <div class="tool">
        <div class="nt">
          <div class="wk">
{NT_ROWS}
            <div class="controls" style="margin-top:10px"><button type="button" class="cta ghost" id="nt-reset">Sıfırla</button></div>
          </div>
          <div>
            <div class="gauge">
              <svg viewBox="0 0 240 240" aria-hidden="true"><circle class="bg" cx="120" cy="120" r="100"/><circle class="fg" id="nt-arc" cx="120" cy="120" r="100" stroke-dasharray="628.3" stroke-dashoffset="628.3"/><line class="t150" x1="220" y1="120" x2="232" y2="120" transform="rotate(144 120 120)"/></svg>
              <div class="c"><b id="nt-tot">0</b><span>dakika / hafta</span></div>
            </div>
            <ul class="res-list" aria-live="polite">
              <li id="nt-r1"><i></i><span></span></li>
            </ul>
          </div>
        </div>
        <div class="nt-strings" hidden>
          <span data-k="low">Haftalık 120 dakikaya {{n}} dakika kaldı. Parça parça da olur: örneğin 4 gün 30 dakika.</span>
          <span data-k="ok">120 dakika eşiğini geçtiniz. Araştırmada bu düzeyde doğada vakit geçirenler daha iyi sağlık ve iyi oluş bildirdi.</span>
          <span data-k="peak">Faydanın en yüksek görüldüğü 200–300 dakika aralığındasınız.</span>
          <span data-k="over">300 dakikanın üstündesiniz. Araştırmada ek fayda görülmedi, ama doğanın tadını çıkarın.</span>
        </div>
      </div>
      <p class="count">Halkadaki ince yeşil çizgi 120 dakikayı, halkanın tamamı 300 dakikayı gösterir.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <p class="eyebrow">İstanbul'da doğa</p>
      <h2>Bu hafta nereye?</h2>
      <p class="soft">Uzağa gitmeniz gerekmez; evinize en yakın park da sayılır. Birkaç öneri:</p>
      <div class="places">
        <div class="place"><h3>Avrupa yakası</h3><ul><li>Belgrad Ormanı</li><li>Emirgan Korusu</li><li>Yıldız Parkı</li><li>Maçka Parkı</li><li>Gülhane Parkı</li><li>Atatürk Kent Ormanı</li><li>Bebek–Rumelihisarı sahili</li><li>Florya sahili</li></ul></div>
        <div class="place"><h3>Anadolu yakası</h3><ul><li>Validebağ Korusu</li><li>Fenerbahçe Parkı</li><li>Göztepe 60. Yıl Parkı</li><li>Moda sahili</li><li>Büyük Çamlıca</li><li>Kuzguncuk–Beylerbeyi sahili</li><li>Polonezköy</li><li>Adalar</li></ul></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Pencereden ağaç görmek bile</h2>
        <p class="soft">1984'te <em>Science</em> dergisinde yayımlanan ünlü bir çalışmada, safra kesesi ameliyatı olan hastaların kayıtları incelendi. Penceresinden ağaçları gören 23 hasta, tuğla duvar gören 23 benzer hastayla karşılaştırıldı.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Ağaç görenler hastanede daha kısa kaldı: ortalama 7,96 güne karşı 8,70 gün.</li>
        <li>Daha az güçlü ağrı kesiciye ihtiyaç duydular.</li>
        <li>Hemşire notlarında haklarında daha az olumsuz yorum vardı.</li>
        <li>Küçük bir çalışmadır, ama hastane tasarımında doğaya yer açılmasına ilham verdi.</li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Hayranlık yürüyüşü</h2>
      <p class="soft">52 sağlıklı yaşlı yetişkin, 8 hafta boyunca haftada bir 15 dakikalık yürüyüş yaptı. Yürürken “hayranlık” duygusuna, yani kendinden çok daha büyük bir şeyin karşısında hissedilen o hayret hâline dikkat etmeleri istenen grupta günlük sıkıntı azaldı; şefkat ve minnet gibi duygular arttı. Yürüyüşte çektikleri fotoğraflarda zamanla kendilerine daha az, manzaraya daha çok yer verdiler ve gülümsemeleri belirginleşti.</p>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Telefonu cebe koyun</h3><p>Fotoğraf çekmek serbest, ama ekrana bakarak yürümeyin.</p></div>
        <div class="kind"><span class="n">2</span><h3>Büyüklüğü fark edin</h3><p>Denizin genişliği, gökyüzü, yaşlı bir çınarın gövdesi: sizi aşan şeylere bakın.</p></div>
        <div class="kind"><span class="n">3</span><h3>Küçüğü de görün</h3><p>Bir yaprağın damarları, taşların arasındaki yosun, martıların uçuşu.</p></div>
        <div class="kind"><span class="n">4</span><h3>Her seferinde yeni</h3><p>Farklı bir yol ya da saat seçin; tanıdık yerler de yeni ayrıntılarla şaşırtabilir.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(NATURE_FAQ)}
      {CTA_CARD("Yeniden güvenle yürümek ve dışarı çıkmak", "yürüme ve denge çalışması")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "White MP, Alcock I, Grellier J, et al. " + ext("https://www.nature.com/articles/s41598-019-44097-3", "Spending at least 120 minutes a week in nature is associated with good health and wellbeing") + ". Sci Rep. 2019;9:7730.",
        "Hunter MR, Gillespie BW, Chen SY. " + ext("https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.00722/full", "Urban nature experiences reduce stress in the context of daily life based on salivary biomarkers") + ". Front Psychol. 2019;10:722.",
        "Ulrich RS. " + ext("https://www.science.org/doi/10.1126/science.6143402", "View through a window may influence recovery from surgery") + ". Science. 1984;224(4647):420-421.",
        "Sturm VE, Datta S, Roy ARK, et al. " + ext("https://pubmed.ncbi.nlm.nih.gov/32955293/", "Big smile, small self: awe walks promote prosocial positive emotions in older adults") + ". Emotion. 2022;22(5):1044-1058.",
      ])}
    </div>
  </section>
</main>'''

NATURE_JS = '''<script>
(function(){
  var root = document.getElementById('takvim'); if (!root) return;
  var S = {}; root.querySelectorAll('.nt-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var $ = function(id){ return document.getElementById(id); };
  var rows = root.querySelectorAll('.dy'), arc = $('nt-arc'), C = 628.3, KEY = 'drihsaneren-doga', v = [0, 0, 0, 0, 0, 0, 0];
  function week(){ var d = new Date(); d.setHours(0, 0, 0, 0); d.setDate(d.getDate() - ((d.getDay() + 6) % 7)); return d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate(); }
  try {
    var s = JSON.parse(localStorage.getItem(KEY) || 'null');
    if (s && s.w === week() && s.v && s.v.length === 7) v = s.v.map(function(x){ return Math.max(0, Math.min(300, +x || 0)); });
  } catch (e) {}
  function save(){ try { localStorage.setItem(KEY, JSON.stringify({ w: week(), v: v })); } catch (e) {} }
  rows.forEach(function(r, i){
    r.addEventListener('click', function(e){
      var b = e.target.closest('button'); if (!b || b.disabled) return;
      v[i] = Math.max(0, Math.min(300, v[i] + (+b.getAttribute('data-d')))); save(); upd();
    });
  });
  function upd(){
    var tot = 0;
    rows.forEach(function(r, i){
      tot += v[i];
      r.querySelector('output').textContent = v[i];
      r.querySelector('.bar i').style.width = Math.min(100, v[i] / 90 * 100).toFixed(1) + '%';
      r.querySelector('[data-d="-10"]').disabled = v[i] <= 0;
      r.querySelector('[data-d="10"]').disabled = v[i] >= 300;
    });
    $('nt-tot').textContent = tot;
    arc.style.strokeDashoffset = (C * (1 - Math.min(tot, 300) / 300)).toFixed(1);
    var li = $('nt-r1'), t;
    if (tot < 120){ li.className = 'low'; t = S.low.replace('{n}', 120 - tot); }
    else { li.className = 'ok'; t = tot > 300 ? S.over : (tot >= 200 ? S.peak : S.ok); }
    li.querySelector('span').textContent = t;
  }
  $('nt-reset').addEventListener('click', function(){ v = [0, 0, 0, 0, 0, 0, 0]; save(); upd(); });
  upd();
})();
</script>
'''

page("doga-recetesi.html", "Doğa Reçetesi",
     "Haftada 120 dakika doğada vakit geçirenler sağlıklarını daha iyi bildiriyor. Doğa takviminiz, İstanbul'dan öneriler, hayranlık yürüyüşü ve pencereden ağaç görmenin etkisi.",
     "doga-recetesi.html", SELF2_CSS, NATURE_BODY, NATURE_JS,
     seo_title="Doğa Reçetesi: Haftada 120 Dakika Doğa ve Sağlık | İhsan Eren",
     about={"@type": "Thing", "name": "Doğada vakit geçirme"},
     faq_items=pick(NATURE_FAQ, 0, 1, 2, 3))

# ------------------------------------------------------------------ 5 · SOSYAL BAĞ
TASKS = [
 ("Arkadaş", "Uzun zamandır konuşmadığınız birine “aklıma geldin” diye kısa bir mesaj atın.",
  "Yaklaşık 6.000 kişiyle yapılan deneylerde insanlar, böyle bir mesajın karşı tarafı ne kadar sevindireceğini tutarlı biçimde olduğundan az tahmin etti."),
 ("Teşekkür", "Hayatınızda iz bırakmış birine kısa bir teşekkür mektubu yazıp gönderin.",
  "Yazanlar, karşı tarafın ne kadar şaşırıp sevineceğini az, ne kadar tuhaf hissedeceğini fazla tahmin ediyor. Yazmak yalnızca birkaç dakika sürüyor."),
 ("Aile", "Bugün bir yakınınıza mesaj yazmak yerine sesli arayın.",
  "Eski arkadaşlarıyla telefonda konuşanlar, yazışanlara göre daha güçlü bağ kurduklarını bildirdi ve bu, yazışmaktan daha tuhaf hissettirmedi."),
 ("Yabancı", "Otobüste, sırada ya da bakkalda biriyle kısa bir sohbet açın.",
  "Trende yanındakiyle konuşanlar, yolculuğu yalnız geçirenlerden daha keyifli buldu; oysa tam tersini bekliyorlardı."),
 ("Komşu", "Bir komşunuzu çaya davet edin ya da kapısını çalıp hâlini hatırını sorun.", ""),
 ("Aile", "Yaşlı bir akrabanızı ziyaret edin ya da görüntülü arayın.",
  "Dünya Sağlık Örgütü'ne göre her 3 yaşlıdan biri sosyal olarak yalıtılmış olabilir."),
 ("Birlikte", "Bugün en az bir öğünü birileriyle, telefonlar masadan kalkmış olarak yiyin.", ""),
 ("Yürüyüş", "Yürüyüşünüzü bir arkadaşınızla, mümkünse bir parkta yapın.",
  "Hareket, doğa ve sohbet bir arada. Doğanın etkisi için Doğa reçetesi sayfasına bakabilirsiniz."),
 ("Dokunma", "Sevdiğiniz birine sarılın.",
  "404 yetişkinle yapılan bir çalışmada daha sık sarılanlar, soğuk algınlığı virüsüne karşı biraz daha korunaklıydı ve hastalananların belirtileri daha hafifti."),
 ("Topluluk", "Bir kursa, koroya, yürüyüş grubuna ya da gönüllü bir etkinliğe katılın.",
  "Düzenli buluşan gruplar, bağları kendiliğinden sürdürmeyi kolaylaştırır."),
 ("Dinlemek", "Bugün birini sözünü kesmeden ve telefona bakmadan dinleyin.", ""),
 ("Anı", "Eski bir fotoğrafı, o anı paylaştığınız kişiye gönderin.",
  "Beklenmedik küçük temaslar, karşı tarafı tahmin ettiğinizden daha fazla sevindirir."),
 ("İyilik", "Birine küçük bir iyilik yapın: alışverişini taşıyın, yol tarif edin, bir yemeği paylaşın.", ""),
]
TASK_HTML = "\n".join(
    f'<div class="task" data-i="{i}"{"" if i == 0 else " hidden"}><span class="k">{k}</span><p>{t}</p>'
    + (f'<small><strong>Neden?</strong> {w}</small>' if w else "") + '</div>'
    for i, (k, t, w) in enumerate(TASKS))

SOCIAL_FAQ = [
 ("Yalnız yaşamak mı zararlı, yalnız hissetmek mi?", "İkisi de. Sosyal yalıtım (az ilişki ve temas) ile yalnızlık hissi farklı şeylerdir ve ikisi de sağlık risklerini artırır. 148 çalışmayı inceleyen analizde, sosyal ilişkileri birden fazla yönüyle ölçen çalışmalarda hayatta kalmayla ilişki daha da güçlüydü."),
 ("Mesajlaşmak yeterli mi?", "Yazışmak da bağ kurar, ama bir çalışmada eski arkadaşlarıyla telefonda konuşanlar, e-postayla yazışanlara göre daha güçlü bağ kurduklarını bildirdi ve beklediklerinin aksine daha fazla tuhaflık yaşamadılar. Mümkünse sesli ya da yüz yüze görüşmeyi deneyin."),
 ("Kaç arkadaşım olmalı?", "Belirli bir sayı yok. 1938'den beri süren Harvard Yetişkin Gelişimi Araştırması'nın yöneticisi Robert Waldinger'in vurguladığı gibi, önemli olan ilişkilerin sayısından çok niteliğidir: güvenebildiğiniz birkaç yakın ilişki bile çok değerlidir."),
 ("Uzun süredir kendimi yalnız ve mutsuz hissediyorum, ne yapmalıyım?", "Bu his yaygındır ve değişebilir. Küçük adımlar yardımcı olabilir; ama haftalardır süren çökkünlük, umutsuzluk ya da uyku ve iştah değişiklikleri varsa bir hekime ya da ruh sağlığı uzmanına başvurun. Kendinize zarar verme düşünceleriniz varsa 112'yi arayın."),
]

SOCIAL_BODY = f'''<header class="page">
  <div class="wrap">
    <a class="back" href="bilgi.html">{BACK}Bilgi köşesi</a>
    <p class="eyebrow">Kendine iyi bak</p>
    <h1>Sosyal bağ: unutulan sağlık önerisi</h1>
    <p class="lede">Dünya Sağlık Örgütü'ne göre dünyada her 6 kişiden biri yalnızlık yaşıyor ve yalnızlık her saat yaklaşık 100 ölümle ilişkili. 148 çalışmayı bir araya getiren bir analizde, güçlü sosyal ilişkileri olanların hayatta kalma olasılığı %50 daha yüksekti. İyi haber: bağ kurmak için büyük adımlar gerekmiyor ve küçük adımların etkisini çoğu zaman olduğundan az tahmin ediyoruz.</p>
    <p class="meta">Son güncelleme: 30 Eylül 2026</p>
  </div>
</header>

<main>
  <section>
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>6 kişiden 1</b><span>Dünyada yalnızlık yaşayanların oranı (DSÖ, 2025)</span></div>
        <div class="stat"><b>871.000</b><span>Yalnızlıkla ilişkili yıllık ölüm: saatte yaklaşık 100</span></div>
        <div class="stat"><b>%50</b><span>Güçlü sosyal ilişkileri olanlarda daha yüksek hayatta kalma olasılığı (148 çalışma, 308.849 kişi)</span></div>
        <div class="stat"><b>2 kat</b><span>Yalnız hissedenlerde depresyona girme olasılığı</span></div>
      </div>
    </div>
  </section>

  <section id="gorev">
    <div class="wrap">
      <p class="eyebrow">Bugün ne yapabilirsiniz?</p>
      <h2>Bugünün bağ önerisi</h2>
      <p class="soft">Her gün küçük bir adım. Beğenmediyseniz başka bir öneri isteyin; yaptığınızda işaretleyin. Haftalık sayınız bu cihazda saklanır ve her pazartesi sıfırlanır.</p>
      <div class="tool">
        <div class="gv">
          <div class="task-wrap" aria-live="polite">
{TASK_HTML}
          </div>
          <div>
            <p class="q">Bu hafta attığınız adımlar</p>
            <div class="gv-count" id="gv-n">0</div>
            <div class="wkdots" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
            <p class="hint" id="gv-msg"></p>
            <div class="controls" style="margin-top:14px">
              <button type="button" class="cta" id="gv-done">Yaptım</button>
              <button type="button" class="cta ghost" id="gv-next">Başka bir öneri</button>
            </div>
          </div>
        </div>
        <div class="gv-strings" hidden>
          <span data-k="m0">Haftanın ilk adımı için hazır mısınız?</span>
          <span data-k="m1">Güzel bir başlangıç. Küçük temaslar da sayılır.</span>
          <span data-k="m3">Harika gidiyorsunuz. Bu adımların karşı tarafı ne kadar sevindirdiğini tahmin etmek zor.</span>
          <span data-k="m7">Her gün bir adım: bu hafta bağlarınıza gerçekten yatırım yaptınız.</span>
          <span data-k="thanks">İşaretlendi</span>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <p class="eyebrow">Şaşırtan bulgular</p>
      <h2>Tahminlerimiz yanılıyor</h2>
      <p class="soft">Psikoloji araştırmaları, bağ kurmaktan çoğu zaman yanlış tahminler yüzünden kaçındığımızı gösteriyor.</p>
      <div class="kinds">
        <div class="kind"><span class="n">1</span><h3>Yabancıyla sohbet</h3><p>Trende yolculara yanındakiyle konuşmaları söylendiğinde, yalnız kalanlardan daha keyifli bir yolculuk geçirdiler; oysa tersini bekliyorlardı. Konuşulan kişiler de bundan hoşlandı.</p></div>
        <div class="kind"><span class="n">2</span><h3>Teşekkür mektubu</h3><p>Yazanlar, alıcının ne kadar şaşırıp sevineceğini az, ne kadar tuhaf hissedeceğini fazla tahmin etti.</p></div>
        <div class="kind"><span class="n">3</span><h3>“Aklıma geldin”</h3><p>13 deneyde yaklaşık 6.000 kişi: kısa bir mesajın ya da küçük bir hediyenin ne kadar takdir göreceğini genellikle az tahmin ettik. Beklenmedik olduğunda etkisi daha da büyüktü.</p></div>
        <div class="kind"><span class="n">4</span><h3>Sesli arama</h3><p>İnsanlar telefonda konuşmanın tuhaf olacağını düşündü; oysa sesli görüşme, yazışmaya göre daha güçlü bağ hissi yarattı ve yaklaşık aynı süreyi aldı.</p></div>
      </div>
      <div class="callout"><p><strong>Sarılmanın gücü:</strong> 404 sağlıklı yetişkinin 14 gün boyunca her akşam sorgulandığı, ardından soğuk algınlığı virüsüyle karşılaştırıldığı bir çalışmada, sosyal desteği güçlü olanlar ve daha sık sarılanlar enfeksiyona karşı biraz daha korunaklıydı; hastalananların belirtileri de daha hafifti.</p></div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Yalnızlık mı, yalnız kalmak mı?</h2>
      <div class="def">
        <div><h3>Yalnızlık</h3><p>İstediğiniz ile sahip olduğunuz ilişkiler arasındaki farktan doğan acı verici his. Kalabalık içinde de yalnız hissedebilirsiniz.</p></div>
        <div><h3>Sosyal yalıtım</h3><p>Nesnel olarak az sayıda ilişki ve temas. Yaşlıların 3'te 1'ini, ergenlerin 4'te 1'ini etkileyebilir.</p></div>
      </div>
      <p class="soft" style="margin-top:18px">Dünya Sağlık Örgütü'nün 2025 raporuna göre yalnızlık ve sosyal yalıtım inme, kalp hastalığı, diyabet, bilişsel gerileme ve erken ölüm riskini artırıyor. 148 çalışmayı inceleyen analizde sosyal ilişkilerin ölüm riski üzerindeki etkisi, sigara ve alkol gibi bilinen risk etkenleriyle karşılaştırılabilir düzeydeydi; hareketsizlik ve obezitenin etkisinden daha büyüktü.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div>
        <h2>Evden çıkamayan yakınlarınız için</h2>
        <p class="soft">İnme, kalça kırığı, Parkinson hastalığı ya da uzun süren bir ağrı, insanı evine ve yatağına bağlayarak yalnızlaştırabilir. Hareket kaybı ile yalnızlık birbirini besler.</p>
      </div>
      <ul class="dots" style="align-self:center">
        <li>Düzenli ziyaret edin ya da arayın; sohbeti yalnızca sağlıkla sınırlı tutmayın.</li>
        <li>Aile kararlarına ve günlük işlere katın; kendini gerekli hissetmek önemlidir.</li>
        <li>İşitme ya da görme sorunları sosyal hayattan çekilmeye yol açabilir; kontrol ettirin.</li>
        <li>Yeniden güvenle yürümek, dışarı çıkmayı ve insanlarla buluşmayı da kolaylaştırır. <a href="inme-rehabilitasyonu.html">İnme sonrası</a> ve <a href="kalca-kirigi.html">kalça kırığı sonrası</a> rehberlerine bakabilirsiniz.</li>
      </ul>
    </div>
  </section>

  <section id="video">
    <div class="wrap">
      <p class="eyebrow">Video</p>
      <h2>İyi bir hayatı ne sağlar?</h2>
      <p class="soft">Harvard'da 1938'den beri süren Yetişkin Gelişimi Araştırması'nın yöneticisi psikiyatrist Robert Waldinger'in, dünyanın en çok izlenen TED konuşmalarından biri. Konuşma İngilizcedir; oynatıcının altyazı ayarlarından Türkçe altyazı seçebilirsiniz.</p>
      <div class="vids">
        <div class="vid">
          {vbox("8KkKuTCFvzI", "İyi bir hayat TED konuşmasını oynat", "What makes a good life? Lessons from the longest study on happiness | Robert Waldinger | TED")}
          <h3>En uzun mutluluk araştırmasından dersler</h3>
          <p>Yüzlerce kişiyi gençliklerinden yaşlılıklarına kadar izleyen araştırmanın ana mesajı: iyi ilişkiler bizi daha mutlu ve daha sağlıklı tutar.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Sık sorulan sorular</h2>
      {faq(SOCIAL_FAQ)}
      {CTA_CARD("Evden çıkamayan yakınınızın yeniden hareket etmesi", "evden çıkamayan yakınım için rehabilitasyon")}
    </div>
  </section>

  <section>
    <div class="wrap col sources">
      <p class="eyebrow">Kaynaklar</p>
      {src_list([
        "World Health Organization. " + ext("https://www.who.int/news/item/30-06-2025-social-connection-linked-to-improved-heath-and-reduced-risk-of-early-death", "Social connection linked to improved health and reduced risk of early death") + ". WHO Commission on Social Connection, 30 June 2025.",
        "Holt-Lunstad J, Smith TB, Layton JB. " + ext("https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1000316", "Social relationships and mortality risk: a meta-analytic review") + ". PLoS Med. 2010;7(7):e1000316.",
        "Epley N, Schroeder J. " + ext("https://psycnet.apa.org/record/2014-28833-001", "Mistakenly seeking solitude") + ". J Exp Psychol Gen. 2014;143(5):1980-1999.",
        "Kumar A, Epley N. " + ext("https://journals.sagepub.com/doi/10.1177/0956797618772506", "Undervaluing gratitude: expressers misunderstand the consequences of showing appreciation") + ". Psychol Sci. 2018;29(9):1423-1435.",
        "Liu PJ, Rim S, Min L, Min KE. " + ext("https://psycnet.apa.org/record/2022-77686-001", "The surprise of reaching out: appreciated more than we think") + ". J Pers Soc Psychol. 2023;124(4):754-771.",
        "Kumar A, Epley N. " + ext("https://www.semanticscholar.org/paper/4146edc85d69e49757178edbb6495ba4c378ea54", "It's surprisingly nice to hear you: misunderstanding the impact of communication media can lead to suboptimal choices of how to connect with others") + ". J Exp Psychol Gen. 2021;150(3):595-607.",
        "Cohen S, Janicki-Deverts D, Turner RB, Doyle WJ. " + ext("https://journals.sagepub.com/doi/abs/10.1177/0956797614559284", "Does hugging provide stress-buffering social support? A study of susceptibility to upper respiratory infection and illness") + ". Psychol Sci. 2015;26(2):135-147.",
      ])}
    </div>
  </section>
</main>'''

SOCIAL_JS = '''<script>
(function(){
  var root = document.getElementById('gorev'); if (!root) return;
  var S = {}; root.querySelectorAll('.gv-strings [data-k]').forEach(function(e){ S[e.getAttribute('data-k')] = e.textContent; });
  var $ = function(id){ return document.getElementById(id); };
  var cards = root.querySelectorAll('.task'), N = cards.length, cur = 0, n = 0, KEY = 'drihsaneren-bag', dots = root.querySelectorAll('.wkdots i');
  var doneB = $('gv-done');
  function week(){ var d = new Date(); d.setHours(0, 0, 0, 0); d.setDate(d.getDate() - ((d.getDay() + 6) % 7)); return d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate(); }
  try { var s = JSON.parse(localStorage.getItem(KEY) || 'null'); if (s && s.w === week()) n = Math.max(0, +s.n || 0); } catch (e) {}
  function save(){ try { localStorage.setItem(KEY, JSON.stringify({ w: week(), n: n })); } catch (e) {} }
  var label = doneB.textContent;
  function show(k){
    cards[cur].hidden = true; cur = k; cards[cur].hidden = false;
    cards[cur].classList.remove('pop'); void cards[cur].offsetWidth; cards[cur].classList.add('pop');
    doneB.disabled = false; doneB.textContent = label;
  }
  function next(){ var k = cur; if (N > 1) while (k === cur) k = Math.floor(Math.random() * N); show(k); }
  function paint(){
    $('gv-n').textContent = n;
    dots.forEach(function(d, j){ d.classList.toggle('on', j < n); });
    $('gv-msg').textContent = n === 0 ? S.m0 : (n < 3 ? S.m1 : (n < 7 ? S.m3 : S.m7));
  }
  $('gv-next').addEventListener('click', next);
  doneB.addEventListener('click', function(){
    n++; save(); paint(); doneB.disabled = true; doneB.textContent = S.thanks + ' ✓';
    setTimeout(next, 1400);
  });
  paint();
})();
</script>
'''

page("bag-kurmak.html", "Sosyal Bağ ve Sağlık",
     "Güçlü sosyal ilişkileri olanların hayatta kalma olasılığı %50 daha yüksek. Yalnızlığın sağlığa etkisi, şaşırtan araştırmalar ve her gün için küçük bir bağ önerisi.",
     "bag-kurmak.html", SELF2_CSS, SOCIAL_BODY, SOCIAL_JS + YT_JS,
     seo_title="Sosyal Bağ ve Sağlık: Yalnızlığa Karşı Küçük Adımlar | İhsan Eren",
     about={"@type": "Thing", "name": "Sosyal bağlantı ve yalnızlık"},
     faq_items=pick(SOCIAL_FAQ, 0, 1, 2, 3))

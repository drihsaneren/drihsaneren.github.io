# -*- coding: utf-8 -*-
# Analiz raporu: beyaz JPG sayfaları yerine sitenin renklerinde, yumuşak geçişli ve
# hareketli grafiklerle kendiliğinden ilerleyen bir slayt gösterisi.
import math

p = "site/index.html"
s = open(p, encoding="utf-8").read()


def rep(old, new, cnt=1):
    global s
    assert s.count(old) == cnt, (old[:80], s.count(old))
    s = s.replace(old, new)


def f(x):
    return f"{x:.1f}".rstrip("0").rstrip(".")


# ---------- 1) fonksiyonel yaş göstergesi ----------
CX, CY, R = 150, 160, 120


def gp(age, r=R):
    th = math.radians(180 - (age - 30) / 60 * 180)
    return CX + r * math.cos(th), CY - r * math.sin(th)


x54, y54 = gp(54)
x62, y62 = gp(62)
ticks = []
for a in range(30, 91, 5):
    (ax, ay), (bx, by) = gp(a, 100), gp(a, 94 if a % 10 else 90)
    ticks.append(f'<line x1="{f(ax)}" y1="{f(ay)}" x2="{f(bx)}" y2="{f(by)}"/>')
(t1x, t1y), (t2x, t2y) = gp(62, 106), gp(62, 136)
l62x, l62y = gp(62, 148)
l54x, l54y = gp(54, 148)
gxl, gyl = gp(58, 82)
GAUGE = f'''<svg class="rs-gauge" viewBox="0 0 300 190" aria-hidden="true" focusable="false">
              <defs><linearGradient id="rs-gg" gradientUnits="userSpaceOnUse" x1="30" y1="160" x2="120" y2="40"><stop offset="0" stop-color="#8fa476"/><stop offset="1" stop-color="#f3c565"/></linearGradient></defs>
              <path class="trk" d="M30 160 A120 120 0 0 1 270 160"/>
              <g class="tk">{"".join(ticks)}</g>
              <path class="arc" pathLength="1" d="M30 160 A120 120 0 0 1 {f(x54)} {f(y54)}"/>
              <path class="gap" pathLength="1" d="M{f(x54)} {f(y54)} A120 120 0 0 1 {f(x62)} {f(y62)}"/>
              <line class="t62" x1="{f(t1x)}" y1="{f(t1y)}" x2="{f(t2x)}" y2="{f(t2y)}"/>
              <text class="l62" x="{f(l62x)}" y="{f(l62y + 4)}">62</text>
              <text class="l54" x="{f(l54x)}" y="{f(l54y + 4)}">54</text>
              <circle class="ring" cx="{f(x54)}" cy="{f(y54)}" r="9"/>
              <circle class="dot" cx="{f(x54)}" cy="{f(y54)}" r="8"/>
              <text class="gl" x="{f(gxl)}" y="{f(gyl + 2)}">−8 yıl</text>
              <text class="big" x="150" y="140" data-from="62">54</text>
              <text class="sub" x="150" y="166">fonksiyonel yaş</text>
              <text class="sc" x="30" y="184">30</text><text class="sc" x="270" y="184">90</text>
            </svg>'''

# ---------- 2) radar ----------
RC, RR = (160, 138), 92
AX = [("Kavrama", 88), ("Bacak gücü", 62), ("Denge", 95), ("Yürüme hızı", 90), ("Esneklik", 55), ("Dayanıklılık", 70)]


def rp(i, v):
    th = math.radians(-90 + 60 * i)
    return RC[0] + RR * v / 100 * math.cos(th), RC[1] + RR * v / 100 * math.sin(th)


rings = []
for v in (25, 50, 75, 100):
    pts = " ".join(f"{f(x)},{f(y)}" for x, y in (rp(i, v) for i in range(6)))
    rings.append(f'<polygon points="{pts}"/>')
spokes = "".join(f'<line x1="{RC[0]}" y1="{RC[1]}" x2="{f(rp(i, 100)[0])}" y2="{f(rp(i, 100)[1])}"/>' for i in range(6))
poly = " ".join(f"{f(x)},{f(y)}" for x, y in (rp(i, v) for i, (_, v) in enumerate(AX)))
dots, labels = [], []
for i, (name, v) in enumerate(AX):
    x, y = rp(i, v)
    low = v < 65
    dots.append(f'<circle class="{"lo" if low else "hi"}" cx="{f(x)}" cy="{f(y)}" r="{4.6 if low else 3.8}" style="--i:{i}"/>'
                + (f'<circle class="pl" cx="{f(x)}" cy="{f(y)}" r="5"/>' if low else ""))
    lx, ly = rp(i, 100 + 21)
    anc = "middle" if abs(lx - RC[0]) < 8 else ("start" if lx > RC[0] else "end")
    if i == 0:
        ly -= 8
    if i == 3:
        ly += 10
    labels.append(f'<text class="nm{" lo" if low else ""}" x="{f(lx)}" y="{f(ly)}" text-anchor="{anc}">{name}</text>'
                  f'<text class="vl{" lo" if low else ""}" x="{f(lx)}" y="{f(ly + 15)}" text-anchor="{anc}">{v}</text>')
RADAR = f'''<svg class="rs-radar" viewBox="0 0 320 282" aria-hidden="true" focusable="false">
              <defs><radialGradient id="rs-rf" cx="50%" cy="50%" r="60%"><stop offset="0" stop-color="#e2ab47" stop-opacity=".05"/><stop offset="1" stop-color="#e2ab47" stop-opacity=".32"/></radialGradient></defs>
              <g class="grid">{"".join(rings)}{spokes}</g>
              <g class="shape"><polygon class="poly" points="{poly}"/>{"".join(dots)}</g>
              <g class="lbls">{"".join(labels)}</g>
            </svg>'''

# ---------- 3) ölçüm tablosu ----------
ROWS = [("El sıkma", "24 kg", "ok", "normal", "up ok", "+1 kg"),
        ("5 kez otur-kalk", "13,8 sn", "mid", "sınırda", "dn ok", "−0,9 sn"),
        ("Otur-kalk gücü", "1,8 W/kg", "low", "düşük", "tg", "hedef"),
        ("Yürüme hızı", "1,15 m/sn", "ok", "normal", "dn low", "−0,05"),
        ("Ayak bileği duvar testi", "7 cm", "low", "kısıtlı", "no", "–"),
        ("Tek ayak durma", "16 sn", "ok", "normal", "up ok", "+2 sn"),
        ("SPPB", "10/12", "ok", "iyi", "no", "–")]
trs = []
for i, (n, v, c, st, ch, cv) in enumerate(ROWS):
    trs.append(f'<li style="--i:{i}"><span class="n">{n}</span><span class="v">{v}</span><span class="st {c}">{st}</span><span class="ch {ch}">{cv}</span></li>')
TABLE = '<ul class="rs-tab">\n              <li class="hd"><span class="n">Test</span><span class="v">Sonuç</span><span class="st">Durum</span><span class="ch">Değişim</span></li>\n              ' + "\n              ".join(trs) + "\n            </ul>"

# ---------- 4) kuvvet asimetrisi ----------
BF = [("Kavrama", 96, 100), ("Ayak bileği dorsifleksiyon", 71, 82), ("Kalça abdüksiyon", 79, 90),
      ("Diz fleksiyon", 88, 95), ("Diz ekstansiyon", 92, 100)]
bfr = []
for i, (n, l, r) in enumerate(BF):
    asym = round((max(l, r) - min(l, r)) / max(l, r) * 100)
    hi = asym >= 10
    bfr.append(f'<div class="rs-bf-r{" hi" if hi else ""}" style="--l:{l / 100:.2f};--r:{r / 100:.2f};--i:{i}"><b>{n}<em>%{asym} fark</em></b>'
               f'<span class="v">{l}</span><i class="bl"></i><i class="bm"></i><i class="br"></i><span class="v">{r}</span></div>')
BFLY = '<div class="rs-bf">\n              <div class="rs-bf-h"><span>Sol</span><span>Yaş normuna göre %</span><span>Sağ</span></div>\n              ' + "\n              ".join(bfr) + "\n            </div>"

# ---------- 5) vücut kompozisyonu + SPPB ----------
RINGS = [("Yağ oranı", "%32", 32, "mid"), ("Kas kütlesi", "%40", 40, "ok"), ("ASMI · kg/m²", "6,2", 62, "mid"), ("Faz açısı", "5,6°", 56, "ok")]
rg = []
for i, (n, v, pc, c) in enumerate(RINGS):
    rg.append(f'<div class="rs-ring {c}" style="--p:{pc};--i:{i}"><span class="rw"><svg viewBox="0 0 100 100" aria-hidden="true" focusable="false"><circle class="bg" cx="50" cy="50" r="42"/><circle class="fg" cx="50" cy="50" r="42" pathLength="100"/></svg>'
              f'<span class="rv" data-count>{v}</span></span><span class="rn">{n}</span></div>')
SP = [("Denge", 4), ("Yürüme", 4), ("Otur-kalk", 2)]
spr, k = [], 0
for n, sc in SP:
    blocks = ""
    for b in range(4):
        blocks += f'<i class="{"on" if b < sc else ""}" style="--i:{k}"></i>'
        k += 1
    spr.append(f'<div class="rs-sp-r"><span>{n}</span><span class="bk">{blocks}</span><b>{sc}/4</b></div>')
BODY = ('<div class="rs-rings">\n              ' + "\n              ".join(rg) + '\n            </div>\n'
        '            <div class="rs-sp"><p class="rs-sp-h"><span>SPPB · fiziksel performans</span><b>10/12</b></p>\n              '
        + "\n              ".join(spr) + "\n            </div>")

# ---------- 6) zaman içinde izlem ----------
XL = ["Oca 24", "Tem 24", "Oca 25", "Tem 25", "Oca 26", "Tem 26"]
X0, X1 = 44, 318
xs = [X0 + (X1 - X0) * i / 5 for i in range(6)]


def series(vals, lo, hi, top, bot):
    return [(x, bot - (v - lo) / (hi - lo) * (bot - top)) for x, v in zip(xs, vals)]


A = series([27, 26.5, 25, 24.5, 23, 24], 14, 30, 22, 100)
B = series([1.28, 1.26, 1.24, 1.22, 1.20, 1.15], 0.95, 1.35, 140, 208)
thr_y = 100 - (16 - 14) / 16 * 78


def path(pts):
    return "M" + " L".join(f"{f(x)} {f(y)}" for x, y in pts)


def area(pts, base):
    return path(pts) + f" L{f(pts[-1][0])} {base} L{f(pts[0][0])} {base} Z"


def pdots(pts, cls):
    return "".join(f'<circle class="{cls}" cx="{f(x)}" cy="{f(y)}" r="3.4" style="--i:{i}"/>' for i, (x, y) in enumerate(pts))


gridl = "".join(f'<line x1="{f(x)}" y1="16" x2="{f(x)}" y2="212"/>' for x in xs)
LINES = f'''<svg class="rs-line" viewBox="0 0 340 236" aria-hidden="true" focusable="false">
              <defs>
                <linearGradient id="rs-la" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e2ab47" stop-opacity=".30"/><stop offset="1" stop-color="#e2ab47" stop-opacity="0"/></linearGradient>
                <linearGradient id="rs-lb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9bf8c" stop-opacity=".30"/><stop offset="1" stop-color="#a9bf8c" stop-opacity="0"/></linearGradient>
              </defs>
              <g class="vg">{gridl}</g>
              <text class="ttl" x="{X0}" y="12">Kavrama gücü (kg)</text>
              <line class="thr" x1="{X0}" y1="{f(thr_y)}" x2="{X1}" y2="{f(thr_y)}"/>
              <text class="thl" x="{X1}" y="{f(thr_y - 5)}" text-anchor="end">Eşik 16 kg</text>
              <path class="ar a" d="{area(A, 100)}"/>
              <path class="ln a" pathLength="1" d="{path(A)}"/>
              {pdots(A, "pa")}
              <circle class="last a" cx="{f(A[-1][0])}" cy="{f(A[-1][1])}" r="5"/>
              <text class="lv a" x="{f(A[-1][0])}" y="{f(A[-1][1] - 10)}" text-anchor="end">24 kg</text>
              <text class="ttl" x="{X0}" y="130">Yürüme hızı (m/sn)</text>
              <path class="ar b" d="{area(B, 208)}"/>
              <path class="ln b" pathLength="1" d="{path(B)}"/>
              {pdots(B, "pb")}
              <circle class="last b" cx="{f(B[-1][0])}" cy="{f(B[-1][1])}" r="5"/>
              <text class="lv b" x="{f(B[-1][0])}" y="{f(B[-1][1] - 10)}" text-anchor="end">1,15</text>
              <g class="xl">{"".join(f'<text x="{f(x)}" y="230" text-anchor="middle">{t}</text>' for x, t in zip(xs, XL))}</g>
            </svg>'''

# ---------- 7) plan ----------
ICO = {
    "leg": '<path d="M9 3v7l-2 5 1 6M9 10l5 3 3 8"/>',
    "ank": '<path d="M8 3v11l-3 5h14l-2-3-5-2V3"/>',
    "flex": '<path d="M4 18c4-8 12-8 16 0M8 12l-2-5M16 12l2-5"/>',
    "walk": '<circle cx="13" cy="4.5" r="1.8"/><path d="M11 21l2-6 3 3v3M13 15l-1-5 3-2 2 3 3 1M10 10l-3 1-1 3"/>',
}
PLAN = [("leg", "Bacak gücü", "Haftada 3 gün, hızlı kalkış odaklı güç çalışması"),
        ("ank", "Ayak bileği", "Her gün 5 dakika mobilite ve germe"),
        ("flex", "Esneklik ve asimetri", "Sol tarafa ek set, kalça ve baldır esnekliği"),
        ("walk", "Günlük yaşam", "Günde 7.000+ adım, günde kilo başına 1,2 g protein")]
pl = "".join(f'<li style="--i:{i}"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">{ICO[ic]}</svg><div><b>{t}</b><span>{d}</span></div></li>'
             for i, (ic, t, d) in enumerate(PLAN))
TL = [("Bugün", "Başlangıç"), ("6. hafta", "Kontrol"), ("3. ay", "Yeniden ölçüm"), ("6. ay", "Tam analiz")]
tl = "".join(f'<li style="--i:{i}"><i></i><b>{a}</b><span>{b}</span></li>' for i, (a, b) in enumerate(TL))
LEAF = '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 15V7.2M8 8.4C8 5.6 6.2 3.8 3.4 3.6c.1 2.7 1.9 4.6 4.6 4.8Zm0 0c0-2.8 1.8-4.6 4.6-4.8-.1 2.7-1.9 4.6-4.6 4.8Z" stroke="currentColor" stroke-width="1.1" fill="none" stroke-linecap="round"/></svg>'

ARW_L = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 6-6 6 6 6"/></svg>'
ARW_R = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg>'
PLAY = '<svg class="i-pause" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14M16 5v14" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg><svg class="i-play" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l10.5-6.5z" fill="currentColor"/></svg>'

SLIDES = f'''          <div class="rs" id="rapor" role="region" aria-label="Örnek analiz raporu">
            <div class="rs-top"><span class="rs-tag">Örnek rapor</span><span class="rs-pt">A.Y. · 62 yaş</span><span class="rs-count" aria-hidden="true"><b id="rs-n">1</b> / 7</span></div>
            <div class="rs-prog" aria-hidden="true"><span id="rs-bar"></span></div>
            <div class="rs-stage" id="rs-stage">
          <div class="rs-slide on" data-dur="8000" role="group" aria-label="1 / 7">
            <div class="rs-who"><span class="rs-av" aria-hidden="true">AY</span><p><b>Hedefi:</b> <q>Bu yaz torunlarımla doğa yürüyüşüne çıkmak istiyorum.</q></p></div>
            <p class="rs-k">Fonksiyonel yaş</p>
            <h4>Yaşıtlarından 8 yıl önde</h4>
            {GAUGE}
            <p class="rs-leg"><span class="f">Fonksiyonel yaş 54</span><span class="c">Takvim yaşı 62</span></p>
            <ul class="rs-risk">
              <li class="ok" style="--i:0"><span>Düşme riski</span><b>Düşük</b></li>
              <li class="mid" style="--i:1"><span>Sarkopeni riski</span><b>Orta</b></li>
              <li class="ok" style="--i:2"><span>Kırılganlık</span><b>Düşük</b></li>
            </ul>
          </div>
          <div class="rs-slide" data-dur="7000" role="group" aria-label="2 / 7">
            <p class="rs-k">Yaş normuna göre profil</p>
            <h4>Güçlü yanlar ve gelişim alanları</h4>
            {RADAR}
            <p class="rs-note">Denge ve yürüme hızı çok iyi; bacak gücü ve esneklik programın odağında.</p>
          </div>
          <div class="rs-slide" data-dur="8000" role="group" aria-label="3 / 7">
            <p class="rs-k">Ölçümler</p>
            <h4>Yedi test, tek bakışta</h4>
            {TABLE}
          </div>
          <div class="rs-slide" data-dur="7500" role="group" aria-label="4 / 7">
            <p class="rs-k">Kuvvet asimetrisi</p>
            <h4>Sol ayak bileği ve kalça biraz geride</h4>
            {BFLY}
            <p class="rs-note">Sağ ile sol arasındaki farkın %10’u aşması denge ve hareket kontrolü açısından dikkate alınır; programda sol tarafa ek set eklenir.</p>
          </div>
          <div class="rs-slide" data-dur="7500" role="group" aria-label="5 / 7">
            <p class="rs-k">Vücut kompozisyonu ve performans</p>
            <h4>Kas kütlesini korumak öncelikli</h4>
            {BODY}
          </div>
          <div class="rs-slide" data-dur="7500" role="group" aria-label="6 / 7">
            <p class="rs-k">Zaman içinde izlem</p>
            <h4>Kavrama gücü toparlanıyor, yürüme hızı takipte</h4>
            {LINES}
            <p class="rs-note">Her kontrolde aynı testler tekrarlanır; küçük değişimler erkenden fark edilir.</p>
          </div>
          <div class="rs-slide" data-dur="9000" role="group" aria-label="7 / 7">
            <p class="rs-k">12 haftalık plan</p>
            <h4>Öncelik: bacak gücü ve ayak bileği</h4>
            <ul class="rs-plan">{pl}</ul>
            <ol class="rs-tl">{tl}</ol>
            <p class="rs-goal">{LEAF}<span>Ve en önemlisi: bu yaz torunlarla doğa yürüyüşü.</span></p>
          </div>
            </div>
            <div class="rs-nav">
              <button type="button" class="rs-btn" id="rs-prev" aria-label="Önceki slayt">{ARW_L}</button>
              <div class="rs-dots" id="rs-dots"></div>
              <button type="button" class="rs-btn rs-play" id="rs-play" aria-label="Otomatik oynatma" aria-pressed="true">{PLAY}</button>
              <button type="button" class="rs-btn" id="rs-next" aria-label="Sonraki slayt">{ARW_R}</button>
            </div>
          </div>
          <p>Örnek rapor: A.Y., 62 yaş. Değerlendirmenin sonunda bütün ölçümler, anlaşılır bir raporda sizinle birlikte gözden geçirilir.</p>'''

# eski rapor bloğunu değiştir
i = s.index('          <div class="report">')
j = s.index('Sayfaları büyütmek için dokunun.</p>', i) + len('Sayfaları büyütmek için dokunun.</p>')
s = s[:i] + SLIDES + s[j:]

CSS = r'''  /* analiz raporu: slayt gösterisi */
  .rs{--coral:#dd8a6f;--sage2:#a9bf8c;position:relative;isolation:isolate;overflow:hidden;border-radius:18px;border:1px solid rgba(216,178,94,.38);
    background:radial-gradient(90% 55% at 100% 0%,rgba(226,171,71,.13),transparent 62%),radial-gradient(80% 60% at 0% 100%,rgba(143,164,118,.15),transparent 66%),#192416;
    box-shadow:0 22px 60px rgba(0,0,0,.34),inset 0 1px 0 rgba(255,240,200,.06);container-type:inline-size}
  .rs::before{content:"";position:absolute;left:-50%;top:-50%;width:200%;height:200%;z-index:-1;pointer-events:none;
    background:conic-gradient(from 90deg at 50% 50%,transparent 0deg,rgba(226,171,71,.06) 60deg,transparent 130deg,rgba(143,164,118,.08) 220deg,transparent 300deg);
    animation:rs-aurora 30s linear infinite}
  @keyframes rs-aurora{to{transform:rotate(1turn)}}
  .rs-top{display:flex;align-items:center;gap:10px;padding:14px 18px 0;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:600}
  .rs-tag{color:var(--ground);background:var(--foil);border-radius:999px;padding:3px 10px;letter-spacing:.08em}
  .rs-count{margin-left:auto;font-variant-numeric:tabular-nums;letter-spacing:.04em}
  .rs-count b{color:var(--gold);font-weight:600}
  .rs-prog{height:2px;margin:12px 18px 0;background:rgba(236,229,207,.10);border-radius:2px;overflow:hidden}
  .rs-prog span{display:block;height:100%;transform-origin:0 50%;transform:scaleX(0);background:linear-gradient(90deg,var(--sage),var(--gold));box-shadow:0 0 8px rgba(226,171,71,.8)}
  .rs-stage{display:grid;padding:16px 18px 6px;touch-action:pan-y}
  .rs:not(.js) .rs-stage{gap:34px}
  .rs:not(.js) .rs-nav,.rs:not(.js) .rs-prog,.rs:not(.js) .rs-count{display:none}
  .rs.js .rs-slide{grid-area:1/1;opacity:0;visibility:hidden;transform:translateY(10px) scale(.985);
    transition:opacity .6s ease,transform .8s cubic-bezier(.2,.7,.2,1),visibility 0s linear .6s}
  .rs.js .rs-slide.on{opacity:1;visibility:visible;transform:none;transition:opacity .8s ease .12s,transform 1s cubic-bezier(.2,.7,.2,1) .12s,visibility 0s}
  .rs.js:not(.seen) .rs-slide *,.rs.js:not(.seen) .rs-slide *::before,.rs.js:not(.seen) .rs-slide *::after{animation-play-state:paused!important}
  .rs-slide{min-width:0;display:grid;align-content:start;gap:10px}
  .rs .rs-k{margin:0;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--foil);font-weight:600}
  .rs h4{margin:-4px 0 2px;font-family:var(--display);font-weight:400;font-size:24px;font-size:clamp(21px,5.2cqw,27px);line-height:1.2;color:var(--ink);text-wrap:balance}
  .rs .rs-note{margin:2px 0 0;font-size:14px;color:var(--ink-soft);max-width:54ch}
  .rs-slide.on h4,.rs-slide.on .rs-k{animation:rs-up .8s cubic-bezier(.2,.7,.2,1) both}
  .rs-slide.on h4{animation-delay:.08s}
  @keyframes rs-up{from{opacity:0;transform:translateY(8px)}}
  @keyframes rs-fade{from{opacity:0}}
  @keyframes rs-draw{from{stroke-dashoffset:1}}
  @keyframes rs-pop{from{opacity:0;transform:scale(.3)}}
  @keyframes rs-in{from{opacity:0;transform:translateY(8px)}}
  @keyframes rs-pulse{0%{opacity:.85;transform:scale(1)}100%{opacity:0;transform:scale(2.6)}}
  /* 1: kişi + gösterge */
  .rs-who{display:flex;align-items:center;gap:12px;padding:10px 12px;border:1px solid var(--line);border-radius:14px;background:rgba(236,229,207,.03);margin-bottom:4px}
  .rs-av{flex:none;width:40px;height:40px;border-radius:50%;display:grid;place-items:center;font-family:var(--display);font-size:15px;color:var(--ground);
    background:radial-gradient(circle at 30% 30%,#f3d58d,var(--foil));box-shadow:0 0 0 3px rgba(216,178,94,.18),0 0 18px rgba(226,171,71,.35)}
  .rs .rs-who p{margin:0;font-size:14.5px;color:var(--ink-soft);line-height:1.45}
  .rs-who b{color:var(--ink);font-weight:600}
  .rs-who q{font-style:italic}
  .rs-gauge{display:block;width:100%;max-width:360px;margin:0 auto;overflow:visible}
  .rs-gauge .trk{fill:none;stroke:rgba(236,229,207,.10);stroke-width:14;stroke-linecap:round}
  .rs-gauge .tk line{stroke:rgba(236,229,207,.22);stroke-width:1.2}
  .rs-gauge .arc{fill:none;stroke:url(#rs-gg);stroke-width:14;stroke-linecap:round;stroke-dasharray:1;filter:drop-shadow(0 0 6px rgba(226,171,71,.55))}
  .rs-gauge .gap{fill:none;stroke:var(--sage2);stroke-width:3;stroke-linecap:round;stroke-dasharray:.06 .05;opacity:.9}
  .rs-gauge .t62{stroke:var(--ink-soft);stroke-width:2;stroke-linecap:round}
  .rs-gauge text{font-family:var(--body);text-anchor:middle}
  .rs-gauge .l62{fill:var(--ink-soft);font-size:13px;font-weight:600}
  .rs-gauge .l54{fill:var(--gold);font-size:13px;font-weight:600}
  .rs-gauge .dot{fill:#fff1c9;stroke:var(--gold);stroke-width:3;filter:drop-shadow(0 0 7px rgba(255,210,120,.95))}
  .rs-gauge .ring{fill:none;stroke:var(--gold);stroke-width:1.6;transform-box:fill-box;transform-origin:center;opacity:0}
  .rs-gauge .gl{fill:var(--sage2);font-size:12.5px;font-weight:600}
  .rs-gauge .big{fill:var(--gold);font-family:var(--display);font-size:58px;filter:drop-shadow(0 0 14px rgba(226,171,71,.35))}
  .rs-gauge .sub{fill:var(--muted);font-size:11px;letter-spacing:.16em;text-transform:uppercase;font-weight:600}
  .rs-gauge .sc{fill:var(--muted);font-size:11px}
  .rs-slide.on .rs-gauge .arc{animation:rs-draw 1.6s cubic-bezier(.4,0,.2,1) .25s both}
  .rs-slide.on .rs-gauge .dot,.rs-slide.on .rs-gauge .l54{animation:rs-pop .6s cubic-bezier(.2,.9,.3,1.4) 1.7s both}
  .rs-slide.on .rs-gauge .ring{animation:rs-pulse 2.4s ease-out 2.1s infinite}
  .rs-slide.on .rs-gauge .gap,.rs-slide.on .rs-gauge .gl{animation:rs-fade .8s ease 2s both}
  .rs .rs-leg{margin:-4px 0 0;display:flex;justify-content:center;flex-wrap:wrap;gap:4px 16px;font-size:13px;color:var(--ink-soft)}
  .rs-leg span{display:inline-flex;align-items:center;gap:6px}
  .rs-leg span::before{content:"";width:10px;height:10px;border-radius:50%}
  .rs-leg .f::before{background:var(--gold);box-shadow:0 0 8px rgba(226,171,71,.8)}
  .rs-leg .c::before{background:transparent;border:2px solid var(--ink-soft);width:6px;height:6px}
  .rs-risk{list-style:none;margin:4px 0 0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
  .rs-risk li{display:grid;gap:2px;padding:10px 10px 9px;border-radius:12px;border:1px solid var(--line);background:rgba(236,229,207,.03);text-align:center}
  .rs-risk span{font-size:12px;color:var(--muted);line-height:1.3}
  .rs-risk b{font-size:15px;font-weight:600}
  .rs-risk .ok b{color:var(--sage2)} .rs-risk .mid b{color:var(--gold)}
  .rs-risk .ok{box-shadow:inset 0 -2px 0 rgba(169,191,140,.55)} .rs-risk .mid{box-shadow:inset 0 -2px 0 rgba(226,171,71,.75)}
  .rs-slide.on .rs-risk li{animation:rs-in .6s ease both;animation-delay:calc(2.2s + var(--i)*.15s)}
  /* 2: radar */
  .rs-radar{display:block;width:100%;max-width:380px;margin:0 auto;overflow:visible}
  .rs-radar .grid polygon,.rs-radar .grid line{fill:none;stroke:rgba(236,229,207,.12);stroke-width:1}
  .rs-radar .grid polygon:last-of-type{stroke:rgba(236,229,207,.22)}
  .rs-radar .shape{transform-box:view-box;transform-origin:160px 138px}
  .rs-radar .poly{fill:url(#rs-rf);stroke:var(--gold);stroke-width:2.2;stroke-linejoin:round;filter:drop-shadow(0 0 8px rgba(226,171,71,.5))}
  .rs-radar circle.hi{fill:#fff1c9;stroke:var(--gold);stroke-width:2}
  .rs-radar circle.lo{fill:var(--coral);stroke:#ffd3c2;stroke-width:1.6;filter:drop-shadow(0 0 6px rgba(221,138,111,.9))}
  .rs-radar .pl{fill:none;stroke:var(--coral);stroke-width:1.4;transform-box:fill-box;transform-origin:center;opacity:0}
  .rs-radar text{font-family:var(--body)}
  .rs-radar .nm{fill:var(--ink-soft);font-size:12px}
  .rs-radar .vl{fill:var(--gold);font-size:13px;font-weight:600}
  .rs-radar text.lo{fill:#f0a78e}
  .rs-slide.on .rs-radar .shape{animation:rs-grow 1.5s cubic-bezier(.2,.8,.2,1.08) .2s both}
  @keyframes rs-grow{from{transform:scale(0) rotate(-40deg);opacity:0}}
  .rs-slide.on .rs-radar .lbls text{animation:rs-fade .7s ease 1s both}
  .rs-slide.on .rs-radar .pl{animation:rs-pulse 2.2s ease-out 1.8s infinite}
  /* 3: ölçüm tablosu */
  .rs-tab{list-style:none;margin:0;padding:0;display:grid}
  .rs-tab li{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr) 74px 74px;gap:8px;align-items:center;padding:9px 2px;border-top:1px solid var(--line);font-size:14.5px}
  .rs-tab li.hd{border-top:0;padding-top:0;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:600}
  .rs-tab .n{color:var(--ink);line-height:1.3}
  .rs-tab .v{color:var(--gold);font-variant-numeric:tabular-nums;font-weight:600;white-space:nowrap}
  .rs-tab li.hd .v{color:var(--muted)}
  .rs-tab .st{justify-self:start;font-size:12px;font-weight:600;padding:2px 9px;border-radius:999px;border:1px solid currentColor}
  .rs-tab li.hd .st{border:0;padding:0}
  .rs-tab .st.ok{color:var(--sage2)} .rs-tab .st.mid{color:var(--gold)} .rs-tab .st.low{color:#f0a78e}
  .rs-tab .ch{font-size:13px;color:var(--muted);white-space:nowrap;font-variant-numeric:tabular-nums}
  .rs-tab .ch.ok{color:var(--sage2)} .rs-tab .ch.low{color:#f0a78e} .rs-tab .ch.tg{color:var(--gold)}
  .rs-tab .ch.up::before{content:"▲ ";font-size:9px} .rs-tab .ch.dn::before{content:"▼ ";font-size:9px}
  .rs-tab .ch.tg::before{content:"◎ ";font-size:11px}
  .rs-slide.on .rs-tab li:not(.hd){animation:rs-row .6s cubic-bezier(.2,.7,.2,1) both;animation-delay:calc(.25s + var(--i)*.14s)}
  @keyframes rs-row{from{opacity:0;transform:translateX(-12px)}}
  .rs-slide.on .rs-tab .st{animation:rs-glow 1.2s ease both;animation-delay:calc(.7s + var(--i)*.14s)}
  @keyframes rs-glow{0%{box-shadow:0 0 0 rgba(226,171,71,0)}40%{box-shadow:0 0 14px rgba(226,171,71,.55)}100%{box-shadow:0 0 0 rgba(226,171,71,0)}}
  @container (max-width:420px){.rs-tab li{grid-template-columns:minmax(0,1.35fr) minmax(0,1fr) auto}.rs-tab .ch{display:none}}
  /* 4: kelebek grafik */
  .rs-bf{display:grid;gap:10px}
  .rs-bf-h{display:flex;justify-content:space-between;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:600}
  .rs-bf-h span:nth-child(2){letter-spacing:.04em;text-transform:none;font-weight:400}
  .rs-bf-r{display:grid;grid-template-columns:26px minmax(0,1fr) 2px minmax(0,1fr) 26px;gap:3px 6px;align-items:center}
  .rs-bf-r b{grid-column:1/-1;display:flex;justify-content:space-between;align-items:baseline;gap:8px;font-weight:500;font-size:13.5px;color:var(--ink-soft)}
  .rs-bf-r em{font-style:normal;font-size:11.5px;color:var(--muted);font-variant-numeric:tabular-nums}
  .rs-bf-r .v{font-size:12.5px;color:var(--ink-soft);font-variant-numeric:tabular-nums;text-align:center}
  .rs-bf-r i{display:block;height:9px}
  .rs-bf-r .bl{border-radius:5px 0 0 5px;background:linear-gradient(270deg,#8fa476,#bccda4);transform-origin:100% 50%;transform:scaleX(var(--l))}
  .rs-bf-r .br{border-radius:0 5px 5px 0;background:linear-gradient(90deg,#8fa476,#bccda4);transform-origin:0 50%;transform:scaleX(var(--r))}
  .rs-bf-r .bm{height:16px;background:rgba(236,229,207,.3);border-radius:1px}
  .rs-bf-r.hi .bl{background:linear-gradient(270deg,#c98f3a,#f3c565);box-shadow:0 0 12px rgba(226,171,71,.55)}
  .rs-bf-r.hi .br{background:linear-gradient(90deg,#8fa476,#bccda4)}
  .rs-bf-r.hi b{color:var(--ink)}
  .rs-bf-r.hi em{color:var(--ground);background:var(--gold);padding:1px 8px;border-radius:999px;font-weight:600;box-shadow:0 0 12px rgba(226,171,71,.5)}
  .rs-slide.on .rs-bf-r .bl,.rs-slide.on .rs-bf-r .br{animation:rs-bar 1.1s cubic-bezier(.2,.8,.2,1) both;animation-delay:calc(.25s + var(--i)*.13s)}
  @keyframes rs-bar{from{transform:scaleX(0)}}
  .rs-slide.on .rs-bf-r em{animation:rs-pop .5s cubic-bezier(.2,.9,.3,1.4) both;animation-delay:calc(1.1s + var(--i)*.13s)}
  /* 5: halkalar + SPPB */
  .rs-rings{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px 8px}
  @container (max-width:430px){.rs-rings{grid-template-columns:repeat(2,minmax(0,1fr))}}
  .rs-ring{position:relative;display:grid;justify-items:center;gap:4px;text-align:center}
  .rs-ring .rw{position:relative;display:block;width:100%;max-width:96px}
  .rs-ring svg{width:100%;display:block;transform:rotate(-90deg);overflow:visible}
  .rs-ring .bg{fill:none;stroke:rgba(236,229,207,.10);stroke-width:8}
  .rs-ring .fg{fill:none;stroke-width:8;stroke-linecap:round;stroke-dasharray:var(--p) 100}
  .rs-ring.ok .fg{stroke:var(--sage2);filter:drop-shadow(0 0 5px rgba(169,191,140,.7))}
  .rs-ring.mid .fg{stroke:var(--gold);filter:drop-shadow(0 0 5px rgba(226,171,71,.8))}
  .rs-ring .rv{position:absolute;inset:0;display:grid;place-items:center;font-family:var(--display);font-size:19px;color:var(--ink);white-space:nowrap;line-height:1}
  .rs-ring .rn{font-size:12.5px;color:var(--ink-soft);line-height:1.25}
  .rs-slide.on .rs-ring .fg{animation:rs-ring 1.5s cubic-bezier(.3,.7,.2,1) both;animation-delay:calc(.25s + var(--i)*.15s)}
  @keyframes rs-ring{from{stroke-dasharray:0 100}}
  .rs-sp{margin-top:6px;padding:12px 14px;border:1px solid var(--line);border-radius:14px;background:rgba(236,229,207,.03);display:grid;gap:7px}
  .rs .rs-sp-h{margin:0;display:flex;justify-content:space-between;align-items:baseline;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:600}
  .rs-sp-h b{font-family:var(--display);font-size:22px;letter-spacing:0;color:var(--gold);font-weight:400;text-shadow:0 0 14px rgba(226,171,71,.5)}
  .rs-sp-r{display:grid;grid-template-columns:86px minmax(0,1fr) 34px;gap:10px;align-items:center;font-size:13.5px;color:var(--ink-soft)}
  .rs-sp-r b{font-weight:600;color:var(--ink);text-align:right;font-variant-numeric:tabular-nums}
  .rs-sp-r .bk{display:grid;grid-template-columns:repeat(4,1fr);gap:5px}
  .rs-sp-r i{display:block;height:10px;border-radius:3px;background:rgba(236,229,207,.10)}
  .rs-sp-r i.on{background:linear-gradient(90deg,#8fa476,#c9d9ae);box-shadow:0 0 8px rgba(169,191,140,.55)}
  .rs-slide.on .rs-sp-r i.on{animation:rs-pop .45s cubic-bezier(.2,.9,.3,1.4) both;animation-delay:calc(1s + var(--i)*.09s)}
  /* 6: çizgi grafik */
  .rs-line{display:block;width:100%;max-width:440px;margin:0 auto;overflow:visible}
  .rs-line .vg line{stroke:rgba(236,229,207,.07);stroke-width:1}
  .rs-line text{font-family:var(--body)}
  .rs-line .ttl{fill:var(--ink-soft);font-size:12px;font-weight:600}
  .rs-line .thr{stroke:var(--coral);stroke-width:1.4;stroke-dasharray:4 4;opacity:.8}
  .rs-line .thl{fill:#f0a78e;font-size:10.5px}
  .rs-line .ln{fill:none;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:1}
  .rs-line .ln.a{stroke:var(--gold);filter:drop-shadow(0 0 6px rgba(226,171,71,.7))}
  .rs-line .ln.b{stroke:var(--sage2);filter:drop-shadow(0 0 6px rgba(169,191,140,.7))}
  .rs-line .ar.a{fill:url(#rs-la)} .rs-line .ar.b{fill:url(#rs-lb)}
  .rs-line .pa{fill:#1b2718;stroke:var(--gold);stroke-width:2}
  .rs-line .pb{fill:#1b2718;stroke:var(--sage2);stroke-width:2}
  .rs-line .last{fill:none;stroke-width:1.5;transform-box:fill-box;transform-origin:center;opacity:0}
  .rs-line .last.a{stroke:var(--gold)} .rs-line .last.b{stroke:var(--sage2)}
  .rs-line .lv{font-size:12px;font-weight:600} .rs-line .lv.a{fill:var(--gold)} .rs-line .lv.b{fill:var(--sage2)}
  .rs-line .xl text{fill:var(--muted);font-size:10.5px}
  .rs-slide.on .rs-line .ln{animation:rs-draw 2s cubic-bezier(.4,0,.2,1) .3s both}
  .rs-slide.on .rs-line .ln.b{animation-delay:.6s}
  .rs-slide.on .rs-line .ar{animation:rs-fade 1.2s ease 1.4s both}
  .rs-slide.on .rs-line .pa,.rs-slide.on .rs-line .pb{animation:rs-fade .4s ease both;animation-delay:calc(.35s + var(--i)*.33s)}
  .rs-slide.on .rs-line .pb{animation-delay:calc(.65s + var(--i)*.33s)}
  .rs-slide.on .rs-line .lv{animation:rs-fade .6s ease 2.3s both}
  .rs-slide.on .rs-line .last{animation:rs-pulse 2.4s ease-out 2.4s infinite}
  /* 7: plan */
  .rs-plan{list-style:none;margin:0;padding:0;display:grid;gap:8px}
  .rs-plan li{display:grid;grid-template-columns:36px minmax(0,1fr);gap:12px;align-items:center;padding:9px 12px;border:1px solid var(--line);border-radius:12px;background:rgba(236,229,207,.03)}
  .rs-plan svg{width:36px;height:36px;padding:7px;border-radius:50%;background:rgba(226,171,71,.12);color:var(--gold);fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;box-shadow:0 0 14px rgba(226,171,71,.18)}
  .rs-plan b{display:block;font-weight:600;color:var(--ink);font-size:14.5px}
  .rs-plan span{display:block;font-size:13.5px;color:var(--ink-soft);line-height:1.4}
  .rs-slide.on .rs-plan li{animation:rs-row .6s cubic-bezier(.2,.7,.2,1) both;animation-delay:calc(.25s + var(--i)*.16s)}
  .rs-tl{list-style:none;margin:6px 0 0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));position:relative}
  .rs-tl::before{content:"";position:absolute;left:12.5%;right:12.5%;top:7px;height:2px;background:linear-gradient(90deg,var(--gold),var(--sage));opacity:.55;transform-origin:0 50%}
  .rs-tl li{position:relative;display:grid;justify-items:center;gap:1px;text-align:center}
  .rs-tl i{width:16px;height:16px;border-radius:50%;background:#1b2718;border:2px solid var(--gold);box-shadow:0 0 10px rgba(226,171,71,.6);margin-bottom:5px}
  .rs-tl li:first-child i{background:var(--gold)}
  .rs-tl b{font-size:13px;font-weight:600;color:var(--ink)}
  .rs-tl span{font-size:12px;color:var(--muted);line-height:1.3}
  .rs-slide.on .rs-tl::before{animation:rs-bar 1.4s cubic-bezier(.4,0,.2,1) 1s both}
  .rs-slide.on .rs-tl li{animation:rs-in .6s ease both;animation-delay:calc(1s + var(--i)*.3s)}
  .rs .rs-goal{margin:4px 0 0;display:flex;align-items:center;gap:10px;font-family:var(--display);font-size:18px;line-height:1.35;color:var(--foil)}
  .rs-goal svg{flex:none;width:22px;height:22px;color:var(--gold);filter:drop-shadow(0 0 6px rgba(226,171,71,.7))}
  .rs-slide.on .rs-goal{animation:rs-up .9s cubic-bezier(.2,.7,.2,1) 2.4s both}
  /* alt gezinme */
  .rs-nav{display:flex;align-items:center;gap:8px;padding:8px 12px 14px}
  .rs-dots{display:flex;justify-content:center;align-items:center;margin:0 auto;min-width:0}
  .rs-dot{all:unset;box-sizing:border-box;cursor:pointer;width:22px;height:28px;display:grid;place-items:center}
  .rs-dot::before{content:"";width:7px;height:7px;border-radius:4px;background:rgba(236,229,207,.24);transition:width .45s ease,background .45s ease,box-shadow .45s ease}
  .rs-dot[aria-current="true"]::before{width:20px;background:var(--gold);box-shadow:0 0 10px rgba(226,171,71,.7)}
  .rs-dot:focus-visible{outline:2px solid var(--gold);outline-offset:-2px;border-radius:6px}
  .rs-btn{all:unset;box-sizing:border-box;cursor:pointer;flex:none;width:40px;height:40px;border-radius:50%;display:grid;place-items:center;border:1px solid var(--line);color:var(--ink);transition:border-color .2s,color .2s,background .2s}
  .rs-btn:hover{border-color:var(--line-strong);color:var(--foil)}
  .rs-btn:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .rs-btn svg{width:18px;height:18px}
  .rs-play .i-play{display:none}
  .rs-play[aria-pressed="false"] .i-play{display:block} .rs-play[aria-pressed="false"] .i-pause{display:none}
  @media (prefers-reduced-motion:reduce){.rs::before{animation:none}}
'''
rep("  .report{display:grid;gap:8px}\n  .rp{all:unset;cursor:zoom-in;display:block;border-radius:8px;overflow:hidden;background:#fff;border:1px solid var(--line)}\n  .rp img{display:block;width:100%;height:auto}\n  .rp-row{display:grid;grid-template-columns:1fr 1fr;gap:8px}\n  .rp-row .rp{aspect-ratio:1/1}\n  .rp-row .rp img{height:100%;object-fit:cover;object-position:top}\n  .rp:focus-visible{outline:2px solid var(--gold);outline-offset:2px}\n",
    CSS)
# adımlar: rapor geniş, animasyonlar yanında
rep("  .steps{display:grid;grid-template-columns:1fr 1fr;gap:18px}\n  @media (max-width:620px){.steps{grid-template-columns:1fr}}\n  @media (min-width:1000px){.steps{gap:44px}}",
    "  .steps{display:grid;grid-template-columns:1fr;gap:36px}\n  @media (min-width:1000px){.steps{grid-template-columns:minmax(0,1.12fr) minmax(0,.88fr);gap:44px;align-items:start}}\n  @media (min-width:700px) and (max-width:999px){.steps .rs{max-width:620px}}")

# ışık kutusu artık yok (galeri kareleri zaten açılmıyor)
i = s.index('<div class="lb" id="lb" hidden')
j = s.index('</div>\n\n', s.index('<div class="lb-bar">', i)) + len('</div>\n\n')
s = s[:i] + s[j:]
i = s.index("  /* lightbox */")
j = s.index("  .btn{", i)
s = s[:i] + s[j:]
i = s.index("  var groups = { kare: [], rapor:")
j = s.index("})();\n</script>", i)
s = s[:i] + s[j:]

JS = r'''<script>
(function(){
  var box = document.getElementById('rapor'); if (!box) return;
  box.classList.add('js');
  var slides = [].slice.call(box.querySelectorAll('.rs-slide')), n = slides.length, cur = 0;
  var bar = document.getElementById('rs-bar'), num = document.getElementById('rs-n'), dotsBox = document.getElementById('rs-dots');
  var playBtn = document.getElementById('rs-play');
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var playing = !reduce, hover = false, focusIn = false, visible = false, t0 = 0, elapsed = 0, raf = null;
  playBtn.setAttribute('aria-pressed', playing ? 'true' : 'false');
  var dots = slides.map(function(sl, i){
    var d = document.createElement('button');
    d.type = 'button'; d.className = 'rs-dot';
    var h = sl.querySelector('h4'); d.setAttribute('aria-label', (i + 1) + ' / ' + n + (h ? ' · ' + h.textContent : ''));
    d.onclick = function(){ go(i, true); };
    dotsBox.appendChild(d); return d;
  });
  // sayılar: son değerden geriye, sayarak gelir (metnin kendi biçimi korunur)
  function counters(sl){
    if (reduce) return;
    [].forEach.call(sl.querySelectorAll('[data-count],[data-from]'), function(el){
      var fin = el.getAttribute('data-fin') || el.textContent; el.setAttribute('data-fin', fin);
      var tok = el._rsTok = {};
      var m = fin.match(/^([^\d]*)(\d+(?:[.,]\d+)?)(.*)$/); if (!m) return;
      var dec = (m[2].split(/[.,]/)[1] || '').length, sep = m[2].indexOf(',') >= 0 ? ',' : '.';
      var to = parseFloat(m[2].replace(',', '.')), from = el.hasAttribute('data-from') ? parseFloat(el.getAttribute('data-from')) : 0;
      var st = null, dur = 1500, delay = el.hasAttribute('data-from') ? 350 : 250;
      function step(ts){
        if (el._rsTok !== tok) return;
        if (st === null) st = ts;
        var t = Math.min(1, Math.max(0, (ts - st - delay) / dur)), e = 1 - Math.pow(1 - t, 3);
        el.textContent = m[1] + (from + (to - from) * e).toFixed(dec).replace('.', sep) + m[3];
        if (t < 1 && sl.classList.contains('on')) requestAnimationFrame(step); else el.textContent = fin;
      }
      requestAnimationFrame(step);
    });
  }
  function dur(){ return +slides[cur].getAttribute('data-dur') || 7000; }
  function go(i, user){
    var prev = cur; cur = (i + n) % n;
    if (prev !== cur) slides[prev].classList.remove('on');
    slides.forEach(function(sl, k){ sl.setAttribute('aria-hidden', k === cur ? 'false' : 'true'); if ('inert' in sl) sl.inert = k !== cur; });
    // aynı slayta dönülse de animasyonlar baştan oynasın
    slides[cur].classList.remove('on'); void slides[cur].offsetWidth; slides[cur].classList.add('on');
    dots.forEach(function(d, k){ d.setAttribute('aria-current', k === cur ? 'true' : 'false'); });
    num.textContent = cur + 1;
    elapsed = 0; t0 = performance.now(); paint(0);
    if (box.classList.contains('seen')) counters(slides[cur]);
  }
  function paint(p){ bar.style.transform = 'scaleX(' + p.toFixed(4) + ')'; }
  function running(){ return playing && visible && !hover && !focusIn && !document.hidden; }
  function tick(ts){
    raf = null;
    if (!running()) return;
    elapsed += ts - t0; t0 = ts;
    var p = Math.min(1, elapsed / dur()); paint(p);
    if (p >= 1) { go(cur + 1); }
    raf = requestAnimationFrame(tick);
  }
  function kick(){ if (running() && !raf) { t0 = performance.now(); raf = requestAnimationFrame(tick); } }
  document.getElementById('rs-prev').onclick = function(){ go(cur - 1, true); };
  document.getElementById('rs-next').onclick = function(){ go(cur + 1, true); };
  playBtn.onclick = function(){ playing = !playing; playBtn.setAttribute('aria-pressed', playing ? 'true' : 'false'); if (playing && elapsed >= dur()) go(cur + 1); kick(); };
  box.addEventListener('mouseenter', function(){ hover = true; });
  box.addEventListener('mouseleave', function(){ hover = false; kick(); });
  box.addEventListener('focusin', function(e){ if (e.target.matches && e.target.matches(':focus-visible')) focusIn = true; });
  box.addEventListener('focusout', function(){ focusIn = false; kick(); });
  box.addEventListener('keydown', function(e){
    if (e.key === 'ArrowRight') { e.preventDefault(); go(cur + 1, true); }
    else if (e.key === 'ArrowLeft') { e.preventDefault(); go(cur - 1, true); }
  });
  document.addEventListener('visibilitychange', kick);
  // kaydırma (dokunmatik)
  var sx = null, sy = null, stage = document.getElementById('rs-stage');
  stage.addEventListener('touchstart', function(e){ sx = e.touches[0].clientX; sy = e.touches[0].clientY; }, {passive: true});
  stage.addEventListener('touchend', function(e){
    if (sx === null) return;
    var dx = e.changedTouches[0].clientX - sx, dy = e.changedTouches[0].clientY - sy; sx = null;
    if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy) * 1.3) go(dx < 0 ? cur + 1 : cur - 1, true);
  }, {passive: true});
  go(0);
  function show(){ if (!box.classList.contains('seen')) { box.classList.add('seen'); go(cur); } }
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function(es){
      visible = es[0].isIntersecting;
      if (visible) { show(); kick(); }
    }, {threshold: .35}).observe(box);
  } else { visible = true; show(); kick(); }
})();
</script>
'''
anchor = "<script>\n(function(){\n  var sec = document.getElementById('logo'); if (!sec) return;"
assert s.count(anchor) == 1
s = s.replace(anchor, JS + anchor, 1)
open(p, "w", encoding="utf-8").write(s)
print("ok", len(s))

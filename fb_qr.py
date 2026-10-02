# -*- coding: utf-8 -*-
# İletişim karekodu: "sinir ağı" karekod. Modüller birbirine akson gibi bağlanan nöronlar;
# ortada beyin logosu. Görününce sinyal beyinden dışa doğru halka halka yayılarak kodu
# kurar, sonra ara ara altın bir dalga beyinden kenarlara akar. Kod her an okunabilir kalır.
import math, qrcode

p = "site/index.html"
s = open(p, encoding="utf-8").read()


def rep(old, new, cnt=1):
    global s
    assert s.count(old) == cnt, (old[:80], s.count(old))
    s = s.replace(old, new)


import os
URL = os.environ.get("QDATA", "https://wa.me/905538815568")
qr = qrcode.QRCode(error_correction=getattr(qrcode.constants, 'ERROR_CORRECT_' + os.environ.get('QEC', 'M')), border=0)
qr.add_data(URL); qr.make(fit=True)
M = qr.get_matrix(); n = len(M)
Q = 3.4                      # sessiz alan (modül)
N = n + 2 * Q
C = (n - 1) / 2              # merkez modül
CLR = int(os.environ.get('QCLR', 5))    # ortadaki logo alanı (modül)
c0 = (n - CLR) // 2


def finder(x, y):
    return (x < 7 and y < 7) or (x >= n - 7 and y < 7) or (x < 7 and y >= n - 7)


def clear(x, y):
    return c0 <= x < c0 + CLR and c0 <= y < c0 + CLR


def on(x, y):
    return 0 <= x < n and 0 <= y < n and M[y][x] and not finder(x, y) and not clear(x, y)


def f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


R = 0.46      # nöron yarı boyu
RR = 0.36     # köşe yuvarlaklığı
NR = 0.17     # altın çekirdek (sinaps ışığı) yarıçapı
RING = 1.7    # halka kalınlığı (modül)
rings = {}
for y in range(n):
    for x in range(n):
        if not on(x, y):
            continue
        cx, cy = x + Q + .5, y + Q + .5
        k = int(math.hypot(x - C, y - C) / RING)
        g = rings.setdefault(k, {"d": [], "l": [], "n": []})
        h, r = R, RR   # yumuşak köşeli nöron (daire kadar yumuşak, kare kadar okunaklı)
        g["d"].append(f"M{f(cx - h + r)} {f(cy - h)}h{f(2 * (h - r))}a{r} {r} 0 0 1 {r} {r}v{f(2 * (h - r))}a{r} {r} 0 0 1 -{r} {r}"
                      f"h{f(-2 * (h - r))}a{r} {r} 0 0 1 -{r} -{r}v{f(-2 * (h - r))}a{r} {r} 0 0 1 {r} -{r}z")
        if on(x + 1, y):
            g["l"].append(f"M{f(cx)} {f(cy)}h1")
        if on(x, y + 1):
            g["l"].append(f"M{f(cx)} {f(cy)}v1")
parts = []
for k in sorted(rings):
    g = rings[k]
    parts.append(f'<path class="nq-r" style="--r:{k}" d="{"".join(g["d"])}{"".join(g["l"])}"/>')


# kıvılcımlar: dört komşu hücrenin de açık olduğu köşe noktaları
def light(x, y):
    return 0 <= x < n and 0 <= y < n and not M[y][x] and not finder(x, y) and not clear(x, y)
import random
random.seed(11)
cand = [(x, y) for y in range(1, n) for x in range(1, n)
        if light(x - 1, y - 1) and light(x, y - 1) and light(x - 1, y) and light(x, y)]
random.shuffle(cand)
sparks, used = [], []
for (x, y) in cand:
    if all(abs(x - a) + abs(y - b) > 4 for a, b in used):
        used.append((x, y))
    if len(used) >= 20:
        break
for (x, y) in used:
    k = int(math.hypot(x - .5 - C, y - .5 - C) / RING)
    px, py = x + Q, y + Q
    a, c = .95, .1
    sparks.append(f'<path class="nq-sp" style="--r:{k}" d="M{f(px)} {f(py - a)}Q{f(px + c)} {f(py - c)} {f(px + a)} {f(py)}Q{f(px + c)} {f(py + c)} {f(px)} {f(py + a)}Q{f(px - c)} {f(py + c)} {f(px - a)} {f(py)}Q{f(px - c)} {f(py - c)} {f(px)} {f(py - a)}z"/>')

eyes = []
for fx, fy in ((0, 0), (n - 7, 0), (0, n - 7)):
    ox, oy = fx + Q, fy + Q
    eyes.append(f'<rect x="{f(ox + .5)}" y="{f(oy + .5)}" width="6" height="6" rx="1.5" fill="none" stroke-width="1"/>'
                f'<rect class="nq-pu" x="{f(ox + 2)}" y="{f(oy + 2)}" width="3" height="3" rx=".8"/>')

L0 = c0 + Q               # logo alanı başlangıcı
LW = CLR
cxm = Q + n / 2
SVG = f'''<svg class="nq" viewBox="0 0 {f(N)} {f(N)}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="WhatsApp karekodu">
              <defs>
                <radialGradient id="nq-pl" cx="50%" cy="45%" r="75%"><stop offset="0" stop-color="#fbf5e3"/><stop offset=".75" stop-color="#f4ecd4"/><stop offset="1" stop-color="#ebdfba"/></radialGradient>
                <linearGradient id="nq-sh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
                <clipPath id="nq-cl"><rect width="{f(N)}" height="{f(N)}" rx="3.2"/></clipPath>
                <radialGradient id="nq-lg"><stop offset=".42" stop-color="#f3c35c" stop-opacity="0"/><stop offset=".62" stop-color="#f0b845" stop-opacity=".8"/><stop offset=".7" stop-color="#f7d68a" stop-opacity=".35"/><stop offset=".86" stop-color="#fff4cf" stop-opacity="0"/></radialGradient>
              </defs>
              <rect class="nq-pl" width="{f(N)}" height="{f(N)}" rx="3.2" fill="url(#nq-pl)"/>
              <g clip-path="url(#nq-cl)"><circle class="nq-lt" cx="{f(cxm)}" cy="{f(cxm)}" r="{f(N * .72)}" fill="url(#nq-lg)"/><rect class="nq-shine" x="-9" y="-4" width="7" height="{f(N + 8)}" fill="url(#nq-sh)" transform="skewX(-18)"/></g>
              <g class="nq-ns">{"".join(parts)}</g>
              <g class="nq-sps">{"".join(sparks)}</g>
              <g class="nq-eye">{"".join(eyes)}</g>
              <circle class="nq-core" cx="{f(cxm)}" cy="{f(cxm)}" r="{f(LW / 2 - .3)}"/>
              <image class="nq-logo" href="img/logo-mark.svg" x="{f(L0 + .55)}" y="{f(L0 + .85)}" width="{f(LW - 1.1)}" height="{f((LW - 1.1) * 448 / 543)}"/>
            </svg>'''

# eski karekodu değiştir
i = s.index('<div class="code" aria-label="WhatsApp karekodu">')
j = s.index('</div>', i) + len('</div>')
s = s[:i] + f'<a class="code" href="https://wa.me/905538815568" target="_blank" rel="noopener" aria-label="WhatsApp’tan yazın (yeni sekmede açılır)">{SVG}</a>' + s[j:]
rep('<figure class="qr">', '<figure class="qr" id="nq">')

CSS = r'''  /* sinir ağı karekod */
  .qr .code{position:relative;display:block;width:220px;height:220px;padding:0;background:none;border-radius:18px;isolation:isolate;
    box-shadow:0 0 0 1px rgba(216,178,94,.55),0 14px 40px rgba(0,0,0,.4),0 0 44px rgba(226,171,71,.22);transition:transform .35s cubic-bezier(.2,.8,.2,1.2),box-shadow .35s}
  .qr .code:hover{transform:translateY(-3px) scale(1.02);box-shadow:0 0 0 1px rgba(216,178,94,.8),0 18px 46px rgba(0,0,0,.45),0 0 60px rgba(226,171,71,.38)}
  .qr .code::before{content:"";position:absolute;inset:-7px;z-index:-1;border-radius:24px;padding:2px;
    background:conic-gradient(from var(--nqa,0deg),transparent 0 12%,rgba(255,215,130,.95) 20%,transparent 30% 55%,rgba(169,191,140,.8) 65%,transparent 75%);
    -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;filter:blur(1.5px);animation:nq-spin 9s linear infinite}
  .qr .code::after{content:"";position:absolute;inset:-26px;z-index:-2;border-radius:50%;background:radial-gradient(closest-side,rgba(226,171,71,.20),transparent);animation:aura 6s ease-in-out infinite}
  @property --nqa{syntax:"<angle>";inherits:false;initial-value:0deg}
  @keyframes nq-spin{to{--nqa:360deg}}
  .nq{display:block;width:100%;height:100%;border-radius:18px;overflow:hidden}
  .nq .nq-r{fill:#101a13;stroke:#101a13;stroke-width:.5;stroke-linecap:round}
  .nq .nq-eye rect{stroke:#101a13} .nq .nq-eye .nq-pu{fill:#101a13}
  .nq .nq-core{fill:#fbf5e3;stroke:rgba(200,150,62,.55);stroke-width:.18}
  .nq .nq-sp{fill:#fffaf0;stroke:#e9b54f;stroke-width:.09;opacity:0;transform-box:fill-box;transform-origin:center;filter:drop-shadow(0 0 2px rgba(240,184,69,.95))}
  .nq .nq-lt{opacity:0;transform-box:fill-box;transform-origin:center}
  .nq .nq-shine{opacity:1}
  .nq .nq-logo{transform-box:fill-box;transform-origin:center}
  /* 1) görününce: sinyal beyinden dışa halka halka yayılır, ağ kurulur */
  #nq.js:not(.go) .nq-r,#nq.js:not(.go) .nq-eye{opacity:0}
  #nq.go .nq-logo{animation:nq-beat 1s cubic-bezier(.2,.8,.2,1.3) both}
  #nq.go .nq-r{animation:nq-fire .9s ease-out both;animation-delay:calc(.35s + var(--r)*70ms)}
  #nq.go .nq-eye{animation:nq-fire .9s ease-out 1.1s both}
  /* 2) döngü: beyin atar, ışık halkası ağın altından yayılır, nöron çekirdekleri sırayla ateşlenir */
  #nq.lp .nq-logo{animation:nq-pulse 6s ease-in-out var(--lb,2.2s) infinite}
  #nq.lp .nq-lt{animation:nq-lt 6s cubic-bezier(.25,.6,.35,1) var(--lb,2.2s) infinite}
  #nq.lp .nq-sp{animation:nq-spark 6s ease-out infinite;animation-delay:calc(var(--lb,2.2s) + .1s + var(--r)*150ms)}
  #nq.lp .nq-shine{animation:nq-shine 6s ease-in-out var(--lb,2.2s) infinite}
  @keyframes nq-beat{0%{opacity:0;transform:scale(.6)}60%{opacity:1;transform:scale(1.12)}100%{transform:none}}
  @keyframes nq-fire{0%{opacity:0;fill:#ffe3a3;stroke:#ffe3a3}35%{opacity:1;fill:#e2ab47;stroke:#e2ab47}100%{opacity:1}}
  @keyframes nq-in{from{opacity:0}}
  @keyframes nq-pulse{0%,14%,100%{transform:none}5%{transform:scale(1.1)}}
  @keyframes nq-lt{0%{opacity:0;transform:scale(.12)}4%{opacity:1}30%{opacity:.9}40%{opacity:0;transform:scale(1.15)}100%{opacity:0;transform:scale(1.15)}}
  @keyframes nq-spark{0%{opacity:0;transform:scale(.2) rotate(0)}5%{opacity:1;transform:scale(1.2) rotate(45deg)}15%,100%{opacity:0;transform:scale(.3) rotate(90deg)}}
  @keyframes nq-shine{0%,48%{transform:skewX(-18deg) translateX(0)}70%,100%{transform:skewX(-18deg) translateX(56px)}}
  @media (prefers-reduced-motion:reduce){.qr .code::before,.qr .code::after{animation:none}}
'''
rep("  footer{border-top:1px solid var(--line);padding-block:28px 36px;", CSS + "  footer{border-top:1px solid var(--line);padding-block:28px 36px;")
rep("  .qr .code{width:150px;height:150px;background:var(--paper);color:#1c2819;border-radius:10px;padding:12px}\n  .qr .code svg{width:100%;height:100%;display:block}\n", "")

JS = r'''<script>
(function(){
  var fig = document.getElementById('nq'); if (!fig) return;
  fig.classList.add('js');
  var last = 0;
  function go(){ fig.classList.add('go', 'lp'); }
  fig.querySelector('.code').addEventListener('mouseenter', function(){
    if (!fig.classList.contains('go') || Date.now() - last < 2000) return; last = Date.now();
    fig.style.setProperty('--lb', '0s'); fig.classList.remove('lp'); void fig.offsetWidth; fig.classList.add('lp');
  });
  if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) { go(); return; }
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(es){ if (es[0].isIntersecting) { io.disconnect(); go(); } }, {threshold: .5});
    io.observe(fig);
  } else go();
})();
</script>
'''
anchor = "<script>\n(function(){\n  var sec = document.getElementById('logo'); if (!sec) return;"
assert s.count(anchor) == 1
s = s.replace(anchor, JS + anchor, 1)
open(p, "w", encoding="utf-8").write(s)
print("ok", n, len(SVG))

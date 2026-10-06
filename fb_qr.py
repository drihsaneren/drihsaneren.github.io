# -*- coding: utf-8 -*-
# İletişim karekodu (kullanıcının gönderdiği tasarıma göre): koyu yeşil zemin, kum rengi kabartma
# kareler, ortada logo. Görününce halkalar bir iris gibi dönerek yerine oturur; sonra ara ara altın
# bir dalga beyinden kenarlara akar. İmleçle eğilir, ışık imleci izler. Kurulduktan sonra kod hep okunur
# (yalnızca renk açılır; biçim ve yer değişmez).
import math, qrcode

p = "site/index.html"
s = open(p, encoding="utf-8").read()


def rep(old, new, cnt=1):
    global s
    assert s.count(old) == cnt, (old[:80], s.count(old))
    s = s.replace(old, new)


import os
URL = os.environ.get("QDATA", "https://wa.me/905538815568")
qr = qrcode.QRCode(error_correction=getattr(qrcode.constants, 'ERROR_CORRECT_' + os.environ.get('QEC', 'Q')), border=0)
qr.add_data(URL); qr.make(fit=True)
M = qr.get_matrix(); n = len(M)
Q = 3.4                      # sessiz alan (modül)
N = n + 2 * Q
C = (n - 1) / 2              # merkez modül
CLR = int(os.environ.get('QCLR', 9))    # ortadaki logo alanı: genişlik (modül); yükseklik 2 modül az (logo yatay)
CLRH = CLR - 2
c0 = (n - CLR) // 2
c0y = (n - CLRH) // 2


def finder(x, y):
    return (x < 7 and y < 7) or (x >= n - 7 and y < 7) or (x < 7 and y >= n - 7)


def clear(x, y):
    return c0 <= x < c0 + CLR and c0y <= y < c0y + CLRH


def on(x, y):
    return 0 <= x < n and 0 <= y < n and M[y][x] and not finder(x, y) and not clear(x, y)


def f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


R = 0.435     # kare yarı boyu (aralarında ince boşluk)
RR = 0.13     # köşe yuvarlaklığı
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
parts = []
for k in sorted(rings):
    g = rings[k]
    parts.append(f'<path class="nq-r" style="--r:{k};--a:{(-1 if k % 2 else 1) * (38 + 11 * k)}deg" d="{"".join(g["d"])}"/>')


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

def rr(x, y, w, r):      # yuvarlak köşeli kare yolu
    return (f"M{f(x + r)} {f(y)}h{f(w - 2 * r)}a{r} {r} 0 0 1 {r} {r}v{f(w - 2 * r)}a{r} {r} 0 0 1 -{r} {r}"
            f"h{f(2 * r - w)}a{r} {r} 0 0 1 -{r} -{r}v{f(2 * r - w)}a{r} {r} 0 0 1 {r} -{r}z")


eyes = []
for fx, fy in ((0, 0), (n - 7, 0), (0, n - 7)):
    ox, oy = fx + Q, fy + Q
    eyes.append(f'<g class="nq-e" style="--e:{len(eyes)}"><path fill-rule="evenodd" d="{rr(ox + .06, oy + .06, 6.88, .62)}{rr(ox + 1.06, oy + 1.06, 4.88, .3)}"/>'
                f'<rect class="nq-pu" x="{f(ox + 2.06)}" y="{f(oy + 2.06)}" width="2.88" height="2.88" rx=".34"/></g>')

L0 = c0 + Q               # logo alanı başlangıcı
LW = CLR
cxm = Q + n / 2
SVG = f'''<svg class="nq" viewBox="0 0 {f(N)} {f(N)}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="WhatsApp karekodu" style="--c:{f(cxm)}px">
              <defs>
                <radialGradient id="nq-pl" cx="50%" cy="46%" r="72%"><stop offset="0" stop-color="#2f4322"/><stop offset=".6" stop-color="#27381c"/><stop offset="1" stop-color="#1f2d17"/></radialGradient>
                <linearGradient id="nq-sh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff6d8" stop-opacity="0"/><stop offset=".5" stop-color="#fff6d8" stop-opacity=".22"/><stop offset="1" stop-color="#fff6d8" stop-opacity="0"/></linearGradient>
                <clipPath id="nq-cl"><rect width="{f(N)}" height="{f(N)}" rx="3.2"/></clipPath>
                <radialGradient id="nq-lg"><stop offset=".42" stop-color="#f3c35c" stop-opacity="0"/><stop offset=".62" stop-color="#f0b845" stop-opacity=".3"/><stop offset=".7" stop-color="#f7d68a" stop-opacity=".14"/><stop offset=".86" stop-color="#fff4cf" stop-opacity="0"/></radialGradient>
                <radialGradient id="nq-co"><stop offset="0" stop-color="#e2ab47" stop-opacity=".2"/><stop offset=".6" stop-color="#a9bf8c" stop-opacity=".07"/><stop offset="1" stop-color="#a9bf8c" stop-opacity="0"/></radialGradient>
                <radialGradient id="nq-gg"><stop offset="0" stop-color="#fff3c9" stop-opacity=".2"/><stop offset=".5" stop-color="#e9d9a0" stop-opacity=".07"/><stop offset="1" stop-color="#e9d9a0" stop-opacity="0"/></radialGradient>
                <filter id="nq-em" x="-4%" y="-4%" width="108%" height="108%"><feDropShadow dx=".05" dy=".09" stdDeviation=".05" flood-color="#060b04" flood-opacity=".85"/></filter>
              </defs>
              <rect class="nq-pl" width="{f(N)}" height="{f(N)}" rx="3.2" fill="url(#nq-pl)"/>
              <g clip-path="url(#nq-cl)"><circle class="nq-lt" cx="{f(cxm)}" cy="{f(cxm)}" r="{f(N * .72)}" fill="url(#nq-lg)"/><circle class="nq-gl" cx="{f(cxm)}" cy="{f(cxm)}" r="{f(N * .42)}" fill="url(#nq-gg)"/><rect class="nq-shine" x="-9" y="-4" width="7" height="{f(N + 8)}" fill="url(#nq-sh)" transform="skewX(-18)"/></g>
              <circle class="nq-core" cx="{f(cxm)}" cy="{f(cxm)}" r="{f(LW / 2 + .5)}" fill="url(#nq-co)"/>
              <g class="nq-ns" filter="url(#nq-em)">{"".join(parts)}</g>
              <g class="nq-sps">{"".join(sparks)}</g>
              <g class="nq-eye" filter="url(#nq-em)">{"".join(eyes)}</g>
              <image class="nq-logo" href="img/logo-mark.svg" x="{f(L0 + .45)}" y="{f(cxm - (LW - .9) * 448 / 543 / 2)}" width="{f(LW - .9)}" height="{f((LW - .9) * 448 / 543)}"/>
            </svg>'''

# eski karekodu değiştir
i = s.index('<div class="code" aria-label="WhatsApp karekodu">')
j = s.index('</div>', i) + len('</div>')
s = s[:i] + f'<a class="code" href="https://wa.me/905538815568" target="_blank" rel="noopener" aria-label="WhatsApp’tan yazın (yeni sekmede açılır)">{SVG}</a>' + s[j:]
rep('<figure class="qr">', '<figure class="qr" id="nq">')

CSS = r'''  /* karekod: koyu yeşil zemin, kum rengi kabartma kareler */
  .qr{perspective:800px}
  .qr .code{position:relative;display:block;width:232px;height:232px;padding:0;background:none;border-radius:18px;isolation:isolate;
    transform:rotateX(var(--tx,0deg)) rotateY(var(--ty,0deg)) translateY(var(--up,0px)) scale(var(--sc,1));
    box-shadow:0 0 0 1px rgba(216,178,94,.42),0 14px 40px rgba(0,0,0,.45),0 0 44px rgba(226,171,71,.14);transition:transform .5s cubic-bezier(.2,.8,.2,1),box-shadow .35s}
  .qr .code:hover{--up:-4px;--sc:1.025;transition:transform .12s linear,box-shadow .35s;box-shadow:0 0 0 1px rgba(216,178,94,.75),0 22px 50px rgba(0,0,0,.5),0 0 64px rgba(226,171,71,.3)}
  .qr .code::before{content:"";position:absolute;inset:-7px;z-index:-1;border-radius:24px;padding:2px;
    background:conic-gradient(from var(--nqa,0deg),transparent 0 12%,rgba(255,215,130,.9) 20%,transparent 30% 55%,rgba(201,201,144,.75) 65%,transparent 75%);
    -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;filter:blur(1.5px);animation:nq-spin 9s linear infinite}
  .qr .code::after{content:"";position:absolute;inset:-26px;z-index:-2;border-radius:50%;background:radial-gradient(closest-side,rgba(201,201,144,.13),transparent);animation:aura 6s ease-in-out infinite}
  @property --nqa{syntax:"<angle>";inherits:false;initial-value:0deg}
  @keyframes nq-spin{to{--nqa:360deg}}
  .nq{display:block;width:100%;height:100%;overflow:visible}   /* köşeleri SVG içindeki zemin yuvarlar; overflow:hidden eğilirken bulanıklaştırıyordu */
  .nq .nq-r{fill:#c9c990;transform-origin:var(--c) var(--c)}
  .nq .nq-e{transform-box:fill-box;transform-origin:center}
  .nq .nq-e path,.nq .nq-e rect{fill:#c9c990}
  .nq .nq-sp{fill:#fff6d6;stroke:#e9b54f;stroke-width:.09;opacity:0;transform-box:fill-box;transform-origin:center;filter:drop-shadow(0 0 2px rgba(240,184,69,.95))}
  .nq .nq-lt{opacity:0;transform-box:fill-box;transform-origin:center}
  .nq .nq-gl{opacity:0;transition:opacity .4s}
  .qr .code:hover .nq-gl{opacity:1}
  .nq .nq-logo{transform-box:fill-box;transform-origin:center;filter:drop-shadow(0 .5px .6px rgba(0,0,0,.55))}
  /* 1) görününce: halkalar bir iris gibi dönerek yerine oturur, köşe gözleri sırayla düşer */
  #nq.js:not(.go) .nq-r,#nq.js:not(.go) .nq-e,#nq.js:not(.go) .nq-logo{opacity:0}
  #nq.go .nq-logo{animation:nq-beat 1.1s cubic-bezier(.2,.8,.2,1.3) both}
  #nq.go .nq-r{animation:nq-iris 1.5s cubic-bezier(.16,.84,.24,1) both;animation-delay:calc(.3s + var(--r)*80ms)}
  #nq.go .nq-e{animation:nq-drop .7s cubic-bezier(.2,.9,.3,1.25) both;animation-delay:calc(1.25s + var(--e)*.14s)}
  /* 2) döngü: beyin atar, altın dalga halka halka dışa akar (yalnızca renk açılır; kod okunur kalır) */
  #nq.lp .nq-logo{animation:nq-pulse 7s ease-in-out var(--lb,3.2s) infinite}
  #nq.lp .nq-r{animation:nq-wave 7s ease-in-out infinite;animation-delay:calc(var(--lb,3.2s) + var(--r)*120ms)}
  #nq.lp .nq-e{animation:none}
  #nq.lp .nq-e>*{animation:nq-wink 7s ease-in-out infinite;animation-delay:calc(var(--lb,3.2s) + 1.25s + var(--e)*.12s)}
  #nq.lp .nq-lt{animation:nq-lt 7s cubic-bezier(.25,.6,.35,1) var(--lb,3.2s) infinite}
  #nq.lp .nq-sp{animation:nq-spark 7s ease-out infinite;animation-delay:calc(var(--lb,3.2s) + .1s + var(--r)*150ms)}
  #nq.lp .nq-shine{animation:nq-shine 7s ease-in-out var(--lb,3.2s) infinite}
  @keyframes nq-beat{0%{opacity:0;transform:scale(.5) rotate(-12deg)}60%{opacity:1;transform:scale(1.12)}100%{opacity:1;transform:none}}
  @keyframes nq-iris{0%{opacity:0;transform:rotate(var(--a)) scale(.45);fill:#fff0c2}45%{opacity:1;fill:#e9b54f}100%{opacity:1;transform:none;fill:#c9c990}}
  @keyframes nq-drop{0%{opacity:0;transform:scale(1.7) rotate(18deg)}100%{opacity:1;transform:none}}
  @keyframes nq-wave{0%,22%,100%{fill:#c9c990}7%{fill:#f6d98f}}
  @keyframes nq-wink{0%,22%,100%{fill:#c9c990}8%{fill:#f3cf7a}}
  @keyframes nq-pulse{0%,14%,100%{transform:none}5%{transform:scale(1.1)}}
  @keyframes nq-lt{0%{opacity:0;transform:scale(.12)}4%{opacity:1}30%{opacity:.9}40%{opacity:0;transform:scale(1.15)}100%{opacity:0;transform:scale(1.15)}}
  @keyframes nq-spark{0%{opacity:0;transform:scale(.2) rotate(0)}5%{opacity:1;transform:scale(1.2) rotate(45deg)}15%,100%{opacity:0;transform:scale(.3) rotate(90deg)}}
  @keyframes nq-shine{0%,48%{transform:skewX(-18deg) translateX(0)}70%,100%{transform:skewX(-18deg) translateX(56px)}}
  @media (prefers-reduced-motion:reduce){.qr .code::before,.qr .code::after,#nq .nq-r,#nq .nq-e,#nq .nq-e>*,#nq .nq-logo,#nq .nq-lt,#nq .nq-sp,#nq .nq-shine{animation:none!important}.qr .code{transform:none}}
'''
rep("  footer{border-top:1px solid var(--line);padding-block:28px 36px;", CSS + "  footer{border-top:1px solid var(--line);padding-block:28px 36px;")
rep("  .qr .code{width:150px;height:150px;background:var(--paper);color:#1c2819;border-radius:10px;padding:12px}\n  .qr .code svg{width:100%;height:100%;display:block}\n", "")

JS = r'''<script>
(function(){
  var fig = document.getElementById('nq'); if (!fig) return;
  fig.classList.add('js');
  var code = fig.querySelector('.code'), gl = fig.querySelector('.nq-gl'), vb = fig.querySelector('.nq').viewBox.baseVal;
  var last = 0, still = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function go(){ fig.classList.add('go'); setTimeout(function(){ fig.classList.add('lp'); }, still ? 0 : 2600); }
  // imleç üstündeyken: dalga hemen başlar, kart imlece doğru eğilir, ışık imleci izler
  code.addEventListener('mouseenter', function(){
    if (!fig.classList.contains('lp') || Date.now() - last < 2000) return; last = Date.now();
    fig.style.setProperty('--lb', '0s'); fig.classList.remove('lp'); void fig.offsetWidth; fig.classList.add('lp');
  });
  if (!still) {
    code.addEventListener('pointermove', function(e){
      if (e.pointerType && e.pointerType !== 'mouse') return;
      var r = code.getBoundingClientRect(), x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
      code.style.setProperty('--ty', ((x - .5) * 14).toFixed(2) + 'deg');
      code.style.setProperty('--tx', ((.5 - y) * 14).toFixed(2) + 'deg');
      if (gl) { gl.setAttribute('cx', (x * vb.width).toFixed(2)); gl.setAttribute('cy', (y * vb.height).toFixed(2)); }
    });
    code.addEventListener('pointerleave', function(){ code.style.removeProperty('--tx'); code.style.removeProperty('--ty'); });
  }
  if (still) { go(); return; }
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

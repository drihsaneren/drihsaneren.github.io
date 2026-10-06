# -*- coding: utf-8 -*-
# Yüz: "Ben kimim" bölümünde kameraya bakan portre ana görsel olur, beyaz önlüklü iş başı karesi küçük
# bir ek olarak köşesine oturur. İletişim yazısının altında mektup imzası gibi küçük bir yüz + ad.
# Girişte (hero) yüz yok: site kişiyi değil işi öne çıkarır; yüz, güvenin gerektiği iki yerde durur.
p = "site/index.html"
s = open(p, encoding="utf-8").read()


def rep(old, new, cnt=1):
    global s
    assert s.count(old) == cnt, (old[:80], s.count(old))
    s = s.replace(old, new)


rep('<figure class="portrait"><img src="img/portre.jpg" alt="İhsan Eren, beyaz önlükle" loading="lazy"></figure>',
    '<div class="pt"><figure class="portrait"><img src="img/portre2.jpg?v=3" alt="İhsan Eren" width="720" height="720" loading="lazy"></figure>'
    '</div>')
rep('          <div class="contact-btns">',
    '          <div class="sig"><img src="img/portre2_s.jpg?v=3" alt="" width="192" height="192" loading="lazy"><div><p class="sig-n">İhsan Eren</p><p class="sig-r">Fizyoterapist · İntörn Tıp Doktoru</p></div></div>\n'
    '          <div class="contact-btns">')
# giriş: logo tek başına kalır; düğmelerin altında ortada küçük bir "kimlik kartı" (yüz + ad), dokununca "Ben kimim"e iner
rep('      <a class="cta ghost" href="#tanisma">Ücretsiz ön görüşme</a>\n    </div>\n',
    '      <a class="cta ghost" href="#tanisma">Ücretsiz ön görüşme</a>\n    </div>\n'
    '    <a class="hero-me" href="#ben-kimim"><img src="img/portre2_m.jpg?v=3" alt="" width="400" height="400"><span><small>Ben kimim</small><b>İhsan Eren</b></span></a>\n')
CSS = '''  /* yüz: ana portre (köşedeki beyaz önlüklü küçük kare kullanıcı isteğiyle kaldırıldı) */
  .pt{position:relative;width:200px;max-width:60vw}
  .pt .portrait{position:relative;width:100%;max-width:none;border-width:4px}
  .pt .portrait::after{content:"";position:absolute;inset:0;border-radius:50%;pointer-events:none;
    background:radial-gradient(closest-side,transparent 60%,rgba(28,40,25,.5) 100%);box-shadow:inset 0 0 0 1px rgba(28,40,25,.25)}
  .pt .portrait img{transform:none;object-position:50% 30%}
  @media (min-width:1000px){.pt{width:240px}}
  @media (max-width:620px){.pt{margin-bottom:6px}}
  /* giriş: düğmelerin altında kimlik kartı */
  .hero-me{display:inline-flex;align-items:center;gap:14px;margin-top:26px;padding:7px 20px 7px 7px;border-radius:999px;text-decoration:none;text-align:left;
    border:1px solid rgba(216,178,94,.38);background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.015));
    box-shadow:0 10px 30px rgba(0,0,0,.28);animation:rise calc(.8s*var(--k)) ease calc(1.12s*var(--k)) both;transition:transform .3s ease,border-color .3s,box-shadow .3s}
  .hero-me:hover{transform:translateY(-2px);border-color:rgba(216,178,94,.8);box-shadow:0 14px 34px rgba(0,0,0,.36),0 0 32px rgba(226,171,71,.16)}
  .hero-me img{flex:none;width:68px;height:68px;border-radius:50%;object-fit:cover;display:block;box-shadow:0 0 0 1px var(--foil)}
  .hero-me span{display:grid;gap:3px}
  .hero-me small{font:600 11px/1 var(--body);letter-spacing:.16em;text-transform:uppercase;color:var(--ink-soft)}
  .hero-me b{font-family:var(--display);font-weight:400;font-size:23px;line-height:1.1;color:var(--foil);white-space:nowrap}
  .hero-me::after{content:"";flex:none;width:8px;height:8px;margin-left:4px;border-right:1.5px solid var(--foil);border-bottom:1.5px solid var(--foil);transform:rotate(45deg) translate(-2px,-2px);opacity:.8;transition:transform .3s ease}
  .hero-me:hover::after{transform:rotate(45deg) translate(1px,1px)}
  @media (min-width:700px){.hero-me{margin-top:30px}.hero-me img{width:76px;height:76px}.hero-me b{font-size:25px}}
  @media (prefers-reduced-motion:reduce){.hero-me{animation:none}}
  /* iletişim: mektup imzası gibi küçük yüz + ad */
  .sig{display:flex;align-items:center;gap:12px;margin:22px 0 24px}
  .sig img{flex:none;width:52px;height:52px;border-radius:50%;object-fit:cover;border:2px solid var(--ground);box-shadow:0 0 0 1px var(--foil)}
  .sig p{margin:0;max-width:none}
  .sig-n{font-family:var(--display);font-size:19px;line-height:1.15;color:var(--foil)}
  .sig-r{font-size:13.5px;line-height:1.3;color:var(--ink-soft)}
'''
rep("  @media (min-width:1000px){.who{grid-template-columns:240px 1fr;gap:56px}.portrait{width:240px}}\n",
    "  @media (min-width:1000px){.who{grid-template-columns:240px 1fr;gap:56px}.portrait{width:240px}}\n" + CSS)
open(p, "w", encoding="utf-8").write(s)
print("ok")

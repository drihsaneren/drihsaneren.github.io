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
    '<div class="pt"><figure class="portrait"><img src="img/portre2.jpg" alt="İhsan Eren" width="720" height="720" loading="lazy"></figure>'
    '<figure class="pt-in"><img src="img/portre.jpg" alt="İhsan Eren, beyaz önlükle" width="640" height="640" loading="lazy"></figure></div>')
rep('          <div class="contact-btns">',
    '          <div class="sig"><img src="img/portre2_s.jpg" alt="" width="192" height="192" loading="lazy"><div><p class="sig-n">İhsan Eren</p><p class="sig-r">Fizyoterapist · İntörn Tıp Doktoru</p></div></div>\n'
    '          <div class="contact-btns">')
# giriş: unvan satırının yanında küçük yüz (dokununca "Ben kimim"e iner); yüz ilk ekranda görünür ama logo ve iş önde kalır
rep('\n    <p class="role">Fizyoterapist · İntörn Tıp Doktoru</p>\n',
    '\n    <div class="hero-by"><a class="hero-face" href="#ben-kimim" aria-label="Ben kimim"><img src="img/portre2_s.jpg" alt="" width="192" height="192"></a>\n'
    '    <p class="role">Fizyoterapist · İntörn Tıp Doktoru</p></div>\n')
CSS = '''  /* yüz: ana portre + köşede iş başı karesi */
  .pt{position:relative;width:200px;max-width:60vw}
  .pt .portrait{position:relative;width:100%;max-width:none;border-width:4px}
  .pt .portrait::after{content:"";position:absolute;inset:0;border-radius:50%;pointer-events:none;
    background:radial-gradient(closest-side,transparent 60%,rgba(28,40,25,.5) 100%);box-shadow:inset 0 0 0 1px rgba(28,40,25,.25)}
  .pt .portrait img{transform:none;object-position:50% 30%}
  .pt-in{position:absolute;right:-7%;bottom:-5%;width:39%;aspect-ratio:1/1;margin:0;border-radius:50%;overflow:hidden;
    border:3px solid var(--ground);box-shadow:0 0 0 1px var(--foil),0 8px 20px rgba(0,0,0,.4);background:var(--ground)}
  .pt-in img{width:100%;height:100%;object-fit:cover;display:block;transform:scale(1.06)}
  @media (min-width:1000px){.pt{width:240px}}
  @media (max-width:620px){.pt{margin-bottom:6px}}
  /* giriş: unvanın yanında küçük yüz */
  .hero-by{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:8px 12px}
  .hero-face{flex:none;display:block;width:46px;height:46px;border-radius:50%;border:2px solid var(--ground);box-shadow:0 0 0 1px var(--foil);overflow:hidden;
    animation:rise calc(.8s*var(--k)) ease calc(.45s*var(--k)) both;transition:transform .3s ease,box-shadow .3s}
  .hero-face:hover{transform:scale(1.07);box-shadow:0 0 0 1px var(--foil),0 0 18px rgba(226,171,71,.35)}
  .hero-face img{width:100%;height:100%;object-fit:cover;display:block}
  @media (min-width:700px){.hero-face{width:54px;height:54px}}
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

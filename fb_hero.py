# Ana sayfa: hero A (logo arkada akar, isim önde), logo-yalnız üst çubuk, beyaz flaş önlemi
p="site/index.html"; s=open(p,encoding="utf-8").read()
def rep(old,new,cnt=1):
    global s
    assert s.count(old)==cnt,(old[:70],s.count(old)); s=s.replace(old,new)
# beyaz flaş: html arka planı
rep("  *{box-sizing:border-box}\n  html{scroll-behavior:smooth}\n",
    "  *{box-sizing:border-box}\n  html{scroll-behavior:smooth;background:#1c2819}\n")
# üst çubuk: yalnızca logo
rep(".brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--foil);font-family:var(--display);font-size:19px;white-space:nowrap}\n  .brand img{height:30px;width:auto;display:block}",
    ".brand{display:flex;align-items:center;flex:none;text-decoration:none;border-radius:8px}\n  .brand img{height:36px;width:auto;display:block;transition:transform .3s ease}\n  .brand:hover img{transform:scale(1.06)}\n  .brand{position:relative}\n  .brand .reg{position:absolute;top:-3px;right:-9px;font:600 9px/1 var(--body);color:var(--foil);letter-spacing:0}")
rep('<a class="brand" href="#top"><img src="img/logo.svg" alt="" width="36" height="30">İhsan Eren</a>',
    '<a class="brand" href="#top"><img src="img/logo-mark.svg" alt="İhsan Eren" width="44" height="36"><sup class="reg">®</sup></a>')
# hero yerleşimi
rep("""  .hero{
    background:
      radial-gradient(120% 70% at 50% 0%, rgba(143,164,118,.16), transparent 60%),
      var(--ground);
    border-bottom:1px solid var(--line);
    padding-block:clamp(36px,8vw,72px) clamp(28px,6vw,48px);
    text-align:center;
  }""", """  .hero{
    position:relative;overflow:hidden;isolation:isolate;
    background:
      radial-gradient(120% 70% at 50% 0%, rgba(143,164,118,.16), transparent 60%),
      var(--ground);
    border-bottom:1px solid var(--line);
    padding-block:clamp(40px,8vw,72px) clamp(32px,6vw,56px);
    text-align:center;
    display:grid;align-items:center;
  }
  @media (min-width:700px){.hero{min-height:calc(100vh - 57px);min-height:calc(100svh - 57px)}}
  .hero{grid-template-columns:minmax(0,1fr)}
  .hero > .wrap{position:relative;z-index:1;width:100%;min-width:0}
  /* logo arka planda, yavaşça akar */
  .hero-bg{position:absolute;inset:0;z-index:0;pointer-events:none;overflow:hidden}
  .hero-bg::before{content:"";position:absolute;left:50%;top:50%;width:min(150vw,1100px);aspect-ratio:1;translate:-50% -50%;border-radius:50%;
    background:radial-gradient(closest-side,rgba(226,171,71,.08),rgba(143,164,118,.045) 45%,rgba(143,164,118,.015) 72%,transparent);
    animation:aura-in calc(1.4s*var(--k)) ease-out both,aura 9s ease-in-out calc(1.6s*var(--k)) infinite}""")
rep("""  .hero-mark{position:relative;width:min(48vw,212px);margin:0 auto 22px;isolation:isolate}
  .hero-mark::before{content:"";position:absolute;inset:-34% -40%;border-radius:50%;z-index:-1;pointer-events:none;
    background:radial-gradient(closest-side,rgba(226,171,71,.20),rgba(143,164,118,.10) 55%,transparent 78%);
    animation:aura-in calc(1.2s*var(--k)) ease-out both,aura 7s ease-in-out calc(1.6s*var(--k)) infinite}""",
"""  .hero-mark{position:absolute;left:50%;top:50%;translate:-50% -50%;width:min(76vw,740px);margin:0;opacity:.34;will-change:transform,opacity;
    -webkit-mask-image:radial-gradient(closest-side,#000 55%,transparent 100%);mask-image:radial-gradient(closest-side,#000 55%,transparent 100%);
    animation:mark-in calc(1.8s*var(--k)) ease-out both,drift 40s ease-in-out calc(1.8s*var(--k)) infinite alternate}
  @keyframes mark-in{from{opacity:0;transform:scale(.96)}}
  @keyframes drift{0%{transform:none}50%{transform:translate(1.2%,-1%) rotate(.8deg) scale(1.02)}100%{transform:translate(-1%,1%) rotate(-.6deg) scale(1.03)}}
  /* arka plan logosu: tek renk, ince çizgi (gravür etkisi); yazının arkası hafifçe koyulaşır */
  .hero-bg .lg-l{stroke:#d8b25e;stroke-width:3.2}
  .hero-bg .lg-v,.hero-bg .lg-v path{fill:none;stroke:#d8b25e;stroke-width:2.4}
  .hero-bg .lg-r{fill:none;stroke:#b9c79a;stroke-width:2.4}
  .hero-bg .lg-y{fill:none;stroke:#e2ab47;stroke-width:2.6}
  .hero-bg .lg-yg{display:none}
  .hero-bg::after{content:"";position:absolute;inset:0;background:radial-gradient(46% 34% at 50% 50%,rgba(28,40,25,.6),transparent 75%)}
  @media (max-width:699px){
    .hero-mark{width:96vw;top:175px;opacity:.15;-webkit-mask-image:linear-gradient(180deg,#000 30%,transparent 72%);mask-image:linear-gradient(180deg,#000 30%,transparent 72%)}
    .hero-bg::after{display:none}
    .hero{padding-block:52px 40px}
    .hero .lede{margin-top:4px}
    .hero-ctas{margin-top:26px}
    /* telefonda bölüm kısayolları tek satır, yana kayar: daha ferah */
    .hero .nav{flex-wrap:nowrap;justify-content:flex-start;overflow-x:auto;margin:30px calc(var(--gut)*-1) 0;padding:2px var(--gut);scrollbar-width:none;
      -webkit-mask-image:linear-gradient(90deg,transparent,#000 var(--gut),#000 calc(100% - var(--gut)),transparent);mask-image:linear-gradient(90deg,transparent,#000 var(--gut),#000 calc(100% - var(--gut)),transparent)}
    .hero .nav::-webkit-scrollbar{display:none}
    .hero .nav li{flex:none}
  }""")
rep(".hero .role{animation-delay:calc(.75s*var(--k))}\n  .hero h1{animation-delay:calc(.85s*var(--k))}\n  .hero .lede{animation-delay:calc(1.1s*var(--k))}\n  .hero .where{animation-delay:calc(1.2s*var(--k))}\n  .hero-ctas{animation-delay:calc(1.3s*var(--k))}\n  .hero .nav{animation-delay:calc(1.4s*var(--k))}",
    ".hero .role{animation-delay:calc(.45s*var(--k))}\n  .hero h1{animation-delay:calc(.55s*var(--k))}\n  .hero .lede{animation-delay:calc(.85s*var(--k))}\n  .hero .where{animation-delay:calc(.95s*var(--k))}\n  .hero-ctas{animation-delay:calc(1.05s*var(--k))}\n  .hero .nav{animation-delay:calc(1.15s*var(--k))}")
rep("animation:rise calc(.85s*var(--k)) cubic-bezier(.2,.7,.2,1) calc(.85s*var(--k)) both,shimmer calc(1.7s*var(--k)) ease-in-out calc(1.9s*var(--k)) both}",
    "animation:rise calc(.85s*var(--k)) cubic-bezier(.2,.7,.2,1) calc(.55s*var(--k)) both,shimmer calc(1.7s*var(--k)) ease-in-out calc(1.7s*var(--k)) both}")
rep(".hero .rule::before,.hero .rule::after{animation:grow-x calc(1s*var(--k)) cubic-bezier(.3,.7,.2,1) both;animation-delay:calc(1s*var(--k))}",
    ".hero .rule::before,.hero .rule::after{animation:grow-x calc(1s*var(--k)) cubic-bezier(.3,.7,.2,1) both;animation-delay:calc(.7s*var(--k))}")
rep(".hero .rule svg{animation:leaf calc(.8s*var(--k)) cubic-bezier(.2,.9,.3,1.3) both;animation-delay:calc(1.2s*var(--k))}",
    ".hero .rule svg{animation:leaf calc(.8s*var(--k)) cubic-bezier(.2,.9,.3,1.3) both;animation-delay:calc(.9s*var(--k))}")
rep("@media (prefers-reduced-motion:reduce){.hero-mark::before,.hero .rule::before,.hero .rule::after{animation:none!important}}",
    "@media (prefers-reduced-motion:reduce){.hero-bg::before,.hero .rule::before,.hero .rule::after{animation:none!important}.hero-mark{animation:none!important}}")
rep(".hero .role{font-size:15px;color:var(--ink-soft);letter-spacing:.02em;margin:0 0 6px}\n  .hero h1{font-size:clamp(40px,11vw,64px);line-height:1.05;color:var(--foil);letter-spacing:.01em}",
    ".hero .role{font-size:clamp(15px,1.6vw,17px);color:var(--ink-soft);letter-spacing:.02em;margin:0 0 8px}\n  .hero h1{font-size:clamp(46px,12.5vw,104px);line-height:1.04;color:var(--foil);letter-spacing:.01em}")
rep(".hero .lede{max-width:40ch;margin:0 auto;color:var(--ink-soft);font-size:17px}",
    ".hero .lede{max-width:42ch;margin:0 auto;color:var(--ink);font-size:clamp(17px,1.8vw,19px)}")
# hero işaretlemesi: logo arka plana
i=s.index('    <div class="hero-mark"><svg class="logo lg-anim" viewBox="0 0 543 448" role="img" aria-label="İhsan Eren logosu: ortasında omurga bulunan beyin">')
j=s.index('</svg></div>\n',i)+len('</svg></div>\n')
mark=s[i:j].strip()
mark=mark.replace('<svg class="logo lg-anim" viewBox="0 0 543 448" role="img" aria-label="İhsan Eren logosu: ortasında omurga bulunan beyin">','<svg class="logo lg-anim" viewBox="0 0 543 448" focusable="false">',1)
assert mark.count('<g filter="url(#lg-emb)">')==1
mark=mark.replace('<g filter="url(#lg-emb)">','<g>',1)
s=s[:i]+s[j:]
rep('<div class="hero" id="top">\n  <div class="wrap">\n',
    '<div class="hero" id="top">\n  <div class="hero-bg" aria-hidden="true">'+mark+'</div>\n  <div class="wrap">\n')
# ışık süpürmesi yerine: omurgadan yukarı akan ışık nabzı (ilk açılışta ve görünürken ara ara)
i=s.index("<script>\n(function(){\n  var svg=document.querySelector('.lg-anim'),spec=document.getElementById('lgspec')")
j=s.index("</script>",i)+len("</script>")
s=s[:i]+"""<script>
(function(){
  var p=document.getElementById('lgpulse'),hero=document.getElementById('top');
  if(!p||!p.beginElement||!hero)return;
  if(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  var k=parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--k'))||1;
  // omurgadan yukarı akan ışık: yalnızca ilk açılışta, bir kez
  if(k>=1)setTimeout(function(){try{p.beginElement()}catch(e){}},1100);
})();
</script>"""+s[j:]
open(p,"w",encoding="utf-8").write(s)
print("ok")

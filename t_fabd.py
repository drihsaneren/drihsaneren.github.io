import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for vw in (1440,1280,1024,390):
            pg=await b.new_page(viewport={'width':vw,'height':860}, device_scale_factor=1)
            errs=[]; pg.on('pageerror',lambda e: errs.append(str(e)))
            await pg.goto('file:///home/claude/drihsaneren.github.io/index.html'); await pg.wait_for_timeout(400)
            await pg.evaluate('window.scrollTo({top:1800,behavior:"instant"})'); await pg.wait_for_timeout(500)
            info=await pg.evaluate("""(()=>{const d=document.querySelector('.fab-d');const cs=getComputedStyle(d);const r=d.getBoundingClientRect();
              const w=document.querySelector('main .wrap');const wr=w.getBoundingClientRect();const pad=parseFloat(getComputedStyle(w).paddingRight);
              return {display:cs.display, x:[Math.round(r.left),Math.round(r.right)], bottom:Math.round(innerHeight-r.bottom), icerikSag:Math.round(wr.right-pad), target:d.target, href:d.href.slice(0,40)}})()""")
            mob=await pg.eval_on_selector('#fab','e=>getComputedStyle(e).display')
            print(vw, info, 'mobil çubuk:', mob, 'hata', errs)
            if vw in (1280,1024):
                await pg.hover('.fab-d'); await pg.wait_for_timeout(300)
                await pg.screenshot(path=f'fabd_{vw}.png', clip={'x':vw-420,'y':860-160,'width':420,'height':160})
            await pg.close()
        await b.close()
asyncio.run(main())

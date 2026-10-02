import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for vw,tag in [(1280,'pc'),(390,'tel')]:
            pg=await b.new_page(viewport={'width':vw,'height':900}, device_scale_factor=2 if tag=='pc' else 2)
            errs=[]; pg.on('pageerror',lambda e: errs.append(str(e)))
            await pg.goto('file://'+sys.argv[1]); await pg.wait_for_timeout(600)
            sec=await pg.query_selector('#logo'); await sec.scroll_into_view_if_needed()
            for n in ([1,2,4,6] if tag=='pc' else [3,5]):
                await pg.click(f'#logo .pin.p{n}', force=True); await pg.wait_for_timeout(900)
                st=await pg.evaluate("(()=>{const f=document.querySelector('#logo .annot');return [f.dataset.a, document.querySelector('#logo .panel.on h3').innerText, document.getElementById('lg-count').innerText]})()")
                print(tag, n, st)
                await sec.screenshot(path=f'logo_{tag}_{n}.png')
            over=await pg.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth')
            print(tag,'overflow',over,'errors',errs)
            await pg.close()
        await b.close()
asyncio.run(main())

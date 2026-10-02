import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1280,'height':900})
        errs=[]; pg.on('pageerror',lambda e: errs.append(str(e)))
        await pg.goto('file://'+sys.argv[1]); await pg.wait_for_timeout(800)
        el=await pg.query_selector('#kareler'); await el.scroll_into_view_if_needed(); await pg.wait_for_timeout(600)
        await el.screenshot(path='el_kareler.png')
        await pg.click('.tile >> nth=1', force=True); await pg.wait_for_timeout(300)
        print('tile click opens lb:', not await pg.eval_on_selector('#lb','e=>e.hidden'))
        rp=await pg.query_selector('.rp')
        if rp:
            await rp.click(); await pg.wait_for_timeout(300)
            print('rapor click opens lb:', not await pg.eval_on_selector('#lb','e=>e.hidden'))
        print('cursor:', await pg.eval_on_selector('.tile','e=>getComputedStyle(e).cursor'), 'errors', errs)
        await b.close()
asyncio.run(main())

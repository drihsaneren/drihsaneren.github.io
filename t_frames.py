import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1280,'height':900}, device_scale_factor=2)
        await pg.goto('file://'+sys.argv[1]); await pg.wait_for_timeout(300)
        el=(await pg.query_selector_all('.exc'))[2]
        await el.scroll_into_view_if_needed()
        for k,t in enumerate([0,1.2,2.4,3.6]):
            await pg.evaluate(f"(()=>{{const s=document.querySelectorAll('.exc')[2].querySelector('svg');s.pauseAnimations();s.setCurrentTime({t});}})()")
            await (await el.query_selector('.an')).screenshot(path=f'glide_{k}.png')
        await b.close()
asyncio.run(main())

import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for page in sys.argv[1:]:
            name=page.split('/')[-1]
            pg=await b.new_page(viewport={'width':390,'height':844}, device_scale_factor=2, has_touch=True)
            errs=[]; pg.on('pageerror',lambda e: errs.append(str(e)))
            await pg.goto('file://'+page); await pg.wait_for_timeout(500)
            st=lambda: pg.eval_on_selector('#fab','e=>[e.classList.contains("on"), getComputedStyle(e).visibility]')
            top=await st()
            await pg.evaluate('window.scrollTo({top: 2200, behavior: "instant"})'); await pg.wait_for_timeout(700)
            mid=await st()
            await pg.screenshot(path=f'fab_{name}.png')
            await pg.evaluate('window.scrollTo({top: document.body.scrollHeight, behavior: "instant"})'); await pg.wait_for_timeout(700)
            end=await st()
            print(name,'üstte',top,'| ortada',mid,'| en altta',end,'| hata',errs)
            await pg.close()
        pg=await b.new_page(viewport={'width':1280,'height':900}); await pg.goto('file://'+sys.argv[1]); await pg.evaluate('window.scrollTo(0,2200)'); await pg.wait_for_timeout(500)
        print('masaüstü görünür mü:', await pg.eval_on_selector('#fab','e=>getComputedStyle(e).display'))
        await b.close()
asyncio.run(main())

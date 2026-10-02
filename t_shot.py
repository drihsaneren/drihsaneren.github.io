import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for vw,h,name in [(1280,800,'pc'),(390,844,'tel')]:
            pg = await b.new_page(viewport={'width':vw,'height':h})
            await pg.goto('file://'+sys.argv[1]+'/stres.html')
            vis = lambda sel: pg.eval_on_selector(sel,'e=>getComputedStyle(e).display!=="none"')
            print(name,'önce: başlat',await vis('#b-start'),'durdur',await vis('#b-stop'))
            await pg.click('.modes button[data-m="kutu"]'); await pg.click('#b-start')
            print(name,'sonra: başlat',await vis('#b-start'),'durdur',await vis('#b-stop'))
            await pg.wait_for_timeout(5000)
            await (await pg.query_selector('#nefes')).screenshot(path=f'breath2_{name}.png')
            await pg.close()
        await b.close()
asyncio.run(main())

import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        errs=[]
        for vw,name in [(1280,'pc'),(390,'tel')]:
            pg = await b.new_page(viewport={'width':vw,'height':900})
            pg.on('pageerror', lambda e: errs.append(str(e)))
            await pg.goto('file://'+sys.argv[1]+'/stres.html')
            await pg.click('.modes button[data-m="kutu"]')
            print(name, await pg.inner_text('#b-desc'))
            await pg.click('#b-start')
            seq=[]
            for i in range(18):
                await pg.wait_for_timeout(1000)
                wtxt=await pg.inner_text('#b-word'); s=await pg.inner_text('#b-sec')
                hold=await pg.eval_on_selector('#orb','e=>e.classList.contains("hold")')
                tr=await pg.eval_on_selector('.ball','e=>getComputedStyle(e).transform')
                seq.append(f"{i+1}s {wtxt} {s} hold={hold} {tr[:22]}")
            print("\n".join(seq))
            el = await pg.query_selector('#nefes')
            await pg.click('.modes button[data-m="478"]')
            await pg.wait_for_timeout(5500)
            print('478 @5.5s:', await pg.inner_text('#b-word'), await pg.inner_text('#b-sec'), await pg.inner_text('#b-count'))
            await el.screenshot(path=f'breath_{name}.png')
            await pg.close()
        print('errors', errs)
        await b.close()
asyncio.run(main())

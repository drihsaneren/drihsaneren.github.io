import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for name,vw,vh,mob in [("pc",1440,900,False),("tel",390,844,True)]:
            ctx=await b.new_context(viewport={"width":vw,"height":vh},device_scale_factor=1,is_mobile=mob,has_touch=mob)
            pg=await ctx.new_page(); errs=[]
            pg.on("pageerror",lambda e: errs.append(str(e)))
            await pg.goto("http://127.0.0.1:8765/en/index.html"); await pg.add_style_tag(content="html{scroll-behavior:auto!important}")
            await pg.wait_for_timeout(3000); await pg.screenshot(path=f"shots5/en_hero_{name}.png")
            await pg.evaluate("document.getElementById('rapor').scrollIntoView({block:'center'})")
            for i in range(7):
                await pg.wait_for_timeout(2700)
                el=await pg.query_selector("#rapor"); await el.screenshot(path=f"shots5/en_rs_{name}_{i}.png")
                if i<6: await pg.evaluate("document.getElementById('rs-next').click()")
            await pg.evaluate("document.getElementById('tanisma').scrollIntoView()")
            await pg.evaluate("document.querySelector('#book-days label:nth-child(2) input').click();document.querySelector('.book-times label:nth-child(4) input').click();document.querySelector('.book-modes label:nth-child(2) input').click()")
            await pg.wait_for_timeout(300)
            bk=await pg.query_selector("#tanisma"); await bk.screenshot(path=f"shots5/en_book_{name}.png")
            print(name, errs, (await pg.get_attribute("#book-wa","href"))[40:260])
            print(await pg.evaluate("document.documentElement.scrollWidth-innerWidth"))
            # alt sayfa
            await pg.goto("http://127.0.0.1:8765/bel-agrisi.html"); await pg.wait_for_timeout(500)
            await pg.screenshot(path=f"shots5/sub_{name}.png")
            cc=await pg.query_selector(".ctacard"); await cc.scroll_into_view_if_needed(); await cc.screenshot(path=f"shots5/subcta_{name}.png")
            await ctx.close()
        await b.close()
asyncio.run(main())

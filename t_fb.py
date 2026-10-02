import asyncio, sys
from playwright.async_api import async_playwright
BASE="http://127.0.0.1:8765/"
OUT="shots5/"
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for name,vw,vh,mob in [("pc",1440,900,False),("lap",1366,768,False),("tel",390,844,True)]:
            ctx=await b.new_context(viewport={"width":vw,"height":vh},device_scale_factor=1 if not mob else 2,is_mobile=mob,has_touch=mob)
            pg=await ctx.new_page()
            errs=[]
            pg.on("console",lambda m: errs.append(m.text) if m.type=="error" else None)
            pg.on("pageerror",lambda e: errs.append(str(e)))
            await pg.goto(BASE+"index.html")
            await pg.add_style_tag(content="html{scroll-behavior:auto!important}")
            await pg.wait_for_timeout(400)
            await pg.screenshot(path=OUT+f"hero_{name}_0.png")
            await pg.wait_for_timeout(2600)
            await pg.screenshot(path=OUT+f"hero_{name}_1.png")
            ov=await pg.evaluate("document.documentElement.scrollWidth - innerWidth")
            el=await pg.query_selector("#rapor")
            await el.scroll_into_view_if_needed()
            await pg.evaluate("document.getElementById('rapor').scrollIntoView({block:'center'})")
            for i in range(7):
                await pg.wait_for_timeout(2600)
                await el.screenshot(path=OUT+f"rs_{name}_{i}.png")
                await pg.click("#rs-next") if i<6 else None
            bk=await pg.query_selector("#tanisma")
            await bk.scroll_into_view_if_needed()
            await pg.click("#book-days label:nth-child(3)")
            await pg.click(".book-times label:nth-child(3)")
            await pg.wait_for_timeout(300)
            await bk.screenshot(path=OUT+f"book_{name}.png")
            href=await pg.get_attribute("#book-wa","href")
            ct=await pg.query_selector("#iletisim"); await ct.scroll_into_view_if_needed(); await ct.screenshot(path=OUT+f"contact_{name}.png")
            print(name,"overflow",ov,"errs",errs[:5]); print(href[:220])
            await ctx.close()
        await b.close()
asyncio.run(main())

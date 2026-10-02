import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for name,vw,vh,mob in [("pc",1440,900,False),("tel",390,844,True)]:
            ctx=await b.new_context(viewport={"width":vw,"height":vh},is_mobile=mob,has_touch=mob)
            pg=await ctx.new_page(); errs=[]
            pg.on("pageerror",lambda e: errs.append(str(e)))
            await pg.goto("http://127.0.0.1:8765/index.html"); await pg.add_style_tag(content="html{scroll-behavior:auto!important}")
            await pg.evaluate("document.getElementById('analiz').scrollIntoView()"); await pg.wait_for_timeout(700)
            await pg.screenshot(path=f"shots5/lx_{name}_a.png",full_page=False)
            await pg.wait_for_timeout(2600)
            el=await pg.query_selector("#lx"); await el.screenshot(path=f"shots5/lx_{name}_b.png")
            print(name,errs,await pg.evaluate("document.documentElement.scrollWidth-innerWidth"))
            await ctx.close()
        await b.close()
asyncio.run(main())

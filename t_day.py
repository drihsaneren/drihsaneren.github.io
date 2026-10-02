import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for name,vw,vh,mob,path in [("pc",1440,900,False,"index.html"),("tel",390,844,True,"index.html"),("enpc",1440,900,False,"en/index.html")]:
            ctx=await b.new_context(viewport={"width":vw,"height":vh},is_mobile=mob,has_touch=mob)
            pg=await ctx.new_page(); errs=[]
            pg.on("pageerror",lambda e: errs.append(str(e)))
            await pg.goto("http://127.0.0.1:8765/"+path); await pg.add_style_tag(content="html{scroll-behavior:auto!important}")
            await pg.evaluate("document.getElementById('bir-gun').scrollIntoView()"); await pg.wait_for_timeout(300)
            el=await pg.query_selector("#bir-gun"); await el.screenshot(path=f"shots5/day_{name}_0.png")
            for i,v in [(0,1),(1,1),(3,0),(4,1),(8,0)]:
                await pg.evaluate(f"document.querySelectorAll('#dms .dm')[{i}].querySelector('button[data-v=\"{v}\"]').click()")
            await pg.wait_for_timeout(700)
            await el.screenshot(path=f"shots5/day_{name}_1.png")
            await pg.evaluate("document.querySelector('#book-days label:nth-child(2) input').click();document.querySelector('.book-times label:nth-child(1) input').click()")
            await pg.wait_for_timeout(200)
            from urllib.parse import unquote
            print(name, errs, unquote((await pg.get_attribute("#book-wa","href")).split("text=")[1]))
            print(await pg.evaluate("document.documentElement.scrollWidth-innerWidth"), await pg.evaluate("document.getElementById('book-add').hidden"))
            await ctx.close()
        await b.close()
asyncio.run(main())

import asyncio
from urllib.parse import unquote
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for name,vw,mob,path in [("tel",390,True,"index.html"),("pc",1366,False,"index.html"),("en",390,True,"en/index.html")]:
            ctx=await b.new_context(viewport={"width":vw,"height":844},is_mobile=mob,has_touch=mob,device_scale_factor=2 if mob else 1); pg=await ctx.new_page(); errs=[]
            pg.on("pageerror",lambda e: errs.append(str(e)))
            await pg.goto("http://127.0.0.1:8765/"+path); await pg.add_style_tag(content="html{scroll-behavior:auto!important}")
            await pg.evaluate("document.getElementById('tanisma').scrollIntoView()")
            await pg.click("#book-days label:nth-child(2)")
            await pg.click(".book-parts label:nth-child(2)"); await pg.wait_for_timeout(100)
            await pg.click("#book-slots label:nth-child(4)")
            await pg.click(".book-parts label:nth-child(3)"); await pg.wait_for_timeout(200)
            el=await pg.query_selector("#book"); await el.screenshot(path=f"shots6/book_{name}.png")
            print(name, errs, await pg.evaluate("document.querySelectorAll('#book-slots label').length"), unquote((await pg.get_attribute("#book-wa","href")).split("text=")[1]))
            print(await pg.evaluate("document.documentElement.scrollWidth-innerWidth"))
            await ctx.close()
        await b.close()
asyncio.run(main())

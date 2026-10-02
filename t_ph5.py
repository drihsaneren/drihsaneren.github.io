import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for path in ["index.html","en/index.html"]:
            for vw,mob in [(360,True),(390,True),(430,True),(700,False),(768,False),(1366,False)]:
                ctx=await b.new_context(viewport={"width":vw,"height":800},is_mobile=mob,has_touch=mob,device_scale_factor=2 if mob else 1); pg=await ctx.new_page(); errs=[]
                pg.on("pageerror",lambda e: errs.append(str(e))); pg.on("console",lambda m: errs.append(m.text) if m.type=="error" else None)
                await pg.goto("http://127.0.0.1:8765/"+path); await pg.wait_for_timeout(2600)
                if path=="index.html" and vw in (390,768): await pg.screenshot(path=f"shots6/ph5_{vw}.png")
                if path=="en/index.html" and vw==390: await pg.screenshot(path="shots6/ph5_en.png")
                print(path,vw,await pg.evaluate("document.documentElement.scrollWidth-innerWidth"),errs[:2]); await ctx.close()
        await b.close()
asyncio.run(main())

import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for name,vw,vh,mob,dsf,path in [("tel",390,844,True,2,"recete.html"),("pc",1440,900,False,1,"recete.html"),("pcen",1440,900,False,1,"en/exercise-plan.html")]:
            ctx=await b.new_context(viewport={"width":vw,"height":vh},is_mobile=mob,has_touch=mob,device_scale_factor=dsf); pg=await ctx.new_page(); errs=[]
            pg.on("pageerror",lambda e: errs.append(str(e)))
            await pg.goto("http://127.0.0.1:8765/"+path); await pg.wait_for_timeout(700)
            await pg.screenshot(path=f"shots6/rec_{name}.png")
            await pg.screenshot(path=f"shots6/rec_{name}_full.png",full_page=True)
            print(name,errs,await pg.evaluate("document.documentElement.scrollWidth-innerWidth"),await pg.evaluate("document.documentElement.scrollHeight"))
            await ctx.close()
        await b.close()
asyncio.run(main())

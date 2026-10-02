import asyncio, sys
from urllib.parse import unquote
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for name,vw,vh,mob,path,age,answers in [("pc",1440,900,False,"index.html",3,[1,2,2,1,2,1,2,1,0]),("tel",390,844,True,"index.html",1,[0,0,0,0,1,0,0,0,0]),("pcR",1440,900,False,"index.html",4,[3,3,2,2,3,2,3,3,3])]:
            ctx=await b.new_context(viewport={"width":vw,"height":vh},is_mobile=mob,has_touch=mob,device_scale_factor=1)
            pg=await ctx.new_page(); errs=[]
            pg.on("pageerror",lambda e: errs.append(str(e)))
            await pg.goto("http://127.0.0.1:8765/"+path); await pg.add_style_tag(content="html{scroll-behavior:auto!important}")
            await pg.evaluate("document.getElementById('bir-gun').scrollIntoView()"); await pg.wait_for_timeout(300)
            el=await pg.query_selector("#bir-gun"); await el.screenshot(path=f"shots5/gh_{name}_0.png")
            await pg.click(f"#gh .gh-step.on .gh-o[data-v='{age}']"); await pg.wait_for_timeout(500)
            for k,v in enumerate(answers):
                if k==4: await el.screenshot(path=f"shots5/gh_{name}_q.png")
                await pg.click(f"#gh .gh-step.on .gh-o[data-v='{v}']"); await pg.wait_for_timeout(450)
            await pg.wait_for_timeout(1400)
            await pg.evaluate("document.getElementById('bir-gun').scrollIntoView()"); await pg.wait_for_timeout(200)
            await el.screenshot(path=f"shots5/gh_{name}_res.png")
            await pg.evaluate("document.querySelector('#book-days label:nth-child(2) input').click();document.querySelector('#book-slots label:nth-child(1) input').click()")
            print(name, errs, unquote((await pg.get_attribute("#book-wa","href")).split("text=")[1]))
            print(await pg.evaluate("document.documentElement.scrollWidth-innerWidth"))
            await ctx.close()
        await b.close()
asyncio.run(main())

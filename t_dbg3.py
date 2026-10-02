import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        ctx=await b.new_context(viewport={"width":390,"height":844},device_scale_factor=2,is_mobile=True,has_touch=True)
        pg=await ctx.new_page()
        await pg.goto("http://127.0.0.1:8765/index.html"); await pg.add_style_tag(content="html{scroll-behavior:auto!important}")
        await pg.wait_for_timeout(500)
        print(await pg.evaluate("[innerWidth, innerHeight, document.documentElement.clientWidth, document.documentElement.scrollWidth, visualViewport.scale, visualViewport.width]"))
        await pg.evaluate("window.scrollTo(0,1500)"); await pg.wait_for_timeout(300)
        print(await pg.evaluate("[scrollY, document.scrollingElement.scrollTop]"))
        r=await pg.evaluate("""()=>{const W=document.documentElement.clientWidth,out=[];for(const e of document.querySelectorAll('body *')){const r=e.getBoundingClientRect();if(r.right>W+1&&r.width>0){out.push(e.tagName+'.'+(e.className&&e.className.baseVal!==undefined?e.className.baseVal:e.className)+' '+Math.round(r.left)+'-'+Math.round(r.right))}}return out.slice(0,12)}""")
        print("\n".join(r))
        await b.close()
asyncio.run(main())

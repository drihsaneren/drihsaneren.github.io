import asyncio, sys
from playwright.async_api import async_playwright
tag=sys.argv[1] if len(sys.argv)>1 else "now"
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for name,vw,vh,mob,dsf in [("tel",390,844,True,2),("pc",1440,900,False,1)]:
            ctx=await b.new_context(viewport={"width":vw,"height":vh},is_mobile=mob,has_touch=mob,device_scale_factor=dsf)
            pg=await ctx.new_page()
            await pg.goto("http://127.0.0.1:8765/index.html")
            t0=0
            for t in [700,1600,3000,9000]:
                await pg.wait_for_timeout(t-t0); t0=t
                await pg.screenshot(path=f"shots6/{tag}_{name}_{t}.png")
            await ctx.close()
        await b.close()
asyncio.run(main())

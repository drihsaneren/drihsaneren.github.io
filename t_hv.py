import asyncio, sys
from playwright.async_api import async_playwright
tag=sys.argv[1]; css=open(sys.argv[2]).read()
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for name,vw,vh,mob,dsf in [("tel",390,844,True,2),("pc",1440,900,False,1)]:
            ctx=await b.new_context(viewport={"width":vw,"height":vh},is_mobile=mob,has_touch=mob,device_scale_factor=dsf)
            pg=await ctx.new_page()
            await pg.route("**/index.html", lambda r: r.continue_())
            await pg.goto("http://127.0.0.1:8765/index.html")
            await pg.add_style_tag(content=css)
            await pg.wait_for_timeout(5000)
            await pg.screenshot(path=f"shots6/{tag}_{name}.png")
            await ctx.close()
        await b.close()
asyncio.run(main())

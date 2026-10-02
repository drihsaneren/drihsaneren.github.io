import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={"width":1440,"height":900})
        await pg.goto("http://127.0.0.1:8765/index.html"); await pg.wait_for_timeout(500)
        r=await pg.evaluate("""()=>{const W=innerWidth,out=[];for(const e of document.querySelectorAll('body *')){const r=e.getBoundingClientRect();if(r.right>W+1&&r.width>0){out.push(e.tagName+'.'+(e.className&&e.className.baseVal!==undefined?e.className.baseVal:e.className)+'#'+e.id+' '+Math.round(r.left)+'-'+Math.round(r.right))}}return out.slice(0,15)}""")
        print("\n".join(r))
        await b.close()
asyncio.run(main())

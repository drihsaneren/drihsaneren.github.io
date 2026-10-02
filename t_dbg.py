import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1280,'height':900})
        await pg.goto('file://'+sys.argv[1]); await pg.wait_for_timeout(300)
        await pg.evaluate("document.getElementById('qt-list').innerHTML='<li><i class=\"m\"></i><div><b>x</b><span>y</span></div></li>'")
        r=await pg.evaluate("(()=>{const i=document.querySelector('#qt-list i');const c=getComputedStyle(i);return [c.width,c.height,c.display,c.padding,c.border, i.getBoundingClientRect().width]})()")
        print(r)
        rules=await pg.evaluate("""(()=>{const i=document.querySelector('#qt-list i');const out=[];for(const ss of document.styleSheets){try{for(const r of ss.cssRules){if(r.selectorText&&i.matches(r.selectorText))out.push(r.cssText.slice(0,160))}}catch(e){}}return out})()""")
        print("\n".join(rules))
        await b.close()
asyncio.run(main())

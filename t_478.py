import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        await pg.add_init_script("(()=>{const r=Date.now.bind(Date);const s=r();Date.now=()=>s+(r()-s)*20;})()")
        await pg.goto('file://'+sys.argv[1]+'/stres.html')
        await pg.click('.modes button[data-m="478"]'); await pg.click('#b-start')
        await pg.wait_for_timeout(4500)
        print(await pg.inner_text('#b-word'), '|', await pg.inner_text('#b-count'), '| start hidden:', await pg.eval_on_selector('#b-start','e=>e.hidden'))
        await b.close()
asyncio.run(main())

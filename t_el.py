import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':int(sys.argv[3]),'height':900}, device_scale_factor=2)
        await pg.goto('file://'+sys.argv[1]); await pg.wait_for_timeout(800)
        el=await pg.query_selector(sys.argv[2]); await el.screenshot(path=sys.argv[4])
        await b.close()
asyncio.run(main())

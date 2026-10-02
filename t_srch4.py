import asyncio, sys, http.server, threading, functools
from playwright.async_api import async_playwright
root=sys.argv[1]
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',8772),functools.partial(Q,directory=root)); threading.Thread(target=srv.serve_forever,daemon=True).start()
QS={'bilgi.html':['huntington','pankreas kanseri','narkolepsi','zayıflama hapı','kolesterol'],'en/health-library.html':['huntington','pancreatic cancer','narcolepsy','weight loss pill','cholesterol']}
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1280,'height':900})
        await pg.route('**/*', lambda r: r.abort() if not r.request.url.startswith('http://127.0.0.1') else r.continue_())
        for page,qs in QS.items():
            await pg.goto(f'http://127.0.0.1:8772/{page}'); await pg.wait_for_timeout(400)
            for q in qs:
                await pg.click('button.srch'); await pg.wait_for_timeout(250)
                inp=await pg.query_selector('dialog.sd input'); await inp.fill(q); await pg.wait_for_timeout(500)
                res=await pg.eval_on_selector_all('dialog.sd .sd-r','els=>els.slice(0,3).map(e=>(e.getAttribute("href")||"").split("#")[0]+" | "+(e.querySelector(".sd-t")||e).textContent.trim().slice(0,50))')
                print(f'{q!r:28}', res)
                await pg.keyboard.press('Escape'); await pg.wait_for_timeout(150)
        await b.close()
asyncio.run(main())

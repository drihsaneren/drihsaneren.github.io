import asyncio, sys, http.server, threading, functools
from playwright.async_api import async_playwright
root=sys.argv[1]; out=sys.argv[2]; lang=sys.argv[3] if len(sys.argv)>3 else 'tr'
P = {'tr': ['otur-kalk-testi.html','duvar-oturusu.html','ic-cekis.html','doga-recetesi.html','bag-kurmak.html'],
     'en': ['en/sitting-rising-test.html','en/wall-sit-blood-pressure.html','en/cyclic-sighing.html','en/nature-prescription.html','en/social-connection.html']}[lang]
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',8767),functools.partial(Q,directory=root)); threading.Thread(target=srv.serve_forever,daemon=True).start()
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for vw,tag in [(1280,'pc'),(390,'tel')]:
            ctx=await b.new_context(viewport={'width':vw,'height':900})
            pg=await ctx.new_page(); errs=[]
            pg.on('pageerror',lambda e: errs.append(str(e)))
            await pg.route('**/*', lambda r: r.abort() if not r.request.url.startswith('http://127.0.0.1') else r.continue_())
            # SRT
            await pg.goto(f'http://127.0.0.1:8767/{P[0]}'); await pg.wait_for_timeout(300)
            await pg.click('[data-k="rise-hand"] [data-d="1"]'); await pg.click('[data-k="rise-hand"] [data-d="1"]')
            await pg.click('[data-k="sit-knee"] [data-d="1"]'); await pg.check('#rise-wob')
            tot=await pg.inner_text('#srt-tot'); lab=await pg.inner_text('#srt-lab'); me=await pg.eval_on_selector('#oran .row.me','e=>e.getAttribute("data-g")')
            print(tag,'SRT total',tot,lab,me, await pg.inner_text('#srt-mini'))
            await pg.eval_on_selector('#puan','e=>e.scrollIntoView()'); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f'{out}/i_srt_{lang}_{tag}.png')
            await pg.eval_on_selector('#oran','e=>e.scrollIntoView()'); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f'{out}/i_srt2_{lang}_{tag}.png')
            # WS
            await pg.goto(f'http://127.0.0.1:8767/{P[1]}'); await pg.wait_for_timeout(300)
            await pg.click('#bp-cmp ~ * button, .seg[aria-label] button[data-v="d"]') if False else None
            await pg.click('button[data-v="d"]'); w=await pg.eval_on_selector('#bp-cmp .row.top b','e=>e.textContent'); print(tag,'dia iso',w)
            await pg.click('#ws-go'); await pg.wait_for_timeout(11500)
            print(tag,'WS',await pg.inner_text('#ws-phase'),await pg.inner_text('#ws-sec'),await pg.inner_text('#ws-rpe'))
            await pg.eval_on_selector('#zamanlayici','e=>e.scrollIntoView()'); await pg.wait_for_timeout(200)
            await pg.screenshot(path=f'{out}/i_ws_{lang}_{tag}.png')
            # Sigh
            await pg.goto(f'http://127.0.0.1:8767/{P[2]}'); await pg.wait_for_timeout(300)
            await pg.click('#br-go'); await pg.wait_for_timeout(3000)
            print(tag,'BR',await pg.inner_text('#br-cue'),await pg.inner_text('#br-time'))
            await pg.eval_on_selector('#nefes','e=>e.scrollIntoView()'); await pg.wait_for_timeout(200)
            await pg.screenshot(path=f'{out}/i_br_{lang}_{tag}.png')
            await pg.wait_for_timeout(8000); print(tag,'BR2',await pg.inner_text('#br-cue'),await pg.inner_text('#br-count'))
            # Nature
            await pg.goto(f'http://127.0.0.1:8767/{P[3]}'); await pg.wait_for_timeout(300)
            rows=await pg.query_selector_all('.dy')
            for i in (0,2,4,5):
                for _ in range(3): await (await rows[i].query_selector('[data-d="10"]')).click()
            print(tag,'NT',await pg.inner_text('#nt-tot'),await pg.inner_text('#nt-r1'))
            await pg.reload(); await pg.wait_for_timeout(300); print(tag,'NT persisted',await pg.inner_text('#nt-tot'))
            await pg.eval_on_selector('#takvim','e=>e.scrollIntoView()'); await pg.wait_for_timeout(200)
            await pg.screenshot(path=f'{out}/i_nt_{lang}_{tag}.png')
            # Social
            await pg.goto(f'http://127.0.0.1:8767/{P[4]}'); await pg.wait_for_timeout(300)
            await pg.click('#gv-done'); await pg.wait_for_timeout(1700)
            vis=await pg.eval_on_selector_all('.task:not([hidden])','els=>els.length')
            print(tag,'GV',await pg.inner_text('#gv-n'),await pg.inner_text('#gv-msg'),'visible',vis)
            await pg.click('#gv-next'); await pg.wait_for_timeout(400)
            await pg.eval_on_selector('#gorev','e=>e.scrollIntoView()'); await pg.wait_for_timeout(200)
            await pg.screenshot(path=f'{out}/i_gv_{lang}_{tag}.png')
            print(tag,'errors',errs[:3])
            await ctx.close()
        await b.close()
asyncio.run(main())

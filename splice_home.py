# build_pages çıktıları -> site/index.html:
#   _home_section.txt: #bilgi bölümü; _home_css.txt: aynı bölümün stilleri; _home_trio.txt: girişteki üç kapı
s=open('site/index.html',encoding='utf-8').read()
sec=open('site/_home_section.txt',encoding='utf-8').read()
i=s.index('  <section id="bilgi">'); j=s.index('  <section id="ben-kimim">')
s=s[:i]+sec+'\n'+s[j:]
css=open('site/_home_css.txt',encoding='utf-8').read()
a=s.index('  /* bilgi köşesi */'); END='  @media (max-width:560px){.kose-more .all{margin-left:0;flex-basis:100%}}\n'
b=s.index(END,a)+len(END)
s=s[:a]+css.strip('\n')+'\n'+s[b:]
trio=open('site/_home_trio.txt',encoding='utf-8').read()
NAV='    <ul class="nav">\n'; CHIP='      <li><a href="#bilgi">Bilgi köşesi</a></li>\n'
assert s.count(NAV)==1 and s.count(CHIP)==1
s=s.replace(NAV,trio+NAV).replace(CHIP,'')
open('site/index.html','w',encoding='utf-8').write(s)

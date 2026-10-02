# -*- coding: utf-8 -*-
# Logo bölümündeki büyük logoya tescil işareti (®): sağ üst köşede, küçük ve sade
p = "site/index.html"
s = open(p, encoding="utf-8").read()
a = '<image href="img/logo.png" x="18" y="9" width="64" height="52.8" preserveAspectRatio="xMidYMid meet" class="base"/>'
assert s.count(a) == 1
s = s.replace(a, a + '<text class="reg-mark" x="78.6" y="12.8" aria-hidden="true">®</text>', 1)
c = "  .annot .base{transition:opacity .5s ease,filter .5s ease}"
assert s.count(c) == 1
s = s.replace(c, c + "\n  .annot .reg-mark{font-family:var(--body);font-size:3.1px;font-weight:600;fill:var(--foil);opacity:.85}", 1)
open(p, "w", encoding="utf-8").write(s)
print("ok")

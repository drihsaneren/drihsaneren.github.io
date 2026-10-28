# "Bu sayfada" + "Geçmişten bugüne" ekleme yardımcıları (srcedit önbelleğini kullanır)
import sys
import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from srcedit import _r, _w, save, replace, src_after, bump

def region(s, start_key, end_key):
    a = s.index(start_key); b = s.index(end_key, a)
    return a, b

def sec_id(f, start_key, end_key, h2, sid):
    """start_key..end_key aralığında, '<h2>h2</h2>' başlığını içeren <section> etiketine id ekler."""
    s = _r(f); a, b = region(s, start_key, end_key)
    key = f"<h2>{h2}</h2>"
    i = s.find(key, a); assert a < i < b, (f, h2)
    assert s.find(key, i + 1, b) == -1, (f, h2, "iki kez")
    j = s.rfind("<section", a, i)
    tag_end = s.index(">", j)
    tag = s[j:tag_end + 1]
    if f'id="{sid}"' in tag: return
    assert tag == "<section>", (f, h2, tag)
    s = s[:j] + f'<section id="{sid}">' + s[tag_end + 1:]
    _w(f, s)

def insert_before_section(f, start_key, end_key, h2, html):
    """h2 başlıklı bölümün <section ...> etiketinden hemen önce html ekler."""
    s = _r(f); a, b = region(s, start_key, end_key)
    if html.strip()[:60] in s[a:b]: return
    i = s.find(f"<h2>{h2}</h2>", a); assert a < i < b, (f, h2)
    j = s.rfind("<section", a, i); ls = s.rfind("\n", 0, j) + 1
    s = s[:ls] + html + s[ls:]
    _w(f, s)

def toc_after_stats(f, start_key, end_key, toc_expr):
    """İlk .stats bloğunun kapanışından sonra toc ifadesini ekler."""
    s = _r(f); a, b = region(s, start_key, end_key)
    if "g_toc(" in s[a:b]: return
    i = s.find('<div class="stats">', a); assert a < i < b
    # stats div'inin kapanışı: ilk '\n      </div>' (6 boşluk girinti)
    e = s.find("\n      </div>", i); assert a < e < b
    e += len("\n      </div>")
    s = s[:e] + "\n      " + toc_expr + s[e:]
    _w(f, s)

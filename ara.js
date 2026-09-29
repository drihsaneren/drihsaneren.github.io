/* drihsaneren.com · site içi arama (TR/EN) */
(() => {
  "use strict";
  const SCRIPT = document.currentScript;
  const BASE = new URL(".", SCRIPT && SCRIPT.src ? SCRIPT.src : location.href);
  const EN = (document.documentElement.lang || "").toLowerCase().startsWith("en");
  const WA = "https://wa.me/905538815568?text=";

  const T = EN ? {
    label: "Search the site",
    ph: "Search pain, symptoms or exercises",
    phShort: "Search topics or symptoms",
    close: "Close",
    popular: "Popular topics",
    loading: "Loading…",
    error: "Search could not be loaded. Please check your connection and try again.",
    none: (q) => `No results for “${q}”.`,
    near: "Closest matches",
    ask: "Would you like to read about this? Suggest the topic on WhatsApp",
    askMsg: (q) => `Hello, I would like to suggest a topic for the Health library: ${q}`,
    count: (n) => (n === 1 ? "1 result" : `${n} results`),
    keys: ["navigate", "open", "close"],
    chips: ["Low back pain", "Neck pain", "Knee osteoarthritis", "Frozen shoulder", "Plantar fasciitis", "Sleep", "Stress", "Parkinson's"],
    stop: "a an and are as at be by can do does for from how i in is it me my of on or should the to what when which why with you your",
    syn: { kegel: ["pelvic", "incontinence"], tmj: ["jaw", "tmd"], bladder: ["incontinence", "bladder"], dizziness: ["vertigo", "dizziness"], arthritis: ["osteoarthritis"], slipped: ["herniation", "hernia"], disc: ["disc", "disk"], disk: ["disc"], insomnia: ["sleep"], anxiety: ["stress"], panic: ["stress"], cva: ["stroke"], paralysis: ["stroke"], osteopenia: ["osteoporosis"], tendinitis: ["tendinopathy"], epicondylitis: ["elbow"], spur: ["spur", "plantar"] },
    file: "ara-en.json",
  } : {
    label: "Sitede ara",
    ph: "Ağrı, hastalık, egzersiz ya da belirti arayın",
    phShort: "Konu ya da belirti arayın",
    close: "Kapat",
    popular: "Sık aranan konular",
    loading: "Yükleniyor…",
    error: "Arama şu anda yüklenemedi. Bağlantınızı kontrol edip yeniden deneyin.",
    none: (q) => `“${q}” için sonuç bulunamadı.`,
    near: "En yakın sonuçlar",
    ask: "Bu konuyu okumak ister misiniz? WhatsApp'tan önerin",
    askMsg: (q) => `Merhaba, Bilgi köşesi için bir konu önermek istiyorum: ${q}`,
    count: (n) => `${n} sonuç`,
    keys: ["gezin", "aç", "kapat"],
    chips: ["Bel ağrısı", "Boyun fıtığı", "Diz kireçlenmesi", "Donuk omuz", "Topuk dikeni", "Uyku", "Stres", "Parkinson"],
    stop: "acaba ama bana ben beni bir biraz bu da de daha en gibi hangi icin ile iyi kac ki mi mu mi misin mu mudur ne neden nedir nasil o olan olur sey siz ve veya ya yapmali yapilir",
    syn: { kegel: ["pelvik", "idrar"], tme: ["cene"], tmj: ["cene"], hamile: ["gebelik", "gebe"], hamilelik: ["gebelik"], vertigo: ["donme", "bppv"], sersemlik: ["donme"], felc: ["inme"], artroz: ["kirec"], osteoartrit: ["kirec"], osteoartroz: ["kirec"], kireclenmesi: ["kirec"], osteopeni: ["osteoporoz", "erimesi"], siyatik: ["siyatik", "fitik"], hernisi: ["fitik"], disk: ["fitik", "disk"], uykusuzluk: ["uyku"], anksiyete: ["stres", "kaygi"], panik: ["stres"], depresyon: ["cokkunluk", "ruh"], tendinit: ["tendon"], epikondilit: ["dirsek"], fasiit: ["topuk"], plantar: ["topuk", "plantar"], menopoz: ["kemik"], yuruyus: ["yuru", "adim"], spor: ["egzersiz"], jimnastik: ["egzersiz"], fizik: ["fizyoterapi"], kolon: ["kolon"], onkoloji: ["kanser"], tumor: ["kanser"], protezi: ["protez"] },
    file: "ara-tr.json",
  };
  const STOP = new Set(T.stop.split(" "));

  // ---------------------------------------------------------------- metin normalleştirme
  const FOLD = { "ç": "c", "ğ": "g", "ı": "i", "ö": "o", "ş": "s", "ü": "u", "â": "a", "î": "i", "û": "u", "é": "e", "è": "e", "ê": "e", "á": "a", "à": "a", "ó": "o", "í": "i", "ñ": "n", "ä": "a", "ë": "e", "ï": "i", "’": "'" };
  // Uzunluğu korur: normalleştirilmiş metindeki konumlar özgün metinle aynıdır.
  function norm(s) {
    let o = "";
    for (let i = 0; i < s.length; i++) {
      const c = s[i];
      let l = c.toLocaleLowerCase("tr");
      if (l.length !== 1) l = c.toLowerCase();
      if (l.length !== 1) l = c;
      o += FOLD[l] || l;
    }
    return o;
  }
  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const isW = (c) => c !== undefined && /[a-z0-9]/.test(c);

  function tokens(q) {
    const raw = norm(q).split(/[^a-z0-9]+/).filter((t) => t.length >= 2);
    const kept = raw.filter((t) => !STOP.has(t));
    return (kept.length ? kept : raw).slice(0, 8);
  }
  // Hafif ek ayıklama (TR: -ım, -yor, -ları, -sında…; EN: -s, -ing, -ed) + eş anlamlılar
  const SUF = EN
    ? ["ing", "ies", "ed", "es", "s", "ly"]
    : ["yor", "iyor", "uyor", "lari", "leri", "larim", "lerim", "imiz", "umuz", "iniz", "unuz", "sinda", "sinde", "inda", "inde", "nda", "nde", "dan", "den", "tan", "ten", "da", "de", "ta", "te", "lar", "ler", "mak", "mek", "dum", "dim", "tum", "tim", "du", "di", "tu", "ti", "si", "su", "im", "um", "in", "un", "ya", "ye", "yi", "yu", "li", "lu", "ki", "i", "u", "a", "e", "m"];
  const CONT = EN
    ? "(?:s|es|'s)?"
    : "(?:l[ae]r)?(?:[iu]m[iu]z|[iu]n[iu]z|[iu]m|[iu]n|s?[iu])?(?:n?(?:d[ea]ki|d[ea]n|t[ea]n|d[ea]|t[ea]|[iu]n|l[ea]|y[ea]|y[iu]|[iu]|[ea]))?";
  function stems(t) {
    const out = [];
    let cur = t;
    for (let round = 0; round < 3; round++) {
      const suf = SUF.find((x) => cur.endsWith(x) && cur.length - x.length >= 3);
      if (!suf) break;
      cur = cur.slice(0, -suf.length);
      out.push(cur);
    }
    return out;
  }
  function variants(t) {
    const out = [], seen = new Set();
    const add = (s, w) => {
      if (s.length < 2 || seen.has(s)) return;
      seen.add(s);
      // kısa sözcükler yalnızca yaygın eklerle eşleşsin: "bel" → belim, belinizde; ama "belirti" değil
      const pat = "(^|[^a-z0-9])" + s + (s.length <= 3 ? "(?=(?:" + CONT + ")(?![a-z0-9]))" : "");
      out.push({ s, w, pat, re: new RegExp(pat) });
    };
    add(t, 1);
    stems(t).forEach((s, i) => add(s, 0.82 - 0.08 * i));
    // Türkçe ünsüz yumuşaması: tutukluk ↔ tutukluğu, kitap ↔ kitabı, kanat ↔ kanadı
    if (!EN) {
      const SOFT = { k: "g", g: "k", p: "b", b: "p", t: "d", d: "t" };
      [...out].forEach((v) => { const c = v.s.slice(-1); if (SOFT[c] && v.s.length >= 4) add(v.s.slice(0, -1) + SOFT[c], v.w * 0.9); });
    }
    [...out].forEach((v) => (T.syn[v.s] || []).forEach((s) => add(s, 0.9)));
    return out;
  }
  function hit(text, vs) {
    let best = 0;
    for (const v of vs) if (v.w > best && v.re.test(text)) best = v.w;
    return best;
  }

  // ---------------------------------------------------------------- dizin
  let IDX = null, loading = null, failed = false;
  function load() {
    if (IDX) return Promise.resolve(IDX);
    if (!loading) {
      loading = fetch(new URL(T.file, BASE).href)
        .then((r) => { if (!r.ok) throw new Error(r.status); return r.json(); })
        .then((d) => {
          IDX = d.p.map((p) => ({
            u: p.u, t: p.t, k: p.k || "", i: p.i || "c", d: p.d || "",
            nt: norm(p.t), nk: norm(p.k || ""), nd: norm(p.d || ""),
            s: p.s.map((s) => ({ h: s[0], nh: norm(s[0]), b: s[1], nb: s[1].map(norm) })),
          }));
          failed = false;
          return IDX;
        })
        .catch((e) => { loading = null; failed = true; throw e; });
    }
    return loading;
  }

  function run(q) {
    const toks = tokens(q);
    if (!toks.length || !IDX) return null;
    const V = toks.map(variants), n = V.length;
    // her sayfa ve bölüm için terim eşleşmeleri
    let total = 0;
    const M = IDX.map((p) => {
      total += 1 + p.s.length;
      return {
        t: V.map((vs) => hit(p.nt, vs)), k: V.map((vs) => hit(p.nk, vs)), d: V.map((vs) => hit(p.nd, vs)),
        s: p.s.map((s) => V.map((vs) => {
          const h = hit(s.nh, vs);
          let b = 0;
          for (const nb of s.nb) { const x = hit(nb, vs); if (x > b) { b = x; if (b === 1) break; } }
          return [h, b];
        })),
      };
    });
    // nadir terimler daha değerli (idf)
    const idf = V.map((_, ti) => {
      let c = 0;
      for (const m of M) { if (m.t[ti] || m.d[ti]) c++; for (const x of m.s) if (x[ti][0] || x[ti][1]) c++; }
      return Math.log(1 + total / (1 + c));
    });
    const found = [];
    IDX.forEach((p, pi) => {
      const m = M[pi], sec = p.s.map(() => 0);
      let score = 0, matched = 0;
      for (let ti = 0; ti < n; ti++) {
        let best = Math.max(12 * m.t[ti], 3 * m.k[ti], 3 * m.d[ti]), hits = 0;
        m.s.forEach((x, si) => {
          const [h, b] = x[ti];
          if (h || b) {
            hits++;
            sec[si] += idf[ti] * (h * 4 + b * 1.5);
            best = Math.max(best, h ? 5 * h : 1.5 * b);
          }
        });
        if (best) { matched++; score += idf[ti] * (best + Math.min(hits, 6) * 0.35); }
      }
      if (n > 1) {
        let co = 0;
        m.s.forEach((x, si) => { if (x.every(([h, b]) => h || b)) { co++; sec[si] *= 1.8; } });
        score += Math.min(co, 3) * 1.6 * (n - 1);
      }
      if (matched) found.push({ p, score, matched, sec, m });
    });
    let res = found.filter((r) => r.matched === n), near = false;
    if (!res.length && n > 1) {
      res = found.filter((r) => r.matched >= Math.ceil(n / 2));
      near = res.length > 0;
    }
    res.sort((a, b) => b.score - a.score || a.p.t.localeCompare(b.p.t));
    return { res: res.slice(0, 12), near, V, idf };
  }

  // ---------------------------------------------------------------- vurgulama ve özet
  function ranges(nt, V) {
    const rs = [];
    for (const vs of V) {
      for (const v of vs) {
        const re = new RegExp(v.pat, "g");
        let m;
        while ((m = re.exec(nt))) {
          let a = m.index + m[1].length, b = a + v.s.length;
          while (isW(nt[b])) b++;
          rs.push([a, b]);
          if (re.lastIndex <= m.index) re.lastIndex = m.index + 1;
        }
      }
    }
    rs.sort((x, y) => x[0] - y[0]);
    const out = [];
    for (const r of rs) {
      const last = out[out.length - 1];
      if (last && r[0] <= last[1]) last[1] = Math.max(last[1], r[1]);
      else out.push(r.slice());
    }
    return out;
  }
  function marked(orig, nt, V, from = 0, to = orig.length) {
    let html = "", pos = from;
    for (const [a, b] of ranges(nt, V)) {
      if (b <= from || a >= to) continue;
      const x = Math.max(a, from), y = Math.min(b, to);
      html += esc(orig.slice(pos, x)) + "<mark>" + esc(orig.slice(x, y)) + "</mark>";
      pos = y;
    }
    return html + esc(orig.slice(pos, to));
  }
  function snippet(orig, nt, V) {
    const rs = ranges(nt, V);
    const LEN = 190;
    if (orig.length <= LEN) return marked(orig, nt, V);
    let start = rs.length ? Math.max(0, rs[0][0] - 55) : 0;
    if (start > 0) { const sp = orig.indexOf(" ", start); start = sp > -1 && sp < rs[0][0] ? sp + 1 : start; }
    let end = Math.min(orig.length, start + LEN);
    if (end < orig.length) { const sp = orig.lastIndexOf(" ", end); if (sp > start + 60) end = sp; }
    return (start > 0 ? "…" : "") + marked(orig, nt, V, start, end) + (end < orig.length ? "…" : "");
  }
  function describe(r, V, idf) {
    const p = r.p;
    let bi = -1, bs = 0;
    r.sec.forEach((v, i) => { if (v > bs) { bs = v; bi = i; } });
    const out = { sec: "", secHtml: "", snip: "", target: "" };
    if (bi < 0) {
      out.snip = snippet(p.d, p.nd, V);
      return out;
    }
    const s = p.s[bi];
    if (s.h && s.nh !== p.nt) { out.sec = s.h; out.secHtml = marked(s.h, s.nh, V); }
    // özet için en çok terimi içeren paragraf
    let bj = -1, bjs = 0;
    let full = 0;
    s.nb.forEach((nb, j) => {
      let c = 0, all = 0;
      V.forEach((vs, ti) => { const x = hit(nb, vs); if (x) all++; c += x * (idf[ti] || 1); });
      if (c > bjs) { bjs = c; bj = j; full = all; }
    });
    if (bj >= 0) {
      out.snip = snippet(s.b[bj], s.nb[bj], V);
      const inHead = s.h && V.some((vs) => hit(s.nh, vs));
      out.target = inHead && full < V.length ? s.h : s.b[bj];
    } else {
      out.snip = s.b.length ? snippet(s.b[0], s.nb[0], V) : snippet(p.d, p.nd, V);
      out.target = s.h;
    }
    return out;
  }
  function href(p, target) {
    const url = new URL(p.u, BASE);
    if (target) url.hash = "ara=" + encodeURIComponent(target.slice(0, 80));
    return url.href;
  }

  // ---------------------------------------------------------------- simgeler
  const svg = (d) => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${d}</svg>`;
  const ICON = {
    c: svg('<path d="M3 12h4l2.5-6 5 12 2.5-6h4"/>'),
    r: svg('<circle cx="13.5" cy="4.5" r="2"/><path d="M8 21l3-6 3 2v4M6.5 12.5l3.2-3.8 4.3.8 3 3.2"/>'),
    s: svg('<path d="M12 20s-7-4.3-7-9.6A4 4 0 0 1 12 8a4 4 0 0 1 7 2.4C19 15.7 12 20 12 20z"/>'),
    n: svg('<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6.3 6.3l2.5 2.5M15.2 15.2l2.5 2.5M6.3 17.7l2.5-2.5M15.2 8.8l2.5-2.5"/>'),
    h: svg('<path d="M4 11.5 12 5l8 6.5V20h-5v-5.5H9V20H4z"/>'),
    t: svg('<rect x="6" y="4.5" width="12" height="16" rx="2"/><path d="M9.5 4.5h5v3h-5zM9.5 12h5M9.5 15.5h3.5"/>'),
  };
  const MAG = svg('<circle cx="11" cy="11" r="6.5"/><path d="m20 20-4.2-4.2"/>').replace('stroke-width="1.8"', 'stroke-width="2"');
  const ARROW = svg('<path d="M7 17 17 7M9 7h8v8"/>');

  // ---------------------------------------------------------------- arayüz
  let dlg, input, body, list = [], active = -1, lastQ = null;
  function build() {
    dlg = document.createElement("dialog");
    dlg.className = "sd";
    dlg.setAttribute("aria-label", T.label);
    dlg.innerHTML =
      `<div class="sd-top">${MAG}<input type="search" role="combobox" aria-expanded="false" aria-autocomplete="list" aria-controls="sd-list" aria-label="${esc(T.label)}" placeholder="${esc(T.ph)}" autocomplete="off" autocapitalize="off" spellcheck="false" enterkeyhint="search"><button type="button" class="sd-x">${esc(T.close)}</button></div>` +
      `<div class="sd-body"><p class="sd-n" aria-live="polite"></p><div class="sd-list" id="sd-list" role="listbox" aria-label="${esc(T.label)}"></div><div class="sd-more"></div></div>` +
      `<div class="sd-foot"><span><kbd>↑</kbd><kbd>↓</kbd> ${T.keys[0]}</span><span><kbd>↵</kbd> ${T.keys[1]}</span><span><kbd>esc</kbd> ${T.keys[2]}</span></div>`;
    document.body.appendChild(dlg);
    input = dlg.querySelector("input");
    body = dlg.querySelector(".sd-body");
    dlg.querySelector(".sd-x").addEventListener("click", () => dlg.close());
    dlg.addEventListener("close", () => document.documentElement.classList.remove("sd-lock"));
    dlg.addEventListener("click", (e) => {
      if (e.target === dlg) {
        const r = dlg.getBoundingClientRect();
        if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
      }
      const chip = e.target.closest(".sd-chips button");
      if (chip) { input.value = chip.textContent; render(); input.focus(); }
      const a = e.target.closest("a.sd-r");
      if (a && sameDoc(a.href)) { e.preventDefault(); go(a.href); }
    });
    input.addEventListener("input", render);
    input.addEventListener("keydown", (e) => {
      if (e.isComposing) return;
      if (e.key === "Escape") { e.preventDefault(); dlg.close(); return; }
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        if (!list.length) return;
        e.preventDefault();
        setActive((active + (e.key === "ArrowDown" ? 1 : -1) + list.length) % list.length);
      } else if (e.key === "Enter") {
        const a = list[active >= 0 ? active : 0];
        if (a) { e.preventDefault(); go(a.href); }
      }
    });
    dlg.querySelector(".sd-list").addEventListener("mousemove", (e) => {
      const a = e.target.closest("a.sd-r");
      if (a) { const i = list.indexOf(a); if (i !== active) setActive(i, false); }
    });
  }
  function setActive(i, scroll = true) {
    list.forEach((a, j) => a.setAttribute("aria-selected", j === i ? "true" : "false"));
    active = i;
    if (list[i]) {
      input.setAttribute("aria-activedescendant", list[i].id);
      if (scroll) list[i].scrollIntoView({ block: "nearest" });
    } else input.removeAttribute("aria-activedescendant");
  }
  function chips() {
    return `<p class="sd-n">${esc(T.popular)}</p><div class="sd-chips">${T.chips.map((c) => `<button type="button">${esc(c)}</button>`).join("")}</div>`;
  }
  function render() {
    const q = input.value.trim();
    const n = body.querySelector(".sd-n"), L = body.querySelector(".sd-list"), more = body.querySelector(".sd-more");
    if (q === lastQ && IDX) return;
    list = []; active = -1;
    input.removeAttribute("aria-activedescendant");
    if (!q) {
      lastQ = q; n.textContent = ""; L.innerHTML = ""; more.innerHTML = chips();
      input.setAttribute("aria-expanded", "false");
      return;
    }
    if (!IDX) {
      n.textContent = failed ? "" : T.loading; L.innerHTML = "";
      more.innerHTML = failed ? `<p class="sd-msg">${esc(T.error)}</p>` : "";
      load().then(() => { lastQ = null; render(); }, () => { lastQ = null; if (dlg.open) render(); });
      return;
    }
    lastQ = q;
    const out = run(q);
    if (!out || !out.res.length) {
      n.textContent = ""; L.innerHTML = "";
      more.innerHTML = `<p class="sd-msg">${esc(T.none(q))}</p><a class="sd-ask" href="${WA + encodeURIComponent(T.askMsg(q))}" target="_blank" rel="noopener">${esc(T.ask)} ${ARROW}</a>` + chips();
      input.setAttribute("aria-expanded", "false");
      return;
    }
    n.textContent = out.near ? T.near : T.count(out.res.length);
    L.innerHTML = out.res.map((r, i) => {
      const d = describe(r, out.V, out.idf);
      const k = esc(r.p.k) + (d.sec ? ` <i>· ${d.secHtml}</i>` : "");
      return `<a class="sd-r" id="sd-o${i}" role="option" aria-selected="false" href="${esc(href(r.p, d.target))}">` +
        `<span class="sd-i">${ICON[r.p.i] || ICON.c}</span><span class="sd-c"><span class="sd-k">${k}</span>` +
        `<span class="sd-t">${marked(r.p.t, r.p.nt, out.V)}</span><span class="sd-s">${d.snip}</span></span></a>`;
    }).join("");
    more.innerHTML = "";
    list = [...L.querySelectorAll("a.sd-r")];
    input.setAttribute("aria-expanded", "true");
    setActive(0, false);
    body.scrollTop = 0;
  }
  function sameDoc(u) {
    const a = new URL(u, location.href);
    return a.origin === location.origin && a.pathname === location.pathname && a.search === location.search;
  }
  function go(u) {
    if (sameDoc(u)) {
      dlg.close();
      const h = new URL(u).hash;
      if (location.hash === h) jump(); else location.hash = h;
    } else {
      location.href = u;
    }
  }
  function open(q) {
    if (!dlg) build();
    if (dlg.open) { input.focus(); return; }
    if (typeof q === "string") input.value = q;
    input.placeholder = window.matchMedia && matchMedia("(max-width: 560px)").matches ? T.phShort : T.ph;
    lastQ = null;
    document.documentElement.classList.add("sd-lock");
    try { dlg.showModal(); } catch (e) { dlg.setAttribute("open", ""); }
    input.focus();
    input.select();
    render();
    load().then(() => { lastQ = null; if (dlg.open) render(); }, () => {});
  }

  // ---------------------------------------------------------------- açma yolları
  document.addEventListener("click", (e) => {
    const b = e.target.closest && e.target.closest("[data-search]");
    if (b) { e.preventDefault(); open(); }
  });
  const warm = (e) => { if (e.target.closest && e.target.closest("[data-search]")) load().catch(() => {}); };
  document.addEventListener("pointerover", warm, { passive: true });
  document.addEventListener("focusin", warm);
  document.addEventListener("keydown", (e) => {
    if ((e.key === "k" || e.key === "K") && (e.metaKey || e.ctrlKey) && !e.altKey) {
      e.preventDefault(); open();
    } else if (e.key === "/" && !e.metaKey && !e.ctrlKey && !e.altKey && !(dlg && dlg.open)) {
      const t = e.target;
      if (t && t.closest && t.closest("input,textarea,select,[contenteditable]")) return;
      e.preventDefault(); open();
    }
  });

  // ---------------------------------------------------------------- sonuca atlama (#ara=…)
  const squash = (s) => norm(s).replace(/\s+/g, "");
  function jump() {
    const m = location.hash.match(/^#ara=(.+)$/);
    if (!m) return;
    let want;
    try { want = squash(decodeURIComponent(m[1])); } catch (e) { return; }
    if (!want) return;
    const SEL = "h1,h2,h3,h4,summary,p,li,td,th,figcaption,blockquote,dt,dd,.stat,.dose";
    const skip = ".bar,footer,dialog,nav,.fab,.sources,.more,.ctacard,script,style";
    let el = null;
    for (const c of document.body.querySelectorAll(SEL)) {
      if (c.closest(skip)) continue;
      if (squash(c.textContent).startsWith(want)) { el = c; break; }
    }
    if (!el) return;
    for (const d of el.querySelectorAll(SEL)) if (squash(d.textContent).startsWith(want)) { el = d; break; }
    for (let d = el.closest("details"); d; d = d.parentElement && d.parentElement.closest("details")) d.open = true;
    const reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
    requestAnimationFrame(() => {
      el.scrollIntoView({ block: "center", behavior: reduce ? "auto" : "smooth" });
      el.classList.remove("sd-hit");
      void el.offsetWidth;
      el.classList.add("sd-hit");
      setTimeout(() => el.classList.remove("sd-hit"), 3000);
    });
    try { history.replaceState(null, "", location.pathname + location.search); } catch (e) {}
  }
  window.addEventListener("hashchange", jump);
  if (document.readyState === "complete") setTimeout(jump, 60);
  else window.addEventListener("load", () => setTimeout(jump, 60));
})();

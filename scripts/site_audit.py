#!/usr/bin/env python3
"""Non-destructive SEO + medical-content QA for drihsaneren.com.

Default mode reports warnings but only exits non-zero for parser/runtime errors.
Use --strict locally when you want warnings to fail the command.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = "drihsaneren.com"

META_RE = re.compile(r"<meta\b[^>]*>", re.I)
LINK_RE = re.compile(r"<link\b[^>]*>", re.I)
HREF_RE = re.compile(r"<a\b[^>]*\bhref=[\"']([^\"']+)[\"']", re.I)
IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
H1_RE = re.compile(r"<h1\b", re.I)
SCRIPT_JSONLD_RE = re.compile(
    r"<script\b[^>]*type=[\"']application/ld\+json[\"'][^>]*>([\s\S]*?)</script>",
    re.I,
)
TAG_RE = re.compile(r"<[^>]+>")

STRONG_CLAIMS = [
    (re.compile(r"\b(kesin|garanti|mucize|tamamen iyileştirir|tedavi eder)\b", re.I), "strong Turkish treatment claim"),
    (re.compile(r"\b(cures?|guaranteed|miracle|completely heals?)\b", re.I), "strong English treatment claim"),
    (re.compile(r"\b(ölüm riskini|mortality risk|death risk)\b", re.I), "mortality-risk claim"),
]
MANUAL_REVIEW = [
    (re.compile(r"\b(akupunktur|acupuncture)\b", re.I), "acupuncture wording"),
    (re.compile(r"\b(kök hücre|stem cell|gen tedavisi|gene therapy)\b", re.I), "advanced/experimental treatment wording"),
]

def attr(tag: str, name: str) -> str | None:
    m = re.search(r"\b" + re.escape(name) + r"\s*=\s*[\"']([^\"']*)[\"']", tag, re.I)
    return html.unescape(m.group(1)).strip() if m else None

def meta_value(text: str, *, name: str | None = None, prop: str | None = None) -> str | None:
    for tag in META_RE.findall(text):
        if name and (attr(tag, "name") or "").lower() == name.lower():
            return attr(tag, "content")
        if prop and (attr(tag, "property") or "").lower() == prop.lower():
            return attr(tag, "content")
    return None

def canonical(text: str) -> str | None:
    for tag in LINK_RE.findall(text):
        rel = (attr(tag, "rel") or "").lower().split()
        if "canonical" in rel:
            return attr(tag, "href")
    return None

def hreflangs(text: str) -> dict[str, str]:
    out = {}
    for tag in LINK_RE.findall(text):
        rel = (attr(tag, "rel") or "").lower().split()
        lang = attr(tag, "hreflang")
        href = attr(tag, "href")
        if "alternate" in rel and lang and href:
            out[lang.lower()] = href
    return out

def visible_text(raw: str) -> str:
    raw = re.sub(r"<script\b[\s\S]*?</script>", " ", raw, flags=re.I)
    raw = re.sub(r"<style\b[\s\S]*?</style>", " ", raw, flags=re.I)
    return html.unescape(re.sub(r"\s+", " ", TAG_RE.sub(" ", raw))).strip()

def expected_file_from_href(source: Path, href: str) -> Path | None:
    if not href or href.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return None
    p = urlsplit(href)
    if p.scheme in ("http", "https") and p.netloc and p.netloc.lower() not in {DOMAIN, "www." + DOMAIN}:
        return None
    path = unquote(p.path)
    if not path:
        return None
    if path.startswith("/"):
        rel = Path(path.lstrip("/"))
    else:
        rel = (source.parent / path)
    if path.endswith("/"):
        rel = rel / "index.html"
    elif not rel.suffix:
        # GitHub Pages clean directory URLs resolve to index.html; extensionless
        # article URLs are not used by this project, so leave them untouched.
        candidate = ROOT / rel
        if candidate.is_dir():
            rel = rel / "index.html"
    return rel

def page_checks(path: Path) -> list[str]:
    rel = path.relative_to(ROOT)
    raw = path.read_text(encoding="utf-8")
    warnings = []
    is_404 = rel.as_posix() == "404.html"

    title_m = re.search(r"<title>([\s\S]*?)</title>", raw, re.I)
    title = html.unescape(title_m.group(1)).strip() if title_m else ""
    desc = meta_value(raw, name="description")
    og_title = meta_value(raw, prop="og:title")
    og_desc = meta_value(raw, prop="og:description")
    og_image = meta_value(raw, prop="og:image")
    tw_card = meta_value(raw, name="twitter:card")
    can = canonical(raw)
    langs = hreflangs(raw)

    if not title:
        warnings.append("missing <title>")
    if not desc:
        warnings.append("missing meta description")
    if not is_404 and not can:
        warnings.append("missing canonical")
    if not is_404 and not {"tr", "en", "x-default"}.issubset(langs):
        warnings.append("incomplete hreflang set (tr/en/x-default)")
    if not is_404 and not (og_title and og_desc and og_image):
        warnings.append("incomplete Open Graph metadata")
    if not is_404 and not tw_card:
        warnings.append("missing Twitter/X card metadata")
    if len(H1_RE.findall(raw)) != 1 and not is_404:
        warnings.append(f"expected exactly one h1, found {len(H1_RE.findall(raw))}")

    for block in SCRIPT_JSONLD_RE.findall(raw):
        try:
            json.loads(html.unescape(block).strip())
        except Exception as exc:
            warnings.append(f"invalid JSON-LD: {exc}")

    for tag in IMG_RE.findall(raw):
        if attr(tag, "alt") is None:
            warnings.append("image without alt attribute")
            break

    for href in HREF_RE.findall(raw):
        target = expected_file_from_href(rel, href)
        if target is None:
            continue
        if not (ROOT / target).exists():
            warnings.append(f"broken internal link: {href}")
            if sum(x.startswith("broken internal link:") for x in warnings) >= 5:
                warnings.append("additional broken links omitted")
                break

    # Medical content QA is advisory by design.
    body = visible_text(raw)
    lower = body.lower()
    looks_medical = (
        "kaynaklar" in lower
        or "references" in lower
        or "bilgilendirme amaçlı" in lower
        or "informational purposes" in lower
    )
    if looks_medical and not is_404:
        ext_links = [
            h for h in HREF_RE.findall(raw)
            if urlsplit(h).scheme in ("http", "https")
            and urlsplit(h).netloc.lower() not in {DOMAIN, "www." + DOMAIN}
        ]
        if not ext_links:
            warnings.append("medical page has no external source link")
        if not re.search(r"\b(kaynaklar|references|sources)\b", body, re.I):
            warnings.append("medical page has no visible sources/references section")
        if not re.search(r"(bilgilendirme amaçlı|informational purposes)", body, re.I):
            warnings.append("medical page has no information-only disclaimer")
        for rx, label in STRONG_CLAIMS:
            if rx.search(body):
                warnings.append(f"manual evidence check: {label}")
        for rx, label in MANUAL_REVIEW:
            if rx.search(body):
                warnings.append(f"manual terminology/legal check: {label}")

    return warnings

def sitemap_checks(html_files: set[str]) -> list[str]:
    p = ROOT / "sitemap.xml"
    if not p.exists():
        return ["sitemap.xml missing"]
    warnings = []
    try:
        tree = ET.parse(p)
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        urls = {
            (loc.text or "").strip()
            for loc in tree.findall(".//s:loc", ns)
            if loc.text
        }
    except Exception as exc:
        return [f"sitemap.xml parse error: {exc}"]

    listed = set()
    for url in urls:
        parts = urlsplit(url)
        if parts.netloc.lower() not in {DOMAIN, "www." + DOMAIN}:
            warnings.append(f"foreign sitemap URL: {url}")
            continue
        pth = parts.path.lstrip("/")
        listed.add(pth + "index.html" if not pth or pth.endswith("/") else pth)

    expected = {x for x in html_files if x != "404.html"}
    missing = sorted(expected - listed)
    extra = sorted(listed - expected)
    if missing:
        warnings.append("pages missing from sitemap: " + ", ".join(missing[:10]) + (" …" if len(missing) > 10 else ""))
    if extra:
        warnings.append("sitemap URLs without matching HTML: " + ", ".join(extra[:10]) + (" …" if len(extra) > 10 else ""))
    return warnings

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="exit 1 when warnings are found")
    args = ap.parse_args()

    pages = sorted(
        p for p in ROOT.rglob("*.html")
        if ".git" not in p.parts
    )
    rels = {p.relative_to(ROOT).as_posix() for p in pages}
    rows = []
    total = 0
    for p in pages:
        warnings = page_checks(p)
        if warnings:
            rows.append((p.relative_to(ROOT).as_posix(), warnings))
            total += len(warnings)

    sw = sitemap_checks(rels)
    if sw:
        rows.append(("sitemap.xml", sw))
        total += len(sw)

    print(f"Site audit: {len(pages)} HTML pages, {total} warning(s).")
    for path, warnings in rows:
        print(f"\n[{path}]")
        for w in warnings:
            print(f"  - {w}")

    summary = Path(os.environ["GITHUB_STEP_SUMMARY"]) if "GITHUB_STEP_SUMMARY" in os.environ else None
    if summary:
        with summary.open("a", encoding="utf-8") as fh:
            fh.write(f"## Site Core audit\n\n**{len(pages)}** HTML pages checked · **{total}** warning(s).\n\n")
            for path, warnings in rows[:30]:
                fh.write(f"### `{path}`\n")
                for w in warnings[:12]:
                    fh.write(f"- {w}\n")

    return 1 if args.strict and total else 0

if __name__ == "__main__":
    import os
    raise SystemExit(main())

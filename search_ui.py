# -*- coding: utf-8 -*-
"""Site içi arama: üst çubuk düğmesi, arama alanı ve stiller. Davranış ara.js'te."""

MAG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
       'stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="m20 20-4.2-4.2"/></svg>')

SEARCH_BTN = f'<button type="button" class="srch" data-search aria-haspopup="dialog" aria-label="Sitede ara" title="Sitede ara">{MAG}</button>'


def search_field(text="Ağrı, hastalık, egzersiz ya da belirti arayın"):
    return (f'<button type="button" class="sfield" data-search aria-haspopup="dialog">{MAG}'
            f'<span>{text}</span><kbd>/</kbd></button>')


SEARCH_TAG = '<script src="ara.js" defer></script>\n'

SEARCH_CSS = """
  /* site içi arama */
  .srch{display:inline-grid;place-items:center;flex:none;width:34px;height:34px;padding:0;border:1px solid var(--line-strong);border-radius:999px;background:transparent;color:var(--ink-soft);cursor:pointer;transition:color .2s,border-color .2s,background .2s}
  .srch:hover{color:var(--foil);border-color:var(--foil);background:rgba(216,178,94,.06)}
  .srch svg{width:16px;height:16px}
  .links + .srch{margin-left:0}
  .bar .srch + .lang{margin-left:0}
  @media (max-width:1000px){.links{display:none}.links + .srch{margin-left:auto}}
  @media (min-width:1001px) and (max-width:1180px){.bar .wrap{gap:12px}.links{gap:15px}}
  @media (max-width:480px){.srch{width:31px;height:31px}.srch svg{width:15px;height:15px}}
  header.page .sfield{margin-top:26px}
  .sec-head + .sfield{margin:-4px 0 24px}
  .sfield{display:flex;align-items:center;gap:12px;width:100%;max-width:560px;height:52px;margin:0;padding:0 9px 0 18px;border:1px solid var(--line-strong);border-radius:999px;background:rgba(236,229,207,.035);color:var(--muted);font:inherit;font-size:16px;text-align:left;cursor:text;transition:border-color .2s,background .2s,color .2s}
  .sfield:hover{border-color:var(--foil);background:rgba(236,229,207,.06);color:var(--ink-soft)}
  .sfield svg{width:18px;height:18px;flex:none;color:var(--foil)}
  .sfield span{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .sfield kbd,.sd kbd{font-family:var(--body);font-size:12px;line-height:1;color:var(--muted);border:1px solid var(--line);border-bottom-width:2px;border-radius:6px;padding:4px 7px;min-width:12px;text-align:center}
  .sfield kbd{margin-right:6px}
  @media (hover:none){.sfield kbd{display:none}}
  html.sd-lock{overflow:hidden}
  dialog.sd{box-sizing:border-box;display:flex;flex-direction:column;width:min(680px,calc(100% - 32px));max-width:none;max-height:min(660px,calc(100dvh - 112px));margin:clamp(20px,9vh,88px) auto auto;padding:0;border:1px solid var(--line-strong);border-radius:18px;background:var(--ground-2);color:var(--ink);box-shadow:0 30px 90px rgba(0,0,0,.55);overflow:hidden}
  dialog.sd:not([open]){display:none}
  dialog.sd[open]{animation:sdin .18s ease-out}
  dialog.sd::backdrop{background:rgba(12,18,11,.64);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}
  @keyframes sdin{from{opacity:0;transform:translateY(-8px) scale(.985)}to{opacity:1;transform:none}}
  .sd-top{display:flex;align-items:center;gap:12px;padding:12px 12px 12px 20px;border-bottom:1px solid var(--line)}
  .sd-top > svg{width:20px;height:20px;flex:none;color:var(--foil)}
  .sd-top input{flex:1;min-width:0;margin:0;padding:8px 0;border:0;outline:0;background:none;color:var(--ink);font:inherit;font-size:18px}
  .sd-top input::placeholder{color:var(--muted);opacity:1}
  .sd-top input::-webkit-search-cancel-button{-webkit-appearance:none;appearance:none}
  .sd-x{flex:none;margin:0;padding:6px 11px;border:1px solid var(--line);border-radius:999px;background:none;color:var(--muted);font:inherit;font-size:13px;cursor:pointer}
  .sd-x:hover{color:var(--foil);border-color:var(--line-strong)}
  .sd-body{flex:1;min-height:0;overflow-y:auto;overscroll-behavior:contain;padding:6px 8px 10px}
  .sd-n{margin:10px 12px 6px;font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);font-weight:600}
  .sd-list{display:grid;gap:2px}
  .sd-r{position:relative;display:flex;gap:14px;align-items:flex-start;padding:12px;border-radius:12px;color:var(--ink);text-decoration:none;scroll-margin:8px}
  .sd-r[aria-selected="true"]{background:rgba(216,178,94,.09)}
  .sd-r[aria-selected="true"]::before{content:"";position:absolute;left:0;top:14px;bottom:14px;width:2px;border-radius:2px;background:var(--gold)}
  .sd-i{flex:none;display:grid;place-items:center;width:38px;height:38px;border:1px solid var(--line);border-radius:11px;background:rgba(143,164,118,.08);color:var(--foil)}
  .sd-i svg{width:18px;height:18px}
  .sd-c{display:grid;gap:3px;min-width:0}
  .sd-k{font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--foil);font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .sd-k i{font-style:normal;color:var(--muted);letter-spacing:.02em;text-transform:none;font-weight:500}
  .sd-t{font-family:var(--display);font-size:19px;line-height:1.3}
  .sd-s{font-size:14.5px;line-height:1.55;color:var(--ink-soft);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
  .sd mark{background:rgba(226,171,71,.24);color:var(--ink);border-radius:3px;padding:0 1px}
  .sd-chips{display:flex;flex-wrap:wrap;gap:8px;padding:4px 12px 12px}
  .sd-chips button{margin:0;padding:8px 14px;border:1px solid var(--line-strong);border-radius:999px;background:none;color:var(--ink-soft);font:inherit;font-size:14px;cursor:pointer}
  .sd-chips button:hover{color:var(--foil);border-color:var(--foil)}
  .sd-msg{margin:14px 12px 4px;color:var(--ink-soft)}
  .sd-ask{display:inline-flex;align-items:center;gap:6px;margin:6px 12px 14px;color:var(--foil);font-weight:600;font-size:15px;text-decoration:none}
  .sd-ask:hover{text-decoration:underline}
  .sd-ask svg{width:15px;height:15px}
  .sd-foot{display:flex;flex-wrap:wrap;gap:6px 18px;padding:10px 20px;border-top:1px solid var(--line);font-size:12.5px;color:var(--muted)}
  .sd-foot span{display:inline-flex;align-items:center;gap:6px}
  @media (hover:none),(max-width:560px){.sd-foot{display:none}}
  @media (max-width:560px){
    dialog.sd{width:100%;height:100%;max-height:100dvh;margin:0;border:0;border-radius:0}
    .sd-top{padding:calc(10px + env(safe-area-inset-top,0px)) 12px 10px 16px}
    .sd-r{padding:12px 10px;gap:12px}
    .sd-i{width:34px;height:34px}
  }
  .sd-hit{animation:sdhit 2.8s ease-out 1;border-radius:6px}
  @keyframes sdhit{0%,40%{background:rgba(226,171,71,.2);box-shadow:0 0 0 8px rgba(226,171,71,.2)}100%{background:transparent;box-shadow:0 0 0 8px rgba(226,171,71,0)}}
  @media (prefers-reduced-motion:reduce){dialog.sd[open],.sd-hit{animation:none}}
"""

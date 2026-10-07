# Site Core v2

This branch modernizes shared site infrastructure without changing the editorial workflow.

## Compatibility rules

1. Existing page-specific CSS and JavaScript stay in place unless a block is proven identical and safe to extract.
2. Shared assets use root-relative URLs (`/assets/...`) so Turkish and `/en/` pages resolve them identically.
3. The audit is advisory by default. It reports SEO/content-quality warnings but does not block Claude or normal content commits.
4. New medical pages should keep: title, description, canonical, TR/EN/x-default hreflang, Open Graph, Twitter/X card metadata, a visible sources section, and the information-only disclaimer.
5. Strong treatment/mortality claims and advanced/experimental treatments are flagged for manual evidence review rather than auto-rewritten.
6. Main remains untouched until this branch is reviewed and merged.

## Shared assets

- `assets/site-core.css`: fonts and only proven-safe global utilities.
- `assets/site-core.js`: dependency-free shared helpers; no automatic DOM mutations.
- `scripts/site_audit.py`: SEO, link, JSON-LD and medical-content QA.
- `.github/workflows/site-audit.yml`: runs the audit on PRs and pushes.

When Claude adds a new page, copy the metadata pattern from a current page and keep page-specific styles/scripts local unless they belong in Site Core.

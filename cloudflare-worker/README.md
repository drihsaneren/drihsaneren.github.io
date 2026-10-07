# Free Health Assistant — Cloudflare Worker

This Worker is optional. The website assistant works without it using `ara-tr.json` / `ara-en.json`.

When deployed on a Cloudflare Workers Free account, it sends only the user's short question and a few already-public excerpts from drihsaneren.com to Workers AI. It does not require an OpenAI API key.

## Cost guardrail

Keep the Cloudflare account on **Workers Free**. Workers AI has a daily free allocation. On Workers Free, usage above the free allocation fails rather than automatically becoming paid usage. Do not upgrade this Worker to Workers Paid if the goal is zero billing.

## Deploy

1. Create/sign in to a Cloudflare account.
2. From this `cloudflare-worker` folder run `npx wrangler deploy`.
3. Wrangler will ask you to authenticate with Cloudflare and will create the AI binding.
4. Copy the resulting `https://...workers.dev` URL.
5. Put that URL into `/assets/assistant-config.json` as `endpoint`.

The site automatically falls back to local site search if the Worker is unavailable or the free AI quota is exhausted.

## Safety

- CORS accepts requests only from drihsaneren.com / www.drihsaneren.com.
- User question length is capped at 500 characters.
- Context is capped to four site pages and a few snippets.
- The system prompt forbids diagnosis, medication changes, unsupported claims and invented sources.
- Common emergency phrases are handled before AI generation.
- No custom database or chat-history storage is used.

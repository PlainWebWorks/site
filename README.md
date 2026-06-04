# Plain Web Works — Marketing Site

Public source for [plainwebworks.co](https://plainwebworks.co).

## What this is

The marketing site for Plain Web Works, a small business web setup and maintenance service. Built in plain HTML, CSS, and JavaScript — no frameworks, no build step, no dependencies.

## Stack

| Layer | Tool |
|---|---|
| Hosting | Cloudflare Pages |
| Deployment | Push to `main` → auto-deploy |
| DNS | Cloudflare |
| Analytics | Cloudflare Web Analytics |

## Pages

| File | URL | Purpose |
|---|---|---|
| `index.html` | `/` | Main landing page |
| `how_it_works.html` | `/how_it_works` | Technical explainer |
| `privacy.html` | `/privacy` | Privacy policy |
| `terms.html` | `/terms` | Terms of service |

## Print assets

| File | Purpose |
|---|---|
| `flyer.html` | One-page capability statement (letter size, print-ready) |
| `business_card.html` | Business card (3.5×2in, print-ready, centers on letter paper) |

## Development

No build step. Open any `.html` file directly in a browser or use any static file server:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Deployment

Pushing to `main` triggers an automatic deploy via Cloudflare Pages. Changes are live within a couple of minutes.

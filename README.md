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
| `contact.html` | `/contact` | Contact form |
| `thank_you.html` | `/thank_you` | Post-form confirmation |
| `how_it_works.html` | `/how_it_works` | Technical explainer |
| `privacy.html` | `/privacy` | Privacy policy |
| `terms.html` | `/terms` | Terms of service |
| `sample_report.html` | `/sample_report` | Example health check report |

## Contact form

The form on `contact.html` submits to [Formspree](https://formspree.io) via `fetch()`. Formspree forwards the submission to `owner@plainwebworks.co` and returns a JSON response. On success, `script.js` redirects the visitor to `/thank_you.html` client-side.

There is no server, no database, and no form data stored anywhere on our end. Formspree processes the submission in transit and delivers it as an email — that's it.

The Formspree endpoint ID is in the form `action` attribute in `contact.html`. If the form ever needs to be pointed at a different endpoint, that's the only thing to change.

## Print assets

| File | Purpose |
|---|---|
| `flyer.html` | One-page capability statement (letter size, print-ready) |
| `business_card.html` | Business card (3.5×2in, print-ready, centers on letter paper) |

## Deployment

Pushing to `main` triggers an automatic deploy via Cloudflare Pages. Changes are live within a couple of minutes.

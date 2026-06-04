# Plain Web Works — Site Repo

## What this is

Marketing site for [plainwebworks.co](https://plainwebworks.co) and associated print assets. Small business web setup and maintenance service targeting local sole operators — landscapers, handymen, contractors, churches, auto shops.

Core value prop: get clients off Facebook-only and off lead-gen platforms, give them a real web presence they own, and make it easy to hand off or fire us. No lock-in. No hostage websites.

## Repository structure

```
index.html              # Main landing page
how_it_works.html       # Technical explainer (stack, deployment, open source)
privacy.html            # Privacy policy
terms.html              # Terms of service
sample_report.html      # Example health check report (linked from how_it_works)
flyer.html              # Print capability statement (letter size)
business_card.html      # Print business card (3.5×2in, centers on letter paper)
styles.css
script.js
favicon.svg
assets/
wrangler.jsonc          # Cloudflare Workers/Pages config (auto-generated, do not edit)
```

## Stack

Pure static HTML/CSS/JS — no frameworks, no build step, no dependencies. Deployed via GitHub push to Cloudflare Pages. Changes are live within ~2 minutes.

**Keep it that way.** Do not introduce npm, bundlers, or JS frameworks unless explicitly asked.

## Related repos

- **[PlainWebWorks/healthcheck](https://github.com/PlainWebWorks/healthcheck)** — Python CLI that runs daily health checks on client sites (DNS, SSL, HTTP, SEO, contact info). Lives in a separate repo. `clients.yml` is gitignored there and not tracked anywhere publicly.

## Conventions

### HTML/CSS/JS

- Semantic HTML, accessible markup (aria labels, skip links, `sr-only` where needed)
- Mobile-first
- No inline styles
- Class names are kebab-case
- **File names use underscores**, not hyphens (`business_card.html`, not `business-card.html`)
- Keep the site fast and simple — it's a brochure, not an app

### Do not change

- Phone number: **(803) 594-2461**
- Email: **hello@plainwebworks.co**
- `wrangler.jsonc` — managed by Cloudflare, leave it alone

## Business context

- Clients are non-technical small business owners — any client-facing output must be in plain English, no jargon
- The health check CLI justifies the monthly retainer — its output should be meaningful to a non-technical reader
- Everything the client touches should be owned by them — no proprietary lock-in in tooling choices
- Severity matters in health checks: DNS down is not the same as a cert expiring in 25 days

## What to avoid

- Do not add dependencies to the marketing site without asking
- Do not make the site clever — it should be plain, fast, and clear
- Do not introduce abstractions or refactor things that are working

# Plain Web Works — Setup Status
_Last updated: 2026-06-03_

---

## Business Status

- **Pre-launch.** Site is live but intentionally hidden from search engines.
- **LLC not yet formed.** Waiting on divorce to finalize (~2026-06-24).
- **Do not:** cold-call, run ads, or take on formal paid clients until legal timing clears.
- **Can do:** discovery conversations, free snapshots, donated work (church), warm leads.

---

## Accounts and Services

| Service | Account / Detail | Status |
|---|---|---|
| Domain registrar | `plainwebworks.co` — Cloudflare | Active |
| DNS | Cloudflare | Active |
| Hosting | Cloudflare Pages — auto-deploys from `main` | Active |
| GitHub repo | `kain2749/business_model` | Active |
| Business email (inbound) | `hello@plainwebworks.co` — Cloudflare Email Routing → personal | Active |
| Business email (outbound) | Google Workspace — active, landing in spam for now | **Warming up** |
| Google Voice | (803) 594-2461 | Active |
| Google Business Profile | Not yet created — post-divorce only | Blocked |
| Google Search Console | Post-launch — no value on a noindex site | Blocked |
| Cloudflare Web Analytics | Active — 24 views, 11 visits as of 2026-06-03 | Active |
| Google Analytics | Not needed yet — revisit post-launch if Cloudflare isn't enough | Backlog |

---

## DNS / Cloudflare Notes

- Google Workspace domain verification TXT record needs to be added in Cloudflare DNS panel if not already done.
- Once the TXT record is in Cloudflare, wait 10–15 minutes then retry verification in Workspace.
- Workspace domain verified and outbound email active as of 2026-06-03.
- Email currently landing in spam on first contact — mark as not junk to train the filter. Testing deliverability with a non-technical recipient (~2026-06-06) to confirm it sticks.
- New domain/IP has no sending reputation yet. Spam classification should improve over days/weeks as the domain warms up. SPF, DKIM, DMARC being in place helps — give it time.

---

## Website (`plainwebworks.co`)

- Pure static HTML/CSS/JS — no frameworks, no build step.
- Deployed via GitHub → Cloudflare Pages (auto-deploy on push to `main`).
- **Currently search-invisible** — `noindex, nofollow` in `index.html`, `robots.txt` blocks all crawlers. Intentional until launch.

### What's done
- [x] Full one-page marketing site
- [x] Mobile, tablet, desktop tested — all good
- [x] Favicon (SVG) — green P brand mark, browser tabs
- [x] Apple touch icon (180×180 PNG) — iOS home screen
- [x] Real phone number: `(803) 594-2461`
- [x] Placeholder email: `hello@plainwebworks.co` (real domain, forwarding active)
- [x] JSON-LD LocalBusiness schema
- [x] OG tags

### Still needed before launch
- [ ] Remove `noindex, nofollow` from `index.html`
- [ ] Update `robots.txt` — change `Disallow: /` to `Allow: /`
- [ ] Swap forwarding email for real Workspace outbound
- [ ] Add Google Business Profile link
- [ ] Add Search Console
- [ ] Add analytics (Cloudflare Web Analytics is simplest — already in the stack)
- [ ] Privacy policy page
- [ ] Terms page
- [ ] Fix OG image to absolute URL (`https://plainwebworks.co/assets/plain-web-works-hero.png`)

---

## Health Check CLI

**Location:** `src/plainwebworks_healthcheck/cli.py`

**Run with:**
```bash
.venv/bin/python -m plainwebworks_healthcheck.cli --clients clients.yml --output-dir reports/daily
```

**Output:** `reports/daily/YYYY-MM-DD.json` and `reports/daily/YYYY-MM-DD.html`

**Note:** `.venv` has the dependencies. System Python does not. The `.venv` exists at project root.

**Report files** are gitignored — they won't auto-stage. Commit them manually if you want to preserve a specific run.

**Current dogfood client:** `plainwebworks.co` (in `clients.yml`). Will show warnings for `noindex` / `nofollow` / `robots_blocks_all` until launch — this is expected and intentional.

---

## Leave-Behind Flyer

**File:** `flyer.html` (project root)

- Open in browser → File → Print → no margins → one page
- Or print to PDF for emailing
- **Update phone** if Google Voice number changes
- Ink-light version: white background, green accent lines — toner-friendly
- Pricing included: $750+$75/mo, $1,500+$150/mo, $500+ cleanup

---

## Pipeline

| Client | Type | Status |
|---|---|---|
| Local church (TBD) | Donated / portfolio | Verbal — not started |
| Lead 1 | Warm lead | Discovery pending |
| Lead 2 | Warm lead | Discovery pending |
| Lincoln, GA Chamber of Commerce | Prospect + membership | Call during business hours — meeting dates unknown, check Facebook |

### Chamber of Commerce notes
- Website: severely outdated (last newsletter August 2023)
- No meeting schedule visible online
- Unmoderated spam posts on Facebook page
- Membership info only available via physical brochure — no online join path
- **This is the pitch:** "I tried to join from your website and couldn't. I do web work for local businesses — want me to take a look?"
- Call first, don't email — email deliverability unknown given their setup

---

## Launch Sequence (when legal timing clears)

1. Form LLC
2. ~~Set up real outbound email via Google Workspace~~ — done
3. ~~Confirm Google Voice is active and tested~~ — done, (803) 594-2461
4. Remove `noindex`/`nofollow` from `index.html`
5. Update `robots.txt` to allow crawling
6. Add Search Console
7. Add analytics (Cloudflare Web Analytics)
8. Add privacy policy and terms pages
9. Push final site
10. Run health check — confirm all green
11. Create Google Business Profile
12. Start calling lead list / join chamber

---

## Key Decisions Made

- **No lock-in model** → client always owns domain and accounts → **payment before service** as the trade-off
- **Dogfooding:** `plainwebworks.co` is the first health-checked client — show clients the same report format you use on your own site
- **Plain Web Works** is the brand — not a personal name brand
- **Static site only** for the marketing site — no frameworks, no build step, keep it that way
- **Stage 1 tooling:** GitHub Issues, Markdown, email, static site, manual reports. Do not jump to dashboard/portal/automation until paying clients exist.
- **reports/daily/ is gitignored** — generated output, not source

# Plain Web Works — Client Health Check & Monthly Reporting Plan

This is the maintenance/reporting idea behind the `$75–$150/month` fee.

The point is simple:

> The setup fee gets a small business online.
> The monthly fee keeps the site, contact flow, DNS/email plumbing, and basic search visibility from quietly rotting.

This document describes the first version of a daily health-check system and how it can turn into monthly customer reports.

---

## 1. What the Customer Is Paying For

A static site on Cloudflare does not need constant babysitting like a WordPress site.

That is good.

But it still needs care.

The customer is paying for:

- Knowing the site is still reachable.
- Knowing HTTPS still works.
- Knowing customers can still contact them.
- Knowing the domain and DNS are not obviously broken.
- Knowing email records are not obviously broken.
- Knowing Google can still crawl the site.
- Knowing `noindex` was not accidentally left on.
- Getting small updates handled without learning DNS, Git, Cloudflare, or Google tooling.
- Having someone competent watching the boring internet plumbing.

Plain English:

> You run the business. We make sure the internet side does not quietly fall apart.

---

## 2. Daily Health Check Script

The core maintenance tool should is a Python script that runs daily.

It should check every client site and write results to a file.

Basic flow:

```text
clients.yml -> healthcheck.py -> daily JSON/CSV results -> alerts/reporting
```

The first version should check the public website only.

Do **not** start with Cloudflare API integration. That adds tokens, secrets, permissions, and more ways to shoot yourself in the foot.

Start with what any customer or search engine can see.

---

## 3. First-Version Checks

### Site Availability

Check:

- Does the site load?
- Does it return HTTP `200`?
- Does it avoid obvious `404`, `500`, timeout, or DNS failure?
- Does the canonical URL work?

Example:

```text
https://example.com -> 200 OK
```

Bad:

```text
https://example.com -> timeout
https://example.com -> 500 Internal Server Error
```

---

### HTTPS

Check:

- Does HTTPS work?
- Is the certificate valid?
- Is the certificate close to expiring?
- Is the browser likely to show a warning?

Plain English:

> Customers should not see a scary browser warning when they open the site.

---

### Redirects

Check:

- Does `http://example.com` redirect to HTTPS?
- Does `www.example.com` behave correctly?
- Does the chosen canonical domain work?
- Are there redirect loops?

Example canonical decision:

```text
https://example.com
```

Then `www.example.com` should redirect cleanly or at least load correctly.

---

### DNS

Check:

- Domain resolves.
- `www` resolves if used.
- No obvious missing DNS records.
- Optional: compare against expected values from the client config.

Plain English:

> The domain should point where it is supposed to point.

---

### Robots and Indexing

Check:

- `robots.txt` does not block the whole site after launch.
- The page does not contain `noindex` after launch.
- The page does not contain `nofollow` accidentally if that matters.
- Sitemap exists if you use one.

Bad launch-state leftovers:

```html
<meta name="robots" content="noindex,nofollow">
```

Bad `robots.txt` after launch:

```text
User-agent: *
Disallow: /
```

Plain English:

> Do not accidentally tell Google to ignore the site.

---

### Page Metadata

Check:

- `<title>` exists.
- Meta description exists.
- OpenGraph title/description exists if used.
- Canonical link exists if used.
- JSON-LD exists if used.

Minimum useful metadata:

```html
<title>Business Name | Service in City, State</title>
<meta name="description" content="Short plain-English description of the business.">
```

Plain English:

> The site should tell Google and link previews what it is.

---

### Contact Path

Check:

- Business phone appears if expected.
- Business email appears if expected.
- `mailto:` link exists if expected.
- `tel:` link exists if expected.
- Contact page exists if expected.
- Contact form endpoint exists if used.
- Form page loads.

Do not just check that the page exists.

Check that the visitor has an obvious way to contact the business.

Plain English:

> If a customer cannot call, email, or contact the business, the site failed.

---

### Required Text

Each client can have required text that must appear on the page.

Examples:

```yaml
required_text:
  - "Acme Plumbing"
  - "Water heater repair"
  - "Augusta, GA"
```

This catches dumb deployment mistakes like pushing the wrong template or deleting key service text.

---

### Required Links

Each client can have required links.

Examples:

```yaml
required_links:
  - "mailto:"
  - "tel:"
  - "/contact"
```

For a church:

```yaml
required_links:
  - "facebook.com"
  - "youtube.com"
```

For a contractor:

```yaml
required_links:
  - "tel:"
  - "/services"
```

---

### Broken Links

Check internal links.

Start simple:

- Fetch homepage.
- Extract links pointing to the same domain.
- Request each one.
- Report non-200 responses.

Do not crawl the entire internet.

Do not hammer third-party sites.

Plain English:

> The site should not send customers to dead pages.

---

### Response Time

Track basic response time.

Example:

```text
Homepage response: 184 ms
```

Do not obsess over it early.

Just flag obvious badness:

- Site takes 10 seconds to respond.
- Site times out.
- Site is suddenly much slower than usual.

Plain English:

> The site should not feel broken or painfully slow.

---

## 4. Later Checks

After the public-surface checker works, add optional advanced checks.

---


### Email Authentication

For each domain, check:

- SPF record exists.
- DKIM record exists if using Google Workspace/Microsoft/etc.
- DMARC record exists.
- There is not more than one SPF record.
- DMARC policy is at least present.

Example:

```text
SPF: OK
DKIM: OK
DMARC: OK, policy=none
```

Starting DMARC at `p=none` is fine for early monitoring.

Tightening to `quarantine` or `reject` should be deliberate.

Plain English:

> Business email should look legitimate and be harder to spoof.

---

### Domain Expiration

If possible, check when the domain expires.

This may be done through:

- Registrar API
- Cloudflare API
- WHOIS/RDAP, if available

Flag:

- Domain expires within 60 days.
- Domain expires within 30 days.
- Domain is expired.

Plain English:

> Do not let the customer lose their domain because nobody noticed the renewal.

---

### Google Search Console

Later, if you have access and it is worth the complexity:

- Check indexing status.
- Check crawl errors.
- Check mobile usability issues.
- Check query impressions/clicks.
- Check page experience issues.

This is probably not day-one automation.

---

### Analytics Summary

Later, include:

- Monthly visitors
- Top pages
- Traffic sources
- Mobile vs desktop
- Basic trend compared to last month

Keep it simple.

No customer needs 14 charts explaining that five people visited their church website.

---

## 5. Suggested File Structure

```text
plainwebworks-health/
├── clients.yml
├── healthcheck.py
├── requirements.txt
├── reports/
│   ├── daily/
│   │   ├── 2026-07-01.json
│   │   ├── 2026-07-02.json
│   │   └── 2026-07-03.json
│   └── monthly/
│       └── 2026-07-summary.md
├── notebooks/
│   └── monthly_report.ipynb
└── README.md
```

Keep it boring.

Boring survives.

---

## 6. Example `clients.yml`

```yaml
clients:
  - name: "Acme Plumbing"
    domain: "acmeplumbing.com"
    canonical_url: "https://acmeplumbing.com"
    tier: "standard"
    required_text:
      - "Acme Plumbing"
      - "Water heater repair"
      - "Augusta, GA"
    required_links:
      - "tel:"
      - "mailto:"
      - "/contact"
    check_paths:
      - "/"
      - "/services"
      - "/contact"
    expected_email:
      - "info@acmeplumbing.com"
    expected_phone:
      - "706-555-0100"

  - name: "First Example Church"
    domain: "firstexamplechurch.org"
    canonical_url: "https://firstexamplechurch.org"
    tier: "basic"
    required_text:
      - "Sunday Service"
      - "Pastor"
      - "Contact"
    required_links:
      - "facebook.com"
      - "youtube.com"
    check_paths:
      - "/"
      - "/contact"
```

---

## 7. Daily Output Format

Each run should write JSON.

Example:

```json
{
  "date": "2026-07-01",
  "client": "Acme Plumbing",
  "domain": "acmeplumbing.com",
  "canonical_url": "https://acmeplumbing.com",
  "status": "healthy",
  "checks": {
    "http_status": {
      "ok": true,
      "value": 200
    },
    "https": {
      "ok": true
    },
    "response_time_ms": {
      "ok": true,
      "value": 184
    },
    "title": {
      "ok": true,
      "value": "Acme Plumbing | Plumbing Repair in Augusta, GA"
    },
    "meta_description": {
      "ok": true
    },
    "robots": {
      "ok": true
    },
    "noindex": {
      "ok": true,
      "found": false
    },
    "contact_path": {
      "ok": true
    },
    "broken_links": {
      "ok": true,
      "count": 0
    }
  },
  "notes": []
}
```

If something fails:

```json
{
  "date": "2026-07-01",
  "client": "Acme Plumbing",
  "domain": "acmeplumbing.com",
  "canonical_url": "https://acmeplumbing.com",
  "status": "warning",
  "checks": {
    "http_status": {
      "ok": true,
      "value": 200
    },
    "noindex": {
      "ok": false,
      "found": true
    }
  },
  "notes": [
    "Homepage contains noindex after launch."
  ]
}
```

---

## 8. Alerts

Monthly reports are nice.

Alerts are more important.

If something is broken today, you need to know today.

Alert on:

- Site down
- DNS failure
- HTTPS failure
- Contact form missing/broken
- `noindex` found after launch
- `robots.txt` blocks the whole site after launch
- Domain expiration close
- Failed Cloudflare Pages deployment
- Missing email authentication records

Early alert options:

- Email yourself
- Print to terminal and run manually
- Write a `problems.md`
- Use cron + mail
- Later: Discord/Slack/Telegram/Pushover/etc.

Do not overbuild alerts until the basic script works.

---

## 9. Monthly Client Report

The client does not need a Jupyter notebook.

The notebook is for you.

The client gets a simple one-page report.

Example:

```markdown
# Monthly Website Report — Acme Plumbing
Month: July 2026

## Overall Status

Healthy.

## Checks This Month

- Website uptime checks: 31/31 passed
- HTTPS: OK
- Contact link/form: OK
- DNS: OK
- Email records: OK
- Broken links: 0 found
- No accidental noindex: OK

## Changes Made

- Updated holiday hours.
- Added water heater repair to services section.
- Replaced staff photo.
- Checked contact form.

## Search / Traffic Notes

- Site is indexed by Google.
- Most visits came from direct traffic and Google Search.
- Mobile visitors were the majority.

## Recommended Next Actions

- Add a dedicated page for water heater repair.
- Add two real project photos.
- Ask recent customers for Google reviews.
```

Plain English:

> The customer should read it and think, “Cool, somebody is watching this stuff.”

Not:

> “What the hell is a canonical redirect histogram?”

---

## 10. Jupyter Notebook Use

Use Jupyter for your internal view.

Good notebook charts/tables:

- Site status over time
- Failed checks by client
- Average response time by client
- Monthly uptime pass rate
- Broken-link counts
- Clients missing DMARC
- Domains expiring soon
- Clients with repeated contact-form issues

The notebook helps you manage many clients at once.

It should not become required for the business to function.

If the notebook breaks, the daily script should still run.

---

## 11. Maintenance Tier Mapping

### Basic Maintenance — $75/month

Good for one-page starter sites.

Includes:

- Daily automated public health check
- Monthly site-load/contact-path check summary
- Small content edits
- Basic DNS/domain support
- Basic email-routing support
- Basic Google Business Profile updates
- Up to 30 minutes of support per month

Customer-facing version:

> We keep the site alive, make small edits, check that customers can still contact you, and handle basic domain/email/DNS issues so you do not have to.

---

### Standard Maintenance — $150/month

Good for five-page local business sites.

Includes everything in Basic, plus:

- Up to 1 hour of support per month
- Monthly report
- Broken-link checks
- Basic Search Console review
- Basic analytics review
- Review-link/contact-flow checks
- More frequent content updates
- Seasonal hours or announcement updates
- Basic local SEO cleanup as needed
- Quarterly source/export handoff check

Customer-facing version:

> We keep your web presence current: website, Google listing, contact flow, search reporting, email/domain records, and small updates. You run the business; we keep the internet side from rotting.

---

## 12. What Maintenance Does Not Include

Monthly maintenance does **not** include:

- Unlimited redesigns
- New full website builds
- Social media management
- Paid ad management
- Logo design
- Photography
- Video editing
- Custom software
- E-commerce setup
- Full IT support
- Printer/router/computer troubleshooting
- Emergency after-hours support
- Malware/incident response
- Regulated-data systems
- Payment-card storage
- Medical/legal confidential intake systems

Plain English:

> Maintenance is maintenance. It is not “own my entire technical life for $75.”

---

## 13. First Implementation Plan

Build the first version in this order.

### Phase 1 — Public Surface Checker

Build:

- Load homepage.
- Check HTTP status.
- Check HTTPS.
- Check title/meta description.
- Check noindex.
- Check robots.txt.
- Check required text.
- Check required links.
- Check a few configured paths.
- Write JSON output.

No APIs yet.

No database yet.

No dashboard yet.

---

### Phase 2 — History and Reports

Add:

- Daily JSON files.
- Monthly summary generation.
- Simple Markdown report per client.
- Summary table of all clients.

Still no fancy dashboard.

---

### Phase 3 — Alerts

Add:

- Email alert to yourself.
- Only alert on real failures.
- Avoid noisy alert spam.

Examples:

```text
ALERT: Acme Plumbing homepage returned 500.
ALERT: First Example Church contains noindex after launch.
ALERT: Smith Auto contact page returned 404.
```

---

### Phase 4 — Cloudflare API

Add only after the basic checker is stable.

Possible checks:

- Pages deployment status
- DNS record snapshot
- Domain expiration/registrar info if available
- Cloudflare analytics summary

Use scoped tokens.

Do not hardcode secrets.

---

### Phase 5 — Search Console / Analytics

Add only if useful.

Do not spend three weeks automating a report nobody reads.

---

## 14. Security Notes

Do not store secrets in Git.

Bad:

```text
CLOUDFLARE_API_TOKEN=supersecret
```

in a committed file.

Good:

- `.env` file ignored by Git
- environment variables
- scoped API tokens
- read-only permissions where possible
- separate tokens per purpose
- no global keys unless absolutely required

Add `.gitignore`:

```gitignore
.env
*.secret
secrets/
```

Plain English:

> The health checker should not become the thing that leaks every customer account.

---

## 15. Why This Supports the Monthly Fee

Without monitoring, the maintenance fee sounds like vibes.

With monitoring, the maintenance fee is backed by actual work:

- Daily checks
- Alerts
- Monthly summaries
- Small updates
- DNS/email support
- Google listing support
- Contact-flow verification
- Source/export sanity checks

The client is buying peace of mind.

Not perfect uptime.

Not guaranteed leads.

Not magic SEO.

They are buying:

> Somebody competent is making sure my business does not look dead online.

That is the product.

### Monthly Maintenance — $75–$150/mo

A website is not “done” just because it is live. Business hours change, staff changes, contact forms break, domains renew, Google listings drift, email records get weird, and customers still need a working way to reach you.

Maintenance covers small updates, basic monitoring, contact-flow checks, domain/DNS/email support, Google Business Profile updates, and simple reporting.

Basic maintenance starts at $75/mo.
Standard maintenance starts at $150/mo.

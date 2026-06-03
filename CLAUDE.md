Plain Web Works
Project Overview
Plain Web Works is a small business web setup and maintenance service targeting local sole operators and small crews — landscapers, handymen, contractors, churches, auto shops. The value proposition is: get them off Facebook-only and off lead-gen platforms (Angi, Thumbtack), give them a real web presence they actually own, and make it easy to hand off or fire us.
No lock-in. No hostage websites. Client always owns their domain and accounts.
Repository Structure
/                        # Marketing site (plainwebworks.co)
├── index.html           # Main landing page
├── styles.css
├── script.js
├── assets/
├── CLAUDE.md
│
├── src/
│   └── plainwebworks_healthcheck/
│       └── cli.py       # Client health check runner
├── clients.yml          # Client list and check config
└── reports/
    └── daily/           # JSON health check output, one file per date
Stack
Marketing Site

Pure static HTML/CSS/JS — no frameworks, no build step, no dependencies
Deployed via GitHub to Cloudflare Pages
Keep it that way. Do not introduce npm, bundlers, or JS frameworks unless explicitly asked

Health Check CLI (src/plainwebworks_healthcheck/cli.py)

Python 3.11+
Dependencies: requests, pyyaml, beautifulsoup4
Checks run synchronously per client, sequentially
Output: JSON to reports/daily/YYYY-MM-DD.json
Client config lives in clients.yml

Conventions
HTML/CSS/JS

Semantic HTML, accessible markup (aria labels, skip links, sr-only where needed)
Mobile-first
No inline styles
Class names are kebab-case
Keep the site fast and simple — it's a brochure, not an app

Python

Type hints throughout
Dataclasses for structured results (CheckResult)
No global mutable state
Errors surface as CheckResult(ok=False, note=...) — do not raise exceptions for expected failure conditions
Keep check functions pure where possible: take inputs, return a CheckResult

clients.yml Schema
yamlclients:
  - name: "Business Name"
    domain: example.com
    canonical_url: https://www.example.com
    launched: true
    expected_email:
      - contact@example.com
    expected_phone:
      - "555-555-5555"
    required_text:
      - "Some text that must appear on the page"
    required_links:
      - /contact
    check_paths:
      - /
      - /contact
Business Context (Relevant to Code Decisions)

Clients are non-technical small business owners — any client-facing output (reports, dashboards, emails) must be in plain English, no jargon
The health check CLI justifies the monthly retainer — its output should be meaningful to a non-technical reader
Severity matters: DNS down is not the same as a cert expiring in 25 days. Flag this distinction in output
Everything the client touches should be owned by them — no proprietary lock-in in tooling choices

What to Avoid

Do not add dependencies to the marketing site without asking
Do not refactor working check functions without a clear reason
Do not generate placeholder phone numbers or emails — (555) 555-5555 and hello@plainwebworks.co are intentional placeholders in the marketing site until real contact info is confirmed
Do not make the site clever — it should be plain, fast, and clear

# Plain Web Works Operating Model

## Purpose

This document defines a lightweight operating model for **Plain Web Works**: a small-business backend support company for 1–10 person local crews.

The goal is to dogfood the same thing being sold:

**simple backend, clean intake, clean follow-up, documented work, and boring repeatable process.**

This is not an MSP cosplay stack. It is a practical workflow for going from first contact to signed work to tickets to monthly reporting.

---

## Core Business Model

Plain Web Works helps small local businesses build and maintain the backend they need to operate professionally without hiring IT staff.

Primary customer:

- 1–10 person local service business
- Contractor, HVAC, plumbing, electrical, landscaping, roofing, handyman, repair shop, small office
- Business that depends on local search, referrals, reviews, phone calls, and quote requests
- Business currently relying too much on Angi/HomeAdvisor/Facebook/random texts/word of mouth

Core promise:

**Customers should be able to find the business, request work, and leave reviews through systems the business owns.**

Core path:

```text
Google search -> business website -> quote request -> owner follow-up -> review request -> repeat
```

---

## Business Offer

### Setup / Cleanup

- Website setup or cleanup
- Domain/DNS cleanup
- Business email setup
- Google Business Profile cleanup
- Review request links
- Quote/request-work forms
- Intake spreadsheet or lightweight CRM
- Basic analytics
- Social media profile cleanup
- Account/password/MFA cleanup
- Basic device/support cleanup

### Monthly Support

- Website checks
- Review monitoring
- Negative review alerts
- Monthly report
- Small content updates
- Quote form monitoring
- Google Business Profile maintenance
- Light social posting or post drafts
- Vendor coordination
- Small account/device/workflow fixes

### Break/Fix Add-On

- Laptop/desktop troubleshooting
- Printer/scanner support
- Router/Wi-Fi triage
- Email/login/account recovery
- File/share cleanup
- New device setup
- Basic software support

---

## Business Boundaries

These boundaries keep liability and scope sane.

### Payment Boundary

Do not collect or store payment-card data on client websites.

Preferred approach:

- No website payments at first
- Client invoices through existing tools
- Later, use Square/Stripe/QuickBooks hosted payment links only

### Healthcare / Regulated Data Boundary

Do not collect patient, medical, financial, legal, or other regulated data unless proper contract scope, insurance, and compliance requirements are in place.

For the first market, prefer contractors/trades/local services.

### Security Claims Boundary

Do not promise:

- secure
- compliant
- ransomware-proof
- HIPAA-compliant
- fully protected

Use specific claims instead:

- enable MFA
- clean up account access
- document current setup
- reduce obvious risk
- coordinate with vendors
- improve backup/account hygiene

### Scope Boundary

No unlimited support unless priced as a real retainer.

Every engagement should define:

- what is included
- what is not included
- response expectations
- pricing
- ownership of accounts
- handoff expectations

---

## Dogfood Stack

Use the same kind of backend being sold.

### Public Face

- Static website
- Markdown/Bootstrap content
- Hosted on GitHub Pages, Cloudflare Pages, or Netlify
- Contact/quote form
- No payments
- Professional email later: `contact@...`, `support@...`

### Internal Source of Truth

- VSCodium
- Git repo
- Markdown files
- GitHub Issues
- GitHub Projects board
- Password manager for secrets
- Email as the customer-facing support interface

### Later Upgrade Path

Stage 1:

- GitHub Issues
- Markdown
- Email
- Static site
- Manual reports

Stage 2:

- Shared inbox/helpdesk such as FreeScout or similar

Stage 3:

- Client portal only if clients actually need it

Stage 4:

- Review/dashboard automation after paid retainers exist

Do not start at Stage 4.

---

## Workflow Overview

```text
Lead
  -> Contacted
  -> Discovery
  -> Free Snapshot
  -> Proposal / SOW
  -> Won / Lost
  -> Onboarding
  -> Active Tickets
  -> Monthly Report
  -> Renewal / Retainer / Follow-up
```

---

## GitHub Project Board

Suggested columns:

```text
Lead
Contacted
Discovery
Snapshot
Proposal
Won
Lost
Onboarding
Active Work
Waiting on Client
Done
```

Suggested labels:

```text
lead
client
proposal
website
domain-dns
email
google-business
reviews
quote-form
social
device-support
vendor
blocked
waiting-on-client
done
```

Client labels:

```text
client-acme-roofing
client-smith-hvac
client-johnson-landscaping
```

---

## Repository Layout

```text
mike-hawkes-ops/
├── README.md
├── prospects/
│   ├── template.md
│   └── acme-roofing.md
├── clients/
│   └── acme-roofing/
│       ├── README.md
│       ├── onboarding.md
│       ├── proposal.md
│       ├── scope.md
│       ├── assets.md
│       ├── tickets.md
│       └── reports/
│           └── 2026-07.md
├── templates/
│   ├── discovery.md
│   ├── snapshot.md
│   ├── proposal.md
│   ├── sow.md
│   ├── monthly-report.md
│   └── ticket.md
├── website/
│   ├── content/
│   ├── assets/
│   └── README.md
├── kb/
│   ├── google-business-profile.md
│   ├── domains-dns.md
│   ├── email-basics.md
│   ├── quote-forms.md
│   └── review-monitoring.md
└── admin/
    ├── pricing.md
    ├── service-boundaries.md
    ├── insurance-notes.md
    └── legal-questions.md
```

Do not store secrets in git.

Never put these in the repo:

- passwords
- API keys
- SSNs
- payment data
- medical data
- client customer lists
- private financial records
- anything that would be ugly in a repo leak

Use a password manager for secrets.

---

## Lead / Prospect Template

File:

```text
prospects/acme-roofing.md
```

Template:

```md
# Acme Roofing

## Status

Lead / Contacted / Discovery / Snapshot / Proposal / Won / Lost

## Contact

Owner:
Phone:
Email:
Website:
Google Business Profile:
Facebook:
Angi/HomeAdvisor/etc:

## Notes

- How they get customers:
- Current pain:
- Current vendors:
- Obvious problems:
- Follow-up date:

## Opportunity

- Website:
- Quote form:
- Reviews:
- Email/domain:
- Social:
- Device/support:
```

Create a matching GitHub issue:

```text
Lead: Acme Roofing
```

---

## Discovery Checklist

Use this for first conversations.

```md
# Discovery Checklist

## Customer Pipeline

- How do customers find you right now?
- Are you paying for leads?
- Are you using Angi, HomeAdvisor, Thumbtack, Facebook, or similar?
- What happens when someone wants a quote?
- Do quote requests ever get lost?
- Where do calls/messages/emails go?

## Web / Search

- Do you have a website?
- Who owns the domain?
- Who can update the site?
- Do you have a Google Business Profile?
- Is the phone number correct?
- Are the hours correct?
- Are photos current?

## Reviews

- Where do reviews come in?
- Do you ask happy customers for reviews?
- Do bad reviews get answered?
- Would a monthly review report help?

## Email / Accounts

- Do you use business email or personal email?
- Who has admin access?
- Are passwords shared?
- Is MFA enabled?

## Tech Pain

- What breaks most often?
- What do you wish someone else handled?
- Which vendor is hardest to deal with?
```

---

## Free Snapshot

The free snapshot is controlled. It should take 30–60 minutes, not become free consulting forever.

File:

```text
prospects/acme-roofing/snapshot.md
```

Template:

```md
# Backend Snapshot: Acme Roofing

## What I Checked

- Website
- Google Business Profile
- Reviews
- Quote/contact path
- Social profiles
- Obvious account/domain issues

## Top Findings

1.
2.
3.
4.
5.

## Recommended Next Step

## Not Included

This snapshot does not include full implementation, emergency support, regulated-data review, account takeover, payment processing, or unlimited consulting.
```

Founding-customer exchange:

```text
For free or discounted snapshots, ask for permission to use an anonymized before/after case study or testimonial if the work is useful.
```

---

## Proposal / SOW Template

File:

```text
clients/acme-roofing/proposal.md
```

Template:

```md
# Proposal: Acme Roofing Backend Cleanup

## Goal

Make it easier for customers to find Acme Roofing, request work, and leave reviews through systems Acme owns.

## Scope

- Website cleanup
- Quote form
- Google Business Profile cleanup
- Review request link
- Monthly review/lead report

## Not Included

- Payment processing
- 24/7 support
- Regulated data
- Unlimited device support
- Emergency incident response
- Security/compliance guarantees

## Client Responsibilities

- Provide access to needed accounts
- Keep ownership of domain and core accounts
- Approve content before publication
- Respond to requests for business details/photos

## Price

Setup:
Monthly:
Hourly support:

## Acceptance

Reply by email with “Approved” or sign attached copy.
```

---

## Onboarding Template

File:

```text
clients/acme-roofing/onboarding.md
```

Template:

```md
# Onboarding

## Accounts Needed

- Domain registrar
- Website host
- Google Business Profile
- Business email
- Facebook page
- Review platforms
- Form backend / CRM / spreadsheet

## Access Rules

- No shared passwords sent by text
- Owner keeps ownership of accounts
- Plain Web Works gets delegated/admin access where possible
- Payment systems stay outside the website
- Access is removed when engagement ends

## Client Assets Needed

- Logo
- Photos
- Services list
- Service area
- Business hours
- Phone number
- Email
- Review links
- Existing website/login info
```

---

## Ticket Template

Use GitHub Issues privately. Clients do not need direct GitHub access.

Example:

```md
# Ticket: Acme Roofing quote form not sending email

Client: Acme Roofing
Priority: Normal
Source: Email
Opened:
Status:

## Problem

Owner reports quote form submissions are not arriving.

## Worklog

- Checked form backend
- Sent test submission
- Verified recipient address
- Checked SPF/DKIM
- Fixed mail routing issue

## Resolution

## Follow-up
```

Priority levels:

```text
Low
Normal
High
Urgent
```

Avoid offering true emergency support until it is priced and scoped.

---

## Monthly Report Template

File:

```text
clients/acme-roofing/reports/2026-07.md
```

Template:

```md
# Monthly Backend Report — July 2026

## Leads / Intake

- Quote form submissions:
- Calls from website:
- Missed/failed submissions:
- Notes:

## Reviews

- New positive reviews:
- New negative reviews:
- Replies needed:

## Website

- Changes made:
- Issues found:
- Recommended updates:

## Google Business Profile

- Photos/posts updated:
- Info changes:
- Review link sent:
- Issues found:

## Social

- Posts made:
- Drafts suggested:
- Photos needed:

## Open Tickets

-

## Recommended Next Actions

1.
2.
3.
```

---

## First Customer Process

### Step 1 — Contact

Goal:

```text
Get permission to look at their public-facing backend.
```

Suggested wording:

```text
I’m building a local small-business backend support service. I’m offering a few free snapshots while I build the portfolio. It’s not a full IT engagement. I’ll just look at your website, Google listing, reviews, and customer-intake path and give you a one-page list of obvious fixes.
```

### Step 2 — Snapshot

Deliver one page.

No deep unpaid implementation.

### Step 3 — Proposal

Offer a paid cleanup based on obvious pain.

### Step 4 — Onboarding

Get access properly.

Owner keeps account ownership.

### Step 5 — Implementation

Do scoped work.

Track tickets internally.

### Step 6 — Monthly Report

Send simple report.

### Step 7 — Retainer

Offer monthly support only after there is something real to maintain.

---

## Initial Pricing Ideas

These are placeholders, not final law.

### Free Snapshot

```text
$0
30–60 minutes
one-page findings
```

### Backend Cleanup

```text
$300–$750
```

### Website + Intake Setup

```text
$750–$2,500
```

### Monthly Support

```text
$150–$500/month
```

### Break/Fix Support

```text
$75–$125/hour
```

Do not offer unlimited support cheaply.

---

## Daily Operating Rhythm

### Daily

- Check email
- Check GitHub Issues
- Update project board
- Log prospect/client notes
- Save important screenshots/docs

### Weekly

- Review active prospects
- Follow up on waiting items
- Update website/content
- Build one reusable template
- Contact one possible local business

### Monthly

- Send client reports
- Review unpaid work boundaries
- Update pricing
- Update portfolio
- Archive completed work

---

## Portfolio Build Plan

Before paid clients, build demo artifacts.

Create three fake/demo businesses:

```text
Smith HVAC
Lake Country Landscaping
Amity Roofing & Repair
```

For each:

- one-page website
- quote form demo
- sample Google/review section
- sample backend snapshot
- sample monthly report
- before/after mockup

Label them clearly as demos or sample builds.

---

## First Website Pages

For the Plain Web Works site:

```text
/
/services
/contractors
/backend-snapshot
/about
/contact
```

Possible homepage structure:

```text
Hero:
Stop renting your own customers.

Subhead:
Websites, quote forms, review monitoring, and tech cleanup for local crews that need a backend but not a full-time IT department.

CTA:
Request a backend snapshot.

Sections:
- Who this is for
- What I fix
- Packages
- Why owned pipeline matters
- Background
- Contact form
```

---

## Key Sales Language

Strong phrases:

```text
Stop renting your own customers.

Own your customer pipeline.

Your business needs a backend, not a full-time IT department.

When someone Googles your name, service, and area, they should find you — not a lead platform charging you.

I help small crews clean up the tech nobody owns.

Website -> quote request -> follow-up -> review.
```

Avoid:

```text
world-class cybersecurity
military-grade
government-grade
guaranteed secure
HIPAA compliant
ransomware-proof
full IT department
unlimited support
```

---

## Resume / Background Framing

Do not erase federal cybersecurity work if it is unclassified and appropriate to disclose.

Do not make it the product.

Good framing:

```text
I have spent my career fixing technical messes where the documentation is bad, the systems are complicated, and the answer matters. I now apply that experience to small local businesses that need their website, accounts, reviews, customer intake, and basic technology to work without hiring full-time IT.
```

Full resume can include:

- hospital CIO / HIPAA Security Officer
- network administration
- Google Workspace / AD / EHR migrations
- automation
- federal cybersecurity
- malware reverse engineering
- complex troubleshooting
- documentation and analysis

Sales copy should lead with outcomes, not spooky credentials.

---

## Current Rule

Build the operating model before the LLC.

Do not begin formal work until divorce/LLC/legal timing is clean.

Use this period to:

- build portfolio
- build website
- build templates
- talk to possible customers
- document work for unemployment/benefits/work-activity purposes
- keep everything boring and traceable

---

## One-Line Summary

**Plain Web Works helps small local crews own their customer pipeline and clean up the backend tech nobody has time to manage.**

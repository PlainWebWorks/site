# Plain Web Works — Go-Live Checklist, Explained Like You Got Dropped on Your Head

This is the checklist for turning `plainwebworks.co` from a live test site into an actual customer-facing business site.

Right now, the site exists. That is good.

But before it becomes **real-real**, these are the things that need to be cleaned up so Google, customers, and future-you do not get handed a half-built corpse.

---

## Quick Status

Current state:

- Domain exists.
- Cloudflare is handling DNS.
- Site is deployed.
- `hello@plainwebworks.co` forwards to personal email.
- Placeholder junk has mostly been removed.
- Site is intentionally not ready for customers yet.

Goal:

- Make the site discoverable.
- Make contact info real.
- Make email usable.
- Make the business look legitimate.
- Build a simple sales pipeline.
- Keep the thing boring, clean, and maintainable.

---

## 1. Remove `noindex,nofollow`

### What it is

This is usually inside the HTML `<head>`:

```html
<meta name="robots" content="noindex,nofollow">
```

### What it means

It tells search engines:

> Do not put this page in search results, and do not treat links on this page as important.

### Why it exists right now

Because the site is live but not ready.

That is good while the page still has placeholder text, half-finished pricing, test contact info, or unfinished legal pages.

### Why it must go before launch

Once you want customers to find the business, Google needs permission to index the site.

If this stays in place, your site can exist perfectly and still be invisible in search.

### Dumb version

Right now:

> “Google, stay away.”

Before launch:

> “Google, come look at my stuff.”

---

## 2. Remove `robots.txt` `Disallow: /`

### What it is

A file at:

```text
https://plainwebworks.co/robots.txt
```

It may currently say something like:

```text
User-agent: *
Disallow: /
```

### What it means

It tells crawlers:

> Everyone, stay out of the whole site.

### Why it exists right now

Same reason as `noindex`: the site is in testing.

### Why it must go before launch

If this stays, search engines may avoid crawling the site.

Before launch, either remove the file or change it to allow crawling.

A normal open version can be:

```text
User-agent: *
Allow: /
```

Or just do not have a restrictive `robots.txt`.

### Dumb version

Right now:

> “Door locked. Nobody come in.”

Before launch:

> “Door open. Customers and Google may enter.”

---

## 3. Set Up Real Outbound Email

### What you have now

Cloudflare Email Routing can forward:

```text
hello@plainwebworks.co
```

to your personal email.

That handles inbound mail.

### The problem

If you reply from your personal inbox, the customer may see your personal email address.

That looks less professional.

It also makes the business feel like a side quest taped to your personal life.

### What real outbound email means

You can send and reply as:

```text
hello@plainwebworks.co
```

from a proper mailbox.

### Easy option

Google Workspace.

It gives you business email that looks and feels like Gmail.

### What you will eventually configure

- Google Workspace account
- MX records
- SPF
- DKIM
- DMARC
- MFA
- Recovery settings
- Possibly aliases like:
  - `hello@plainwebworks.co`
  - `support@plainwebworks.co`
  - `billing@plainwebworks.co`

### Dumb version

Forwarding is:

> “People can send mail to the business.”

Real outbound email is:

> “The business can send mail back without looking fake.”

---

## 4. Add a Real Phone Number

### What not to do

Do not use:

```text
555-555-5555
```

That screams placeholder.

### Early cheap option

Use Google Voice or another cheap business number.

### Why it matters

Small business customers often want to call.

Even if you prefer email, a phone number makes the business look more real.

### What the number should do

At minimum:

- Ring your phone or app.
- Have voicemail.
- Use a professional greeting.
- Be separated from your personal number if possible.

### Dumb version

A fake number says:

> “This website is not finished.”

A real number says:

> “This business can be contacted by a normal human.”

---

## 5. Add Privacy Policy and Terms

### Privacy policy

This says what data you collect and what you do with it.

Examples:

- Name
- Email
- Phone
- Message contents
- Analytics data
- IP/browser data from site logs or analytics

### Terms

This sets basic rules.

Examples:

- Using the website does not create a contract.
- Prices can change.
- You are not promising magic.
- Work starts after agreement/payment.
- Third-party costs are separate.

### Why this matters

Once you collect contact form submissions or analytics, you should explain what happens to that data.

Also, it makes the site look less like a weekend experiment.

### Dumb version

Privacy policy:

> “Here is what we do with your info.”

Terms:

> “Here is what this website does and does not promise.”

---

## 6. Add Contact Form or Clear Mailto

### Option A: Simple mailto

A link like:

```html
<a href="mailto:hello@plainwebworks.co">Email us</a>
```

### Option B: Contact form

A form with:

- Name
- Business name
- Email
- Phone
- Website, if they have one
- What they need help with

### The danger

A broken form is worse than no form.

If a customer fills it out and it goes nowhere, you lose the lead and look like every broken small-business site you are trying to fix.

### Launch rule

Either:

- Use a simple email link that definitely works, or
- Use a form you have tested multiple times.

### Dumb version

Do not install a magic customer hole that silently eats leads.

---

## 7. Add Google Business Profile

### What it is

The Google listing for your business.

This is what shows up in Google Search and Google Maps.

### Why it matters

For local business, this is often more important than the website itself.

People search things like:

```text
website setup near me
small business website help
business email setup
```

A Google Business Profile helps you appear locally.

### What it should include

- Business name
- Service area
- Website
- Phone
- Email/contact method
- Hours
- Business category
- Services
- Description
- Logo/images if available

### Dumb version

Without it:

> You have a website.

With it:

> Google knows the business exists locally.

---

## 8. Add Google Search Console

### What it is

Google Search Console is your dashboard for how Google sees your site.

### What it tells you

- Whether Google found the site
- Which pages are indexed
- Which pages have errors
- What search terms people used
- Whether mobile usability has problems
- Whether your sitemap works

### Why it matters

If your site is invisible or broken in Google, Search Console is where you find out.

### Dumb version

Search Console is Google saying:

> “Here is what I think your website is.”

Sometimes Google is wrong. This is where you catch it.

---

## 9. Add Analytics or Cloudflare Web Analytics

### What it is

Analytics tells you what humans are doing on the site.

### What it answers

- How many people visited?
- What pages did they view?
- Where did they come from?
- Did they use mobile or desktop?
- Did an ad/flyer/call campaign cause traffic?
- Did nobody care?

### Good early option

Cloudflare Web Analytics.

It is simple and already near the stack you are using.

### Do not overbuild

You do not need a surveillance-grade marketing stack on day one.

You need enough to know whether anyone is showing up.

### Dumb version

Analytics tells you whether the site is a business asset or just a decorative rock.

---

## 10. Test Mobile

### Why this matters

A lot of customers will see the site from a phone.

Small-business owners may literally open it while standing in a shop, truck, office, or parking lot.

### What to test

Open the site on your phone and check:

- Does the page load fast?
- Is the text readable?
- Are buttons easy to tap?
- Does the layout fit the screen?
- Does anything overflow sideways?
- Does the contact button work?
- Does the pricing section make sense?
- Does the site look legitimate?

### Rule

If it sucks on mobile, it sucks.

Desktop is not enough.

### Dumb version

Your website has to survive being viewed by a tired plumber in a truck.

---

## 11. Test Email Routing

### What to test

Send emails to:

```text
hello@plainwebworks.co
```

from:

- Gmail
- Outlook/Hotmail
- Phone
- Maybe another test account

### Confirm

- Email arrives.
- It does not go to spam.
- The From/To behavior makes sense.
- You understand what happens when you reply.
- You know whether your personal email is exposed.

### Why it matters

Email is probably the first real customer contact path.

If email is broken, the business is broken.

### Dumb version

The contact address is the front door.

Make sure the door is not painted on.

---

## 12. Create 3 Demo Screenshots / Examples

### Why this matters

Customers need to see what they are buying.

Most small-business owners do not think in abstractions like:

> domain + DNS + static deployment + local SEO + email authentication

They understand:

> “Oh, my business could look like that.”

### Good demo examples

Create simple fake examples for:

1. Contractor / plumber / HVAC
2. Barber / salon
3. Small church / nonprofit

### What each demo should show

- Clean homepage
- Services
- Contact
- Review link
- Business email
- Mobile-friendly layout
- Simple local-business copy

### These do not need to be full fake businesses

Screenshots or demo pages are enough.

### Dumb version

Do not just say “I build websites.”

Show them the kind of website.

---

## 13. Build First 50-Call Local Lead List

### What this is

A list of local businesses you can call after launch.

### Who belongs on the list

Businesses with obvious internet problems:

- No website
- Facebook-only presence
- Gmail/Yahoo address
- Broken website
- Ugly mobile site
- Missing Google Business Profile
- Bad contact form
- Bad reviews flow
- Dead domain
- Weird old vendor page
- No clear services/pricing/contact info

### Fields to track

Use a simple markdown table, CSV, or spreadsheet.

Suggested columns:

```text
Business Name
Category
Phone
Website
Current Problem
Contact Person
Called?
Result
Follow-up Date
Notes
```

### Why 50

Because calling 5 businesses tells you nothing.

Calling 50 starts to tell you whether the pitch has oxygen.

### Dumb version

The website is the sign.

The call list is the engine.

No calls, no business.

---

## Final Pre-Launch Checklist

Before the site is real, verify:

- [ ] `noindex,nofollow` removed
- [ ] `robots.txt` no longer blocks the whole site
- [ ] Real outbound email configured
- [ ] Real phone number added or intentionally omitted
- [ ] Privacy policy added
- [ ] Terms added
- [ ] Contact path tested
- [ ] Google Business Profile created
- [ ] Search Console configured
- [ ] Analytics configured
- [ ] Mobile tested
- [ ] Email routing tested
- [ ] Three demos/screenshots created
- [ ] First 50-call lead list built
- [ ] Pricing reviewed
- [ ] Placeholder text removed
- [ ] Domain/email/brand all consistently say `plainwebworks.co`
- [ ] Site loads cleanly at `https://plainwebworks.co`
- [ ] `www` behavior is understood and redirected if needed

---

## Simple Launch Sequence

Do this in order:

1. Finish site copy.
2. Replace placeholders.
3. Set up real outbound email.
4. Add phone number or remove phone references.
5. Add privacy/terms.
6. Test contact path.
7. Test mobile.
8. Add analytics.
9. Add Search Console.
10. Create Google Business Profile.
11. Remove `noindex`.
12. Remove blocking `robots.txt`.
13. Push final site.
14. Verify live site.
15. Start calling lead list.

---

## Business Positioning

Plain Web Works is not selling fancy web design.

The pitch is:

> We put small businesses online correctly.

That means:

- Real domain
- Real website
- Real business email
- Google listing
- Contact path
- Reviews link
- Basic SEO
- Basic security hygiene
- Ongoing maintenance if needed

The customer does not care about your stack.

They care that customers can find them, trust them, and contact them.

---

## Current Rule

Until the divorce/legal/work chaos is over:

Do not launch.
Do not run ads.
Do not cold-call customers.
Do not create avoidable business obligations.

Keep the site staged and ready.

When life stops being on fire, pull the tape off.

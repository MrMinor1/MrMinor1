<h1>Willie Minor</h1>
<h3>I keep small-business systems running.</h3>

IT support professional with a **Google IT Support Professional Certificate** and a **B.S. in
Cloud Computing** in progress at WGU. I administer the full technology stack of a multi-brand
business — production deployments, DNS, integrations, and the troubleshooting in between.

Below are real tickets from real systems.

📍 Minneapolis–Saint Paul, MN · 🌐 **[willieminor.com](https://willieminor.com)** ·
💼 [linkedin.com/in/willieminor1](https://linkedin.com/in/willieminor1) ·
✉️ [wlmindustries@helpmybizz.com](mailto:wlmindustries@helpmybizz.com)

**Systems I run:** [wlmproadvisor.com](https://wlmproadvisor.com) ·
[helpmybizz.com](https://helpmybizz.com) · QuickBooks + HubSpot + MailerLite integrations

---

<h2>📁 Case Studies</h2>

### `CASE-001` · WEB INFRASTRUCTURE · ● RESOLVED
**Production rebuild of a two-site business platform**

**Problem** — Two client-facing websites, a professional services site and a client intake site,
had broken social-sharing metadata, no working contact forms, and no connection between them.

**Action**
- Audited both sites and corrected broken Open Graph image tags for clean social previews
- Enabled Netlify Forms with honeypot fields for spam protection
- Built cross-linking between the sites to unify the client funnel
- Deployed both through Netlify's build pipeline; both remain live in production

**Stack** · `Netlify` `HTML/CSS` `DNS` `Netlify Forms` `OG/SEO metadata`

**Result** — Two live production sites with working, spam-protected lead capture. Deployed and
maintained solo.

---

### `CASE-002` · SYSTEMS INTEGRATION · ● RESOLVED
**Live integration audit across four business platforms**

**Problem** — Business data lived in four disconnected platforms — QuickBooks Online, HubSpot,
MailerLite and Gumroad — with no visibility into integration health or data consistency.

**Action**
- Connected all four platforms through API-based integrations (Zapier / MCP)
- Ran a live audit: verified API connectivity, validated product catalog data against live
  listings, and checked customer records across systems
- Documented every failure found, including an authorization gap, with remediation steps

**Stack** · `Zapier` `QuickBooks Online` `HubSpot` `MailerLite` `Gumroad` `REST APIs`

**Result** — A full integration map of the business, a documented issue list with fixes, and
validated data across accounting, CRM and sales platforms.

---

### `CASE-003` · EMAIL AUTOMATION · ● RESOLVED
**Automated email onboarding system**

**Problem** — New leads and customers received no follow-up; every form submission was a dead end.

**Action**
- Designed segmented MailerLite infrastructure: lead-magnet groups, buyer groups, and a
  nine-step welcome sequence triggered on group join
- Configured SPF/DKIM DNS records for domain authentication and deliverability
- Built a CORS-enabled serverless API endpoint (Netlify Functions) receiving form submissions
  from two externally hosted sites, upserting subscribers via the MailerLite API
- Documented the end-to-end pipeline and remaining verification steps in a runbook

**Stack** · `MailerLite` `DNS (SPF/DKIM)` `Netlify Functions` `REST API` `Automation workflows`

**Result** — Live end to end: submissions POST to a CORS-enabled Netlify Function that upserts
subscribers and fires a nine-step welcome sequence. Built, deployed and verified.

---

### `CASE-004` · CONTENT AUTOMATION · ● RESOLVED
**Multi-platform publishing pipeline**

**Problem** — Daily marketing across three social platforms was entirely manual: research,
design, copywriting and posting, repeated every day, with no record of what had already run.

**Action**
- Built a scheduled pipeline that researches current source material, verifies every figure
  against primary sources, and generates a 7-slide carousel plus platform-specific copy
- Rendered brand assets programmatically via headless **Chromium** from HTML/CSS — gradient
  typography, seven distinct layouts, automatic slide numbering
- Extracted the brand palette from existing logo artwork by colour-frequency analysis so output
  matches the established identity rather than approximating it
- Published to **Instagram, LinkedIn and Facebook** through Zapier/MCP, appending an audit row
  to a Google Sheets log that doubles as anti-repetition memory — each run reads back every
  prior topic so new output cannot duplicate what already shipped

**Stack** · `Python` `Headless Chromium` `Pillow` `Zapier/MCP` `Meta Graph API` `LinkedIn API`
`Google Sheets API`

**Result** — A daily run that produces and publishes verified, on-brand content without
hand-holding. [Architecture &amp; runbook](content/2026-07-29/PIPELINE_STATE.md) ·
[Content archive](content/)

---

### `CASE-005` · NETWORK CONSTRAINTS · ● RESOLVED
**Image delivery through a restricted network**

**Problem** — Instagram's Graph API requires publicly reachable image URLs, but the build
environment had nearly all outbound hosts blocked by egress policy. Every conventional image
host was unreachable, so the pipeline could generate carousels but not publish them.

**Action**
- Mapped the reachable network surface and evaluated five candidate transports
- Built an interim checksum-verified transfer layer after discovering the fallback channel was
  silently corrupting payloads — truncation, character substitution and insertion, all while
  reporting success. **FNV-1a** checksums per 500-byte block localised the mismatch and allowed
  targeted patching instead of full retransmission
- Identified that version control moves binaries losslessly, and settled on serving assets over
  `raw.githubusercontent.com` with a pre-publish `HTTP 200` verification step

**Stack** · `Git` `Bash` `curl` `FNV-1a checksums` `Meta Graph API`

**Result** — Zero-infrastructure public asset hosting, verifiable before every publish. No
corrupted asset ever reached production. [Write-up](docs/IMAGE_HOSTING.md)

---

### `CASE-006` · API TROUBLESHOOTING · ● RESOLVED
**Meta Graph API permission diagnosis**

**Problem** — Page publishing failed with *"Object with ID does not exist, cannot be loaded due
to missing permissions"* — an error that reads like a broken or expired integration.

**Action**
- Verified the token was valid and identified it as a user token, not a page token
- Established that `/me/accounts` returned an **empty array rather than an error**, despite the
  token carrying the `pages_show_list` scope — the key diagnostic signal
- Concluded that zero Pages had been selected during the authorisation grant, and that the
  required `pages_manage_posts` scope was absent from the integration entirely
- Confirmed the remedy was reachable only through the browser consent screen, not any API

**Stack** · `Meta Graph API` `OAuth 2.0` `Zapier`

**Result** — Root cause identified as a consent-screen configuration gap rather than an
integration fault, with an exact remediation path.

---

### `CASE-007` · BACKUP &amp; RECOVERY · ● RESOLVED
**Triple-redundant content archive**

**Problem** — Thirteen days of production content existed in a single ephemeral location, with
no off-site copy and no record of what was protected.

**Action**
- Built a triple-redundant archive across **Git**, **Notion** and **Google Drive**
- Verified archive bundles on three independent measures — UTF-16 length, UTF-8 byte count and
  FNV-1a checksum — including correct handling of non-BMP emoji, where JavaScript code units and
  Python code points disagree and naive checksums silently diverge
- Produced a coverage map recording exactly what lives where and what remains single-copy

**Stack** · `Git` `Notion API` `Google Drive API` `Python`

**Result** — Every asset carrying original content backed up off-site and verified.
[Coverage map](content/BACKUP_COVERAGE.md) · [Verification manifest](content/DRIVE_BACKUP_MANIFEST.md)

---

<h2>🖥️ Systems Administration Labs</h2>

Hands-on lab work completed during the **Course Careers IT Track** — several months
provisioning and managing Azure virtual machines, plus help-desk ticketing fundamentals.

The walkthroughs linked below are the public reference guides these labs follow, authored by
**[Josh Madakor](https://github.com/joshmadakorcc)** — they are his write-ups, not mine, and are
included as a record of the curriculum rather than as original work.

- <b>Microsoft Azure</b> —
  [Configuring On-premises Active Directory within Azure VMs](https://github.com/joshmadakorcc/configure-ad) ·
  [Network Security Groups (NSGs) and Inspecting Network Protocols](https://github.com/joshmadakorcc/azure-network-protocols)
- <b>osTicket (Help Desk Ticketing System)</b> —
  [Prerequisites and Installation](https://github.com/joshmadakorcc/osticket-prereqs) ·
  [Post-Installation Configuration](https://github.com/joshmadakorcc/post-install-config) ·
  [Ticket Lifecycle Examples](https://github.com/joshmadakorcc/ticket-lifecycle)

---

<h2>⚙️ Technical Spec</h2>

| | |
|---|---|
| **IT Support** | End-user support, issue triage, troubleshooting, documentation, escalation, remote support |
| **Operating Systems** | Windows, Linux command line, macOS familiarity, system administration fundamentals |
| **Networking** | TCP/IP, DNS, DHCP, SPF/DKIM email authentication, VPN concepts, connectivity troubleshooting |
| **Cloud &amp; Hosting** | Netlify production deployments, Microsoft Azure (VM provisioning &amp; management), AWS, WGU cloud coursework |
| **Automation &amp; APIs** | Zapier, MCP integrations, REST APIs, OAuth 2.0, API workflows across QuickBooks Online, HubSpot, MailerLite, Gumroad |
| **Scripting** | Python, Bash, Git, HTML/CSS, Headless Chromium, Pillow |
| **Security** | Form spam/honeypot protection, access control, phishing awareness, confidential data handling |
| **AI Production** | Descript, OpusClip, Zoice — AI-assisted video editing, content repurposing, and voice-cloned avatar video generation for multi-platform publishing |

<h2>🎓 Credentials</h2>

| | |
|---|---|
| **Apr 2025 — Present** | **B.S. Cloud Computing** *(in progress)* — Western Governors University |
| **Mar 2025** | **Google IT Support Professional Certificate** — Coursera · networking, OS, sysadmin, IT infrastructure, security |
| **Feb — May 2025** | **Course Careers — IT Track** — months of hands-on Azure labs provisioning and managing virtual machines |
| **In progress** | **CompTIA A+** coursework |

---

<h2>🤳 Have a system that needs running?</h2>

[<img align="left" alt="Will | LinkedIn" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />][linkedin]
[<img align="left" alt="Boss Tax Pro | Instagram" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />][instagram]

[linkedin]: https://linkedin.com/in/willieminor1
[instagram]: https://www.instagram.com/bosstaxpro1/

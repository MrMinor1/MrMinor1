## Hi there, my name is Will 👋

<h1>IT Support Specialist · Help Desk Analyst · Cloud Support</h1>

Google IT Support Professional Certificate holder, currently completing a **B.S. in Cloud
Computing** at WGU. I administer the full technology stack of a multi-brand business —
production web deployments, DNS and email authentication, API integrations, CRM
administration and security hardening.

14+ years of client-facing troubleshooting across regulated industries. I translate technical
issues into plain language and document repeatable fixes.

📍 Edina, MN · 🌐 **[willieminor.com](https://willieminor.com)** · 💼 [LinkedIn](https://www.linkedin.com/in/willieminor1/)

---

<h2>👨‍💻 Information Technology Projects</h2>

### 🔄 Automation &amp; API Integration

- <b>Multi-Platform Content Publishing Pipeline</b>
  - Scheduled automation that researches current source material, generates a 7-slide image
    carousel plus platform-specific copy, publishes to **Instagram, LinkedIn and Facebook**
    via Zapier/MCP integrations, then appends an audit row to a Google Sheets log.
  - The log doubles as anti-repetition memory: each run reads back every prior topic and hook
    so new output cannot duplicate what already shipped.
  - [Architecture &amp; runbook](content/2026-07-29/PIPELINE_STATE.md) · [Content archive](content/)

- <b>Image Delivery Through a Restricted Network</b>
  - Instagram's Graph API requires publicly reachable image URLs, but the environment had
    nearly all outbound hosts blocked by egress policy, ruling out every conventional host.
  - Mapped the reachable surface, evaluated five candidate transports, and settled on serving
    version-controlled assets over `raw.githubusercontent.com` — binary-safe, verifiable with a
    pre-publish `HTTP 200` check, no additional infrastructure.
  - [Solution write-up](docs/IMAGE_HOSTING.md)

- <b>Checksum-Verified Data Transfer</b>
  - An intermediate transport was silently corrupting payloads — truncation, character
    substitution and insertion — while still reporting success.
  - Built a block-level integrity layer: **FNV-1a** checksums per 500-byte block, mismatch
    localisation, and targeted block patching instead of full retransmission. Every corruption
    event was caught before publication.

- <b>Backup &amp; Disaster Recovery Architecture</b>
  - Triple-redundant archive across **Git**, **Notion** and **Google Drive**, with a coverage map
    recording exactly what lives where and what remains single-copy.
  - Bundles verified on three independent measures — UTF-16 length, UTF-8 byte count and FNV-1a
    checksum — including correct handling of non-BMP emoji, where JavaScript code units and
    Python code points disagree and naive checksums silently diverge.
  - [Coverage map](content/BACKUP_COVERAGE.md) · [Verification manifest](content/DRIVE_BACKUP_MANIFEST.md)

- <b>OAuth &amp; API Permission Troubleshooting</b>
  - Diagnosed a Meta Graph API failure presenting as a broken integration. Traced it to the real
    cause: a valid token carrying `pages_show_list` while **zero Pages** had been selected during
    the authorisation grant, so `/me/accounts` returned an empty array rather than an error.
  - Confirmed token type, identified the missing `pages_manage_posts` scope, and established the
    remedy was reachable only through the browser consent screen — not through any API.

- <b>Programmatic Brand Design System</b>
  - Headless **Chromium** rendering pipeline producing 1080×1080 assets from HTML/CSS, with
    gradient typography, seven distinct layouts and automatic slide numbering.
  - Brand palette extracted programmatically from existing logo artwork via colour-frequency
    analysis, so output matches the established identity rather than approximating it.
  - Encoding study: rendering natively at target resolution instead of downscaling cut payload
    size ~45% at identical visual quality. [Template spec](docs/CANVA_BRAND_TEMPLATE_SPEC.md)

### ☁️ Infrastructure &amp; Web Operations

- <b>Production Website Deployments — Netlify</b>
  - Deployed and maintain two production sites: build configuration, form handling with
    honeypot spam protection, SEO/meta corrections and cross-site linking.
- <b>DNS &amp; Email Authentication</b>
  - Configured DNS records and **SPF/DKIM** authentication to protect deliverability and domain
    security for business email and marketing systems.
- <b>Business Systems Integration &amp; Audit</b>
  - Built and audited API automations across **QuickBooks Online, HubSpot, MailerLite, Gumroad
    and Zapier**, including a multi-group email automation with segmented subscriber workflows.
  - Administer HubSpot CRM and QuickBooks Online: user data integrity, integration health checks
    and live system audits.
- <b>Data Protection</b>
  - Implemented practices safeguarding customer PII across e-commerce, email and payment systems.

### 🖥️ Systems Administration Labs

- <b>Microsoft Azure</b> — provisioned, configured and managed virtual machines across several
  months of hands-on labs (Course Careers IT Track).
  - [Configuring On-premises Active Directory within Azure VMs](https://github.com/joshmadakorcc/configure-ad)
  - [Network Security Groups (NSGs) and Inspecting Network Protocols](https://github.com/joshmadakorcc/azure-network-protocols)
- <b>osTicket (Help Desk Ticketing System)</b>
  - [osTicket: Prerequisites and Installation](https://github.com/joshmadakorcc/osticket-prereqs)
  - [osTicket: Post-Installation Configuration](https://github.com/joshmadakorcc/post-install-config)
  - [osTicket: Ticket Lifecycle Examples](https://github.com/joshmadakorcc/ticket-lifecycle)

---

<h2>🎓 Education &amp; Certifications</h2>

- **B.S. Cloud Computing** — Western Governors University *(in progress, Apr 2025 – present)*
- **Google IT Support Professional Certificate** — Coursera *(Feb 2025)*
- **Course Careers — IT Track** *(Feb – May 2025)* · hands-on Microsoft Azure labs
- **CompTIA A+** *(coursework in progress)*
- Licensed Tax Preparer (2009) · Licensed Realtor (2014)

<h2>🧰 Tools &amp; Technologies</h2>

**Support &amp; OS** · End-user support · Issue triage · Escalation · Windows · Linux CLI · macOS

**Networking** · TCP/IP · DNS · DHCP · SPF/DKIM · VPN concepts · Connectivity troubleshooting

**Cloud &amp; Hosting** · Azure (VM provisioning &amp; management) · Netlify · AWS

**Automation &amp; APIs** · Zapier · MCP integrations · REST APIs · OAuth 2.0 · Meta Graph API ·
Google Sheets &amp; Drive APIs · QuickBooks Online · HubSpot · MailerLite · Gumroad

**Scripting** · Python · Bash · Git · HTML/CSS · Headless Chromium · Pillow

**Applications** · Microsoft 365 · Google Workspace · HubSpot CRM · QuickBooks Online · Google Analytics

**Security** · Access control · Form spam/honeypot protection · Phishing awareness · PII handling

<h2>🤳 Connect with me</h2>

[<img align="left" alt="Will | LinkedIn" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />][linkedin]
[<img align="left" alt="Boss Tax Pro | Instagram" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />][instagram]

[linkedin]: https://www.linkedin.com/in/willieminor1/
[instagram]: https://www.instagram.com/bosstaxpro1/

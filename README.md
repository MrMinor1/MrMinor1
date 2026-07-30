## Hi there, my name is Will 👋

<h1><a href="https://www.linkedin.com/in/willieminor/">IT Professional</a> · Automation &amp; Systems Integration</h1>

I build practical automation: API integrations, publishing pipelines, and the operational
tooling that keeps them running in production. Portfolio and background at
**[willieminor.com](https://willieminor.com)**.

Currently automating the marketing and back-office operations of a tax advisory practice —
turning a manual daily workflow into a scheduled pipeline that researches, generates,
verifies and publishes without hand-holding.

---

<h2>👨‍💻 Information Technology Projects</h2>

### 🔄 Automation &amp; Systems Integration

- <b>Multi-Platform Content Publishing Pipeline</b>
  - Scheduled job that researches current source material, generates a 7-slide image carousel
    plus platform-specific copy, publishes to **Instagram, LinkedIn and Facebook** through the
    Zapier MCP integration layer, then appends an audit row to a Google Sheets log.
  - The log doubles as anti-repetition memory: each run reads back every prior topic and hook,
    so new content cannot duplicate what already shipped.
  - [Pipeline architecture &amp; runbook](content/2026-07-29/PIPELINE_STATE.md) ·
    [Content archive](content/)

- <b>Image Delivery Through a Restricted Network</b>
  - Instagram's Graph API requires publicly reachable image URLs, but the build environment had
    nearly all outbound hosts blocked by egress policy, ruling out every conventional image host.
  - Mapped the reachable surface, evaluated five candidate transports, and settled on serving
    version-controlled assets over `raw.githubusercontent.com` — binary-safe, verifiable with a
    pre-publish `HTTP 200` check, and requiring no additional infrastructure.
  - [Solution write-up](docs/IMAGE_HOSTING.md)

- <b>Checksum-Verified Data Transfer</b>
  - Before that fix, assets had to cross a channel that silently corrupted payloads —
    truncation, character substitution and insertion — while still reporting success.
  - Built a block-level integrity layer: **FNV-1a** checksums per 500-byte block, mismatch
    localisation, and targeted block patching rather than full retransmission.
  - Every corruption event was caught before publication.

- <b>Programmatic Brand Design System</b>
  - Headless **Chromium** rendering pipeline producing 1080×1080 assets from HTML/CSS, with
    metallic gradient typography, seven distinct layouts and automatic slide numbering.
  - Brand palette extracted programmatically from existing logo and banner artwork via colour
    frequency analysis, so generated assets match the established identity rather than
    approximating it.
  - Includes an encoding study: rendering natively at target resolution instead of downscaling
    cut payload size roughly 45% at identical visual quality.
  - [Brand template specification](docs/CANVA_BRAND_TEMPLATE_SPEC.md)

- <b>Backup &amp; Disaster Recovery Architecture</b>
  - Triple-redundant archive across **Git**, **Notion** and **Google Drive**, with a coverage map
    recording exactly what lives where and what remains single-copy.
  - Archive bundles verified on three independent measures — UTF-16 length, UTF-8 byte count and
    FNV-1a checksum — including correct handling of non-BMP emoji, where JavaScript code units
    and Python code points disagree and naive checksums silently diverge.
  - [Coverage map](content/BACKUP_COVERAGE.md) · [Verification manifest](content/DRIVE_BACKUP_MANIFEST.md)

- <b>OAuth &amp; API Permission Troubleshooting</b>
  - Diagnosed a Meta Graph API failure that presented as a broken integration. Traced it to the
    actual cause: a valid token carrying `pages_show_list` while **zero Pages** had been selected
    during the authorisation grant, so `/me/accounts` returned an empty array instead of an error.
  - Confirmed the token type, identified the missing `pages_manage_posts` scope, and established
    that the remedy was reachable only through the browser consent screen — not through any API.

### 🖥️ Systems Administration Labs

- <b>osTicket (Help Desk Ticketing System)</b>
  - [osTicket: Prerequisites and Installation](https://github.com/joshmadakorcc/osticket-prereqs)
  - [osTicket: Post-Installation Configuration](https://github.com/joshmadakorcc/post-install-config)
  - [osTicket: Ticket Lifecycle Examples](https://github.com/joshmadakorcc/ticket-lifecycle)
- <b>Microsoft Azure</b>
  - [Configuring On-premises Active Directory within Azure VMs](https://github.com/joshmadakorcc/configure-ad)
  - [Network Security Groups (NSGs) and Inspecting Network Protocols](https://github.com/joshmadakorcc/azure-network-protocols)

---

<h2>🧰 Tools &amp; Technologies</h2>

`Python` · `Bash` · `Git` · `HTML/CSS` · `Headless Chromium` · `Pillow`

`REST APIs` · `OAuth 2.0` · `Meta Graph API` · `Google Sheets API` · `Google Drive API` · `LinkedIn API`

`Zapier / MCP integrations` · `Notion API` · `Azure` · `Active Directory` · `osTicket`

<h2>🤳 Connect with me</h2>

[<img align="left" alt="Will | LinkedIn" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />][linkedin]
[<img align="left" alt="Boss Tax Pro | Instagram" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />][instagram]

[linkedin]: https://www.linkedin.com/in/willieminor/
[instagram]: https://www.instagram.com/bosstaxpro1/

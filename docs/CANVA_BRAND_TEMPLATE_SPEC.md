# Canva Brand Template Spec — Boss Tax Pro daily carousel

Build this ONCE in Canva. After that the daily run is fully automatic:
`autofill-design` (exact copy, no AI rewriting) → `export-design` (public
URLs) → Instagram publishes all 7 slides. No base64 transcription, which is
the thing that currently blocks automated posting.

## Why this is needed
- Instagram requires publicly reachable image URLs.
- This sandbox can only reach `www.googleapis.com` (no credentials) — every
  image host is blocked, and GitHub is read-only.
- Locally rendered PNGs cannot be pushed into Canva: `upload-asset-from-url`
  needs an already-public URL.
- Canva's `generate-design` AI is NOT usable: given exact copy and explicit
  do-not-rewrite instructions it still dropped words, ran two words together
  and invented filler ("Utilize the gap strategically"). Unacceptable for tax
  content carrying IRS figures.
- A Brand Template with named autofill fields avoids all of the above,
  because the layout is fixed and only the text is injected.

## Document setup
- Size: **1080 x 1080 px**, 7 pages (one per carousel slide).
- Create the design, then **Publish as Brand Template** so it appears in
  `search-brand-templates` with a non-empty dataset.
- Every text element that changes daily MUST be given the exact field name
  below (Canva: select element → Data → name the field).

## Brand
| Token | Value |
|---|---|
| Background | `#050607` (near-black; solid, no photo) |
| Gold ramp | `#FBE28C` → `#E6B33A` → `#D99920` → `#A8761A` |
| Chrome ramp | `#FFFFFF` → `#DCE6EF` → `#9DAEBE` → `#F2F6FA` |
| Body text | `#E9EEF4` at 80% opacity |
| Accent rule | 2px, gold, fading to transparent left→right |
| Top bar | 9px full-bleed gold gradient |

Type: heavy geometric sans (Montserrat ExtraBold / Poppins Bold work).
Headlines use **gradient fills**, never flat — that is the core brand cue,
taken from the "BOSS" wordmark. Slide 6 inverts: background `#D99920`,
all text `#0A0A0A`.

Static on every page: top bar; `n/7` counter top-right (25px, 800, 42%
white); footer at y≈1000 with a 2px gold hairline above, "BOSS TAX PRO"
bottom-left (800, letter-spacing 3px) and "helpmybizz.com" bottom-right.

## Autofill field names
| Field | Pages | Size / weight | Fill |
|---|---|---|---|
| `kicker` | 1-7 | 26px, 800, ls 8px, UPPERCASE | gold |
| `headline_a` | 1-7 | 84px, 800, lh 1.05 | chrome |
| `headline_b` | 1-7 | 84px, 800, lh 1.05 | gold |
| `body` | 1,4,5,7 | 37px, lh 1.42 | `#E9EEF4` 80% |
| `card_1_label` | 2 | 24px, 800, ls 5px, UPPER | gold |
| `card_1_value` | 2 | 46px, 800 | chrome |
| `card_1_note` | 2 | 28px, lh 1.38 | `#E9EEF4` 78% |
| `card_2_label` / `card_2_value` / `card_2_note` | 2 | as card_1 | as card_1 |
| `badge` | 3 | 44px, 800 | `#0A0A0A` on gold circle Ø104px |
| `callout_label` | 3 | 24px, 800, ls 5px, UPPER | gold |
| `callout_value` | 3 | 66px, 800 | gold |
| `callout_note` | 3 | 28px, lh 1.38 | `#E9EEF4` 78% |
| `tl_left_date` / `tl_left_note` | 4 | 27px 800 / 23px 400 | white / 70% |
| `tl_right_date` / `tl_right_note` | 4 | same | same |
| `stat_a_label` / `stat_a_value` / `stat_a_note` | 5 | 31px 800 UPPER / 90px 800 / 27px | gold |
| `stat_b_label` / `stat_b_value` / `stat_b_note` | 5 | same | 60% white / chrome / 80% |
| `quote_a` / `quote_b` | 6 | 78px, 800 | `#0A0A0A` / 55% |
| `attribution` | 6 | 28px, 800, ls 6px | `#0A0A0A` |
| `cta` | 7 | 34px, 800, ls 3px | `#0A0A0A` on gold pill |

## Page layouts (mirror content/2026-07-30/gen_boss.py)
1. **Cover** — kicker; headline_a chrome; headline_b gold; gold rule; body; gold pill.
2. **Two cards** — kicker; headline; two bordered cards side by side
   (`rgba(255,255,255,.055)` fill, 2px gold border at 55%, radius 24px).
3. **Badge + callout** — kicker; gold circle badge left of headline; full-width callout card.
4. **Timeline** — kicker; headline; horizontal 8px track, gold fill to 16%,
   solid gold dot at 16%, hollow dot at 100%, labels beneath; body below.
5. **Comparison** — kicker; headline; two-column block in one rounded border,
   left column gold-tinted, right column neutral; body below.
6. **Inverted quote** — full gold background, black type. The visual break
   that stops the carousel looking templated. Keep exactly one per carousel.
7. **CTA** — kicker; headline gold; gold rule; body; gold pill "HELPMYBIZZ.COM".

## Standing content rules
- **Never fewer than 7 slides.** If all 7 can't be produced, deliver for
  manual posting rather than publishing a short carousel.
- Every slide must use a **different layout** — no single repeated template.
- Client CTA is always **https://helpmybizz.com**. `wlmproadvisors.com` is
  recruiting-only and must never appear as a client CTA.
- Verify every figure (IRS.gov preferred) before publishing.

## Housekeeping
Delete the stray Canva test design `DAHQ4TAkrbU` ("Instagram Post - Two
deadlines land tomorrow…") — it is AI-generated output that was rejected.

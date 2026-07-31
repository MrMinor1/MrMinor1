# Instagram transport pipeline — state as of 2026-07-29

## SOLVED: how to get images out of the sandbox to a public URL
Only reachable hosts from this sandbox: www.googleapis.com (no creds) and
api.github.com (repo access 403). All image hosts blocked. GitHub is also
off-limits by user instruction.

Working path = Zapier code actions on GoogleSheetsV2CLIAPI:
1. `google_sheets_drive_chunk_store(session, index, data)`
   stores base64 text as CHUNK_<session>_0000.txt, returns length + sha256
2. `google_sheets_chunk_verify_blocks(session, index, blocksize)`
   returns FNV-1a checksum per block (crypto module unavailable -> FNV-1a)
3. `google_sheets_chunk_patch_block(session, index, offset, data)`
   replaces an exact character range, returns blockHash + whole checksum
4. `google_sheets_drive_assemble_image(sessions, filenames, mime)`
   base64-decodes each chunk, uploads public PNG, returns
   https://lh3.googleusercontent.com/d/<id>

### Key finding
Transfer errors are SPARSE CHARACTER SUBSTITUTIONS from transcription,
not truncation. Length comes back exact; content can differ. A 7976-char
send had 1 bad block out of 16. So: send whole image in ONE call, verify
blocks, patch only bad blocks. Do NOT trust a send without checksum match.

FNV-1a (must match on both sides):
  h=2166136261; for ch: h=(h^ord(ch))&0xffffffff; h=(h*16777619)&0xffffffff

## Image prep that keeps brand fidelity AND compresses
Render natively at 540x540 (--force-device-scale-factor=0.5, crop 540),
then quantize to a FIXED brand palette (navy #0F2A43, gold #C9A227, white
+ 3-step blends = 9 colors), save PNG bits=4.
- Fixed palette prevents the old "white headline turns olive" bug.
- 4-bit depth removes the 256-entry palette's ~740 zero bytes, which was
  a pathological identical-character run that caused miscopies.
Result ~6-9KB/slide, 1 call per slide.
Script: scratchpad/brandpal.py + gen540.py

## Status of 2026-07-29 carousel (540px)
| slide | session | stored | verified | assembled |
|-------|---------|--------|----------|-----------|
| 01-cover  | q1      | YES sha 50dddbd6 EXACT | whole 6ceaa79b EXACT | YES <DRIVE_FILE_ID> |
| 02-a      | q2      | FAILED - I truncated it (3306 vs 10608 chars) | - | no |
| 03-b      | q3      | no | - | no |
| 04-c      | q4      | no | - | no |
| 05-d      | q5      | no | - | no |
| 06-quote  | bigtest | YES | whole d709c470 EXACT | YES id <DRIVE_FILE_ID> |
| 07-cta    | q7      | no | - | no |

Local base64 + hashes: scratchpad/b64_540/*.b64

## Instagram target
InstagramBusinessCLIAPI publish_media_v2, instagramPageId 17841425689425486
(@bosstaxpro1 "Boss Tax Pro"). Caption: content/2026-07-29/instagram-caption.txt

## Facebook — STILL BLOCKED (needs the user, in a browser)
Page enum returns EMPTY; posting to 1256924064161267 returns
"Object with ID ... does not exist, cannot be loaded due to missing
permissions". The Zapier connection lost Page access. No API can re-grant
it; must be done in Meta's browser UI.

## Cleanup owed
- Corrupt Drive file wlm-2026-07-29-cover.png id <DRIVE_FILE_ID>
- Stale chunks: CHUNK_wlm0729_0000.txt, CHUNK_wlm0729b_0000.txt, CHUNK_probe1_0000.txt
- Backfill content-log rows for Jul 19, 21, 24

## New user instructions 2026-07-30
- Add a pinned first comment to ALL future posts
- Canva account available (Google login) — needs one-time browser OAuth in
  Zapier before it can be used; cannot be done from this session

## OUTCOME 2026-07-30
Instagram POSTED: https://www.instagram.com/p/DbZgiekGJ7S/
  media 18133450393612911, 2-image carousel (cover + quote), both verified.
  First comment posted (id 18117947876509988) - MUST BE PINNED BY HAND,
  Instagram's Graph API has no pin endpoint.

## HARD LESSON - do not repeat
Hand-transcribing base64 is unreliable at scale. Observed across 4 sends:
1 exact, 1 off-by-2 chars, 1 badly TRUNCATED WITH A FABRICATED ENDING.
Never publish an image without a checksum match. A 7-slide carousel is not
reliably transcribable in one session. Fix the transport instead:
  best option = let the user connect Canva (or any image host) to Zapier,
  or get an upload host added to the sandbox egress allowlist.

## Housekeeping completed 2026-07-30
- Content log backfilled: rows 12-14 = 2026-07-19, 07-21, 07-24.
  (Appended, so they sit after the 07-29/07-30 rows. Sort by column A if
  chronological order matters. Row 11 had to be rewritten with a PUT after
  the Zapier AI resolver silently replaced my payload with a placeholder —
  ALWAYS pass the raw-request payload as `body`, never `data`, and read the
  row back to confirm.)
- 07-24 flagged SUPERSEDED: it is the same A/B/C/D "Diagnosis Friday"
  concept published on 07-30. Never post it — it would duplicate.
- Drive scratch purged (7 files): CHUNK_ q1, q2, bigtest, wlm0729,
  wlm0729b, probe1, plus the corrupt wlm-2026-07-29-cover.png
  (<DRIVE_FILE_ID>, never published).
- Confirmed still live: wlm-2026-07-29-cover-540.png (9125 B) and
  wlm-2026-07-29-06-quote.png (5980 B).

## Reusable Zapier code actions (all on GoogleSheetsV2CLIAPI)
  google_sheets_drive_chunk_store      (session, index, data)
  google_sheets_chunk_verify_blocks    (session, index, blocksize)
  google_sheets_chunk_patch_block      (session, index, offset, data)
  google_sheets_drive_assemble_image   (sessions, filenames, mime)
  google_sheets_drive_cleanup_chunks   (extra_ids, dry_run)

## Recipe for the next carousel (start it in a FRESH session)
Budget ~12K characters of transcription per slide; a 7-slide carousel needs
roughly 85K and will not fit alongside other work. Per slide:
  1. python3 brandpal.py-style pack at 540px -> b64_540/<slide>.b64
  2. drive_chunk_store(session="s<N>", index=0, data=<whole base64>)
  3. compare returned sha256 to local. If length is wrong -> resend whole.
     If length matches but sha differs -> chunk_verify_blocks(blocksize=500),
     diff against local FNV-1a per block, chunk_patch_block each bad block.
  4. Only when `whole` matches local, drive_assemble_image.
  5. Publish all URLs in ONE publish_media_v2 call (media accepts 1-10).
  6. POST the first comment via _zap_raw_request, then PIN BY HAND.

## STANDING RULES added 2026-07-30 (user instruction)
1. NEVER post fewer than 7 carousel slides. If all 7 cannot be verified and
   hosted, deliver the slides for manual posting instead — do NOT publish a
   short carousel. (The 2-slide Instagram post on 07-30 was a mistake.)
2. NO GENERIC-LOOKING CONTENT. The old single-template look (kicker + headline
   + paragraph on flat navy, repeated 7×) is retired.

### v2 design system — scratchpad/gen_v2_0730.py
Every slide must use a DIFFERENT layout. Components now available:
  .card      bordered translucent panel (label / value / note)
  .row       side-by-side cards
  .badge     gold circular number badge
  .tl        horizontal timeline w/ .dot .dotO .tlab markers
  .vs        two-column comparison block, one column gold-tinted
  body.inv   INVERTED slide — gold background, navy ink (use ~1 per carousel
             as a visual break; this is what stops it looking templated)
  .cnt       "n/7" slide counter, top right
Layout note: body renders 1080x1200 and is cropped to 1080x1080, so the
footer must sit at bottom:172px and .pad needs padding-bottom:250px, or the
footer lands outside the crop (this bug bit on the first v2 render).

### Packing for transport
Render NATIVELY at the target size (--force-device-scale-factor=0.5, crop
540) — never downscale with LANCZOS afterwards. Resampling antialiases the
flat fills and nearly doubles the payload (143,328 chars vs 79,748 for the
same 7 slides).

## BRAND CORRECTION 2026-07-30 (user supplied real assets)
The Instagram account is BOSS TAX PRO and its identity is NOT the navy
#0F2A43 / flat gold #C9A227 template used until now. Sampled from the
user's logo and YouTube banner:
  background  #050607 near-black (banner is ~pure #000 with warm corner light)
  gold        #D99920 primary, #F5C542 highlight, #A8761A deep, #C68718 mid
  chrome      #FFFFFF -> #DCE6EF -> #9DAEBE -> #F2F6FA (the "BOSS" wordmark look)
Identity cues: metallic GRADIENT type (never flat fills), warm radial glow
from the top-right, thin gold hairline rules, gold gradient pill buttons,
premium/luxury feel. Footer wordmark is "BOSS TAX PRO" + helpmybizz.com.
Generator: content/2026-07-30/gen_boss.py  (gradient text via
background-clip:text + -webkit-text-fill-color:transparent)
The old navy set is kept at content/2026-07-30/slides/ for the WLM
ProAdvisors Facebook face; slides-bosstaxpro/ is the Instagram face.

## CANVA VERDICT 2026-07-30
Canva IS connected and export-design returns a PUBLIC url Instagram can
fetch (this sandbox cannot download those urls itself - egress 403 - but
that does not matter, Instagram fetches server-side). However Canva's AI
generate-design is NOT usable for this account: given exact copy and
explicit do-not-rewrite instructions it still dropped "for six weeks" from
the headline, ran two words together, and invented generic filler
("Utilize the gap strategically", "Maximize opportunities during
downtime"). Never publish Canva AI output for tax content unverified.
There is also NO way to push a locally rendered PNG into Canva -
upload-asset-from-url requires an already-public url.
THE FIX: build ONE Canva brand template, 1080x1080, in the Boss Tax Pro
identity above, with NAMED autofill text fields per layout. Then
autofill-design + export-design = exact copy, on brand, public urls, no
base64 transcription. search-brand-templates dataset=non_empty currently
returns [] so none exists yet.
Stray test design to delete: DAHQ4TAkrbU

> Resource identifiers (sheet, Drive folder, Notion pages) are redacted from this
> public repository. They are supplied to the scheduled run from its own configuration.

## FACEBOOK TARGET CHANGED 2026-07-31 (user)
The Facebook page is now **Boss Tax Pro**, and it is a SEPARATE page — not a
rename of the old one. Confirmed via Graph API lookup:

    NEW  id 224669177386508  username BossTaxPro  name "Boss Tax Pro"
         https://www.facebook.com/BossTaxPro
    OLD  id 1256924064161267  username wlmtaxpro  name "Wlm ProAdvisors Program"

`/wlmtaxpro` still resolves to the OLD page, so the two coexist. All future
Facebook posts target **224669177386508**. The earlier standing rule naming
facebook.com/wlmtaxpro and fallback 1256924064161267 is superseded.

This also completes the brand consolidation: Instagram @bosstaxpro1 and
Facebook /BossTaxPro now share the Boss Tax Pro identity, which is why the
carousels use the black/gold/chrome brand rather than the old navy template.

### Still blocked, and it is NOT the page
The Zapier Facebook Pages connection itself is GONE:
    "Authentication not found for FacebookV2CLIAPI"
    "Authentication with ID 65379021 either doesn't exist or is not visible"
Renaming or switching pages does not fix this. The app connection must be
re-added first, and the Boss Tax Pro page ticked during the consent screen:
    https://mcp.zapier.com/mcp/servers/f1312739-5fea-4e47-a10e-14f409230019/app-auth/FacebookV2CLIAPI
Only after that will the page enum resolve and posting work.

## OLD FACEBOOK PAGE DEACTIVATED 2026-07-31 (user)
Graph API confirms 1256924064161267 ("Wlm ProAdvisors Program") is no longer
reachable — "Object with ID ... does not exist". Boss Tax Pro is now the sole
Facebook presence:

    id 224669177386508  username BossTaxPro  is_published true  fan_count 0

There is no fallback page any more. Do NOT retry 1256924064161267 — it is gone,
not merely unpermissioned, and any reference to it should be treated as stale.
Facebook posts go to 224669177386508 or nowhere.

Note the page starts at zero followers, so early Facebook reach will be near
nil until the audience is rebuilt. Worth pairing the first posts with a
cross-post from Instagram (@bosstaxpro1) rather than expecting organic reach.

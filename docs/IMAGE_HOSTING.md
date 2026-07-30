# Image hosting for Instagram — SOLVED via raw.githubusercontent.com

**Status: working. Proven 2026-07-30 with a full 7-slide carousel.**
https://www.instagram.com/p/DbbaPshmpTx/ (CAROUSEL_ALBUM, 7 children)

## The method
1. Render slides locally to `content/YYYY-MM-DD/slides-bosstaxpro/*.png`.
2. `git add` + commit + **push the branch**.
3. Build the public URL for each slide:
   `https://raw.githubusercontent.com/MrMinor1/MrMinor1/<branch>/content/<date>/slides-bosstaxpro/<slide>.png`
   Branch currently `claude/wlm-tax-content-creator-l44qho` (slashes are fine).
4. Pass all 7 URLs, in order, to `InstagramBusinessCLIAPI publish_media_v2`
   with `instagramPageId` 17841425689425486. The `media` param takes 1-10
   public URLs.
5. POST the first comment via `_zap_raw_request` to
   `graph.facebook.com/v21.0/<media_id>/comments`, then PIN IT BY HAND
   (no pin endpoint exists on either Meta platform).

## Why this works when everything else failed
Git moves binary losslessly. The whole earlier problem was that the only
channel out of the sandbox was a tool-call parameter, which meant
hand-transcribing base64 — and that is unreliable (observed: one exact, one
off-by-two, one truncated with a fabricated ending, one 8-char insertion).
Pushing the repo sidesteps transcription completely.

raw.githubusercontent.com serves the files publicly and unauthenticated
(verified HTTP 200, image/png, ~200-500 KB each). This sandbox can reach it
too, so URLs can be verified with curl BEFORE publishing.

## Requirements
- The repo must stay **public** for raw URLs to resolve unauthenticated.
- The branch must be **pushed before publishing** — the URL 404s otherwise.
- Verify every URL returns HTTP 200 + `image/png` before calling publish.

## What this supersedes
- The Google Drive base64 chunk pipeline (`drive_chunk_store`,
  `chunk_verify_blocks`, `chunk_patch_block`, `drive_assemble_image`).
  Keep them only as a fallback if the repo ever goes private.
- The Canva autofill brand template in `CANVA_BRAND_TEMPLATE_SPEC.md` is no
  longer required for publishing. It remains useful only if the design work
  itself moves into Canva. Canva's generative AI still must not be used for
  tax copy — it rewrites figures and invents filler.

## Daily run order (updated)
generate slides -> write copy -> **commit + push** -> verify raw URLs ->
publish Instagram carousel (7 min) -> first comment -> LinkedIn -> Facebook
(when the Meta grant is fixed) -> append log row.

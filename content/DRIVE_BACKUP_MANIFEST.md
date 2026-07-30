# Google Drive text backup — WLM ProAdvisors content archive

Drive folder: **WLM-Content-Archive**  (id <DRIVE_ARCHIVE_FOLDER_ID>)

Bundles are one file per day containing that day's facebook-post.txt,
instagram-caption.txt, linkedin-post.txt (and any .md), separated by
`===== FILE: <name> =====` markers.

## Verification method
Zapier action `google_sheets_drive_store_text(filename, data, folder)`
returns length / byteLength / fnv. All three must match the local values
below before a day counts as backed up.

`length` = UTF-16 code units (JS charCodeAt), NOT Python code points.
Emoji outside the BMP count as 2. Compute locally with:

    def fnv1a_utf16(s):
        b = s.encode('utf-16-le'); h = 2166136261
        for i in range(0, len(b), 2):
            u = b[i] | (b[i+1] << 8)
            h = ((h ^ u) * 16777619) & 0xffffffff
        return '%08x' % h

## Status
| day        | utf16len | bytes | fnv      | backed up |
|------------|----------|-------|----------|-----------|
| 2026-07-08 |     3582 |  3642 | c68fde3f | YES verified |
| 2026-07-10 |     3163 |  3205 | bf596b67 | YES verified |
| 2026-07-11 |     3859 |  3931 | 987d1f72 | YES verified |
| 2026-07-12 |     3645 |  3711 | 708da934 | YES verified |
| 2026-07-13 |     3825 |  3901 | 0a1bd42b | pending |
| 2026-07-14 |     3558 |  3610 | 3754bf3d | pending |
| 2026-07-15 |     3856 |  3918 | 2c28d107 | pending |
| 2026-07-16 |     3878 |  3968 | 2e804c1b | pending |
| 2026-07-19 |     3751 |  3807 | 9a8c45cf | pending |
| 2026-07-21 |     4035 |  4099 | f93c86db | pending |
| 2026-07-29 |    12584 | 12694 | 425b43f3 | pending (largest; includes
                                             PIPELINE_STATE.md and the
                                             posted-record file) |
| 2026-07-24 |        - |     - | -        | no text (slides only) |

Local bundles are regenerated into scratchpad/bk/ by the script in the
session notes; they are derived from content/<day>/*.txt so they can always
be rebuilt from the repo working tree.

## Not backed up to Drive
Slide PNGs (~4.5 MB across 12 days). Binary cannot be transcribed reliably —
that was proven today when a base64 send truncated and fabricated an ending.
The slides ARE committed to git locally and will be preserved the moment
push access is granted. They are also regenerable from the gen_slides_*.py
scripts in the session scratchpad.

## Fastest complete fix
Grant the Claude GitHub App **Contents: Read and write** on MrMinor1/MrMinor1.
One `git push` then preserves all 14 commits including every PNG. Until then
this Drive folder is the text-only safety net.

> Resource identifiers (sheet, Drive folder, Notion pages) are redacted from this
> public repository. They are supplied to the scheduled run from its own configuration.

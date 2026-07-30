# Content archive — backup coverage

Two independent off-container backups now exist. Neither holds the slide
PNGs; those live only in the local git commits until push access is granted.

## Notion  (primary — captions/posts, full text)
Parent page: "Boss Tax Pro / WLM ProAdvisors — Brand + Content Ops"
https://app.notion.com/p/3ad64f54e68c81228711fadcca380399
Also holds the brand system, standing content rules, Canva findings,
per-channel status and the image-transport constraints.

| day        | Notion | Google Drive |
|------------|--------|--------------|
| 2026-07-08 | —      | YES verified |
| 2026-07-10 | —      | YES verified |
| 2026-07-11 | —      | YES verified |
| 2026-07-12 | —      | YES verified |
| 2026-07-13 | YES    | —            |
| 2026-07-14 | YES    | —            |
| 2026-07-15 | YES    | —            |
| 2026-07-16 | YES    | —            |
| 2026-07-19 | YES    | — (never posted) |
| 2026-07-21 | YES    | — (never posted) |
| 2026-07-24 | n/a    | n/a  (slides only, no captions; SUPERSEDED by 07-29) |
| 2026-07-29 | YES    | —            |
| 2026-07-30 | YES    | —            |

Every day that has caption text is now backed up somewhere off-container.

## Google Drive (secondary — earlier text bundles)
Folder: WLM-Content-Archive  (id 1N3OYG2IXxsLueVlVxNmwYA7hW-WzS3ln)
One file per day, verified on UTF-16 length + UTF-8 bytes + FNV-1a.
See DRIVE_BACKUP_MANIFEST.md for the expected checksums.

## Still only in this container
- Slide PNGs for all 13 days (~4.5 MB). Regenerable from the committed
  gen_slides_*.py / gen_v2_0730.py / gen_boss.py scripts.
- The git history itself (19 signed commits).
Granting the Claude GitHub App "Contents: Read and write" on
MrMinor1/MrMinor1 preserves all of it with a single push.

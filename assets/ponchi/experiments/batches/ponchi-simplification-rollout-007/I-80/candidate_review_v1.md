# I-80 candidate v1 independent review

- **Verdict:** HOLD (meaning/layout pass; palette review and exact-white fail)
- **Reviewer:** `/root/review_wave001_c` (independent candidate review)
- **Date:** 2026-09-28
- **Candidate:** `I-80_candidate_v1.png`, 1774×887 RGB
- **Candidate SHA-256:** `6b0504e750d386d0d9073848953cee0be3a6c77e57a82c8c49cd5c8030ff30bf`
- **Sidecar:** `assets/ponchi/experiments/prompts/ponchi-simplification-rollout-007/I-80.md`
- **Sidecar SHA-256:** `5c7d768d4f6a6364cbbd0cc660168f264a92282092f9921e1ed3b54edb1db880`
- **Source:** `assets/ponchi/final/I-80.webp`, SHA-256 `f7312fbe52652e19a41db37babd92704679979ab65aaeeaa4fa51895d66bf0a8` (logo-free source; visually inspected)
- **Character A reference:** `assets/ponchi/references/character-a-reader-woman.png`, SHA-256 `18e2b7e216bf76cd382002ca4e6caf20ef175332e28ec7b6ab0e5ebc2af7ddf0` (visually inspected)
- **Logo mode / ROI:** `not_required`; no logo-clearspace ROI is required or reserved.

## Findings

- **Meaning and 200px readability — PASS.** One central server cabinet with three separate drawers is the clear subject. The wrench, storage/database cylinder, and blank speech-shaped card distinguish the Tools, Resources, and Prompts concepts. Two distinct branches read as a nearby personal computer for local use and a network path to multiple shared endpoints. At 200px, cabinet, drawer count, and local-versus-shared topology remain apparent.
- **Character and content constraints — PASS.** Exactly one Character A developer is visibly assembling the server and matches the supplied reference. No second person or robot. The monitor/device screens are blank; no labels, readable text, fake text, or pseudo-text is visible.
- **Brand/no-logo — PASS.** No product logo or branded UI appears. The generic globe/network symbol does not resemble a specific service mark. Since `LOGO_MODE: not_required`, there is no ROI to reserve; the image-audit `clearspace_required=false` row is correct, and its 0.0477 ratio is informational only.
- **Series style and geometry — PARTIAL.** The 1774×887 RGB output is approximately 2:1; image audit reports bbox `0.610`, density and size pass, and no required clearspace. The palette audit is `review`, not pass, at off-palette ratio `0.010950` (`17,230/1,573,538` disallowed pixels; mostly dark and blue). The illustration is coherent with the blue/black series style, but the mechanical palette review remains open.
- **Exact-white background — FAIL.** All four corners fail exact `#FFFFFF`; only 2 of 12 sidecar perimeter samples pass (sidecar points 2 and 6). `background_samples_roi_v1.csv` reports exact-white canvas fraction `0.134212`. The sidecar requests fail-fast perimeter checks only; no full-canvas mask is recorded or required by that check. Do not post-process the background.

## Gate

Keep candidate v1 on HOLD pending an opaque uniform `#FFFFFF` background that passes all four corner and all 12 registered perimeter checks. The central server meaning, three distinct capabilities, local/shared split, character, and no-logo constraints pass. No ROI is required. Keep the candidate in experiments; no promotion, adoption, publication, or release.

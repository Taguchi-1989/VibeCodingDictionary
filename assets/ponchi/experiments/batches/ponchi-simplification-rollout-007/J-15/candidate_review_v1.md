# J-15 candidate v1 independent review

- **Verdict:** HOLD
- **Reviewer:** `/root/review_wave001_c` (independent candidate review)
- **Date:** 2026-09-28
- **Candidate:** `J-15_candidate_v1.png`, 1774×887 RGB
- **Candidate SHA-256:** `646407bb6e2cbda76f46b9acb0ec1da62fd6af8c9703907a77fe7d3f43a3108c`
- **Sidecar:** `assets/ponchi/experiments/prompts/ponchi-simplification-rollout-007/J-15.md`
- **Sidecar SHA-256:** `992ff4a15b184ab9d6b4892e34e7f217c95d77e9ee5a8a09c4ee2b998515e6ca`
- **Source:** `assets/ponchi/final/J-15.webp`, SHA-256 `b0025952ea39352d278251907afb3b87b5d3bbfccff5f72482e8f07964386b74` (logo-free source; visually inspected)
- **Character A reference:** `assets/ponchi/references/character-a-reader-woman.png`, SHA-256 `18e2b7e216bf76cd382002ca4e6caf20ef175332e28ec7b6ab0e5ebc2af7ddf0` (visually inspected)
- **Logo mode / ROI:** `not_required`; no logo-clearspace ROI is required or reserved.

## Findings

- **Meaning and 200px flow — PASS.** One image tile feeds a compact encoder/patch stage and a short embedding sequence. A separate row of text-token tiles joins before one generic model block, followed by one text-response bubble. The image-to-language direction and two incoming representations remain distinguishable at thumbnail size; this does not read as text-to-image generation.
- **Character and no-brand constraints — PASS.** Exactly one Character A engineer appears beside the source image and matches the approved reference. The source robot has been removed. No product logo, branded UI, other person, or robot is visible. `LOGO_MODE: not_required`, so no ROI is required; image audit correctly says `clearspace_required=false`.
- **Text-free requirement — FAIL.** The final response bubble contains three horizontal strokes that read as pseudo-text. The prompt calls for an empty speech-bubble outline and expressly bans pseudo-text. Remove the strokes while retaining the outline.
- **Series style and geometry — PARTIAL.** Candidate uses the blue/black editorial palette; color audit passes at off-palette ratio `0.007819` (`12,304/1,573,538` pixels). Image audit confirms native dimensions `1774×887` and no required clearspace, but reports bbox `0.497`, below the `0.50` density threshold (`density_ok=false`, status `review`). The central flow remains readable, though overall content occupancy is just below the audit target.
- **Exact-white background — FAIL.** One of four corners passes (`top-left` only); 3 of 12 registered perimeter points pass (points 2, 5, and 6). The remaining corner/sample RGBs are off-white. No full-canvas mask is recorded; the sidecar specifies fail-fast perimeter checks only, and there is no logo ROI. Keep the background unchanged and regenerate if the white gate is to be retried.

## Gate

Keep candidate v1 on HOLD. The image-to-encoder/embedding plus text-token join→LLM→response flow, Character A, no-logo constraint, and palette pass. The pseudo-text response lines, exact-white failures, and image-density review remain unresolved. No ROI is required; do not post-process the candidate or promote, adopt, publish, or release it.

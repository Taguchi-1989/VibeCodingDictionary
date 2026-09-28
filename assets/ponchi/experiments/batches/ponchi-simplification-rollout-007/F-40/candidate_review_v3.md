# F-40 candidate v3 independent review

- Reviewer: `/root/review_wave001_b/review_g47_h57_v2` (independent candidate review)
- Review date: 2026-09-28
- Verdict: **HOLD** — final corrective revision 2/2; do not promote or adopt.
- Candidate: `F-40_candidate_v3.png`
- Candidate SHA-256: `cb5eda4e21ed6f1ff749e086aa7e75a4d0aca7bd9841f6dc8bd58054321f384f`
- Dimensions/mode: 1774×887 RGB
- Current sidecar SHA-256: `e6e95f02c309be95c03f913d02820f02da56e5a5607bda478f193040ea941dbe`
- Current v3 prompt-body SHA-256 (UTF-8, LF-normalized, fences excluded): `e945966c83aa0b1c720f6f74722729d06a3c47f2ff6237e6c82af18be0e91dbd`; matches the v3 prompt body SHA in `prompt_review_v3.md` (PASS).

## Inputs and brief alignment

- Logo-free source `assets/ponchi/experiments/batches/ponchi-batch-009/F-40_base_1254x627.png`: actual SHA-256 `6b1d4f17a4ceeabf80e22c2c21db3f568f134a49b7d3db093ef163e9f15c6317`; 1254×627 RGB; matches the prompt and sidecar.
- Character B reference `assets/ponchi/references/character-b-teacher-man.png`: actual SHA-256 `6ce81ea4957f8e2522292e5f48cab2ce718a5e807024f755794079c7283f9c99`; 320×420 RGB; matches the prompt and sidecar.
- The human brief `content/entries/term_tool/F-40_npm[済].md` describes package dependencies, their installation into `node_modules`, and subsequent script use. The v3 prompt preserves the intended manifest → generic package source → project store → script/output order and the internal-only `logo_avoid` boundary.

## Visual review at 200×100

- **Meaning and order — PARTIAL.** The visible order is manifest → generic source box → project store → Character B at a laptop → empty output block. Arrows connect these stages left to right. The dependency record and installed package store are distinct. However, the required play-shaped script-run cue is absent, and the laptop has no blank terminal/console cue; at 200×100 the person reads as working at a laptop, but the image does not clearly show a script being run.
- **Package-block simplification — PASS with style note.** The source box and project store each contain exactly three large matching abstract package blocks, a substantial simplification from v2's six small source cubes. The blocks remain recognizable at 200×100. Their faceted, shaded sides add a 3D treatment and multiple blue tones, which contributes to the palette-review result below.
- **Character identity/count — PASS.** Exactly one developer is present. His short black hair, thoughtful hand-to-chin pose, light neutral clothing, and seated laptop posture match the approved Character B reference. No extra person or robot appears.
- **Text, logo avoidance, and pseudo-text — PASS.** The manifest squares, package blocks, store, laptop, and output are blank or unlabeled. No readable or pseudo-text, npm mark, logo-like wordmark, or branded service UI is visible.
- **Series style — PARTIAL.** The restrained navy outlines, pale background fills, whitespace, and neutral Character B treatment broadly match the v1.3 editorial series. The cubes use faceted blue shading rather than uniformly flat shapes, consistent with the machine color audit's blue-dominant review finding.
- **Reserved ROI — HOLD.** The prompt reserves `[970,0,1707,312)` and forbids any person, face, or other content there. At 200×100, the top of Character B's hair enters the lower edge of that region; the enlarged ROI crop confirms the intrusion. No logo is present, but the reserved rectangle is not entirely empty.

## Machine evidence and gates

- `image_audit_v3.csv` / `.md`: bbox coverage `0.327`, `density_ok=false`, `clearspace_required=true`, clearspace ink ratio `0.0073`, `clearspace_ok=true`, status `review`. The `clearspace_ok` flag does not satisfy the prompt's absolute empty-ROI requirement; visual review finds hair in the reserved area.
- `color_audit_v3.csv` / `.md`: off-palette ratio `0.014169`, status `review`; disallowed pixels `22,295/1,573,538`, dominated by blue (`21,218`) and dark (`1,055`), with purple `12`, neutral `9`, cyan/teal `1`.
- `background_samples_v3.md`: exact-white corners `0/4`; registered points `3/8`; exact-white 3% perimeter pixels `39,546/184,094`; reserved ROI `[970,0,1707,312)` exact-white pixels `37,363/229,944`; mask `not_created_fail_fast`; verdict `HOLD_fail_fast`. The ROI exact-white count is not a foreground-ink count; the separate image clearspace audit and visual crop record the small but disallowed hair intrusion.

## Final decision

**HOLD.** The sequence order, three-block package representation, Character B identity, and text/logo avoidance are acceptable. The explicit script-run/play cue is missing, Character B's hair enters the reserved logo ROI, and the strict-white mask gate did not run because fail-fast checks failed. The bbox/density and palette audits also remain in `review`. Keep this final 2/2 candidate internal and retain HOLD; no promotion, adoption, publication, or release.

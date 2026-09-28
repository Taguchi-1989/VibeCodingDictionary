# J-62 candidate v3 independent review

- **Verdict: HOLD**
- **Reviewer:** `/root/review_wave001_b` (independent visual review)
- **Date:** 2026-09-28
- **Candidate:** `J-62_candidate_v3.png`, 1774×887 RGB
- **Candidate SHA-256:** `B5D403C1861E39E8B7241AF6748548C82B4FEA23304F071C0E2E4A7924D0FEEA`
- **Current sidecar SHA-256:** `B030F02BC8D0569411CCB7EC1A4BA025AFD6CBADEB515B188E811CAC80992398`
- **PASS-reviewed v3 prompt body SHA-256:** `30D990DAB0C51BDEE8E8D7DEB957EBC8FDE70102B763ABB745883A345F6EC4C1`
- **Source:** `assets/ponchi/final/J-62.webp`, actual SHA-256 `32C751FC85AABD3ADF82BC6FE60896F5AD8A42E0D278ABC31F32C0EE9906739C`, 1254×627 RGB; matches sidecar/prompt.
- **Character references:** Character A `assets/ponchi/references/character-a-reader-woman.png`, actual SHA-256 `18E2B7E216BF76CD382002CA4E6CAF20EF175332E28EC7B6AB0E5EBC2AF7DDF0`, 320×420 RGB; Character C `assets/ponchi/references/character-c-pet-robot.png`, actual SHA-256 `BE52EC9F31CCCCC881A164CABF3EB2FE0F7AE1196B04229866B7613D73D636FD`, 320×420 RGB. Both match the approved inputs.

## Findings

- **Meaning and 200×100 route clarity — HOLD.** The thumbnail shows the judge outside the central partition, with one respondent on each side of the two route levels. The upper dashed route reads as tablet-to-human; the lower route reads as robot-to-judge. It does not clearly show the same question being sent to both respondents and a separate answer returning from each. There are four blank cards, arranged one per side of each opening, but the cards' question/answer roles and two forward/two return flows are ambiguous at 200px. This falls short of the PASS-reviewed prompt's two tablet-origin question routes and two distinct returning answer routes.
- **Partition and roles — PARTIAL.** The wall visually separates the judge from both respondents and the arrows use two visible openings; no direct judge-to-respondent sightline is apparent. The left judge resembles approved Character A, and the lower-right robot's square white head, blue antenna and blue side accents match Character C. However, the upper-right generic human has the same black bob, dark jacket and light shirt as Character A, so the required ordinary respondent is not visually distinct from the fixed series character. The judge's device is drawn as an open laptop rather than the specified plain tablet, and both respondents also have laptops; these added devices clutter the written-card schematic and read as unrequested interface/terminal content.
- **Text, brand and series rendering — PARTIAL.** No readable/pseudo-text, speech cue, logo or branded mark is visible. J-62 is `not_needed` / `logo_avoid`; no logo ROI or clearspace is required. The simple navy dashed routes and reference-like characters fit the series line style, but laptop bases/keyboards and the partition's 3D faces add unnecessary structure.
- **Geometry/color audit — PASS, not acceptance of meaning.** Current `image_audit_v3.md` reports 1774×887, bbox `0.703`, `clearspace_required=false`, status `pass`. `color_audit_v3.md` reports `pass`, off-palette ratio `0.005251`.
- **Strict-white and perimeter — FAIL.** `background_samples_v3.md` reports exact-white corners `1/4`, registered points `4/12`, and exact-white pixels in the required 3% perimeter `42,572/184,094`; fail-fast verdict is `HOLD_fail_fast`. No mask was created and no post-processing is recorded. Visually the judge's desk baseline extends to about x=35px, inside the 53px left margin.

## Gate

Keep v3 on HOLD. The prompt is PASS-reviewed, but the candidate does not unambiguously encode two questions and two replies at thumbnail size, repeats Character A's appearance in the generic respondent, substitutes laptops for the specified tablet, and fails exact-white fail-fast. The candidate is final revision 2/2; no further generation or promotion is approved by this review.

# I-80 candidate v2 independent review

- **Verdict:** HOLD (composition regression and strict-white background fail)
- **Reviewer:** `/root/review_wave001_b/review_i80_j17_v2` (independent candidate review)
- **Date:** 2026-09-28
- **Candidate:** `I-80_candidate_v2.png`, 1774×887 RGB
- **Candidate SHA-256:** `78be7341d0d3a789a09578795dcbaaaccf005d7768057100a3ab55601c646a2f`
- **Current sidecar SHA-256:** `483b79bd6131c703f2a6b1e1a11092cd456f948e19f60f3f2d06dccb28026c44`
- **Exact v2 prompt body SHA-256:** `506f84347baafc118489fbde424f41e0829599171e9aa885b3869026db15eac7` (matches the independently PASS-reviewed prompt body)
- **Source:** `assets/ponchi/final/I-80.webp`, actual SHA-256 `f7312fbe52652e19a41db37babd92704679979ab65aaeeaa4fa51895d66bf0a8`, 1254×627 RGB; matches sidecar and prompt.
- **Character A reference:** `assets/ponchi/references/character-a-reader-woman.png`, actual SHA-256 `18e2b7e216bf76cd382002ca4e6caf20ef175332e28ec7b6ab0e5ebc2af7ddf0`, 320×420 RGB; matches sidecar and prompt.
- **Human brief:** `content/entries/mcp/I-80_diy_mcp_template[人書].md` describes one developer-built MCP Server with Tools, Resources, and Prompts, then a local stdio or shared HTTP connection choice.
- **Logo policy:** `LOGO_MODE: not_required`; the brand matrix identifies I-80 as `logo_avoid`. No official logo is needed or visible.

## Findings

- **Core meaning — PARTIAL.** A central server, a local computer branch, and a shared network branch remain recognizable. The center server shows three icons, but its middle puzzle-piece does not preserve the v1-approved blank speech-card cue for Prompts, and the surrounding extra icon panels make the intended three capabilities less distinct.
- **200px readability and simplification — FAIL.** At 200px wide, the central server and two connection routes can still be found, but the image is crowded with a large left board of repeated slots and controls, a separate tray of four capability cards, the server's own cards, and several endpoints. This is materially more complex than the v1-reviewed single-server composition and contradicts the v2 prompt's “strict exact-white background only” revision scope and its prohibition on extra panels/cards/UI. The worker and content also reach into the left/right perimeter rather than keeping the requested clear margin.
- **v1-approved composition preservation — FAIL.** `candidate_review_v1.md` accepted one central server with exactly three drawers, one Character A developer, and distinct local/shared routes. V2 reintroduces multiple host/product-like panels and duplicate capability cards instead of preserving that accepted layout while correcting only the background.
- **Character, text, and brand constraints — PASS.** Exactly one Character A developer is visible and her hair, face, and dark jacket/white blouse are consistent with the approved reference. No extra person or robot appears. No readable or pseudo-text, logo, or branded UI is visible; symbols are generic.
- **Series palette and geometry — PARTIAL.** The 2:1 RGB format and dark/navy plus pale-blue line-art style fit the series. `color_audit_v2.csv` reports `pass`, with 14,627 disallowed pixels out of 1,573,538 (ratio `0.009296`). The current `image_audit_v2.csv` reports bbox `0.680`, density pass, `clearspace_required=false`, and overall `pass`; this agrees with `audit_clearspace_policy_v2.csv` (`not_needed`, `logo_avoid`). Its `clearspace_ink_ratio` of `0.0407` is informational because no logo clearspace is required. These palette/geometry passes do not override the visual composition and background holds.
- **Exact-white background — FAIL.** `background_samples_v2.md` reports exact-white corners `0/4`, registered points `2/12`, exact-white pixels in the 3% perimeter `34,352/184,094`, and `HOLD_fail_fast`. The CSV also has non-white corners and a registered sample landing on the developer. `Background-mask status: not_created_fail_fast`; no mask result is available.

## Gate

Keep the v2 candidate on HOLD. It fails the targeted exact-white correction and does not preserve the v1-approved simplified layout. A future candidate should return to one central server with three clearly distinct capability symbols and the two approved connection choices, keep extra panels/cards out, preserve the 3% blank perimeter, and pass the strict-white checks before any mask review. Keep all candidates in experiments; no promotion or production adoption.

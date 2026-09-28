# H-57 candidate v1 independent review

- **Verdict:** HOLD
- **Reviewer:** `/root/review_wave001_c` (independent candidate review)
- **Date:** 2026-09-28
- **Candidate:** `H-57_candidate_v1.png`, 1774×887 RGB
- **Candidate SHA-256:** `8dbd283177a6f2815625eb49d6562391d6dfb47cb7c6571a3816203a59348d39`
- **Sidecar:** `assets/ponchi/experiments/prompts/ponchi-simplification-rollout-007/H-57.md`
- **Sidecar SHA-256:** `1b6b4dc9cbe06d0bd5d2e7c1da444e1bb0be898ab25af6591fb64c9c47850207`
- **Edit source:** `assets/ponchi/experiments/batches/ponchi-batch-014/H-57_base_1254x627.png`, SHA-256 `fa22a75414d2df28e4e7019f5133c3920677701d1d3fd27d6d27cdce0f150b56` (visually inspected)
- **Character B reference:** `assets/ponchi/references/character-b-teacher-man.png`, SHA-256 `6ce81ea4957f8e2522292e5f48cab2ce718a5e807024f755794079c7283f9c99` (visually inspected)
- **Official Gemini sparkle:** `assets/logos/gemini/gemini_sparkle_4g_512_lt.png`, SHA-256 `5e7cfecaa53f4f65a313fe89b0f389548126544a78fad8489510c70ae641a4a1`; recorded as official context only. `LOGO_MODE: internal_base_only`.

## Findings

- **Meaning and 200px hierarchy — PARTIAL.** A left-to-right sequence of five large generation cards is apparent, with one smaller chip group under each and a lower five-node spine. The first group has three chips; each later group has four chips, which visually asserts unsupported exact counts. The second lower spine duplicates the card timeline, so the composition has two generation tracks plus variant chips rather than the single five-node spine requested. At 200px, these layers and the dense repeated cards make the generation-versus-variant hierarchy harder to read.
- **Simplification, text-free design, and style — FAIL.** The five upper cards contain repeated bullet dots, horizontal strokes, colored tiles, large icons, and decorative rays; these resemble pseudo-text/UI and repeat the card structures that the brief asked to remove. The lower spine, vertical dashed links, card arrows, chip groups, and rays add several extra visual layers. The palette audit is `review` at off-palette ratio `0.013097` (`20,609/1,573,538` pixels; mostly blue). This is not a palette pass.
- **Character and brand — PARTIAL.** Exactly one thoughtful male observer appears at lower left and visually matches the supplied Character B reference. No readable Gemini text or exact official sparkle lockup is visible. The candidate is internal-only, with no composited official logo. However, the rays and decorative star-like marks are unnecessary in this no-logo illustration, and one ray group is inside the reserved area.
- **Reserved logo ROI — FAIL.** The required clearspace `[966,16,240,240]` on the 1254×627 canvas maps to candidate bounds `[1366,22,341,341]`. It contains `98,605` non-white pixels out of `116,281`; the upper-right generation card and decorative rays occupy the reservation. The image audit also reports clearspace required `true`, clearspace ink `0.0765`, status `review`. Keep the complete mapped rectangle empty.
- **Exact-white background — FAIL.** All four corners and all eight registered background points fail exact `#FFFFFF` (0/4 corners, 0/8 samples). Corner RGBs: `(253,255,255)`, `(254,255,254)`, `(253,253,254)`, `(253,253,253)`. Registered points 1–8: `(253,253,253)`, `(255,254,255)`, `(254,254,254)`, `(254,254,254)`, `(254,254,254)`, `(254,253,254)`, `(253,253,253)`, `(254,254,254)`. Fail-fast reports 13 failures across corners, samples, and ROI; no full-canvas mask was created. Do not post-process the background.
- **Geometry — PASS.** Candidate is 1774×887 RGB, approximately 2:1; the image audit reports bbox `0.705` and `density_ok=true`. Geometry does not resolve the content, reserved-ROI, or white-background failures.

## Gate

Keep candidate v1 on HOLD. A revision must return to one generation spine with five nodes, remove the repeated UI-like cards and pseudo-text strokes, avoid unsupported later chip counts, place the full mapped logo reservation outside all content, and pass exact-white corners, samples, and a same-size background mask. Keep the logo-free candidate in experiments; no overlay, promotion, adoption, publication, or release.

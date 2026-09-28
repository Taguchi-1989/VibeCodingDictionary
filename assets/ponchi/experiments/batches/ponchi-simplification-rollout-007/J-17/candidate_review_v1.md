# J-17 candidate v1 independent review

- **Verdict:** HOLD (semantic/topology PASS; exact-white FAIL)
- **Reviewer:** `/root/review_wave001_c` (independent candidate review)
- **Date:** 2026-09-28
- **Candidate:** `J-17_candidate_v1.png`, 1774×887 RGB
- **Candidate SHA-256:** `5763bf1a7ef2742de63c8fdf2c8e276d5fc66bfc30b6b26dbe6776d73f3158ea`
- **Sidecar:** `assets/ponchi/experiments/prompts/ponchi-simplification-rollout-007/J-17.md`
- **Sidecar SHA-256:** `6312ea6bd6be517fe3ceda3eeb33bec9466e37dee8b9592c7a0c5cb7ae01304d`
- **Source:** `assets/ponchi/final/J-17.webp`, SHA-256 `241bac1b908021ff04ecc06e7e67e62112118e1857ab4d85c7b1e74b0c1132f9` (logo-free current source, visually inspected; read-only edit input)
- **Character A reference:** `assets/ponchi/references/character-a-reader-woman.png`, SHA-256 `18e2b7e216bf76cd382002ca4e6caf20ef175332e28ec7b6ab0e5ebc2af7ddf0` (visually inspected)
- **Logo mode:** `not_required`; no logo asset/clearspace required.

## Findings

- **Meaning and 200px readability — PASS.** The five blank tiles are in the required left-to-right order with position 3 visibly selected. At thumbnail size, the row, selected tile, directed links, and relative line weights remain easy to distinguish. The observer sits outside the relationship diagram.
- **Arrow topology and weights — PASS.** Exactly four directed relationships are visible and originate from token 3: thin 3→1, thin 3→4, thick self-loop 3→3, and thick 3→5. The self-loop clearly leaves and returns to the selected tile. The two heavy arrows are visibly thicker than the two thin links; no extra arrow/link, crossing, second token row, legend, or auxiliary attention map is present.
- **Character, text, and logo constraints — PASS.** Exactly one Character A observer appears, matching the supplied reference. No robot, other person, readable text, fake token text, numeric weight, logo, or branded UI is visible.
- **Series style and geometry — PASS with white-gate exception.** Candidate is 1774×887 RGB (approximately 2:1). `image_audit_v1.md` reports bbox `0.554`, clearspace required `false`, status `pass`. The palette audit reports `pass` with off-palette ratio `0.004290`. There is no reserved logo ROI for J-17.
- **Exact-white background — FAIL.** All four corners fail exact `#FFFFFF`; 7 of 8 registered points fail (only point 5 passes). Corners: `(254,255,255)`, `(254,255,254)`, `(254,253,253)`, `(254,253,254)`. Registered points 1–8: `(253,253,253)`, `(255,254,255)`, `(254,254,254)`, `(254,254,254)`, `(255,255,255)`, `(255,254,255)`, `(254,254,254)`, `(254,254,254)`. The background audit is fail-fast; no full same-size background mask is recorded. The tolerant palette pass does not override this strict-white failure.

## Gate

Keep candidate v1 on HOLD pending a new internal candidate with an opaque, uniform exact `#FFFFFF` background and passing corner/sample plus full same-size mask checks. Its visual meaning, character, arrow topology/weights, palette, and no-logo constraints pass. Do not post-process/paint the background, promote, adopt, publish, or release this candidate.

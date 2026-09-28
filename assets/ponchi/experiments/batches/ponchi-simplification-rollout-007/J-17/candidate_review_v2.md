# J-17 candidate v2 independent review

- **Verdict:** HOLD (strict-white background fail; blank-perimeter and image-audit geometry remain open)
- **Reviewer:** `/root/review_wave001_b/review_i80_j17_v2` (independent candidate review)
- **Date:** 2026-09-28
- **Candidate:** `J-17_candidate_v2.png`, 1774×887 RGB
- **Candidate SHA-256:** `a0b68619ffc23d717483caf83e285937ca1f2e9b9608d58b3d5bc7e52e9af36f`
- **Current sidecar SHA-256:** `5d5fe18920d2dd538221fd7b99b9e7c632f7450c6ff3492c0f8124b78886b56b`
- **Exact v2 prompt body SHA-256:** `1ea328e070f716b0358aee1d606801ed4bdd4c181d21f1eb598a5b351d082984` (matches the independently PASS-reviewed prompt body)
- **Source:** `assets/ponchi/final/J-17.webp`, actual SHA-256 `241bac1b908021ff04ecc06e7e67e62112118e1857ab4d85c7b1e74b0c1132f9`, 1254×627 RGB; matches sidecar and prompt.
- **Character A reference:** `assets/ponchi/references/character-a-reader-woman.png`, actual SHA-256 `18e2b7e216bf76cd382002ca4e6caf20ef175332e28ec7b6ab0e5ebc2af7ddf0`, 320×420 RGB; matches sidecar and prompt.
- **Human brief:** `content/entries/term_general/J-17_attention[済].md` and the figure memo specify five tokens in order, with token 3 selected and four outgoing relationships with two thin and two thick arrows.
- **Logo policy:** `LOGO_MODE: not_required`; the brand matrix identifies J-17 as `logo_avoid`. No official logo is needed or visible.

## Findings

- **Meaning and 200px readability — PASS.** At 200px wide, the five blank tiles remain distinguishable, the third tile is visibly selected, and the arrows read as relationships from that tile. The observer sits outside the diagram.
- **Arrow topology and weights — PASS.** There are exactly four directed relationships: thin 3→1 and 3→4; thick 3→3 as a visible self-loop and 3→5. Directions and relative thicknesses match the human brief and the v1-approved arrangement; there is no second row, legend, or extra processing stage.
- **Character, text, and logo constraints — PASS.** One Character A observer appears, with the approved dark hair, face, and dark jacket/white blouse design. No robot or additional person is present. Tiles and laptop screen are blank; no readable/pseudo-text, logo, or branded UI is visible.
- **Series style and geometry — PARTIAL.** The 2:1 RGB composition uses the established dark/navy and pale-blue line style, and the color audit is `pass`: 4,936 disallowed pixels out of 1,573,538 (ratio `0.003137`). At 200px the concept remains clear, though the figure and diagram occupy a relatively narrow vertical band. The current `image_audit_v2.csv` reports bbox `0.467`, `density_ok=false`, `clearspace_required=false`, `clearspace_ok=true`, and overall `review`; density remains an open geometry gate, while the clearspace fields agree with `audit_clearspace_policy_v2.csv` (`not_needed`, `logo_avoid`). The visible work-surface line also extends into the left 3% margin, contrary to the v2 prompt's blank-perimeter requirement.
- **Exact-white background — FAIL.** `background_samples_v2.md` reports exact-white corners `0/4`, registered points `1/8`, exact-white pixels in the 3% perimeter `34,136/184,094`, and `HOLD_fail_fast`. `background-mask status: not_created_fail_fast`; no mask result is available.

## Gate

Keep the v2 candidate on HOLD. Its semantic layout, arrow relationships, character, palette, and no-logo treatment pass visual review, but it did not correct the strict-white defect, and perimeter/density gates remain open. A future candidate must keep the blank perimeter clear and pass the corner/sample checks before a full same-size mask can be created and independently reviewed. Keep the candidate in experiments; no promotion or production adoption.

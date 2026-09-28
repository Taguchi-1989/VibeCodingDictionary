# J-21 candidate v3 independent review

- **Verdict:** HOLD (strict-white fail-fast; v3 changes the accepted composition beyond the background-only correction)
- **Reviewer:** `/root/review_j17_v3`
- **Date:** 2026-09-28
- **Candidate:** `assets/ponchi/experiments/batches/ponchi-simplification-rollout-007/J-21/J-21_candidate_v3.png`, 1774×887 RGB
- **Candidate SHA-256:** `edbd71f8369c76c5f10d31fcdbaa8b75284f551e82d9f4198b048901e5b2a66a`
- **Current prompt sidecar SHA-256:** `2f7aad57a1291035e984736bef41298e09d25168ae91fb54cd302723912565522`
- **Exact v3 prompt-body SHA-256:** `4249050fe57a9fd1c682d38a0dde8771b4dd443223215660663d3e39727039c8`; matches the independently PASS-reviewed body in `prompt_review_v3.md`.
- **Human brief:** `content/entries/term_general/J-21_lora[済].md`.

## Findings

- **Meaning and comparison — PARTIAL PASS at 200×100.** The two side-by-side states remain distinguishable: the left uses distributed navy updates across the full model; the right has an unfilled outlined model, a lock, and a pale-blue adapter symbol. Blank document stacks and incoming data arrows are present. At 200px the left/right contrast and lock are visible, but the many tiny internal model diagrams collapse into dense marks and the adapter/update relationship is less clear.
- **Composition preservation and simplification — HIGH.** The v3 prompt says to preserve the independently accepted v2 composition exactly and make only the strict-white correction. The v2 candidate uses one simple whole-model node grid on the left and one frozen node grid plus a single adapter on the right. V3 replaces those with repeated miniature workflow cards inside each model, additional node rows, internal grids, plus signs, arrows, input-token rows, and ellipsis dots. These are substantial added/changed elements, not just a background correction; they increase visual complexity and weaken 200px legibility. Keep the accepted v2 composition for any future prompt template or comparable item. Do not generate another J-21 candidate.
- **Update/lock/adapter glyph check — PARTIAL.** One lock appears on the right and no blue update glyph appears on the frozen model itself. A single pale-blue adapter tile is present, but it contains several blue nodes and a separate blue circular-update glyph sits outside the tile to its right. The v3 prompt requires the adapter to carry its single active mark; the current separation makes that relationship less direct. Preserve one update mark inside the adapter and remove unrequested external update glyphs in future comparable prompts.
- **Text, document, brand, and character constraints — PASS.** Both document stacks have blank front pages; there is no readable or pseudo-text, logo, branded mark, person, or robot. This matches the no-characters and logo-avoid policy.
- **Series style — PARTIAL.** The navy, near-black, and pale-blue line art is coherent, but the dense repeated internal diagrams conflict with the user's simplification goal and with the v3 instruction to retain the simpler reviewed composition.
- **Geometry and color audits — PASS with a non-applicable clearspace field.** `image_audit_v3.md` reports `bbox_coverage=0.626`; its generic clearspace value is `0.0343` and status is REVIEW. J-21 has `logo_avoid` and no reserved ROI, so that generic top-right measure is not an item logo-clearspace gate. `color_audit_v3.csv` passes at `0.006428` (10,115/1,573,538 disallowed pixels).
- **Exact-white background — FAIL.** Candidate-bound `background_samples_v3.md/csv` reports corners `0/4`, registered points `3/12`, and exact-white pixels in the 3% perimeter `51,609/184,094`. The mask is `not_created_fail_fast`; no post-processing is recorded.

## Gate

Keep J-21 v3 internal and on HOLD. Although the broad Fine-tuning-versus-LoRA contrast and palette remain visible, v3 adds/changes substantial internal composition against its exact prompt, and the mandatory exact-white gate fails. Since this is final corrective revision 2/2, close the item without another generation, mask, post-processing, or production adoption.

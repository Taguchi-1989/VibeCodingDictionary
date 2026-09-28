# J-17 candidate v3 independent review

- **Verdict:** HOLD (strict-white fail-fast and 3% perimeter breach)
- **Reviewer:** `/root/review_j17_v3`
- **Date:** 2026-09-28
- **Candidate:** `assets/ponchi/experiments/batches/ponchi-simplification-rollout-007/J-17/J-17_candidate_v3.png`, 1774×887 RGB
- **Candidate SHA-256:** `4c97923269730b4da26a1c521162173717ce2fdc736b9e01897138a38540dffb`
- **Current prompt sidecar SHA-256:** `53bc3fcd736573b48e92ed6b9cc08e0f89bda939a7a4826b4cf0420cf04f9782`
- **Exact v3 prompt body SHA-256:** `e56d9f77d8af5b4c8ecb8f42310a4c8cbe0546f4cb820fe80abe7377869ca992`; matches the v3 prompt body recorded as independently PASS-reviewed in `prompt_review_v3.md`.
- **Human brief:** `content/entries/term_general/J-17_attention[済].md` and the item sidecar.

## Findings

- **Meaning, order, arrows, and 200px legibility — PASS.** I inspected the candidate at 200×100 px. The five blank tiles read left-to-right, the third tile is selected, and the four relationships remain discernible: thin 3→1 and 3→4; thick 3→3 as a self-loop and 3→5. Arrowheads point to the intended tiles. Character A sits outside the diagram and looks toward it. No readable/pseudo-text, extra person, robot, or logo appears.
- **Character and series style — PASS.** Character A’s dark hair/jacket, white blouse, chair, and laptop follow the supplied character reference. The navy, pale-blue, and dark line-art style is coherent with the series. The laptop screen is blank.
- **Simplification — MEDIUM observation.** Each of the five token tiles has both an outer frame and a second inset square. This repeated inner frame is not needed to convey a blank token tile and adds visual scaffolding. For future similar prompts, request one outline per tile. This candidate is already the final allowed revision, so do not generate another J-17 revision.
- **Geometry and 3% perimeter — HOLD.** The image audit reports `bbox_coverage=0.781`, `density_ok=true`, and `clearspace_required=false`; no logo ROI is required for J-17. However, the candidate’s leftmost chair/work-surface ink reaches approximately x=27 px, inside the required 3% left margin (about 53 px; about 6 px at 200px width). The color audit’s off-palette bounding box also begins at x=27. This contradicts the v3 prompt’s requirement that all ink stay inside a blank 3% perimeter.
- **Palette — PASS.** The tolerant color audit passes with 4,950/1,573,538 disallowed pixels (`0.003146` ratio). The visual palette remains predominantly navy, pale blue, and dark/neutral line art.
- **Exact-white background — FAIL.** `background_samples_v3.csv/md` reports exact-white corners `0/4`, registered points `3/8`, and exact-white pixels in the 3% perimeter `32,942/184,094`. The image audit and color audit do not override this background fail-fast gate. No background mask was created and no post-processing is recorded.

## Gate

Keep the v3 candidate internal and on HOLD. Its semantic layout, arrow topology, 200px legibility, character treatment, geometry density, and tolerant palette audit pass. The strict-white gate fails, and visible ink also enters the required 3% left perimeter. Because v3 is corrective revision 2 of 2 and its prompt says to stop if it fails, close J-17 without another candidate generation, mask, post-processing, or production adoption.

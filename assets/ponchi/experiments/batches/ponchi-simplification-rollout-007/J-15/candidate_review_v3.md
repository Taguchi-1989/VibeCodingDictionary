# J-15 candidate v3 independent review

- **Verdict:** HOLD (strict-white fail-fast; candidate retains a prohibited second input bubble with pseudo-text-like marks)
- **Reviewer:** `/root/review_j17_v3`
- **Date:** 2026-09-28
- **Candidate:** `assets/ponchi/experiments/batches/ponchi-simplification-rollout-007/J-15/J-15_candidate_v3.png`, 1774×887 RGB
- **Candidate SHA-256:** `746b52a194df30a89ae9b508fb67d2c618adc1f867461a52e2ae9b7677a52f5b`
- **Current prompt sidecar SHA-256:** `caa3d0e98c2c86f98d525b5fe9d36c31d4e09509d87a385546c9ef6d42535597`
- **Exact v3 prompt-body SHA-256:** `ffcde6e47af48ed1e919a5cefa8284e5b37299d8e77cf3624d515440724fb861`; matches the independently PASS-reviewed body in `prompt_review_v3.md`.
- **Human brief:** `content/entries/term_general/J-15_vlm[済].md`.

## Findings

- **Image-to-language meaning and flow — PASS at the high level.** I inspected the image at 200×100 px. The input landscape, three-patch encoder, three image-embedding tiles, three separate blank text-token tiles, shared LLM input, plain LLM block, and blank response bubble can be followed from left to right. The two input roles remain distinct and converge before the LLM, consistent with the article brief.
- **Character and series style — PASS.** Exactly one Character A appears; the bobbed dark hair, dark jacket, white blouse, and laptop-side pose follow the supplied reference. The source robot is absent. The black/navy/pale-blue linework is consistent with the series.
- **Prompt compliance: secondary bubble and pseudo-text — HIGH.** A second bubble appears below the embedding row, with two pale-blue horizontal strokes. It remains visible at 200px and reads as a second input speech/text cue. The v3 prompt explicitly removes all secondary input bubbles and requires the separate text-token row to be the sole text-input representation; it also prohibits pseudo-text and marks in the output. Keep only the required blank response bubble and text-token row. This is revision 2/2, so do not generate another J-15 candidate.
- **Glyph and layout checks — PARTIAL.** The image tile is distinct; the encoder has exactly three prominent patch squares; image and text each have three token tiles; their arrows meet before one solid LLM block; the response bubble on the far right is empty. The extra lower bubble is an unrequested competing input symbol and duplicates the text-token row's role.
- **Text, logo, and ROI — PARTIAL.** There is no logo, branded UI, readable text, or logo-like mark. The item prompt and brand matrix require no official logo/ROI, so the image audit's generic `clearspace_required=true` field is not a brand-clearspace requirement. The two strokes inside the extra bubble are pseudo-text-like even though no words can be read.
- **Geometry and palette — PASS by the listed audits.** `image_audit_v3.csv` reports exact 1774×887 size, `bbox_coverage=0.551`, density pass, and overall image-audit PASS. `color_audit_v3.csv` passes at `0.003775` (5,940/1,573,538 disallowed pixels).
- **Exact-white background — FAIL.** Candidate-bound `background_samples_v3.md/csv` reports exact-white corners `1/4`, registered points `2/12`, and exact-white pixels in the 3% perimeter `37,344/184,094`. No background mask was created; no post-processing is recorded.

## Gate

Keep J-15 v3 internal and on HOLD. The core image/text-to-LLM flow is visible at 200px and the geometry/palette audits pass, but a prohibited second input bubble with pseudo-text-like strokes remains and exact-white fail-fast checks do not pass. Since v3 is final corrective revision 2/2, close the item without another generation, mask, post-processing, or production adoption.

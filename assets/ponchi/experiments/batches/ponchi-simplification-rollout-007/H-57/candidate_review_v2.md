# H-57 candidate v2 independent review

- Reviewer: `/root/review_wave001_b/review_g47_h57_v2` (independent visual review)
- Review date: 2026-09-28
- Verdict: **HOLD** — keep this candidate internal; no promotion or adoption.
- Candidate: `H-57_candidate_v2.png`
- Candidate SHA-256: `206E66D495FA05D910CB0AB7894109F4C7E056A5F61D9461A7F64B37DB480281`
- Dimensions/mode: 1774×887 RGB
- Current sidecar SHA-256: `C8739266AA2838BC8EA79EF99271E993D0E30DB05F8B1CD319EAF5619502C09C`
- Current v2 prompt body SHA-256 (UTF-8, LF, excluding Markdown fence): `df868feb0cf9c2e99c59022f8c9309097cf74953c613c7a3627ba28375ad87ea`; matches the body hash in the v2 prompt PASS record.

## Inputs and brief alignment

- Logo-free source `assets/ponchi/experiments/batches/ponchi-batch-014/H-57_base_1254x627.png`: actual SHA-256 `FA22A75414D2DF28E4E7019F5133C3920677701D1D3FD27D6D27CDCE0F150B56`; 1254×627 RGB; matches the sidecar and approved v2 prompt. The current final is explicitly excluded because it contains an official Gemini mark.
- Character B reference `assets/ponchi/references/character-b-teacher-man.png`: actual SHA-256 `6CE81EA4957F8E2522292E5F48CAB2CE718A5E807024F755794079C7283F9C99`; 320×420 RGB; matches the sidecar and approved v2 prompt.
- The human brief `content/entries/history/H-57_gemini_naming_history[人書].md` supports five generations, the distinction between generation and subordinate variant, and an explicitly three-member original Ultra/Pro/Nano family. The v1 review held for duplicate timelines, UI-like repetition, unsupported later counts, logo-ROI intrusion, and non-white background. The v2 prompt body remains the independently reviewed body and addresses those findings.

## Visual review at 200×100

- **Meaning and timeline — PARTIAL.** One horizontal, left-to-right spine with five equal-level nodes remains; the duplicate lower timeline and repeated large cards are gone. At 200×100 the five-node chronology and subordinate groups are legible.
- **Variant-count fidelity — HOLD.** Every one of the five nodes has a visible three-circle group below it. Only the original generation has an explicitly confirmed three-member Ultra/Pro/Nano family. Later nodes were required to avoid asserting unsupported counts; the repeated filled-plus-two-outline circles still present three visible slots per later generation, with no legend to identify the outlines as non-counting placeholders.
- **Character identity/count — PASS.** Exactly one thoughtful, short-haired male observer appears at left and matches the approved Character B Teacher-man reference in pose and design. No other figure or robot is visible.
- **Logo avoidance and series treatment — PASS.** No Gemini sparkle or other brand mark is drawn or imitated. The linework is clean and flat, using the approved blue progression with neutral Character B colors; it reads as the same editorial series at 200×100. The source logo reservation is nevertheless violated by diagram content, recorded below.

## Machine evidence and gates

- `image_audit_v2.csv` / `.md`: bbox coverage `0.311`, `density_ok=false`, `clearspace_required=true`, clearspace ink ratio `0.0035`, `clearspace_ok=true`, status `review`.
- `color_audit_v2.csv` / `.md`: off-palette ratio `0.001453`, status `pass`. This improves on the v1 palette audit (`review`, ratio `0.013097`); no visual off-palette hue large enough to overturn the v2 palette result was observed at 200×100.
- `background_samples_v2.md`: exact-white corners `1/4`; exact-white registered points `1/8`; exact-white 3% perimeter pixels `51,617/184,094`; reserved ROI `[1366,22,1707,363)` contains `92,081/116,281` non-white pixels; mask status `not_created_fail_fast`; verdict `HOLD_fail_fast`.
- The strict-white v2 report conflicts with the image audit's `clearspace_ok=true` result. Although the image audit reports clearspace ink ratio `0.0035`, the dedicated reserved-ROI report says `92,081/116,281` pixels are non-white, and an enlarged crop shows the bottom of a timeline node crossing into the rectangle. Treat the reserved area as failed until the audit discrepancy is reconciled; do not treat the image-audit clearspace flag as clearance.

## Final decision

**HOLD** for the unsupported repeated three-slot variant groups, visible intrusion into the reserved logo area, and strict-white fail-fast result. The simplified five-node structure, observer identity, palette audit, and logo-free appearance are acceptable. Keep the candidate internal; revise later-generation groups to avoid implying counts, move all diagram content out of the complete reserved ROI, and rerun the strict-white checks before any later gate.

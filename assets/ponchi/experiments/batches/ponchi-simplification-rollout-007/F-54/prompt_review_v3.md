# F-54 candidate v3 prompt independent review

- **Verdict:** PASS (prompt only)
- **Reviewer:** `/root/review_wave001_c` (independent of the prompt author and candidate-v2 reviewer)
- **Date:** 2026-09-28
- **Sidecar:** `assets/ponchi/experiments/prompts/ponchi-simplification-rollout-007/F-54.md`
- **Whole-sidecar SHA-256:** `a3388d43e2e40fbd3ef0a6abe2d0a413b499b145f96ca56089d012cd51397dfc`
- **Reviewed prompt:** candidate v3 block, UTF-8/LF, excluding its code fence and terminal newline
- **Prompt-body SHA-256:** `f45811b8d7e4b6e4129d5838ec634ab385f55630bf0922fdb19df8ec8b0b1784`
- **Exact source:** `assets/ponchi/final/F-54.webp`, SHA-256 `6ca239ee02c95aa820d9ddf0b5f81c498d3e76a758c02aefc480befe64e17b8a`
- **Character B reference:** `assets/ponchi/references/character-b-teacher-man.png`, SHA-256 `6ce81ea4957f8e2522292e5f48cab2ce718a5e807024f755794079c7283f9c99`
- **Candidate v2 reviewed for context:** `F-54_candidate_v2.png`, SHA-256 `fdfd93c36c80c31857747b83741421783876a952e3869750f57dc3ac7d26b949`, 1774×887 RGB
- **Candidate v2 audit:** `candidate_review_v2.md`, `ponchi-image-audit-v2.md`, and `ponchi-color-audit-v2.md` in this folder
- **Candidate v3:** absent at review time

## Review findings

- **Revision scope — PASS.** v3 targets the single recurring v2 failure: exact-white background fidelity. It specifies an opaque, flat background with every background pixel exactly RGB `(255,255,255)`, asks for a pure-white blank canvas from the start, and explicitly rejects near-white, gray/off-white, warm/tinted, shaded, gradient, or other non-white background pixels. It retains the four-corner and eight-point checks, the full-canvas same-size 1-bit mask check, independent contour review, fail-to-HOLD behavior, and prohibition on painting/whitening/replacing/post-processing after generation.
- **Meaning/layout/style — PASS.** It preserves v2's three sequential checkpoint nodes, one connecting line, identical blank snapshot glyphs, highlighted middle checkpoint, one curved return arrow from the right checkpoint to the highlighted earlier checkpoint, and one calm Character B at the right. It retains the v2 2:1 composition and clean v1.3 palette/style; it does not introduce branches, merges, a remote, push/transfer cues, or additional figures. The v2 candidate's independent 200px review found this structure clear; visual inspection here agrees.
- **Source/reference and brand constraints — PASS.** v3 retains the exact source and SHA above, the attached Character B reference and SHA above, and requires the same identity/design. It keeps `LOGO_MODE: not_required`, prohibits logos/Git/GitHub marks/branded UI/product symbols, and correctly reserves no logo-clearspace rectangle. Source and reference files match the listed hashes.
- **Internal-only and output gate — PASS.** The requested output is one native-resolution PNG at `assets/ponchi/experiments/batches/ponchi-simplification-rollout-007/F-54/F-54_candidate_v3.png`, kept in experiments, with no adoption, publication, or release. At review time that output did not exist. The v3 prompt explicitly blocks generation until an independent PASS; this review supplies that prompt-level PASS. Candidate v2 remains unchanged and on HOLD.
- **Candidate v2 evidence — HOLD remains appropriate.** `candidate_review_v2.md` records semantic/style PASS and exact-white HOLD. It reports 3/4 corner failures, 4/8 registered-point failures, and only 266,658/1,573,538 exact-white pixels (16.9464%); no mask was retained because fail-fast checks failed. The v2 image audit reports geometry pass (`bbox 0.556`) and no required logo clearspace. Its tolerance color pass does not satisfy exact-white. v3 addresses that failure without relaxing or replacing the v2 meaning/style constraints.

## Gate

The candidate v3 prompt passes independent review. This does not approve candidate v2 or any production use. Keep v2 unchanged on HOLD; if a v3 candidate is generated under the reconciled wave gate, review its semantic/style, exact-white samples and full mask independently before any later decision. No generation, ledger edit, or adoption was performed in this review.

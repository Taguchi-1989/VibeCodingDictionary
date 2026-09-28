# H-57 v2 independent prompt review

- Reviewer: `/root/review_wave001_c` (independent of prompt author)
- Review date: 2026-09-28
- Verdict: **PASS** for prompt content; candidate-side visual and palette checks remain separate.
- Sidecar SHA-256: `22ba50c2fdaeca93dde9c8fac5981030ab1edfdd2fc7dd6da9da36f5602f4460`
- Exact v2 prompt body SHA-256 (UTF-8, LF, excluding Markdown fence): `df868feb0cf9c2e99c59022f8c9309097cf74953c613c7a3627ba28375ad87ea`

## Inputs and source meaning

- Logo-free Batch 014 base `assets/ponchi/experiments/batches/ponchi-batch-014/H-57_base_1254x627.png`: actual SHA-256 `fa22a75414d2df28e4e7019f5133c3920677701d1d3fd27d6d27cdce0f150b56`; matches sidecar and prompt.
- Character B reference `assets/ponchi/references/character-b-teacher-man.png`: actual SHA-256 `6ce81ea4957f8e2522292e5f48cab2ce718a5e807024f755794079c7283f9c99`; matches sidecar and prompt. The single observer in the source is retained as Character B.
- Human brief `content/entries/history/H-57_gemini_naming_history[人書].md` describes five generations (1.0, 1.5, 2.0, 2.5, 3) and within-generation size/variant names. V2 preserves those five nodes and keeps variant groups subordinate; it limits the original Ultra/Pro/Nano group to three chips and leaves unsupported later counts/names/dates/rankings unspecified.
- Candidate v1 review HOLDs the duplicated lower timeline, pseudo-text/UI-like repeated cards, unsupported later chip counts, intrusion into the reserved logo ROI, and exact-white background. V2 directly removes the duplicate timeline and UI-like marks, constrains later variants, and maps the complete ROI to blank white.

## Acceptance review

- Exactly one horizontal five-generation spine remains, with equal-level chronological nodes and smaller groups connected only to their own node. Exactly one Character B observer remains.
- `LOGO_MODE: internal_base_only` is preserved without generating, imitating, attaching, or compositing Gemini marks. The mapped source clearspace `[966,16,240,240]` and corresponding 1774×887 area are required to remain entirely blank white, including all content and observer parts.
- V2 explicitly restricts colors to the approved palette plus Character B's existing neutral colors; it removes star/ray decoration and fake UI/text. The v1 machine palette audit was `review`, so the generated candidate still needs its own palette audit; this prompt PASS does not waive that check.
- Opaque exact-white background is required at every corner, all eight registered points, and the full reserved ROI. Fail-fast checks precede same-size mask creation/review; post-generation painting is prohibited. Internal experiment path and no-promotion boundary are explicit.

## Gate status

`H-57_candidate_v2.png` was absent at review time. Prompt content is **PASS**; keep generation blocked until the independent PASS is reconciled in the applicable gate/ledger. Candidate v1 remains HOLD.

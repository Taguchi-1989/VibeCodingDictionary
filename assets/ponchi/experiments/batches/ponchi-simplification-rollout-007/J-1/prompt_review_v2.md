# J-1 v2 independent prompt review

- Reviewer: `/root/review_wave001_c` (independent of prompt author)
- Review date: 2026-09-28
- Verdict: **PASS** for the v2 prompt content. This review record does not reconcile other generation gates.
- Sidecar SHA-256: `8986a0955c61a105b4d270d6e6e728312905e7391035295cadaf75a008640d5c`
- Exact v2 prompt body SHA-256 (UTF-8, LF, excluding Markdown fence): `cfc08ed8e2d8e0217f8d97120694e8d7cb58f257cd3ede5524f4c50bdd5efa90`

## Inputs verified

- Source `assets/ponchi/final/J-1.webp`: SHA-256 `87e93c2cb304ef4063c7bdd866dd615fb80ba56033d7d4298634eb992bd2aac7`; matches the v2 prompt and sidecar.
- Character C reference `assets/ponchi/references/character-c-pet-robot.png`: SHA-256 `be52ec9f31ccccc881a164cabf3eb2fe0f7ae1196b04229866b7613d73d636fd`; matches the v2 prompt and sidecar.
- Character B reference `assets/ponchi/references/character-b-teacher-man.png`: SHA-256 `6ce81ea4957f8e2522292e5f48cab2ce718a5e807024f755794079c7283f9c99`; matches the v2 prompt and sidecar.
- Human brief: `content/entries/term_general/J-1_agi[済].md`. It frames AGI as an unsettled concept, contrasts current specialist AI with a hypothetical broad-capability system, and includes a researcher asking how the boundary can be verified.
- The v1 candidate review is HOLD for exact-white background, brain icon, pseudo-text document, large question mark, and unclear visual-perception cue. Those findings are directly addressed in v2.

## Acceptance review

- The prompt preserves two depictions of the same approved Character C robot and one approved Character B researcher, with the intended specialist-left → hypothetical AGI-middle → researcher-right order. It explicitly keeps the researcher beyond the AGI group, prohibits extra people/robots, and retains a dashed hypothetical boundary without claiming AGI has been achieved.
- It replaces the ambiguous capability symbols with exactly three simple cues: abstract language/reasoning, planning/path, and a distinct eye looking toward a framed scene for visual perception. The brain, document/text-like strokes, question mark, cards, and pseudo-text are explicitly removed/prohibited. This closes the prior visual-meaning and text-free findings while remaining aligned with the human brief.
- It preserves the editorial line style, 2:1 composition, approved palette/reference-only neutral regions, and 200px readability requirement. `LOGO_MODE` is not required; the prompt prohibits logos and does not invent a logo clearspace.
- It specifies opaque exact RGB `#FFFFFF` edge to edge, exact-white corners and all 12 registered sample points, a 3% clear perimeter, and no post-generation painting or recoloring. The fail-fast sampling requirement is explicit.
- It identifies the exact source and character-reference paths/hashes, reserves only the internal experiment output path, and prohibits production overwrite, promotion, adoption, publication, and release.

## Gate status

`J-1_candidate_v2.png` was absent at review time. The prompt content is **PASS**, but generation must remain blocked until the sidecar/ledger record this independent review and every applicable wave-level gate is reconciled. Candidate v1 remains HOLD; this review does not approve or promote any image.

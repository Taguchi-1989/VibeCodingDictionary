# J-17 v2 independent prompt review

- Reviewer: `/root/review_wave001_c` (independent of prompt author)
- Review date: 2026-09-28
- Verdict: **PASS** for prompt content; candidate image gates remain separate.
- Sidecar SHA-256: `60fb36e5bf98c44392f40064c1f1070200c86d641df1169edf5f7703aca623fe`
- Exact v2 prompt body SHA-256 (UTF-8, LF, excluding Markdown fence): `1ea328e070f716b0358aee1d606801ed4bdd4c181d21f1eb598a5b351d082984`

## Inputs and source meaning

- Source `assets/ponchi/final/J-17.webp`: actual SHA-256 `241bac1b908021ff04ecc06e7e67e62112118e1857ab4d85c7b1e74b0c1132f9`; matches sidecar and prompt and is read-only.
- Character A reference `assets/ponchi/references/character-a-reader-woman.png`: actual SHA-256 `18e2b7e216bf76cd382002ca4e6caf20ef175332e28ec7b6ab0e5ebc2af7ddf0`; matches sidecar and prompt.
- Human brief `content/entries/term_general/J-17_attention[済].md` specifies five tokens `今日 / の / 天気 / は / ?`, with position 3 (`天気`) selected, thin arrows `3→1` and `3→4`, and thick arrows `3→3` and `3→5`.
- Candidate v1 review passes meaning, 200px readability, Character A, arrow topology/weights, style, and no-logo; it holds only for strict-white background. V2 preserves all accepted semantic/topology properties and scopes its revision to exact-white compliance.

## Acceptance review

- V2 explicitly requires one horizontal row of five blank tiles in order, third selected, with exactly the four required directed links and relative line weights. It prohibits changing directions/count/weights, crossings, a second row, legend, matrix, or extra stage. The observer remains outside the row and matches Character A.
- It prohibits logos and branded content; no logo ROI is required. The approved palette is retained, with neutral clothing colors limited to the reference.
- It requires an opaque flat exact RGB `#FFFFFF` canvas, all corners and eight registered points exact white, and a 3% perimeter. If fail-fast samples pass, the same-size background mask receives independent contour review. No post-generation painting/recoloring is allowed.
- Output is internal-only in the experiment folder; promotion, adoption, publication, and release are prohibited.

## Gate status

`J-17_candidate_v2.png` was absent at review time. Prompt content is **PASS**; keep generation blocked until the independent PASS is reconciled in the applicable gate/ledger. Candidate v1 remains HOLD for its image background result.

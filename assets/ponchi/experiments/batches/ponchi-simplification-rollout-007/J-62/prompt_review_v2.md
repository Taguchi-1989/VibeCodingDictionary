# J-62 v2 independent prompt review

- Reviewer: `/root/review_wave001_c` (independent of prompt author)
- Review date: 2026-09-28
- Verdict: **PASS** for the v2 prompt content. This review record does not reconcile other generation gates.
- Sidecar SHA-256: `469b0e52bef265e0274ca3af31a5ca9e20df33fef61fad09836afe811ffb9841`
- Exact v2 prompt body SHA-256 (UTF-8, LF, excluding Markdown fence): `bc29fbfa08e101f6ac05f73c6ad9453a27c04976a4b1614f40f551baa53771d0`

## Inputs verified

- Source `assets/ponchi/final/J-62.webp`: SHA-256 `32c751fc85aabd3adf82bc6fe60896f5ad8a42e0d278abc31f32c0ee9906739c`; matches the v2 prompt and sidecar.
- Character A reference `assets/ponchi/references/character-a-reader-woman.png`: SHA-256 `18e2b7e216bf76cd382002ca4e6caf20ef175332e28ec7b6ab0e5ebc2af7ddf0`; matches the v2 prompt and sidecar.
- Character C reference `assets/ponchi/references/character-c-pet-robot.png`: SHA-256 `be52ec9f31ccccc881a164cabf3eb2fe0f7ae1196b04229866b7613d73d636fd`; matches the v2 prompt and sidecar.
- Human brief: `content/entries/term_general/J-62_turing_test[人書].md`. It describes a judge exchanging written questions and replies with unseen human and machine respondents, and warns against treating the test as proof of inner understanding or asserting a definitive pass/fail.
- The v1 candidate review is HOLD for exact-white background and apparently duplicated question cards. Other reviewed elements (core meaning, partition, respondents, character identity, text-free treatment, and style) were acceptable. V2 directly addresses both holds.

## Acceptance review

- The prompt preserves the human brief's written, silent exchange: one judge in front of an opaque partition, one generic human and one approved Character C robot behind it, with the wall blocking every direct judge-to-respondent sightline. It preserves Character A as the sole judge, the approved robot appearance/accent, and prohibits extra people/robots.
- It unambiguously specifies exactly four blank cards total: two question cards, first appearing only beyond the wall (one per respondent), and two distinct returning answer cards. The tablet screen is plain; cards are prohibited before the wall, on the judge side of openings, inside openings, or as duplicated/intermediate copies. Separate routes and restrained arrows communicate the exchange. This closes the v1 duplication finding while preserving the source's paired question/reply meaning.
- The prompt prohibits speech/oral cues, readable or pseudo-text, symbols, scores, branded UI, logos, and extra decorative marks. It also says a reply does not prove inner understanding, consistent with the article's caution. `LOGO_MODE` is not required, so no logo or blank logo area is introduced.
- It preserves the editorial line style, approved palette/reference-only neutral regions, 2:1 layout, and 200px readability requirement. It requires opaque exact RGB `#FFFFFF` edge to edge, exact-white corners and all 12 registered points, a 3% perimeter, and no post-generation painting or recoloring.
- Exact source/reference paths and hashes are supplied; output is reserved only under the experiment folder. Production overwrite, promotion, adoption, publication, and release are prohibited.

## Gate status

`J-62_candidate_v2.png` was absent at review time. The prompt content is **PASS**, but generation must remain blocked until the sidecar/ledger record this independent review and every applicable wave-level gate is reconciled. Candidate v1 remains HOLD; this review does not approve or promote any image.

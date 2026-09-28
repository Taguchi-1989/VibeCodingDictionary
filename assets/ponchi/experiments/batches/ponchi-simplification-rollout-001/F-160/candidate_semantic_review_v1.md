# F-160 candidate v1 semantic review

- Verdict: **PASS**
- Review date: 2026-09-27
- Candidate: `F-160_candidate_v1.png`
- Candidate SHA-256: `4609C39419160EA83DAE5AC07474BE96B486A8F84B8CD255752A673DF1B96233`
- Dimensions: 1774×887 (2:1); inspected full-size and at 200×100 px.
- Prompt/source checked: `prompt_v1_1.md`; human brief `content/entries/term_tool/F-160_dom[済].md`. Prompt's source hash matches the current `assets/ponchi/final/F-160.webp`.

## Findings

- The left-to-right chain is visually clear at 200 px: source document → browser/parse cue → hierarchical tree → selected-node action → updated page. The tree has a root and two immediate child branches, with descendants; it preserves the required DOM hierarchy without rendering text labels.
- One existing male character appears at lower left. No extra person or robot appears.
- The document and updated page use abstract line content only; no legible code, words, labels, logos, or branded browser UI are visible.
- White background, navy/blue linework, and preserved neutral-gray character areas fit the stated style. No material semantic, count, or layout regression observed.
- Brief-path check: prompt, metadata, and `ledgers/ponchi_generation_batches.csv` all point to the existing `content/entries/term_tool/F-160_dom[済].md`.

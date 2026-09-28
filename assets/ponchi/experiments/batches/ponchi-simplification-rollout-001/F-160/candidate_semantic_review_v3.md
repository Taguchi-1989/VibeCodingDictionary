# F-160 candidate v3 semantic review

- Verdict: **HOLD for exact-scope compliance; semantic content passes**
- Review date: 2026-09-27
- Candidate: `F-160_candidate_v3.png`
- Candidate SHA-256: `7971DEBD0B0DED69264B37E98507FB2F127632410B63CE9941FE7AB8944F2616`
- Dimensions: 1774×887 (2:1); inspected full-size and after LANCZOS resize to 200×100.
- Compared against: `prompt_v1_3.md`, `revision_v3.md`, and `content/entries/term_tool/F-160_dom[済].md`.
- Source WebP SHA-256 recorded in the prompt matches the source asset: `962808A91EF2E0152731316EE63521261B0C869265D0FF4A812AAD9AE52D2FA4`.
- Edit input v2 SHA-256 matches the prompt/revision: `645D534D1364B07D3DF958AE105DFD749169F21716872D8D92A03E78265905E0`.

## Findings

- **Five-stage flow — PASS.** Full size and 200×100 retain the left-to-right source document → browser parsing → central DOM tree → selected-node action → updated page sequence. Arrows and the selected-descendant cue remain visible. The tree remains rooted above its two branches and descendants; the dotted action cue targets a highlighted lower node.
- **Core meaning — PASS.** The image still communicates browser parsing into a hierarchical in-memory tree and a JavaScript-driven node change reflected in the output page. The gear and pointer/action cue were already present in v2; v3 adds no new claim or explanatory label. The output remains a generic updated page.
- **Character and brand/text constraints — PASS.** One existing male character remains; no additional person or robot is visible. No readable or pseudo-text, logo, watermark, or recognizable branded browser identity appears. The restrained navy, white, and pale-blue treatment remains.
- **Six-dot removal — PASS.** The parser window and result window each have blank header bands in v3; v2 had three dots in each. Neither area received a replacement mark or control.
- **Targeted-only change — FAIL.** The prompt says to remove only those six dots and leave every other part unchanged. A v2→v3 RGB pixel comparison shows broader changes: at a per-pixel max-channel delta threshold of 20, 2.248% of the canvas differs; generous rectangles covering both dot clusters contain 0.193% of the canvas difference, while 2.055% is outside them. The changed-pixel bounding box is `(4, 210)–(1738, 815)`, spanning nearly the full illustration. Fine outlines/positions in the character, browser frame/gear, tree, action cue, and result illustration also differ slightly. Composition and meaning remain intact, but the exact-delta instruction was not met.
- **Thumbnail check — PASS with expected detail loss.** At 200×100, the five stages, arrows, central tree, selected-node cue, output page, and character can still be distinguished; small node details are necessarily reduced.

## Final disposition

Semantic fidelity and visible cleanup pass, but the candidate does not satisfy the prompt's “remove only the six dots” constraint. Overall verdict is **HOLD** on revision-scope compliance. This is the final authorized attempt per `revision_v3.md`; this review records the limitation and does not recommend another image or prompt revision.

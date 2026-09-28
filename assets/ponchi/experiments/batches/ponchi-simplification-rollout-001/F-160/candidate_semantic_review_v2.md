# F-160 candidate v2 semantic review

- Verdict: **HOLD**
- Review date: 2026-09-27
- Candidate: `F-160_candidate_v2.png`
- Candidate SHA-256: `645D534D1364B07D3DF958AE105DFD749169F21716872D8D92A03E78265905E0`
- Dimensions: 1774×887 (2:1); inspected full-size and at 200×100 px.
- Edit target check: candidate v1 SHA-256 is `4609C39419160EA83DAE5AC07474BE96B486A8F84B8CD255752A673DF1B96233`, matching the v1.2 prompt/revision input.
- Source checked: `content/entries/term_tool/F-160_dom[済].md`; original source SHA-256 in prompt matches `assets/ponchi/final/F-160.webp`.

## Findings

- The five-stage flow remains intact and distinguishable at 200 px: source document → browser parsing → hierarchical DOM tree → one selected-node action → updated page. The tree remains central; the existing male character and his pose/identity are preserved.
- Targeted cleanup largely succeeded: document and node placeholder strokes are removed; node geometry and connecting tree lines remain; the laptop screen is blank; plant, mug, and desk clutter are removed. The updated page retains one generic landscape result image, not a text row or branded UI.
- **Blocker:** both the parsing-window frame and result-page frame still have the same three-dot header controls. They remain visible at 200 px and read as repeated browser UI marks, which the v1.2 prompt explicitly directs the edit to remove from browser/page panels. Remove those repeated dots while preserving the generic parsing/result frames and five-stage sequence.
- No readable text, pseudo-text, logo, or product/browser branding is visible. The remaining elements use the approved blue/white palette and preserve the series style.
- The v2 file exists even though the prompt/revision preambles still say generation has not run; this is a status-text mismatch, not the visual blocker above.


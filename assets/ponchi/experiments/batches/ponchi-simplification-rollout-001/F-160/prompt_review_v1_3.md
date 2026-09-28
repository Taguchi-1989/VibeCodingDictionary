# F-160 prompt v1.3 — independent prompt-only review

**Verdict: PASS**

## Evidence

- Reviewed `prompt_v1_3.md`, `revision_v3.md`, `candidate_style_review_v2.md`, the human-authored `content/entries/term_tool/F-160_dom[済].md` brief, `docs/ponchi_image_generation_rules.md`, and the current v2 candidate.
- The v2 edit target is `F-160_candidate_v2.png`, SHA-256 `645d534d1364b07d3df958ae105dfd749169f21716872d8d92a03e78265905e0`, dimensions 1774×887 (2:1). Its hash and dimensions agree with the prompt, revision note, and metadata.
- The v2 style HOLD identifies only the three-dot controls on each of the parser and updated-result windows. The v1.3 prompt explicitly removes those three dots from each header (six total), keeps both generic window frames and blank headers, and forbids replacement marks or any other image edits. The revision note matches this scope and target.

## Findings

- **Targeted correction:** directly resolves the recorded residual-control HOLD without reopening earlier cleanup or permitting broad repainting. “Do not alter any other part” and the explicit keep-list bound the edit to the six dots.
- **Meaning and layout protected:** the source document → browser parsing → DOM tree → one JavaScript node change → updated page sequence remains in the human-confirmed order. The prompt preserves all five stages, arrows and positions, the `html`/`head`/`body` hierarchy and descendants, selected-node cue, and updated-page result. This is consistent with the brief’s HTML-to-DOM-to-JavaScript-to-visible-page explanation.
- **Character protected:** keep the existing male series character with the same identity and design; add no person or robot.
- **Style and policy:** keeps the exact 2:1 composition, current approved colors and existing character-only neutral gray; adds no hues, gray props, texture, or decoration. It prohibits text, pseudo-text, labels, logos, watermarks, branded browser identity, and real or imitated UI marks. The generic frames remain unbranded; removing the dots reduces the remaining UI-like detail.
- **Candidate boundary:** v3 is a new review candidate; the v2 target, original source, and production files are protected. Metadata still records human decision pending and adoption not authorized. The prompt/revision correctly identify this as the final targeted edit.

## Acceptance

The v1.3 prompt and revision note consistently constrain the final edit to the six identified header dots while explicitly protecting both frames and all semantic, layout, character, brand, text, and palette constraints. Prompt review passes; this does not approve or visually validate a future v3 image.

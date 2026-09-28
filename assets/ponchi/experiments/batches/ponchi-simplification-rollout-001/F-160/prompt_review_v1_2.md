# F-160 prompt v1.2 — independent prompt-only review

**Verdict: PASS**

## Evidence

- Reviewed `prompt_v1_2.md` and `revision_v2.md` against the prior semantic PASS, the style HOLD, the human-authored `[済]` brief, and the v1 candidate.
- The proposed edit input is `F-160_candidate_v1.png`, SHA-256 `4609c39419160ea83dae5ac07474be96b486a8f84b8cd255752a673df1b96233`, dimensions 1774×887. The actual candidate hash and dimensions match the prompt and revision note.
- The v2 output target is a new candidate file; no v2 image exists at review time.

## Findings

- The prior HOLD concerned text-like placeholder strokes, repeated UI rows, and small desk props. The revision explicitly removes text-like strokes and repeated UI marks across the source, browser/page/result and auxiliary panels, and laptop screen. Replacement shapes must be isolated, non-text geometry, not rows, writing, controls, icons, or data.
- It also removes the laptop and desk items where separable without harming the character. The fallback is bounded: if part of the laptop must remain to preserve the pose, its screen stays blank with at most one simple geometric shape.
- The five human-confirmed stages remain ordered: source document, browser parsing, central DOM tree, one node change, updated page. The root/head/body hierarchy, node shapes, connector lines, changed-node cue, arrows, and one existing male character are explicitly preserved. No new stage, example, or concept is added.
- The no-text policy is consistent: HTML/DOM structure must be communicated by the document-to-tree relationship and node hierarchy, not rendered labels. The prompt prohibits pseudo-text, text-like strokes, code, logos, browser branding, and branded UI.
- The 2:1 composition and approved palette are retained; gray is limited to existing character areas, with no gray props or other hues. Candidate v1, original source, and production files cannot be overwritten.
- The revision note matches the prompt's target hash, dimensions, correction scope, five-stage flow, and new output path. No material new ambiguity or overbroad semantic deletion found.

## Acceptance

The revision directly addresses the recorded pseudo-text/UI clutter HOLD while retaining the human-authored flow, tree hierarchy, character, brand restrictions, palette, and no-text rules.

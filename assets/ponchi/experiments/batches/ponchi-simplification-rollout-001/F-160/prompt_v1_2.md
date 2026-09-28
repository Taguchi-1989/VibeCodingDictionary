# F-160 DOM — targeted v1.2 image-edit prompt

Status: candidate v1 semantic review passed; style review held for text-like placeholder rows and repeated UI marks. This prompt targets a v2 edit of candidate v1; no v2 image has been generated.

## Source and human-confirmed fields

- Entry: F-160 — DOM
- Human brief: content/entries/term_tool/F-160_dom[済].md
- Original source: assets/ponchi/final/F-160.webp
- Original source SHA-256: 962808a91ef2e0152731316ee63521261b0c869265d0ff4a812aad9ae52d2fa4
- Candidate v1 edit target: assets/ponchi/experiments/batches/ponchi-simplification-rollout-001/F-160/F-160_candidate_v1.png
- Candidate v1 SHA-256: 4609c39419160ea83dae5ac07474be96b486a8f84b8cd255752a673df1b96233
- Candidate v1 dimensions: 1774x887 (2:1)
- Intended meaning: The browser parses HTML into an in-memory DOM tree; JavaScript can operate on that tree and the visible page changes.
- Layout and reading order: One left-to-right flow: HTML source document → browser parsing → central DOM tree → one JavaScript node operation → updated page. Preserve this order and each of its five stages.
- Brand record: docs/brand_usage_audit.md has no F-160 brand asset; ledgers/ponchi_generation_batches.csv row F-160 says logo_avoid and not_needed. Generic, unbranded diagram.
- Logo mode: not_required.
- Character policy: Preserve the one existing male series character and design from candidate v1. Add no other person or robot.

## Instantiated image-edit prompt

Use the attached candidate v1 image as the exact edit target. Do not use the original final image as the edit target or as a loose reference. Keep the exact 2:1 canvas.

ENTRY_ID: F-160
ENTRY_TITLE: DOM (context only; do not draw these words)
EDIT_TARGET_PATH: assets/ponchi/experiments/batches/ponchi-simplification-rollout-001/F-160/F-160_candidate_v1.png
EDIT_TARGET_SHA256: 4609c39419160ea83dae5ac07474be96b486a8f84b8cd255752a673df1b96233
EDIT_TARGET_VERSION: candidate v1, 1774x887

INTENDED MEANING (human-confirmed):
The browser parses HTML into a DOM tree in memory; JavaScript can operate on that tree and the visible page changes.

LAYOUT AND READING ORDER (human-confirmed):
Preserve one left-to-right sequence: source document → browser parsing → one central tree rooted at html with head/body and descendants → one JavaScript node change → one updated page.

MUST KEEP:
- The distinction between an HTML source document and the DOM tree created by browser parsing.
- One central, clearly hierarchical tree with html as root and head/body beneath it.
- One JavaScript action changing one selected node, followed by one visibly updated page.
- The existing male series character, with the same identity and established design.

TARGETED CLEANUP:
- Remove all horizontal text-like placeholder strokes and repeated UI marks from the source-document card, browser/page/result panels, other small panels, and the character’s laptop screen. Do not replace them with lines, pseudo-text, glyphs, or tiny controls.
- Remove repeated menu/list rows, button-like marks, thumbnail grids, and duplicate panel details throughout the image.
- Replace any removed source/page/result placeholder rows only with the minimum non-text geometric cue needed to preserve the stage: for example, one simple pale-blue filled rectangle or one navy circle/square. Do not arrange these cues as rows or make them resemble writing, controls, icons, or data.
- Remove the laptop, desk surface, plant, and mug where they can be separated without damaging the character’s body, hands, or pose. Add no replacement prop. If part of the laptop must remain to preserve the pose, leave its screen blank white with at most one simple geometric shape and no strokes or UI marks.

Preserve the DOM node circles/squares and connecting tree lines, the browser parsing cue, the single changed-node cue, and the arrows needed to read the five-stage flow. Do not add stages, examples, or concepts. Do not draw any readable code, words, labels, letters, numbers, logos, branded browser identity, or watermarks.

SERIES STYLE
- Preserve the clean minimal editorial line illustration and exact 2:1 composition.
- Palette: white #FFFFFF, deep navy #123E82, near-black #1A1A1A, pale blue #EAF1FB. Keep only neutral-gray character areas already in candidate v1; add no gray props or other hues.
- Use uniform linework. Add no textures, grain, speckles, shadows, glow, or decorative background.

BRAND AND TEXT
LOGO_MODE: not_required. No logo clearspace is needed.
Do not create or imitate any company/service logo, browser icon, framework mark, mascot, branded interface, or brand-color treatment. Do not generate text-like strokes, pseudo-text, words, letters, numbers, labels, or watermark.

CHARACTERS
Keep the existing male series character’s identity and design. Add no person, robot, or replacement design.

OUTPUT
Return one clean 2:1 PNG candidate for review. Preserve the candidate v1 canvas dimensions if supported. Do not upscale a smaller result or overwrite candidate v1, the original source, or any production file.

# C-51 candidate prompt — ponchi-simplification-v1.1

Status: prompt review passed; candidate v1 generated; independent candidate image review pending.

## Source and human-confirmed meaning

- Entry: C-51 — Dario Amodei
- Human-authored source: `content/entries/person/C-51_dario_amodei[済].md`
- Current image: `assets/ponchi/final/C-51.webp`
- Current image SHA-256: `243d719483df7edf81827f7b8950f850f871b59276ce128697ef6a8fd4272cbe`
- Source version: current final, inventoried 2026-09-27
- Intended meaning: Show Dario Amodei as a public speaker on AI safety and future impacts through four milestones: Anthropic co-founding, Constitutional AI research, the “Machines of Loving Grace” essay, and public policy discussion.
- Brand record: `ledgers/ponchi_generation_batches.csv` row C-51 (`logo_need=not_needed`, `logo_status=logo_avoid`); no company logo is required.
- Logo mode: `not_required`
- Character policy: Keep one existing male Dario-like silhouette and the one existing pet robot only where it serves the authored Constitutional AI milestone; remove the other source-scene people. Do not add or redesign characters.

## Instantiated image-edit prompt

```text
Edit only the exact logo-free source image attached as the reference.
ENTRY_ID: C-51
ENTRY_TITLE: Dario Amodei (context only; do not draw these words)
SOURCE_IMAGE_PATH: assets/ponchi/final/C-51.webp
SOURCE_IMAGE_SHA256: 243d719483df7edf81827f7b8950f850f871b59276ce128697ef6a8fd4272cbe
SOURCE_IMAGE_VERSION: current final, inventoried 2026-09-27

INTENDED MEANING (human-confirmed):
Depict Dario Amodei as a public speaker on AI safety and future impacts through four chronological milestones: co-founding Anthropic, Constitutional AI research, the “Machines of Loving Grace” essay, and public policy discussion.

LAYOUT AND READING ORDER (human-confirmed; preserve exactly):
The current image has four vignette groups linked around a central building; the authored entry memo explicitly specifies a single horizontal four-point timeline, so the memo takes precedence. Read left to right: co-founding (2021), Constitutional AI research (2022 onward), the essay (2023 onward), then public policy discussion (2024 onward). Use one small, consistent male speaker silhouette and four simple milestone icons; retain four small, empty speech-bubble outlines as cues, with no text inside. The chronology is conveyed by position only; do not write dates or labels.

MUST KEEP:
- Exactly four ordered milestone nodes: founding, safety research, essay, and policy discussion.
- One consistent male speaker silhouette from the source; keep him secondary to the timeline.
- The existing pet robot only as the simple Constitutional AI safety icon; preserve its identity and design.
- Distinct, simple icon cues for the four milestones: an office/building, a shield, a book with pen, and a government-building/microphone. Keep them separate and readable.
- One left-to-right timeline; do not reconnect the nodes as branches around a central hub.

REMOVE ONLY THESE CONFIRMED REDUNDANT OR CONFLICTING DETAILS:
- The central building hub and its branching connector layout, which conflict with the authored linear timeline.
- The unrelated collaboration, interface, chart, growth-graph, and crowd vignettes; keep only the four authored milestones.
- All other people in the source scenes; the authored illustration memo specifies one male speaker figure.
- Any title, date, word, letter, number, code, pseudo-text, logo, brand-like mark, or watermarked detail.

Preserve the exact 2:1 canvas and the recorded human-authored timeline. Keep all four events distinct and in order. Do not imply that Dario personally authored all Anthropic policy or that a single speech represents the whole company.

Simplify to four bold timeline nodes that remain recognizable at 200px thumbnail width. Use clean, flat shapes and minimal internal detail. Do not add panels, extra events, charts, people, or decorative elements.

SERIES STYLE
- Minimal editorial line illustration for a Japanese technical book.
- Wide 2:1 landscape on pure white #FFFFFF.
- Use only white #FFFFFF, deep navy #123E82, near-black #1A1A1A, and pale blue #EAF1FB. Do not add gray or another hue.
- Prefer flat fills and uniform linework. No texture, grain, glow, drop shadows, glossy 3D, or decorative background.
- Keep the timeline and its four event cues legible at 200px width.

BRAND AND TEXT
- LOGO_MODE: not_required, explicitly supported by the C-51 generation-batch row.
- Do not generate or imitate Anthropic/Claude logos, official marks, branded UI, or brand-color substitutes.
- Do not draw any words, letters, numbers, dates, labels, captions, code, pseudo-text, or watermarks.

CHARACTERS
CHARACTER_POLICY: Preserve exactly one existing male Dario-like silhouette and the existing pet robot only as the safety-research icon. Remove the other people as listed above. Do not add, duplicate, or redesign any character.

OUTPUT
Return one clean 2:1 PNG candidate at the highest supported native resolution. Aim for a long edge of at least 1500px; do not upscale a smaller result. Do not alter or overwrite any production file.
```

# A-6 candidate prompt — ponchi-simplification-v1

Status: candidate v2 reviewed; focused semantic/style checks pass, with a source-layout deviation recorded. Human decision remains pending. See `review_v1.md`, `revision_v2.md`, and `review_v2.md`.

## Source and human-confirmed meaning

- Entry: A-6 — 評価日・時変情報の見方
- Source image: `assets/ponchi/final/A-6.webp`
- Source SHA-256: `8a809bfc3ff8df00fe6582ed4f71273ac7e0a956f83a1799810c5f702c78b2e5`
- Source version: current final as inventoried on 2026-09-27
- Intended meaning: Each entry describes information as of its evaluation date. Optional `version_status` and `pricing_note` fields describe time-varying facts; when either is present, its source note must also record a checked date.
- Brand record: `ledgers/ponchi_generation_batches.csv`, A-6 row (`logo_avoid`; non-brand base candidate). No official brand asset is required for this generic date-and-status legend.
- Logo mode: `not_required`
- Character policy: No fixed character is required by A-6's human-authored brief. Remove the incidental people and pet robot shown in the current illustration; create no character.
- Planned output: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-001/A-6/A-6_candidate_v1.png`

## Instantiated image-edit prompt

```text
Use Image 1 as the exact edit target. It is the current logo-free A-6 illustration; do not use it as a loose style reference.

ENTRY_ID: A-6
ENTRY_TITLE: 評価日・時変情報の見方 (context only; do not draw these words)
SOURCE_IMAGE_PATH: assets/ponchi/final/A-6.webp
SOURCE_IMAGE_SHA256: 8a809bfc3ff8df00fe6582ed4f71273ac7e0a956f83a1799810c5f702c78b2e5
SOURCE_IMAGE_VERSION: current final, inventoried 2026-09-27

INTENDED MEANING (human-authored entry brief):
Each entry describes information as of its evaluation date. Optional version_status and pricing_note fields describe time-varying facts; when either field is present, its source note must also record a checked date.

MUST KEEP:
- Exactly three distinct information groups: one required evaluation-date group and two optional groups, version status and pricing note.
- The calendar-and-clock pictogram is the required evaluation-date group itself; do not create a separate calendar anchor or duplicate it.
- A single small checked-date cue shared by the two optional groups, without adding another calendar pictogram.
- The optional version-status group uses three equal dots in one approved navy or near-black color as abstract possible states; do not mark or imply that any one state is selected.
- The optional pricing-note group uses one generic, unbranded tag outline with three equal dots in that same approved color; do not mark or imply a specific price or pricing state.
- A clean 2:1 landscape composition suitable for the front-matter legend.

REMOVE ONLY THESE CONFIRMED UNNECESSARY DETAILS:
- The incidental people and pet robot; the A-6 human-authored brief does not require characters.
- The books, plant, mug, laptop, desk/table edges, and other scene props.
- Repeated timelines, multiple charts, duplicate dashboards, stacks of miniature cards, decorative device/browser frames, and connector arrows between unrelated panels.
- Gray dashboard fills and any color outside the approved palette.
- Any pseudo-text, labels, letters, numbers, currency marks, or watermark.

Edit the source into a much simpler visual legend while preserving the exact 2:1 aspect ratio and its general left-to-right balance. Use exactly three clearly separated, compact field groups: the calendar-with-clock is the required evaluation-date group; the other two groups represent the optional version-status and pricing-note fields. Give the status group three equal, identical-color, unselected navy or near-black dots as abstract possible states. Give the pricing group a generic, unbranded tag outline with three equal, identical-color, unselected navy or near-black dots. A single small navy or near-black check mark shared by the two optional groups indicates that their sources require a checked date. Keep the optional groups visually secondary but clearly separate. Do not create a fourth group, duplicate the calendar, select a status or price, or turn this into a general workflow or dashboard.

Keep the main forms large and recognizable at 200px thumbnail width. Preserve the correct relationship between the required evaluation date and the two optional fields. Do not invent examples, dates, service names, exact prices, or extra relationships.

SERIES STYLE
- Minimal editorial line illustration for a Japanese technical book.
- Wide 2:1 landscape on pure white #FFFFFF.
- For diagrams and background, use only deep navy #123E82, near-black #1A1A1A, pale blue #EAF1FB, and white #FFFFFF. Do not introduce gray or any other hue. The fixed-character gray exception does not apply because this image has no characters.
- Prefer clean flat fills and uniform linework. Gradients are permitted only from navy to pale blue, sparingly.
- No texture, grain, speckles, shadows, ambient glow, glossy 3D, or decorative background.

BRAND AND TEXT
- This is a generic, non-brand legend (`LOGO_MODE=not_required`); do not reserve logo clearspace.
- Keep the version-status dots and pricing-tag marks abstract, generic, and unselected; do not invent a concrete state or price.
- Do not generate or imitate any company/service/product logo, app or product icon, official mark, mascot, or branded UI.
- Do not draw words, letters, numbers, currency symbols, fake text, labels, captions, or watermarks.

OUTPUT
Return one clean 2:1 PNG candidate at the highest supported native resolution, aiming for a long edge of at least 1500px. Do not upscale a smaller result or claim print-master resolution. Do not overwrite or modify any production file.
```

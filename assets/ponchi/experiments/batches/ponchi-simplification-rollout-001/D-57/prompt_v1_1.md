# D-57 candidate prompt — ponchi-simplification-v1.1

Status: prompt draft pending independent review. Base-only internal candidate; no image has been generated.

## Source and human-confirmed meaning

- Entry: D-57 — Flow
- Human-authored source: `content/entries/model/D-57_flow[済].md`
- Current final: `assets/ponchi/final/D-57.webp` (SHA-256 `ed5bddf84b1bd1a642f6b855ec137b93256f126357701f76c078f5d5094908b1`)
- Editable logo-free base: `assets/ponchi/experiments/batches/ponchi-batch-006/D-57_base_1254x627.png`
- Editable base SHA-256: `9945d5fdb122328c2a28c0ee9184060311b7e1e9b247a673bba952edb9c9c971`
- Base verification: current final PNG hash equals `ponchi-batch-006/D-57_overlay_1254x627.png`; its overlay metadata names the above base. The base is the only permitted image-edit input.
- Brand record: `ledgers/ponchi_generation_batches.csv` row D-57 (`official_logo_applied`); `docs/brand_usage_audit.md` lines 313–333 and 1121–1129.
- Official asset: `assets/logos/google-flow/flow_favicon_w_on-approved-blue-plate.png` (SHA-256 `48948946ee82bff301e7c5243e128610b78edbbb63e56df05bf54de6432a30f6`); official white favicon from `https://labs.google/fx/tools/flow` / `https://labs.google/fx/icons/favicon/flow_favicon_w.png`, retrieved 2026-06-03.
- Use conditions: review pending; standalone Flow lockup not confirmed. Use `internal_base_only`; no overlay, adoption, or publication.
- Intended meaning: Flow is a creator-facing video studio combining scene building, camera controls, and asset management in one workspace.
- Character policy: Keep the one existing creator figure. Do not add, duplicate, or redesign people, robots, or mascots.

## Instantiated image-edit prompt

```text
Edit only the exact logo-free base image attached as the reference.
ENTRY_ID: D-57
ENTRY_TITLE: Flow (context only; do not draw these words)
SOURCE_IMAGE_PATH: assets/ponchi/experiments/batches/ponchi-batch-006/D-57_base_1254x627.png
SOURCE_IMAGE_SHA256: 9945d5fdb122328c2a28c0ee9184060311b7e1e9b247a673bba952edb9c9c971
SOURCE_IMAGE_VERSION: logo-free base paired with the current final overlay, verified 2026-09-27

INTENDED MEANING (human-confirmed):
Flow is a creator-facing video studio that combines scene building, camera controls, and asset management in one workspace.

LAYOUT AND READING ORDER (human-confirmed; preserve exactly):
The current base shows a dense multi-step software workflow. The authored entry memo explicitly specifies one central studio window with Scene Builder on the left, Camera Controls at upper right, and Asset Management at lower right; that arrangement takes precedence. Keep the existing creator figure secondary to this central window. Use only generic abstract interface shapes, not a realistic or branded UI.

MUST KEEP:
- One central, generic studio-window diagram.
- Three separate functions in the authored positions: Scene Builder at left; Camera Controls at upper right; Asset Management at lower right.
- One existing creator figure operating the studio; keep the person count and design unchanged.
- The three functions read as parts of one studio workspace, not as separate products or a four-stage workflow.
- A calm white negative-space rectangle in the upper right for the recorded official icon overlay: LOGO_CLEARSPACE_RECT [1000,0,206,130]. Keep it empty in the generated base.

REMOVE ONLY THESE CONFIRMED REDUNDANT OR CONFLICTING DETAILS:
- Extra workflow panels, repeated timelines, duplicate preview screens, and arrows that turn the studio into a multi-stage process.
- Dense scenic thumbnails, miniature controls, toolbar icons, duplicate asset cards, and repeated sliders; keep only a few abstract cues for the three authored functions.
- Any additional person/robot, real or branded UI detail, Google/Flow/Veo/Imagen/Gemini mark, logo, text, fake control label, or watermark.
- Any drawing, person, face, hand, essential node, arrow, or pattern from the upper-right logo clearspace.

Preserve the exact 2:1 canvas and the stated three-part arrangement. Keep all three functions separate and legible. Do not draw words, letters, numbers, code, fake text, branded controls, or a recognizable product screenshot.

Simplify the interface into three large functional areas that remain distinct at 200px thumbnail width. Let the creator remain secondary and the central studio window fill more than half of the canvas width.

SERIES STYLE
- Minimal editorial line illustration for a Japanese technical book.
- Wide 2:1 landscape on pure white #FFFFFF.
- Use only white #FFFFFF, deep navy #123E82, near-black #1A1A1A, and pale blue #EAF1FB. Do not add gray or another hue.
- Prefer flat fills and uniform linework. No texture, grain, glow, drop shadows, glossy 3D, or decorative background.
- No visual element in LOGO_CLEARSPACE_RECT; the official asset's blue plate is applied separately and unchanged.

BRAND AND TEXT
- Brand record: `docs/brand_usage_audit.md` D-57 / `ponchi-batch-006`; official white Flow favicon on approved blue plate, review-pending icon overlay.
- LOGO_MODE: internal_base_only
- LOGO_RECT: [1066,36,140,59] (official asset scaled proportionally; 48px right margin)
- LOGO_CLEARSPACE_RECT: [1000,0,206,130]
- OFFICIAL_ASSET_PATH: assets/logos/google-flow/flow_favicon_w_on-approved-blue-plate.png
- OFFICIAL_ASSET_SHA256: 48948946ee82bff301e7c5243e128610b78edbbb63e56df05bf54de6432a30f6
- OFFICIAL_ASSET_SOURCE_URL: https://labs.google/fx/tools/flow (favicon: https://labs.google/fx/icons/favicon/flow_favicon_w.png)
- OFFICIAL_ASSET_RETRIEVED_AT: 2026-06-03
- USE_CONDITIONS_STATUS: review_pending; internal_base_only; no logo overlay, adoption, or publication; standalone Flow lockup not confirmed.
- Do not generate, imitate, redraw, or composite any Google/Flow/Veo/Imagen/Gemini mark or brand-colored substitute. Leave the exact clearspace empty.
- Do not draw words, letters, numbers, labels, captions, code, fake text, or watermarks.

CHARACTERS
CHARACTER_POLICY: Preserve the one existing creator figure in the source without duplication or redesign. Add no person or robot.

OUTPUT
Return one clean 2:1 PNG candidate at the highest supported native resolution. Aim for a long edge of at least 1500px; do not upscale a smaller result. This is an internal base-only candidate, not publication-ready. Do not alter or overwrite any production file.
```

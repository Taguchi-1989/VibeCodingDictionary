# C-59 candidate prompt — ponchi-simplification-v1.1

Status: prompt review passed; candidate v1 generated; independent candidate image review pending.

## Source and human-confirmed meaning

- Entry: C-59 — Jensen Huang
- Human-authored source: `content/entries/person/C-59_jensen_huang[済].md`
- Current image: `assets/ponchi/final/C-59.webp`
- Current image SHA-256: `d4e94f5e43d65ffb91d92322211812b704066f1f2397a3e454a7e151c1734d65`
- Source version: current final, inventoried 2026-09-27
- Intended meaning: Show three career/company milestones that connect Jensen Huang's GPU strategy to today's AI-chip demand: NVIDIA co-founding, CUDA, and the 2024–2025 generative-AI investment boom.
- Brand record: `ledgers/ponchi_generation_batches.csv` row C-59 (`logo_need=not_needed`, `logo_status=logo_avoid`); no company logo is required.
- Logo mode: `not_required`
- Character policy: Keep one existing Jensen-like male figure only. Do not add or redesign people, robots, or mascots.

## Instantiated image-edit prompt

```text
Edit only the exact logo-free source image attached as the reference.
ENTRY_ID: C-59
ENTRY_TITLE: Jensen Huang (context only; do not draw these words)
SOURCE_IMAGE_PATH: assets/ponchi/final/C-59.webp
SOURCE_IMAGE_SHA256: d4e94f5e43d65ffb91d92322211812b704066f1f2397a3e454a7e151c1734d65
SOURCE_IMAGE_VERSION: current final, inventoried 2026-09-27

INTENDED MEANING (human-confirmed):
Show Jensen Huang's role through three ordered milestones: NVIDIA's founding as a GPU company, CUDA opening GPU computing to research, and 2024–2025 demand for AI chips during the generative-AI investment boom.

LAYOUT AND READING ORDER (human-confirmed; preserve exactly):
The source is a dense infrastructure-and-applications map. The authored entry memo explicitly specifies a three-point horizontal timeline, so that layout takes precedence. Read left to right: founding, CUDA, then AI-chip demand. Place one small, consistent Jensen-like figure alongside the timeline. Use only simple event icons; represent dates and labels by order and icon meaning, with no rendered words or numbers.

MUST KEEP:
- Exactly three distinct, ordered milestone nodes: GPU-company founding; CUDA enabling general GPU computing; later AI-chip demand.
- One existing Jensen-like male figure as the sole person, secondary to the timeline.
- A simple generic GPU/chip cue at the first node, an abstract computation/network cue at the second, and generic AI-chip/server demand at the third.
- One clear horizontal timeline; keep the three milestone groups separate and in order.
- No claim about company valuation, market rank, or product specifications.

REMOVE ONLY THESE CONFIRMED REDUNDANT OR CONFLICTING DETAILS:
- The dense multi-level server racks and their repeated module/port details.
- The separate application panels for code, chat, images, video, robotics, and other compute uses; these are not the three milestones in the authored memo.
- The charts, small infrastructure strip, connector branches, and secondary computer operator.
- Any NVIDIA or product logo, branded icon, realistic product UI, title, date, word, letter, number, code, pseudo-text, or watermark.

Preserve the exact 2:1 canvas and the author-defined three-node chronology. Use generic unbranded technology forms only. Do not depict NVIDIA's logo, a recognizable official GPU mark, or a branded interface.

Reduce the illustration to three large timeline nodes and one secondary figure, readable at 200px thumbnail width. Avoid small repeated server components, tiny cards, and detailed dashboards.

SERIES STYLE
- Minimal editorial line illustration for a Japanese technical book.
- Wide 2:1 landscape on pure white #FFFFFF.
- Use only white #FFFFFF, deep navy #123E82, near-black #1A1A1A, and pale blue #EAF1FB. Do not add gray or another hue.
- Prefer flat fills and uniform linework. No texture, grain, glow, drop shadows, glossy 3D, or decorative background.
- Keep the timeline and three event cues legible at 200px width.

BRAND AND TEXT
- LOGO_MODE: not_required, explicitly supported by the C-59 generation-batch row.
- Do not generate or imitate NVIDIA, H100, CUDA, or any company/product logo, official mark, branded UI, or brand-color substitute.
- Do not draw words, letters, numbers, dates, labels, captions, code, pseudo-text, or watermarks.

CHARACTERS
CHARACTER_POLICY: Preserve exactly one existing Jensen-like male figure without duplication or redesign. Add no people or robots.

OUTPUT
Return one clean 2:1 PNG candidate at the highest supported native resolution. Aim for a long edge of at least 1500px; do not upscale a smaller result. Do not alter or overwrite any production file.
```

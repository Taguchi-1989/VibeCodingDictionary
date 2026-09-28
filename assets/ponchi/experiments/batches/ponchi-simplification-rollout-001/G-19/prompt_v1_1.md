# G-19 candidate prompt — ponchi-simplification-v1.1

Status: original prompt for candidate v1; reviews were partial on the initial-write ratio. Follow-up edits are tracked in `revision_v2.md` through `revision_v4.md`; latest candidate v4 remains partial and is not adopted.

## Source and human-confirmed meaning

- Entry: G-19 — Prompt Caching
- Human-authored source: `content/entries/term_llm/G-19_prompt_caching[済].md`
- Source image: `assets/ponchi/final/G-19.webp`
- Source SHA-256: `cda57e5cc06f5919e97f90e2bc06ee66aa6f963cc1220d8a76e9b576ce1c7707`
- Source version: current final, inventoried 2026-09-27
- Intended meaning: Reusing the same long instruction through prompt caching lowers repeated input-token cost. The source specifies ten uncached full-cost requests, a cache-write request at about 1.25 times the normal write cost, and each later cache-hit request at about one-tenth the normal input charge; these are per-request amounts, not a claim that caching removes requests or cuts the entire group total to one-tenth.
- Brand record: `ledgers/ponchi_generation_batches.csv` row G-19 (`logo_avoid`); generic non-brand comparison.
- Logo mode: `not_required`
- Character policy: Keep the single existing engineer from the source as the one person at a generic API console; do not duplicate, redesign, or add people or robots.
- Planned output: `assets/ponchi/experiments/batches/ponchi-simplification-rollout-001/G-19/G-19_candidate_v1.png`

## Instantiated image-edit prompt

```text
Edit only the exact logo-free base image attached as the reference.

ENTRY_ID: G-19
ENTRY_TITLE: Prompt Caching (context only; do not draw these words)
SOURCE_IMAGE_PATH: assets/ponchi/final/G-19.webp
SOURCE_IMAGE_SHA256: cda57e5cc06f5919e97f90e2bc06ee66aa6f963cc1220d8a76e9b576ce1c7707
SOURCE_IMAGE_VERSION: current final, inventoried 2026-09-27

INTENDED MEANING (human-confirmed):
The same long instruction is sent repeatedly without caching, creating repeated full-cost request charges. With prompt caching, later requests reuse the cached instruction and have a much smaller input charge.

LAYOUT AND READING ORDER (human-confirmed; preserve exactly):
Two before/after panels read from left to right. Show the same ten request rows in each panel. On the left, all ten rows have equal full-cost billing marks. On the right, show one initial cache-write request with a billing mark 1.25 times as long as a normal full-cost mark, followed by nine cache-hit requests, each with a billing mark one-tenth as long as a normal full-cost mark. Keep the one existing engineer in the source at a generic API console as a single secondary figure; do not duplicate the person. The per-request difference on later cache hits is the main visual message. The ten rows are a schematic sample, not a total-cost claim.

MUST KEEP:
- Exactly two clearly separate comparison groups with ten aligned request rows each: uncached repeated requests on the left, cached reuse on the right.
- The same long instruction document is represented as the input in both groups; the right group reuses it from a simple cache boundary.
- Ten equal full-cost billing marks on the left. On the right, one initial cache-write mark 1.25 times the length of a normal full-cost mark, followed by nine hit marks each one-tenth as long as a normal full-cost mark. These lengths represent per-request charges only, not one-tenth the total of ten requests.
- One plain shelf line supporting the compact billing rows; do not add a cabinet, room, or scene background.
- One engineer from the source at one generic API console, secondary to the bill comparison.
- A simple one-way reading order from left to right. Do not imply caching removes the need to send new user requests.

REMOVE ONLY THESE CONFIRMED REDUNDANT DETAILS:
- Repeated intermediate request cards, repeated small process panels, extra icon rows, duplicate cache/search loops, and miniature charts that restate the cost contrast.
- The notebook, plant, mug, and decorative desk details; retain only the single simple API console needed by the source brief.
- Product names, Anthropic/Claude/Claude Code marks, logos, branded UI, and any generated or imitated app screen.
- Pseudo-text, code, labels, captions, dates, numbers, currency symbols, exact prices, or watermarks.

Preserve the exact 2:1 canvas. Follow LAYOUT AND READING ORDER exactly. Keep the two comparison groups separate, left before and right after. Retain every element and relationship under MUST KEEP. Remove only the details under REMOVE. Do not add a third state, new workflow, additional savings claim, or new relationship.

Reduce visual clutter so repeated-instruction reuse and the smaller per-hit charge remain unmistakable at 200px thumbnail width. Use ten simple aligned line marks per side without surrounding each row in its own card; make the nine short hit marks visibly shorter than a full-cost mark. Do not add other intermediate request cards or tiny repeated panels.

SERIES STYLE
- Minimal editorial line illustration for a Japanese technical book.
- Wide 2:1 landscape on pure white #FFFFFF.
- Use only white #FFFFFF, deep navy #123E82, near-black #1A1A1A, and pale blue #EAF1FB for diagrams and backgrounds. Do not introduce gray or another hue. There is no fixed-character gray exception for the source person unless a separately approved character reference confirms it.
- Prefer clean flat fills and uniform linework. Gradients are permitted only within navy-to-pale-blue, sparingly.
- No texture, grain, speckles, decorative or ambient glow, drop shadows, glossy 3D, or decorative background.
- Preserve the core meaning at 200px thumbnail width.

BRAND AND TEXT
- This is a generic, non-brand comparison (`LOGO_MODE=not_required`); do not reserve logo clearspace.
- Do not generate or imitate a company/service/product logo, app or product icon, official mark, mascot, or branded UI.
- Do not draw words, letters, numbers, fake text, code, captions, labels, currency symbols, prices, or watermarks.

CHARACTERS
CHARACTER_POLICY: Preserve the single existing engineer from the source without duplication or redesign. Do not add another person or a robot.

OUTPUT
Return one clean 2:1 PNG candidate at the highest supported native resolution. Aim for a long edge of at least 1500px. Do not upscale a smaller result or claim print-master resolution. Do not alter or overwrite any production file.
```

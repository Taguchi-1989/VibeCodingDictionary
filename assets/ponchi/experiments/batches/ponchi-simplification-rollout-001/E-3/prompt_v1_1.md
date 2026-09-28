# E-3 candidate prompt — ponchi-simplification-v1.1

Status: prompt draft pending independent review. No image has been generated.

## Source and human-confirmed meaning

- Entry: E-3 — Terminal-Bench
- Human-authored source: `content/entries/benchmark/E-3_terminal_bench[済].md`
- Current image: `assets/ponchi/final/E-3.webp`
- Current image SHA-256: `64640902d2aedab4d189fb83cc8324525e174ddacce299cc2278e168b05cd1fb`
- Source version: current final, inventoried 2026-09-27
- Intended meaning: Terminal-Bench measures whether an agent can complete multi-step CLI work, distinguishing terminal task execution from code generation alone.
- Brand record: `ledgers/ponchi_generation_batches.csv` row E-3 (`logo_need=not_needed`, `logo_status=logo_avoid`); no logo is required.
- Logo mode: `not_required`
- Character policy: Keep the one existing pet robot as the agent. The authored figure memo specifies a single robot; remove the two human figures. Do not add or redesign characters.

## Instantiated image-edit prompt

```text
Edit only the exact logo-free source image attached as the reference.
ENTRY_ID: E-3
ENTRY_TITLE: Terminal-Bench (context only; do not draw these words)
SOURCE_IMAGE_PATH: assets/ponchi/final/E-3.webp
SOURCE_IMAGE_SHA256: 64640902d2aedab4d189fb83cc8324525e174ddacce299cc2278e168b05cd1fb
SOURCE_IMAGE_VERSION: current final, inventoried 2026-09-27

INTENDED MEANING (human-confirmed):
Terminal-Bench measures whether an agent can complete a chain of CLI tasks. Make the distinction between code generation and completing terminal work clear.

LAYOUT AND READING ORDER (human-confirmed; preserve exactly):
The source has four dense panels and two human figures. The authored entry memo explicitly specifies one robot agent at a terminal and a left-to-right sequence, so that layout and character count take precedence. Show task input, command action, file/result check, next-step decision, and completion/scoring as one clear sequence. At each stage, use a compact input → check → decision cue; do not turn the stages into unrelated dashboards.

MUST KEEP:
- One existing pet robot at one generic terminal, as the sole character.
- One left-to-right task chain: task instruction, command action, file/result check, next-step decision, and completion/scoring.
- Small repeated input/check/decision cues that show the agent evaluates intermediate results before continuing.
- A simple completion gauge without a numeric score; keep it distinct from the command sequence.
- The distinction between terminal-task completion and code generation, using a simple generic contrast only if it fits the same sequence.

REMOVE ONLY THESE CONFIRMED REDUNDANT OR CONFLICTING DETAILS:
- The two human figures at the left and right of the current source; the authored figure memo specifies one robot agent as the only character.
- The four oversized dashboard cards, repeated chart blocks, dense file-tree rows, and command-like micro-lines; preserve only simple task, file, check, decision, and completion cues.
- Any second robot, extra person, unrelated chart, decorative desk object, or additional workflow stage.
- Any words, letters, numbers, code, pseudo-text, title, labels, score numerals, branded UI, logo, or watermark.

Preserve the exact 2:1 canvas and the authored single-agent left-to-right sequence. A generic terminal frame is allowed, but it must not resemble a real branded product UI. Use only a few abstract symbols; do not draw fake commands or text-like rows.

Simplify the process to a small number of bold forms readable at 200px thumbnail width. Keep the robot prominent enough to read as the agent and the completion gauge secondary.

SERIES STYLE
- Minimal editorial line illustration for a Japanese technical book.
- Wide 2:1 landscape on pure white #FFFFFF.
- Use only white #FFFFFF, deep navy #123E82, near-black #1A1A1A, and pale blue #EAF1FB. Do not add gray or another hue.
- Prefer flat fills and uniform linework. No texture, grain, glow, drop shadows, glossy 3D, or decorative background.
- Keep the terminal-task chain and robot legible at 200px width.

BRAND AND TEXT
- LOGO_MODE: not_required, explicitly supported by the E-3 generation-batch row.
- Do not generate or imitate any company/product logo, mascot, official mark, brand-color substitute, or real product UI.
- Do not draw words, letters, numbers, code, pseudo-text, labels, captions, percentage signs, or watermarks.

CHARACTERS
CHARACTER_POLICY: Preserve the single existing pet robot exactly as one agent. Remove the two source human figures as explicitly listed above. Add or redesign no characters.

OUTPUT
Return one clean 2:1 PNG candidate at the highest supported native resolution. Aim for a long edge of at least 1500px; do not upscale a smaller result. Do not alter or overwrite any production file.
```

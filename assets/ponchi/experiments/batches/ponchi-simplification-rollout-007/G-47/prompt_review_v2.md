# G-47 v2 independent prompt review

- Reviewer: `/root/review_wave001_c` (independent of prompt author)
- Review date: 2026-09-28
- Verdict: **PASS** for prompt content; this is not a candidate-image approval.
- Sidecar SHA-256: `8a5d685b6797a1edeea3454a59682ab974ed098e8d0fdee887e4e8b62683c991`
- Exact v2 prompt body SHA-256 (UTF-8, LF, excluding Markdown fence): `9886d8af57fe49a5bb14dae87bfb532a52aa47838411227ff21414cc396d089e`

## Inputs and source meaning

- Logo-free source `assets/ponchi/experiments/batches/ponchi-batch-013/G-47_base_1254x627.png`: actual SHA-256 `d73caa0f0e5ee1f935697e650a4436ea33ecce405f221d206310e9a03b26146a`; matches sidecar and prompt.
- Character B reference `assets/ponchi/references/character-b-teacher-man.png`: actual SHA-256 `6ce81ea4957f8e2522292e5f48cab2ce718a5e807024f755794079c7283f9c99`; matches sidecar and prompt. The source has two repeated depictions of the same engineer; v2 keeps one.
- Human brief `content/entries/term_llm/G-47_auto_compact[済].md` describes a long conversation being compressed into a short digest so work can continue. The v2 prompt retains this sequence and one engineer without introducing a product UI or unsupported stage.
- Candidate v1 review HOLDs the image for exact-white background, pseudo-text bars, and forked continuation arrows. V2 explicitly blanks every message shape and text-like mark, makes the two follow-up messages serial within one continuation flow, and disallows branching the dominant flow.

## Acceptance review

- Meaning and order remain long conversation → one compaction transition → one compact summary → continued work, with exactly one approved Character B and no extra person/robot/product stage.
- The pseudo-text and parallel-branch findings are directly addressed. Product names, commands, labels, UI, marks, and logos are prohibited. `LOGO_MODE` is `not_required`; no clearspace is invented.
- The prompt retains the 2:1 editorial style and allowed palette, including only approved neutral clothing colors. It requires exact-white corners and all eight registered points, fail-fast checks, and a same-size mask only after the checks pass; post-generation whitening is prohibited.
- The output is reserved in the experiment folder and cannot overwrite or be promoted to production.

## Gate status

`G-47_candidate_v2.png` was absent at review time. Prompt content is **PASS**; keep generation blocked until the independent PASS is reconciled in the applicable gate/ledger. Candidate v1 remains HOLD for its image findings.

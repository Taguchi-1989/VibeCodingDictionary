# J-21 v2 independent prompt review

- Reviewer: `/root/review_wave001_c` (independent of prompt author)
- Review date: 2026-09-28
- Verdict: **PASS** for prompt content; candidate image gates remain separate.
- Sidecar SHA-256: `d062235049c641a99eef561f83355714de50d2c07a29ff9faa5003b3e946d1e8`
- Exact v2 prompt body SHA-256 (UTF-8, LF, excluding Markdown fence): `737f9aec463ffa5ac93ee820e08b48d7d93f4428beba1657a7a30e54f99d1c68`

## Inputs and source meaning

- Source `assets/ponchi/final/J-21.webp`: actual SHA-256 `839f8ad76990c5f2272d825472d747dfc387ee4863b2bf4b29ff2bf1cb711db5`; matches sidecar and prompt and remains read-only. No character reference is required or attached, consistent with the sidecar's no-people/no-robots policy.
- Human brief `content/entries/term_general/J-21_lora[済].md` contrasts whole-model Full Fine-tuning with LoRA, which freezes the base and trains only its difference/adapter. V2 keeps two equal side-by-side panels, distributes update marks only across the left full model, and gives the right panel one frozen outlined base, exactly one lock, and exactly one attached pale-blue adapter with the sole active mark.
- Candidate v1 review accepts the conceptual contrast, layout, palette, and absence of characters/branding; it flags document-front strokes as pseudo-text and exact-white failures. It also notes a generic audit default incorrectly reports clearspace required even though this item has no logo ROI. V2 removes document strokes and correctly requires no logo ROI.

## Acceptance review

- V2 preserves the full-update versus frozen-base-plus-one-adapter meaning and prohibits updating the right-hand base, extra adapter/lock, new stage, people, robots, brand marks, and pseudo-text. Blank document shapes retain their limited input-document role without text-like lines.
- The approved navy/black/pale-blue palette is retained; the frozen model is an unfilled near-black outline, avoiding an extra gray fill. No logo or logo clearspace is required.
- The prompt requires exact RGB `#FFFFFF` at all corners and all 12 registered perimeter points, a blank 3% perimeter, and fail-fast HOLD if any sample fails. It prohibits post-generation painting or recoloring.
- Output remains a single internal experiment candidate; promotion, adoption, publication, and release are prohibited.

## Gate status

`J-21_candidate_v2.png` was absent at review time. Prompt content is **PASS**; keep generation blocked until the independent PASS is reconciled in the applicable gate/ledger. Candidate v1 remains HOLD for its background finding.

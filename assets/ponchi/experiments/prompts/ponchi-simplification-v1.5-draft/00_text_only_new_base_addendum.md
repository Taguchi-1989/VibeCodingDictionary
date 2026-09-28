# Ponchi simplification prompt v1.5 draft — text-only new-base mode

Created: 2026-09-28  
Status: DRAFT / review evidence is recorded in the batch ledger; each item sidecar requires separate independent review. This file does not replace or modify v1.4, and no template review authorizes image generation or adoption.

## Why this branch exists

The v1.4 template edits only an attached, exact, logo-free source image. Several reviewed Batch 008 candidates have a logo-bearing current final, and there is no eligible logo-free source to attach. Passing that composite to image generation could reproduce the existing logo. This branch describes a new base from text and approved character sheets only. It keeps the audited current image as human-side comparison evidence, not as a generation input.

## Required sidecar fields

Keep all v1.4 fields and add:

- `GENERATION_MODE`: exactly `edit_logo_free_source` or `text_only_new_base`.
- `SOURCE_ATTACHMENT_STATUS`: `attached_hash_matched_logo_free_source` for edit mode, or `comparison_only_not_attached` for text-only mode.
- `REFERENCE_INPUTS`: exact list of image files that will actually be attached to the image-generation call, with path, SHA-256, and purpose. Use `none` when no visual reference is needed. For text-only mode, approved character sheets are the only allowed image inputs.
- `TEXT_ONLY_LAYOUT`: a complete human-confirmed description of composition, positions, groups, connections, counts, and reading order. It cannot say `source`, `same as source`, or rely on an unstated visual detail.
- `CURRENT_SOURCE_VISUAL_NOTES`: concise human audit notes for reviewers only. Exclude this field from prompt assembly and from every generator input. It must not define the new composition, layout, facts, examples, negative content, or deletions.

Every listed reference must exist and match its SHA-256. If an input is missing, has an ambiguous role, or is not approved for this purpose, stop before generation.

## Input routing rules

### `edit_logo_free_source`

- Attach only the exact source image whose path and SHA-256 are recorded and whose image has been checked to contain no official logo, generated logo-like mark, or composite overlay.
- Do not attach a logo-bearing current final, prior composite, contact sheet containing marks, or unreviewed candidate.
- Keep the v1.4 instruction to edit only that exact attached source.

### `text_only_new_base`

- `SOURCE_IMAGE_PATH` and `SOURCE_IMAGE_SHA256` are audit/comparison metadata only. Do not attach, upload, or otherwise provide the current final, its crop, a prior composite, or an image containing its logo to the generator.
- Use only the explicit text fields in the reviewed sidecar plus, when required, the approved character-sheet inputs named in `REFERENCE_INPUTS`. Do not attach a logo file, logo screenshot, current art, contact sheet, or external brand page screenshot.
- `TEXT_ONLY_LAYOUT` must fully specify all meaning-bearing placement and relationships. `LAYOUT_AND_READING_ORDER=source`, `keep the same layout`, and other visual-reference-dependent directions are invalid in this mode. Rewrite them explicitly or set `prompt_readiness=hold_layout_underspecified`.
- Do not include `SOURCE_IMAGE_PATH`, `SOURCE_IMAGE_SHA256`, or `CURRENT_SOURCE_VISUAL_NOTES` in the generator prompt. Keep these as audit metadata outside prompt assembly.
- In text-only mode, `REMOVE` may list only negative content explicitly grounded in the human brief, approved policy, or human-confirmed target specification. Do not derive a deletion, exclusion, or negative prompt from the current illustration. If a simpler target cannot be described from those text authorities alone, hold the item until its target is stated in text.
- `REMOVE` does not authorize deleting a fact or relationship required by `MUST_KEEP` or the human brief.
- Preserve only the human-confirmed facts and forms in the sidecar. Do not infer extra examples, stages, values, people, brands, UI, or relationships from the current image.
- Use the v1.4 text description of series style. Do not supply an existing Ponchi image as a style reference. The series-style result remains unverified until separate 200px, palette, background, geometry, and visual review.
- If a fixed character is required, attach only its approved character reference, confirm its identity/role/count in `CHARACTER_POLICY`, and exclude every other current illustration. If no character is explicitly required, attach no character sheet and add no character.

The sidecar author must inspect the actual tool input list before generation and record it. Prompt wording cannot make an unsafe attachment safe; any current logo-bearing composite in the tool input list blocks the call.

## Brand and overlay constraints

- Never generate, imitate, stylize, or approximate an official logo, product mark, branded icon, or product UI. The text-only mode does not change this rule.
- For `internal_base_only`, the exact official asset must already be acquired and its path, hash, source, retrieval date, and use-condition status must be recorded. Reserve the reviewed `LOGO_CLEARSPACE_RECT` as uniformly pure white, but do not attach, draw, or composite the mark. Use conditions remain unresolved; the output is an internal base only.
- For `reserve_official_asset`, use the same blank-area rule. Deterministic overlay is a later, separate operation after the base passes review and the official asset's use conditions are verified.
- If the brand matrix does not explicitly support `not_required`, do not omit the brand gate. If an official asset is missing or the required logo treatment is unclear, hold the item.
- Never use an image-generation input or output to decide whether the logo's use is permitted.

## Text-only prompt block

For `GENERATION_MODE=text_only_new_base`, replace the opening lines of the v1.4 image-edit block with the following. Keep the rest of the reviewed v1.4 instructions unless this addendum explicitly changes them.

```text
Generate one new, logo-free 2:1 Japanese technical-book illustration from this text specification only.
GENERATION_MODE: text_only_new_base
ENTRY_ID: {ENTRY_ID}
ENTRY_TITLE: {ENTRY_TITLE} (context only; do not draw these words)
TEXT_ONLY_LAYOUT: {TEXT_ONLY_LAYOUT}
REFERENCE_INPUTS: {REFERENCE_INPUTS} (the only permitted image inputs are the approved character references listed here)

The SOURCE_IMAGE_PATH, SOURCE_IMAGE_SHA256, and CURRENT_SOURCE_VISUAL_NOTES fields are audit-only metadata: exclude them from this generator prompt and from the actual generation request. Do not request, use, inspect, recreate, or derive visual details or negative-content instructions from the current source image. It is not attached and must not be supplied to this generation call. Do not use any logo-bearing composite, logo file, contact sheet, or prior Ponchi illustration as a reference. Build the composition and negative-content checklist only from the human-confirmed TEXT_ONLY_LAYOUT, meaning fields, human brief, approved policy, and other explicitly named text authorities. If those text authorities do not fully define a required relation or layout, stop instead of guessing.
```

The remainder of the prompt must include the same `INTENDED_MEANING`, `MUST_KEEP`, `TEXT_FREE_TRANSLATION`, verified external fact anchors, `REMOVE`, series-style, brand/text, character, background, and output blocks required by v1.4. In text-only mode, update every sentence that says “source image”, “attached source”, or “preserve the source” so it refers to the explicitly written sidecar fields instead. Do not leave contradictory edit-only instructions in the final prompt body.

## Review and release gates

1. Independently review this addendum against v1.4, the Ponchi style/palette policy, and logo-input constraints. Record this file's SHA-256 in the review.
2. For each item, verify source/brief/brand hashes and confirm `TEXT_ONLY_LAYOUT`, text-free meaning, and `REFERENCE_INPUTS` are complete.
3. Independently review the full item prompt and its exact prompt-body SHA-256. A common-template review does not approve individual sidecars.
4. Before any call, verify that the actual image-input attachments exactly match `REFERENCE_INPUTS`; a human-readable path in a prompt is not an attachment.
5. If both template and item prompt pass, generate one internal candidate only. Run the existing fail-fast, full background-mask, palette, ROI, geometry, 200px meaning, and series-style reviews. Keep `assets/ponchi/final/` untouched and wait for separate human selection/adoption gates.

No prompt or template review is image-generation or adoption authorization.

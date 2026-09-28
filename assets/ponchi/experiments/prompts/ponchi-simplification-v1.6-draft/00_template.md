# Ponchi simplification prompt v1.6 — shared template draft

Created: 2026-09-28  
Status: **DRAFT / common template review PASS recorded in rollout plan; item-specific prompt, generation, overlay, adoption, and publication are not authorized by this template**  
Scope: experiment-only shared prompt template. This draft does not modify or replace v1.3, v1.4, or v1.5. A template review, sidecar review, or ledger status does not authorize generation, selection, adoption, overlay, or publication.

## 1. Purpose and separation of concerns

Use this template to simplify a Ponchi illustration while preserving the human-confirmed meaning and composition. Keep three layers separate:

1. **Generator text:** short, item-specific visual directions and the shared style/safety rules below.
2. **Sidecar and ledger:** source facts, approvals, paths, hashes, manifests, coordinates, operational measurements, and status fields. Do not append this operational record to the generator prompt.
3. **Machine and independent-review gates:** validate exact inputs and outputs, prompt provenance, brand constraints, and legibility outside the image-generation call.

Do not assemble a prompt or call a generator while any required item field, input, approval, or review is missing or inconsistent.

## 2. Required sidecar and ledger fields

Store these fields in the item sidecar/ledger. They are records for authors and reviewers; include only fields explicitly marked as generator text in the assembled prompt.

### Item intent and composition

- `ENTRY_ID`, `ENTRY_TITLE` (title is context only; never render it as image text).
- `HUMAN_BRIEF_SOURCE`, `HUMAN_BRIEF_SHA256`, and the human-confirmed target specification or approval reference.
- `INTENDED_MEANING`: one concise, human-confirmed statement of the concept.
- `LAYOUT` or `TEXT_ONLY_LAYOUT`: a complete drawn composition: canvas orientation, all meaning-bearing elements and their counts, positions/groups, connections and directions, and reading order. `TEXT_ONLY_LAYOUT` must stand alone without a visual source or unstated visual detail.
- `MUST_KEEP`: the essential semantic elements, roles, counts, and relationships that must survive simplification. Do not use it as a list of optional decoration.
- `REMOVE`: only specific deletions explicitly approved by a human and supported by the human brief or target specification. Never infer deletions from an image.
- `TEXT_FREE_TRANSLATION`: the human-confirmed shapes, placement, and relationships that convey the meaning without readable words or numerals. If a required meaning cannot be represented unambiguously, set readiness to HOLD.
- `FACTS_RETAINED_OUTSIDE_IMAGE`: verified article/entry locations retaining important terms, numbers, and names omitted from the drawing.
- `CHARACTER_POLICY`: approved character identity, role, and count, or explicitly `none`.

### Mode, source, and actual image inputs

- `GENERATION_MODE`: exactly `edit_logo_free_source` or `text_only_new_base`.
- `SOURCE_IMAGE_PATH`, `SOURCE_IMAGE_SHA256`, and `SOURCE_IMAGE_VERSION`: audit/comparison metadata. For text-only mode, the source is never an input.
- `SOURCE_ATTACHMENT_STATUS`: `attached_hash_matched_logo_free_source` in edit mode; `comparison_only_not_attached` in text-only mode.
- `REFERENCE_INPUTS`: the complete manifest of actual image attachments, each with exact path, SHA-256, purpose, and approved status. Use `none` if no image is needed. The manifest must match the attachments sent to the generator exactly.
- `CURRENT_SOURCE_VISUAL_NOTES`: human-review notes only. Never include them in prompt assembly or generator inputs.
- `OUTPUT_PATH`, `MODEL`, generation timestamp, actual output dimensions, output SHA-256, and actual-dimension 3% edge-inset measurement result/violating-pixel count, recorded only if generation is separately authorized.

### Brand, policy, and audit records

- `BRAND_AUDIT_RECORD`: exact brand-policy source and item-specific ledger row.
- `LOGO_MODE`: `reserve_official_asset`, `internal_base_only`, or evidence-backed `not_required`.
- For a required official asset: `OFFICIAL_ASSET_PATH`, SHA-256, source URL, retrieval date, and use-condition status. Missing source, asset, or unresolved eligibility blocks the item.
- `LOGO_CLEARSPACE_RECT` and any output-coordinate/ROI mapping: sidecar/ledger audit data only; keep coordinates and pixel-level instructions out of generator text. Describe any required blank area in the human-confirmed layout in ordinary visual terms.
- `BACKGROUND_SAMPLE_POINTS`, background-mask path/SHA/dimensions, exact-white precheck results, ROI measurements, palette/geometry audit paths, candidate paths/SHAs, and all audit statuses: sidecar/ledger only.
- `TEMPLATE_VERSION`, exact template SHA-256, assembled prompt SHA-256, prompt readiness, human decision, generation authorization, and adoption authorization.

## 3. Mode-specific generator opening

Use exactly one opening. Fill it only from approved, human-confirmed sidecar fields.

### `edit_logo_free_source`

```text
Edit only the exact attached image designated as the hash-matched, logo-free edit source. Do not use any other artwork as a visual reference.
ENTRY_ID: {ENTRY_ID}
ENTRY_TITLE: {ENTRY_TITLE} (context only; do not draw these words)
LAYOUT: {LAYOUT}
```

The edit source must be a separately approved, exact logo-free base. Do not attach a current final, logo-bearing composite, logo screenshot, contact sheet, or prior Ponchi illustration. Add only approved character-sheet references listed in `REFERENCE_INPUTS` when `CHARACTER_POLICY` requires them.

### `text_only_new_base`

```text
Create one new illustration from this complete text specification only. No source artwork is attached or available as a visual reference.
ENTRY_ID: {ENTRY_ID}
ENTRY_TITLE: {ENTRY_TITLE} (context only; do not draw these words)
TEXT_ONLY_LAYOUT: {TEXT_ONLY_LAYOUT}
```

The text layout must fully specify the intended drawing, including counts, positions, groups, connections, and reading order. Do not attach a current final, logo-bearing composite, logo screenshot, contact sheet, or prior Ponchi illustration. Only the approved character-sheet references listed in `REFERENCE_INPUTS` may be attached. Never infer content, layout, meaning, or deletions from `SOURCE_IMAGE_PATH`, `SOURCE_IMAGE_SHA256`, or `CURRENT_SOURCE_VISUAL_NOTES`; those fields remain outside the prompt and call.

## 4. Shared generator instructions

Append this compact shared block after the selected opening and item-specific fields:

```text
HUMAN-CONFIRMED MEANING:
{INTENDED_MEANING}

ESSENTIAL CONTENT TO PRESERVE:
{MUST_KEEP}

TEXT-FREE VISUAL EXPRESSION:
{TEXT_FREE_TRANSLATION}

APPROVED DELETIONS ONLY:
{REMOVE}

Draw the complete composition specified in LAYOUT or TEXT_ONLY_LAYOUT. Preserve every essential element, count, role, group, connection, direction, and reading order stated there and in MUST_KEEP. Remove only the human-approved items in REMOVE. Do not invent facts, examples, labels, relationships, or extra content. If the specification is incomplete or contradictory, stop instead of guessing.

At 200px thumbnail width, every essential role and relationship must remain identifiable. If they cannot be distinguished at that size, treat the result as unsuccessful and stop for review; do not compensate by shrinking details, dropping required meaning, or rearranging the composition. There is no fixed maximum number of forms: use the number the confirmed meaning requires.

Keep all illustration ink at least 3% of the canvas width from both vertical edges and at least 3% of the canvas height from both horizontal edges.

SERIES STYLE
- Minimal editorial line illustration for a Japanese technical book; wide 2:1 landscape.
- Opaque, flat, pure white #FFFFFF canvas with no gradient, texture, lighting, vignette, grain, noise, transparency, or background shadow.
- Use only author-approved illustration colors: deep navy #123E82, near-black #1A1A1A, and pale blue #EAF1FB. Preserve gray only within an approved fixed character reference. Do not introduce other colors.
- Use clean, consistent linework and simple flat forms. Keep separate any groups whose separation carries meaning.

BRAND AND TEXT
- Never draw, imitate, stylize, or approximate an official logo, product mark, branded icon, a third-party brand's official character or mascot, or a real/branded interface. Do not draw words, letters, numbers, fake text, labels, captions, or watermarks.
- Leave any human-confirmed official-asset clear area empty, plain white, and free of all illustration content. Do not draw a placeholder or logo. No official asset is attached to or composited into this illustration.
- Respect the approved brand mode and policy. `internal_base_only` is an internal base only. `not_required` is valid only when the brand record explicitly supports it.

CHARACTERS
- Approved Ponchi series characters are allowed only when the exact `CHARACTER_POLICY` specifies their identity, role, and count and the matching approved character reference is listed as an actual input. Preserve that approved identity and design; do not substitute another character or add decorative characters. Third-party brands' official characters and mascots remain prohibited.

OUTPUT
- Return one clean 2:1 PNG at the highest supported native resolution, targeting a native long edge of at least 1500px. Report actual dimensions; if the tool misses that target, state the actual dimensions and do not upscale or claim a higher native resolution.
- This is an internal experiment candidate only. Do not overlay a logo, modify or overwrite a production asset, move it into `assets/ponchi/final`, adopt it, or publish it.
```

Do not put file paths, hashes, attachment manifests, mask/ROI coordinates, pixel-sampling rules, audit commands, or machine-review instructions in the generator prompt. The actual attachment list must be inspected and recorded separately; prose in the prompt does not establish what was attached.

## 5. Input and policy gates

1. **Mode and source gate:** select one mode. For edit mode, verify the exact separately approved logo-free source by path and SHA-256. For text-only mode, keep every current-final image and visual note out of the generator call. A current final, logo composite, logo screenshot, contact sheet, or prior Ponchi artwork is never an allowed reference input.
2. **Manifest gate:** confirm each actual attachment matches `REFERENCE_INPUTS` by path, SHA-256, purpose, and approval. Any unlisted, missing, changed, ambiguous, or disallowed input means HOLD.
3. **Meaning gate:** confirm the complete layout, `MUST_KEEP`, approved `REMOVE`, text-free expression, facts retained in the article, and human brief agree. Do not deduce a deletion or target from current art. Any unresolved meaning, relationship, count, layout, or text dependency means HOLD.
4. **Character gate:** confirm each attached character sheet is on the allowlist, is necessary under `CHARACTER_POLICY`, and matches the approved identity, role, and count. No other illustration is a character/style reference.
5. **Brand gate:** verify the brand audit, required official asset provenance, use conditions, approved `LOGO_MODE`, and blank clear-area placement. Never generate a mark. Missing or unclear policy/asset evidence means HOLD. Image-generation output cannot establish whether an official asset may be used.
6. **Prompt review gate:** an independent reviewer must check the complete item sidecar, exact assembled prompt, mode-specific input opening, and actual attachment manifest against their exact SHA-256 values before any generation. Common-template review does not approve an item prompt.
7. **Generation gate:** this draft grants no generation authorization. A separate explicit item-level decision and all required approvals must be recorded before a call. If authorized later, produce one internal candidate only.
8. **Candidate gate:** after any separately authorized generation, independently bind every audit to the exact candidate SHA-256. Check format, 2:1 dimensions, opacity, exact-white background and full background mask, palette, geometry, applicable blank-area ROI, and 200px meaning/series-style readability. For actual dimensions `W×H`, calculate the inset as `mx=int(0.03*W+0.5)` and `my=int(0.03*H+0.5)` (round fractional pixels to nearest integer, with halves rounded up). Measure the actual-dimension pixel bounds against this 3%-inset boundary on all four edges; any ink outside the inset is HOLD. Any missing, failed, or mismatched check is HOLD. Keep the production final untouched.
9. **Adoption gate:** generation is not adoption. Require a separate human selection/adoption decision and all production/brand gates before any overlay, production placement, or publication. This draft authorizes none of those actions.

## 6. Review record

Before this template can be used, an independent reviewer must review this exact file SHA against the existing style/palette policy, brand requirements, source-input restrictions, and prompt workflow. Record the review result and SHA in the ledger. Then review every item-specific sidecar and assembled prompt independently. Until both applicable reviews pass and all separate authorization gates are met, status remains **DRAFT / not reviewed / not generation-authorized**.

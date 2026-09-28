# Prompt revision set: ponchi-simplification-v1.1

- `00_template.md` adds a human-confirmed layout and reading-order field after the A-6 experiment exposed a layout deviation.
- Independent prompt review: PASS. The layout/reading-order field and hold-on-unresolved-conflict rule close the A-6 gap without material regressions to brand, palette, character, or logo constraints. This revision has not yet been applied to an image and creates no candidate.
- Existing pilot prompt files remain unchanged as generation records.
- Create per-entry prompt copies only after current-image triage confirms the exact source path/hash and fills meaning, keep/remove, brand, and character fields.
- The A-6 candidate v2 remains tied to template v1. Its semantic and style reviews passed, but human decision is pending because the candidate's left-to-right layout differs from the authored memo's top-calendar/vertical-flags layout.
- For every entry prompt, derive the layout field from the complete human-authored brief; use `source` only when the brief specifies no layout.

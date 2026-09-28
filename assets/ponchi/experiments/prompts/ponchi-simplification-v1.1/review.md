# ponchi-simplification-v1.1 independent prompt review

- Verdict: PASS.
- `LAYOUT_AND_READING_ORDER` is an explicit human-confirmed field. It defaults to `source` only when the authored brief specifies no layout.
- When the source and authored brief differ, the prompt requires explicit precedence and holds generation while precedence is unresolved.
- The image-edit instructions operationalize the rule by preserving specified positions and forbidding conversion between row and stack layouts.
- No material regressions were found in brand provenance/state, palette, fixed-character and neutral-gray handling, robot glow, logo geometry, or text/asset restrictions.
- Review note: populate the field from the complete human-authored layout brief for every entry; `source` intentionally freezes the current arrangement.

# G-19 candidate v3 — preserve reference length and add 25% extension

Status: v2 still measured about 1.10× for the initial write bar. This revision anchors the edit to the unchanged 153px normal-bar reference.

## Input and scope

- Edit target: `G-19_candidate_v2.png`
- Edit target SHA-256: `aea8aad25777a422ac22409d31cac5c4920dd6870eac943c70e5fc4cba19452c`
- Keep the candidate v2 canvas, layout, rows, person, console, and other visual details.
- Preserve v1 and v2 unchanged. Save the result as `G-19_candidate_v3.png`.
- Edit only the first cached write mark and the nine short cached-hit marks.

## Targeted edit prompt

```text
Edit only the billing marks in the attached G-19 candidate v2. Preserve its exact 1774x887 2:1 canvas, two panels, all ten aligned rows per panel, illustration, engineer, palette, and layout.

Use the existing left-panel full-cost bars as the fixed reference. Each is about 153 pixels long in this 1774px-wide image. Do not shorten, resize, or recolor those ten reference bars.

In the cached panel, change only these marks:

- First row: keep a solid deep-navy core about 153px long, equal to one unchanged left-panel reference bar. Append a separate pale-blue outlined segment about 38px long (one quarter of the reference-bar length). Do not shorten the navy core to make room for this segment. The complete first-row mark from its left edge to its right edge must be about 191px long: 153px + 38px = 1.25 times the normal 153px reference. The extra 38px must be visibly outside the end of the full normal-length core.
- Rows two through ten: each deep-navy hit mark should be about 15px long, approximately one-tenth of the same 153px reference. Keep all nine hit marks identical and aligned to their rows.

Keep all ten rows in each panel. Do not alter the document, cache cylinder, arrows, request symbols, shelf, panel boundaries, engineer or console. Do not add labels, numbers, icons, panels, people, robots, logos, text, or any other visual element. Keep the existing white, deep navy, near-black, and pale-blue palette only. Preserve the no-total-savings meaning and do not imply requests disappear. Return one clean PNG at exactly 2:1; do not alter production files.
```

## Review focus

- Measure the first cached mark against an unchanged left full-cost bar; target total ratio is 1.25×.
- Measure all nine cache-hit marks; target ratio is about 0.1×.
- Confirm no collateral layout, character, brand, palette, or meaning changes.

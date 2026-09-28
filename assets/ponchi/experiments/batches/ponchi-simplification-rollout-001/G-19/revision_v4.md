# G-19 candidate v4 — correct measured bar endpoints

Status: v3 remained short of the ratio target. Independent audits measured a 153px normal bar, a 132px navy core plus a 50px extension (182px total), and 19px hit marks.

## Input and scope

- Edit target: `G-19_candidate_v3.png`
- Edit target SHA-256: `e9424237eadcc25f9f987ae077ab42ecb6a516d62cd1120e5844d54e112d26d5`
- Preserve v1, v2, and v3 unchanged. Save the result as `G-19_candidate_v4.png`.
- Change only the first cached write bar and the nine cached-hit marks.

## Targeted edit prompt

```text
Make one precise correction to the billing marks in the attached G-19 candidate v3. Keep the exact 1774x887 2:1 canvas and preserve every panel, row, arrow, document, cache cylinder, engineer, console, shelf, color, and position.

The measured reference values in the current image are: an unchanged left full-cost bar is 153px long; the first cached write mark is currently 132px of navy plus 50px of outlined pale blue, 182px total; each hit mark is currently 19px. Change only those cached marks to these targets:

- First cached write mark: 153px of solid deep navy (exactly matching the unchanged left normal-bar length), followed by a 38px outlined pale-blue extension at its right end. Total span about 191px, exactly 1.25 times the normal 153px reference. Keep the navy core at 153px; do not shorten it. Shorten the current 50px extension to 38px while extending the navy core from 132px to 153px.
- Each of the next nine cached-hit marks: shorten from 19px to about 15px, one-tenth of the 153px reference. Keep all nine identical and aligned.

Do not alter the left-panel reference bars or change any other mark. Do not add or remove elements. No text, numbers, labels, logos, extra hues, people, robots, or new panels. Preserve the exact original meaning: ten requests on both sides, one first write at 1.25x, and nine later per-request hits at 0.1x; this does not assert that requests disappear or that the group total is one-tenth. Return one clean 2:1 PNG and do not touch production images.
```

## Review focus

- Independently measure 153px normal vs about 191px write total and about 15px per hit.
- Confirm no collateral changes to meaning, layout, people, palette, or brand policy.

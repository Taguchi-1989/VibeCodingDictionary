# G-19 candidate v2 — targeted visual revision

Status: one focused image edit requested after independent v1 semantic and visual review.

## Input and scope

- Edit target: `G-19_candidate_v1.png`
- Edit target SHA-256: `70fe0d0685802350e3209a6981a9ef0cabf759f979d58c4d9d71a68e18c5951d`
- Source meaning, human-confirmed layout, brand policy, palette, and all other constraints: `prompt_v1_1.md`
- Preserve v1 unchanged. Save the result as `G-19_candidate_v2.png`.
- Change only the first billing mark in the cached panel and the relative prominence of the existing engineer/console.

## Targeted edit prompt

```text
Edit the attached G-19 candidate v1. Keep the exact wide 2:1 canvas, two side-by-side groups, all ten aligned rows in each group, document, arrows, cache cylinder, shelf line, palette, and left-to-right meaning.

Change only these two things:

1. Make the first billing bar in the cached group a visibly accurate 1.25× of a normal full-cost bar. A normal bar is the 1.0× reference. The whole first bar must measure exactly 1.25 times that reference, and each of the next nine hit bars must remain 0.1 times that reference. Make the added 0.25 segment clearly visible at a 200px-wide thumbnail: use a normal-length deep-navy core plus a distinct pale-blue outlined end segment exactly one quarter of the core's length. The combined core plus end segment is the 1.25× write cost; do not enlarge it beyond that. Keep all ten row marks aligned and individually readable. Preserve ten full-length marks in the uncached group.

2. Reduce the one existing engineer and the generic console together to roughly 60% of their current displayed size, keeping them at the far left and secondary to the comparison. Preserve the engineer's same identity, pose, and single-person count; do not redesign or duplicate the person.

Do not change any other element. No new panels, symbols, icons, text, labels, numbers, currency, prices, logos, product names, UI, people, robots, shadows, texture, gradients, glow, or extra hues. Keep the permitted white, deep navy, near-black, and pale blue palette only. Do not imply that caching removes requests or makes the ten-request total one-tenth. Do not modify or overwrite any production image. Return one clean PNG at the same 2:1 aspect ratio.
```

## Review focus

- Confirm at 200px that the initial write bar is visibly and accurately 1.25× a full-cost bar; hits remain 0.1×.
- Confirm the person remains one engineer at a console but is secondary to the comparison.
- Confirm no unintended semantic, brand, palette, layout, or rendering changes.

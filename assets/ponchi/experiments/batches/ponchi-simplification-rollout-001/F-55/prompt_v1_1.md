# F-55 merge — v1.1 prompt draft

Status: prompt review passed; candidate v1 generated; independent candidate image review pending.

## Source and human-confirmed fields

- Entry: F-55 — merge
- Human brief: content/entries/term_tool/F-55_merge[済].md
- Source image: assets/ponchi/final/F-55.webp
- Source SHA-256: 13e29d62d708a17e9b0b99409d0e29b1691b47b62c3066614f84e126f0a45d5e
- Source version: current final, inventoried 2026-09-27; 1254x627 (2:1); SHA matches rollout queue.
- Intended meaning: git merge joins independently advancing main and feature branches, records a merge commit, and preserves their history in one shared line.
- Layout and reading order: Two separate side-by-side states, read left to right. Before: main and feature have diverged and each has commits. After: the same histories converge at one merge commit on main, then continue as one shared history. The human-authored main-figure memo is authoritative over the source image's duplicate miniature workflows.
- Brand record: docs/brand_usage_audit.md has no F-55 brand asset; ledgers/ponchi_generation_batches.csv row F-55 says logo_avoid and not_needed. Generic, unbranded diagram.
- Logo mode: not_required.
- Character policy: Show the same existing male series character once in each state: unhappy in Before and relieved in After. These are two depictions of one person, not two identities; add no third character or robot.

## Instantiated image-edit prompt

Use the attached F-55 image as the exact edit target, not as a loose reference. Keep its 2:1 canvas.

ENTRY_ID: F-55
ENTRY_TITLE: merge (context only; do not draw these words)
SOURCE_IMAGE_PATH: assets/ponchi/final/F-55.webp
SOURCE_IMAGE_SHA256: 13e29d62d708a17e9b0b99409d0e29b1691b47b62c3066614f84e126f0a45d5e
SOURCE_IMAGE_VERSION: current final, inventoried 2026-09-27

INTENDED MEANING (human-confirmed):
git merge joins two diverged branches, records a merge commit, and preserves their history as one shared line.

LAYOUT AND READING ORDER (human-confirmed):
Use two separate side-by-side states, read left to right. Before: main and feature are separate branches with commits on each. After: the two histories converge once at a merge commit on main, followed by one shared continuation. This human-authored main-figure memo takes precedence over duplicate workflow strips in the source.

MUST KEEP:
- Distinguishable main and feature branches before the merge, with commits on both.
- One merge point that records the two histories joining; a single shared history after it.
- The side-by-side before/after comparison and its left-to-right order.
- The same existing male series character depicted once in each panel: unhappy in Before and relieved in After. Preserve one identity and design; add no distinct or third character.

REMOVE ONLY THESE REDUNDANT SOURCE DETAILS:
- The separate bottom five-step process strip; it repeats the same branch-to-merge sequence and is not part of the authored main figure.
- The additional miniature branch diagrams inside the left card and laptop; retain the main comparison as the sole branch-history illustration.
- The separate right-side pseudo-history/list panel; the after state already shows the unified history.
- Tiny pseudo-text, repeated list rows, decorative desk objects, and nonessential dotted connectors.

Edit only this image. Do not invent a conflict, pull request, rebase, extra branch, or additional merge. Do not draw readable code, words, labels, letters, numbers, logos, product UI, or watermarks.

SERIES STYLE
- Minimal editorial line illustration for a Japanese technical book; wide 2:1 on pure white #FFFFFF.
- For diagrams and backgrounds use only deep navy #123E82, near-black #1A1A1A, pale blue #EAF1FB, and white #FFFFFF.
- Keep only neutral-gray character areas already present in the source. Do not add other colors, textures, grain, speckles, shadows, glow, or decorative background.
- Use clean, uniform linework and make the two histories and merge point clear at 200px thumbnail width.

BRAND AND TEXT
LOGO_MODE: not_required. No logo clearspace is needed.
Do not create or imitate any company/service logo, icon, mark, mascot, branded interface, or brand-color treatment. Draw no words, letters, numbers, pseudo-text, labels, captions, or watermark.

CHARACTERS
Show the same existing male series character once in the Before panel with an unhappy expression and once in the After panel with a relieved expression. These are two depictions of one person in two states. Preserve his established identity, role, and design; add no other or third person, robot, or replacement design.

OUTPUT
Return one clean 2:1 PNG candidate at the highest supported native resolution, aiming for a long edge of at least 1500px. Report actual dimensions. Do not upscale a smaller result or overwrite any production file.

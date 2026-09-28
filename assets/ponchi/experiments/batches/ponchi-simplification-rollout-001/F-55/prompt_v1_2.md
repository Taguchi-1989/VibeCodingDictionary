# F-55 merge — targeted v1.2 image-edit prompt

Status: candidate v1 semantic review passed; style review held only for gray chair-back props. This prompt targets a v2 edit of candidate v1; no v2 image has been generated.

## Source and human-confirmed fields

- Entry: F-55 — merge
- Human brief: content/entries/term_tool/F-55_merge[済].md
- Original source: assets/ponchi/final/F-55.webp
- Original source SHA-256: 13e29d62d708a17e9b0b99409d0e29b1691b47b62c3066614f84e126f0a45d5e
- Candidate v1 edit target: assets/ponchi/experiments/batches/ponchi-simplification-rollout-001/F-55/F-55_candidate_v1.png
- Candidate v1 SHA-256: b1077aa96e8cd964d661b33c8345691dc4ffa22d51fb7f075accc2762237ebd1
- Candidate v1 dimensions: 1774x887 (2:1)
- Intended meaning: git merge joins two diverged branches, records a merge commit, and preserves their history as one shared line.
- Layout and reading order: Two side-by-side states, left to right. Before shows main and feature diverged, each with commits. After shows those histories converging at one merge commit on main, followed by a shared history.
- Brand record: docs/brand_usage_audit.md has no F-55 brand asset; ledgers/ponchi_generation_batches.csv row F-55 says logo_avoid and not_needed. Generic, unbranded diagram.
- Logo mode: not_required.
- Character policy: Show the same existing male series character once in each state: unhappy in Before and relieved in After. These are two depictions of one person, not separate identities. Do not add a third character or robot.

## Instantiated image-edit prompt

Use the attached candidate v1 image as the exact edit target. Do not use the original final image as the edit target or as a loose reference. Keep the exact 2:1 canvas.

ENTRY_ID: F-55
ENTRY_TITLE: merge (context only; do not draw these words)
EDIT_TARGET_PATH: assets/ponchi/experiments/batches/ponchi-simplification-rollout-001/F-55/F-55_candidate_v1.png
EDIT_TARGET_SHA256: b1077aa96e8cd964d661b33c8345691dc4ffa22d51fb7f075accc2762237ebd1
EDIT_TARGET_VERSION: candidate v1, 1774x887

INTENDED MEANING (human-confirmed):
git merge joins two diverged branches, records a merge commit, and preserves their history as one shared line.

LAYOUT AND READING ORDER (human-confirmed):
Keep the side-by-side before/after composition unchanged. Before: main and feature are distinct commit-bearing branches. After: they converge once at one merge commit on main and continue as one shared history.

MUST KEEP:
- Both branch histories, the single merge point, and the shared history after it.
- The same male series character depicted once in each state, unhappy in Before and relieved in After. Preserve one identity and design; do not add a third character.

TARGETED REVISION ONLY:
- Remove both separate gray chair-back props visible behind the character depictions. Keep each person’s outline, body, clothing, face, hands, pose, and expression intact; fill the removed chair areas with the existing white background.
- If removing a chair would damage a person’s silhouette, recolor only the affected chair shape to pale blue #EAF1FB or deep navy #123E82. Do not leave any gray chair area.
- Preserve all other candidate v1 content, positions, linework, and proportions exactly. Do not add or remove any other element.

SERIES STYLE
- Preserve the existing clean line illustration and exact 2:1 composition.
- Palette: white #FFFFFF, deep navy #123E82, near-black #1A1A1A, pale blue #EAF1FB. Neutral-gray areas already in character clothing/body may remain; no gray props.
- Do not add other colors, textures, grain, shadows, glow, or decorative background.

BRAND AND TEXT
LOGO_MODE: not_required. No logo clearspace is needed.
Do not create or imitate any company/service logo, icon, mark, mascot, branded interface, or brand-color treatment. Add no readable text, pseudo-text, labels, letters, numbers, or watermark.

CHARACTERS
Keep the same existing male character once in each state, unhappy in Before and relieved in After. These are two depictions of one person. Preserve his established identity, role, and design; add no other or third person or robot.

OUTPUT
Return one clean 2:1 PNG candidate for review. Preserve the candidate v1 canvas dimensions if supported. Do not upscale a smaller result or overwrite candidate v1, the original source, or any production file.

# F-160 DOM — v1.1 prompt draft

Status: prompt review passed; candidate v1 generated; independent candidate image review pending.

## Source and human-confirmed fields

- Entry: F-160 — DOM
- Human brief: content/entries/term_tool/F-160_dom[済].md
- Source image: assets/ponchi/final/F-160.webp
- Source SHA-256: 962808a91ef2e0152731316ee63521261b0c869265d0ff4a812aad9ae52d2fa4
- Source version: current final, inventoried 2026-09-27; 1254x627 (2:1); SHA matches rollout queue.
- Intended meaning: The browser parses HTML text into an in-memory DOM tree; JavaScript can change a node, and the visible page updates.
- Layout and reading order: One left-to-right flow: HTML source document → browser parsing → central DOM tree → one JavaScript node operation → updated page. This follows the human-authored main-figure memo and takes precedence over the source image's extra page thumbnails and detached mini-tree.
- Brand record: docs/brand_usage_audit.md has no F-160 brand asset; ledgers/ponchi_generation_batches.csv row F-160 says logo_avoid and not_needed. Generic, unbranded diagram.
- Logo mode: not_required.
- Character policy: Preserve the one existing male series character and established design from the source. Add no other person or robot.

## Instantiated image-edit prompt

Use the attached F-160 image as the exact edit target, not as a loose reference. Keep its 2:1 canvas.

ENTRY_ID: F-160
ENTRY_TITLE: DOM (context only; do not draw these words)
SOURCE_IMAGE_PATH: assets/ponchi/final/F-160.webp
SOURCE_IMAGE_SHA256: 962808a91ef2e0152731316ee63521261b0c869265d0ff4a812aad9ae52d2fa4
SOURCE_IMAGE_VERSION: current final, inventoried 2026-09-27

INTENDED MEANING (human-confirmed):
The browser parses HTML into a DOM tree in memory; JavaScript can operate on that tree and the visible page changes.

LAYOUT AND READING ORDER (human-confirmed):
A single left-to-right sequence: one abstract HTML source document, browser parsing, one central tree rooted at html with head/body and descendant nodes, one JavaScript action on a node, and one updated page view. Preserve this authored order if the source's existing panel arrangement differs.

MUST KEEP:
- The distinction between HTML source text and the DOM tree created from it.
- A browser parsing step between the source document and tree.
- One readable-at-thumbnail tree hierarchy with html as root and head/body beneath it.
- One JavaScript operation that changes one selected node, followed by a visibly updated page.
- The one existing male series character, with the same identity and design.

REMOVE ONLY THESE REDUNDANT SOURCE DETAILS:
- The detached miniature DOM tree at far left; keep one central tree.
- Repeated page thumbnails and duplicate content-card grids inside the browser frame; retain one simple page silhouette as the result.
- Repeated tiny menu, list, and control marks in the browser and API panels; retain one abstract JavaScript operation cue.
- Grain/dotted fill textures and connector branches that do not represent the single left-to-right sequence.

Edit only this image. Do not add CSS, framework, browser-brand, or HTML-tag examples beyond the stated tree structure. Do not imply HTML and DOM are identical. Do not draw readable code, words, labels, letters, numbers, logos, product UI, or watermarks.

SERIES STYLE
- Minimal editorial line illustration for a Japanese technical book; wide 2:1 on pure white #FFFFFF.
- For diagrams and backgrounds use only deep navy #123E82, near-black #1A1A1A, pale blue #EAF1FB, and white #FFFFFF.
- Keep only neutral-gray character areas already present in the source. Do not add other colors, textures, grain, speckles, shadows, glow, or decorative background.
- Use clean, uniform linework; the source/tree/action/result must remain distinct and understandable at 200px thumbnail width.

BRAND AND TEXT
LOGO_MODE: not_required. No logo clearspace is needed.
Do not create or imitate any company/service logo, browser icon, framework mark, mascot, branded interface, or brand-color treatment. Draw no words, letters, numbers, pseudo-text, labels, captions, or watermark.

CHARACTERS
Keep the existing male series character's identity, role, count, and design. Add no person, robot, or replacement design.

OUTPUT
Return one clean 2:1 PNG candidate at the highest supported native resolution, aiming for a long edge of at least 1500px. Report actual dimensions. Do not upscale a smaller result or overwrite any production file.

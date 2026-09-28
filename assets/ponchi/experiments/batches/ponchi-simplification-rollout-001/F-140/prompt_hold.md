# F-140 Mermaid — prompt held

No v1.1 prompt or metadata created; no image candidate generated.

## Evidence

- Queue current final: assets/ponchi/final/F-140.webp
- Current final SHA-256: a23f7c89e2629a823cbdfca6d5a979071053a3fb4545bb4d260ea387252be9b1 (verified match); 1254x627, reviewed at 200px.
- Logo-free base from the generation batch: assets/ponchi/experiments/batches/ponchi-batch-011/F-140_base_1254x627.png
- Base SHA-256: a4df09b51cc41917663696571227deb8fa78718d4fc69b979997ffbd969cae3c (verified); 1254x627. The current final includes a separate official Mermaid overlay; it must not be passed to image-edit.
- Human brief: content/entries/term_tool/F-140_mermaid[人書].md
- Brand evidence is complete: docs/brand_usage_audit.md records the official Mermaid asset and source; ledgers/ponchi_generation_batches.csv row F-140 is official_logo_applied. Any later image-edit must use the logo-free base and preserve separate deterministic overlay handling.
- Human-authored main figure: before/after contrast between replacing a PNG manually and editing text that generates a diagram.
- Current logo-free base: code-like blocks feed three output diagram panels (flow, sequence, graph); it does not show the manual-PNG before state or the authored text-edit contrast.

## Hold reason and decision needed

The source and authored brief differ in layout and the comparison being shown. Simplifying the three-output diagram would preserve a different main figure; making the requested PNG-versus-text before/after would redesign the source. Please decide whether the candidate prompt should follow the human-authored before/after brief or preserve the current three-output diagram and simplify only its detail.

Keep generation on hold until this precedence is confirmed. If later authorized, use only the logo-free base SHA listed above as the image-edit input; reserve the verified official Mermaid asset for the separate overlay step.

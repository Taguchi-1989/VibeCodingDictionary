# D-10 prompt hold — ponchi-simplification-v1.1

**Status:** Hold before prompt drafting; no image generated.

- Queue source: `assets/ponchi/final/D-10.webp`, SHA-256 `667ae60844b7a84cdc6f501b7afed9533074394c62a17cd316625c68d9e9e7e3`.
- The current final is an official-logo composite. Its PNG matches `assets/ponchi/experiments/batches/ponchi-batch-005/D-10_overlay_1254x627.png` byte-for-byte. The corresponding editable, logo-free base exists at `assets/ponchi/experiments/batches/ponchi-batch-005/D-10_base_1254x627.png`, SHA-256 `f68b05f2424c10ad1c2b22f978b18b7f6cd70071d7ede7faf965ce2d6152b68f`.
- The batch record says D-10 uses the official Claude Slate logo. `docs/brand_usage_audit.md` confirms Anthropic’s press kit and imported local Claude logo, but does not record this asset’s retrieval date or D-10 use-condition status. v1.1 requires those fields before a brand-item prompt can be drafted.
- The authored memo specifies a four-date model-retirement timeline and a small author character; the current final contains three dense model panels, several people/robot, and a top-right Claude wordmark. The layout is explicit, but the current prompt policy also forbids drawing the dates and model names, so the timeline’s exact milestones would not be readable in a candidate without a human-approved text exception.

**Exact unblock question:** Can the official Claude logo’s acquisition date and D-10 use-condition status be recorded from the source provenance, and should this image be allowed to show the source-supported model names/dates despite v1.1’s no-text rule? Until both are resolved, do not create a per-entry prompt or candidate.

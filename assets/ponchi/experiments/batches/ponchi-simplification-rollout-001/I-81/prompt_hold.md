# Prompt hold — I-81

Status: `prompt_hold`; no per-entry prompt or image candidate created.

- Current source: `assets/ponchi/final/I-81.webp` (1254×627), SHA-256 `ff1afd4a8f5dec6a6bd35ba1037f1c6e60d09194b70da1bcdcad7b3e44561ae4`; matches the selected queue row.
- Human brief: `content/entries/mcp/I-81_mcp_setup[人書].md` specifies server at left, settings file/command in the center, using tool at right, with three registration-scope branches below the center. It also calls for one developer character and a secret/API-key caution.
- Thumbnail evidence (200px wide): source places the person and configuration sheet on the left, three server-like items in the middle, and two tool/UI panels on the right, with extra database and connector paths. This differs from the authored server → settings → tool order and scope-branch layout.
- Brand: `ponchi_generation_batches.csv` row `ponchi-batch-015/I-81` says `logo_need=not_needed`, `logo_status=logo_avoid`. `docs/brand_usage_audit.md` has no I-81-specific section; keep tool depictions generic and do not imitate Claude product UI or logos.

**Hold reason / question:** The authored flow order conflicts with the current image's left-to-right arrangement. Should the prompt rearrange the composition to the authored server → settings → tool flow with scope branches, or preserve the current arrangement and only simplify its contents? Record the chosen precedence in `LAYOUT_AND_READING_ORDER` before drafting.

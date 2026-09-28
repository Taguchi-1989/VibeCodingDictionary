# I-80 v2 independent prompt review

- Reviewer: `/root/review_wave001_c` (independent of prompt author)
- Review date: 2026-09-28
- Verdict: **PASS** for prompt content; the candidate's palette audit remains a separate gate.
- Sidecar SHA-256: `907d670f5d66a65bdbe0b2d32b845e79130e6758295f34d12c55452f404d5ffc`
- Exact v2 prompt body SHA-256 (UTF-8, LF, excluding Markdown fence): `506f84347baafc118489fbde424f41e0829599171e9aa885b3869026db15eac7`

## Inputs and source meaning

- Source `assets/ponchi/final/I-80.webp`: actual SHA-256 `f7312fbe52652e19a41db37babd92704679979ab65aaeeaa4fa51895d66bf0a8`; matches sidecar and prompt and remains read-only.
- Character A reference `assets/ponchi/references/character-a-reader-woman.png`: actual SHA-256 `18e2b7e216bf76cd382002ca4e6caf20ef175332e28ec7b6ab0e5ebc2af7ddf0`; matches sidecar and prompt.
- Human brief `content/entries/mcp/I-80_diy_mcp_template[人書].md` describes one MCP Server with Tools, Resources, and Prompts, plus a local stdio path versus a shared HTTP path. The source visibly contains a server cabinet, three drawer concepts, the developer, and local/shared routes.
- Candidate v1 review accepts the meaning, 200px readability, Character A, and no-logo treatment. It holds for exact-white background and leaves a palette audit at `review` (off-palette ratio 0.010950). V2 scopes its visual edit to the white-background defect while explicitly retaining the three drawers, developer, and connection topology.

## Acceptance review

- The prompt retains exactly one generic MCP Server with three distinct unlabelled Tools/Resources/Prompts drawers, exactly one approved Character A developer, and two separate routes: local stdio to one nearby computer and shared HTTP to multiple neutral endpoints. It prohibits new panels, servers, marks, or extra detail, preserving the human brief and v1-passing layout.
- It prohibits product logos and branded interfaces; `LOGO_MODE` is not required and no logo clearspace is introduced.
- It names the existing palette and allows only the approved Character A clothing neutrals, then requires no extra colors. Exact-white background, all four corners, all 12 registered points, and the 3% perimeter are explicitly specified. Fail-fast failure keeps the candidate on HOLD; post-processing is prohibited.
- The output is experiment-only; promotion, adoption, publication, and release are prohibited.

## Gate status

`I-80_candidate_v2.png` was absent at review time. Prompt content is **PASS**; this does not clear the prior candidate palette-audit concern. The generated candidate must pass an independent palette audit as well as the strict-white gate. Keep generation blocked until the prompt PASS is reconciled in the applicable gate/ledger. Candidate v1 remains HOLD.

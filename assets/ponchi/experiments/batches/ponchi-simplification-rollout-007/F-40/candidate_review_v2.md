# F-40 candidate v2 independent review

- **Verdict:** HOLD
- **Reviewer:** `/root/review_wave001_b` (independent visual review)
- **Date:** 2026-09-28
- **Candidate:** `F-40_candidate_v2.png`, 1774×887 RGB
- **Candidate SHA-256:** `52D4E0FD2135715E7D4FAD7D1C7E2329C539CE655D09EEC322FB45E922A4F594`
- **Current sidecar SHA-256:** `B987B08351901BF9AE16B356FE8E09B35C03269557F200FC36601073A920F71D`
- **Reviewed v2 prompt body SHA-256:** `67FBA5EC2CF102C7BA986BACC27804F60C9D088C1A2C94798C3D4CAC05E96485`
- **Source:** `assets/ponchi/experiments/batches/ponchi-batch-009/F-40_base_1254x627.png`, actual SHA-256 `6B1D4F17A4CEEABF80E22C2C21DB3F568F134A49B7D3DB093EF163E9F15C6317`, 1254×627 RGB; matches sidecar.
- **Character reference:** `assets/ponchi/references/character-b-teacher-man.png`, actual SHA-256 `6CE81EA4957F8E2522292E5F48CAB2CE718A5E807024F755794079C7283F9C99`, 320×420 RGB; matches sidecar.

## Findings

- **Meaning and 200px readability — HOLD.** At 200×100, the package/source tray, blank dependency document, project folder, play control, and output window remain recognizable. However, left-to-right flow is source tray → manifest → project store → run/output. The human-approved reading order and reviewed prompt require manifest → packages from registry → store → script. The source tray arrow visibly points into the manifest, reversing the required first relationship and suggesting packages feed the dependency record. Rework the flow so the blank manifest leads into package acquisition and then the store/script. The source tray also contains six small package cubes rather than the simpler three large package blocks specified in the approved text-free translation.
- **Character — PASS.** Exactly one thoughtful Character B developer appears beside a generic laptop/terminal-like device. Hair, face, light gray clothing, and pose match the approved reference. No additional person or robot is visible.
- **Text, marks, and brand — PASS with simplification note.** There is no readable text, pseudo-text, npm logo, logo-like wordmark, or branded service UI. The output window’s three header dots are generic UI chrome, not text, but are unnecessary small controls under the removal/simplification instructions and should be removed in any further revision.
- **Series style — PASS.** The navy, pale-blue, black, and existing neutral-gray line illustration fits the v1.3 editorial style. The workflow symbols and person remain identifiable at thumbnail size.
- **Logo ROI and background — visual check only; machine gate pending.** The mapped internal-only reserved region `[970,0,1706,311)` appears blank, and no logo or other foreground mark is visible there. The canvas corners and open background look white on visual inspection. I did not measure exact RGB samples, corners, or full-mask coverage; root's machine audit and required mask review remain pending, so exact-white is not claimed PASS.

## Gate

Keep v2 on HOLD for the reversed manifest/source order and excess source-package detail. This review records no promotion/adoption decision. Complete root's independent machine checks and the v1.3 full-background-mask gate after any approved corrective generation.

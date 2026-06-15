# Catalog Synchronization Status

Last updated: 2026-06-12 (Codex selected-cap/Obsidian consolidation).

| Host | Catalog state | Raw workspace state | Access state |
|---|---|---|---|
| Batman | Canonical catalog present and updated (2026-06-12) | Obsidian report consolidated and plots regenerated in the vault. Local reports/configs, forensic audit scripts in `/checks/` | Available |
| Bob | Full catalog mirror synchronized on 2026-06-12. | OOD 0.3/0.5/q95 full-suite sweeps complete; selected-cap 10ep and 100ep comparisons complete. Best Bob selected-cap-family result is selected-cap delay30: 1,723/1,800, paired +5 vs Modified. | Available through `pcrobot` |
| Dean | Full catalog mirror synchronized on 2026-06-12. | Selected-cap 100ep complete and positive: 1,741/1,800, paired +15 vs Modified. Delay30 100ep complete and negative: 1,718/1,800, paired -3 vs Modified. OOD assets are available through experiment-local fallback `/home/dean/LIBERO-PRO`, not the canonical `/home/redafrix/LIBERO-PRO` tree. | Available through direct `dean` when reachable and fallback `dean-via-bob` |
| Sam | Full catalog mirror synchronized on 2026-06-10. | V2B/V2C/V2D adaptive-horizon diagnostics complete. No active processes. | Available |

## Sam Re-Integration Completed (2026-06-09)

Sam is back online and has been integrated into the workspace experiment catalog. The following actions were taken:
1. Checked and mapped all active/completed run paths and reports on Sam.
2. Created `SAM_WORKSPACE_SCAN_20260609.md` outlining host/workspace specifications and verifying all raw evaluations.
3. Updated `HOST_WORKSPACE_MAP.md` and `SYNC_STATUS.md` to reflect Sam's workspace paths.
4. Created `/home/rootalkhatib/test/reda_ws/fiper_ws/experiment_catalog/` on Sam and synchronized all canonical catalog files.

## Catalog Files Update Log (2026-06-09)

New files created by the workspace catalog audit:
- `TRUSTED_RESULTS_SUMMARY.md` — forensic-verified results with corrected intervention rates
- `MASTER_EXPERIMENT_INDEX.md` — central table of all campaigns
- `DATASET_MAP.md` — all datasets across hosts with provenance chain
- `HOST_WORKSPACE_MAP.md` — host details, SSH configs, GPU specs, paths
- `MODEL_AND_SUITE_IDENTITY.md` — checkpoint/detector hashes and suite verification
- `FORENSIC_AUDIT_MAP.md` — map of the 8-step forensic audit
- `OBSIDIAN_REPORT_ACCURACY_AUDIT_20260609.md` — cross-check of Obsidian report claims

Existing files updated:
- `KEY_RESULTS.md` — added OOD goal-swap results, forensic corrections, updated active work status
- `README.md` — added links to new files, new semantic corrections
- `SYNC_STATUS.md` — this file (updated host statuses)

Backup files (pre-update snapshots):
- `README.md.20260609_115800.bak`
- `KEY_RESULTS.md.20260609_115800.bak`
- `WORKSPACE_MAP.md.20260609_115800.bak`
- `inventory.json.20260609_115800.bak`

## Catalog Files Update Log (2026-06-10)

Updates from the Codex full workspace audit:
- `MASTER_EXPERIMENT_INDEX.md` — corrected Bob Campaign 7 from running to complete, added Bob 0.5 and q95 campaigns, added Sam V2 adaptive-horizon diagnostics.
- `TRUSTED_RESULTS_SUMMARY.md` — added q95 completed net-negative status and Sam V2B/V2C/V2D trusted-negative diagnostics.
- `KEY_RESULTS.md` — added full-suite OOD goal-object summary and adaptive-horizon interpretation.
- `HOST_WORKSPACE_MAP.md` — updated Bob completed q95 status, Dean direct SSH status, and Dean OOD asset caveat.
- `hosts/bob.md` — added recent OOD campaign paths.
- `hosts/sam.md` — added V2D commit-gate experiment entry.
- `CODEX_FULL_WORKSPACE_AUDIT_20260610.md` — direct Codex audit report from raw JSONL/config/host checks.
- `hosts/dean.md` / `MASTER_EXPERIMENT_INDEX.md` — added completed Dean selected-cap 10ep diagnostic and active 100ep confirmation.
- `DEAN_SELECTED_CAP_GATE_20260610.md` — detailed selected-cap result report and 100ep confirmation status.
- `MASTER_EXPERIMENT_INDEX.md` / `DEAN_SELECTED_CAP_GATE_20260610.md` — added completed Dean selected-cap margin-0.10 10ep diagnostic; mechanically valid but not selected for scaling.
- `MASTER_EXPERIMENT_INDEX.md` / `TRUSTED_RESULTS_SUMMARY.md` / `KEY_RESULTS.md` — marked Bob q95 OOD full-suite sweep complete: 1,710/1,800 risk successes, 10 rescues / 18 regressions, net -8 vs modified baseline.
- `DEAN_SELECTED_CAP_GATE_20260610.md` / `CODEX_FULL_WORKSPACE_AUDIT_20260610.md` / `source_reports/dean/reports/DEAN_SELECTED_CAP_INTERIM_FORENSIC_AUDIT_20260610.md` — added direct Codex forensic checks for the active Dean selected-cap 100ep run, including config schema, hashes, Task 0-3 paired results, Task 4 active progress, and the post-hoc `risk_reduction >= 0.08` candidate gate.
- `MASTER_EXPERIMENT_INDEX.md` / `TRUSTED_RESULTS_SUMMARY.md` / `KEY_RESULTS.md` / `source_reports/dean/reports/DEAN_SELECTED_CAP_FINAL_ANALYSIS_20260611.md` — marked Dean selected-cap 100ep full-suite run complete and trusted positive: 1,741/1,800 vs 1,726/1,800, paired 38 rescues / 23 regressions, net +15.
- `MASTER_EXPERIMENT_INDEX.md` / `TRUSTED_RESULTS_SUMMARY.md` — registered active Dean delay30 replication with seeds 400-499 in tmux `dean_selected_cap_delay30_100ep_20260611`.
- `source_configs/dean/realtime_deployment/selected_cap_delay30_100ep_20260611/` — archived the generator and README for the active Dean delay30 replication.
- `MASTER_EXPERIMENT_INDEX.md` / `KEY_RESULTS.md` / `inventory.json` / `hosts/bob.md` — added the June 5 Bob chunk10 modified-vs-official SimVLA diagnostic: modified 80/100, official 78/100, net +2. This is historical diagnostic evidence, not risk-aware evidence.

## Catalog Files Update Log (2026-06-12)

Updates from the selected-cap replication and report cleanup:
- `MASTER_EXPERIMENT_INDEX.md` — marked Bob selected-cap 10ep/100ep and Dean delay30 100ep as complete.
- `TRUSTED_RESULTS_SUMMARY.md` — added final Bob selected-cap 100ep table and Dean delay30 final table.
- `KEY_RESULTS.md` — added Bob selected-cap replication interpretation and updated Dean delay30 verdict.
- `source_reports/bob/reports/BOB_SELECTED_CAP_100EP_FINAL_ANALYSIS_20260612.md` — final Bob 100ep selected-cap report.
- `source_reports/dean/reports/DEAN_SELECTED_CAP_DELAY30_FINAL_ANALYSIS_20260612.md` — final Dean delay30 report.
- Obsidian main report rewritten as a consolidated single-file report with updated results, corrected architecture explanation, and five plot assets under `FIPER Risk-Aware Report 20260602/assets/`.

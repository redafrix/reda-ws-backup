---
title: Source Artifacts and Trust Checks
created: 2026-06-02
tags:
  - fiper/sources
  - audit
---

# Source Artifacts and Trust Checks

This note lists the local artifacts used to build the report. It is meant to make the numbers traceable for a future session.

## Main Source Reports

| Artifact | Used for |
|---|---|
| `reports/FIPER_WS_CURRENT_BASELINE_AND_ORGANIZATION_REPORT_20260528.md` | selected baseline definition, offline metrics, split summary, rejected ideas |
| `realtime_deployment/reports/REALTIME_TASK7_FINAL_CLEAN_AUDIT_AND_TIMING_REPORT_20260529.md` | first Task7 real-time baseline-vs-risk-aware result and timing |
| `gana's_zip/riskaware_v2_018_repro_20260602.zip` | 4-task same-seed summary and reproducibility bundle |
| `dean_uncertainty_work/outputs/all_tasks_random_v2/all_tasks_summary.csv` | Dean all-tasks random base vs uncertainty result |
| `dean_uncertainty_work/outputs/ood_last2_taskids_v1/ood_last2_summary.csv` | Dean last-two-task-id OOD base vs uncertainty result |

## Generated Report Artifacts

| Artifact | Purpose |
|---|---|
| `scripts/generate_fiper_obsidian_report_20260602.py` | regenerates this Obsidian report and all plots |
| `obsidian_reports/FIPER_RiskAware_Report_20260602/assets/*.png` | report plots |
| `obsidian_reports/FIPER_RiskAware_Report_20260602/*.md` | Obsidian notes |

## Trust Checks Already Encoded In The Story

- The selected model passed feature hygiene audits: no reward, success flag, future timestep, object pose, or OOD leakage as model input.
- The 4-task real-time comparison is same-reset-seed paired.
- The selected policy is not claimed as deployment-ready because recoveries and regressions both occur.
- Chunk-execution results are mentioned only as a separate finding, not as the main selected FIPER risk-aware result.

## Known Caveats

- Some timing and same-action-seed details depend on logs generated on Bob/Sam. The report focuses on the final audited summaries rather than reconstructing every raw rollout.
- Dean uncertainty features are promising but not yet selected as the main baseline. Raw 98D concatenation did not beat the base model overall on the OOD split.

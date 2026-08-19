# Converted OOD150 Evaluation of Current Main Isaac Risk Model

**Experiment**: `isaac_ood150_3cm350_main_v2_offline_eval`  
**Date**: 2026-08-19  
**Model**: `isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`  
**Dataset Scope**: **EXACT-ONLY NEW-PROTOCOL OOD150 SUBSET**  

---

## 1. Scope & Relabelability Audit

- **Historical OOD150 Baseline**: 150 episodes (72 old success, 78 old failure; 5,887 decision rows).
- **Relabeling Protocol**: 3.0 cm threshold, 350 control ticks (11.67 s), 30 Hz, H10 execution, **NO DWELL**.
- **Conversion Mode**: `EXACT_ONLY`.
  - **72 Proven Successes**: All 72 historical success episodes completed within $\le 863$ physics steps ($\le 216$ control ticks), mathematically proving a $\le 3$ cm crossing prior to tick 350.
  - **64 Proven Failures**: 64 historical failure episodes had full-trajectory minimum TCP-target distance $> 0.030$ m, mathematically proving they never reached $\le 3$ cm by tick 350.
  - **14 Excluded Episodes**: 14 historical failure episodes entered the region $(0.020\text{ m}, 0.030\text{ m}]$ but did not dwell. Because tick-by-tick trajectory distance was not logged prior to tick 350, their exact first crossing time relative to tick 350 is unresolvable with 100% mathematical certainty. They were strictly excluded.
- **Included Exact Subset**: **136 episodes** (72 success, 64 failure).
- **Retained Decision Rows (`decision_index <= 34`)**: **3,447 rows** (1,207 success rows, 2,240 failure rows). Max decision index: 34.

---

## 2. Model Discrimination Performance

Evaluated using frozen model checkpoint `model.pt` (`00ad096a...`) and normalization parameters `norm.npz` (`6fbd2b22...`):
- **Query AUROC**: **0.9201** (0.920088)
- **Query AUPRC**: **0.9621** (0.962124)
- **Episode-Balanced AUROC**: **0.9954** (0.995443)
- **Episode-Balanced AUPRC**: **0.9940** (0.993960)

---

## 3. Success Episode Length Diagnostic

Across the 72 included exact success episodes:
- **Mean Retained Query Length**: 16.76 queries
- **Median Query Length**: 17.0 queries
- **Range**: [8, 22] queries
- **OOD Mean Success Cutoff**: **17 queries** ($\approx 170$ control ticks)
- **Canonical Seen Test Cutoff**: **18 queries** ($\approx 180$ control ticks)

---

## 4. Frozen Operating Threshold Transfer

Operating thresholds are frozen from the canonical Seen validation split. **NO threshold calibration was performed on OOD data.**

### Paper-Style Table

| Rule | tau | Succ FA % | Fail Det % | Det@25 % | Det@50 % | Det@100 % | Det@OODMeanSucc100 % | Det@Canonical18Q % | Never % |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Best F1 | 0.5791 | 18.06% | 100.00% | 70.31% | 85.94% | 100.00% | 82.81% | 85.94% | 0.00% |
| Fixed 0.5 | 0.5000 | 25.00% | 100.00% | 75.00% | 89.06% | 100.00% | 89.06% | 89.06% | 0.00% |
| q90 success | 0.5631 | 19.44% | 100.00% | 70.31% | 85.94% | 100.00% | 84.38% | 85.94% | 0.00% |
| q95 success | 0.6643 | 13.89% | 100.00% | 59.38% | 81.25% | 100.00% | 78.12% | 81.25% | 0.00% |
| q99 success | 0.8792 | 5.56% | 100.00% | 42.19% | 75.00% | 100.00% | 67.19% | 75.00% | 0.00% |

---

## 5. Artifact Inventory
- `OOD150_SOURCE_AUDIT.json`: Original baseline vs active controller paths and raw inventory
- `OOD150_CONVERSION_AUDIT.json`: Relabeling proof, inclusion/exclusion counts
- `OOD150_INCLUDED_EPISODES.jsonl`: Metadata for all 136 included episodes
- `OOD150_EXCLUDED_EPISODES.jsonl`: Audit of all 14 excluded episodes with exact reasons
- `OOD150_FEATURE_AUDIT.json`: Verification of feature compatibility with SeqRiskModel
- `OOD150_MODEL_METRICS.json`: Discrimination metrics and success length stats
- `OOD150_THRESHOLD_SWEEP.json`: Complete 13-row sweep across all frozen operating thresholds
- `OOD150_THRESHOLD_SWEEP.csv`: Full sweep in CSV format
- `OOD150_THRESHOLD_SWEEP.md`: Full markdown table
- `OOD150_PAPER_STYLE_TABLE.md`: Compact 5-row paper table
- `SEEN_VS_OOD_PAPER_TABLE.md`: Side-by-side Seen internal TEST vs OOD150 transfer
- `OOD150_SCORES.jsonl`: Step-by-step risk predictions for all 3,447 retained rows

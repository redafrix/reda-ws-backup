# Experiment 006: Current Main Model Evaluation on Converted Exact-Only OOD150 Subset

**Status**: AUDITED PRIMARY EXTERNAL/OOD TRANSFER  
**Date**: 2026-08-19  
**Model**: `isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`  
**Dataset Scope**: **Exact-only converted historical OOD150 subset (136/150 episodes)**  
**Authoritative Commit**: [`cdd55fbd6958264322b3bc53aea8c63b4edeff33`](https://github.com/redafrix/reda-ws-backup/commit/cdd55fbd6958264322b3bc53aea8c63b4edeff33)  

---

## 1. Executive Summary

This experiment evaluates the zero-shot transfer of the canonical main Isaac temporal risk head (`isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`) on historical candidate-0 OOD150 evaluation trajectories converted to the current 3cm / 350-tick / no-dwell protocol.

### Key Results
- **Query AUROC / AUPRC**: **0.9201 / 0.9621**
- **Episode-Balanced AUROC / AUPRC**: **0.9954 / 0.9940**
- **100% Failure Detection Across All Frozen Thresholds**: Every proven failure episode was detected prior to the 350-tick horizon across all tested conformal operating points (`q50` through `q99`, Best F1, Fixed 0.5).
- **Early Detection**: At the `q95` operating point ($\tau = 0.6643$), 59.38% of failures were detected within the first 25% of the episode duration, and 81.25% within 50%.

---

## 2. Dataset Provenance & Relabelability Proof

### Historical OOD150 Baseline
- **Source Path**: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_locked_h10_ood150_seed20260728`
- **Frozen Arrays**: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/frozen_datasets/locked_h10_ood150_eval`
- **Total Historical Pool**: 150 episodes (72 old success, 78 old failure; 5,887 decision rows).

### New Reaching Protocol
- **Target Distance**: $d \le 0.030$ m (3.0 cm).
- **Max Horizon**: 350 control ticks (11.67 s @ 30 Hz).
- **Termination**: First crossing $\implies$ immediate SUCCESS (Label 0); tick 350 reached without crossing $\implies$ FAILURE/TIMEOUT (Label 1).
- **Dwell Requirement**: **NO DWELL**.

### Why Conversion is Exact-Only
1. **72 Proven Successes (Label 0)**: All 72 historical successes under the strict 2cm/dwell protocol completed in $\le 863$ physics steps ($\le 216$ control ticks), mathematically proving they crossed $\le 3$ cm prior to tick 350.
2. **64 Proven Failures (Label 1)**: 64 historical failures had full-trajectory minimum distance $> 0.030$ m, mathematically proving they never reached $\le 3$ cm.
3. **14 Excluded Episodes**: 14 historical failure episodes reached $\le 3\text{ cm}$ at some unknown point during the full legacy trajectory, but the first crossing time relative to tick 350 cannot be reconstructed from the saved evidence. Their new-protocol outcome is therefore unresolved and they are excluded.
   - **Excluded IDs**: `000007`, `000022`, `000023`, `000038`, `000044`, `000084`, `000090`, `000103`, `000114`, `000170`, `000195`, `000226`, `000232`, `000284`.
- **Included Exact Subset**: **136 episodes** (72 success, 64 failure).
- **Retained Rows (`decision_index <= 34`)**: **3,447 rows** (1,207 success rows, 2,240 failure rows; max decision index: 34).

---

## 3. Evaluated Model & Checksums
- **Model Checkpoint**: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/model.pt`
  - **SHA256**: `00ad096a9ca38577366e992e1d7f8aa25b6f56f2f2bd7354abce1790baf890f1`
- **Normalization Parameters**: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/norm.npz`
  - **SHA256**: `6fbd2b221c4490c975e3e1492c96a9e879a586f0b3a4c4eaf97ea05920960341`

---

## 4. Threshold Transfer Performance (Frozen Seen Validation Thresholds)

> [!IMPORTANT]
> **NO threshold calibration or tuning was performed on OOD data.** All operating thresholds are frozen directly from the canonical Seen validation calibration ($n=658$).

### Paper-Style Table

| Rule | tau | Succ FA % | Fail Det % | Det@25 % | Det@50 % | Det@100 % | Det@OODMeanSucc100 % | Det@Canonical18Q % | Never % |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Best F1 | 0.5791 | 18.06% | 100.00% | 70.31% | 85.94% | 100.00% | 82.81% | 85.94% | 0.00% |
| Fixed 0.5 | 0.5000 | 25.00% | 100.00% | 75.00% | 89.06% | 100.00% | 89.06% | 89.06% | 0.00% |
| q90 success | 0.5631 | 19.44% | 100.00% | 70.31% | 85.94% | 100.00% | 84.38% | 85.94% | 0.00% |
| q95 success | 0.6643 | 13.89% | 100.00% | 59.38% | 81.25% | 100.00% | 78.12% | 81.25% | 0.00% |
| q99 success | 0.8792 | 5.56% | 100.00% | 42.19% | 75.00% | 100.00% | 67.19% | 75.00% | 0.00% |

### Side-by-Side Comparison: Seen Internal TEST vs Converted OOD150

| Rule | Split | tau | Succ FA % | Fail Det % | Det@25 % | Det@50 % | Det@100 % | Never % |
|:---|:---|---:|---:|---:|---:|---:|---:|---:|
| **Best F1** | **Seen internal TEST** | 0.5791 | 7.60% | 100.00% | 60.26% | 85.90% | 100.00% | 0.00% |
| | **OOD150 converted exact** | 0.5791 | 18.06% | 100.00% | 70.31% | 85.94% | 100.00% | 0.00% |
| **Fixed 0.5** | **Seen internal TEST** | 0.5000 | 17.48% | 100.00% | 69.23% | 91.03% | 100.00% | 0.00% |
| | **OOD150 converted exact** | 0.5000 | 25.00% | 100.00% | 75.00% | 89.06% | 100.00% | 0.00% |
| **q90 success** | **Seen internal TEST** | 0.5631 | 8.97% | 100.00% | 61.54% | 85.90% | 100.00% | 0.00% |
| | **OOD150 converted exact** | 0.5631 | 19.44% | 100.00% | 70.31% | 85.94% | 100.00% | 0.00% |
| **q95 success** | **Seen internal TEST** | 0.6643 | 3.65% | 100.00% | 55.13% | 83.33% | 100.00% | 0.00% |
| | **OOD150 converted exact** | 0.6643 | 13.89% | 100.00% | 59.38% | 81.25% | 100.00% | 0.00% |
| **q99 success** | **Seen internal TEST** | 0.8792 | 1.22% | 100.00% | 38.46% | 74.36% | 100.00% | 0.00% |
| | **OOD150 converted exact** | 0.8792 | 5.56% | 100.00% | 42.19% | 75.00% | 100.00% | 0.00% |

---

## 5. Success-Length Diagnostic Caveat
- Across the 72 included exact success episodes, the mean retained query length is `16.76` queries (median: `17.0`, min: `8`, max: `22`).
- **Caveat**: These represent legacy query durations under the old dwell protocol, not exact reconstructed first-3cm termination lengths.

---

## 6. Primary Evidence Index
All primary artifacts, JSON reports, CSV files, and checksums are located in:
[`prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/`](file:///home/redafrix/tests/internship/prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/PAPER_EVIDENCE_INDEX.md)
- `OOD150_SOURCE_AUDIT.json`: `01191abc19ce03fabe98b72a8d6e85b8100eb54d33d7dec11eb6459cd1568b6f`
- `OOD150_CONVERSION_AUDIT.json`: `c44fd5f8b60407d05d077a94a61ad9a81dc7df2a30c95d68ce897f525dfe1a30`
- `OOD150_MODEL_METRICS.json`: `9a6494fffba5ae843fdb0e9a6d0baa78cbe18ec6aba0e3d18f8ce5e7c636f0f1`
- `OOD150_THRESHOLD_SWEEP.json`: `924fbdd9540b22c04f3e13b65774b90e22cc6b2b635ad6957a245c8a87176c8e`

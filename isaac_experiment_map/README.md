# Isaac Sim Experiment Map

Created: 2026-07-03
Updated: 2026-08-19

This folder is a documentation map for the Isaac Sim / IsaacLab experiments run in this workspace. It does not contain raw rollout data and does not move, rename, or perturb existing experiment folders.

---

## Result Hierarchy

### CURRENT MAIN (Audited 2026-08-19)
- **Protocol**: 3 cm distance threshold, 350 max control ticks (11.67 s), 30 Hz, H10 execution, **NO DWELL**.
- **Dataset**: `isaac_seen4904_h10_3cm350_exact_v1` (4,904 exact episodes: 4,387 success, 517 failure; 96,813 decision rows; 96 unresolvable episodes excluded).
- **Model**: `isaac_seen4904_h10_topk8_temporal_3cm350_main_v2` (SeqRiskModel, 128 width, 3 layers, 4 heads, pos_weight=4.3453).
- **Split**: Unified label-stratified 70/15/15 (Train: 3,433 eps / 67,725 rows; Val: 735 eps / 14,562 rows; Test: 736 eps / 14,526 rows).
- **Performance (Locked Internal TEST)**:
  - Query AUROC: **0.9408** | Query AUPRC: **0.8748**
  - Episode-Balanced AUROC: **0.9987** | Episode-Balanced AUPRC: **0.9782**
  - Conformal Best Val F1 Threshold (`0.5791`): **100.0% Failure Detection**, **7.60% Success False Alarm**.
- **Full Current Results**: [CURRENT_MAIN_ISAAC_RESULTS_20260819.md](CURRENT_MAIN_ISAAC_RESULTS_20260819.md) | [current_main_isaac_results_20260819.json](current_main_isaac_results_20260819.json)

### HISTORICAL (Preserved 2026-08-18)
- **Protocol**: 2 cm distance threshold, 600 max control ticks (20.0 s), 30 Hz, H10 execution, 0.2 s dwell settling requirement.
- **Seen4000 V1**: 4,000 episodes (3,908 success, 92 failure), `isaac_h10_topk8_temporal_v1`.
- **Historical Locked OOD150 Detector**: AUROC/AUPRC 0.91655 / 0.98003.
- **Historical Active OOD150 Controller**: 75/150 success (+3 rescues net, 11 rescues, 8 regressions).
- **Historical Record**: [FINAL_ISAAC_RESULTS_20260818.md](FINAL_ISAAC_RESULTS_20260818.md)

---

## Quick Index

| Experiment | Status | Main Local Evidence | Details |
|:---|:---|:---|:---|
| **CURRENT MAIN — 3cm350 exact4904 risk model** | **Audited Current Main** | `prepared_experiments/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/` | [CURRENT_MAIN_ISAAC_RESULTS_20260819.md](CURRENT_MAIN_ISAAC_RESULTS_20260819.md) |
| Corrected true-H10 SimVLA risk campaign (Historical) | Historical 2026-08-18 | `prepared_experiments/dean_isaac_online_ood150_engineering_cap090_v1/FINAL_RESULT.json` | [FINAL_ISAAC_RESULTS_20260818.md](FINAL_ISAAC_RESULTS_20260818.md) |
| SimVLA basic, Isaac no-rotation 10 tests | Completed, all failed | `vids/old/simvla_basic_10_tests_agent_view_2x_no_rotation.mp4` | [experiments/001_simvla_basic_no_rotation.md](experiments/001_simvla_basic_no_rotation.md) |
| Pi0.5 LIBERO, Isaac 5 reaching + 5 pick-place | Completed, all failed | `vids/pi05_libero_10_tests_agent_view_4x_labeled.mp4` | [experiments/002_pi05_libero_isaac.md](experiments/002_pi05_libero_isaac.md) |
| Pi0.5 DROID, Isaac 5 reaching + 5 pick-place | Completed, all failed | `vids/pi05_droid_10_tests_agent_view_4x_labeled.mp4` | [experiments/003_pi05_droid_isaac.md](experiments/003_pi05_droid_isaac.md) |
| Combined video speed + readable task labels | Completed | `*_4x_labeled.mp4` files in `vids/` | [experiments/004_video_outputs_and_labels.md](experiments/004_video_outputs_and_labels.md) |

---

## Files In This Map

- [CURRENT_MAIN_ISAAC_RESULTS_20260819.md](CURRENT_MAIN_ISAAC_RESULTS_20260819.md)
- [current_main_isaac_results_20260819.json](current_main_isaac_results_20260819.json)
- [FINAL_ISAAC_RESULTS_20260818.md](FINAL_ISAAC_RESULTS_20260818.md)
- [final_isaac_results_20260818.json](final_isaac_results_20260818.json)
- [experiments/001_simvla_basic_no_rotation.md](experiments/001_simvla_basic_no_rotation.md)
- [experiments/002_pi05_libero_isaac.md](experiments/002_pi05_libero_isaac.md)
- [experiments/003_pi05_droid_isaac.md](experiments/003_pi05_droid_isaac.md)
- [experiments/004_video_outputs_and_labels.md](experiments/004_video_outputs_and_labels.md)
- [experiments/005_seen4904_3cm350_main_v2.md](experiments/005_seen4904_3cm350_main_v2.md)
- [inventory/artifacts.md](inventory/artifacts.md)
- [inventory/experiment_index.json](inventory/experiment_index.json)
- [rerun_notes.md](rerun_notes.md)

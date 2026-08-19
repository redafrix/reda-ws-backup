# FINAL CLOSURE — Seen4904 Strict Mimic V3 Ablation

Experiment: `isaac_mimic_h10_strict_3cm350_seen4904_v3`

Main comparator: `isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`

This document freezes the final scientific disposition. No further retraining, feature changes, threshold changes, seed promotion, test rescoring or performance-driven modification is permitted for this ablation.

## 1. Dataset / protocol

Source dataset: `isaac_seen4904_h10_3cm350_exact_v1`

Frozen census:
- 4,904 episodes
- 4,387 success / 517 failure
- 96,813 query rows
- H10
- success: first `tcp_target_distance_m <= 0.030` within 350 control ticks at 30 Hz
- no dwell

Exact main-model split:
- train: 3,433 episodes, 3,071 success / 362 failure, 67,725 rows
- validation: 735 episodes, 658 success / 77 failure, 14,562 rows
- held-out test: 736 episodes, 658 success / 78 failure, 14,526 rows

Mimic and TopK8 held-out ordered `(final_episode_id, decision_index)` sequences are exact-equal for all 14,526 rows.

## 2. Strict Mimic fidelity decision

A recursive audit streamed all 96,813 source rows. The exact portable-Mimic cross-candidate trace names were absent on every row:
- `sample_pairwise_mse_mean`
- `sample_variance_max`
- `sample_variance_mean`
- `sample_velocity_mse_mean`
- `vector_field_l2_mean`

Therefore the strict fidelity baseline uses:
- dims 0..8: exact source-reproducible 8-candidate final-action disagreement features
- dims 9..33: exact zero
- dims 34..36: exact temporal-change features
- horizon: exact `[10,6]` source-reproducible Mimic H10 tensor

No candidate0 dynamics proxy is used.

## 3. Frozen primary Mimic result

Primary seed was frozen before test access:
- seed: 0
- checkpoint SHA256: `857e16b7d846051c29921d148d8545198e7057f2e1458040250de7b8cc965b82`
- primary operating point: validation-derived `conformal_alpha_0.10`
- threshold: `0.8907762169837952`

Held-out result:
- row AUROC: `0.8012386392854348`
- row AUPRC: `0.6697971252864523`
- success false alarms: `66/658` = 10.03%
- failure detected: `77/78` = 98.72%
- Det@10: `0/78`
- Det@25: `0/78`
- Det@50: `27/78`
- never detected: `1/78`
- mean first-alarm fraction: `0.520964749536178`

Seed2 is not promoted despite higher validation/test performance; it remains robustness evidence only.

## 4. Final threshold-independent matched comparison

The test query sequence is exact-equal across TopK8 and Mimic for all 14,526 rows.

TopK8:
- AUROC: `0.9407651224665466`
- AUPRC: `0.874846604284548`

Strict Mimic V3 seed0:
- AUROC: `0.8012386392854348`
- AUPRC: `0.6697971252864523`

TopK8 advantage:
- AUROC: `+0.13952648318111183`
- AUPRC: `+0.20504947899809567`

These are the primary matched ablation discrimination results.

## 5. Matched validation-row-best-F1 comparison

TopK8 threshold: `0.579133152961731`
Mimic seed0 threshold: `0.6724033355712891`

Both thresholds are selected from their respective validation row scores by maximizing row-level F1 and then applied unchanged to held-out test.

Important implementation nuance: the selection criterion is the same, but the tie-break implementation is not literally byte-identical. TopK8 uses `precision_recall_curve` plus `np.nanargmax`, while Mimic scans sorted unique score thresholds and chooses the higher threshold on an exact F1 tie. Therefore describe this comparison as **matched validation-row-best-F1 criterion**, not as identical threshold-selection code.

Held-out episode results:

TopK8:
- success false alarms: `50/658` = 7.60%
- failure detection: `78/78` = 100%
- Det@25: `47/78` = 60.26%
- Det@50: `67/78` = 85.90%

Strict Mimic V3 seed0:
- success false alarms: `243/658` = 36.93%
- failure detection: `78/78` = 100%
- Det@25: `3/78` = 3.85%
- Det@50: `60/78` = 76.92%

Differences, Mimic minus TopK8:
- false alarms: `+193` = +29.33 percentage points
- failure detection: `0`
- Det@25: `-44` = -56.41 percentage points
- Det@50: `-7` = -8.97 percentage points

## 6. Test-independence wording correction

Verbatim TopK8 source shows:

1. `validation_scores = predict(...)`
2. `test_scores = predict(...)`
3. `thresholds = threshold_table(validation.label, validation_scores)`

Thus test scores are computed before threshold calculation in execution order. However, the threshold function receives only validation labels and validation scores; test scores/labels do not enter threshold selection. The scientifically correct statement is:

**The TopK8 best-F1 threshold is validation-derived and test-independent in its selection inputs.**

Do NOT claim that the threshold file was physically written before test scoring.

## 7. Final scientific claim

Paper-safe claim:

> On the exact same 736-episode / 14,526-query Seen4904 held-out split under the 3 cm / 350-tick protocol, the proposed TopK8 risk monitor substantially outperformed the strict source-fidelity Mimic-H10 adaptation in row-level discrimination and early failure warning. TopK8 improved AUROC by 0.140 and AUPRC by 0.205. Under matched validation-row-best-F1 selection, both detected all 78 failures, but TopK8 reduced successful-episode false alarms from 36.9% to 7.6% and detected 47/78 failures by the first quarter of the retained query sequence versus 3/78 for Mimic.

Do NOT claim this is the exact original Mimic/W2A K1 implementation because the five genuine cross-candidate denoising traces were not retained in the source dataset. The correct name is **strict source-fidelity Mimic-H10 adaptation with unavailable denoising channels disabled**.

## 8. Closure

FINAL. No more optimization or test-driven changes to this ablation.

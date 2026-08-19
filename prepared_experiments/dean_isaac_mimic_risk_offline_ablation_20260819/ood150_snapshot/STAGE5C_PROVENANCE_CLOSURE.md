# Stage 5C — OOD150 Provenance Closure & Exact Matched Comparison

## 1. TopK8 Dataset Manifest Provenance
- Manifest Path: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/frozen_datasets/locked_h10_ood150_eval/manifest.json`
- Manifest SHA256: `e5b6cf816d9c10d346f62516d9770258512686b1aefa80c14b432fab5c3bc86a`
- Source Collection: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_locked_h10_ood150_seed20260728`
- Source Audit SHA256: `44f3bd850f25344ba6c445e82af72bcd45c9d063e8920cbe4cf42d90fc0ac289`
- Schema Version: `simvla_locked_evaluation_arrays_v1`

## 2. Exact Episode Membership Proof
- Mimic Unique Episodes: 150
- TopK8 Unique Episodes: 150
- Intersection: 150
- Mimic-Only: 0
- TopK8-Only: 0
- **Exact Set Equal**: YES
- **Exact Order Equal**: YES
- Mimic Sorted Set SHA256: `93dc36305b692c9ab48125bb26a5c17c808e69183cd9b03014b2bc4cda59ee4f`
- TopK8 Sorted Set SHA256: `93dc36305b692c9ab48125bb26a5c17c808e69183cd9b03014b2bc4cda59ee4f`

## 3. Row & Label Parity
- Mimic Rows: 5887 | TopK8 Rows: 5887
- Mimic Success/Failure: 72/78 | TopK8 Success/Failure: 72/78
- Query Key Equality: EXACT_MATCH (5887/5887 pairs)

## 4. Matched Comparison (Threshold-Independent)
| Metric | TopK8 | Mimic (Seed 0) | Delta (Mimic - TopK8) |
|---|---|---|---|
| Row AUROC | 0.9166 | 0.9284 | +0.0119 |
| Row AUPRC | 0.9800 | 0.9825 | +0.0025 |

## 5. Matched Operating Point: Row Best-F1
| Model | Threshold | Success FA | Failure Det | Det@10 | Det@25 | Det@50 |
|---|---|---|---|---|---|---|
| TopK8 (best_val_f1) | 0.7990 | 1/72 (1.39%) | 78/78 (100.00%) | 5/78 (6.41%) | 31/78 (39.74%) | 78/78 (100.00%) |
| Mimic (row_best_f1) | 0.9380 | 3/72 (4.17%) | 78/78 (100.00%) | 13/78 (16.67%) | 35/78 (44.87%) | 78/78 (100.00%) |

- FA Delta: +2.78 pp (+2 false alarms)
- Failure Detection Delta: 0
- Det@10 Delta: +8
- Det@25 Delta: +4
- Det@50 Delta: 0

## 6. Mimic Primary Operating Point: Conformal Alpha=0.10
- Threshold: 0.736110
- Success FA: 6/72 (8.33%)
- Failure Detection: 78/78 (100.00%)
- Det@10: 25/78 (32.05%)
- Det@25: 48/78 (61.54%)
- Det@50: 78/78 (100.00%)

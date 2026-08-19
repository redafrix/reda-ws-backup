# Stage 4B Summary — Corrected TopK8 Matched-Split Comparison

## 1. Provenance & Hash Identity Gate
- TopK8 Dataset Manifest SHA256: `8e3b7f4929fce4a648f174735ec9c0530966cf4e8a93a66a3e793432a5be4859`
- TopK8 Split Assignments SHA256: `a4b82dd6e6d944b2719ea071d1e66636cc4816e5e159c23adee382ff9e9ecac3`
- Mimic Expected Source Manifest SHA256: `8e3b7f4929fce4a648f174735ec9c0530966cf4e8a93a66a3e793432a5be4859`
- Mimic Expected Source Split SHA256: `a4b82dd6e6d944b2719ea071d1e66636cc4816e5e159c23adee382ff9e9ecac3`
- **All Hashes Match 100%**: YES

## 2. Exact Episode Membership Proof
- TopK8 Test Split Unique Episodes: 600
- Mimic Test Split Unique Episodes: 600
- Intersection: 600
- Mimic-Only: 0
- TopK8-Only: 0
- **Exact Set Equal**: YES
- Previous Stage4 133/600 Overlap Claim Status: INVALID (caused by comparing integer array indices directly to string episode IDs)

## 3. Threshold-Independent Metrics
| Metric | TopK8 | Mimic (Seed 0) | Delta (Mimic - TopK8) |
|---|---|---|---|
| Row AUROC | 0.9311 | 0.9171 | -0.0140 |
| Row AUPRC | 0.8186 | 0.8080 | -0.0106 |

## 4. Matched Calibration Rule: Row Best-F1
| Model | Threshold | Success FA | Failure Det | Det@10 | Det@25 | Det@50 |
|---|---|---|---|---|---|---|
| TopK8 (best_val_f1) | 0.7990 | 12/586 (2.05%) | 14/14 (100.00%) | 2/14 (14.29%) | 5/14 (35.71%) | 14/14 (100.00%) |
| Mimic (row_best_f1) | 0.9380 | 17/586 (2.90%) | 14/14 (100.00%) | 1/14 (7.14%) | 5/14 (35.71%) | 14/14 (100.00%) |

- FA Delta: +0.85 pp (+5 false alarms)
- Failure Detection Delta: 0
- Det@10 Delta: -1
- Det@25 Delta: 0
- Det@50 Delta: 0

## 5. Supplemental: Fixed 0.5 & Mimic Primary Alpha=0.10
- TopK8 Fixed 0.5: FA 50/586 (8.53%) | Det 14/14 (100%) | Det@10 5/14 (35.71%) | Det@25 8/14 (57.14%) | Det@50 14/14 (100%)
- Mimic Fixed 0.5: FA 94/586 (16.04%) | Det 14/14 (100%) | Det@10 6/14 (42.86%) | Det@25 10/14 (71.43%) | Det@50 14/14 (100%)
- Mimic Primary Alpha=0.10: Threshold 0.736110 | FA 43/586 (7.34%) | Det 14/14 (100%) | Det@10 4/14 (28.57%) | Det@25 8/14 (57.14%) | Det@50 14/14 (100%)

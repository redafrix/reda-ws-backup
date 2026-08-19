# Stage 1B Summary — TopK8 Comparison Provenance Closure

## 1. Provenance Verification
- TopK8 Test Results Path: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/test_results.json` (SHA256: `2c3de0d3153ffc58b7f1c228af0eb7515f0dc146439b5307f809593e2da7ce56`)
- TopK8 Thresholds Path: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/thresholds.json` (SHA256: `43a43e24c96d5820ccd4dc389cca8c8a330cbe2e1682020564adf291a039d1ac`)
- Query Key Parity: Exact ordered match across all 14,526 test queries (Sequence SHA256: `0f38b7d96e93c6e1e5147021e9347d7cceaf21d856bcacec18d8daa318723614`)
- Threshold Provenance: Proven validation-only selection for TopK8 `best_val_f1` (threshold 0.579133)

## 2. Threshold-Independent Comparison
- TopK8 AUROC: 0.9408 | Mimic Seed0 AUROC: 0.8012 | Delta: -0.1395
- TopK8 AUPRC: 0.8748 | Mimic Seed0 AUPRC: 0.6698 | Delta: -0.2050

## 3. Matched Row-Best-F1 Operating Point Comparison
- TopK8 (Threshold 0.5791): FA 50/658 (7.60%), Det 78/78 (100.00%), Det@25 47/78 (60.26%), Det@50 67/78 (85.90%)
- Mimic Seed0 (Threshold 0.6724): FA 243/658 (36.93%), Det 78/78 (100.00%), Det@25 3/78 (3.85%), Det@50 60/78 (76.92%)

## 4. Mimic Primary Operating Point (Conformal Alpha=0.10)
- Threshold: 0.890776
- Success False Alarms: 66/658 (10.03%)
- Failure Detection: 77/78 (98.72%)
- Det@25: 0/78 (0.00%)
- Det@50: 27/78 (34.62%)
- Never Detected: 1/78

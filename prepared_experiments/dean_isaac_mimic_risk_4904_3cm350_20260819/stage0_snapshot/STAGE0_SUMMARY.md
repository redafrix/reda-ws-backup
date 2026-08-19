# Stage 0 Summary — isaac_mimic_h10_strict_3cm350_seen4904_v3

## 1. Source Gate & Census
- Dataset Root: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/frozen_datasets/isaac_seen4904_h10_3cm350_exact_v1`
- Total Episodes: 4904 (4387 success / 517 failure)
- Total Rows: 96813
- Train Split: 3433 eps (3071/362), 67725 rows (12670/55055)
- Validation Split: 735 eps (658/77), 14562 rows (2695/11867)
- Test Split: 736 eps (658/78), 14526 rows (2730/11796)

## 2. Materialization & Hashes
- Derived Root: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/derived_datasets/isaac_mimic_h10_strict_3cm350_seen4904_v3`
- Normalization SHA256: `5564083f1561b627c81305c9ebfcb34732c4f3529bc2421ab6d4124682e84b26`
- Dataset Manifest SHA256: `26e633c8815d92a46df841bd7976ec942740b83ec477cc20e7d9f6cf87bb3019`
- Dynamics Mode: STRICT_MISSING (dims 9..33 set to 0.0)

## 3. Training & Validation Freeze Across All 5 Seeds
| Seed | Best Epoch | Val AUROC | Val AUPRC | Alpha 0.10 Threshold | Checkpoint SHA256 |
|---|---|---|---|---|---|
| Seed 0 | Ep 07 | 0.7962 | 0.6569 | 0.890776 | `857e16b7d846051c...` |
| Seed 1 | Ep 04 | 0.8069 | 0.6725 | 0.826866 | `df54e5d58e8a9d15...` |
| Seed 2 | Ep 09 | 0.8902 | 0.8100 | 0.936884 | `6d15f87136a7e2ef...` |
| Seed 3 | Ep 08 | 0.8015 | 0.6657 | 0.879802 | `ee427aa4f710bfac...` |
| Seed 4 | Ep 09 | 0.7938 | 0.6546 | 0.907982 | `449cf5d4d2bf1b8b...` |

- Training Freeze SHA256: `ec925b2dea8a66dd7b5317790d8f8c18bf59e67da0ddb0278ca678b5d8637e21`
- All Seed Validation Freeze SHA256: `99013ab9c4a857ba9f3b48e2b9abe80613aeb2afc91b89fdfada27631201aa7e`
- Primary Seed: 0 | Primary Operating Point: conformal_alpha_0.10 | Threshold: 0.890776

## 4. Pre-Scoring Safety Locks
- Held-out seen test scored: NO
- OOD scored: NO
- Isaac Sim launched: NO
- HARD1000 touched: NO

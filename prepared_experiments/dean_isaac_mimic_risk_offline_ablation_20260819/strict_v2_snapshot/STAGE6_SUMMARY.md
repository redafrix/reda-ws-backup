# Stage 6 Summary — Strict Mimic Fidelity Baseline V2

## 1. Dataset & Parity Audit
- Dataset Root: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/derived_datasets/isaac_mimic_h10_strict_missingdyn_v2`
- Total Rows: 75603
- Parity Status: PASSED (scalar 0..8 max diff 0.000e+00, horizon max diff 0.000e+00, disabled dims 9..33 zero)
- Normalization SHA256: `d055a71bc2e531264f35d8bdd91e545d3f3b39cbba1cc543699ec1b987107830`
- Dataset Manifest SHA256: `852ad05e6208caba23c630174eb6784793304281169e5e24a25da22d030b57a1`

## 2. Multi-Seed Training Results
| Seed | Best Epoch | Val AUROC | Val AUPRC | Checkpoint SHA256 | Alpha 0.10 Threshold |
|---|---|---|---|---|---|
| Seed 0 | Ep 04 | 0.8890 | 0.7724 | `78b801c907156110...` | 0.628429 |
| Seed 1 | Ep 00 | 0.9069 | 0.7844 | `3297d3a891b369cd...` | 0.886208 |
| Seed 2 | Ep 03 | 0.8888 | 0.7696 | `14e9fe86991ab33d...` | 0.753820 |
| Seed 3 | Ep 04 | 0.8791 | 0.7653 | `7d1a32cc8e2b7f5d...` | 0.809265 |
| Seed 4 | Ep 07 | 0.8823 | 0.7649 | `775c585c4bc5edcc...` | 0.674970 |

- Primary Seed 0 Validation AUROC: 0.888961
- Primary Seed 0 Validation AUPRC: 0.772387
- Primary Seed 0 Alpha 0.10 Threshold: 0.628429

## 3. Pre-Scoring Safety Locks
- Held-out seen test scored: NO
- OOD scored: NO
- Isaac Sim launched: NO
- HARD1000 touched: NO

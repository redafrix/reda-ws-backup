# Stage 3/3B Summary — Five-Seed Training & Validation Freeze

## 1. Primary Predeclared Operating Point
- Primary Seed: 0
- Primary Operating Point: `conformal_alpha_0.10`
- Model Checkpoint: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_mimic_h10_c0dyn_v1/seed_0/best_model.pt`
- Checkpoint SHA256: `3b8d4f40f09a8008a0d9b4db73d6bb6ef03191cbda8d4bfd1999908611fe6723`
- Best Epoch: 3
- Validation Row AUROC: 0.927682
- Validation Row AUPRC: 0.827582
- Conformal alpha=0.10 Threshold: 0.736110

## 2. Robustness Repeats (Seeds 0..4)
| Seed | Best Epoch | Val AUROC | Val AUPRC | Alpha 0.10 Thresh |
|---|---|---|---|---|
| Seed 0 (Primary) | 3 | 0.927682 | 0.827582 | 0.736110 |
| Seed 1 | 4 | 0.926862 | 0.830886 | 0.829799 |
| Seed 2 | 2 | 0.918695 | 0.815742 | 0.756277 |
| Seed 3 | 3 | 0.923015 | 0.826365 | 0.679524 |
| Seed 4 | 5 | 0.922836 | 0.826488 | 0.649247 |

- Mean Validation AUROC: 0.923818 +/- 0.003199
- Mean Validation AUPRC: 0.825413 +/- 0.005089

## 3. Cryptographic Hashes
- Training Freeze SHA256: `8d84010c2989d605a910775e4a762e084f9b34de6855b323781356d3258876a0`
- All-Seed Validation Freeze SHA256: `4235179f98634a1dce53f013b3dd06ecb37cf2a7ad7e12564b4027dc9889a50a`
- Dataset Manifest V2 SHA256: `043f894e82c8cfc94c1ba8a5c788064a31d33f6112d1eefe09cbe14da40977d3`
- Normalization SHA256: `40ff9aeab3adfd80d30ac7b689733a55d9551a780ebd80b2789805cee7e60e0a`

## Corrected True-H10 Isaac Large / Local-Only Artifacts (2026-08-18)

These primary artifacts remain in the Dean workspace and should be referenced by path/hash instead of moving large binary/raw rollout payloads into Git.

| Artifact | Dean path | Recorded identity / handling |
|---|---|---|
| V1 model | `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_h10_topk8_temporal_v1/model.pt` | SHA-256 `ad049519746913c4c2ce1a0b57fb32ad5c3395f5bce6841648c68cc94f862b38`; do not duplicate large binary unless explicitly required |
| Frozen normalization | `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/frozen_datasets/isaac_seen_h10_topk8_v1/normalization.json` | SHA-256 `78c934b33e0536bd7cb6b7e5b1962da32305729f602d8269d3a38422841ce050`; small file may be mirrored |
| Raw Seen4000 | `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_seen_h10_round_000_seed20260730/` | 4000 true-H10 episodes; keep raw episode payloads local |
| Historical locked OOD150 | `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_locked_h10_ood150_seed20260728/` | 150 true-H10 episodes; keep per-row/raw payloads local, mirror only small metadata/evaluation files |
| Definitive active OOD150 raw run | `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/online_evals/isaac_ood150_engineering_cap090_v1/runs/definitive_full150/` | 150 completed; final small evidence already mirrored under `prepared_experiments/dean_isaac_online_ood150_engineering_cap090_v1/` |
| HARD1000 | `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_seen_h10_round_002_seed20260804/` | active collection; preserve original 249 identity snapshot SHA `12dcd6f6c3d24b0bb271879f3f75deb04774cc727252b9ba31dd120d75197bc9` |

Never treat the invalid historical alternative-score reconstruction from commit `70327b4b31bde35c01fda29a807f9100b5295a62` as a primary artifact for candidate-wise calibration. Correction commit: `86f5baf3281596df2305409499fc9e0c21d119ed`.

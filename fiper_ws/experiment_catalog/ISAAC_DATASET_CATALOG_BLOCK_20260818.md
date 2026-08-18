## Corrected True-H10 Isaac Datasets (2026-08-18)

Canonical workspace: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`.

| Role | Path | Episodes / rows | Status |
|---|---|---:|---|
| Raw Seen Round0 true-H10 | `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_seen_h10_round_000_seed20260730/` | 4000 episodes: 3908 success / 92 failure | `AUDITED_PRIMARY` |
| Frozen V1 dataset | `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/frozen_datasets/isaac_seen_h10_topk8_v1/` | 75,603 rows; train 52,825 / val 11,410 / test 11,368 | `AUDITED_PRIMARY` |
| Locked historical true-H10 OOD150 | `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_locked_h10_ood150_seed20260728/` | 150 episodes: 72 success / 78 failure; 5,887 rows | `AUDITED_PRIMARY_OFFLINE` |
| Definitive active OOD150 | `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/online_evals/isaac_ood150_engineering_cap090_v1/runs/definitive_full150/` | 150 episodes; 5,757 decisions | `AUDITED_FINAL_ENGINEERING_EVAL` |
| HARD1000 enrichment | `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_seen_h10_round_002_seed20260804/` | target 1000; resumed from preserved 249 | `ACTIVE_NOT_FINAL` |

Frozen V1 model SHA-256: `ad049519746913c4c2ce1a0b57fb32ad5c3395f5bce6841648c68cc94f862b38`.

Frozen V1 normalization SHA-256: `78c934b33e0536bd7cb6b7e5b1962da32305729f602d8269d3a38422841ce050`.

Do not mix these true-H10 datasets with the superseded H1/receding-H1 Isaac collections. Do not use commit `70327b4b31bde35c01fda29a807f9100b5295a62` as a source of valid historical alternative-candidate scores.

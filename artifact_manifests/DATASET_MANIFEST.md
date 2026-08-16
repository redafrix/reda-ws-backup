# Scientific Dataset Manifest

| Dataset Identifier | Path | Episodes | Decisions | Label Contracts Supported | Scientific Role |
|---|---|---|---|---|---|
| `isaac_seen_h10_round0` | `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/outputs/final_seen_h10_round_000_seed20260730` | 3,737 (aim 4,000) | ~600,000 | `strict_2cm`, `operational_4cm` | Primary H10 execution training dataset |
| `isaac_seen_round0_broad` | `/mnt/ai/projects/simvla_isaac_risk_collection_20260730/outputs/final_seen_round_000_seed20260730` | 4,000 | 731,418 | `strict_2cm`, `operational_4cm` | Round 0 baseline broad collection |
| `locked_ood150_eval` | `/mnt/ai/projects/simvla_isaac_risk_collection_20260730/outputs/final_locked_ood150_seed20260728` | 150 | 60,262 | Binary failure / timeout | Locked out-of-distribution evaluation set |
| `libero_goal_object_900` | `/media/redafrix/My Passport1/reda_ws/fiper_ws/datasets/goal_object_900.hdf5` | 900 | 180,000 | Multi-task success / intervention | Online LIBERO-PRO intervention dataset |
| `libero_official_2000` | `/media/redafrix/My Passport1/reda_ws/fiper_ws/datasets/official_2000.hdf5` | 2,000 | 450,000 | Official benchmark criteria | Standard in-distribution baseline |

# Dataset Map

Updated: 2026-06-09 by workspace catalog audit.

This file catalogs all known offline training datasets and data collections across hosts.

---

## 1. FIPER Sweep Eternal (Bob + Sam, 2026-05-27)

| Property | Value |
| :--- | :--- |
| **Purpose** | Original FIPER receding-horizon rollout data collection for detector training |
| **Execution Mode** | Receding horizon (execute first action only) |
| **Instances** | `bob_instance_A` (5.7 GB), `bob_instance_B`, `sam_instance_A`, `sam_instance_B` |
| **Bob Path** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/data/frozen/fiper_sweep_eternal_20260527_combined` |
| **Sam Path** | `/home/rootalkhatib/test/reda_ws/fiper_ws/data/frozen/fiper_sweep_eternal_20260527_combined` |
| **Batman Path** | `/home/redafrix/tests/internship/fiper_ws/data/frozen/fiper_sweep_eternal_20260526_combined` |
| **Data Format** | `fiper_receding_samples.jsonl` per instance |
| **Total Rows** | ~734,266 receding rows (combined) |
| **Status** | Frozen. Used for the original `v2_018_transformer_k16` detector training. |

---

## 2. Dean Object Uncertainty Collection (Dean, 2026-05-29)

| Property | Value |
| :--- | :--- |
| **Purpose** | Data collection with modified SimVLA `ckpt-60000` to capture uncertainty features |
| **Execution Mode** | Receding horizon with uncertainty head active |
| **Workers** | 4 workers (worker_0 through worker_3) |
| **Dean Path** | `/home/dean/fiper_uncertainty_collection/runs/dean_object_uncertainty_20260529` |
| **Episodes** | worker_0: 1,136 / worker_1: 1,043 / worker_2: 1,084 / worker_3: 994 = **4,257 total** |
| **Data Format** | `episode_summaries.jsonl` + `fiper_receding_samples.jsonl` (7.3 GB per worker) per worker |
| **Suites** | Multi-suite (includes `libero_spatial_object`, `libero_goal_object`, etc.) |
| **Status** | Frozen. Used for Dean's offline detector training (all-tasks, OOD last2-taskids, TopK sweep). |

---

## 3. Goal-Object Production Collection (Dean, 2026-06-05)

| Property | Value |
| :--- | :--- |
| **Purpose** | Focused `libero_goal_object` data collection for H10 chunk-10 detector training |
| **Execution Modes** | Dual: chunk10 + receding (paired collections) |
| **Dean Path** | `/home/dean/fiper_goal_object_collection_20260605/runs/production_20260605` |
| **Sub-datasets** | |
| | `exact_200/chunk10` — 200 validated episodes (162 success, 38 failure) |
| | `exact_200/receding` — 200 validated episodes (153 success, 47 failure) |
| | `continuous_100000/chunk10` — 17,409 episodes (ongoing) |
| | `continuous_100000/receding` — 2,745 episodes (ongoing) |
| **Validation** | `EXACT_200_VALIDATED_AND_PROTECTED.json` — validated at 2026-06-05T19:05 |
| **Data Format** | `episode_summaries.jsonl` + `.npz` per episode |
| **Status** | The `exact_200` subset is frozen and validated. The `continuous_100000` dataset continues to grow. |

---

## 4. H10 Continuous Chunk10 Flat (Bob, 2026-06-08)

| Property | Value |
| :--- | :--- |
| **Purpose** | The specific dataset used to train the production H10 base and TopK8 detectors |
| **Execution Mode** | Chunk-10 (H10) |
| **Bob Path** | `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/inputs/datasets/continuous_chunk10_flat` |
| **Total Episodes** | **17,409** (14,005 successes, 3,404 failures/timeouts) |
| **Split Allocations** | |
| | `failure_train_seen`: 2,724 episodes (68,100 query rows) |
| | `failure_val_seen`: 680 episodes (17,000 query rows) |
| | `success_train_seen`: 11,205 episodes (120,030 query rows) |
| | `success_val_seen`: 1,400 episodes (14,997 query rows) |
| | `success_calib_seen`: 1,400 episodes (15,339 query rows) |
| | `success_test_seen` / `failure_test_seen`: 0 episodes (test evaluated separately on `exact_200_chunk10`) |
| **Task Distribution** | Task 3: 1,368 episodes / Task 6: 1,423 episodes / Task 8: also present |
| **Seed Overlap with Evaluation** | **0%** |
| **Status** | Frozen. This is the canonical training dataset for the H10 detector campaign. |

---

## 5. Dean Offline Detector Models (Dean, 2026-06-01/02)

| Path on Dean | Split | Detectors |
| :--- | :--- | :--- |
| `experiments/dean_all_tasks_full_uncertainty_test_20260601` | all_tasks_random | base, unc_raw |
| `experiments/dean_ood_last2_taskids_full_v1_20260601` | ood_last2_taskids_full | base, unc_raw |
| `experiments/dean_uncertainty_topk_feature_sweep_v1_20260602` | all_tasks_full + ood_last2_taskids_full | unc_topk8, unc_topk16, unc_topk32 |
| `experiments/current_dean_risk_models_20260602` | all_tasks_full + ood_last2_taskids_full | base, unc_topk8 (packaged current models) |

---

## Provenance Chain

```
Dean object uncertainty collection (4,257 episodes, multi-suite)
  → Dean offline detector training (all_tasks_full, ood_last2_taskids, topk sweep)
  → TopK8 feature selection: dims [6, 21, 25, 27, 23, 2, 26, 24]
  → Old TopK8 detector (hash 0ea8e943...)

Dean goal-object production (17,409 chunk10 episodes, libero_goal_object only)
  → Transferred to Bob as continuous_chunk10_flat
  → H10 base + TopK8 detector training on Bob
  → H10 TopK8 detector (hash 687b5d35...)
  → Production deployment in online campaigns (Task 3/6/8 + OOD goal-swap)
```

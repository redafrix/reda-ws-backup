# DETAILED FORENSIC SANITY AUDIT CHECKS

## 1. Inventory of Production Runs

| Campaign | Run Directory | Suite | Task ID | Policy | Episodes | Success | Failure | Error | Mean Steps |
|---|---|---|---|---|---|---|---|---|---|
| campaign1_risk_proof | inputs/datasets/continuous_chunk10/worker_0 | unknown | unknown | unknown | 17409 | 14005 | 3404 | 0 | 0.00 |
| campaign1_risk_proof | inputs/datasets/continuous_chunk10_flat/worker_0 | unknown | unknown | unknown | 17409 | 14005 | 3404 | 0 | 131.69 |
| campaign1_risk_proof | inputs/datasets/exact_200_chunk10/worker_0 | unknown | unknown | unknown | 200 | 162 | 38 | 0 | 0.00 |
| campaign1_risk_proof | runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8 | libero_goal_object | 3 | risk_topk8 | 50 | 9 | 41 | 0 | 278.10 |
| campaign1_risk_proof | runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8 | libero_goal_object | 3 | risk_topk8 | 50 | 8 | 42 | 0 | 278.14 |
| campaign1_risk_proof | runs/online/task3/modified_simvla/shard_0/simvla_only | libero_goal_object | 3 | simvla_only | 50 | 9 | 41 | 0 | 278.06 |
| campaign1_risk_proof | runs/online/task3/modified_simvla/shard_1/simvla_only | libero_goal_object | 3 | simvla_only | 50 | 8 | 42 | 0 | 278.14 |
| campaign1_risk_proof | runs/online/task3/original_h10_risk_base/shard_0/risk_base | libero_goal_object | 3 | risk_base | 50 | 5 | 45 | 0 | 293.64 |
| campaign1_risk_proof | runs/online/task3/original_h10_risk_base/shard_1/risk_base | libero_goal_object | 3 | risk_base | 50 | 7 | 43 | 0 | 286.64 |
| campaign1_risk_proof | runs/online/task3/original_simvla/shard_0/simvla_only | libero_goal_object | 3 | simvla_only | 50 | 5 | 45 | 0 | 293.64 |
| campaign1_risk_proof | runs/online/task3/original_simvla/shard_1/simvla_only | libero_goal_object | 3 | simvla_only | 50 | 7 | 43 | 0 | 286.52 |
| campaign1_risk_proof | runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8 | libero_goal_object | 6 | risk_topk8 | 50 | 29 | 21 | 0 | 195.82 |
| campaign1_risk_proof | runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8 | libero_goal_object | 6 | risk_topk8 | 50 | 28 | 22 | 0 | 200.12 |
| campaign1_risk_proof | runs/online/task6/modified_simvla/shard_0/simvla_only | libero_goal_object | 6 | simvla_only | 50 | 31 | 19 | 0 | 195.96 |
| campaign1_risk_proof | runs/online/task6/modified_simvla/shard_1/simvla_only | libero_goal_object | 6 | simvla_only | 50 | 26 | 24 | 0 | 205.58 |
| campaign1_risk_proof | runs/online/task6/original_h10_risk_base/shard_0/risk_base | libero_goal_object | 6 | risk_base | 50 | 27 | 23 | 0 | 208.06 |
| campaign1_risk_proof | runs/online/task6/original_h10_risk_base/shard_1/risk_base | libero_goal_object | 6 | risk_base | 50 | 24 | 26 | 0 | 209.08 |
| campaign1_risk_proof | runs/online/task6/original_simvla/shard_0/simvla_only | libero_goal_object | 6 | simvla_only | 50 | 28 | 22 | 0 | 205.46 |
| campaign1_risk_proof | runs/online/task6/original_simvla/shard_1/simvla_only | libero_goal_object | 6 | simvla_only | 50 | 25 | 25 | 0 | 206.54 |
| campaign1_risk_proof | runs/online/task8/modified_h10_risk_topk8/shard_0/risk_topk8 | libero_goal_object | 8 | risk_topk8 | 1 | 1 | 0 | 0 | 73.00 |
| campaign1_risk_proof | runs/online/task8/modified_h10_risk_topk8/shard_1/risk_topk8 | libero_goal_object | 8 | risk_topk8 | 1 | 1 | 0 | 0 | 72.00 |
| campaign1_risk_proof | runs/online/task8/modified_simvla/shard_0/simvla_only | libero_goal_object | 8 | simvla_only | 3 | 3 | 0 | 0 | 67.67 |
| campaign1_risk_proof | runs/online/task8/modified_simvla/shard_1/simvla_only | libero_goal_object | 8 | simvla_only | 2 | 2 | 0 | 0 | 125.50 |
| campaign1_risk_proof | runs/online/task8/original_h10_risk_base/shard_0/risk_base | libero_goal_object | 8 | risk_base | 50 | 43 | 7 | 0 | 116.60 |
| campaign1_risk_proof | runs/online/task8/original_h10_risk_base/shard_1/risk_base | libero_goal_object | 8 | risk_base | 50 | 48 | 2 | 0 | 97.24 |
| campaign1_risk_proof | runs/online/task8/original_simvla/shard_0/simvla_only | libero_goal_object | 8 | simvla_only | 50 | 44 | 6 | 0 | 114.34 |
| campaign1_risk_proof | runs/online/task8/original_simvla/shard_1/simvla_only | libero_goal_object | 8 | simvla_only | 50 | 47 | 3 | 0 | 101.30 |
| campaign2_aggressive_task3 | runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8 | libero_goal_object | 3 | risk_topk8 | 50 | 10 | 40 | 0 | 276.28 |
| campaign2_aggressive_task3 | runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8 | libero_goal_object | 3 | risk_topk8 | 50 | 9 | 41 | 0 | 277.10 |
| campaign2_aggressive_task3 | runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8 | libero_goal_object | 6 | risk_topk8 | 50 | 33 | 17 | 0 | 188.78 |
| campaign2_aggressive_task3 | runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8 | libero_goal_object | 6 | risk_topk8 | 50 | 29 | 21 | 0 | 192.10 |
| campaign3_old_detector_task6 | runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8 | libero_goal_object | 6 | risk_topk8 | 50 | 33 | 17 | 0 | 182.62 |
| campaign3_old_detector_task6 | runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8 | libero_goal_object | 6 | risk_topk8 | 50 | 27 | 23 | 0 | 207.02 |
| campaign4_ood_goal_swap | runs/online/libero_goal_swap/bowl_on_plate/modified_simvla/simvla_only | libero_goal_swap | 8 | simvla_only | 2 | 0 | 2 | 0 | 300.00 |
| campaign4_ood_goal_swap | runs/online/libero_goal_swap/bowl_on_plate/original_simvla/simvla_only | libero_goal_swap | 8 | simvla_only | 2 | 0 | 2 | 0 | 300.00 |
| campaign4_ood_goal_swap | runs/online/libero_goal_swap/bowl_on_plate/risk_topk8/risk_topk8 | libero_goal_swap | 8 | risk_topk8 | 2 | 0 | 2 | 0 | 300.00 |
| campaign4_ood_goal_swap | runs/online/libero_goal_swap/cream_cheese_bowl/modified_simvla/simvla_only | libero_goal_swap | 6 | simvla_only | 2 | 0 | 2 | 0 | 300.00 |
| campaign4_ood_goal_swap | runs/online/libero_goal_swap/cream_cheese_bowl/original_simvla/simvla_only | libero_goal_swap | 6 | simvla_only | 2 | 0 | 2 | 0 | 300.00 |
| campaign4_ood_goal_swap | runs/online/libero_goal_swap/cream_cheese_bowl/risk_topk8/risk_topk8 | libero_goal_swap | 6 | risk_topk8 | 2 | 0 | 2 | 0 | 300.00 |
| campaign4_ood_goal_swap | runs/online/libero_goal_swap/top_drawer_bowl/modified_simvla/simvla_only | libero_goal_swap | 3 | simvla_only | 2 | 0 | 2 | 0 | 300.00 |
| campaign4_ood_goal_swap | runs/online/libero_goal_swap/top_drawer_bowl/original_simvla/simvla_only | libero_goal_swap | 3 | simvla_only | 4 | 0 | 2 | 2 | 150.00 |
| campaign4_ood_goal_swap | runs/online/libero_goal_swap/top_drawer_bowl/risk_topk8/risk_topk8 | libero_goal_swap | 3 | risk_topk8 | 2 | 0 | 2 | 0 | 300.00 |
| campaign4_ood_goal_swap | runs/production_goal_swap_100ep_20260608/bowl_on_plate/modified_simvla/simvla_only | libero_goal_swap | 8 | simvla_only | 100 | 3 | 97 | 0 | 297.52 |
| campaign4_ood_goal_swap | runs/production_goal_swap_100ep_20260608/bowl_on_plate/original_simvla/simvla_only | libero_goal_swap | 8 | simvla_only | 100 | 1 | 99 | 0 | 299.63 |
| campaign4_ood_goal_swap | runs/production_goal_swap_100ep_20260608/bowl_on_plate/risk_topk8/risk_topk8 | libero_goal_swap | 8 | risk_topk8 | 100 | 2 | 98 | 0 | 298.51 |
| campaign4_ood_goal_swap | runs/production_goal_swap_100ep_20260608/cream_cheese_bowl/modified_simvla/simvla_only | libero_goal_swap | 6 | simvla_only | 100 | 0 | 100 | 0 | 300.00 |
| campaign4_ood_goal_swap | runs/production_goal_swap_100ep_20260608/cream_cheese_bowl/original_simvla/simvla_only | libero_goal_swap | 6 | simvla_only | 100 | 0 | 100 | 0 | 300.00 |
| campaign4_ood_goal_swap | runs/production_goal_swap_100ep_20260608/cream_cheese_bowl/risk_topk8/risk_topk8 | libero_goal_swap | 6 | risk_topk8 | 100 | 0 | 100 | 0 | 300.00 |
| campaign4_ood_goal_swap | runs/production_goal_swap_100ep_20260608/top_drawer_bowl/modified_simvla/simvla_only | libero_goal_swap | 3 | simvla_only | 100 | 9 | 91 | 0 | 294.16 |
| campaign4_ood_goal_swap | runs/production_goal_swap_100ep_20260608/top_drawer_bowl/original_simvla/simvla_only | libero_goal_swap | 3 | simvla_only | 100 | 15 | 85 | 0 | 289.35 |
| campaign4_ood_goal_swap | runs/production_goal_swap_100ep_20260608/top_drawer_bowl/risk_topk8/risk_topk8 | libero_goal_swap | 3 | risk_topk8 | 100 | 8 | 92 | 0 | 295.53 |

### Smoke / Online Smoke / Test Runs

| Campaign | Run Directory | Suite | Task ID | Policy | Episodes | Success | Failure | Error | Mean Steps |
|---|---|---|---|---|---|---|---|---|---|
| campaign2_aggressive_task3 | runs/online_smoke/task3_aggressive/risk_topk8 | libero_goal_object | 3 | risk_topk8 | 2 | 0 | 1 | 1 | 150.00 |
| campaign2_aggressive_task3 | runs/online_smoke/task6_aggressive/risk_topk8 | libero_goal_object | 6 | risk_topk8 | 1 | 1 | 0 | 0 | 84.00 |
| campaign3_old_detector_task6 | runs/online_smoke/task6_aggressive_old_detector/risk_topk8 | libero_goal_object | 6 | risk_topk8 | 1 | 1 | 0 | 0 | 214.00 |

## 2. Config Sanity Audit

### Campaign: campaign1_risk_proof

**Run:** `runs/online/task3/original_simvla/shard_0/simvla_only`
- Suite: `libero_goal_object`
- Task ID: `3`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/online/task3/original_simvla/shard_1/simvla_only`
- Suite: `libero_goal_object`
- Task ID: `3`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/online/task3/original_h10_risk_base/shard_0/risk_base`
- Suite: `libero_goal_object`
- Task ID: `3`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6450968980789185, "q99": 0.9761446714401245}`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `risk_base`

**Run:** `runs/online/task3/original_h10_risk_base/shard_1/risk_base`
- Suite: `libero_goal_object`
- Task ID: `3`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6450968980789185, "q99": 0.9761446714401245}`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `risk_base`

**Run:** `runs/online/task3/modified_simvla/shard_0/simvla_only`
- Suite: `libero_goal_object`
- Task ID: `3`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/online/task3/modified_simvla/shard_1/simvla_only`
- Suite: `libero_goal_object`
- Task ID: `3`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8`
- Suite: `libero_goal_object`
- Task ID: `3`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6155413389205933, "q99": 0.9665935635566711}`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `risk_topk8`

**Run:** `runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8`
- Suite: `libero_goal_object`
- Task ID: `3`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6155413389205933, "q99": 0.9665935635566711}`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `risk_topk8`

**Run:** `runs/online/task6/original_simvla/shard_0/simvla_only`
- Suite: `libero_goal_object`
- Task ID: `6`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080923`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/online/task6/original_simvla/shard_1/simvla_only`
- Suite: `libero_goal_object`
- Task ID: `6`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080923`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/online/task6/original_h10_risk_base/shard_0/risk_base`
- Suite: `libero_goal_object`
- Task ID: `6`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6450968980789185, "q99": 0.9761446714401245}`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080923`, model_load_seed=`206080911`
- Policy Type: `risk_base`

**Run:** `runs/online/task6/original_h10_risk_base/shard_1/risk_base`
- Suite: `libero_goal_object`
- Task ID: `6`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6450968980789185, "q99": 0.9761446714401245}`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080923`, model_load_seed=`206080911`
- Policy Type: `risk_base`

**Run:** `runs/online/task6/modified_simvla/shard_0/simvla_only`
- Suite: `libero_goal_object`
- Task ID: `6`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080923`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/online/task6/modified_simvla/shard_1/simvla_only`
- Suite: `libero_goal_object`
- Task ID: `6`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080923`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8`
- Suite: `libero_goal_object`
- Task ID: `6`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6155413389205933, "q99": 0.9665935635566711}`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080923`, model_load_seed=`206080911`
- Policy Type: `risk_topk8`

**Run:** `runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8`
- Suite: `libero_goal_object`
- Task ID: `6`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6155413389205933, "q99": 0.9665935635566711}`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080923`, model_load_seed=`206080911`
- Policy Type: `risk_topk8`

**Run:** `runs/online/task8/original_simvla/shard_0/simvla_only`
- Suite: `libero_goal_object`
- Task ID: `8`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080925`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/online/task8/original_simvla/shard_1/simvla_only`
- Suite: `libero_goal_object`
- Task ID: `8`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080925`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/online/task8/original_h10_risk_base/shard_0/risk_base`
- Suite: `libero_goal_object`
- Task ID: `8`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6450968980789185, "q99": 0.9761446714401245}`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080925`, model_load_seed=`206080911`
- Policy Type: `risk_base`

**Run:** `runs/online/task8/original_h10_risk_base/shard_1/risk_base`
- Suite: `libero_goal_object`
- Task ID: `8`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6450968980789185, "q99": 0.9761446714401245}`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080925`, model_load_seed=`206080911`
- Policy Type: `risk_base`

**Run:** `runs/online/task8/modified_simvla/shard_0/simvla_only`
- Suite: `libero_goal_object`
- Task ID: `8`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080925`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/online/task8/modified_simvla/shard_1/simvla_only`
- Suite: `libero_goal_object`
- Task ID: `8`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080925`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/online/task8/modified_h10_risk_topk8/shard_0/risk_topk8`
- Suite: `libero_goal_object`
- Task ID: `8`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6155413389205933, "q99": 0.9665935635566711}`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080925`, model_load_seed=`206080911`
- Policy Type: `risk_topk8`

**Run:** `runs/online/task8/modified_h10_risk_topk8/shard_1/risk_topk8`
- Suite: `libero_goal_object`
- Task ID: `8`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`q95`, streak=`q95`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6155413389205933, "q99": 0.9665935635566711}`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080925`, model_load_seed=`206080911`
- Policy Type: `risk_topk8`

**Run:** `inputs/datasets/exact_200_chunk10/worker_0`
- Suite: `N/A`
- Task ID: `N/A`
- Task Language: `N/A`
- Model Checkpoint Path: `N/A`
- Detector Path: `N/A`
- Horizon Setting: `N/A`
- Threshold Settings (config): main=`N/A`, streak=`N/A`
- Reset Seeds count: `0`
- Seed Settings: global_action_seed=`N/A`, model_load_seed=`N/A`
- Policy Type: `N/A`

**Run:** `inputs/datasets/continuous_chunk10/worker_0`
- Suite: `N/A`
- Task ID: `N/A`
- Task Language: `N/A`
- Model Checkpoint Path: `/home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `N/A`
- Horizon Setting: `N/A`
- Threshold Settings (config): main=`N/A`, streak=`N/A`
- Reset Seeds count: `0`
- Seed Settings: global_action_seed=`N/A`, model_load_seed=`N/A`
- Policy Type: `N/A`

**Run:** `inputs/datasets/continuous_chunk10_flat/worker_0`
- Suite: `N/A`
- Task ID: `N/A`
- Task Language: `N/A`
- Model Checkpoint Path: `N/A`
- Detector Path: `N/A`
- Horizon Setting: `N/A`
- Threshold Settings (config): main=`N/A`, streak=`N/A`
- Reset Seeds count: `0`
- Seed Settings: global_action_seed=`N/A`, model_load_seed=`N/A`
- Policy Type: `N/A`

### Campaign: campaign2_aggressive_task3

**Run:** `runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8`
- Suite: `libero_goal_object`
- Task ID: `3`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`0.3`, streak=`0.3`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6155413389205933, "q99": 0.9665935635566711}`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `risk_topk8`

**Run:** `runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8`
- Suite: `libero_goal_object`
- Task ID: `3`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`0.3`, streak=`0.3`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6155413389205933, "q99": 0.9665935635566711}`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `risk_topk8`

**Run:** `runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8`
- Suite: `libero_goal_object`
- Task ID: `6`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`0.3`, streak=`0.3`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6155413389205933, "q99": 0.9665935635566711}`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080923`, model_load_seed=`206080911`
- Policy Type: `risk_topk8`

**Run:** `runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8`
- Suite: `libero_goal_object`
- Task ID: `6`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`0.3`, streak=`0.3`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6155413389205933, "q99": 0.9665935635566711}`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080923`, model_load_seed=`206080911`
- Policy Type: `risk_topk8`

### Campaign: campaign3_old_detector_task6

**Run:** `runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8`
- Suite: `libero_goal_object`
- Task ID: `6`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/dean_artifacts/current_dean_risk_models_20260602/all_tasks_full/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`0.3`, streak=`0.3`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.8500646352767944, "q99": 0.9937206506729126}`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080923`, model_load_seed=`206080911`
- Policy Type: `risk_topk8`

**Run:** `runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8`
- Suite: `libero_goal_object`
- Task ID: `6`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/dean_artifacts/current_dean_risk_models_20260602/all_tasks_full/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`0.3`, streak=`0.3`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.8500646352767944, "q99": 0.9937206506729126}`
- Reset Seeds count: `50`
- Seed Settings: global_action_seed=`206080923`, model_load_seed=`206080911`
- Policy Type: `risk_topk8`

### Campaign: campaign4_ood_goal_swap

**Run:** `runs/online/libero_goal_swap/top_drawer_bowl/original_simvla/simvla_only`
- Suite: `libero_goal_swap`
- Task ID: `3`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`1.0`, streak=`1.0`
- Reset Seeds count: `2`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/online/libero_goal_swap/top_drawer_bowl/risk_topk8/risk_topk8`
- Suite: `libero_goal_swap`
- Task ID: `3`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`0.3`, streak=`0.3`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6155413389205933, "q99": 0.9665935635566711}`
- Reset Seeds count: `2`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `risk_topk8`

**Run:** `runs/online/libero_goal_swap/top_drawer_bowl/modified_simvla/simvla_only`
- Suite: `libero_goal_swap`
- Task ID: `3`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`1.0`, streak=`1.0`
- Reset Seeds count: `2`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/online/libero_goal_swap/cream_cheese_bowl/original_simvla/simvla_only`
- Suite: `libero_goal_swap`
- Task ID: `6`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`1.0`, streak=`1.0`
- Reset Seeds count: `2`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/online/libero_goal_swap/cream_cheese_bowl/modified_simvla/simvla_only`
- Suite: `libero_goal_swap`
- Task ID: `6`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`1.0`, streak=`1.0`
- Reset Seeds count: `2`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/online/libero_goal_swap/cream_cheese_bowl/risk_topk8/risk_topk8`
- Suite: `libero_goal_swap`
- Task ID: `6`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`0.3`, streak=`0.3`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6155413389205933, "q99": 0.9665935635566711}`
- Reset Seeds count: `2`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `risk_topk8`

**Run:** `runs/online/libero_goal_swap/bowl_on_plate/original_simvla/simvla_only`
- Suite: `libero_goal_swap`
- Task ID: `8`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`1.0`, streak=`1.0`
- Reset Seeds count: `2`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/online/libero_goal_swap/bowl_on_plate/modified_simvla/simvla_only`
- Suite: `libero_goal_swap`
- Task ID: `8`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`1.0`, streak=`1.0`
- Reset Seeds count: `2`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/online/libero_goal_swap/bowl_on_plate/risk_topk8/risk_topk8`
- Suite: `libero_goal_swap`
- Task ID: `8`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`0.3`, streak=`0.3`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6155413389205933, "q99": 0.9665935635566711}`
- Reset Seeds count: `2`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `risk_topk8`

**Run:** `runs/production_goal_swap_100ep_20260608/top_drawer_bowl/original_simvla/simvla_only`
- Suite: `libero_goal_swap`
- Task ID: `3`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`1.0`, streak=`1.0`
- Reset Seeds count: `100`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/production_goal_swap_100ep_20260608/top_drawer_bowl/modified_simvla/simvla_only`
- Suite: `libero_goal_swap`
- Task ID: `3`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`1.0`, streak=`1.0`
- Reset Seeds count: `100`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/production_goal_swap_100ep_20260608/top_drawer_bowl/risk_topk8/risk_topk8`
- Suite: `libero_goal_swap`
- Task ID: `3`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`0.3`, streak=`0.3`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6155413389205933, "q99": 0.9665935635566711}`
- Reset Seeds count: `100`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `risk_topk8`

**Run:** `runs/production_goal_swap_100ep_20260608/cream_cheese_bowl/original_simvla/simvla_only`
- Suite: `libero_goal_swap`
- Task ID: `6`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`1.0`, streak=`1.0`
- Reset Seeds count: `100`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/production_goal_swap_100ep_20260608/cream_cheese_bowl/modified_simvla/simvla_only`
- Suite: `libero_goal_swap`
- Task ID: `6`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`1.0`, streak=`1.0`
- Reset Seeds count: `100`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/production_goal_swap_100ep_20260608/cream_cheese_bowl/risk_topk8/risk_topk8`
- Suite: `libero_goal_swap`
- Task ID: `6`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`0.3`, streak=`0.3`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6155413389205933, "q99": 0.9665935635566711}`
- Reset Seeds count: `100`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `risk_topk8`

**Run:** `runs/production_goal_swap_100ep_20260608/bowl_on_plate/original_simvla/simvla_only`
- Suite: `libero_goal_swap`
- Task ID: `8`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`1.0`, streak=`1.0`
- Reset Seeds count: `100`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/production_goal_swap_100ep_20260608/bowl_on_plate/modified_simvla/simvla_only`
- Suite: `libero_goal_swap`
- Task ID: `8`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`1.0`, streak=`1.0`
- Reset Seeds count: `100`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `simvla_only`

**Run:** `runs/production_goal_swap_100ep_20260608/bowl_on_plate/risk_topk8/risk_topk8`
- Suite: `libero_goal_swap`
- Task ID: `8`
- Task Language: `N/A`
- Model Checkpoint Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Horizon Setting: `10`
- Threshold Settings (config): main=`0.3`, streak=`0.3`
  - Conformal thresholds (from manifest): `{"conformal_mass": 0.15, "q95": 0.6155413389205933, "q99": 0.9665935635566711}`
- Reset Seeds count: `100`
- Seed Settings: global_action_seed=`206080920`, model_load_seed=`206080911`
- Policy Type: `risk_topk8`


## 3. Seed Parity Audit

### Campaign: campaign1_risk_proof

#### Task: `3`
- Policy `simvla_only_s0`: `50` seeds, `50` unique.
- Policy `simvla_only_s1`: `50` seeds, `50` unique.
- Policy `risk_base_s0`: `50` seeds, `50` unique.
- Policy `risk_base_s1`: `50` seeds, `50` unique.
- Policy `simvla_only_s0`: `50` seeds, `50` unique.
- Policy `simvla_only_s1`: `50` seeds, `50` unique.
- Policy `risk_topk8_s0`: `50` seeds, `50` unique.
- Policy `risk_topk8_s1`: `50` seeds, `50` unique.
  - **Cross-policy Seed Parity for shard_0:**
    - `simvla_only_s0` vs `risk_base_s0`: **PASS** (exact match and order)
    - `simvla_only_s0` vs `risk_topk8_s0`: **PASS** (exact match and order)
  - **Cross-policy Seed Parity for shard_1:**
    - `simvla_only_s1` vs `risk_base_s1`: **PASS** (exact match and order)
    - `simvla_only_s1` vs `risk_topk8_s1`: **PASS** (exact match and order)
  - **Cross-policy Seed Parity for all:**
    - `simvla_only_s0` vs `simvla_only_s1`: **FAIL**
      - In `simvla_only_s0` but not `simvla_only_s1` (first 10): `[1448376064, 798781185, 1034388353, 1285069188, 1799388041, 562990346, 2084640018, 1980476309, 1130719382, 1324848410]`
      - In `simvla_only_s1` but not `simvla_only_s0` (first 10): `[1127910528, 942896265, 54105097, 1411805069, 1689510033, 584199315, 2021907988, 211088021, 964738199, 669593880]`
    - `simvla_only_s0` vs `risk_base_s0`: **PASS** (exact match and order)
    - `simvla_only_s0` vs `risk_base_s1`: **FAIL**
      - In `simvla_only_s0` but not `risk_base_s1` (first 10): `[1448376064, 798781185, 1034388353, 1285069188, 1799388041, 562990346, 2084640018, 1980476309, 1130719382, 1324848410]`
      - In `risk_base_s1` but not `simvla_only_s0` (first 10): `[1127910528, 942896265, 54105097, 1411805069, 1689510033, 584199315, 2021907988, 211088021, 964738199, 669593880]`
    - `simvla_only_s0` vs `risk_topk8_s0`: **PASS** (exact match and order)
    - `simvla_only_s0` vs `risk_topk8_s1`: **FAIL**
      - In `simvla_only_s0` but not `risk_topk8_s1` (first 10): `[1448376064, 798781185, 1034388353, 1285069188, 1799388041, 562990346, 2084640018, 1980476309, 1130719382, 1324848410]`
      - In `risk_topk8_s1` but not `simvla_only_s0` (first 10): `[1127910528, 942896265, 54105097, 1411805069, 1689510033, 584199315, 2021907988, 211088021, 964738199, 669593880]`

#### Task: `6`
- Policy `simvla_only_s0`: `50` seeds, `50` unique.
- Policy `simvla_only_s1`: `50` seeds, `50` unique.
- Policy `risk_base_s0`: `50` seeds, `50` unique.
- Policy `risk_base_s1`: `50` seeds, `50` unique.
- Policy `simvla_only_s0`: `50` seeds, `50` unique.
- Policy `simvla_only_s1`: `50` seeds, `50` unique.
- Policy `risk_topk8_s0`: `50` seeds, `50` unique.
- Policy `risk_topk8_s1`: `50` seeds, `50` unique.
  - **Cross-policy Seed Parity for shard_0:**
    - `simvla_only_s0` vs `risk_base_s0`: **PASS** (exact match and order)
    - `simvla_only_s0` vs `risk_topk8_s0`: **PASS** (exact match and order)
  - **Cross-policy Seed Parity for shard_1:**
    - `simvla_only_s1` vs `risk_base_s1`: **PASS** (exact match and order)
    - `simvla_only_s1` vs `risk_topk8_s1`: **PASS** (exact match and order)
  - **Cross-policy Seed Parity for all:**
    - `simvla_only_s0` vs `simvla_only_s1`: **FAIL**
      - In `simvla_only_s0` but not `simvla_only_s1` (first 10): `[634248193, 352560642, 448048899, 212142211, 1165183492, 492767111, 107614348, 2142599694, 1771685116, 1026915864]`
      - In `simvla_only_s1` but not `simvla_only_s0` (first 10): `[143160192, 2099302537, 287547146, 1717619211, 288290959, 1001840528, 47766804, 251434644, 386737046, 84682135]`
    - `simvla_only_s0` vs `risk_base_s0`: **PASS** (exact match and order)
    - `simvla_only_s0` vs `risk_base_s1`: **FAIL**
      - In `simvla_only_s0` but not `risk_base_s1` (first 10): `[634248193, 352560642, 448048899, 212142211, 1165183492, 492767111, 107614348, 2142599694, 1771685116, 1026915864]`
      - In `risk_base_s1` but not `simvla_only_s0` (first 10): `[143160192, 2099302537, 287547146, 1717619211, 288290959, 1001840528, 47766804, 251434644, 386737046, 84682135]`
    - `simvla_only_s0` vs `risk_topk8_s0`: **PASS** (exact match and order)
    - `simvla_only_s0` vs `risk_topk8_s1`: **FAIL**
      - In `simvla_only_s0` but not `risk_topk8_s1` (first 10): `[634248193, 352560642, 448048899, 212142211, 1165183492, 492767111, 107614348, 2142599694, 1771685116, 1026915864]`
      - In `risk_topk8_s1` but not `simvla_only_s0` (first 10): `[143160192, 2099302537, 287547146, 1717619211, 288290959, 1001840528, 47766804, 251434644, 386737046, 84682135]`

#### Task: `8`
- Policy `simvla_only_s0`: `50` seeds, `50` unique.
- Policy `simvla_only_s1`: `50` seeds, `50` unique.
- Policy `risk_base_s0`: `50` seeds, `50` unique.
- Policy `risk_base_s1`: `50` seeds, `50` unique.
- Policy `simvla_only_s0`: `3` seeds, `3` unique.
- Policy `simvla_only_s1`: `2` seeds, `2` unique.
- Policy `risk_topk8_s0`: `1` seeds, `1` unique.
- Policy `risk_topk8_s1`: `1` seeds, `1` unique.
  - **Cross-policy Seed Parity for shard_0:**
    - `simvla_only_s0` vs `risk_base_s0`: **FAIL**
      - In `risk_base_s0` but not `simvla_only_s0` (first 10): `[720835593, 35383693, 610894479, 1827203343, 1059644433, 182364051, 28472471, 668985496, 229426715, 1937344412]`
    - `simvla_only_s0` vs `risk_topk8_s0`: **FAIL**
      - In `simvla_only_s0` but not `risk_topk8_s0` (first 10): `[1748468229, 228614271]`
  - **Cross-policy Seed Parity for shard_1:**
    - `simvla_only_s1` vs `risk_base_s1`: **FAIL**
      - In `risk_base_s1` but not `simvla_only_s1` (first 10): `[444833156, 1042449797, 701612810, 2097979917, 348780688, 1434999569, 1445361301, 124260902, 1928634409, 351686057]`
    - `simvla_only_s1` vs `risk_topk8_s1`: **FAIL**
      - In `simvla_only_s1` but not `risk_topk8_s1` (first 10): `[616823035]`
  - **Cross-policy Seed Parity for all:**
    - `simvla_only_s0` vs `simvla_only_s1`: **FAIL**
      - In `simvla_only_s0` but not `simvla_only_s1` (first 10): `[1748468229, 42431854, 228614271]`
      - In `simvla_only_s1` but not `simvla_only_s0` (first 10): `[901501224, 616823035]`
    - `simvla_only_s0` vs `risk_base_s0`: **FAIL**
      - In `risk_base_s0` but not `simvla_only_s0` (first 10): `[720835593, 35383693, 610894479, 1827203343, 1059644433, 182364051, 28472471, 668985496, 229426715, 1937344412]`
    - `simvla_only_s0` vs `risk_base_s1`: **FAIL**
      - In `simvla_only_s0` but not `risk_base_s1` (first 10): `[1748468229, 42431854, 228614271]`
      - In `risk_base_s1` but not `simvla_only_s0` (first 10): `[444833156, 1042449797, 701612810, 2097979917, 348780688, 1434999569, 1445361301, 124260902, 901501224, 1928634409]`
    - `simvla_only_s0` vs `risk_topk8_s0`: **FAIL**
      - In `simvla_only_s0` but not `risk_topk8_s0` (first 10): `[1748468229, 228614271]`
    - `simvla_only_s0` vs `risk_topk8_s1`: **FAIL**
      - In `simvla_only_s0` but not `risk_topk8_s1` (first 10): `[1748468229, 42431854, 228614271]`
      - In `risk_topk8_s1` but not `simvla_only_s0` (first 10): `[901501224]`

#### Task: `datasets`
- Policy `exact_200_chunk10`: `0` seeds, `0` unique.
- Policy `continuous_chunk10`: `0` seeds, `0` unique.
- Policy `continuous_chunk10_flat`: `0` seeds, `0` unique.
  - **Cross-policy Seed Parity for all:**
    - `exact_200_chunk10` vs `continuous_chunk10`: **PASS** (exact match and order)
    - `exact_200_chunk10` vs `continuous_chunk10_flat`: **PASS** (exact match and order)

### Campaign: campaign2_aggressive_task3

#### Task: `3`
- Policy `risk_topk8_s1`: `50` seeds, `50` unique.
- Policy `risk_topk8_s0`: `50` seeds, `50` unique.
  - **Cross-policy Seed Parity for all:**
    - `risk_topk8_s1` vs `risk_topk8_s0`: **FAIL**
      - In `risk_topk8_s1` but not `risk_topk8_s0` (first 10): `[1127910528, 942896265, 54105097, 1411805069, 1689510033, 584199315, 2021907988, 211088021, 964738199, 669593880]`
      - In `risk_topk8_s0` but not `risk_topk8_s1` (first 10): `[1448376064, 798781185, 1034388353, 1285069188, 1799388041, 562990346, 2084640018, 1980476309, 1130719382, 1324848410]`

#### Task: `6`
- Policy `risk_topk8_s0`: `50` seeds, `50` unique.
- Policy `risk_topk8_s1`: `50` seeds, `50` unique.
  - **Cross-policy Seed Parity for all:**
    - `risk_topk8_s0` vs `risk_topk8_s1`: **FAIL**
      - In `risk_topk8_s0` but not `risk_topk8_s1` (first 10): `[634248193, 352560642, 448048899, 212142211, 1165183492, 492767111, 107614348, 2142599694, 1771685116, 1026915864]`
      - In `risk_topk8_s1` but not `risk_topk8_s0` (first 10): `[143160192, 2099302537, 287547146, 1717619211, 288290959, 1001840528, 47766804, 251434644, 386737046, 84682135]`

### Campaign: campaign3_old_detector_task6

#### Task: `6`
- Policy `risk_topk8_s1`: `50` seeds, `50` unique.
- Policy `risk_topk8_s0`: `50` seeds, `50` unique.
  - **Cross-policy Seed Parity for all:**
    - `risk_topk8_s1` vs `risk_topk8_s0`: **FAIL**
      - In `risk_topk8_s1` but not `risk_topk8_s0` (first 10): `[143160192, 2099302537, 287547146, 1717619211, 288290959, 1001840528, 47766804, 251434644, 386737046, 84682135]`
      - In `risk_topk8_s0` but not `risk_topk8_s1` (first 10): `[634248193, 352560642, 448048899, 212142211, 1165183492, 492767111, 107614348, 2142599694, 1771685116, 1026915864]`

### Campaign: campaign4_ood_goal_swap

#### Task: `3`
- Policy `simvla_only`: `4` seeds, `2` unique.
  - **WARNING:** Duplicated seeds found: `[12345, 67890]`
- Policy `risk_topk8`: `2` seeds, `2` unique.
- Policy `simvla_only`: `2` seeds, `2` unique.
- Policy `simvla_only`: `100` seeds, `100` unique.
- Policy `simvla_only`: `100` seeds, `100` unique.
- Policy `risk_topk8`: `100` seeds, `100` unique.
  - **Cross-policy Seed Parity for all:**
    - `simvla_only` vs `risk_topk8`: **PASS** (exact match and order)

#### Task: `6`
- Policy `simvla_only`: `2` seeds, `2` unique.
- Policy `simvla_only`: `2` seeds, `2` unique.
- Policy `risk_topk8`: `2` seeds, `2` unique.
- Policy `simvla_only`: `100` seeds, `100` unique.
- Policy `simvla_only`: `100` seeds, `100` unique.
- Policy `risk_topk8`: `100` seeds, `100` unique.
  - **Cross-policy Seed Parity for all:**
    - `simvla_only` vs `risk_topk8`: **PASS** (exact match and order)

#### Task: `8`
- Policy `simvla_only`: `2` seeds, `2` unique.
- Policy `simvla_only`: `2` seeds, `2` unique.
- Policy `risk_topk8`: `2` seeds, `2` unique.
- Policy `simvla_only`: `100` seeds, `100` unique.
- Policy `simvla_only`: `100` seeds, `100` unique.
- Policy `risk_topk8`: `100` seeds, `100` unique.
  - **Cross-policy Seed Parity for all:**
    - `simvla_only` vs `risk_topk8`: **PASS** (exact match and order)

## 4. Horizon and Execution Semantics

From config inspection, the execution horizon is explicitly set to `10` (H10) across all policies.
Let's audit whether step counts match horizon boundaries (e.g. env steps should be multiples of 10 plus terminal truncation, or success truncation).
Let's look at steps of failed episodes (which run to timeout/limit unless they fail early or succeed).
For failed episodes, if the timeout is 300 steps, we expect the number of steps to be exactly 300 if execution horizon doesn't truncate, or we expect steps to be a multiple of 10 if chunk execution is correct.
Let's check the step count distributions for failed episodes in production runs:

- Run: `runs/online/task3/original_simvla/shard_0/simvla_only` | Mean Steps (All): `293.64` | Success Mean Steps: `236.40` | Failure Mean Steps: `300.00`
- Run: `runs/online/task3/original_simvla/shard_1/simvla_only` | Mean Steps (All): `286.52` | Success Mean Steps: `203.71` | Failure Mean Steps: `300.00`
- Run: `runs/online/task3/original_h10_risk_base/shard_0/risk_base` | Mean Steps (All): `293.64` | Success Mean Steps: `236.40` | Failure Mean Steps: `300.00`
- Run: `runs/online/task3/original_h10_risk_base/shard_1/risk_base` | Mean Steps (All): `286.64` | Success Mean Steps: `204.57` | Failure Mean Steps: `300.00`
- Run: `runs/online/task3/modified_simvla/shard_0/simvla_only` | Mean Steps (All): `278.06` | Success Mean Steps: `178.11` | Failure Mean Steps: `300.00`
- Run: `runs/online/task3/modified_simvla/shard_1/simvla_only` | Mean Steps (All): `278.14` | Success Mean Steps: `163.38` | Failure Mean Steps: `300.00`
- Run: `runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8` | Mean Steps (All): `278.10` | Success Mean Steps: `178.33` | Failure Mean Steps: `300.00`
- Run: `runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8` | Mean Steps (All): `278.14` | Success Mean Steps: `163.38` | Failure Mean Steps: `300.00`
- Run: `runs/online/task6/original_simvla/shard_0/simvla_only` | Mean Steps (All): `205.46` | Success Mean Steps: `131.18` | Failure Mean Steps: `300.00`
- Run: `runs/online/task6/original_simvla/shard_1/simvla_only` | Mean Steps (All): `206.54` | Success Mean Steps: `113.08` | Failure Mean Steps: `300.00`
- Run: `runs/online/task6/original_h10_risk_base/shard_0/risk_base` | Mean Steps (All): `208.06` | Success Mean Steps: `129.74` | Failure Mean Steps: `300.00`
- Run: `runs/online/task6/original_h10_risk_base/shard_1/risk_base` | Mean Steps (All): `209.08` | Success Mean Steps: `110.58` | Failure Mean Steps: `300.00`
- Run: `runs/online/task6/modified_simvla/shard_0/simvla_only` | Mean Steps (All): `195.96` | Success Mean Steps: `132.19` | Failure Mean Steps: `300.00`
- Run: `runs/online/task6/modified_simvla/shard_1/simvla_only` | Mean Steps (All): `205.58` | Success Mean Steps: `118.42` | Failure Mean Steps: `300.00`
- Run: `runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8` | Mean Steps (All): `195.82` | Success Mean Steps: `120.38` | Failure Mean Steps: `300.00`
- Run: `runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8` | Mean Steps (All): `200.12` | Success Mean Steps: `121.64` | Failure Mean Steps: `300.00`
- Run: `runs/online/task8/original_simvla/shard_0/simvla_only` | Mean Steps (All): `114.34` | Success Mean Steps: `89.02` | Failure Mean Steps: `300.00`
- Run: `runs/online/task8/original_simvla/shard_1/simvla_only` | Mean Steps (All): `101.30` | Success Mean Steps: `88.62` | Failure Mean Steps: `300.00`
- Run: `runs/online/task8/original_h10_risk_base/shard_0/risk_base` | Mean Steps (All): `116.60` | Success Mean Steps: `86.74` | Failure Mean Steps: `300.00`
- Run: `runs/online/task8/original_h10_risk_base/shard_1/risk_base` | Mean Steps (All): `97.24` | Success Mean Steps: `88.79` | Failure Mean Steps: `300.00`
- Run: `runs/online/task8/modified_simvla/shard_0/simvla_only` | Mean Steps (All): `67.67` | Success Mean Steps: `67.67` | Failure Mean Steps: `0.00`
- Run: `runs/online/task8/modified_simvla/shard_1/simvla_only` | Mean Steps (All): `125.50` | Success Mean Steps: `125.50` | Failure Mean Steps: `0.00`
- Run: `runs/online/task8/modified_h10_risk_topk8/shard_0/risk_topk8` | Mean Steps (All): `73.00` | Success Mean Steps: `73.00` | Failure Mean Steps: `0.00`
- Run: `runs/online/task8/modified_h10_risk_topk8/shard_1/risk_topk8` | Mean Steps (All): `72.00` | Success Mean Steps: `72.00` | Failure Mean Steps: `0.00`
- Run: `inputs/datasets/exact_200_chunk10/worker_0` | Mean Steps (All): `0.00` | Success Mean Steps: `0.00` | Failure Mean Steps: `0.00`
- Run: `inputs/datasets/continuous_chunk10/worker_0` | Mean Steps (All): `0.00` | Success Mean Steps: `0.00` | Failure Mean Steps: `0.00`
- Run: `inputs/datasets/continuous_chunk10_flat/worker_0` | Mean Steps (All): `131.69` | Success Mean Steps: `102.93` | Failure Mean Steps: `250.00`
- Run: `runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8` | Mean Steps (All): `277.10` | Success Mean Steps: `172.78` | Failure Mean Steps: `300.00`
- Run: `runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8` | Mean Steps (All): `276.28` | Success Mean Steps: `181.40` | Failure Mean Steps: `300.00`
- Run: `runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8` | Mean Steps (All): `188.78` | Success Mean Steps: `131.48` | Failure Mean Steps: `300.00`
- Run: `runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8` | Mean Steps (All): `192.10` | Success Mean Steps: `113.97` | Failure Mean Steps: `300.00`
- Run: `runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8` | Mean Steps (All): `207.02` | Success Mean Steps: `127.81` | Failure Mean Steps: `300.00`
- Run: `runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8` | Mean Steps (All): `182.62` | Success Mean Steps: `122.15` | Failure Mean Steps: `300.00`
- Run: `runs/online/libero_goal_swap/top_drawer_bowl/original_simvla/simvla_only` | Mean Steps (All): `150.00` | Success Mean Steps: `0.00` | Failure Mean Steps: `300.00`
- Run: `runs/online/libero_goal_swap/top_drawer_bowl/risk_topk8/risk_topk8` | Mean Steps (All): `300.00` | Success Mean Steps: `0.00` | Failure Mean Steps: `300.00`
- Run: `runs/online/libero_goal_swap/top_drawer_bowl/modified_simvla/simvla_only` | Mean Steps (All): `300.00` | Success Mean Steps: `0.00` | Failure Mean Steps: `300.00`
- Run: `runs/online/libero_goal_swap/cream_cheese_bowl/original_simvla/simvla_only` | Mean Steps (All): `300.00` | Success Mean Steps: `0.00` | Failure Mean Steps: `300.00`
- Run: `runs/online/libero_goal_swap/cream_cheese_bowl/modified_simvla/simvla_only` | Mean Steps (All): `300.00` | Success Mean Steps: `0.00` | Failure Mean Steps: `300.00`
- Run: `runs/online/libero_goal_swap/cream_cheese_bowl/risk_topk8/risk_topk8` | Mean Steps (All): `300.00` | Success Mean Steps: `0.00` | Failure Mean Steps: `300.00`
- Run: `runs/online/libero_goal_swap/bowl_on_plate/original_simvla/simvla_only` | Mean Steps (All): `300.00` | Success Mean Steps: `0.00` | Failure Mean Steps: `300.00`
- Run: `runs/online/libero_goal_swap/bowl_on_plate/modified_simvla/simvla_only` | Mean Steps (All): `300.00` | Success Mean Steps: `0.00` | Failure Mean Steps: `300.00`
- Run: `runs/online/libero_goal_swap/bowl_on_plate/risk_topk8/risk_topk8` | Mean Steps (All): `300.00` | Success Mean Steps: `0.00` | Failure Mean Steps: `300.00`
- Run: `runs/production_goal_swap_100ep_20260608/top_drawer_bowl/original_simvla/simvla_only` | Mean Steps (All): `289.35` | Success Mean Steps: `229.00` | Failure Mean Steps: `300.00`
- Run: `runs/production_goal_swap_100ep_20260608/top_drawer_bowl/modified_simvla/simvla_only` | Mean Steps (All): `294.16` | Success Mean Steps: `235.11` | Failure Mean Steps: `300.00`
- Run: `runs/production_goal_swap_100ep_20260608/top_drawer_bowl/risk_topk8/risk_topk8` | Mean Steps (All): `295.53` | Success Mean Steps: `244.12` | Failure Mean Steps: `300.00`
- Run: `runs/production_goal_swap_100ep_20260608/cream_cheese_bowl/original_simvla/simvla_only` | Mean Steps (All): `300.00` | Success Mean Steps: `0.00` | Failure Mean Steps: `300.00`
- Run: `runs/production_goal_swap_100ep_20260608/cream_cheese_bowl/modified_simvla/simvla_only` | Mean Steps (All): `300.00` | Success Mean Steps: `0.00` | Failure Mean Steps: `300.00`
- Run: `runs/production_goal_swap_100ep_20260608/cream_cheese_bowl/risk_topk8/risk_topk8` | Mean Steps (All): `300.00` | Success Mean Steps: `0.00` | Failure Mean Steps: `300.00`
- Run: `runs/production_goal_swap_100ep_20260608/bowl_on_plate/original_simvla/simvla_only` | Mean Steps (All): `299.63` | Success Mean Steps: `263.00` | Failure Mean Steps: `300.00`
- Run: `runs/production_goal_swap_100ep_20260608/bowl_on_plate/modified_simvla/simvla_only` | Mean Steps (All): `297.52` | Success Mean Steps: `217.33` | Failure Mean Steps: `300.00`
- Run: `runs/production_goal_swap_100ep_20260608/bowl_on_plate/risk_topk8/risk_topk8` | Mean Steps (All): `298.51` | Success Mean Steps: `225.50` | Failure Mean Steps: `300.00`

Wait, let's verify if failed episodes have exactly 300 steps or if they deviate.
In Campaign 1 and others, the failure mean steps are exactly `300.0` or close to it, which indicates failed episodes ran for the full limit of 300 steps.
Let's check if there are any failed episodes that have non-300 step counts. This would indicate early termination on failure (which might be normal if `done` is returned by the env, or abnormal if there is a bug).

## 5. Success Semantics Audit

From runner code inspection (`run_policy_matrix.py`):
- Success is checked via two methods:
  1. Environment reward: `reward_success = bool(float(rew) > 0.0)`
  2. Explicit environment check: `checked_success = check_success(env)`
  - These are combined: `success = success or reward_success or bool(checked_success)`
- Let's check if there are 0-step or error rows in production runs:

- `runs/online/task3/original_simvla/shard_0/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task3/original_simvla/shard_1/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task3/original_h10_risk_base/shard_0/risk_base`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task3/original_h10_risk_base/shard_1/risk_base`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task3/modified_simvla/shard_0/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task3/modified_simvla/shard_1/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task6/original_simvla/shard_0/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task6/original_simvla/shard_1/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task6/original_h10_risk_base/shard_0/risk_base`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task6/original_h10_risk_base/shard_1/risk_base`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task6/modified_simvla/shard_0/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task6/modified_simvla/shard_1/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task8/original_simvla/shard_0/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task8/original_simvla/shard_1/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task8/original_h10_risk_base/shard_0/risk_base`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task8/original_h10_risk_base/shard_1/risk_base`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task8/modified_simvla/shard_0/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task8/modified_simvla/shard_1/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task8/modified_h10_risk_topk8/shard_0/risk_topk8`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task8/modified_h10_risk_topk8/shard_1/risk_topk8`: PASS (0 zero-step episodes, 0 error episodes)
- **WARNING** in `inputs/datasets/exact_200_chunk10/worker_0`: `200` zero-step episodes, `0` error episodes.
- **WARNING** in `inputs/datasets/continuous_chunk10/worker_0`: `17409` zero-step episodes, `0` error episodes.
- `inputs/datasets/continuous_chunk10_flat/worker_0`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8`: PASS (0 zero-step episodes, 0 error episodes)
- **WARNING** in `runs/online/libero_goal_swap/top_drawer_bowl/original_simvla/simvla_only`: `2` zero-step episodes, `2` error episodes.
- `runs/online/libero_goal_swap/top_drawer_bowl/risk_topk8/risk_topk8`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/libero_goal_swap/top_drawer_bowl/modified_simvla/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/libero_goal_swap/cream_cheese_bowl/original_simvla/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/libero_goal_swap/cream_cheese_bowl/modified_simvla/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/libero_goal_swap/cream_cheese_bowl/risk_topk8/risk_topk8`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/libero_goal_swap/bowl_on_plate/original_simvla/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/libero_goal_swap/bowl_on_plate/modified_simvla/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/online/libero_goal_swap/bowl_on_plate/risk_topk8/risk_topk8`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/production_goal_swap_100ep_20260608/top_drawer_bowl/original_simvla/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/production_goal_swap_100ep_20260608/top_drawer_bowl/modified_simvla/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/production_goal_swap_100ep_20260608/top_drawer_bowl/risk_topk8/risk_topk8`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/production_goal_swap_100ep_20260608/cream_cheese_bowl/original_simvla/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/production_goal_swap_100ep_20260608/cream_cheese_bowl/modified_simvla/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/production_goal_swap_100ep_20260608/cream_cheese_bowl/risk_topk8/risk_topk8`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/production_goal_swap_100ep_20260608/bowl_on_plate/original_simvla/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/production_goal_swap_100ep_20260608/bowl_on_plate/modified_simvla/simvla_only`: PASS (0 zero-step episodes, 0 error episodes)
- `runs/production_goal_swap_100ep_20260608/bowl_on_plate/risk_topk8/risk_topk8`: PASS (0 zero-step episodes, 0 error episodes)

## 6. Model Identity Audit

Let's summarize the checkpoints used in each campaign:

### Campaign: campaign1_risk_proof
- Policy: `simvla_only`
  - Checkpoint: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
  - Expected Checkpoint SHA256: `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`
  - Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Policy: `risk_topk8`
  - Checkpoint: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
  - Expected Checkpoint SHA256: `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`
  - Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Policy: `N/A`
  - Checkpoint: `N/A`
  - Expected Checkpoint SHA256: `N/A`
  - Detector Path: `N/A`
- Policy: `N/A`
  - Checkpoint: `/home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000`
  - Expected Checkpoint SHA256: `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`
  - Detector Path: `N/A`
- Policy: `simvla_only`
  - Checkpoint: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
  - Expected Checkpoint SHA256: `9d3b1767773da86906d771b1eca2c2911087371bf8b3890a7336b6773270f6be`
  - Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Policy: `risk_base`
  - Checkpoint: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
  - Expected Checkpoint SHA256: `9d3b1767773da86906d771b1eca2c2911087371bf8b3890a7336b6773270f6be`
  - Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
### Campaign: campaign2_aggressive_task3
- Policy: `risk_topk8`
  - Checkpoint: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
  - Expected Checkpoint SHA256: `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`
  - Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
### Campaign: campaign3_old_detector_task6
- Policy: `risk_topk8`
  - Checkpoint: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
  - Expected Checkpoint SHA256: `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`
  - Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/dean_artifacts/current_dean_risk_models_20260602/all_tasks_full/unc_topk8`
### Campaign: campaign4_ood_goal_swap
- Policy: `risk_topk8`
  - Checkpoint: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
  - Expected Checkpoint SHA256: `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`
  - Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Policy: `simvla_only`
  - Checkpoint: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
  - Expected Checkpoint SHA256: `9d3b1767773da86906d771b1eca2c2911087371bf8b3890a7336b6773270f6be`
  - Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Policy: `simvla_only`
  - Checkpoint: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000`
  - Expected Checkpoint SHA256: `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`
  - Detector Path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`

## 7. Detector Training and Data Leakage Audit

### Split Allocations (from bucket_counts.json):

| Bucket Name | Episodes |
|---|---|
| failure_eval_ood | 0 |
| failure_test_seen | 0 |
| failure_train_seen | 2724 |
| failure_val_seen | 680 |
| success_calib_seen | 1400 |
| success_test_ood | 0 |
| success_test_seen | 0 |
| success_train_seen | 11205 |
| success_val_seen | 1400 |

### Task Distribution in Training/Val/Calib Buckets:

| Bucket Name | Task 3 count | Task 6 count | Task 8 count | Other Tasks |
|---|---|---|---|---|
| failure_eval_ood | 0 | 0 | 0 | {} |
| failure_test_seen | 0 | 0 | 0 | {} |
| failure_train_seen | 1309 | 653 | 106 | {'4': 208, '0': 191, '9': 211, '1': 33, '5': 12, '2': 1} |
| failure_val_seen | 355 | 137 | 30 | {'4': 62, '0': 32, '9': 51, '1': 8, '2': 1, '5': 3, '7': 1} |
| success_calib_seen | 11 | 88 | 143 | {'0': 157, '4': 134, '7': 182, '9': 184, '5': 155, '2': 178, '1': 168} |
| success_test_ood | 0 | 0 | 0 | {} |
| success_test_seen | 0 | 0 | 0 | {} |
| success_train_seen | 59 | 770 | 1307 | {'0': 1207, '7': 1392, '9': 1156, '1': 1351, '5': 1385, '2': 1388, '4': 1190} |
| success_val_seen | 7 | 93 | 155 | {'4': 147, '2': 173, '5': 185, '9': 139, '0': 154, '7': 166, '1': 181} |

### Seed Leakage Check:

Let's compare the seeds used in the online evaluation of Task 3, 6, 8 with the seeds present in the training/validation/calibration buckets.
We want to know if evaluation seeds for a task appear in the training data for that same task.

#### Task `3`: `100` unique evaluation seeds
- Bucket `failure_eval_ood` has `0` seeds for Task `3`. Overlap with evaluation: `0` seeds.
- Bucket `failure_test_seen` has `0` seeds for Task `3`. Overlap with evaluation: `0` seeds.
- Bucket `failure_train_seen` has `1309` seeds for Task `3`. Overlap with evaluation: `0` seeds.
- Bucket `failure_val_seen` has `355` seeds for Task `3`. Overlap with evaluation: `0` seeds.
- Bucket `success_calib_seen` has `11` seeds for Task `3`. Overlap with evaluation: `0` seeds.
- Bucket `success_test_ood` has `0` seeds for Task `3`. Overlap with evaluation: `0` seeds.
- Bucket `success_test_seen` has `0` seeds for Task `3`. Overlap with evaluation: `0` seeds.
- Bucket `success_train_seen` has `59` seeds for Task `3`. Overlap with evaluation: `0` seeds.
- Bucket `success_val_seen` has `7` seeds for Task `3`. Overlap with evaluation: `0` seeds.

#### Task `6`: `100` unique evaluation seeds
- Bucket `failure_eval_ood` has `0` seeds for Task `6`. Overlap with evaluation: `0` seeds.
- Bucket `failure_test_seen` has `0` seeds for Task `6`. Overlap with evaluation: `0` seeds.
- Bucket `failure_train_seen` has `653` seeds for Task `6`. Overlap with evaluation: `0` seeds.
- Bucket `failure_val_seen` has `137` seeds for Task `6`. Overlap with evaluation: `0` seeds.
- Bucket `success_calib_seen` has `88` seeds for Task `6`. Overlap with evaluation: `0` seeds.
- Bucket `success_test_ood` has `0` seeds for Task `6`. Overlap with evaluation: `0` seeds.
- Bucket `success_test_seen` has `0` seeds for Task `6`. Overlap with evaluation: `0` seeds.
- Bucket `success_train_seen` has `770` seeds for Task `6`. Overlap with evaluation: `0` seeds.
- Bucket `success_val_seen` has `93` seeds for Task `6`. Overlap with evaluation: `0` seeds.

#### Task `8`: `100` unique evaluation seeds
- Bucket `failure_eval_ood` has `0` seeds for Task `8`. Overlap with evaluation: `0` seeds.
- Bucket `failure_test_seen` has `0` seeds for Task `8`. Overlap with evaluation: `0` seeds.
- Bucket `failure_train_seen` has `106` seeds for Task `8`. Overlap with evaluation: `0` seeds.
- Bucket `failure_val_seen` has `30` seeds for Task `8`. Overlap with evaluation: `0` seeds.
- Bucket `success_calib_seen` has `143` seeds for Task `8`. Overlap with evaluation: `0` seeds.
- Bucket `success_test_ood` has `0` seeds for Task `8`. Overlap with evaluation: `0` seeds.
- Bucket `success_test_seen` has `0` seeds for Task `8`. Overlap with evaluation: `0` seeds.
- Bucket `success_train_seen` has `1307` seeds for Task `8`. Overlap with evaluation: `0` seeds.
- Bucket `success_val_seen` has `155` seeds for Task `8`. Overlap with evaluation: `0` seeds.

## 8. Aggressive Threshold Audit

Let's confirm the results for the aggressive TopK8 campaigns:

### Campaign 2 (Aggressive TopK8 Task 3 Campaign):

#### Task 3:
- Shard: `runs/online/task3/modified_h10_risk_topk8/shard_1/risk_topk8` | Total: `50` | Success: `9`
- Shard: `runs/online/task3/modified_h10_risk_topk8/shard_0/risk_topk8` | Total: `50` | Success: `10`
- **Total Aggressive Task 3 Success:** `19/100` (Success rate: `19.00%`)

#### Task 6:
- Shard: `runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8` | Total: `50` | Success: `33`
- Shard: `runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8` | Total: `50` | Success: `29`
- **Total Aggressive Task 6 Success:** `62/100` (Success rate: `62.00%`)

### Campaign 3 (Old Detector Task 6):
- Shard: `runs/online/task6/modified_h10_risk_topk8/shard_1/risk_topk8` | Total: `50` | Success: `27`
- Shard: `runs/online/task6/modified_h10_risk_topk8/shard_0/risk_topk8` | Total: `50` | Success: `33`
- **Total Old Detector Task 6 Success:** `60/100` (Success rate: `60.00%`)

## 9. Suspicious Findings and Log Issues

### Campaign: campaign1_risk_proof
Found `6` log issues:
1. File: `logs/online_supervisor.log` (line 1) | Label: **Traceback found**
   - Snippet: `Traceback (most recent call last):`
2. File: `logs/online_supervisor.log` (line 14) | Label: **KeyboardInterrupt found**
   - Snippet: `KeyboardInterrupt`
3. File: `logs/online/prod_task8_modified_simvla_s0.log` (line 20) | Label: **Traceback found**
   - Snippet: `Traceback (most recent call last):`
4. File: `logs/online/prod_task8_modified_simvla_s0.log` (line 31) | Label: **KeyboardInterrupt found**
   - Snippet: `KeyboardInterrupt`
5. File: `logs/online/prod_task8_modified_simvla_s1.log` (line 18) | Label: **Traceback found**
   - Snippet: `Traceback (most recent call last):`
6. File: `logs/online/prod_task8_modified_simvla_s1.log` (line 27) | Label: **KeyboardInterrupt found**
   - Snippet: `KeyboardInterrupt`

### Campaign: campaign2_aggressive_task3
No issues found in logs.

### Campaign: campaign3_old_detector_task6
No issues found in logs.

### Campaign: campaign4_ood_goal_swap
No issues found in logs.

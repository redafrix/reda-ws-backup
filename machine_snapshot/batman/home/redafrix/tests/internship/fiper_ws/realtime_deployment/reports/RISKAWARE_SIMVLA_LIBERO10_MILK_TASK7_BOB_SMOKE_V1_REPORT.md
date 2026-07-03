# Smoke Test Report: Risk-Aware SimVLA on Bob (Task 7)

## 1. Process/GPU/RAM/Disk Status Before Run
- **GPU Status:**
  - NVIDIA GeForce RTX 4060 Laptop GPU (Driver Version: 580.95.05, CUDA Version: 13.0)
  - Memory Usage: 15MiB / 8188MiB (0% usage by active computation)
  - GPU Utilization: 19%
- **RAM Status:**
  - Total Memory: 30 GiB
  - Used Memory: 10 GiB
  - Available Memory: 18 GiB
- **Disk Space (Bob root filesystem):**
  - `/dev/nvme0n1p5` mounted on `/`
  - Size: 306.8 GB (Used: 246 GB, Available: 41 GB, Use: 86%)
- **Active Processes Check:**
  - Checked: `ps aux | grep -E 'run_clean|collect_fiper|simvla|python3'`
  - Result: No conflicting or active processes running on Bob.

## 2. Risk Model Path Selection
- **Selected Job Dir:** `experiments/current_baseline_v2_018_20260528/00_global_main/jobs/v2_018_transformer_k16`
- **Trained/Calibrated Detector Directory:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiments/current_baseline_v2_018_20260528/00_global_main/jobs/v2_018_transformer_k16`
- **Fallback Detector Directory (OOD):** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiments/current_baseline_v2_018_20260528/01_ood_task_8_9/jobs/v2_018_transformer_k16`
- **Normalization Statistics Artifact Generation:**
  - Plotted and computed standardizers (`h_stats`, `a_stats`, `st_stats`) using the training splits (`success_train_seen` and `failure_train_seen`) directly from raw data on Bob without utilizing test data or re-training.
  - Successfully generated and saved `normalization.json` under `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiments/current_baseline_v2_018_20260528/00_global_main/jobs/v2_018_transformer_k16/normalization.json` and fallback paths.

## 3. Deployment Artifacts Audit
- **ALL DEPLOYMENT ARTIFACTS EXIST:** **YES**
- **Detail:** `model.pt`, `config.json`, `FEATURE_AUDIT.json`, `thresholds.json`, and the newly generated `normalization.json` are now fully present in the job directory.

## 4. Exact Files Created / Configured
- **Smoke Config File:**
  - `realtime_deployment/configs/riskaware_simvla_libero10_milk_task7_bob_smoke_v1.json`
- **Deployment Python Script:**
  - `realtime_deployment/scripts/run_riskaware_simvla_one_task_v1.py`
- **Run Directory & Logs:**
  - Output Dir: `realtime_deployment/runs/riskaware_simvla_libero10_milk_task7_bob_smoke_v1`
  - Log File: `realtime_deployment/runs/riskaware_simvla_libero10_milk_task7_bob_smoke_v1/logs/smoke.log`
  - Summary File: `realtime_deployment/runs/riskaware_simvla_libero10_milk_task7_bob_smoke_v1/episode_summary.json`
  - Step Scores JSONL: `realtime_deployment/runs/riskaware_simvla_libero10_milk_task7_bob_smoke_v1/step_scores.jsonl`

## 5. Exact Command Run
```bash
cd "/media/rootalkhatib/My Passport/reda_ws/fiper_ws"
source ../asynchvla_ws/scripts/activate_simvla_bob.sh
python3 realtime_deployment/scripts/run_riskaware_simvla_one_task_v1.py \
  --config realtime_deployment/configs/riskaware_simvla_libero10_milk_task7_bob_smoke_v1.json \
  --num-episodes 1 \
  --worker-id smoke \
  > realtime_deployment/runs/riskaware_simvla_libero10_milk_task7_bob_smoke_v1/logs/smoke.log 2>&1
```

## 6. Episode Result & Timestep Metrics
- **Episode Result:** `success`
- **Number of Timesteps:** `267`
- **Risk Score Range (Min/Mean/Max):** `0.1004 / 0.5987 / 0.9947`
- **Alarm Count:** `264` (Breaches at step 3, conformal mass continues accumulating above 0.15)
- **First Alarm Timestep:** `3`

## 7. Seed Validation Statistics
- **SEED_UNIQUENESS_ENFORCED:** **YES**
- **TIMESTEPS_SEED_CHECKED:** **267**
- **SEED_COLLISIONS:** **0**
- **MAIN_SEED_COLLISIONS_WITH_ACE:** **0**
- **ACTION_MODIFICATION_ENABLED:** **NO** (passive monitoring only)

## 8. Configuration Confirmations
```text
MODEL = v2_018_transformer_k16
SUITE = libero_10_with_milk
TASK_ID = 7
EPISODES_RUN = 1
ACE_CANDIDATE_COUNT = 8
ACTION_SELECTION_POLICY = passive_monitor_only
ACTIONS_MODIFIED = NO
EXTRA_CANDIDATES_USED_FOR_ACE = YES
TRAINING_LAUNCHED = NO
FULL_RUN_LAUNCHED = NO
MISSING_DEPLOYMENT_ARTIFACTS = NO
SMOKE_PASS = YES
```

***

# Sam Baseline Run Seeds Update & Relaunch

## 1. Seeds & Config Setup
- **RESET_SEEDS_RANDOM_UNIQUE:** **YES**
- **RESET_SEED_RNG_SEED:** `20260528`
- **RESET_SEQUENTIAL_RANGE_USED:** **NO** (discarded range 10000..10099)
- **Exact Reset Seed List:**
```json
[
  889528444, 1869585543, 222736063, 712704968, 1559319872, 1370034125, 1681172831,
  1468778042, 1462228070, 430311902, 1858339168, 1000843407, 1087826667, 28988984,
  1853458601, 1597141723, 30405057, 8875216, 1338331430, 851425259, 1927867320,
  882332360, 592539777, 961587619, 2125793409, 2066021479, 898826943, 121193683,
  1066716213, 748443181, 2103798454, 362935916, 1694066566, 1366835203, 583476408,
  889729065, 244649919, 1842261384, 912348275, 1011503542, 997596451, 684274533,
  664778041, 537987890, 1035155427, 1504123035, 1356278573, 1370605298, 1865224713,
  891807693, 1863229726, 1627053988, 739924898, 30059441, 580208571, 1154215038,
  1503281803, 1379637289, 84282265, 687403930, 1234978087, 44687053, 711780808,
  1038499445, 1449925264, 1204802372, 921744183, 1481053913, 763989210, 1798363275,
  892194176, 311411032, 1074948272, 1091520091, 1249209539, 876887711, 573642814,
  2098207460, 1762009182, 300148760, 116341756, 1470429140, 775635457, 583937680,
  232940023, 1924444070, 585873120, 240639906, 298627156, 1400597197, 364288759,
  878847657, 1834786408, 1517830958, 1625532177, 2127167168, 1631024127, 1604230628,
  416158729, 1450765950
]
```

## 2. Process Management Details
- **Cleanup Actions:**
  - Terminated active baseline workers cleanly (`kill 3168360 3168361`).
  - Discarded and moved partial sequential-seed run folder to: `realtime_deployment/runs/archive/baseline_simvla_libero10_milk_task7_sam_v1_sequential_seed_aborted_20260528_160522`
- **Relaunch Commands Executed on Sam:**
```bash
# Worker 0 (Episodes 0-50)
ssh sam "cd /home/rootalkhatib/test/reda_ws/fiper_ws && source ../asynchvla_ws/scripts/activate_simvla_sam.sh && export MUJOCO_GL='egl' && export PYOPENGL_PLATFORM='egl' && mkdir -p realtime_deployment/runs/baseline_simvla_libero10_milk_task7_sam_v1/logs && nohup /home/rootalkhatib/envs/simvla/bin/python3 realtime_deployment/scripts/run_baseline_simvla_one_task_v1.py --config realtime_deployment/configs/baseline_simvla_libero10_milk_task7_sam_v1.json --worker-id worker_0 --episode-start 0 --episode-end 50 > realtime_deployment/runs/baseline_simvla_libero10_milk_task7_sam_v1/logs/worker_0.log 2>&1 &"

# Worker 1 (Episodes 50-100)
ssh sam "cd /home/rootalkhatib/test/reda_ws/fiper_ws && source ../asynchvla_ws/scripts/activate_simvla_sam.sh && export MUJOCO_GL='egl' && export PYOPENGL_PLATFORM='egl' && mkdir -p realtime_deployment/runs/baseline_simvla_libero10_milk_task7_sam_v1/logs && nohup /home/rootalkhatib/envs/simvla/bin/python3 realtime_deployment/scripts/run_baseline_simvla_one_task_v1.py --config realtime_deployment/configs/baseline_simvla_libero10_milk_task7_sam_v1.json --worker-id worker_1 --episode-start 50 --episode-end 100 > realtime_deployment/runs/baseline_simvla_libero10_milk_task7_sam_v1/logs/worker_1.log 2>&1 &"
```
- **Relaunch Status:** Both processes are verified running cleanly on Sam using the correct environment.

# Action Modification Smoke Test Report: Risk-Aware SimVLA on Bob (Task 7)

## 1. Episode Outcome and Seed Uniqueness Metrics
- **Episode Outcome:** `failure_or_timeout` (Reached maximum limit of 300 steps)
- **Number of Steps (`num_steps`):** 300
- **Action Modifications Count:** 214
- **First Modification Timestep:** 2
- **Main Risk Score (Main Chunk):**
  - Min: 0.0599
  - Mean: 0.7109
  - Max: 0.9953
- **Selected Risk Score (Executed Chunk):**
  - Min: 0.0599
  - Mean: 0.6707
  - Max: 0.9849
- **Seed Collisions:** 0
- **Main Seed Collisions with ACE:** 0
- **`step_scores.jsonl` Line Count:** 300

## 2. Configuration & Policy Confirmations
```text
ACTION_SELECTION_POLICY = risk_filtered_lowest_score_candidate_v1
ACTIONS_MODIFIED = YES
FULL_RUN_LAUNCHED = NO
SAME_RESET_SEED_LIST_AS_SAM_READY_FOR_FULL_RUN = YES
```

## 3. Seed Uniqueness Verification Details
- **Worker RNG:** numpy.random.default_rng(global_action_seed + worker_offset)
- **Resampling Duplicates:** Checked and validated at every timestep that all 9 seeds (1 main and 8 candidates) are mutually distinct.
- **Reset Seed Used:** 889528444 (The first seed from the Sam control seed list).

## 4. Episode Summary Content (`episode_summary.json`)
```json
{
  "episode_index": 0,
  "suite": "libero_10_with_milk",
  "task_id": 7,
  "reset_seed": 889528444,
  "global_action_seed": 424242,
  "outcome": "failure_or_timeout",
  "success": false,
  "num_steps": 300,
  "wall_time_seconds": 328.6786539554596,
  "conformal_mass_final": 85.49940517544746,
  "alarm_triggered": true,
  "alarm_timestep": 4,
  "action_modifications_count": 214,
  "first_modification_timestep": 2,
  "risk_score_min": 0.0599311962723732,
  "risk_score_max": 0.9953344464302063,
  "risk_score_mean": 0.7109126413365205,
  "selected_risk_min": 0.0599311962723732,
  "selected_risk_max": 0.984906792640686,
  "selected_risk_mean": 0.6706501566867034,
  "error_message": "",
  "timesteps_seed_checked": 300,
  "seed_collisions": 0,
  "main_seed_collisions_with_ace": 0
}
```

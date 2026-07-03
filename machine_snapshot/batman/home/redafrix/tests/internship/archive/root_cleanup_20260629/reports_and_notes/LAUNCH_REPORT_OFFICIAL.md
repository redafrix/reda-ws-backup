# Launch Report: Goal Object Official SimVLA Chunk10 Evaluation

**Date:** Friday, June 5, 2026
**Host:** Bob (pcrobot)
**Trash Directory:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/goal_object_official_simvla_chunk10_100_20260605/`

## Audit & Verification

### Paths and Hashes
- **Checkpoint:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO/model.safetensors`
  - **SHA-256:** `9d3b1767773da86906d771b1eca2c2911087371bf8b3890a7336b6773270f6be` (MATCHED Official)
- **Reproduction Bundle:** Reused from `goal_object_modified_simvla_chunk10_100_20260605`

## Smoke Test Results
- **Status:** PASS
- **Validation JSON:**
```json
{
  "summary_exists": true,
  "events_exists": true,
  "bddl_hash_match": true,
  "init_hash_match": true,
  "checkpoint_hash_match": true,
  "chunk_shape_10x7": true,
  "query_timesteps_correct": true,
  "contiguous_timesteps": true,
  "first_chunk_10_actions": true,
  "total_steps_match": true,
  "no_errors": true,
  "pass": true
}
```

## Production Launch

### Execution Details
- **Tmux Session:** `bob_goal_object_official_simvla_chunk10_100_20260605`
- **Command:** `python3 src/run_goal_object_official_simvla_chunk10.py --mode production`

### First Production Episode Summary
- **Episode UID:** `goal_object_t0to9_task0_init0`
- **Instruction:** "Open the middle layer of the drawer"
- **Success:** `True`
- **Steps:** 125
- **Wall Time:** 3.5s

## Comparison Note (Episode 0)
- **Modified SimVLA:** 119 steps (Success)
- **Official SimVLA:** 125 steps (Success)

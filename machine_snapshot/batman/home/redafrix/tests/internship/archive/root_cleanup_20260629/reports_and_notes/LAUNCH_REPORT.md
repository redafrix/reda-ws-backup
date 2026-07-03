# Launch Report: Goal Object Modified SimVLA Chunk10 Evaluation

**Date:** Friday, June 5, 2026
**Host:** Bob (pcrobot)
**Trash Directory:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/goal_object_modified_simvla_chunk10_100_20260605/`

## Audit & Verification

### Paths and Hashes
- **FIPER Root:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws`
- **Modified SimVLA Source:** `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified`
- **LIBERO-PRO Source:** `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO`
- **Normalization Stats:** `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified/norm_stats/libero_norm.json`
- **SmolVLM Cache:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/smolvlm_cache`
- **Environment Activation:** `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh`
- **Checkpoint:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000/model.safetensors`
  - **SHA-256:** `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71` (MATCHED)
- **Reproduction Bundle:** `libero_goal_object_reproduction_bundle_20260605.zip`
  - **SHA-256:** `453a07c9bbb8469046ebae2b49de041075f3be8e68ab11f0fb5aea7caac0a653`
- **Episode Identity Manifest:** `bundle/verification/episode_identity_table.csv`
  - **SHA-256:** `0aeb109636779b145466bca2cbc44a67e2ac82bda45f599e922dfee6712529d1`

### Bundle Verification
- **Verifier Script:** `bundle/verification/verify_bundle.py`
- **Result:** `VERIFIER_PASS`

## Smoke Test Results
- **Mode:** Foreground Smoke
- **Manifest Row:** 0
- **Policy Steps:** 13 (Max)
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
- **Tmux Session:** `bob_goal_object_modified_simvla_chunk10_100_20260605`
- **Process ID (PID):** `3489231`
- **GPU Usage:** ~4GB Memory, ~14% Utility (RTX 4070 Ti)
- **Command:** `python3 src/run_goal_object_modified_simvla_chunk10.py --mode production`
- **Environment Variables:**
  - `MUJOCO_GL=egl`
  - `PYOPENGL_PLATFORM=egl`
  - `USE_TF=0`
  - `TRANSFORMERS_NO_TF=1`
  - `USE_FLAX=0`
  - `TOKENIZERS_PARALLELISM=false`

### First Production Episode Summary
- **Episode UID:** `goal_object_t0to9_task0_init0`
- **Run ID:** `goal_object_t0to9`
- **Task ID:** 0
- **Init Index:** 0
- **Instruction:** "Open the middle layer of the drawer"
- **Success:** `True`
- **Steps:** 119
- **Wall Time:** 3.2s

## Conclusion
The experiment is running healthily. The first episode resulted in success, confirming that the environment loading, BDDL parsing, and model inference are all functioning as expected.

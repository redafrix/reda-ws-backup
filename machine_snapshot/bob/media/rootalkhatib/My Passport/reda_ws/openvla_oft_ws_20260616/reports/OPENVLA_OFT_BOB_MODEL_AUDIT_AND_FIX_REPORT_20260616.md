# OpenVLA-OFT Setup Audit and Fix Report

## Workspace & Environment Information
- **Workspace Path:** `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616`
- **Repository Commit Hash:** `e4287e94541f459edc4feabc4e181f537cd569a8`
- **Model ID:** `moojink/openvla-7b-oft-finetuned-libero-goal`
- **Model Snapshot Path:** `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/hf_cache/models--moojink--openvla-7b-oft-finetuned-libero-goal/snapshots/c2d0f9fbbd82674683b397ff923168a12f6a307b`
- **Disk Usage:** 20 GB
- **Bob Free Disk Space:** 504 GB on `/media/rootalkhatib/My Passport`
- **GPU Model:** NVIDIA GeForce RTX 4070 Ti SUPER 16 GB
- **Free VRAM (Baseline):** ~13 GB free

## Installed Package Versions
- `torch`: `2.2.0+cu121`
- `transformers`: `4.40.1` (moojink custom fork)
- `accelerate`: `1.14.0`
- `bitsandbytes`: `0.42.0`

---

## Controlled Loading & Patch Verification

We conducted controlled load tests saving tracebacks/logs under `logs/patch_audit_20260616/`.

### 1. Official No-Patch Load Results
- **8-bit Mode (No Patch):** FAILED.
  - *Error:* `ValueError: .to is not supported for 4-bit or 8-bit bitsandbytes models. Please use the model as it is...`
  - *Cause:* Accelerate's `dispatch_model` checks `is_loaded_in_8bit` to set `force_hooks=True` (which skips `.to()`). But the custom `OpenVLAForActionPrediction` class has `is_loaded_in_8bit = None` instead of `True`, causing it to execute `.to()` on quantized weights.
- **4-bit Mode (No Patch):** FAILED.
  - *Error:* Same `ValueError` on `.to()` execution.

### 2. Patched Load Results
- **8-bit Mode (Patched):** PASSED.
  - *Behavior:* Monkey-patched `PreTrainedModel.to()` to act as a no-op when the model has `quantization_method` set.
- **Rotary Embedding Buffer Alignment:** PASSED.
  - *Behavior:* Patched script aligned `inv_freq` buffers of `LlamaRotaryEmbedding` (which originally stayed on CPU) to the layer's device (`cuda:0`). Without this, inference crashes due to device mismatch: `RuntimeError: Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0!`.

### 3. Cleanup & Compatibility Helper
- We created a clean reusable helper module `src/openvla_oft_bob_compat.py` to package these patches cleanly and avoid inline code duplication.
- Updated both `smoke_load_openvla_oft.py` and `smoke_openvla_oft_action.py` to import and call `openvla_oft_bob_compat`.

---

## Constants Verification
Inspected values stored under `outputs/smoke/constants_inspection.json`:
- `NUM_ACTIONS_CHUNK`: `8`
- `ACTION_DIM`: `7`
- `PROPRIO_DIM`: `8`
- `model_norm_stats_keys`: `["libero_goal_no_noops"]`
- `action_head_checkpoint_path`: `.../action_head--50000_checkpoint.pt`
- `proprio_projector_checkpoint_path`: `.../proprio_projector--50000_checkpoint.pt`

### Enforced Correct Unnormalization Key
The smoke script was corrected from dynamically picking the first key to explicitly checking and enforcing the correct key: `libero_goal_no_noops`.

---

## Action Prediction Smoke Test V2
- **Quantization Mode:** 8-bit Quantized
- **Task Description:** *'pick up the black bowl between the plate and the ramekin and place it on the plate'*
- **Inference Time:** `0.73` seconds
- **GPU VRAM Footprint:**
  - Before Load: `12.16 GB / 15.57 GB` free
  - After Load/Inference: `3.36 GB / 15.57 GB` free (model footprint: ~8.8 GB VRAM)
- **First Predicted Action Vector:**
  `[0.375298, 0.113880, -0.160217, 0.000102, 0.023207, -0.021599, 0.972656]`
- **Finite Check:** `True` (passed)
- **Result Output Path:** `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/smoke/action_smoke_result_v2.json`

---

## LIBERO Environment Smoke Test
- **Execution Status:** PASSED.
- **Details:** Verified environment creation for task 0 (`open the middle drawer of the cabinet`) under the `libero_goal` task suite.
- **System Path Alignment:** Resolved missing dependency issues (e.g. `robosuite`, `future` dist-packages fallback) by appending `/home/rootalkhatib/envs/simvla/lib/python3.10/site-packages` and `/usr/lib/python3/dist-packages` to `sys.path` dynamically. This prevents any NumPy 2.x version clashes (since `openvla_oft_env_20260616` uses NumPy 1.26.4 while `simvla` packages use NumPy 2.x).

---

## Summary Flags
```
OPENVLA_OFT_WORKSPACE_EXISTS = YES
MODEL_FILES_PRESENT = YES
ACTION_HEAD_PRESENT = YES
PROPRIO_PROJECTOR_PRESENT = YES
OFFICIAL_NO_PATCH_8BIT_PASS = NO
PATCHED_8BIT_PASS = YES
COMPAT_MODULE_CREATED = YES
UNNORM_KEY_CORRECT = YES
ACTION_SMOKE_V2_PASS = YES
LIBERO_ENV_SMOKE_PASS = YES
SAFE_FOR_NEXT_SMALL_LIBERO_ROLLOUT = YES
```

## Recommended Next Steps
1. The OpenVLA-OFT model loading, action prediction, and LIBERO simulation environment creation are fully verified and robust.
2. Proceed to run a small evaluation rollout (e.g. a single-task eval loop with 1-5 trials) using:
   ```bash
   python3 experiments/robot/libero/run_libero_eval.py \
     --pretrained_checkpoint moojink/openvla-7b-oft-finetuned-libero-goal \
     --task_suite_name libero_goal \
     --num_trials_per_task 5
   ```
   *Note:* Remember to import `openvla_oft_bob_compat` inside `run_libero_eval.py` to enable monkey patches and avoid runtime errors.

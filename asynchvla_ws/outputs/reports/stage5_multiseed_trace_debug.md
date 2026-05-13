# Stage 5 Multi-Seed Trace Debug Report

Machine: Bob / `pcrobot` / `PCROBOTUBUNTU02`
Workspace: `/media/rootalkhatib/My Passport/reda_ws`
Branch: `bob`
Date: 2026-05-13

## 1. Trace Debug Dataset Status

Status: `OK`

Dataset:
`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/stage5_debug/multiseed_trace_debug.pt`

Builder:
`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_building/build_multiseed_trace_dataset.py`

Command:
```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
python3 asynchvla_ws/src/data_building/build_multiseed_trace_dataset.py --debug true
```

## 2. Dataset Properties

- **Number of Contexts:** 50
- **File Size:** 0.63 MB
- **SimVLA Checkpoint:** `intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000`
- **Generated Seeds:** 0, 1, 2, 3, 4
- **Flow Steps:** 10

## 3. Tensor Shapes (per sample)

| Key | Shape / Type |
| --- | --- |
| `sample_id` | str |
| `context_id` | str |
| `task_name` | str |
| `source_hdf5` | str |
| `source_local_index` | int |
| `language_instruction` | str |
| `proprio` | `[8]` torch.float32 |
| `expert_normalized_action` | `[10, 7]` torch.float32 |
| `expert_postprocessed_action` | `[10, 7]` torch.float32 |
| `split` | str |
| `pooled_vlm_features` | `[960]` torch.float32 |
| `simvla_seed{0,1,2,3,4}_normalized_action` | `[10, 7]` torch.float32 |
| `simvla_seed{0,1,2,3,4}_postprocessed_action`| `[10, 7]` torch.float32 |
| `simvla_seed{0,1,2,3,4}_per_step_l2_error` | `[10]` torch.float32 |
| `simvla_seed{0,1,2,3,4}_chunk_l2_error` | float |

No NaN/Inf found in tensors.

## 4. Error Statistics Per Seed

| Seed | Mean Error | Std Dev | Min Error | Max Error |
| --- | --- | --- | --- | --- |
| 0 | 1.5281 | 0.6913 | 0.3198 | 2.7826 |
| 1 | 1.5119 | 0.6578 | 0.3313 | 2.6603 |
| 2 | 1.4843 | 0.6614 | 0.3338 | 2.5982 |
| 3 | 1.5402 | 0.6643 | 0.3443 | 2.7052 |
| 4 | 1.4850 | 0.6422 | 0.3455 | 2.5581 |

## 5. Seed Diversity

- **Contexts where all seeds are nearly identical (dist < 1e-4):** 0 / 50 (0.0%)

**Examples of LOW seed diversity:**
- `debug_ctx_0000021` (put the white bowl on the plate): mean pairwise distance = 0.101694
- `debug_ctx_0000020` (put the white bowl on the plate): mean pairwise distance = 0.104640
- `debug_ctx_0000022` (put the white bowl on the plate): mean pairwise distance = 0.109290

**Examples of HIGH seed diversity:**
- `debug_ctx_0000033` (put the white bowl on the plate): mean pairwise distance = 0.354466
- `debug_ctx_0000034` (put the white bowl on the plate): mean pairwise distance = 0.360265
- `debug_ctx_0000035` (put the white bowl on the plate): mean pairwise distance = 0.361625

## 6. Conclusion
SimVLA generated actions vary meaningfully across different seeds for the same observation. The multi-seed trace generation works and is meaningful. We can proceed to Phase 2 to build the candidate dataset.

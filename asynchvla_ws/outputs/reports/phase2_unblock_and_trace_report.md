# Phase 2 Unblock And Trace Report

Machine: Bob / `pcrobot` / `PCROBOTUBUNTU02`  
Workspace: `/media/rootalkhatib/My Passport/reda_ws`  
Branch: `bob`  
Date: 2026-05-13  
Scope: unblock SimVLA checkpoint loading with a local SmolVLM backbone, then run only tiny LIBERO/dataset-loader/trace smoke tests. No rater training was started.

## 1. SmolVLM Backbone Status

Status: `OK`

The local SmolVLM backbone now exists at:

`/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct`

The first download path through Hugging Face Xet was slow/unstable and hit a `Connection reset by peer` in the Xet log. The successful download used the regular Hugging Face transfer path with `HF_HUB_DISABLE_XET=1` and a stable local destination.

Command used:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh >/dev/null
export HF_HOME="/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/models/huggingface/.hf_cache"
export TRANSFORMERS_CACHE="$HF_HOME/transformers"
export HF_HUB_CACHE="$HF_HOME/hub"
export HF_HUB_DISABLE_XET=1
python3 - <<'PY'
from huggingface_hub import snapshot_download
from pathlib import Path
repo="HuggingFaceTB/SmolVLM-500M-Instruct"
local_dir=Path("intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct").resolve()
local_dir.mkdir(parents=True, exist_ok=True)
path=snapshot_download(repo_id=repo, local_dir=str(local_dir), ignore_patterns=["onnx/*","*.onnx"], resume_download=True)
print("snapshot_path", path)
PY
```

Output:

```text
snapshot_path /media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct
```

Size and key files:

```text
1023M intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct
model.safetensors 1015025832 bytes
config.json 7339 bytes
preprocessor_config.json 486 bytes
processor_config.json 68 bytes
tokenizer.json 3548256 bytes
tokenizer_config.json 28249 bytes
generation_config.json 136 bytes
vocab.json 800662 bytes
merges.txt 466391 bytes
```

Local Transformers verification succeeded with `Idefics3Config` and `Idefics3Processor`.

## 2. Checkpoint Load Status

Status: `OK`

Checkpoint used:

`/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000`

The original checkpoint config was not overwritten. The smoke script loads `SmolVLMVLAConfig` from the checkpoint and overrides `config.smolvlm_model_path` in memory to the local SmolVLM path.

Script:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/smoke_load_simvla_local_backbone.py`

Log:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/smoke_load_simvla_local_backbone.log`

Command:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh >/dev/null
python3 asynchvla_ws/scripts/smoke_load_simvla_local_backbone.py \
  > asynchvla_ws/outputs/reports/smoke_load_simvla_local_backbone.log 2>&1
```

Important output:

```text
model_loaded: OK
config_values: {
  "num_actions": 10,
  "action_dim": 7,
  "action_mode": "libero_joint",
  "num_views": 3,
  "image_size": 384,
  "use_proprio": true,
  "predict_uncertainty": true,
  "model_type": "smolvlm_vla",
  "smolvlm_model_path": "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct"
}
gpu_memory_before: 3272, 16376, 0 MiB_used,total,util_percent
gpu_memory_after_cpu_load: 3272, 16376, 0 MiB_used,total,util_percent
model_to_cuda: OK
gpu_memory_after_cuda_load: 6621, 16376, 1 MiB_used,total,util_percent
```

## 3. LIBERO Data Status

Status: `OK`

HDF5 inspected:

`/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/data/libero_datasets/libero_90/KITCHEN_SCENE5_close_the_top_drawer_of_the_cabinet_demo.hdf5`

Report:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/one_libero_demo_inspection.md`

Key shapes from `demo_0`:

| Key | Shape | Dtype |
| --- | ---: | --- |
| `actions` | `(65, 7)` | `float64` |
| `obs/agentview_rgb` | `(65, 128, 128, 3)` | `uint8` |
| `obs/eye_in_hand_rgb` | `(65, 128, 128, 3)` | `uint8` |
| `obs/ee_pos` | `(65, 3)` | `float64` |
| `obs/ee_ori` | `(65, 3)` | `float64` |
| `obs/gripper_states` | `(65, 2)` | `float64` |
| `obs/joint_states` | `(65, 7)` | `float64` |

Expert actions are available directly in HDF5 under `data/demo_X/actions`.

## 4. Dataset Loader Status

Status: `OK`

The real SimVLA modified dataset loader works after adding two optional import-time dependencies to the existing Bob target site-packages:

```bash
python3 -m pip install --target /home/rootalkhatib/envs/simvla/lib/python3.10/site-packages pyarrow av
```

Output:

```text
Successfully installed av-17.0.1 pyarrow-24.0.0
```

Loader script:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/smoke_simvla_dataset_loader.py`

Report:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/simvla_dataset_loader_smoke.md`

Loader path:

`/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified/datasets/dataset_smolvlm.py`

Handler path:

`/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified/datasets/domain_handler/libero_hdf5.py`

Debug meta created:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/debug/one_libero_meta.json`

Sample output:

```text
dataset_loader_smoke: OK
keys ['action', 'image_input', 'image_mask', 'language_instruction', 'proprio']
action {'shape': [10, 7], 'dtype': 'torch.float32'}
image_input {'shape': [3, 3, 384, 384], 'dtype': 'torch.float32'}
image_mask {'shape': [3], 'dtype': 'torch.bool'}
language_instruction {'type': 'str', 'repr': "'close the top drawer of the cabinet'"}
proprio {'shape': [8], 'dtype': 'torch.float32'}
expert_action_chunk_shape [10, 7]
expert_action_min_mean_max -1.0 -0.12530101835727692 0.6187499761581421
```

Alignment decision:

The official `LiberoHDF5Handler._get_action_chunk()` creates `[num_actions + 1, 7]` chunks internally: current action at index 0 plus 10 future actions. `datasets/utils.py::action_slice()` then sets `action = abs_traj[1:].clone()`, so the dataset sample exposes `action` as `[10, 7]`. For SimVLA generated chunks with `num_actions=10`, compare generated `[10,7]` against `sample['action']`. Do not include the current action at index 0 in the target.

## 5. Trace API Status

Status: `OK`

A non-breaking trace wrapper was added outside the SimVLA codebase:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/simvla_trace/trace.py`

Function:

`generate_actions_trace(...)`

This does not modify `SimVLA_modified` and does not change existing `generate_actions()` behavior.

Smoke script:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/smoke_trace_one_sample.py`

Report:

`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/trace_one_sample_smoke.md`

Trace return keys in v1:

- `generated_normalized_action`
- `generated_postprocessed_action`
- `pooled_vlm_features`
- `vlm_feature_shape`
- `proprio`
- `proprio_norm`
- `seed`
- `num_flow_steps`
- `flow_steps`
- optional `initial_noise` if requested

Trace smoke output:

```text
trace_one_sample_smoke: OK
input_ids {'shape': [1, 50], 'dtype': 'torch.int64', 'device': 'cuda:0'}
image_input {'shape': [1, 3, 3, 384, 384], 'dtype': 'torch.float32', 'device': 'cuda:0'}
image_mask {'shape': [1, 3], 'dtype': 'torch.bool', 'device': 'cuda:0'}
proprio {'shape': [1, 8], 'dtype': 'torch.float32', 'device': 'cuda:0'}
expert_postprocessed_action {'shape': [1, 10, 7], 'dtype': 'torch.float32', 'device': 'cuda:0'}
expert_normalized_action {'shape': [1, 10, 7], 'dtype': 'torch.float32', 'device': 'cuda:0'}
generated_normalized_action_seed0 {'shape': [1, 10, 7], 'dtype': 'torch.float32', 'device': 'cuda:0'}
generated_postprocessed_action_seed0 {'shape': [1, 10, 7], 'dtype': 'torch.float32', 'device': 'cuda:0'}
pooled_vlm_features_seed0 {'shape': [1, 960], 'dtype': 'torch.float32', 'device': 'cuda:0'}
vlm_feature_shape_seed0 [1, 122, 960]
proprio_norm_seed0 {'shape': [1, 8], 'dtype': 'torch.float32', 'device': 'cuda:0'}
seed0 0
seed1 1
num_flow_steps 10
actions_differ_between_seed0_seed1 True
normalized_action_error_chunk_l2_mean 1.4050766229629517
postprocessed_action_error_chunk_l2_mean 1.4050766229629517
first_flow_step {'t': 1.0, 'dt': -0.1, 'velocity_mean': 0.11160401999950409, 'logvar_mean': -5.36920690536499}
last_flow_step {'t': 0.10000000000000014, 'dt': -0.1, 'velocity_mean': 0.16131801903247833, 'logvar_mean': -2.2472708225250244}
```

Seed behavior:

- Seed `0` and seed `1` produce different generated action chunks.
- The trace wrapper uses a per-call `torch.Generator(device=device).manual_seed(seed)`.

No trajectory timestep, episode progress, episode length, file-name difficulty, success/failure labels, or TDQC features are included in trace outputs.

## 6. Files Created Or Modified

Created/updated under the new workspace:

- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/smoke_load_simvla_local_backbone.py`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/inspect_one_libero_demo.py`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/smoke_simvla_dataset_loader.py`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/smoke_trace_one_sample.py`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/simvla_trace/__init__.py`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/simvla_trace/trace.py`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/debug/one_libero_meta.json`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/smoke_load_simvla_local_backbone.log`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/one_libero_demo_inspection.md`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/simvla_dataset_loader_smoke.md`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/trace_one_sample_smoke.md`
- `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/phase2_unblock_and_trace_report.md`

Created/downloaded model files:

- `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct/`

Environment packages added to target site-packages, not globally:

- `pyarrow==24.0.0`
- `av==17.0.1`

No TDQC experiment files were modified by this phase.

## 7. Next Recommended Step

The next step is ready: build a 50-200 sample debug trace dataset from ID LIBERO only.

Recommended immediate implementation sequence:

1. Create `asynchvla_ws/src/data_building/build_debug_trace_dataset.py` using the working loader and `generate_actions_trace()`.
2. Save only compact fields first: IDs, instruction, proprio, pooled VLM features, generated normalized/postprocessed action, expert normalized/postprocessed action, per-step L2 error, chunk L2 error, seed, and split label `debug_id`.
3. Add a validation script that prints keys, shapes, NaN/Inf checks, min/mean/max error, and file size.
4. Build same-image candidate-action examples before any rater training: expert, SimVLA, same-task far timestep, other trajectory, other task, controlled perturbation, optional extra seeds.
5. Only after same-image candidate examples validate, train the tiny debug rater.

Blocking issues: none for the tiny ID smoke path. Full-scale extraction is not launched yet and should be run later via tmux/nohup according to `REMOTE_EXPERIMENT_GUIDE.md`.

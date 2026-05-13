# AsyncVLA-SimVLA Implementation Report

Date: 2026-05-13  
Machine: Bob / `pcrobot` / `PCROBOTUBUNTU02`  
Workspace: `/media/rootalkhatib/My Passport/reda_ws`  
Branch: `bob`

## 1. Environment Status

Status: partially fixed and usable for Python imports/CUDA smoke checks.

Activation command:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
```

Why a Bob-specific activation script was created:

- `intern_ship_ws/activate_simvla.sh` still points to `/home/redafrix/envs/simvla`.
- `/home/redafrix/envs/simvla` does not exist on Bob.
- `/home/rootalkhatib/envs/simvla` did not exist before this run.
- `conda`, `mamba`, and `micromamba` were not found in the requested search paths.
- `python3 -m venv` failed because `ensurepip` / `python3.10-venv` is unavailable. I did not install it with apt because that would be a global package change.

Implemented fallback:

```text
/home/rootalkhatib/envs/simvla/lib/python3.10/site-packages
```

This is a project-local target-package environment using `/usr/bin/python3` plus existing system CUDA PyTorch.

Important verification output:

```text
/usr/bin/python3
Python 3.10.12
torch OK 2.5.1+cu121
torch_cuda 2.5.1+cu121 True 12.1
transformers OK 4.57.6
h5py OK 3.16.0
safetensors OK 0.7.0
numpy OK 2.2.6
scipy OK 1.15.3
sklearn OK 1.6.1
PIL OK 12.2.0
cv2 OK 4.13.0
fastapi OK 0.136.1
mmengine OK 0.10.7
```

Detailed environment report:

```text
asynchvla_ws/outputs/reports/env_check.md
```

## 2. Checkpoint Status

Checkpoint selected from the audit:

```text
intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000
```

Files present:

```text
config.json 570 bytes
model.safetensors 3245557952 bytes
state.json 22 bytes
```

Config values:

```text
model_type: smolvlm_vla
num_actions: 10
action_mode: libero_joint
image_size: 384
num_views: 3
predict_uncertainty: true
hidden_size: 1024
depth: 24
num_heads: 16
smolvlm_model_path: HuggingFaceTB/SmolVLM-500M-Instruct
```

Smoke result: failed at Phase 2.

The class import works:

```text
from models.modeling_smolvlm_vla import SmolVLMVLA
```

But `SmolVLMVLA.from_pretrained("intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000")` fails because the SmolVLM backbone files for `HuggingFaceTB/SmolVLM-500M-Instruct` are not present in the local Hugging Face cache. Offline mode was intentionally enabled to avoid a large download.

Exact failure excerpt:

```text
huggingface_hub.errors.LocalEntryNotFoundError: Cannot find the requested files in the disk cache and outgoing traffic has been disabled.
OSError: We couldnt connect to https://huggingface.co to load the files, and couldnt find them in the cached files.
File ".../SimVLA_modified/models/modeling_smolvlm_vla.py", line 84, in __init__
  self.vlm = AutoModelForImageTextToText.from_pretrained(
```

Detailed checkpoint report:

```text
asynchvla_ws/outputs/reports/checkpoint_smoke_test.md
```

## 3. Trace API Status

Status: not implemented.

Reason: hard stop at Phase 2 per instruction:

```text
Stop if the checkpoint cannot load. Do not continue to implement extraction if the model cannot load.
```

No SimVLA model files were modified.

## 4. LIBERO Data Status

Status: not executed in this implementation run.

Reason: hard stop at Phase 2 before trace/data extraction phases.

The audit already established that ID LIBERO HDF5 files exist under:

```text
intern_ship_ws/assets/data/libero_datasets
```

but alignment/debug extraction was not run after checkpoint load failed.

## 5. Candidate-Action Dataset

Status: not created.

Reason: checkpoint load failed at Phase 2. Same-image candidate-action generation depends on trace/model generation and expert alignment, which were not reached.

## 6. Rater Debug Results

Status: not trained.

Reason: no trace/candidate dataset was created because Phase 2 failed.

## 7. Calibration Results

Status: not run.

Reason: no debug rater was trained.

## 8. OOD Status

Status: not searched in this implementation run beyond the audit.

Reason: hard stop at Phase 2. The audit remains the current truth: raw OOD expert demonstrations were not confirmed, and TDQC OOD `.pt` files must not be used as if they contain expert action data.

## 9. Files Created or Modified

Created:

```text
asynchvla_ws/
asynchvla_ws/README.md
asynchvla_ws/configs/
asynchvla_ws/scripts/
asynchvla_ws/scripts/activate_simvla_bob.sh
asynchvla_ws/src/
asynchvla_ws/src/simvla_trace/
asynchvla_ws/src/rater/
asynchvla_ws/src/calibration/
asynchvla_ws/src/eval/
asynchvla_ws/src/data_building/
asynchvla_ws/data/
asynchvla_ws/data/features/
asynchvla_ws/data/debug/
asynchvla_ws/outputs/
asynchvla_ws/outputs/logs/
asynchvla_ws/outputs/checkpoints/
asynchvla_ws/outputs/reports/
asynchvla_ws/outputs/reports/env_check.md
asynchvla_ws/outputs/reports/checkpoint_smoke_test.md
asynchvla_ws/ASYNCVLA_SIMVLA_IMPLEMENTATION_REPORT.md
```

Created outside workspace as local package target:

```text
/home/rootalkhatib/envs/simvla/lib/python3.10/site-packages
```

Modified existing SimVLA/TDQC files: none.

Commits/pushes: none.

## 10. Next Steps

1. Provide or approve download of `HuggingFaceTB/SmolVLM-500M-Instruct` backbone files on Bob.
2. Re-run Phase 2 checkpoint smoke test without offline mode after the backbone is local.
3. Only after checkpoint load succeeds, add a non-breaking trace API in `SimVLA_modified` or a wrapper that returns normalized action, postprocessed action, pooled VLM features, proprio, seed, and flow metadata.
4. Verify LIBERO expert action alignment on a tiny HDF5 sample before generating any rater dataset.
5. Build the same-image candidate-action debug dataset before training any rater.
6. Do not launch long jobs yet. Full extraction/training is not ready until checkpoint load and tiny debug validation succeed.

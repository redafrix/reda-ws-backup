# SimVLA Baseline Audit

Workspace:
- `/home/redafrix/tests/intern_ship_research/intern_ship_ws`

Official repo cloned:
- `/home/redafrix/tests/intern_ship_research/intern_ship_ws/SimVLA`
- Remote: `https://github.com/LUOyk1999/SimVLA.git`
- Commit inspected: `32700d0ad8991996e123e4b685abe370ce6e9aab`

Local paper inspected:
- `/home/redafrix/tests/intern_ship_research/06_papers/read_list_pdfs/2026 - SimVLA.pdf`
- `/home/redafrix/tests/intern_ship_research/06_papers/read_list_pdfs/2026 - SimVLA.txt`

## What the released code actually is

This release is not a generic full-paper implementation. It is:
- a SmolVLM-only SimVLA variant
- a LIBERO-only training pipeline
- a LIBERO evaluation server/client stack

Key entry points:
- Training: `SimVLA/train_smolvlm.py`
- Main model: `SimVLA/models/modeling_smolvlm_vla.py`
- Action head: `SimVLA/models/transformer_smolvlm.py`
- Dataset loader: `SimVLA/datasets/dataset_smolvlm.py`
- LIBERO server: `SimVLA/evaluation/libero/serve_smolvlm_libero.py`
- LIBERO client: `SimVLA/evaluation/libero/libero_client.py`

## What the unchanged baseline expects

### Runtime
- Python `3.10`
- `torch` with CUDA support
- `transformers>=4.57.0`
- `fastapi`, `uvicorn`
- `mmengine`
- `json_numpy`
- `peft`
- `tensorflow`
- several smaller packages from the repo README

### Data
- Official LIBERO HDF5 files placed under repo-relative paths like:
  - `./datasets/metas/libero_10/*.hdf5`
  - `./datasets/metas/libero_goal/*.hdf5`
  - `./datasets/metas/libero_object/*.hdf5`
  - `./datasets/metas/libero_spatial/*.hdf5`
- Training metadata JSON:
  - `SimVLA/datasets/metas/libero_train.json`
- Normalization stats:
  - `SimVLA/norm_stats/libero_norm.json`

### Training shape
- Backbone: `HuggingFaceTB/SmolVLM-500M-Instruct`
- Action mode: `libero_joint`
- Action dimension: `7`
- Proprio dimension: `8`
- Default action horizon: `10`
- Training loss: plain flow-matching velocity MSE

## Hard blockers on this machine

Verified by:
- `src/check_simvla_baseline.py`

Current blockers:
1. Missing Python dependencies for model import.
2. Installed PyTorch is CPU-only, so unchanged training/inference will not use the GPU.
3. LIBERO HDF5 data referenced by the repo metadata is not present.
4. The released repo is narrower than the paper: SmolVLM-only and LIBERO-only.

## Exact changes needed before it can run here

### To run the repo unchanged
1. Create an isolated environment for SimVLA in this workspace.
2. Install the missing dependencies from the repo README.
3. Replace CPU-only PyTorch with a CUDA build that matches the machine.
4. Put the actual LIBERO dataset in the path the repo expects, or regenerate metadata for the real dataset path.
5. For evaluation, install LIBERO and either:
   - use their websocket path and add `openpi_client`, or
   - switch evaluation to the built-in HTTP client path.

### To adapt it to your project
1. Replace `libero_joint` action space with your robot/action space.
2. Replace the LIBERO HDF5 dataset handler with your own dataset handler.
3. Replace the LIBERO evaluation server/client assumptions with your observation format.
4. Keep the baseline flow head first, then add uncertainty changes on top of the existing velocity head.

## Important code-level facts

### The released baseline loss
In `models/modeling_smolvlm_vla.py`, training is:
- sample `t ~ Beta(1.5, 1) * 0.999 + 0.001`
- build `x_t = t * noise + (1 - t) * action_norm`
- target `u_t = noise - action_norm`
- optimize:
  - `velocity_loss = mean((v_t - u_t)^2)`

### Inference
In `generate_actions(...)`:
- start from Gaussian noise
- run Euler integration for `steps` iterations
- default is `10` steps
- return postprocessed actions through the action space

### Paper vs repo
- The paper is architecture-level and benchmark-level.
- The repo is a concrete SmolVLM implementation, not a backbone-agnostic release.
- The repo is enough to bootstrap your reactive branch, but not enough to claim full paper coverage.

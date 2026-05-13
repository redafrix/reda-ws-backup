# AsyncVLA-Style SimVLA Action-Error Uncertainty Audit

Audit date: 2026-05-13  
Machine audited: Bob / `pcrobot` / `PCROBOTUBUNTU02`  
Workspace: `/media/rootalkhatib/My Passport/reda_ws`  
Scope: inspection only. No training, no code implementation, no package installation, no commits/pushes.

## 1. Machine and Environment Audit

| Item | Observed value |
|---|---|
| Hostname | `PCROBOTUBUNTU02` |
| User | `rootalkhatib` |
| OS | Ubuntu 22.04.5 LTS, kernel `6.8.0-111-generic` |
| Default `python3` | `Python 3.10.12` |
| Default `python` | missing: `bash: python: command not found` |
| GPU | `NVIDIA GeForce RTX 4070 Ti SUPER` |
| VRAM | `16376 MiB` |
| Driver | `570.211.01` |
| CUDA compiler | `nvcc` not found on shell PATH |
| Workspace disk | `/dev/sda1`, 1.9T total, 321G used, 1.6T free |
| Home/root disk | `/dev/nvme0n1p2`, 468G total, 42G used, 403G free |

Commands used included:

```bash
hostname; whoami; uname -a; lsb_release -a; python3 --version; python --version
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader
df -h "/media/rootalkhatib/My Passport/reda_ws" "$HOME"
```

The requested activation command currently fails on Bob:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source intern_ship_ws/activate_simvla.sh
```

Observed output:

```text
intern_ship_ws/activate_simvla.sh: line 9: conda: command not found
Error: Environment not found at /home/redafrix/envs/simvla
```

`intern_ship_ws/activate_simvla.sh` hardcodes `/home/redafrix/envs/simvla` and calls `conda activate`, but `conda` is not available on Bob's PATH in this SSH shell and `/home/redafrix/envs/simvla` was not present from Bob. A large environment-like folder exists at `intern_ship_ws/assets/envs/envs/simvla`, but it did not expose a normal `bin/activate` or obvious runnable `bin/python` in the inspected path. Its `site-packages` can be partly reached with `PYTHONPATH`, but that workaround produced incomplete namespace imports for packages such as `h5py` and `safetensors`, so it is not a valid environment solution.

A system package probe showed:

```text
gym==0.26.2
gym-notices==0.0.8
numpy==2.2.6
scipy==1.15.3
torch==2.5.1+cu121
torchaudio==2.5.1+cu121
torchvision==0.20.1+cu121
```

Because activation fails, the requested post-activation values for `which python`, `python --version`, full package grep, and `python -c "import torch; ..."` could not be truthfully reported. Recommendation: repair/repoint the existing SimVLA activation before creating a new environment. The workspace already contains a lot of SimVLA/LIBERO-compatible assets, so a new env should be a fallback, not the first move.

## 2. Git and Workspace Audit

| Item | Observed value |
|---|---|
| Repo root | `/media/rootalkhatib/My Passport/reda_ws` |
| Current branch | `bob` |
| Remote | `origin` configured; GitHub token was present in URL and is intentionally redacted here |
| Branches | local `bob`, `main`, `sam`; remote `origin/bob`, `origin/main`, `origin/sam` |

`git status --short` before this report showed pre-existing untracked files:

```text
?? intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/c_hardcore_50/eval_log.txt
?? intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/c_hardcore_50/eval_results_1_50.json
?? intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/c_hardcore_50/eval_results_fast.json
?? intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/c_hardcore_50/evaluate_50.py
?? intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/c_hardcore_50/evaluate_all_progress.py
?? intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/c_hardcore_50/evaluate_fast.py
```

Important workspace areas:

| Area | Path | Notes |
|---|---|---|
| SimVLA baseline | `intern_ship_ws/simvla/code/SimVLA` | Main baseline implementation. |
| SimVLA modified | `intern_ship_ws/simvla/code/SimVLA_modified` | Prior phase-1 uncertainty implementation. |
| SimVLA config | `intern_ship_ws/simvla/config/libero` | Exported by activation script. |
| TDQC standalone | `intern_ship_ws/tdqc/code/phase2_tdqc_standalone` | Previous uncertainty/risk experiments. |
| LIBERO data | `intern_ship_ws/assets/data/libero_datasets` | 130 HDF5 files, 94G. |
| OOD data | `intern_ship_ws/ood_data` | Contains `libero_object_object_new/ckpt-60000`. |
| Eval outputs | `intern_ship_ws/outputs/eval` | 633M of eval JSON/log outputs. |
| SimVLA run checkpoint | `intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000` | Local 3.1G safetensors checkpoint. |
| HF cache dirs | `intern_ship_ws/assets/models/huggingface` | Directory names exist, but full model weights were not visible. |
| Root capsule | `experiments/v8_exp10_33d` | TDQC v8 experiment capsule. |

Top-level `reda_ws` includes `00_subjects`, `01_context`, `02_search_strategy`, `03_search_runs`, `04_structured_research`, `05_external_assets`, `06_papers`, `docs`, `experiments`, `intern_ship_ws`, `plans`, `REMOTE_EXPERIMENT_GUIDE.md`, and workspace summary dumps.

## 3. SimVLA Code Audit

Main paths:

| Component | Path |
|---|---|
| Main model | `intern_ship_ws/simvla/code/SimVLA/models/modeling_smolvlm_vla.py` |
| Flow/action transformer | `intern_ship_ws/simvla/code/SimVLA/models/transformer_smolvlm.py` |
| Config | `intern_ship_ws/simvla/code/SimVLA/models/configuration_smolvlm_vla.py` |
| Processor | `intern_ship_ws/simvla/code/SimVLA/models/processing_smolvlm_vla.py` |
| Action helpers / normalization | `intern_ship_ws/simvla/code/SimVLA/models/action_hub.py` |
| Training | `intern_ship_ws/simvla/code/SimVLA/train_smolvlm.py` |
| Eval server | `intern_ship_ws/simvla/code/SimVLA/evaluation/libero/serve_smolvlm_libero.py` |
| Eval client | `intern_ship_ws/simvla/code/SimVLA/evaluation/libero/libero_client.py` |
| Dataset loader | `intern_ship_ws/simvla/code/SimVLA/datasets/dataset_smolvlm.py` |
| LIBERO HDF5 handler | `intern_ship_ws/simvla/code/SimVLA/datasets/domain_handler/libero_hdf5.py` |
| Norm stats | `intern_ship_ws/simvla/code/SimVLA/norm_stats/libero_norm.json` |

Yes, SimVLA is implemented as flow matching here. In `models/modeling_smolvlm_vla.py:333-384`, training samples `t ~ Beta(1.5, 1)`, creates `noise = torch.randn_like(action_norm)`, interpolates `x_t = t * noise + (1 - t) * action_norm`, uses target velocity `u_t = noise - action_norm`, and trains `v_t` with MSE. In `models/modeling_smolvlm_vla.py:421-441`, inference initializes `x_t = torch.randn(B, self.num_actions, D, ...)` and Euler-integrates from `t=1` to `0` before returning `action_space.postprocess(x_t)`.

Important shapes and constants:

| Tensor / setting | Observed shape/value |
|---|---|
| Eval server state dim | `8` |
| Eval server action dim | `7` |
| Eval server action horizon | `10` |
| Generated action chunk | `[B, self.num_actions, D]`, normally `[B, 10, 7]` |
| Dataset raw expert actions | `[T, 7]` |
| Dataset expert chunk | `[num_actions + 1, action_dim]`, normally `[11, 7]` |
| Proprio | `[ee_pos(3), axis_angle(3), gripper(2)] = [8]` |
| Action transformer output | predicted velocity `[B, T_action, dim_action]` |
| VLM features into action transformer | `[B, T_vlm, D]` |

The `[11, 7]` expert chunk vs `[10, 7]` generated chunk is a real alignment issue to verify during implementation. The loader says the expert chunk includes current action plus future actions.

Generation currently does not accept a `seed` or `torch.Generator`. Multiple samples from the same observation are possible only by externally changing global RNG, e.g. `torch.manual_seed(...)`, before calling `generate_actions()`. A clean implementation should add `seed` or `generator` and return the seed/initial noise.

Feature exposure status:

| Feature | Current status |
|---|---|
| Generated postprocessed action | Returned by `generate_actions()`. |
| Generated normalized action | Exists as final `x_t` but not returned. |
| VLM features | Computed as `enc["vlm_features"]`, used by transformer, not returned. |
| Action transformer hidden states | Not returned. Current transformer returns velocity only, or `(velocity, logvar)` in modified code. |
| Flow timesteps | Local loop variable only. |
| Noise seed / initial noise | Not returned. |

Useful rater inputs available with small code changes:

```text
language ids / instruction
image_input [B, 3, C, H, W]
image_mask [B, 3]
proprio and proprio_norm [B, 8]
VLM features [B, T_vlm, D]
generated normalized action [B, 10, 7]
generated postprocessed action [B, 10, 7]
optional per-flow-step x_t, v_t, t
optional action-token hidden states [B, 10, H]
expert action chunk [10 or 11, 7] from HDF5
```

Needed SimVLA changes for the new branch:

1. Add `generate_actions_trace(...)` or `return_trace=True` without breaking existing callers.
2. Return normalized and postprocessed generated actions.
3. Return pooled/full VLM features.
4. Optionally modify `SmolVLMActionTransformer.forward()` to return action-token hidden states before the output head.
5. Add deterministic RNG support and store seed/initial noise.
6. Store exact timestep schedule if used by the rater or debugging.

The prior uncertainty code in `intern_ship_ws/simvla/code/SimVLA_modified` already adds `predict_uncertainty`, `uncertainty_beta`, `uncertainty_eps`, `return_uncertainty`, a logvar head, and `generate_actions_with_uncertainty(...)`. It returns `action`, `path_variance`, and `last_step_variance`. That is not the target method because it predicts uncertainty from the model head, not calibrated action error for a candidate action.

## 4. Weights and Checkpoints Audit

| Path | Size | Type | Load status |
|---|---:|---|---|
| `intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000/model.safetensors` | 3,245,557,952 bytes | SimVLA checkpoint | Full load not tested because activation is broken. |
| `intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000/config.json` | 570 bytes | HF config | Read successfully. |
| `intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000/state.json` | 22 bytes | run state | Present. |

Checkpoint config highlights:

```json
{
  "architectures": ["SmolVLMVLA"],
  "model_type": "smolvlm_vla",
  "num_actions": 10,
  "action_mode": "libero_joint",
  "hidden_size": 1024,
  "depth": 24,
  "num_heads": 16,
  "image_size": 384,
  "num_views": 3,
  "predict_uncertainty": true,
  "smolvlm_model_path": "HuggingFaceTB/SmolVLM-500M-Instruct"
}
```

Visible Hugging Face directories:

```text
intern_ship_ws/assets/models/huggingface/SimVLA-LIBERO
intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct
```

Only `.cache` metadata and a SmolVLM `onnx` directory were visible in the inspected files; full HF model weights were not visible. The best local checkpoint candidate is therefore:

```text
intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000
```

Folder names `intern_ship_ws/outputs/temp/TDQC/openpi` and `intern_ship_ws/outputs/temp/TDQC/openvla` exist, but no clearly loadable local AsyncVLA, OpenPI, pi0, OpenVLA, or ReconVLA weights were found in the lightweight audit.

## 5. Dataset Audit

LIBERO HDF5 root:

```text
intern_ship_ws/assets/data/libero_datasets
```

Counts and size:

```text
libero_10      10 files
libero_90      90 files
libero_goal    10 files
libero_object  10 files
libero_spatial 10 files
Total          130 HDF5 files
Disk usage     94G
```

Direct HDF5 opening failed because `h5py.File` was not usable in the current broken environment. The SimVLA loader confirms these expected demo keys:

```text
data/<demo>/actions             -> expert actions [T, 7]
data/<demo>/obs/agentview_rgb   -> image [T, H, W, 3]
data/<demo>/obs/eye_in_hand_rgb -> wrist image [T, H, W, 3]
data/<demo>/obs/ee_pos          -> [T, 3]
data/<demo>/obs/ee_ori          -> [T, 3], euler converted to axis-angle
data/<demo>/obs/gripper_states  -> [T, 2]
```

The loader yields:

```text
language_instruction: str
image_input: [3, C, H, W]
image_mask: [3], first two views true
proprio: [8]
abs_trajectory: [num_actions+1, 7]
```

Critical answer: for ID LIBERO, expert action chunks aligned with observations are available through the original HDF5 datasets. They should be reconstructed/loaded from HDF5, not from TDQC `.pt` files.

Important TDQC `.pt` files inspected:

| Path | Episodes | First feature shape | Expert actions/images? |
|---|---:|---|---|
| `data/v8_33d/v8_train.pt` | 22312 | `[119, 33]` | No |
| `data/v8_33d/v8_test.pt` | 2790 | `[400, 33]` | No |
| `data/v8_33d/v8_val.pt` | 2788 | not deeply printed | No |
| `data/v8_33d/v8_unseen_obj_ood.pt` | 2212 | `[112, 33]` | No |
| `data/v8_balanced/v8_train.pt` | 22312 | `[119, 22]` | No |
| `data/v8_balanced/v8_unseen_obj_ood.pt` | 2212 | `[112, 22]` | No |
| `data/v7_22d/v7_22d_test.pt` | 3942 | `[400, 22]` | No |
| `data/goal_object_ood/v7_22d_ood.pt` | 450 | `[120, 22]` | No |
| `data/libero_object_object_new/v7_22d_ood.pt` | 500 | `[400, 22]` | No |

Representative `.pt` episode keys:

```text
features: Tensor [T, F]
success: bool
task_id: int
episode_idx: int
task_suite: str
instruction: str
```

They do not include images, robot states, expert action chunks, generated SimVLA actions, VLM hidden states, or action-transformer hidden states.

OOD summary found:

```text
intern_ship_ws/ood_data/libero_object_object_new/ckpt-60000/collection_summary.json
```

Summary values:

```json
{
  "jobs": 50,
  "jobs_ok": 50,
  "valid_episodes": 500,
  "success": 450,
  "failure": 50,
  "by_task": {
    "0": {"episodes": 50, "success": 13, "failure": 37},
    "1": {"episodes": 50, "success": 50, "failure": 0},
    "2": {"episodes": 50, "success": 47, "failure": 3}
  }
}
```

Critical answer: OOD rollout/evaluation data exists, but OOD expert demonstrations with aligned expert actions were not confirmed. The current OOD `.pt` files are uncertainty-feature rollouts, not raw demonstration datasets.

## 6. Previous Experiment Audit

Important experiment folders:

| Path | Summary |
|---|---|
| `intern_ship_ws/simvla/code/SimVLA_modified` | Prior phase-1 SimVLA uncertainty head/logvar implementation. |
| `intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000` | Local modified SimVLA checkpoint. |
| `intern_ship_ws/outputs/eval/*` | LIBERO evaluation JSONs and uncertainty traces. |
| `intern_ship_ws/tdqc/code/phase2_tdqc_standalone` | TDQC standalone training/eval/data. |
| `intern_ship_ws/tdqc/code/phase2_tdqc_standalone/data/v8_33d` | 33D TDQC datasets including unseen-object OOD. |
| `experiments/v8_exp10_33d` | Root experiment capsule. |
| `intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/c_hardcore_50` | Current untracked TDQC eval scripts/results. |

Prior SimVLA uncertainty returns variance-like tensors:

```text
generate_actions_with_uncertainty(...) -> {
  "action": action,
  "path_variance": path_variance,
  "last_step_variance": last_step_variance
}
```

TDQC features were built from handcrafted aggregates of those uncertainty traces: mean/std/max path variance, last-step variance, gripper variance, denoise initial/final summaries, and later 22D/33D variants. Code paths include `build_dataset_v7.py`, `tdqc_features.py`, `train_tdqc.py`, and `eval_tdqc.py`.

Evidence of failure pattern: `experiments/c_hardcore_50/eval_results_1_50.json` showed degenerate warning behavior:

```json
{
  "1": {"Recall": 100.0, "FPR": 100.0, "LeadTime": 399.99, "StartConf": 40.17, "EndConf": 29.71},
  "2": {"Recall": 100.0, "FPR": 100.0, "LeadTime": 394.92, "StartConf": 58.37, "EndConf": 63.98}
}
```

That means the detector can warn on everything: high recall and 100% false-positive rate. This supports replacing TDQC with a candidate-action error rater.

Reusable artifacts: SimVLA code, LIBERO HDF5 data, checkpoint config/checkpoint after environment repair, TDQC metric/logging conventions, and OOD rollout metadata. Not reusable as direct rater training data: `v8_33d`, `v8_balanced`, and `v7_22d` `.pt` datasets, because they lack raw observations/actions/internal features.

## 7. Feasibility of the New Method

| Step | Status | Files involved | Risks / missing work |
|---|---|---|---|
| A. Load SimVLA checkpoint | Partially ready | `outputs/runs/simvla_libero_uncertainty/ckpt-60000` | Env activation broken; load test blocked. |
| B. Generate action chunk | Partially ready | `models/modeling_smolvlm_vla.py` | Need deterministic seed/generator and trace API. |
| C. Retrieve expert chunk | Ready for ID LIBERO | `assets/data/libero_datasets`, `libero_hdf5.py` | Align `[11,7]` expert chunks with `[10,7]` generated chunks. |
| D. Compute action error | Partially ready | action_space/norm stats | Decide normalized vs postprocessed target. |
| E. Save rater dataset | Missing | new `asynchvla_ws/data/features` | Need schema and shard format. |
| F. Train rater | Missing | new `src/rater` | Must condition on candidate action, not only image. |
| G. Calibrate | Missing | new `src/calibration` | Need calibration split and bound definition. |
| H. Evaluate ID/OOD | Partially ready | ID HDF5 ready; OOD rollouts partial | OOD expert actions unclear. |
| I. Same-image wrong-action tests | Partially ready | ID ready; OOD unclear | Need normalization-safe wrong action construction. |

Conclusion: the method is feasible immediately for ID LIBERO after environment repair and trace extraction. OOD claims require finding or building OOD expert demonstrations.

## 8. OOD-Specific Feasibility

The desired anti-OOD-detector test is:

```text
same OOD observation + correct expert action -> low uncertainty
same OOD observation + SimVLA action -> uncertainty tracks actual error
same OOD observation + deliberately wrong action -> high uncertainty
same OOD observation + action from another trajectory -> high uncertainty
```

For ID LIBERO, this is straightforward because HDF5 demos provide observation, language, state, and expert action chunks. For OOD, this is not ready from the inspected files. `v8_unseen_obj_ood.pt` and `libero_object_object_new/v7_22d_ood.pt` contain feature sequences and success labels, not expert chunks/images/states.

Safe wrong-action candidates:

```text
same task, different timestep far away
same scene/task, different trajectory action chunk
different task action chunk
controlled normalized-space perturbation of expert action
SimVLA samples from different seeds, labeled by actual expert distance
```

Metrics to use:

```text
risk-coverage curve
Spearman/Pearson correlation between predicted uncertainty and action error
AUROC for bad-action detection after thresholding true error
calibration/coverage of predicted action-error bound
OOD low-vs-high uncertainty action error
same-image contrastive ranking accuracy
```

## 9. Recommended New Workspace Layout

Recommended path:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws
```

The name is acceptable. If clarity matters, `asyncvla_simvla_ws` would communicate that this is AsyncVLA-inspired rather than a literal AsyncVLA reimplementation.

Proposed layout:

```text
asynchvla_ws/
  README.md
  configs/
  scripts/
  src/
  src/simvla_trace/
  src/rater/
  src/calibration/
  src/eval/
  data/
  data/features/
  data/calibration/
  outputs/
  outputs/logs/
  outputs/checkpoints/
  outputs/reports/
```

Recommendation: make it a small Python package plus scripts. Import SimVLA from the existing code path during development; for production experiments, follow the capsule rule and copy exact code snapshots into experiment folders. Reuse/fix the existing SimVLA env first. If a new env is required, it needs `torch`, `transformers`, `safetensors`, `numpy`, `scipy`, `scikit-learn`, `h5py`, `pandas`, `tqdm`, `robosuite`, `libero`, `Pillow`, and `torchvision`.

## 10. Implementation Risks and Missing Information

Ready:

```text
Bob reachable; branch is bob.
ID LIBERO HDF5 data present: 130 files / 94G.
SimVLA flow-matching code present.
Prior SimVLA_modified uncertainty branch present.
Local ckpt-60000 exists.
TDQC datasets/eval logs exist for failure-pattern context.
```

Missing or blocked:

```text
activate_simvla.sh fails on Bob.
Full checkpoint load not verified.
Direct HDF5 key dump blocked by broken h5py environment.
OOD expert demonstrations with aligned expert actions not found.
Current generation does not return normalized actions, hidden features, seeds, or transformer hidden states.
TDQC .pt files do not contain raw observations/actions needed for the new rater.
```

Risks:

```text
expert chunk [num_actions+1,7] vs generated chunk [num_actions,7]
normalized vs postprocessed error target inconsistency
huge storage if saving full VLM token features for every timestep
feature leakage from timestep/progress repeating TDQC failure
OOD evaluation degenerating into OOD detection if no same-image action contrasts exist
fragile global RNG for multiple SimVLA samples
```

Decisions before implementation:

```text
Use baseline SimVLA or SimVLA_modified as trace source. Recommendation: SimVLA_modified for checkpoint compatibility, but keep the new rater separate.
Define error target: normalized action-space L2 per step, with postprocessed metrics also logged.
Choose candidate-action representation: full [10,7] chunk plus pooled VLM features/proprio.
Choose feature storage: pooled VLM first, full token features only if needed.
Find/generate OOD expert demos before claiming anti-OOD behavior.
Repair environment activation first.
```

Next commands to run after this audit:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
find /home/rootalkhatib /home/redafrix intern_ship_ws/assets/envs -maxdepth 4 -name python -o -name activate -o -name conda
sed -n '1,80p' intern_ship_ws/activate_simvla.sh
# after env repair:
python -c "import torch; print(torch.__version__, torch.cuda.is_available(), torch.version.cuda)"
python -c "from models.modeling_smolvlm_vla import SmolVLMVLA; m=SmolVLMVLA.from_pretrained('intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000'); print('loaded')"
python -c "import h5py; f=h5py.File('<one_libero_hdf5>'); print(list(f['data'].keys())[:1])"
```

## 11. Final Recommendation

Best checkpoint:

```text
intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000
```

Best dataset start:

```text
Use ID LIBERO HDF5 under intern_ship_ws/assets/data/libero_datasets with trajectory-level or task-level splits. Use TDQC v8 OOD files only as context until raw OOD expert demos are found.
```

OOD expert actions: not confirmed. OOD rollout feature datasets exist, but raw OOD expert demonstrations with aligned expert chunks were not found.

Feasibility: the action-error rater is feasible for ID immediately after environment repair and trace API implementation. OOD anti-detector evaluation is partially feasible and depends on finding/generating OOD expert demonstrations.

Create `asynchvla_ws`: yes, after implementation begins. Keep it separate from SimVLA and import existing code rather than copying immediately.

Reuse env or new env: repair/reuse existing SimVLA env first. Create a new env only if the current one cannot be recovered cleanly.

First five implementation steps, not executed here:

1. Fix and verify SimVLA activation on Bob.
2. Load `ckpt-60000` in a short smoke test.
3. Add a non-breaking trace generation API returning normalized action, postprocessed action, VLM features, optional transformer features, seed, and flow metadata.
4. Extract a tiny LIBERO trace dataset and verify observation/expert/generated alignment.
5. Train/evaluate a first same-image candidate-action rater on a small ID split before making OOD claims.

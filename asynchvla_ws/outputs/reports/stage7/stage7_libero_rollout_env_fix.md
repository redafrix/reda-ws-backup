# Stage 7 — LIBERO Rollout Environment Fix

- Timestamp: `2026-05-15 11:13` (Bob)
- Status: **UNBLOCKED.** Real LIBERO `OffScreenRenderEnv` instantiates, resets, and `env.step()` returns observation/reward/done on Bob.

## Smoke test (proved end-to-end)

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
export LIBERO_CONFIG_PATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/configs/libero_bob"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
python3 asynchvla_ws/src/eval_stage7/check_libero_rollout_env.py \
    --suite libero_spatial --task-id 0 --resolution 128 \
    --out asynchvla_ws/outputs/reports/stage7/stage7_libero_rollout_env_check.json
```

Returns blockers=[], smoke.ok=true. Task language: *"pick up the black bowl between the plate and the ramekin and place it on the plate"*. Image shape `(128, 128, 3)`. First `OffScreenRenderEnv()` instantiate ≈ 2.4 s, first `env.step()` ≈ 4.0 s (subsequent steps will be cheaper after JIT/MuJoCo warmup). EGL teardown emits a harmless cleanup warning at process exit — not a functional issue.

## What changed in the environment

Installed into `/home/rootalkhatib/envs/simvla/lib/python3.10/site-packages` via `pip install --target=...`:

| Package | Version | Notes |
|---|---|---|
| `robosuite` | 1.4.0 | LIBERO requirements pin; works against numpy 2.x via `--no-deps` |
| `mujoco` | 3.8.1 | Native python bindings (not `mujoco-py`) |
| `bddl` | 3.6.0 | BDDL problem files |
| `einops` | 0.8.2 | LIBERO/SimVLA |
| `hydra-core` | 1.3.2 | LIBERO lifelong train scripts (optional for rollout) |
| `omegaconf` | 2.3.0 | hydra dep |
| `antlr4-python3-runtime` | 4.9.3 | hydra dep (must be 4.9.x, not 4.13.x) |
| `easydict` | 1.13 | LIBERO config helpers |
| `robomimic` | 0.3.0 | LIBERO lifelong train (optional for rollout) |
| `numba` | 0.65.1 | `robosuite.utils.transform_utils` JIT |
| `llvmlite` | 0.47.0 | numba |
| `coverage` | 7.14.0 | numba 0.65 needs `coverage.types` (system 6.2 too old) |
| `PyOpenGL` / `PyOpenGL-accelerate` | 3.1.10 | EGL bindings for `mujoco.egl` |
| `glfw` | 2.10.0 | optional GL window for human render |
| `absl-py` | 2.4.0 | mujoco dep |
| `etils[epath]` | 1.13.0 | mujoco dep |

All installs used `--no-deps` to avoid pulling an older numpy/transformers that would break the rest of the Stage 7 codebase. The running extra-OOD `python3` already had its imports cached so it was not disturbed. `numpy` stayed at `2.2.6`, `torch` at `2.5.1+cu121`, `transformers` at `4.57.6`.

## LIBERO config

The existing `intern_ship_ws/simvla/config/libero/config.yaml` points to a Batman path that does not exist on Bob. I left it untouched (per "do not delete old work") and wrote a Bob-local override:

```yaml
# asynchvla_ws/configs/libero_bob/config.yaml
benchmark_root: /media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/data/LIBERO/libero/libero
bddl_files:     /media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/data/LIBERO/libero/libero/bddl_files
init_states:    /media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/data/LIBERO/libero/libero/init_files
datasets:       /media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/data/LIBERO/libero/libero/../datasets
assets:         /media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/data/LIBERO/libero/libero/assets
```

Rollout scripts must set `LIBERO_CONFIG_PATH` to this directory.

## `openpi_client` decision

Not installed — not required for rollout. The websocket bridge in `evaluation/libero/libero_client.py` is only used to talk to a separate `serve_smolvlm_libero.py` policy server. We will run an **in-process** rollout in `asynchvla_ws/src/eval_stage7/libero_execution_uncertainty_eval.py` that loads SimVLA directly and steps the env in the same Python process. This avoids the websocket layer entirely and the `image_tools`/`websocket_client_policy` deps.

## Environment variables required at rollout time

```
LIBERO_CONFIG_PATH=/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/configs/libero_bob
MUJOCO_GL=egl
PYOPENGL_PLATFORM=egl
```

If headless EGL fails on a future re-launch, fall back to `MUJOCO_GL=osmesa` (would require installing `osmesa`).

## Remaining risks for rollout

1. **GPU contention.** Bob GPU is currently 87% utilised by the extra-OOD job. Tiny rollout must wait until that job releases the GPU, or be limited to CPU-only forward (SmolVLM is too large for that to be practical).
2. **SimVLA in-process load.** Need to import `models.modeling_smolvlm_vla.SmolVLMVLA` from `intern_ship_ws/simvla/code/SimVLA_modified/`. PYTHONPATH already includes that dir.
3. **State+action dim alignment.** Rollout server uses `state_dim=8, action_dim=7, action_horizon=10`. The Stage 5/6 rater was trained on `libero_joint` SimVLA candidate features. Need to confirm that the production action format produced by SimVLA's predict path matches what the env expects (delta xyz / axis-angle / gripper).
4. **No real-time progress signal.** LIBERO returns `(obs, reward, done, info)`; reward is essentially 0 until success at the final step in most tasks. We will rely on rater uncertainty traces vs final binary success and a heuristic "TCP-pose to goal-region" distance derived from `_pos`/`_quat` obs entries, not on an explicit progress scalar.

## Next action

Phase 4 tiny rollout cannot start until the GPU is free. While waiting, Phase 1 metrics and Phase 6 multi-expert target build (CPU-bound) proceed.

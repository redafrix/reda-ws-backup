# Stage 7 Claude Resume-State Audit

- Timestamp: `2026-05-15 11:05` (Bob local)
- Operator: Claude session resuming Stage 7 from prior Codex session.
- Active machine: Bob (`pcrobot`, `PCROBOTUBUNTU02`), branch `bob`.
- Standby machine: Sam (`PCROBOTUBUNTU05`), branch `sam`, model-sync incomplete (resume launched, see below).

## Bob — process and GPU state

- `nvidia-smi`: RTX 4070 Ti SUPER, 6807 MiB / 16376 MiB used, **87% GPU util**. Active CUDA process is PID `466026` (`python3 build_multiseed_trace_dataset.py ... --split-name holdout_libero_goal ...`).
- Wrapper: PID `466022` (`bash extra_ood_completion_bob_job.sh`) launched at `13:29 elapsed ≈ 1h35m`.
- `git status --short`: existing Stage 5/6/7 reports and code (flow-trace addition, `simvla_trace/trace.py` modified, `calibrate_stage7_repair.py`, `data_building/build_flowtrace_multiseed_dataset.py`, `src/eval_stage7/libero_execution_uncertainty_eval.py`, `src/rater_stage6/`, `src/features_stage7/`). No accidental deletions; branch `bob` clean of unwanted changes.

## Extra controlled-OOD job — is it running?

YES — still running, on **first** split `holdout_libero_goal`. Sequencing inside `extra_ood_completion_bob_job.sh`:
1. `build_multiseed_trace_dataset.py` → trace_train.pt, trace_calib.pt, trace_test_id.pt, trace_test_ood.pt
2. `build_multiseed_candidate_dataset.py`
3. `run_stage6_experiments.py` with variants `action_only_baseline full_old_baseline context_gated_action`, `--out-prefix stage7_extra_<split>`

Three splits scheduled in this order: `holdout_libero_goal`, `holdout_scene_kitchen_scene2`, `holdout_object_cabinet`.

Progress so far (file mtimes inside `data/processed_stage5/holdout_libero_goal/`):

| File | size | mtime |
|---|---|---|
| `manifest_used.json` | 23,011 | 10:49 |
| `multiseed_trace_train.pt` | 13,273,090 | 10:58 |
| `multiseed_trace_calib.pt` | 3,311,800 | 11:01 |
| `multiseed_trace_test_id.pt` | (in progress) | n/a |

Log tail at `outputs/logs/stage7/extra_ood_completion_bob.log`: at line ~245, currently `test_id collected 100`. No error.

Rough timing (extrapolated): train 200ctx/min → split-build ≈ 18–25 min; full pipeline per split (build + candidates + experiments@80 epochs) ≈ 60–90 min. 3 splits ≈ 3–4 hours total. Expected completion **~13:30–14:30 Bob time** unless OOM or expert-pool failures.

## Sam — readiness

- Tailscale reachable, SSH OK from Bob via `100.112.19.30`.
- SmolVLM directory on Sam: 478 MB; `model.safetensors` 479,232,000 bytes. Bob is 1023 MB with `model.safetensors` 1,015,025,832 bytes. **Sync is incomplete by ~537 MB.**
- Resume launched: `nohup /tmp/sam_smolvlm_sync.sh` (rsync `-a --partial --inplace --info=progress2` Bob→Sam) → PID `476317`, log `outputs/logs/stage7/sam_smolvlm_sync.log`. Running at ~10 MB/s; ETA ≈ 1 min.
- Sam GPU is idle (3645 MiB resident, 0% util — desktop xorg only).

## Stage 7 reports already present (Bob)

```
outputs/reports/stage7/
  stage7_calibration_repair.md
  stage7_extra_ood_completion.md
  stage7_flow_trace_features.md
  stage7_history_models.md
  stage7_isaac_sim_data_plan.md
  stage7_libero_execution_eval.md
  stage7_libero_pro_feasibility.md
  stage7_parallel_jobs_status.md
  stage7_parallel_setup.md
  stage7_target_comparison.md
```

Local duplicates at `/home/redafrix/tests/internship/codex_reports/stage7/` are in sync with above (verified).

## Stage 5/6 datasets present

```
data/processed_stage5/
  holdout_libero_goal/      (extra-OOD job in progress)
  holdout_libero_object/    (Stage 5 baseline)
  holdout_libero_spatial/
  holdout_object_bowl/
  id_task_split/
```

Stage 6 checkpoints exist for: `holdout_libero_object`, `holdout_libero_spatial`, `holdout_object_bowl`, `id_task_split`. Variants per split include: `action_only_baseline`, `full_old_baseline`, `context_only_baseline`, `context_gated_action`, `full_engineered_mlp`, `full_engineered_simvla_focused`, `per_step_error_head`, `seed_relative_pairwise`, `seed_relative_rater`, `seed_relative_simvla_focused`.

Split manifests exist for many extra holdouts: `holdout_object_basket/book/cabinet/drawer/plate/scene2`, `holdout_scene_kitchen_scene{1..10}`, `holdout_scene_living_room_scene{1..6}`, `holdout_scene_study_scene{1,2}`, `holdout_libero_10/90`.

## LIBERO rollout import status

Under `activate_simvla_bob.sh`:

| Package | Status |
|---|---|
| `libero` | True (via PYTHONPATH) |
| `libero.libero` | True |
| `robosuite` | **False** — blocker |
| `openpi_client` | False — only needed for websocket client; in-process fallback feasible |
| `openpi` | False |
| `mujoco` | False — robosuite needs it |
| `hydra` | False (LIBERO config-driven scripts will need it) |
| `imageio` | True |
| `msgpack_numpy` | True |

`intern_ship_ws/assets/data/LIBERO/requirements.txt` lists:

```
hydra-core==1.2.0, numpy==1.22.4, wandb==0.13.1, easydict==1.9, transformers==4.21.1,
opencv-python==4.6.0.66, robomimic==0.2.0, einops==0.4.1, thop==0.1.1-2209072238,
robosuite==1.4.0, bddl==1.0.1, future==0.18.2, matplotlib==3.5.3, cloudpickle==2.1.0,
gym==0.25.2
```

`serve_smolvlm_libero.py` (server side) does not need `openpi_client`. Only `libero_client.py` uses it through `WebSocketClient`. A direct in-process loop (server module + client loop in one process, skipping websocket) bypasses `openpi_client`.

The mandatory installs to unblock rollout: `robosuite==1.4.0`, `mujoco`, `bddl==1.0.1`, plus the small helpers (`hydra-core`, `robomimic`, `easydict`, `cloudpickle`, `gym==0.25.2`, `future`). Most are pure-python or cython wheels that target the current site-packages without sudo. Risks: numpy pinning (`numpy==1.22.4`) is older than current env; will pin only if torch already depends on it.

## What should run next

1. **Phase 0 reported** (this file).
2. While Bob GPU is busy with extra-OOD job, do CPU/IO tasks:
   - Continue Sam SmolVLM sync (running).
   - Install `robosuite` / `mujoco` / `bddl` / `gym` / `hydra-core` into Bob env (`/home/rootalkhatib/envs/simvla/lib/python3.10/site-packages`). User-space pip with `--prefix` or `--target`. **Do not touch the running job's Python imports** — those are already cached in memory.
   - Write `asynchvla_ws/src/eval_stage7/check_libero_rollout_env.py` (smoke import + minimal OffScreenRenderEnv instantiation).
   - Plan multi-expert min-distance target script (pure-CPU after candidates exist).
3. Once extra-OOD job finishes (or per-split when each completes):
   - Collect metrics: SimVLA-only pairwise, switch proxy gap, AUROC top-30 bad, action-only vs full_old vs context_gated_action.
   - Write `stage7_extra_ood_completion_final.md`.
4. Once GPU is free:
   - Run flow-trace experiment (`holdout_libero_object`).
   - Run multi-expert min-distance target training/eval.
   - Calibration follow-up.
   - LIBERO tiny rollout if Phase 3 succeeded.
5. Skip history models until/unless real sequence logs exist (Phase 4 rollout output).
6. Skip Isaac Sim per stated rule.

## Open risks / blockers

- `robosuite` install may pull an incompatible numpy version against torch in the active env; pin install order to avoid disturbing the running build job (which uses cached imports anyway).
- `mujoco` and EGL rendering on Bob — needs to confirm offscreen GL works on this box. The `OffScreenRenderEnv` uses MuJoCo's OSMesa/EGL backends. If EGL fails, fall back to OSMesa.
- Network speed Bob→Sam: ~10 MB/s. SmolVLM resume looks fine.
- No real-time progress signal is exposed by LIBERO OffScreenRenderEnv beyond reward shaping; success is binary at end. Multi-expert and uncertainty will use existing target proxies + final success.

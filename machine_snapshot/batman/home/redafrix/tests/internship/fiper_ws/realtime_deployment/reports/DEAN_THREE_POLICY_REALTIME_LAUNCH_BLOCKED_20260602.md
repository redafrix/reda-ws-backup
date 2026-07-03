# Dean Three-Policy Realtime Launch Blocked (2026-06-02)

## Goal

Compare three policies on the same reset seeds for one seen and one held-out task from the Dean uncertainty dataset:

- `simvla_only`: checkpoint `ckpt-60000`, no risk model.
- `risk_base`: current Dean OOD split base transformer detector.
- `risk_unc_topk8`: current Dean OOD split transformer detector with top-8 uncertainty static features.

## Active Model Canonicalization

Canonical current models were copied on Dean to:

- `/home/dean/fiper_uncertainty_collection/experiments/current_dean_risk_models_20260602/ood_last2_taskids_full/base`
- `/home/dean/fiper_uncertainty_collection/experiments/current_dean_risk_models_20260602/ood_last2_taskids_full/unc_topk8`
- `/home/dean/fiper_uncertainty_collection/experiments/current_dean_risk_models_20260602/all_tasks_full/base`
- `/home/dean/fiper_uncertainty_collection/experiments/current_dean_risk_models_20260602/all_tasks_full/unc_topk8`

Rejected/non-active uncertainty ideas were moved to:

- `/home/dean/fiper_uncertainty_collection/experiments/archive/rejected_uncertainty_ideas_20260602`

## Realtime Files Created

Local and Dean script:

- `fiper_ws/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py`
- `/home/dean/fiper_uncertainty_collection/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py`

Configs:

- `fiper_ws/realtime_deployment/configs/dean_three_policy_seen_object_task7_100eps_20260602.json`
- `fiper_ws/realtime_deployment/configs/dean_three_policy_unseen_object_task8_100eps_20260602.json`
- synced to `/home/dean/fiper_uncertainty_collection/realtime_deployment/configs/`

Selected tasks:

- seen: `libero_object_object`, task `7`
- unseen/held-out last2: `libero_object_object`, task `8`

Each task config contains 100 unique reset seeds. The three policies use the same seed list within a task.

## Critical Bug Found And Fixed

Initial smokes showed a confound:

- unseen `simvla_only`: timeout at 300 steps.
- unseen `risk_base`: success with `mods=0`.
- unseen `risk_unc_topk8`: success with `mods=0`.

That is invalid because a risk policy with zero modifications must reproduce the baseline. Cause: the main action was generated inside a batch of 9 samples for risk policies, while baseline generated it alone. Batched diffusion sampling can change sample 0 enough to alter the rollout.

Patch applied:

- Generate the main chunk alone for every policy.
- Generate the 8 ACE candidates separately for risk policies.
- Recombine `[main + ACE]` only after generation.
- Recompute group-level sample-spread uncertainty features over the combined candidate set.

After patch, unseen smoke on reset seed `379147613` became sane:

- `simvla_only`: timeout, 300 steps, 0 modifications.
- `risk_base`: timeout, 300 steps, 6 modifications.
- `risk_unc_topk8`: timeout, 300 steps, 11 modifications.

So the previous false success was removed.

## Blocker

During the final patched seen-task smoke, Dean stopped responding:

- `ssh dean`: timeout
- `ssh -i /home/redafrix/tests/internship/id_dean dean@100.124.50.124`: timeout
- `ping 100.124.50.124`: 100% packet loss
- `tailscale ping 100.124.50.124`: no reply

The long 100-episode campaign was **not launched** because Dean cannot be monitored or stopped safely while unreachable.

## Resume Instructions When Dean Returns

First archive/remove smoke-contaminated run directories before the full run:

```bash
ssh dean "cd /home/dean/fiper_uncertainty_collection && mkdir -p realtime_deployment/runs/archive/prelaunch_smokes_20260602 && mv realtime_deployment/runs/dean_three_policy_seen_object_task7_100eps_20260602 realtime_deployment/runs/dean_three_policy_unseen_object_task8_100eps_20260602 realtime_deployment/runs/archive/prelaunch_smokes_20260602/ 2>/dev/null || true"
```

Then re-run one patched smoke for `risk_base` and `risk_unc_topk8` on the seen config.

If Dean remains healthy, launch two tmux orchestrators, one per task, each running:

1. `simvla_only`
2. `risk_base`
3. `risk_unc_topk8`

Use `/home/redafrix/miniconda3/envs/simvla/bin/python`; system `python3` on Dean does not have PyTorch.

## Do Not Trust

Do not use any smoke outputs written before this report as final results. They are setup/smoke artifacts only.

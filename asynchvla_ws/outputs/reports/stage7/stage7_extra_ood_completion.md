# Stage 7 Extra Controlled-OOD Completion

## Status

The remaining controlled-OOD completion was launched on Bob via `nohup`, not directly in the main shell.

Command:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
bash asynchvla_ws/scripts/stage7_parallel_job_launcher.sh extra-ood-bob
```

Log:

- `asynchvla_ws/outputs/logs/stage7/extra_ood_completion_bob.log`

Splits scheduled:

- `holdout_libero_goal`
- `holdout_scene_kitchen_scene2`
- `holdout_object_cabinet`

Dataset/eval size:

- train contexts: `1000`
- calib contexts: `250`
- test_id contexts: `250`
- test_ood contexts: `250`
- seeds: `0 1 2 3 4`
- cap per file: `20`

## Current Progress

At report time, `holdout_libero_goal` trace extraction was running and had collected at least 200 train contexts. Final candidate counts and metrics are pending job completion.

## Required Metrics After Completion

For each split, read the generated Stage 7 reports and record:

- SimVLA-only pairwise seed ranking.
- Improvement over seed0.
- Switch proxy accepted/rejected true-error gap.
- Calibration coverage.
- Whether `context_gated_action` still beats `action_only_baseline`.

## Current Limitation

Sam is not yet model-ready because SmolVLM backbone sync is incomplete, so this job currently runs only on Bob.

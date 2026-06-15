# Three-Policy Task 0 100-Episode Launch Supervision (2026-06-03)

## Objective

Compare three realtime policies on the same task and the same 100 reset seeds:

- `simvla_only`: modified SimVLA checkpoint `ckpt-60000`, no risk detector.
- `risk_base`: modified SimVLA checkpoint plus all-tasks base risk detector.
- `risk_unc_topk8`: modified SimVLA checkpoint plus all-tasks uncertainty top-8 risk detector.

Chosen task:

- suite: `libero_object_object`
- task_id: `0`
- reason: historical Dean data showed a usable hard seen task with both successes and failures.

## Critical Fixes Applied

- Stopped relying on Gemini's local `/tmp` staging transfer path for multi-GB assets.
- Pulled `ckpt-60000` and SmolVLM assets Dean -> Bob directly from a Bob tmux transfer.
- Patched `run_dean_uncertainty_realtime_policy_v1.py` so it can import the collector from the script directory, not only Dean's hardcoded source path.
- Mirrored `collect_fiper_uncertainty_receding_dean_v1.py` into Dean/Bob deployment script directories.
- Copied SmolVLM snapshot files into Bob's expected HuggingFace cache layout and reran Bob smoke with `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`.

## Artifact Verification

- Bob checkpoint SHA256:
  - `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`
- Bob SmolVLM model file:
  - `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/smolvlm_cache/model.safetensors`
  - size: `1015025832`
- Bob expected HF snapshot also populated:
  - `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/models/huggingface/.hf_home/transformers/models--HuggingFaceTB--SmolVLM-500M-Instruct/snapshots/a7da5b986cb59b408707209984f360a5f4ad7e47`
- Detector feature audit from embedded `metrics.json`:
  - base static dim: `43`
  - unc_topk8 static dim: `51`
  - unc_topk8 dims: `[6, 21, 25, 27, 23, 2, 26, 24]`
  - no reward/success/future timestep/task metadata inputs reported.

## Smoke Results

Dean smoke config:

- `/home/dean/fiper_uncertainty_collection/realtime_deployment/configs/dean_three_policy_seen_object_task0_smoke_dean_20260603.json`

Dean smoke results:

- `risk_unc_topk8`: 300 steps, `failure_or_timeout`, 7 modifications, seed collisions 0, main/ACE collisions 0.
- `simvla_only`: 300 steps, `failure_or_timeout`, no ACE/risk path, no error.

Bob smoke config:

- `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/configs/bob_three_policy_seen_object_task0_smoke_20260603.json`

Bob smoke result:

- `risk_base`: 162 steps, `success`, 1 modification, seed collisions 0, main/ACE collisions 0.

## Full Runs Launched

Dean:

- `simvla_only`
  - tmux: `dean_task0_simvla_only_20260603`
  - log: `/home/dean/fiper_uncertainty_collection/realtime_deployment/logs/three_policy_task0_20260603/simvla_only.log`
- `risk_unc_topk8`
  - tmux: `dean_task0_risk_unc_topk8_20260603`
  - log: `/home/dean/fiper_uncertainty_collection/realtime_deployment/logs/three_policy_task0_20260603/risk_unc_topk8.log`

Bob:

- `risk_base`
  - tmux: `bob_task0_risk_base_20260603`
  - log: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/logs/three_policy_task0_20260603/risk_base.log`

Sam:

- unavailable by SSH at launch time; not used.

## Current Verified Progress

Last checked after launch:

- Dean `simvla_only`: 12 completed episodes.
  - last: episode 11, seed `590370725`, `success`, 185 steps, seed collisions 0.
- Dean `risk_unc_topk8`: 4 completed episodes.
  - last: episode 3, seed `1521263274`, `success`, 123 steps, 1 modification, seed collisions 0.
- Bob `risk_base`: 1 completed episode.
  - last: episode 0, seed `677580737`, `success`, 162 steps, 1 modification, seed collisions 0.

## Caveats

- Bob still has an orphan GPU allocation (`[Not Found]`, about 3158 MiB), but the `risk_base` run loaded and stepped successfully with enough free memory.
- Dean A5000 is running two full policies concurrently at 100 percent GPU and reached about 85 C; this is high but currently functioning.
- Sam is offline, so the practical deployment is two hosts and three active policies, not three hosts.

# Dean Collection and Remote Campaign Worklog - 2026-05-29

## Objective

Set up Dean for long-running FIPER-style data collection using the modified SimVLA uncertainty model, with 49D uncertainty features plus 49D temporal deltas, then verify Dean is collecting healthily. After that, audit the existing Sam/Bob risk-aware rollout campaign without interrupting it.

## User Requirements

- Dean collection must use modified SimVLA uncertainty checkpoint, not a baseline checkpoint.
- Collection should be LIBERO-PRO only, using the generic object perturbation.
- Include all available suite families, including LIBERO-90, excluding LIBERO-100.
- Collection schedule should be sequential round-robin: one episode for every task of every selected suite, then loop back.
- Record the same trusted FIPER-style data as the current dataset, plus uncertainty 49D features and 49D deltas.
- Use Dean GPU aggressively but correctly; run enough workers to maximize throughput without breaking the environment.
- Keep this worklog updated after every substantive step so another session can resume safely.
- Do not interrupt Sam/Bob campaigns unless a real mistake requires a fix.

## Current Plan

1. Audit Dean/Bob checkpoint locations and recover the correct uncertainty checkpoint directly from Bob to Dean if needed.
2. Verify Dean environment, LIBERO-PRO object suite availability, and collector dependencies.
3. Build/adapt the trusted FIPER collector for uncertainty features.
4. Run tiny and multi-episode smoke tests on Dean.
5. Launch long-running Dean collection in tmux/nohup with logs and status files.
6. Audit Sam/Bob 4-worker risk-aware campaign health and correctness.
7. Write final status and monitoring commands.

## Step Log

### Step 0 - Worklog Created

- Created this persistent worklog at `fiper_ws/reports/DEAN_COLLECTION_AND_REMOTE_CAMPAIGN_WORKLOG_20260529.md`.
- Next: audit remote access guide and current checkpoint transfer state.

### Step 1 - Remote Guide and Checkpoint State Audited

- Read `REMOTE_EXPERIMENT_GUIDE.md`; Dean is reachable as user `dean` at `100.124.50.124`, Bob is `pcrobot`/`100.105.217.20`.
- Dean GPU is idle: NVIDIA RTX A5000, 24,564 MiB VRAM, 15 MiB used.
- Dean local uncertainty checkpoint inventory:
  - `ckpt-60000`: has `config.json` and `state.json`, missing `model.safetensors`.
  - `ckpt-80000`: has `model.safetensors`, `config.json`, `state.json`; config has `predict_uncertainty=true`, LoRA enabled.
  - `ckpt-110000`: has `model.safetensors`, `config.json`, `state.json`; config has `predict_uncertainty=true`, LoRA enabled.
- Bob has the exact intended `ckpt-60000` full checkpoint at `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000`.
- Bob `ckpt-60000/model.safetensors` size: `3245557952` bytes.
- Bob `ckpt-60000/model.safetensors` sha256: `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`.
- Verified Dean can SSH directly into Bob using `/home/dean/.ssh/id_tmp_bob` and can resolve Bob symlink `/tmp/ckpt60k_link`.
- Next: transfer Bob `ckpt-60000` directly to Dean without passing through local filesystem, then verify checksum.

### Step 2 - Checkpoint Transfer Attempt and Permission/Connectivity Issues

- Direct Dean-to-Bob rsync into `/home/redafrix/SimVLA_modified/.../ckpt-60000` failed because SSH user `dean` cannot write into `/home/redafrix` owned folders.
- Dean has no passwordless sudo (`sudo -n true` requires a password), so the safe writable checkpoint destination is `/home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000`.
- Retried direct Dean-to-Bob rsync to the Dean-owned checkpoint path; transfer speed over Bob Tailscale was unusably slow (~100 KB/s).
- Stopped stale checkpoint rsync/scp processes on Dean and removed partial checkpoint files.
- After the transfer attempts, Bob became temporarily unreachable from Batman by both Tailscale alias `pcrobot` and local IP `172.16.8.104`; Sam and Dean remain reachable.
- Dean already has complete local modified uncertainty checkpoints:
  - `/home/redafrix/SimVLA_modified/runs/simvla_libero_uncertainty/ckpt-80000`
  - `/home/redafrix/SimVLA_modified/runs/simvla_libero_uncertainty/ckpt-110000`
- Both local Dean complete checkpoints have `predict_uncertainty=true`, `use_lora=true`, and full `model.safetensors` files.
- Next: continue setup using Dean-local complete uncertainty checkpoint candidate unless Bob connectivity recovers; prefer `ckpt-110000` after validating it loads and outputs uncertainty traces.

### Step 3 - Dean Environment and Suite Registry Verified

- Repaired Dean `simvla` Python environment by installing missing `tqdm` into the user site for `/home/redafrix/miniconda3/envs/simvla/bin/python`.
- Verified `simvla` env imports:
  - Python: `/home/redafrix/miniconda3/envs/simvla/bin/python`
  - Torch: `2.6.0+cu124`
  - CUDA: available on NVIDIA RTX A5000
  - `tqdm`, `transformers`, `huggingface_hub`, and `safetensors`: import successfully.
- Verified Dean `libero` env imports LIBERO, robosuite, mujoco, and torch successfully.
- Dean LIBERO-PRO benchmark registry has 83 suites.
- Generic object perturbation suites available:
  - `libero_spatial_object`
  - `libero_object_object`
  - `libero_goal_object`
  - `libero_10_object`
- No `libero_90_object` suite exists in the registry. Base `libero_90` exists and will be treated as the requested 90-suite inclusion/control unless a later code audit reveals a hidden object-perturbed 90 variant.
- `libero_100` exists but is explicitly excluded by user requirement.
- Next: copy trusted FIPER collector into Dean-owned workspace and inspect SimVLA uncertainty feature extraction code.

### Step 4 - Single-Process Dean Environment Enabled

- Copied the trusted local FIPER collection module directory to Dean:
  - Source: `fiper_ws/collection/data_collection_stage9/`
  - Destination: `/home/dean/fiper_uncertainty_collection/src/data_collection_stage9/`
- The local trusted collector imports `simvla_candidate_sampler.py`, which was not in `fiper_ws/collection/data_collection_stage9`; a copy exists locally at `reda_ws/video_labeling_ws/src/simvla_candidate_sampler.py`.
- To make the trusted in-process collector viable, installed missing simulation packages into Dean `simvla` Python environment:
  - `robosuite==1.4.0`
  - `mujoco==3.2.3`
  - dependencies `glfw`, `pyopengl`, `numba`, `llvmlite`
- Verified one Dean Python process can now import SimVLA dependencies plus LIBERO/robosuite/mujoco with:
  - `PYTHONPATH=/home/redafrix/LIBERO-PRO:/home/redafrix/SimVLA_modified`
  - `MUJOCO_GL=egl`, `PYOPENGL_PLATFORM=egl`
- Selected suite plan verified in Dean `simvla` env:
  - `libero_spatial_object`: 10 tasks
  - `libero_object_object`: 10 tasks
  - `libero_goal_object`: 10 tasks
  - `libero_10_object`: 10 tasks
  - `libero_90`: 90 tasks
  - Total round-robin cycle: 130 tasks/episodes.
- Next: create Dean-specific sampler/collector that uses `generate_actions_with_uncertainty`, writes 49D features and 49D deltas, and runs in the repaired `simvla` env.

### Step 5 - Dean Uncertainty Collector Implemented Locally

- Added `fiper_ws/collection/data_collection_stage9/collect_fiper_uncertainty_receding_dean_v1.py`.
- The collector is Dean-specific and self-contained around the confirmed Dean paths:
  - SimVLA source: `/home/redafrix/SimVLA_modified`
  - LIBERO-PRO source: `/home/redafrix/LIBERO-PRO`
  - target checkpoint: `/home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000`
- It preserves the trusted FIPER receding structure:
  - one main action chunk per timestep
  - eight ACE candidate chunks by default
  - execute only the first action from the main chunk
  - store current state, history, main/ACE chunks, deployability flags, episode outcome backfill
- It adds:
  - exact 49D uncertainty feature vector using the previously audited `feature_stats.json` key order
  - exact 49D temporal deltas
  - raw path/last variance summaries from the uncertainty head
  - runtime seed uniqueness checks for main + ACE candidates
- To avoid the known buggy `generate_actions_with_uncertainty(num_action_samples > 1)` path, it batches the 1 main + 8 ACE chunks in one GPU pass while explicitly constructing the per-candidate initial noise from unique seeds.
- Local syntax check passed: `python3 -m py_compile collect_fiper_uncertainty_receding_dean_v1.py`.
- Checkpoint transfer from Sam to Dean is still active; latest observed progress was about 2.07GB of 3.25GB.
- Next: sync this collector to Dean, run remote py_compile/import checks, then wait for checkpoint checksum verification before model smoke tests.

### Step 6 - Dean Collector Synced and Remote Syntax/Import Checked

- Synced `collect_fiper_uncertainty_receding_dean_v1.py` to Dean:
  - `/home/dean/fiper_uncertainty_collection/src/data_collection_stage9/collect_fiper_uncertainty_receding_dean_v1.py`
- Remote `py_compile` passed in Dean `simvla` env.
- Remote import check passed and confirmed:
  - uncertainty base key count = 49
  - uncertainty delta key count = 49
  - selected suites = `libero_spatial_object`, `libero_object_object`, `libero_goal_object`, `libero_10_object`, `libero_90`
- Found that importing `torchvision` on Dean currently fails through a missing `mpmath` dependency. To reduce fragility, removed the collector's `torchvision` dependency and replaced image preprocessing with direct PIL resize + torch tensor normalization.
- Next: wait for `ckpt-60000/model.safetensors` transfer to finish, verify size and sha256, then run a model-load smoke.

### Step 7 - Correct `ckpt-60000` Recovered on Dean

- The first Sam-to-Dean streamed transfer through Batman broke at 2,390,097,920 bytes and left a partial file.
- Created direct Dean-to-Sam SSH access with Dean key `/home/dean/.ssh/id_tmp_sam` and Sam Tailscale IP `100.112.19.30`.
- Resumed the partial checkpoint using direct Dean pull:
  - `rsync -av --append-verify --progress -e 'ssh -i /home/dean/.ssh/id_tmp_sam ...' rootalkhatib@100.112.19.30:/home/rootalkhatib/test/reda_ws/intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000/model.safetensors /home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000/model.safetensors`
- Final Dean checkpoint verification:
  - size: `3245557952` bytes
  - sha256: `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`
- This matches the verified Sam/Bob checksum for the modified uncertainty checkpoint.
- Dean disk after transfer: about 93GB free on `/home/dean`.
- Dean GPU remains idle before model smoke: RTX A5000, 15MiB used.
- Next: run a model-load and one-batch inference smoke using the verified checkpoint before starting environment rollouts.

### Step 8 - Dean Model-Load Smoke Passed

- Installed missing Dean user-site dependencies required by the existing `simvla` env:
  - `annotated-doc`
  - `annotated-types`
  - `mpmath==1.3.0` (pinned because `sympy 1.13.1` requires `mpmath < 1.4`)
- Added PyTorch-only transformer environment guards to the collector:
  - `USE_TF=0`
  - `TRANSFORMERS_NO_TF=1`
  - `USE_FLAX=0`
- Model-load smoke command used the verified Dean-owned checkpoint and local SmolVLM cache.
- Smoke result:
  - CUDA available: yes
  - checkpoint loaded on GPU: yes
  - `predict_uncertainty`: true
  - action horizon: 10
  - action dim: 7
  - state norm dim: 8
  - processor image size: 384
  - CUDA allocated after load: about 3.27GB
- Next: run one-timestep collector smoke with a LIBERO-PRO environment and verify the produced row schema.

### Step 9 - One-Step Collector Smoke Passed

- Repaired additional Dean `simvla` env dependencies required by LIBERO-PRO environment creation:
  - `bddl==1.0.1`
  - `future`
  - `easydict`
  - `python-dateutil`
  - `gym==0.25.2`
- `libero_spatial_object` is registered in LIBERO-PRO but its BDDL/init directories are missing in the checked-out data tree. The collector now resolves only this missing suite to base `libero_spatial` files and records:
  - `declared_problem_folder=libero_spatial_object`
  - `resolved_problem_folder=libero_spatial`
- Patched LIBERO init-state load for PyTorch 2.6 by using `torch.load(..., weights_only=False)` on trusted local LIBERO init-state assets.
- One-step smoke run:
  - suite: `libero_spatial_object`
  - task id: 0
  - max timesteps: 1
  - ACE candidates: 2
  - outcome: completed one row, no crash
- Schema audit passed:
  - rows = 1
  - episode summaries = 1
  - uncertainty feature length = 49
  - uncertainty delta length = 49
  - main chunk shape = 10x7
  - ACE count = 2, ACE chunk shape = 10x7
  - seed uniqueness = true
  - all feature/delta values finite = true
  - saved sim state path exists = true
- Next: run normal 8-ACE multi-step smoke to validate temporal deltas and standard ACE settings.

### Step 10 - 8-ACE and All-Suite Smokes Passed, Long Run Launched

- Normal 8-ACE multi-step smoke passed:
  - suite: `libero_object_object`
  - task id: 0
  - max timesteps: 3
  - ACE candidates: 8
  - rows written: 3
  - feature length: 49 for every row
  - delta length: 49 for every row
  - first-row deltas are zero
  - later-row deltas are nonzero
  - no seed collisions and no main/ACE seed collisions
- All selected suites one-step smoke passed:
  - `libero_spatial_object`
  - `libero_object_object`
  - `libero_goal_object`
  - `libero_10_object`
  - `libero_90`
  - rows written: 5
  - summaries written: 5
  - ACE count: 8 for every row
  - all 49D features and deltas finite
  - no episode errors
- Confirmed `libero_spatial_object` resolves to base `libero_spatial`; the other selected suites resolve to their declared folders.
- Added Dean launch script:
  - `/home/dean/fiper_uncertainty_collection/src/data_collection_stage9/launch_dean_uncertainty_collection_20260529.sh`
- Launched long-running Dean collection:
  - tmux session: `dean_fiper_uncertainty_20260529`
  - workers: 4
  - run root: `/home/dean/fiper_uncertainty_collection/runs/dean_object_uncertainty_20260529`
  - sharding: 4-way over the 130-task round-robin plan
  - suites: `libero_spatial_object`, `libero_object_object`, `libero_goal_object`, `libero_10_object`, `libero_90`
  - excluded suite: `libero_100`
  - ACE candidates: 8
  - max timesteps: 300
  - checkpoint SHA enforced at worker startup
  - resume enabled per worker
- Next: wait for workers to finish model load and audit live health, row counts, crashes, GPU memory, and disk usage.

### Step 11 - Post-Launch Dean Connectivity Issue Under Investigation

- Immediately after launching 4 Dean workers, Dean stopped responding to SSH and ICMP/Tailscale ping from Batman.
- Tailscale still lists Dean (`100.124.50.124`, `batman-1`) as active, but:
  - `ssh dean@100.124.50.124` times out
  - `ping 100.124.50.124` receives no packets
  - `tailscale ping 100.124.50.124` times out
- Most likely cause: 4 simultaneous model loads saturated Dean CPU/RAM/IO or wedged the host before the follow-up health check could run.
- A retry loop is active from Batman to reconnect and, if successful, inspect tmux/GPU/processes. If Dean recovers and shows unhealthy pressure, reduce to fewer workers before continuing.
- Local worklog is updated; syncing this step to Dean is pending until SSH returns.

### Step 12 - Sam/Bob Campaign Read-Only Audit During Dean Retry

- Sam and Bob risk-aware 4-worker campaign was audited without interruption.
- Sam:
  - tmux session `riskaware_4worker_sam_20260529` alive
  - two workers active on GPU
  - `sam_w0_seen_task7`: 23 episode summaries, 17 successes, 6 failures, 0 seed collisions, 0 main/ACE collisions, 0 errors
  - `sam_w1_ood_task8`: 22 episode summaries, 13 successes, 9 failures, 0 seed collisions, 0 main/ACE collisions, 0 errors
- Bob:
  - tmux session `riskaware_4worker_bob_20260529` alive
  - two workers active on GPU
  - `bob_w0_fold00_seen_butter_t2`: 24 episode summaries, 12 successes, 12 failures, 0 seed collisions, 0 main/ACE collisions, 0 errors
  - `bob_w1_fold00_unseen_alphabet_soup_t0`: 26 episode summaries, 15 successes, 11 failures, 0 seed collisions, 0 main/ACE collisions, 0 errors
- Step-score rows exceed completed episode step sums because each worker was actively inside a new in-progress episode during the audit; this is expected.
- Next: regain Dean SSH and either confirm 4-worker health or relaunch with a safer lower worker count.

### Step 13 - Dean Recovered, Three-Day Collection Audit

- Audit time: `2026-06-01 09:30:49 CEST`.
- Dean is reachable again at `100.124.50.124`.
- The original tmux session is still alive:
  - `dean_fiper_uncertainty_20260529`
  - 4 worker windows
  - workers still actively running
- Machine health:
  - GPU: NVIDIA RTX A5000
  - GPU memory: `16155 MiB / 24564 MiB`
  - GPU utilization: `100%`
  - GPU temperature: `85 C`
  - RAM: `21 GiB / 31 GiB` used
  - swap: `2.0 GiB / 2.0 GiB` used
  - disk: `/home/dean` root filesystem has `60G` free, `87%` used
- Run root:
  - `/home/dean/fiper_uncertainty_collection/runs/dean_object_uncertainty_20260529`
  - total size: about `31G`
- Completed episode summaries at audit:
  - worker 0: `1098`
  - worker 1: `1008`
  - worker 2: `1047`
  - worker 3: `962`
  - total: `4115`
- Completed low-level rows reported by live status:
  - worker 0: `165393`
  - worker 1: `165762`
  - worker 2: `165913`
  - worker 3: `165918`
  - total completed rows: `662986`
- Outcomes at audit:
  - successes: `3293`
  - failures/timeouts/non-success: `822`
  - overall success rate: about `80.02%`
- Coverage:
  - all `130` selected suite/task pairs have been reached
  - selected suites present: `libero_spatial_object`, `libero_object_object`, `libero_goal_object`, `libero_10_object`, `libero_90`
  - `libero_100` remains excluded
- Feature/schema spot audit passed on first and latest rows from every worker:
  - `simvla_uncertainty_49d` length = `49`
  - `simvla_uncertainty_delta_49d` length = `49`
  - uncertainty keys length = `49`
  - delta keys length = `49`
  - all sampled feature/delta values finite
  - main candidate chunks are `10 x 7`
  - ACE candidate chunks are `8 x 10 x 7`
  - 9 seeds per timestep are unique
  - saved simulator state paths exist
  - checkpoint SHA matches `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`
  - `model_predict_uncertainty = true`
  - `object_perturbation_collection = true`
  - deployability flags show no reward/success used for action and no future timestep usage
- Seed checks:
  - total seed collisions: `0`
  - total main-vs-ACE collisions: `0`
- Issues found:
  - `64` zero-step environment errors were logged.
  - They are isolated to two task IDs:
    - `libero_goal_object/task_9`: `31` errors, `KeyError: 'wine_rack_stand_1_top_region'`
    - `libero_10_object/task_4`: `33` errors, `ZeroDivisionError: integer division or modulo by zero`
  - These do not corrupt row data because they occur before any timestep is written, but those task/sweep attempts are not usable episodes.
- Current verdict:
  - Dean collection worked and is still running.
  - Dataset rows collected so far look valid for the rows that exist.
  - The run is not perfectly clean because two tasks repeatedly error at reset/environment setup.
  - Do not call the entire run "clean" without either excluding/fixing those two task IDs or documenting them as zero-step skipped tasks.
- Next:
  - Decide whether to leave the current run alive to keep gathering usable rows, or patch/relaunch with `libero_goal_object/task_9` and `libero_10_object/task_4` excluded.
  - Disk is the main operational limit: at roughly `31G` collected in about `2.64` days, the remaining `60G` is enough for several more days but not unlimited.

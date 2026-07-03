# Handoff Prompt For CLI `pi0`: Pi0.5-LIBERO + H10 Risk-Aware Plan On Bob

Use this prompt exactly for the new CLI session named `cli pi0`.

---

## Prompt To Send To CLI `pi0`

You are working for Reda on the VLA/risk-aware LIBERO project. Your job is to set up and test a third VLA family, **Physical Intelligence `pi05_libero` from openpi**, on **Bob / pcrobot only**. Do not touch Dean or Sam. Do not touch existing SimVLA/OpenVLA workspaces except read-only inspection if absolutely needed for schema reference.

The final research goal is to test whether Reda's H10 risk-aware selected-cap idea transfers to a Pi0-family flow-matching VLA. However, your **first deliverable is only two smoke tests**. Do not launch large data collection or training until Reda explicitly tells you to continue after the smoke report.

Read this file before every major action and keep your work aligned with it.

---

## Hard Constraints

1. Work only on Bob / pcrobot.
2. Create a new isolated workspace. Recommended:

```bash
/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623
```

3. Do not modify existing SimVLA/FIPER/OpenVLA workspaces.
4. Do not kill or pause unrelated tmux sessions.
5. Do not start long jobs in the foreground. Use tmux for anything longer than a few minutes.
6. Do not run full collection, risk training, or OOD online eval yet. First deliverable is smoke tests only.
7. Before using Bob's GPU for actual rollout smoke tests, identify the currently running Bob process, wait for an episode boundary if needed, pause it safely, run the smoke tests, then resume it exactly.
8. Write a markdown report at the end of the smoke phase.
9. Preserve exact paths, commands, environment names, logs, and any error messages in the report.

---

## Why This VLA

Use **openpi `pi05_libero`**:

- It is from the Pi0 family.
- It is flow-matching, unlike `pi0-FAST`, which is autoregressive.
- It has an official LIBERO checkpoint:

```text
gs://openpi-assets/checkpoints/pi05_libero
```

- The official config predicts an H10 action chunk:

```text
name = "pi05_libero"
model = Pi0Config(pi05=True, action_horizon=10, discrete_state_input=False)
```

So action output should be:

```text
(10, 7)
```

This is important because Reda's best SimVLA selected-cap risk setup is H10.

Useful official references:

- openpi repo: `https://github.com/Physical-Intelligence/openpi`
- LIBERO example README: `https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/examples/libero/README.md`
- openpi config: `https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/training/config.py`

---

## Existing Risk-Aware Target We Eventually Want To Match

The eventual target is to reproduce the best SimVLA-style risk-aware selected-cap logic as closely as possible:

- VLA outputs one main H10 action chunk.
- Generate 8 additional H10 candidate chunks using different flow noise seeds.
- Compute ACE from the 8 candidate chunks.
- Build H10 risk features:
  - history: `16 x 21`
  - action: `10 x 7`
  - static: `51`
- Static layout:

```text
action_stats_28 + ACE_7 + proprio_8 + uncertainty_topk8_8
```

- For Pi0.5, use real ACE.
- For Pi0.5 uncertainty TopK8, use zeros for now, because we are not modifying Pi0.5 internals.
- Selected-cap online logic later should match the SimVLA selected-cap gate:

```text
main_threshold = 0.3
selection_min_margin = 0.02
selection_strong_margin = 0.05
selection_max_selected_score = 0.4
execution_horizon = H10
```

But again: do not implement the full online risk-aware test until Reda approves after smoke tests.

---

## First Deliverable: Two Smoke Tests Only

You must implement only enough to run and verify these two smoke tests on `libero_goal_object`.

### Smoke Test A: Normal Pi0.5 LIBERO Input, Two Cameras

Goal:
Run `pi05_libero` on LIBERO with the usual official LIBERO camera inputs:

- `observation/image`
- `observation/wrist_image`

Use the official openpi LIBERO input pipeline as much as possible. Confirm:

1. model/checkpoint loads;
2. LIBERO env initializes;
3. one `libero_goal_object` task can reset;
4. policy inference returns finite actions;
5. action shape is exactly `(10, 7)`;
6. a short rollout can execute without infrastructure errors;
7. save a small video or GIF if easy;
8. save JSON summary.

Recommended smoke size:

```text
suite = libero_goal_object
task_id = 0
episodes = 1 or 2
max_steps = 300 or 800
execution_horizon = 10
```

If the episode fails task success, that is okay for smoke. The smoke only needs infrastructure validity and finite H10 actions.

### Smoke Test B: One-Camera Agent-View Only

Goal:
Run the same smoke but with only the agent/base view as real visual input.

Use one real camera:

```text
observation/image = agent/base/front image
```

For wrist image, test the least invasive adapter:

```text
observation/wrist_image = zeros_like(base_image)
```

Masking behavior must be documented. If openpi's default `LiberoInputs` forces the left wrist mask to true, do not silently change it without documenting. If you create a tiny local custom input adapter to set wrist image mask false, keep it isolated inside the new workspace and explain exactly what changed.

Confirm the same checks:

1. model/checkpoint loads;
2. env resets;
3. policy inference returns finite actions;
4. action shape is `(10, 7)`;
5. rollout executes without infrastructure errors;
6. save summary and video/GIF if easy.

---

## Important Implementation Notes

### Workspace

Create:

```bash
/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623
```

Suggested subfolders:

```text
src/
logs/
outputs/
reports/
checkpoints_or_cache/
third_party/
```

### Environment

Prefer a fresh environment. Do not alter existing `simvla` or FIPER envs.

Possible environment name:

```text
pi05_openpi_20260623
```

Use openpi's documented setup. If `uv` is available, use it. If Docker is needed, report that before doing heavy work.

### GPU/Compute

Before installing or running:

```bash
hostname
nvidia-smi
df -h
tmux ls || true
```

Record this in the report.

### Current Bob Process Protection

There is already something running on Bob. Protect it.

Before any GPU rollout smoke:

1. Identify active tmux sessions and GPU processes:

```bash
tmux ls || true
nvidia-smi
ps aux | grep -E "python|openvla|simvla|libero|collect|eval|sweep" | grep -v grep || true
```

2. Identify the active experiment exactly:
   - tmux session name;
   - script path;
   - env activation command;
   - output root;
   - log path;
   - `episode_summaries.jsonl` path if available;
   - current row count;
   - last completed episode.

3. Do not kill blindly. If a rollout episode is running, wait until the current episode finishes and a summary row is written.
4. Pause only at an episode boundary.
5. Record the exact resume command before pausing.
6. Run the Pi0.5 smoke tests.
7. Resume the original process using the same env, script, args, output root, and tmux session name.
8. Verify it resumed from the next expected episode and did not overwrite existing rows.

If the active process has no safe resume path, do not pause it. Report the blocker and stop before GPU smoke tests.

### Checkpoint

Use:

```text
gs://openpi-assets/checkpoints/pi05_libero
```

Do not train Pi0.5. This is inference only for smoke.

### LIBERO

Use Bob's existing LIBERO/LIBERO-PRO installation if available, but do not modify it. If paths are missing, locate read-only:

```bash
find /media/rootalkhatib /home/rootalkhatib -maxdepth 6 -type d -name 'LIBERO*' 2>/dev/null
find /media/rootalkhatib /home/rootalkhatib -maxdepth 7 -type d -path '*libero*' 2>/dev/null
```

Use `libero_goal_object` for smoke, not OOD yet.

### Cameras

For the two-camera smoke, use the official mapping.

For the one-camera smoke, use only one real image. Document whether the wrist image is:

- zero-filled with mask true,
- zero-filled with mask false,
- or duplicated from base image.

For the first one-camera smoke, prefer zero-filled wrist. Do not switch to duplicated camera unless zero-filled fails and you document why.

### Action Horizon

Expected:

```text
predicted_horizon = 10
action_dim = 7
execution_horizon = 10
```

Do not use H1 adaptive horizon in this Pi0.5 smoke. We are trying to match SimVLA H10, not OpenVLA H1/H8.

### ACE Later, Not Required For First Smoke

For the first smoke tests, you do not need to run risk or selected-cap. But if it is easy, add a separate tiny "candidate generation smoke" after the two required smokes:

- generate one main action chunk;
- generate 8 candidate chunks using explicit different noise tensors/seeds;
- verify candidate chunks are not identical;
- compute ACE with the existing SimVLA ACE formula;
- save a JSON record.

This candidate-generation smoke is useful, but do not let it block the two required smoke tests.

---

## Later Full Plan, Do Not Execute Yet

Only after Reda approves the smoke results, continue with this staged plan.

### Phase 1: Pi0.5 Goal-Object Data Collection

Collect new data on `libero_goal_object` using Pi0.5, because the risk head should be trained on the same VLA family if possible.

For every query/timestep, save:

- episode id;
- suite;
- task id;
- task language;
- timestep;
- env seed / init state index;
- success/failure label eventually;
- current proprio, 8 dims;
- executed action, 7 dims;
- main Pi0.5 action chunk, `(10, 7)`;
- 8 candidate Pi0.5 chunks, `(8, 10, 7)`;
- ACE metrics, 7 dims;
- history enough to reconstruct `16 x 21`;
- uncertainty TopK8 vector as zeros, 8 dims;
- optional images/video/state paths for audit, if storage allows;
- run manifest with exact checkpoint/config/camera adapter.

Use max steps 800 unless Reda asks for 300.

Collect sequentially round-robin by task:

```text
task0 ep0, task1 ep0, ..., task9 ep0, task0 ep1, ...
```

Do not choose episode count yourself without reporting ETA/storage first. Recommend a staged target:

1. 10 episodes/task = 100 total smoke dataset;
2. train quick risk model;
3. if sane, scale to 1000+ or more.

### Phase 2: Train Pi0.5 H10 Risk Head

Train the same family of risk head:

```text
SeqRiskModel
history = 16 x 21
action = 10 x 7
static = 51
```

Feature construction:

```text
history step = proprio_8 + executed_action_7 + ACE_first6
action tokens = main/candidate chunk 10x7
static = action_stats_28 + ACE_7 + proprio_8 + uncertainty_zeros_8
```

Do not include explicit task id.
Do not include explicit timestep.

### Phase 3: Offline Audit

Compute:

- AUROC / AUPRC;
- success false alarm;
- failure detection;
- Det@10;
- Det@25;
- Det@50;
- mean detection fraction;
- never detected;
- per-task breakdown;
- threshold sweeps:
  - fixed score thresholds;
  - q95/q99 K-window;
  - q95 mass thresholds;
  - selected operating point.

### Phase 4: Online OOD Test

Only after offline model is sane.

Target suite:

```text
libero_goal_object_ood
```

Use same seeds as the best SimVLA selected-cap test if available from experiment maps. Pair policies by `(task_id, reset_seed)`.

Policies:

```text
pi05_basic_h10
pi05_selected_cap_topk8_zero_unc_h10
```

Execution:

```text
H = 10 for both
max_steps = 800
```

This must be a selected-cap action replacement test, not an adaptive H1 horizon-control test.

---

## Required Smoke Report

Write final smoke report to:

```text
/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/reports/PI05_LIBERO_SMOKE_TWO_CAMERA_AND_ONE_CAMERA_20260623.md
```

The report must include:

1. hostname and GPU;
2. workspace path;
3. env path/name;
4. openpi commit hash;
5. checkpoint path;
6. exact LIBERO suite/task/seeds;
7. currently running Bob process identified before GPU smoke;
8. pause/resume method and exact resume command;
9. proof the previous Bob process resumed correctly after smoke;
10. two-camera smoke result;
11. one-camera smoke result;
12. action shapes and finite checks;
13. whether videos/GIFs were saved;
14. any patches/adapters created;
15. clear flags:

```text
PI05_LIBERO_CHECKPOINT_LOADED = YES/NO
CURRENT_BOB_PROCESS_IDENTIFIED = YES/NO
CURRENT_BOB_PROCESS_PAUSED_SAFELY = YES/NO/NOT_NEEDED
CURRENT_BOB_PROCESS_RESUMED_CORRECTLY = YES/NO/NOT_NEEDED
TWO_CAMERA_SMOKE_PASS = YES/NO
ONE_CAMERA_AGENT_VIEW_SMOKE_PASS = YES/NO
ACTION_SHAPE_10X7_CONFIRMED = YES/NO
FINITE_ACTIONS_CONFIRMED = YES/NO
NO_EXISTING_WORKSPACES_MODIFIED = YES/NO
SAFE_FOR_DATA_COLLECTION_PHASE = YES/NO
```

At the end, stop. Do not start full data collection until Reda explicitly approves.

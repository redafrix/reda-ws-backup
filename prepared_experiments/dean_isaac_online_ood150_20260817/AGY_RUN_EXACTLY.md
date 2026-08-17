# Agy execution instruction — DO NOT INTERPRET

You have no authority to design, edit, optimize, select thresholds manually, or summarize scientifically.

Repository: `redafrix/reda-ws-backup`
Branch: `experiment/dean-isaac-online-ood150-20260817`
Prepared directory: `prepared_experiments/dean_isaac_online_ood150_20260817`

## Required action
1. Fetch/pull this branch.
2. Verify your checkout is clean.
3. Do **not edit any file** in the prepared directory.
4. Launch exactly this prepared orchestrator in a new tmux session named `dean_isaac_online_ood150_20260817`:

```bash
tmux kill-session -t dean_isaac_online_ood150_20260817 2>/dev/null || true
tmux new-session -d -s dean_isaac_online_ood150_20260817 \
  'bash prepared_experiments/dean_isaac_online_ood150_20260817/run_online_protocol.sh'
```

5. Wait 20 seconds, then only inspect (read-only):

```bash
tmux ls
tmux capture-pane -pt dean_isaac_online_ood150_20260817 -S -80
```

## Forbidden
- do not kill the HARD1000 collector;
- do not remove stop markers;
- do not change the threshold grid;
- do not run your own scripts;
- do not launch a second Isaac job;
- do not rerun or replace the baseline OOD150;
- do not choose a threshold yourself;
- do not modify the risk model;
- do not summarize results as good/bad.

The prepared script itself cleanly pauses HARD1000, freezes its state, performs preflight, performs the shadow parity gate, runs the dev40 grid, chooses the controller deterministically, and then runs the untouched holdout110.

## Reply to Reda only with

```text
BRANCH HEAD:
TMUX SESSION: RUNNING / NOT RUNNING
HARD1000 PAUSE SNAPSHOT PATH:
PREFLIGHT: PASS / FAIL / NOT REACHED
SHADOW PARITY: PASS / FAIL / NOT REACHED
CURRENT PROTOCOL PHASE:
LAST 25 LOG LINES:
```

Do not wait for the full multi-hour online evaluation before replying.

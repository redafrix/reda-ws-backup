#!/usr/bin/env bash
set -euo pipefail

ROOT="/media/rootalkhatib/My Passport/reda_ws/fiper_ws"
CONFIG="$ROOT/realtime_deployment/configs/bob_three_policy_seen_object_task0_topk8_shard70_100_20260603.json"
RUNNER="$ROOT/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py"
SESSION="bob_task0_topk8_shard70_100_20260603"
LOG="$ROOT/realtime_deployment/logs/three_policy_task0_20260603/risk_unc_topk8_bob_shard70_100.log"

mkdir -p "$(dirname "$LOG")"

if tmux has-session -t "$SESSION" 2>/dev/null; then
  echo "[skip] $SESSION already exists"
else
  tmux new-session -d -s "$SESSION" \
    "cd '$ROOT' && source ../asynchvla_ws/scripts/activate_simvla_bob.sh && env MUJOCO_GL=egl PYOPENGL_PLATFORM=egl USE_TF=0 TRANSFORMERS_NO_TF=1 USE_FLAX=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python3 '$RUNNER' --config '$CONFIG' --policy risk_unc_topk8 --episode-start 70 --episode-end 100 > '$LOG' 2>&1"
  echo "[launch] $SESSION log=$LOG"
fi

tmux ls

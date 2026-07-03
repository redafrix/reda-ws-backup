#!/usr/bin/env bash
set -euo pipefail

ROOT="/media/rootalkhatib/My Passport/reda_ws/fiper_ws"
CONFIG="$ROOT/realtime_deployment/configs/bob_three_policy_seen_object_task0_100eps_20260603.json"
RUNNER="$ROOT/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py"
LOG_DIR="$ROOT/realtime_deployment/logs/three_policy_task0_20260603"
SESSION="bob_task0_risk_base_20260603"
LOG="$LOG_DIR/risk_base.log"

mkdir -p "$LOG_DIR"

if tmux has-session -t "$SESSION" 2>/dev/null; then
  echo "[skip] tmux session already exists: $SESSION"
else
  tmux new-session -d -s "$SESSION" \
    "cd '$ROOT' && source ../asynchvla_ws/scripts/activate_simvla_bob.sh && env MUJOCO_GL=egl PYOPENGL_PLATFORM=egl USE_TF=0 TRANSFORMERS_NO_TF=1 USE_FLAX=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python3 '$RUNNER' --config '$CONFIG' --policy risk_base > '$LOG' 2>&1"
  echo "[launch] risk_base session=$SESSION log=$LOG"
fi

tmux ls

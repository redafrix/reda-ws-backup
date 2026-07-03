#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/dean/fiper_uncertainty_collection"
CONFIG="$ROOT/realtime_deployment/configs/dean_three_policy_seen_object_task0_100eps_20260603.json"
RUNNER="$ROOT/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py"
PY="/home/redafrix/miniconda3/envs/simvla/bin/python"
LOG_DIR="$ROOT/realtime_deployment/logs/three_policy_task0_20260603"
mkdir -p "$LOG_DIR"

launch_policy() {
  local policy="$1"
  local session="$2"
  local log="$LOG_DIR/${policy}.log"

  if tmux has-session -t "$session" 2>/dev/null; then
    echo "[skip] tmux session already exists: $session"
    return 0
  fi

  tmux new-session -d -s "$session" \
    "cd '$ROOT' && env MUJOCO_GL=egl PYOPENGL_PLATFORM=egl USE_TF=0 TRANSFORMERS_NO_TF=1 USE_FLAX=0 '$PY' '$RUNNER' --config '$CONFIG' --policy '$policy' > '$log' 2>&1"
  echo "[launch] $policy session=$session log=$log"
}

launch_policy "simvla_only" "dean_task0_simvla_only_20260603"
launch_policy "risk_unc_topk8" "dean_task0_risk_unc_topk8_20260603"

tmux ls

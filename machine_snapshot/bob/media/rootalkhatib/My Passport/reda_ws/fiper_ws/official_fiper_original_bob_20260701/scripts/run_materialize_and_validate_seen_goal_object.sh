#!/usr/bin/env bash
set -euo pipefail
ROOT="/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701"
LOG_DIR="$ROOT/logs"
mkdir -p "$LOG_DIR"
source "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export TOKENIZERS_PARALLELISM=false
export FIPER_VLM_MICRO_BATCH=8
{
  echo "[start] $(date -Is) materialization"
  python3 -u "$ROOT/scripts/materialize_official_fiper_seen_goal_object.py" --overwrite
  echo "[done] $(date -Is) materialization"
  echo "[start] $(date -Is) validation"
  python3 -u "$ROOT/scripts/validate_official_fiper_seen_goal_object.py"
  echo "[done] $(date -Is) validation"
} 2>&1 | tee -a "$LOG_DIR/materialize_seen_goal_object.log"

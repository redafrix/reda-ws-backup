#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/dean/fiper_uncertainty_collection"
RUN_ID="canonical_dean_bob_task0_4policy_seq100_20260604"
RUNNER="$ROOT/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py"
PY="/home/redafrix/miniconda3/envs/simvla/bin/python"
RUN_DIR="$ROOT/realtime_deployment/runs/$RUN_ID"
LOG_DIR="$RUN_DIR/logs"
STATUS="$RUN_DIR/sequential_status.jsonl"

mkdir -p "$LOG_DIR"
: > "$STATUS"

export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export USE_TF=0
export TRANSFORMERS_NO_TF=1
export USE_FLAX=0
export TOKENIZERS_PARALLELISM=false
export PYTHONUNBUFFERED=1
export NVIDIA_TF32_OVERRIDE=0
export CUBLAS_WORKSPACE_CONFIG=:4096:8

if pgrep -af "run_dean_uncertainty_realtime_policy_v1.py" | grep -v grep | grep -v "$$" >/dev/null; then
  echo "[launcher] ERROR: conflicting realtime runner already active" | tee -a "$LOG_DIR/launcher.log"
  pgrep -af "run_dean_uncertainty_realtime_policy_v1.py" | tee -a "$LOG_DIR/launcher.log"
  exit 2
fi

record_status() {
  local stage="$1"
  local event="$2"
  local code="${3:-}"
  local now
  now="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  if [[ -n "$code" ]]; then
    printf '{"time":"%s","host":"dean","stage":"%s","event":"%s","code":%s}\n' "$now" "$stage" "$event" "$code" >> "$STATUS"
  else
    printf '{"time":"%s","host":"dean","stage":"%s","event":"%s"}\n' "$now" "$stage" "$event" >> "$STATUS"
  fi
}

run_stage() {
  local stage="$1"
  local policy="$2"
  local config="$3"
  local log="$LOG_DIR/${stage}.log"
  record_status "$stage" start
  echo "[launcher] START $stage policy=$policy config=$config $(date -Is)" | tee -a "$LOG_DIR/launcher.log"
  "$PY" "$RUNNER" --config "$config" --policy "$policy" --episode-start 0 --episode-end 100 > "$log" 2>&1
  local code=$?
  record_status "$stage" end "$code"
  echo "[launcher] END $stage code=$code $(date -Is)" | tee -a "$LOG_DIR/launcher.log"
  return "$code"
}

echo "[launcher] host=$(hostname) start=$(date -Is) run_id=$RUN_ID" | tee -a "$LOG_DIR/launcher.log"

run_stage "01_original_simvla" "simvla_only" "$ROOT/realtime_deployment/configs/${RUN_ID}_dean_original_simvla.json"
run_stage "02_modified_simvla_ckpt60000" "simvla_only" "$ROOT/realtime_deployment/configs/${RUN_ID}_dean_modified_simvla_ckpt60000.json"
run_stage "03_risk_base" "risk_base" "$ROOT/realtime_deployment/configs/${RUN_ID}_dean_risk_base.json"
run_stage "04_risk_unc_topk8" "risk_unc_topk8" "$ROOT/realtime_deployment/configs/${RUN_ID}_dean_risk_unc_topk8.json"

echo "[launcher] ALL_DONE $(date -Is)" | tee -a "$LOG_DIR/launcher.log"

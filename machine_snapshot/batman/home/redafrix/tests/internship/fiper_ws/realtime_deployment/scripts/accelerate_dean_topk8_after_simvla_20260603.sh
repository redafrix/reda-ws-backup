#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/dean/fiper_uncertainty_collection"
BASE_RUN="$ROOT/realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603"
BASE_CONFIG="$ROOT/realtime_deployment/configs/dean_three_policy_seen_object_task0_100eps_20260603.json"
RUNNER="$ROOT/realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py"
PY="/home/redafrix/miniconda3/envs/simvla/bin/python"
LOG_DIR="$ROOT/realtime_deployment/logs/three_policy_task0_20260603"
ACCEL_ROOT="$ROOT/realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603_topk8_parallel_after_simvla"
ACCEL_CONFIG_DIR="$ROOT/realtime_deployment/configs/topk8_parallel_after_simvla_20260603"
STATUS="$LOG_DIR/topk8_parallel_after_simvla_status.log"
TARGET_END=70

mkdir -p "$LOG_DIR" "$ACCEL_ROOT" "$ACCEL_CONFIG_DIR"

count_summaries() {
  local path="$1"
  if [ -f "$path" ]; then
    grep -cve '^[[:space:]]*$' "$path"
  else
    echo 0
  fi
}

log() {
  printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S %Z')" "$*" | tee -a "$STATUS"
}

SIM_SUM="$BASE_RUN/simvla_only/episode_summaries.jsonl"
TOPK_SUM="$BASE_RUN/risk_unc_topk8/episode_summaries.jsonl"

log "watcher started; waiting for simvla_only to reach 100 summaries"
while true; do
  sim_done="$(count_summaries "$SIM_SUM")"
  topk_done="$(count_summaries "$TOPK_SUM")"
  log "progress simvla_only=$sim_done/100 risk_unc_topk8_original=$topk_done/100"
  if [ "$sim_done" -ge 100 ]; then
    break
  fi
  sleep 60
done

log "simvla_only complete; stopping original single risk_unc_topk8 worker"
tmux send-keys -t dean_task0_risk_unc_topk8_20260603 C-c 2>/dev/null || true
sleep 8
tmux kill-session -t dean_task0_risk_unc_topk8_20260603 2>/dev/null || true
sleep 2

done_count="$(count_summaries "$TOPK_SUM")"
log "original risk_unc_topk8 completed summaries after stop: $done_count"

if [ "$done_count" -ge "$TARGET_END" ]; then
  log "nothing to shard on Dean; original risk_unc_topk8 already reached target end $TARGET_END"
  exit 0
fi

remaining=$((TARGET_END - done_count))
mid=$((done_count + (remaining + 1) / 2))

make_config() {
  local shard_name="$1"
  local output_dir="$2"
  local out_config="$3"
  "$PY" - "$BASE_CONFIG" "$output_dir" "$out_config" <<'PY'
import json
import sys
from pathlib import Path

src = Path(sys.argv[1])
out_dir = sys.argv[2]
dst = Path(sys.argv[3])
cfg = json.loads(src.read_text())
cfg["output_dir"] = out_dir
dst.parent.mkdir(parents=True, exist_ok=True)
dst.write_text(json.dumps(cfg, indent=2, sort_keys=True) + "\n")
PY
}

launch_shard() {
  local name="$1"
  local start="$2"
  local end="$3"
  local shard_root="$ACCEL_ROOT/$name"
  local cfg="$ACCEL_CONFIG_DIR/${name}.json"
  local session="dean_topk8_${name}_20260603"
  local log_path="$LOG_DIR/${session}.log"

  make_config "$name" "$shard_root" "$cfg"

  log "launching $session episodes [$start, $end) output=$shard_root"
  tmux new-session -d -s "$session" \
    "cd '$ROOT' && env MUJOCO_GL=egl PYOPENGL_PLATFORM=egl USE_TF=0 TRANSFORMERS_NO_TF=1 USE_FLAX=0 '$PY' '$RUNNER' --config '$cfg' --policy risk_unc_topk8 --episode-start '$start' --episode-end '$end' > '$log_path' 2>&1"
}

launch_shard "shard_a_${done_count}_${mid}" "$done_count" "$mid"
launch_shard "shard_b_${mid}_${TARGET_END}" "$mid" "$TARGET_END"

log "parallel topk8 shards launched for Dean lower range [$done_count, $TARGET_END); Bob handles [70, 100)"
tmux ls | tee -a "$STATUS"

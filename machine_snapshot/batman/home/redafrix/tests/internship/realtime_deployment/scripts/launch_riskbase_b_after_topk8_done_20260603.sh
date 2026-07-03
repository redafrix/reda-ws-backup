#!/usr/bin/env bash
set -u

ROOT=/home/dean/fiper_uncertainty_collection
LOGDIR="$ROOT/realtime_deployment/logs/three_policy_task0_20260603"
LOG="$LOGDIR/riskbase_b_after_topk8_watcher.log"
mkdir -p "$LOGDIR"

count_file() {
  local p="$1"
  if [ -f "$p" ]; then
    grep -c '^{' "$p" || true
  else
    echo 0
  fi
}

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S %Z')] $*" | tee -a "$LOG"
}

log "watcher started; waiting for topk8 complete count 100 before risk_base shard_b 50-100"
while true; do
  c0=$(count_file "$ROOT/realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603/risk_unc_topk8/episode_summaries.jsonl")
  c1=$(count_file "$ROOT/realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603_topk8_parallel_after_simvla/shard_a_35_53/risk_unc_topk8/episode_summaries.jsonl")
  c2=$(count_file "$ROOT/realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603_topk8_parallel_after_simvla/shard_b_53_70/risk_unc_topk8/episode_summaries.jsonl")
  c3=$(count_file "$ROOT/realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603_topk8_parallel_after_simvla/shard_c_70_100/risk_unc_topk8/episode_summaries.jsonl")
  total=$((c0 + c1 + c2 + c3))
  rb_b=$(count_file "$ROOT/realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603_riskbase_parallel_after_topk8/shard_b_50_100/risk_base/episode_summaries.jsonl")
  log "topk8_total=$total parts=$c0,$c1,$c2,$c3 riskbase_b=$rb_b"

  if [ "$rb_b" -ge 50 ]; then
    log "riskbase shard_b already complete; exiting"
    exit 0
  fi

  if [ "$total" -ge 100 ]; then
    log "topk8 complete; launching risk_base shard_b episodes 50-100"
    tmux has-session -t dean_riskbase_shard_b_50_100_20260603 2>/dev/null && tmux kill-session -t dean_riskbase_shard_b_50_100_20260603 || true
    tmux new-session -d -s dean_riskbase_shard_b_50_100_20260603 \
      "cd /home/dean/fiper_uncertainty_collection && env MUJOCO_GL=egl PYOPENGL_PLATFORM=egl USE_TF=0 TRANSFORMERS_NO_TF=1 USE_FLAX=0 /home/redafrix/miniconda3/envs/simvla/bin/python realtime_deployment/scripts/run_dean_uncertainty_realtime_policy_v1.py --config realtime_deployment/configs/dean_task0_riskbase_shard50_100_same_machine_20260603.json --policy risk_base --episode-start 50 --episode-end 100 > realtime_deployment/logs/three_policy_task0_20260603/risk_base_shard_b_50_100.log 2>&1"
    log "launched risk_base shard_b; exiting watcher"
    exit 0
  fi

  sleep 120
done

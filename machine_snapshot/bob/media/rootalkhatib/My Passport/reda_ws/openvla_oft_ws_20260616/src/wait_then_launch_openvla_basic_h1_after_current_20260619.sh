#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616"
CURRENT_OUT="$WORKSPACE/online_evals/libero_goal_object_ood_openvla_basic_vs_risk_100ep_20260618"
CURRENT_SUMMARY="$CURRENT_OUT/episode_summaries.jsonl"
TARGET_LINES=3600

NEXT_SESSION="openvla_ood_basic_h1_100ep_20260619"
NEXT_OUT="$WORKSPACE/online_evals/libero_goal_object_ood_openvla_basic_h1_100ep_20260619"
NEXT_LOG_DIR="$WORKSPACE/logs/libero_goal_object_ood_openvla_basic_h1_100ep_20260619"
NEXT_LOG="$NEXT_LOG_DIR/sweep_supervisor.log"
RUNNER="$WORKSPACE/src/run_openvla_ood_basic_h1_full_20260619.py"

mkdir -p "$NEXT_LOG_DIR"

echo "[$(date -Is)] wait_then_launch started"
echo "[$(date -Is)] current_summary=$CURRENT_SUMMARY"
echo "[$(date -Is)] target_lines=$TARGET_LINES"
echo "[$(date -Is)] next_session=$NEXT_SESSION"
echo "[$(date -Is)] next_out=$NEXT_OUT"

while true; do
  if [[ -f "$CURRENT_SUMMARY" ]]; then
    current_lines="$(wc -l < "$CURRENT_SUMMARY")"
  else
    current_lines="0"
  fi
  echo "[$(date -Is)] current run progress: $current_lines/$TARGET_LINES summaries"
  if [[ "$current_lines" -ge "$TARGET_LINES" ]]; then
    break
  fi
  sleep 300
done

if tmux has-session -t "$NEXT_SESSION" 2>/dev/null; then
  echo "[$(date -Is)] $NEXT_SESSION already exists; not launching duplicate"
  exit 0
fi

mkdir -p "$NEXT_OUT" "$NEXT_LOG_DIR"

echo "[$(date -Is)] launching $NEXT_SESSION"
tmux new-session -d -s "$NEXT_SESSION" "source \"$WORKSPACE/activate_openvla_oft_bob.sh\" && python3 -u \"$RUNNER\" --suite libero_goal_object_ood --output-root \"$NEXT_OUT\" --episodes-per-task 100 --seed-start 10 --max-steps 800 --task-ids all > \"$NEXT_LOG\" 2>&1"
echo "[$(date -Is)] launched $NEXT_SESSION; log=$NEXT_LOG"

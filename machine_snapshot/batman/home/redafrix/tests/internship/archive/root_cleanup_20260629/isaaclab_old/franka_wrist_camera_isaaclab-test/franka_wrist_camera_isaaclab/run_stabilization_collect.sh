#!/usr/bin/env bash
set -e

WS="/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test"
REPO="$WS/franka_wrist_camera_isaaclab"
REPORTS="$WS/reports"
LOGS="$WS/logs"
OUT="$WS/outputs"

cd "$REPO"

echo "Clearing old baseline reachable apple outputs..."
rm -rf "$OUT/baseline_reachable_apple"
mkdir -p "$OUT/baseline_reachable_apple"

export ISAACLAB_ROOT="/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab"
export TERM=xterm
export PYTHONPATH="/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/source/isaaclab:/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/source/isaaclab_assets:/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/source/isaaclab_mimic:/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/source/isaaclab_rl:/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab/source/isaaclab_tasks:$REPO/src"

echo "Starting data collection with baseline_reachable_apple.yaml..."
set +e
timeout --signal=INT --kill-after=60s 1800s \
  "$ISAACLAB_ROOT/isaaclab.sh" -p scripts/collect.py \
  --headless \
  --collection_config baseline_reachable_apple.yaml \
  2>&1 | tee "$LOGS/baseline_reachable_apple_collect.log"

COLLECT_STATUS=${PIPESTATUS[0]}
set -e

echo "Collection finished with status: $COLLECT_STATUS"

{
  echo
  echo "## baseline reachable apple collect result"
  echo "status=$COLLECT_STATUS"
  echo "log=$LOGS/baseline_reachable_apple_collect.log"
  grep -Ei "success|failed|Traceback|Exception|Error|episode|saved|out of reach|reach|object|apple|omni.kvdb|lock|CUDA|out of memory" \
    "$LOGS/baseline_reachable_apple_collect.log" | tail -400 || true
  echo
  echo "## outputs"
  find "$OUT/baseline_reachable_apple" -maxdepth 5 -type f -printf "%p | %s bytes\n" | sort || true
} | tee -a "$REPORTS/BASELINE_STABILIZATION_REPORT.md"

exit $COLLECT_STATUS

#!/usr/bin/env bash
set -euo pipefail

ROOT=/home/redafrix/tests/internship/isaac_dynamicVLA-test
STAGE="$ROOT/reports/real_collision_viewer/dom_collision_viewer_stage.usd"

echo "Stage: $STAGE"

if [ ! -f "$STAGE" ]; then
  echo "ERROR: stage not found"
  exit 1
fi

echo "Checking for running Isaac/Kit/Omniverse processes..."
# Exclude the current script's PID and the grep process itself
MYPID=$$
RUNNING=$(ps -fu "$USER" | grep -Ei "isaac|kit|omni|carb|SimulationApp|isaaclab|simulate.py|translate_dataset_seq.py|replay_dataset_seq.py|evaluate.py" | grep -v grep | grep -v "$MYPID" || true)

if [ -n "$RUNNING" ]; then
  echo "STOP: Another Isaac/Kit/Omniverse process is running. Not launching."
  echo "$RUNNING"
  exit 20
fi

# Try to find isaac-sim.sh
ISAAC_SH=""
for p in \
  "$ROOT/IsaacLab/_isaac_sim/isaac-sim.sh" \
  "$ROOT/isaacsim/isaac-sim.sh" \
  "/home/redafrix/isaacsim/isaac-sim.sh" \
  "$HOME/.local/share/ov/pkg/isaac-sim-4.2.0/isaac-sim.sh" \
  "$HOME/.local/share/ov/pkg/isaac-sim-2023.1.1/isaac-sim.sh"
do
  if [ -x "$p" ]; then
    ISAAC_SH="$p"
    break
  fi
done

if [ -z "$ISAAC_SH" ]; then
  echo "ERROR: Could not find isaac-sim.sh"
  exit 2
fi

echo "Launching Isaac GUI:"
echo "$ISAAC_SH $STAGE"

# We use nohup to keep it running if the terminal closes, and & for background.
# On many systems, we need to ensure DISPLAY is set.
export DISPLAY=${DISPLAY:-:1}

nohup "$ISAAC_SH" "$STAGE" > "$ROOT/logs/dom_collision_viewer_gui.log" 2>&1 &
PID=$!
echo "$PID" > "$ROOT/logs/dom_collision_viewer_gui.pid"

echo "LAUNCHED_PID=$PID"
echo "LOG=$ROOT/logs/dom_collision_viewer_gui.log"

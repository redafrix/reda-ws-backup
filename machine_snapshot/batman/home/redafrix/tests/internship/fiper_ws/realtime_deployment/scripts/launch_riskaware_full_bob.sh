#!/usr/bin/env bash
# Launch 2-worker risk-aware full run on Bob
# Worker 0: episodes 0-49, Worker 1: episodes 50-99
set -euo pipefail

FIPER_WS="/media/rootalkhatib/My Passport/reda_ws/fiper_ws"
cd "$FIPER_WS"
source ../asynchvla_ws/scripts/activate_simvla_bob.sh

CONFIG="realtime_deployment/configs/riskaware_actionmod_v2_strict_libero10_milk_task7_bob_full_20260528.json"
SCRIPT="realtime_deployment/scripts/run_riskaware_simvla_one_task_v1.py"
RUN_DIR="realtime_deployment/runs/riskaware_actionmod_v2_strict_libero10_milk_task7_bob_full_20260528"

echo "=== Launching Worker 0 (episodes 0-49) ==="
nohup python3 "$SCRIPT" \
    --config "$CONFIG" \
    --num-episodes 50 \
    --episode-offset 0 \
    --worker-id 0 \
    > "${RUN_DIR}/logs/worker_0.log" 2>&1 &
W0_PID=$!
echo "Worker 0 PID: $W0_PID"

echo "=== Launching Worker 1 (episodes 50-99) ==="
nohup python3 "$SCRIPT" \
    --config "$CONFIG" \
    --num-episodes 50 \
    --episode-offset 50 \
    --worker-id 1 \
    > "${RUN_DIR}/logs/worker_1.log" 2>&1 &
W1_PID=$!
echo "Worker 1 PID: $W1_PID"

echo ""
echo "Both workers launched."
echo "  Worker 0 PID: $W0_PID (episodes 0-49)"
echo "  Worker 1 PID: $W1_PID (episodes 50-99)"
echo "  Logs: ${RUN_DIR}/logs/"
echo ""
echo "Monitor with:"
echo "  tail -f ${RUN_DIR}/logs/worker_0.log"
echo "  tail -f ${RUN_DIR}/logs/worker_1.log"
echo "  cat ${RUN_DIR}/live_status.json"

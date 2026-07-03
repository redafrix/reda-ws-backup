#!/usr/bin/env bash
# Launch sequential 100-episode Horizon 5 baseline on Bob
set -euo pipefail

FIPER_WS="/media/rootalkhatib/My Passport/reda_ws/fiper_ws"
cd "$FIPER_WS"

echo "=== Sourcing Bob env ==="
source ../asynchvla_ws/scripts/activate_simvla_bob.sh

echo "=== Launching Horizon 5 Baseline ==="
python3 realtime_deployment/scripts/run_baseline_simvla_chunk_exec_h5_v1.py \
    --config realtime_deployment/configs/baseline_simvla_chunk_exec_task7_100eps_h5_20260529.json \
    --worker-id bob_h5 \
    --num-episodes 100 \
    > realtime_deployment/runs/baseline_simvla_chunk_exec_task7_100eps_h5_20260529/logs/worker.log 2>&1

echo "=== Horizon 5 Baseline completed ==="

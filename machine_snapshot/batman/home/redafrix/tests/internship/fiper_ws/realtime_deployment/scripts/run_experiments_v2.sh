#!/usr/bin/env bash
# Sequentially run Task 7 chunk-exec baseline and risk-aware experiments (v2) on Bob
set -euo pipefail

FIPER_WS="/media/rootalkhatib/My Passport/reda_ws/fiper_ws"
cd "$FIPER_WS"

echo "=== Sourcing Bob env ==="
source ../asynchvla_ws/scripts/activate_simvla_bob.sh

echo "=== Launching Baseline Rerun ==="
python3 realtime_deployment/scripts/run_baseline_simvla_chunk_exec_v2.py \
    --config realtime_deployment/configs/baseline_simvla_chunk_exec_task7_100eps_rerun_v2_20260529.json \
    --worker-id bob_baseline_v2 \
    > realtime_deployment/runs/baseline_simvla_chunk_exec_task7_100eps_rerun_v2_20260529/logs/worker.log 2>&1

echo "=== Baseline Finished. Launching Risk-Aware Rerun ==="
python3 realtime_deployment/scripts/run_riskaware_simvla_chunk_exec_v2.py \
    --config realtime_deployment/configs/riskaware_actionmod_v2_strict_chunk_exec_task7_100eps_rerun_v2_20260529.json \
    --worker-id bob_riskaware_v2 \
    > realtime_deployment/runs/riskaware_actionmod_v2_strict_chunk_exec_task7_100eps_rerun_v2_20260529/logs/worker.log 2>&1

echo "=== All reruns completed successfully ==="

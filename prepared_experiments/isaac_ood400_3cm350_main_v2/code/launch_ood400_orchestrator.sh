#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXP_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
ORCH_DIR="${EXP_DIR}/orchestrator"
mkdir -p "${ORCH_DIR}"

WORKSPACE="${SIMVLA_ISAAC_H10_WORKSPACE:-/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813}"
export PYTHONPATH="${WORKSPACE}:${WORKSPACE}/src:${SCRIPT_DIR}:${PYTHONPATH:-}"

LOG_FILE="${ORCH_DIR}/ORCHESTRATOR.log"
PID_FILE="${ORCH_DIR}/ORCHESTRATOR.pid"

if [[ -f "${PID_FILE}" ]] && kill -0 "$(cat "${PID_FILE}")" 2>/dev/null; then
    echo "Orchestrator is already running with PID $(cat "${PID_FILE}")"
    exit 0
fi

echo "Launching OOD400 Orchestrator in background..."
nohup python3 "${SCRIPT_DIR}/orchestrate_ood400_pipeline.py" --exp-dir "${EXP_DIR}" > "${LOG_FILE}" 2>&1 &
ORCH_PID=$!
echo "${ORCH_PID}" > "${PID_FILE}"
echo "OOD400 Orchestrator successfully launched with PID ${ORCH_PID}"
echo "Log file: ${LOG_FILE}"

#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXP_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
ORCH_DIR="${EXP_DIR}/orchestrator"
mkdir -p "${ORCH_DIR}"

WORKSPACE="${SIMVLA_ISAAC_H10_WORKSPACE:-/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813}"
export PYTHONPATH="${WORKSPACE}:${WORKSPACE}/src:${SCRIPT_DIR}:${PYTHONPATH:-}"
ISAAC_PY="${ISAAC_PYTHON:-/mnt/ai/isaac/envs/env_isaaclab_6_0/bin/python}"

LOG_FILE="${ORCH_DIR}/ORCHESTRATOR.log"
PID_FILE="${ORCH_DIR}/ORCHESTRATOR.pid"
TMUX_SESSION="ood400_orchestrator"

# Check if tmux session already exists
if tmux has-session -t "${TMUX_SESSION}" 2>/dev/null; then
    echo "Tmux session '${TMUX_SESSION}' is already running."
    tmux list-panes -t "${TMUX_SESSION}" -F "#{pane_pid} #{pane_current_command} #{pane_dead}"
    exit 0
fi

echo "Launching OOD400 Orchestrator inside Dean TMUX session '${TMUX_SESSION}'..."

# Launch inside dedicated detached tmux session
ORCH_CMD="cd ${WORKSPACE} && export PYTHONPATH=${WORKSPACE}:${WORKSPACE}/src:${SCRIPT_DIR} && '${ISAAC_PY}' '${SCRIPT_DIR}/orchestrate_ood400_pipeline.py' --exp-dir '${EXP_DIR}' >> '${LOG_FILE}' 2>&1"

tmux new-session -d -s "${TMUX_SESSION}" "${ORCH_CMD}"
tmux set-option -t "${TMUX_SESSION}" remain-on-exit on

# Get pane PID
PANE_PID=$(tmux list-panes -t "${TMUX_SESSION}" -F "#{pane_pid}")
echo "${PANE_PID}" > "${PID_FILE}"

echo "OOD400 Orchestrator successfully launched in TMUX '${TMUX_SESSION}' with PID ${PANE_PID}"
echo "Log file: ${LOG_FILE}"
echo "Attach command: tmux attach -t ${TMUX_SESSION}"
echo "Capture command: tmux capture-pane -pt ${TMUX_SESSION} -S -100"

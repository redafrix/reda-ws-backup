#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OPENPI_CLIENT_SRC="${OPENPI_CLIENT_SRC:-/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/openpi/packages/openpi-client/src}"

export PYTHONPATH="${OPENPI_CLIENT_SRC}:${PYTHONPATH:-}"
export ISAACLAB_PYTHON_SCRIPT="${SCRIPT_DIR}/scripts/pi05_reaching_rollout.py"

exec "${SCRIPT_DIR}/run_collect.sh" "$@"

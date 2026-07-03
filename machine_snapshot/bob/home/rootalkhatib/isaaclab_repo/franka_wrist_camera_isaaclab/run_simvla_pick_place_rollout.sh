#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export ISAACLAB_PYTHON_SCRIPT="${SCRIPT_DIR}/scripts/simvla_pick_place_rollout.py"

exec "${SCRIPT_DIR}/run_collect.sh" "$@"

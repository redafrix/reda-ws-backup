#!/usr/bin/env bash
set -euo pipefail

OPENPI_ROOT="${OPENPI_ROOT:-/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/openpi}"
OPENPI_ENV="${OPENPI_ENV:-/home/rootalkhatib/pi05_openpi_20260623_env}"
CHECKPOINT_DIR="${CHECKPOINT_DIR:-/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/checkpoints/openpi-assets/checkpoints/pi05_droid}"
PORT="${PORT:-8006}"

source "${OPENPI_ENV}/bin/activate"
cd "${OPENPI_ROOT}"

exec python scripts/serve_policy.py \
  --port "${PORT}" \
  policy:checkpoint \
  --policy.config=pi05_droid \
  --policy.dir="${CHECKPOINT_DIR}"

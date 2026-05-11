#!/usr/bin/env bash
set -euo pipefail

WS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
ENV_PATH="$WS_ROOT/assets/envs/simvla"
HOST="${HOST:-0.0.0.0}"
PORT="${PORT:-8000}"

export PYTHONNOUSERSITE=1

cd "$WS_ROOT"
exec "$ENV_PATH/bin/python" "$WS_ROOT/simvla/scripts/serve_simvla_local.py" \
  --host "$HOST" \
  --port "$PORT"

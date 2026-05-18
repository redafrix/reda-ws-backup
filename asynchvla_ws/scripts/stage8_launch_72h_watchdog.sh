#!/usr/bin/env bash
set -euo pipefail

ROOT="/media/rootalkhatib/My Passport/reda_ws"
cd "$ROOT"
mkdir -p asynchvla_ws/stage8_ultimate/logs asynchvla_ws/stage8_ultimate/status

PID_FILE="asynchvla_ws/stage8_ultimate/status/stage8_watchdog.pid"
LOG_FILE="asynchvla_ws/stage8_ultimate/logs/stage8_watchdog.nohup.log"

if [ -s "$PID_FILE" ] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
  echo "watchdog already running pid=$(cat "$PID_FILE")"
  exit 0
fi

nohup python3 asynchvla_ws/scripts/stage8_watchdog.py --hours 72 --interval-sec 600 > "$LOG_FILE" 2>&1 &
echo $! > "$PID_FILE"
echo "watchdog launched pid=$(cat "$PID_FILE") log=$LOG_FILE"

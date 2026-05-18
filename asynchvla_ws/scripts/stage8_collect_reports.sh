#!/usr/bin/env bash
set -euo pipefail

LOCAL=${LOCAL:-/home/redafrix/tests/internship/codex_reports/stage8}
mkdir -p "$LOCAL"

collect_bob() {
  ssh pcrobot 'cd "/media/rootalkhatib/My Passport/reda_ws" && find asynchvla_ws/stage8_ultimate/reports -maxdepth 1 -type f \( -name "*.md" -o -name "*.json" \) -print' | while IFS= read -r p; do
    [ -n "$p" ] || continue
    ssh pcrobot "cd '/media/rootalkhatib/My Passport/reda_ws' && cat '$p'" < /dev/null > "$LOCAL/$(basename "$p")"
  done
  if ssh pcrobot 'test -f "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/ASYNCVLA_SIMVLA_STAGE8_ULTIMATE_EXPERIMENT_REPORT.md"'; then
    ssh pcrobot 'cat "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/ASYNCVLA_SIMVLA_STAGE8_ULTIMATE_EXPERIMENT_REPORT.md"' < /dev/null > "$LOCAL/ASYNCVLA_SIMVLA_STAGE8_ULTIMATE_EXPERIMENT_REPORT.md"
  fi
}

collect_sam() {
  ssh sam 'find "/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/reports" -maxdepth 1 -type f \( -name "*.md" -o -name "*.json" \) -print 2>/dev/null || true' | while IFS= read -r p; do
    [ -n "$p" ] || continue
    ssh sam "cat \"$p\"" < /dev/null > "$LOCAL/sam_$(basename "$p")"
  done
}

collect_bob
collect_sam
find "$LOCAL" -maxdepth 2 -type f | sort

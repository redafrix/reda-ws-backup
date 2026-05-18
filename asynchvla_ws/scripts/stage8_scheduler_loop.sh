#!/usr/bin/env bash
set -euo pipefail

ROOT="/media/rootalkhatib/My Passport/reda_ws"
cd "$ROOT"
LOG="asynchvla_ws/stage8_ultimate/logs/stage8_scheduler_loop.log"
DASH="asynchvla_ws/stage8_ultimate/reports/stage8_live_dashboard.md"
mkdir -p "$(dirname "$LOG")" "$(dirname "$DASH")"

end=$(( $(date +%s) + 72*3600 ))
while [ "$(date +%s)" -lt "$end" ]; do
  {
    echo
    echo "## scheduler tick $(date -Is)"
    python3 asynchvla_ws/scripts/stage8_job_manager.py status || true
    python3 asynchvla_ws/scripts/stage8_job_manager.py launch-ready --limit 2 || true
    python3 - <<'PY'
import json, subprocess, datetime
from pathlib import Path
root=Path('/media/rootalkhatib/My Passport/reda_ws')
out=root/'asynchvla_ws/stage8_ultimate/reports/stage8_live_dashboard.md'
try:
    rows=json.loads(subprocess.check_output(['python3','asynchvla_ws/scripts/stage8_job_manager.py','status'], cwd=root, text=True))
except Exception as exc:
    rows=[{'job_id':'status_error','state':'FAILED','error':repr(exc)}]
lines=['# Stage 8 Live Dashboard','',f'Updated: `{datetime.datetime.now().isoformat(timespec="seconds")}`','',
       '| job | machine | state | attempt | log |','|---|---|---:|---:|---|']
for r in rows:
    lines.append(f"| {r.get('job_id')} | {r.get('machine','')} | {r.get('state','')} | {r.get('attempt','')} | `{r.get('log_path','')}` |")
lines += ['','## Current Recommendation','',
          'Keep LIBERO-PRO as the primary benchmark. Normal LIBERO remains fallback/baseline only.']
out.write_text('\\n'.join(lines)+'\\n')
PY
  } >> "$LOG" 2>&1
  sleep 600
done

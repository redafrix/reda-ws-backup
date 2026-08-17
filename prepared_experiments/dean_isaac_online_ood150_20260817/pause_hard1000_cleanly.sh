#!/usr/bin/env bash
set -euo pipefail
W=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813
HARD="$W/outputs/final_seen_h10_round_002_seed20260804"
AUTO="$W/automation"
mkdir -p "$W/online_evals/isaac_ood150_argmin_cap_v1/protocol"
touch "$AUTO/STOP_HARD1000_PIPELINE_AFTER_CURRENT_EPISODE"
touch "$HARD/STOP_AFTER_CURRENT_EPISODE"
echo "Requested clean pause after current HARD1000 episode at $(date -Iseconds)"
for _ in $(seq 1 180); do
  if ! pgrep -af '[c]ollect_isaac_risk.py' | grep -F "$HARD" >/dev/null; then break; fi
  sleep 10
done
if pgrep -af '[c]ollect_isaac_risk.py' | grep -F "$HARD" >/dev/null; then
  echo "ERROR: collector did not pause within 30 minutes; NOT killing it" >&2; exit 2
fi
# Wait briefly for the supervisor to notice the clean pause and exit.
for _ in $(seq 1 60); do
  if ! pgrep -af '[h]ard1000_pipeline.py' >/dev/null; then break; fi
  sleep 5
done
python3 - <<'PY'
import json,time
from pathlib import Path
W=Path('/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813')
H=W/'outputs/final_seen_h10_round_002_seed20260804'
rows=[json.loads(x) for x in (H/'episode_summaries.jsonl').read_text().splitlines() if x.strip()] if (H/'episode_summaries.jsonl').exists() else []
live=json.loads((H/'live_status.json').read_text()) if (H/'live_status.json').exists() else {}
status=json.loads((W/'automation/hard1000_pipeline_status.json').read_text()) if (W/'automation/hard1000_pipeline_status.json').exists() else {}
out={'schema_version':'hard1000_clean_pause_snapshot_v1','timestamp_unix':time.time(),'completed':len(rows),'successes':sum(bool(r['success']) for r in rows),'failures':sum(not bool(r['success']) for r in rows),'live_status':live,'pipeline_status':status,'stop_markers_preserved':True}
p=W/'online_evals/isaac_ood150_argmin_cap_v1/protocol/HARD1000_PAUSE_SNAPSHOT.json';p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
PY

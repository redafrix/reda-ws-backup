#!/usr/bin/env bash
set -euo pipefail

WORKSPACE=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813
PY=/mnt/ai/isaac/envs/env_isaaclab_6_0/bin/python
CONFIG="$WORKSPACE/configs/final_seen_h10_round_000_seed20260730.yaml"
MANIFEST="$WORKSPACE/manifests/seen_4000_master.json"
OUTPUT="$WORKSPACE/outputs/final_seen_h10_round_000_seed20260730"
LOG="$WORKSPACE/logs/final_seen_h10_round_000_seed20260730.log"
REPORTS="$OUTPUT/reports"
STAGE_STATUS="$REPORTS/stage_status.json"

mkdir -p "$REPORTS" "$(dirname "$LOG")"
chmod 0755 "$OUTPUT" "$REPORTS" "$(dirname "$LOG")"
touch "$LOG"
chmod 0644 "$LOG"

write_stage_status() {
    local state=$1
    local rc=$2
    STATE="$state" RC="$rc" OUTPUT="$OUTPUT" LOG="$LOG" \
        "$PY" - "$STAGE_STATUS" <<'PY'
import json
import os
from pathlib import Path
import sys
import time

destination = Path(sys.argv[1])
payload = {
    "state": os.environ["STATE"],
    "collector_exit_code": int(os.environ["RC"]),
    "output_dir": os.environ["OUTPUT"],
    "collector_log": os.environ["LOG"],
    "updated_at_unix_s": time.time(),
}
temporary = destination.with_suffix(".tmp")
temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
temporary.replace(destination)
PY
}

write_stage_status running 0
set +e
"$WORKSPACE/scripts/run_collector.sh" \
    --run-config "$CONFIG" \
    --manifest "$MANIFEST" \
    --output-dir "$OUTPUT" \
    --offset 0 --count 4000 \
    --round-id 0 \
    --round-kind broad \
    --round-master-seed 20260730 \
    --balanced-order \
    --execution-mode chunk_h10 \
    --viz none --device cuda:0 \
    >> "$LOG" 2>&1
collector_rc=$?
set -e

if ((collector_rc != 0)); then
    write_stage_status collector_failed "$collector_rc"
    exit "$collector_rc"
fi

collector_state=$("$PY" - "$OUTPUT/live_status.json" <<'PY'
import json
from pathlib import Path
import sys
print(json.loads(Path(sys.argv[1]).read_text()).get("state", "unknown"))
PY
)
if [[ "$collector_state" != complete ]]; then
    write_stage_status "$collector_state" 0
    exit 0
fi

write_stage_status exhaustive_audit_running 0
"$PY" "$WORKSPACE/scripts/audit_corrected_collection.py" \
    "$OUTPUT" \
    --report-json "$REPORTS/exhaustive_audit.json" \
    --expected-outcome production_round \
    > "$REPORTS/exhaustive_audit.log" 2>&1

write_stage_status round_summary_running 0
"$PY" "$WORKSPACE/scripts/summarize_production_round.py" \
    "$OUTPUT" \
    --audit-json "$REPORTS/exhaustive_audit.json" \
    --report-json "$REPORTS/round_audit_summary.json" \
    > "$REPORTS/round_summary.log" 2>&1

write_stage_status complete_and_audited 0

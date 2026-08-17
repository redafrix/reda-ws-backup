#!/usr/bin/env bash
set -euo pipefail
W=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813
PROTO="$W/online_evals/isaac_ood150_argmin_cap_v1"
[[ -f "$PROTO/ONLINE_OOD150_PROTOCOL_COMPLETE" ]] || { echo 'REFUSING: online protocol not complete' >&2; exit 2; }
pgrep -af '[r]un_isaac_online_risk.py' >/dev/null && { echo 'REFUSING: online runner still active' >&2; exit 3; }
rm -f "$W/automation/STOP_HARD1000_PIPELINE_AFTER_CURRENT_EPISODE"
rm -f "$W/outputs/final_seen_h10_round_002_seed20260804/STOP_AFTER_CURRENT_EPISODE"
# Re-enter the existing guarded HARD1000 pipeline. It resumes already committed episodes.
exec /home/redafrix/miniconda3/bin/python -u "$W/automation/hard1000_pipeline.py"

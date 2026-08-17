#!/usr/bin/env bash
set -euo pipefail
W=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813
OLD="$W/online_evals/isaac_ood150_argmin_cap_v1"
PROTO="$W/online_evals/isaac_ood150_offline_select_single_online_v1"
CODE="$PROTO/code_snapshot"
RUNS="$PROTO/runs"
SUM="$PROTO/summaries"
LOG="$PROTO/logs"
MODEL="$W/models/isaac_h10_topk8_temporal_v1"
NORM="$W/frozen_datasets/isaac_seen_h10_topk8_v1/normalization.json"
MASTER="$W/automation/generated/locked_ood150/manifest.json"
RUNCFG="$W/automation/generated/locked_ood150/run_config.yaml"
BASELINE="$W/outputs/final_locked_h10_ood150_seed20260728"
ISAAC_PY=/mnt/ai/isaac/envs/env_isaaclab_6_0/bin/python
BASE_PY=/home/redafrix/miniconda3/bin/python
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SEL=${1:-}
[[ -n "$SEL" && -f "$SEL" ]] || { echo 'usage: run_ONE_selected_full150_online.sh SELECTED_CONTROLLER.json' >&2; exit 2; }
mkdir -p "$PROTO" "$CODE" "$RUNS" "$SUM" "$LOG" "$PROTO/protocol"
[[ ! -f "$PROTO/ONLINE_OOD150_SINGLE_RUN_COMPLETE" ]] || { echo 'REFUSING: single online campaign already complete' >&2; exit 3; }
# HARD must already be paused; never silently run concurrently.
if pgrep -af '[c]ollect_isaac_risk.py' | grep -F "$W/outputs/final_seen_h10_round_002_seed20260804" >/dev/null; then echo 'REFUSING: HARD1000 collector still running' >&2; exit 4; fi
# No competing online/training GPU job.
if pgrep -af '[r]un_isaac_online_risk.py' >/dev/null || pgrep -af '[t]rain_isaac_topk8.py' >/dev/null; then echo 'REFUSING: competing GPU experiment active' >&2; exit 5; fi
# Validate historical baseline identity and core configuration.
"$BASE_PY" "$HERE/preflight_online.py" --output "$PROTO/protocol/PREFLIGHT.json" | tee "$LOG/00_preflight.log"
# Existing 3-episode shadow must pass the functional safety gate; strict historical bitwise replay is intentionally not required.
"$BASE_PY" "$HERE/verify_shadow_functional.py" --baseline-root "$BASELINE" --shadow-root "$OLD/runs/shadow3" --output "$PROTO/protocol/SHADOW_FUNCTIONAL_GATE.json" | tee "$LOG/01_shadow_functional.log"
# Read exactly one offline-selected alarm threshold. Cap is locked to seen q90_success.
read -r MAIN < <("$BASE_PY" - "$SEL" <<'PY'
import json,sys
x=json.load(open(sys.argv[1]))
assert x.get('schema_version')=='isaac_offline_selected_controller_v1'
assert x.get('selected_cap_name')=='q90_success'
print(x['main_threshold_name'])
PY
)
"$BASE_PY" - "$MODEL/thresholds.json" "$MAIN" <<'PY'
import json,sys
x=json.load(open(sys.argv[1])); k=sys.argv[2]
assert k in x, k
print('SELECTED_MAIN_THRESHOLD',k,x[k]); print('SELECTED_CAP q90_success',x['q90_success'])
PY
# Freeze exact runtime sources.
cp -f "$HERE/online_isaac_runtime.py" "$CODE/online_isaac_runtime.py"
cp -f "$HERE/summarize_online.py" "$CODE/summarize_online.py"
cp -f "$HERE/build_online_runner.py" "$CODE/build_online_runner.py"
cp -f "$HERE/build_full150_runner.py" "$CODE/build_full150_runner.py"
"$BASE_PY" "$CODE/build_full150_runner.py" --base-builder "$CODE/build_online_runner.py" --source "$W/scripts/collect_isaac_risk.py" --output "$CODE/run_isaac_online_risk.py" | tee "$LOG/02_build_runner.log"
"$BASE_PY" -m py_compile "$CODE"/*.py
find "$CODE" -maxdepth 1 -type f -exec sha256sum {} + | sort > "$PROTO/protocol/CODE_SHA256SUMS.txt"
cp -f "$SEL" "$PROTO/protocol/SELECTED_CONTROLLER.json"
# Exactly ONE active online run on all 150 locked OOD episodes.
OUT="$RUNS/selected_full150"
[[ ! -e "$OUT" ]] || { echo "REFUSING: output already exists: $OUT" >&2; exit 6; }
export PYTHONPATH="$W:$W/src:${PYTHONPATH:-}"
"$ISAAC_PY" -u "$CODE/run_isaac_online_risk.py" \
  --run-config "$RUNCFG" --manifest "$MASTER" --output-dir "$OUT" \
  --risk-model-root "$MODEL" --risk-normalization "$NORM" \
  --main-threshold "$MAIN" --selected-cap q90_success \
  --online-mode active --online-role full150 --protocol-id isaac_ood150_SINGLE_SELECTED_ONLINE \
  --offset 0 --count 150 --execution-mode chunk_h10 --viz none --device cuda:0 \
  2>&1 | tee "$LOG/03_selected_full150_online.log"
lines=$(wc -l < "$OUT/episode_summaries.jsonl")
[[ "$lines" -eq 150 ]] || { echo "REFUSING completion: online run incomplete $lines/150" >&2; exit 7; }
"$BASE_PY" "$CODE/summarize_online.py" --baseline "$BASELINE/episode_summaries.jsonl" --online "$OUT/episode_summaries.jsonl" --output "$SUM/FINAL_SELECTED_FULL150.json" --variant "${MAIN}__cap_q90_success" | tee "$LOG/04_final_summary.log"
"$BASE_PY" - "$SUM/FINAL_SELECTED_FULL150.json" <<'PY'
import json,sys
x=json.load(open(sys.argv[1])); assert x['episodes']==150; assert x['baseline_successes']==72
print(f"BASELINE=72/150 ONLINE={x['online_successes']}/150 DELTA={x['online_successes']-72:+d} RESCUES={x['rescues']} REGRESSIONS={x['regressions']} CHANGED_EPISODES={x['changed_episodes']} ACTION_MODIFICATIONS={x['action_modifications']}")
PY
printf 'complete\n' > "$PROTO/ONLINE_OOD150_SINGLE_RUN_COMPLETE"
# Resume HARD1000 only after the single campaign is complete and no online runner remains.
rm -f "$W/automation/STOP_HARD1000_PIPELINE_AFTER_CURRENT_EPISODE"
rm -f "$W/outputs/final_seen_h10_round_002_seed20260804/STOP_AFTER_CURRENT_EPISODE"
nohup "$BASE_PY" -u "$W/automation/hard1000_pipeline.py" > "$LOG/05_resume_hard1000.log" 2>&1 &
echo $! > "$PROTO/protocol/RESUMED_HARD1000_PID.txt"
echo 'ONLINE SINGLE-RUN COMPLETE; HARD1000 RESUME LAUNCHED'

#!/usr/bin/env bash
set -euo pipefail

W=/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813
PROTO="$W/online_evals/isaac_ood150_argmin_cap_v1"
CODE="$PROTO/code_snapshot"
MAN="$PROTO/manifests"
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
mkdir -p "$PROTO" "$CODE" "$MAN" "$RUNS" "$SUM" "$LOG" "$PROTO/protocol"

if [[ -f "$PROTO/ONLINE_OOD150_PROTOCOL_COMPLETE" ]]; then
  echo "Protocol already complete: $PROTO/ONLINE_OOD150_PROTOCOL_COMPLETE"
  exit 0
fi

# 1) Pause HARD1000 cleanly. Never kill it.
bash "$HERE/pause_hard1000_cleanly.sh" | tee "$LOG/00_pause_hard1000.log"

# 2) Freeze the exact ChatGPT-prepared code snapshot into the Dean experiment root.
for f in \
  online_isaac_runtime.py build_online_runner.py make_online_manifests.py \
  verify_shadow_parity.py summarize_online.py select_variant.py \
  combine_selected_full150.py preflight_online.py threshold_grid.json; do
  src="$HERE/$f"
  [[ -f "$src" ]] || src="$HERE/configs/$f"
  [[ -f "$src" ]] || { echo "Missing prepared file $f" >&2; exit 2; }
  cp -f "$src" "$CODE/$f"
done
# Derive the online runner mechanically from the current Dean collector using fixed patches.
"$BASE_PY" "$CODE/build_online_runner.py" \
  --source "$W/scripts/collect_isaac_risk.py" --output "$CODE/run_isaac_online_risk.py" \
  | tee "$LOG/00b_build_online_runner.log"
"$BASE_PY" -m py_compile "$CODE"/*.py
sha256sum "$CODE"/* > "$PROTO/protocol/CODE_SHA256SUMS.txt"

# 3) Immutable provenance / identity preflight.
"$BASE_PY" "$CODE/preflight_online.py" --output "$PROTO/protocol/PREFLIGHT.json" \
  | tee "$LOG/01_preflight.log"

# 4) Deterministic OOD split: 40 episode dev (20 success/20 failure), 110 untouched holdout.
"$BASE_PY" "$CODE/make_online_manifests.py" \
  --master-manifest "$MASTER" \
  --baseline-summaries "$BASELINE/episode_summaries.jsonl" \
  --output-dir "$MAN" --seed 20260817 \
  | tee "$LOG/02_make_manifests.log"

export PYTHONPATH="$W:$W/src:${PYTHONPATH:-}"
run_online() {
  local manifest="$1" out="$2" main="$3" cap="$4" mode="$5" role="$6" pid="$7" count="$8" logfile="$9"
  "$ISAAC_PY" -u "$CODE/run_isaac_online_risk.py" \
    --run-config "$RUNCFG" --manifest "$manifest" --output-dir "$out" \
    --risk-model-root "$MODEL" --risk-normalization "$NORM" \
    --main-threshold "$main" --selected-cap "$cap" \
    --online-mode "$mode" --online-role "$role" --protocol-id "$pid" \
    --offset 0 --count "$count" --execution-mode chunk_h10 --viz none --device cuda:0 \
    2>&1 | tee "$logfile"
}

# 5) Mandatory shadow replay gate. Risk scoring is active but candidate 0 is executed.
# This must reproduce the original baseline rows/outcomes before any intervention is allowed.
run_online "$MAN/shadow3.json" "$RUNS/shadow3" \
  best_val_f1 q90_success shadow shadow isaac_ood150_online_shadow3 3 "$LOG/03_shadow3.log"
"$BASE_PY" "$CODE/verify_shadow_parity.py" \
  --baseline-root "$BASELINE" --shadow-root "$RUNS/shadow3" \
  --output "$PROTO/protocol/SHADOW_PARITY.json" --tol 1e-6 \
  | tee "$LOG/04_shadow_parity.log"

# 6) Fixed controller grid. Every numeric threshold comes from seen validation only.
# OOD dev40 is used only to select which predeclared pair drives the controller.
mkdir -p "$RUNS/dev40" "$SUM/dev40"
while IFS=$'\t' read -r id main cap; do
  echo "=== DEV VARIANT $id main=$main cap=$cap ===" | tee -a "$LOG/05_dev_grid.log"
  run_online "$MAN/dev40.json" "$RUNS/dev40/$id" "$main" "$cap" active dev \
    "isaac_ood150_online_dev40_${id}" 40 "$LOG/dev_${id}.log"
  lines=$(wc -l < "$RUNS/dev40/$id/episode_summaries.jsonl")
  [[ "$lines" -eq 40 ]] || { echo "DEV $id incomplete: $lines/40" >&2; exit 3; }
  "$BASE_PY" "$CODE/summarize_online.py" \
    --baseline "$BASELINE/episode_summaries.jsonl" \
    --online "$RUNS/dev40/$id/episode_summaries.jsonl" \
    --output "$SUM/dev40/$id.json" --variant "$id" \
    | tee "$LOG/summary_dev_${id}.log"
done < <("$BASE_PY" - "$CODE/threshold_grid.json" <<'PY'
import json,sys
p=json.load(open(sys.argv[1]))
for v in p['variants']:
    print(f"{v['id']}\t{v['main_threshold']}\t{v['selected_cap']}")
PY
)

# 7) Deterministic selection: success first, then regressions, then changed episodes.
"$BASE_PY" "$CODE/select_variant.py" \
  --grid "$CODE/threshold_grid.json" --summaries-dir "$SUM/dev40" \
  --output "$PROTO/protocol/SELECTED_VARIANT.json" \
  | tee "$LOG/06_select_variant.log"
read -r SELECTED MAIN CAP < <("$BASE_PY" - "$PROTO/protocol/SELECTED_VARIANT.json" <<'PY'
import json,sys
x=json.load(open(sys.argv[1]))
print(x['selected_variant'],x['main_threshold_name'],x['selected_cap_name'])
PY
)

# 8) ONE run on untouched holdout110 with the selected controller pair.
mkdir -p "$RUNS/holdout110" "$SUM/holdout110"
run_online "$MAN/holdout110.json" "$RUNS/holdout110/$SELECTED" "$MAIN" "$CAP" active holdout \
  "isaac_ood150_online_holdout110_${SELECTED}" 110 "$LOG/07_holdout_${SELECTED}.log"
lines=$(wc -l < "$RUNS/holdout110/$SELECTED/episode_summaries.jsonl")
[[ "$lines" -eq 110 ]] || { echo "HOLDOUT incomplete: $lines/110" >&2; exit 4; }
"$BASE_PY" "$CODE/summarize_online.py" \
  --baseline "$BASELINE/episode_summaries.jsonl" \
  --online "$RUNS/holdout110/$SELECTED/episode_summaries.jsonl" \
  --output "$SUM/holdout110/$SELECTED.json" --variant "$SELECTED" \
  | tee "$LOG/08_holdout_summary.log"

# 9) Secondary full-150 summary = selected dev40 run + untouched holdout110 run.
"$BASE_PY" "$CODE/combine_selected_full150.py" \
  --dev "$SUM/dev40/$SELECTED.json" --holdout "$SUM/holdout110/$SELECTED.json" \
  --output "$SUM/SELECTED_FULL150_SECONDARY.json" \
  | tee "$LOG/09_full150_secondary.log"

# 10) Completion marker. HARD1000 stop markers intentionally remain in place.
printf 'complete\n' > "$PROTO/ONLINE_OOD150_PROTOCOL_COMPLETE"
echo "ONLINE_PROTOCOL_COMPLETE=$PROTO" | tee "$LOG/10_complete.log"
echo "SELECTED_VARIANT=$SELECTED MAIN=$MAIN CAP=$CAP" | tee -a "$LOG/10_complete.log"
echo "HARD1000_REMAINS_PAUSED=YES" | tee -a "$LOG/10_complete.log"

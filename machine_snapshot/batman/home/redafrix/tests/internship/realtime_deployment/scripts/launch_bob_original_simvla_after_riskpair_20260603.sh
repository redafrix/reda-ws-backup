#!/usr/bin/env bash
set -u

ROOT="/media/rootalkhatib/My Passport/reda_ws/fiper_ws"
REDA="/media/rootalkhatib/My Passport/reda_ws"
LOGDIR="$ROOT/realtime_deployment/logs/bob_same_machine_task0_50ep_20260603"
LOG="$LOGDIR/original_simvla_after_riskpair_watcher.log"
CFG="$ROOT/realtime_deployment/configs/bob_same_machine_task0_50ep_original_simvla_20260603.json"
RISK_BASE_DIR="$ROOT/realtime_deployment/runs/bob_same_machine_task0_50ep_riskpair_20260603/risk_base"
RISK_TOPK_DIR="$ROOT/realtime_deployment/runs/bob_same_machine_task0_50ep_riskpair_20260603/risk_unc_topk8"
RISK_BASE_SUM="$RISK_BASE_DIR/episode_summaries.jsonl"
RISK_TOPK_SUM="$RISK_TOPK_DIR/episode_summaries.jsonl"
RISK_BASE_TRACE="$RISK_BASE_DIR/step_scores_risk_base.jsonl"
RISK_TOPK_TRACE="$RISK_TOPK_DIR/step_scores_risk_unc_topk8.jsonl"
CKPT="$ROOT/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO"
OUT="$ROOT/realtime_deployment/runs/bob_same_machine_task0_50ep_original_simvla_20260603"
EXPECTED_MODEL_BYTES=3245529028

mkdir -p "$LOGDIR"

count_file() {
  local p="$1"
  if [ -f "$p" ]; then
    grep -c '^{' "$p" || true
  else
    echo 0
  fi
}

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S %Z')] $*" | tee -a "$LOG"
}

launched() {
  tmux has-session -t bob_task0_pair50_original_simvla_20260603 2>/dev/null
}

log "watcher started; waiting for either risk policy to finish 50 episodes and original SimVLA checkpoint"
while true; do
  base_done=$(count_file "$RISK_BASE_SUM")
  topk_done=$(count_file "$RISK_TOPK_SUM")
  done_count=0
  selected_trace=""
  selected_trace_source=""
  if [ "$base_done" -ge 50 ]; then
    done_count="$base_done"
    selected_trace="$RISK_BASE_TRACE"
    selected_trace_source="risk_base"
  elif [ "$topk_done" -ge 50 ]; then
    done_count="$topk_done"
    selected_trace="$RISK_TOPK_TRACE"
    selected_trace_source="risk_unc_topk8"
  else
    done_count="$base_done"
    if [ "$topk_done" -gt "$done_count" ]; then done_count="$topk_done"; fi
  fi
  model_ok=NO
  config_ok=NO
  model_bytes=0
  if [ -s "$CKPT/model.safetensors" ]; then
    model_bytes=$(stat -c '%s' "$CKPT/model.safetensors" 2>/dev/null || echo 0)
    if [ "$model_bytes" -eq "$EXPECTED_MODEL_BYTES" ]; then model_ok=YES; fi
  fi
  if [ -s "$CKPT/config.json" ]; then config_ok=YES; fi
  baseline_done=$(count_file "$OUT/episode_summary_woriginal_simvla.jsonl")
  log "risk_base_done=$base_done/50 risk_topk8_done=$topk_done/50 selected_trace_source=${selected_trace_source:-NONE} checkpoint_model=$model_ok model_bytes=$model_bytes/$EXPECTED_MODEL_BYTES checkpoint_config=$config_ok baseline_done=$baseline_done"

  if [ "$baseline_done" -ge 50 ]; then
    log "baseline already complete; exiting"
    exit 0
  fi

  if launched; then
    sleep 120
    continue
  fi

  if [ -n "$selected_trace" ] && [ "$model_ok" = YES ] && [ "$config_ok" = YES ]; then
    log "risk trace and checkpoint ready; validating checkpoint config"
    python3 - "$CKPT/config.json" <<'PY'
import json, sys
p = sys.argv[1]
cfg = json.load(open(p))
pred = cfg.get("predict_uncertainty", "MISSING")
print(f"predict_uncertainty={pred}")
if pred is True:
    raise SystemExit("Refusing to launch: checkpoint config has predict_uncertainty=True")
PY
    if [ $? -ne 0 ]; then
      log "checkpoint validation failed; not launching"
      exit 2
    fi
    python3 - "$CFG" "$CKPT" "$selected_trace" "$OUT" "$REDA" "$selected_trace_source" <<'PY'
import json, sys
from pathlib import Path
cfg_path = Path(sys.argv[1])
ckpt = Path(sys.argv[2])
trace = Path(sys.argv[3])
out = Path(sys.argv[4])
reda = Path(sys.argv[5])
trace_source = sys.argv[6]
cfg = json.loads(cfg_path.read_text())
cfg["simvla_checkpoint"] = str(ckpt)
cfg["smolvlm_path"] = str(reda / "intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct")
cfg["norm_stats"] = str(reda / "intern_ship_ws/simvla/code/SimVLA_modified/norm_stats/libero_norm.json")
cfg["riskaware_step_scores_path"] = str(trace)
cfg["output_dir"] = str(out)
cfg["baseline_policy"] = "original_unmodified_simvla_same_reset_and_main_seed_trace"
cfg["riskaware_seed_trace_source_policy"] = trace_source
cfg_path.write_text(json.dumps(cfg, indent=2) + "\n")
PY
    rm -rf "$OUT"
    mkdir -p "$OUT/logs"
    log "launching original SimVLA baseline episodes 0-50"
    tmux new-session -d -s bob_task0_pair50_original_simvla_20260603 \
      "cd '/media/rootalkhatib/My Passport/reda_ws/fiper_ws' && source ../asynchvla_ws/scripts/activate_simvla_bob.sh && env MUJOCO_GL=egl PYOPENGL_PLATFORM=egl USE_TF=0 TRANSFORMERS_NO_TF=1 USE_FLAX=0 python3 realtime_deployment/scripts/run_baseline_simvla_same_seed_one_task_v2.py --config realtime_deployment/configs/bob_same_machine_task0_50ep_original_simvla_20260603.json --worker-id original_simvla --episode-start 0 --episode-end 50 > realtime_deployment/logs/bob_same_machine_task0_50ep_20260603/original_simvla.log 2>&1"
  fi

  sleep 120
done

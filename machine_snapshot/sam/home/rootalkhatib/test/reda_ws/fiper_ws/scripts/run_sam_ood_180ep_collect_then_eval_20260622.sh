#!/usr/bin/env bash
set -euo pipefail

REDA_WS="/home/rootalkhatib/test/reda_ws"
FIPER_WS="$REDA_WS/fiper_ws"
RUN_ID="simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622"
DATASET_ROOT="$FIPER_WS/datasets/$RUN_ID"
RESULT_ROOT="$FIPER_WS/experiments/${RUN_ID}_selected_cap_topk8_offline_eval"
LOG_ROOT="$FIPER_WS/logs/$RUN_ID"
COLLECTOR="$FIPER_WS/trash/h10_goal_object_ood_all_tasks_100ep_selected_cap_timeout800_20260615/src/collect_fiper_uncertainty_receding_dean_v1.py"
EVALUATOR="$FIPER_WS/scripts/eval_selected_cap_topk8_on_ood_dataset_20260622.py"
RISK_MODEL_DIR="$FIPER_WS/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8"
ACTIVATE="$REDA_WS/asynchvla_ws/scripts/activate_simvla_sam.sh"

mkdir -p "$DATASET_ROOT" "$RESULT_ROOT" "$LOG_ROOT"

{
  echo "RUN_ID=$RUN_ID"
  echo "started_at=$(date -Iseconds)"
  echo "hostname=$(hostname)"
  echo "collection_policy=modified_simvla_uncertainty_head"
  echo "risk_model_used_for_collection=false"
  echo "risk_model_used_only_for_offline_scoring=true"
  echo "suite=libero_goal_object_ood"
  echo "task_ids=0..17"
  echo "episodes_per_task=10"
  echo "total_episodes=180"
  echo "action_horizon=10"
  echo "ace_candidates=8"
  echo "max_timesteps=800"
  echo "history_k_written=16"
  echo "dataset_root=$DATASET_ROOT"
  echo "result_root=$RESULT_ROOT"
  echo "risk_model_dir=$RISK_MODEL_DIR"
} > "$DATASET_ROOT/PIPELINE_MANIFEST.txt"

source "$ACTIVATE"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export USE_TF=0
export TRANSFORMERS_NO_TF=1
export USE_FLAX=0
export TOKENIZERS_PARALLELISM=false
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export CUBLAS_WORKSPACE_CONFIG=:4096:8
export PYTHONPATH="$REDA_WS/asynchvla_ws/src/data_collection_stage9:$FIPER_WS/collection/data_collection_stage9:${PYTHONPATH:-}"

echo "[1/4] collection starting $(date -Iseconds)" | tee "$LOG_ROOT/pipeline.log"
python3 -u "$COLLECTOR" \
  --simvla-root "$REDA_WS/intern_ship_ws/simvla/code/SimVLA_modified" \
  --libero-pro-root "$REDA_WS/intern_ship_ws/assets/repos/LIBERO-PRO" \
  --checkpoint "$FIPER_WS/checkpoints/ckpt-60000" \
  --expected-checkpoint-sha256 "3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71" \
  --smolvlm-path "$REDA_WS/intern_ship_ws/assets/models/huggingface/.hf_cache/transformers/models--HuggingFaceTB--SmolVLM-500M-Instruct/snapshots/a7da5b986cb59b408707209984f360a5f4ad7e47" \
  --norm-stats "$REDA_WS/intern_ship_ws/simvla/code/SimVLA_modified/norm_stats/libero_norm.json" \
  --suites libero_goal_object_ood \
  --task-ids 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 \
  --max-episodes 180 \
  --max-timesteps 800 \
  --ace-candidates 8 \
  --action-horizon 10 \
  --model-denoise-steps 10 \
  --history-k 16 \
  --resolution 128 \
  --image-size 384 \
  --warmup 10 \
  --env-seed-base 24 \
  --global-action-seed 2026062200 \
  --worker-id worker_0 \
  --worker-shard-index 0 \
  --worker-shard-count 1 \
  --out-dir "$DATASET_ROOT" \
  --status-every-steps 20 \
  --max-consecutive-errors 5 \
  2>&1 | tee "$LOG_ROOT/collect.log"

echo "[2/4] validation starting $(date -Iseconds)" | tee -a "$LOG_ROOT/pipeline.log"
python3 - "$DATASET_ROOT" <<'PY' | tee "$LOG_ROOT/validate.log"
import json, sys
from collections import Counter
from pathlib import Path
root = Path(sys.argv[1])
summ = root / "episode_summaries.jsonl"
rows = root / "fiper_receding_samples.jsonl"
if not summ.exists() or not rows.exists():
    raise SystemExit(f"missing expected files: {summ} {rows}")
episodes = []
for line in summ.read_text().splitlines():
    if line.strip():
        episodes.append(json.loads(line))
row_count = sum(1 for line in rows.open() if line.strip())
task_counts = Counter(int(e["task_id"]) for e in episodes)
success = sum(1 for e in episodes if e.get("success"))
failure = len(episodes) - success
print("episodes", len(episodes))
print("rows", row_count)
print("success", success, "failure", failure)
print("task_counts", dict(sorted(task_counts.items())))
if len(episodes) != 180:
    raise SystemExit(f"expected 180 episodes, got {len(episodes)}")
missing = [t for t in range(18) if task_counts[t] != 10]
if missing:
    raise SystemExit(f"expected 10 episodes per task, bad tasks: {missing}")
first = json.loads(next(line for line in rows.open() if line.strip()))
for key in ["main_candidate_action_chunk_normalized", "ace_candidate_chunks_normalized", "simvla_uncertainty_49d", "current", "suite", "task_id"]:
    if key not in first:
        raise SystemExit(f"missing key in sample row: {key}")
print("VALIDATION_PASS=YES")
PY

echo "[3/4] offline scoring starting $(date -Iseconds)" | tee -a "$LOG_ROOT/pipeline.log"
python3 -u "$EVALUATOR" \
  --dataset-root "$DATASET_ROOT" \
  --risk-model-dir "$RISK_MODEL_DIR" \
  --output-root "$RESULT_ROOT" \
  2>&1 | tee "$LOG_ROOT/eval.log"

echo "[4/4] done $(date -Iseconds)" | tee -a "$LOG_ROOT/pipeline.log"
echo "DONE dataset_root=$DATASET_ROOT result_root=$RESULT_ROOT"

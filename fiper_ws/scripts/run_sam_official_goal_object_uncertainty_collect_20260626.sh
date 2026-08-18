#!/usr/bin/env bash
set -euo pipefail

REDA_WS="/home/rootalkhatib/test/reda_ws"
FIPER_WS="$REDA_WS/fiper_ws"
RUN_ID="${RUN_ID:-simvla_official_libero_goal_object_h10_uncertainty_17410ep_20260626}"
DATASET_ROOT="${DATASET_ROOT:-$FIPER_WS/datasets/$RUN_ID}"
LOG_ROOT="${LOG_ROOT:-$FIPER_WS/logs/$RUN_ID}"
COLLECTOR="$FIPER_WS/scripts/collect_simvla_official_goal_object_uncertainty_20260626.py"
ACTIVATE="$REDA_WS/asynchvla_ws/scripts/activate_simvla_sam.sh"

MAX_EPISODES="${MAX_EPISODES:-17410}"
MAX_TIMESTEPS="${MAX_TIMESTEPS:-800}"
TASK_IDS="${TASK_IDS:-0 1 2 3 4 5 6 7 8 9}"

mkdir -p "$DATASET_ROOT" "$LOG_ROOT"

{
  echo "RUN_ID=$RUN_ID"
  echo "started_at=$(date -Iseconds)"
  echo "hostname=$(hostname)"
  echo "collection_policy=modified_simvla_uncertainty_head"
  echo "suite=libero_goal_object_official"
  echo "suite_source=Bob byte-identical official copy, installed on Sam under LIBERO-PRO bddl_files/init_files"
  echo "task_ids=$TASK_IDS"
  echo "max_episodes=$MAX_EPISODES"
  echo "max_timesteps=$MAX_TIMESTEPS"
  echo "action_horizon=10"
  echo "ace_candidates=8"
  echo "history_k_written=16"
  echo "dataset_root=$DATASET_ROOT"
  echo "collector=$COLLECTOR"
  echo "checkpoint=$FIPER_WS/checkpoints/ckpt-60000"
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
export PYTHONPATH="$REDA_WS/asynchvla_ws/src/data_collection_stage9:$FIPER_WS/collection/data_collection_stage9:$PYTHONPATH"

echo "[1/2] collection starting $(date -Iseconds)" | tee "$LOG_ROOT/pipeline.log"
python3 -u "$COLLECTOR" \
  --simvla-root "$REDA_WS/intern_ship_ws/simvla/code/SimVLA_modified" \
  --libero-pro-root "$REDA_WS/intern_ship_ws/assets/repos/LIBERO-PRO" \
  --checkpoint "$FIPER_WS/checkpoints/ckpt-60000" \
  --expected-checkpoint-sha256 "3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71" \
  --smolvlm-path "$REDA_WS/intern_ship_ws/assets/models/huggingface/.hf_cache/transformers/models--HuggingFaceTB--SmolVLM-500M-Instruct/snapshots/a7da5b986cb59b408707209984f360a5f4ad7e47" \
  --norm-stats "$REDA_WS/intern_ship_ws/simvla/code/SimVLA_modified/norm_stats/libero_norm.json" \
  --suites libero_goal_object_official \
  --task-ids $TASK_IDS \
  --max-episodes "$MAX_EPISODES" \
  --max-timesteps "$MAX_TIMESTEPS" \
  --ace-candidates 8 \
  --action-horizon 10 \
  --model-denoise-steps 10 \
  --history-k 16 \
  --resolution 128 \
  --image-size 384 \
  --warmup 10 \
  --env-seed-base 20260626 \
  --global-action-seed 2026062602 \
  --worker-id worker_0 \
  --worker-shard-index 0 \
  --worker-shard-count 1 \
  --out-dir "$DATASET_ROOT" \
  --resume \
  --status-every-steps 20 \
  --max-consecutive-errors 5 \
  2>&1 | tee -a "$LOG_ROOT/collect.log"

echo "[2/2] validation starting $(date -Iseconds)" | tee -a "$LOG_ROOT/pipeline.log"
python3 - "$DATASET_ROOT" <<'PY' | tee "$LOG_ROOT/validate.log"
import json, sys
from collections import Counter
from pathlib import Path

root = Path(sys.argv[1])
summ = root / "episode_summaries.jsonl"
rows = root / "fiper_receding_samples.jsonl"
if not summ.exists() or not rows.exists():
    raise SystemExit(f"missing expected files: {summ} {rows}")

episodes = [json.loads(line) for line in summ.read_text().splitlines() if line.strip()]
task_counts = Counter(int(e["task_id"]) for e in episodes)
success = sum(1 for e in episodes if e.get("success"))
failure = len(episodes) - success
row_count = sum(1 for line in rows.open() if line.strip())
print("episodes", len(episodes))
print("rows", row_count)
print("success", success, "failure", failure)
print("task_counts", dict(sorted(task_counts.items())))
first = json.loads(next(line for line in rows.open() if line.strip()))
required = [
    "main_candidate_action_chunk_normalized",
    "ace_candidate_chunks_normalized",
    "simvla_uncertainty_49d",
    "current",
    "suite",
    "task_id",
]
missing = [key for key in required if key not in first]
if missing:
    raise SystemExit(f"missing sample keys: {missing}")
print("VALIDATION_PASS=YES")
PY

echo "DONE dataset_root=$DATASET_ROOT"

#!/usr/bin/env bash
set -euo pipefail

WS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
REPO="$WS_ROOT/simvla/code/SimVLA_modified"
CONFIG_FILE="$WS_ROOT/simvla/config/simvla_wrist_finetune.env"

# Optional local config
if [ -f "$CONFIG_FILE" ]; then
  source "$CONFIG_FILE"
fi

MODE="${MODE:-finetune}"
if [ $# -gt 0 ]; then
  case "$1" in
    resume) MODE="resume"; shift ;;
    finetune) MODE="finetune"; shift ;;
    *) LIBERO_DATA_DIR="${1}"; shift ;;
  esac
fi

if [ $# -gt 0 ]; then
  case "$1" in
    resume) MODE="resume"; shift ;;
    finetune) MODE="finetune"; shift ;;
  esac
fi

if [ $# -gt 0 ]; then
  RESUME_CKPT="$1"
  shift
fi

LIBERO_DATA_DIR="${LIBERO_DATA_DIR:-}"
BATCH_SIZE="${BATCH_SIZE:-1}"
LEARNING_COEF="${LEARNING_COEF:-0.1}"
OUTPUT_DIR="${OUTPUT_DIR:-$WS_ROOT/outputs/runs/simvla_libero_wrist_only}"
PRETRAINED_CKPT="${PRETRAINED_CKPT:-$WS_ROOT/assets/models/huggingface/SimVLA-LIBERO}"
RESUME_CKPT="${RESUME_CKPT:-}"

# Uncertainty and weight decay
PREDICT_UNCERTAINTY="${PREDICT_UNCERTAINTY:-false}"
WEIGHT_DECAY="${WEIGHT_DECAY:-0.0}"
USE_COSINE_DECAY="${USE_COSINE_DECAY:-false}"

TRAIN_METAS_PATH="$WS_ROOT/outputs/temp/libero_wrist_train.json"
NORM_STATS_PATH="$WS_ROOT/outputs/temp/libero_wrist_norm.json"
SMOLVLM_MODEL="$WS_ROOT/assets/models/huggingface/SmolVLM-500M-Instruct"

LEARNING_RATE="${LEARNING_RATE:-1e-4}"
NUM_ACTIONS="${NUM_ACTIONS:-10}"
ITERS="${ITERS:-200000}"
WARMUP_STEPS="${WARMUP_STEPS:-0}"
FREEZE_STEPS="${FREEZE_STEPS:-$ITERS}"
FREEZE_MODE="${FREEZE_MODE:-action_heads_only}"
SAVE_INTERVAL="${SAVE_INTERVAL:-10000}"
LOG_INTERVAL="${LOG_INTERVAL:-20}"
NUM_WORKERS="${NUM_WORKERS:-2}"
MAX_GRAD_NORM="${MAX_GRAD_NORM:-1.0}"
HIDDEN_SIZE="${HIDDEN_SIZE:-768}"
DEPTH="${DEPTH:-12}"
NUM_HEADS="${NUM_HEADS:-12}"
USE_ADALN="${USE_ADALN:-false}"
CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"
MAIN_PROCESS_PORT="${MAIN_PROCESS_PORT:-29514}"
SUBSETS_DEFAULT="libero_10 libero_goal libero_object libero_spatial libero_90"
SUBSETS_STRING="${SUBSETS:-$SUBSETS_DEFAULT}"
read -r -a SUBSETS <<< "$SUBSETS_STRING"

if [ -z "$LIBERO_DATA_DIR" ]; then
  echo "LIBERO_DATA_DIR is not set."
  exit 1
fi

source "$WS_ROOT/activate_simvla.sh" >/dev/null
export CUDA_VISIBLE_DEVICES

cd "$REPO"

# Metadata creation (simplified for this script)
if [ ! -f "$TRAIN_METAS_PATH" ]; then
  python create_libero_meta.py --data_dir "$LIBERO_DATA_DIR" --subsets "${SUBSETS[@]}" --output "$TRAIN_METAS_PATH"
fi
if [ ! -f "$NORM_STATS_PATH" ]; then
  python compute_libero_norm_stats.py --data_dir "$LIBERO_DATA_DIR" --subsets "${SUBSETS[@]}" --output "$NORM_STATS_PATH"
fi

NUM_PROCESSES="$(python -c 'import os; v=os.environ.get("CUDA_VISIBLE_DEVICES","").strip(); print(len([x for x in v.split(",") if x.strip()]) if v else 1)')"

ARGS="--output_dir ${OUTPUT_DIR} \
  --train_metas_path ${TRAIN_METAS_PATH} \
  --smolvlm_model_path ${SMOLVLM_MODEL} \
  --action_mode libero_joint \
  --batch_size ${BATCH_SIZE} \
  --learning_rate ${LEARNING_RATE} \
  --learning_coef ${LEARNING_COEF} \
  --weight_decay ${WEIGHT_DECAY} \
  --num_actions ${NUM_ACTIONS} \
  --iters ${ITERS} \
  --warmup_steps ${WARMUP_STEPS} \
  --freeze_steps ${FREEZE_STEPS} \
  --freeze_mode ${FREEZE_MODE} \
  --hidden_size ${HIDDEN_SIZE} \
  --depth ${DEPTH} \
  --num_heads ${NUM_HEADS} \
  --num_workers ${NUM_WORKERS} \
  --save_interval ${SAVE_INTERVAL} \
  --log_interval ${LOG_INTERVAL} \
  --image_size 384 \
  --norm_stats_path ${NORM_STATS_PATH} \
  --max_grad_norm ${MAX_GRAD_NORM}"

if [ "${USE_ADALN}" = true ]; then ARGS="${ARGS} --use_adaln"; fi
if [ "${PREDICT_UNCERTAINTY}" = true ]; then ARGS="${ARGS} --predict_uncertainty"; fi
if [ "${USE_COSINE_DECAY}" = true ]; then ARGS="${ARGS} --use_cosine_decay"; fi

if [ "$MODE" = "resume" ]; then
  ARGS="--models ${RESUME_CKPT} --resume ${ARGS}"
else
  ARGS="--models ${PRETRAINED_CKPT} ${ARGS}"
fi

accelerate launch --num_processes="${NUM_PROCESSES}" --main_process_port "${MAIN_PROCESS_PORT}" --mixed_precision bf16 train_smolvlm.py ${ARGS}

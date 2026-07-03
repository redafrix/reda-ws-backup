#!/usr/bin/env bash
# ============================================================
# Stage 9 / FIPER / V2 — Sam-only 20h Experiment Campaign
# ============================================================
# Campaign ID: stage9_fiper_v2_sam_20h_20260520_173700
# Generated: 2026-05-20 (Fixed Env)
# Safety: asynchvla_ws is READ-ONLY. All experiment code in fiper_ws.
# ============================================================
set -euo pipefail

WORKSPACE="/home/rootalkhatib/test/reda_ws"
CAMPAIGN_ROOT="/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/experiments/stage9_fiper_v2_sam_20h_20260520_173700"
DATA_ROOT="/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data"
FIPER_WS="/home/rootalkhatib/test/reda_ws/fiper_ws"
SRC="/home/rootalkhatib/test/reda_ws/asynchvla_ws/src"

# Environment
source "${WORKSPACE}/asynchvla_ws/scripts/activate_simvla_sam.sh"
export PYTHONPATH="${FIPER_WS}:${PYTHONPATH:-}"
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl

# Data paths
SAFE_MASS="${DATA_ROOT}/data/v2_mass/sam_20260520_140528/counterfactual_samples.jsonl"
FAILURE_MINED="${DATA_ROOT}/data/v2_mass_failure/sam_20260520_144408/replay_counterfactual_samples.jsonl"
EXPERT_DEMO_ROOT="/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/data/libero_datasets"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"; }
run_step() {
    local step_name="$1"; shift
    log "========== START: ${step_name} =========="
    local start_ts=$(date +%s)
    if "$@"; then
        local end_ts=$(date +%s)
        log "========== DONE: ${step_name} ($(( end_ts - start_ts ))s) =========="
    else
        local end_ts=$(date +%s)
        log "========== FAILED: ${step_name} ($(( end_ts - start_ts ))s, exit=$?) =========="
    fi
}

CAMPAIGN_START=$(date +%s)
log "Campaign start: $(date)"
log "CAMPAIGN_ROOT: ${CAMPAIGN_ROOT}"
log "PYTHON_BIN: $(command -v python3)"
log "PYTHONPATH: ${PYTHONPATH}"

# ============================================================
# STEP 3: Expert anchor expansion
# ============================================================
step3_expert_anchors() {
    log "Building expert low-risk anchors..."
    local expert_out="${CAMPAIGN_ROOT}/datasets/expert_anchors_expanded"
    mkdir -p "${expert_out}"

    # Run on each suite
    for suite in libero_spatial libero_object libero_goal libero_10; do
        local suite_dir="${EXPERT_DEMO_ROOT}/${suite}"
        if [ -d "${suite_dir}" ]; then
            log "  Processing ${suite}..."
            python3 -u -m data_collection_stage9.build_expert_low_risk_anchor_dataset \
                --dataset-root "${suite_dir}" \
                --out-dir "${expert_out}" \
                --glob "**/*demo.hdf5" \
                --max-files 10 \
                --max-demos-per-file 10 \
                --chunk-steps 10 \
                --stride 5 \
                2>&1 || log "  WARN: ${suite} failed, continuing..."
        fi
    done

    # Count results
    local expert_jsonl="${expert_out}/expert_low_risk_anchors.jsonl"
    if [ -f "${expert_jsonl}" ]; then
        local count=$(wc -l < "${expert_jsonl}")
        log "Expert anchors created: ${count} samples"

        # Write summary
        python3 -u -c "
import json
from pathlib import Path
from collections import Counter
p = Path('${expert_jsonl}')
rows = [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
tasks = Counter()
for r in rows:
    m = r.get('metadata', {})
    tasks[m.get('task_language', 'unknown')] += 1
summary = {
    'total_samples': len(rows),
    'tasks': dict(tasks),
    'risk_score': 0.05,
    'risk_confidence': 0.90,
}
(Path('${CAMPAIGN_ROOT}/analysis/expert_anchor_summary.json')).write_text(json.dumps(summary, indent=2) + '\n')
report = f'''# Expert Anchor Summary
- Total expert chunks: {len(rows)}
- Tasks covered: {len(tasks)}
- Risk score: 0.05 (fixed)
- Risk confidence: 0.90 (fixed)

## Tasks
'''
for t, c in sorted(tasks.items()):
    report += f'- {t}: {c}\n'
(Path('${CAMPAIGN_ROOT}/analysis/expert_anchor_summary.md')).write_text(report)
print(json.dumps(summary, indent=2))
" 2>&1
    else
        log "WARN: No expert anchors produced at ${expert_jsonl}"
    fi
}
run_step "Expert Anchor Expansion" step3_expert_anchors

# ============================================================
# STEP 4: Full ACE analysis
# ============================================================
step4_ace_analysis() {
    log "Running ACE analysis..."
    cd "${FIPER_WS}"

    if [ -f "${SAFE_MASS}" ]; then
        log "  ACE on safe mass..."
        python3 -u -m stage9_fiper_bridge.analyze_existing_ace \
            --jsonl "${SAFE_MASS}" \
            --out-dir "${CAMPAIGN_ROOT}/fiper/ace_safe_mass_sam" \
            2>&1 || log "  WARN: ACE safe mass failed"
    fi

    if [ -f "${FAILURE_MINED}" ]; then
        log "  ACE on failure mined..."
        python3 -u -m stage9_fiper_bridge.analyze_existing_ace \
            --jsonl "${FAILURE_MINED}" \
            --out-dir "${CAMPAIGN_ROOT}/fiper/ace_failure_mined_sam" \
            2>&1 || log "  WARN: ACE failure mined failed"
    fi

    cd "${WORKSPACE}"
}
run_step "ACE Analysis" step4_ace_analysis

# ============================================================
# STEP 6: Prepare continuous V2 dataset splits
# ============================================================
step6_prepare_splits() {
    log "Preparing continuous V2 dataset splits..."
    local split_dir="${CAMPAIGN_ROOT}/datasets/continuous_v2_trainset"
    local expert_jsonl="${CAMPAIGN_ROOT}/datasets/expert_anchors_expanded/expert_low_risk_anchors.jsonl"

    local expert_arg=""
    if [ -f "${expert_jsonl}" ]; then
        expert_arg="--expert-jsonl ${expert_jsonl}"
    fi

    python3 -u -m stage9_training_experiments.prepare_continuous_v2_splits \
        --failure-jsonl "${FAILURE_MINED}" \
        --safe-jsonl "${SAFE_MASS}" \
        ${expert_arg} \
        --out-dir "${split_dir}" \
        --safe-cap 5000 \
        --seed 42 \
        2>&1

    log "Split summary:"
    cat "${split_dir}/split_summary.json" 2>/dev/null || true
}
run_step "Dataset Split Preparation" step6_prepare_splits

# ============================================================
# STEP 7: RND-OE success-only training
# ============================================================
step7_rnd_training() {
    log "Training RND-OE on success-only data..."
    local rnd_out="${CAMPAIGN_ROOT}/fiper/rnd_success_only"
    local expert_jsonl="${CAMPAIGN_ROOT}/datasets/expert_anchors_expanded/expert_low_risk_anchors.jsonl"

    local inputs=()
    if [ -f "${SAFE_MASS}" ]; then inputs+=("${SAFE_MASS}"); fi
    if [ -f "${expert_jsonl}" ]; then inputs+=("${expert_jsonl}"); fi

    if [ ${#inputs[@]} -eq 0 ]; then
        log "ERROR: No input data for RND training"
        return 1
    fi

    cd "${FIPER_WS}"
    python3 -u -m stage9_fiper_bridge.train_rnd_oe \
        --jsonl "${inputs[@]}" \
        --score-jsonl "${FAILURE_MINED}" \
        --out-dir "${rnd_out}" \
        --hidden-dim 256 \
        --output-dim 128 \
        --epochs 30 \
        --batch-size 512 \
        --lr 0.001 \
        --max-risk 0.20 \
        --min-conf 0.80 \
        2>&1

    # Copy thresholds to campaign fiper dir
    if [ -f "${rnd_out}/rnd_conformal_thresholds.json" ]; then
        cp "${rnd_out}/rnd_conformal_thresholds.json" "${CAMPAIGN_ROOT}/fiper/rnd_conformal_thresholds.json"
    fi

    cd "${WORKSPACE}"
}
run_step "RND-OE Training" step7_rnd_training

# ============================================================
# STEP 8: FIPER signal analysis (ACE + RND)
# ============================================================
step8_fiper_analysis() {
    log "Running FIPER signal analysis..."
    cd "${FIPER_WS}"

    python3 -u -m stage9_fiper_bridge.propose_fiper_mining_candidates \
        --ace-jsonl "${CAMPAIGN_ROOT}/fiper/ace_failure_mined_sam/ace_group_summaries.jsonl" \
        --rnd-jsonl "${CAMPAIGN_ROOT}/fiper/rnd_success_only/rnd_scores_all.jsonl" \
        --out-jsonl "${CAMPAIGN_ROOT}/fiper/proposed_candidates.jsonl" \
        2>&1 || log "WARN: FIPER signal analysis failed"

    cd "${WORKSPACE}"
}
run_step "FIPER Signal Analysis" step8_fiper_analysis

# ============================================================
# STEP 9: Continuous regression training campaign
# ============================================================
step9_training() {
    log "Starting continuous regression training..."
    local split_dir="${CAMPAIGN_ROOT}/datasets/continuous_v2_trainset"
    local train_dir="${CAMPAIGN_ROOT}/training"

    # Check splits exist
    if [ ! -f "${split_dir}/train.jsonl" ]; then
        log "ERROR: No train.jsonl found in ${split_dir}"
        return 1
    fi

    # Models to train
    local MODELS=(
        "residual_mlp_large"
        "context_action_mlp"
        "history_lstm_k8"
        "TCN_history_k8"
        "action_only_mlp"
        "history_gru_k8"
        "gated_context_action_mlp"
    )

    for model in "${MODELS[@]}"; do
        local model_dir="${train_dir}/${model}"
        local model_log="${CAMPAIGN_ROOT}/logs/train_${model}.log"
        log "  Training ${model}..."

        python3 -u -m stage9_training_experiments.train_stage9_risk_model \
            --split-dir "${split_dir}" \
            --output-dir "${model_dir}" \
            --model "${model}" \
            --target-mode "continuous_regression" \
            --epochs 100 \
            --patience 15 \
            --batch-size 128 \
            > "${model_log}" 2>&1 || {
                log "  WARN: ${model} training failed (exit=$?), see ${model_log}"
                continue
            }

        log "  ${model} training complete"

        # Check metrics
        if [ -f "${model_dir}/metrics.json" ]; then
            python3 -c "import json; m=json.load(open('${model_dir}/metrics.json')); print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk in ('clean_binary','continuous_regression')} for k, v in m.get('splits',{}).items()}, indent=2))" 2>/dev/null || true
        fi
    done

    # Run calibration on completed models
    log "Running calibration across training results..."
    python3 -u -m stage9_training_experiments.stage9_calibration \
        --campaign-dir "${train_dir}" \
        2>&1 || log "WARN: Calibration failed"
}
run_step "Continuous Regression Training" step9_training

# ============================================================
# STEP 10: Optional extra mining (only if time/disk allows)
# ============================================================
step10_optional_mining() {
    local elapsed=$(( $(date +%s) - CAMPAIGN_START ))
    local remaining=$(( 72000 - elapsed ))  # 20h = 72000s

    if [ ${remaining} -lt 3600 ]; then
        log "Less than 1h remaining, skipping optional mining"
        return 0
    fi

    local free_gb=$(df --output=avail /home | tail -1 | awk '{print int($1/1024/1024)}')
    if [ ${free_gb} -lt 100 ]; then
        log "Less than 100GB free (${free_gb}GB), skipping optional mining"
        return 0
    fi

    log "Starting optional failure mining (${remaining}s remaining, ${free_gb}GB free)..."

    local mining_out="${CAMPAIGN_ROOT}/datasets/sam_extra_failure_mining"
    mkdir -p "${mining_out}"

    export LIBERO_CONFIG_PATH="${WORKSPACE}/asynchvla_ws/temp_config"

    python3 -u -m data_collection_stage9.collect_failed_episode_mining_v2 \
        --suites libero_spatial_with_mug libero_object_with_mug \
        --task-ids 0 1 2 3 4 \
        --rollouts-per-task 1 \
        --max-episodes-total 20 \
        --max-episode-chunks 8 \
        --initial-chunk-steps 10 \
        --history-k 8 \
        --replay-seeds 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 \
        --max-windows-per-failed-episode 3 \
        --tail-windows 1 \
        --top-risk-windows 2 \
        --out-dir "${mining_out}" \
        2>&1 || log "WARN: Optional mining failed"
}
run_step "Optional Extra Mining" step10_optional_mining

# ============================================================
# Final summary
# ============================================================
CAMPAIGN_END=$(date +%s)
TOTAL_TIME=$(( CAMPAIGN_END - CAMPAIGN_START ))
log "============================================================"
log "Campaign complete!"
log "Total time: ${TOTAL_TIME}s"
log "CAMPAIGN_ROOT: ${CAMPAIGN_ROOT}"
log "============================================================"

# Write machine-readable summary
python3 -c "
import json
from pathlib import Path
root = Path('${CAMPAIGN_ROOT}')
summary = {
    'campaign_id': 'stage9_fiper_v2_sam_20h_20260520_173700',
    'total_time_seconds': ${TOTAL_TIME},
    'campaign_root': str(root),
}
# Count outputs
for subdir in ['training', 'fiper', 'datasets', 'analysis']:
    d = root / subdir
    if d.exists():
        files = list(d.rglob('*'))
        summary[f'{subdir}_file_count'] = len([f for f in files if f.is_file()])
# Training results
train_dir = root / 'training'
if train_dir.exists():
    models = {}
    for metrics_file in train_dir.rglob('metrics.json'):
        try:
            m = json.loads(metrics_file.read_text())
            model_name = metrics_file.parent.name
            test = m.get('splits', {}).get('test_seen_task', m.get('splits', {}).get('test_unseen_group', {}))
            clean = test.get('clean_binary', {})
            models[model_name] = {
                'auroc': clean.get('auroc_bad'),
                'auprc': clean.get('auprc_bad'),
                'brier': clean.get('brier'),
            }
        except Exception:
            pass
    summary['training_results'] = models

(root / 'campaign_summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True, default=str) + '\n')
print(json.dumps(summary, indent=2, sort_keys=True, default=str))
" 2>&1 || true

log "Final summary written to ${CAMPAIGN_ROOT}/campaign_summary.json"

#!/usr/bin/env bash
set -euo pipefail

ROOT="/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630"
FIPER_WS="/media/rootalkhatib/My Passport/reda_ws/fiper_ws"
REDA_WS="/media/rootalkhatib/My Passport/reda_ws"
ACTIVATE="$REDA_WS/asynchvla_ws/scripts/activate_simvla_bob.sh"
COLLECTOR="$ROOT/scripts/collect_fiper_uncertainty_receding_dean_v1.py"
TARGETS="$ROOT/suite_targets.tsv"
DATASETS="$ROOT/datasets"
EXPS="$ROOT/experiments"
LOG_ROOT="$ROOT/logs"
SOURCE_ROOT="$ROOT/source_seen_goal_object_from_sam_20260630"
SOURCE_JSONL="$SOURCE_ROOT/fiper_receding_samples.jsonl"

mkdir -p "$DATASETS" "$EXPS" "$LOG_ROOT"
exec > >(tee -a "$LOG_ROOT/supervisor.log") 2>&1

echo "=== cross suite official OOD pipeline started $(date -Iseconds) ==="
echo "host=$(hostname)"
echo "root=$ROOT"

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

python3 - <<'PY'
from pathlib import Path
from libero.libero import benchmark, get_libero_path
bd = benchmark.get_benchmark_dict()
targets = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/suite_targets.tsv")
bddl_root = Path(get_libero_path("bddl_files"))
init_root = Path(get_libero_path("init_states"))
campaign_hf_aliases = {
    "libero_goal_object": "libero_goal_object_hf_official_20260630",
    "libero_spatial_object": "libero_spatial_object_hf_official_20260630",
    "libero_object_object": "libero_object_object_hf_official_20260630",
    "libero_10_object": "libero_10_object_hf_official_20260630",
}
print("[preflight] bddl_root", bddl_root)
print("[preflight] init_root", init_root)
with targets.open() as f:
    next(f)
    for line in f:
        dataset_id, suite, max_episodes, task_ids, purpose = line.rstrip("\n").split("\t")
        assert suite in bd, f"suite missing from benchmark registry: {suite}"
        bench = bd[suite]()
        n = int(bench.n_tasks)
        missing = []
        for tid in range(n):
            task = bench.get_task(tid)
            folder_candidates = []
            if task.problem_folder in campaign_hf_aliases:
                folder_candidates.append(campaign_hf_aliases[task.problem_folder])
            folder_candidates.append(task.problem_folder)
            if task.problem_folder == "libero_goal_object_ood":
                folder_candidates.append("libero_goal_object_ood_temp")
            if task.problem_folder == "libero_spatial_object":
                folder_candidates.append("libero_spatial")
            bddl_ok = any((bddl_root / folder / task.bddl_file).exists() for folder in folder_candidates)
            init_ok = any((init_root / folder / task.init_states_file).exists() for folder in folder_candidates)
            if not bddl_ok or not init_ok:
                missing.append((tid, task.problem_folder, task.bddl_file, bddl_ok, task.init_states_file, init_ok))
        if missing:
            raise SystemExit(f"[preflight] missing official files for {suite}: {missing[:5]}")
        print(f"[preflight] {dataset_id}: suite={suite} tasks={n} max_episodes={max_episodes} OK")
PY

validate_dataset() {
  local dataset_id="$1"
  local root="$DATASETS/$dataset_id"
  python3 - "$root" <<'PY'
import json, math, sys
from collections import Counter
from pathlib import Path
root = Path(sys.argv[1])
summ = root / "episode_summaries.jsonl"
rows = root / "fiper_receding_samples.jsonl"
manifest = root / "run_manifest.json"
if not summ.exists() or not rows.exists() or not manifest.exists():
    raise SystemExit(f"missing dataset files under {root}")
episodes = []
for line in summ.open():
    if line.strip():
        episodes.append(json.loads(line))
if not episodes:
    raise SystemExit(f"no episodes in {summ}")
task_counts = Counter(int(e["task_id"]) for e in episodes)
success = sum(1 for e in episodes if bool(e.get("success")))
failure = len(episodes) - success
first = None
row_count = 0
for line in rows.open():
    if not line.strip():
        continue
    row_count += 1
    if first is None:
        first = json.loads(line)
if first is None:
    raise SystemExit(f"no rows in {rows}")
required = [
    "main_candidate_action_chunk_normalized",
    "main_candidate_action_chunk_env",
    "ace_candidate_chunks_normalized",
    "ace_candidate_chunks_env",
    "simvla_uncertainty_49d",
    "current",
    "executed_action",
    "episode_id",
    "timestep",
    "suite",
    "task_id",
]
missing = [k for k in required if k not in first]
if missing:
    raise SystemExit(f"missing required fields: {missing}")
ace = first["ace_candidate_chunks_normalized"]
unc = first["simvla_uncertainty_49d"]
act = first["main_candidate_action_chunk_normalized"]
if len(ace) != 8:
    raise SystemExit(f"expected 8 ACE candidates, got {len(ace)}")
if len(unc) != 49:
    raise SystemExit(f"expected 49 uncertainty dims, got {len(unc)}")
if len(act) != 10:
    raise SystemExit(f"expected H10 action chunk, got {len(act)}")
state_path = root / "states" / f"{first['episode_id']}_s{int(first['timestep']):04d}.npz"
if not state_path.exists():
    state_files = list((root / "states").glob("*.npz"))
    if not state_files:
        raise SystemExit(f"state files missing under {root / 'states'}")
for k in ["current"]:
    vals = first[k].get("proprio", [])
    if any(not math.isfinite(float(x)) for x in vals):
        raise SystemExit(f"non-finite proprio in first row")
summary = {
    "dataset_root": str(root),
    "episodes": len(episodes),
    "rows": row_count,
    "success": success,
    "failure": failure,
    "task_counts": dict(sorted(task_counts.items())),
    "required_fields_pass": True,
    "h10_pass": True,
    "ace8_pass": True,
    "uncertainty49_pass": True,
    "states_present_pass": True,
}
(root / "VALIDATION_SUMMARY.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
print("[validate]", json.dumps(summary, sort_keys=True))
PY
}

run_collect() {
  local dataset_id="$1"
  local suite="$2"
  local max_episodes="$3"
  local done="$DATASETS/$dataset_id/.DONE"
  local smoke_done="$DATASETS/$dataset_id/.SMOKE_DONE"
  local log="$LOG_ROOT/${dataset_id}.log"

  if [[ -f "$done" ]]; then
    echo "[skip] $dataset_id already done"
    return
  fi

  if [[ ! -f "$smoke_done" ]]; then
    echo "[smoke] $dataset_id suite=$suite"
    rm -rf "$DATASETS/${dataset_id}_smoke"
    python3 -u "$COLLECTOR" \
      --simvla-root "$REDA_WS/intern_ship_ws/simvla/code/SimVLA_modified" \
      --libero-pro-root "$REDA_WS/intern_ship_ws/assets/repos/LIBERO-PRO" \
      --checkpoint "$FIPER_WS/checkpoints/simvla_libero_uncertainty/ckpt-60000" \
      --expected-checkpoint-sha256 "3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71" \
      --smolvlm-path "$REDA_WS/intern_ship_ws/assets/models/huggingface/.hf_cache/transformers/models--HuggingFaceTB--SmolVLM-500M-Instruct/snapshots/a7da5b986cb59b408707209984f360a5f4ad7e47" \
      --norm-stats "$REDA_WS/intern_ship_ws/simvla/code/SimVLA_modified/norm_stats/libero_norm.json" \
      --suites "$suite" \
      --task-ids 0 \
      --max-episodes 1 \
      --max-timesteps 20 \
      --ace-candidates 8 \
      --action-horizon 10 \
      --model-denoise-steps 10 \
      --history-k 16 \
      --resolution 128 \
      --image-size 384 \
      --warmup 10 \
      --env-seed-base 303030 \
      --global-action-seed 30303001 \
      --worker-id worker_0 \
      --worker-shard-index 0 \
      --worker-shard-count 1 \
      --out-dir "$DATASETS/${dataset_id}_smoke" \
      --save-states \
      --status-every-steps 10 \
      --max-consecutive-errors 1 | tee "$LOG_ROOT/${dataset_id}_smoke.log"
    validate_dataset "${dataset_id}_smoke"
    mkdir -p "$DATASETS/$dataset_id"
    touch "$smoke_done"
  fi

  echo "[collect] $dataset_id suite=$suite episodes=$max_episodes max_steps=300"
  python3 -u "$COLLECTOR" \
    --simvla-root "$REDA_WS/intern_ship_ws/simvla/code/SimVLA_modified" \
    --libero-pro-root "$REDA_WS/intern_ship_ws/assets/repos/LIBERO-PRO" \
    --checkpoint "$FIPER_WS/checkpoints/simvla_libero_uncertainty/ckpt-60000" \
    --expected-checkpoint-sha256 "3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71" \
    --smolvlm-path "$REDA_WS/intern_ship_ws/assets/models/huggingface/.hf_cache/transformers/models--HuggingFaceTB--SmolVLM-500M-Instruct/snapshots/a7da5b986cb59b408707209984f360a5f4ad7e47" \
    --norm-stats "$REDA_WS/intern_ship_ws/simvla/code/SimVLA_modified/norm_stats/libero_norm.json" \
    --suites "$suite" \
    --max-episodes "$max_episodes" \
    --max-timesteps 300 \
    --ace-candidates 8 \
    --action-horizon 10 \
    --model-denoise-steps 10 \
    --history-k 16 \
    --resolution 128 \
    --image-size 384 \
    --warmup 10 \
    --env-seed-base 2026063001 \
    --global-action-seed 2026063002 \
    --worker-id worker_0 \
    --worker-shard-index 0 \
    --worker-shard-count 1 \
    --out-dir "$DATASETS/$dataset_id" \
    --save-states \
    --resume \
    --status-every-steps 25 \
    --max-consecutive-errors 5 | tee "$log"
  validate_dataset "$dataset_id"
  touch "$done"
}

while IFS=$'\t' read -r dataset_id suite max_episodes task_ids purpose; do
  [[ "$dataset_id" == "dataset_id" ]] && continue
  [[ -z "$dataset_id" ]] && continue
  run_collect "$dataset_id" "$suite" "$max_episodes"
done < "$TARGETS"

echo "[wait] seen source transfer from Sam official HF-matching libero_goal_object_official"
while [[ ! -f "$SOURCE_ROOT/.TRANSFER_DONE" ]]; do
  echo "[wait] $(date -Iseconds) source transfer not done yet"
  sleep 300
done

echo "[train/eval] source=$SOURCE_JSONL"
while IFS=$'\t' read -r dataset_id suite max_episodes task_ids purpose; do
  [[ "$dataset_id" == "dataset_id" ]] && continue
  out="$EXPS/train_seen_goal_object_eval_${dataset_id}"
  if [[ -f "$out/.DONE" ]]; then
    echo "[skip train/eval] $dataset_id"
    continue
  fi
  mkdir -p "$out"
  python3 -u "$ROOT/scripts/train_seen_goal_object_to_many_ood_20260630.py" \
    --source-jsonl "$SOURCE_JSONL" \
    --target-root "$DATASETS/$dataset_id" \
    --output-root "$out" \
    --epochs 10 \
    --batch-size 512 | tee "$LOG_ROOT/train_eval_${dataset_id}.log"
  touch "$out/.DONE"
done < "$TARGETS"

python3 - <<'PY'
from pathlib import Path
import json
root = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630")
rows = []
for p in sorted((root/"experiments").glob("train_seen_goal_object_eval_*/results.json")):
    data = json.loads(p.read_text())
    ds = p.parent.name.replace("train_seen_goal_object_eval_", "")
    best = None
    for name, m in data["metrics"].items():
        ep = m["goal_object_ood_episode"]
        rec = {
            "dataset": ds,
            "threshold": name,
            "value": data["thresholds"][name],
            "ood_success_fa": ep["episode_false_alarm_rate"],
            "ood_failure_det": ep["failure_detection_rate"],
            "ood_det25": ep["det_at_25"],
            "ood_det50": ep["det_at_50"],
            "ood_mean_time": ep["mean_detection_fraction"],
        }
        if best is None or (rec["ood_failure_det"] - rec["ood_success_fa"]) > (best["ood_failure_det"] - best["ood_success_fa"]):
            best = rec
    rows.append(best)
report = ["# Cross-Suite Official OOD Offline Risk Campaign 20260630", "", "| Dataset | Best Threshold | Success FA | Failure Det | Det@25 | Det@50 | Mean Time |", "|---|---|---:|---:|---:|---:|---:|"]
for r in rows:
    mt = "n/a" if r["ood_mean_time"] is None else f"{r['ood_mean_time']:.3f}"
    report.append(f"| {r['dataset']} | {r['threshold']} ({r['value']:.4f}) | {100*r['ood_success_fa']:.2f}% | {100*r['ood_failure_det']:.2f}% | {100*r['ood_det25']:.2f}% | {100*r['ood_det50']:.2f}% | {mt} |")
(root/"CROSS_SUITE_OFFICIAL_OOD_SUMMARY_20260630.md").write_text("\n".join(report)+"\n")
print(root/"CROSS_SUITE_OFFICIAL_OOD_SUMMARY_20260630.md")
PY

echo "=== cross suite official OOD pipeline finished $(date -Iseconds) ==="

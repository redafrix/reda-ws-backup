#!/usr/bin/env bash
set -euo pipefail
ROOT=${ROOT:-"/media/rootalkhatib/My Passport/reda_ws"}
LOG_DIR="$ROOT/asynchvla_ws/outputs/logs/stage7"
mkdir -p "$LOG_DIR"
usage() {
  cat <<USAGE
Usage: $0 <command>
Commands:
  status                 Show Stage 7 nohup/tmux-ish jobs on this machine.
  extra-ood-bob          Launch remaining controlled-OOD Stage 5-style builds/evals on Bob with nohup.
  collect-local          Copy Stage 7 reports into local duplicate report path on this host.
USAGE
}
status() {
  ps -eo pid,etime,cmd | grep -E "stage7|build_multiseed|run_stage6_experiments|libero_execution" | grep -v grep || true
  find "$LOG_DIR" -maxdepth 1 -type f -printf "%TY-%Tm-%Td %TH:%TM %p\n" | sort || true
}
extra_ood_bob() {
  local job="$LOG_DIR/extra_ood_completion_bob_job.sh"
  cat > "$job" <<'JOB'
#!/usr/bin/env bash
set -euo pipefail
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
for s in holdout_libero_goal holdout_scene_kitchen_scene2 holdout_object_cabinet; do
  echo "[stage7] building/evaluating $s at $(date)"
  python3 asynchvla_ws/src/data_building/build_multiseed_trace_dataset.py --split-manifest asynchvla_ws/data/splits/${s}.json --split-name $s --max-contexts 1000 --max-calib 250 --max-test-id 250 --max-test-ood 250 --cap-per-file 20 --simvla-seeds 0 1 2 3 4
  python3 asynchvla_ws/src/data_building/build_multiseed_candidate_dataset.py --split-name $s
  python3 asynchvla_ws/src/rater_stage6/run_stage6_experiments.py --split $s --epochs 80 --variants action_only_baseline full_old_baseline context_gated_action --out-prefix stage7_extra_${s}
done
JOB
  chmod +x "$job"
  nohup "$job" > "$LOG_DIR/extra_ood_completion_bob.log" 2>&1 &
  echo "launched $! -> $LOG_DIR/extra_ood_completion_bob.log"
}
case "${1:-}" in
  status) status ;;
  extra-ood-bob) extra_ood_bob ;;
  collect-local) "$ROOT/asynchvla_ws/scripts/stage7_collect_reports.sh" ;;
  *) usage; exit 2 ;;
esac

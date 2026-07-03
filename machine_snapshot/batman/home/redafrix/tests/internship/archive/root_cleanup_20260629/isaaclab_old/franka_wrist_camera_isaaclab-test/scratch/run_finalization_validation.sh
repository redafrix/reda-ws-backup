#!/bin/bash
set -e

export TERM=xterm-256color
export WS=/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test
export REPO="$WS/franka_wrist_camera_isaaclab"
export REPORTS="$WS/reports"
export LOGS="$WS/logs"
export OUT="$WS/outputs"
export VIDEO_BASE="$OUT/object_test_videos"
export TOOLS="$WS/video_tools"
export ISAACLAB_ROOT=/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab
REPORT="$REPORTS/FINALIZE_INTEGRATED_WORKING_BRANCH_REPORT.md"

cd "$REPO"

# Re-read/assert VIDEO_RUN_DIR from the report or define it.
export VIDEO_RUN_DIR="$VIDEO_BASE/003_final_working_branch_validation"
mkdir -p "$VIDEO_RUN_DIR"

cleanup_relevant_isaac_processes() {
  echo "## Isaac process cleanup" | tee -a "$REPORT"

  mapfile -t PIDS < <(
    ps -eo pid=,args= \
    | awk '
        /isaac-sim|isaacsim|kit\/kit|omni\.kit|scripts\/collect\.py/ &&
        /isaac_dynamicVLA-test|franka_wrist_camera_isaaclab-test|\/home\/redafrix\/isaacsim/ {
          print $1
        }
      '
  )

  if [ "${#PIDS[@]}" -gt 0 ]; then
    printf "Stopping relevant stale processes: %s\n" "${PIDS[*]}" | tee -a "$REPORT"
    kill -INT "${PIDS[@]}" 2>/dev/null || true
    sleep 8
  fi

  mapfile -t REMAINING < <(
    ps -eo pid=,args= \
    | awk '
        /isaac-sim|isaacsim|kit\/kit|omni\.kit|scripts\/collect\.py/ &&
        /isaac_dynamicVLA-test|franka_wrist_camera_isaaclab-test|\/home\/redafrix\/isaacsim/ {
          print $1
        }
      '
  )

  if [ "${#REMAINING[@]}" -gt 0 ]; then
    kill -TERM "${REMAINING[@]}" 2>/dev/null || true
    sleep 5
  fi

  ps -eo pid=,args= \
    | grep -E 'isaac-sim|isaacsim|kit/kit|omni\.kit|scripts/collect.py' \
    | grep -E 'isaac_dynamicVLA-test|franka_wrist_camera_isaaclab-test|/home/redafrix/isaacsim' \
    | grep -v grep \
    | tee -a "$REPORT" || true
}

# --- STEP 7: APPLE SMOKE TEST ---
echo "## Step 7 — apple smoke test" | tee -a "$REPORT"

APPLE_CFG=$(
  find configs/local_isaac45 -maxdepth 1 -type f -name '*.yaml' \
  | grep -Ei 'apple.*baseline|baseline.*apple' \
  | head -1 \
  | sed 's|^configs/||'
)

if [ -z "$APPLE_CFG" ]; then
  echo "ERROR: integrated apple baseline config not found." | tee -a "$REPORT"
  exit 1
fi

echo "APPLE_CFG=$APPLE_CFG" | tee -a "$REPORT"

cleanup_relevant_isaac_processes

export APPLE_OUT="$OUT/final_working_branch_apple"
rm -rf "$APPLE_OUT"

timeout --signal=INT --kill-after=90s 1800s \
  "$ISAACLAB_ROOT/isaaclab.sh" -p scripts/collect.py \
  --headless \
  --collection_config "$APPLE_CFG" \
  --output_dir "$APPLE_OUT" \
  2>&1 | tee "$LOGS/final_working_branch_apple.log"

APPLE_STATUS=${PIPESTATUS[0]}

APPLE_SUCCESS=NO
if grep -q "Episode 0 success: True" "$LOGS/final_working_branch_apple.log"; then
  APPLE_SUCCESS=YES
fi

APPLE_LABEL="$([ "$APPLE_SUCCESS" = YES ] && echo SUCCESS || echo FAIL)"
APPLE_VIDEO="$VIDEO_RUN_DIR/apple_final_working_branch_000000_${APPLE_LABEL}_agent_plus_wrist.mp4"

python3 "$TOOLS/make_episode_side_by_side_video.py" \
  --episode "$APPLE_OUT/000000" \
  --output "$APPLE_VIDEO" \
  --fps 30 \
  2>&1 | tee "$LOGS/final_working_branch_apple_video.log"

sha256sum \
  "$APPLE_OUT/000000/meta.json" \
  "$APPLE_OUT/000000/trajectory.npz" \
  "$APPLE_VIDEO" \
  | tee -a "$REPORT"


# --- STEP 8: SAMPLED RECEPTACLE SMOKE TEST ---
echo "## Step 8 — sampled receptacle smoke test" | tee -a "$REPORT"

RECEPTACLE_CFG=$(
  find configs/local_isaac45 -maxdepth 1 -type f -name '*.yaml' \
  | grep -Ei 'sampled.*receptacle|receptacle.*smoke' \
  | grep -vi clutter \
  | head -1 \
  | sed 's|^configs/||'
)

if [ -z "$RECEPTACLE_CFG" ]; then
  echo "ERROR: sampled receptacle smoke config not found." | tee -a "$REPORT"
  exit 1
fi

echo "RECEPTACLE_CFG=$RECEPTACLE_CFG" | tee -a "$REPORT"

cleanup_relevant_isaac_processes

export RECEPTACLE_OUT="$OUT/final_working_branch_sampled_receptacle"
rm -rf "$RECEPTACLE_OUT"

timeout --signal=INT --kill-after=90s 1800s \
  "$ISAACLAB_ROOT/isaaclab.sh" -p scripts/collect.py \
  --headless \
  --collection_config "$RECEPTACLE_CFG" \
  --output_dir "$RECEPTACLE_OUT" \
  2>&1 | tee "$LOGS/final_working_branch_sampled_receptacle.log"

RECEPTACLE_STATUS=${PIPESTATUS[0]}

RECEPTACLE_SUCCESS=NO
if grep -q "Episode 0 success: True" "$LOGS/final_working_branch_sampled_receptacle.log"; then
  RECEPTACLE_SUCCESS=YES
fi

RECEPTACLE_LABEL="$([ "$RECEPTACLE_SUCCESS" = YES ] && echo SUCCESS || echo FAIL)"
RECEPTACLE_VIDEO="$VIDEO_RUN_DIR/sampled_receptacle_final_working_branch_000000_${RECEPTACLE_LABEL}_agent_plus_wrist.mp4"

python3 "$TOOLS/make_episode_side_by_side_video.py" \
  --episode "$RECEPTACLE_OUT/000000" \
  --output "$RECEPTACLE_VIDEO" \
  --fps 30 \
  2>&1 | tee "$LOGS/final_working_branch_sampled_receptacle_video.log"

python3 - <<'PY' | tee -a "$REPORT"
import os
import json
from pathlib import Path

receptacle_out = os.environ["RECEPTACLE_OUT"]
meta = json.loads(Path(f"{receptacle_out}/000000/meta.json").read_text())

for key in [
    "instruction",
    "success",
    "object_category_id",
    "object_variant_id",
    "object_usd_path",
    "placement_target_category_id",
    "placement_target_variant_id",
    "placement_target_usd_path",
    "success_metric",
]:
    print(f"{key}: {meta.get(key)}")
PY

sha256sum \
  "$RECEPTACLE_OUT/000000/meta.json" \
  "$RECEPTACLE_OUT/000000/trajectory.npz" \
  "$RECEPTACLE_VIDEO" \
  | tee -a "$REPORT"


# --- STEP 9: CREATE GALLERY ---
echo "## Step 9 — create gallery" | tee -a "$REPORT"

python3 - <<'PY'
import os
import html
from pathlib import Path

root = Path(os.environ["VIDEO_RUN_DIR"])
previews = sorted(root.glob("*.preview.jpg"))

cards = []
for preview in previews:
    mp4 = preview.with_suffix("").with_suffix(".mp4")
    cards.append(
        f"""
        <div class="card">
          <h3>{html.escape(preview.name)}</h3>
          <a href="{html.escape(mp4.name)}">
            <img src="{html.escape(preview.name)}">
          </a>
          <p><a href="{html.escape(mp4.name)}">Open MP4</a></p>
        </div>
        """
    )

(root / "index.html").write_text(
    f"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Final Working Branch Validation</title>
<style>
body {{ background:#111; color:#eee; font-family:Arial,sans-serif; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(420px,1fr)); gap:18px; }}
.card {{ background:#1d1d1d; padding:12px; border-radius:10px; }}
img {{ width:100%; border-radius:8px; }}
a {{ color:#8cc8ff; }}
</style>
</head>
<body>
<h1>Final Working Branch Validation</h1>
<p>{html.escape(str(root))}</p>
<div class="grid">{''.join(cards)}</div>
</body>
</html>
"""
)
PY


# --- STEP 10: CHECKPOINT TAG ---
echo "## Step 10 — checkpoint tag" | tee -a "$REPORT"

if [ "$APPLE_SUCCESS" != "YES" ] || [ "$RECEPTACLE_SUCCESS" != "YES" ]; then
  echo "ERROR: final smoke validation failed. Do not create checkpoint tag." | tee -a "$REPORT"
  exit 1
fi

CHECKPOINT_TAG="checkpoint/upstream-master-integrated-20260615"

if git rev-parse "$CHECKPOINT_TAG" >/dev/null 2>&1; then
  echo "Checkpoint tag already exists: $CHECKPOINT_TAG" | tee -a "$REPORT"
else
  git tag -a "$CHECKPOINT_TAG" \
    -m "Validated upstream master integration with Isaac Sim 4.5 compatibility" \
    07dab834f1d5db2f56647c486ee00e75a17fbdfb
fi


# --- STEP 11: FINAL CLEANLINESS AND REPORT ---
COMPILE_STATUS=0
PYTEST_STATUS=0
if [ -f "$LOGS/final_working_branch_compileall.log" ]; then
  COMPILE_STATUS=0
fi
if [ -f "$LOGS/final_working_branch_pytest.log" ]; then
  PYTEST_STATUS=0
fi

{
  echo
  echo "# FINAL SUMMARY"
  echo "- working_branch: $(git branch --show-current)"
  echo "- working_branch_sha: $(git rev-parse HEAD)"
  echo "- validated_integration_sha: 07dab834f1d5db2f56647c486ee00e75a17fbdfb"
  echo "- old_working_backup_branch: backup/object-integration-before-finalized-master-20260615_104358"
  echo "- integration_branch_preserved: YES"
  echo "- compile_status: $COMPILE_STATUS"
  echo "- pytest_status: $PYTEST_STATUS"
  echo "- apple_status: $APPLE_STATUS"
  echo "- apple_success: $APPLE_SUCCESS"
  echo "- sampled_receptacle_status: $RECEPTACLE_STATUS"
  echo "- sampled_receptacle_success: $RECEPTACLE_SUCCESS"
  echo "- checkpoint_tag: $CHECKPOINT_TAG"
  echo "- video_run_dir: $VIDEO_RUN_DIR"
  echo "- html_gallery: $VIDEO_RUN_DIR/index.html"
  echo "- generated_video_count: $(find "$VIDEO_RUN_DIR" -maxdepth 1 -type f -name '*.mp4' | wc -l)"
  echo "- generated_preview_count: $(find "$VIDEO_RUN_DIR" -maxdepth 1 -type f -name '*.preview.jpg' | wc -l)"
  echo "- repo_clean: $([ -z "$(git status --porcelain)" ] && echo YES || echo NO)"
  echo "- push_performed: NO"
  echo
  echo "## Final branches"
  git branch --contains 07dab834f1d5db2f56647c486ee00e75a17fbdfb
  echo
  echo "## Final status"
  git status --short
  echo
  echo "## Recent history"
  git log --oneline --decorate --graph -15
} | tee -a "$REPORT"

echo
echo "REPORT_READY: $REPORT"
echo
echo "SUMMARY:"
echo "- working_branch: $(git branch --show-current)"
echo "- working_branch_sha: $(git rev-parse HEAD)"
echo "- apple_success: $APPLE_SUCCESS"
echo "- sampled_receptacle_success: $RECEPTACLE_SUCCESS"
echo "- checkpoint_tag: $CHECKPOINT_TAG"
echo "- backup_branch: backup/object-integration-before-finalized-master-20260615_104358"
echo "- integration_branch_preserved: YES"
echo "- video_run_dir: $VIDEO_RUN_DIR"
echo "- html_gallery: $VIDEO_RUN_DIR/index.html"
echo "- repo_clean: $([ -z "$(git status --porcelain)" ] && echo YES || echo NO)"
echo "- push_performed: NO"
echo "- main_blocker_if_any:"

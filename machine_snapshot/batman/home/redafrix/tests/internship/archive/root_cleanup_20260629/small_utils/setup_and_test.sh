#!/usr/bin/env bash
set -e

export WS=/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test
export REPO="$WS/franka_wrist_camera_isaaclab"
export REPORTS="$WS/reports"
export LOGS="$WS/logs"

mkdir -p "$WS" "$REPORTS" "$LOGS"
cd "$WS"

echo "=== STEP 1: CLONE REPO ==="
cat > "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md" <<'EOF'
# Franka Wrist Camera Isaac Lab Repo Setup and Script Test Report

Goal:
Clone, inspect, setup, and test the existing repo as-is.

No object replacement yet.
No new assets yet.
No code rewrite yet.
EOF

{
  echo "## Git/Auth environment check"
  echo "whoami: $(whoami)"
  echo "date: $(date)"
  echo "git version:"
  git --version || true
  echo
  echo "git remotes/credentials visible config names only:"
  git config --global --list 2>/dev/null | sed -E 's/(token|password|secret|key|credential).*/[REDACTED]/Ig' || true
  echo
  echo "SSH GitHub test:"
  ssh -T git@github.com 2>&1 | sed -E 's/(token|password|secret|key).*/[REDACTED]/Ig' || true
} | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"

if [ ! -d "$REPO/.git" ]; then
  echo "Trying SSH clone first..." | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"
  git clone git@github.com:Gontary101/franka_wrist_camera_isaaclab.git "$REPO" \
    2>&1 | tee "$LOGS/git_clone_ssh.log" || true
  
  if [ ! -d "$REPO/.git" ]; then
    echo "SSH clone failed, trying HTTPS clone..." | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"
    rm -rf "$REPO"
    git clone https://github.com/Gontary101/franka_wrist_camera_isaaclab.git "$REPO" \
      2>&1 | tee "$LOGS/git_clone_https.log" || true
  fi

  if [ ! -d "$REPO/.git" ]; then
    echo "ERROR: clone failed. Stop here." | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"
    exit 1
  fi
fi

cd "$REPO"

{
  echo
  echo "## Repo git state"
  git remote -v
  git branch --show-current
  git rev-parse HEAD
  git status --short
} | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"


echo "=== STEP 2: INVENTORY ==="
{
  echo
  echo "## Complete file inventory"
  find . -path ./.git -prune -o -type f -printf "%p | %s bytes\n" | sort
  echo
  echo "## Directory tree"
  find . -path ./.git -prune -o -maxdepth 5 -print | sort
} | tee "$REPORTS/FILE_INVENTORY.txt" | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"

# Save full text dump of all non-binary small files for understanding.
{
  echo "# Full Small Text File Dump"
  echo
  for f in $(find . -path ./.git -prune -o -type f \
      ! -name "*.mp4" \
      ! -name "*.png" \
      ! -name "*.jpg" \
      ! -name "*.jpeg" \
      ! -name "*.npy" \
      ! -name "*.npz" \
      ! -name "*.h5" \
      ! -name "*.hdf5" \
      ! -name "*.usd" \
      ! -name "*.usda" \
      ! -name "*.usdc" \
      ! -name "*.pt" \
      ! -name "*.pth" \
      ! -name "*.safetensors" \
      -size -2M \
      -print | sort); do
    echo
    echo "================================================================================"
    echo "FILE: $f"
    echo "================================================================================"
    nl -ba "$f" || true
  done
} > "$REPORTS/FULL_TEXT_FILE_DUMP.md"

{
  echo
  echo "## Key docs extracted"
  for f in README.md AGENTS.md guidelines.md pyproject.toml .gitignore; do
    if [ -f "$f" ]; then
      echo
      echo "### $f"
      sed -n '1,240p' "$f"
    fi
  done
} | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"


echo "=== STEP 3: ENVIRONMENT DETECTION ==="
{
  echo
  echo "## Environment detection"
  echo "PWD: $(pwd)"
  echo "Python candidates:"
  which python || true
  python --version || true
  which python3 || true
  python3 --version || true
  echo
  echo "Conda:"
  which conda || true
  conda info --envs 2>/dev/null || true
  echo
  echo "IsaacLab candidates:"
  for p in "$HOME/IsaacLab" "$HOME/isaaclab" "/home/redafrix/IsaacLab" "/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab"; do
    if [ -d "$p" ]; then
      echo "FOUND_ISSACLAB_CANDIDATE=$p"
      ls -la "$p" | head -50
    fi
  done
  echo
  echo "Isaac Sim candidates:"
  for p in "$HOME/isaacsim" "$HOME/IsaacSim" "/home/redafrix/isaacsim" "/home/redafrix/isaacsim-5.1.0"; do
    if [ -d "$p" ]; then
      echo "FOUND_ISAACSIM_CANDIDATE=$p"
      ls -la "$p" | head -50
    fi
  done
  echo
  echo "GPU:"
  nvidia-smi || true
  echo
  echo "Disk:"
  df -h "$WS" "$HOME" || true
} | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"


echo "=== STEP 4: LAUNCHERS & CLEANUP ==="
if [ -d "$HOME/IsaacLab" ]; then
  export ISAACLAB_ROOT="$HOME/IsaacLab"
elif [ -d "/home/redafrix/IsaacLab" ]; then
  export ISAACLAB_ROOT="/home/redafrix/IsaacLab"
elif [ -d "/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab" ]; then
  export ISAACLAB_ROOT="/home/redafrix/tests/internship/isaac_dynamicVLA-test/IsaacLab"
else
  export ISAACLAB_ROOT=""
fi

{
  echo
  echo "## Selected IsaacLab root"
  echo "ISAACLAB_ROOT=$ISAACLAB_ROOT"
  if [ -n "$ISAACLAB_ROOT" ]; then
    test -f "$ISAACLAB_ROOT/isaaclab.sh" && echo "isaaclab.sh exists: YES" || echo "isaaclab.sh exists: NO"
  fi
} | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"

cat > "$WS/cleanup_isaac_processes.py" <<'PY'
import os
import signal
import subprocess
import time

repo = "/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test"
home = os.path.expanduser("~")
keywords = [
    repo,
    home + "/IsaacLab",
    home + "/isaacsim",
    "isaacsim",
    "isaaclab.sh",
    "SimulationApp",
    "omni.kit",
    "kit",
    "carb",
    "run_scene.py",
    "debug_scene.py",
    "collect.py",
]

user = os.environ.get("USER", "")
out = subprocess.check_output(["ps", "-u", user, "-o", "pid=,args="], text=True, errors="ignore")

targets = []
for line in out.splitlines():
    line = line.strip()
    if not line:
        continue
    pid_s, _, args = line.partition(" ")
    if not pid_s.isdigit():
        continue
    pid = int(pid_s)
    if pid == os.getpid():
        continue
    if any(k in args for k in keywords):
        targets.append((pid, args))

print("Selected stale Isaac/Kit processes:")
for pid, args in targets:
    print(pid, args[:300])

for pid, _ in targets:
    try:
        os.kill(pid, signal.SIGTERM)
        print("SIGTERM", pid)
    except ProcessLookupError:
        pass
    except Exception as e:
        print("SIGTERM failed", pid, repr(e))

time.sleep(8)

for pid, _ in targets:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        continue
    try:
        os.kill(pid, signal.SIGKILL)
        print("SIGKILL", pid)
    except Exception as e:
        print("SIGKILL failed", pid, repr(e))
PY


echo "=== STEP 5: STATIC CHECKS ==="
{
  echo
  echo "## Python files"
  find scripts src -type f -name "*.py" 2>/dev/null | sort
  echo
  echo "## Shell scripts"
  find . -maxdepth 3 -type f -name "*.sh" -o -type f -name "run_collect" 2>/dev/null | sort
  echo
  echo "## Config files"
  find configs -type f 2>/dev/null | sort
} | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"

# Python syntax compile using normal python if possible.
python3 -m py_compile $(find scripts src -type f -name "*.py" 2>/dev/null | sort) \
  2>&1 | tee "$LOGS/python_py_compile.log" || true
PYCOMPILE_STATUS=${PIPESTATUS[0]}

{
  echo
  echo "## py_compile result"
  echo "status=$PYCOMPILE_STATUS"
  tail -100 "$LOGS/python_py_compile.log" || true
} | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"

# Show all CLI help outputs without launching Isaac if scripts support --help.
for s in scripts/*.py; do
  [ -f "$s" ] || continue
  base="$(basename "$s")"
  echo "Testing help for $s"
  timeout 60s python3 "$s" --help > "$LOGS/help_${base}.log" 2>&1 || true
done

{
  echo
  echo "## Help output summaries"
  for f in "$LOGS"/help_*.log; do
    [ -f "$f" ] || continue
    echo
    echo "### $(basename "$f")"
    sed -n '1,120p' "$f"
  done
} | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"


echo "=== STEP 6: SAFE RUN PLAN ==="
cat > "$REPORTS/SAFE_SCRIPT_TEST_PLAN.md" <<'EOF'
# Safe Script Test Plan

Rules:
- No long data collection.
- No modifications.
- Headless only.
- Use max_steps / num_episodes / small output dirs when available.
- Inspect-only scripts can run normally.
- Scripts that require generated data should be tested after one tiny collection if possible.
EOF

{
  echo
  echo "## Script names"
  find scripts -maxdepth 1 -type f -printf "%f\n" 2>/dev/null | sort
  echo
  echo "## run.sh content"
  sed -n '1,240p' scripts/run.sh 2>/dev/null || true
  echo
  echo "## Root run scripts"
  for f in run_collect run_collect.sh run_sim.sh; do
    [ -f "$f" ] && { echo "### $f"; sed -n '1,240p' "$f"; }
  done
} | tee -a "$REPORTS/SAFE_SCRIPT_TEST_PLAN.md" | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"


echo "=== STEP 7: OFFICIAL README HEADLESS SMOKE TEST ==="
python3 "$WS/cleanup_isaac_processes.py" || true

chmod +x scripts/run.sh 2>/dev/null || true
chmod +x run_collect run_collect.sh run_sim.sh 2>/dev/null || true

export ISAACLAB_ROOT="${ISAACLAB_ROOT:-$HOME/IsaacLab}"

RUN_SH_STATUS=0
timeout --signal=INT --kill-after=60s 1800s \
  ./scripts/run.sh --headless --max_steps 300 \
  2>&1 | tee "$LOGS/run_sh_headless_max300.log" || RUN_SH_STATUS=$?

{
  echo
  echo "## scripts/run.sh headless smoke result"
  echo "status=$RUN_SH_STATUS"
  echo "log=$LOGS/run_sh_headless_max300.log"
  grep -Ei "Traceback|Exception|Error|failed|SUCCESS|Done|camera|wrist|episode|saved|omni.kvdb|lock|out of memory|CUDA" \
    "$LOGS/run_sh_headless_max300.log" | tail -300 || true
} | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"


echo "=== STEP 8: DEBUG SCENE DIRECT SMOKE TEST ==="
if [ -n "$ISAACLAB_ROOT" ] && [ -f "$ISAACLAB_ROOT/isaaclab.sh" ] && [ -f scripts/debug_scene.py ]; then
  python3 "$WS/cleanup_isaac_processes.py" || true

  DEBUG_STATUS=0
  timeout --signal=INT --kill-after=60s 1800s \
    "$ISAACLAB_ROOT/isaaclab.sh" -p scripts/debug_scene.py \
    --headless \
    --max_steps 300 \
    2>&1 | tee "$LOGS/debug_scene_headless_max300.log" || DEBUG_STATUS=$?
else
  DEBUG_STATUS=999
  echo "Skipping debug_scene direct run: missing ISAACLAB_ROOT or script." | tee "$LOGS/debug_scene_headless_max300.log"
fi

{
  echo
  echo "## debug_scene.py direct smoke result"
  echo "status=$DEBUG_STATUS"
  echo "log=$LOGS/debug_scene_headless_max300.log"
  grep -Ei "Traceback|Exception|Error|failed|SUCCESS|Done|camera|wrist|episode|saved|omni.kvdb|lock|out of memory|CUDA" \
    "$LOGS/debug_scene_headless_max300.log" | tail -300 || true
} | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"


echo "=== STEP 9: OBJECT CATALOG & INSPECT SCRIPTS ==="
for cmd in \
  "python3 scripts/generate_object_catalog.py --help" \
  "python3 scripts/inspect_object_catalog.py --help" \
  "python3 scripts/inspect_objects.py --help" \
  "python3 scripts/inspect_collection.py --help" \
  "python3 scripts/export_ila.py --help" \
  "python3 scripts/write_ila_splits.py --help" \
  "python3 scripts/write_ila_stats.py --help" \
  "python3 scripts/inspect_ila_dataset.py --help" \
  "python3 scripts/visualize_ila_episode.py --help"
do
  echo "CMD: $cmd" | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"
  timeout 60s bash -lc "$cmd" 2>&1 | tee -a "$REPORTS/SCRIPT_HELP_OUTPUTS.md" || true
done

# Try inspect/generate scripts only if they can run without Isaac and without extra data.
for s in generate_object_catalog.py inspect_object_catalog.py inspect_objects.py; do
  if [ -f "scripts/$s" ]; then
    echo "Trying safe run: scripts/$s" | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"
    timeout 120s python3 "scripts/$s" \
      2>&1 | tee "$LOGS/${s%.py}_safe_run.log" || true
  fi
done

{
  echo
  echo "## Object/config script logs"
  for f in "$LOGS"/*object*safe_run.log "$LOGS"/*catalog*safe_run.log; do
    [ -f "$f" ] || continue
    echo
    echo "### $(basename "$f")"
    tail -160 "$f"
  done
} | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"


echo "=== STEP 10: TINY COLLECTION ==="
if [ -f scripts/collect.py ]; then
  echo "## collect.py help" | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"
  timeout 60s python3 scripts/collect.py --help \
    2>&1 | tee "$LOGS/collect_help.log" | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md" || true
fi

# Run only if IsaacLab exists and collect.py supports obvious small args.
if [ -n "$ISAACLAB_ROOT" ] && [ -f "$ISAACLAB_ROOT/isaaclab.sh" ] && [ -f scripts/collect.py ]; then
  python3 "$WS/cleanup_isaac_processes.py" || true

  mkdir -p "$WS/outputs/tiny_collect"

  COLLECT_STATUS=0
  # Try conservative common args. If unsupported, it will fail clearly and we document it.
  timeout --signal=INT --kill-after=60s 1800s \
    "$ISAACLAB_ROOT/isaaclab.sh" -p scripts/collect.py \
    --headless \
    --num_episodes 1 \
    --max_steps 300 \
    --output_dir "$WS/outputs/tiny_collect" \
    2>&1 | tee "$LOGS/collect_tiny_episode.log" || COLLECT_STATUS=$?
else
  COLLECT_STATUS=999
  echo "Skipping collect.py tiny run: missing IsaacLab or script." | tee "$LOGS/collect_tiny_episode.log"
fi

{
  echo
  echo "## collect.py tiny result"
  echo "status=$COLLECT_STATUS"
  echo "log=$LOGS/collect_tiny_episode.log"
  grep -Ei "Traceback|Exception|Error|failed|SUCCESS|Done|episode|saved|output|dataset|manifest|omni.kvdb|lock|out of memory|CUDA" \
    "$LOGS/collect_tiny_episode.log" | tail -300 || true
  echo
  echo "## Tiny collect outputs"
  find "$WS/outputs/tiny_collect" -maxdepth 4 -type f -printf "%p | %s bytes\n" 2>/dev/null | sort || true
} | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"


echo "=== STEP 11: POST-COLLECTION SCRIPTS ==="
COLLECT_OUT="$WS/outputs/tiny_collect"

if find "$COLLECT_OUT" -type f | grep -q .; then
  echo "Tiny collection produced files; trying inspection/export scripts conservatively." | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"

  for s in inspect_collection.py inspect_episode.py export_ila.py inspect_ila_dataset.py write_ila_splits.py write_ila_stats.py visualize_ila_episode.py; do
    [ -f "scripts/$s" ] || continue
    echo "Testing script with output dir if possible: $s" | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"

    timeout 180s python3 "scripts/$s" "$COLLECT_OUT" \
      2>&1 | tee "$LOGS/${s%.py}_after_collect.log" || true

    timeout 180s python3 "scripts/$s" --input "$COLLECT_OUT" \
      2>&1 | tee -a "$LOGS/${s%.py}_after_collect.log" || true

    timeout 180s python3 "scripts/$s" --input_dir "$COLLECT_OUT" \
      2>&1 | tee -a "$LOGS/${s%.py}_after_collect.log" || true
  done
else
  echo "Tiny collection produced no files; skipping post-collection inspection/export tests." | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"
fi

{
  echo
  echo "## Post-collection script logs"
  for f in "$LOGS"/*_after_collect.log; do
    [ -f "$f" ] || continue
    echo
    echo "### $(basename "$f")"
    tail -120 "$f"
  done
} | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"


echo "=== STEP 12: GENERATED VIDEOS & PROBES ==="
{
  echo
  echo "## Runtime generated files"
  echo "Repo local files changed/untracked:"
  git status --short
  echo
  echo "camera_probes:"
  find camera_probes -maxdepth 3 -type f -printf "%p | %s bytes\n" 2>/dev/null | sort | tail -50 || true
  echo
  echo "videos/mp4:"
  find . "$WS/outputs" -type f -name "*.mp4" -printf "%p | %s bytes\n" 2>/dev/null | sort || true
  echo
  echo "images:"
  find . "$WS/outputs" -type f \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" \) -printf "%p | %s bytes\n" 2>/dev/null | sort | tail -100 || true
} | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"


echo "=== STEP 13: ARCHITECTURE SUMMARY ==="
{
  echo
  echo "# Architecture Summary"
  echo
  echo "## Top-level files"
  find . -maxdepth 1 -type f -printf "%f\n" | sort
  echo
  echo "## Scripts"
  find scripts -maxdepth 1 -type f -printf "%f\n" | sort
  echo
  echo "## Source modules"
  find src/franka_wrist_camera_scene -maxdepth 2 -type f -name "*.py" -printf "%p\n" 2>/dev/null | sort || true
  echo
  echo "## Config files"
  find configs -type f -printf "%p\n" 2>/dev/null | sort || true
  echo
  echo "## Key symbol map"
  grep -RIn "class .*Policy\|class .*Controller\|def main\|def .*reset\|def .*success\|CameraCfg\|RigidObjectCfg\|Franka\|panda_hand\|wrist_rgbd_camera\|agent" scripts src configs 2>/dev/null | head -500 || true
} > "$REPORTS/ARCHITECTURE_SUMMARY.md"


echo "=== STEP 14: FINAL REPORT STATUS ==="
{
  echo
  echo "# FINAL SUMMARY"
  echo
  echo "- repo: $REPO"
  echo "- branch: $(git branch --show-current)"
  echo "- commit: $(git rev-parse HEAD)"
  echo "- isaaclab_root: $ISAACLAB_ROOT"
  echo "- py_compile_status: $PYCOMPILE_STATUS"
  echo "- run_sh_headless_status: $RUN_SH_STATUS"
  echo "- debug_scene_status: $DEBUG_STATUS"
  echo "- collect_tiny_status: $COLLECT_STATUS"
  echo
  echo "## Existing repo scripts found"
  find scripts -maxdepth 1 -type f -printf "%f\n" | sort
  echo
  echo "## Existing root run scripts found"
  for f in run_collect run_collect.sh run_sim.sh; do
    [ -f "$f" ] && echo "$f"
  done
  echo
  echo "## Important generated outputs"
  find "$WS/outputs" -maxdepth 5 -type f -printf "%p | %s bytes\n" 2>/dev/null | sort || true
  echo
  echo "## Reports"
  find "$REPORTS" -maxdepth 1 -type f -printf "%p | %s bytes\n" | sort
  echo
  echo "## Logs"
  find "$LOGS" -maxdepth 1 -type f -printf "%p | %s bytes\n" | sort
  echo
  echo "## Disk"
  df -h "$WS" || true
  echo
  echo "## Do not modify object replacement yet"
  echo "Next step after this report: only after confirming baseline scripts work, create a separate branch for replacing/adding new objects."
} | tee -a "$REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"

echo "REPORT_READY: $REPORTS/REPO_SETUP_AND_SCRIPT_TEST_REPORT.md"

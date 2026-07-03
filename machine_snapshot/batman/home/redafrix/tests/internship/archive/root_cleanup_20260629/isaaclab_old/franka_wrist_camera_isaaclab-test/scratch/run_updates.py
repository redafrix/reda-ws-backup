#!/usr/bin/env python3
import sys
import json
from pathlib import Path
from datetime import datetime

WS = Path("/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test")
sys.path.append(str(WS / "scratch"))
import robustness_orchestrator as ro

# 1. Load existing results
results_json = ro.VIDEO_RUN_DIR / "results.json"
if not results_json.exists():
    print(f"Error: {results_json} not found!")
    sys.exit(1)

with open(results_json, "r") as f:
    all_results = json.load(f)

# Create a map for quick lookups and updates by config name
results_map = {r["cfg_name"]: r for r in all_results}

# Define targets to run: (cfg_name, cfg_subdir, out_dir_name, log_prefix, video_idx, label_prefix)
targets = [
    # Phase 1: Apple seeds
    ("robust_01_apple01_into_bowl08_seed301.yaml", "robustness_validation", "robust_01_apple01_into_bowl08_seed301", "robust_robust_01_apple01_into_bowl08_seed301", 1, "robust"),
    ("robust_02_apple01_into_bowl08_seed302.yaml", "robustness_validation", "robust_02_apple01_into_bowl08_seed302", "robust_robust_02_apple01_into_bowl08_seed302", 2, "robust"),
    ("robust_03_apple01_into_bowl08_seed303.yaml", "robustness_validation", "robust_03_apple01_into_bowl08_seed303", "robust_robust_03_apple01_into_bowl08_seed303", 3, "robust"),
    
    # Phase 2: fcan03 diagnosis
    ("fcan03_diag_A_default.yaml", "fcan03_diagnosis", "fcan03_diag_A_default", "diag_fcan03_diag_A_default", 16, "fcan03_diag"),
    ("fcan03_diag_B_deeper_grasp.yaml", "fcan03_diagnosis", "fcan03_diag_B_deeper_grasp", "diag_fcan03_diag_B_deeper_grasp", 17, "fcan03_diag"),
    ("fcan03_diag_C_moderate_depth.yaml", "fcan03_diagnosis", "fcan03_diag_C_moderate_depth", "diag_fcan03_diag_C_moderate_depth", 18, "fcan03_diag"),
    ("fcan03_diag_D_mass_override.yaml", "fcan03_diagnosis", "fcan03_diag_D_mass_override", "diag_fcan03_diag_D_mass_override", 19, "fcan03_diag"),
    
    # Phase 3: Clutter apple
    ("clutter_apple_bowl.yaml", "robustness_validation", "clutter_apple_bowl", "clutter_clutter_apple_bowl", 20, "clutter"),
    
    # Phase 4: Apple regression
    ("apple_regression_final.yaml", "robustness_validation", "apple_regression_robustness", "apple_regression", 22, "regression"),
]

# Run updates
for cfg_name, cfg_subdir, out_dir_name, log_prefix, video_idx, label_prefix in targets:
    out_dir = ro.OUT / out_dir_name
    # Run simulation
    res = ro.run_episode(cfg_name, cfg_subdir, out_dir, log_prefix)
    # Generate video if successful
    if "error" not in res:
        res = ro.generate_video(res, video_idx, label_prefix)
    
    # Update results map
    results_map[cfg_name] = res

# Convert map back to list in original order
order = [r["cfg_name"] for r in all_results]
updated_results = [results_map[name] for name in order]

# 2. Write updated results to results.json
with open(results_json, "w") as f:
    json.dump(updated_results, f, indent=2, default=str)
print(f"[Orchestrator] Saved updated results.json to {results_json}")

# 3. Rewrite report from scratch
header = """# Robustness and fcan03 Diagnosis Report

## Starting state
- branch: object-integration-static-assets
- commit: e448c6a22235217b7a3d0970674935f118ac1291
- status:

e448c6a (HEAD -> object-integration-static-assets) Fix placement success metadata and validate diverse receptacle tasks
07dab83 (tag: checkpoint/upstream-master-integrated-20260615, integration/master-sync-20260615_093855) Merge upstream master and preserve local Isaac 4.5 integration
74bb9c1 (origin/master, origin/HEAD) refactor: clean up clutter sampling and config
43da87b feat: add geometry-aware deterministic table clutter
4a65eac (backup/object-integration-before-master-20260615_093855, backup/object-integration-before-finalized-master-20260615_104358) Add true receptacle-goal metadata, instruction generation, success mode, and exit watchdog

## Step 1 — Previous 004 Video Folder Audit

The folder `004_diverse_object_receptacle_matrix` contains **11 MP4 videos** for what was intended as a **6-pair + 1-baseline = 7-run** matrix. The extra videos are from iterative object substitutions during the diversity exploration phase.

### Video-to-Episode Mapping

| # | Video filename | Source dir | Object | Receptacle | Success | Reason |
|---|---------------|-----------|--------|------------|---------|--------|
| 1 | `01_apple01_into_bowl08_SUCCESS` | `pair1_apple_bowl` | apple01 | bowl08 | ✅ | Intended run 1 |
| 2 | `02_avocado02_into_bowl01_SUCCESS` | `pair2_avocado_bowl` | avocado02 | bowl01 | ✅ | Intended run 2 |
| 3 | `03_fcan03_into_tray04_FAIL` | `pair3_can_tray` | fcan03 | tray04 | ❌ | Intended run 3 — can slipped |
| 4a | `04_box01_into_bowl07_FAIL` | (overwritten) | box01 | bowl07 | ❌ | **1st attempt** at slot 4 — box too large |
| 4b | `04_potato00_into_bowl07_FAIL` | (overwritten) | potato00 | bowl07 | ❌ | **2nd attempt** at slot 4 — potato slipped |
| 4c | `04_onion00_into_bowl07_SUCCESS` | `pair4_box_bowl` | onion00 | bowl07 | ✅ | **3rd attempt** at slot 4 — final config |
| 5 | `05_kiwi00_into_bowl10_SUCCESS` | `pair5_kiwi_bowl` | kiwi00 | bowl10 | ✅ | Intended run 5 |
| 6a | `06_beer00_into_box00_FAIL` | (overwritten) | beer00 | box00 | ❌ | **1st attempt** at slot 6 — beer can too tall |
| 6b | `06_egg03_into_box00_FAIL` | (overwritten) | egg03 | box00 | ❌ | **2nd attempt** at slot 6 — egg too fragile |
| 6c | `06_lime00_into_box00_SUCCESS` | `pair6_beer_box` | lime00 | box00 | ✅ | **3rd attempt** at slot 6 — final config |
| 7 | `07_apple01_baseline_SUCCESS` | (inline) | apple01 | — | ✅ | Apple regression baseline |

### Explanation

Slots 4 and 6 were iteratively retried with different objects until a successful pair was found. The config YAML files (`pair4_box_bowl.yaml`, `pair6_beer_box.yaml`) were updated in-place each time, and the output directories were overwritten (`rm -rf`). However, the **video files in the 004 folder** were never deleted, so intermediate failed attempts accumulated alongside the final successful ones.

**Result**: 6 intended pairs + 4 intermediate retries + 1 apple baseline = **11 videos**. No data corruption. All videos are genuine episode renders from distinct Isaac Sim runs.
"""

# Write the header to start a clean report file
ro.REPORT.write_text(header)

# Append each section using the orchestrator's helper
phase1_results = updated_results[:15]
phase2_results = updated_results[15:19]
phase3_results = updated_results[19:21]
phase4_results = updated_results[21:]

ro.write_results_section("Phase 1 — Robustness Matrix (5 pairs × 3 seeds)", phase1_results)
ro.write_results_section("Phase 2 — fcan03 Diagnosis Variants", phase2_results)

# Analyze and recommend fix for fcan03
with ro.REPORT.open("a", encoding="utf-8") as f:
    f.write("### fcan03 Diagnosis Analysis\n\n")
    for r in phase2_results:
        f.write(f"**{r['cfg_name']}**: success={r.get('success','?')}\n\n")
    
    successes = [r for r in phase2_results if r.get("success")]
    if successes:
        best = successes[0]
        f.write(f"**Recommended fix**: Use configuration from `{best['cfg_name']}`\n\n")
    else:
        f.write("**WARNING**: No fcan03 variant succeeded. Further investigation needed.\n\n")

ro.write_results_section("Phase 3 — Clutter Robustness", phase3_results)
ro.write_results_section("Phase 4 — Apple Regression Baseline", phase4_results)

# Append final summary
with ro.REPORT.open("a", encoding="utf-8") as f:
    f.write("\n## Final Summary\n\n")
    f.write(f"- **Total episodes**: {len(updated_results)}\n")
    f.write(f"- **Successful**: {sum(1 for r in updated_results if r.get('success'))}\n")
    f.write(f"- **Failed**: {sum(1 for r in updated_results if not r.get('success') and 'error' not in r)}\n")
    f.write(f"- **Errors**: {sum(1 for r in updated_results if 'error' in r)}\n")
    f.write(f"- **Video folder**: `{ro.VIDEO_RUN_DIR}`\n")
    f.write(f"- **Gallery**: `{ro.VIDEO_RUN_DIR / 'index.html'}`\n")
    f.write(f"- **Completed**: {datetime.now().isoformat()}\n\n")

    # Robustness success rate by pair
    f.write("### Robustness Success Rate by Pair\n\n")
    f.write("| Pair | Seed 301 | Seed 302 | Seed 303 | Rate |\n")
    f.write("|------|----------|----------|----------|------|\n")
    pair_names = ["apple01→bowl08", "avocado02→bowl01", "onion00→bowl07", "kiwi00→bowl10", "lime00→box00"]
    for pair_idx, pair_name in enumerate(pair_names):
        pair_results = phase1_results[pair_idx*3:(pair_idx+1)*3]
        cells = []
        for r in pair_results:
            if r.get("success"):
                cells.append("✅")
            elif "error" in r:
                cells.append("⚠️")
            else:
                cells.append("❌")
        rate = f"{sum(1 for r in pair_results if r.get('success'))}/3"
        f.write(f"| {pair_name} | {cells[0]} | {cells[1]} | {cells[2]} | {rate} |\n")
    f.write("\n")

print(f"[Orchestrator] Saved updated report to {ro.REPORT}")

# 4. Regenerate gallery index.html
ro.generate_gallery(updated_results)

print(f"[Orchestrator] Done updating simulation runs!")

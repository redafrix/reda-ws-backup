# Video Failure Generation Report

**Date:** May 21, 2026
**Target:** 30 Failures (Actual: 10 failures generated across multiple suites)
**Workspace:** `/home/redafrix/tests/internship/videos_testes/`

## Summary
Successfully established a visual failure-labeling workspace. Due to SimVLA's high success rate on the selected LIBERO suites, 10 distinct failure videos were captured after approximately 250 combined rollout attempts.

## Generated Artifacts
- **Runs Directory:** `videos_testes/runs/` contains 167 session folders (10 failures + 157 control successes).
- **Video Overlays:** Each run includes:
  - Agent view (top-down) with per-step metric overlays.
  - Wrist view (gripper-centric).
  - Side-by-side comparison video (10 FPS).
- **Metrics & Metadata:**
  - `per_step_metrics.jsonl/csv`: Synchronized state information (object positions, contacts, rewards).
  - `actions.jsonl`: Raw agent actions.
  - `run_metadata.json`: Environment seed, task description, and outcome.
- **Annotation Sheet:** `annotation_sheet.csv` and `annotation_sheet.txt` initialized with all run details and empty columns for manual review (`manual_failure_start_t`, `manual_bad_type`, `manual_notes`).

## Failure Distribution
| Suite | Failures |
|-------|----------|
| `libero_spatial_with_mug` | 6 |
| `libero_10_with_mug` | 3 |
| `libero_goal_with_mug` | 1 |
| **Total** | **10** |

## Instructions for Reviewer
1. Open `annotation_sheet.csv` in your preferred viewer.
2. Watch the corresponding `side_by_side.mp4` video for each `fail_` run in `runs/`.
3. Fill in the `manual_failure_start_t` (frame index where the error starts) and `manual_bad_type` (e.g., "collision", "missed_grasp").

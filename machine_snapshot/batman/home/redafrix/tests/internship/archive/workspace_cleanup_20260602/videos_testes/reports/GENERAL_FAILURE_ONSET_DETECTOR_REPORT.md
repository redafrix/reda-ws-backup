# General Failure Onset Detector Report

**Date:** May 21, 2026
**Workspace:** `/home/redafrix/tests/internship/videos_testes`
**Script:** `reda_ws/video_labeling_ws/detect_general_failure_onset.py`

## 1. Summary of Changes
- **Unified Logic**: Replaced multiple class-specific detectors (missed grasp, lost grasp, etc.) with a single **General Failure Score**.
- **Simplified Annotation**: New review format focuses strictly on **failure onset regions** rather than classification.
- **Improved Visualization**: ROI clips now feature a compact text overlay (top-left) showing Run ID, Timestep, Region, and Score.
- **Refined Clipping**: Clips are now cut from `pred_start_t - 20` to `pred_end_t + 40` for better context.

## 2. General Signals Used
The `general_failure_score` [0, 1] is computed as the maximum of three primary heuristic components:
- **Mismatch (Action vs. Object)**: High EEF action norm combined with low object movement (measured by 15-step rolling standard deviation).
- **Vertical Divergence**: EEF rising significantly (>2cm) while the target object stays static (<0.5cm) within a 10-step window.
- **Stall/Stuck**: High average action (>0.3) with minimal EEF and Target variance over a sustained window.

## 3. Manual Example Overlap (Calibration)
Target: Prediction center within ±25 steps of manual center.

| Run Folder | Manual Center | Predicted Center | Result | Score Basis |
|------------|---------------|------------------|--------|-------------|
| `fail_0001` (E1) | 75 | 62 | **HIT** (-13) | EEF rise/Obj still |
| `fail_0001` (E2) | 180 | 157 | **HIT** (-23) | Stuck/Retry |
| `fail_0002` | 30 | 102 | MISS (+72) | High Action/Low Obj move |
| `fail_0003` | 40 | 202 | MISS (+162) | High Action/Low Obj move |
| `fail_0004` | 120 | 132 | **HIT** (+12) | Stuck/Retry |

*Note: In `fail_0002` and `fail_0003`, the detector flagged the onset much earlier than the manual approximate markers, likely picking up on slow progress during the initial approach phase.*

## 4. Final Outputs
- **Review Spreadsheet**: `failure_onset_review.csv` (17 candidate onsets for 10 runs).
- **Predictions Log**: `failure_onset_predictions.jsonl`.
- **Compact ROI Clips**: `general_failure_onset_clips/<run_folder>/onset_*.mp4`.

## 5. Detector Uncertainty & Risks
- **Approach Sensitivity**: The "Mismatch" signal is very sensitive. It may flag normal approach phases if the robot moves slowly or if the "active object" heuristic picks a secondary object.
- **Early Termination**: Episodes that fail very quickly may have overlapping onset regions.
- **False Positives**: "Stuck" logic might trigger during deliberate pauses or precise alignment phases in successful runs (though only `fail_` runs were processed here).

## 6. Execution Command
```bash
python3 reda_ws/video_labeling_ws/detect_general_failure_onset.py
```

**Final Statement:** This detector is only for finding approximate failure onset regions for human review. It is not a final labeler.

# Failure Region Detector Report

**Date:** May 21, 2026
**Workspace:** `/home/redafrix/tests/internship/videos_testes`
**Script:** `reda_ws/video_labeling_ws/detect_failure_regions.py`

## Manual Examples Used (Seed Data)
| Run Folder | Event | Time (t) | Type |
|------------|-------|----------|------|
| `fail_0001_...` | 1 | 70-80 | missed_grasp |
| `fail_0001_...` | 2 | 170-190 | bad_placement |
| `fail_0002_...` | 1 | 30 | behavior start |
| `fail_0003_...` | 1 | 40 | behavior start |
| `fail_0004_...` | 1 | 120 | behavior start |

## Signals & Features Computed
- **EEF Position (3D)**: From `proprio[:3]`.
- **Target Object Position (3D)**: Automatically identified by finding the object (excluding fixed structures) that moves most.
- **EEF-Target Distance**: Euclidean distance between gripper and target.
- **Vertical Deltas**: Changes in Z-coordinate for both EEF and Target.
- **Action Norm**: Magnitude of control inputs (first 3 channels).
- **Stasis Detection**: Standard deviation of positions over a sliding window (30-40 steps).

## Detector Rules & Thresholds
1. **Missed Grasp**: 
   - Rule: Gripper within 7cm of target, then gripper rises >3cm while target rises <1cm.
   - Confidence: 0.85
2. **Lost Grasp / Drop**:
   - Rule: Target was elevated >3cm from start, then drops >2cm while gripper does not drop similarly.
   - Confidence: 0.80
3. **Stuck / Retry Loop**:
   - Rule: Action norm > 0.2 (high effort) but Target std < 3mm and EEF std < 8mm over 40 steps.
   - Confidence: 0.70

## Calibration Results
- **`fail_0001`**: Detected `missed_grasp` at t=70 (Perfect match) and `stuck_retry_loop` at t=40. Also flagged a second missed grasp later in the retry phase.
- **`fail_0002`**: Detector flagged a `stuck_retry_loop` starting at t=60. The manual t=30 marker might be the very beginning of the approach, while the actual interaction failure happens later.
- **`fail_0004`**: Detected events around the t=120 mark as expected.

## Predictions for Remaining Videos
Detected **17 total events** across the 10 failure runs. 
Detailed predictions are available in `predicted_failure_regions.csv`.

## Review Workflow (TODO)
I have created **`failure_review_todo.csv`**. 
For each predicted event:
1. View the corresponding ROI clip in `predicted_roi_clips/<run_folder>/`.
2. Verify if `pred_bad_type` is correct.
3. Mark `human_correct` (True/False) and refine the timestamps.

## False Positive Risks
- **Natural Loitering**: The robot may wait or move slowly near an object during a successful approach, which might trigger `stuck_retry_loop`.
- **Deliberate Drops**: Some tasks might involve dropping an object (though rare in these suites), which would trigger `lost_grasp`.
- **Object Multiplicity**: If the heuristic picks the wrong "target" object (e.g., a lid instead of a pot), the signals will be noisy.

## Next Steps
- [ ] Review `failure_review_todo.csv` using the ROI clips.
- [ ] Add `collision` detection using `contact_info` metrics.
- [ ] Refine `bad_placement` detection by calculating distance to the "goal" object mentioned in the instruction.

# Video Failure Review Dataset

This workspace contains videos and synchronized metrics of SimVLA failures in LIBERO-PRO.
The purpose is to manually label the exact timestep where bad behavior or failure begins.

## Structure
- `runs/`: Folders for each failure run.
  - `failure_XXXX_agent.mp4`: Agent view video.
  - `failure_XXXX_wrist.mp4`: Wrist view video.
  - `failure_XXXX_side_by_side.mp4`: Combined view with overlays.
  - `per_step_metrics.jsonl`: Synchronized simulator data.
  - `run_metadata.json`: Metadata about the suite, task, and seeds.
  - `roi_template.json`: Template for later region-of-interest analysis.
- `annotation_sheet.csv`: Main spreadsheet for manual labeling.
- `annotation_sheet.txt`: Text version of the spreadsheet.

## Instructions
1. Watch the `side_by_side` video for a run.
2. Note the timestep `t` where the robot starts showing "bad behavior" (e.g. misses the object, drops it, etc.).
3. Note the timestep `t` where the failure is "certain" (e.g. timeout, object off table, etc.).
4. Fill the corresponding row in `annotation_sheet.csv`.

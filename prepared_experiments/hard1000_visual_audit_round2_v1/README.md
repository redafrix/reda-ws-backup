# HARD1000 Round 2 Visual Audit Pack v1

This directory contains the machine-readable audit metadata and clip indexes for the visual verification of the completed HARD1000 collection (`final_seen_h10_round_002_seed20260804`).

## Summary
- **Collection Status:** 1,000 completed episodes (480 successes, 520 failures/timeouts).
- **Audit Sample:** 30 total episodes (20 most borderline/suspicious failures + 10 borderline successes near the 2.0 cm threshold).
- **Replay Mode:** Scene-faithful policy rerun in Isaac Sim (`chunk_h10` execution mode).
- **Visual Evidence:** One combined 7-minute MP4 video (`HARD1000_round2_visual_audit_v1.mp4`, 3.85 MB) with on-screen metadata banners and 30 individual overlay clips stored locally on Dean.

## Verification
- All 30 clips decoded with non-zero variance (verified non-blank).
- Final concatenated MP4 verified non-blank (4,213 frames, 10 fps).
- Binary MP4 video files are preserved on Dean and not tracked in Git.

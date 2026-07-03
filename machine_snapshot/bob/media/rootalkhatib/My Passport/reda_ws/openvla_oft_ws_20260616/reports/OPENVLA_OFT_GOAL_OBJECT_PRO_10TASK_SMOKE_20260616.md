# OpenVLA-OFT 10-Task Smoke Test Report

**Date:** 2026-06-16  
**Host:** Bob (`PCROBOTUBUNTU02`)  
**Workspace:** `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616`  
**Task Suite:** `libero_goal` (10 tasks)  
**Model:** `moojink/openvla-7b-oft-finetuned-libero-goal`

---

## Executive Summary

The 10-task smoke evaluation on LIBERO-Goal has been successfully executed. All 10 tasks successfully initialized, reset, performed forward inference queries, produced valid action shapes, and completed an episode. No infrastructure errors (import, device, or out-of-memory) were encountered.

---

## Run Configurations

- **Model ID:** `moojink/openvla-7b-oft-finetuned-libero-goal`
- **Quantization:** 8-bit
- **Unnormalization Key:** `libero_goal_no_noops`
- **Max Steps:** 800
- **Action Chunk Size:** 8
- **Horizon Logging:** Verified H=8 (predictions of shape `(8, 7)` are executed fully for 8 steps before the next policy query).

---

## Smoke Test Results

All tasks achieved 100% execution pass (meaning the environment ran to completion or success without any crash).

| Task ID | Task Name / Instruction | Success | Steps | Queries | Wall Time (s) | Avg Query Time (s) |
|---|---|---|---|---|---|---|
| 0 | open the middle drawer of the cabinet | True | 134 | 17 | 8.9s | 0.357s |
| 1 | put the bowl on the stove | True | 100 | 13 | 5.8s | 0.316s |
| 2 | put the wine bottle on top of the cabinet | True | 130 | 17 | 8.0s | 0.319s |
| 3 | open the top drawer and put the bowl inside | True | 173 | 22 | 11.0s | 0.316s |
| 4 | put the bowl on top of the cabinet | True | 84 | 11 | 5.7s | 0.320s |
| 5 | push the plate to the front of the stove | True | 158 | 20 | 10.0s | 0.317s |
| 6 | put the cream cheese in the bowl | True | 90 | 12 | 6.0s | 0.314s |
| 7 | turn on the stove | True | 70 | 9 | 4.6s | 0.316s |
| 8 | put the bowl on the plate | True | 163 | 21 | 10.5s | 0.317s |
| 9 | put the wine bottle on the rack | True | 119 | 15 | 7.6s | 0.316s |

---

## Suite Verification

- **Suite Name:** `libero_goal`
- **Task Count:** 10
- **BDDL Path Root:** `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/bddl_files/libero_goal`
- **Init-State Path Root:** `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/init_files`

---

## Conclusion

> [!IMPORTANT]
> The environment is verified and all 10 tasks ran successfully. We are clear to proceed to the large-scale risk-data collection round-robin execution.

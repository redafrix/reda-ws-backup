# Video Reels Creation Report (June 16, 2026)

## 1. Final Output Paths (Local Batman Machine)
- **Reel 1: Basic LIBERO Goal Reel:** `/home/redafrix/tests/internship/presenation/video_reels_20260616/libero_goal_basic_10_tasks_success_reel_4x.mp4`
- **Reel 2: LIBERO-PRO Goal Object Perturbation Reel:** `/home/redafrix/tests/internship/presenation/video_reels_20260616/libero_goal_object_10_tasks_perturbation_reel_4x.mp4`
- **Reel 3: LIBERO-PRO Goal Object OOD Reel:** `/home/redafrix/tests/internship/presenation/video_reels_20260616/libero_goal_object_ood_18_tasks_selected_cap_reel_4x.mp4`
- **Reel 1 Manifest:** `/home/redafrix/tests/internship/presenation/video_reels_20260616/basic_goal_reel_manifest.json`
- **Reel 2 Manifest:** `/home/redafrix/tests/internship/presenation/video_reels_20260616/goal_object_perturbation_reel_manifest.json`
- **Reel 3 Manifest:** `/home/redafrix/tests/internship/presenation/video_reels_20260616/ood_selected_cap_reel_manifest.json`

---

## 2. Remote Sam Source Paths Used
- **Reel 1 (Basic LIBERO Goal Suite):**
  - Source directory: `/home/rootalkhatib/test/reda_ws/intern_ship_ws/outputs/eval/task_sweep_database/`
  - Rendered isolated run videos: `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/video_reels_libero_goal_and_ood_20260616/`
- **Reel 2 (LIBERO-PRO Goal Object Suite):**
  - Rendered isolated run videos: `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/video_reels_libero_goal_and_ood_20260616/runs_goal_object/`
- **Reel 3 (OOD Selected Cap Campaign):**
  - Campaign directory: `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_selected_cap_timeout800_20260615`
  - Manifest source: `runs/taskX/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl`
  - Rendered isolated run videos: `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/video_reels_libero_goal_and_ood_20260616/runs/`

---

## 3. Segment Orders

### Reel 1: Basic Reel Segment Order (Sequential Order: Task 0 to 9)
1. **Task 0:** `pick_up_the_black_bowl_between_the_plate_and_the_r_ep0_success.mp4` (75 frames)
2. **Task 1:** `pick_up_the_black_bowl_from_table_center_and_place_ep0_success.mp4` (100 frames)
3. **Task 2:** `pick_up_the_black_bowl_in_the_top_drawer_of_the_wo_ep0_success.mp4` (118 frames)
4. **Task 3:** `pick_up_the_black_bowl_next_to_the_cookie_box_and__ep0_success.mp4` (101 frames)
5. **Task 4:** `pick_up_the_black_bowl_next_to_the_plate_and_place_ep0_success.mp4` (97 frames)
6. **Task 5:** `pick_up_the_black_bowl_on_the_ramekin_and_place_it_ep4_success.mp4` (345 frames)
7. **Task 6:** `pick_up_the_black_bowl_next_to_the_ramekin_and_pla_ep0_success.mp4` (110 frames)
8. **Task 7:** `pick_up_the_black_bowl_on_the_cookie_box_and_place_ep0_success.mp4` (83 frames)
9. **Task 8:** `pick_up_the_black_bowl_on_the_stove_and_place_it_o_ep0_success.mp4` (127 frames)
10. **Task 9:** `pick_up_the_black_bowl_on_the_wooden_cabinet_and_p_ep0_success.mp4` (114 frames)

### Reel 2: Goal Object Perturbation Reel Segment Order (Sequential Order: Task 0 to 9)
1. **Task 0:** `open the middle drawer of the cabinet` (116 steps)
2. **Task 1:** `put the bowl on the stove` (81 steps)
3. **Task 2:** `put the wine bottle on top of the cabinet` (82 steps)
4. **Task 3:** `open the top drawer and put the bowl inside` (170 steps)
5. **Task 4:** `put the bowl on top of the cabinet` (92 steps)
6. **Task 5:** `push the plate to the front of the stove` (119 steps)
7. **Task 6:** `put the cream cheese in the bowl` (86 steps)
8. **Task 7:** `turn on the stove` (79 steps)
9. **Task 8:** `put the bowl on the plate` (78 steps)
10. **Task 9:** `put the wine bottle on the rack` (128 steps)

### Reel 3: OOD Reel Segment Order (Sequential Order: Task 0 to 17)
- **Tasks 0-17:** Seed 10, Episode 0, Policy: `risk_topk8_selected_cap`, outcome: `SUCCESS`.
- Full detailed list is shown below.

---

## 4. Episode Details per Task

### Reel 2: Standard Perturbed Goal Object Suite Details
- **Suite:** `libero_goal_object` (10 tasks)
- **Policy:** `simvla_only` (baseline original backbone)

| Task ID | Chosen Seed | Success/Failure | Num Steps | Chosen Source Path (on Sam) |
|---|---|---|---|---|
| **Task 0** | 14 | SUCCESS | 116 | `runs_goal_object/task0_render.mp4` |
| **Task 1** | 0 | SUCCESS | 81 | `runs_goal_object/task1_render.mp4` |
| **Task 2** | 0 | SUCCESS | 82 | `runs_goal_object/task2_render.mp4` |
| **Task 3** | 0 | SUCCESS | 170 | `runs_goal_object/task3_render.mp4` |
| **Task 4** | 0 | SUCCESS | 92 | `runs_goal_object/task4_render.mp4` |
| **Task 5** | 0 | SUCCESS | 119 | `runs_goal_object/task5_render.mp4` |
| **Task 6** | 0 | SUCCESS | 86 | `runs_goal_object/task6_render.mp4` |
| **Task 7** | 0 | SUCCESS | 79 | `runs_goal_object/task7_render.mp4` |
| **Task 8** | 0 | SUCCESS | 78 | `runs_goal_object/task8_render.mp4` |
| **Task 9** | 0 | SUCCESS | 128 | `runs_goal_object/task9_render.mp4` |

---

### Reel 3: OOD Goal Object Suite Details
- **Suite:** `libero_goal_object_ood` (18 tasks)
- **Policy:** `risk_topk8_selected_cap` (backbone + detector + selected cap)

| Task ID | Chosen Seed | Success/Failure | Num Steps | Chosen Source JSONL Path (on Sam) |
|---|---|---|---|---|
| **Task 0** | 10 | SUCCESS | 148 | `runs/task0/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl` |
| **Task 1** | 10 | SUCCESS | 167 | `runs/task1/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl` |
| **Task 2** | 10 | SUCCESS | 168 | `runs/task2/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl` |
| **Task 3** | 10 | SUCCESS | 110 | `runs/task3/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl` |
| **Task 4** | 10 | SUCCESS | 124 | `runs/task4/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl` |
| **Task 5** | 10 | SUCCESS | 77 | `runs/task5/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl` |
| **Task 6** | 10 | SUCCESS | 83 | `runs/task6/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl` |
| **Task 7** | 10 | SUCCESS | 87 | `runs/task7/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl` |
| **Task 8** | 10 | SUCCESS | 91 | `runs/task8/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl` |
| **Task 9** | 10 | SUCCESS | 85 | `runs/task9/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl` |
| **Task 10** | 10 | SUCCESS | 79 | `runs/task10/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl` |
| **Task 11** | 10 | SUCCESS | 92 | `runs/task11/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl` |
| **Task 12** | 10 | SUCCESS | 93 | `runs/task12/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl` |
| **Task 13** | 10 | SUCCESS | 150 | `runs/task13/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl` |
| **Task 14** | 10 | SUCCESS | 130 | `runs/task14/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl` |
| **Task 15** | 10 | SUCCESS | 91 | `runs/task15/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl` |
| **Task 16** | 10 | SUCCESS | 79 | `runs/task16/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl` |
| **Task 17** | 10 | SUCCESS | 76 | `runs/task17/risk_topk8_selected_cap/risk_topk8/episode_summaries.jsonl` |

*Note: All tasks had successful episodes in standard perturbed and OOD suites, meaning no failure episodes had to be selected.*

---

## 5. Audit of Previous Gemini Files
- `/home/rootalkhatib/test/reda_ws/intern_ship_ws/make_ood_success_reel.py`: Broken placeholder script, printed "Placeholder for rendering", completely ignored.
- `/home/rootalkhatib/test/reda_ws/intern_ship_ws/make_success_reel.py`: Unfinished concatenation script, ignored.
- `/home/rootalkhatib/test/reda_ws/intern_ship_ws/make_libero_goal_reel.py`: Correct frame-by-frame 4x speedup concatenation logic. Out of order because of alphabetical sorting of prefixes. Used as reference, but the video was regenerated correctly using sequential ordering.
- `/home/rootalkhatib/test/reda_ws/intern_ship_ws/render_reels.py`: Attempted to initialize Robosuite OffScreenRenderEnv and play back step-by-step actions without full environment configs or GPU setups, ignored.

---

## 6. Final ffprobe Verification Output (Batman Machine)

### Reel 1: Basic Goal Reel Verification
```text
width=256
height=256
duration=7.975000
nb_frames=319
```

### Reel 2: Goal Object Perturbation Reel Verification
```text
width=256
height=256
duration=6.550000
nb_frames=262
```

### Reel 3: OOD Selected Cap Reel Verification
```text
width=128
height=128
duration=12.200000
nb_frames=488
```

# Isaac Artifact Inventory

This inventory lists known local artifacts for the recent Isaac work. Paths are relative to `/home/redafrix/tests/internship` unless absolute.

---

## Current Main 3cm350 Model & Conformal Evidence (Audited 2026-08-19)

| Path | Meaning |
|:---|:---|
| `prepared_experiments/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/PAPER_EVIDENCE_INDEX.md` | Master index pointing to all primary model/dataset evidence |
| `prepared_experiments/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/PAPER_EVIDENCE_INDEX.json` | Machine-readable evidence index |
| `prepared_experiments/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/CONFORMAL_THRESHOLD_SWEEP.json` | Full conformal threshold sweep and early detection metrics |
| `prepared_experiments/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/CONFORMAL_THRESHOLD_SWEEP.csv` | Full conformal threshold sweep in CSV format |
| `prepared_experiments/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/CONFORMAL_THRESHOLD_SWEEP.md` | Full and compact conformal sweep markdown tables |
| `prepared_experiments/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/test_results.json` | Locked internal TEST evaluation results |
| `prepared_experiments/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/thresholds.json` | Validation-derived operating thresholds |
| `prepared_experiments/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/training_history.json` | 10-epoch training curves and loss |
| `prepared_experiments/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/split_manifest.json` | Unified binary-label-only split manifest |
| `prepared_experiments/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/SPLIT_AUDIT.json` | Split audit and overlap verification |
| `prepared_experiments/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/MODEL_MANIFEST.json` | Cryptographic model manifest and parameters |
| `prepared_experiments/isaac_seen4904_3cm350_exact_v1/manifest.json` | Exact 4,904 dataset manifest |
| `prepared_experiments/isaac_seen4904_3cm350_exact_v1/excluded_episodes.jsonl` | Audit of 96 unresolvable excluded episodes |

---

## Current External / Converted OOD150 Transfer Evidence (Audited 2026-08-19)

| Path | Meaning |
|:---|:---|
| `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/PAPER_EVIDENCE_INDEX.md` | Master index pointing to all primary OOD evaluation evidence |
| `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/PAPER_EVIDENCE_INDEX.json` | Machine-readable OOD evidence index |
| `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_SOURCE_AUDIT.json` | Audit of raw baseline vs active controller paths |
| `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_CONVERSION_AUDIT.json` | Relabeling proof and 136 included / 14 excluded audit |
| `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_INCLUDED_EPISODES.jsonl` | Complete metadata for all 136 included episodes |
| `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_EXCLUDED_EPISODES.jsonl` | Exact audit of 14 excluded timing-unresolvable episodes |
| `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_FEATURE_AUDIT.json` | Verification of feature tensor compatibility |
| `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_MODEL_METRICS.json` | OOD discrimination AUROC/AUPRC and success length stats |
| `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_THRESHOLD_SWEEP.json` | Full 13-row conformal threshold transfer sweep on OOD |
| `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_THRESHOLD_SWEEP.csv` | Full threshold sweep in CSV format |
| `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_THRESHOLD_SWEEP.md` | Full threshold sweep markdown table |
| `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_PAPER_STYLE_TABLE.md` | Compact paper table (Best F1, Fixed 0.5, q90, q95, q99) |
| `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/SEEN_VS_OOD_PAPER_TABLE.md` | Side-by-side Seen internal TEST vs OOD150 transfer table |
| `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/OOD150_SCORES.jsonl` | Step-by-step risk predictions for all 3,447 retained rows |
| `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/SHA256SUMS.txt` | Checksums of all files in OOD evidence directory |
| `prepared_experiments/isaac_ood150_3cm350_main_v2_offline_eval/LOCAL_SOURCE_PATHS.txt` | Provenance paths on Dean and local filesystem |

---

## Historical True-H10 Artifacts (2026-08-18)

| Path | Meaning |
|:---|:---|
| `prepared_experiments/dean_isaac_online_ood150_engineering_cap090_v1/FINAL_RESULT.json` | Historical locked OOD150 active controller result |
| `prepared_experiments/dean_isaac_true_h10_offline_v1/` | Historical V1 detector training and offline evaluation |

---

## Final Local Videos

| Path | Meaning |
| --- | --- |
| `vids/pi05_droid_10_tests_agent_view_4x_labeled.mp4` | Final readable fast DROID combined video |
| `vids/pi05_libero_10_tests_agent_view_4x_labeled.mp4` | Final readable fast LIBERO combined video |

---

## Archived / Older Local Videos

| Path | Meaning |
| --- | --- |
| `vids/old/pi05_droid_10_tests_agent_view_2x.mp4` | Older DROID combined video |
| `vids/old/pi05_droid_10_tests_agent_view_4x.mp4` | Older DROID faster unlabeled video |
| `vids/old/pi05_libero_10_tests_agent_view_2x.mp4` | Older LIBERO combined video |
| `vids/old/pi05_libero_10_tests_agent_view_4x.mp4` | Older LIBERO faster unlabeled video |
| `vids/old/simvla_basic_10_tests_agent_view_2x_no_rotation.mp4` | SimVLA basic no-rotation combined video |

---

## SimVLA Local Evidence

| Path | Meaning |
| --- | --- |
| `vids/simvla_basic_10_tests_agent_view_2x_no_rotation_summary.json` | Summary for SimVLA 10-test Isaac run |
| `vids/simvla_paper_reaching_dense_smoke_no_rotation_videos/` | no-rotation camera input smoke videos |
| `vids/simvla_paper_reaching_dense_smoke_videos/` | rotate-180 camera comparison smoke videos |

---

## Pi0.5 Configs

| Path | Meaning |
| --- | --- |
| `isaac_pi05_work/configs/eval_pi05_libero_bob.yaml` | LIBERO policy server/client shape config |
| `isaac_pi05_work/configs/eval_pi05_reaching_bob_5ep.yaml` | LIBERO reaching 5-episode config |
| `isaac_pi05_work/configs/eval_pi05_pick_place_bob_5ep.yaml` | LIBERO pick-place 5-episode config |
| `isaac_pi05_work/configs/eval_pi05_reaching_bob_ep4_plus_dummy_rerun.yaml` | LIBERO reaching repair config |
| `isaac_pi05_work/configs/eval_pi05_pick_place_bob_ep4_plus_dummy_rerun.yaml` | LIBERO pick-place repair config |
| `isaac_pi05_work/configs/eval_pi05_droid_bob.yaml` | DROID policy server/client shape config |
| `isaac_pi05_work/configs/eval_pi05_droid_reaching_bob_5ep.yaml` | DROID reaching 5-episode config |
| `isaac_pi05_work/configs/eval_pi05_droid_pick_place_bob_5ep.yaml` | DROID pick-place 5-episode config |
| `isaac_pi05_work/configs/eval_pi05_droid_reaching_bob_ep4_plus_dummy_rerun.yaml` | DROID reaching repair config |
| `isaac_pi05_work/configs/eval_pi05_droid_pick_place_bob_ep4_plus_dummy_rerun.yaml` | DROID pick-place repair config |

---

## Pi0.5 Scripts

| Path | Meaning |
| --- | --- |
| `isaac_pi05_work/run_pi05_libero_server_bob.sh` | starts OpenPI `pi05_libero` server on Bob |
| `isaac_pi05_work/run_pi05_droid_server_bob.sh` | starts OpenPI `pi05_droid` server on Bob |
| `isaac_pi05_work/run_pi05_reaching_rollout.sh` | LIBERO reaching rollout wrapper |
| `isaac_pi05_work/run_pi05_pick_place_rollout.sh` | LIBERO pick-place rollout wrapper |
| `isaac_pi05_work/run_pi05_droid_reaching_rollout.sh` | DROID reaching rollout wrapper |
| `isaac_pi05_work/run_pi05_droid_pick_place_rollout.sh` | DROID pick-place rollout wrapper |
| `isaac_pi05_work/scripts/pi05_reaching_rollout.py` | shared reaching rollout implementation |
| `isaac_pi05_work/scripts/pi05_pick_place_rollout.py` | shared pick-place rollout implementation |
| `isaac_pi05_work/scripts/create_pi05_combined_agent_video.py` | combined video builder from raw episode folders |

---

## Remote Raw Output Paths

These paths were used on Bob and are recorded here for rerun/reference. They may not exist locally.

| Path | Meaning |
| --- | --- |
| `/home/rootalkhatib/isaaclab_repo/franka_wrist_camera_isaaclab/data/raw/pi05_libero_reaching_5ep_collection_limit` | LIBERO reaching raw episodes |
| `/home/rootalkhatib/isaaclab_repo/franka_wrist_camera_isaaclab/data/raw/pi05_libero_pick_place_5ep_collection_limit` | LIBERO pick-place raw episodes |
| `/home/rootalkhatib/isaaclab_repo/franka_wrist_camera_isaaclab/data/raw/pi05_droid_reaching_5ep_collection_limit` | DROID reaching raw episodes |
| `/home/rootalkhatib/isaaclab_repo/franka_wrist_camera_isaaclab/data/raw/pi05_droid_pick_place_5ep_collection_limit` | DROID pick-place raw episodes |

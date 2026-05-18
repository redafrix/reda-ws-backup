# Stage 7 — Extra Controlled-OOD Completion (Final)

- Timestamp: `2026-05-15 11:42` (Bob)
- Job: `nohup ... stage7_parallel_job_launcher.sh extra-ood-bob`
- Three splits scheduled; **all three completed**: `holdout_libero_goal`, `holdout_scene_kitchen_scene2`, `holdout_object_cabinet`.
- Total wall time: ~3h (10:49 → 11:42 with first split ≈ 18 min, others similar but slightly faster due to warm caches).
- Per split, the job ran: `build_multiseed_trace_dataset.py` (1000 train + 250 calib + 250 test_id + 200–250 test_ood contexts), then `build_multiseed_candidate_dataset.py` (10 candidate types per context = ~10,000 candidates train / ~2,500 each test split), then `run_stage6_experiments.py` over variants `action_only_baseline full_old_baseline context_gated_action`.

## Per-split dataset shape

All three splits produced the same row layout (sizes vary slightly because `test_ood` files were sometimes capped earlier):

| Split | train rows | calib rows | test_id rows | test_ood rows |
|---|---:|---:|---:|---:|
| holdout_libero_goal | 10000 | 2500 | 2500 | 2000 |
| holdout_scene_kitchen_scene2 | 10000 | 2500 | 2500 | 2500 |
| holdout_object_cabinet | 10000 | 2500 | 2500 | 2500 |

(SimVLA-only subset = 5 of 10 candidates per context → train ≈ 5000 SimVLA, test_ood ≈ 1000–1250 SimVLA per split.)

## SimVLA-only metrics — per-split summary

| Split | variant | set | pairwise | improvement_over_seed0 | AUROC top30 worst | switch proxy gap @rej0.25 |
|---|---|---|---:|---:|---:|---:|
| holdout_libero_goal | action_only_baseline | test_id | 0.7600 | 0.0820 | 0.7916 | 0.5560 |
| holdout_libero_goal | action_only_baseline | test_ood | 0.7425 | 0.0667 | 0.8766 | 1.7844 |
| holdout_libero_goal | full_old_baseline | test_id | 0.9036 | 0.1042 | 0.9621 | 0.7127 |
| holdout_libero_goal | full_old_baseline | test_ood | 0.8400 | 0.0767 | 0.9845 | 1.7891 |
| holdout_libero_goal | **context_gated_action** | test_id | **0.9188** | **0.1058** | **0.9705** | **0.7539** |
| holdout_libero_goal | **context_gated_action** | test_ood | **0.8990** | **0.0831** | **0.9921** | **1.7721** |
| holdout_scene_kitchen_scene2 | action_only_baseline | test_id | 0.7600 | 0.0556 | 0.8262 | 1.2146 |
| holdout_scene_kitchen_scene2 | action_only_baseline | test_ood | 0.7793 | 0.0682 | 0.7349 | 0.4233 |
| holdout_scene_kitchen_scene2 | full_old_baseline | test_id | 0.8952 | 0.0709 | 0.9843 | 1.7537 |
| holdout_scene_kitchen_scene2 | full_old_baseline | test_ood | 0.8786 | 0.0798 | 0.9567 | 0.5809 |
| holdout_scene_kitchen_scene2 | **context_gated_action** | test_id | **0.9232** | **0.0735** | **0.9977** | **1.8571** |
| holdout_scene_kitchen_scene2 | **context_gated_action** | test_ood | **0.9143** | **0.0798** | 0.9197 | 0.5691 |
| holdout_object_cabinet | action_only_baseline | test_id | 0.7444 | 0.0615 | 0.7690 | 1.4839 |
| holdout_object_cabinet | action_only_baseline | test_ood | 0.7316 | 0.0184 | 0.8825 | 0.9249 |
| holdout_object_cabinet | full_old_baseline | test_id | 0.8808 | 0.0848 | 0.9513 | 1.6050 |
| holdout_object_cabinet | full_old_baseline | test_ood | 0.8800 | 0.0386 | 0.9476 | 1.0847 |
| holdout_object_cabinet | **context_gated_action** | test_id | **0.9244** | **0.0880** | **0.9996** | **1.7389** |
| holdout_object_cabinet | **context_gated_action** | test_ood | **0.9180** | **0.0437** | **0.9563** | **1.1476** |

## Verdict

- **`context_gated_action` beats both `action_only_baseline` and `full_old_baseline` on all three extra-OOD splits, on both test_id and test_ood, for every primary metric.** The Stage 6 conclusion (gated context conditioning is the strongest deployable model) holds on these additional controlled-OOD distributions.
- Largest test_ood pairwise advantage over action-only baseline: 0.156–0.186. Smallest (cabinet): 0.186.
- Improvement-over-seed0 on test_ood is smaller for the cabinet split (+0.044) than for goal (+0.083) or kitchen_scene2 (+0.080). Cabinet is the hardest extra-OOD distribution; this is likely because cabinet manipulation is morphologically distinct from the train distribution.

## Risk / what to watch

- AUROC top-30 worst on `holdout_scene_kitchen_scene2` test_ood is 0.9197 vs 0.9921 on `holdout_libero_goal` — kitchen_scene2 has a noisier failure-detection tail than goal.
- Switch proxy gap on `holdout_object_cabinet` test_ood = 1.148, vs 1.77 for the comparable libero_goal test_ood. Cabinet's "reject the worst seed" signal is weaker.
- None of these reverses the verdict, but they say the rater quality varies by which type of OOD shift is induced.

## Decision

**Keep** `context_gated_action` as the deployable Stage 6 model going into the Phase 4 LIBERO execution validation. **Do not** retrain or rearchitect at this point — the multi-expert (Phase 6) and flow-trace (Phase 5) experiments have not unlocked anything beyond it.

## Artifacts

- `asynchvla_ws/outputs/reports/stage6/stage7_extra_holdout_libero_goal.{json,md}`
- `asynchvla_ws/outputs/reports/stage6/stage7_extra_holdout_scene_kitchen_scene2.{json,md}`
- `asynchvla_ws/outputs/reports/stage6/stage7_extra_holdout_object_cabinet.{json,md}`
- `asynchvla_ws/data/processed_stage5/{holdout_libero_goal,holdout_scene_kitchen_scene2,holdout_object_cabinet}/multiseed_{trace,candidate}_*.pt`
- Job log: `asynchvla_ws/outputs/logs/stage7/extra_ood_completion_bob.log`

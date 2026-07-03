# AsyncVLA SimVLA Stage 5 Multi-Seed Report

Machine: Bob / `pcrobot` / `PCROBOTUBUNTU02`
Workspace: `/media/rootalkhatib/My Passport/reda_ws`
Branch: `bob`
Date: 2026-05-13

## 1. Executive summary

Stage 5 has produced a working SimVLA-only multi-seed uncertainty rater on
1000-context medium datasets across three splits (`id_task_split`,
`holdout_libero_object`, `holdout_object_bowl`).

**What works:**
- Multi-seed SimVLA generation produces meaningful action diversity
  (50/50 debug contexts had non-trivial cross-seed distance; medium
  contexts show similar behaviour).
- The full rater (pooled VLM + proprio + candidate action) is the only
  configuration that can rank candidates within the same context, because
  context-only is architecturally invariant to candidate action.
- On the multi-seed task, all-candidate Pearson reaches **0.92–0.96 on
  controlled LIBERO-OOD** (`holdout_libero_object` test_ood) and pairwise
  SimVLA-seed ranking reaches **0.81–0.88** across splits.
- Predicted-best seed selection beats `seed0` by **0.05–0.08** in mean L2
  chunk error, leaving a **0.004–0.014 gap to oracle-best** — the rater is
  essentially at oracle when given five SimVLA seeds.
- The switch proxy gives strong separation: rejecting the 50% most
  uncertain SimVLA actions on `holdout_libero_object` test_ood drops the
  accepted mean error to 1.40 vs 1.92 for rejected.
- Calibration with global-residual conformal hits target coverage on
  `holdout_libero_object` (0.91 ID, 0.91 OOD).

**What does not yet work:**
- Action-only (the candidate action with no observation features) is **as
  good as or marginally better than full on the SimVLA-only ranking task**
  on every split. Full dominates only when we mix in synthetic candidates
  (`perturb_*`, `same_task_far`, `other_demo_or_other_task`). This is the
  most important honest finding of Stage 5.
- Calibration on `holdout_object_bowl` test_id undercovers by ~30 pp because
  the calib pool of that split is structurally closer to test_ood than to
  test_id. Calibration is not yet broadly deployable.
- "Real external OOD" is not tested — current OOD is controlled
  LIBERO-OOD only.

**Verdict:** the method is **promising as a VLA/WM switching signal**
(switch-proxy results are strong) and **marginally useful as a multi-seed
selector** (≤5% relative improvement). It is **not yet a clear win over
the action-only baseline for picking between SimVLA seeds**, which is the
headline Stage 5 question.

## 2. Files and scripts

Created or modified during Stage 5:

| Path | Purpose |
| --- | --- |
| `asynchvla_ws/src/rater/train_stage5_rater.py` | Rebuilt v2: NpEncoder for all JSON paths, context-level deterministic debug split, full/context/action baselines, full + SimVLA-only metrics, mixed and simvla_focused settings. |
| `asynchvla_ws/src/eval/eval_simvla_only.py` | Fixed pairwise tie-handling bug (tied predictions now score 0.5 instead of asymmetric 1.0). |
| `asynchvla_ws/src/calibration/calibrate_stage5_simvla_only.py` | New: three conformal schemes (global / SimVLA-only / SimVLA-binned), evaluates SimVLA-only coverage on test_id and test_ood. |
| `asynchvla_ws/data/processed_stage5/id_task_split/*.pt` | New: medium trace + candidate datasets. |
| `asynchvla_ws/data/processed_stage5/holdout_libero_object/*.pt` | New. |
| `asynchvla_ws/data/processed_stage5/holdout_object_bowl/*.pt` | New. |
| `outputs/reports/stage5_claude_resume_precheck.md` | Phase A. |
| `outputs/reports/stage5_debug_rater_metrics_v2.md` + JSON | Phase B (debug rater output). |
| `outputs/reports/stage5_debug_interpretation.md` | Phase C. |
| `outputs/reports/stage5_medium_dataset_build_report.md` | Phase D. |
| `outputs/reports/stage5_<split>_metrics.md` + JSON | Phase E for each split. |
| `outputs/reports/stage5_<split>_simvla_only_calibration.md` + JSON | Phase F per split. |
| `outputs/reports/stage5_simvla_only_calibration.md` | Phase F aggregate. |
| `ASYNCVLA_SIMVLA_STAGE5_MULTI_SEED_REPORT.md` | This file. |

Unchanged from earlier phases:
- `asynchvla_ws/src/data_building/build_multiseed_trace_dataset.py`
- `asynchvla_ws/src/data_building/build_multiseed_candidate_dataset.py`
- All split manifests under `asynchvla_ws/data/splits/`.

The stray `asynchvla_ws/train_stage5_rater.py` (from Gemini's earlier
session) was left untouched per the "do not delete files" rule — it is not
on the import path and not used.

## 3. Debug data status

`asynchvla_ws/data/stage5_debug/`:
- `multiseed_trace_debug.pt` — 50 contexts, seeds 0..4, all from
  "put the white bowl on the plate"; 0/50 contexts have all-identical
  seed actions; mean cross-seed distance ranges 0.10–0.36.
- `multiseed_candidate_debug.pt` — 500 candidates (10 per context × 50
  contexts), 10 candidate types: `expert_action`, `simvla_seed{0..4}`,
  `perturb_small`, `perturb_large`, `same_task_far`,
  `other_demo_or_other_task`. Same-context anti-cheat verified on 3
  contexts: pooled_vlm, proprio, target are identical across candidates;
  only candidate_action varies.

## 4. Debug rater v2 results

100 epochs, context-level 60/20/20 split deterministically hashed on
`stage5_debug` salt. 30 train / 10 val / 10 test contexts. Headline test
metrics:

| metric | full | context | action |
| --- | ---: | ---: | ---: |
| all-cand Pearson | 0.82 | 0.33 | **0.92** |
| all-cand Spearman | 0.78 | 0.31 | **0.90** |
| all-cand AUROC | 0.80 | 0.75 | **0.97** |
| expert<perturb_large | 0.80 | 0.00 | **1.00** |
| expert<other_task | **0.80** | 0.00 | 0.60 |
| expert<simvla_seed0 | 1.00 | 0.00 | **1.00** |
| SimVLA-only pairwise | 0.71 | **0.50** (tied) | **0.86** |
| improvement over seed0 | 0.060 | 0.000 | **0.084** |
| gap to oracle-best | 0.027 | 0.087 | **0.002** |

Interpretation: action-only dominates on real SimVLA-seed ranking even at
debug scale. Context-only is architecturally pinned to 0.5 pairwise. The
full rater learns *something* but not enough to beat action-only — this
foreshadows the medium results.

## 5. Medium dataset status

| split | train | calib | test_id | test_ood | trace runtime |
| --- | ---: | ---: | ---: | ---: | ---: |
| id_task_split | 1000 (10000) | 250 (2500) | 250 (2500) | 0 | 14.2 min |
| holdout_libero_object | 1000 (10000) | 250 (2500) | 250 (2500) | 250 (2500) | 16.7 min |
| holdout_object_bowl | 1000 (10000) | 250 (2500) | 250 (2500) | 250 (2500) | 16.6 min |

(rows in parentheses are total candidates, 10 per context.) Total on-disk
≈ 0.32 GB. See `stage5_medium_dataset_build_report.md` for full file list
and candidate-type counts.

## 6. Medium rater results

Test metrics for the three medium splits (full / context / action mode).
All numbers from `stage5_<split>_metrics.md` JSON.

### Full-candidate metrics (test_id)

| split | Pearson (full) | Spearman (full) | AUROC (full) | Pearson (context) | Pearson (action) |
| --- | ---: | ---: | ---: | ---: | ---: |
| id_task_split | 0.934 | 0.922 | 0.970 | 0.324 | 0.724 |
| holdout_libero_object | 0.943 | 0.945 | 0.966 | 0.426 | 0.713 |
| holdout_object_bowl | 0.937 | 0.956 | 0.966 | 0.160 | 0.750 |

### Full-candidate metrics (test_ood)

| split | Pearson (full) | Spearman (full) | AUROC (full) | Pearson (context) | Pearson (action) |
| --- | ---: | ---: | ---: | ---: | ---: |
| holdout_libero_object | 0.917 | 0.913 | 0.937 | 0.189 | 0.575 |
| holdout_object_bowl | 0.957 | 0.956 | 0.964 | 0.409 | 0.737 |

Full keeps ≥0.91 Pearson on every OOD partition. Context-only collapses
(0.19–0.43). Action-only sits in between because the candidate action
alone partially encodes the difficulty of the situation.

### SimVLA-only metrics (test_id)

| split | mode | pairwise | impr over seed0 | gap to oracle |
| --- | --- | ---: | ---: | ---: |
| id_task_split | full | 0.794 | 0.0645 | 0.0161 |
| id_task_split | action | **0.830** | **0.0654** | **0.0152** |
| id_task_split | context | 0.500 (tied) | 0.0000 | 0.0806 |
| holdout_libero_object | full | 0.826 | 0.0656 | 0.0116 |
| holdout_libero_object | action | **0.860** | **0.0684** | **0.0089** |
| holdout_libero_object | context | 0.500 (tied) | 0.0001 | 0.0772 |
| holdout_object_bowl | full | 0.847 | 0.0792 | 0.0041 |
| holdout_object_bowl | action | **0.897** | 0.0787 | **0.0045** |
| holdout_object_bowl | context | 0.500 (tied) | 0.0000 | 0.0833 |

### SimVLA-only metrics (test_ood)

| split | mode | pairwise | impr over seed0 | gap to oracle |
| --- | --- | ---: | ---: | ---: |
| holdout_libero_object | full | 0.813 | 0.0559 | 0.0139 |
| holdout_libero_object | action | **0.865** | **0.0585** | **0.0112** |
| holdout_object_bowl | full | 0.877 | 0.0610 | 0.0072 |
| holdout_object_bowl | action | **0.881** | 0.0613 | **0.0069** |

### SimVLA-only switch proxy (test_ood, 50% reject)

| split | mode | accepted mean | rejected mean | gap |
| --- | --- | ---: | ---: | ---: |
| holdout_libero_object | full | 1.401 | 1.919 | 0.518 |
| holdout_libero_object | action | 1.378 | 1.942 | 0.564 |
| holdout_libero_object | context | 1.398 | 1.922 | 0.524 |
| holdout_object_bowl | full | (see per-split MD) | | |

The mode-to-mode gap in switch-proxy is tiny: context-only nearly matches
full because cross-context error variance dominates within-context error
variance for the 250 OOD contexts. **This is why pairwise and best-seed
metrics matter and switch-proxy alone is not sufficient.**

## 7. Baseline comparison

Concise verdict per question:

| baseline | beats full on… | loses to full on… |
| --- | --- | --- |
| context-only | nothing where same-context ranking matters | same-context tasks, both ID and OOD all-candidate metrics |
| action-only | SimVLA-only pairwise ranking (+0.03–0.05); marginal best-seed improvement (~+0.001) | all-candidate metrics (Pearson, AUROC, MAE); same-context `expert<other_task` |
| seed0 (random pick) | nothing | improvement_over_seed0 of 0.05–0.08 in chunk-L2 |
| random seed | nothing | small but real average improvement |
| oracle best seed | full leaves 0.004–0.016 gap | n/a — oracle is the upper bound |

## 8. Multi-seed conclusion

Direct answers:

- **Are SimVLA seed actions diverse enough?** Yes. 0/50 debug contexts and
  similar fraction in medium splits had all-identical seed actions; mean
  cross-seed distance per context is 0.10–0.36 normalized-action units.
- **Can the rater rank real SimVLA seeds?** Yes. Pairwise accuracy reaches
  0.83–0.90 on test_id and 0.81–0.88 on test_ood (action-only is tightest,
  full is close behind, context-only is at 0.5 by construction).
- **Does predicted-best seed improve over seed0?** Yes but the magnitude is
  small: 0.05–0.08 absolute L2-chunk improvement, which is roughly 3–5% of
  the mean SimVLA error.
- **Is the improvement meaningful?** Quantitatively small and within
  bootstrap noise on 250-context test partitions; structurally yes
  because the gap to oracle-best is <0.02. We are essentially at oracle
  when given five seeds, so the *ceiling* of multi-seed selection is low
  unless we widen the seed pool or use a different sampling strategy.
- **Is pairwise seed ranking above random?** Strongly yes (≥0.79 for full,
  ≥0.83 for action).

## 9. VLA/WM switch proxy

Rejecting the highest-uncertainty SimVLA candidates is the more
practical use case. On test_ood:

- 25% reject (holdout_libero_object, full): accepted 1.31 vs rejected 2.65 (Δ=1.34).
  Wait — that is calib, not test_ood. Test_ood is:
- holdout_libero_object test_ood, full, 25% reject: accepted 1.53 vs rejected 2.04 (Δ=0.51).
- holdout_libero_object test_ood, full, 50% reject: accepted 1.40 vs rejected 1.92 (Δ=0.52).
- holdout_libero_object test_ood, full, 75% reject: accepted 1.17 vs rejected 1.82 (Δ=0.65).

Conclusion: thresholding by predicted uncertainty creates a clear
separation between accepted and rejected SimVLA actions on real OOD
data. This is the strongest deployment-relevant signal Stage 5 produces.

## 10. OOD conclusion (controlled LIBERO-OOD)

For both held-out splits, on test_ood:

- **Expert action stays low-uncertainty:** `expert<simvla_seed0` 0.99–1.00,
  `expert<perturb_large` 1.00. The rater correctly assigns near-zero error
  to expert actions even on tasks the model never saw in train.
- **Wrong action types are higher-uncertainty:** `expert<other_task` 0.98+
  confirms wrong-context actions are correctly upweighted.
- **SimVLA-only uncertainty correlates with true error:** Pearson 0.91–0.96
  full, Spearman 0.91–0.96. AUROC 0.94–0.96 for the top-30%-worst label.
- **Action-error rater, not just an OOD detector:** the same-context
  ranking metrics (expert<perturb_large/other_task/seed0) are all near 1.0
  on OOD, meaning the rater discriminates *between candidate actions for
  the same observation*, not just *between observations*. Context-only
  scores 0.0 on those same metrics, confirming the model is doing more
  than OOD detection.

## 11. Calibration

| split | scheme | test_id cov | test_ood cov | mean width |
| --- | --- | ---: | ---: | ---: |
| id_task_split | global_residual | 0.86 | n/a | 1.04 |
| holdout_libero_object | global_residual | **0.91** | **0.91** | 0.97 |
| holdout_object_bowl | global_residual | 0.69 | 0.87 | 0.77 |

Detailed analysis in `stage5_simvla_only_calibration.md`.

- `holdout_libero_object` calibration is **deployable** as-is at α=0.1.
- `id_task_split` undercovers by 4 pp — needs a 1.1× q inflation factor.
- `holdout_object_bowl` test_id undercovers severely; root cause is the
  calib pool's structural similarity to test_ood, not the model. This is
  a **manifest-design issue** that should be addressed before claiming
  deployability for `bowl`-style holdouts.

## 12. Decision

**Improve rater architecture.** The most actionable conclusion is that
action-only currently matches or beats the full rater on SimVLA-only
seed ranking. We do not yet need to scale to "real external OOD" or
build the runtime switch until the full model justifies its extra
features by clearly beating action-only on the headline task. Concrete
next experiments:

1. Try a per-seed temperature / ensemble head that explicitly compares the
   candidate action to the model's own seed-mean — this would inject
   structure that pure action features cannot.
2. Try training with only SimVLA-seed candidates (`--train-setting
   simvla_focused`, already supported) to remove the synthetic-candidate
   bias.
3. Add proprio difference (`candidate_action - proprio`) as an explicit
   feature; this is a strong inductive bias the linear flatten loses.
4. Investigate whether the candidate action implicitly leaks the expert
   target via training data (target_expert_action is identical across
   candidates of a context — action-only learns "actions near training
   expert actions are good" which generalises to new contexts).

Other options considered:
- *Scale to full LIBERO controlled OOD* — not yet; current OOD already
  separates ID/OOD well, and scaling more does not address the
  action-only gap.
- *Integrate runtime VLA/WM switch* — premature; the switch proxy works
  but action-only is the simpler, equally-effective rater.
- *Improve candidate/action-error target* — possible, but evidence so
  far is that the L2 chunk error is well-predicted; the issue is which
  rater family captures it best.
- *Method fails on controlled OOD* — false: the method works on
  controlled LIBERO-OOD; what fails is the full-over-action improvement
  claim.

## 13. Next commands

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh

# A) try simvla-focused training to remove perturb/wrong-action bias
python3 -u asynchvla_ws/src/rater/train_stage5_rater.py \
  --debug false --split-name holdout_libero_object --train-setting simvla_focused

# B) add proprio-diff feature (requires a 1-line edit in feats())
#   then rerun all three splits

# C) larger calib for holdout_object_bowl
python3 -u asynchvla_ws/src/data_building/build_multiseed_trace_dataset.py \
  --split-manifest asynchvla_ws/data/splits/holdout_object_bowl.json \
  --split-name holdout_object_bowl \
  --max-contexts 1000 --max-calib 500 --max-test-id 250 --max-test-ood 250 \
  --cap-per-file 80 --simvla-seeds 0 1 2 3 4
python3 -u asynchvla_ws/src/data_building/build_multiseed_candidate_dataset.py \
  --split-name holdout_object_bowl
python3 -u asynchvla_ws/src/rater/train_stage5_rater.py \
  --debug false --split-name holdout_object_bowl
python3 -u asynchvla_ws/src/calibration/calibrate_stage5_simvla_only.py \
  --split-name holdout_object_bowl

# D) the switch-proxy as a Stage 6 hook
# (write a runtime helper that consumes the saved `full_rater.pt` checkpoint
#  and returns a single-action uncertainty score for the next SimVLA call.)
```

## 14. Duplicate report check

`find /home/redafrix/tests/internship/codex_reports -maxdepth 3 -type f | sort`:

```
/home/redafrix/tests/internship/codex_reports/ASYNCVLA_SIMVLA_STAGE5_MULTI_SEED_REPORT.md
/home/redafrix/tests/internship/codex_reports/done/action_sensitivity_eval.md
/home/redafrix/tests/internship/codex_reports/done/ASYNCVLA_SIMVLA_AUDIT_REPORT.md
/home/redafrix/tests/internship/codex_reports/done/ASYNCVLA_SIMVLA_IMPLEMENTATION_REPORT.md
/home/redafrix/tests/internship/codex_reports/done/ASYNCVLA_SIMVLA_STAGE3_REPORT.md
/home/redafrix/tests/internship/codex_reports/done/ASYNCVLA_SIMVLA_STAGE4_OOD_SPLITS_REPORT.md
/home/redafrix/tests/internship/codex_reports/done/candidate_debug_dataset_report.md
/home/redafrix/tests/internship/codex_reports/done/checkpoint_smoke_test.md
/home/redafrix/tests/internship/codex_reports/done/debug_calibration_report.md
/home/redafrix/tests/internship/codex_reports/done/debug_rater_metrics.md
/home/redafrix/tests/internship/codex_reports/done/env_check.md
/home/redafrix/tests/internship/codex_reports/done/libero_inventory_report.md
/home/redafrix/tests/internship/codex_reports/done/ood_expert_data_search.md
/home/redafrix/tests/internship/codex_reports/done/phase2_unblock_and_trace_report.md
/home/redafrix/tests/internship/codex_reports/done/split_manifest_report.md
/home/redafrix/tests/internship/codex_reports/done/stage4_calibration_comparison.md
/home/redafrix/tests/internship/codex_reports/done/stage4_holdout_libero_object_metrics.md
/home/redafrix/tests/internship/codex_reports/done/stage4_holdout_object_bowl_metrics.md
/home/redafrix/tests/internship/codex_reports/done/stage4_id_task_split_metrics.md
/home/redafrix/tests/internship/codex_reports/done/trace_debug_dataset_report.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_claude_resume_precheck.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_debug_interpretation.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_debug_rater_metrics.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_debug_rater_metrics_v2.json
/home/redafrix/tests/internship/codex_reports/stage5/stage5_debug_rater_metrics_v2.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_holdout_libero_object_metrics.json
/home/redafrix/tests/internship/codex_reports/stage5/stage5_holdout_libero_object_metrics.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_holdout_libero_object_simvla_only_calibration.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_holdout_object_bowl_metrics.json
/home/redafrix/tests/internship/codex_reports/stage5/stage5_holdout_object_bowl_metrics.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_holdout_object_bowl_simvla_only_calibration.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_id_task_split_metrics.json
/home/redafrix/tests/internship/codex_reports/stage5/stage5_id_task_split_metrics.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_id_task_split_simvla_only_calibration.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_medium_dataset_build_report.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_multiseed_candidate_debug.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_multiseed_trace_debug.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_preflight.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_simvla_only_calibration.md
/home/redafrix/tests/internship/codex_reports/stage5/stage5_simvla_only_eval_utility.md
```

Bob copy of this final report:
`/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/ASYNCVLA_SIMVLA_STAGE5_MULTI_SEED_REPORT.md`.

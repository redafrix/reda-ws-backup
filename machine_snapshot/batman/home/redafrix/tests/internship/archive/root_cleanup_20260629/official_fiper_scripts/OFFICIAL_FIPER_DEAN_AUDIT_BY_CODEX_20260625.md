# Official FIPER Dean Ablation Audit by Codex - 2026-06-25

## Scope

Audited the Antigravity/Gemini CLI session artifacts for the Dean official-FIPER ablation work, especially session:

`/home/redafrix/.gemini/antigravity-cli/brain/e7b67e76-d7b5-4262-9978-23b724a54de7`

Primary verified report:

`/home/redafrix/tests/internship/fiper_ws/experiments/official_fiper_rndoe_entropy_fold00_20260622/reports/OFFICIAL_FIPER_FINAL_ABLATION_COMPARISON_VERIFIED_20260624.md`

Remote Dean experiment root:

`/home/dean/fiper_uncertainty_collection/experiments/official_fiper_rndoe_entropy_fold00_20260622`

## What Was Verified

- Final Option A and Option B logs completed with 5 seeds for the official FIPER run.
- `option_a_results/complete_results.csv` and `option_b_results/complete_results.csv` each contain 18,601 lines.
- Dean materialized tensors exist and match expected shapes:
  - `obs_embeddings.pt`: `(170943, 960)`
  - `action_preds.pt`: `(170943, 9, 10, 7)`
  - rollouts: `1042`
- `metadata.pkl` confirms:
  - train rollouts: `497`
  - calibration rollouts: `135`
  - test rollouts: `410`
  - test ID rollouts: `157`
  - test OOD rollouts: `253`
  - OOD successes: `211`
  - OOD failures: `42`
  - no calibration/test leakage
  - no success/failure overlap
  - no ID/OOD overlap
- FIPER AND fusion is implemented as `np.minimum(...)` in Dean's official FIPER code, matching the report interpretation.

## Corrected Issue

The verified report and Obsidian report had incorrect step-count values in the split table. The episode counts and all main metrics were not changed, but the step counts were wrong.

Correct step counts from `metadata.pkl`:

| Split | Rollouts | Steps | Success | Failure | ID | OOD |
|---|---:|---:|---:|---:|---:|---:|
| RND Train | 497 | 75,463 | 497 | 0 | 497 | 0 |
| Calibration | 135 | 20,334 | 135 | 0 | 135 | 0 |
| Test | 410 | 75,146 | 347 | 63 | 157 | 253 |
| Test ID | 157 | 27,617 | 136 | 21 | 157 | 0 |
| Test OOD | 253 | 47,529 | 211 | 42 | 0 | 253 |

Updated files:

- `/home/redafrix/tests/internship/fiper_ws/experiments/official_fiper_rndoe_entropy_fold00_20260622/reports/OFFICIAL_FIPER_FINAL_ABLATION_COMPARISON_VERIFIED_20260624.md`
- `/home/redafrix/Documents/Obsidian Vault/FIPER Risk-Aware Report 20260602/FIPER Risk-Aware SimVLA - Full Report.md`
- `/home/redafrix/.gemini/antigravity-cli/brain/e7b67e76-d7b5-4262-9978-23b724a54de7/OFFICIAL_FIPER_FINAL_ABLATION_COMPARISON_VERIFIED_20260624.md`
- synced corrected report back to Dean at:
  `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_rndoe_entropy_fold00_20260622/reports/OFFICIAL_FIPER_FINAL_ABLATION_COMPARISON_VERIFIED_20260624.md`

## Trusted Final OOD Metrics

Use these as the official FIPER ablation comparison on the strict OOD test split:

| Method | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never | Balanced Acc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| FIPER entropy Option B | 35.1% | 100.0% | 7.1% | 47.6% | 71.4% | 0.393 | 0.0% | 82.5% |
| FIPER RND-OE Option B | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 0.000 | 0.0% | 50.0% |
| FIPER Fusion AND Option B | 38.9% | 97.6% | 11.9% | 52.4% | 78.6% | 0.314 | 2.4% | 79.4% |
| Our v2_018 score q95 K3 | 25.59% | 95.24% | 0.0% | 26.19% | 85.71% | 0.333 | 4.76% | 84.82% |

## Matched-False-Alarm Caveat

A wider sweep over Dean's `option_b_ood_only_complete_results.csv` shows that official FIPER/entropy can find operating points with Success FA near or below our 25.59% while preserving 100% failure detection. However, those points are much later:

| Method | Window | Quantile | Threshold | Success FA | Failure Det | Mean Time | Never | Accuracy |
|---|---:|---:|---|---:|---:|---:|---:|---:|
| entropy | 37 | 0.97 | tvt_quantile | 23.7% | 100.0% | 0.531 | 0.0% | 88.2% |
| entropy | 48 | 0.96 | tvt_quantile | 24.6% | 100.0% | 0.542 | 0.0% | 87.7% |
| rnd_oe_and_entropy | 1/37 | 0.97 | tvt_quantile | 23.7% | 100.0% | 0.531 | 0.0% | 88.2% |
| Our v2_018 score q95 K3 | n/a | n/a | q95 K3 | 25.59% | 95.24% | 0.333 | 4.76% | 84.82% |

This means the strongest supported claim is not "FIPER fails on every metric." The accurate claim is:

- FIPER RND-OE novelty alone fails on OOD because it saturates immediately.
- FIPER Fusion at the canonical q95/window row has higher false alarms than our method.
- When FIPER is allowed to sweep windows/quantiles, it can recover high detection at comparable false alarm, but it tends to detect substantially later than our temporal risk model.
- Our method is better as an early-warning detector at the selected operating point; FIPER can be competitive as a late timeout/failure detector.

## Caveats

- The report is valid for the materialized fold00 OOD split, not for every possible LIBERO OOD suite.
- Option A is only available for seed 42 in the verified OOD table because the other Option A seeds were overwritten/replaced during subsequent Option B handling.
- The Dean `repair_supervisor.log` contains an earlier failed official run, but the final Option A/Option B result logs and CSVs are complete.
- The Bob clean rerun report is a separate simplified comparison path. It should not be merged conceptually with the Dean official FIPER materialized-code ablation unless clearly labeled.

## Verdict

The main OOD metrics used for the official-FIPER ablation are legitimate after correcting the split step-count table. The conclusion is still supported: on strict OOD, official FIPER Fusion Option B has higher false alarms than our `v2_018` detector while only slightly higher failure detection.

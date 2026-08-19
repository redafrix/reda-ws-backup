# Dean Isaac Mimic-style risk-head offline ablation — no recollection

Date: 2026-08-19
Machine: Dean only
Canonical Isaac workspace: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`
Source collection: `outputs/final_seen_h10_round_000_seed20260730`

## Goal

Perform an offline architecture/feature-family ablation that adapts the friend's Mimic/video-model risk monitor as closely as the retained Isaac Round0 evidence permits.

This is NOT an attempt to improve the promoted Isaac TopK8 detector. Poorer results are scientifically acceptable. Fidelity to the friend's monitor family and transparent handling of unavailable evidence are more important than performance.

## Hard constraints

- NO new data collection.
- NO Isaac rollout or environment stepping is required for the primary experiment.
- NO regeneration of the 4000 source episodes.
- Use ONLY the accepted true-H10 Round0 source collection and its existing episode outcomes.
- All work is done on Dean.
- Preserve HARD1000 and all existing frozen/online evaluations untouched.
- The invalid candidate-trace reconstruction associated with commit `70327b4b31bde35c01fda29a807f9100b5295a62` is blacklisted and must never be reused.
- Never reuse candidate-0 diffusion/denoising traces as if they belonged to candidates 1..8.
- Never fabricate missing cross-candidate denoising quantities.

## Frozen source split

Reuse the existing episode-grouped split exactly:

- train: 2800 episodes
- validation: 600 episodes
- held-out seen test: 600 episodes

Expected source composition:

- total episodes: 4000
- successes: 3908
- failures: 92
- total decision/query rows: 75,603
- train rows: 52,825
- validation rows: 11,410
- test rows: 11,368

Do not resplit episodes and do not fit any normalizer on validation/test.

## Source-evidence reality

Round0 rows retain one main H10 proposal and eight alternative H10 proposals. The final candidate chunks are therefore available for exact candidate-disagreement calculations.

Round0 retains `simvla_uncertainty_raw` / denoising evidence for candidate 0 only. Candidate-specific denoising traces for alternatives 1..8 were not archived.

Therefore the primary offline ablation MUST distinguish four classes of feature evidence:

1. **EXACT_SAVED** — directly stored values from the accepted row.
2. **EXACT_RECONSTRUCTIBLE** — quantities deterministically recomputed from retained final candidate chunks/history without policy reinference.
3. **PROXY_FROM_CANDIDATE0** — a Mimic-family dynamic quantity approximated using genuine candidate-0 denoising evidence only; it must retain an explicit proxy name and must not be represented as exact cross-candidate dynamics.
4. **UNAVAILABLE** — cannot be recovered without missing alternative denoising trajectories or unavailable friend-model latent/video evidence. These must be omitted or explicitly masked according to the final source-backed model adapter; never fabricated.

## Friend-head source priority

Before implementation, resolve the actual friend/Mimic risk-head source available on Dean.

Priority order:

1. exact friend source code / handoff files on Dean;
2. exact copied source snapshot with verifiable hash;
3. only if exact code is unavailable, the retained paper-level K1 contract may be used as a fallback architecture description.

The paper-level retained K1 description is:

- eight-query temporal history;
- two-layer GRU;
- action/W2A uncertainty evidence;
- static branch width 128;
- GRU width 128;
- fused representation through a 64-D latent layer to a risk logit;
- episode-outcome supervision;
- successful-episode episode-max calibration.

Do not silently substitute the existing Isaac SeqRiskModel Transformer. The point of this experiment is to change the risk-head family.

## Candidate policy

Do not freeze an arbitrary eight-of-nine subset until the exact friend source/handoff candidate convention is recovered.

The retained Isaac rows contain enough final proposals for any friend contract requiring <=9 final candidates. If the friend code requires exactly 8 samples, select the deterministic subset specified by the recovered source/handoff. If no subset convention exists, use candidate0 + alternatives 1..7 and record this as an Isaac adaptation choice.

## What can be computed closely without recollection

Subject to the Stage-1 audit, expected exact/reconstructible families include:

- final candidate coordinate variance mean/max;
- final candidate pairwise chunk MSE/distances;
- main-vs-candidate-mean distance;
- per-action-index candidate variance across the H10 horizon;
- translation/rotation/gripper dispersion where action semantics permit;
- endpoint / cumulative positional-spread style features from final H10 chunks;
- main-plan geometry and plan-drift summaries;
- query-to-query change features;
- temporal histories from prior logged query records;
- all genuine candidate-0 denoising/path-variance/update summaries actually present in `simvla_uncertainty_raw` / the retained 49-D map.

Expected unavailable exact families include cross-candidate denoising-state and velocity-field statistics before the final samples because alternative X_d/V_d traces were not archived.

## Dynamic proxy rule

The experiment should preserve as much of the friend's dynamic-feature *structure* as evidence permits, but proxy features must be honest.

Examples of potentially defensible candidate-0 proxies, only if the raw audit verifies the necessary values:

- first/final/mean/max/delta of candidate-0 predicted-variance trace;
- candidate-0 velocity/update norm summaries;
- candidate-0 update oscillation/direction-flip summaries;
- candidate-0 accumulated path variance;
- exact final-sample disagreement across retained candidates.

Do NOT create pseudo traces by repeating a final-sample value over denoising steps.
Do NOT copy candidate0 trace values into alternative slots.
Do NOT infer unavailable X_d/V_d arrays from final chunks.

## Supervision

Reuse the existing episode-outcome target:

- success episode -> target 0 for its query rows
- failure/timeout episode -> target 1 for its query rows

No reward, future observation, task ID, source episode ID, scene category, timestep, OOD flag or final-distance value may enter neural features.

## Model selection and calibration

- Fit feature normalization on TRAIN only.
- Train only on TRAIN.
- Select checkpoint/hyperparameters using VALIDATION only.
- Freeze the selected model and all feature definitions before inspecting held-out TEST metrics.
- Report TEST only after freeze.

For comparability with the existing Isaac detector, report row AUROC/AUPRC and episode-level false alarm, failure detection, Det@25 and Det@50.

Also preserve the friend monitor's episode-max-success calibration if the recovered source confirms it. At minimum materialize validation-only operating points for best-F1, fixed 0.5 and success-derived q90/q95/q99, plus friend-style episode-max conformal levels when source-backed.

## OOD

OOD150 is OUT OF SCOPE until the Mimic-style model, preprocessing, feature contract and thresholds are frozen from the 4000 seen episodes. No OOD150 label or score may influence implementation choice, checkpoint selection, feature selection or thresholds.

## Stage order

1. Read-only source + friend-head + raw-feature audit.
2. Freeze a feature-availability matrix and exact adaptation contract.
3. Build offline materializer only; verify against deterministic sample rows.
4. Materialize train/validation/test arrays from existing Round0 rows only.
5. Train the friend-style head with no simulator.
6. Freeze checkpoint/thresholds on validation.
7. Evaluate held-out seen test and produce false-alarm/detection/timing metrics.
8. Only afterward decide whether to run frozen OOD150 as an additional transfer test.

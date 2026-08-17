# Dean Isaac V1 — offline threshold selection then ONE full OOD150 online intervention

## Goal
Reproduce the spirit of the LIBERO online risk-head experiment with exactly one active Isaac OOD150 intervention campaign.

Historical locked baseline is already complete and is the reference:
- 150 episodes
- 72 successes
- 78 failures
- strict success threshold 0.02 m
- H10

DO NOT rerun a fresh 150-episode baseline.

## Current compute state
HARD1000 is intentionally paused at 249/1000 while this protocol is executed. It must remain paused until the single active OOD150 campaign finishes or the protocol is explicitly abandoned.

## Scientific invariants
- Risk model: `models/isaac_h10_topk8_temporal_v1/model.pt`
- Frozen seen data: `frozen_datasets/isaac_seen_h10_topk8_v1`
- Locked OOD150: `frozen_datasets/locked_h10_ood150_eval` and historical rollout `outputs/final_locked_h10_ood150_seed20260728`
- OOD150 must never be used to retrain or normalize the model.
- Controller: LIBERO-final-style TopK8 `argmin_on_alarm` with zero margin.
- Execution horizon: H10, unchanged.
- Nine candidates: main + 8 alternatives.
- Selected alternative risk cap for the final controller is FIXED to the seen-derived `q90_success` value.
- Only the main alarm threshold is selected offline.

## Allowed main alarm thresholds
Use ONLY the five already-existing named thresholds from the V1 seen calibration file:
- `q90_success`
- `q95_success`
- `q99_success`
- `best_val_f1`
- `fixed_0.5`

Do not invent a numeric OOD-derived threshold and do not edit `thresholds.json`.

## Phase A — quick offline sweep on the complete seen-4000 campaign
No Isaac simulation. No recollection. No retraining.

Use existing frozen arrays / existing evaluator code / existing model to score the seen dataset. Inspect local array layouts as needed. It is allowed to create temporary analysis-only scripts under the new protocol output directory.

Compute metrics for all five allowed thresholds over the 4000 seen episodes, preserving train / validation / test split identities. Report aggregate-4000 metrics descriptively, but DO NOT select a threshold because it looks good on training data.

For validation and test separately compute at minimum:
- successful-episode false-alarm rate
- failure episode detection rate
- Det@10%
- Det@25%
- Det@50%
- never-detected failures
- mean normalized first-detection time where applicable

Construct a seen shortlist of at most 3 unique thresholds:
1. aggressive: highest test Det@25 among thresholds with test success false-alarm <= 20% and total failure detection >= 95%;
2. balanced: highest test Det@25 among thresholds with test success false-alarm <= 10% and total failure detection >= 95%;
3. conservative: lowest test success false-alarm among thresholds with total failure detection >= 95%.

Use validation metrics as a sanity check. If a requested tier has no feasible threshold, take the closest Pareto-optimal threshold and record why. Deduplicate identical choices.

Write:
`online_evals/isaac_ood150_offline_select_single_online_v1/offline/SEEN4000_THRESHOLD_SWEEP.json`
`online_evals/isaac_ood150_offline_select_single_online_v1/offline/SEEN_SHORTLIST.json`

## Phase B — offline test of the seen shortlist on locked OOD150
Still NO Isaac simulation.

Use the already-completed locked OOD150 risk scores / frozen arrays and evaluate ONLY the shortlisted main alarm thresholds.

For each shortlisted threshold compute on all 150 OOD episodes:
- success false-alarm rate over the historical 72 successful episodes
- failure detection rate over the historical 78 failed episodes
- Det@10 / Det@25 / Det@50
- never detected
- mean normalized first-detection time

Select exactly ONE final main threshold using this deterministic balanced rule:
1. require total OOD failure detection >= 95%;
2. prefer candidates with OOD success false-alarm <= 10%;
3. within that feasible set maximize Det@25;
4. tie-break by higher Det@10;
5. then lower success false-alarm;
6. then higher total failure detection;
7. final deterministic tie-break: lexical threshold name.

If no shortlisted threshold satisfies the 10% false-alarm constraint, widen once to 15% and apply the same ranking. If none satisfies 15%, choose from the Pareto frontier and document the trade-off explicitly before continuing.

The selected-risk cap remains `q90_success`; OOD is not used to invent or tune its numeric value.

Write:
`online_evals/isaac_ood150_offline_select_single_online_v1/offline/OOD150_SHORTLIST_OFFLINE.json`
`online_evals/isaac_ood150_offline_select_single_online_v1/offline/SELECTED_CONTROLLER.json`

`SELECTED_CONTROLLER.json` MUST contain at minimum:
```json
{
  "schema_version": "isaac_offline_selected_controller_v1",
  "main_threshold_name": "<one existing threshold name>",
  "selected_cap_name": "q90_success",
  "selection_source": "seen4000 shortlist then locked OOD150 offline balanced ranking",
  "historical_baseline_successes": 72,
  "historical_baseline_failures": 78
}
```
plus the actual seen and OOD metrics supporting selection.

## Phase C — functional shadow safety gate
Use the already-existing 3 shadow episodes; do not demand historical bitwise replay equality.

Run prepared `verify_shadow_functional.py` against the historical baseline and existing shadow3. It must verify:
- same three episode outcomes;
- same decision-row counts;
- same main and ACE candidate seed sequences;
- zero executed interventions in shadow mode;
- shadow executed action sequence equals candidate-0 main action sequence internally at <= 1e-6.

If this functional gate fails for a real scientific reason, do not run active OOD150. Infrastructure/data-format bugs may be diagnosed and fixed without changing controller semantics.

## Phase D — exactly ONE real active online test
Run exactly once:
`run_ONE_selected_full150_online.sh <absolute path to SELECTED_CONTROLLER.json>`

This launcher must use:
- all 150 locked OOD episodes;
- selected main alarm threshold from offline selection;
- fixed `q90_success` selected-risk cap;
- active risk-aware candidate selection;
- H10;
- strict 2 cm success threshold;
- same locked OOD manifest;
- no horizon shortening;
- no VLA or risk-model weight changes.

Do not run the other threshold candidates online.

Final paired summary is relative to the existing historical locked baseline 72/150 and must report:
- online successes /150
- delta successes vs 72
- rescues: historical baseline failure -> online success
- regressions: historical baseline success -> online failure
- unchanged successes
- unchanged failures
- changed episodes
- total action modifications

Because Isaac replay is not bitwise deterministic, rescues/regressions are paired descriptive comparisons to the historical locked rollout; the headline result is the active run success count versus the historical locked 72/150 reference.

## Phase E — resume HARD1000
Only after the single 150-episode online run is complete and the final summary is written, resume the existing HARD1000 pipeline from its committed 249 episodes. Verify the collector/pipeline actually restarts and progress continues beyond 249.

## Agy autonomy boundary
Agy MAY:
- solve Git, SSH, user-account, tmux, filesystem, shell, and environment plumbing;
- inspect local Dean file/array formats;
- write temporary OFFLINE ANALYSIS ONLY utilities needed to read `.npy/.npz/.jsonl` and compute the specified metrics;
- fix obvious non-scientific path/glob/reporting bugs while preserving the protocol;
- retry recoverable infrastructure failures using the same episode IDs/seeds/settings;
- push scripts, manifests, summaries, checksums, and audit evidence to the experiment branch.

Agy MUST NOT:
- retrain the model;
- edit model weights or normalization;
- change the five allowed threshold values;
- invent an OOD-derived numeric threshold;
- change the fixed q90 selected-risk cap;
- change H10, strict 2 cm, candidate count, controller semantics, or zero margin;
- run more than ONE active full-150 risk-aware campaign;
- rerun a fresh baseline150;
- resume HARD1000 before the online run completes.

If a scientific ambiguity appears that would require changing any invariant above, stop rather than improvise.

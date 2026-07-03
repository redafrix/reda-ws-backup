# Stage 5 Debug Rater v2 — Interpretation

Date: 2026-05-13
Source: `outputs/reports/stage5_debug_rater_metrics_v2.md`
Eval bug fix: `eval_simvla_only.py` pairwise tie-handling fixed to score tied predictions as 0.5 regardless of which true error is larger (previously asymmetric, biasing context-only to ~0.75).

## Setup recap

- 50 contexts, 500 candidates, 10 candidate types per context.
- Context-level deterministic split, salted on `stage5_debug`:
  - train: 30 contexts (300 rows), val: 10 contexts (100 rows), test: 10 contexts (100 rows).
- No context_id appears in more than one partition (anti-leakage).
- Three rater modes trained with identical Huber+AdamW recipe, 100 epochs.

## Headline metrics (test partition)

| metric | full | context | action |
| --- | ---: | ---: | ---: |
| all-cand Pearson | 0.821 | 0.325 | 0.921 |
| all-cand Spearman | 0.776 | 0.309 | 0.899 |
| all-cand AUROC@top30 | 0.803 | 0.748 | 0.966 |
| all-cand MAE | 0.256 | 0.522 | 0.178 |
| exp<perturb_large | 0.80 | 0.00 | 1.00 |
| exp<other_task | 0.80 | 0.00 | 0.60 |
| exp<simvla_seed0 | 1.00 | 0.00 | 1.00 |
| action_sensitivity_std (mean) | 0.539 | 0.000 | 0.568 |
| **SimVLA-only Spearman** | 0.939 | 0.935 | **0.994** |
| **SimVLA-only AUROC** | 0.964 | 0.981 | **0.994** |
| **SimVLA-only pairwise** | 0.710 | **0.500** (tied baseline) | **0.860** |
| **best-pred mean error** | 1.488 | 1.548 (= seed0) | **1.464** |
| seed0 mean error | 1.548 | 1.548 | 1.548 |
| oracle-best mean error | 1.461 | 1.461 | 1.461 |
| improvement_over_seed0 | 0.060 | 0.000 | **0.084** |
| gap_to_oracle | 0.027 | 0.087 | **0.002** |

Switch-proxy summary (test, full mode):
- accepted mean at 25% reject = 1.318, rejected mean = 2.108
- accepted mean at 50% reject = 1.195, rejected mean = 1.852
- accepted mean at 75% reject = 0.891, rejected mean = 1.724

All three modes produce *near-identical* switch-proxy numbers, which is exactly what we predicted: rejecting the highest-uncertainty SimVLA candidates is dominated by between-context error variation, which even context-only captures because hard contexts get higher predictions for all their seeds.

## Answers to the Phase C questions

### 1. Does the full rater beat context-only on same-context ranking?
**Yes.** Context-only has identical features within a context, so it cannot rank candidates of the same context at all (every `expert_lt_*` accuracy is exactly 0.0, action_sensitivity_std = 0.0). Full rater achieves 0.80 / 0.80 / 1.00 on the three expert-vs-noise rankings. This is the cleanest demonstration that full is doing something context-only architecturally cannot.

### 2. Does the full rater beat action-only on SimVLA-only seed ranking?
**No — action-only dominates on real SimVLA seed ranking.**
- pairwise: action 0.86 vs full 0.71
- best-pred improvement over seed0: action 0.084 vs full 0.060
- gap to oracle: action 0.002 vs full 0.027
The candidate action alone carries more signal about "which seed is closest to expert" than the action + context together do, at this dataset size.

### 3. Does action-only dominate? If yes, say so.
**Yes, on this 50-context debug set.** Hypotheses for why:
1. Action features (70 dims) are a tighter, more discriminative input than VLM features (960 dims) plus proprio (8 dims) + action (70 dims) when the train pool is only 300 rows. The high-dim context simply over-parameterises a tiny task.
2. The expert action is identical across all 10 candidates of a context, so the model can essentially learn `||cand - target||` from the candidate alone if it has memorised the target. With only 30 distinct contexts in train, this is plausible.
3. Action-only loses the same-context expert-vs-other_task ordering (0.60 < full's 0.80), showing it isn't strictly better — its win is concentrated on simvla-seed ranking and AUROC.

We need the medium runs (1000+ contexts) to see whether full catches up once context features stop being noise.

### 4. Is multi-seed selection meaningful on debug?
**Marginally.** Best-pred reduces mean SimVLA error from 1.548 (seed0) to 1.464 (action) or 1.488 (full). Oracle is 1.461. So action-only is essentially at oracle, full leaves 0.027 on the table. The headline is: predicted-best ≈ oracle when seeds are diverse and the rater can see the action. But the **magnitude** of the gain is small (~0.08 in L2 chunk units) and depends entirely on whether seeds are diverse enough to give the rater something to choose between.

### 5. Does predicted-best seed improve over seed0?
**Yes, but small.** Action-only: 0.084 absolute drop (5.4% relative). Full: 0.060 (3.8% relative). On 10 test contexts this is well within sampling noise — we cannot claim statistical significance from debug data alone.

### 6. Is pairwise seed ranking better than random 0.5?
- action: **0.86 — clearly above random.**
- full: **0.71 — clearly above random.**
- context: **0.50 — at random by construction** (tied predictions; this is now the corrected baseline, not 0.75).

### 7. Are synthetic candidate metrics much better than real SimVLA-only metrics?
**Yes, by a lot.** On test:
- `expert_lt_perturb_large` = 1.00 (action) — trivial: perturb_large always has higher error.
- `expert_lt_simvla_seed0` = 1.00 (action and full) — also trivial because seed0 errors are far larger than expert error.
- pairwise SimVLA-only = 0.71/0.86 — the **real** problem of distinguishing between five SimVLA seeds with similar errors is much harder.

Conclusion: synthetic perturbation candidates are an easy bound that almost any model can saturate, and they do not predict performance on the real multi-seed ranking task. We should keep them for unit-test sanity but stop using them as the headline metric.

### 8. Is the debug dataset too small or too dominated by one task?
**Yes to both.** From `stage5_multiseed_trace_debug.md`, all 50 contexts come from `put the white bowl on the plate`. With only 10 test contexts, every metric in this report has a sample noise of at least ~0.05 on accuracies and ~0.02 on mean-error gaps. The debug set is fit for plumbing tests only — every conclusion must be reverified on the medium splits.

### 9. Should we proceed to medium splits?
**Yes.** The plumbing works:
- context-level split is leak-free,
- NpEncoder works on every JSON path,
- three modes train and produce sane numbers,
- the eval bug is fixed,
- the SimVLA-only utility integrates cleanly.

But proceed with the explicit understanding that:
- action-only is the baseline to beat, not context-only;
- expect medium dataset build to be the slowest single step (≈5000+ SimVLA forward passes for train alone with 1000 contexts × 5 seeds);
- if medium runs still show action-only dominating, that is a real result, not a debug artifact.

## Action items for Phase D

1. Build medium trace + candidate datasets for `id_task_split`, `holdout_libero_object`, `holdout_object_bowl`. Start at 1000/250/250 sizes; degrade gracefully if runtime is excessive.
2. Re-run the rater on each split. Compare `full` vs `action` head-to-head on SimVLA-only pairwise, best-pred improvement, and switch proxy.
3. Specifically watch whether `holdout_object_bowl` (which removes the exact task the debug data was built from) breaks the action-only model: if action-only collapses while full holds, that is strong evidence the context features matter on OOD.

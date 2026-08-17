# Protocol: Pair-Calibrated Risk Controller (v2)

## 1. Problem Statement & Rationale
In initial online pilot evaluations, an uncoupled calibration where `main_threshold` was set independently while `selected_cap` was fixed to `q90_success = 0.2370966` led to zero online action modifications. This occurred because whenever the primary trajectory triggered an alarm state (`main_score >= 0.7990`), the entire candidate ensemble's risk distribution shifted upward (median alarm-conditioned best alternative risk ~0.999), causing the static `q90_success` cap to reject all safer alternatives.

To restore intended controller function, both parameters must be systematically and jointly calibrated from seen data:
1. **Main Alarm Threshold ($A$)**: Calibrated from the empirical distribution of episode-maximum main candidate risks on successful validation episodes.
2. **Alternative Safety Cap ($C$)**: Calibrated conditionally from the empirical distribution of best-alternative risks on validation decisions where $main\_score \ge A$ and $best\_alt\_score < main\_score$.

---

## 2. Seen Main Threshold Grid
Candidate alarm thresholds are generated systematically from the empirical quantiles of episode-maximum main scores across successful validation episodes:
- Percentiles: `q50`, `q60`, `q70`, `q75`, `q80`, `q85`, `q90`, `q92.5`, `q95`, `q97.5`, `q99`
- Named baselines: `best_val_f1`, `fixed_0.5`, `legacy_q90`, `legacy_q95`, `legacy_q99`
- Exact values are deduplicated to produce a unique candidate set.

---

## 3. Alarm-Conditioned Alternative-Cap Grid
For each candidate main alarm threshold $A$:
- Select all validation decision rows satisfying:
  $$main\_score \ge A \quad \text{and} \quad best\_alt\_score < main\_score$$
- Compute the conditional percentiles of $best\_alt\_score$:
  `q05`, `q10`, `q20`, `q25`, `q30`, `q40`, `q50`, `q60`, `q70`, `q75`, `q80`, `q90`, `q95`.

---

## 4. Offline Pair Evaluation on Seen Splits
For each pair $(A, C)$, counterfactual intervention opportunities are evaluated under the exact controller rule:
$$\text{Intervene with } best\_alt \iff main\_score \ge A \land best\_alt\_score < main\_score \land best\_alt\_score \le C$$

Metrics computed separately across Validation, Test, and Train:
- **Success Intervention Episode Rate**: Fraction of historical success episodes receiving $\ge 1$ intervention opportunity.
- **Failure Intervention Episode Rate**: Fraction of historical failure episodes receiving $\ge 1$ intervention opportunity.
- **Failure Opportunity@25**: Fraction of failure episodes receiving an intervention within the first 25% of the episode duration.
- **Separation**: $\text{Failure Rate} - \text{Success Rate}$.
- **Intervention Precision**: $\frac{\text{Failure Interventions}}{\text{Total Interventions}}$.

---

## 5. Seen Pareto Shortlist
A pair is dominated on validation if another pair achieves equal/lower success intervention rate and equal/higher failure intervention rate and Failure Opportunity@25. Non-dominated pairs are tiered into operating regimes:
- **Very Conservative**: $\text{Success Rate} \le 5\%$
- **Balanced**: $\text{Success Rate} \le 10\%$
- **Moderate**: $\text{Success Rate} \le 20\%$
- **Aggressive**: $\text{Success Rate} \le 30\%$

---

## 6. OOD150 Evaluation & Deterministic Selection
The frozen shortlist of 5–12 seen-derived pairs is evaluated counterfactually on the locked historical OOD150 dataset (72 successes, 78 failures).

Deterministic Ranking Rules:
1. Require $\text{Predicted Accepted Replacements} > 0$.
2. Require $\text{Failure Intervention Rate} > \text{Success Intervention Rate}$.
3. Prefer $\text{Success Intervention Rate} \le 20\%$.
4. Maximize $\text{Failure Intervention Rate}$.
5. Maximize $\text{Failure Opportunity@25}$.
6. Maximize $\text{Separation}$.
7. Maximize $\text{Failure-Side Replacements}$.
8. Minimize $\text{Success Intervention Rate}$.
9. Tie-break: higher main alarm $A$, then lower cap $C$.

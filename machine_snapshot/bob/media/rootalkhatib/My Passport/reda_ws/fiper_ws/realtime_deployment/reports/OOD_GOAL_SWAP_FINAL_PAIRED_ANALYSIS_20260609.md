# OOD Goal-Swap Production Final Paired Analysis (2026-06-09)

## 1. Executive Summary
The paired analysis of the 900-episode OOD goal-swap production run reveals that **aggressive TopK8 failed to improve overall performance** and, in some cases, introduced slight regressions. While the system intervened frequently (70-100% of episodes), the number of rescues was negligible (only 2 across all 900 episodes), and it was balanced by an equal or greater number of regressions.

**Verdict:** Aggressive TopK8 (threshold 0.3) is **NOT RECOMMENDED** for this OOD goal-swap scenario. It adds significant computational overhead and intervention complexity for zero net gain in success rate.

## 2. Methodology & Data Sources
- **Host:** Bob (`pcrobot`)
- **Root Path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_ood_goal_object_and_swap_20260608/runs/production_goal_swap_100ep_20260608`
- **Episodes:** 100 per Task/Policy (Total 900)
- **Seeds:** Perfect parity verified across all three policies for each task.

**JSONL Source Files:**
1. `top_drawer_bowl`:
   - `original_simvla/simvla_only/episode_summaries.jsonl`
   - `modified_simvla/simvla_only/episode_summaries.jsonl`
   - `risk_topk8/risk_topk8/episode_summaries.jsonl`
2. `cream_cheese_bowl`: (Same structure as above)
3. `bowl_on_plate`: (Same structure as above)

## 3. Aggregate Performance Comparison

| Task | Policy | Success Rate | Mean Steps | Mod Ep Count | Total Mods |
| :--- | :--- | :---: | :---: | :---: | :---: |
| top_drawer_bowl | original_simvla | 15% | 289.4 | 0 | 0 |
| | modified_simvla | 9% | 294.2 | 0 | 0 |
| | risk_topk8 | 8% | 295.5 | 70 | 200 |
| cream_cheese_bowl | original_simvla | 0% | 300.0 | 0 | 0 |
| | modified_simvla | 0% | 300.0 | 0 | 0 |
| | risk_topk8 | 0% | 300.0 | 100 | 530 |
| bowl_on_plate | original_simvla | 1% | 299.6 | 0 | 0 |
| | modified_simvla | 3% | 297.5 | 0 | 0 |
| | risk_topk8 | 2% | 298.5 | 93 | 371 |

## 4. Paired Analysis (Seed-to-Seed Comparison)

### Risk TopK8 vs. Modified SimVLA
This is the critical comparison to see if the detector helps the policy it was built on.

| Task | Shared Success | Shared Failure | Risk Rescue | Risk Regress |
| :--- | :---: | :---: | :---: | :---: |
| top_drawer_bowl | 7 | 90 | 1 | 2 |
| cream_cheese_bowl | 0 | 100 | 0 | 0 |
| bowl_on_plate | 1 | 96 | 1 | 2 |
| **TOTAL** | **8** | **286** | **2** | **4** |

**Observation:** Across 300 paired episodes, Risk TopK8 rescued 2 failures but caused 4 regressions. This is a net **NEGATIVE** impact.

## 5. Intervention Effectiveness
Analysis of episodes where `risk_topk8` actually modified the actions:

| Task | Mod Episodes | Rescue in Mod | Regress in Mod | Neutral in Mod |
| :--- | :---: | :---: | :---: | :---: |
| top_drawer_bowl | 70 | 1 | 2 | 67 |
| cream_cheese_bowl | 100 | 0 | 0 | 100 |
| bowl_on_plate | 93 | 1 | 2 | 90 |

- **In 263 modified episodes, only 2 (0.76%) resulted in a rescue.**
- 97.7% of interventions were "Neutral," meaning they did not change the final outcome (mostly shared failures).
- Interventions were slightly more likely to break a successful run (4) than fix a failing one (2).

## 6. Detailed Modification Distribution
- **top_drawer_bowl:** Mean 2.0 mods/ep. Peak at 1-2 mods. Max 7.
- **cream_cheese_bowl:** Mean 5.3 mods/ep. Extremely aggressive. Peak at 6 mods. Max 13.
- **bowl_on_plate:** Mean 3.7 mods/ep. Peak at 2-3 mods. Max 12.

The high intervention rate in `cream_cheese_bowl` (100% of episodes) without a single success indicates the detector is "panic-triggering" on a task the base policy simply cannot solve.

## 7. Final Recommendation
1. **Abandon Aggressive 0.3 Threshold:** It is too sensitive and induces jitter without corrective power in OOD.
2. **Investigate Policy Gap:** The drop from `original_simvla` to `modified_simvla` in `top_drawer_bowl` (15% -> 9%) suggests that the "modified" fine-tuning itself might have regressed on some OOD distributions.
3. **Threshold Tuning:** If TopK8 is used again, it requires a much higher threshold or a more conservative streak requirement to avoid over-intervention.

# OBSIDIAN_AND_WORKSPACE_UPDATE_20260608

## Files Modified
- `/home/redafrix/Documents/Obsidian Vault/FIPER Risk-Aware Report 20260602/FIPER Risk-Aware SimVLA - Full Report.md`
- `/home/redafrix/tests/internship/fiper_ws/EXPERIMENT_CATALOG.md`
- `/home/redafrix/tests/internship/fiper_ws/experiment_catalog/KEY_RESULTS.md`
- `/home/redafrix/tests/internship/fiper_ws/experiment_catalog/ARTIFACT_INDEX.md`
- `/home/redafrix/tests/internship/fiper_ws/experiment_catalog/WORKSPACE_MAP.md`
- `/home/redafrix/tests/internship/fiper_ws/README_CURRENT_WORKSPACE.md`
- `/home/redafrix/tests/internship/fiper_ws/experiment_catalog/README.md`
- `/home/redafrix/tests/internship/fiper_ws/experiment_catalog/hosts/bob.md`

## New Entries Created
- `experiment_catalog/entries/bob/bob__trash__h10_goal_object_risk_proof_20260608/README.md`
- `experiment_catalog/entries/bob/bob__trash__h10_goal_object_topk8_aggressive_task3_20260608/README.md`
- `experiment_catalog/entries/bob/bob__trash__h10_goal_object_task6_old_topk8_aggressive_20260608/README.md`

## Figures Created
All stored in `/home/redafrix/Documents/Obsidian Vault/FIPER Risk-Aware Report 20260602/assets/20260608_h10_topk8_ablation/`:
- `task3_sr.png`: Task 3 success rate comparison.
- `task6_sr.png`: Task 6 success rate comparison.
- `intervention_counts.png`: Log-scale intervention frequency for T3/T6.
- `task6_paired_outcomes.png`: Pie chart of rescues, regressions, and unchanged outcomes.
- `threshold_effect.png`: Dual-axis plot of SR vs Intervention Rate across thresholds.

## Exact Result Numbers Inserted
- **Task 3:** Greedy 17%, Cons 17%, Aggr 19%. Rescues: [211088021, 923894520]. Regressions: 0.
- **Task 6:** Greedy 57%, Cons 57%, Aggr 62%. Rescues: 17. Regressions: 12.
- **Old Detector (Task 6):** 60% SR, 194.82 Mean Steps, 606 mods.

## Summary of Findings
- The H10-retrained `unc_topk8` detector at 0.3 threshold is the new "aggressive" state-of-the-art for Bob precision tasks.
- H10 retraining is confirmed superior (+2% SR) to the previous Dean all-tasks-full detector.
- Intervention rate at 0.3 is very high (94% of episodes in Task 6), acting as a tight closed-loop correction layer.

## Uncertainties / Audit Issues
- The 0.3 threshold is a manual "best guess" for ablation and not yet formally calibrated on OOD tasks.
- Same-seed provenance remains valid for reset seeds, but late-timestep action-sampling seeds diverge if trajectory lengths differ (as documented in Section 8).

# Agy Execution Plan

Agy must execute the following stages in order and stop on any failed gate:

1. Read-only HARD1000/GPU preflight.
2. Locate and hash the exact current V1 trainer/source/model code on Dean.
3. Copy V1 trainer to a new V2 trainer path; never edit V1.
4. Implement only the frozen episode-balanced/class-balanced loss and validation-selection changes described in this directory.
5. Run static code diff and CPU unit/synthetic weighting tests before production training.
6. Recompute the exact training weighting audit from the frozen arrays.
7. Train V2 for the exact 10-epoch recipe.
8. Freeze selected checkpoint by Seen-validation episode-balanced AUPRC.
9. Derive both legacy-query and episode-balanced threshold families from Seen validation only.
10. Evaluate V1 and V2 on identical frozen Seen validation/test rows.
11. Freeze V2 checkpoint/model/threshold hashes.
12. Only then evaluate V2 on the already existing locked OOD150 offline dataset, without tuning.
13. Do not launch OOD400 and do not launch any Isaac process.
14. Verify HARD1000 health after every expensive stage and at the end.
15. Commit only new V2 code/evidence files and push the existing experiment branch.

Agy returns raw paths/hashes/metrics only. ChatGPT interprets whether V2 is scientifically better.
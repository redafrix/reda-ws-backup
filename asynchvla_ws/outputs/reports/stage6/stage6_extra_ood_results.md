# Stage 6 Extra Controlled-OOD Results

Completed extra split: `holdout_libero_spatial`. Additional requested splits (`holdout_libero_goal`, scene-heldout, second object-heldout) were not completed in this session because each full five-seed extraction takes about 16 minutes; commands are included in the final report for nohup execution.

| Split | Variant | Part | Pairwise | Impr over seed0 | Gap oracle | AUROC | Acc50 | Rej50 | Expert<other |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| `holdout_libero_spatial` | `action_only_baseline` | `test_ood` | 0.7075 | 0.0411 | 0.0219 | 0.7677 | 1.7787 | 2.0508 | 0.495 |
| `holdout_libero_spatial` | `full_old_baseline` | `test_ood` | 0.8715 | 0.0581 | 0.0048 | 0.9573 | 1.6485 | 2.1810 | 0.995 |
| `holdout_libero_spatial` | `context_gated_action` | `test_ood` | 0.9170 | 0.0614 | 0.0016 | 0.9657 | 1.6590 | 2.1705 | 1.0 |

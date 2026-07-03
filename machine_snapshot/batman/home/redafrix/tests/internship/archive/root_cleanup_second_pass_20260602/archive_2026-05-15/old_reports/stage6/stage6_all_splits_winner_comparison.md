# Stage 6 Winner Comparison Across Core Splits

| Split | Variant | Part | Pairwise | Impr over seed0 | Gap oracle | AUROC | Acc50 | Rej50 | Expert<other |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| `id_task_split` | `action_only_baseline` | `test_id` | 0.7164 | 0.0573 | 0.0233 | 0.8657 | 1.0791 | 1.8627 | 0.508 |
| `id_task_split` | `context_only_baseline` | `test_id` | 0.5000 | 0.0000 | 0.0806 | 0.9259 | 1.0333 | 1.9085 | 0.5 |
| `id_task_split` | `full_old_baseline` | `test_id` | 0.8052 | 0.0648 | 0.0158 | 0.9926 | 1.0016 | 1.9402 | 0.944 |
| `id_task_split` | `context_gated_action` | `test_id` | 0.8932 | 0.0727 | 0.0079 | 0.9982 | 0.9406 | 2.0011 | 0.988 |
| `id_task_split` | `full_engineered_simvla_focused` | `test_id` | 0.8968 | 0.0727 | 0.0079 | 0.9887 | 0.9580 | 1.9838 | 1.0 |
| `holdout_libero_object` | `action_only_baseline` | `test_ood` | 0.7512 | 0.0473 | 0.0224 | 0.7072 | 1.4715 | 1.8481 | 0.516 |
| `holdout_libero_object` | `context_only_baseline` | `test_ood` | 0.5000 | 0.0000 | 0.0697 | 0.7243 | 1.4388 | 1.8808 | 0.5 |
| `holdout_libero_object` | `full_old_baseline` | `test_ood` | 0.8240 | 0.0558 | 0.0139 | 0.9103 | 1.3774 | 1.9423 | 0.972 |
| `holdout_libero_object` | `context_gated_action` | `test_ood` | 0.9160 | 0.0638 | 0.0059 | 0.9721 | 1.3581 | 1.9615 | 0.992 |
| `holdout_libero_object` | `full_engineered_simvla_focused` | `test_ood` | 0.8996 | 0.0646 | 0.0052 | 0.9641 | 1.3606 | 1.9591 | 0.996 |
| `holdout_object_bowl` | `action_only_baseline` | `test_ood` | 0.7552 | 0.0531 | 0.0151 | 0.8406 | 1.3356 | 1.9104 | 0.524 |
| `holdout_object_bowl` | `context_only_baseline` | `test_ood` | 0.5008 | 0.0000 | 0.0682 | 0.9671 | 1.1410 | 2.1050 | 0.5 |
| `holdout_object_bowl` | `full_old_baseline` | `test_ood` | 0.8756 | 0.0594 | 0.0088 | 0.9935 | 1.1234 | 2.1226 | 0.988 |
| `holdout_object_bowl` | `context_gated_action` | `test_ood` | 0.9256 | 0.0660 | 0.0022 | 0.9968 | 1.1178 | 2.1283 | 0.972 |
| `holdout_object_bowl` | `full_engineered_simvla_focused` | `test_ood` | 0.9052 | 0.0642 | 0.0040 | 0.9984 | 1.1152 | 2.1308 | 1.0 |

Conclusion: context-gated and engineered SimVLA-focused models beat the Stage 6 action-only baseline on every core split. Compared with the Stage 5 action-only baseline reported in Stage 5, context-gated also improves pairwise ranking on the key holdout_libero_object OOD split (0.916 vs 0.865).

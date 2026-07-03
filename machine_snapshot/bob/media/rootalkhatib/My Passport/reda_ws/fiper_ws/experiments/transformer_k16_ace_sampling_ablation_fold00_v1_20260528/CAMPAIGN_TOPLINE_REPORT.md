# NextGen Clean Temporal Campaign Report

| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `ace_ablate_02_first4_every_step` | supervised | seq_transformer | 1.0200 | 45.02% | 100.00% | 42.86% | NA | NA |
| 2 | `ace_ablate_03_first4_every_2_steps` | supervised | seq_transformer | 0.9055 | 22.27% | 92.86% | 19.05% | NA | NA |
| 3 | `ace_ablate_00_control_full8_every_step` | supervised | seq_transformer | 0.8611 | 50.24% | 100.00% | 40.48% | NA | NA |
| 4 | `ace_ablate_01_full8_every_2_steps` | supervised | seq_transformer | 0.8283 | 25.59% | 90.48% | 19.05% | NA | NA |

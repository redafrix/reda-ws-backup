# OOD400 Setup-Only Preflight Checklist

This checklist is for preparing the benchmark while HARD1000 continues. It must not launch simulation.

Required PASS conditions before the benchmark is marked `FROZEN_READY_FOR_FUTURE_EVAL`:

1. The copied manifest SHA-256 is exactly `264dae5a7de872e5aee0a9554f88adfe7af3d38b5a7e29fd7f9b3e0d1c10da41`.
2. Schema is `simvla_reaching_ood_benchmark_v1`.
3. Benchmark name is `reaching_pose_v1_mimic_risk_full_ood400`.
4. Exactly 400 episodes exist, benchmark IDs are exactly 0..399, and all are `risk_split=ood_test`.
5. There are 400 unique `scene.source_episode_id` values.
6. There are 400 unique scene fingerprints.
7. Target position indices are exactly 100..499 once each.
8. Clutter position indices are exactly 100..499 once each.
9. There are exactly 31 target variants represented.
10. Every referenced target/clutter asset variant resolves through the current Dean Isaac scene/object registry.
11. Every scene can be parsed/materialized by the current benchmark loader without rewriting the manifest.
12. Exact source-ID overlap with the existing locked true-H10 OOD150 is zero.
13. No file under the active HARD1000 output tree is modified.
14. No Isaac/SimVLA/Mimic rollout is launched.
15. No OOD400 outcome, detector score, success/failure label, or controller intervention is generated during setup.

Allowed outputs are metadata-only compatibility/audit files and the exact copied manifest.

The future evaluation remains forbidden until HARD1000 is complete and a separate explicit launch instruction is issued.

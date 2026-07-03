# FIPER Experiment Catalog

This is the canonical navigation layer for the distributed FIPER, SimVLA, and risk-aware experiments. Original artifacts remain in place so existing scripts and provenance paths are not broken.

## Start Here

- [Cross-machine experiment map 2026-07-03](CROSS_MACHINE_EXPERIMENT_MAP_20260703.md)
- [Deep experiment coverage audit 2026-07-03](DEEP_EXPERIMENT_COVERAGE_AUDIT_20260703.md)
- [Key results and their actual meaning](KEY_RESULTS.md)
- [Trusted results summary (forensic-verified)](TRUSTED_RESULTS_SUMMARY.md)
- [Master experiment index](MASTER_EXPERIMENT_INDEX.md)
- [Dataset map](DATASET_MAP.md)
- [Big artifacts not in Git 2026-07-03](BIG_ARTIFACTS_NOT_IN_GIT_20260703.md)
- [Git sync plan 2026-07-03](GIT_SYNC_PLAN_20260703.md)
- [Host workspace map](HOST_WORKSPACE_MAP.md)
- [Model and suite identity verification](MODEL_AND_SUITE_IDENTITY.md)
- [Forensic audit map (8-step audit)](FORENSIC_AUDIT_MAP.md)
- [Codex full workspace audit 2026-06-10](CODEX_FULL_WORKSPACE_AUDIT_20260610.md)
- [CLI session provenance 2026-06-10](CLI_SESSION_PROVENANCE_20260610.md)
- [Dean selected-cap gate 2026-06-10](DEAN_SELECTED_CAP_GATE_20260610.md)
- [OpenVLA experiment map 2026-06-19](OPENVLA_EXPERIMENT_MAP_20260619.md)
- [Obsidian report accuracy audit](OBSIDIAN_REPORT_ACCURACY_AUDIT_20260609.md)
- [Workspace map (legacy)](WORKSPACE_MAP.md)
- [Synchronization status](SYNC_STATUS.md)
- [Required README schema](README_SCHEMA.md)
- [Artifact index](ARTIFACT_INDEX.md)
- [Entries requiring semantic verification](UNVERIFIED_ENTRIES.md)
- [Batman index](hosts/batman.md): 15 catalog entries
- [Bob index](hosts/bob.md): 83 catalog entries
- [Dean index](hosts/dean.md): 109 catalog entries
- [Sam index](hosts/sam.md): 5 catalog entries

## Deep Coverage Audit

The 2026-07-03 deep audit rescanned local/Batman, Bob, Sam, and Dean workspaces, including archive folders. It reduced 2,888 experiment-like roots and identified 445 roots that were not clearly covered by the previous text maps. Many are archived/script/package false positives, but the audit restored important families to the active navigation layer: Bob Pi0.5 subruns, Bob `bob_risk_matrix_campaign_20260605`, Bob `re_run_v2_018_audit_20260624`, Sam video-review reels, Dean `fiper_goal_object_collection_20260605`, Dean TDQC/SimVLA legacy roots, and local Stage6-9 archive material.

Use [DEEP_EXPERIMENT_COVERAGE_AUDIT_20260703.md](DEEP_EXPERIMENT_COVERAGE_AUDIT_20260703.md) and [manifests/deep_audit_summary_20260703.json](manifests/deep_audit_summary_20260703.json) when a future session needs to recover old or archived evidence.

## Semantic Corrections

> The May 29 to June 1 four-task reports label their paired baseline as vanilla SimVLA, but both runners loaded the default modified checkpoint ckpt-60000. Treat those experiments as modified SimVLA versus modified SimVLA plus the base risk detector.
> Bob and Dean are separate hardware replications. Their closed-loop outcomes are not expected to match episode-for-episode even with identical seeds because GPU-level numerical differences alter generated actions.
> A result is canonical only when its checkpoint, runner, detector artifacts, reset-seed manifest, action-seed protocol, and raw episode summaries are all identified. Aggregate-only reports are evidence summaries, not substitutes for raw logs.
> The Step 5 Synthesis report (2026-06-09) incorrectly claimed "98.9% intervention rate" for Task 3. The correct query-level modification rate is 1.04%. See [TRUSTED_RESULTS_SUMMARY.md](TRUSTED_RESULTS_SUMMARY.md).
> OOD goal-swap (2026-06-08) was net negative (-2 successes). Do not claim OOD generalization.
> The 2026-06-09/10 full-suite OOD goal-object sweep is the current strongest OOD evidence: threshold 0.3 was net negative vs modified SimVLA, threshold 0.5 tied modified SimVLA globally, and q95 completed net negative.
> Sam V2B/V2C/V2D adaptive-horizon diagnostics are mechanically valid negative controls; none beat fixed H10 modified SimVLA.
> Dean selected-cap TopK8 is the current most promising OOD risk-aware variant: 10ep full-suite result was +6 net vs modified SimVLA, and a 100ep confirmation is running.
> OpenVLA-OFT work is isolated under Bob's `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616` workspace. Its datasets, risk models, and online OOD runs use a different policy and feature schema from SimVLA/FIPER; start from `OPENVLA_EXPERIMENT_MAP_20260619.md` before interpreting those results.

## Status Vocabulary

- `active`: a matching process was running when the manifest was captured.
- `complete`: observed episode rows met the episode count declared in an associated config.
- `inactive_with_results`: results exist, but automatic completion proof is unavailable.
- `artifacts_only_or_unknown`: model/config/report artifacts exist without a recognized episode summary.
- `archived`: historical material retained for provenance.
- `host_offline_result_known_from_audit`: only a prior audited summary is locally available.

## Operating Rule

Never compare two folders based only on names such as `baseline`, `risk_base`, or `vanilla`. Verify the checkpoint, runner, seed manifest, execution horizon, and success semantics recorded in the experiment README.

Generated: `2026-06-05T11:53:02.370785+00:00`
Last updated: `2026-07-03T12:20:00+02:00` (deep cross-host/archive coverage audit added; Git repair status corrected)

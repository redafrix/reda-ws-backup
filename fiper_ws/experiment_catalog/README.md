# FIPER Experiment Catalog

This is the canonical navigation layer for the distributed FIPER, SimVLA, and risk-aware experiments. Original artifacts remain in place so existing scripts and provenance paths are not broken.

## Start Here

- [Key results and their actual meaning](KEY_RESULTS.md)
- [Trusted results summary (forensic-verified)](TRUSTED_RESULTS_SUMMARY.md)
- [Master experiment index](MASTER_EXPERIMENT_INDEX.md)
- [Dataset map](DATASET_MAP.md)
- [Host workspace map](HOST_WORKSPACE_MAP.md)
- [Model and suite identity verification](MODEL_AND_SUITE_IDENTITY.md)
- [Forensic audit map (8-step audit)](FORENSIC_AUDIT_MAP.md)
- [Codex full workspace audit 2026-06-10](CODEX_FULL_WORKSPACE_AUDIT_20260610.md)
- [CLI session provenance 2026-06-10](CLI_SESSION_PROVENANCE_20260610.md)
- [Dean selected-cap gate 2026-06-10](DEAN_SELECTED_CAP_GATE_20260610.md)
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

## Semantic Corrections

> The May 29 to June 1 four-task reports label their paired baseline as vanilla SimVLA, but both runners loaded the default modified checkpoint ckpt-60000. Treat those experiments as modified SimVLA versus modified SimVLA plus the base risk detector.
> Bob and Dean are separate hardware replications. Their closed-loop outcomes are not expected to match episode-for-episode even with identical seeds because GPU-level numerical differences alter generated actions.
> A result is canonical only when its checkpoint, runner, detector artifacts, reset-seed manifest, action-seed protocol, and raw episode summaries are all identified. Aggregate-only reports are evidence summaries, not substitutes for raw logs.
> The Step 5 Synthesis report (2026-06-09) incorrectly claimed "98.9% intervention rate" for Task 3. The correct query-level modification rate is 1.04%. See [TRUSTED_RESULTS_SUMMARY.md](TRUSTED_RESULTS_SUMMARY.md).
> OOD goal-swap (2026-06-08) was net negative (-2 successes). Do not claim OOD generalization.
> The 2026-06-09/10 full-suite OOD goal-object sweep is the current strongest OOD evidence: threshold 0.3 was net negative vs modified SimVLA, threshold 0.5 tied modified SimVLA globally, and q95 completed net negative.
> Sam V2B/V2C/V2D adaptive-horizon diagnostics are mechanically valid negative controls; none beat fixed H10 modified SimVLA.
> Dean selected-cap TopK8 is the current most promising OOD risk-aware variant: 10ep full-suite result was +6 net vs modified SimVLA, and a 100ep confirmation is running.

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
Last updated: `2026-06-10T18:55:00+02:00` (Codex full workspace audit and Dean selected-cap follow-up)

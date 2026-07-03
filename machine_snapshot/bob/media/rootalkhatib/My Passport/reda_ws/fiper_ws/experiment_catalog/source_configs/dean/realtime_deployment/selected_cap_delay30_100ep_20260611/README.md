# Dean Selected-Cap Delay30 100ep Config Source

This folder preserves the generator used to create the active Dean replication:

`/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_delay30_100ep_20260611`

Purpose:

- Replicate the successful selected-cap OOD run with fresh seeds.
- Test whether suppressing early replacements reduces regressions.

Key configuration:

- Suite: `libero_goal_object_ood`
- Tasks: 0-17
- Seeds: 400-499
- Policies: modified SimVLA fixed H10 baseline and TopK8 selected-cap delay30
- Checkpoint: modified SimVLA `ckpt-60000`, SHA256 `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`
- Detector: H10 TopK8, SHA256 `687b5d35eed65abfe63b5ff600e52c2228318ad94209e379e73fbaad981dbb2d`
- Gate: `selection_main_threshold=0.3`, `selection_min_margin=0.02`, `selection_strong_margin=0.05`, `selection_max_selected_score=0.4`
- New condition: `selection_min_timestep=30`

The generator was created locally under:

`/home/redafrix/tests/internship/checks/codex_full_workspace_audit_20260610/generate_dean_selected_cap_delay30_100ep_campaign.py`

and copied here so the synchronized experiment catalog contains the reproducible setup.

# Current Dean Risk Models (2026-06-02)

Only two ideas are kept as active future-facing risk detectors:

- `base`: same architecture and inputs as the selected transformer risk baseline.
- `unc_topk8`: same architecture, plus the 8 selected SimVLA uncertainty dimensions in the static branch.

Canonical splits copied here:

- `ood_last2_taskids_full`: primary split for seen-vs-held-out realtime tests.
- `all_tasks_full`: in-distribution reference split, preserved for future checks.

Other uncertainty ideas remain archived or in their original experiment reports, but should not be treated as active baselines.

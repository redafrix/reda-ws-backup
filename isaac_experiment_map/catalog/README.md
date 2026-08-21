# Isaac Experiment Map Catalog

Permanent, machine-readable, analysis-ready registry of all Isaac Sim / IsaacLab SimVLA experiments and active risk controller evaluations.

## Structure
- `experiments.jsonl`: Rich JSONL records of all experiments, benchmarks, models, statuses, and metadata.
- `experiment_results.csv`: Flat tabular summary (1 row per experiment/variant) for pandas.
- `metrics_long.csv`: Tidy/long-format metric table for easy querying and plotting.
- `paired_comparisons.csv`: Valid paired comparison matrices (Baseline vs C090, Baseline vs Q95, C090 vs Q95).
- `controller_operating_points.csv`: Risk threshold operating points ($A, C, M$, source calibration, executed status).
- `dataset_model_registry.csv`: Registry of datasets, models, architectures, parameter counts, weights hashes, and norm hashes.
- `protocol_registry.json`: Formal evaluation protocols and physics/control decimation specifications.
- `artifact_registry.jsonl`: Checksums, sizes, and file paths for all models, manifests, videos, and evidence artifacts.
- `quarantine_registry.csv`: Registry of quarantined and invalid runs (`safe_to_use = false`).

## Analysis-Ready Tables (`../analysis_ready/`)
- `ood400_episode_results.csv`: 1,200 rows ($400\text{ episodes} \times 3\text{ variants}$) containing exact episode outcomes, durations, distances, interventions, and paired categorizations.
- `ood400_decision_summary.csv`: 19,514 online decision queries with main risk, best alt risk, selected candidate, alarm, and intervention flags.

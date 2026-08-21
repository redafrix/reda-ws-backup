# Isaac Sim / SimVLA Experiment Map & Permanent Results Catalog

Authoritative index and machine-readable data repository for all Isaac Sim and IsaacLab SimVLA experiments, risk models, and active controller evaluations.

## Directory Structure
- `catalog/`: Machine-readable catalog files (`experiments.jsonl`, `experiment_results.csv`, `metrics_long.csv`, `paired_comparisons.csv`, `controller_operating_points.csv`, `dataset_model_registry.csv`, `protocol_registry.json`, `artifact_registry.jsonl`, `quarantine_registry.csv`).
- `analysis_ready/`: Tidy, analysis-ready datasets (`ood400_episode_results.csv`, `ood400_decision_summary.csv`, `ood150_episode_results.csv`, `risk_model_metrics.csv`, `threshold_sweep.csv`).
- `experiments/`: Narrative Markdown records for all experimental series (EXP-001 through EXP-011).
- `inventory/`: Artifact inventory and index JSONs.
- `tools/`: Build and validation scripts (`build_isaac_results_catalog.py`, `validate_isaac_results_catalog.py`).
- `CURRENT_MAIN_ISAAC_RESULTS_20260821.md`: Current canonical results narrative.

## Quick Start in Python
```python
import pandas as pd
import json

# Load flat experiment results
df_results = pd.read_csv("isaac_experiment_map/catalog/experiment_results.csv")

# Filter canonical primary experiments
canonical_df = df_results.query("use_for_primary_results == True")

# Load 1200-row episode results
df_episodes = pd.read_csv("isaac_experiment_map/analysis_ready/ood400_episode_results.csv")
```

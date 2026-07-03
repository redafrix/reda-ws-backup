# TDQC Standalone Workspace

## Directory layout

| Path | Purpose |
|------|---------|
| `core/phase2_tdqc/` | Shared importable library. Never edit directly for experiments — copy into experiment's `code/` first. |
| `data/v6/` | v6 dataset (3924 episodes, 8D features). Active file: `final_calibrated_3924rollouts_v6.pt` |
| `data/v6/archive/` | Old intermediate v2/v3/v4/v5 datasets — do not use. |
| `data/v7/` | v7 dataset (39421 episodes, 11D features, pre-split). Use `v7_11d_{train,val,test}.pt` |
| `docs/` | Gemini prompts, proposals, planning notes. |
| `experiments/` | One folder per experiment. See naming convention below. |

## Experiment naming convention

```
v{dataset_version}_{short_description}/
```

Examples:
- `v6_idea1_mc_loss` — v6 dataset, testing MC loss
- `v7_exp01_combined134` — v7 dataset, first combined experiment
- `v7_exp03_no_task_embed` — v7 dataset, ablation: no task embedding

## Inside each experiment folder

```
experiment_name/
├── code/        ← copy of all Python files used (never import from core/ directly)
├── runs/        ← best.pt, last.pt, history.json, config.json
├── plots/       ← all .png outputs for this experiment
├── analysis/    ← eval scripts + result JSONs
├── logs/        ← training_log.txt
└── README.md    ← params + results summary (fill in when done)
```

## How to launch a training

```bash
cd /home/redafrix/tests/intern_ship_research/intern_ship_ws/tdqc/code/phase2_tdqc_standalone

PYTHONPATH=experiments/<name>/code \npython3 experiments/<name>/code/phase2_tdqc/train_tdqc.py \n    --train_path data/v7/v7_11d_train.pt \n    --val_path   data/v7/v7_11d_val.pt   \n    --test_path  data/v7/v7_11d_test.pt  \n    --output_dir experiments/<name>/runs/<name> \n    ... \n    2>&1 | tee experiments/<name>/logs/training_log.txt
```

## Data paths (always use these)

- v7 train: `data/v7/v7_11d_train.pt`
- v7 val:   `data/v7/v7_11d_val.pt`
- v7 test:  `data/v7/v7_11d_test.pt`
- v6 main:  `data/v6/final_calibrated_3924rollouts_v6.pt`

## Rules

1. Never run scripts from the wrong working directory — always `cd` to project root first.
2. Every experiment gets its own `code/` copy — never share code between experiments.
3. Plots go in `plots/`, eval scripts go in `analysis/`. Nothing loose at experiment root.
4. Fill in `README.md` with key results when the experiment finishes.
5. Old/unused datasets go to `data/v6/archive/` — never delete.

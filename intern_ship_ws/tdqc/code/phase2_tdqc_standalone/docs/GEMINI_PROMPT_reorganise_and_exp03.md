# TDQC Workspace: Reorganise + Experiment 03 (No Task Embedding)

All commands run from the standalone project root unless stated otherwise:
```
/home/redafrix/tests/intern_ship_research/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/
```

---

## PART 1 — Workspace Reorganisation

### Why

The workspace has grown messy: orphaned plots in `results/`, orphaned scripts in `scripts/`,
datasets named inconsistently in `data/`, and experiments in `tests_trains/` with no clear
naming convention. Fix it once and keep it clean forever.

### Target layout

```
phase2_tdqc_standalone/
├── WORKSPACE.md               ← rules for future work
├── core/                      ← shared importable library (renamed from code/)
│   └── phase2_tdqc/
├── data/
│   ├── v6/                    ← all 3924-rollout datasets
│   └── v7/                    ← all 39421-episode datasets (train/val/test .pt)
├── docs/                      ← planning docs, Gemini prompts, proposals
└── experiments/               ← renamed from tests_trains/
    ├── v6_baseline/
    ├── v6_idea1_mc_loss/
    ├── v6_idea2_delta_features/
    ├── v6_idea3_task_embed/
    ├── v6_idea4_large_lstm/
    ├── v6_idea5_transformer/
    ├── v6_combined_14/
    ├── v6_combined_134/
    ├── v7_exp01_combined134/
    ├── v7_exp02_combined134_reg/
    └── v7_exp03_no_task_embed/   ← NEW (Part 2)
```

Each experiment folder has exactly this internal layout:
```
experiment_name/
├── code/        ← copy of code used for this run
├── runs/        ← best.pt, last.pt, history.json, config.json
├── plots/       ← all .png outputs
├── analysis/    ← eval scripts + result .json files
├── logs/        ← training_log.txt
└── README.md    ← one-page summary: idea, params, key results
```

---

### Step 1 — Create new top-level directories

```bash
cd /home/redafrix/tests/intern_ship_research/intern_ship_ws/tdqc/code/phase2_tdqc_standalone

mkdir -p core docs experiments data/v6/archive data/v7
```

---

### Step 2 — Move core library

```bash
cp -r code/phase2_tdqc core/
# Keep code/ in place too so nothing breaks — core/ is the clean canonical copy
```

---

### Step 3 — Organise data/

```bash
# v7 (current active dataset)
mv data/v7_11d_train.pt data/v7/
mv data/v7_11d_val.pt   data/v7/
mv data/v7_11d_test.pt  data/v7/

# v6 active files
mv data/final_calibrated_3924rollouts_v6.pt       data/v6/
mv data/final_calibrated_3924rollouts_v6_README.txt data/v6/
mv data/final_calibrated_3924rollouts_v6_delta.pt  data/v6/

# Everything else to v6/archive (old intermediate versions)
mv data/final_calibrated_3751rollouts.pt              data/v6/archive/
mv data/final_calibrated_3924rollouts_misaligned.pt   data/v6/archive/
mv data/final_calibrated_3924rollouts_v2.pt           data/v6/archive/
mv data/final_calibrated_3924rollouts_v3.pt           data/v6/archive/
mv data/final_calibrated_3924rollouts_v4.pt           data/v6/archive/
mv data/final_calibrated_3924rollouts_v5.pt           data/v6/archive/
mv data/final_calibrated_3924rollouts_v5_README.txt   data/v6/archive/
```

---

### Step 4 — Move docs

```bash
mv GEMINI_EXPERIMENT_PROMPTS.md     docs/
mv GEMINI_PROMPT_v7_combined134.md  docs/
mv GEMINI_PROMPT_v7_eval_and_v2.md  docs/
mv TDQC_IMPROVEMENT_PROPOSAL.md     docs/
mv README.md                        docs/
# eval_on_test_split.py is a loose script — move to docs/archive
mkdir -p docs/archive
mv eval_on_test_split.py            docs/archive/
```

---

### Step 5 — Rename and tidy experiments

```bash
cd experiments   # We are now inside experiments/

# Rename to match new convention
mv ../tests_trains/idea1              v6_idea1_mc_loss
mv ../tests_trains/idea2              v6_idea2_delta_features
mv ../tests_trains/idea3              v6_idea3_task_embed
mv ../tests_trains/idea4_capacity     v6_idea4_large_lstm
mv ../tests_trains/idea5_transformer  v6_idea5_transformer
mv ../tests_trains/combined_idea14    v6_combined_14
mv ../tests_trains/combined_idea134   v6_combined_134
mv ../tests_trains/combined_idea134_v7    v7_exp01_combined134
mv ../tests_trains/combined_idea134_v7_v2 v7_exp02_combined134_reg
mv ../tests_trains/combined_analysis.md   v6_combined_134/analysis/combined_analysis.md

# For each experiment, ensure the standard sub-folders exist
for exp in v6_idea1_mc_loss v6_idea2_delta_features v6_idea3_task_embed \
           v6_idea4_large_lstm v6_idea5_transformer v6_combined_14 \
           v6_combined_134 v7_exp01_combined134 v7_exp02_combined134_reg; do
    mkdir -p $exp/plots $exp/analysis $exp/logs
done

# Move training logs into logs/ subfolders
mv v6_combined_14/training_log_combined_idea14.txt    v6_combined_14/logs/training_log.txt
mv v6_combined_134/training_log_combined_idea134.txt  v6_combined_134/logs/training_log.txt
mv v7_exp01_combined134/training_log.txt              v7_exp01_combined134/logs/
mv v7_exp02_combined134_reg/training_log.txt          v7_exp02_combined134_reg/logs/

# Move training curve png that was in wrong place
mv v7_exp01_combined134/training_curve.png            v7_exp01_combined134/plots/

# Move eval/analysis scripts into analysis/ subfolders
for f in eval_best.py eval_full_analysis.py eval_stepwise_accuracy.py \
         make_trajectory_plot.py plot_training.py; do
    [ -f v7_exp01_combined134/$f ] && mv v7_exp01_combined134/$f v7_exp01_combined134/analysis/
done

# Move plots subfolder content into plots/
[ -d v7_exp01_combined134/plots/plots ] && mv v7_exp01_combined134/plots/plots/* v7_exp01_combined134/plots/ && rmdir v7_exp01_combined134/plots/plots

cd ..  # back to project root
```

---

### Step 6 — Move orphaned results/ and scripts/ into v6_combined_134

The files in `results/` and `scripts/` belong to the v6 era (baseline + ideas 1-5 combined analysis).
Move them into `experiments/v6_combined_134/`.

```bash
mkdir -p experiments/v6_combined_134/plots
mkdir -p experiments/v6_combined_134/analysis

# Plots
mv results/*.png          experiments/v6_combined_134/plots/ 2>/dev/null
mv results/plots/*.png    experiments/v6_combined_134/plots/ 2>/dev/null
mv results/general_analysis.md experiments/v6_combined_134/analysis/

# Old checkpoints — archive them inside the experiment
mkdir -p experiments/v6_combined_134/runs/archive
mv results/checkpoints/*  experiments/v6_combined_134/runs/archive/ 2>/dev/null

# Scripts
mv scripts/*.py  experiments/v6_combined_134/analysis/ 2>/dev/null

# Clean up now-empty dirs
rmdir results/checkpoints results/plots results scripts 2>/dev/null
```

---

### Step 7 — Create a baseline experiment folder for the original v6 run

```bash
mkdir -p experiments/v6_baseline/runs experiments/v6_baseline/plots \
         experiments/v6_baseline/analysis experiments/v6_baseline/logs
```

Write `experiments/v6_baseline/README.md`:
```markdown
# v6 Baseline

- **Dataset**: v6 (3924 episodes, 8D features, single .pt file)
- **Model**: LSTM 128 hidden / 1 layer, TD(0) loss, no task embedding
- **Best val Brier**: 0.1232
- **Test Brier**: 0.1497
- **Notes**: Original baseline from which all ideas were measured.
  Checkpoints archived in experiments/v6_combined_134/runs/archive/
```

---

### Step 8 — Write README.md for each major experiment

**`experiments/v7_exp01_combined134/README.md`**:
```markdown
# v7 Experiment 01 — Combined Ideas 1+3+4 (v7 dataset, first run)

**Ideas combined**: MC loss (1) + Task embedding (3) + 256/2L LSTM (4)
**Dataset**: v7 11D, 31537 train / 3942 val / 3942 test episodes
**Hyperparams**: dropout=0.05, weight_decay=0.01, epochs=500
**Best epoch**: 61 (early overfit — val kept worsening after epoch 61)
**Val Brier**: 0.037176 | **Test Brier**: 0.038560
**Test AUC-ROC**: 0.9967
**Early AUC @ step 20**: 0.884
**Stepwise accuracy @ step 10, τ=0.5**: 78.8%
**Status**: DONE. Overfit after epoch 61. See v7_exp02 for regularized version.
```

**`experiments/v7_exp02_combined134_reg/README.md`**:
```markdown
# v7 Experiment 02 — Combined Ideas 1+3+4 (regularized)

**Ideas combined**: MC loss (1) + Task embedding (3) + 256/2L LSTM (4)
**Dataset**: v7 11D, 31537 train / 3942 val / 3942 test episodes
**Hyperparams**: dropout=0.30, weight_decay=0.05, early_stop_patience=40
**Val Brier**: 0.037634 | **Test Brier**: 0.039086
**Status**: DONE. Slightly worse than exp01 best — more regularization reduced overfit
           but also capped peak performance. Eval pending (run eval scripts from exp01).
```

---

### Step 9 — Write WORKSPACE.md at the root

Write the following to `WORKSPACE.md`:

```markdown
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

PYTHONPATH=experiments/<name>/code \
python3 experiments/<name>/code/phase2_tdqc/train_tdqc.py \
    --train_path data/v7/v7_11d_train.pt \
    --val_path   data/v7/v7_11d_val.pt   \
    --test_path  data/v7/v7_11d_test.pt  \
    --output_dir experiments/<name>/runs/<name> \
    ... \
    2>&1 | tee experiments/<name>/logs/training_log.txt
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
```

---

## PART 2 — Experiment 03: No Task Embedding (Ablation)

### What and why

Experiment 01 combined three ideas: MC loss (1) + task embedding (3) + large LSTM (4).
We want to know: **does the task embedding actually help?**
This experiment keeps everything identical but removes the task embedding from the model.

If exp03 is worse than exp01 → task embedding is genuinely useful.
If exp03 matches exp01 → the embedding adds complexity without benefit and we should drop it.

### What changes vs exp01/exp02

| Component | exp01/exp02 | exp03 |
|---|---|---|
| MC loss | ✓ | ✓ |
| 256/2L LSTM | ✓ | ✓ |
| Task ID embedding | ✓ | **✗ removed** |
| dropout | 0.30 | 0.30 |
| weight_decay | 0.05 | 0.05 |
| early stopping | patience=40 | patience=40 |
| dataset | v7 11D | v7 11D |

---

### Step 1 — Create experiment directory

```bash
cd /home/redafrix/tests/intern_ship_research/intern_ship_ws/tdqc/code/phase2_tdqc_standalone

mkdir -p experiments/v7_exp03_no_task_embed/code
cp -r experiments/v7_exp02_combined134_reg/code/phase2_tdqc \
      experiments/v7_exp03_no_task_embed/code/
mkdir -p experiments/v7_exp03_no_task_embed/runs/v7_exp03_no_task_embed \
         experiments/v7_exp03_no_task_embed/plots \
         experiments/v7_exp03_no_task_embed/analysis \
         experiments/v7_exp03_no_task_embed/logs
```

---

### Step 2 — Remove task embedding from the model

Write the following to `experiments/v7_exp03_no_task_embed/code/phase2_tdqc/tdqc_model.py`:

```python
from __future__ import annotations

from typing import Optional, Tuple

import torch
import torch.nn as nn


class TDQCLSTMCalibrator(nn.Module):
    """LSTM TDQC calibrator — no task embedding (ablation of idea 3)."""

    def __init__(
        self,
        input_dim: int,
        hidden_dim: int = 256,
        num_layers: int = 2,
        dropout: float = 0.0,
    ):
        super().__init__()
        self.input_dim  = int(input_dim)
        self.hidden_dim = int(hidden_dim)
        self.num_layers = int(num_layers)

        self.input_proj = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(inplace=False),
        )

        self.rnn = nn.LSTM(
            input_size=hidden_dim,
            hidden_size=hidden_dim,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
        )

        self.head = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(inplace=False),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, 1),
        )

    def forward(
        self,
        x: torch.Tensor,
        lengths: Optional[torch.Tensor] = None,
        task_ids: Optional[torch.Tensor] = None,  # accepted but ignored
    ) -> torch.Tensor:
        z = self.input_proj(x)
        out, _ = self.rnn(z)
        logits = self.head(out).squeeze(-1)
        return torch.sigmoid(logits)

    @torch.no_grad()
    def step(
        self,
        phi_t: torch.Tensor,
        state: Optional[Tuple[torch.Tensor, torch.Tensor]] = None,
        task_id: Optional[torch.Tensor] = None,
    ):
        if phi_t.ndim == 1:
            phi_t = phi_t.unsqueeze(0)
        x = phi_t.unsqueeze(1)
        z = self.input_proj(x)
        out, new_state = self.rnn(z, state)
        p_fail = torch.sigmoid(self.head(out).squeeze(-1)).squeeze(1)
        return p_fail, new_state


def hard_update(target: nn.Module, source: nn.Module) -> None:
    target.load_state_dict(source.state_dict())
```

---

### Step 3 — Launch training

```bash
cd /home/redafrix/tests/intern_ship_research/intern_ship_ws/tdqc/code/phase2_tdqc_standalone

screen -S tdqc_exp03

PYTHONPATH=experiments/v7_exp03_no_task_embed/code \
python3 experiments/v7_exp03_no_task_embed/code/phase2_tdqc/train_tdqc.py \
    --train_path   data/v7/v7_11d_train.pt \
    --val_path     data/v7/v7_11d_val.pt   \
    --test_path    data/v7/v7_11d_test.pt  \
    --output_dir   experiments/v7_exp03_no_task_embed/runs/v7_exp03_no_task_embed \
    --hidden_dim   256   \
    --num_layers   2     \
    --dropout      0.30  \
    --batch_size   64    \
    --epochs       500   \
    --lr           1e-4  \
    --weight_decay 5e-2  \
    --lr_patience  20    \
    --early_stop_patience 40 \
    --device       cuda  \
    2>&1 | tee experiments/v7_exp03_no_task_embed/logs/training_log.txt
```

Detach: Ctrl+A, D. Monitor: `tail -f experiments/v7_exp03_no_task_embed/logs/training_log.txt`

---

### Step 4 — Full evaluation after training completes

Once training stops (early stopping will trigger), run this eval script.
Write it to `experiments/v7_exp03_no_task_embed/analysis/eval_full.py` and execute it:

```python
"""Full eval for v7_exp03_no_task_embed."""
import sys, torch, numpy as np, json, random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from torch.utils.data import DataLoader
from scipy.stats import gaussian_kde
from sklearn.metrics import roc_auc_score, roc_curve

ROOT     = Path(".")
EXP      = ROOT / "experiments/v7_exp03_no_task_embed"
sys.path.insert(0, str(EXP / "code"))

from phase2_tdqc.tdqc_dataset import TDQCDataset, tdqc_collate
from phase2_tdqc.tdqc_features import normalize_features
from phase2_tdqc.tdqc_model    import TDQCLSTMCalibrator
from phase2_tdqc.tdqc_losses   import sequential_brier_score

CKPT  = EXP / "runs/v7_exp03_no_task_embed/best.pt"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

ckpt  = torch.load(CKPT, map_location=device)
mean  = ckpt["mean"].to(device)
std   = ckpt["std"].to(device)
cfg   = ckpt["config"]
print(f"Best checkpoint: epoch={ckpt['epoch']}  val_brier={ckpt['val_seq_brier']:.6f}")

model = TDQCLSTMCalibrator(
    input_dim=cfg["input_dim"], hidden_dim=cfg["hidden_dim"],
    num_layers=cfg["num_layers"], dropout=cfg["dropout"],
).to(device)
model.load_state_dict(ckpt["model"])
model.eval()

test_set    = TDQCDataset(str(ROOT / "data/v7/v7_11d_test.pt"))
test_loader = DataLoader(test_set, batch_size=64, shuffle=False,
                         collate_fn=tdqc_collate, num_workers=2)

print("Running inference...")
trajs = []
with torch.no_grad():
    for batch in test_loader:
        batch = {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
        x = normalize_features(batch["features"], mean, std)
        q = model(x, batch["lengths"], task_ids=batch["task_ids"])
        for b in range(q.shape[0]):
            L   = int(batch["lengths"][b].item())
            lbl = int(batch["failure"][b].item())
            trajs.append((lbl, q[b, :L].cpu().numpy()))

fail_trajs    = [t for lbl, t in trajs if lbl == 1]
success_trajs = [t for lbl, t in trajs if lbl == 0]
labels = np.array([lbl for lbl, _ in trajs])
print(f"  failures={len(fail_trajs)}  successes={len(success_trajs)}")

# ── Sequential Brier (per-step, all episodes) ─────────────────────────────────
# Compute manually from trajs
all_sq_err = []
for lbl, traj in trajs:
    all_sq_err.extend(((traj - lbl)**2).tolist())
seq_brier = np.mean(all_sq_err)
print(f"\nTest Sequential Brier : {seq_brier:.6f}")

# ── Episode-level AUC-ROC (max p_fail per episode) ────────────────────────────
ep_max = np.array([t.max() for _, t in trajs])
auc_ep = roc_auc_score(labels, ep_max)
print(f"Test Episode AUC-ROC  : {auc_ep:.4f}")

# ── Stepwise accuracy (p_fail[t] at exactly step t) ──────────────────────────
STEPS      = list(range(10, 201, 10))
THRESHOLDS = [0.3, 0.4, 0.5, 0.6, 0.7]

print(f"\n{'Step':>5}", end="")
for tau in THRESHOLDS:
    print(f"  τ={tau:.1f}", end="")
print(f"  {'AUC':>6}  {'n':>5}")
print("─" * (5 + len(THRESHOLDS)*7 + 16))

step_results = []
for t in STEPS:
    idx    = t - 1
    preds  = {tau: [] for tau in THRESHOLDS}
    sliced = []
    labs_t = []
    for lbl, traj in trajs:
        if len(traj) <= idx:
            continue
        p = float(traj[idx])
        sliced.append(p)
        labs_t.append(lbl)
        for tau in THRESHOLDS:
            preds[tau].append(int((p >= tau) == lbl))
    auc_t = roc_auc_score(labs_t, sliced) if len(set(labs_t)) > 1 else float("nan")
    print(f"{t:>5}", end="")
    row = {"step": t, "auc": auc_t, "n": len(sliced)}
    for tau in THRESHOLDS:
        acc = np.mean(preds[tau]) if preds[tau] else float("nan")
        row[f"acc_{tau}"] = acc
        print(f"  {acc:.3f}", end="")
    print(f"  {auc_t:.4f}  {len(sliced):>5}")
    step_results.append(row)

# Save results
(EXP / "analysis/step_metrics.json").write_text(json.dumps(step_results, indent=2))

# ── Plot 1: Trajectory + threshold ────────────────────────────────────────────
MAX_T = 300
def step_mean_std(tl, max_t):
    ms, ss = [], []
    for t in range(max_t):
        v = [tr[t] for tr in tl if len(tr) > t]
        ms.append(np.mean(v) if v else np.nan)
        ss.append(np.std(v)  if v else np.nan)
    return np.array(ms), np.array(ss)

fm, fs = step_mean_std(fail_trajs,    MAX_T)
sm, ss_ = step_mean_std(success_trajs, MAX_T)
tx = np.arange(MAX_T)

fig, axes = plt.subplots(1, 2, figsize=(18, 7))
fig.suptitle("TDQC v7 Exp03 — No Task Embedding  (test set)", fontsize=13, fontweight="bold")

ax = axes[0]
random.seed(42)
for tr in random.sample(success_trajs, min(1200, len(success_trajs))):
    ax.plot(np.arange(len(tr)), tr, color="#3a86ff", alpha=0.018, linewidth=0.4)
for tr in random.sample(fail_trajs, min(1200, len(fail_trajs))):
    ax.plot(np.arange(len(tr)), tr, color="#e63946", alpha=0.018, linewidth=0.4)
vf = ~np.isnan(fm);  vs = ~np.isnan(sm)
ax.fill_between(tx[vs], np.clip(sm[vs]-ss_[vs],0,1), np.clip(sm[vs]+ss_[vs],0,1), color="#3a86ff", alpha=0.12)
ax.fill_between(tx[vf], np.clip(fm[vf]-fs[vf],0,1), np.clip(fm[vf]+fs[vf],0,1), color="#e63946", alpha=0.12)
ax.plot(tx[vs], sm[vs], color="#3a86ff", linewidth=2.5, label=f"Success mean (n={len(success_trajs)})")
ax.plot(tx[vf], fm[vf], color="#e63946", linewidth=2.5, label=f"Failure mean (n={len(fail_trajs)})")
ax.axhline(0.5, color="#2dc653", linewidth=2.0, linestyle="--", label="τ=0.5")
ax.axhline(0.3, color="#ffd166", linewidth=1.2, linestyle=":",  label="τ=0.3")
ax.axhline(0.7, color="#ef476f", linewidth=1.2, linestyle=":",  label="τ=0.7")
ax.set_xlim(0, MAX_T); ax.set_ylim(-0.02, 1.02)
ax.set_xlabel("Step"); ax.set_ylabel("p_fail")
ax.set_title("Trajectories + mean ± 1σ"); ax.legend(fontsize=9); ax.grid(True, alpha=0.18)

ax2 = axes[1]
x_grid = np.linspace(0, 1, 400)
FCOLS = ["#d00000","#e85d04","#9d0208","#6a040f","#370617"]
SCOLS = ["#0077b6","#00b4d8","#023e8a","#48cae4","#0096c7"]
for i, N in enumerate([10, 20, 50, 100, 200]):
    idx = N - 1
    fv = np.array([tr[idx] for tr in fail_trajs    if len(tr) > idx])
    sv = np.array([tr[idx] for tr in success_trajs if len(tr) > idx])
    for vals, col, ls, lbl in [(fv, FCOLS[i], "-", f"Fail step={N}"), (sv, SCOLS[i], "--", f"Succ step={N}")]:
        if vals.std() > 1e-4:
            y = gaussian_kde(vals, bw_method=0.12)(x_grid)
            y = y / y.max() * 0.9
            ax2.fill_between(x_grid, y, alpha=0.18, color=col)
            ax2.plot(x_grid, y, color=col, linewidth=1.6, linestyle=ls, label=lbl)
ax2.axvline(0.5, color="#2dc653", linewidth=2.5, linestyle="--", label="τ=0.5")
ax2.set_xlim(0, 1); ax2.set_xlabel("p_fail[t] at exactly step t")
ax2.set_ylabel("Normalised KDE"); ax2.set_title("Distribution at fixed steps\n(solid=failure, dashed=success)")
ax2.legend(fontsize=8, ncol=2); ax2.grid(True, alpha=0.18)

plt.tight_layout()
plt.savefig(str(EXP / "plots/trajectory_and_threshold.png"), dpi=160, bbox_inches="tight")
print("Saved trajectory plot.")

# ── Plot 2: Stepwise accuracy ─────────────────────────────────────────────────
COLORS = {0.3:"#ff7f00", 0.4:"#f0c000", 0.5:"#4daf4a", 0.6:"#377eb8", 0.7:"#984ea3"}
fig2, axes2 = plt.subplots(1, 2, figsize=(16, 6))
fig2.suptitle("TDQC v7 Exp03 — Per-step accuracy at fixed thresholds", fontsize=13)
ax3 = axes2[0]
for tau in THRESHOLDS:
    accs = [r[f"acc_{tau}"] for r in step_results]
    ax3.plot(STEPS, accs, color=COLORS[tau], linewidth=2, marker="o", markersize=4, label=f"τ={tau}")
ax3.axhline(len(success_trajs)/len(trajs), color="black", linewidth=1.2, linestyle="--", label="Naive baseline")
ax3.set_xlabel("Step"); ax3.set_ylabel("Accuracy"); ax3.legend(fontsize=9)
ax3.set_title("Accuracy at step t (p_fail[t] exactly)"); ax3.grid(True, alpha=0.25)
ax3.set_xlim(5, 205); ax3.set_ylim(0.5, 1.01)

ax4 = axes2[1]
aucs = [r["auc"] for r in step_results]
ax4.plot(STEPS, aucs, color="#e63946", linewidth=2.5, marker="o", markersize=5, label="AUC-ROC at step t")
ax4.axhline(0.5, color="gray", linewidth=0.8, linestyle=":")
ax4.set_xlabel("Step"); ax4.set_ylabel("AUC-ROC")
ax4.set_title("AUC-ROC at exactly step t"); ax4.legend(); ax4.grid(True, alpha=0.25)
ax4.set_xlim(5, 205); ax4.set_ylim(0.4, 1.01)

plt.tight_layout()
plt.savefig(str(EXP / "plots/stepwise_accuracy.png"), dpi=160, bbox_inches="tight")
print("Saved stepwise accuracy plot.")

# ── Plot 3: Training curve ─────────────────────────────────────────────────────
history = json.loads((EXP / "runs/v7_exp03_no_task_embed/history.json").read_text())
epochs   = [h["epoch"]        for h in history]
tr_loss  = [h["train_loss"]   for h in history]
vl_brier = [h["val_seq_brier"] for h in history]
best_ep  = min(range(len(vl_brier)), key=lambda i: vl_brier[i])

fig3, ax5 = plt.subplots(figsize=(12, 5))
ax5.plot(epochs, tr_loss,  color="steelblue", linewidth=1.4, label="Train loss")
ax5.plot(epochs, vl_brier, color="tomato",    linewidth=1.4, label="Val seq Brier")
ax5.axvline(epochs[best_ep], color="green", linestyle="--", linewidth=1.2,
            label=f"Best: epoch {epochs[best_ep]}, val={vl_brier[best_ep]:.4f}")
ax5.fill_between(epochs, tr_loss, vl_brier,
                 where=[v > t for v, t in zip(vl_brier, tr_loss)],
                 alpha=0.12, color="red", label="Overfit gap")
ax5.set_xlabel("Epoch"); ax5.set_ylabel("Loss / Brier")
ax5.set_title("v7 Exp03 — Training curve (no task embedding)")
ax5.legend(); ax5.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(str(EXP / "plots/training_curve.png"), dpi=150, bbox_inches="tight")
print("Saved training curve.")

# ── Summary ───────────────────────────────────────────────────────────────────
print(f"\n{'='*55}")
print(f"SUMMARY — v7_exp03_no_task_embed")
print(f"{'='*55}")
print(f"Best epoch        : {ckpt['epoch']}")
print(f"Val Brier (best)  : {ckpt['val_seq_brier']:.6f}")
print(f"Test seq Brier    : {seq_brier:.6f}")
print(f"Test AUC-ROC      : {auc_ep:.4f}")
print(f"Acc @ step10, τ=0.5 : {step_results[0]['acc_0.5']:.3f}")
print(f"Acc @ step20, τ=0.5 : {step_results[1]['acc_0.5']:.3f}")
print(f"Acc @ step50, τ=0.5 : {step_results[4]['acc_0.5']:.3f}")
print(f"{'='*55}")
print("\nAll plots saved to experiments/v7_exp03_no_task_embed/plots/")
```

Run it:
```bash
cd /home/redafrix/tests/intern_ship_research/intern_ship_ws/tdqc/code/phase2_tdqc_standalone
python3 experiments/v7_exp03_no_task_embed/analysis/eval_full.py 2>&1 | tee experiments/v7_exp03_no_task_embed/analysis/eval_results.txt
```

---

### Step 5 — Write README.md after eval

Once eval finishes, write `experiments/v7_exp03_no_task_embed/README.md` filling in the actual numbers from the eval summary output.

Template:
```markdown
# v7 Experiment 03 — No Task Embedding (Ablation of Idea 3)

**Ablation**: Removed task ID embedding vs exp01/exp02
**Dataset**: v7 11D, 31537 train / 3942 val / 3942 test
**Model**: 256/2L LSTM, MC loss, NO task embedding
**Hyperparams**: dropout=0.30, weight_decay=0.05, early_stop=40
**Best epoch**: ???
**Val Brier**: ??? | **Test Brier**: ???
**Test AUC-ROC**: ???
**Stepwise acc @ step10, τ=0.5**: ???

**Comparison vs exp01 (with task embed)**:
- exp01: val=0.037176, test=0.038560, AUC=0.9967, step10=78.8%
- exp03: val=???,      test=???,      AUC=???,    step10=???

**Conclusion**: task embedding [helps / does not help / ???]
```

---

## Reference: Current experiment results

| Experiment | Dataset | Val Brier | Test Brier | AUC-ROC | step10 acc |
|---|---|---|---|---|---|
| v6_baseline | v6 8D | 0.1232 | 0.1497 | — | — |
| v6_combined_134 | v6 8D | 0.0899 | 0.0932 | 0.9805 | — |
| v7_exp01_combined134 | v7 11D | **0.0372** | **0.0386** | **0.9967** | **78.8%** |
| v7_exp02_combined134_reg | v7 11D | 0.0376 | 0.0391 | — | — |
| v7_exp03_no_task_embed | v7 11D | ??? | ??? | ??? | ??? |

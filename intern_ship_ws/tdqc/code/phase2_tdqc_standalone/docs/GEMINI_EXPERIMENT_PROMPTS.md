# TDQC Improvement Experiment Prompts

Working directory for all experiments:
`intern_ship_ws/tdqc/code/phase2_tdqc_standalone/`

Base dataset (8D, v6):
`data/final_calibrated_3924rollouts_v6.pt`

Delta dataset (16D, idea 2):
`data/final_calibrated_3924rollouts_v6_delta.pt`

---

## Idea 1 — Monte Carlo targets (terminal label at every step)

**What to run:**
```
python3 code/phase2_tdqc/train_tdqc.py \
  --dataset_path data/final_calibrated_3924rollouts_v6.pt \
  --output_dir runs/idea1_mc_targets \
  --hidden_dim 128 --num_layers 1 --dropout 0.05 \
  --epochs 200 --lr 1e-4 --batch_size 64
```

**But first, modify `code/phase2_tdqc/train_tdqc.py` to switch from TD(0) to Monte Carlo targets.**

---

**Gemini prompt:**

```
You are modifying a PyTorch LSTM training script for TDQC (Temporal Difference Q-Calibrator),
a sequential failure predictor for robot manipulation episodes.

CONTEXT:
- The model reads uncertainty feature sequences [B, T, 8] and outputs p_fail [B, T]
- Currently uses TD(0) loss: target[t] = q_target[t+1] for t < T-1, target[T-1] = failure[b]
  This requires a separate frozen "target network" that gets hard-updated every 100 steps.
- Validation uses "sequential Brier score": compare p_fail[t] vs terminal failure label at
  every step (all steps, not just the last)
- Dataset: 3924 robot episodes, 8D per-step features, 57.4% success / 42.6% failure

TASK:
Replace TD(0) with Monte Carlo targets (terminal labels) in the training loss.

The change is: every step's target is the episode's final outcome — failure[b] for every t,
instead of bootstrapping from the next step's prediction. This is supervised learning with
the terminal label broadcast to all steps, identical to what the validation metric already does.

SPECIFIC CHANGES:

1. In `code/phase2_tdqc/tdqc_losses.py`:
   Add a new function `tdqc_brier_mc_loss` that:
   - Takes q_online [B,T], failure [B], mask [B,T], fail_weight, success_weight
   - Targets: terminal = failure[:, None].expand_as(q_online)   # same label at all steps
   - Applies class weights per sample (same as the existing TD loss)
   - Returns weighted masked Brier loss (same formula as existing, different target)
   - Does NOT need q_target or target_model at all

2. In `code/phase2_tdqc/train_tdqc.py`:
   - Import `tdqc_brier_mc_loss` from tdqc_losses
   - Remove target_model initialization, hard_update calls, and target_update_freq logic
     (no target network needed for Monte Carlo)
   - In the training loop, replace the `tdqc_brier_td_loss(...)` call with `tdqc_brier_mc_loss(...)`
   - Remove the `q_target = target_model(x, ...)` inference step
   - Keep everything else identical: optimizer, scheduler, normalization, evaluation, checkpointing

Do NOT change the model architecture, dataset loading, validation metric (sequential Brier),
or any command-line argument interface. The output_dir, checkpointing, and history.json format
must remain the same so results are comparable.

Files to modify:
  code/phase2_tdqc/tdqc_losses.py
  code/phase2_tdqc/train_tdqc.py

After modifying, run:
  python3 code/phase2_tdqc/train_tdqc.py \
    --dataset_path data/final_calibrated_3924rollouts_v6.pt \
    --output_dir runs/idea1_mc_targets \
    --hidden_dim 128 --num_layers 1 --dropout 0.05 \
    --epochs 200 --lr 1e-4 --batch_size 64 --device cuda

Report best val_seq_brier achieved and the epoch it occurred at.
```

---

## Idea 2 — Delta features (16D: levels + per-step differences)

**Dataset:** `data/final_calibrated_3924rollouts_v6_delta.pt`
- 16D = [f0..f7] + [Δf0..Δf7] where Δf_t = f_t - f_{t-1}, Δf_0 = 0
- 3924 episodes, same structure as v6 but input_dim=16

**Gemini prompt:**

```
You are running a TDQC (Temporal Difference Q-Calibrator) experiment with a 16D feature dataset.

CONTEXT:
- Standard TDQC: LSTM reads 8D uncertainty features per step, outputs p_fail [B,T]
- TD(0) loss with target network (hard update every 100 steps)
- AdamW optimizer, ReduceLROnPlateau scheduler, class-weighted Brier loss
- Dataset has 3924 robot manipulation episodes
- The model input_dim is read automatically from dataset.input_dim

TASK:
Run training with the delta-features dataset (16D input). The dataset already exists at
`data/final_calibrated_3924rollouts_v6_delta.pt`.

Feature layout of this dataset:
  [0-7]   Same as v6: mean_path, mean_last, std_path, std_last, max_path, max_last, gripper_path, gripper_last
  [8-15]  Per-step deltas: Δf_t = f_t - f_{t-1} for each of the 8 base features (Δf_0 = 0)

The model's input_proj layer already uses dataset.input_dim at construction time, so it will
automatically expand to 16 inputs. No code changes needed.

Run:
  python3 code/phase2_tdqc/train_tdqc.py \
    --dataset_path data/final_calibrated_3924rollouts_v6_delta.pt \
    --output_dir runs/idea2_delta_features \
    --hidden_dim 128 --num_layers 1 --dropout 0.05 \
    --epochs 200 --lr 1e-4 --batch_size 64 --device cuda

Report:
- best val_seq_brier and the epoch it occurred at
- Compare to baseline v6 result (best val_seq_brier from runs/lstm_td0_final_stretch/best.pt)
- Note whether delta features helped or hurt
```

---

## Idea 3 — Task ID conditioning (per-task embedding)

**Dataset:** `data/final_calibrated_3924rollouts_v6.pt` (8D, same as baseline)
- task_id is already stored in each episode (10 unique integer IDs)

**Gemini prompt:**

```
You are modifying the TDQC LSTM model to condition on task identity via a learned embedding.

CONTEXT:
- TDQCLSTMCalibrator: input_proj (Linear→LayerNorm→ReLU) → LSTM → head (→ p_fail)
- Each episode has a task_id (int, 10 unique values in dataset)
- Dataset already stores task_id per episode; collate batch already exposes it
- 3924 episodes across 10 LIBERO tasks (spatial/object/goal/libero_10 suites)
- Goal: let the model know which task is running so it can calibrate differently per-task

TASK:
Add a task embedding to the model and train. The embedding is looked up once per episode
and added to every timestep's projection before the LSTM.

SPECIFIC CHANGES:

1. In `code/phase2_tdqc/tdqc_model.py`:
   Add to TDQCLSTMCalibrator.__init__:
     self.task_embed = nn.Embedding(num_embeddings=20, embedding_dim=hidden_dim)
     # 20 gives headroom; actual IDs are 0-9 in this dataset
   
   In forward(self, x, lengths=None, task_ids=None):
     z = self.input_proj(x)   # [B, T, H]
     if task_ids is not None:
         te = self.task_embed(task_ids)  # [B, H]
         z = z + te.unsqueeze(1)         # broadcast over T
     out, _ = self.rnn(z)
     ...
   
   In step(self, phi_t, state=None, task_id=None):
     # same pattern: add task embedding to z before rnn step
     z = self.input_proj(x)
     if task_id is not None:
         te = self.task_embed(task_id.unsqueeze(0) if task_id.ndim == 0 else task_id)
         z = z + te.unsqueeze(1)
     out, new_state = self.rnn(z, state)
     ...

2. In `code/phase2_tdqc/tdqc_dataset.py` — check TDQCDataset and tdqc_collate:
   The episode dict has task_id (int). The collate function must include it as a
   tensor in the batch: batch["task_ids"] = torch.tensor([ep.task_id for ep in batch_list])
   If it's already there, no change needed. If not, add it.

3. In `code/phase2_tdqc/train_tdqc.py`:
   - When constructing the model, pass nothing extra (task_embed is inside the model already)
   - In the training loop, pass task_ids to model and target_model:
       q_online = model(x, batch["lengths"], task_ids=batch["task_ids"].to(device))
       q_target = target_model(x, batch["lengths"], task_ids=batch["task_ids"].to(device))
   - Same for the evaluate() function

Do NOT change the loss, optimizer, scheduler, or anything else.

Run:
  python3 code/phase2_tdqc/train_tdqc.py \
    --dataset_path data/final_calibrated_3924rollouts_v6.pt \
    --output_dir runs/idea3_task_embed \
    --hidden_dim 128 --num_layers 1 --dropout 0.05 \
    --epochs 200 --lr 1e-4 --batch_size 64 --device cuda

Report best val_seq_brier and epoch.
```

---

## hidden_dim=256, num_layers=2 (larger LSTM)

**Dataset:** `data/final_calibrated_3924rollouts_v6.pt` (8D, baseline)
No code changes needed — just different CLI args.

**Gemini prompt:**

```
You are running a TDQC capacity experiment: larger LSTM (hidden_dim=256, 2 layers).

CONTEXT:
- Baseline TDQC: hidden_dim=128, num_layers=1, dropout=0.05
- All other settings identical: TD(0) loss, target network, AdamW, ReduceLROnPlateau
- Dataset: data/final_calibrated_3924rollouts_v6.pt (3924 episodes, 8D features)

TASK:
Run training with increased capacity. No code changes needed.

Run:
  python3 code/phase2_tdqc/train_tdqc.py \
    --dataset_path data/final_calibrated_3924rollouts_v6.pt \
    --output_dir runs/idea_lstm_256_2layer \
    --hidden_dim 256 --num_layers 2 --dropout 0.1 \
    --epochs 200 --lr 1e-4 --batch_size 64 --device cuda

Notes:
- Dropout raised to 0.1 because more capacity = more regularization needed
- With 2 LSTM layers, inter-layer dropout activates automatically (PyTorch applies
  dropout between layers when num_layers > 1)

Report best val_seq_brier, epoch, and whether the curve shows overfitting
(rising val_seq_brier while train_loss falls).
```

---

## Idea 5 — Causal Transformer (replace LSTM)

**Dataset:** `data/final_calibrated_3924rollouts_v6.pt` (8D, baseline)

**Gemini prompt:**

```
You are replacing the LSTM in TDQC with a causal Transformer encoder.

CONTEXT:
- TDQCLSTMCalibrator: input_proj (Linear→LayerNorm→ReLU) → LSTM → head → sigmoid → p_fail [B,T]
- step() method does stateful single-step inference (used at deployment time)
- The rest of the training pipeline (loss, optimizer, scheduler, dataset) stays identical
- 3924 episodes, variable-length sequences, padded to max T in batch, mask [B,T] removes padding

TASK:
Create a new model class TDQCTransformerCalibrator with the same API and drop it into
the existing training script.

SPECIFIC CHANGES:

1. In `code/phase2_tdqc/tdqc_model.py`, add:

```python
class TDQCTransformerCalibrator(nn.Module):
    """
    Causal Transformer TDQC calibrator.
    Same input/output API as TDQCLSTMCalibrator.
    """
    def __init__(self, input_dim, hidden_dim=128, num_layers=2, dropout=0.1, nhead=4):
        super().__init__()
        self.input_proj = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(inplace=False),
        )
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=hidden_dim,
            nhead=nhead,
            dim_feedforward=hidden_dim * 4,
            dropout=dropout,
            batch_first=True,
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.head = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(inplace=False),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, 1),
        )

    def _causal_mask(self, T, device):
        # Upper-triangular mask: position t can only attend to positions <= t
        return torch.triu(torch.ones(T, T, device=device, dtype=torch.bool), diagonal=1)

    def forward(self, x, lengths=None):
        # x: [B, T, F]
        B, T, _ = x.shape
        z = self.input_proj(x)  # [B, T, H]
        mask = self._causal_mask(T, x.device)  # [T, T]
        # key_padding_mask: True = ignore (padding positions)
        if lengths is not None:
            kpm = torch.arange(T, device=x.device).unsqueeze(0) >= lengths.unsqueeze(1)
        else:
            kpm = None
        out = self.transformer(z, mask=mask, src_key_padding_mask=kpm)
        logits = self.head(out).squeeze(-1)  # [B, T]
        return torch.sigmoid(logits)

    @torch.no_grad()
    def step(self, phi_t, state=None):
        """
        Stateful online inference. State = list of past projected features [cache].
        phi_t: [F] or [B, F]
        Returns: p_fail_t, new_state
        """
        if phi_t.ndim == 1:
            phi_t = phi_t.unsqueeze(0)  # [1, F]
        z_t = self.input_proj(phi_t.unsqueeze(1))  # [1, 1, H]
        if state is None:
            cache = z_t
        else:
            cache = torch.cat([state, z_t], dim=1)  # [1, t+1, H]
        T = cache.shape[1]
        mask = self._causal_mask(T, phi_t.device)
        out = self.transformer(cache, mask=mask)  # [1, t+1, H]
        last_out = out[:, -1, :]  # [1, H] — current step only
        p_fail = torch.sigmoid(self.head(last_out).squeeze(-1))
        return p_fail.squeeze(0), cache
```

2. In `code/phase2_tdqc/train_tdqc.py`:
   - Import TDQCTransformerCalibrator
   - Add CLI arg: `--model_type` with choices ["lstm", "transformer"], default "lstm"
   - In model construction, branch on args.model_type:
     ```python
     if args.model_type == "transformer":
         model = TDQCTransformerCalibrator(
             input_dim=dataset.input_dim,
             hidden_dim=args.hidden_dim,
             num_layers=args.num_layers,
             dropout=args.dropout,
         )
     else:
         model = TDQCLSTMCalibrator(...)
     ```
   - Same for target_model construction
   - Everything else (loss, optimizer, checkpointing) stays identical

Do NOT change loss, dataset, evaluation, or checkpoint format.

Run:
  python3 code/phase2_tdqc/train_tdqc.py \
    --dataset_path data/final_calibrated_3924rollouts_v6.pt \
    --output_dir runs/idea5_transformer \
    --model_type transformer \
    --hidden_dim 128 --num_layers 2 --dropout 0.1 \
    --epochs 200 --lr 3e-4 --batch_size 64 --device cuda

Notes:
- lr=3e-4 is typical for transformers (vs 1e-4 for LSTM)
- num_layers=2 because a 1-layer transformer is underpowered
- The causal mask ensures position t only sees positions 0..t (same causality as LSTM)
- Online step() uses a KV-cache (growing context tensor) — O(T) memory per step

Report best val_seq_brier, epoch, and training stability (does loss diverge early?).
```

---

## Idea 7 — Silver Bullet: action means + robot state as features

**Status: IMPOSSIBLE from existing data. Do not attempt.**

**Explanation:**

The raw JSONL (`combined_all_suites_all_seeds.jsonl`) stores only uncertainty statistics
per plan-prediction step. The fields per step are:

```
env_step, plan_step_idx,
path_step_mean, last_step_mean,       ← these are mean(path_variance), not action values
path_variance[7], last_step_variance[7],
mean_path_var, mean_last_var, max_path_var, max_last_var
```

There are NO actual action means (the μ of the denoised action chunk), NO joint positions,
NO robot proprioception, NO gripper state, NO object positions.

`path_step_mean` sounds like action mean but is actually `mean(path_variance)` —
the average of the 7-dimensional variance array, not the predicted action itself.

To implement idea 7, a new data collection run is required where SmolVLA's data logger
is modified to also save:
  - `action_mean[H, 7]`: the predicted action chunk (mean of denoised distribution)
  - `proprio[D]`: the robot's proprioceptive state at each plan step

This requires re-running SmolVLA with `predict_uncertainty=True` AND a modified logger.
The existing 3924 episodes cannot be augmented retroactively.

---

## Quick reference — all runs

| Experiment            | Dataset       | Key change              | Output dir                |
|-----------------------|---------------|-------------------------|---------------------------|
| Baseline (existing)   | v6 (8D)       | —                       | runs/lstm_td0_final_stretch|
| Idea 1: MC targets    | v6 (8D)       | TD(0) → terminal labels | runs/idea1_mc_targets     |
| Idea 2: delta feats   | v6_delta (16D)| input_dim=16            | runs/idea2_delta_features |
| Idea 3: task embed    | v6 (8D)       | +Embedding(20, H)       | runs/idea3_task_embed     |
| hidden=256/layers=2   | v6 (8D)       | capacity                | runs/idea_lstm_256_2layer |
| Idea 5: Transformer   | v6 (8D)       | LSTM→Transformer        | runs/idea5_transformer    |
| Idea 7               | —             | IMPOSSIBLE (no raw data)| —                         |

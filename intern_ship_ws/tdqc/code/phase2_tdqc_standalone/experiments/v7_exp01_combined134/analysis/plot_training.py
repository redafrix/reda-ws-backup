"""Plot training history for combined_idea134_v7 — shows overfitting."""
import json, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HISTORY_PATH = "tests_trains/combined_idea134_v7/runs/combined_idea134_v7/history.json"
OUT_PATH     = "tests_trains/combined_idea134_v7/training_curve.png"

history = json.load(open(HISTORY_PATH))
epochs     = [h["epoch"] for h in history]
train_loss = [h["train_loss"] for h in history]
val_brier  = [h["val_seq_brier"] for h in history]

best_epoch = min(range(len(val_brier)), key=lambda i: val_brier[i])
best_val   = val_brier[best_epoch]

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(epochs, train_loss, label="Train loss", color="steelblue", linewidth=1.2)
ax.plot(epochs, val_brier,  label="Val seq Brier", color="tomato", linewidth=1.2)
ax.axvline(epochs[best_epoch], color="green", linestyle="--", linewidth=1,
           label=f"Best: epoch {epochs[best_epoch]}, val={best_val:.4f}")
ax.fill_between(epochs, train_loss, val_brier,
                where=[v > t for v, t in zip(val_brier, train_loss)],
                alpha=0.15, color="red", label="Overfit gap")
ax.set_xlabel("Epoch")
ax.set_ylabel("Loss / Brier")
ax.set_title("combined_idea134_v7 — Overfitting (dropout=0.05, wd=0.01)")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(OUT_PATH, dpi=150)
print(f"Saved → {OUT_PATH}")

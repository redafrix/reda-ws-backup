import json
import matplotlib.pyplot as plt
import os

# Load history data
def load_history(path):
    with open(path, 'r') as f:
        return json.load(f)

exp08_hist = load_history('/media/redafrix/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v8_exp08_balanced/runs/history.json')
exp10_hist = load_history('/media/redafrix/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v8_exp10_33d/runs/history.json')
exp11_hist = load_history('/media/redafrix/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v8_exp11_transformer/outputs_v2/history.json')

# Plot Validation Sequential Brier Score
plt.figure(figsize=(10, 6))
plt.plot([h['epoch'] for h in exp08_hist], [h['val_seq_brier'] for h in exp08_hist], label='Exp 08 (LSTM, 22D)', alpha=0.7)
plt.plot([h['epoch'] for h in exp10_hist], [h['val_seq_brier'] for h in exp10_hist], label='Exp 10 (LSTM, 33D)', alpha=0.7)
plt.plot([h['epoch'] for h in exp11_hist], [h['val_seq_brier'] for h in exp11_hist], label='Exp 11 (Transformer, 22D)', linewidth=2.5)

plt.xlabel('Epoch')
plt.ylabel('Val Seq Brier Score')
plt.title('TDQC Evolution: LSTM vs. Causal Transformer')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.yscale('log')
plt.tight_layout()

output_path = '/media/redafrix/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v8_exp11_transformer/outputs_v2/comparison_plot.png'
plt.savefig(output_path)
print(f"Plot saved to {output_path}")

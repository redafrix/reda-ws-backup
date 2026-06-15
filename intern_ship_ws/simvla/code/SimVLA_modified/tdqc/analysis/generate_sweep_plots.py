import re
import matplotlib.pyplot as plt
import os
from pathlib import Path

# Dynamic paths
WS_ROOT = Path(__file__).parents[2]

def parse_log(file_path):
    steps, losses, vars, mses = [], [], [], []
    pattern = re.compile(r"\[(\d+)/\d+\] loss=([-0-9.]+) var=([-0-9.]+) mse=([-0-9.]+)")
    
    if not os.path.exists(file_path):
        return None
        
    with open(file_path, "r") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                steps.append(int(match.group(1)))
                losses.append(float(match.group(2)))
                vars.append(float(match.group(3)))
                mses.append(float(match.group(4)))
    return {"steps": steps, "loss": losses, "var": vars, "mse": mses}

runs = [
    {"lr": "5e-5", "path": WS_ROOT / "outputs/runs/sweep_test_1_lr_5e-5/train_smolvlm.log"},
    {"lr": "8e-5", "path": WS_ROOT / "outputs/runs/sweep_test_2_lr_8e-5/train_smolvlm.log"},
    {"lr": "1e-4", "path": WS_ROOT / "outputs/runs/sweep_test_3_lr_1e-4/train_smolvlm.log"},
]

output_dir = WS_ROOT / "outputs/plots/sweep_plots"
os.makedirs(output_dir, exist_ok=True)

for run in runs:
    data = parse_log(run["path"])
    if not data or not data["steps"]:
        print(f"Skipping {run['lr']}, log not found or empty.")
        continue
        
    plt.figure(figsize=(10, 6))
    plt.plot(data["steps"], data["loss"], label="Total Loss", color="blue", linewidth=1.5)
    plt.plot(data["steps"], data["var"], label="Mean Variance (Uncertainty)", color="green", linestyle="--")
    plt.plot(data["steps"], data["mse"], label="MSE Proxy (Accuracy)", color="red", linestyle=":")
    
    plt.title(f"SimVLA Uncertainty Sweep - Learning Rate: {run['lr']}")
    plt.xlabel("Training Steps")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    save_path = os.path.join(output_dir, f"sweep_plot_lr_{run['lr']}.png")
    plt.savefig(save_path)
    plt.close()
    print(f"Generated plot: {save_path}")

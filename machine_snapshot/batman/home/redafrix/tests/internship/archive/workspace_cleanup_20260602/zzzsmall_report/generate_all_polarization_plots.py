import torch
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.stats import gaussian_kde

# Setup output directories
output_dir = '/home/redafrix/tests/internship/zzzsmall_report/detailed_plots'
artifacts_dir = '/home/redafrix/.gemini/antigravity/brain/1e440ef5-bc4f-4d8c-af3a-116da6c55bae/artifacts'
os.makedirs(output_dir, exist_ok=True)
os.makedirs(artifacts_dir, exist_ok=True)

# Set global matplotlib style for high-end aesthetics
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Liberation Sans']
plt.rcParams['text.color'] = '#2b2b2b'
plt.rcParams['axes.labelcolor'] = '#2b2b2b'
plt.rcParams['xtick.color'] = '#2b2b2b'
plt.rcParams['ytick.color'] = '#2b2b2b'
plt.rcParams['grid.color'] = '#e0e0e0'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.linewidth'] = 0.5

def plot_polarization_panels(model_name, id_data, ood_data, file_name):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))
    
    # 1. In-Distribution (Left)
    plot_single_panel(ax1, id_data, "In-Distribution (ID)")
    
    # 2. Out-of-Distribution (Right)
    plot_single_panel(ax2, ood_data, "Out-of-Distribution (OOD)")
    
    # Global Title
    fig.suptitle(f"Prediction Confidence Polarization: {model_name}\nChecking Separation and Decision Boundary (τ = 0.5)", 
                 fontsize=14, fontweight='bold', y=0.98)
    plt.tight_layout()
    
    # Save both locally and in artifacts
    local_path = os.path.join(output_dir, file_name)
    artifact_path = os.path.join(artifacts_dir, file_name)
    plt.savefig(local_path, dpi=200)
    plt.savefig(artifact_path, dpi=200)
    plt.close()
    print(f"Generated and saved: {file_name}")

def plot_single_panel(ax, data, title):
    probs = np.array(data["probs"])
    targets = np.array(data["targets"])
    
    success_probs = probs[targets == 0]
    failure_probs = probs[targets == 1]
    
    # Plot histograms
    bins = np.linspace(0, 1, 40)
    ax.hist(success_probs, bins=bins, density=True, alpha=0.4, color='#1D3557', label='Actual Successes', edgecolor='none')
    ax.hist(failure_probs, bins=bins, density=True, alpha=0.4, color='#E63946', label='Actual Failures', edgecolor='none')
    
    # Add smooth KDE curve if possible
    x = np.linspace(0, 1, 500)
    if len(success_probs) > 1 and np.var(success_probs) > 1e-8:
        try:
            kde_s = gaussian_kde(success_probs)
            ax.plot(x, kde_s(x), color='#1D3557', linewidth=2)
        except Exception:
            pass
            
    if len(failure_probs) > 1 and np.var(failure_probs) > 1e-8:
        try:
            kde_f = gaussian_kde(failure_probs)
            ax.plot(x, kde_f(x), color='#E63946', linewidth=2)
        except Exception:
            pass
            
    ax.axvline(0.5, color='#2b2b2b', linestyle='--', linewidth=1.5, label='Threshold (τ = 0.5)')
    
    # Annotate metrics
    preds = (probs > 0.5).astype(int)
    acc = np.mean(preds == targets)
    tp = np.sum((preds == 1) & (targets == 1))
    fn = np.sum((preds == 0) & (targets == 1))
    fp = np.sum((preds == 1) & (targets == 0))
    tn = np.sum((preds == 0) & (targets == 0))
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0.0
    
    textstr = '\n'.join((
        f'Accuracy: {acc:.2%}',
        f'Recall: {recall:.2%}',
        f'FPR: {fpr:.2%}',
        f'N_succ: {len(success_probs)}',
        f'N_fail: {len(failure_probs)}'
    ))
    
    # place a text box in upper center
    props = dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='#e0e0e0')
    ax.text(0.5, 0.95, textstr, transform=ax.transAxes, fontsize=9.5,
            verticalalignment='top', horizontalalignment='center', bbox=props)
            
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.set_xlabel('Predicted Probability (p_fail)')
    ax.set_ylabel('Density')
    ax.set_xlim(-0.05, 1.05)
    ax.grid(True)
    ax.legend(loc='upper right', fontsize=8.5)

def main():
    data_path = '/home/redafrix/tests/internship/zzzsmall_report/all_predictions_data.pt'
    if not os.path.exists(data_path):
        print(f"Error: {data_path} does not exist.")
        return
        
    results = torch.load(data_path)
    
    # Define mapping to clean names and output filenames
    configs_to_plot = [
        # 1. v8 tests balanced
        {
            "name": "LSTM Calibrator with Suite ID Prior (Suite ID Enabled)",
            "file": "polarization_1_lstm_suite_id_enabled.png"
        },
        {
            "name": "LSTM Calibrator with Suite ID Prior (Suite ID Disabled at Eval)",
            "file": "polarization_2_lstm_suite_id_disabled.png"
        },
        {
            "name": "LSTM Calibrator (No Suite ID - Trained Without It)",
            "file": "polarization_3_lstm_no_suite_id.png"
        },
        # 2. Selected ideas from 100 tests folder
        {
            "name": "Time-Blind MLP with Log-Compressed Uncertainty (Idea 139)",
            "file": "polarization_4_mlp_idea139.png"
        },
        {
            "name": "Time-Blind MLP with Softplus-Compressed Uncertainty (Idea 166)",
            "file": "polarization_5_mlp_idea166.png"
        },
        {
            "name": "Time-Blind MLP Safety Specialist (Idea 176)",
            "file": "polarization_6_mlp_idea176.png"
        },
        {
            "name": "Time-Blind MLP Uncertainty-Gated Alerts (Idea 210)",
            "file": "polarization_7_mlp_idea210.png"
        },
        # 3. Final 49D * 2
        {
            "name": "Entropy LSTM (49D + Suite ID - Suite ID Enabled)",
            "file": "polarization_8_entropy_lstm_enabled.png"
        },
        {
            "name": "Entropy LSTM (49D + Suite ID - Suite ID Disabled at Eval)",
            "file": "polarization_8_entropy_lstm_disabled.png"
        },
        {
            "name": "Entropy LSTM (49D - Trained Without Suite ID)",
            "file": "polarization_9_entropy_lstm_no_suite_id.png"
        }
    ]
    
    for c in configs_to_plot:
        # 1. Plot Step 150
        id_key_150 = c["name"] + "_ID_150"
        ood_key_150 = c["name"] + "_OOD_150"
        file_150 = c["file"].replace(".png", "_150.png")
        if id_key_150 in results and ood_key_150 in results:
            plot_polarization_panels(
                model_name=c["name"] + " (Step 150)",
                id_data=results[id_key_150],
                ood_data=results[ood_key_150],
                file_name=file_150
            )
        else:
            print(f"Skipping Step 150 for {c['name']}")
            
        # 2. Plot Overall (Full Horizon)
        id_key_overall = c["name"] + "_ID_overall"
        ood_key_overall = c["name"] + "_OOD_overall"
        file_overall = c["file"].replace(".png", "_overall.png")
        if id_key_overall in results and ood_key_overall in results:
            plot_polarization_panels(
                model_name=c["name"] + " (Full Horizon)",
                id_data=results[id_key_overall],
                ood_data=results[ood_key_overall],
                file_name=file_overall
            )
        else:
            print(f"Skipping Overall for {c['name']}")

if __name__ == '__main__':
    main()

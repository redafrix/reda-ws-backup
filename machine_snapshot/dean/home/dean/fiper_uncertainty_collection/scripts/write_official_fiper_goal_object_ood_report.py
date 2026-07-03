import json
from pathlib import Path
import pandas as pd

EXP_DIR = Path("/home/dean/fiper_uncertainty_collection/experiments/official_fiper_goal_object_ood_ablation_20260625")
REPORT_DIR = EXP_DIR / "reports"
REPORT_DIR.mkdir(parents=True, exist_ok=True)
CSV = EXP_DIR / "official_fiper_ablation_results.csv"
VAL = EXP_DIR / "VALIDATION_SUMMARY.json"
REPORT = REPORT_DIR / "OFFICIAL_FIPER_ON_LIBERO_GOAL_OBJECT_OOD_180EP_20260625.md"

def pct(x):
    return f"{100*float(x):.1f}%"

def fmt(x):
    return f"{float(x):.3f}"

df = pd.read_csv(CSV)
val = json.loads(VAL.read_text()) if VAL.exists() else {}
lines = []
lines.append("# Official FIPER on LIBERO Goal-Object-OOD 180ep")
lines.append("")
lines.append("Date: 2026-06-25")
lines.append("")
lines.append("## Dataset and Validation")
lines.append("")
for k in ["validation", "obs_shape", "action_shape", "num_rollouts", "num_steps", "train_rollouts", "calibration_rollouts", "ood_test_rollouts", "ood_success", "ood_failure"]:
    if k in val:
        lines.append(f"- {k}: `{val[k]}`")
lines.append("- In-domain train/calib split: stratified `50 train + 15 calibration` success episodes per task over tasks 0..9.")
lines.append("- OOD test: all 180 episodes from official `libero_goal_object_ood`, 10 per task over tasks 0..17.")
lines.append("- Threshold calibration: in-domain calibration successes only; no OOD tuning.")
lines.append("")
lines.append("## Official FIPER Metrics")
lines.append("")
lines.append("| Method | Window | Style | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |")
lines.append("|---|---:|---|---:|---:|---:|---:|---:|---:|---:|")
for _, r in df.iterrows():
    lines.append("| {Method} | {Window} | {Style} | {sfa} | {fd} | {d10} | {d25} | {d50} | {mt} | {never} |".format(
        Method=r["Method"], Window=r["Window"], Style=r["Style"],
        sfa=pct(r["Success FA"]), fd=pct(r["Failure Det"]), d10=pct(r["Det@10"]),
        d25=pct(r["Det@25"]), d50=pct(r["Det@50"]), mt=fmt(r["Mean Time"]), never=pct(r["Never"])))
lines.append("")
lines.append("## Reference: Our H10 TopK8 Results on the Same OOD Dataset")
lines.append("")
lines.append("| Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |")
lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
ref_rows = [
    ("score_q95_K3", "95.3%", "100.0%", "100.0%", "100.0%", "100.0%", "0.028", "0.0%"),
    ("score_q99_K3", "60.4%", "100.0%", "45.2%", "90.3%", "96.8%", "0.142", "0.0%"),
    ("saved q95_mass_0.15", "96.0%", "100.0%", "100.0%", "100.0%", "100.0%", "0.027", "0.0%"),
    ("q95_mass_10", "34.9%", "100.0%", "12.9%", "93.5%", "96.8%", "0.157", "0.0%"),
    ("q95_mass_20", "20.8%", "96.8%", "3.2%", "90.3%", "96.8%", "0.166", "3.2%"),
    ("q95_mass_50", "2.7%", "96.8%", "0.0%", "16.1%", "90.3%", "0.288", "3.2%"),
]
for row in ref_rows:
    lines.append("| " + " | ".join(row) + " |")
lines.append("")
lines.append("## Caveats")
lines.append("")
lines.append("- In-domain train/calibration embeddings are reconstructed by replaying saved rollout NPZs; logs may include proprio drift warnings. OOD test embeddings use exact saved MuJoCo states.")
lines.append("- The OOD dataset is small but directly aligned with the official 18-task `libero_goal_object_ood` suite: 180 episodes, 31 failures.")
REPORT.write_text("\n".join(lines) + "\n")
print(REPORT)

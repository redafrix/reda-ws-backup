# Stage 8 Switch Policy Results

Episodes parsed: `4065`

| mode | episodes | success_rate | avg_steps | avg_rejects | avg_unc |
|---|---:|---:|---:|---:|---:|
| `A_passive` | 995 | 0.910 | 197.14 | 11.12 | 1.630 |
| `B_deliberation` | 995 | 0.910 | 202.76 | 11.34 | 1.634 |
| `C_random_seed` | 995 | 0.921 | 195.86 | 11.43 | 1.643 |
| `D_low_uncertainty_reject_log` | 995 | 0.910 | 197.14 | 11.15 | 1.630 |
| `E_conservative_switch_proxy` | 85 | 0.824 | 244.02 | 12.89 | 1.690 |

## Interpretation

- This is an offline policy analysis over available rollout logs.
- Oracle WM/expert fallback is not claimed unless expert-action rollout substitution is explicitly available.
- Threshold stability and accepted/rejected risk should be revisited after expanded LIBERO-PRO and hard-task jobs finish.

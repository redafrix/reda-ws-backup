#!/usr/bin/env bash
set -euo pipefail

ROOT="/media/rootalkhatib/My Passport/reda_ws"
cd "$ROOT"

python3 - <<'PY'
import json
from pathlib import Path
from statistics import mean

result_dirs=[
    Path('asynchvla_ws/stage8_ultimate/results/libero_pro_pilot'),
    Path('asynchvla_ws/stage8_ultimate/results/libero_pro_expanded_5eps'),
    Path('asynchvla_ws/stage8_ultimate/results/libero_pro_expanded_30eps'),
    Path('asynchvla_ws/stage8_ultimate/results/normal_libero_hard'),
    Path('asynchvla_ws/stage8_ultimate/results/normal_libero_hard_30eps'),
]
rows=[]
for d in result_dirs:
    if not d.exists():
        continue
    for p in sorted(d.glob('*.json')):
        try:
            data=json.loads(p.read_text())
        except Exception:
            continue
        for ep in data.get('episodes',[]):
            trace=ep.get('trace',[])
            rejects=sum(1 for t in trace if t.get('seed0_rejected_by_threshold') is True)
            uncs=[t.get('chosen_seed_unc') for t in trace if isinstance(t.get('chosen_seed_unc'),(int,float))]
            rows.append({
                'source':str(p),
                'suite':data.get('task_suite'),
                'task_id':data.get('task_id'),
                'mode':ep.get('mode'),
                'success':bool(ep.get('success')),
                'steps':ep.get('steps'),
                'rejects':rejects,
                'unc_mean':mean(uncs) if uncs else None,
                'unc_max':max(uncs) if uncs else None,
            })

out=Path('asynchvla_ws/stage8_ultimate/reports/stage8_switch_policy_results.md')
lines=['# Stage 8 Switch Policy Results','',f'Episodes parsed: `{len(rows)}`','']
lines += ['| mode | episodes | success_rate | avg_steps | avg_rejects | avg_unc |','|---|---:|---:|---:|---:|---:|']
modes=sorted(set(r['mode'] for r in rows if r.get('mode')))
for m in modes:
    rs=[r for r in rows if r.get('mode')==m]
    steps=[r['steps'] for r in rs if isinstance(r.get('steps'),(int,float))]
    rejects=[r['rejects'] for r in rs if isinstance(r.get('rejects'),(int,float))]
    uncs=[r['unc_mean'] for r in rs if isinstance(r.get('unc_mean'),(int,float))]
    succ=sum(1 for r in rs if r.get('success'))/len(rs) if rs else 0.0
    lines.append(f"| `{m}` | {len(rs)} | {succ:.3f} | {(mean(steps) if steps else float('nan')):.2f} | {(mean(rejects) if rejects else 0.0):.2f} | {(mean(uncs) if uncs else float('nan')):.3f} |")
lines += ['', '## Interpretation', '', '- This is an offline policy analysis over available rollout logs.', '- Oracle WM/expert fallback is not claimed unless expert-action rollout substitution is explicitly available.', '- Threshold stability and accepted/rejected risk should be revisited after expanded LIBERO-PRO and hard-task jobs finish.']
out.write_text('\n'.join(lines)+'\n')
print(out)
PY

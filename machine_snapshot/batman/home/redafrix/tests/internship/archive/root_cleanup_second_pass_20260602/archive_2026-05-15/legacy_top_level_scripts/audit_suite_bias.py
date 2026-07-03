import torch
d = torch.load('/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v9_exp01/data/v9_train.pt', map_location='cpu')
eps = d['episodes'] if isinstance(d, dict) else d

suite_stats = {}
for e in eps:
    suite = e.get('task_suite', '')
    succ = int(e.get('success', 0))
    if suite not in suite_stats:
        suite_stats[suite] = {'succ': 0, 'fail': 0}
    if succ == 1:
        suite_stats[suite]['succ'] += 1
    else:
        suite_stats[suite]['fail'] += 1

print(f"{'Suite':<25} | {'Succ':<6} | {'Fail':<6} | {'% Succ':<8}")
print("-" * 55)
for s in sorted(suite_stats.keys()):
    st = suite_stats[s]
    total = st['succ'] + st['fail']
    pct = st['succ'] / total * 100 if total > 0 else 0
    print(f"{s:<25} | {st['succ']:<6} | {st['fail']:<6} | {pct:>6.2f}%")

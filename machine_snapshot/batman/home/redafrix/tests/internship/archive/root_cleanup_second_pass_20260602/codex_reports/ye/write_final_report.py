from __future__ import annotations
import json, pathlib, datetime, statistics, collections, os
ROOT=pathlib.Path('/home/redafrix/tests/internship/codex_reports/ye')
summary=json.loads((ROOT/'parsed_summary.json').read_text())
status=json.loads((ROOT/'bob_stage8_status.json').read_text())

def fmt(x, nd=3):
    if x is None: return 'n/a'
    if isinstance(x,float): return f'{x:.{nd}f}'
    return str(x)

def table(headers, rows):
    out=['| '+' | '.join(headers)+' |','|'+ '|'.join(['---']*len(headers))+'|']
    for r in rows: out.append('| '+' | '.join(str(x) for x in r)+' |')
    return '\n'.join(out)

# model aggregate from earlier script
import glob
SAM=ROOT/'sam_bundle/asynchvla_ws/stage8_ultimate/reports'
model_rows=[]
for p in SAM.glob('stage8_big_arch_*.json'):
    d=json.loads(p.read_text())
    for res in d['results']:
        sm=(res.get('metrics',{}).get('test_ood',{}) or {}).get('simvla_only')
        if sm:
            model_rows.append((res['variant'],d['split'],sm['pairwise_seed_ranking'],sm['improvement_over_seed0'],sm['auroc_top30_worst']))
by=collections.defaultdict(list)
for r in model_rows: by[r[0]].append(r)
variant_avg=[]
for var,rs in by.items():
    variant_avg.append((var,len(rs),statistics.mean(x[2] for x in rs),statistics.mean(x[3] for x in rs),statistics.mean(x[4] for x in rs)))
variant_avg=sorted(variant_avg,key=lambda x:x[2],reverse=True)

# flowtrace aggregate
flow_rows=[]
for p in SAM.glob('stage7_flowtrace_*.json'):
    d=json.loads(p.read_text())
    for res in d['variants']:
        sm=(res.get('metrics',{}).get('test_ood',{}) or {}).get('simvla_only')
        if sm and sm.get('pairwise_seed_ranking') is not None:
            flow_rows.append((res['variant'],d['split'],sm['pairwise_seed_ranking'],sm['improvement_over_seed0'],sm['auroc_top30_worst']))
flow_by=collections.defaultdict(list)
for r in flow_rows: flow_by[r[0]].append(r)
flow_avg=sorted([(k,len(v),statistics.mean(x[2] for x in v),statistics.mean(x[3] for x in v),statistics.mean(x[4] for x in v)) for k,v in flow_by.items()], key=lambda x:x[2], reverse=True)

# target aggregate from collected outputs
tr_root=ROOT/'sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6'
target_rows=[]
for p in tr_root.glob('stage7_multi_expert_target_*.json'):
    d=json.loads(p.read_text())
    for target, arr in d['by_target'].items():
        for res in arr:
            sm=(res.get('metrics',{}).get('test_ood',{}) or {}).get('simvla_only')
            if sm and all(sm.get(k) is not None for k in ['pairwise_seed_ranking','improvement_over_seed0','auroc_top30_worst']):
                target_rows.append((target,d['split'],res['variant'],sm['pairwise_seed_ranking'],sm['improvement_over_seed0'],sm['auroc_top30_worst']))
tar_by=collections.defaultdict(list)
for r in target_rows: tar_by[r[0]].append(r)
target_avg=sorted([(k,len(v),statistics.mean(x[3] for x in v),statistics.mean(x[4] for x in v),statistics.mean(x[5] for x in v)) for k,v in tar_by.items()], key=lambda x:x[2], reverse=True)

# calibration aggregate
cal_rows=[]
for q in ['0.80','0.90','0.95']:
    p=SAM/f'stage8_calibration_real_q{q}.json'
    if not p.exists(): continue
    arr=json.loads(p.read_text())
    tmp=collections.defaultdict(list)
    for r in arr:
        if r.get('variant')=='context_gated_action' and r.get('eval','').endswith('simvla'):
            tmp[r['method']].append(r)
    for method,rs in tmp.items():
        cal_rows.append((q,method,len(rs),statistics.mean(r['coverage'] for r in rs),min(r['coverage'] for r in rs),statistics.mean(r['mean_width'] for r in rs),statistics.mean(r['auroc'] for r in rs)))

lines=[]
lines += ['# Final SimVLA / AsyncVLA-Style Uncertainty Experiment Report', '', f'Generated locally: `{datetime.datetime.now().isoformat(timespec="seconds")}`', '', 'Local report folder: `/home/redafrix/tests/internship/codex_reports/ye`', '']
lines += ['## Executive Summary', '', '- The 72-hour Stage 8 campaign mostly completed successfully: `26` jobs were done, `0` were failed, Sam was fully done, and Bob still had one long 50-episode backup rollout running at the snapshot time.', '- LIBERO-PRO became the main execution benchmark. The strongest completed LIBERO-PRO result is the 20 episodes/task expanded run: 20 task/mode groups, 1600 episodes total.', '- The uncertainty/rater is useful for offline action reliability and controlled OOD SimVLA-seed ranking. The strongest family remains context/seed-aware models, not action-only.', '- For real rollout control, multi-seed deliberation was not clearly better than seed0. On LIBERO-PRO, B_deliberation improved success only slightly over A_passive but took slightly more steps; C_random_seed was similar or slightly better in aggregate, which means the current uncertainty score is not yet a reliable seed selector for execution.', '- Calibration improved but is not deployable across all domains. 90% conformal-style coverage still undercovers badly on some splits, especially heldout spatial and some ID/OOD mismatches.', '- Flowtrace features did not improve pairwise ranking in the completed small/medium runs. Flow-only had high bad-action AUROC in some splits, but poor seed ranking, so it is not a replacement for the context/seed/action rater.', '- Multi-expert targets did not beat the original single-expert L2 target on average. They may help individual splits, but the simple target remains the most stable completed training target.', '- History models were not actually trained because the available rollout outputs were aggregate episode JSON, not clean sequential per-step windows with previous action/uncertainty/proprio/VLM features.', '']
lines += ['## Final Decision', '', '**Do not integrate a real VLA/WM switch yet.** The method is promising as a warning/risk-ranking signal and for offline action-error filtering, but it is not yet a reliable runtime switch policy. The next scientific step should be progress/next-state labels from rollouts, not more synthetic action-L2 sweeps.', '']

lines += ['## Queue / Machine Status', '']
rows=[]
for r in status:
    rows.append([r.get('job_id'), r.get('machine'), r.get('state'), r.get('completed_at',''), r.get('started_at','')])
lines.append(table(['job_id','machine','state','completed_at','started_at'], rows))
lines += ['', 'Snapshot interpretation:', '- Sam: all Stage 8 jobs done.', '- Bob: `stage8_libero_pro_50eps_backup_bob` still running at snapshot, `stage8_normal_libero_50eps_backup_bob` pending. This is a backup extension, not a blocker for the completed 20/30 episode analysis.', '']

lines += ['## LIBERO-PRO Rollout Results', '', 'Source: `bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_libero_pro_expanded_rollout_results.md`', '', '### Aggregate by mode, 20 episodes/task', '']
lines.append(table(['mode','episodes','tasks','success','avg_steps','avg_unc','avg_rejects','min_task_success'], [[k,v['episodes'],v['tasks'],fmt(v['success_rate']),fmt(v['avg_steps'],2),fmt(v['avg_unc']),fmt(v['avg_rejects'],2),fmt(v['min_task_success'])] for k,v in summary['libero_pro_mode_summary'].items()]))
lines += ['', 'Key reading:', '- `A_passive` seed0 baseline: 94.5% success, 176.09 avg steps.', '- `B_deliberation`: 95.5% success, 177.21 avg steps. This is +1.0 success point but slightly slower.', '- `C_random_seed`: 95.75% success, 176.30 avg steps. Random seed selection slightly beat deliberation, so the current rater does not yet prove it can choose the best seed in live execution.', '- `D_low_uncertainty_reject_log` exactly mirrors seed0 execution, as expected, because it logs reject decisions without changing actions.', '', 'Worst LIBERO-PRO seed0 tasks:']
lines.append(table(['suite','task','success','avg_steps','avg_unc','max_unc'], [[x[2],x[3],fmt(x[0]),fmt(x[1],2),x[4]['avg_unc'],x[4]['max_unc']] for x in summary['libero_pro_worst_A'][:6]]))
lines += ['', 'Best task-level improvements from non-seed0 modes:']
lines.append(table(['suite/task','mode','success_delta','steps_delta_vs_A','mode_success','A_success'], [[f'{x[2][0]} {x[2][1]}',x[3],fmt(x[0]),fmt(x[1],2),x[4]['success_rate'],x[5]['success_rate']] for x in summary['libero_pro_best_deltas'][:6]]))
lines += ['', 'Largest regressions:', '']
lines.append(table(['suite/task','mode','success_delta','steps_delta_vs_A','mode_success','A_success'], [[f'{x[2][0]} {x[2][1]}',x[3],fmt(x[0]),fmt(x[1],2),x[4]['success_rate'],x[5]['success_rate']] for x in summary['libero_pro_bad_deltas'][:6]]))
lines += ['', 'Interpretation: uncertainty-guided deliberation sometimes helps specific tasks, but the task-level regressions and the random-seed baseline mean this is not yet a robust runtime policy.', '']

lines += ['## Normal LIBERO Hard-Task Baseline', '', 'Source: `stage8_normal_libero_hard_task_results.md`, 30 episodes/task, 840 episodes total.', '']
lines.append(table(['mode','episodes','tasks','success','avg_steps','avg_unc','avg_rejects','min_task_success'], [[k,v['episodes'],v['tasks'],fmt(v['success_rate']),fmt(v['avg_steps'],2),fmt(v['avg_unc']),fmt(v['avg_rejects'],2),fmt(v['min_task_success'])] for k,v in summary['hard_mode_summary'].items()]))
lines += ['', 'Hardest task remains `libero_spatial task 5`: seed0 success 0.133, avg 540.93 steps. Deliberation and random did not fix it. This task is useful as a failure/stress benchmark.', '']

lines += ['## Switch Policy Analysis', '', 'Source: `stage8_switch_policy_results.md`, 4065 parsed episodes.', '']
lines += ['| mode | episodes | success | avg_steps | avg_rejects | avg_unc |','|---|---:|---:|---:|---:|---:|','| A_passive | 995 | 0.910 | 197.14 | 11.12 | 1.630 |','| B_deliberation | 995 | 0.910 | 202.76 | 11.34 | 1.634 |','| C_random_seed | 995 | 0.921 | 195.86 | 11.43 | 1.643 |','| D_reject_log | 995 | 0.910 | 197.14 | 11.15 | 1.630 |','| E_conservative_switch_proxy | 85 | 0.824 | 244.02 | 12.89 | 1.690 |','', 'Interpretation: the current offline switch proxy does not yet demonstrate deployment benefit. Conservative fallback underperformed on the small available subset. The main reliable use is warning/rejection analysis, not automatic action replacement.', '']

lines += ['## Model / Architecture Results', '', 'Source: Sam `stage8_big_arch_*.json`, test_ood SimVLA-only metrics averaged across 6 controlled OOD splits.', '']
lines.append(table(['variant','splits','pairwise_seed_rank','improvement_over_seed0','AUROC_top30_worst'], [[v,n,fmt(pair),fmt(imp),fmt(auc)] for v,n,pair,imp,auc in variant_avg]))
lines += ['', 'Important result: action-only is clearly worse after Stage 8. Average test_ood pairwise seed ranking was `0.7515` for action-only versus `0.9174` for `seed_relative_pairwise`, `0.9161` for `full_engineered_simvla_focused`, and `0.9141` for `context_gated_action`.', '', 'Best per controlled-OOD split:', '']
lines.append(table(['split/part','best_variant','pairwise','improvement','AUROC'], [[k,v['variant'],fmt(v['pairwise']),fmt(v['improve']),fmt(v['auroc'])] for k,v in summary['best_pairwise'].items() if 'test_ood' in k]))
lines += ['', 'Recommended model family from completed offline metrics: `seed_relative_pairwise` or `full_engineered_simvla_focused` for action-error ranking; `context_gated_action` remains the simplest strong baseline.', '']

lines += ['## Flowtrace Feature Results', '', 'Source: `stage7_flowtrace_*.json`, smaller/medium flowtrace runs.', '']
lines.append(table(['variant','splits','pairwise','improvement','AUROC'], [[v,n,fmt(pair),fmt(imp),fmt(auc)] for v,n,pair,imp,auc in flow_avg]))
lines += ['', 'Interpretation: flowtrace did not improve SimVLA seed ranking. `context_gated_action_no_flow` beat all flow-augmented variants on pairwise ranking in this run. `flow_only` had high AUROC but poor pairwise ranking, so flow dynamics may help bad-action detection but not seed selection yet.', '']

lines += ['## Target Sweep Results', '', 'Source: detailed Sam `stage7_multi_expert_target_*.json` outputs.', '']
lines.append(table(['target','rows','avg_pairwise','avg_improvement','avg_AUROC'], [[t,n,fmt(pair),fmt(imp),fmt(auc)] for t,n,pair,imp,auc in target_avg]))
lines += ['', 'Interpretation: the original single-expert L2 target remained best on average. Multi-expert min-distance K=5/K=10 helped some individual splits, but did not produce a global improvement. Softmin was worst/unstable in this completed sweep.', '']

lines += ['## Calibration Results', '', 'Source: `stage8_calibration_real_q*.json`, context_gated_action, SimVLA-only evals.', '']
lines.append(table(['target_coverage','method','eval_rows','avg_coverage','min_coverage','avg_width','avg_AUROC'], [[q,m,n,fmt(cov),fmt(mn),fmt(width),fmt(auc)] for q,m,n,cov,mn,width,auc in cal_rows]))
lines += ['', 'Interpretation:', '- Calibration ranking/AUROC is strong, but coverage is not reliable enough. At target 90%, average SimVLA-only coverage was only 0.845-0.860 depending on method, with worst split around 0.629-0.648.', '- At target 95%, average coverage improved to 0.894-0.917, but still undercovered badly in the worst split and widened bounds.', '- Best deployable current choice if forced: `global_residual_simvla` or `affine_plus_residual_simvla` at 95% target, but this is conservative and still not guaranteed on all splits.', '- Needed next: small target-domain calibration pools or progress-risk probability calibration, not just residual bounds on action L2.', '']

lines += ['## History Models', '', 'History models were not trained. The Stage 8 history job truthfully reported that only aggregate rollout JSON was available on Sam; clean sequential rollout traces with previous action, previous uncertainty, previous proprio, previous VLM features, and current candidate action were not available in a usable dataset. This remains future work.', '']

lines += ['## Previous Uncertainty Feature Assets', '', 'An inventory was written to `stage8_uncertainty_feature_assets_inventory.md`. Stage 5/6 rater checkpoints and predictions are reusable as baselines or ensembles. TDQC/failure-oriented artifacts should remain baselines only and must not become primary training data for this action-error method.', '']

lines += ['## Failures / Blockers / Caveats', '', '- One backup job, `stage8_libero_pro_50eps_backup_bob`, was still running at the final snapshot. The completed analysis uses the robust 20 episodes/task LIBERO-PRO report plus completed 30-episode normal-LIBERO hard-task report.', '- `stage8_normal_libero_50eps_backup_bob` was still pending. This does not invalidate the completed 30-episode hard-task benchmark.', '- LIBERO-PRO logs still contain `FileNotFoundError` for some missing `.pruned_init` states. The runner skipped/continued on available suites; not all perturbation/task combinations were valid.', '- The Stage 8 final report generated on Bob at `2026-05-17T00:34:03` was interim; this report is the consolidated local post-run report using later collected artifacts.', '- Flowtrace and target sweeps ran after path fixes; earlier placeholder jobs should be ignored in favor of the `*_real_*` reports.', '- Runtime deployment was not tested with a real world-model fallback. `E_conservative_switch_proxy` is SimVLA-only fallback, not a WM switch.', '']

lines += ['## What Worked', '', '- SimVLA action-error uncertainty is feasible and scientifically meaningful for offline SimVLA candidate ranking.', '- Context/seed-relative models now beat action-only clearly across controlled OOD splits.', '- LIBERO-PRO rollout infrastructure works enough to run large execution benchmarks.', '- Hard normal-LIBERO benchmark identifies real hard tasks, especially `libero_spatial task 5`.', '- Calibration code produces useful risk separation and AUROC, even though bound coverage is not yet reliable.', '']
lines += ['## What Did Not Work Yet', '', '- Uncertainty-guided seed deliberation did not reliably beat random seed choice in real LIBERO-PRO execution.', '- Conservative switch proxy did not improve execution on the parsed subset.', '- Flowtrace features did not improve pairwise ranking.', '- Multi-expert L2 target did not beat single-expert L2 on average.', '- History models were blocked by missing sequential rollout logs.', '- Calibration is still undercovered on several controlled OOD/ID combinations.', '']

lines += ['## Recommended Next Steps', '', '1. Instrument rollout logging at every decision step: context id, task, observation metadata, selected action, all seed actions, predicted uncertainty, reward delta, success/progress within H steps, proprio, and optional VLM features. This is required for progress targets and history models.', '2. Train a progress/risk target, not only action L2: predict slow/failure risk or success-within-H from the current action and context.', '3. Use `seed_relative_pairwise` / `full_engineered_simvla_focused` as the offline ranking baseline, and keep `context_gated_action` as the simple deployable baseline.', '4. Do not use deliberation as a default runtime policy yet. If deploying anything now, use uncertainty as a warning/reject signal only.', '5. Re-run calibration with small target-domain calibration pools and probability calibration for bad/slow actions once progress labels exist.', '6. Keep LIBERO-PRO as the main benchmark, but fix or filter missing `.pruned_init` task configs so every reported perturbation suite has a known valid task set.', '7. Use `libero_spatial task 5` as a normal-LIBERO stress test because all current policies fail it.', '']

lines += ['## Exact Artifacts To Read First', '', '- This report: `/home/redafrix/tests/internship/codex_reports/ye/FINAL_SIMVLA_UNCERTAINTY_FULL_REPORT.md`', '- Parsed summary: `/home/redafrix/tests/internship/codex_reports/ye/parsed_summary.json`', '- LIBERO-PRO rollout: `bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_libero_pro_expanded_rollout_results.md`', '- Hard normal LIBERO: `bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_normal_libero_hard_task_results.md`', '- Switch analysis: `bob_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_switch_policy_results.md`', '- Big model sweep: `sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_architecture_loss_big_sweep_results.md` plus `stage8_big_arch_*.json`', '- Calibration: `sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_mega_sweep_results.md` and `stage8_calibration_real_q*.json`', '- Flowtrace: `sam_bundle/asynchvla_ws/stage8_ultimate/reports/stage8_flowtrace_real_results.md` and `stage7_flowtrace_*.json`', '- Target sweep: `sam_outputs_stage7/asynchvla_ws/outputs/reports/stage6/stage7_multi_expert_target_*.json`', '']

lines += ['## Final Recommendation', '', '**Proceed, but change the claim.** The project has a strong action-error rater for ranking SimVLA-generated candidate actions under controlled OOD, and context-aware models beat action-only. However, the current uncertainty is not yet validated as a robust runtime VLA/WM switch. The next claim should be: “SimVLA action-error uncertainty can rank candidate action reliability and identify risky actions; execution-risk deployment requires progress-target training and better calibration.”', '', 'Do not write a paper claim that deliberation improves execution based on this run; the LIBERO-PRO results do not support that strongly enough.']

# append file list
files=[]
for p in ROOT.rglob('*'):
    if p.is_file(): files.append(str(p.relative_to(ROOT)))
lines += ['', '## Local Artifact List', '', '```text'] + sorted(files)[:500] + ['```']

out=ROOT/'FINAL_SIMVLA_UNCERTAINTY_FULL_REPORT.md'
out.write_text('\n'.join(lines)+'\n')
print(out)

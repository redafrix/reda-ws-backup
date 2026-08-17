#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
import numpy as np

def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--baseline-root', type=Path, required=True)
    parser.add_argument('--shadow-root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--tol', type=float, default=1e-6)
    args = parser.parse_args()

    base_sums = {int(r['source_episode_id']): r for r in load_jsonl(args.baseline_root / 'episode_summaries.jsonl')}
    shad_sums = {int(r['source_episode_id']): r for r in load_jsonl(args.shadow_root / 'episode_summaries.jsonl')}

    base_rows = load_jsonl(args.baseline_root / 'risk_receding_samples.jsonl')
    shad_rows = load_jsonl(args.shadow_root / 'risk_receding_samples.jsonl')

    base_by_ep = {}
    for r in base_rows:
        base_by_ep.setdefault(int(r['metadata']['source_episode_id']), []).append(r)
    shad_by_ep = {}
    for r in shad_rows:
        shad_by_ep.setdefault(int(r['metadata']['source_episode_id']), []).append(r)

    checks = []
    for sid in [0, 1, 2]:
        if sid not in shad_sums:
            checks.append({'episode': sid, 'check': 'shadow_episode_present', 'pass': False})
            continue
        bs = base_sums[sid]
        ss = shad_sums[sid]
        outcome_match = bool(bs['success']) == bool(ss['success'])
        ticks_match = int(bs['control_ticks']) == int(ss['control_ticks'])
        rows_match = int(bs['decision_rows']) == int(ss['decision_rows'])
        checks.append({'episode': sid, 'check': 'outcome_match', 'pass': outcome_match, 'baseline': bs['success'], 'shadow': ss['success']})
        checks.append({'episode': sid, 'check': 'control_ticks_match', 'pass': ticks_match, 'baseline': bs['control_ticks'], 'shadow': ss['control_ticks']})
        checks.append({'episode': sid, 'check': 'decision_rows_match', 'pass': rows_match, 'baseline': bs['decision_rows'], 'shadow': ss['decision_rows']})

        brows = base_by_ep.get(sid, [])
        srows = shad_by_ep.get(sid, [])
        if len(brows) != len(srows):
            checks.append({'episode': sid, 'check': 'row_count_match', 'pass': False, 'baseline': len(brows), 'shadow': len(srows)})
            continue

        max_proprio_diff = 0.0
        max_chunk_diff = 0.0
        max_ace_diff = 0.0
        max_action_diff = 0.0

        for br, sr in zip(brows, srows):
            bp = np.asarray(br['current']['proprio'], dtype=np.float32)
            sp = np.asarray(sr['current']['proprio'], dtype=np.float32)
            max_proprio_diff = max(max_proprio_diff, float(np.max(np.abs(bp - sp))))

            bc = np.asarray(br['main_candidate_action_chunk_env'], dtype=np.float32)
            sc = np.asarray(sr['main_candidate_action_chunk_env'], dtype=np.float32)
            max_chunk_diff = max(max_chunk_diff, float(np.max(np.abs(bc - sc))))

            bace = np.asarray(br['ace_features_7d'], dtype=np.float32)
            sace = np.asarray(sr['ace_features_7d'], dtype=np.float32)
            max_ace_diff = max(max_ace_diff, float(np.max(np.abs(bace - sace))))

            ba = np.asarray(br['executed_action_sequence'], dtype=np.float32)
            sa = np.asarray(sr['executed_action_sequence'], dtype=np.float32)
            max_action_diff = max(max_action_diff, float(np.max(np.abs(ba - sa))))

        checks.append({'episode': sid, 'check': 'proprio_parity', 'max_abs_diff': max_proprio_diff, 'pass': max_proprio_diff <= args.tol})
        checks.append({'episode': sid, 'check': 'main_chunk_parity', 'max_abs_diff': max_chunk_diff, 'pass': max_chunk_diff <= args.tol})
        checks.append({'episode': sid, 'check': 'ace_parity', 'max_abs_diff': max_ace_diff, 'pass': max_ace_diff <= args.tol})
        checks.append({'episode': sid, 'check': 'executed_actions_parity', 'max_abs_diff': max_action_diff, 'pass': max_action_diff <= args.tol})

    all_pass = all(c['pass'] for c in checks)
    result = {
        'schema_version': 'isaac_online_shadow_parity_v1',
        'tolerance': args.tol,
        'pass': all_pass,
        'checks': checks,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if all_pass else 2

if __name__ == '__main__':
    raise SystemExit(main())

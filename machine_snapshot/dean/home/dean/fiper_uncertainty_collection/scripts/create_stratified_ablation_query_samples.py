import json
from pathlib import Path
from collections import defaultdict, Counter
root = Path("/home/dean/fiper_uncertainty_collection/data/simvla_goal_object_ood_ablation_20260625/worker_0")
summ_path = root / "episode_summaries.jsonl"
query_path = root / "query_samples.jsonl"
out_path = root / "stratified_query_samples_50train_15calib_per_task.jsonl"
manifest_path = root / "stratified_query_samples_50train_15calib_per_task_manifest.json"
by_task = defaultdict(list)
summaries = {}
for line in summ_path.open():
    if not line.strip():
        continue
    r = json.loads(line)
    if bool(r.get("success", False)):
        tid = int(r["task_id"])
        by_task[tid].append(r["episode_id"])
    summaries[r["episode_id"]] = r
selected_train, selected_calib = [], []
counts = {str(t): len(by_task.get(t, [])) for t in range(10)}
missing = {t: len(by_task.get(t, [])) for t in range(10) if len(by_task.get(t, [])) < 65}
if missing:
    raise RuntimeError(f"not enough success episodes per task: {missing}; counts={counts}")
for t in range(10):
    eps = sorted(by_task[t])
    selected_train.extend(eps[:50])
    selected_calib.extend(eps[50:65])
selected = set(selected_train) | set(selected_calib)
rows = 0
ep_rows = Counter()
with query_path.open() as fin, out_path.open("w") as fout:
    for line in fin:
        if not line.strip():
            continue
        r = json.loads(line)
        ep = r.get("episode_id")
        if ep in selected:
            r["official_fiper_ablation_split"] = "train" if ep in set(selected_train) else "calib"
            fout.write(json.dumps(r, separators=(",", ":")) + "\n")
            rows += 1
            ep_rows[ep] += 1
missing_rows = sorted(selected - set(ep_rows))
if missing_rows:
    raise RuntimeError(f"selected episodes missing query rows: {missing_rows[:10]} total={len(missing_rows)}")
manifest = {
    "source_query_samples": str(query_path),
    "output": str(out_path),
    "train_episodes": selected_train,
    "calib_episodes": selected_calib,
    "train_count": len(selected_train),
    "calib_count": len(selected_calib),
    "rows": rows,
    "success_counts_available_by_task": counts,
    "train_counts_by_task": {str(t): sum(int(summaries[e]["task_id"]) == t for e in selected_train) for t in range(10)},
    "calib_counts_by_task": {str(t): sum(int(summaries[e]["task_id"]) == t for e in selected_calib) for t in range(10)},
    "row_count_minmax_per_episode": [min(ep_rows.values()), max(ep_rows.values())],
}
manifest_path.write_text(json.dumps(manifest, indent=2))
print(json.dumps({k: manifest[k] for k in ["train_count","calib_count","rows","train_counts_by_task","calib_counts_by_task","row_count_minmax_per_episode"]}, indent=2))

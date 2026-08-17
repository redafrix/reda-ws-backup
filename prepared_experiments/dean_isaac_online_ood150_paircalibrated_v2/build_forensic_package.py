#!/usr/bin/env python3
"""Build the 4-part forensic evidence package for ChatGPT inspection."""
import os, sys, json, hashlib, shutil, zipfile, io
from pathlib import Path
import numpy as np
import zstandard as zstd

WORKSPACE = Path(sys.argv[1] if len(sys.argv) > 1 else "/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
ROUND0 = WORKSPACE / "outputs/final_seen_h10_round_000_seed20260730"
OOD = WORKSPACE / "outputs/final_locked_h10_ood150_seed20260728"
FROZEN = WORKSPACE / "frozen_datasets/isaac_seen_h10_topk8_v1"
MODELS = WORKSPACE / "models/isaac_h10_topk8_temporal_v1"
ONLINE_DEV40 = WORKSPACE / "online_evals/isaac_ood150_argmin_cap_v1/runs/dev40/f1_cap95"

STAGE = Path("/tmp/forensic_stage")
if STAGE.exists():
    shutil.rmtree(STAGE)
STAGE.mkdir(parents=True)

OUT_DIR = Path("/tmp/forensic_chatgpt_package_20260817")
if OUT_DIR.exists():
    shutil.rmtree(OUT_DIR)
OUT_DIR.mkdir(parents=True)

manifest_entries = []

def sha256_f(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        while chunk := f.read(1024 * 1024):
            h.update(chunk)
    return h.hexdigest()

# ==========================================
# ZIP 1: 01_RAW_SEEN_EXAMPLES.zip
# ==========================================
print("Building ZIP 1: RAW SEEN EXAMPLES...")
z1_stage = STAGE / "01_raw_seen"
z1_stage.mkdir(parents=True)

splits_map = json.loads((FROZEN / "split_assignments.json").read_text())
all_summaries = [json.loads(l) for l in (ROUND0 / "episode_summaries.jsonl").read_text().splitlines() if l.strip()]

by_split_outcome = {}
for s in all_summaries:
    ep_id = s["episode_id"]
    split = splits_map.get(ep_id, {}).get("split", "train")
    succ = s.get("success", False)
    key = (split, succ)
    if key not in by_split_outcome:
        by_split_outcome[key] = []
    by_split_outcome[key].append(s)

for k in by_split_outcome:
    by_split_outcome[k].sort(key=lambda x: x["source_episode_id"])

# Priority counts per category:
counts_spec = {
    ("train", True): 6,
    ("train", False): 6,
    ("validation", True): 6,
    ("validation", False): 6,
    ("test", True): 6,
    ("test", False): 6,
}

selected_eps = []
for (split, succ), count in counts_spec.items():
    eps = by_split_outcome.get((split, succ), [])[:count]
    for e in eps:
        selected_eps.append((e["episode_id"], split, succ))

sel_meta = []
sel_summaries = []

for ep_id, split_name, succ in selected_eps:
    ep_src_dir = ROUND0 / "episodes" / ep_id
    ep_dst_dir = z1_stage / "episodes" / ep_id
    shutil.copytree(ep_src_dir, ep_dst_dir)
    
    matching_sum = next(s for s in all_summaries if s["episode_id"] == ep_id)
    sel_summaries.append(matching_sum)
    
    files_info = {}
    for f in ep_src_dir.iterdir():
        files_info[f.name] = {
            "size_bytes": f.stat().st_size,
            "sha256": sha256_f(f)
        }
        manifest_entries.append({
            "zip_name": "01_RAW_SEEN_EXAMPLES.zip",
            "rel_path": f"episodes/{ep_id}/{f.name}",
            "orig_path": str(f),
            "orig_size": f.stat().st_size,
            "orig_sha256": files_info[f.name]["sha256"]
        })
        
    sel_meta.append({
        "episode_id": ep_id,
        "source_episode_id": matching_sum["source_episode_id"],
        "split": split_name,
        "success": succ,
        "decision_rows_count": matching_sum.get("decision_rows", 0),
        "original_path": str(ep_src_dir),
        "files": files_info
    })

shutil.copy2(FROZEN / "split_assignments.json", z1_stage / "split_assignments.json")
manifest_entries.append({
    "zip_name": "01_RAW_SEEN_EXAMPLES.zip",
    "rel_path": "split_assignments.json",
    "orig_path": str(FROZEN / "split_assignments.json"),
    "orig_size": (FROZEN / "split_assignments.json").stat().st_size,
    "orig_sha256": sha256_f(FROZEN / "split_assignments.json")
})

(z1_stage / "SELECTED_EPISODE_SUMMARIES.json").write_text(json.dumps(sel_summaries, indent=2))
manifest_entries.append({
    "zip_name": "01_RAW_SEEN_EXAMPLES.zip",
    "rel_path": "SELECTED_EPISODE_SUMMARIES.json",
    "orig_path": "GENERATED FORENSIC EXTRACTION (from episode_summaries.jsonl)",
    "orig_size": (z1_stage / "SELECTED_EPISODE_SUMMARIES.json").stat().st_size,
    "orig_sha256": sha256_f(z1_stage / "SELECTED_EPISODE_SUMMARIES.json")
})

(z1_stage / "RAW_SEEN_SELECTION.json").write_text(json.dumps(sel_meta, indent=2))
manifest_entries.append({
    "zip_name": "01_RAW_SEEN_EXAMPLES.zip",
    "rel_path": "RAW_SEEN_SELECTION.json",
    "orig_path": "GENERATED FORENSIC INDEX",
    "orig_size": (z1_stage / "RAW_SEEN_SELECTION.json").stat().st_size,
    "orig_sha256": sha256_f(z1_stage / "RAW_SEEN_SELECTION.json")
})

z1_zip_path = OUT_DIR / "01_RAW_SEEN_EXAMPLES.zip"
with zipfile.ZipFile(z1_zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(z1_stage):
        for f in files:
            full_p = Path(root) / f
            rel_p = full_p.relative_to(z1_stage)
            zipf.write(full_p, rel_p)

print(f"ZIP 1 created: {z1_zip_path} ({z1_zip_path.stat().st_size / 1e6:.2f} MB)")


# ==========================================
# ZIP 2: 02_RISK_MODEL_TRAINING_EVIDENCE.zip
# ==========================================
print("Building ZIP 2: RISK MODEL TRAINING EVIDENCE...")
z2_stage = STAGE / "02_training_evidence"
z2_stage.mkdir(parents=True)

for fname in ["promoted_trainer_reference.py", "results.json", "thresholds.json", "temporal_thresholds.json", "model_manifest.json", "seen_scores.npz", "TRAINING_COMPLETE", "model.pt"]:
    src_f = MODELS / fname
    if src_f.exists():
        shutil.copy2(src_f, z2_stage / fname)
        manifest_entries.append({
            "zip_name": "02_RISK_MODEL_TRAINING_EVIDENCE.zip",
            "rel_path": fname,
            "orig_path": str(src_f),
            "orig_size": src_f.stat().st_size,
            "orig_sha256": sha256_f(src_f)
        })

for fname in ["dataset_manifest.json", "normalization.json", "split_assignments.json", "FROZEN_AND_VALIDATED"]:
    src_f = FROZEN / fname
    if src_f.exists():
        shutil.copy2(src_f, z2_stage / fname)
        manifest_entries.append({
            "zip_name": "02_RISK_MODEL_TRAINING_EVIDENCE.zip",
            "rel_path": fname,
            "orig_path": str(src_f),
            "orig_size": src_f.stat().st_size,
            "orig_sha256": sha256_f(src_f)
        })

(z2_stage / "scripts").mkdir(parents=True, exist_ok=True)
for fname in ["train_isaac_topk8.py", "build_frozen_dataset.py", "build_locked_eval_dataset.py", "common.py"]:
    src_f = WORKSPACE / "risk_head_pipeline" / fname
    if src_f.exists():
        shutil.copy2(src_f, z2_stage / f"scripts/{fname}")
        manifest_entries.append({
            "zip_name": "02_RISK_MODEL_TRAINING_EVIDENCE.zip",
            "rel_path": f"scripts/{fname}",
            "orig_path": str(src_f),
            "orig_size": src_f.stat().st_size,
            "orig_sha256": sha256_f(src_f)
        })

# Extract training samples: 20 train, 10 val, 10 test
def extract_samples(dest_dir: Path):
    sample_index = []
    arrays = {}
    splits_spec = [("train", 20), ("validation", 10), ("test", 10)]
    for split_name, count in splits_spec:
        s_dir = FROZEN / split_name
        act = np.load(s_dir / "action.npy", mmap_mode="r")[:count]
        hist = np.load(s_dir / "history.npy", mmap_mode="r")[:count]
        stat = np.load(s_dir / "static.npy", mmap_mode="r")[:count]
        lbl = np.load(s_dir / "label.npy", mmap_mode="r")[:count]
        ep_idx = np.load(s_dir / "episode_index.npy", mmap_mode="r")[:count]
        dec_idx = np.load(s_dir / "decision_index.npy", mmap_mode="r")[:count]
        
        arrays[f"{split_name}_action"] = np.array(act)
        arrays[f"{split_name}_history"] = np.array(hist)
        arrays[f"{split_name}_static"] = np.array(stat)
        arrays[f"{split_name}_label"] = np.array(lbl)
        arrays[f"{split_name}_episode_index"] = np.array(ep_idx)
        arrays[f"{split_name}_decision_index"] = np.array(dec_idx)
        
        episodes_meta = json.loads((s_dir / "episodes.json").read_text())
        for i in range(count):
            e_idx = int(ep_idx[i])
            sample_index.append({
                "split": split_name,
                "sample_within_split_index": i,
                "episode_index": e_idx,
                "episode_id": episodes_meta[e_idx]["episode_id"] if e_idx < len(episodes_meta) else str(e_idx),
                "decision_index": int(dec_idx[i]),
                "label": int(lbl[i]),
                "action_shape": list(act[i].shape),
                "history_shape": list(hist[i].shape),
                "static_shape": list(stat[i].shape),
                "candidate_representation": "Candidate 0 trajectory features (main candidate action chunk + TopK8 uncertainty features derived from candidate 0 diffusion trace)"
            })
            
    npz_path = dest_dir / "TRAINING_INPUT_SAMPLE.npz"
    np.savez_compressed(npz_path, **arrays)
    idx_path = dest_dir / "TRAINING_INPUT_SAMPLE_INDEX.json"
    idx_path.write_text(json.dumps(sample_index, indent=2))
    print(f"Extracted {len(sample_index)} samples across train (20), validation (10), test (10).")

extract_samples(z2_stage)

# Save extract script
extract_script_path = z2_stage / "extract_training_input_sample.py"
extract_script_path.write_text("""#!/usr/bin/env python3
# Non-scientific extraction tool: copy deterministic training input samples without recomputation
import json
from pathlib import Path
import numpy as np

WORKSPACE = Path('/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813')
FROZEN = WORKSPACE / 'frozen_datasets/isaac_seen_h10_topk8_v1'

def extract_samples():
    sample_index = []
    arrays = {}
    splits_spec = [('train', 20), ('validation', 10), ('test', 10)]
    for split_name, count in splits_spec:
        s_dir = FROZEN / split_name
        act = np.load(s_dir / 'action.npy', mmap_mode='r')[:count]
        hist = np.load(s_dir / 'history.npy', mmap_mode='r')[:count]
        stat = np.load(s_dir / 'static.npy', mmap_mode='r')[:count]
        lbl = np.load(s_dir / 'label.npy', mmap_mode='r')[:count]
        ep_idx = np.load(s_dir / 'episode_index.npy', mmap_mode='r')[:count]
        dec_idx = np.load(s_dir / 'decision_index.npy', mmap_mode='r')[:count]
        arrays[f'{split_name}_action'] = np.array(act)
        arrays[f'{split_name}_history'] = np.array(hist)
        arrays[f'{split_name}_static'] = np.array(stat)
        arrays[f'{split_name}_label'] = np.array(lbl)
        arrays[f'{split_name}_episode_index'] = np.array(ep_idx)
        arrays[f'{split_name}_decision_index'] = np.array(dec_idx)
        episodes_meta = json.loads((s_dir / 'episodes.json').read_text())
        for i in range(count):
            e_idx = int(ep_idx[i])
            sample_index.append({
                'split': split_name,
                'sample_within_split_index': i,
                'episode_index': e_idx,
                'episode_id': episodes_meta[e_idx]['episode_id'] if e_idx < len(episodes_meta) else str(e_idx),
                'decision_index': int(dec_idx[i]),
                'label': int(lbl[i]),
                'action_shape': list(act[i].shape),
                'history_shape': list(hist[i].shape),
                'static_shape': list(stat[i].shape),
                'candidate_representation': 'Candidate 0 trajectory features (main candidate action chunk + TopK8 uncertainty features derived from candidate 0 diffusion trace)'
            })
    np.savez_compressed('TRAINING_INPUT_SAMPLE.npz', **arrays)
    Path('TRAINING_INPUT_SAMPLE_INDEX.json').write_text(json.dumps(sample_index, indent=2))
    print(f'Extracted {len(sample_index)} samples.')

if __name__ == '__main__':
    extract_samples()
""")

manifest_entries.append({
    "zip_name": "02_RISK_MODEL_TRAINING_EVIDENCE.zip",
    "rel_path": "extract_training_input_sample.py",
    "orig_path": "GENERATED FORENSIC EXTRACTION SCRIPT",
    "orig_size": extract_script_path.stat().st_size,
    "orig_sha256": sha256_f(extract_script_path)
})
manifest_entries.append({
    "zip_name": "02_RISK_MODEL_TRAINING_EVIDENCE.zip",
    "rel_path": "TRAINING_INPUT_SAMPLE.npz",
    "orig_path": "GENERATED FORENSIC EXTRACTION (exact array slices from frozen dataset)",
    "orig_size": (z2_stage / "TRAINING_INPUT_SAMPLE.npz").stat().st_size,
    "orig_sha256": sha256_f(z2_stage / "TRAINING_INPUT_SAMPLE.npz")
})
manifest_entries.append({
    "zip_name": "02_RISK_MODEL_TRAINING_EVIDENCE.zip",
    "rel_path": "TRAINING_INPUT_SAMPLE_INDEX.json",
    "orig_path": "GENERATED FORENSIC INDEX",
    "orig_size": (z2_stage / "TRAINING_INPUT_SAMPLE_INDEX.json").stat().st_size,
    "orig_sha256": sha256_f(z2_stage / "TRAINING_INPUT_SAMPLE_INDEX.json")
})

z2_zip_path = OUT_DIR / "02_RISK_MODEL_TRAINING_EVIDENCE.zip"
with zipfile.ZipFile(z2_zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(z2_stage):
        for f in files:
            full_p = Path(root) / f
            rel_p = full_p.relative_to(z2_stage)
            zipf.write(full_p, rel_p)

print(f"ZIP 2 created: {z2_zip_path} ({z2_zip_path.stat().st_size / 1e6:.2f} MB)")


# ==========================================
# ZIP 3: 03_OOD_AND_ONLINE_9CANDIDATE_EXAMPLES.zip
# ==========================================
print("Building ZIP 3: OOD AND ONLINE 9-CANDIDATE EXAMPLES...")
z3_stage = STAGE / "03_ood_online"
z3_stage.mkdir(parents=True)

for ood_ep_id in ["000000", "000001"]:
    ep_src = OOD / "episodes" / ood_ep_id
    if ep_src.exists():
        ep_dst = z3_stage / "ood_episodes" / ood_ep_id
        shutil.copytree(ep_src, ep_dst)
        for f in ep_src.iterdir():
            manifest_entries.append({
                "zip_name": "03_OOD_AND_ONLINE_9CANDIDATE_EXAMPLES.zip",
                "rel_path": f"ood_episodes/{ood_ep_id}/{f.name}",
                "orig_path": str(f),
                "orig_size": f.stat().st_size,
                "orig_sha256": sha256_f(f)
            })

for fname in ["manifest.json", "run_config.yaml", "episode_summaries.jsonl"]:
    src_f = OOD / fname
    if src_f.exists():
        shutil.copy2(src_f, z3_stage / f"ood_{fname}")
        manifest_entries.append({
            "zip_name": "03_OOD_AND_ONLINE_9CANDIDATE_EXAMPLES.zip",
            "rel_path": f"ood_{fname}",
            "orig_path": str(src_f),
            "orig_size": src_f.stat().st_size,
            "orig_sha256": sha256_f(src_f)
        })

dev40_samples_file = ONLINE_DEV40 / "risk_receding_samples.jsonl"
live_rows = []
if dev40_samples_file.exists():
    with open(dev40_samples_file, "r") as f:
        for idx, line in enumerate(f):
            if not line.strip(): continue
            row = json.loads(line)
            if idx < 5 or (row.get("online_risk", {}).get("selected_candidate_index", 0) != 0) or (row.get("online_risk", {}).get("main_score", 0) > 0.5):
                live_rows.append(row)
            if len(live_rows) >= 15:
                break

live_rows_dst = z3_stage / "LIVE_9CANDIDATE_ROWS.jsonl"
with open(live_rows_dst, "w") as f:
    for r in live_rows:
        f.write(json.dumps(r) + "\n")

manifest_entries.append({
    "zip_name": "03_OOD_AND_ONLINE_9CANDIDATE_EXAMPLES.zip",
    "rel_path": "LIVE_9CANDIDATE_ROWS.jsonl",
    "orig_path": str(dev40_samples_file) + " (first 15 representative decisions)",
    "orig_size": live_rows_dst.stat().st_size,
    "orig_sha256": sha256_f(live_rows_dst)
})

for fname in ["online_isaac_runtime.py", "run_isaac_online_risk.py"]:
    src_f = ONLINE_DEV40 / "code_snapshot" / fname
    if not src_f.exists():
        src_f = Path("/home/redafrix/tests/internship/prepared_experiments/dean_isaac_online_ood150_20260817") / fname
    if src_f.exists():
        shutil.copy2(src_f, z3_stage / fname)
        manifest_entries.append({
            "zip_name": "03_OOD_AND_ONLINE_9CANDIDATE_EXAMPLES.zip",
            "rel_path": fname,
            "orig_path": str(src_f),
            "orig_size": src_f.stat().st_size,
            "orig_sha256": sha256_f(src_f)
        })

z3_zip_path = OUT_DIR / "03_OOD_AND_ONLINE_9CANDIDATE_EXAMPLES.zip"
with zipfile.ZipFile(z3_zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(z3_stage):
        for f in files:
            full_p = Path(root) / f
            rel_p = full_p.relative_to(z3_stage)
            zipf.write(full_p, rel_p)

print(f"ZIP 3 created: {z3_zip_path} ({z3_zip_path.stat().st_size / 1e6:.2f} MB)")


# ==========================================
# ZIP 4: 04_COLLECTION_FEATURE_CODE.zip
# ==========================================
print("Building ZIP 4: COLLECTION FEATURE CODE...")
z4_stage = STAGE / "04_code"
z4_stage.mkdir(parents=True)

src_dir = WORKSPACE / "src/risk_collection"
dst_src_dir = z4_stage / "src/risk_collection"
dst_src_dir.mkdir(parents=True)
for f in src_dir.iterdir():
    if f.suffix == ".py":
        shutil.copy2(f, dst_src_dir / f.name)
        manifest_entries.append({
            "zip_name": "04_COLLECTION_FEATURE_CODE.zip",
            "rel_path": f"src/risk_collection/{f.name}",
            "orig_path": str(f),
            "orig_size": f.stat().st_size,
            "orig_sha256": sha256_f(f)
        })

scripts_to_include = [
    (WORKSPACE / "scripts/collect_isaac_risk.py", "scripts/collect_isaac_risk.py"),
    (WORKSPACE / "risk_head_pipeline/train_isaac_topk8.py", "risk_head_pipeline/train_isaac_topk8.py"),
    (WORKSPACE / "risk_head_pipeline/build_frozen_dataset.py", "risk_head_pipeline/build_frozen_dataset.py"),
    (WORKSPACE / "risk_head_pipeline/common.py", "risk_head_pipeline/common.py"),
]
for src_f, rel_name in scripts_to_include:
    if src_f.exists():
        dst_p = z4_stage / rel_name
        dst_p.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_f, dst_p)
        manifest_entries.append({
            "zip_name": "04_COLLECTION_FEATURE_CODE.zip",
            "rel_path": rel_name,
            "orig_path": str(src_f),
            "orig_size": src_f.stat().st_size,
            "orig_sha256": sha256_f(src_f)
        })

feature_map_content = """# Feature and Feature-Pipeline Symbol Mapping

build_uncertainty_49d                 -> src/risk_collection/features.py
DenoisingTrace                        -> src/risk_collection/features.py
TOPK8_INDICES                         -> src/risk_collection/constants.py
UNCERTAINTY_49D_KEYS                  -> src/risk_collection/constants.py
action_statistics                     -> src/risk_collection/ace.py and risk_head_pipeline/common.py
compute_ace_new_training              -> src/risk_collection/ace.py
sample_nine_candidates                -> src/risk_collection/adapter.py
candidate_seeds                       -> src/risk_collection/seeds.py
DeployableHistory                     -> src/risk_collection/history.py
NineCandidateBatch                    -> src/risk_collection/schema.py
collect_isaac_risk.py                 -> scripts/collect_isaac_risk.py (Episode execution and risk_rows serialization)
build_frozen_dataset.py               -> risk_head_pipeline/build_frozen_dataset.py (Extracts Candidate 0 features into frozen .npy arrays)
common.py (feature_tensors)           -> risk_head_pipeline/common.py (Extracts static (51d), history (16,21), action (10,7))
train_isaac_topk8.py                  -> risk_head_pipeline/train_isaac_topk8.py (Trains SeqRiskModel on frozen arrays)
online_isaac_runtime.py               -> online_isaac_runtime.py (Live 9-candidate scoring with candidate-specific 49D vectors)
"""
(z4_stage / "FEATURE_CODE_MAP.txt").write_text(feature_map_content)
manifest_entries.append({
    "zip_name": "04_COLLECTION_FEATURE_CODE.zip",
    "rel_path": "FEATURE_CODE_MAP.txt",
    "orig_path": "GENERATED FORENSIC CODE MAP",
    "orig_size": (z4_stage / "FEATURE_CODE_MAP.txt").stat().st_size,
    "orig_sha256": sha256_f(z4_stage / "FEATURE_CODE_MAP.txt")
})

z4_zip_path = OUT_DIR / "04_COLLECTION_FEATURE_CODE.zip"
with zipfile.ZipFile(z4_zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(z4_stage):
        for f in files:
            full_p = Path(root) / f
            rel_p = full_p.relative_to(z4_stage)
            zipf.write(full_p, rel_p)

print(f"ZIP 4 created: {z4_zip_path} ({z4_zip_path.stat().st_size / 1e6:.2f} MB)")


# ==========================================
# MANIFESTS & SHA256SUMS
# ==========================================
manifest_txt = "FORENSIC EVIDENCE PACKAGE MANIFEST\n"
manifest_txt += "=" * 80 + "\n\n"
for e in manifest_entries:
    manifest_txt += f"ZIP: {e['zip_name']}\n"
    manifest_txt += f"  File: {e['rel_path']}\n"
    manifest_txt += f"  Original Path: {e['orig_path']}\n"
    manifest_txt += f"  Size: {e['orig_size']} bytes\n"
    manifest_txt += f"  SHA256: {e['orig_sha256']}\n\n"

(OUT_DIR / "FORENSIC_PACKAGE_MANIFEST.txt").write_text(manifest_txt)

sha_txt = ""
for zp in [z1_zip_path, z2_zip_path, z3_zip_path, z4_zip_path]:
    z_sha = sha256_f(zp)
    sha_txt += f"{z_sha}  {zp.name}\n"

(OUT_DIR / "PACKAGE_SHA256SUMS.txt").write_text(sha_txt)

total_bytes = sum(zp.stat().st_size for zp in [z1_zip_path, z2_zip_path, z3_zip_path, z4_zip_path])
print(f"\nALL 4 ZIPS CREATED SUCCESSFULLY! Total size: {total_bytes / 1e6:.2f} MB")

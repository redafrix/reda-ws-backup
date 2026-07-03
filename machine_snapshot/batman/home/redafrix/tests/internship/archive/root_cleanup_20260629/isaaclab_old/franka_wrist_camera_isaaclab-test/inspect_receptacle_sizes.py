from pathlib import Path
import subprocess
import json
import re

REPO = Path("/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/franka_wrist_camera_isaaclab")
candidates_file = Path("/tmp/receptacle_candidates.tsv")

rows = []
for line in candidates_file.read_text().splitlines():
    if not line.strip():
        continue
    cat, label, vid, usd = line.split("\t")
    path = REPO / "objects" / usd
    rows.append((cat, label, vid, usd, path))

print("## Receptacle size inspection")
print("| category | variant | usd | exists | approx_note |")
print("|---|---|---|---:|---|")

for cat, label, vid, usd, path in rows:
    exists = path.exists()
    note = ""
    if exists:
        txt = path.read_text(errors="ignore")
        # lightweight scan only; real bounds may need USD APIs, but this gives clues.
        lower = txt.lower()
        if "basket" in lower:
            note += "mentions basket; "
        if "bowl" in lower:
            note += "mentions bowl; "
        if "tray" in lower:
            note += "mentions tray; "
        if "extent" in lower:
            note += "has extent; "
    print(f"| {cat} | {vid} | {usd} | {exists} | {note} |")

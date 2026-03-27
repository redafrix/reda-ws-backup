#!/usr/bin/env bash
set -euo pipefail

vault="/home/redafrix/Documents/Obsidian Vault/Internship Research"
paper_dir="$vault/03 Papers"
final_set="$vault/05 Reviews/Final Must-Read Set.md"
reading_queue="$vault/05 Reviews/Reading Queue.md"
ranked_current="$vault/05 Reviews/Ranked Final Current.md"
ranked_source="$vault/05 Reviews/Ranked Final Current.md"
pdf_summaries="$vault/05 Reviews/PDF-Backed Read-First Summaries.md"

tmp_items="$(mktemp)"
tmp_reasons="$(mktemp)"
tmp_summaries="$(mktemp)"
trap 'rm -f "$tmp_items" "$tmp_reasons" "$tmp_summaries"' EXIT

for f in "$paper_dir"/*.md; do
  if rg -q 'graph/final-must-read' "$f"; then
    name="$(basename "$f" .md)"
    rank="$(sed -n 's/^project_rank: //p' "$f" | head -n1)"
    desired_rank="$(sed -n 's/^desired_rank: //p' "$f" | head -n1)"
    decision="$(sed -n 's/^reader_decision: //p' "$f" | head -n1)"
    if [[ -z "$decision" ]]; then
      decision="keep"
    fi
    if [[ -z "$desired_rank" ]]; then
      desired_rank="$rank"
    fi
    group=0
    if [[ "$decision" == "demote" ]]; then
      group=1
    fi
    printf '%s\t%06d\t%06d\t%s\t%s\n' "$group" "$desired_rank" "$rank" "$name" "$f"
  fi
done | sort -t$'\t' -k1,1n -k2,2n -k3,3n > "$tmp_items"

python3 - "$ranked_source" "$tmp_reasons" <<'PY'
import re, sys
src, out = sys.argv[1], sys.argv[2]
name = None
rows = []
for line in open(src, encoding="utf-8"):
    m = re.match(r"^\d+\. \[\[(?:03 Papers/)?(.+)\]\]\s*$", line)
    if m:
        name = m.group(1)
        continue
    if name and line.startswith("Why: "):
        rows.append(f"{name}\t{line[len('Why: '):].rstrip()}")
        name = None
open(out, "w", encoding="utf-8").write("\n".join(rows))
PY

python3 - "$pdf_summaries" "$tmp_summaries" <<'PY'
import re, sys
src, out = sys.argv[1], sys.argv[2]
rows = []
in_core = False
for raw_line in open(src, encoding="utf-8"):
    line = raw_line.rstrip("\n")
    if line == "## Core Read-First Set":
        in_core = True
        continue
    if in_core and line.startswith("## "):
        break
    if not in_core:
        continue
    m = re.match(r"^\d+\. \[\[(?:03 Papers/)?(.+)\]\]: (.+)\s*$", line)
    if m:
        rows.append(f"{m.group(1)}\t{m.group(2)}")
open(out, "w", encoding="utf-8").write("\n".join(rows))
PY

declare -A WHY
declare -A SUMMARY

while IFS=$'\t' read -r name why; do
  WHY["$name"]="$why"
done < "$tmp_reasons"

while IFS=$'\t' read -r name summary; do
  SUMMARY["$name"]="$summary"
done < "$tmp_summaries"

mapfile -t ordered_lines < "$tmp_items"

rank=0
list_block=""
queue_block=""
ranked_block=""
summary_block=""

for line in "${ordered_lines[@]}"; do
  IFS=$'\t' read -r _ _ _ name path <<< "$line"
  rank=$((rank + 1))
  perl -0pi -e "s/^project_rank: \\d+/project_rank: $rank/m" "$path"

  list_block+="$rank. [[${name}]]"$'\n'
  queue_block+="$rank. [[${name}]]"$'\n'

  why="${WHY[$name]-No reason written yet.}"
  ranked_block+="$rank. [[${name}]]"$'\n'
  ranked_block+="Why: $why"$'\n'$'\n'

  summary="${SUMMARY[$name]-No short summary written yet.}"
  if [[ "$summary" == "No short summary written yet." ]]; then
    summary="$(python3 - "$path" <<'PY'
import re, sys
text = open(sys.argv[1], encoding="utf-8").read()
m = re.search(r"## PDF-Backed Resume\s+Short take:\s*(.+?)\s*(?:\n\n|$)", text, flags=re.S)
if m:
    print(" ".join(m.group(1).split()))
PY
)"
    if [[ -z "$summary" ]]; then
      summary="No short summary written yet."
    fi
  fi
  summary_block+="$rank. [[${name}]]: $summary"$'\n'
done

python3 - "$final_set" "$list_block" <<'PY'
import re, sys
path, block = sys.argv[1], sys.argv[2]
text = open(path, encoding="utf-8").read()
pattern = r"(## Final Must-Read Papers\n\nPapers are ranked here from most important to least important for the current internship target\.\n\n)(.*?)(\n## Fastest Way To Read This Set)"
text = re.sub(pattern, lambda m: m.group(1) + block.rstrip() + "\n" + m.group(3), text, flags=re.S)
text = text.replace("[[05 Reviews/Ranked Final 30]]", "[[05 Reviews/Ranked Final Current]]")
open(path, "w", encoding="utf-8").write(text)
PY

python3 - "$reading_queue" "$queue_block" <<'PY'
import re, sys
path, block = sys.argv[1], sys.argv[2]
text = open(path, encoding="utf-8").read()
pattern = r"(## Read First: Same Task On A New Unseen Object\n\n)(.*?)(\nUse \[\[05 Reviews/Ranked Final [^\]]+\]\] if you only want the ranked order with one-line reasons\.)"
text = re.sub(pattern, lambda m: m.group(1) + block.rstrip() + "\n" + m.group(3), text, flags=re.S)
text = re.sub(r"Use \[\[05 Reviews/Ranked Final [^\]]+\]\] if you only want the ranked order with one-line reasons\.",
              "Use [[05 Reviews/Ranked Final Current]] if you only want the ranked order with one-line reasons.",
              text)
open(path, "w", encoding="utf-8").write(text)
PY

cat > "$ranked_current" <<EOF
---
title: Ranked Final Current
type: review
tags:
  - internship/review
  - internship/ranking
---

# Ranked Final Current

This ranking is rebuilt from each paper's \`reader_decision\` property.

- \`keep\` stays in the main order
- \`demote\` is pushed to the low ranks

## Current Order

${ranked_block%$'\n'$'\n'}
EOF

python3 - "$pdf_summaries" "$summary_block" <<'PY'
import re, sys
path, block = sys.argv[1], sys.argv[2]
text = open(path, encoding="utf-8").read()
pattern = r"(## Core Read-First Set\n\n)(.*?)(\n## (?:Simple Memory Explanations|How To Use This Note))"
text = re.sub(pattern, lambda m: m.group(1) + block.rstrip() + "\n" + m.group(3), text, flags=re.S)
open(path, "w", encoding="utf-8").write(text)
PY

perl -0pi -e 's/\[\[05 Reviews\/Ranked Final 30\]\]/[[05 Reviews\/Ranked Final Current]]/g' "$vault/00 Home.md"

echo "Updated rankings for $rank selected papers."

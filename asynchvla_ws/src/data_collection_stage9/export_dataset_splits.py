from __future__ import annotations
import argparse,json,random
from pathlib import Path

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--dataset',required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--seed',type=int,default=0); args=ap.parse_args(); rows=[json.loads(x) for x in Path(args.dataset).read_text().splitlines() if x.strip()]
 rng=random.Random(args.seed); rng.shuffle(rows); n=len(rows); splits={'train':rows[:int(.7*n)],'calib':rows[int(.7*n):int(.85*n)],'test':rows[int(.85*n):]}; out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
 for k,v in splits.items(): (out/f'{k}.jsonl').write_text('\n'.join(json.dumps(x) for x in v)+'\n')
 print(out)
if __name__=='__main__': main()

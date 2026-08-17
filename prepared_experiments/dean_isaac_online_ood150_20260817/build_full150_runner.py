#!/usr/bin/env python3
from __future__ import annotations
import argparse,subprocess,sys
from pathlib import Path

def replace_once(text:str,old:str,new:str,label:str)->str:
    n=text.count(old)
    if n!=1: raise RuntimeError(f'{label}: expected exactly one anchor, found {n}')
    return text.replace(old,new,1)

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument('--base-builder',type=Path,required=True); ap.add_argument('--source',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
    subprocess.run([sys.executable,str(a.base_builder),'--source',str(a.source),'--output',str(a.output)],check=True)
    t=a.output.read_text()
    t=replace_once(t,'parser.add_argument("--online-role", choices=("shadow", "dev", "holdout"), required=True)','parser.add_argument("--online-role", choices=("shadow", "full150"), required=True)','role choices')
    t=replace_once(t,'"ood_dev_used_for_controller_pair_selection": args.online_role == "dev",\n        "ood_holdout_used_for_controller_pair_selection": False,','"ood150_used_for_controller_pair_selection": args.online_role == "full150",\n        "evaluation_scope": "full_locked_ood150",','role metadata')
    a.output.write_text(t); a.output.chmod(0o755)
    print('FULL150_RUNNER_READY='+str(a.output)); return 0
if __name__=='__main__': raise SystemExit(main())

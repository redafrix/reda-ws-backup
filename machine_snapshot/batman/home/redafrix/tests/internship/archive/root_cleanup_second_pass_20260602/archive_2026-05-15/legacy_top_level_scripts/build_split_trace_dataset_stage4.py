#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,sys,time
from pathlib import Path
import torch
REDA_WS=Path('/media/rootalkhatib/My Passport/reda_ws'); SIM=REDA_WS/'intern_ship_ws/simvla/code/SimVLA_modified'; CKPT=REDA_WS/'intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000'; BACK=REDA_WS/'intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct'; OUTROOT=REDA_WS/'asynchvla_ws/data/processed'
sys.path.insert(0,str(REDA_WS/'asynchvla_ws/src')); sys.path.insert(0,str(SIM))
from datasets.dataset_smolvlm import SmolVLMDataReader
from models.configuration_smolvlm_vla import SmolVLMVLAConfig
from models.modeling_smolvlm_vla import SmolVLMVLA
from models.processing_smolvlm_vla import SmolVLMVLAProcessor
from simvla_trace.trace import generate_actions_trace

def task(p):
    p=Path(p); s=p.stem.removesuffix('_demo'); m=re.search(r'(KITCHEN|LIVING_ROOM|STUDY|LIBERO)_SCENE\d+_',s); s=s[m.end():] if m else s; return s.replace('_',' ')
def meta_for(path,out):
    meta={'dataset_name':'libero_hdf5','data_dir':str(Path(path).parent.parent),'datalist':[{'path':path,'task':task(path),'subset':Path(path).parent.name}], 'num_episodes':1,'state_dim':8,'action_dim':7}
    out.write_text(json.dumps(meta)); return out
def load_model():
    cfg=SmolVLMVLAConfig.from_pretrained(str(CKPT)); cfg.smolvlm_model_path=str(BACK); m=SmolVLMVLA.from_pretrained(str(CKPT),config=cfg); dev=torch.device('cuda' if torch.cuda.is_available() else 'cpu'); return m.to(dev).eval(),dev
def build_part(files,part,max_samples,cap,model,dev,proc,outdir,steps):
    samples=[]; idx=0; metas=outdir/'metas'; metas.mkdir(parents=True,exist_ok=True)
    per=max(1,cap)
    for fi,path in enumerate(files):
        if len(samples)>=max_samples: break
        mp=meta_for(path,metas/f'{part}_{fi:04d}.json')
        ds=SmolVLMDataReader(str(mp),num_actions=10,num_views=3,training=False,action_mode='libero_joint',image_size=384)
        for li,s in enumerate(ds):
            if len(samples)>=max_samples or li>=per: break
            ids=proc.encode_language(s['language_instruction'])['input_ids'].to(dev); img=s['image_input'].unsqueeze(0).to(dev); mask=s['image_mask'].unsqueeze(0).to(dev); prop=s['proprio'].unsqueeze(0).to(dev); exp=s['action'].unsqueeze(0).to(dev)
            expn=model.action_space.normalize_action(exp) if hasattr(model.action_space,'normalize_action') else exp
            tr=generate_actions_trace(model,input_ids=ids,image_input=img,image_mask=mask,proprio=prop,steps=steps,seed=0)
            gen=tr['generated_normalized_action']; err=torch.linalg.vector_norm(gen-expn,dim=-1).squeeze(0)
            cid=f'{part}_ctx_{idx:07d}'
            samples.append({'sample_id':f'{part}_{idx:07d}','context_id':cid,'task_name':task(path),'source_hdf5':path,'source_local_index':li,'language_instruction':s['language_instruction'],'proprio':prop.squeeze(0).detach().cpu(),'pooled_vlm_features':tr['pooled_vlm_features'].squeeze(0).detach().cpu(),'generated_normalized_action':gen.squeeze(0).detach().cpu(),'generated_postprocessed_action':tr['generated_postprocessed_action'].squeeze(0).detach().cpu(),'expert_normalized_action':expn.squeeze(0).detach().cpu(),'expert_postprocessed_action':exp.squeeze(0).detach().cpu(),'per_step_l2_error_normalized':err.detach().cpu(),'chunk_l2_error_normalized':float(err.mean().cpu()),'seed':0,'split':part})
            idx+=1
        if len(samples)%100==0 and samples: print(part,'collected',len(samples),flush=True)
    torch.save({'schema_version':'split_trace_v1','part':part,'num_samples':len(samples),'checkpoint':str(CKPT),'samples':samples}, outdir/f'trace_{part}.pt')
    print('saved',part,len(samples),outdir/f'trace_{part}.pt')
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--manifest',required=True); ap.add_argument('--max-train',type=int,default=1000); ap.add_argument('--max-calib',type=int,default=250); ap.add_argument('--max-test-id',type=int,default=250); ap.add_argument('--max-test-ood',type=int,default=250); ap.add_argument('--cap-per-file',type=int,default=20); ap.add_argument('--steps',type=int,default=10); args=ap.parse_args()
    man=json.load(open(args.manifest)); outdir=OUTROOT/man['split_name']; outdir.mkdir(parents=True,exist_ok=True); (outdir/'manifest_used.json').write_text(json.dumps(man,indent=2)); start=time.time(); model,dev=load_model(); proc=SmolVLMVLAProcessor.from_pretrained(str(BACK))
    specs=[('train',man['train_files'],args.max_train),('calib',man['calib_files'],args.max_calib),('test_id',man.get('test_id_files',[]),args.max_test_id),('test_ood',man.get('test_ood_files',[]),args.max_test_ood)]
    for part,files,mx in specs:
        if files and mx>0: build_part(files,part,mx,args.cap_per_file,model,dev,proc,outdir,args.steps)
    (outdir/'trace_build_summary.json').write_text(json.dumps({'split_name':man['split_name'],'seconds':time.time()-start},indent=2)); print('done',man['split_name'],time.time()-start)
if __name__=='__main__': main()

from __future__ import annotations
import os, sys, math
from pathlib import Path
import numpy as np, torch
from PIL import Image
from torchvision import transforms
REDA_WS = Path(os.environ.get("REDA_WS", "/media/rootalkhatib/My Passport/reda_ws"))
SIM = REDA_WS / "intern_ship_ws/simvla/code/SimVLA_modified"
CKPT_DEFAULT = REDA_WS / "intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000"
BACK_DEFAULT = REDA_WS / "intern_ship_ws/assets/models/huggingface/SmolVLM-500M-Instruct"
for p in [REDA_WS / "asynchvla_ws/src", SIM]:
    if str(p) not in sys.path: sys.path.insert(0, str(p))
from simvla_trace.trace import generate_actions_trace  # noqa
from models.modeling_smolvlm_vla import SmolVLMVLA  # noqa
from models.processing_smolvlm_vla import SmolVLMVLAProcessor  # noqa
from models.configuration_smolvlm_vla import SmolVLMVLAConfig  # noqa

def load_simvla(device=None, ckpt=CKPT_DEFAULT, smolvlm=BACK_DEFAULT, norm_stats=None):
    device = device or torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    cfg = SmolVLMVLAConfig.from_pretrained(str(ckpt)); cfg.smolvlm_model_path = str(smolvlm)
    model = SmolVLMVLA.from_pretrained(str(ckpt), config=cfg).to(device).eval()
    proc = SmolVLMVLAProcessor.from_pretrained(str(smolvlm))
    candidates=[Path(norm_stats)] if norm_stats else []
    candidates += [Path(ckpt)/'norm_stats.json', SIM/'norm_stats/libero_norm.json']
    for c in candidates:
        if c and c.exists() and hasattr(model,'action_space'):
            try: model.action_space.load_norm_stats(str(c)); break
            except Exception: pass
    return model, proc, device

def preprocess_images(image0, image1, image_size=384):
    tf=transforms.Compose([transforms.Resize((image_size,image_size)), transforms.ToTensor(), transforms.Normalize((0.485,0.456,0.406),(0.229,0.224,0.225))])
    img0=tf(Image.fromarray(image0.astype(np.uint8))); img1=tf(Image.fromarray(image1.astype(np.uint8))); pad=torch.zeros_like(img0)
    return torch.stack([img0,img1,pad],0).unsqueeze(0), torch.tensor([[True,True,False]])

def sample_candidate(model, processor, prompt, image0, image1, proprio, seed:int, device, steps:int=10, flowtrace:bool=True):
    images, mask = preprocess_images(image0, image1); images=images.to(device); mask=mask.to(device)
    lang=processor.encode_language([prompt]); lang={k:v.to(device) for k,v in lang.items()}
    prop=torch.tensor(proprio,dtype=torch.float32,device=device).unsqueeze(0)
    out=generate_actions_trace(model,input_ids=lang['input_ids'],image_input=images,image_mask=mask,proprio=prop,steps=steps,seed=int(seed),return_flow_trace=flowtrace,return_initial_noise=False)
    pooled = out.get('pooled_vlm_features')
    if pooled is None:
        vlm = out.get('vlm_features')
        pooled = vlm.mean(dim=1) if vlm is not None and getattr(vlm, 'ndim', 0) >= 3 else vlm
    d={"simvla_seed":int(seed),"candidate_action_normalized":out['generated_normalized_action'][0].detach().cpu(),"candidate_action_env":out['generated_postprocessed_action'][0].detach().cpu(),"pooled_vlm_features":(pooled[0].detach().cpu() if pooled is not None else None),"num_flow_steps":int(out.get('num_flow_steps',steps))}
    if flowtrace and 'flow_trace_summary' in out:
        d['flow_trace_summary']={k:(v.squeeze(0).detach().cpu() if hasattr(v,'detach') else v) for k,v in out['flow_trace_summary'].items()}
    return d

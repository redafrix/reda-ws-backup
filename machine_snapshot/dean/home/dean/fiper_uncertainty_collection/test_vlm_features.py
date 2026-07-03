import sys
import torch
import numpy as np

sys.path.append("/home/redafrix/SimVLA_modified")
sys.path.append("/home/redafrix/LIBERO-PRO")

from models.modeling_smolvlm_vla import SmolVLMVLA
from models.processing_smolvlm_vla import SmolVLMVLAProcessor

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    # Load model
    checkpoint = "/home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000"
    model = SmolVLMVLA.from_pretrained(checkpoint).to(device).eval()
    processor = SmolVLMVLAProcessor.from_pretrained("HuggingFaceTB/SmolVLM-500M-Instruct")
    
    # Preprocessor mock inputs
    # Let's mock a 384x384 image
    img0 = torch.randn(3, 384, 384, device=device)
    img1 = torch.randn(3, 384, 384, device=device)
    pad = torch.zeros_like(img0)
    images = torch.stack([img0, img1, pad], dim=0).unsqueeze(0).to(device)
    image_mask = torch.tensor([[True, True, False]], device=device)
    
    lang = "pick up the black bowl and place it on the plate"
    lang_t = processor.encode_language([lang])
    input_ids = lang_t["input_ids"].to(device)
    
    with torch.inference_mode():
        enc = model.forward_vlm_efficient(images, image_mask, input_ids)
        
    print("VLM features shape:", enc["vlm_features"].shape)
    
if __name__ == "__main__":
    main()

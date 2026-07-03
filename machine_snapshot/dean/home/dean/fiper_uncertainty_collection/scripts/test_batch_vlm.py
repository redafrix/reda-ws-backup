import sys
import torch
import numpy as np
from PIL import Image

sys.path.append("/home/redafrix/SimVLA_modified")
sys.path.append("/home/redafrix/LIBERO-PRO")

from models.modeling_smolvlm_vla import SmolVLMVLA
from models.processing_smolvlm_vla import SmolVLMVLAProcessor

class ImagePreprocessor:
    def __init__(self, image_size: int = 384):
        self.image_size = int(image_size)
        self.mean = torch.tensor([0.485, 0.456, 0.406], dtype=torch.float32).view(3, 1, 1)
        self.std = torch.tensor([0.229, 0.224, 0.225], dtype=torch.float32).view(3, 1, 1)

    def _to_tensor(self, image: np.ndarray) -> torch.Tensor:
        pil = Image.fromarray(image.astype(np.uint8)).resize((self.image_size, self.image_size), Image.BILINEAR)
        arr = np.asarray(pil, dtype=np.float32) / 255.0
        if arr.ndim == 2:
            arr = np.repeat(arr[..., None], 3, axis=-1)
        if arr.shape[-1] > 3:
            arr = arr[..., :3]
        tensor = torch.from_numpy(np.ascontiguousarray(arr)).permute(2, 0, 1)
        return (tensor - self.mean) / self.std

    def __call__(self, image0: np.ndarray, image1: np.ndarray, device: torch.device):
        img0 = self._to_tensor(image0)
        img1 = self._to_tensor(image1)
        pad = torch.zeros_like(img0)
        images = torch.stack([img0, img1, pad], dim=0).unsqueeze(0).to(device)
        image_mask = torch.tensor([[True, True, False]], device=device)
        return images, image_mask

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    model = SmolVLMVLA.from_pretrained("/home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000").to(device).eval()
    processor = SmolVLMVLAProcessor.from_pretrained("HuggingFaceTB/SmolVLM-500M-Instruct")
    image_preprocessor = ImagePreprocessor(384)

    # Make dummy images
    img0 = np.random.randint(0, 255, (128, 128, 3), dtype=np.uint8)
    img1 = np.random.randint(0, 255, (128, 128, 3), dtype=np.uint8)
    task_instruction = "open the middle drawer of the cabinet"

    # Sequential VLM forward pass
    images_t, mask_t = image_preprocessor(img0, img1, device)
    lang_t = processor.encode_language([task_instruction])
    input_ids = lang_t["input_ids"].to(device)
    
    with torch.inference_mode():
        enc = model.forward_vlm_efficient(images_t, mask_t, input_ids)
    seq_feat = enc["vlm_features"].mean(dim=1).squeeze(0).cpu().numpy().astype(np.float32)
    print("Sequential feature shape:", seq_feat.shape)

    # Batched VLM forward pass
    images_batched = torch.cat([images_t, images_t], dim=0) # Batch size = 2
    mask_batched = mask_t.repeat(2, 1)
    input_ids_batched = input_ids.repeat(2, 1)

    with torch.inference_mode():
        enc_batched = model.forward_vlm_efficient(images_batched, mask_batched, input_ids_batched)
    batch_feat = enc_batched["vlm_features"].mean(dim=1).cpu().numpy().astype(np.float32)
    print("Batched feature shape:", batch_feat.shape)

    # Compare
    diff = np.max(np.abs(batch_feat[0] - seq_feat))
    print("Maximum difference between sequential and batched feature:", diff)
    assert diff < 1e-4, "Features mismatch!"
    print("Success: Batched VLM features match sequential features perfectly!")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
SimVLA TDQC Data Collection Server (WebSocket + Uncertainty)
"""

import argparse
import asyncio
import logging
import os
import sys
import traceback
from pathlib import Path
from typing import Any, Dict, Optional

import numpy as np
import torch
from PIL import Image
from torchvision import transforms
import websockets
import torch.nn.functional as F

try:
    import msgpack
    import msgpack_numpy
    HAS_MSGPACK = True
except ImportError:
    HAS_MSGPACK = False

# Add project root to path
WS_ROOT = Path(__file__).parents[4]
ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT))

from models.modeling_smolvlm_vla import SmolVLMVLA
from models.processing_smolvlm_vla import SmolVLMVLAProcessor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global state
model: Optional[SmolVLMVLA] = None
processor: Optional[SmolVLMVLAProcessor] = None
device = "cuda" if torch.cuda.is_available() else "cpu"

CONFIG = {
    "state_dim": 8,
    "action_dim": 7,
    "action_horizon": 10,
    "image_size": 384,
}


def load_model(checkpoint_path: str, norm_stats_path: str = None, smolvlm_model_path: str = None):
    global model, processor
    logger.info(f"Loading SimVLA (TDQC mode) from {checkpoint_path}...")
    model = SmolVLMVLA.from_pretrained(
        checkpoint_path, 
        smolvlm_model_path=smolvlm_model_path,
        predict_uncertainty=True
    )
    model = model.to(device)
    model.eval()
    smolvlm_path = smolvlm_model_path or "HuggingFaceTB/SmolVLM-500M-Instruct"
    processor = SmolVLMVLAProcessor.from_pretrained(smolvlm_path)
    if norm_stats_path and os.path.exists(norm_stats_path):
        logger.info(f"Loading norm stats from: {norm_stats_path}")
        model.action_space.load_norm_stats(norm_stats_path)


def preprocess_images(image0: np.ndarray, image1: np.ndarray):
    image_size = CONFIG["image_size"]
    transform = transforms.Compose([
        transforms.Resize((image_size, image_size)),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
    ])
    img0 = Image.fromarray(image0.astype(np.uint8))
    img1 = Image.fromarray(image1.astype(np.uint8))
    img0_t = transform(img0)
    img1_t = transform(img1)
    padding = torch.zeros_like(img0_t)
    images = torch.stack([img0_t, img1_t, padding], dim=0)
    image_mask = torch.tensor([[True, True, False]])
    return images.unsqueeze(0), image_mask


def decode_numpy(obj):
    if isinstance(obj, dict) and (b'__ndarray__' in obj or '__ndarray__' in obj):
        data_key = b'data' if b'data' in obj else 'data'
        dtype_key = b'dtype' if b'dtype' in obj else 'dtype'
        shape_key = b'shape' if b'shape' in obj else 'shape'
        data = obj[data_key]
        dtype_str = obj[dtype_key]
        shape = obj[shape_key]
        if isinstance(dtype_str, bytes): dtype_str = dtype_str.decode()
        shape = tuple(int(s) for s in shape) if shape and isinstance(shape[0], bytes) else tuple(shape)
        return np.frombuffer(data, dtype=np.dtype(dtype_str)).reshape(shape)
    return obj


def infer(observation: Dict[str, Any]) -> Dict[str, Any]:
    global model, processor
    try:
        image0 = decode_numpy(observation.get("observation/image"))
        image1 = decode_numpy(observation.get("observation/wrist_image"))
        state = decode_numpy(observation.get("observation/state", np.zeros(8)))
        prompt = observation.get("prompt", "")
        
        if not isinstance(image0, np.ndarray): image0 = np.array(image0, dtype=np.uint8)
        if not isinstance(image1, np.ndarray): image1 = np.array(image1, dtype=np.uint8)
        if not isinstance(state, np.ndarray): state = np.array(state, dtype=np.float32)
        
        state = np.pad(state[:8], (0, 8 - len(state[:8])))
        images, image_mask = preprocess_images(image0, image1)
        images, image_mask = images.to(device), image_mask.to(device)
        lang = processor.encode_language([prompt])
        lang = {k: v.to(device) for k, v in lang.items()}
        proprio_tensor = torch.tensor(state, dtype=torch.float32).unsqueeze(0).to(device)
        
        with torch.no_grad():
            out = model.generate_actions_with_uncertainty(
                input_ids=lang['input_ids'],
                image_input=images,
                image_mask=image_mask,
                proprio=proprio_tensor,
                steps=CONFIG["action_horizon"],
            )
        
        return {
            "actions": out["action"].cpu().numpy()[0].tolist(),
            "path_variance": out["path_variance"].cpu().numpy()[0].tolist(),
            "last_step_variance": out["last_step_variance"].cpu().numpy()[0].tolist(),
        }
    except Exception as e:
        logger.error(f"Inference error: {e}")
        return {"actions": [], "path_variance": [], "last_step_variance": []}


async def handle_connection(websocket, path=None):
    logger.info("New connection established")
    metadata = {"model": "SimVLA-TDQC", "uncertainty": True}
    await websocket.send(msgpack_numpy.packb(metadata, use_bin_type=True) if HAS_MSGPACK else json.dumps(metadata))
    
    async for message in websocket:
        try:
            request = msgpack_numpy.unpackb(message, raw=False) if HAS_MSGPACK and isinstance(message, bytes) else json.loads(message)
            logger.info("Received inference request")
            result = infer(request)
            await websocket.send(msgpack.packb(result, use_bin_type=True) if HAS_MSGPACK else json.dumps(result))
        except Exception as e:
            logger.error(f"Error handling request: {e}")


async def serve(host: str, port: int):
    stop = asyncio.Event()
    async with websockets.serve(handle_connection, host, port, max_size=None, compression=None):
        logger.info(f"SimVLA TDQC server listening on {host}:{port}")
        await stop.wait()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", type=str, required=True)
    parser.add_argument("--norm_stats", type=str, default=str(WS_ROOT / "outputs/temp/libero_wrist_norm.json"))
    parser.add_argument("--smolvlm_model", type=str, default=str(WS_ROOT / "assets/models/huggingface/SmolVLM-500M-Instruct"))
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    load_model(args.checkpoint, args.norm_stats, args.smolvlm_model)
    asyncio.run(serve(args.host, args.port))


if __name__ == "__main__":
    main()

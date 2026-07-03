#!/usr/bin/env python3
"""
SimVLA LIBERO Policy Server (WebSocket)

A WebSocket-based policy server for LIBERO evaluation:
- Uses msgpack_numpy serialization for efficient data transfer
- Sends server metadata on connection
- Receives: observation/image, observation/wrist_image, observation/state, prompt
- Returns: {"actions": [...]}

State format (8D): [ee_pos(3), axis_angle(3), gripper_qpos(2)]
Action format (7D): [delta_xyz(3), delta_axisangle(3), gripper_cmd(1)]
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

try:
    import msgpack
    import msgpack_numpy
    HAS_MSGPACK = True
except ImportError:
    HAS_MSGPACK = False
    print("Warning: msgpack_numpy not installed, using JSON fallback")

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from models.modeling_smolvlm_vla import SmolVLMVLA
from models.processing_smolvlm_vla import SmolVLMVLAProcessor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global state
model: Optional[SmolVLMVLA] = None
processor: Optional[SmolVLMVLAProcessor] = None
device = "cuda" if torch.cuda.is_available() else "cpu"

# Configuration
CONFIG = {
    "state_dim": 8,
    "action_dim": 7,
    "action_horizon": 10,
    "image_size": 384,
    "num_action_samples": int(os.environ.get("NUM_ACTION_SAMPLES", "1")),
}

UNCERTAINTY_SCALAR_KEYS = (
    "denoise_initial_mean",
    "denoise_final_mean",
    "denoise_delta",
    "denoise_slope",
    "denoise_final_max",
    "denoise_spike",
    "denoise_final_gripper",
    "denoise_final_rotation_mean",
    "denoise_velocity_norm_mean",
    "denoise_velocity_norm_max",
    "denoise_update_norm_mean",
    "denoise_update_norm_max",
    "denoise_update_norm_final",
    "denoise_update_spike",
    "denoise_update_oscillation_mean",
    "denoise_update_direction_flip_mean",
    "denoise_final_initial_action_l2",
    "sample_action_var_mean",
    "sample_action_var_max",
    "sample_action_l2_mean",
    "sample_action_l2_max",
    "sample_action_translation_var",
    "sample_action_rotation_var",
    "sample_action_gripper_var",
)


def set_seed(seed: int) -> None:
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def load_model(checkpoint_path: str, norm_stats_path: str = None, smolvlm_model_path: str = None, seed: int = 7):
    """Load SimVLA model and processor."""
    global model, processor
    
    logger.info(f"Loading SimVLA from {checkpoint_path}...")
    logger.info(f"Using inference RNG seed: {seed}")
    set_seed(seed)
    
    model = SmolVLMVLA.from_pretrained(checkpoint_path)
    model = model.to(device)
    model.eval()
    
    smolvlm_path = smolvlm_model_path or "HuggingFaceTB/SmolVLM-500M-Instruct"
    processor = SmolVLMVLAProcessor.from_pretrained(smolvlm_path)
    
    if norm_stats_path and os.path.exists(norm_stats_path):
        logger.info(f"Loading norm stats from: {norm_stats_path}")
        model.action_space.load_norm_stats(norm_stats_path)
        if hasattr(model.action_space, 'state_norm_stats') and model.action_space.state_norm_stats:
            logger.info(f"   State norm: mean={model.action_space.state_norm_stats.mean[:3].tolist()}")
        if hasattr(model.action_space, 'action_norm_stats') and model.action_space.action_norm_stats:
            logger.info(f"   Action norm: mean={model.action_space.action_norm_stats.mean[:3].tolist()}")
    else:
        logger.warning("No norm_stats loaded!")
    
    logger.info(f"Model loaded! Device: {device}, Image size: {CONFIG['image_size']}x{CONFIG['image_size']}")


def preprocess_images(image0: np.ndarray, image1: np.ndarray):
    """Preprocess images to model input format."""
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
    
    # Pad to 3 views (model processes all views together)
    padding = torch.zeros_like(img0_t)
    images = torch.stack([img0_t, img1_t, padding], dim=0)
    image_mask = torch.tensor([[True, True, False]])
    
    return images.unsqueeze(0), image_mask


def decode_numpy(obj):
    """Decode numpy array from msgpack_numpy dict format."""
    if isinstance(obj, dict):
        if b'__ndarray__' in obj or '__ndarray__' in obj:
            data_key = b'data' if b'data' in obj else 'data'
            dtype_key = b'dtype' if b'dtype' in obj else 'dtype'
            shape_key = b'shape' if b'shape' in obj else 'shape'
            
            data = obj[data_key]
            dtype_str = obj[dtype_key]
            shape = obj[shape_key]
            
            if isinstance(dtype_str, bytes):
                dtype_str = dtype_str.decode()
            
            if shape and isinstance(shape[0], bytes):
                shape = tuple(int(s) for s in shape)
            else:
                shape = tuple(shape)
            
            return np.frombuffer(data, dtype=np.dtype(dtype_str)).reshape(shape)
    return obj


def infer(observation: Dict[str, Any]) -> Dict[str, Any]:
    """Run inference on a single observation."""
    global model, processor
    
    try:
        # Extract observation fields
        image0 = observation.get("observation/image")
        image1 = observation.get("observation/wrist_image")
        state = observation.get("observation/state", np.zeros(8))
        prompt = observation.get("prompt", "")
        
        # Decode msgpack_numpy format if needed
        image0 = decode_numpy(image0)
        image1 = decode_numpy(image1)
        state = decode_numpy(state)
        
        # Ensure numpy arrays
        if not isinstance(image0, np.ndarray):
            image0 = np.array(image0, dtype=np.uint8)
        if not isinstance(image1, np.ndarray):
            image1 = np.array(image1, dtype=np.uint8)
        if not isinstance(state, np.ndarray):
            state = np.array(state, dtype=np.float32)
        
        if len(state) < 8:
            state = np.pad(state, (0, 8 - len(state)))
        state = state[:8]
        
        # Preprocess images
        images, image_mask = preprocess_images(image0, image1)
        images = images.to(device)
        image_mask = image_mask.to(device)
        
        # Encode language instruction
        lang = processor.encode_language([prompt])
        lang = {k: v.to(device) for k, v in lang.items()}
        
        # Proprioception
        proprio_tensor = torch.tensor(state, dtype=torch.float32).unsqueeze(0).to(device)
        
        # Inference
        with torch.no_grad():
            if CONFIG["num_action_samples"] > 1:
                action_samples = model.generate_action_samples(
                    input_ids=lang['input_ids'],
                    image_input=images,
                    image_mask=image_mask,
                    proprio=proprio_tensor,
                    steps=CONFIG["action_horizon"],
                    num_action_samples=CONFIG["num_action_samples"],
                )
                actions = action_samples[:, 0].cpu().numpy()[0]
                result_payload = {
                    "actions": actions,
                    "action_samples": action_samples.cpu().numpy()[0],
                }
                if not getattr(model.config, "predict_uncertainty", False):
                    return result_payload

            if getattr(model.config, "predict_uncertainty", False):
                result = model.generate_actions_with_uncertainty(
                    input_ids=lang['input_ids'],
                    image_input=images,
                    image_mask=image_mask,
                    proprio=proprio_tensor,
                    steps=CONFIG["action_horizon"],
                    num_action_samples=CONFIG["num_action_samples"],
                )
                actions = result["action"].cpu().numpy()[0]
                path_variance = result["path_variance"].cpu().numpy()[0]
                last_step_variance = result["last_step_variance"].cpu().numpy()[0]

                path_step_mean = path_variance.mean(axis=-1)
                last_step_mean = last_step_variance.mean(axis=-1)

                uncertainty = {
                    "path_variance": path_variance.tolist(),
                    "last_step_variance": last_step_variance.tolist(),
                    "path_step_mean": path_step_mean.tolist(),
                    "last_step_mean": last_step_mean.tolist(),
                    "mean_path_var": float(path_variance.mean()),
                    "mean_last_var": float(last_step_variance.mean()),
                    "max_path_var": float(path_variance.max()),
                    "max_last_var": float(last_step_variance.max()),
                }
                for key in UNCERTAINTY_SCALAR_KEYS:
                    if key in result:
                        uncertainty[key] = float(result[key].cpu().numpy()[0])
                if "sample_action_variance" in result:
                    uncertainty["sample_action_variance"] = result["sample_action_variance"].cpu().numpy()[0].tolist()

                return {
                    "actions": actions,
                    "action_samples": result.get("action_samples", torch.empty(0)).cpu().numpy()[0]
                    if "action_samples" in result
                    else action_samples.cpu().numpy()[0]
                    if CONFIG["num_action_samples"] > 1
                    else None,
                    "uncertainty": uncertainty,
                }

            actions = model.generate_actions(
                input_ids=lang['input_ids'],
                image_input=images,
                image_mask=image_mask,
                proprio=proprio_tensor,
                steps=CONFIG["action_horizon"],
            )

        actions = actions.cpu().numpy()[0]
        return {"actions": actions}
        
    except Exception as e:
        logger.error(f"Inference error: {e}")
        traceback.print_exc()
        return {"actions": np.zeros((CONFIG["action_horizon"], CONFIG["action_dim"]))}


async def handle_connection(websocket, path=None):
    """Handle a WebSocket connection."""
    logger.info(f"Connection from {websocket.remote_address} opened")
    
    try:
        # Send server metadata on connection
        metadata = {
            "model": "SimVLA",
            "action_dim": CONFIG["action_dim"],
            "action_horizon": CONFIG["action_horizon"],
            "image_size": CONFIG["image_size"],
        }
        if HAS_MSGPACK:
            await websocket.send(msgpack_numpy.packb(metadata, use_bin_type=True))
        else:
            import json
            await websocket.send(json.dumps(metadata))
        
        # Process requests
        async for message in websocket:
            try:
                # Parse request
                if HAS_MSGPACK and isinstance(message, bytes):
                    request = msgpack_numpy.unpackb(message, raw=False)
                else:
                    import json
                    request = json.loads(message)
                
                # Run inference
                result = infer(request)
                
                # Send response (convert numpy to list for compatibility)
                actions = result["actions"]
                if isinstance(actions, np.ndarray):
                    actions = actions.tolist()
                
                response_data = {"actions": actions}
                if "action_samples" in result and result["action_samples"] is not None:
                    samples = result["action_samples"]
                    if isinstance(samples, np.ndarray):
                        samples = samples.tolist()
                    response_data["action_samples"] = samples
                if "uncertainty" in result:
                    response_data["uncertainty"] = result["uncertainty"]
                
                if HAS_MSGPACK:
                    import msgpack
                    response = msgpack.packb(response_data, use_bin_type=True)
                else:
                    import json
                    response = json.dumps(response_data)
                
                await websocket.send(response)
                
            except Exception as e:
                logger.error(f"Error processing message: {e}")
                traceback.print_exc()
                error_msg = f"Error: {str(e)}"
                await websocket.send(error_msg)
                
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        logger.info(f"Connection from {websocket.remote_address} closed")


async def serve(host: str, port: int):
    """Start the WebSocket server."""
    logger.info(f"Creating SimVLA server (host: {host}, port: {port})")
    
    async with websockets.serve(handle_connection, host, port, max_size=None, compression=None):
        logger.info(f"SimVLA server listening on {host}:{port}")
        await asyncio.Future()


def main():
    parser = argparse.ArgumentParser(description="SimVLA LIBERO Server (WebSocket)")
    parser.add_argument("--checkpoint", type=str, required=True,
                        help="Path to SimVLA checkpoint")
    parser.add_argument("--norm_stats", type=str, default=None,
                        help="Path to normalization stats JSON")
    parser.add_argument("--smolvlm_model", type=str, 
                        default="HuggingFaceTB/SmolVLM-500M-Instruct",
                        help="SmolVLM model path or HuggingFace repo")
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--seed", type=int, default=7,
                        help="Random seed for stochastic action sampling during inference")
    parser.add_argument("--num_action_samples", type=int, default=CONFIG["num_action_samples"],
                        help="Number of parallel flow samples for action-disagreement uncertainty. 1 disables it.")
    
    args = parser.parse_args()
    
    if not HAS_MSGPACK:
        logger.warning("msgpack_numpy not installed! Install with: pip install msgpack-numpy")
    
    load_model(args.checkpoint, args.norm_stats, args.smolvlm_model, seed=args.seed)
    CONFIG["num_action_samples"] = max(1, int(args.num_action_samples))
    
    logger.info(f"Starting SimVLA server on {args.host}:{args.port}")
    logger.info(f"  Image size: {CONFIG['image_size']}x{CONFIG['image_size']}")
    logger.info(f"  Action horizon: {CONFIG['action_horizon']}")
    logger.info(f"  Action disagreement samples: {CONFIG['num_action_samples']}")
    
    asyncio.run(serve(args.host, args.port))


if __name__ == "__main__":
    main()

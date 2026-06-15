"""
SmolVLM-VLA Model

HuggingFace-compatible Vision-Language-Action policy using SmolVLM-500M-Instruct
as the visual-language backbone.

Key differences from FlorenceVLA:
  - Uses SmolVLM-500M-Instruct (efficient 500M parameter model)
  - 512x512 image input (SmolVLM-500M uses 512x512 patches)
  - All views processed together by SmolVLM, no aux_visual_inputs
  - Unified VLM output for multi-view inputs
"""

from __future__ import annotations

import logging
import os
import math
import traceback
from typing import Any, Dict

import numpy as np
import torch
import torch.nn.functional as F
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from PIL import Image
import uvicorn
import json_numpy
import cv2
from safetensors.torch import load_file as load_safetensors_file

from transformers import PreTrainedModel, AutoProcessor, AutoModelForImageTextToText
from .transformer_smolvlm import SmolVLMActionTransformer
from .action_hub import build_action_space
from .configuration_smolvlm_vla import SmolVLMVLAConfig


class SmolVLMVLA(PreTrainedModel):
    """
    SmolVLM-VLA: HuggingFace-compatible Vision-Language-Action policy.

    Components:
      • SmolVLM-500M-Instruct backbone (vision-language)
      • SmolVLMActionTransformer (flow matching action head)
      • Action space (pre/post-processing + loss)
      
    Key differences from FlorenceVLA:
      • All camera views are input to VLM together (no aux_visual_inputs)
      • 512x512 image resolution (SmolVLM-500M uses 512x512 patches)
      • Efficient 500M parameter model
    """
    config_class = SmolVLMVLAConfig
    base_model_prefix = "smolvlm_vla"
    supports_gradient_checkpointing = True
    _keys_to_ignore_on_load_missing = [
        r"transformer\.velocity_head\..*",
        r"transformer\.logvar_head\..*",
        r"transformer\.velocity_final_layer\..*",
        r"transformer\.logvar_final_layer\..*",
    ]
    _keys_to_ignore_on_load_unexpected = [
        r"transformer\.action_decoder\..*",
        r"transformer\.final_layer\..*",
    ]

    def __init__(self, config: SmolVLMVLAConfig, *args, **kwargs):
        super().__init__(config, *args, **kwargs)

        # Core settings
        self.num_actions: int = config.num_actions
        self.use_proprio: bool = config.use_proprio
        self.action_mode: str = config.action_mode.lower()
        self.image_size: int = config.image_size
        self.num_views: int = config.num_views
        
        # Action space
        self.action_space = build_action_space(config.action_mode.lower())
        dim_action = self.action_space.dim_action
        dim_proprio = getattr(self.action_space, "dim_proprio", dim_action)

        # SmolVLM backbone
        logging.info(f"Loading SmolVLM from: {config.smolvlm_model_path}")
        self.vlm = AutoModelForImageTextToText.from_pretrained(
            config.smolvlm_model_path,
            torch_dtype=torch.float32,  # Use float32 for training stability
            trust_remote_code=True,
        )
        self.vlm_processor = AutoProcessor.from_pretrained(
            config.smolvlm_model_path,
            trust_remote_code=True,
        )
        
        # Get SmolVLM hidden size from model config
        # SmolVLM-500M has hidden_size from text_config
        vlm_hidden_size = self.vlm.config.text_config.hidden_size
        logging.info(f"SmolVLM hidden size: {vlm_hidden_size}")

        # DiT/AdaLN mode setting
        self.use_adaln = getattr(config, 'use_adaln', False)
        
        # Flow matching action head (SmolVLM version - no aux_visual)
        self.transformer = SmolVLMActionTransformer(
            hidden_size=config.hidden_size,
            vlm_hidden_size=vlm_hidden_size,
            depth=config.depth,
            num_heads=config.num_heads,
            mlp_ratio=config.mlp_ratio,
            dim_action=dim_action,
            dim_propio=dim_proprio,
            dim_time=config.dim_time,
            max_len_seq=config.max_len_seq,
            use_adaln=self.use_adaln,
            predict_uncertainty=getattr(config, "predict_uncertainty", False),
        )
        self._init_uncertainty_heads_from_legacy()
        
        if self.use_adaln:
            logging.info("✓ DiT/AdaLN mode enabled: conditions injected via Adaptive Layer Norm")
        else:
            logging.info("✓ Concat mode enabled: conditions concatenated to sequence")

        # Deferred FastAPI app
        self.app: FastAPI | None = None

    def _init_uncertainty_heads_from_legacy(self) -> None:
        if not getattr(self.config, "predict_uncertainty", False):
            return

        if self.use_adaln:
            if hasattr(self.transformer, "velocity_final_layer"):
                nn = torch.nn
                nn.init.constant_(self.transformer.logvar_final_layer.linear.weight, 0.0)
                nn.init.constant_(self.transformer.logvar_final_layer.linear.bias, -2.0)
        else:
            if hasattr(self.transformer, "velocity_head"):
                torch.nn.init.constant_(self.transformer.logvar_head.weight, 0.0)
                torch.nn.init.constant_(self.transformer.logvar_head.bias, -2.0)

    def _upgrade_legacy_state_dict_for_uncertainty(
        self,
        state_dict: Dict[str, torch.Tensor],
        prefix: str = "",
    ) -> None:
        if not getattr(self.config, "predict_uncertainty", False):
            return

        transformer_prefix = prefix + "transformer."
        if self.use_adaln:
            legacy_base = transformer_prefix + "final_layer."
            velocity_base = transformer_prefix + "velocity_final_layer."
            if legacy_base + "linear.weight" in state_dict:
                for suffix in (
                    "norm.weight",
                    "norm.bias",
                    "adaLN_modulation.0.weight",
                    "adaLN_modulation.0.bias",
                    "adaLN_modulation.1.weight",
                    "adaLN_modulation.1.bias",
                    "linear.weight",
                    "linear.bias",
                ):
                    legacy_key = legacy_base + suffix
                    velocity_key = velocity_base + suffix
                    if legacy_key in state_dict and velocity_key not in state_dict:
                        state_dict[velocity_key] = state_dict.pop(legacy_key)
        else:
            legacy_weight = transformer_prefix + "action_decoder.weight"
            legacy_bias = transformer_prefix + "action_decoder.bias"
            velocity_weight = transformer_prefix + "velocity_head.weight"
            velocity_bias = transformer_prefix + "velocity_head.bias"
            if legacy_weight in state_dict and velocity_weight not in state_dict:
                state_dict[velocity_weight] = state_dict.pop(legacy_weight)
            if legacy_bias in state_dict and velocity_bias not in state_dict:
                state_dict[velocity_bias] = state_dict.pop(legacy_bias)

    def load_state_dict(self, state_dict: Dict[str, torch.Tensor], strict: bool = True, assign: bool = False):
        upgraded_state = dict(state_dict)
        self._upgrade_legacy_state_dict_for_uncertainty(upgraded_state)
        return super().load_state_dict(upgraded_state, strict=strict, assign=assign)

    def _maybe_copy_legacy_output_head(self, pretrained_model_name_or_path: str) -> None:
        if not getattr(self.config, "predict_uncertainty", False):
            return

        model_path = os.path.join(pretrained_model_name_or_path, "model.safetensors")
        if not os.path.exists(model_path):
            return

        state_dict = load_safetensors_file(model_path, device="cpu")
        if self.use_adaln:
            legacy_base = "transformer.final_layer."
            if legacy_base + "linear.weight" in state_dict and hasattr(self.transformer, "velocity_final_layer"):
                src = self.transformer.velocity_final_layer
                if hasattr(src.norm, "weight") and src.norm.weight is not None and legacy_base + "norm.weight" in state_dict:
                    src.norm.weight.data.copy_(state_dict[legacy_base + "norm.weight"])
                if hasattr(src.norm, "bias") and src.norm.bias is not None and legacy_base + "norm.bias" in state_dict:
                    src.norm.bias.data.copy_(state_dict[legacy_base + "norm.bias"])
                src.adaLN_modulation[1].weight.data.copy_(state_dict[legacy_base + "adaLN_modulation.1.weight"])
                src.adaLN_modulation[1].bias.data.copy_(state_dict[legacy_base + "adaLN_modulation.1.bias"])
                src.linear.weight.data.copy_(state_dict[legacy_base + "linear.weight"])
                src.linear.bias.data.copy_(state_dict[legacy_base + "linear.bias"])
                torch.nn.init.constant_(self.transformer.logvar_final_layer.linear.weight, 0.0)
                torch.nn.init.constant_(self.transformer.logvar_final_layer.linear.bias, -2.0)
        else:
            if "transformer.action_decoder.weight" in state_dict and hasattr(self.transformer, "velocity_head"):
                self.transformer.velocity_head.weight.data.copy_(state_dict["transformer.action_decoder.weight"])
                self.transformer.velocity_head.bias.data.copy_(state_dict["transformer.action_decoder.bias"])
                torch.nn.init.constant_(self.transformer.logvar_head.weight, 0.0)
                torch.nn.init.constant_(self.transformer.logvar_head.bias, -2.0)

    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: str | os.PathLike, *model_args, **kwargs):
        model = super().from_pretrained(pretrained_model_name_or_path, *model_args, **kwargs)
        model._maybe_copy_legacy_output_head(str(pretrained_model_name_or_path))
        return model

    # ============================= SmolVLM encoder =============================
    def forward_vlm(
        self,
        pixel_values: torch.FloatTensor,    # [B, V, C, H, W] - multi-view images
        image_mask: torch.Tensor,           # [B, V] (bool or 0/1)
        language_instruction: list[str] | None = None,  # Optional text prompts
    ) -> Dict[str, torch.Tensor]:
        """
        Encode multi-view images via SmolVLM2.
        
        All views are processed together by SmolVLM, producing unified features.
        No aux_visual_inputs needed - everything goes through VLM.

        Returns:
          { "vlm_features": [B, T_enc, D] }
        """
        if pixel_values.dim() == 6:
            if pixel_values.size(2) == 1:
                pixel_values = pixel_values.squeeze(2)
            else:
                pixel_values = pixel_values[:, :, 0]
            
        B, V, C, H, W = pixel_values.shape
        device = pixel_values.device
        
        # Prepare images for SmolVLM - flatten views and filter by mask
        # SmolVLM can handle multiple images as part of multi-image inference
        batch_features = []
        
        for b in range(B):
            # Get valid images for this sample
            valid_mask = image_mask[b].bool()
            valid_images = pixel_values[b][valid_mask]  # [num_valid, C, H, W]
            
            if valid_images.shape[0] == 0:
                raise ValueError("At least one image view must be valid per batch.")
            
            # Convert to PIL images for SmolVLM processor
            pil_images = []
            for img_tensor in valid_images:
                # Denormalize and convert to PIL
                img_np = img_tensor.permute(1, 2, 0).cpu().numpy()
                # Assuming normalized with ImageNet stats, denormalize
                img_np = img_np * np.array([0.229, 0.224, 0.225]) + np.array([0.485, 0.456, 0.406])
                img_np = (img_np * 255).clip(0, 255).astype(np.uint8)
                pil_images.append(Image.fromarray(img_np))
            
            # Build message for SmolVLM with multiple images
            content = []
            for i, img in enumerate(pil_images):
                content.append({"type": "image", "image": img})
            
            # Add text prompt if provided
            if language_instruction is not None and b < len(language_instruction):
                content.append({"type": "text", "text": language_instruction[b]})
            else:
                content.append({"type": "text", "text": "Describe the robot's observation."})
            
            messages = [{"role": "user", "content": content}]
            
            # Process with SmolVLM
            inputs = self.vlm_processor.apply_chat_template(
                messages,
                add_generation_prompt=True,
                tokenize=True,
                return_dict=True,
                return_tensors="pt",
            ).to(device)
            
            # Get encoder outputs (hidden states) instead of generating text
            with torch.no_grad():
                outputs = self.vlm(
                    **inputs,
                    output_hidden_states=True,
                    return_dict=True,
                )
            
            # Use the last hidden state as features
            # Shape: [1, seq_len, hidden_size]
            hidden_states = outputs.hidden_states[-1]
            batch_features.append(hidden_states.squeeze(0))  # [seq_len, hidden_size]
        
        # Pad to same length and stack
        max_len = max(f.shape[0] for f in batch_features)
        hidden_size = batch_features[0].shape[-1]
        
        padded_features = torch.zeros(B, max_len, hidden_size, device=device, dtype=batch_features[0].dtype)
        for b, feat in enumerate(batch_features):
            padded_features[b, :feat.shape[0]] = feat
        
        return {"vlm_features": padded_features}

    def forward_vlm_efficient(
        self,
        pixel_values: torch.FloatTensor,    # [B, V, C, H, W] - Already preprocessed
        image_mask: torch.Tensor,           # [B, V]
        input_ids: torch.LongTensor | None = None,  # [B, L] - Pre-tokenized text
    ) -> Dict[str, torch.Tensor]:
        """
        Efficient VLM forward for training - uses FULL VLM to fuse vision and language.
        
        Key improvement: Uses complete VLM forward (vision encoder + language model)
        to get features that fuse visual and linguistic information, rather than
        just using the vision encoder alone.
        
        Pipeline:
          pixel_values → vision_encoder → image_features
                                               ↓
          input_ids → text_embeddings ─────────┤
                                               ↓
                                 [image_feats, text_embeds] (concat)
                                               ↓
                                 language_model forward
                                               ↓
                                 fused VLM features → return
        
        Returns:
          { "vlm_features": [B, T_enc, D] }
        """
        if pixel_values.dim() == 6:
            if pixel_values.size(2) == 1:
                pixel_values = pixel_values.squeeze(2)
            else:
                pixel_values = pixel_values[:, :, 0]
        B, V, C, H, W = pixel_values.shape
        device = pixel_values.device
        dtype = pixel_values.dtype
        
        # ========== Step 1: Get vision features ==========
        # Flatten images: [B, V, C, H, W] -> [B*V, C, H, W]
        flat_images = pixel_values.flatten(0, 1)
        flat_mask = image_mask.view(-1).bool()
        
        # Get valid images
        valid_images = flat_images[flat_mask]  # [num_valid, C, H, W]
        
        if valid_images.shape[0] == 0:
            raise ValueError("At least one image view must be valid.")
        
        # Encode images through SmolVLM's vision encoder (SigLIP)
        vision_outputs = self.vlm.model.vision_model(
            pixel_values=valid_images,
            output_hidden_states=True,
            return_dict=True,
        )
        
        # Get image features and project to LM space
        image_features = vision_outputs.last_hidden_state  # [num_valid, num_patches, vision_hidden]
        
        # Project to language model space using the connector/projector
        if hasattr(self.vlm.model, 'connector'):
            image_features = self.vlm.model.connector(image_features)
        elif hasattr(self.vlm.model, 'multi_modal_projector'):
            image_features = self.vlm.model.multi_modal_projector(image_features)
        
        # ========== Step 2: Get text embeddings ==========
        # Idefics3 (SmolVLM) uses 'text_model' instead of 'language_model'
        text_embeds = self.vlm.model.text_model.get_input_embeddings()(input_ids)  # [B, L, D]
        
        # ========== Step 3: Build combined sequence per sample ==========
        # For each sample, concatenate: [image_features_view1, ..., image_features_viewN, text_embeds]
        hidden_size = image_features.shape[-1]
        num_patches = image_features.shape[1]
        
        # Reconstruct image features with batch structure
        full_image_features = image_features.new_zeros(B * V, num_patches, hidden_size)
        full_image_features[flat_mask] = image_features
        full_image_features = full_image_features.view(B, V, num_patches, hidden_size)
        
        # Count valid views per sample for proper concatenation
        valid_per_sample = image_mask.sum(dim=1).int()  # [B]
        
        batch_inputs_embeds = []
        max_seq_len = 0
        
        for b in range(B):
            # Get valid image features for this sample
            num_valid = valid_per_sample[b].item()
            sample_image_feats = full_image_features[b, :num_valid]  # [num_valid, num_patches, D]
            sample_image_feats = sample_image_feats.reshape(-1, hidden_size)  # [num_valid*num_patches, D]
            
            # Get text embeddings for this sample
            sample_text_embeds = text_embeds[b]  # [L, D]
            
            # Concatenate: [image_features, text_embeds]
            combined = torch.cat([sample_image_feats, sample_text_embeds], dim=0)  # [T, D]
            batch_inputs_embeds.append(combined)
            max_seq_len = max(max_seq_len, combined.shape[0])
        
        # ========== Step 4: Pad and stack ==========
        padded_inputs_embeds = torch.zeros(B, max_seq_len, hidden_size, device=device, dtype=dtype)
        attention_mask = torch.zeros(B, max_seq_len, device=device, dtype=torch.long)
        
        for b, embeds in enumerate(batch_inputs_embeds):
            seq_len = embeds.shape[0]
            padded_inputs_embeds[b, :seq_len] = embeds
            attention_mask[b, :seq_len] = 1
        
        # ========== Step 5: Forward through text model (Idefics3/SmolVLM) ==========
        # This fuses visual and linguistic information through the full transformer
        lm_outputs = self.vlm.model.text_model(
            inputs_embeds=padded_inputs_embeds,
            attention_mask=attention_mask,
            output_hidden_states=True,
            return_dict=True,
        )
        
        # Use the last hidden state as VLM features
        # This now contains fused vision-language representations
        vlm_features = lm_outputs.last_hidden_state  # [B, max_seq_len, D]
        
        return {"vlm_features": vlm_features}

    # ================================= training =================================
    def forward(
        self,
        input_ids: torch.LongTensor,        # [B, L] - tokenized language instruction
        image_input: torch.FloatTensor,     # [B, V, C, H, W]
        image_mask: torch.Tensor,           # [B, V]
        proprio: torch.Tensor,              # [B, dim_proprio]
        action: torch.Tensor,               # [B, T=num_actions, D=dim_action]
    ) -> Dict[str, torch.Tensor]:
        """
        Flow Matching training.
        
        1) Time sampling: t ~ Beta(1.5, 1) * 0.999 + 0.001
        2) Interpolation: x_t = t * noise + (1-t) * actions
        3) Target: velocity u_t = noise - actions
        4) Model predicts v_t, compute MSE(v_t, u_t)
        """
        enc = self.forward_vlm_efficient(image_input, image_mask, input_ids)

        B = input_ids.shape[0]
        device = input_ids.device
        
        # Beta(1.5, 1) time sampling
        beta_dist = torch.distributions.Beta(
            torch.tensor(1.5, device=device), 
            torch.tensor(1.0, device=device)
        )
        t = beta_dist.sample((B,)) * 0.999 + 0.001

        # Normalize action and proprio
        if hasattr(self.action_space, 'normalize_action'):
            action_norm = self.action_space.normalize_action(action)
        elif hasattr(self.action_space, 'normalize'):
            action_norm = self.action_space.normalize(action)
        else:
            action_norm = action
            
        if hasattr(self.action_space, 'normalize_state'):
            proprio_norm = self.action_space.normalize_state(proprio)
        elif hasattr(self.action_space, 'normalize'):
            proprio_norm = self.action_space.normalize(proprio)
        else:
            proprio_norm = proprio
        
        # Flow Matching
        noise = torch.randn_like(action_norm)
        t_expanded = t.view(-1, 1, 1)
        x_t = t_expanded * noise + (1 - t_expanded) * action_norm
        u_t = noise - action_norm

        # Model prediction (no aux_visual_inputs for SmolVLM)
        pred = self.transformer(
            vlm_features=enc["vlm_features"],
            action_with_noise=x_t,
            t=t,
            proprio=proprio_norm,
        )

        if getattr(self.config, "predict_uncertainty", False):
            v_t, logvar_t = pred
            var_t = F.softplus(logvar_t) + self.config.uncertainty_eps
            beta = self.config.uncertainty_beta
            sq_err = torch.square(v_t - u_t)
            weight = var_t.pow(beta).detach()
            nonnegative_const = -0.5 * math.log(self.config.uncertainty_eps)
            per_elem = weight * (sq_err / (2.0 * var_t) + 0.5 * torch.log(var_t) + nonnegative_const)
            velocity_nll_loss = per_elem.mean()
            mse_proxy = sq_err.mean()
            return {
                "loss": velocity_nll_loss,
                "velocity_nll_loss": velocity_nll_loss,
                "mse_proxy": mse_proxy,
                "mean_var": var_t.mean(),
                "mean_logvar": logvar_t.mean(),
            }

        v_t = pred
        velocity_loss = torch.mean(torch.square(v_t - u_t))
        return {"loss": velocity_loss, "velocity_loss": velocity_loss}

    # ================================= inference =================================
    @torch.no_grad()
    def generate_actions(
        self,
        input_ids: torch.LongTensor,
        image_input: torch.FloatTensor,
        image_mask: torch.Tensor,
        proprio: torch.Tensor,
        steps: int = 10,
    ) -> torch.Tensor:
        """
        Flow Matching inference (Euler integration).
        
        1) Initialize x_t = noise (t=1)
        2) Loop t from 1 to 0:
           - Model predicts velocity v_t
           - Euler update: x_t = x_t + dt * v_t
        3) Final x_0 ≈ target action
        """
        self.eval()
        enc = self.forward_vlm_efficient(image_input, image_mask, input_ids)

        B = input_ids.shape[0]
        D = self.action_space.dim_action
        device = proprio.device
        dtype = proprio.dtype

        # Normalize proprio
        if hasattr(self.action_space, 'normalize_state'):
            proprio_norm = self.action_space.normalize_state(proprio)
        elif hasattr(self.action_space, 'normalize'):
            proprio_norm = self.action_space.normalize(proprio)
        else:
            proprio_norm = proprio

        # Euler integration
        steps = max(1, int(steps))
        dt = -1.0 / steps
        
        x_t = torch.randn(B, self.num_actions, D, device=device, dtype=dtype)
        t = 1.0
        
        while t > -dt / 2:
            t_tensor = torch.full((B,), t, device=device, dtype=dtype)
            
            pred = self.transformer(
                vlm_features=enc["vlm_features"],
                action_with_noise=x_t,
                proprio=proprio_norm,
                t=t_tensor,
            )

            if getattr(self.config, "predict_uncertainty", False):
                v_t, _ = pred
            else:
                v_t = pred

            x_t = x_t + dt * v_t
            t = t + dt
        
        return self.action_space.postprocess(x_t)

    @torch.no_grad()
    def generate_actions_with_uncertainty(
        self,
        input_ids: torch.LongTensor,
        image_input: torch.FloatTensor,
        image_mask: torch.Tensor,
        proprio: torch.Tensor,
        steps: int = 10,
    ) -> Dict[str, torch.Tensor]:
        self.eval()
        enc = self.forward_vlm_efficient(image_input, image_mask, input_ids)

        B = input_ids.shape[0]
        D = self.action_space.dim_action
        device = proprio.device
        dtype = proprio.dtype

        if hasattr(self.action_space, 'normalize_state'):
            proprio_norm = self.action_space.normalize_state(proprio)
        elif hasattr(self.action_space, 'normalize'):
            proprio_norm = self.action_space.normalize(proprio)
        else:
            proprio_norm = proprio

        steps = max(1, int(steps))
        dt = -1.0 / steps

        x_t = torch.randn(B, self.num_actions, D, device=device, dtype=dtype)
        path_variance = torch.zeros_like(x_t)
        last_step_variance = torch.zeros_like(x_t)
        t = 1.0

        while t > -dt / 2:
            t_tensor = torch.full((B,), t, device=device, dtype=dtype)
            pred = self.transformer(
                vlm_features=enc["vlm_features"],
                action_with_noise=x_t,
                proprio=proprio_norm,
                t=t_tensor,
            )

            if getattr(self.config, "predict_uncertainty", False):
                v_t, logvar_t = pred
                var_t = F.softplus(logvar_t) + self.config.uncertainty_eps
                last_step_variance = var_t
                path_variance = path_variance + (dt * dt) * var_t
            else:
                v_t = pred

            x_t = x_t + dt * v_t
            t = t + dt

        action = self.action_space.postprocess(x_t)
        return {
            "action": action,
            "path_variance": path_variance,
            "last_step_variance": last_step_variance,
        }

    # =============================== FastAPI service =============================
    def _build_app(self, processor):
        """Build FastAPI app for SmolVLM-VLA inference."""
        if self.app is not None:
            return

        app = FastAPI()

        @app.post("/act")
        def act(payload: Dict[str, Any]):
            try:
                self.eval()
                # Decode images
                images = []
                for key in ("image0", "image1", "image2"):
                    if key not in payload:
                        continue
                    v = json_numpy.loads(payload[key])
                    if isinstance(v, np.ndarray):
                        if v.ndim == 1:
                            v = cv2.imdecode(v, cv2.IMREAD_COLOR)
                        images.append(Image.fromarray(v))
                    elif isinstance(v, (list, tuple)):
                        images.append(Image.fromarray(np.array(v)))
                    elif isinstance(v, str):
                        images.append(Image.open(v))
                        
                if not images:
                    return JSONResponse({"error": "No valid images found."}, status_code=400)

                # Process inputs
                inputs = processor(images, payload["language_instruction"])
                if not {"input_ids", "image_input", "image_mask"}.issubset(inputs):
                    return JSONResponse({"error": "Processor returned incomplete inputs."}, status_code=400)

                # Build proprio tensor
                proprio = torch.as_tensor(np.asarray(json_numpy.loads(payload["proprio"])))

                # Align to model device/dtype
                device = next(self.parameters()).device
                dtype = next(self.parameters()).dtype

                def to_model(t: torch.Tensor) -> torch.Tensor:
                    if not isinstance(t, torch.Tensor):
                        t = torch.as_tensor(t)
                    return t.to(device=device, dtype=dtype) if t.is_floating_point() else t.to(device=device)

                inputs = {k: to_model(v) for k, v in inputs.items()}
                inputs["proprio"] = to_model(proprio.unsqueeze(0))

                # Inference
                steps = int(payload.get("steps", 10))
                action = self.generate_actions(**inputs, steps=steps).squeeze(0).float().cpu().numpy()
                return JSONResponse({"action": action.tolist()})

            except Exception:
                logging.error(traceback.format_exc())
                return JSONResponse({"error": "Request failed"}, status_code=400)

        self.app = app

    def run(self, processor, host: str = "0.0.0.0", port: int = 8000):
        """Launch the FastAPI service."""
        self._build_app(processor)
        assert self.app is not None
        uvicorn.run(self.app, host=host, port=port)

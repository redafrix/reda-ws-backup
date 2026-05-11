from __future__ import annotations

from typing import Optional, Tuple, Dict, Any

import torch
import torch.nn as nn

try:
    from mamba_ssm import Mamba
    from mamba_ssm.utils.generation import InferenceParams
except ImportError:
    Mamba = None
    InferenceParams = None


class RMSNorm(nn.Module):
    def __init__(self, d_model: int, eps: float = 1e-5):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(d_model))

    def forward(self, x):
        output = x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)
        return output * self.weight


class TDQCMambaCalibrator(nn.Module):
    """
    Mamba-based TDQC calibrator.

    Input:
        uncertainty feature sequence, [B, T, F]
        suite_id embedding (additive)

    Output:
        p_fail sequence, [B, T]
    """

    def __init__(
        self,
        input_dim: int,
        hidden_dim: int = 128,
        num_layers: int = 2,
        dropout: float = 0.0,
        d_state: int = 16,
        d_conv: int = 4,
        expand: int = 2,
    ):
        super().__init__()
        if Mamba is None:
            print("Warning: mamba_ssm not found. Model will not be functional.")

        self.input_dim = int(input_dim)
        self.hidden_dim = int(hidden_dim)
        self.num_layers = int(num_layers)

        self.input_proj = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            RMSNorm(hidden_dim),
            nn.SiLU(),
        )

        self.layers = nn.ModuleList([
            Mamba(
                d_model=hidden_dim,
                d_state=d_state,
                d_conv=d_conv,
                expand=expand,
                layer_idx=i,
            )
            for i in range(num_layers)
        ])

        self.norms = nn.ModuleList([
            RMSNorm(hidden_dim) for _ in range(num_layers)
        ])

        self.head = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.SiLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, 1),
        )

    def forward(self, x: torch.Tensor, suite_embed: Optional[torch.Tensor] = None) -> torch.Tensor:
        """
        x: [B, T, F]
        suite_embed: [B, F] or [B, hidden_dim] - optional additive context

        Returns:
            p_fail: [B, T]
        """
        z = self.input_proj(x)
        
        if suite_embed is not None:
            # If suite_embed is F-dim, project it first. 
            # For simplicity, we assume suite_embed is already hidden_dim or matches input_proj output.
            if suite_embed.shape[-1] != z.shape[-1]:
                # This would need a separate projection if we pass raw suite features.
                # Assuming additive integration as per blueprint.
                pass 
            z = z + suite_embed.unsqueeze(1)

        for layer, norm in zip(self.layers, self.norms):
            z = layer(z)
            z = norm(z)

        logits = self.head(z).squeeze(-1)
        p_fail = torch.sigmoid(logits)
        return p_fail

    @torch.no_grad()
    def step(
        self,
        phi_t: torch.Tensor,
        state: Optional[Dict[str, Any]] = None,
        suite_embed: Optional[torch.Tensor] = None,
    ):
        """
        Stateful online inference for one control step (O(1)).

        phi_t: [F] or [B, F]
        state: Dictionary containing 'inference_params'
        suite_embed: [B, hidden_dim]

        Returns:
            p_fail_t, updated_state
        """
        if phi_t.ndim == 1:
            phi_t = phi_t.unsqueeze(0)
        
        batch_size = phi_t.shape[0]
        
        if state is None:
            # Initialize InferenceParams for all layers
            inference_params = InferenceParams(
                max_seqlen=100000, # Large enough for any episode
                max_batch_size=batch_size
            )
            state = {"inference_params": inference_params}
        
        inference_params = state["inference_params"]
        
        # [B, 1, F]
        x = phi_t.unsqueeze(1)
        z = self.input_proj(x)
        
        if suite_embed is not None:
            z = z + suite_embed.unsqueeze(1)

        # Mamba .step is usually handled via forward with inference_params
        for layer, norm in zip(self.layers, self.norms):
            # Mamba's forward method handles single-step if inference_params is provided
            z = layer(z, inference_params=inference_params)
            z = norm(z)

        p_fail = torch.sigmoid(self.head(z).squeeze(-1)).squeeze(1)
        return p_fail, state


def hard_update(target: nn.Module, source: nn.Module) -> None:
    target.load_state_dict(source.state_dict())


@torch.no_grad()
def soft_update(target: nn.Module, source: nn.Module, tau: float = 0.005) -> None:
    for p_targ, p_src in zip(target.parameters(), source.parameters()):
        p_targ.data.mul_(1.0 - tau)
        p_targ.data.add_(tau * p_src.data)

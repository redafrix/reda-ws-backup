from __future__ import annotations

from typing import Optional, Tuple, Dict, Any

import torch
import torch.nn as nn
import torch.nn.functional as F


class RMSNorm(nn.Module):
    def __init__(self, dim: int, eps: float = 1e-6):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim))

    def _norm(self, x):
        return x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)

    def forward(self, x):
        output = self._norm(x.float()).type_as(x)
        return output * self.weight


class SwiGLU(nn.Module):
    def __init__(self, dim: int, hidden_dim: int):
        super().__init__()
        self.w1 = nn.Linear(dim, hidden_dim, bias=False)
        self.w2 = nn.Linear(hidden_dim, dim, bias=False)
        self.w3 = nn.Linear(dim, hidden_dim, bias=False)

    def forward(self, x):
        return self.w2(F.silu(self.w1(x)) * self.w3(x))


class CausalConv1d(nn.Module):
    def __init__(self, dim: int, kernel_size: int = 3):
        super().__init__()
        self.kernel_size = kernel_size
        self.conv = nn.Conv1d(dim, dim, kernel_size, padding=kernel_size - 1, groups=dim)
        self.act = nn.SiLU()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: [B, T, D]
        x = x.transpose(1, 2) # [B, D, T]
        x = self.conv(x)
        x = x[:, :, :-(self.kernel_size - 1)] # Keep strict causality!
        return self.act(x.transpose(1, 2))


class TransformerBlock(nn.Module):
    def __init__(self, dim: int, n_heads: int, dropout: float = 0.0):
        super().__init__()
        self.n_heads = n_heads
        self.attention_norm = RMSNorm(dim)
        self.ffn_norm = RMSNorm(dim)
        self.dropout = nn.Dropout(dropout)

        self.wq = nn.Linear(dim, dim, bias=False)
        self.wk = nn.Linear(dim, dim, bias=False)
        self.wv = nn.Linear(dim, dim, bias=False)
        self.wo = nn.Linear(dim, dim, bias=False)
        
        # Upgrade 2: QK-Norm
        self.q_norm = RMSNorm(dim)
        self.k_norm = RMSNorm(dim)

        ffn_hidden_dim = int(2 * 4 * dim / 3)
        self.feed_forward = SwiGLU(dim, ffn_hidden_dim)

    def forward(self, x, mask=None):
        # x: [B, T, D]
        h = x + self.dropout(self.attention(self.attention_norm(x), mask))
        out = h + self.dropout(self.feed_forward(self.ffn_norm(h)))
        return out

    def attention(self, x, mask=None):
        bsz, seqlen, dim = x.shape
        # Upgrade 2: Apply QK-Norm
        queries = self.q_norm(self.wq(x))
        keys = self.k_norm(self.wk(x))
        values = self.wv(x)

        queries = queries.view(bsz, seqlen, self.n_heads, dim // self.n_heads).transpose(1, 2)
        keys = keys.view(bsz, seqlen, self.n_heads, dim // self.n_heads).transpose(1, 2)
        values = values.view(bsz, seqlen, self.n_heads, dim // self.n_heads).transpose(1, 2)

        # Upgrade 2: is_causal=False because ALiBi handles it via mask
        output = F.scaled_dot_product_attention(
            queries,
            keys,
            values,
            attn_mask=mask,
            dropout_p=self.dropout.p if self.training else 0.0,
            is_causal=False,
        )

        output = output.transpose(1, 2).contiguous().view(bsz, seqlen, dim)
        return self.wo(output)

    def forward_with_kv(self, x, kv_cache=None):
        # NOTE: ALiBi inference with KV cache needs distance-based bias adjustment
        # For simplicity in this training script, we focus on the batch forward pass
        # but we keep the structure.
        norm_x = self.attention_norm(x)
        bsz, seqlen, dim = norm_x.shape

        queries = self.q_norm(self.wq(norm_x))
        keys = self.k_norm(self.wk(norm_x))
        values = self.wv(norm_x)

        queries = queries.view(bsz, seqlen, self.n_heads, dim // self.n_heads).transpose(1, 2)
        keys = keys.view(bsz, seqlen, self.n_heads, dim // self.n_heads).transpose(1, 2)
        values = values.view(bsz, seqlen, self.n_heads, dim // self.n_heads).transpose(1, 2)

        if kv_cache is not None:
            k_prev, v_prev = kv_cache
            keys = torch.cat([k_prev, keys], dim=2)
            values = torch.cat([v_prev, values], dim=2)

        new_kv = (keys, values)

        output = F.scaled_dot_product_attention(
            queries,
            keys,
            values,
            attn_mask=None,
            dropout_p=0.0,
            is_causal=False,
        )

        output = output.transpose(1, 2).contiguous().view(bsz, seqlen, dim)
        attn_out = self.wo(output)

        h = x + self.dropout(attn_out)
        out = h + self.dropout(self.feed_forward(self.ffn_norm(h)))
        return out, new_kv


class TDQCTransformerCalibrator(nn.Module):
    """
    Causal Transformer TDQC calibrator v2 (OOD Optimized).
    """

    def __init__(
        self,
        input_dim: int,
        hidden_dim: int = 256,
        n_heads: int = 8,
        num_layers: int = 4,
        dropout: float = 0.1,
        max_seq_len: int = 512,
    ):
        super().__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers

        self.input_proj = nn.Linear(input_dim, hidden_dim)
        
        # Upgrade 1: Replace absolute pos_emb with CausalConv1d
        self.causal_conv = CausalConv1d(dim=hidden_dim, kernel_size=3)

        self.blocks = nn.ModuleList(
            [TransformerBlock(hidden_dim, n_heads, dropout) for _ in range(num_layers)]
        )

        self.norm = RMSNorm(hidden_dim)
        self.head = nn.Linear(hidden_dim, 1)
        self.dropout = nn.Dropout(dropout)

    def forward(
        self,
        x: torch.Tensor,
        mask: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        """
        x: [B, T, F]
        mask: [B, T] (1 for valid, 0 for padding)

        Returns:
            p_fail: [B, T]
        """
        B, T, F = x.shape

        # Upgrade 1: Input Projection -> Causal Conv -> Dropout
        x = self.input_proj(x)  # [B, T, D]
        x = self.causal_conv(x) # [B, T, D]
        x = self.dropout(x)

        # Upgrade 2: ALiBi Mask Construction
        base_mask = torch.triu(torch.full((T, T), float('-inf'), device=x.device), diagonal=1)
        m = torch.arange(1, self.blocks[0].n_heads + 1, device=x.device)
        slopes = (2.0 ** (-8.0 * m / self.blocks[0].n_heads)).view(1, -1, 1, 1)
        distances = torch.clamp(torch.arange(T, device=x.device).unsqueeze(1) - torch.arange(T, device=x.device).unsqueeze(0), min=0).unsqueeze(0).unsqueeze(0)
        alibi_bias = (distances * -1) * slopes

        if mask is not None: # Apply padding mask
            pad_mask = mask.view(B, 1, 1, T).expand(B, self.blocks[0].n_heads, T, T)
            float_pad_mask = torch.where(pad_mask == 1.0, 0.0, float('-inf'))
            attn_mask = base_mask.view(1, 1, T, T) + alibi_bias + float_pad_mask
        else:
            attn_mask = base_mask.view(1, 1, T, T) + alibi_bias

        for block in self.blocks:
            x = block(x, mask=attn_mask)

        x = self.norm(x)
        logits = self.head(x).squeeze(-1)  # [B, T]
        p_fail = torch.sigmoid(logits)  # [B, T]
        return p_fail

    @torch.no_grad()
    def step(
        self,
        phi_t: torch.Tensor,
        state: Optional[Dict[str, Any]] = None,
    ) -> Tuple[torch.Tensor, Dict[str, Any]]:
        # NOTE: Online inference with CausalConv + ALiBi requires specialized state management
        # for the convolution window and relative distances.
        # This implementation remains a structural placeholder for runtime consistency.
        if phi_t.ndim == 1:
            phi_t = phi_t.unsqueeze(0)

        if state is None:
            step = 0
            kv_caches = [None] * self.num_layers
        else:
            step = state["step"]
            kv_caches = state["kv_caches"]

        z = self.input_proj(phi_t.unsqueeze(1))
        # (Conv and ALiBi logic would go here for a true online step)
        
        x = z
        new_kv_caches = []
        for i, block in enumerate(self.blocks):
            x, kv = block.forward_with_kv(x, kv_caches[i])
            new_kv_caches.append(kv)

        x = self.norm(x)
        p_fail = torch.sigmoid(self.head(x).squeeze(-1)).squeeze(1)

        return p_fail, {"step": step + 1, "kv_caches": new_kv_caches}


def hard_update(target: nn.Module, source: nn.Module) -> None:
    target.load_state_dict(source.state_dict())


@torch.no_grad()
def soft_update(target: nn.Module, source: nn.Module, tau: float = 0.005) -> None:
    for p_targ, p_src in zip(target.parameters(), source.parameters()):
        p_targ.data.mul_(1.0 - tau)
        p_targ.data.add_(tau * p_src.data)

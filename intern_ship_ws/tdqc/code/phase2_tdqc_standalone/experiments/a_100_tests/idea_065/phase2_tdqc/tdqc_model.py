from __future__ import annotations

from typing import Optional, Tuple, Dict, Any
import math
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


class SinusoidalPositionalEncoding(nn.Module):
    def __init__(self, d_model: int, max_len: int = 5000):
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)
        self.register_buffer('pe', pe)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: [B, T, D]
        return x + self.pe[:, :x.size(1)]


class CausalConv1d(nn.Module):
    def __init__(self, dim: int, kernel_size: int = 3):
        super().__init__()
        self.kernel_size = kernel_size
        self.conv = nn.Conv1d(dim, dim, kernel_size, padding=kernel_size - 1, groups=dim)
        self.act = nn.SiLU()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = x.transpose(1, 2)
        x = self.conv(x)
        x = x[:, :, :-(self.kernel_size - 1)]
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
        
        self.q_norm = RMSNorm(dim)
        self.k_norm = RMSNorm(dim)
        self.qk_temp = nn.Parameter(torch.tensor(10.0))

        ffn_hidden_dim = int(2 * 4 * dim / 3)
        self.feed_forward = SwiGLU(dim, ffn_hidden_dim)

    def forward(self, x, mask=None):
        # Action 4: norm_first=True behavior implemented via pre-norm pattern
        h = x + self.dropout(self.attention(self.attention_norm(x), mask))
        out = h + self.dropout(self.feed_forward(self.ffn_norm(h)))
        return out

    def attention(self, x, mask=None):
        bsz, seqlen, dim = x.shape
        queries = self.q_norm(self.wq(x)) * self.qk_temp
        keys = self.k_norm(self.wk(x))
        values = self.wv(x)

        queries = queries.view(bsz, seqlen, self.n_heads, dim // self.n_heads).transpose(1, 2)
        keys = keys.view(bsz, seqlen, self.n_heads, dim // self.n_heads).transpose(1, 2)
        values = values.view(bsz, seqlen, self.n_heads, dim // self.n_heads).transpose(1, 2)

        output = F.scaled_dot_product_attention(
            queries, keys, values,
            attn_mask=mask,
            dropout_p=self.dropout.p if self.training else 0.0,
            is_causal=False,
        )
        output = output.transpose(1, 2).contiguous().view(bsz, seqlen, dim)
        return self.wo(output)


class TDQCTransformerCalibrator(nn.Module):
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
        
        # Action 2: Sinusoidal PE
        self.pos_encoder = SinusoidalPositionalEncoding(hidden_dim, max_len=max_seq_len)
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
        B, T, D = x.shape

        x = self.input_proj(x)
        
        # Action 1: Relative Feature Mapping
        # Subtract the starting state to blind the model to Step 0 scene bias.
        x = x - x[:, :1, :].detach() 
        
        x = self.pos_encoder(x)
        x = self.causal_conv(x)
        x = self.dropout(x)

        # Causal mask construction (ALiBi omitted for pure sinusoidal approach as requested)
        causal_mask = torch.triu(torch.full((T, T), float('-inf'), device=x.device), diagonal=1)
        
        if mask is not None:
            # mask is [B, T], 1 for valid, 0 for pad
            float_pad_mask = torch.where(mask == 1, 0.0, float('-inf'))
            attn_mask = causal_mask.unsqueeze(0).unsqueeze(0) + float_pad_mask.view(B, 1, 1, T)
        else:
            attn_mask = causal_mask.unsqueeze(0).unsqueeze(0)

        for block in self.blocks:
            x = block(x, mask=attn_mask)

        x = self.norm(x)
        logits = self.head(x).squeeze(-1)
        p_fail = torch.sigmoid(logits)
        return p_fail


def hard_update(target: nn.Module, source: nn.Module) -> None:
    target.load_state_dict(source.state_dict())


@torch.no_grad()
def soft_update(target: nn.Module, source: nn.Module, tau: float = 0.005) -> None:
    for p_targ, p_src in zip(target.parameters(), source.parameters()):
        p_targ.data.mul_(1.0 - tau)
        p_targ.data.add_(tau * p_src.data)

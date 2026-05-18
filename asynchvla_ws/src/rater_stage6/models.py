from __future__ import annotations
import torch
import torch.nn as nn

class ResidualBlock(nn.Module):
    def __init__(self, dim, dropout=0.05):
        super().__init__(); self.net=nn.Sequential(nn.LayerNorm(dim), nn.Linear(dim,dim*2), nn.GELU(), nn.Dropout(dropout), nn.Linear(dim*2,dim))
    def forward(self,x): return x+self.net(x)

class MLPRegressor(nn.Module):
    def __init__(self, in_dim, hidden=256, depth=2, out_dim=1, softplus=True):
        super().__init__(); self.inp=nn.Sequential(nn.LayerNorm(in_dim), nn.Linear(in_dim,hidden), nn.GELU())
        self.blocks=nn.Sequential(*[ResidualBlock(hidden) for _ in range(depth)])
        self.out=nn.Linear(hidden,out_dim); self.softplus=nn.Softplus() if softplus else nn.Identity()
    def forward(self,x): return self.softplus(self.out(self.blocks(self.inp(x))))

class ContextGatedAction(nn.Module):
    def __init__(self, context_dim, action_dim, hidden=256):
        super().__init__(); self.ctx=nn.Sequential(nn.LayerNorm(context_dim), nn.Linear(context_dim,hidden), nn.GELU(), nn.Linear(hidden,hidden*2))
        self.act=nn.Sequential(nn.LayerNorm(action_dim), nn.Linear(action_dim,hidden), nn.GELU())
        self.head=nn.Sequential(ResidualBlock(hidden), ResidualBlock(hidden), nn.LayerNorm(hidden), nn.Linear(hidden,1), nn.Softplus())
    def forward(self,x):
        c=x[:,:self.context_dim] if hasattr(self,'context_dim') else None
        raise RuntimeError('context_dim not set')

class ContextGatedActionFixed(nn.Module):
    def __init__(self, context_dim, action_dim, hidden=256):
        super().__init__(); self.context_dim=context_dim
        self.ctx=nn.Sequential(nn.LayerNorm(context_dim), nn.Linear(context_dim,hidden), nn.GELU(), nn.Linear(hidden,hidden*2))
        self.act=nn.Sequential(nn.LayerNorm(action_dim), nn.Linear(action_dim,hidden), nn.GELU())
        self.head=nn.Sequential(ResidualBlock(hidden), ResidualBlock(hidden), nn.LayerNorm(hidden), nn.Linear(hidden,1), nn.Softplus())
    def forward(self,x):
        c=x[:,:self.context_dim]; a=x[:,self.context_dim:]
        scale,shift=self.ctx(c).chunk(2,dim=-1); h=self.act(a); h=h*(1+0.1*torch.tanh(scale))+0.1*shift
        return self.head(h).squeeze(-1)

class PerStepHead(nn.Module):
    def __init__(self,in_dim,hidden=256):
        super().__init__(); self.base=MLPRegressor(in_dim,hidden=hidden,depth=2,out_dim=10,softplus=True)
    def forward(self,x): return self.base(x)

class HeteroscedasticHead(nn.Module):
    def __init__(self,in_dim,hidden=256):
        super().__init__(); self.backbone=nn.Sequential(nn.LayerNorm(in_dim), nn.Linear(in_dim,hidden), nn.GELU(), ResidualBlock(hidden), ResidualBlock(hidden), nn.LayerNorm(hidden)); self.mean=nn.Sequential(nn.Linear(hidden,1), nn.Softplus()); self.logvar=nn.Linear(hidden,1)
    def forward(self,x):
        h=self.backbone(x); return self.mean(h).squeeze(-1), self.logvar(h).squeeze(-1).clamp(-6,4)

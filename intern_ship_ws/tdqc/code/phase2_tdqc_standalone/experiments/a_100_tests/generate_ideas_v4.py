import os, shutil

base_dir = '/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/a_100_tests'

for i in range(115, 125):
    dest = f'{base_dir}/idea_{i:03d}'
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(f'{base_dir}/idea_101', dest)
    os.makedirs(f'{dest}/runs', exist_ok=True)

models = {}

models[115] = '''class TDQCTransformerCalibrator(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int = 256, num_layers: int = 4, dropout: float = 0.1):
        super().__init__()
        layers = []
        in_d = input_dim
        for _ in range(num_layers):
            layers.extend([nn.Linear(in_d, hidden_dim), RMSNorm(hidden_dim), nn.SiLU(), nn.Dropout(dropout)])
            in_d = hidden_dim
        self.mlp = nn.Sequential(*layers)
        self.head = nn.Linear(hidden_dim, 1)

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        logits = self.head(self.mlp(x)).squeeze(-1)
        return torch.sigmoid(logits)
'''

models[116] = '''class TDQCTransformerCalibrator(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int = 256, num_layers: int = 4, dropout: float = 0.1):
        super().__init__()
        self.in_proj = nn.Linear(input_dim, hidden_dim)
        self.convs = nn.ModuleList([nn.Conv1d(hidden_dim, hidden_dim, kernel_size=3, padding=1) for _ in range(num_layers)])
        self.norms = nn.ModuleList([RMSNorm(hidden_dim) for _ in range(num_layers)])
        self.silu = nn.SiLU()
        self.head = nn.Linear(hidden_dim, 1)

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        x = self.in_proj(x)
        x_c = x.transpose(1, 2)
        for conv, norm in zip(self.convs, self.norms):
            x_c = x_c + self.silu(norm(conv(x_c).transpose(1, 2)).transpose(1, 2))
        logits = self.head(x_c.transpose(1, 2)).squeeze(-1)
        return torch.sigmoid(logits)
'''

models[117] = '''class TDQCTransformerCalibrator(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int = 256, num_layers: int = 4, dropout: float = 0.1):
        super().__init__()
        var_dim = max(1, input_dim - 7)
        layers = []
        in_d = var_dim
        for _ in range(num_layers):
            layers.extend([nn.Linear(in_d, hidden_dim), RMSNorm(hidden_dim), nn.SiLU(), nn.Dropout(dropout)])
            in_d = hidden_dim
        self.mlp = nn.Sequential(*layers)
        self.head = nn.Linear(hidden_dim, 1)

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        x_var = x[:, :, 7:] if x.shape[-1] > 7 else x
        logits = self.head(self.mlp(x_var)).squeeze(-1)
        return torch.sigmoid(logits)
'''

models[118] = '''class TDQCTransformerCalibrator(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int = 256, num_layers: int = 4, dropout: float = 0.1):
        super().__init__()
        in_d = input_dim * 3
        layers = []
        for _ in range(num_layers):
            layers.extend([nn.Linear(in_d, hidden_dim), RMSNorm(hidden_dim), nn.SiLU(), nn.Dropout(dropout)])
            in_d = hidden_dim
        self.mlp = nn.Sequential(*layers)
        self.head = nn.Linear(hidden_dim, 1)

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        v = torch.zeros_like(x)
        v[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        a = torch.zeros_like(x)
        a[:, 1:, :] = v[:, 1:, :] - v[:, :-1, :]
        logits = self.head(self.mlp(torch.cat([x, v, a], dim=-1))).squeeze(-1)
        return torch.sigmoid(logits)
'''

models[119] = '''class TDQCTransformerCalibrator(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int = 256, num_layers: int = 4, dropout: float = 0.1):
        super().__init__()
        layers = []
        in_d = input_dim
        for _ in range(num_layers):
            layers.extend([nn.Linear(in_d, hidden_dim), RMSNorm(hidden_dim), nn.SiLU(), nn.Dropout(dropout)])
            in_d = hidden_dim
        self.mlp = nn.Sequential(*layers)
        self.head = nn.Linear(hidden_dim, 1)

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        fast_ema = torch.zeros_like(x)
        slow_ema = torch.zeros_like(x)
        af, as_ = 0.3, 0.05
        fast_ema[:, 0] = x[:, 0]
        slow_ema[:, 0] = x[:, 0]
        for t in range(1, x.size(1)):
            fast_ema[:, t] = af * x[:, t] + (1 - af) * fast_ema[:, t-1]
            slow_ema[:, t] = as_ * x[:, t] + (1 - as_) * slow_ema[:, t-1]
        logits = self.head(self.mlp(fast_ema - slow_ema)).squeeze(-1)
        return torch.sigmoid(logits)
'''

models[120] = '''class TDQCTransformerCalibrator(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int = 256, num_layers: int = 4, dropout: float = 0.1):
        super().__init__()
        self.in_proj = nn.Linear(input_dim, hidden_dim)
        self.blocks = nn.ModuleList([TransformerBlock(hidden_dim, 8, dropout) for _ in range(num_layers)])
        self.norm = RMSNorm(hidden_dim)
        self.head = nn.Linear(hidden_dim, 1)

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        B, T, _ = x.shape
        x = self.in_proj(x)
        causal = torch.triu(torch.ones(T, T, device=x.device), diagonal=1).bool()
        window = torch.tril(torch.ones(T, T, device=x.device), diagonal=-5).bool()
        attn_mask = (causal | window).unsqueeze(0).unsqueeze(0)
        float_mask = torch.zeros_like(attn_mask, dtype=torch.float32)
        float_mask.masked_fill_(attn_mask, float('-inf'))
        if mask is not None:
            float_mask = float_mask + (mask == 0).view(B, 1, 1, T).float() * float('-inf')
        for block in self.blocks:
            x = block(x, mask=float_mask)
        logits = self.head(self.norm(x)).squeeze(-1)
        return torch.sigmoid(logits)
'''

models[121] = '''class TDQCTransformerCalibrator(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int = 256, num_layers: int = 4, dropout: float = 0.1):
        super().__init__()
        layers = []
        in_d = input_dim
        for _ in range(num_layers):
            layers.extend([nn.Linear(in_d, hidden_dim), RMSNorm(hidden_dim), nn.SiLU(), nn.Dropout(dropout)])
            in_d = hidden_dim
        self.mlp = nn.Sequential(*layers)
        self.head = nn.Linear(hidden_dim, 1)

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        delta = torch.zeros_like(x)
        delta[:, 1:, :] = x[:, 1:, :] - x[:, :-1, :]
        smoothed = torch.zeros_like(delta)
        for t in range(delta.size(1)):
            smoothed[:, t, :] = delta[:, max(0, t-4):t+1, :].mean(dim=1)
        logits = self.head(self.mlp(smoothed)).squeeze(-1)
        return torch.sigmoid(logits)
'''

models[122] = '''class TDQCTransformerCalibrator(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int = 256, num_layers: int = 4, dropout: float = 0.1):
        super().__init__()
        self.inst_norm = nn.InstanceNorm1d(input_dim, affine=False)
        layers = []
        in_d = input_dim
        for _ in range(num_layers):
            layers.extend([nn.Linear(in_d, hidden_dim), RMSNorm(hidden_dim), nn.SiLU(), nn.Dropout(dropout)])
            in_d = hidden_dim
        self.mlp = nn.Sequential(*layers)
        self.head = nn.Linear(hidden_dim, 1)

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        z = self.inst_norm(x.transpose(1, 2)).transpose(1, 2)
        logits = self.head(self.mlp(z)).squeeze(-1)
        return torch.sigmoid(logits)
'''

models[123] = '''class TDQCTransformerCalibrator(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int = 256, num_layers: int = 4, dropout: float = 0.1):
        super().__init__()
        self.gru = nn.GRU(input_dim, hidden_dim, num_layers=1, batch_first=True)
        for name, param in self.gru.named_parameters():
            if 'bias' in name:
                with torch.no_grad():
                    param[hidden_dim:2*hidden_dim].fill_(-2.0)
        self.norm = RMSNorm(hidden_dim)
        self.head = nn.Linear(hidden_dim, 1)

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        out, _ = self.gru(x)
        logits = self.head(self.norm(out)).squeeze(-1)
        return torch.sigmoid(logits)
'''

models[124] = '''class TDQCTransformerCalibrator(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int = 256, num_layers: int = 4, dropout: float = 0.1):
        super().__init__()
        in_d = input_dim * 3
        layers = []
        for _ in range(num_layers):
            layers.extend([nn.Linear(in_d, hidden_dim), RMSNorm(hidden_dim), nn.SiLU(), nn.Dropout(dropout)])
            in_d = hidden_dim
        self.mlp = nn.Sequential(*layers)
        self.head = nn.Linear(hidden_dim, 1)

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        x1 = torch.zeros_like(x)
        x1[:, 1:, :] = x[:, :-1, :]
        x2 = torch.zeros_like(x)
        x2[:, 2:, :] = x[:, :-2, :]
        logits = self.head(self.mlp(torch.cat([x, x1, x2], dim=-1))).squeeze(-1)
        return torch.sigmoid(logits)
'''

for i in range(115, 125):
    filepath = f'{base_dir}/idea_{i:03d}/phase2_tdqc/tdqc_model.py'
    with open(filepath, 'r') as f:
        content = f.read()
    
    parts = content.split('class TDQCTransformerCalibrator(nn.Module):')
    if len(parts) > 1:
        new_content = parts[0] + models[i]
        
        hard_update_code = '''
def hard_update(target: nn.Module, source: nn.Module) -> None:
    for target_param, param in zip(target.parameters(), source.parameters()):
        target_param.data.copy_(param.data)
'''
        if 'def hard_update' not in new_content:
            new_content += hard_update_code
            
        with open(filepath, 'w') as f:
            f.write(new_content)

print('Success')

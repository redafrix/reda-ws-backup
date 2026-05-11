import torch
import sys
import os

# Add the code directory to path
sys.path.append(os.path.abspath("."))

from phase2_tdqc.tdqc_model import TDQCLSTMCalibrator

def verify():
    input_dim = 22
    hidden_dim = 128
    model = TDQCLSTMCalibrator(input_dim=input_dim, hidden_dim=hidden_dim)
    
    # Test forward pass
    batch_size = 2
    seq_len = 10
    x = torch.randn(batch_size, seq_len, input_dim)
    p_fail = model(x)
    
    print(f"Forward pass output shape: {p_fail.shape}")
    assert p_fail.shape == (batch_size, seq_len)
    
    # Test step pass
    phi_t = torch.randn(batch_size, input_dim)
    p_fail_t, state = model.step(phi_t)
    print(f"Step pass output shape: {p_fail_t.shape}")
    assert p_fail_t.shape == (batch_size,)
    
    # Test step pass with episode_stats
    mean = torch.randn(input_dim)
    std = torch.ones(input_dim)
    p_fail_t_stats, state = model.step(phi_t, state=state, episode_stats=(mean, std))
    print(f"Step pass with stats output shape: {p_fail_t_stats.shape}")
    assert p_fail_t_stats.shape == (batch_size,)

    print("Verification successful!")

if __name__ == "__main__":
    verify()

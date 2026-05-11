
import torch
from phase2_tdqc.tdqc_model import TDQCLSTMCalibrator

def verify():
    input_dim = 22
    hidden_dim = 128
    model = TDQCLSTMCalibrator(input_dim, hidden_dim)
    model.eval()

    # Create a dummy sequence [B=1, T=5, F=22]
    x = torch.randn(1, 5, input_dim)
    
    # Forward pass
    p_fail_forward = model(x)
    
    # Step-by-step inference
    p_fail_steps = []
    state = None
    running_stats = None
    
    for t in range(x.shape[1]):
        phi_t = x[:, t, :]
        p_t, state, running_stats = model.step(phi_t, state, running_stats)
        p_fail_steps.append(p_t)
    
    p_fail_steps = torch.stack(p_fail_steps, dim=1)
    
    print(f"Forward p_fail: {p_fail_forward}")
    print(f"Steps p_fail:   {p_fail_steps}")
    
    diff = torch.abs(p_fail_forward - p_fail_steps).max().item()
    print(f"Max difference: {diff}")
    
    if diff < 1e-6:
        print("Verification SUCCESS: Forward and Step results match!")
    else:
        print("Verification FAILURE: Results do not match.")

if __name__ == "__main__":
    verify()

import torch
import sys
import os

# Add current directory to path to import local modules
sys.path.append(os.getcwd())

from tdqc_model import TDQCMambaCalibrator

import traceback

def test_inference():
    print("--- Starting Mock Inference Validation ---")
    
    input_dim = 22
    hidden_dim = 128
    batch_size = 1
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    
    try:
        model = TDQCMambaCalibrator(input_dim=input_dim, hidden_dim=hidden_dim).to(device)
        model.eval()
        print("Model initialized successfully.")
    except Exception as e:
        print(f"FAILED: Model initialization: {e}")
        traceback.print_exc()
        return

    # Test Forward Pass
    print("\nTesting full sequence forward pass...")
    seq_len = 10
    x = torch.randn(batch_size, seq_len, input_dim).to(device)
    try:
        p_fail = model(x)
        print(f"Forward output shape: {p_fail.shape} (Expected: [{batch_size}, {seq_len}])")
        assert p_fail.shape == (batch_size, seq_len)
    except Exception as e:
        print(f"FAILED: Forward pass: {e}")
        traceback.print_exc()
        return

    # Test Step-by-Step Inference (O(1))
    print("\nTesting step-by-step inference (O(1))...")
    state = None
    suite_embed = torch.randn(batch_size, hidden_dim).to(device)
    
    for t in range(5):
        phi_t = torch.randn(batch_size, input_dim).to(device)
        try:
            p_fail_t, state = model.step(phi_t, state=state, suite_embed=suite_embed)
            print(f"Step {t}: p_fail = {p_fail_t.item():.4f}")
            
            # Verify state is updated and contains inference_params
            assert state is not None
            assert "inference_params" in state
        except Exception as e:
            print(f"FAILED: Inference step {t}: {e}")
            traceback.print_exc()
            return

    print("\n--- Mock Inference Validation SUCCESSFUL ---")

if __name__ == "__main__":
    test_inference()

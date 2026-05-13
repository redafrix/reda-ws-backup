import os

# Base code setup for the new marathon
ideas = [
    # Idea 301: VAE Reconstruction Calibrator
    {'id': '301', 'type': 'vae', 'latent_dim': 8, 'weight': 1.0},
    # Idea 304: Forward Predictor
    {'id': '304', 'type': 'forward', 'horizon': 1, 'hidden': 256},
    # Idea 307: The 100-step Danger Ramp (Our fix for your confidence issue)
    {'id': '307', 'type': 'classifier', 'danger_zone': 100, 'ramp': 'linear'},
    # Idea 308: The 50-step Sudden Spike
    {'id': '308', 'type': 'classifier', 'danger_zone': 50, 'ramp': 'hard'},
]

print(f'Generated {len(ideas)} primary calibrator tests.')

# Template for training scripts...

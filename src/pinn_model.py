import torch
import torch.nn as nn

class PINN(nn.Module):
    def __init__(self, in_dim=1, hidden_dim=64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, 1)
        )

    def forward(self, x):
        raw = self.net(x)
        return torch.exp(raw)  # enforce u >= 0

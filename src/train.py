import torch
import torch.optim as optim
from src.pinn_model import PINN
from src.pde_operator import pde_residual

def boundary_loss(model):
    x0 = torch.zeros((1,1))
    return (model(x0) - 1.0) ** 2

def train_pinn(q_value, dim=1, epochs=3000):
    model = PINN(in_dim=dim)
    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    params = (0.5, q_value, 1.0, 0.0, 2.5)

    x = torch.linspace(-2, 2, 200).unsqueeze(1)

    losses = []

    for epoch in range(epochs):
        optimizer.zero_grad()

        residual, u, grad_u = pde_residual(model, x, params)

        loss = torch.mean(residual**2) + boundary_loss(model)

        loss.backward()
        optimizer.step()

        losses.append(loss.item())

    return model, x.detach(), losses

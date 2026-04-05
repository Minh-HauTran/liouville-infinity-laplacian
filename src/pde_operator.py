import torch

def infinity_laplacian(u, x):
    grads = torch.autograd.grad(u, x, grad_outputs=torch.ones_like(u), create_graph=True)[0]
    lap = torch.zeros_like(u)

    for i in range(x.shape[1]):
        grad_i = grads[:, i:i+1]
        grad2_i = torch.autograd.grad(grad_i, x, grad_outputs=torch.ones_like(grad_i), create_graph=True)[0]
        for j in range(x.shape[1]):
            lap += grads[:, i:i+1] * grads[:, j:j+1] * grad2_i[:, j:j+1]

    return lap


def pde_residual(model, x, params):
    c, q, lam, a, p = params

    x.requires_grad_(True)
    u = model(x)

    grad_u = torch.autograd.grad(u, x, grad_outputs=torch.ones_like(u), create_graph=True)[0]
    lap_inf = infinity_laplacian(u, x)

    lhs = -lap_inf + c * torch.norm(grad_u, dim=1, keepdim=True) ** q
    rhs = lam * torch.norm(x, dim=1, keepdim=True) ** a * u ** p

    return lhs - rhs, u, grad_u

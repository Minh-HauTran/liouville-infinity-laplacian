from src.train import train_pinn
import matplotlib.pyplot as plt
import torch
import os
import numpy as np

def estimate_decay(x, u):
    r = np.linalg.norm(x, axis=1)
    mask = (r > 1.0) & (r < 2.0)

    r = r[mask]
    u = u[mask]

    log_r = np.log(r + 1e-8)
    log_u = np.log(np.abs(u) + 1e-8)

    coeff = np.polyfit(log_r, log_u, 1)
    return coeff[0].item()


def phase_study(q_values):
    results = {}

    for q in q_values:
        model, x, _ = train_pinn(q)

        with torch.no_grad():
            u_pred = model(x).detach().numpy()

        results[q] = (x.numpy(), u_pred)

    return results


if __name__ == "__main__":
    q_values = [1,2,3,4,5]
    results = phase_study(q_values)

    os.makedirs("experiments/phase_transition", exist_ok=True)

    plt.figure(figsize=(12,5))

    for q, (x, u) in results.items():
        plt.plot(x, u, label=f"q={q}")

    plt.legend()
    plt.title("Phase Transition (q)")

    plt.savefig("experiments/phase_transition/q_plot.png", dpi=300)
    plt.show()

    # 🔥 scaling verification
    for q, (x, u) in results.items():
        beta = estimate_decay(x, u)
        print(f"q={q}, beta ≈ {-beta:.3f}")

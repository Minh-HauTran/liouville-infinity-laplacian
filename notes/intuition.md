# Intuition

This note summarizes the key intuition behind the results in this project.

## 1. Structure of the Infinity Laplacian

The infinity Laplacian is defined as:

Δ∞u = ⟨D²u ∇u, ∇u⟩

In a radial setting, this reduces to:

Δ∞u ≈ (u')² u''

This reveals a fundamental feature:

> The operator behaves like a cubic structure in the gradient.

---

## 2. Why the Critical Exponent p ≈ 3

Consider the equation:

-Δ∞u = u^p

Using a scaling ansatz:

u(r) ≈ r^{-β}

we obtain:

Δ∞u ≈ r^{-3β - 2}

while:

u^p ≈ r^{-pβ}

Balancing the powers:

3β + 2 = pβ  
⇒ β(p - 3) = 2

This suggests:

> p = 3 is the critical exponent.

- If p < 3: no consistent decay → nonexistence
- If p > 3: possible existence of solutions

---

## 3. Gradient Term and Threshold q ≈ 3

For gradient-dependent nonlinearities:

H(x,u,∇u) ≈ |∇u|^q

Using u(r) ≈ r^{-β}, we get:

|∇u| ≈ r^{-β - 1}  
⇒ |∇u|^q ≈ r^{-q(β + 1)}

Compare with:

Δ∞u ≈ r^{-3β - 2}

The competition depends on q:

- q > 3 → gradient dominates
- q < 3 → diffusion dominates

Thus:

> q ≈ 3 acts as a natural threshold.

---

## 4. Effect of Hardy–Hénon Weight

For the weighted term:

|x|^a u^p

we have:

|x|^a u^p ≈ r^{a - pβ}

This modifies the balance condition and shifts the admissible range of solutions.

---

## 5. Key Insight

The number "3" arises naturally from the cubic structure:

Δ∞u ≈ |∇u|² u''

This is fundamentally different from the classical Laplacian:

Δu ≈ u''

and leads to different critical phenomena.

---

## 6. Summary

- Infinity Laplacian behaves as a cubic operator  
- Critical exponent: p ≈ 3  
- Gradient threshold: q ≈ 3  
- Hardy–Hénon weights modify scaling behavior  

These observations guide the formal proofs in the paper.

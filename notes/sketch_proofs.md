# Sketch Proofs

This note outlines the main ideas behind the proofs in the paper.

---

## 1. Strategy for Liouville-Type Nonexistence

We aim to show that any global solution must be trivial under certain conditions.

The strategy consists of:

1. Reduction to radial setting  
2. Scaling analysis  
3. Contradiction argument  

---

## 2. Radial Reduction

Let:

u(x) = v(r),  r = |x|

Then:

Δ∞u = (v')² v''

This reduces the PDE to a one-dimensional nonlinear ODE.

---

## 3. Scaling Argument

Assume:

v(r) ≈ r^{-β}

Then:

Δ∞u ≈ r^{-3β - 2}  
|x|^a u^p ≈ r^{a - pβ}

Balancing exponents leads to:

β(p - 3) = a + 2

This identifies the critical role of p = 3.

---

## 4. Contradiction Argument

Assume a nontrivial positive solution exists.

Using the scaling relation:

- If p ≤ 3, no consistent decay is possible  
- This contradicts the assumption of a global solution  

Thus:

> Only the trivial solution can exist.

---

## 5. Gradient Domination

Consider:

H(x,u,∇u) ≈ |∇u|^q

Compare:

Δ∞u ≈ r^{-3β - 2}  
|∇u|^q ≈ r^{-q(β + 1)}

If q > 3:

- Gradient term dominates  
- Diffusion becomes negligible  

This changes the qualitative behavior of solutions.

---

## 6. Limitations

These arguments are formal and rely on scaling heuristics.

A fully rigorous treatment requires:

- Viscosity solution framework  
- Comparison principles  
- Careful justification of asymptotic behavior  

---

## 7. Conclusion

The proofs rely on:

- Structural properties of the infinity Laplacian  
- Scaling arguments  
- Reduction to simpler models  

These ideas provide insight into the behavior of solutions in highly nonlinear and degenerate PDEs.

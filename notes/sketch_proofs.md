# Sketch of the Main Arguments

This note outlines the structural strategy behind the Liouville-type nonexistence results.

---

## 1. General Strategy

We aim to prove that any non-negative global solution must be trivial.

The approach combines:

- Scaling analysis  
- Radial reduction  
- Viscosity comparison arguments  
- Contradiction via asymptotic profiles  

---

## 2. Scaling Analysis

Consider the equation:

-Δ∞u = λ |x|^a u^p

Introduce the scaling:

u_τ(x) = τ^θ u(τx)

Then:

Δ∞u_τ = τ^{3θ + 4} Δ∞u  
|x|^a u_τ^p = τ^{-a + pθ} |x|^a u^p

Balancing invariance gives:

3θ + 4 = -a + pθ  
⇒ θ(p - 3) = a + 4

For decaying solutions, θ < 0, which requires:

p > 3

---

## 3. Radial Reduction

For radial functions:

u(x) = v(r), r = |x|

the infinity Laplacian simplifies to:

Δ∞u = (v')² v''

Thus, the PDE reduces to the ODE:

-(v')² v'' = λ r^a v^p

---

## 4. Asymptotic Contradiction

Assume a decaying profile:

v(r) ≈ r^{-β}

Then:

-Δ∞v ≈ -r^{-3β - 4} < 0  
λ r^a v^p ≈ r^{a - pβ} > 0

This yields a contradiction:

negative ≥ positive

Hence, no decaying positive solution exists.

---

## 5. Extension to General Solutions

To extend beyond radial symmetry, define:

m(r) = inf_{|x| = r} u(x)

Using viscosity theory:

- m(r) inherits supersolution properties  
- m satisfies a radial inequality  

Since radial supersolutions cannot exist, general solutions must also be trivial.

---

## 6. Gradient-Dominated Regime

Consider:

-Δ∞u + c|∇u|^q ≥ λ |x|^a u^p

Using cutoff functions and viscosity test arguments:

- Diffusion scales as: R^{-4} u³  
- Gradient term scales as: R^{-q} u^q  

For q > 3:

- Gradient dominates diffusion  
- Inequality cannot hold asymptotically  

This forces:

u ≡ 0

---

## 7. Maximum Principle Argument (Gradient Source Case)

For:

Δ∞u + |∇u|^q + |x|^a u^p ≤ 0

At a maximum point:

- ∇u = 0  
- Δ∞u = 0  

Thus:

|x|^a u^p ≤ 0

which is impossible unless u ≡ 0.

---

## 8. Remarks on Rigor

The full proofs require:

- Viscosity solution framework  
- Comparison principles  
- Stability under infimum operations  
- Careful handling of degeneracy  

This sketch highlights only the structural mechanism behind the results.

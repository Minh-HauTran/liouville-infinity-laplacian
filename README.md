# Liouville-Type Results for Infinity Elliptic Equations with Gradient and Hardy–Hénon Nonlinearities

> A dimension-free Liouville theory for the infinity Laplacian, identifying the sharp critical threshold **p = 3** arising from its intrinsic cubic scaling structure.

---

## 📌 Overview

This repository contains a research project developed at the Vietnam Institute for Advanced Study in Mathematics (VIASM) during the Summer 2025 Research Fellowship.

We study Liouville-type nonexistence phenomena for a class of highly degenerate elliptic equations of the form

\[
-\Delta_\infty u + c|\nabla u|^q = \lambda |x|^a u^p 
\quad \text{in } \mathbb{R}^n
\]

involving:

- the **infinity Laplacian** \( \Delta_\infty \),
- **gradient-dependent nonlinearities**,
- **Hardy–Hénon-type spatial weights**.

Our goal is to understand how degeneracy, gradient effects, and spatial heterogeneity interact to determine global solution behavior.

---

## 🔥 Core Mechanism

The key structural feature of the infinity Laplacian is its **cubic homogeneity**:

\[
\Delta_\infty (\tau u) = \tau^3 \Delta_\infty u
\]

This induces a rigid scaling constraint for equations of the form

\[
-\Delta_\infty u = |x|^a u^p
\]

leading to the balance relation:

\[
\theta (p - 3) = a + 4
\]

As a consequence:

- the exponent **p = 3** emerges as a **critical threshold**,  
- this threshold is **independent of the spatial dimension**,
- subcritical regimes \( p \le 3 \) are incompatible with decaying entire solutions.

This behavior contrasts with classical Laplacian theory, where critical exponents depend explicitly on dimension.

---

## ⭐ Main Results (Informal)

- **(Liouville Nonexistence)**  
  If \( 1 < p \le 3 \), any bounded nonnegative viscosity solution is trivial.

- **(Gradient Domination)**  
  If \( q > 3 \) and \( p < q \), the gradient term dominates and enforces triviality under mild decay conditions.

- **(Critical Thresholds)**  
  Both \( p = 3 \) and \( q = 3 \) arise as sharp thresholds dictated by the cubic structure of \( \Delta_\infty \).

- **(Dimension-Free Behavior)**  
  The critical exponent does not depend on \( n \), in contrast to classical elliptic theory.

---

## 🎯 Problem Statement

We investigate nonlinear PDEs of the form

\[
-\Delta_\infty u + c|\nabla u|^q = \lambda |x|^a u^p 
\quad \text{in } \mathbb{R}^n
\]

with the following guiding questions:

- When do nontrivial entire solutions exist?
- How do gradient nonlinearities alter Liouville-type phenomena?
- How do Hardy–Hénon weights affect global behavior?

---

## 🧠 Main Contributions

This work establishes new Liouville-type results for infinity elliptic equations with combined nonlinear effects:

- Identification of a **dimension-independent critical exponent** \( p = 3 \)
- Discovery of a **gradient domination threshold** \( q = 3 \)
- Development of analytical techniques based on:
  - scaling invariance
  - radial reduction
  - viscosity solution framework
- Extension of Liouville theory to:
  - gradient-dependent equations
  - weighted Hardy–Hénon structures

---

## 📚 Relation to Existing Work

This work builds upon classical Liouville-type results for:

- semilinear elliptic equations (Gidas–Spruck),
- Hardy–Hénon equations,
- infinity Laplacian and AMLE theory (Aronsson, Jensen, Crandall–Lions).

We extend these frameworks to a **fully nonlinear, non-divergence setting** with:

- gradient-dependent Hamiltonians,
- spatial weights,
- dimension-independent scaling behavior.

---

## 📄 Paper

📥 **Full manuscript:** [Download PDF](paper/liouville_infinity_elliptic_equations.pdf)

The LaTeX source is included for reproducibility.

---

## 🧩 Conceptual Structure

![PDE Structure](figures/pde-structure-diagram.png)

The diagram illustrates the interaction between:

- cubic diffusion (infinity Laplacian),
- gradient nonlinearity \( |\nabla u|^q \),
- spatial forcing \( |x|^a u^p \),

leading to a critical transition at \( p = 3 \).

---

## 🔗 Interdisciplinary Insight

The infinity Laplacian arises as the Euler–Lagrange equation for **absolutely minimizing Lipschitz extensions (AMLE)**.

This connects naturally to:

### PDE Theory
- degenerate elliptic operators
- viscosity solutions
- rigidity and nonexistence theory

### Machine Learning
- Lipschitz regularization
- adversarial robustness
- gradient penalties

Our results suggest that excessive gradient penalization (large \( q \)) can force trivial behavior, providing a PDE perspective on **model collapse** in robust learning.

---

## 🚀 Future Directions

- Extension to parabolic (time-dependent) models  
- Boundary value problems in weighted settings  
- Anisotropic or non-radial weights  
- Connections with stochastic control (tug-of-war games)

---

## ❓ Open Problems

- Classification of sign-changing (nodal) solutions  
- Sharp thresholds in mixed nonlinear regimes  
- Stability under perturbations  
- PDE–probability connections  

---

## ⚠️ Status

This is an ongoing research project.  
Several results are being refined toward full rigor and potential publication.

---

## 👨‍🏫 Advisors

- Prof. Hai-Long Dao (University of Kansas)  
- Prof. Dac-Tuan Ngo (CNRS)  
- Dr. Tuan-Minh Nguyen (Monash University)  

---

## 👤 Author

**Tran Minh Hau**  
Undergraduate, Computer Science  
University of Information Technology – VNU-HCM  

**Huynh Trung Hieu**
Undergraduate, Mathematics
Ho Chi Minh City University of Education (HCMUE)

---

## 📬 Contact

📧 hautm.cs@gmail.com

---

## 📚 Notes

- [Intuition](notes/intuition.md)
- [Sketch Proofs](notes/sketch_proofs.md)

---
order: 20
id: learning-and-control
title: Learning and Control
tags:
- Learning-based control
- Barrier and Lyapunov methods
- Policy adaptation
image: assets/learning-and-control.webp
image_alt: Diagram of stability regions and mappings between latent and original state spaces.
papers:
- journals-corr-abs-2606-15366
- arxiv-2610.40931
summary: We integrate machine learning with control theory to design complex control systems that provably achieve their design objectives, while accounting for model uncertainty, limited data, and computational constraints.
---

We combine learned dynamics and policies with barrier and Lyapunov methods to reason about safety and stability. Control decisions influence the data available for learning, so we study how this feedback affects model updates and controller adaptation. We seek methods that use data efficiently and remain computationally tractable under uncertainty.

### Current directions

- Data-efficient learning of dynamical models and feedback policies.
- Safety and stability under model and observation uncertainty.
- Computationally tractable policy adaptation and control.

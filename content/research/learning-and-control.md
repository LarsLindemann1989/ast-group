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
summary: We combine learning with control theory to design systems that adapt to uncertainty and pursue complex objectives, while accounting for the feedback between their decisions, data, and safety.
---

We develop control methods that use data and learned models while retaining a clear connection to system dynamics and constraints. Our interests include learning from imperfect observations, adapting controllers as new information becomes available, and combining learning with barrier and Lyapunov methods.

A central challenge is that control decisions change the data a system encounters. We study how to account for this feedback when updating models and policies, with the aim of improving performance while preserving safety and stability guarantees under clearly stated assumptions.

### Current directions

- Learning dynamical models and feedback policies from data.
- Barrier and Lyapunov methods for safe and stabilizing control.
- Policy adaptation and control under model and observation uncertainty.

---
order: 20
id: learning-and-control
title: Learning and Control
tags:
- Control barrier functions
- Prescribed-performance control
- Latent representations
image: assets/learning-and-control.webp
image_alt: Diagram of stability regions and mappings between latent and original state spaces.
papers:
- conf-cdc-RobeyHLZDTM20
- journals-corr-abs-2607-23876
- conf-cdc-LutkusWLT25
- arxiv-2610.40931
summary: We integrate machine learning with control theory to design complex control systems that provably achieve their design objectives, while accounting for model uncertainty, limited data, and computational constraints.
---

We learn control barrier functions (CBFs) from safe demonstrations to synthesize feedback controllers with safety guarantees. For prescribed-performance control (PPC), we jointly learn performance bounds and feedback laws from state trajectories, with guarantees on transient and steady-state behavior under input constraints.

We also learn low-dimensional representations and dynamical models to simplify control design for complex systems. Our work establishes conditions under which stability and safety guarantees obtained in latent space carry over to the original system. We develop learning objectives that preserve the dynamical structure needed for feedback stabilization.

### Current directions

- Learning control barrier functions from demonstrations for safe feedback control.
- Learning prescribed-performance controllers from state trajectories under input constraints.
- Learning latent representations and dynamics for control with stability and safety guarantees.

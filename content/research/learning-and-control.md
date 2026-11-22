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
- journals-corr-abs-2111-09971
- conf-cdc-LutkusWLT25
- arxiv-2610.40931
summary: We integrate machine learning with control theory to design complex control systems that provably achieve their design objectives, while accounting for model uncertainty, limited data, and computational constraints.
---

How can learning be used to design control systems that provably achieve their objectives? We study this question by combining machine learning with control-theoretic tools such as control barrier functions and prescribed-performance control. Our methods aim to turn data into controllers with guarantees on safety, stability, and performance.

We are particularly interested in settings where complex dynamics and high-dimensional state spaces make control design challenging. This motivates approaches ranging from learning controllers and safety certificates from data to learning latent representations that preserve the information needed for control.

### Current directions

- Learning control barrier functions from demonstrations for safe feedback control.
- Learning prescribed-performance controllers from state trajectories under input constraints.
- Learning latent representations and dynamics for control with stability and safety guarantees.

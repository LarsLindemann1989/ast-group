---
order: 10
id: safe-learning
title: Statistical Foundations of Safe Autonomy
tags:
- Conformal prediction
- Sequential inference
- Safety certification
image: assets/statistical-safe-autonomy.jpg
image_alt: Illustration of calibration data and conformal prediction supporting a safe autonomous robot trajectory.
papers:
- cp-survey-2025
- conf-iccps-ZhaoHFDL24
summary: We develop statistical methods to quantify uncertainty and reason about safety from finite and evolving data, connecting conformal prediction and sequential inference with autonomous decision making.
---

How can data support meaningful safety guarantees for autonomous systems? We study this question through conformal prediction, uncertainty quantification, and sequential statistical inference. Our methods aim to turn observations into actionable bounds on prediction errors and risk.

We are particularly interested in settings where observations arrive over time and changes in the environment or controller affect their distribution. This motivates approaches to predictive verification and safety certification that account explicitly for the assumptions behind statistical guarantees and for the interaction between data and system behavior.

### Current directions

- Conformal prediction for trajectories, dynamical systems, and safety assessment.
- Sequential inference, e-values, and anytime-valid safety certification.
- Statistical guarantees under distribution shifts and changing control policies.

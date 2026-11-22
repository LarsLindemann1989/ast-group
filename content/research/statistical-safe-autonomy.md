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
summary: We develop statistical methods to quantify uncertainty in learning-enabled systems and reason about safety from finite and evolving data, connecting conformal prediction and sequential hypothesis testing with decision making.
---

How can data be used to obtain safety guarantees for autonomous systems? We study this question through statistical tools such as conformal prediction and sequential hypothesis testing. Our methods aim to turn observations into actionable confidence bounds of model and prediction errors.

We are particularly interested in settings where observations arrive over time and change as a consequence of an evolving environment or interaction between data and the decision making system. This motivates approaches ranging from safety certification and predictive runtime verification to motion planning and robust control.

### Current directions

- Conformal prediction for trajectories, dynamical systems, and safety assessment.
- Sequential hypothesis testing, e-values, and anytime-valid safety certification.
- Statistical guarantees under distribution shifts and changing control policies.

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

Our methods turn observations into bounds on prediction errors and risk that can inform verification and control. We study settings where data arrive sequentially and environmental changes or updated policies alter their distribution. A central goal is to make the assumptions behind safety guarantees explicit and assess when those guarantees remain valid.

### Current directions

- Conformal prediction for trajectories, dynamical systems, and safety assessment.
- Sequential hypothesis testing, e-values, and anytime-valid safety certification.
- Statistical guarantees under distribution shifts and changing control policies.

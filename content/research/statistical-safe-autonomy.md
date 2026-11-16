---
order: 10
id: safe-learning
title: Statistical Foundations of Safe Autonomy
tags:
- Conformal prediction
- Sequential inference
- Safety certification
image: assets/control-pipeline.png
image_alt: Predictive runtime verification workflows using conformal prediction.
image_source: https://arxiv.org/abs/2409.00536
image_credit: Lindemann et al. · Conformal prediction survey
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

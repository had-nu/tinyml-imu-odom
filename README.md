# TinyML IMU-Based Motion Decision Pipeline

> This repository contains an experimental engineering pipeline for evaluating motion-related decisions in IMU-based TinyML systems under embedded constraints.

> The focus is not on achieving accurate odometry, but on observing how small models behave, fail, and degrade when deployed on resource-limited hardware, using reproducible workflows and controlled datasets.

---

## About This Project

**tinyml-imu-odom** is an experimental engineering pipeline for evaluating motion-related decisions in IMU-based TinyML systems under embedded constraints.

The project focuses on observing how IMU-only models behave, fail, and degrade when deployed on resource-limited hardware, using controlled datasets and reproducible workflows across training (Python) and deployment (Go) environments.

Rather than targeting accurate odometry or complete navigation stacks, the system is intentionally limited in scope to expose decision instability, error patterns, and practical constraints relevant to embedded inertial systems operating without GPS.

---

## Context & Motivation

Autonomous and semi-autonomous systems operating in indoor environments rely heavily on inertial sensing to make real-time decisions about motion and system state. In many practical scenarios, the critical requirement is not precise localization, but the ability to reliably detect and reason about basic motion-related conditions under uncertainty.

When deployed on embedded or resource-limited hardware, IMU-based models are subject to sensor noise, drift, limited temporal context, and strict constraints on memory, latency, and energy consumption. These constraints directly affect the stability of motion-related decisions, especially when models are reduced to TinyML-scale representations.

Despite extensive research on inertial odometry and learning-based motion estimation, less attention is given to how small, embedded models behave, fail, or degrade when used as decision-making components rather than high-accuracy estimators. This gap becomes particularly relevant for safety, monitoring, and control tasks in low-cost robotic systems, where incorrect motion decisions may have disproportionate operational impact.

The MAGF-ID dataset is used in this project as a methodological reference and controlled laboratory for inertial signal analysis. Its role is not to provide state-of-the-art performance benchmarks, but to support reproducible experimentation and systematic observation of model behavior under constrained conditions.

---

## Project Scope

This project explicitly does not aim to solve global localization, SLAM, or full navigation problems. Its scope is intentionally constrained to the evaluation of minimal motion-related decisions derived from IMU data under embedded and real-time constraints.

The initial focus is on binary motion state decisions (e.g., moving vs. stationary), treated as observable system outputs rather than accurate pose estimates. This limitation allows the project to expose decision instability, error patterns, and degradation effects caused by sensor noise, model compression, and resource constraints.

By restricting the problem to small models, short temporal windows, and IMU-only inputs, the project prioritizes reproducibility and behavioral analysis over performance optimization or completeness.

---

## License

MIT License — see the LICENSE file.

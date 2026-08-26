# UDCF Research Tools: Universal Dimensionless Cutting Framework

This repository contains the official source code, benchmark scripts, and raw experimental datasets for the **UDCF Profiler v3.1** and the **Instrumented Pendulum Rig v2.1**. 

This package is designed to ensure full reproducibility of the results presented in the associated manuscript, specifically Tables 1–4 and Figures 3 and 4.

## 📊 Project Overview
The Universal Dimensionless Cutting Framework (UDCF) utilizes a dimensionless efficiency index ($\eta$) to predict phenomenological outcomes (Severance vs. Deformation) across multi-scale cutting scenarios.

The core governing equation used in these tools is:
$$\eta = \frac{k_Y \cdot m \cdot v^2}{2 \cdot d \cdot \tau_{ult} \cdot A}$$

## 📁 Repository Structure
- `/scripts`: 
    - `udcf_benchmark.py`: Python script to reproduce the calculation of $\eta$ for all experimental trials and theoretical extrapolations.
- `/data`:
    - `raw_per_trial_table1.csv`: The 5-trial repeat dataset used for statistical validation of material "fingerprints."
    - `extrapolation_100_trials.csv`: The comprehensive 100-trial dataset covering scenarios from surgical scalpels to industrial shredders.
- `/docs`: Documentation regarding the Instrumented Pendulum Rig calibration.

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Pandas
- NumPy

### Reproducing Results
To verify the calculations for Tables 1, 2, and 5 in the manuscript, run the benchmark script:
```bash
python scripts/udcf_benchmark.py

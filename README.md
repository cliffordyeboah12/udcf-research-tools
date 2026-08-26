# UDCF Research Tools: Reproducibility Package

## Overview
This repository contains the raw experimental data and validation scripts for the **Unified Dimensionless Cutting Framework (UDCF)**, as presented in the manuscript by *Clifford Yeboah et al.* 

The purpose of this package is to provide full transparency and reproducibility for the statistical analysis (Table 1) and the benchmark efficiency calculations (Table 4) discussed in the study.

## Repository Contents

| File Name | Description |
| :--- | :--- |
| `udcf_raw_data.csv` | Raw experimental dataset containing 100 trials, including material properties, kinematic inputs, and calculated $\eta$ outcomes. |
| `udcf_reproducibility_script.m` | MATLAB script designed to reproduce the Mean, Standard Deviation, and Coefficient of Variation (CV%) values reported in Table 1. |
| `udcf_benchmark.py` | Python script to verify the UDCF formula against the validation matrix and benchmark scenarios (Axe vs. Wood, Scalpel vs. Tissue, etc.). |

## Getting Started

### Prerequisites
- **For MATLAB Script:** MATLAB (R2020a or later recommended).
- **For Python Script:** Python 3.x and the `pandas` library.

### Execution Instructions

#### 1. Reproducing Table 1 Statistics (MATLAB)
1. Open MATLAB and navigate to the directory containing `udcf_reproducibility_script.m`.
2. Run the script by typing `udcf_reproducibility_script` in the Command Window.
3. The output will display the statistical verification for Dermis, HDPE, and other materials, matching the manuscript's Table 1.

#### 2. Verifying UDCF Benchmarks (Python)
1. Ensure `udcf_benchmark.py` and `udcf_raw_data.csv` are in the same folder.
2. Run the script via terminal/command prompt:
   ```bash
   python udcf_benchmark.py

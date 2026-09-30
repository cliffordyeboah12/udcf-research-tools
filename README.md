# UDCF Research Tools: Unified Dimensionless Cutting Framework

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22112130.svg)](https://doi.org/10.5281/zenodo.22112130)

This repository contains the official source code, statistical benchmark scripts, and raw experimental datasets for the **Unified Dimensionless Cutting Framework (UDCF)**. These tools support the **UDCF Profiler v3.1** and the **Instrumented Pendulum Cutting Rig (IPCR) v3.1**.

This package ensures full reproducibility of the results presented in the associated manuscript, covering Tables 2–5 and Figures 5, 6, 7, and 10.

## 📊 Project Overview
The Unified Dimensionless Cutting Framework (UDCF) utilizes a dimensionless separation index ($\eta$) to predict phenomenological outcomes (Severance vs. Deformation) across multi-scale cutting scenarios.

The core governing equation used in these tools is:

$$\eta = k_Y \left[ \frac{m \cdot v^2}{2 \cdot d \cdot t_{ult} \cdot A} \right]$$

To preserve dimensional homogeneity and physical fidelity, the parameter \(A\) is rigorously defined as the 2D projected area of the tool’s apex interface. Its value is determined by the interaction between the micro-scale edge radius \(r_e\) and the macro-scale effective contact length \(L_e\):

$$A = r_e \cdot L_e \cdot 10^{-9}$$


Where:
*   $m$ is mass
*   $v$ is velocity
*   $d$ is thickness
*   $t_{ult}$ is ultimate shear strength
*   $A$ is contact area
*   $k_Y$ is Systemic Energy Recovery Factor

## 📂 Repository Structure

### 📁 /data (Excel Datasets)
Contains the source data for all manuscript tables and figures:
- `raw_per_trial_table2.xlsx`: 5-trial repeat dataset for statistical validation.
- `extrapolation_100_trials.xlsx`: Comprehensive dataset (surgical scalpels to industrial shredders).
- `Figure_5_Source_Data.xlsx` to `Figure_10_Source_Data.xlsx`: Specific data points used for graphical plotting.

### 📁 /scripts (Python Analysis)
Python scripts to reproduce the statistical analysis and tables:
- `udcf_benchmark.py`: Core logic for calculating \(\eta\) across all trials.
- `udcf_stats_table2.py`: Generates the statistical "fingerprints" for Table 2.
- `table4_uncertainty.py`: Performs the uncertainty quantification for Table 4.
- `udcf_extrapolation_table5.py`: Models the extreme-scale scenarios for Table 5.

### 📁 /tools (Web Simulators)
Standalone HTML/JavaScript tools for real-time calculation:
- `udcf_profiler.html`: The primary interface for calculating the Separation Index.
- `udcf_ipcr.html`: Digital twin for the Instrumented Pendulum Cutting Rig.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Required Libraries: `pandas`, `numpy`, `matplotlib`

### Reproducing Results
To verify the statistical calculations for the manuscript, execute the scripts from the root directory:

```bash
# To reproduce Table 2 Statistics
python scripts/udcf_stats_table2.py

# To reproduce Table 4 Uncertainty Analysis
python scripts/table4_uncertainty.py

# To reproduce Table 5 Extrapolation
python scripts/udcf_extrapolation_table5.py

⚖️ License
This project is licensed under the MIT License - see the LICENSE file for details.

✉️ Contact
Clifford Yeboah
The Yeboah Institute Research Ghana
Email address: cliffordyeboah@yahoo.com
ORCID ID: https://orcid.org/0009-0000-9001-2643

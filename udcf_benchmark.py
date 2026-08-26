import numpy as np
import pandas as pd

def calculate_eta(m, v, d_mm, A_scaled, tau_mpa, ky=1.0):
    """Calculates Dimensionless Efficiency (eta) with unit normalization."""
    d_m = d_mm / 1000.0          # mm to meters
    A_m2 = A_scaled * 1e-4       # Table 2 uses x10^-4 m^2
    tau_pa = tau_mpa * 1e6       # MPa to Pascals
    
    numerator = m * (v**2)
    denominator = 2 * d_m * tau_pa * A_m2
    return round(ky * (numerator / denominator), 2)

def verify_manuscript_data():
    print("--- UDCF VALIDATION REPORT (TABLE 2) ---")
    # Data from Page 3 of PDF
    table_2_tests = [
        {"ID": "Exp A1", "m": 0.50, "v": 1.20, "d": 2.00, "A": 5.00, "tau": 2.50, "ky": 0.95, "target": 0.14},
        {"ID": "Exp A2", "m": 0.50, "v": 3.50, "d": 2.00, "A": 5.00, "tau": 2.50, "ky": 0.95, "target": 1.16},
        {"ID": "Exp B2", "m": 4.50, "v": 5.00, "d": 20.0, "A": 1.67, "tau": 12.0, "ky": 0.82, "target": 1.15},
        {"ID": "Exp C4", "m": 10.0, "v": 10.0, "d": 5.00, "A": 1.50, "tau": 400., "ky": 0.70, "target": 1.16},
    ]
    
    for t in table_2_tests:
        res = calculate_eta(t['m'], t['v'], t['d'], t['A'], t['tau'], t['ky'])
        status = "PASS" if abs(res - t['target']) < 0.05 else "FAIL"
        print(f"{t['ID']}: Calc={res} | Target={t['target']} | {status}")

if __name__ == "__main__":
    verify_manuscript_data()

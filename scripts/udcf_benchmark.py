import numpy as np
import pandas as pd

def calculate_eta(m, v, d_mm, A_scaled, tau_mpa, ky=1.0):
    """
    Calculates Dimensionless Efficiency (eta) with unit normalization.
    d_m = thickness in meters
    A_m2 = area in m^2 (input is scaled by 10^-4)
    tau_pa = shear strength in Pascals
    """
    d_m = d_mm / 1000.0          # mm to meters
    A_m2 = A_scaled * 1e-4       # Table 3 uses x10^-4 m^2
    tau_pa = tau_mpa * 1e6       # MPa to Pascals

    numerator = m * (v**2)
    denominator = 2 * d_m * tau_pa * A_m2
    
    # Applying the systemic recovery factor ky
    return round(ky * (numerator / denominator), 2)

def verify_manuscript_data():
    print("--- UDCF VALIDATION REPORT (TABLE 3: VALIDATION MATRIX) ---")
    
    # Data from Table 3 of the Manuscript
    table_3_tests = [
        {"ID": "Exp A1", "m": 0.50, "v": 1.20, "d": 2.00, "A": 5.00, "tau": 2.50, "ky": 0.95, "target": 0.14},
        {"ID": "Exp A2", "m": 0.50, "v": 3.50, "d": 2.00, "A": 5.00, "tau": 2.50, "ky": 0.95, "target": 1.16},
        {"ID": "Exp A3", "m": 1.00, "v": 2.50, "d": 2.00, "A": 5.00, "tau": 2.50, "ky": 0.95, "target": 1.19},
        {"ID": "Exp A4", "m": 0.10, "v": 8.00, "d": 2.00, "A": 5.00, "tau": 2.50, "ky": 0.95, "target": 1.22},
        {"ID": "Exp A5", "m": 0.10, "v": 4.00, "d": 2.00, "A": 5.00, "tau": 2.50, "ky": 0.95, "target": 0.30},
        {"ID": "Exp B1", "m": 2.00, "v": 4.50, "d": 20.0, "A": 1.00, "tau": 12.0, "ky": 0.82, "target": 0.69},
        {"ID": "Exp B2", "m": 2.00, "v": 7.50, "d": 20.0, "A": 1.00, "tau": 12.0, "ky": 0.82, "target": 1.92},
        {"ID": "Exp B3", "m": 2.00, "v": 9.00, "d": 20.0, "A": 1.00, "tau": 12.0, "ky": 0.82, "target": 2.77},
        {"ID": "Exp B4", "m": 1.50, "v": 5.00, "d": 20.0, "A": 1.00, "tau": 7.50, "ky": 0.85, "target": 1.06},
        {"ID": "Exp B5", "m": 1.50, "v": 3.00, "d": 20.0, "A": 1.00, "tau": 7.50, "ky": 0.85, "target": 0.38},
        {"ID": "Exp C1", "m": 2.50, "v": 4.50, "d": 10.0, "A": 1.00, "tau": 15.0, "ky": 0.88, "target": 1.48},
        {"ID": "Exp C2", "m": 2.50, "v": 2.30, "d": 10.0, "A": 1.00, "tau": 15.0, "ky": 0.75, "target": 0.33},
        {"ID": "Exp C3", "m": 10.0, "v": 7.00, "d": 5.00, "A": 1.00, "tau": 400., "ky": 0.70, "target": 0.86},
        {"ID": "Exp C4", "m": 10.0, "v": 12.0, "d": 5.00, "A": 1.00, "tau": 400., "ky": 0.70, "target": 2.52},
        {"ID": "Exp C5", "m": 10.0, "v": 9.00, "d": 5.00, "A": 1.00, "tau": 400., "ky": 0.70, "target": 1.42},
    ]

    results = []
    for t in table_3_tests:
        calc = calculate_eta(t['m'], t['v'], t['d'], t['A'], t['tau'], t['ky'])
        # Check if calculation matches target within a small rounding margin
        status = "PASS" if abs(calc - t['target']) <= 0.02 else "FAIL"
        results.append({"ID": t['ID'], "Calculated": calc, "Manuscript": t['target'], "Status": status})
        print(f"{t['ID']}: Calc={calc} | Target={t['target']} | {status}")

    df = pd.DataFrame(results)
    if all(df['Status'] == "PASS"):
        print("\nSUCCESS: All Table 3 values verified against UDCF framework.")
    else:
        print("\nWARNING: Some values do not match. Check rounding or input parameters.")

if __name__ == "__main__":
    verify_manuscript_data()
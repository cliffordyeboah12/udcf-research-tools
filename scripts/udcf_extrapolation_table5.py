import pandas as pd
import numpy as np

def reproduce_table_5():
    print("--- UDCF TABLE 5: MULTI-SCALE EXTRAPOLATION VALIDATION ---")
    
    # Complete list of 20 scenarios from the manuscript
    data = [
        {"Scenario": "Axe vs. Pine Wood", "m": 2.500, "v": 12.0, "d": 0.050, "A": 5.00e-5, "tau": 8.0e6, "kY": 0.40, "target": 3.60},
        {"Scenario": "Razor vs. Pine Wood", "m": 0.001, "v": 12.0, "d": 0.050, "A": 1.20e-7, "tau": 8.0e6, "kY": 0.10, "target": 0.15},
        {"Scenario": "Scalpel vs. Soft Tissue", "m": 0.025, "v": 0.10, "d": 0.005, "A": 1.00e-8, "tau": 2.0e5, "kY": 0.90, "target": 11.25},
        {"Scenario": "Robotic Blade vs. Syn Tissue", "m": 0.020, "v": 0.525, "d": 0.005, "A": 1.00e-6, "tau": 5.0e5, "kY": 0.95, "target": 1.05},
        {"Scenario": "Industrial Shredder vs. HDPE", "m": 132.20, "v": 2.50, "d": 0.015, "A": 4.50e-4, "tau": 3.0e7, "kY": 0.75, "target": 1.53},
        {"Scenario": "Stamping Die vs. AHSS DP900", "m": 33.90, "v": 2.50, "d": 0.002, "A": 4.00e-5, "tau": 9.0e8, "kY": 0.78, "target": 1.15},
        {"Scenario": "Chef's knife vs. Carrot", "m": 0.250, "v": 2.00, "d": 0.020, "A": 5.00e-7, "tau": 1.5e6, "kY": 0.60, "target": 20.00},
        {"Scenario": "Katana vs. Bamboo", "m": 1.200, "v": 15.0, "d": 0.050, "A": 5.00e-7, "tau": 4.0e7, "kY": 0.80, "target": 108.00},
        {"Scenario": "Butter Knife vs. Steak", "m": 0.050, "v": 0.50, "d": 0.010, "A": 2.50e-5, "tau": 5.0e5, "kY": 0.20, "target": 0.01},
        {"Scenario": "Guillotine vs. Paper", "m": 2.000, "v": 3.00, "d": 0.020, "A": 6.00e-6, "tau": 3.0e7, "kY": 0.70, "target": 1.75},
        {"Scenario": "Machete vs. Thick Vine", "m": 0.600, "v": 15.0, "d": 0.030, "A": 5.24e-7, "tau": 6.0e6, "kY": 0.70, "target": 500.95},
        {"Scenario": "Scissor vs. Cardboard", "m": 0.100, "v": 0.50, "d": 0.005, "A": 2.00e-7, "tau": 2.0e6, "kY": 0.85, "target": 5.31},
        {"Scenario": "Plastic Knife vs. Apple", "m": 0.010, "v": 1.00, "d": 0.040, "A": 1.50e-5, "tau": 8.0e5, "kY": 0.30, "target": 0.003},
        {"Scenario": "Cleaver vs. Bone", "m": 1.500, "v": 8.00, "d": 0.020, "A": 2.00e-5, "tau": 5.0e7, "kY": 0.50, "target": 1.20},
        {"Scenario": "Waterjet vs. Steel", "m": 0.005, "v": 900.0, "d": 0.020, "A": 8.00e-7, "tau": 4.0e8, "kY": 0.90, "target": 284.76},
        {"Scenario": "Microtome vs. Resin", "m": 0.050, "v": 0.01, "d": 0.001, "A": 1.00e-12, "tau": 5.0e7, "kY": 0.95, "target": 47.50},
        {"Scenario": "Saw Tooth vs. Hardwood", "m": 0.020, "v": 50.0, "d": 0.001, "A": 5.00e-6, "tau": 1.5e7, "kY": 0.60, "target": 200.00},
        {"Scenario": "Wire Saw vs. Silicon", "m": 0.100, "v": 15.0, "d": 0.010, "A": 2.00e-6, "tau": 1.5e8, "kY": 0.50, "target": 1.87},
        {"Scenario": "Micro-projectile vs. Armor", "m": 1.00e-6, "v": 1200., "d": 5.0e-4, "A": 8.00e-9, "tau": 2.5e9, "kY": 0.92, "target": 66.24},
        {"Scenario": "Abrasive Waterjet vs. Ti-6Al-4V", "m": 5.0e-4, "v": 752.0, "d": 0.01, "A": 7.8e-7, "tau": 9.5e8, "kY": 0.65, "target": 12.40}
    ]

    results = []
    for s in data:
        # Formula: eta = kY * (m * v^2) / (2 * d * tau * A)
        numerator = s['kY'] * s['m'] * (s['v']**2)
        denominator = 2 * s['d'] * s['tau'] * s['A']
        eta = numerator / denominator
        
        # Rounding to match manuscript display
        calc_eta = round(eta, 2) if eta > 0.01 else round(eta, 4)
        status = "PASS" if abs(calc_eta - s['target']) < 0.05 else "FAIL"
        
        results.append({
            "Scenario": s['Scenario'], 
            "Calculated": calc_eta, 
            "Target": s['target'], 
            "Status": status
        })

    df = pd.DataFrame(results)
    print(df.to_string(index=False))

    if all(df['Status'] == "PASS"):
        print("\nSUCCESS: All 20 scenarios in Table 5 verified.")
    else:
        print("\nWARNING: Discrepancies found in calculations.")

if __name__ == "__main__":
    reproduce_table_5()
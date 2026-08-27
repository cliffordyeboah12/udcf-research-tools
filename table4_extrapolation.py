import pandas as pd

def reproduce_table_4():
    data = [
        {"Scenario": "Axe vs. Pine Wood", "m": 2.5, "v": 12.0, "d": 0.05, "A": 5.0e-5, "tau": 8.0e6, "kY": 0.40},
        {"Scenario": "Razor vs. Pine Wood", "m": 0.001, "v": 12.0, "d": 0.05, "A": 1.2e-7, "tau": 8.0e6, "kY": 0.10},
        {"Scenario": "Scalpel vs. Soft Tissue", "m": 0.025, "v": 0.1, "d": 0.005, "A": 1.0e-8, "tau": 2.0e5, "kY": 0.90},
        {"Scenario": "Chef's knife vs. Carrot", "m": 0.25, "v": 2.0, "d": 0.02, "A": 5.0e-7, "tau": 1.5e6, "kY": 0.60},
        {"Scenario": "Waterjet vs. Steel", "m": 0.005, "v": 900.0, "d": 0.02, "A": 8.0e-7, "tau": 4.0e8, "kY": 0.90}
    ]

    results = []
    for s in data:
        # Formula: eta = kY * (m * v^2) / (2 * d * tau * A)
        numerator = s['kY'] * s['m'] * (s['v']**2)
        denominator = 2 * s['d'] * s['tau'] * s['A']
        eta = numerator / denominator
        results.append({"Scenario": s['Scenario'], "Calculated_eta": round(eta, 2)})

    df = pd.DataFrame(results)
    print("--- Table 4: Extrapolation Sample Check ---")
    print(df)

if __name__ == "__main__":
    reproduce_table_4()

import pandas as pd

def calculate_udcf_eta(m, v, d_mm, A_scaled, tau_mpa, ky):
    """
    Calculates eta based on the UDCF formula: 
    eta = ky * [(m * v^2) / (2 * d * tau * A)]
    
    Converts units to SI (meters and Pascals) for dimensionless consistency.
    """
    # Unit Conversions
    d_m = d_mm / 1000.0          # mm to meters
    A_m2 = A_scaled * 1e-4       # Table 2 uses x10^-4 m^2
    tau_pa = tau_mpa * 1e6       # MPa to Pascals (N/m^2)
    
    numerator = m * (v**2)
    denominator = 2 * d_m * tau_pa * A_m2
    
    eta = ky * (numerator / denominator)
    return round(eta, 2)

def run_benchmarks():
    print("UDCF BENCHMARK VERIFICATION REPORT")
    print("="*40)
    
    # Data from Manuscript Table 2
    benchmarks = [
        {"ID": "Exp A1", "m": 0.50, "v": 1.20, "d": 2.00, "A": 5.00, "tau": 2.50, "ky": 0.95, "expected": 0.14},
        {"ID": "Exp A2", "m": 0.50, "v": 3.50, "d": 2.00, "A": 5.00, "tau": 2.50, "ky": 0.95, "expected": 1.16},
        {"ID": "Exp A3", "m": 1.00, "v": 2.50, "d": 2.00, "A": 5.00, "tau": 2.50, "ky": 0.95, "expected": 1.19},
        {"ID": "Exp B1", "m": 4.50, "v": 3.00, "d": 20.0, "A": 1.67, "tau": 12.0, "ky": 0.82, "expected": 0.41},
    ]
    
    passed = 0
    for test in benchmarks:
        calc_eta = calculate_udcf_eta(test["m"], test["v"], test["d"], test["A"], test["tau"], test["ky"])
        status = "PASS" if abs(calc_eta - test["expected"]) <= 0.02 else "FAIL"
        
        print(f"{test['ID']}: Calculated η={calc_eta:.2f} | Expected={test['expected']:.2f} | Result: {status}")
        if status == "PASS": passed += 1

    print("-" * 40)
    print(f"Validation Summary: {passed}/{len(benchmarks)} Tests Passed")
    
    # Table 5 Extrapolation Check
    print("\nEXTRAPOLATION SCENARIOS (Table 5)")
    # Axe vs Wood: m=2.5, v=12, d=0.05m (50mm), A=5e-5, tau=8e6, ky=0.40
    axe_eta = calculate_udcf_eta(2.5, 12.0, 50.0, 0.5, 8.0, 0.40) 
    print(f"Axe vs. Pine Wood: Calculated η={axe_eta} (Expected: 3.60)")

if __name__ == "__main__":
    run_benchmarks()

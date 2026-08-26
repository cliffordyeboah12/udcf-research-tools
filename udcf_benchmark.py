import pandas as pd

def calculate_udcf(m, v, d, tau, A, kY):
    return kY * ((m * (v**2)) / (2 * d * tau * A))

# Data from Table 2 Validation Matrix
validation_cases = [
    {"name": "Exp A1 (Dermis)", "m": 0.5, "v": 1.2, "d": 0.002, "tau": 2.5e5, "A": 5e-7, "kY": 0.95, "expected": 0.14},
    {"name": "Exp A2 (Dermis)", "m": 0.5, "v": 3.5, "d": 0.002, "tau": 2.5e5, "A": 5e-7, "kY": 0.95, "expected": 1.16},
]

print("UDCF BENCHMARK REPORT")
print("-" * 30)
for case in validation_cases:
    result = calculate_udcf(case['m'], case['v'], case['d'], case['tau'], case['A'], case['kY'])
    status = "PASS" if round(result, 2) == case['expected'] else "FAIL"
    print(f"{case['name']}: Calculated η={result:.2f} | Result: {status}")

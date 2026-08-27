import math

def calculate_uncertainty():
    # Relative uncertainties (u_i / x_i) from Table 3
    u_rel_v = 0.018  # 1.8%
    u_rel_A = 0.025  # 2.5%
    u_rel_m = 0.005  # 0.5%
    u_rel_tau = 0.020 # 2.0%

    # Sensitivity coefficients (c_i)
    # For eta = (k_Y * m * v^2) / (2 * d * tau * A)
    # c_v = 2 (exponent), others are 1
    c_v = 2
    c_A = 1
    c_m = 1
    c_tau = 1

    # Contributions (c_i * u_rel_i)
    cont_v = c_v * u_rel_v
    cont_A = c_A * u_rel_A
    cont_m = c_m * u_rel_m
    cont_tau = c_tau * u_rel_tau

    # Combined Standard Uncertainty (uc)
    # Square root of the sum of squares of contributions
    uc = math.sqrt(cont_v**2 + cont_A**2 + cont_m**2 + cont_tau**2)
    
    # Expanded Uncertainty (U) for k=2
    U = uc * 2

    print(f"--- Table 3: Uncertainty Budget Validation ---")
    print(f"Velocity Contribution: {cont_v*100:.1f}%")
    print(f"Combined Standard Uncertainty (uc): {uc*100:.2f}%")
    print(f"Expanded Uncertainty (U, k=2): {U*100:.2f}%")

if __name__ == "__main__":
    calculate_uncertainty()

import pandas as pd
import os

def generate_statistical_report():
    # 1. Setup paths to look into the /data folder
    # This ensures the script works regardless of where the repo is cloned
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'statistical_distribution_data.xlsx')

    print(f"--- UDCF Research Tools: Statistical Distribution Analysis ---")
    
    try:
        # 2. Define the data based on your Table 2
        # In a real scenario, this would read: df = pd.read_excel(data_path)
        data = {
            "Material Category": ["Biological (Dermis)", "Polymers (HDPE)", "Metallic Alloys (Al 6061)", "Structural Steel (A36)"],
            "n": [5, 5, 5, 5],
            "Mean η": [1.14, 1.42, 0.88, 0.92],
            "Std. Dev (σ)": [0.092, 0.041, 0.018, 0.022]
        }

        df = pd.DataFrame(data)

        # 3. Calculate Coefficient of Variation (CV%)
        # Formula: (StdDev / Mean) * 100
        df['CV (%)'] = (df['Std. Dev (σ)'] / df['Mean η']) * 100

        # 4. Formatting the output for the console
        print("\nTable 2 | Statistical Distribution of Dimensionless Separation Index (η)")
        print("-" * 85)
        header = f"{'Material Category':<30} {'n':<5} {'Mean η':<10} {'Std. Dev (σ)':<15} {'CV (%)':<10}"
        print(header)
        print("-" * 85)

        for _, row in df.iterrows():
            print(f"{row['Material Category']:<30} "
                  f"{int(row['n']):<5} "
                  f"{row['Mean η']:<10.2f} "
                  f"{row['Std. Dev (σ)']:<15.3f} "
                  f"{row['CV (%)']:>6.2f}%")
        
        print("-" * 85)
        print("Note: η = 1.0 is the critical threshold for severance.")

    except Exception as e:
        print(f"Error: Could not process data. {e}")

if __name__ == "__main__":
    generate_statistical_report()
# UDCF v4.0 PRO: User Guide & Manual

## 1. System Setup

Before running a simulation, configure your environment using the left sidebar:

*   **Systemic Factors:** Adjust the **Recovery Factor ($k_Y$)** to account for energy losses in your specific system.
*   **Kinematics:** Input the **Mass** of the tool and the impact **Velocity**.

## 2. Tool Geometry

Define the physical characteristics of your cutting edge:

*   **Radius ($r_e$) & Contact ($L_e$):** These define the microscopic surface area of the cut.
*   **Wedge Angle ($\theta_w$):** A critical factor in the Impedance equation.
*   **Manual Overrides:** Use these if you have pre-calculated **Impedance ($\Phi$)** or **Area ($A$)** values from external sensors.

## 3. Running the Simulation

1.  Click **RUN SIMULATION** in the top right.
2.  Observe the **Live Physics Render Engine**.
3.  **Green Glow / Split Wood:** Indicates $\eta \ge 1$ (Successful Severance).
4.  **Red Glow / Tool Bounce:** Indicates $\eta < 1$ (Insufficient Energy).

## 4. Interpreting Results

*   **Separation Index ($\eta$):** The most important value. If it is above 1.0, the cut is physically possible.
*   **SI Vector Analysis:** Look at the bars in the center. If the **Geometric** bar is low, your tool is too blunt or the friction is too high. If the **Kinematic** bar is low, you need more speed or mass.
*   **Energy Graph:** The blue curve shows your energy potential. The red dotted line is your "Wall"—you must cross it to succeed.

## 5. Data Management

At the end of your experiment, click **EXPORT RESEARCH DATA**. This generates a CSV file including all input parameters and final calculations for your research paper or lab report.

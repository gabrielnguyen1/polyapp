import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import streamlit as st

# Define polymer properties: name, activation energy (J/mol), pre-exponential factor (1/s)
polymers = {
    "Polyethylene": {"Ea": 25000, "A": 1e5, "color": "b", "linestyle": "-", "marker": "o"},
    "Polystyrene": {"Ea": 30000, "A": 2e5, "color": "r", "linestyle": "--", "marker": "s"},
    "Polyvinyl Chloride": {"Ea": 35000, "A": 1.5e5, "color": "g", "linestyle": "-.", "marker": "^"},
    "Nylon": {"Ea": 40000, "A": 2.5e5, "color": "m", "linestyle": ":", "marker": "v"},
    "Polymethyl Methacrylate": {"Ea": 45000, "A": 1.8e5, "color": "c", "linestyle": "-", "marker": "d"},
}

def arrhenius_equation(A: float, Ea: float, T: float) -> float:
    R = 8.314  # Universal gas constant (J/mol·K)
    return A * np.exp(-Ea / (R * T))

def simulate_polymerization(initial_concentration: float, rate_constant: float, total_time: float, gel_point: float, diffusion_factor: float):
    def rate_equation(t, C):
        # Apply diffusion limitations
        if C < gel_point:
            diffusion_limit = max(1 - diffusion_factor * (C / gel_point), 0)
        else:
            diffusion_limit = 0.1  # Minimal reaction rate beyond the gel point
        return -rate_constant * diffusion_limit * C

    # Solve ODE using scipy's solve_ivp
    solution = solve_ivp(rate_equation, [0, total_time], [initial_concentration], method='RK45', t_eval=np.linspace(0, total_time, 100))
    return solution.t, solution.y[0]

def calculate_degree_of_polymerization(concentration_initial: float, concentration_final: float) -> float:
    if concentration_initial == concentration_final:
        return float('inf')  # Avoid division by zero
    return concentration_initial / (concentration_initial - concentration_final)

# Streamlit app title and description
st.title('Polymerization Reaction with Diffusion Limitations')
st.write("Adjust the parameters in the sidebar to see how they affect polymerization over time.")

# Interactive sliders in the sidebar
temperature = st.sidebar.slider('Temperature (K)', min_value=250.0, max_value=500.0, step=10.0, value=300.0)
gel_point = st.sidebar.slider('Gel Point (mol/L)', min_value=0.1, max_value=1.0, step=0.1, value=0.5)
diffusion_factor = st.sidebar.slider('Diffusion Factor', min_value=0.1, max_value=1.0, step=0.1, value=0.8)
initial_concentration = 1.0  # mol/L
total_time = 50  # seconds

# Set up plot
fig, ax = plt.subplots(figsize=(12, 6))

# Create a line for each polymer
for polymer, properties in polymers.items():
    Ea = properties["Ea"]
    A = properties["A"]
    rate_constant = arrhenius_equation(A, Ea, temperature)

    # Simulate polymerization
    times, concentrations = simulate_polymerization(initial_concentration, rate_constant, total_time, gel_point, diffusion_factor)
    dp = calculate_degree_of_polymerization(initial_concentration, concentrations[-1])

    # Plot data
    ax.plot(times, concentrations, color=properties["color"], linestyle=properties["linestyle"],
            marker=properties["marker"], lw=2, label=f'{polymer}: DP = {dp:.2f}')

# Configure plot settings
ax.set_title('Polymerization Reaction with Diffusion Limitations')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Concentration (mol/L)')
ax.set_xlim(0, total_time)
ax.set_ylim(0, initial_concentration)
ax.grid()
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)
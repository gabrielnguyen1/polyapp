import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def schulz_zimm_distribution(Mn, PDI, size=1000):
    """
    Generate molecular weight distribution using the Schulz-Zimm distribution.

    Parameters:
        Mn (float): Number-average molecular weight.
        PDI (float): Polydispersity index (Mw/Mn).
        size (int): Number of samples to generate.

    Returns:
        molecular_weights (numpy array): Array of molecular weights.
    """
    z = (PDI - 1) / (1 - (1 / PDI))
    beta = Mn / (z + 1)
    molecular_weights = np.random.gamma(z + 1, beta, size)
    return molecular_weights

def plot_schulz_zimm_interactive(Mn, PDI, temperature, size=1000):
    """
    Plot molecular weight distribution for the Schulz-Zimm model based on user input.

    Parameters:
        Mn (float): Number-average molecular weight.
        PDI (float): Polydispersity index (Mw/Mn).
        temperature (float): Temperature at which the simulation is being conducted.
        size (int): Number of samples to generate for the distribution.
    """
    # Generate the distribution
    molecular_weights = schulz_zimm_distribution(Mn, PDI, size)

    # Plot the distribution
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.hist(molecular_weights, bins=50, alpha=0.7, color='b', density=True)
    ax.set_title(f'Schulz-Zimm Distribution at {temperature} K (PDI={PDI:.2f})')
    ax.set_xlabel('Molecular Weight')
    ax.set_ylabel('Density')
    ax.grid()

    # Display the plot in Streamlit
    st.pyplot(fig)

# Streamlit app configuration and title
st.set_page_config(page_title="Schulz-Zimm Distribution", page_icon="📊")
st.title("Schulz-Zimm Distribution Simulation")

# Sidebar sliders for interactive input
Mn = st.sidebar.slider('Mn (Number-average molecular weight)', min_value=1000.0, max_value=50000.0, step=1000.0, value=10000.0)
PDI = st.sidebar.slider('PDI (Polydispersity index)', min_value=1.1, max_value=3.0, step=0.1, value=1.5)
temperature = st.sidebar.slider('Temperature (K)', min_value=250.0, max_value=500.0, step=10.0, value=300.0)

# Plot the distribution based on user inputs
plot_schulz_zimm_interactive(Mn, PDI, temperature)
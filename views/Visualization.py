import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Page title and description
st.title("Polymer Molecular Weight Distribution Heat Map")
st.write("""
This interactive heat map visualizes the distribution of molecular weights along a polymer chain. 
Use the sliders to adjust parameters and observe how the molecular weight varies along the polymer chain.
""")

# Define function to generate molecular weight distribution
def generate_molecular_weights(length, base_weight, variance):
    # Simulate molecular weight as a normal distribution around base_weight with variance
    weights = np.random.normal(loc=base_weight, scale=variance, size=length)
    weights = np.clip(weights, a_min=0, a_max=None)  # No negative weights
    return weights

# Sidebar inputs
st.sidebar.header("Adjust Polymer Parameters")
polymer_length = st.sidebar.slider("Polymer Chain Length", min_value=50, max_value=500, step=50, value=100)
base_weight = st.sidebar.slider("Base Molecular Weight (g/mol)", min_value=1000, max_value=50000, step=1000, value=10000)
variance = st.sidebar.slider("Molecular Weight Variance", min_value=100, max_value=5000, step=100, value=1000)

# Generate molecular weights
molecular_weights = generate_molecular_weights(polymer_length, base_weight, variance)

# Plotting the heat map
fig, ax = plt.subplots(figsize=(10, 2))

# Create a colormap that maps molecular weights to colors
cmap = cm.get_cmap('coolwarm')
norm = plt.Normalize(molecular_weights.min(), molecular_weights.max())
heatmap = ax.imshow([molecular_weights], aspect="auto", cmap=cmap, norm=norm)

# Color bar for reference
cbar = plt.colorbar(heatmap, orientation="horizontal", pad=0.2)
cbar.set_label("Molecular Weight (g/mol)")

# Add titles and labels
ax.set_title("Molecular Weight Distribution Along Polymer Chain")
ax.set_xlabel("Polymer Chain Segment")
ax.set_yticks([])  # Hide y-axis labels

# Display the plot in Streamlit
st.pyplot(fig)
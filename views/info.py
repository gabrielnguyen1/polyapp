import streamlit as st

# Page title and description
st.title("PolyOptimize")
st.subheader("Maximizing The Optimization of Polymer Production")

# Problem Statement
st.header("Problem Statement")
st.write("""
Within specific polymer processing industries, each industry has a set of desired polymer properties over a set of reaction parameters. Several factors such as molecular weight distribution, reaction temperature, and cross-linking density are crucial in determining the mechanical properties, durability, and flexibility of a polymer. However, high distribution in these properties suggest inconsistencies within production ultimately impacting the quality and performance of polymer-based products. Optimization is necessary in order to assure that polymers are produced with necessary regulations for industry applications.
""")

# App Features
st.header("App Features")
st.write("By allowing users to visualize the impact of several parameters on the potential molecular structure and distribution of polymer chains, it is possible to maximize the uniformity and efficiency of building these molecules. Users can navigate through each of these features to gain an adept knowledge and simulated research of the conditions they may need to build their polymer at.")

# Feature 1: Polymerization Reactions
st.subheader("1. Polymerization Reactions")
st.write("""
This section allows users to visualize polymer reactions across several types with diffusion limitations, reinforcing the realistic approach processing engineers may face.

**Interactive Features**:
- **Temperature Slider**: Adjusts the temperatures in Kelvins which impacts the reaction rate constant.
- **Gel Point Slider**: By adjusing the gel point concentration (mol/L), you can be given a simulated approach where diffusion limitations begin to significantly impact reaction rates.
- **Diffusion Factor Slider**: As the reaction reaches gel point, users may be able to interact and change the diffusion factor to see it's influence on the reaction.
""")

# Feature 2: Molecular Weight Distribution Graph
st.subheader("2. Schulz-Zimm Distribution Graph")
st.write("""
This section models molecular weight variation within polymers and showing a potential visualization of chain lengths within a sample, demonstrating the distribution of densities at several conditions.

**Interactive Features**:
- **Number-Average Molecular Weight Slider**: Controlling the average molecular weight allows users to gain insight onto the position of distribution according to the x-axis.
- **PDI (Polydisperity Index): Varying the PDI allows users to illustrate the spread of distribution which are illustrated by the premise of variability within the chain lengths.
""")

# Feature 3: Polymer Molecular Weight Distribution Heat Map
st.subheader("3. Polymer Molecular Weight Distribution Heat Map")
st.write("""
This section allows user to view a color-coded heat map of the molecular weight distribution along the polymer chain, indicating specific places where some parts of the chain may contain high, medium, or low molecular weight.

**Interactive Features**:
- **Polymer Chain Length**: Controls the number of segments along the polymer chain in the heat map
- **Base Molecular Weight (g/mol)**: Shifts the central molecular weight for the polymer by changing the range up or down.
- **Molecular Weight Variance** : By controling the distribution of molecular weights along the chain, users are able to broaden the weight distribution. This is reflected in the affluence of color variation within the heat map.
""")

# Conclusion
st.header("Conclusion")
st.write("""
These toolsets for optimizing polymer production can ultimately be reflected in the reduction of waste and the achievement of efficiently producing targeted properties in a polymer. Real-time feedback found in this simulation as well as user-friendly interactions provides the foundation for a data-driven approach to the polymer processing industry. This helps potential engineers enhance or improve their product quality.
""")
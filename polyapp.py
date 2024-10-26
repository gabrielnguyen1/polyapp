import streamlit as st

# --- page setup ---

about_page = st.Page(
    page="views/info.py",
    title= "PolyOptimize",
    default=True,
)

project_3_page = st.Page(
    page="views/Visualization.py",
    title= "Molecular Weight Heat Map",
)

project_1_page= st.Page(
    page="views/Reaction.py",
    title="Polymerization Reactions",
)

project_2_page = st.Page(
    page="views/Distribution.py",
    title="Molecular Weight Distribution",
)

# --- NAVIGATION SETUP WITHOUT SECTIONS --- #

pg = st.navigation(pages=[about_page, project_1_page, project_2_page, project_3_page])

# -- RUN NAVIGATION -- #
pg.run()
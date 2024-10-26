import streamlit as st

# --- page setup ---

project_1_page = st.Page(
    page="views/simulation1.py",
    title= "Molecular Weight Distribution",
    default=True,
)

project_2_page= st.Page(
    page="views/simulation2.py",
    title="Another Distribution",
)

project_3_page = st.Page(
    page="views/simu3.py",
    title="Another Pimpibution",
)

# --- NAVIGATION SETUP WITHOUT SECTIONS --- #

pg = st.navigation(pages=[project_1_page, project_2_page, project_3_page])

# -- RUN NAVIGATION -- #
pg.run()
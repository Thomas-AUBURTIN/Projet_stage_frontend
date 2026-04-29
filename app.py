import streamlit as st


st.sidebar.title("ollama")
st.sidebar.markdown("llm gratuit")

pg = st.navigation([
    st.Page("page_1.py", title="Accueil"),
    st.Page("page_2.py", title="historique"),
    
])

pg.run()
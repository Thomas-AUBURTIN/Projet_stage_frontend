import streamlit as st

st.title("Démo st.chat_message")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
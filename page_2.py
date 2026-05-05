import streamlit as st

import Proxy.proxy as pr

historique = pr.get_historique()

st.title("Démo st.chat_message")

for message in historique:
    with st.chat_message('user'):
        st.markdown(message["question"])
    with st.chat_message("assistant"):
        st.markdown(message["reponse"])
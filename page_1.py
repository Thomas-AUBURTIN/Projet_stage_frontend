import streamlit as st
import Proxy.proxy as pr

left, center, right = st.columns([1, 50, 1])

if "messages_recent" not in st.session_state:
    st.session_state.messages_recent = []

for message in st.session_state.messages_recent:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("quelle est votre question"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages_recent.append({
        "role": "user",
        "content": prompt
    })

    reponse = pr.ask_api(prompt)
    reponse_json = reponse.json()


    if isinstance(reponse_json, dict):
        assistant_text = reponse_json.get("reponse", str(reponse_json))
    else:
        assistant_text = str(reponse_json)

    with st.chat_message("assistant"):
        st.markdown(assistant_text)

    st.session_state.messages_recent.append({
        "role": "assistant",
        "content": assistant_text
    })
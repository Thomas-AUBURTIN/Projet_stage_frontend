import streamlit as st
import os

import json

left, center, right = st.columns([1, 50, 1])

if "message" not in st.session_state:
    if os.path.exists("messages.json"):
        try:
            with open("messages.json", "r", encoding="utf-8") as f:
                st.session_state.messages = json.load(f)
        except json.JSONDecodeError:
            st.session_state.messages = []
    else:
        st.session_state.messages = []

if "messages_recent" not in st.session_state:
    st.session_state.messages_recent = []

for message in st.session_state.messages_recent:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("quelle est votre question"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    st.session_state.messages_recent.append({
        "role": "user",
        "content": prompt
    })

    reponse = "quelquechose"

    with st.chat_message("assistant"):
        st.markdown(reponse)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reponse
    })

    st.session_state.messages_recent.append({
        "role": "assistant",
        "content": reponse
    })

    with open("messages.json", "w", encoding="utf-8") as f:
        json.dump(st.session_state.messages, f, ensure_ascii=False, indent=2)


       



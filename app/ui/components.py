import streamlit as st


def render_chat_history(messages: list[dict]) -> None:
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def add_message(role: str, content: str) -> None:
    st.session_state.messages.append({"role": role, "content": content})
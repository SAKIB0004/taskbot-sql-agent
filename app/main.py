import streamlit as st
from app.config.settings import settings
from app.db.schema import init_db
from app.db.reset import reset_tasks_table
from app.db.seed import seed_tasks
from app.services.chat_service import process_user_query
from app.ui.components import render_chat_history, add_message

st.set_page_config(page_title=settings.APP_TITLE, layout="wide")

# Initialize DB once at startup
init_db()

st.title(settings.APP_TITLE)
st.write(
    "Manage your tasks with natural language. "
    "You can create, read, update, and delete tasks using chat."
)

# Sidebar
with st.sidebar:
    st.header("Session Settings")

    if "thread_id" not in st.session_state:
        st.session_state.thread_id = settings.DEFAULT_THREAD_ID

    st.session_state.thread_id = st.text_input(
        "Thread ID",
        value=st.session_state.thread_id,
        help="Use different thread IDs for separate conversations."
    )

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    if st.button("Insert Demo Tasks"):
        seed_tasks()
        st.success("Demo tasks inserted.")
        st.rerun()

    if st.button("Reset Tasks Table"):
        reset_tasks_table()
        st.session_state.messages = []
        st.success("All tasks deleted and ID reset to 1.")
        st.rerun()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

render_chat_history(st.session_state.messages)

prompt = st.chat_input("Enter your task query...")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    add_message("user", prompt)

    with st.chat_message("assistant"):
        with st.spinner("Processing your request..."):
            try:
                result = process_user_query(
                    prompt=prompt,
                    thread_id=st.session_state.thread_id
                )
                st.markdown(result)
                add_message("assistant", result)
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                st.error(error_msg)
                add_message("assistant", error_msg)
import streamlit as st
from langgraph_backend import get_chat_response


if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = 'streamlit-chat'

# Loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message["role"]):
        st.text(message["content"])

user_input = st.chat_input("Type your message here...")

if user_input:

    # First add the user message to the message history
    st.session_state['message_history'].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    ai_message = get_chat_response(user_input, thread_id=st.session_state['thread_id'])

    st.session_state['message_history'].append({"role": "assistant", "content": ai_message})
    with st.chat_message("assistant"):
        st.text(ai_message)
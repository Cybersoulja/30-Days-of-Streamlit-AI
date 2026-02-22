"""
Day 1: AI Chatbot with Claude
30 Days of Streamlit: AI Edition

A simple multi-turn chatbot powered by Claude claude-opus-4-6 with streaming responses.
"""

import streamlit as st
import anthropic

# Page config
st.set_page_config(
    page_title="Day 1 — AI Chatbot",
    page_icon="🤖",
    layout="centered",
)

st.title("Day 1: AI Chatbot")
st.caption("Powered by Claude claude-opus-4-6 · 30 Days of Streamlit: AI Edition")

# Initialize the Anthropic client (reads ANTHROPIC_API_KEY from environment)
client = anthropic.Anthropic()

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar controls
with st.sidebar:
    st.header("Settings")
    system_prompt = st.text_area(
        "System prompt",
        value="You are a helpful, friendly AI assistant. Be concise and clear.",
        height=120,
    )
    if st.button("Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.markdown("**Day 1 of 30**")
    st.markdown("Building a streaming multi-turn chatbot using the Anthropic Python SDK.")

# Render existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Message Claude..."):
    # Append user message to history and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Stream Claude's response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        with client.messages.stream(
            model="claude-opus-4-6",
            max_tokens=1024,
            system=system_prompt,
            messages=st.session_state.messages,
        ) as stream:
            for text_chunk in stream.text_stream:
                full_response += text_chunk
                response_placeholder.markdown(full_response + "▌")

        response_placeholder.markdown(full_response)

    # Save assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

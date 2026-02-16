import streamlit as st

st.set_page_config(page_title="30 Days of Streamlit AI", page_icon="🤖", layout="wide")

st.title("🤖 30 Days of Streamlit: AI Edition")

st.markdown("""
Welcome to the **30 Days of Streamlit AI** challenge!

This app tracks a journey through building AI-powered applications with Streamlit.

### What's being built:
- AI chatbots
- Computer vision apps
- Real-time dashboards
- LLM-powered tools

### Getting Started
Select a day from the sidebar to explore each project.
""")

st.sidebar.header("Navigation")
st.sidebar.info("Projects will appear here as they are added.")

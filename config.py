import os
import streamlit as st

# Try to load from .env file first (for local development)

def get_key(key_name):
    try:
        from dotenv import load_dotenv
        load_dotenv(override=True)
        return os.getenv(key_name)
    except FileNotFoundError:
        return st.secrets[key_name]

OPENAI_API_KEY = get_key("OPENAI_API_KEY")
GROQ_API_KEY = get_key("GROQ_API_KEY")
LANGCHAIN_TRACING_V2=get_key("LANGCHAIN_TRACING_V2")
LANGCHAIN_API_KEY=get_key("LANGCHAIN_API_KEY")
LANGCHAIN_PROJECT=get_key("LANGCHAIN_PROJECT")

# import streamlit as st

# OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
# GROQ_API_KEY = st.secrets["GROQ_API_KEY"]


if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY MIA")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY MIA")

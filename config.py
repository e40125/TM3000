import os
import streamlit as st

# Try to load from .env file first (for local development)

def get_key(key_name):
    try:
        from dotenv import load_dotenv
        load_dotenv(override=True)
        # Load the key from .env
        key = os.getenv(key_name)
        if key:
            # Set it as an environment variable for the current process
            os.environ[key_name] = key
        return key
    except FileNotFoundError:
        # Fallback to Streamlit secrets if .env is not found
        key = st.secrets.get(key_name)
        if key:
            os.environ[key_name] = key
        return key

OPENAI_API_KEY = get_key("OPENAI_API_KEY")
GROQ_API_KEY = get_key("GROQ_API_KEY")
LANGCHAIN_TRACING_V2 = get_key("LANGSMITH_TRACING")
LANGCHAIN_ENDPOINT = get_key("LANGSMITH_ENDPOINT")
LANGCHAIN_API_KEY = get_key("LANGSMITH_API_KEY")
LANGCHAIN_PROJECT = get_key("LANGSMITH_PROJECT")

# import streamlit as st

# OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
# GROQ_API_KEY = st.secrets["GROQ_API_KEY"]


if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY MIA")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY MIA")

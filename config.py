import os
import streamlit as st

# Try to load from .env file first (for local development)
try:
    from dotenv import load_dotenv
    load_dotenv(override=True)
except ImportError:
    pass  # .env not available? fuck it we ball


# Function to get them keys, handling both local and cloud setups
def get_key(key_name):
    try:
        return st.secrets[key_name]
    except FileNotFoundError:
        # If we can't find the secrets file, we're probably local
        return os.getenv(key_name)

OPENAI_API_KEY = get_key("OPENAI_API_KEY")
GROQ_API_KEY = get_key("GROQ_API_KEY")
LANGCHAIN_TRACING_V2=get_key("LANGCHAIN_TRACING_V2")
LANGCHAIN_API_KEY=get_key("LANGCHAIN_API_KEY")
LANGCHAIN_PROJECT=get_key("LANGCHAIN_PROJECT")
# Check if we got the goods
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY missing. Where the fuck is it at?")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY MIA. Get your shit straight!")

# import os
# from dotenv import load_dotenv

# load_dotenv(override=True)

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# if not OPENAI_API_KEY:
#     raise ValueError("OPENAI_API_KEY not found.")

# import os
# import streamlit as st

# OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
# GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# if not OPENAI_API_KEY:
#     raise ValueError("OPENAI_API_KEY not found")
# utils.py
import streamlit as st

class ConversationManager:
    def __init__(self, max_history=6):
        self.max_history = max_history
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def initialize_chat(self, intro_message):
        st.session_state.messages = [{"role": "assistant", "content": intro_message}]

    def add_message(self, role, content):
        st.session_state.messages.append({"role": role, "content": content})
        if len(st.session_state.messages) > self.max_history + 1:
            st.session_state.messages.pop(1)  # Keep the initial message

    def get_history(self):
        return st.session_state.messages[1:]  # Exclude the initial message

    def clear_history(self):
        st.session_state.messages = []

class ChatbotException(Exception):
    pass

def handle_chatbot_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise ChatbotException(f"Shit's fucked up: {str(e)}")
    return wrapper

def render_sidebar():
    with st.sidebar:
        st.title("Flex Chatbot")
        current_model = st.selectbox('Choose a model', ['GPT', 'TM3000', 'GS6000', 'Groq', 'TMD3100'], key='model_select')
        temp = st.slider('temperature', 0.01, 1.0, 0.5, 0.01)
        
        # Disable max_len slider for TMD3100
        if current_model == 'TMD3100':
            st.text("Max length: Unlimited")
            max_len = None
        else:
            max_len = st.slider('max_length', 32, 256, 128, 4)
        
        use_history = st.toggle("Use Chat History", True)
    
    # Check if model has changed
    model_changed = False
    if 'current_model' not in st.session_state or st.session_state.current_model != current_model:
        model_changed = True
        st.session_state.current_model = current_model

    return current_model, temp, max_len, use_history, model_changed
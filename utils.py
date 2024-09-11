# utils.py
import streamlit as st
from models import BOT_CONFIGS

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
        current_model = st.selectbox('Choose a model', list(BOT_CONFIGS.keys()), key='model_select')
        config = BOT_CONFIGS[current_model]
        
        if isinstance(config['params']['temperature'], dict):
            temp_config = config['params']['temperature']
            temp = st.slider('Temperature', 
                             min_value=temp_config['min'], 
                             max_value=temp_config['max'], 
                             value=temp_config['default'], 
                             step=temp_config['step'])
        else:
            temp = config['params']['temperature']
            st.text(f"Temperature: {temp}")
        
        if isinstance(config['params']['max_tokens'], dict):
            max_tokens_config = config['params']['max_tokens']
            max_len = st.slider('Max Length', 
                                min_value=max_tokens_config['min'], 
                                max_value=max_tokens_config['max'], 
                                value=max_tokens_config['default'], 
                                step=max_tokens_config['step'])
        elif config['params']['max_tokens'] is None:
            st.text("Max length: Unlimited")
            max_len = None
        else:
            max_len = config['params']['max_tokens']
            st.text(f"Max length: {max_len}")
        
        use_history = st.toggle("Use Chat History", True)
    
    model_changed = 'current_model' not in st.session_state or st.session_state.current_model != current_model
    st.session_state.current_model = current_model

    return current_model, temp, max_len, use_history, model_changed
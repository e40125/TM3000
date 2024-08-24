import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama

from dotenv import load_dotenv
import os

load_dotenv(override=True)

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

if not (os.environ['OPENAI_API_KEY']):
    st.warning("OPEN_API_KEY not found.")
    st.stop()



# UI
st.set_page_config(page_title="TM3000")
with st.sidebar:
    st.title("Chatbot")
    st.subheader('Models and Parameters')
    selected_model = st.sidebar.selectbox('Choose a model', ['GPT', 'TM3000'], key='selected_model')
    temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=1.0, value=0.5, step=0.01)
    max_length = st.sidebar.slider('max_length', min_value=32, max_value=128, value=120, step=4)
    st.markdown('📖')

def model_initialization():
    if selected_model == 'GPT':
        llm = ChatOpenAI(
                model="gpt-4o-mini",
                temperature= temperature,
                max_tokens=50,
        )
    elif selected_model == 'TM3000':
        llm = ChatOpenAI(
                model="ft:gpt-4o-mini-2024-07-18:personal::9zIKV308",
                temperature = temperature,
                max_tokens=max_length
        )
    return llm
llm = model_initialization()
if selected_model == 'GPT':
    st.session_state.llm = ChatOpenAI(
                model="gpt-4o-mini",
                temperature= temperature,
                max_tokens=50,)

if selected_model == 'TM3000':
    st.session_state.llm = ChatOpenAI(
                model="ft:gpt-4o-mini-2024-07-18:personal::9zIKV308",
                temperature = temperature,
                max_tokens=max_length
        )

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

def generate_response(model,prompt):
    model.invoke(prompt)


# Handle user input
if user_input := st.chat_input("What's poppin'?"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get that AI response
    with st.chat_message("assistant"):
        response = llm.invoke(user_input)
        st.write(response.content)
    st.session_state.messages.append({"role": "assistant", "content": response.content})
    print(st.session_state.messages)




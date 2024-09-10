# main.py
import streamlit as st
from config import OPENAI_API_KEY, GROQ_API_KEY, LANGCHAIN_TRACING_V2, LANGCHAIN_API_KEY, LANGCHAIN_PROJECT
from models import ChatbotFactory
from utils import ConversationManager, handle_chatbot_error, render_sidebar
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(page_title="Chatbot Playground")

def intro_page():
    st.title("Welcome to the Chatbot Playground")
    
    st.write("This versatile chatbot playground offers multiple AI language models to explore.")
    
    st.markdown("""
    ### Features:
    - Multiple AI models with distinct personalities
    - Adjustable parameters for customized interactions
    - Optional conversation history with up to 6 messages
    """)
    
    st.write("Click 'Begin Interaction' to start your conversation with the AI.")
    
    if st.button("Begin Interaction"):
        st.session_state.show_chat = True
        st.rerun()

@handle_chatbot_error
def create_chain(bot, use_history):
    default_system_message = f"You are a helpful AI assistant. Keep response tokens under {bot.max_len}"
    system_message = bot.system_message or default_system_message
    
    if use_history:
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_message),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
        ])
    else:
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_message),
            ("human", "{input}"),
        ])
    
    chain = prompt | bot.model | StrOutputParser()
    return chain

def chat_interface():
    model_name, temp, max_len, use_history = render_sidebar()
    
    try:
        bot = ChatbotFactory.create_bot(model_name, temp, max_len)
        chain = create_chain(bot, use_history)
    except Exception as e:
        st.error(f"Shit's fucked up: {str(e)}")
        return

    conversation = ConversationManager()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            
    if user_input := st.chat_input("Spit your game:"):
        conversation.add_message("user", user_input)
        with st.chat_message("user"):
            st.write(user_input)
        
        with st.chat_message("assistant"):
            try:
                if use_history:
                    chat_history = conversation.get_history()
                    response = chain.invoke({"input": user_input, "chat_history": chat_history})
                else:
                    response = chain.invoke({"input": user_input})
                st.write(response)
                conversation.add_message("assistant", response)
            except Exception as e:
                st.error(f"Shit hit the fan: {str(e)}")
    
    st.sidebar.button('Clear Chat History', on_click=conversation.clear_history)

def main():
    if "show_chat" not in st.session_state:
        st.session_state.show_chat = False
    
    if not st.session_state.show_chat:
        intro_page()
    else:
        chat_interface()

if __name__ == "__main__":
    main()
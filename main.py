import streamlit as st
from config import OPENAI_API_KEY, GROQ_API_KEY #,LANGCHAIN_TRACING_V2,LANGCHAIN_API_KEY,LANGCHAIN_PROJECT
from models import get_model
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(page_title="Flex Chatbot")

#with chat history
def create_chain(llm, system_message, use_history, max_len):
    default_system_message= f"You are a helpful AI assistant. Keep response tokens under {max_len}"
    if use_history:
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_message if system_message else default_system_message),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
        ])
    else:
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_message if system_message else default_system_message),
            ("human", "{input}"),
        ])
    chain = prompt | llm | StrOutputParser()
    return chain
# # no chat history vanilla
# def create_chain(llm, system_message,max_len):
#     default_system_message= f"You are a helpful AI assistant. Keep response tokens under {max_len}"
#     prompt = ChatPromptTemplate.from_messages([
#         ("system", system_message if system_message else default_system_message),
#         ("human", "{input}"),
#     ])
#     chain = prompt | llm | StrOutputParser()
#     return chain
# # with chat history vanilla
# def create_chain(llm, system_message):
#     prompt = ChatPromptTemplate.from_messages([
#         ("system", system_message if system_message else "You are a helpful AI assistant."),
#         MessagesPlaceholder(variable_name="chat_history"),
#         ("human", "{input}"),
#     ])
#     chain = prompt | llm | StrOutputParser()
#     return chain

## when calling chain.invoke:
# chat_history = st.session_state.messages[-6:]  # Last 3 exchanges
# response = chain.invoke({"input": user_input, "chat_history": chat_history})

def main():
    with st.sidebar:
        st.title("Flex Chatbot")
        st.subheader('Models and Parameters')
        model_name = st.selectbox('Choose a model', ['GPT', 'TM3000', 'GS6000','Groq'], key='selected_model')
        temp = st.slider('temperature', min_value=0.01, max_value=1.0, value=0.5, step=0.01)
        max_len = st.slider('max_length', min_value=32, max_value=256, value=128, step=4)
        
        # Add toggle for chat history
        use_history = st.toggle("Use Chat History", value=True)

        st.markdown('📖')
    
    try:
        llm, system_message = get_model(model_name, temp, max_len)
        chain = create_chain(llm, system_message, use_history, max_len)
    except Exception as e:
        st.error(f"Shit's fucked up: {str(e)}")
        return

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    # option to toggle chat history        
    if user_input := st.chat_input("Spit your game:"):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)
        
        with st.chat_message("assistant"):
            try:
                if use_history:
                    chat_history = st.session_state.messages[-6:]  # Last 3 exchanges
                    response = chain.invoke({"input": user_input, "chat_history": chat_history})
                else:
                    response = chain.invoke({"input": user_input})
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Shit hit the fan: {str(e)}")
    # no chat history vanilla version
    # if user_input := st.chat_input("Spit your game:"):
    #     st.session_state.messages.append({"role": "user", "content": user_input})
    #     with st.chat_message("user"):
    #         st.write(user_input)
        
    #     with st.chat_message("assistant"):
    #         try:
    #             response = chain.invoke({"input": user_input})
    #             st.write(response)
    #             st.session_state.messages.append({"role": "assistant", "content": response})
    #         except Exception as e:
    #             st.error(f"Shit hit the fan: {str(e)}")
    def clear_chat_history():
        st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

if __name__ == "__main__":
    main()
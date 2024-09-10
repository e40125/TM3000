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

# # when calling chain.invoke:
# chat_history = st.session_state.messages[-6:]  # Last 3 exchanges
# response = chain.invoke({"input": user_input, "chat_history": chat_history})

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




#models.py original
# models.py
# from langchain_openai import ChatOpenAI
# from langchain_groq import ChatGroq

# def get_model(model_name, temp, max_len):
#     model_config = {
#         'GPT': {
#             'class': ChatOpenAI,
#             'params': {"model": "gpt-4o-mini", "temperature": temp, "max_tokens": max_len}
#         },
#         'TM3000': {
#             'class': ChatOpenAI,
#             'params': {"model": "ft:gpt-4o-mini-2024-07-18:personal::9zIKV308", "temperature": temp, "max_tokens": max_len},
#             'system_message': "Tao Master 3000 is a wise Taoist sage that offers guidance based on Taoist principles.Keep response tokens under {max_len}"
#         },
#         'GS6000': {
#             'class': ChatOpenAI,
#             'params': {"model": "ft:gpt-4o-mini-2024-07-18:personal:gs6000:9ytKXg3C", "temperature": temp, "max_tokens": max_len},
#             'system_message': "GS6000 is a self-improvement chatbot that talks like an G. Keep response tokens under {max_len}"
#         },
#         'Groq': {
#             'class': ChatGroq,
#             'params': {"model": "Llama-3.1-8B-Instant", "temperature": temp, "max_tokens": max_len}
#         }
#     }
    
#     config = model_config[model_name]
#     model = config['class'](**config['params'])
#     return model, config.get('system_message')
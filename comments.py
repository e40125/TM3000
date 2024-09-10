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
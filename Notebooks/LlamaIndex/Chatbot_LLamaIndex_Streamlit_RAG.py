import sys
import os
import openai
import streamlit as st

os.environ["OPENAI_API_KEY"] = "<key>"

import openai
from llama_index.core import VectorStoreIndex
from llama_index.core import StorageContext
from llama_index.core import load_index_from_storage

PERSIST_DIR = "../../Index/ChatExample/VectorStoreIndex/"

vectorstoreindex = load_index_from_storage(storage_context=StorageContext.from_defaults(persist_dir=PERSIST_DIR))
chat_engine = vectorstoreindex.as_chat_engine(chat_mode="condense_question", verbose=True)

st.header("Chat with Documents from your Vector Index")
# Initialize the chat message history
if "messages" not in st.session_state.keys(): 
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about the Documents!"}
    ]
# Prompt for user input and save to chat history    
if prompt := st.chat_input("Your question"): 
    st.session_state.messages.append({"role": "user", "content": prompt})

# Display the prior chat messages
for message in st.session_state.messages: 
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            # Add response to message history
            st.session_state.messages.append(message)
import os
import openai
import streamlit as st
from llama_index.core import VectorStoreIndex
from llama_index.core import StorageContext
from llama_index.core import load_index_from_storage

PERSIST_DIR = "../../Index/VectorStoreIndex/"

# Title
st.title("💬 Chat with Documents from your Vector Index")

# Sidebar for API Key input
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    if openai_api_key:
        os.environ["OPENAI_API_KEY"] = openai_api_key
        st.success("API key set successfully!")
    else:
        st.warning("Please add your OpenAI API key to continue.")
        st.stop()

# Load the vector store index
try:
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    vectorstoreindex = load_index_from_storage(storage_context=storage_context)
    chat_engine = vectorstoreindex.as_chat_engine(chat_mode="condense_question", verbose=True)
except Exception as e:
    st.error(f"Failed to load the vector store index: {e}")
    st.stop()

# Initialize the chat message history
if "messages" not in st.session_state:
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

# If the last message is not from the assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = chat_engine.chat(st.session_state.messages[-1]["content"])
                st.write(response.response)
                st.session_state.messages.append(
                    {"role": "assistant", "content": response.response}
                )
            except Exception as e:
                st.error(f"Error generating response: {e}")

            
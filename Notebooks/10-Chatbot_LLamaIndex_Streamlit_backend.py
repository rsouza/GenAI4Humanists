#Run on terminal: python -m streamlit run ./10-Chatbot_LLamaIndex_Streamlit_backend.py

import sys
import subprocess
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'llama-index'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'streamlit'])

import os
import sys
import shutil
import glob
import re
import logging
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

import openai
import streamlit as st

import os
os.environ["OPENAI_API_KEY"] = "key"

import sys
import shutil
import glob
import logging
from pathlib import Path

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import openai

## Llamaindex readers
from llama_index.core import SimpleDirectoryReader

## LlamaIndex Index Types
from llama_index.core import ListIndex
from llama_index.core import VectorStoreIndex
from llama_index.core import TreeIndex
from llama_index.core import KeywordTableIndex
from llama_index.core import SimpleKeywordTableIndex
from llama_index.core import DocumentSummaryIndex
from llama_index.core import KnowledgeGraphIndex


## LlamaIndex Context Managers
from llama_index.core import StorageContext
from llama_index.core import load_index_from_storage
from llama_index.core.response_synthesizers import get_response_synthesizer
from llama_index.core.response_synthesizers import ResponseMode
from llama_index.core.schema import Node

## LlamaIndex Templates
from llama_index.core.prompts import PromptTemplate
from llama_index.core.prompts import ChatPromptTemplate
from llama_index.core.base.llms.types import ChatMessage, MessageRole

## LlamaIndex Callbacks
from llama_index.core.callbacks import CallbackManager
from llama_index.core.callbacks import LlamaDebugHandler

PERSIST_DIR = "../Index/ChatExample/"

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
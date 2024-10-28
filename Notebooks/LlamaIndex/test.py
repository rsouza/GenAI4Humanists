#pip install streamlit llama-index openai
import streamlit as st
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex
import os

# Streamlit setup
st.title("Document Processing with LlamaIndex")

# Step 1: Ask for OpenAI API Key
api_key = st.text_input("Enter your OpenAI API key:", type="password")

# Verify API key is provided
if not api_key:
    st.warning("Please enter your OpenAI API key to proceed.")
    st.stop()
else:
    # Set OpenAI API key as an environment variable for LlamaIndex
    os.environ["OPENAI_API_KEY"] = api_key

# Step 2: Upload documents
uploaded_files = st.file_uploader("Upload your documents (txt, pdf, etc.):", accept_multiple_files=True)

# Check if any documents were uploaded
if uploaded_files:
    st.success(f"{len(uploaded_files)} document(s) uploaded successfully!")

    # Save uploaded documents temporarily
    doc_paths = []
    for uploaded_file in uploaded_files:
        doc_path = f"/tmp/{uploaded_file.name}"
        with open(doc_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        doc_paths.append(doc_path)

    # Load documents with LlamaIndex
    st.write("Processing documents with LlamaIndex...")
    document_loader = SimpleDirectoryReader(input_files=doc_paths)
    documents = document_loader.load_data()

    # Indexing the documents
    index = GPTVectorStoreIndex(documents)
    st.write("Documents have been indexed successfully!")

    # Add a sample query (optional)
    query = st.text_input("Enter a query to search the indexed documents:")
    if query:
        response = index.query(query)
        st.write("Response:", response)
else:
    st.info("Please upload one or more documents.")


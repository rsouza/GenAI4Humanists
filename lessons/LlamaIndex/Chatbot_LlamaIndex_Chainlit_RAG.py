import os
import chainlit as cl
from llama_index.core import StorageContext, load_index_from_storage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Path to the index (relative to the lesson directory)
PERSIST_DIR = "../../Index/VectorStoreIndex/"

@cl.on_chat_start
async def start():
    """
    This function is called when the chat session starts.
    It loads the LlamaIndex and initializes the chat engine.
    """
    try:
        # Load the index from disk
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context=storage_context)
        
        # Create a chat engine
        # 'context' mode allows the chatbot to remember previous interactions
        chat_engine = index.as_chat_engine(chat_mode="context", verbose=True)
        
        # Store the chat engine in the user session to maintain state
        cl.user_session.set("chat_engine", chat_engine)
        
        await cl.Message(content="Greetings! I'm your Chainlit RAG assistant. Ask me anything about your documents.").send()
    
    except Exception as e:
        error_msg = f"Failed to load the index. Make sure it exists at {PERSIST_DIR}. Error: {e}"
        await cl.Message(content=error_msg).send()

@cl.on_message
async def main(message: cl.Message):
    """
    This function is called whenever a user sends a message.
    """
    chat_engine = cl.user_session.get("chat_engine")
    
    if not chat_engine:
        await cl.Message(content="Chat engine not initialized properly.").send()
        return

    # Use cl.make_async to run the synchronous LlamaIndex chat call without blocking
    # response = await cl.make_async(chat_engine.chat)(message.content)
    
    # Alternatively, use streaming if supported
    msg = cl.Message(content="")
    
    # We use cl.make_async for the chat call
    response = await cl.make_async(chat_engine.chat)(message.content)
    
    msg.content = response.response
    await msg.send()

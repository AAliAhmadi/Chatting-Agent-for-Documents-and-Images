import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from config import USE_OPENAI, OPENAI_API_KEY, GEMMA_MODEL, OPENAI_MODEL

from utils import (
    encode_image,
    read_text_file,
    init_chat_history,
    display_chat_history,
    store_uploaded_file,
    get_uploaded_file_content,
)

# -----------------------------
# Initialize AI model
# -----------------------------
if USE_OPENAI:
    from langchain_openai import ChatOpenAI
    if not OPENAI_API_KEY:
        st.error("⚠️ OpenAI API key not set. Get one at https://platform.openai.com/account/api-keys and enter in config.py")
        st.stop()
    llm = ChatOpenAI(model=OPENAI_MODEL, api_key=OPENAI_API_KEY)
    st.info("Using OpenAI GPT model (requires API key and may incur costs).")
else:
    llm = ChatOllama(model=GEMMA_MODEL)
    st.info(f"Using local AI model: {GEMMA_MODEL} (free, no API key required)")

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🧠 Smart Document & Image Chat with Memory")
st.caption("Ask follow-up questions about documents or images. The model remembers context.")

# Initialize chat history
chat_history = init_chat_history()
display_chat_history(chat_history)

# Clear history button
if st.button("🗑️ Clear Chat History"):
    st.session_state["chat_history"].clear()
    st.session_state["uploaded_files"] = {}
    st.experimental_rerun()

# Uploaders
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
uploaded_text_file = st.file_uploader("Upload a text/doc file", type=["txt", "pdf", "docx"])
question = st.text_input("Enter your question")

# -----------------------------
# Store uploaded files in memory
# -----------------------------
if uploaded_text_file:
    store_uploaded_file(uploaded_text_file, "document_content")

document_content = get_uploaded_file_content("document_content")

# -----------------------------
# Handle user input
# -----------------------------
if question:
    # Build history string
    history_str = ""
    for msg in chat_history:
        speaker = "User" if msg["role"] == "user" else "Assistant"
        history_str += f"{speaker}: {msg['content']}\n"

    input_content = question

    # Prepare prompt
    if uploaded_image:
        image = encode_image(uploaded_image)
        prompt = ChatPromptTemplate.from_template(
            """You are a helpful assistant that can describe and discuss images.
Conversation history:
{history}

User question:
{text}

Image: data:image/jpeg;base64,{image}"""
        )
        response = llm.invoke(prompt.format(history=history_str, text=input_content, image=image))

    elif document_content:
        prompt = ChatPromptTemplate.from_template(
            """You are a helpful assistant that answers questions based on a document.
Conversation history:
{history}

Document content:
{text_content}

User question:
{text}

Answer using both document and prior conversation."""
        )
        response = llm.invoke(
            prompt.format(history=history_str, text_content=document_content[:5000], text=input_content)
        )
    else:
        prompt = ChatPromptTemplate.from_template(
            """You are a helpful conversational assistant.
Conversation history:
{history}

User question:
{text}

Answer helpfully and naturally."""
        )
        response = llm.invoke(prompt.format(history=history_str, text=input_content))

    # Display and store response
    st.chat_message("assistant").write(response.content)
    chat_history.append({"role": "user", "content": question})
    chat_history.append({"role": "assistant", "content": response.content})

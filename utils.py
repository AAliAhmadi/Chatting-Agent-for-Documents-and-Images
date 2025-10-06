import base64
import docx
import PyPDF2
import streamlit as st


def encode_image(image_file):
    """Convert image file to base64 string."""
    return base64.b64encode(image_file.read()).decode()


def read_text_file(file):
    """
    Read content from text, PDF, or DOCX file.
    Warns if the file has no extractable text.
    """
    text = ""
    if file.type == "text/plain":
        text = file.read().decode()

    elif file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        if not text.strip():
            st.warning("⚠️ PDF uploaded, but no extractable text found. It may be scanned or image-based.")

    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        text = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
        if not text.strip():
            st.warning("⚠️ DOCX uploaded, but no text found in document.")

    else:
        st.error("Unsupported file type!")
        return None

    return text if text.strip() else None


def init_chat_history():
    """Initialize or return existing chat history in Streamlit session state."""
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    return st.session_state["chat_history"]


def display_chat_history(chat_history):
    """Display previous messages in Streamlit chat."""
    for msg in chat_history:
        if msg["role"] == "user":
            st.chat_message("user").write(msg["content"])
        else:
            st.chat_message("assistant").write(msg["content"])

def store_uploaded_file(file, key):
    """Store uploaded file content in Streamlit session state."""
    if "uploaded_files" not in st.session_state:
        st.session_state["uploaded_files"] = {}
    st.session_state["uploaded_files"][key] = read_text_file(file)


def get_uploaded_file_content(key):
    """Retrieve previously stored file content from session state."""
    return st.session_state.get("uploaded_files", {}).get(key, None)


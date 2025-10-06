## 🧠 Smart Document & Image Chat with Memory

This Streamlit app lets you chat with documents and images, using either:

Gemma3:4b (local and free via Ollama), or

OpenAI GPT models (requires API key).

It remembers your chat history and uploaded documents, so you can ask multiple follow-up questions naturally — like a conversation!

## ✨ Features

✅ Upload and chat with:

- .txt, .pdf, and .docx documents

- .jpg, .jpeg, or .png images

✅ Persistent memory:

- Keeps chat history for ongoing conversations

- Remembers uploaded files — no need to re-upload for follow-up questions

✅ Flexible model options:

- Gemma3:4b (local, free) via Ollama

- OpenAI GPT (cloud) with your API key (paid)

✅ Clean modular code:

- main.py → Streamlit UI

- utils.py → helper functions

- config.py → model and API settings

## 🏗️ Project Structure
```
📂 smart-chat-app
├── main.py               # Streamlit app entry point
├── utils.py              # Helper functions (file handling, encoding, memory)
├── config.py             # Model and API configuration
├── requirements.txt      # Python dependencies
├── README.md             # You are here 😄
└── .streamlit/
    └── config.toml       # Optional UI customization
```

## ⚙️ Installation
1️⃣ Clone this repository
```bash
git clone https://github.com/YOUR_USERNAME/smart-chat-app.git
cd smart-chat-app
```

2️⃣ Create a virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate    # On Windows
```
# or
```bash
source venv/bin/activate # On macOS/Linux
```

3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

## 🔑 Model Setup
### Option A: 🧠 Use Gemma (Free, Local)

- 1. Install Ollama


- 2. Pull the Gemma model:

```bash
ollama pull gemma3:4b
```

- 3. Make sure Ollama is running in the background.

- 4. No API key needed!

### Option B: ☁️ Use OpenAI GPT

- 1. Get your API key from OpenAI’s platform

- 2. Open config.py and update:
```bash
USE_OPENAI = True
OPENAI_API_KEY = "sk-your-key-here"
```

⚠️ Note: Using OpenAI models requires a paid API key — usage will be billed according to OpenAI pricing.

## 🚀 Run the App
```bash
streamlit run main.py
```

Then open the provided local URL (usually http://localhost:8501) in your browser.

## 💬 Usage

- 1. Upload an image or document (.txt, .pdf, .docx).

- 2. Type a question like:
```bash
What is this document about?
```

or
```bash
Describe the main object in the image.
```

- 3. The model answers based on:

-- The document or image you uploaded, and

-- The previous chat history (multi-turn memory).

- 4. You can ask follow-up questions — no need to re-upload the same file.

- 5. Use the 🗑️ Clear Chat History button to reset memory.

## 🎨 Optional Streamlit Customization

You can add a .streamlit/config.toml file for dark mode or theming:

[theme]
base="dark"
primaryColor="#00ADB5"
backgroundColor="#222831"
secondaryBackgroundColor="#393E46"
textColor="#EEEEEE"
font="sans serif"

🧩 Requirements

requirements.txt includes:

streamlit
langchain
langchain-openai
langchain-community
PyPDF2
python-docx

🧠 How It Works

Files and chat messages are stored in st.session_state so they persist across turns.

Uploaded documents are read (via PyPDF2, docx, or plain text).

The LLM (Gemma or GPT) gets:

Chat history

Document or image context

The user’s new question

The response is displayed and stored for context in the next turn.

☁️ Push to GitHub

Once everything works, you can upload your code to your GitHub account.

1️⃣ Initialize git (if not already)
git init

2️⃣ Add your remote repo
git remote add origin https://github.com/YOUR_USERNAME/smart-chat-app.git

3️⃣ Add and commit files
git add .
git commit -m "Initial commit: smart chat app with memory"

4️⃣ Push to GitHub
git branch -M main
git push -u origin main


✅ Done! Your repository will now be visible on GitHub at:

https://github.com/YOUR_USERNAME/smart-chat-app

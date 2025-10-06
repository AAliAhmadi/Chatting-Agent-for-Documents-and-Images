"""
Configuration for AI model.

You can choose between:
- Gemma3 (local, free)
- OpenAI GPT (requires API key and paid subscription)

For OpenAI:
- Get an API key at https://platform.openai.com/account/api-keys
- You will be billed per usage.
"""

USE_OPENAI = False  # Set True to use OpenAI GPT
OPENAI_API_KEY = ""  # Your OpenAI API key here

# Model names
GEMMA_MODEL = "gemma3:4b"
OPENAI_MODEL = "gpt-4o"

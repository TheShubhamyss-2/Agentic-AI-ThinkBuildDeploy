"""
CodeSensei — Configuration & LLM Connection
=============================================
This file is FULLY PROVIDED. No TODOs here.

It loads environment variables and initializes the Gemini LLM
via LangChain's ChatGoogleGenerativeAI wrapper.

Concepts used:
- python-dotenv for environment management (Lecture 2)
- LangChain LLM wrappers (Lecture 3 & 4)
"""

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# ──────────────────────────────────────────────
# Load environment variables from .env file
# ──────────────────────────────────────────────
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found! "
        "Copy .env.example to .env and add your key.\n"
        "Get one at: https://aistudio.google.com/apikey"
    )

# ──────────────────────────────────────────────
# Initialize the Gemini LLM via LangChain
# ──────────────────────────────────────────────
# This is the LLM instance that all agents will use.
# We use ChatGoogleGenerativeAI which wraps Google's
# Gemini API into LangChain's standard interface.
#
# temperature=0.2 → More deterministic, less creative
#   (good for code review — we want consistent analysis)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.2,
)

print("Gemini LLM initialized successfully!")

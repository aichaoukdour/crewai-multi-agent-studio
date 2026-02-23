import os
from dotenv import load_dotenv
from crewai import LLM

# Load environment variables
load_dotenv()

# Accessing an LLM
# Note: Ensure GROQ_API_KEY is set in your environment or .env file
AGENT_LLM = LLM(model="groq/llama-3.3-70b-versatile")

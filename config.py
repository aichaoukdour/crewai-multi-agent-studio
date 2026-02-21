import os
from dotenv import load_dotenv
from crewai import LLM

# Load environment variables
load_dotenv()

# Accessing an LLM
# Note: Ensure OPENAI_API_KEY is set in your environment or .env file
AGENT_LLM = LLM(model="openai/gpt-4o-mini")

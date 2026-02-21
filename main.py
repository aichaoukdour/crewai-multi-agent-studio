import os
from dotenv import load_dotenv
from crewai import LLM, Agent

# Load environment variables
load_dotenv()

# Accessing an LLM
AGENT_LLM = LLM(model="openai/gpt-4o-mini")

# Define the Research agent
research_agent = Agent(
  role="Senior Research Analyst",
  goal="Analyze the content of the provided website and extract key insights.",
  backstory="""You are a world-class research analyst with a knack for identifying
  the most important trends and data points from any text. You have a keen eye for detail
  and are known for your concise and insightful summaries.""",
  verbose=False,
  llm=AGENT_LLM
)

if __name__ == "__main__":
    print("✅ Research Agent Created!")
    print(f"Role: {research_agent.role}")
    print(f"Goal: {research_agent.goal}")


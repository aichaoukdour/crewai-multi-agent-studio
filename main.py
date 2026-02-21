import os
from dotenv import load_dotenv
from typing import Dict, Any
from pydantic import BaseModel
from crewai import LLM, Agent, Task, Crew, Process
from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

# Load environment variables
load_dotenv()

# Accessing an LLM
AGENT_LLM = LLM(model="openai/gpt-4o-mini")

# Adding a tool
search_tool_instance = DuckDuckGoSearchRun()

@tool("DuckDuckGo Search")
def search_tool(query: str) -> str:
    """A tool for searching the web using DuckDuckGo."""
    return search_tool_instance.run(query)

# Define the Research agent
research_agent = Agent(
  role="Senior Research Analyst",
  goal="Analyze the content of the provided website and extract key insights.",
  backstory="""You are a world-class research analyst with a knack for identifying
  the most important trends and data points from any text. You have a keen eye for detail
  and are known for your concise and insightful summaries.""",
  verbose=False,
  llm=AGENT_LLM,
  tools=[search_tool]
)

# CODE: Create a research task
research_task = Task(
    description="""Research the latest developments in AI agent technology in 2025.
    Focus on:
    1. Key breakthroughs and innovations
    2. Major companies and their contributions
    3. Practical applications and use cases
    4. Future trends and predictions

    Provide a comprehensive analysis that a business executive could use for strategic planning.""",
    expected_output="A detailed research report with key insights, trends, and actionable recommendations about AI agent technology developments in 2025.",
    agent=research_agent
)

# CODE: Assemble your research crew
research_crew = Crew(
    agents=[research_agent],
    tasks=[research_task],
    process=Process.sequential,
    verbose=False
)

if __name__ == "__main__":
    print(" Research Agent Created!")
    print("\n Research Task Created!")
    print("\n Launching Research Crew...")
    # research_result = research_crew.kickoff()
    # print(research_result.raw)

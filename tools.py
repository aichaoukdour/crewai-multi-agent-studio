from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

# Initialize the search tool
search_tool_instance = DuckDuckGoSearchRun()

# Wrap the search tool with the CrewAI @tool decorator
@tool("DuckDuckGo Search")
def search_tool(query: str) -> str:
    """A tool for searching the web using DuckDuckGo."""
    return search_tool_instance.run(query)

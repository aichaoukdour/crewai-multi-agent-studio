from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

# Initialize the search tool
search_tool_instance = DuckDuckGoSearchRun()

# Wrap the search tool with the CrewAI @tool decorator
@tool("DuckDuckGo Search")
def search_tool(query: str) -> str:
    """A tool for searching the web using DuckDuckGo."""
    try:
        return search_tool_instance.run(query)
    except Exception as e:
        return f"Error performing search: {str(e)}. Please proceed with available information or try a different approach."

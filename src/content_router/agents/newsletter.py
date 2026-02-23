from crewai import Agent
from content_router.config.settings import AGENT_LLM
from content_router.tools.search import search_tool

def create_newsletter_agents():
    """Create agents specialized for newsletter content"""
    newsletter_researcher = Agent(
        role="Newsletter Content Researcher",
        goal="Extract key insights from web content for newsletter format",
        backstory="""You are an expert at identifying the most newsworthy and actionable
        insights from web content.""",
        verbose=False,
        tools=[search_tool],
        llm=AGENT_LLM,
        max_iter=5
    )

    newsletter_writer = Agent(
        role="Newsletter Writer",
        goal="Create engaging newsletter content that provides immediate value",
        backstory="""You are a newsletter specialist who knows how to craft content that
        busy professionals want to read.""",
        verbose=False,
        llm=AGENT_LLM
    )

    return newsletter_researcher, newsletter_writer

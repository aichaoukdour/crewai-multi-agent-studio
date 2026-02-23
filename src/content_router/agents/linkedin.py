from crewai import Agent
from content_router.config.settings import AGENT_LLM
from content_router.tools.search import search_tool

def create_linkedin_agents():
    """Create agents specialized for LinkedIn content"""
    linkedin_researcher = Agent(
        role="LinkedIn Content Researcher",
        goal="Extract professional insights suitable for LinkedIn audience",
        backstory="""You are an expert at identifying professional insights and industry
        trends that resonate with LinkedIn's professional audience.""",
        verbose=False,
        tools=[search_tool],
        llm=AGENT_LLM,
        max_iter=5
    )

    linkedin_writer = Agent(
        role="LinkedIn Content Writer",
        goal="Create engaging LinkedIn posts that drive professional engagement",
        backstory="""You are a LinkedIn content specialist who knows how to craft posts
        that get noticed in the professional feed.""",
        verbose=False,
        llm=AGENT_LLM
    )

    return linkedin_researcher, linkedin_writer

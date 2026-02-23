from crewai import Agent
from content_router.config.settings import AGENT_LLM
from content_router.tools.search import search_tool

def create_blog_agents():
    """Create agents specialized for blog content"""
    blog_researcher = Agent(
        role="Blog Content Researcher",
        goal="Extract and analyze web content to identify key insights for blog posts",
        backstory="""You are an expert content researcher who specializes in analyzing
        web content and identifying the most valuable insights for creating engaging blog posts.""",
        verbose=False,
        tools=[search_tool],
        llm=AGENT_LLM,
        max_iter=5
    )

    blog_writer = Agent(
        role="Blog Content Writer",
        goal="Transform research into engaging, well-structured blog posts",
        backstory="""You are a skilled blog writer with expertise in creating compelling content.""",
        verbose=False,
        llm=AGENT_LLM
    )

    return blog_researcher, blog_writer

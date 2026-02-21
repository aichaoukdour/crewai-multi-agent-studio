from crewai import Agent
from config import AGENT_LLM
from tools import search_tool

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

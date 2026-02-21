import os
from typing import Dict, Any
from pydantic import BaseModel
from dotenv import load_dotenv
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

# 🤖🤖 Define specialized agent pairs

def create_blog_agents():
    """Create agents specialized for blog content"""

    blog_researcher = Agent(
        role="Blog Content Researcher",
        goal="Extract and analyze web content to identify key insights for blog posts",
        backstory="""You are an expert content researcher who specializes in analyzing
        web content and identifying the most valuable insights for creating engaging blog posts.
        You excel at understanding complex topics and breaking them down into digestible content.""",
        verbose=False,
        tools=[search_tool], # CODE: Add a search tool to the researcher agent
        llm=AGENT_LLM,
        max_iter=5
    )

    blog_writer = Agent(
        role="Blog Content Writer",
        goal="Transform research into engaging, well-structured blog posts",
        backstory="""You are a skilled blog writer with expertise in creating compelling content
        that engages readers and drives meaningful discussions. You excel at taking complex
        information and making it accessible and interesting.""",
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
        insights from web content. You understand what makes content valuable for newsletter
        subscribers and how to present information concisely.""",
        verbose=False,
        tools=[search_tool],
        llm=AGENT_LLM,
        max_iter=5
    )

    newsletter_writer = Agent(
        role="Newsletter Writer",
        goal="Create engaging newsletter content that provides immediate value",
        backstory="""You are a newsletter specialist who knows how to craft content that
        busy professionals want to read. You excel at creating scannable, actionable content
        with clear takeaways.""",
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
        trends that resonate with LinkedIn's professional audience. You understand what
        content drives engagement on professional networks.""",
        verbose=False,
        tools=[search_tool],
        llm=AGENT_LLM,
        max_iter=5
    )

    linkedin_writer = Agent(
        role="LinkedIn Content Writer",
        goal="Create engaging LinkedIn posts that drive professional engagement",
        backstory="""You are a LinkedIn content specialist who knows how to craft posts
        that get noticed in the professional feed. You excel at creating content that
        sparks meaningful professional discussions.""",
        verbose=False,
        llm=AGENT_LLM
    )

    return linkedin_researcher, linkedin_writer

# 📝 Define task creation functions for each content type

def create_blog_tasks(researcher, writer, url):
    """Create tasks for blog content generation"""

    # CODE: Define the blog research task
    research_task = Task(
        description=f"""
        Analyze the content from {url} and extract key insights for a blog post.
        Your analysis should identify:
        1. Main themes and key points
        2. Interesting insights or data points
        3. Potential angles for blog content
        4. Target audience considerations
        5. SEO-worthy topics and keywords

        Provide a comprehensive research summary that will guide blog writing.
        """,
        expected_output="A detailed research summary with key insights, themes, and recommendations for blog content",
        agent=researcher 
    )

    writing_task = Task(
        description="""
        Create an engaging blog post based on the research findings.

        Requirements:
        - 800-1200 words
        - Engaging headline
        - Clear introduction with hook
        - Well-structured body with subheadings
        - Actionable insights or takeaways
        - Strong conclusion
        - SEO-optimized content
        - Professional yet accessible tone

        Format the output in markdown.
        """,
        expected_output="A complete, well-structured blog post in markdown format",
        agent=writer,
        # CODE: add the research task as context to the writing task
        context=[research_task]
    )

    return [research_task, writing_task]

def create_newsletter_tasks(researcher, writer, url):
    """Create tasks for newsletter content generation"""

    research_task = Task(
        description=f"""
        Analyze the content from {url} and extract the most newsworthy insights for a newsletter.
        Focus on:
        1. Most important news or updates
        2. Actionable insights subscribers can use immediately
        3. Key statistics or data points
        4. Industry implications
        5. Quick takeaways for busy professionals

        Prioritize information that provides immediate value.
        """,
        expected_output="A focused research summary highlighting the most valuable and actionable insights",
        agent=researcher
    )

    writing_task = Task(
        description="""
        Create a compelling newsletter section based on the research.

        Requirements:
        - 400-600 words
        - Catchy subject line
        - Scannable format with bullet points
        - Clear action items or takeaways
        - Conversational yet professional tone
        - Include relevant links or resources
        - End with a clear call-to-action

        Format for easy reading in email.
        """,
        expected_output="A complete newsletter section with subject line and formatted content",
        agent=writer,
        context=[research_task]
    )

    return [research_task, writing_task]

def create_linkedin_tasks(researcher, writer, url):
    """Create tasks for LinkedIn content generation"""

    research_task = Task(
        description=f"""
        Analyze the content from {url} and extract insights suitable for LinkedIn audience.
        Consider what would engage LinkedIn's professional audience based on the content.
        """,
        expected_output="Research summary focused on professional insights and engagement opportunities",
        agent=researcher
    )

    writing_task = Task(
        description="""
        Create an engaging LinkedIn post based on the research.

        Requirements:
        - 150-300 words (optimal LinkedIn length)
        - Professional yet conversational tone
        - Include relevant hashtags (3-5)
        - Pose a question to encourage engagement
        - Share a key insight or lesson learned from the content
        - Use line breaks for readability
        - Include a call-to-action for comments

        Make it shareable and discussion-worthy.
        """,
        expected_output="A complete LinkedIn post with hashtags and engagement elements",
        agent=writer,
        context=[research_task]
    )

    return [research_task, writing_task]

# Define the Research agent (Initial from part 1)
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
    print("? Research Agent Created!")
    print("\n? Research Task Created!")
    print("\n?? Launching Research Crew...")
    research_result = research_crew.kickoff()
    print(research_result.raw)

# 🧠 Define the memory for the Flow
# The state model, or memory, is like a shared notebook that all agents can read and write to.
# It persists data throughout the entire workflow execution.

# CODE: Define the state model and add its fields
class ContentState(BaseModel):
  """
  State model that tracks information throughout the content creation workflow.

  Think of this as a form that gets filled out as the workflow progresses:
  - Start: Only URL is filled
  - After routing: Content type is determined
  - After processing: Final content is ready
  - Throughout: Metadata can be added by any step
  """
  url: str = "" # CODE
  content_type: str = ""  
  final_content: str = ""  
  metadata: Dict[str, Any] = {} # CODE


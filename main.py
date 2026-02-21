from crewai import Agent, Task, Crew, Process
from config import AGENT_LLM
from tools import search_tool
from agents import create_blog_agents, create_newsletter_agents, create_linkedin_agents
from tasks import create_blog_tasks, create_newsletter_tasks, create_linkedin_tasks
from models import ContentState

def run_research_demonstration():
    """Run the initial research analyst demonstration"""
    # Define the Research agent
    research_agent = Agent(
        role="Senior Research Analyst",
        goal="Analyze the content of the provided website and extract key insights.",
        backstory="""You are a world-class research analyst with a knack for identifying
        the most important trends and data points from any text.""",
        verbose=False,
        llm=AGENT_LLM,
        tools=[search_tool]
    )

    # Create a research task
    research_task = Task(
        description="""Research the latest developments in AI agent technology in 2025.""",
        expected_output="A detailed research report with key insights, trends, and actionable recommendations.",
        agent=research_agent
    )

    # Assemble and launch the crew
    research_crew = Crew(
        agents=[research_agent],
        tasks=[research_task],
        process=Process.sequential,
        verbose=False
    )

    print("✅ Research Agent Created!")
    print("\n🚀 Launching Research Crew...")
    research_result = research_crew.kickoff()
    
    print("\n" + "="*50)
    print("📊 RESEARCH REPORT COMPLETE")
    print("="*50)
    print(research_result.raw)

if __name__ == "__main__":
    run_research_demonstration()
    
    print("\n" + "-"*50)
    print("📌 Roles, models, and applications of crews")
    print("Code is now refactored into a modular structure!")
    print("- config.py: Environment and LLM setup")
    print("- tools.py: Reusable tools")
    print("- agents.py: Specialized agent teams")
    print("- tasks.py: Content-specific tasks")
    print("- models.py: Flow state memory")
    print("-"*50)

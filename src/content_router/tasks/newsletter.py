from crewai import Task

def create_newsletter_tasks(researcher, writer, url):
    """Create tasks for newsletter content generation"""
    research_task = Task(
        description=f"Analyze content from {url} and extract newsworthy insights for a newsletter.",
        expected_output="A focused research summary highlighting the most valuable and actionable insights",
        agent=researcher
    )

    writing_task = Task(
        description="Create a compelling newsletter section based on the research.",
        expected_output="A complete newsletter section with subject line and formatted content",
        agent=writer,
        context=[research_task]
    )

    return [research_task, writing_task]

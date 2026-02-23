from crewai import Task

def create_linkedin_tasks(researcher, writer, url):
    """Create tasks for LinkedIn content generation"""
    research_task = Task(
        description=f"Analyze content from {url} and extract insights suitable for LinkedIn audience.",
        expected_output="Research summary focused on professional insights and engagement opportunities",
        agent=researcher
    )

    writing_task = Task(
        description="Create an engaging LinkedIn post based on the research.",
        expected_output="A complete LinkedIn post with hashtags and engagement elements",
        agent=writer,
        context=[research_task]
    )

    return [research_task, writing_task]

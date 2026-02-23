from crewai import Task

def create_blog_tasks(researcher, writer, url):
    """Create tasks for blog content generation"""
    research_task = Task(
        description=f"Analyze content from {url} and extract key insights for a blog post.",
        expected_output="A detailed research summary with key insights, themes, and recommendations for blog content",
        agent=researcher 
    )

    writing_task = Task(
        description="Create an engaging blog post based on the research findings.",
        expected_output="A complete, well-structured blog post in markdown format",
        agent=writer,
        context=[research_task]
    )

    return [research_task, writing_task]

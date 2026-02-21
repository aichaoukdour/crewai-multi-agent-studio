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

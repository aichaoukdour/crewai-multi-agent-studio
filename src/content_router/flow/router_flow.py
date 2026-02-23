from crewai.flow.flow import Flow, listen, router, start
from crewai.flow.persistence import persist
from crewai import Crew

from content_router.flow.state import ContentState
from content_router.agents import create_blog_agents, create_newsletter_agents, create_linkedin_agents
from content_router.tasks import create_blog_tasks, create_newsletter_tasks, create_linkedin_tasks

@persist(verbose=True)
class ContentRouterFlow(Flow[ContentState]):
    """
    A dynamic workflow that routes content creation to specialized crews.
    """

    @start()
    def get_user_input(self):
        """Get URL and desired content type from user"""
        url = "https://blog.crewai.com/pwc-choses-crewai/"
        content_type = "newsletter"
        self.state.url = url
        self.state.content_type = content_type
        return "Input collected"

    @router(get_user_input)
    def route_to_crew(self, previous_result):
        """Route to appropriate crew based on content type"""
        return self.state.content_type

    @listen("blog")
    def process_blog_content(self):
        """Process content using blog crew"""
        try:
            researcher, writer = create_blog_agents()
            tasks = create_blog_tasks(researcher, writer, self.state.url)
            blog_crew = Crew(
                agents=[researcher, writer],
                tasks=tasks,
                verbose=False
            )
            result = blog_crew.kickoff()
            self.state.final_content = result.raw
            return "Blog content created"
        except Exception as e:
            self.state.error = f"Blog processing failed: {str(e)}"
            return f"Error: {str(e)}"

    @listen("newsletter")
    def process_newsletter_content(self):
        """Process content using newsletter crew"""
        try:
            researcher, writer = create_newsletter_agents()
            tasks = create_newsletter_tasks(researcher, writer, self.state.url)
            newsletter_crew = Crew(
                agents=[researcher, writer],
                tasks=tasks,
                verbose=False
            )
            result = newsletter_crew.kickoff()
            self.state.final_content = result.raw
            return "Newsletter content created"
        except Exception as e:
            self.state.error = f"Newsletter processing failed: {str(e)}"
            return f"Error: {str(e)}"

    @listen("linkedin")
    def process_linkedin_content(self):
        """Process content using LinkedIn crew"""
        try:
            researcher, writer = create_linkedin_agents()
            tasks = create_linkedin_tasks(researcher, writer, self.state.url)
            linkedin_crew = Crew(
                agents=[researcher, writer],
                tasks=tasks,
                verbose=False
            )
            result = linkedin_crew.kickoff()
            self.state.final_content = result.raw
            return "LinkedIn content created"
        except Exception as e:
            self.state.error = f"LinkedIn processing failed: {str(e)}"
            return f"Error: {str(e)}"

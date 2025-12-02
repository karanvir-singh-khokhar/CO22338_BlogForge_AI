from crewai import Crew, Process
from crew.agents import BlogAgents
from crew.tasks import BlogTasks

class BlogCrew:
    
    def __init__(self, topic, tone="professional"):
        self.topic = topic
        self.tone = tone
        
    def run(self):
        # Initialize agents
        researcher = BlogAgents.researcher()
        writer = BlogAgents.writer()
        editor = BlogAgents.editor()
        
        # Create tasks
        research_task = BlogTasks.research_task(researcher, self.topic)
        writing_task = BlogTasks.writing_task(writer, self.topic, self.tone, research_task)
        editing_task = BlogTasks.editing_task(editor, writing_task)
        
        # Create crew
        crew = Crew(
            agents=[researcher, writer, editor],
            tasks=[research_task, writing_task, editing_task],
            process=Process.sequential,
            verbose=True
        )
        
        # Execute
        result = crew.kickoff()
        
        # Return structured output
        return {
            'final_blog': str(result),
            'research': research_task.output.raw if hasattr(research_task, 'output') else '',
            'logs': [
                'Researcher: Completed information gathering',
                'Writer: Completed blog draft',
                'Editor: Completed final review'
            ]
        }
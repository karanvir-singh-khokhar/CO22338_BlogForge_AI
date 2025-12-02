from crewai import Task

class BlogTasks:
    
    @staticmethod
    def research_task(agent, topic):
        return Task(
            description=f"""Research the topic: {topic}
            
            Your tasks:
            1. Identify 5-7 key points about this topic
            2. Find relevant facts, statistics, or examples
            3. Note any important context or background information
            4. Identify the target audience and their interests
            5. Suggest angles or perspectives to explore
            
            Provide a structured research summary that will help 
            the writer create an informative blog post.""",
            agent=agent,
            expected_output="A comprehensive research summary with key points, facts, and insights"
        )
    
    @staticmethod
    def writing_task(agent, topic, tone, research_context):
        return Task(
            description=f"""Write a blog post about: {topic}
            Tone: {tone}
            
            Using the research provided, create a blog post that:
            1. Has an attention-grabbing title
            2. Includes an engaging introduction
            3. Covers 3-5 main points with supporting details
            4. Uses clear section headings
            5. Ends with a strong conclusion
            6. Is 500-800 words long
            7. Matches the {tone} tone throughout
            
            Research Context:
            {research_context}
            
            Make it informative, engaging, and valuable to readers.""",
            agent=agent,
            expected_output="A complete blog post with title, introduction, body sections, and conclusion",
            context=[research_context] if research_context else []
        )
    
    @staticmethod
    def editing_task(agent, draft_context):
        return Task(
            description=f"""Review and refine the blog post draft.
            
            Your tasks:
            1. Check grammar, spelling, and punctuation
            2. Ensure logical flow and coherence
            3. Verify facts and claims are reasonable
            4. Improve clarity and readability
            5. Enhance engagement where needed
            6. Ensure tone consistency
            7. Format properly with markdown
            
            Provide the final, polished version ready for publication.""",
            agent=agent,
            expected_output="A polished, publication-ready blog post",
            context=[draft_context] if draft_context else []
        )
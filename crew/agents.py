from crewai import Agent, LLM
import os

def get_llm():
    """Initialize Gemini LLM with API key"""
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not found in environment variables. "
            "Please create a .env file with your API key."
        )
    
    # Use stable Gemini 2.0 Flash with optimized settings
    return LLM(
        model="gemini/gemini-2.0-flash",
        api_key=api_key,
        temperature=0.5,  # Reduced from 0.7 for faster, more consistent responses
        timeout=60  # Add timeout to prevent hanging
    )

class BlogAgents:
    
    @staticmethod
    def researcher():
        return Agent(
            role='Research Specialist',
            goal='Gather comprehensive and accurate information about the given topic in a concise manner',
            backstory="""You are an expert researcher with years of experience in 
            information gathering and analysis. You excel at finding key facts, 
            statistics, and insights that make content valuable and credible. 
            Be concise and focus on the most relevant information.""",
            verbose=False,  # Disabled to reduce overhead
            allow_delegation=False,
            llm=get_llm(),
            max_iter=5,  # Limit iterations to prevent infinite loops
            memory=True
        )
    
    @staticmethod
    def writer():
        return Agent(
            role='Content Writer',
            goal='Create engaging and well-structured blog posts based on research, with clear organization',
            backstory="""You are a talented content writer who specializes in 
            creating compelling blog posts. You know how to structure content 
            effectively, use storytelling techniques, and adapt your writing 
            style to match different tones and audiences. Write concisely 
            and keep paragraphs focused.""",
            verbose=False,  # Disabled to reduce overhead
            allow_delegation=False,
            llm=get_llm(),
            max_iter=5,  # Limit iterations to prevent infinite loops
            memory=True
        )
    
    @staticmethod
    def editor():
        return Agent(
            role='Content Editor',
            goal='Review, refine, and perfect blog posts for publication with focus on clarity and quality',
            backstory="""You are a meticulous editor with a keen eye for detail. 
            You ensure content is clear, coherent, grammatically correct, and 
            engaging. You fact-check information and polish writing to 
            professional standards. Keep edits focused on quality improvements.""",
            verbose=False,  # Disabled to reduce overhead
            allow_delegation=False,
            llm=get_llm(),
            max_iter=3,  # Lower limit for editor to prevent excessive revisions
            memory=True
        )

from app.agents.agent_crewai import create_crew_agents, create_crew_tasks
from crewai import Crew

def agent_crewai_execute_analysis(output):
    agents = create_crew_agents()
    tasks = create_crew_tasks(output, agents)    
    crew = Crew(agents=agents, tasks=tasks, verbose=True)
    result = crew.kickoff()
    return result
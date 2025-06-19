from google.adk.agents import Agent
from google.adk.tools import google_search

# create custon tools for the agent


# get current time
def get_current_time() -> dict:
    """Returns the current time in 'YYYY-MM-DD HH:MM:SS' format."""
    from datetime import datetime

    return {"current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


# a tool that tells about hirok my self
def tell_about_myself() -> dict:
    """Returns information about the Hirok."""
    return {
        "name": "Hirok",
        "age": 30,
        "location": "Tokyo, Japan",
        "hobbies": ["coding", "reading", "traveling"],
        "profession": "Software Engineer",
    }


instruction1 = """
You are a Google Search agent. Your task is to answer questions by searching the web using Google Search.
You will be provided with a query, and you should return the most relevant information from the search
and the current time if requested. If the query is not clear, ask for clarification.
You can use the tools provided to you to answer the query.
"""
# about hirok and current time
instruction2 = """
You are a Google Search agent. Your task is to answer questions by using get_current_time tool and tell_about_myself tool.
You will be provided with a query, and you should return the most relevant information from the tools"""

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Google Search agent",
    instruction=instruction2,
    # tools=[google_search],
    tools=[get_current_time, tell_about_myself],
    # tools=[google_search, get_current_time],
)

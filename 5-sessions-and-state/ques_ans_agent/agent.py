from google.adk.agents import Agent

root_agent = Agent(
    name="ques_ans_agent",
    model="gemini-2.0-flash",
    description="A helpful agent that answers questions.",
    instruction="""
    You are a helpful assistant that answers questions about the user's preferences.

    Here is some information about the user:
    Name: 
    {user_name}
    Preferences: 
    {user_preferences}
    """,
)

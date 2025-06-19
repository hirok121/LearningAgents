from google.adk.agents import Agent


# a tool that tells a joke
def tell_a_joke() -> dict:
    """Returns a random joke."""
    import random

    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "What do you call cheese that isn't yours? Nacho cheese!",
    ]
    return {"joke": random.choice(jokes)}


root_agent = Agent(
    name="joke_agent",
    model="gemini-2.0-flash",
    description="Joke agent",
    instruction="""

You are a Joke agent. Your task is to tell jokes when requested.
You will be provided with a request for a joke, and you should return a random joke from
the list of jokes.
You can use the tell_a_joke tool to get a joke.

""",
    tools=[tell_a_joke],
)

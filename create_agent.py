import os
from pathlib import Path

# Default values
DEFAULTS = {
    "name": "greeting_agent",
    "model": "gemini-2.0-flash",
    "description": "Greeting agent",
    "instruction": """
You are a helpful assistant that greets the user.
Ask for the user's name and greet them by name.
""",
}


def prompt(field, default):
    value = input(f"Enter {field} (press Enter to use default: '{default}'): ")
    return value.strip() or default


def main():
    print("Agent Directory Structure Creator\n")
    name = prompt("agent name", DEFAULTS["name"])
    model = prompt("model", DEFAULTS["model"])
    description = prompt("description", DEFAULTS["description"])
    instruction = prompt("instruction", DEFAULTS["instruction"])

    # Directory structure: <name>/agent.py
    base_dir = Path(f"{name}")
    agent_dir = base_dir
    agent_dir.mkdir(parents=True, exist_ok=True)

    agent_py = agent_dir / "agent.py"
    agent_code = f'''from google.adk.agents import Agent\n\nroot_agent = Agent(\n    name="{name}",\n    model="{model}",\n    description="{description}",\n    instruction="""\n{instruction}\n""",\n)\n'''
    with open(agent_py, "w", encoding="utf-8") as f:
        f.write(agent_code)
    # Create __init__.py in agent_dir with import statement
    init_file = agent_dir / "__init__.py"
    with open(init_file, "w", encoding="utf-8") as f:
        f.write("from . import agent\n")
    # Create .env.example in base_dir with example content
    env_example = agent_dir / ".env.example"
    with open(env_example, "w", encoding="utf-8") as f:
        f.write("Gemini_API_KEY=\nDefault_Model=gemini-2.0-flash\n")
    print(f"Created agent at: {agent_py}")
    # Readme file
    readme_file = agent_dir / "README.md"
    readme_content = f"""# {name}
This agent is designed to greet the user.
## Model
{model}
## Description
{description}
## Instruction
{instruction.strip()}
"""
    with open(readme_file, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"Created README at: {readme_file}")


if __name__ == "__main__":
    main()

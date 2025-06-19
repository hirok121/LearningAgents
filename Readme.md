# My Learning Agents Practice

This repository is my personal playground for practicing and experimenting with agent development using Google's Agent Development Kit (ADK).

## What I'll Do Here

- Try out different types of agents (basic, tool-using, multi-agent, etc.)
- Practice setting up environments and API keys
- Experiment with state, memory, and persistent storage
- Build, break, and fix agents to learn by doing

## Getting Started (for myself)

1. Create a virtual environment (only once):
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
2. For each example, copy `.env.example` to `.env` and add my API key.

## Example Folders

- **1-basic-agent**: My first simple agent
- **2-tool-agent**: Agents with tools
- **3-litellm-agent**: Switching LLM providers
- **4-structured-outputs**: Using Pydantic for structured responses
- **5-sessions-and-state**: Keeping state and memory
- **6-persistent-storage**: Saving agent data
- **7-multi-agent**: Multiple agents working together
- **8-stateful-multi-agent**: Multi-agent with state
- **9-callbacks**: Using callbacks
- **10-sequential-agent**: Pipeline workflows
- **11-parallel-agent**: Parallel/concurrent agents
- **12-loop-agent**: Agents with feedback loops

## Docs & Help

- [Official ADK Docs](https://google.github.io/adk-docs/get-started/quickstart)
- [AI Developer Accelerator Community](https://www.skool.com/ai-developer-accelerator/about)

I'll update this as I learn more!

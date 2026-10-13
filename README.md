# AgenticAI

## Deep Agents research agent

Create a virtual environment and install the dependencies:

```bash
python3.14 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Set `GOOGLE_API_KEY` in your shell or in a local `.env` file. The `.env` file is
ignored by Git. Then run the quickstart research query:

```bash
.venv/bin/python research_agent.py
```

The agent uses Google's built-in web search, so Tavily configuration is not
required.
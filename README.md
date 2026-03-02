# Functional Expert MCP (LangGraph Version)

## Installation

1. Unzip the project
2. Edit config.json with absolute paths and OpenAI key
3. Install dependencies:

   pip install -r requirements.txt

4. Run server:

   python server.py

## VS Code settings.json

Add:

{
  "github.copilot.chat.mcpServers": [
    {
      "name": "functional-expert-langgraph",
      "command": "python",
      "args": ["C:/absolute/path/to/server.py"]
    }
  ]
}

Restart VS Code.

## Running Unit Tests

To validate the core services you can run the automated tests using `pytest`. If you don’t have `pytest` installed already, run:

```powershell
pip install pytest
```

Then from the project root directory execute:

```powershell
cd c:\Users\T0043336\project\functional-mcp-langgraph-ready\functional-mcp-langgraph
pytest -q
```

This will discover and run tests located in the `tests/` folder.

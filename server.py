import json
from modelcontextprotocol.server import Server
from services.vector_store import build_vector_store
from graph import build_graph

with open("config.json") as f:
    config = json.load(f)

vector_store = build_vector_store(
    config["spec_repo_path"],
    config["openai_api_key"]
)

app = build_graph(vector_store, config["code_repo_path"])

server = Server(
    name="functional-expert-mcp-langgraph",
    version="1.0.0"
)

@server.tool()
async def functionalExpert(question: str):
    result = app.invoke({
        "question": question
    })
    return result["answer"]

server.start()

from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from services.git_service import get_current_version

class AgentState(TypedDict):
    question: str
    domains: List[str]
    version: str
    documents: List[dict]
    answer: str

def build_graph(vector_store, code_repo_path):

    llm = ChatOpenAI(model="gpt-4o-mini")

    def detect_domain(state: AgentState):
        prompt = f"""
Identify functional domains (IHM, GUI, backend, data, loads, database, query)
from this question:
{state['question']}
Return comma separated list.
"""
        result = llm.invoke(prompt)
        domains = [d.strip() for d in result.content.split(",")]
        return {"domains": domains}

    def get_version(state: AgentState):
        version = get_current_version(code_repo_path)
        return {"version": version}

    def semantic_search(state: AgentState):
        results = vector_store.similarity_search(state["question"], k=4)
        formatted = [
            {
                "source": r.metadata["source"],
                "content": r.page_content[:1000]
            }
            for r in results
        ]
        return {"documents": formatted}

    def format_answer(state: AgentState):
        context = "\n\n".join([d["content"] for d in state["documents"]])

        prompt = f"""
You are a functional expert.

Domains: {state['domains']}
Version: {state['version']}

Documentation excerpts:
{context}

Question:
{state['question']}

Provide structured answer with:
- Domains
- Version
- Functional Answer
- Sources
"""

        result = llm.invoke(prompt)
        return {"answer": result.content}

    graph = StateGraph(AgentState)

    graph.add_node("detect_domain", detect_domain)
    graph.add_node("get_version", get_version)
    graph.add_node("semantic_search", semantic_search)
    graph.add_node("format_answer", format_answer)

    graph.set_entry_point("detect_domain")

    graph.add_edge("detect_domain", "get_version")
    graph.add_edge("get_version", "semantic_search")
    graph.add_edge("semantic_search", "format_answer")
    graph.add_edge("format_answer", END)

    return graph.compile()

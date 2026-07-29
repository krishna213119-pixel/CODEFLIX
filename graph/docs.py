from nodes.chunks import Chunk_load
from nodes.embedd import embed_node
from nodes.load_repo import Load_Repo_Node
from state.docs_state import docs_state
from langgraph.graph import StateGraph,START,END
from nodes.git_node import GitHub_Node,route_repository

graph = StateGraph(docs_state)
graph.add_node("github",GitHub_Node)
graph.add_node("load_repo", Load_Repo_Node)
graph.add_node("chunk", Chunk_load)
graph.add_node("embedding", embed_node)

graph.add_conditional_edges(START, route_repository,{
    "github": "github",
        "local": "load_repo",
},)
graph.add_edge("github","load_repo")
graph.add_edge("load_repo", "chunk")
graph.add_edge("chunk", "embedding")
graph.add_edge("embedding", END)
workflow = graph.compile()

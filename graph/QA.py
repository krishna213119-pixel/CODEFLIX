from langgraph.graph import StateGraph, START, END

from state.q_state import QA_State

from nodes.related_node import R_Node
from nodes.ans_node import Generate_Node


graph = StateGraph(QA_State)

graph.add_node("retrieve", R_Node)
graph.add_node("generate", Generate_Node)

graph.add_edge(START, "retrieve")
graph.add_edge("retrieve", "generate")
graph.add_edge("generate", END)

workflow = graph.compile()
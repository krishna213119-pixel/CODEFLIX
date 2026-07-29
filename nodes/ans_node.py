from state.q_state import QA_State

from services.ans import LLMService
from services.history import MemoryService
from services.source import SourceService


def Generate_Node(state: QA_State):

    history = state["history"]

    MemoryService.add_user_message(
        history,
        state["ques"]
    )

    answer = LLMService.generate(
        question=state["ques"],
        documents=state["retrive_docs"],
        history=history
    )

    MemoryService.add_ai_message(
        history,
        answer
    )

    sources = SourceService.get_sources(
        state["retrive_docs"]
    )

    state["ans"] = answer
    state["sources"] = sources
    state["history"] = history

    return state
from services.chunks_logic import CHUNKS_SERVICE
from state.docs_state import docs_state
from services.embedd_logic import EmbeddingService

def embed_node(state : docs_state):
    state["vectorstore"] = EmbeddingService.create_vectorstore(
        state["chunks"]
    )

    state["status"] = "Embedding Completed!!"

    return state
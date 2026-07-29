from services.chunks_logic import CHUNKS_SERVICE
from state.docs_state import docs_state

def Chunk_load(state: docs_state):
    state['chunks'] = CHUNKS_SERVICE.create_chunks(state['docs'])
    state['status'] = 'chunking completed!!'
    return state
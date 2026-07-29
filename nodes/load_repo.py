from services.load_Logic import Repo_Load
from state.docs_state import docs_state

def Load_Repo_Node(state : docs_state):
    doccuments = Repo_Load.Load(state['repo_path'])
    state['docs']= doccuments
    state['status'] = 'repo Loaded!!'
    return state


from state.q_state import QA_State
from langchain_core.documents import Document
from langchain_chroma import Chroma
from services.Related_docs import Ques_docs

def R_Node(state : QA_State):
     state['retrive_docs']= Ques_docs.fun_ques_docs(
    state['vectorstore'],state['ques'] 
    )
     return state

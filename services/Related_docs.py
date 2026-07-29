from state.q_state import QA_State
from langchain_core.documents import Document
from langchain_chroma import Chroma


class Ques_docs:

    @classmethod
    def fun_ques_docs(cls,vectorstore: Chroma,ques : str,k : int = 3):
        print(type(vectorstore))
        print(vectorstore)
        retriver = vectorstore.as_retriever(search_kwargs={"k":k})
        return retriver.invoke(ques)
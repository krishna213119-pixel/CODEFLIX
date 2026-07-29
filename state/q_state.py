from typing import TypedDict
from langchain_core.documents import Document
from langchain_core.messages import BaseMessage

class QA_State(TypedDict):
    ques : str
    ans : str
    retrive_docs : list[Document]
    vectorstore : object
    sources : list[str]
    history : list[BaseMessage]

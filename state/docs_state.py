from typing import TypedDict,Any
from langchain_core.documents import Document





class docs_state(TypedDict):
    repo_path : str
    chunks: list[Document]
    docs : list[Document]
    vectorstore : Any
    status : str
    error : str
    
    


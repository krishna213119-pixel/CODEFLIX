from fastapi import APIRouter, HTTPException

from api.schemas.chat_schema import ChatRequest
import api.store.repository_store as repository_store

from graph.QA import workflow as qa_workflow


router = APIRouter(
    prefix="/chat",
    tags=["Repository Chat"]
)


@router.post("/")
def chat_with_repository(
    request: ChatRequest
):

    print(
        "Current vectorstore:",
        repository_store.vectorstore
    )

    if repository_store.vectorstore is None:

        raise HTTPException(
            status_code=400,
            detail=(
                "No repository is indexed. "
                "Index a GitHub repository first."
            )
        )

    qa_state = {
        "ques": request.question,
        "retrive_docs": [],
        "ans": "",
        "vectorstore": repository_store.vectorstore,
        "sources": [],
        "history": repository_store.history,
    }

    try:

        result = qa_workflow.invoke(
            qa_state
        )

        repository_store.history = (
            result["history"]
        )

        return {
            "answer": result["ans"],
            "sources": result["sources"]
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )
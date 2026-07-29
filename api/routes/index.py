from fastapi import APIRouter, HTTPException

from api.schemas.index_schema import IndexRequest
import api.store.repository_store as repository_store

from graph.docs import workflow as indexing_workflow


router = APIRouter(
    prefix="/index",
    tags=["Repository Indexing"]
)


@router.post("/")
def index_repository(
    request: IndexRequest
):

    index_state = {
        "repo_path": request.repo_url,
        "docs": [],
        "chunks": [],
        "vectorstore": None,
        "status": "",
        "error": "",
    }

    try:

        result = indexing_workflow.invoke(
            index_state
        )

        if result.get("error"):

            raise HTTPException(
                status_code=400,
                detail=result["error"]
            )

        repository_store.vectorstore = (
            result["vectorstore"]
        )

        repository_store.history = []

        print(
            "Vectorstore saved:",
            repository_store.vectorstore
        )

        return {
            "status": result["status"],
            "documents": len(
                result["docs"]
            ),
            "chunks": len(
                result["chunks"]
            )
        }

    except HTTPException:

        raise

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )
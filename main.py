# from fastapi import FastAPI

# from api.routes.index import (
#     router as index_router
# )

# from api.routes.chat import (
#     router as chat_router
# )


# app = FastAPI(
#     title="AI Software Engineer",
#     description="GitHub Repository AI Assistant",
#     version="1.0.0"
# )


# app.include_router(
#     index_router
# )

# app.include_router(
#     chat_router
# )


# @app.get("/")
# def home():

#     return {
#         "message": (
#             "AI Software Engineer API "
#             "is running"
#         )
#     }


# @app.get("/health")
# def health():

#     return {
#         "status": "healthy"
#     }
from fastapi import FastAPI

from api.routes.index import router as index_router
from api.routes.chat import router as chat_router


app = FastAPI(
    title="CODEFLIX AI Backend"
)


@app.get("/")
def home():
    return {
        "message": "CODEFLIX AI Backend is running"
    }


app.include_router(index_router)
app.include_router(chat_router)
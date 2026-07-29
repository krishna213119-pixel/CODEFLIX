from pydantic import BaseModel


class IndexRequest(BaseModel):

    repo_url: str
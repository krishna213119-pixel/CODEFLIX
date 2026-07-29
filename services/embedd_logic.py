import os

from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEndpointEmbeddings


class EmbeddingService:

    @classmethod
    def get_embedding_model(cls):

        return HuggingFaceEndpointEmbeddings(
            model="sentence-transformers/all-MiniLM-L6-v2",
            huggingfacehub_api_token=os.getenv(
                "HUGGINGFACEHUB_API_TOKEN"
            )
        )

    @classmethod
    def create_vectorstore(
        cls,
        chunks: list[Document]
    ):

        embedding_model = cls.get_embedding_model()

        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model,
            persist_directory="./vectorstore"
        )

        return vectorstore
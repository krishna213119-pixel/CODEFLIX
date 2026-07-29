from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings




class EmbeddingService:

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    @classmethod
    def create_vectorstore(
        cls,
        chunks: list[Document]
    ) :

        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=cls.embedding_model,
            persist_directory="./vectorstore"
        )

        return vectorstore

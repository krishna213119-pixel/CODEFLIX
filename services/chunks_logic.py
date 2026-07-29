from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

class CHUNKS_SERVICE:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=[
            "\n\n",
            "\n",
            " ",
            ""
        ]
    )

    @classmethod
    def create_chunks(cls,docs: list[Document]):
        chunk = cls.text_splitter.split_documents(docs)
        return chunk

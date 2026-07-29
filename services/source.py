from langchain_core.documents import Document


class SourceService:

    @classmethod
    def get_sources(
        cls,
        documents: list[Document]
    ) -> list[str]:

        sources = []

        for document in documents:

            source = document.metadata.get(
                "source",
                "Unknown"
            )

            if source not in sources:
                sources.append(source)

        return sources
from langchain_core.documents import Document
from langchain_core.messages import BaseMessage


class PromptService:

    @classmethod
    def build_prompt(
        cls,
        question: str,
        documents: list[Document],
        history: list[BaseMessage]
    ) -> str:

        context = "\n\n".join(
            f"""
File: {doc.metadata.get("source", "Unknown")}

Code:
{doc.page_content}
"""
            for doc in documents
        )

        history = "\n".join(
            f"{message.type}: {message.content}"
            for message in history
        )

        prompt = f"""
You are an expert AI Software Engineer.

Use the repository context and conversation history
to answer the user's question.

Rules:
1. Use repository context as the main source.
2. Use conversation history to understand follow-up questions.
3. Do not invent files or functions.
4. If information is missing, say that you could not find it.

Conversation History:
{history}

Repository Context:
{context}

Current Question:
{question}

Answer:
"""

        return prompt
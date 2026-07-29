from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    BaseMessage
)


class MemoryService:

    @classmethod
    def add_user_message(
        cls,
        history: list[BaseMessage],
        question: str
    ) -> list[BaseMessage]:

        history.append(
            HumanMessage(content=question)
        )

        return history

    @classmethod
    def add_ai_message(
        cls,
        history: list[BaseMessage],
        answer: str
    ) -> list[BaseMessage]:

        history.append(
            AIMessage(content=answer)
        )

        return history
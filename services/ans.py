from dotenv import load_dotenv
from services.prompt import PromptService
from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface import ChatHuggingFace

load_dotenv()


class LLMService:

    chat = HuggingFaceEndpoint(
        repo_id="Qwen/Qwen2.5-7B-Instruct",
         task="conversational",
        max_new_tokens=512,
        
    )
    llm = ChatHuggingFace(llm = chat)

    @classmethod
    def generate(cls, question: str, documents,history):

        

         prompt = PromptService.build_prompt(
            question=question,
            documents=documents,
            history= history
        )


         response = cls.llm.invoke(prompt)

         return response.content
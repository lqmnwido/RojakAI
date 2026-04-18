from app.core.context_builder import ContextBuilder
from app.core.memory_manager import MemoryManager
from app.core.reflector import Reflector
from app.llm.ollama_client import OllamaClient
from app.llm.prompt_builder import PromptBuilder
from app.rag.retriever import Retriever
from app.storage.postgres_repository import PostgresRepository

class CodingAgent:
    def __init__(self) -> None:
        self.ollama = OllamaClient()
        self.retriever = Retriever()
        self.reflector = Reflector()
        self.context_builder = ContextBuilder()
        self.prompt_builder = PromptBuilder()
        self.memory = MemoryManager()
        self.postgres = PostgresRepository()

        self.postgres.create_tables()

    def ask(self, question: str) -> str:
        self.memory.save_last_question(question)

        rag_context = self.retriever.retrieve(question)
        tool_context = self.context_builder.build(question)

        full_context = f"""
RAG CONTEXT:
{rag_context}

TOOL CONTEXT:
{tool_context}
"""

        prompt = self.prompt_builder.build(question, full_context)

        first_answer = self.ollama.generate(prompt)
        final_answer = self.reflector.improve(question, first_answer)

        self.postgres.save_message(question, final_answer)

        return final_answer
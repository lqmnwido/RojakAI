from app.llm.ollama_client import OllamaClient
from app.rag.vector_store import VectorStore

class Retriever:
    def __init__(self) -> None:
        self.ollama = OllamaClient()
        self.vector_store = VectorStore()

    def retrieve(self, query: str) -> str:
        embedding = self.ollama.embed(query)
        results = self.vector_store.search(embedding)

        context_parts: list[str] = []

        for result in results:
            payload = result.payload
            context_parts.append(
                f"FILE: {payload['file']}\n\n{payload['content']}"
            )

        return "\n\n---\n\n".join(context_parts)
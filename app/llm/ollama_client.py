import ollama

from app.config.settings import settings

class OllamaClient:
    def __init__(self) -> None:
        self.model = settings.OLLAMA_MODEL
        self.embed_model = settings.OLLAMA_EMBED_MODEL

    def generate(self, prompt: str) -> str:
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a senior software engineer and coding assistant.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return response["message"]["content"]

    def embed(self, text: str) -> list[float]:
        response = ollama.embeddings(
            model=self.embed_model,
            prompt=text,
        )

        return response["embedding"]
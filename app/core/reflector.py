from app.llm.ollama_client import OllamaClient

class Reflector:
    def __init__(self) -> None:
        self.ollama = OllamaClient()

    def improve(self, question: str, answer: str) -> str:
        critique = self.ollama.generate(
            f"""
Critique this answer.

QUESTION:
{question}

ANSWER:
{answer}

Find mistakes, missing details, assumptions, and better reasoning.
"""
        )

        improved = self.ollama.generate(
            f"""
Improve the original answer using the critique.

QUESTION:
{question}

ORIGINAL ANSWER:
{answer}

CRITIQUE:
{critique}
"""
        )

        return improved
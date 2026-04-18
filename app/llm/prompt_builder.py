class PromptBuilder:
    def build(self, question: str, context: str) -> str:
        return f"""
You are a senior software engineer.

Use the supplied project context to answer accurately.

If there is not enough information, say what additional file or command is needed.

PROJECT CONTEXT:

{context}

QUESTION:

{question}
"""